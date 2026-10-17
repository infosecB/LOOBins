"""Validate the coverage scan's findings.json and open one triage issue per candidate.

The findings are produced by an LLM that read untrusted web pages, so every
field is checked and re-rendered here rather than passed through. Mentions are
neutralized so a crafted page can't ping people, and anything malformed or
already tracked is dropped with a note in the job summary.

Usage: python .github/scripts/file_coverage_issues.py findings.json existing-issues.json LOOBins [--dry-run]
"""

import json
import os
import pathlib
import re
import subprocess
import sys

MAX_ISSUES = 5
REPO_URL = (
    f"https://github.com/{os.environ.get('GITHUB_REPOSITORY', 'infosecB/LOOBins')}"
)
LABELS = ["coverage-scan", "needs-triage"]
TACTICS = {
    "Reconnaissance",
    "Resource Development",
    "Initial Access",
    "Execution",
    "Persistence",
    "Privilege Escalation",
    "Defense Evasion",
    "Credential Access",
    "Discovery",
    "Lateral Movement",
    "Collection",
    "Exfiltration",
    "Command and Control",
    "Impact",
}
BINARY_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._+-]{0,63}$")
PATH_RE = re.compile(r"^/[A-Za-z0-9 ._+/-]{1,255}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def clean(text, limit):
    """Plain single-paragraph text: no mentions, no HTML, bounded length."""
    text = " ".join(str(text or "").split())[:limit]
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    return re.sub(r"@(?=\w)", "@​", text)


def fenced(code):
    code = str(code).strip()[:1000]
    longest = max([len(run) for run in re.findall(r"`+", code)] + [0])
    ticks = "`" * max(3, longest + 1)
    return f"{ticks}bash\n{code}\n{ticks}"


def valid_url(url):
    return (
        isinstance(url, str) and re.match(r"^https://[^\s<>()\[\]]+$", url) is not None
    )


def existing_names(loobins_dir):
    names = {}
    for path in pathlib.Path(loobins_dir).glob("*.yml"):
        match = re.search(
            r"^name:\s*['\"]?(.+?)['\"]?\s*$", path.read_text(encoding="utf-8"), re.M
        )
        if match:
            names[match.group(1).strip().lower()] = path.name
    return names


def tracked_binaries(issues):
    """Binary names already mentioned in an issue title (open or closed)."""
    return [issue["title"].lower() for issue in issues]


def validate(candidate, names, titles):
    """Return (issue_title, issue_body) or raise ValueError with the reason."""
    kind = candidate.get("kind")
    binary = str(candidate.get("binary", "")).strip()
    if kind not in ("new_binary", "new_use_case"):
        raise ValueError(f"unknown kind {kind!r}")
    if not BINARY_RE.match(binary):
        raise ValueError(f"invalid binary name {binary!r}")
    known = binary.lower() in names
    if kind == "new_binary" and known:
        raise ValueError(f"{binary} already has a LOOBin ({names[binary.lower()]})")
    if kind == "new_use_case" and not known:
        raise ValueError(f"{binary} has no LOOBin to add a use case to")
    if kind == "new_binary" and any(
        re.search(rf"\b{re.escape(binary.lower())}\b", t) for t in titles
    ):
        raise ValueError(f"{binary} is already mentioned in an existing issue")
    if candidate.get("confidence") not in ("high", "medium"):
        raise ValueError("confidence must be high or medium")

    tactics = [t for t in candidate.get("tactics") or [] if t in TACTICS]
    sources = [
        s
        for s in candidate.get("sources") or []
        if isinstance(s, dict) and valid_url(s.get("url"))
    ][:5]
    if not sources:
        raise ValueError("no valid https source")
    path = str(candidate.get("path", "")).strip()

    if kind == "new_binary":
        title = f"New LOOBin candidate: {binary}"
    else:
        title = f"New use case candidate: {binary}"
    if title.lower() in titles:
        raise ValueError("an issue with this title already exists")

    body = [
        "_Opened automatically by the weekly coverage scan. An LLM summarized public research, "
        "so verify the sources before acting on this._",
        "",
        f"**Binary:** `{binary}`",
    ]
    if kind == "new_binary" and PATH_RE.match(path):
        body.append(f"**Path:** `{path}`")
    if kind == "new_use_case":
        body.append(f"**Existing entry:** `LOOBins/{names[binary.lower()]}`")
    body += [
        f"**Confidence:** {candidate['confidence']}",
        f"**Suggested tactics:** {', '.join(tactics) or 'none given'}",
        "",
        "### Summary",
        "",
        clean(candidate.get("summary"), 800),
        "",
        "### Why it belongs in LOOBins",
        "",
        clean(candidate.get("macos_specific"), 800),
    ]
    if candidate.get("example"):
        body += ["", "### Example (unverified)", "", fenced(candidate["example"])]
    body += ["", "### Sources", ""]
    for source in sources:
        published = source.get("published", "")
        date = f" ({published})" if DATE_RE.match(str(published)) else ""
        name = re.sub(r"[\[\]]", "", clean(source.get("title") or source["url"], 200))
        body.append(f"- [{name}]({source['url']}){date}")
    body += [
        "",
        f"If this checks out, follow [CONTRIBUTING.md]({REPO_URL}/blob/main/CONTRIBUTING.md) to add it. "
        "Otherwise close this issue so future scans skip it.",
    ]
    return title, "\n".join(body) + "\n"


def main():
    findings_path, issues_path, loobins_dir = sys.argv[1:4]
    dry_run = "--dry-run" in sys.argv
    findings = json.loads(pathlib.Path(findings_path).read_text(encoding="utf-8"))
    issues = json.loads(pathlib.Path(issues_path).read_text(encoding="utf-8"))
    names = existing_names(loobins_dir)
    titles = tracked_binaries(issues)

    summary = ["## Coverage scan", ""]
    sources = [s for s in findings.get("sources_reviewed") or [] if valid_url(s)]
    summary.append(f"Reviewed {len(sources)} sources.")
    summary.append("")

    filed = 0
    for candidate in (findings.get("candidates") or [])[: MAX_ISSUES * 2]:
        if not isinstance(candidate, dict):
            continue
        label = clean(candidate.get("binary"), 64) or "(unnamed)"
        try:
            if filed >= MAX_ISSUES:
                raise ValueError(f"over the {MAX_ISSUES}-issue cap")
            title, body = validate(candidate, names, titles)
        except ValueError as err:
            summary.append(f"- Skipped `{label}`: {clean(err, 200)}")
            continue
        if dry_run:
            print(f"=== {title}\n{body}")
            url = "(dry run)"
        else:
            cmd = ["gh", "issue", "create", "--title", title, "--body-file", "-"]
            for name in LABELS:
                cmd += ["--label", name]
            url = subprocess.run(
                cmd, input=body, text=True, capture_output=True, check=True
            ).stdout.strip()
        titles.append(title.lower())
        filed += 1
        summary.append(f"- Opened {url}: {title}")

    if filed == 0:
        summary.append("- No new candidates.")
    summary += ["", "<details><summary>Sources reviewed</summary>", ""]
    summary += [f"- {s}" for s in sources] + ["", "</details>"]

    out = os.environ.get("GITHUB_STEP_SUMMARY")
    text = "\n".join(summary) + "\n"
    if out:
        with open(out, "a", encoding="utf-8") as fh:
            fh.write(text)
    print(text)


if __name__ == "__main__":
    main()
