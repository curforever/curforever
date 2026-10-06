"""Generate profile badges from public GitHub repository counters."""

import json
import os
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REPOS = ("curforever-skills", "CangQiongWaiMai-Java", "Keyboard", "CSSLearning")


def github_repo(name):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "curforever-profile"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"https://api.github.com/repos/curforever/{name}", headers=headers)
    with urlopen(request, timeout=30) as response:
        data = json.load(response)
    if data["full_name"].lower() != f"curforever/{name}".lower():
        raise ValueError(f"Unexpected repository for {name}")
    return {"stars": data["stargazers_count"], "forks": data["forks_count"]}


def badge(label, value, color):
    label_width = 16 + sum(12 if ord(char) > 127 else 7 for char in label)
    value_width = 18 + sum(12 if ord(char) > 127 else 7 for char in str(value))
    width = label_width + value_width
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="22" '
        f'viewBox="0 0 {width} 22" role="img" aria-label="{escape(label)}: {escape(str(value))}">'
        f'<clipPath id="r"><rect width="{width}" height="22" rx="4"/></clipPath>'
        f'<g clip-path="url(#r)"><rect width="{label_width}" height="22" fill="#334155"/>'
        f'<rect x="{label_width}" width="{value_width}" height="22" fill="{color}"/></g>'
        '<g fill="white" font-family="Segoe UI,Microsoft YaHei,Arial,sans-serif" '
        'font-size="11" text-anchor="middle">'
        f'<text x="{label_width / 2}" y="15">{escape(label)}</text>'
        f'<text x="{label_width + value_width / 2}" y="15">{escape(str(value))}</text></g></svg>\n'
    )


def counter_badge(kind, value, color):
    width = 38 + 7 * len(str(value))
    icon = (
        '<path d="m12 4 2.2 4.5 4.8.7-3.5 3.4.8 4.8-4.3-2.3-4.3 2.3.8-4.8L5 9.2l4.8-.7Z" fill="#c4b5fd"/>'
        if kind == "stars" else
        '<g fill="none" stroke="#99f6e4" stroke-width="1.3"><circle cx="8" cy="6" r="2"/>'
        '<circle cx="16" cy="6" r="2"/><circle cx="12" cy="17" r="2"/>'
        '<path d="M8 8v2l4 3v2m4-7v2l-4 3"/></g>'
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="22" '
        f'viewBox="0 0 {width} 22" role="img" aria-label="{kind}: {value}">'
        f'<rect width="{width}" height="22" rx="4" fill="{color}"/>{icon}'
        f'<text x="{(24 + width) / 2}" y="15" fill="white" font-family="Segoe UI,Arial,sans-serif" '
        f'font-size="11" text-anchor="middle">{value}</text></svg>\n'
    )


def main():
    # Fetch all counters before writing; preserve the snapshot if a request fails.
    counters = {name: github_repo(name) for name in REPOS}
    today = datetime.now(timezone(timedelta(hours=8))).date().isoformat()
    output = ROOT / "assets" / "metrics"
    output.mkdir(parents=True, exist_ok=True)
    for name, values in counters.items():
        for key, color in (("stars", "#7c3aed"), ("forks", "#0d9488")):
            (output / f"{name}-{key}.svg").write_text(
                counter_badge(key, values[key], color), encoding="utf-8"
            )
    (output / "updated.svg").write_text(badge("更新", today, "#475569"), encoding="utf-8")
    (output / "updated-en.svg").write_text(badge("Updated", today, "#475569"), encoding="utf-8")
    (output / "snapshot.json").write_text(
        json.dumps({"updated_date_cst": today, "repositories": counters}, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Updated metrics for {len(counters)} public repositories ({today}).")


if __name__ == "__main__":
    main()
