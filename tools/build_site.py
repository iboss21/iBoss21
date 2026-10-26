"""Builds the iboss21.github.io site from the same project map as the README.
Run: python tools/build_site.py <path-to-iboss21.github.io-checkout>"""
import html, pathlib, shutil, sys
from urllib.parse import quote
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_readme import SECTIONS, SCRIPTS, TOOLS  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(sys.argv[1]).resolve()
e = html.escape

def card(p):
    host = p['url'].split('//', 1)[1].split('/', 1)[0]
    repos = ''.join(f'<a class="chip" href="https://github.com/iboss21/{r}">GitHub · {e(r)}</a>' for r in p.get('repos', []))
    shot = f'<img src="cards/{p["card"]}.jpg" alt="{e(p["name"])}" loading="lazy" width="640" height="360">' if p.get('card') else ''
    return (f'<article class="card"><a class="shot" href="{p["url"]}">{shot}</a>'
            f'<div class="body"><h3><a href="{p["url"]}">{e(p["name"])}</a></h3><p>{e(p["what"])}</p>'
            f'<div class="meta"><img class="live" alt="{e(host)} status" loading="lazy" src="https://img.shields.io/website?url={quote(p["url"], safe="")}&amp;label={quote(host)}&amp;up_message=live&amp;up_color=c8161d&amp;down_message=offline&amp;style=flat-square&amp;labelColor=121214">{repos}</div></div></article>')

sections = ''.join(
    f'<section class="fam" id="{k}"><header><p class="kicker">{i + 1:02d}</p><h2>{e(t.split(" ", 1)[1])}</h2><p class="lede">{e(intro)}</p></header>'
    f'<div class="grid">{"".join(card(p) for p in items)}</div></section>'
    for i, (k, t, intro, items) in enumerate(SECTIONS))
oss = ''.join(f'<li><a href="https://github.com/iboss21/{r}"><b>{e(r)}</b><span>{e(d)}</span></a></li>' for r, d in TOOLS)
scripts = ''.join(f'<a class="chip" href="https://github.com/iboss21/{s}">{e(s)}</a>' for s in SCRIPTS)
nav = ''.join(f'<a href="#{k}">{e(t.split(" ", 1)[1].split(":")[0])}</a>' for k, t, _, _ in SECTIONS)

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>LIKE A KING INC. · iBoss</title>
<meta name="description" content="LIKE A KING INC. is a New York software company: websites, ordering systems, apps and private AI for businesses, plus Reges, AnimatedWebs, ReadySeen and LXRCore.">
<meta property="og:title" content="LIKE A KING INC. · iBoss">
<meta property="og:description" content="Websites, ordering systems, apps and private AI for real businesses. New York.">
<meta property="og:image" content="https://iboss21.github.io/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0b0d">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
<script type="importmap">{{"imports":{{"three":"https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js"}}}}</script>
</head>
<body>
<canvas id="gl" aria-hidden="true"></canvas>
<header class="top"><a class="brand" href="#top">LAKI<span>LIKE A KING INC.</span></a><nav>{nav}<a href="#oss">Open source</a><a href="#activity">Activity</a><a class="cta" href="https://likeakinginc.com/contact">Start a project</a></nav></header>
<main>
<section class="hero" id="top">
  <p class="kicker">iBoss · LIKE A KING INC. · New York</p>
  <h1>We build the web<br><em>that moves.</em></h1>
  <p class="lede">Websites, online ordering and booking, dashboards, apps and private AI for real businesses. We run our own products alongside client work.</p>
  <div class="row"><a class="btn" href="https://likeakinginc.com/contact">Start a project</a><a class="btn ghost" href="#reges">See the work</a></div>
  <ul class="stats"><li><b>{sum(len(s[3]) for s in SECTIONS)}</b>live projects</li><li><b>5</b>product families</li><li><b>7–21</b>days to launch</li></ul>
</section>
{sections}
<section class="fam" id="oss"><header><p class="kicker">{len(SECTIONS) + 1:02d}</p><h2>Open source</h2><p class="lede">Tools we publish and maintain.</p></header>
<ul class="oss">{oss}</ul><p class="lede small">LXR scripts for RedM and FiveM:</p><div class="chips">{scripts}</div></section>
<section class="fam" id="activity"><header><p class="kicker">GitHub</p><h2>Activity</h2><p class="lede">Live from GitHub: every commit, public and private, rebuilt daily.</p></header>
<div class="stats-cards"><img src="https://github-readme-stats-eight-theta.vercel.app/api?username=iBoss21&show_icons=true&include_all_commits=true&count_private=true&title_color=a40619&icon_color=a960ff&text_color=ffffff&bg_color=0c0b0c" alt="GitHub stats" loading="lazy">
<img src="https://streak-stats.demolab.com/?user=iboss21&hide_border=true&background=0B0B0D&ring=C8161D&fire=FF6B5E&currStreakLabel=FF6B5E&sideLabels=F4F2EF&currStreakNum=F4F2EF&sideNums=F4F2EF&dates=A6A6AB&stroke=2A070B" alt="GitHub streak" loading="lazy">
<img src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=iBoss21&layout=compact&langs_count=8&title_color=a40619&text_color=ffffff&bg_color=0c0b0c" alt="Top languages" loading="lazy"></div>
<img class="city" src="https://raw.githubusercontent.com/iboss21/iBoss21/main/profile-3d-contrib/profile-night-rainbow.svg" alt="3D contribution city" loading="lazy"></section>
<section class="end"><h2>Have something to build?</h2><p class="lede">Tell us what your business needs. We answer within a day.</p>
<div class="row"><a class="btn" href="https://likeakinginc.com/contact">Start a project</a><a class="btn ghost" href="https://github.com/iboss21">GitHub</a><a class="btn ghost" href="https://x.com/RegesCoreAi">X</a></div></section>
</main>
<footer><span>© 2026 LIKE A KING INC. · New York</span><a href="https://github.com/iboss21/iboss21.github.io">Source</a></footer>
<script type="module" src="main.js"></script>
</body>
</html>
'''
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'index.html').write_text(page, encoding='utf-8')
shutil.copytree(ROOT / 'assets' / 'cards', OUT / 'cards', dirs_exist_ok=True)
print('site written to', OUT)
