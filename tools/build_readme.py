"""Builds README.md from the project map below. Edit PROJECTS, then run: python tools/build_readme.py"""
from urllib.parse import quote
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
RED = 'c8161d'

def live(url, label):
    return (f'<a href="{url}"><img alt="{label} status" src="https://img.shields.io/website?url={quote(url, safe="")}'
            f'&label={quote(label)}&up_message=live&up_color={RED}&down_message=offline&style=flat-square"></a>')

def repo_badge(repo):
    return (f'<a href="https://github.com/iboss21/{repo}"><img alt="{repo} repo" '
            f'src="https://img.shields.io/badge/repo-{quote(repo.replace("-", "--"))}-0b0b0d?style=flat-square&logo=github"></a>')

def card(p):
    img = f'<a href="{p["url"]}"><img src="assets/cards/{p["card"]}.jpg" alt="{p["name"]}" width="100%"></a>' if p.get('card') else ''
    badges = ' '.join(([live(p['url'], p['label'])] if p.get('label') else []) + [repo_badge(r) for r in p.get('repos', [])])
    return (f'<td width="50%" valign="top">\n{img}\n\n<b><a href="{p["url"]}">{p["name"]}</a></b><br>\n'
            f'<sub>{p["what"]}</sub><br>\n{badges}\n</td>')

def grid(items):
    rows = []
    for i in range(0, len(items), 2):
        pair = items[i:i + 2]
        cells = '\n'.join(card(p) for p in pair) + ('\n<td width="50%"></td>' if len(pair) == 1 else '')
        rows.append(f'<tr>\n{cells}\n</tr>')
    return '<table>\n' + '\n'.join(rows) + '\n</table>'

SECTIONS = [
    ('reges', '🤖 Reges: private AI platform', 'A local-first AI OS whose agents ask before they send, post, pay or share anything. Runs on your own PC or your own server.', [
        dict(name='RegesCore', url='https://regescore.pro', label='regescore.pro', card='regescore', what='The Reges platform: private AI assistants, automation and dashboards for people and businesses.'),
        dict(name='Reges Code', url='https://regescode.com', label='regescode.com', card='regescode', what='An AI code editor for developers, with licences and automatic updates.'),
        dict(name='Reges Town', url='https://regestown.com', label='regestown.com', card='regestown', what='A living 3D town of AI characters, streamed live around the clock.'),
        dict(name='RegesARC', url='https://regesarc.com', label='regesarc.com', card='regesarc', repos=['RegesARC'], what='Research: running bigger AI models on everyday 12 GB graphics cards.'),
        dict(name='Millicent', url='https://heymillicent.com', label='heymillicent.com', card='millicent', what='An AI community member for Discord servers that chats, helps and plays.'),
        dict(name='My Little Bots', url='https://mylittlebots.com', label='mylittlebots.com', card='mylittlebots', what='Custom AI bot designs.'),
    ]),
    ('web', '🎨 Web, design and motion', 'Cinematic websites, templates and the tools behind them.', [
        dict(name='AnimatedWebs', url='https://animatedwebs.com', label='animatedwebs.com', card='animatedwebs', repos=['animatedwebs-claude'], what='Animated, cinematic website templates, plus a Claude Code plugin with 1,200+ templates through MCP.'),
        dict(name='Georgian supra house demo', url='https://animatedwebs.com/demos/tamada-supra-house/index.html', label='live demo', card='tamada', what='A restaurant template: WebGL particles, menu, booking and hours. The base for our restaurant builds.'),
        dict(name='LIKE A KING INC.', url='https://likeakinginc.com', label='likeakinginc.com', card='likeakinginc', what='Web development, hosting and AI for businesses: websites, online ordering, dashboards and apps.'),
        dict(name='davidio.dev', url='https://davidio.dev', label='davidio.dev', card='davidio', what='Our developer studio: web development and AI integrations.'),
    ]),
    ('products', '💼 Products', 'Software we run and sell.', [
        dict(name='ReadySeen', url='https://readyseen.com', label='readyseen.com', card='readyseen', what='Patients prepare for doctor visits and book clinics online. Clinics get a ready brief and an inbox.'),
        dict(name='CreditFixExpert', url='https://creditfixexpert.com', label='creditfixexpert.com', card='creditfixexpert', what='A credit-repair platform with client accounts and online payments.'),
    ]),
    ('clients', '🤝 Client work', 'Built for clients, end to end.', [
        dict(name='PrimeAuto Connect', url='https://primeautoconnect.net', label='primeautoconnect.net', card='primeauto', what='Auto transport: online quotes, booking, e-signed contracts, live vehicle tracking and a full CRM dashboard.'),
        dict(name='Frei Company', url='https://freicompany.ge', label='freicompany.ge', card='freicompany', what='A company website, designed and built end to end.'),
    ]),
    ('roleplay', '🎮 Roleplay and game servers', 'Frameworks, scripts and communities for RedM and FiveM.', [
        dict(name='LXRCore', url='https://www.lxrcore.com', label='lxrcore.com', card='lxrcore', what='A modular, fast RedM roleplay framework, with farming, hunting, police and economy modules.'),
        dict(name='The Land of Wolves', url='https://wolves.land', label='wolves.land', card='wolves', what='A roleplay community: website, server and systems.'),
        dict(name='The Lux Empire', url='https://theluxempire.com', label='theluxempire.com', card='luxempire', what='A roleplay community: website, server and systems.'),
    ]),
]

SCRIPTS = ['LXRCore-Police-System', 'lxr-mdt', 'lxr-tattoos', 'lxr-whitelist', 'lxr-pedscale', 'lxr-fight', 'lxr-drag', 'lxr-voicerange',
           'lxr-spirits', 'lxr-minigames', 'lxr-doorhash', 'lx-inventory', 'RedM-Server-Economic-System-Structure']
TOOLS = [('RegesMoE', 'Run RegesCore models on a normal PC: one installer, a local OpenAI/Anthropic-compatible API'),
         ('regescore-benchmark', 'Benchmark your local LLMs'),
         ('gguf-editor', 'Inspect and edit GGUF model files'),
         ('llm-trainer', 'Local single- and multi-GPU GGUF manager'),
         ('claude-lmstudio', 'Connection and API-error fixes for Claude with LM Studio'),
         ('git-pr-extractor', 'Extract, upload and download GitHub PRs from a Windows UI')]

def mermaid():
    lines = ['```mermaid', 'mindmap', '  root((LIKE A KING INC.))']
    for key, title, _, items in SECTIONS:
        lines.append(f'    {title.split(" ", 1)[1].split(":")[0]}')
        for p in items:
            lines.append(f'      {p["name"]}')
    lines.append('    Open source')
    lines.append('      RegesMoE')
    lines.append('      LXR scripts')
    lines.append('```')
    return '\n'.join(lines)

def build():
    out = []
    out.append('<p align="center"><img src="assets/hero.svg" alt="LIKE A KING INC. · We build the web that moves" width="100%"></p>\n')
    out.append('<p align="center">\n'
               '<a href="https://likeakinginc.com"><img src="https://img.shields.io/badge/LIKE%20A%20KING%20INC.-New%20York-c8161d?style=for-the-badge" alt="LIKE A KING INC."></a>\n'
               '<a href="https://x.com/RegesCoreAi"><img src="https://img.shields.io/badge/X-@RegesCoreAi-0b0b0d?style=for-the-badge&logo=x&logoColor=white" alt="X @RegesCoreAi"></a>\n'
               '<a href="https://www.linkedin.com/in/bossonline/"><img src="https://img.shields.io/badge/LinkedIn-connect-0b0b0d?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>\n'
               '<a href="https://github.com/iboss21?tab=followers"><img src="https://img.shields.io/github/followers/iboss21?style=for-the-badge&color=c8161d&labelColor=0b0b0d&logo=github" alt="GitHub followers"></a>\n'
               '<img src="https://komarev.com/ghpvc/?username=iBoss21&label=profile%20views&color=c8161d&style=for-the-badge" alt="Profile views">\n'
               '</p>\n')
    out.append('<p align="center"><a href="https://github.com/iboss21"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=3200&pause=900&color=FF6B5E&center=true&vCenter=true&width=760&lines=Websites+%C2%B7+ordering+systems+%C2%B7+apps+for+real+businesses;Reges%3A+private%2C+local-first+AI+that+asks+before+it+acts;Cinematic+templates+%C2%B7+roleplay+frameworks+%C2%B7+open+source" alt="What we build"></a></p>\n')
    out.append('## 🗺️ Map\n')
    toc = ' · '.join(f'[{t.split(" ", 1)[1].split(":")[0]}](#{k})' for k, t, _, _ in SECTIONS)
    out.append(f'{toc} · [Open source](#open-source) · [Stack](#stack) · [Activity](#activity) · [Work with us](#work-with-us)\n')
    out.append('**LIKE A KING INC.** is a New York software company. We design and build websites, online ordering and booking systems, dashboards, apps and private AI for businesses, and we run our own products alongside client work.\n')
    out.append(mermaid() + '\n')
    for key, title, intro, items in SECTIONS:
        out.append(f'<h2 id="{key}">{title}</h2>\n\n{intro}\n\n{grid(items)}\n')
    out.append('<details>\n<summary><b>LXR scripts for RedM and FiveM</b> (open source)</summary>\n\n' +
               ' '.join(f'[`{s}`](https://github.com/iboss21/{s})' for s in SCRIPTS) + '\n\n</details>\n')
    out.append('<h2 id="open-source">🧪 Open source</h2>\n\n| Repo | What it does |\n|---|---|\n' +
               '\n'.join(f'| [**{r}**](https://github.com/iboss21/{r}) | {d} |' for r, d in TOOLS) + '\n')
    out.append('<h2 id="stack">🧰 Stack</h2>\n\n<p align="center"><img src="https://skillicons.dev/icons?i=ts,js,nodejs,react,nextjs,threejs,tailwind,vite,python,cpp,lua,docker,linux,nginx,postgres,redis,githubactions,git&perline=9&theme=dark" alt="Stack"></p>\n')
    out.append('<h2 id="activity">📈 Activity</h2>\n\n'
               '<p align="center"><img src="profile-3d-contrib/profile-night-rainbow.svg" alt="3D contribution city" width="100%"></p>\n\n'
               '<p align="center">\n'
               '<img height="165" src="https://github-readme-stats-eight-theta.vercel.app/api?username=iBoss21&show_icons=true&include_all_commits=true&count_private=true&title_color=a40619&icon_color=a960ff&text_color=ffffff&bg_color=0c0b0c" alt="GitHub stats">\n'
               '<img height="165" src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=iBoss21&layout=compact&langs_count=8&title_color=a40619&text_color=ffffff&bg_color=0c0b0c" alt="Top languages">\n'
               '</p>\n\n'
               '<p align="center"><img src="https://streak-stats.demolab.com/?user=iboss21&hide_border=true&background=0B0B0D&ring=C8161D&fire=FF6B5E&currStreakLabel=FF6B5E&sideLabels=F4F2EF&currStreakNum=F4F2EF&sideNums=F4F2EF&dates=A6A6AB&stroke=2A070B" alt="Streak"></p>\n\n'
               '<picture>\n  <source media="(prefers-color-scheme: dark)" srcset="assets/generated/snake-dark.svg">\n'
               '  <img alt="Contribution snake" src="assets/generated/snake-light.svg" width="100%">\n</picture>\n')
    out.append('<h2 id="work-with-us">📫 Work with us</h2>\n\n'
               'Need a website that takes orders, a booking system, a dashboard, an app or private AI for your business?\n\n'
               '<p>\n<a href="https://likeakinginc.com/contact"><img src="https://img.shields.io/badge/Start%20a%20project-likeakinginc.com-c8161d?style=for-the-badge" alt="Start a project"></a>\n'
               '<a href="https://animatedwebs.com"><img src="https://img.shields.io/badge/Templates-animatedwebs.com-0b0b0d?style=for-the-badge" alt="AnimatedWebs"></a>\n'
               '<a href="https://regescore.pro"><img src="https://img.shields.io/badge/Private%20AI-regescore.pro-0b0b0d?style=for-the-badge" alt="RegesCore"></a>\n</p>\n')
    out.append('<p align="center"><sub>Status badges check each site live · cards are screenshots of the real sites · the 3D city and snake rebuild daily from contributions</sub></p>\n')
    (ROOT / 'README.md').write_text('\n'.join(out), encoding='utf-8')

if __name__ == '__main__':
    build()
    print('README.md written')
