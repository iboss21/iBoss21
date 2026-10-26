"""Builds the iboss21.github.io site from the same project map as the README, on the Noesis layout
(tools/site_template.html) in the LXR UI Kit palette.
Run: python tools/build_site.py <path-to-iboss21.github.io-checkout>"""
import html, json, pathlib, shutil, sys
from urllib.parse import quote
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_readme import SECTIONS, SCRIPTS, TOOLS  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = pathlib.Path(sys.argv[1]).resolve()
e = html.escape

def card(p):
    host = p['url'].split('//', 1)[1].split('/', 1)[0]
    repos = ''.join(f'<a class="chip" href="https://github.com/iboss21/{r}">GitHub · {e(r)}</a>' for r in p.get('repos', []))
    shot = f'<a class="shot" href="{p["url"]}"><img src="cards/{p["card"]}.jpg" alt="{e(p["name"])}" loading="lazy" width="640" height="360"></a>' if p.get('card') else ''
    badge = (f'<img class="live" alt="{e(host)} status" loading="lazy" src="https://img.shields.io/website?url={quote(p["url"], safe="")}'
             f'&amp;label={quote(host)}&amp;up_message=live&amp;up_color=c21c37&amp;down_message=offline&amp;style=flat-square&amp;labelColor=0e0e11">')
    return (f'<article class="card">{shot}<div class="body"><h3><a href="{p["url"]}">{e(p["name"])}</a></h3>'
            f'<p>{e(p["what"])}</p><div class="meta">{badge}{repos}</div></div></article>')

def short(title):
    return title.split(' ', 1)[1].split(':')[0]

sections = '\n'.join(
    f'<section class="fam" id="{k}" data-scene="4"><div class="wrap"><div class="head"><div class="kick mono">{i + 1:02d} · {e(short(t))}</div>'
    f'<h2>{e(short(t))}</h2><p class="lede">{e(intro)}</p></div><div class="grid">{"".join(card(p) for p in items)}</div></div></section>'
    for i, (k, t, intro, items) in enumerate(SECTIONS))
family_list = ''.join(f'<li><a href="#{k}">{e(short(t))}<small>{len(items)} {"project" if len(items) == 1 else "projects"}</small></a></li>'
                      for k, t, _, items in SECTIONS)
oss = ''.join(f'<li><a href="https://github.com/iboss21/{r}"><b>{e(r)}</b><span>{e(d)}</span></a></li>' for r, d in TOOLS)
scripts = ''.join(f'<a class="chip" href="https://github.com/iboss21/{s}">{e(s)}</a>' for s in SCRIPTS)

QA = [
    {'q': 'Can you build a restaurant site that takes orders?',
     'a': ['Yes. A bilingual site with online ordering, kitchen printing and every delivery app on one screen, live in 7 to 21 days.<span class=cite>1</span>',
           'This Georgian supra house template is one of the designs we build from.<span class=cite>2</span>'],
     'src': [['AnimatedWebs', 'https://animatedwebs.com'], ['Supra house demo', 'https://animatedwebs.com/demos/tamada-supra-house/index.html']]},
    {'q': 'Do you build private AI for a business?',
     'a': ['Reges runs AI on your own PC or server, and it asks before it sends, posts, pays or shares anything.<span class=cite>1</span>',
           'Developers get Reges Code, an AI code editor.<span class=cite>2</span>'],
     'src': [['RegesCore', 'https://regescore.pro'], ['Reges Code', 'https://regescode.com']]},
    {'q': 'Show me something you built for a client.',
     'a': ['PrimeAuto Connect: online quotes, booking, e-signed contracts, live vehicle tracking and a full CRM.<span class=cite>1</span>',
           'Frei Company: a company website, designed and built end to end.<span class=cite>2</span>'],
     'src': [['PrimeAuto Connect', 'https://primeautoconnect.net'], ['Frei Company', 'https://freicompany.ge']]},
    {'q': 'What do you make for game servers?',
     'a': ['LXRCore is our RedM roleplay framework, with farming, hunting, police and economy modules.<span class=cite>1</span>',
           'We also run two roleplay communities of our own.<span class=cite>2</span><span class=cite>3</span>'],
     'src': [['LXRCore', 'https://www.lxrcore.com'], ['The Land of Wolves', 'https://wolves.land'], ['The Lux Empire', 'https://theluxempire.com']]},
]

page = (ROOT / 'tools' / 'site_template.html').read_text(encoding='utf-8')
for key, val in {
    '{{SECTIONS}}': sections, '{{FAMILY_LIST}}': family_list, '{{FAMILY_COUNT}}': str(len(SECTIONS)),
    '{{PROJECT_COUNT}}': str(sum(len(s[3]) for s in SECTIONS)), '{{OSS}}': oss, '{{SCRIPTS}}': scripts,
    '{{QA}}': json.dumps(QA, ensure_ascii=False),
}.items():
    page = page.replace(key, val)
OUT.mkdir(parents=True, exist_ok=True)
(OUT / 'index.html').write_text(page, encoding='utf-8')
shutil.copytree(ROOT / 'assets' / 'cards', OUT / 'cards', dirs_exist_ok=True)
for stale in ('style.css', 'main.js'):
    (OUT / stale).unlink(missing_ok=True)
print('site written to', OUT)
