"""Refresh the public project index, counters and weekly star snapshots."""

import json
import os
from datetime import datetime, timedelta, timezone
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CATALOG = {
    'curforever-skills': ('Agent Skills', '开发、学习与项目管理技能集', 'Development, learning & project skills'),
    'curforever.github.io': ('博客站点', '工程复盘、研究图解与阅读笔记', 'Engineering, research & reading notes'),
    'Keyboard': ('键盘记录', '试轴照片、手感体验与选型清单', 'Switch photos, feel & selection notes'),
    'CSSLearning': ('CSS 实验', 'CSS 学习案例与界面探索', 'CSS learning & interface experiments'),
    'leetcode-master': ('开源贡献', 'Fork：补充 Java、修正文档；4 个 PR 已合并', 'Fork: Java & documentation; 4 merged PRs'),
    'CangQiongWaiMai-Java': ('外卖平台', '课程练习：业务、缓存与 Spring', 'Course practice: business, cache & Spring'),
    'HexoBlogBackup': ('博客源码', 'Hexo 内容、主题与站点配置', 'Hexo content, theme & configuration'),
    'curforever': ('主页工程', '中英文主页、展示素材与指标刷新', 'Bilingual profile, assets & metric refresh'),
}


def github_public_repos():
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "curforever-profile"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    repositories = []
    page = 1
    while True:
        request = Request(f'https://api.github.com/users/curforever/repos?type=owner&per_page=100&page={page}', headers=headers)
        with urlopen(request, timeout=30) as response:
            data = json.load(response)
        for repo in data:
            if repo['private'] or repo['owner']['login'].lower() != 'curforever':
                continue
            repositories.append(repo)
        if len(data) < 100:
            break
        page += 1
    order = list(CATALOG)
    return sorted(repositories, key=lambda r: (order.index(r['name']) if r['name'] in order else 4, r['name'].lower()))


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


def project_index(repos, english=False):
    rows = ['| Project | Stars | Forks | Purpose & context |' if english else '| 项目 | Stars | Forks | 用途与边界 |', '| :--- | :---: | :---: | :--- |']
    for repo in repos:
        name = repo['name']
        label, cn, en = CATALOG.get(name, (name, '公开仓库 · 说明待补充', 'Public repository · description to follow'))
        # Never inject arbitrary API descriptions into Markdown or expose private repositories.
        label = name if english else label
        description = en if english else cn
        if repo['fork'] and name not in CATALOG:
            description = ('Fork · ' if english else 'Fork · ') + description
        safe_label = label.replace('|', '\\|').replace('[', '\\[').replace(']', '\\]')
        rows.append(f'| [{safe_label}](https://github.com/curforever/{name}) | ![Stars](assets/metrics/{name}-stars.svg) | ![Forks](assets/metrics/{name}-forks.svg) | {description} |')
    return '\n'.join(rows)


def trend_svg(history):
    points = history['snapshots']
    width, height = 840, 112
    max_value = max(1, max(p['total_stars'] for p in points))
    first = datetime.fromisoformat(points[0]['date'])
    span = max(7, (datetime.fromisoformat(points[-1]['date']) - first).days)
    coords = [(58 + 728 * (datetime.fromisoformat(p['date'])-first).days/span, 82 - 36*p['total_stars']/max_value) for p in points]
    polyline = ' '.join(f'{x:.2f},{y:.2f}' for x, y in coords)
    dots = ''.join(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="3.5" fill="#5eead4"><title>{p["date"]}: {p["total_stars"]} stars</title></circle>' for (x,y),p in zip(coords,points))
    last = points[-1]
    note = 'First snapshot recorded · more points arrive weekly' if len(points)==1 else f'{len(points)} observed snapshots · current total can rise or fall'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Public non-fork repository stars: weekly observed totals">
<rect width="840" height="112" rx="10" fill="#101827"/>
<g font-family="Segoe UI,Arial,sans-serif"><text x="24" y="22" fill="#a5b4fc" font-size="11" letter-spacing="1.5">PUBLIC REPOSITORIES / STAR SNAPSHOTS</text><text x="24" y="38" fill="#cbd5e1" font-size="11">{note}</text><text x="788" y="30" fill="#5eead4" font-size="24" text-anchor="end" font-weight="700">{last['total_stars']}</text>
<path d="M58 46V82H786M58 46H786M58 64H786" fill="none" stroke="#334155" stroke-width="1"/>
<text x="47" y="50" text-anchor="end" fill="#94a3b8" font-size="10">{max_value}</text><text x="47" y="86" text-anchor="end" fill="#94a3b8" font-size="10">0</text>
<polyline points="{polyline}" fill="none" stroke="#2dd4bf" stroke-width="2"/>{dots}
<text x="58" y="103" fill="#94a3b8" font-size="11">{points[0]['date']}</text><text x="786" y="103" fill="#94a3b8" font-size="11" text-anchor="end">Latest: {last['date']} · weekly snapshots</text></g></svg>\n'''


def main():
    # Fetch all counters before writing; preserve the snapshot if a request fails.
    repos = github_public_repos()
    counters = {r['name']: {'stars': r['stargazers_count'], 'forks': r['forks_count']} for r in repos}
    today = datetime.now(timezone(timedelta(hours=8))).date().isoformat()
    output = ROOT / "assets" / "metrics"
    output.mkdir(parents=True, exist_ok=True)
    history_path = output / 'stars-history.json'
    history = json.loads(history_path.read_text(encoding='utf-8')) if history_path.exists() else {'scope': 'Public non-fork repositories owned by curforever; observed current total, not cumulative-ever stars', 'snapshots': []}
    total = sum(r['stargazers_count'] for r in repos if not r['fork'])
    sample = {'date': today, 'total_stars': total, 'repositories': {r['name']: r['stargazers_count'] for r in repos if not r['fork']}}
    history['snapshots'] = sorted([s for s in history['snapshots'] if s['date'] != today] + [sample], key=lambda s:s['date'])
    # Prepare both documents before writing; missing markers signal a template error.
    readmes = {}
    for filename in ('README.md', 'README.en.md'):
        text = (ROOT / filename).read_text(encoding='utf-8')
        start, end = '<!-- PUBLIC_PROJECTS_START -->', '<!-- PUBLIC_PROJECTS_END -->'
        if text.count(start) != 1 or text.count(end) != 1:
            raise ValueError(f'Missing/duplicate project markers in {filename}')
        before, middle = text.split(start)
        _, after = middle.split(end)
        readmes[filename] = before + start + '\n' + project_index(repos, filename.endswith('.en.md')) + '\n' + end + after
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
    history_path.write_text(json.dumps(history, indent=2) + '\n', encoding='utf-8')
    (output / 'stars-trend.svg').write_text(trend_svg(history), encoding='utf-8')
    for filename, text in readmes.items():
        (ROOT / filename).write_text(text, encoding='utf-8')
    print(f"Updated metrics for {len(counters)} public repositories ({today}).")


if __name__ == "__main__":
    main()
