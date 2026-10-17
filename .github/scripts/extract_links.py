"""Write each LOOBin's detection and resource URLs to <out_dir>/<entry>.md for lychee.

Only these fields are link-checked. URLs inside example `code` blocks are
illustrative (and can point at attacker infrastructure), so they are skipped.
One file per entry makes lychee group its report by LOOBin.

Usage: python .github/scripts/extract_links.py LOOBins links
"""

import pathlib
import sys

import yaml

src, out = (pathlib.Path(arg) for arg in sys.argv[1:3])
out.mkdir(parents=True, exist_ok=True)
for path in sorted(src.glob("*.yml")):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    links = [
        f"- {field}: <{url}>"
        for field in ("detections", "resources")
        for item in data.get(field) or []
        if (url := str(item.get("url", "")).strip())
        .lower()
        .startswith(("http://", "https://"))
    ]
    if links:
        (out / f"{path.stem}.md").write_text("\n".join(links) + "\n", encoding="utf-8")
