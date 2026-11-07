"""Gather inputs for the coverage scan without an LLM.

Writes two files for Claude to read:

- research.json: recent macOS-related posts from the feeds in
  .github/coverage-feeds.txt, newest first, plus each feed's status.
- coverage-index.md: every LOOBin and the names of its use cases, so the scan
  doesn't spend turns reading LOOBins/ file by file.

Feed content is untrusted. Only titles, https links and dates are kept, and
they are written as data for Claude to fetch and judge, never acted on here.

Usage: python .github/scripts/collect_research.py FEEDS LOOBINS_DIR LOOKBACK_DAYS OUT_DIR
"""

import datetime as dt
import email.utils
import json
import os
import pathlib
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

MAX_ARTICLES = 40
MAX_BYTES = 5_000_000
USER_AGENT = "LOOBins-coverage-scan/1.0 (+https://github.com/infosecB/LOOBins)"
ATOM = "{http://www.w3.org/2005/Atom}"
DC_DATE = "{http://purl.org/dc/elements/1.1/}date"
MACOS_RE = re.compile(
    r"\b(mac ?os|os ?x|mac|apple|darwin|xprotect|gatekeeper|notari[sz]|tcc|"
    r"launch ?(agent|daemon)s?|applescript|osascript|mach-o|keychain|"
    r"atomic stealer|amos|poseidon|banshee|cuckoo)\b",
    re.I,
)


def parse_date(text):
    text = (text or "").strip()
    if not text:
        return None
    try:
        parsed = email.utils.parsedate_to_datetime(text)
    except (TypeError, ValueError):
        try:
            parsed = dt.datetime.fromisoformat(text.replace("Z", "+00:00"))
        except ValueError:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=dt.timezone.utc)
    return parsed


def text_of(node, tag):
    child = node.find(tag)
    return "".join(child.itertext()).strip() if child is not None else ""


def entries(root):
    """Yield (title, link, published, blob) for RSS 2.0 and Atom feeds."""
    for item in root.iter("item"):
        published = parse_date(text_of(item, "pubDate") or text_of(item, DC_DATE))
        cats = " ".join(c.text or "" for c in item.findall("category"))
        title = text_of(item, "title")
        yield title, text_of(item, "link"), published, (
            f"{title} {text_of(item, 'description')[:2000]} {cats}"
        )
    for entry in root.iter(f"{ATOM}entry"):
        link = ""
        for candidate in entry.findall(f"{ATOM}link"):
            if candidate.get("rel", "alternate") == "alternate":
                link = candidate.get("href", "")
                break
        published = parse_date(
            text_of(entry, f"{ATOM}published") or text_of(entry, f"{ATOM}updated")
        )
        cats = " ".join(c.get("term", "") for c in entry.findall(f"{ATOM}category"))
        title = text_of(entry, f"{ATOM}title")
        yield title, link, published, (
            f"{title} {text_of(entry, f'{ATOM}summary')[:2000]} {cats}"
        )


def fetch(url):
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read(MAX_BYTES)


def read_feeds(feeds_file):
    feeds = []
    for line in pathlib.Path(feeds_file).read_text(encoding="utf-8").splitlines():
        parts = line.split("#", 1)[0].split()
        if parts and parts[0].startswith("https://"):
            feeds.append((parts[0], "mac" in parts[1:]))
    return feeds


def collect(feeds, since):
    articles, status = {}, []
    for url, mac_only in feeds:
        try:
            root = ET.fromstring(fetch(url))
        except Exception as err:  # pylint: disable=broad-except
            status.append({"feed": url, "ok": False, "error": str(err)[:200]})
            continue
        total = kept = 0
        for title, link, published, blob in entries(root):
            total += 1
            link = link.strip()
            if not re.match(r"^https://[^\s<>\"']+$", link):
                continue
            if published is None or published < since:
                continue
            if not mac_only and not MACOS_RE.search(blob):
                continue
            kept += 1
            articles.setdefault(
                link,
                {
                    "title": " ".join(title.split())[:200],
                    "url": link,
                    "published": published.date().isoformat(),
                    "feed": url,
                },
            )
        status.append({"feed": url, "ok": True, "entries": total, "kept": kept})
    ordered = sorted(articles.values(), key=lambda a: a["published"], reverse=True)
    return ordered[:MAX_ARTICLES], status


def coverage_index(loobins_dir):
    lines = [
        "# LOOBins coverage index",
        "",
        "Each LOOBin and the names of its existing use cases.",
        "",
    ]
    for path in sorted(
        pathlib.Path(loobins_dir).glob("*.yml"), key=lambda p: p.name.lower()
    ):
        text = path.read_text(encoding="utf-8")
        name = re.search(r"^name:\s*['\"]?(.+?)['\"]?\s*$", text, re.M)
        block = re.search(
            r"^example_use_cases:\s*$(.*?)(?=^[A-Za-z_]+:|\Z)", text, re.M | re.S
        )
        uses = re.findall(
            r"^\s*-\s+name:\s*['\"]?(.+?)['\"]?\s*$",
            block.group(1) if block else "",
            re.M,
        )
        lines.append(
            f"## {name.group(1) if name else path.stem} (`LOOBins/{path.name}`)"
        )
        lines += [f"- {use}" for use in uses] + [""]
    return "\n".join(lines)


def main():
    feeds_file, loobins_dir, lookback, out_dir = sys.argv[1:5]
    out = pathlib.Path(out_dir)
    since = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=int(lookback))
    articles, status = collect(read_feeds(feeds_file), since)

    (out / "research.json").write_text(
        json.dumps(
            {"since": since.date().isoformat(), "articles": articles, "feeds": status},
            indent=2,
        ),
        encoding="utf-8",
    )
    (out / "coverage-index.md").write_text(
        coverage_index(loobins_dir), encoding="utf-8"
    )

    ok = sum(1 for s in status if s["ok"])
    summary = [
        "## Coverage scan inputs",
        "",
        f"{ok}/{len(status)} feeds read, {len(articles)} macOS posts since {since.date()}.",
        "",
        "| Feed | Result |",
        "| --- | --- |",
    ]
    for s in status:
        result = (
            f"{s['kept']} kept of {s['entries']}"
            if s["ok"]
            else f"failed: {s['error']}"
        )
        summary.append(f"| {s['feed']} | {result.replace('|', '/')} |")
    text = "\n".join(summary) + "\n"
    if os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fh:
            fh.write(text)
    print(text)
    if ok == 0:
        print(
            "::warning::No feeds could be read; the scan will rely on web search only."
        )


if __name__ == "__main__":
    main()
