"""Generate a dependency-free GitHub Pages website. Run: python build.py."""
from pathlib import Path
from html import escape
import json
import re

ROOT = Path(__file__).parent
OUT = ROOT / 'docs'
analytics = json.loads((ROOT / 'analytics.json').read_text(encoding='utf-8'))
project_id = str(analytics.get('statcounter_project_id', '')).strip()
security_code = str(analytics.get('statcounter_security_code', '')).strip()
analytics_ready = bool(project_id or security_code)
if analytics_ready and not (
    re.fullmatch(r'[0-9]{1,15}', project_id)
    and int(project_id) > 0
    and re.fullmatch(r'[A-Za-z0-9]{8,64}', security_code)
):
    raise ValueError('Set both Statcounter installation identifiers in analytics.json, or leave both empty.')
def author(name):
    if name == 'Jingyuan Yang':
        return '<strong>Jingyuan Yang</strong>'
    return escape(name)

def paper(title, names, status, ssrn=None, extra=''):
    url = f'https://papers.ssrn.com/sol3/papers.cfm?abstract_id={ssrn}' if ssrn else None
    heading = f'<a href="{url}">{escape(title)}</a>' if url else escape(title)
    return f'<li class="paper"><h3>{heading}</h3><p class="authors">{", ".join(author(n) for n in names)}</p><p class="status">{status}</p>{extra}</li>'

home = '''<h1>Welcome!</h1>
<p>I’m Jingyuan Yang (杨静远). I am a Ph.D. student in Management Science and Operations Management at the <a href="http://chicagobooth.edu/phd">University of Chicago Booth School of Business</a>. I am honored to be advised by <a href="https://xin.engineering.cornell.edu/">Prof. Linwei Xin</a>.</p>
<p>My research focuses on <strong>AI for supply chains</strong>, especially <strong>inventory management</strong>. My recent work explores how foundation models can move from forecasting to decision-making. I am interested in combining them with the structural insight of classical inventory theory to make inventory decisions high-performing, scalable, and implementable in practice, while also providing managerial insights. Involved methodologies include stochastic modeling, optimization, and deep learning.</p>
<p>Before joining Chicago Booth, I earned master’s degrees from Tsinghua University and Columbia University, and a bachelor’s degree from Shanghai University of Finance and Economics.</p>
<section aria-labelledby="education"><h2 id="education">Education</h2>
<dl class="education">
<div><dt>University of Chicago, Booth School of Business</dt><dd><span class="degree">Ph.D. in Management Science and Operations Management</span><span class="education-date">2023 – 2028 (expected)</span></dd></div>
<div><dt>Tsinghua University</dt><dd><span class="degree">M.S. in Management Science and Engineering</span><span class="education-date">2021 – 2023</span></dd></div>
<div><dt>Columbia University</dt><dd><span class="degree">M.S. in Operations Research</span><span class="education-date">2022 – 2023</span></dd></div>
<div><dt>Shanghai University of Finance and Economics</dt><dd><span class="degree">B.S. in Information Management and Systems</span><span class="education-date">2017 – 2021</span></dd></div>
</dl></section>
<section aria-labelledby="contact"><h2 id="contact">Contact</h2><p>For research discussions or collaborations, please email <a href="mailto:jyang21@chicagobooth.edu">jyang21@chicagobooth.edu</a>.</p></section>'''

research = '<h1>Working papers</h1><ol class="papers">'
research += paper('Foundation Models for Newsvendor Decisions', ['Jingyuan Yang', 'Linwei Xin', 'Qichuan Yin'], 'Work in progress.')
research += paper('A Bitter Lesson for Retail Demand Forecasting: Evidence from Fine-Tuning Foundation Models', ['Yi Sui', 'Chenjie Xiao', 'Linwei Xin', 'Jingyuan Yang', 'Donghai Huang', 'Lei Cao'], 'Major revision at <em>Manufacturing &amp; Service Operations Management</em>.', '6788658')
research += paper('Beyond Asymptotic Policies: A Deep Learning-Based HDPO Approach to Remanufacturing Systems', ['Linwei Xin', 'Jingyuan Yang'], 'Work in progress.', '3760906', '<p class="paper-note">Earlier version: <em>Asymptotic Analysis of a Remanufacturing System with Non-Identical Lead Times.</em></p>')
research += paper('Losing Sales to Gain: Mitigating Demand Spillover in Inventory Networks', ['Jingyuan Yang', 'Linwei Xin', 'Yuan Zhong'], 'Major revision at <em>Management Science</em>.', '5291958')
research += paper('Auto-Formulating Dynamic Programming Problems with Large Language Models', ['Chenyu Zhou', 'Jingyuan Yang', 'Linwei Xin', 'Yitian Chen', 'Ziyan He', 'Dongdong Ge'], 'Second-round major revision at <em>Manufacturing &amp; Service Operations Management</em>.', '5350161')
research += '</ol><h2>Publications</h2><ol class="papers">'
research += paper('Technical Note—Error Noted in “Robust Contract Designs: Linear Contracts and Moral Hazard” by Yu and Kong (2020)', ['Jingyuan Yang', 'Linwei Xin'], '<em>Operations Research</em>, 74(2), 722–729, 2026.', '3895883')
research += '</ol>'

teaching = '''<h1>Teaching</h1>
<section class="teaching-section" aria-labelledby="teaching-assistant"><h2 id="teaching-assistant">Teaching Assistant, Booth School of Business</h2>
<ul class="teaching-list">
<li><div class="course-row"><span>BUSN 40000 Operations Management (MBA)</span><span class="course-date">Winter and Spring 2025; Spring 2026</span></div></li>
<li><div class="course-row"><span>BUSN 40101 Supply Chain Strategy and Practice (MBA)</span><span class="course-date">Winter 2026</span></div></li>
<li><div class="course-row"><span>BUSN 36106 Managerial Decision Modeling (MIM)</span><span class="course-date">Autumn 2025; Autumn 2026</span></div></li>
<li><div class="course-row"><span>BUSN 36106 Managerial Decision Modeling (MBA)</span><span class="course-date">Summer 2026</span></div></li>
</ul></section>
<section class="teaching-section" aria-labelledby="teaching-assistant-sufe"><h2 id="teaching-assistant-sufe">Teaching Assistant, Shanghai University of Finance and Economics</h2>
<ul class="teaching-list">
<li><div class="course-row"><span>High-dimensional Data Analysis</span><span class="course-date">Sep 2020 – Jan 2021</span></div></li>
</ul></section>'''

for slug, label, content in [('', 'Homepage', home), ('research', 'Research', research), ('teaching', 'Teaching', teaching)]:
    base = '../' if slug else './'
    tracking = (
        f'<script src="{base}assets/analytics.js" data-project="{project_id}" '
        f'data-security="{security_code}" defer></script>'
        if analytics_ready else ''
    )
    nav = ''.join(f'<a href="{base}{s + "/" if s else ""}"' + (' aria-current="page"' if s == slug else '') + f'>{l}</a>' for s,l in [('', 'Homepage'), ('research', 'Research'), ('teaching', 'Teaching')])
    html = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{label} | Jingyuan (Angela) Yang</title><meta name="description" content="Jingyuan (Angela) Yang, Ph.D. student at Chicago Booth. Research on AI for supply chains, foundation models for inventory decisions, stochastic modeling, optimization, and deep learning.">
<link rel="canonical" href="https://angelaaa218.github.io/{slug + '/' if slug else ''}"><link rel="stylesheet" href="{base}assets/style.css"><link rel="icon" href="{base}assets/favicon.svg" type="image/svg+xml"></head>
<body><a class="skip-link" href="#main">Skip to content</a><header class="masthead"><div class="masthead-inner"><a class="site-name" href="{base}">Jingyuan (Angela) Yang</a><nav aria-label="Main navigation">{nav}</nav></div></header>
<div class="layout"><aside class="profile" aria-label="Profile"><img class="portrait" src="{base}assets/portrait.jpg" alt="Jingyuan (Angela) Yang" width="3971" height="5957"><h2>Jingyuan (Angela) Yang</h2><p class="role">Ph.D. student, Management Science and Operations Management, Chicago Booth</p><ul class="profile-links"><li><span aria-hidden="true">⌖</span> Chicago, Illinois</li><li><span aria-hidden="true">▥</span> <a href="http://chicagobooth.edu/phd">University of Chicago</a></li><li><span aria-hidden="true">✉</span> <a href="mailto:jyang21@chicagobooth.edu">jyang21@chicagobooth.edu</a></li></ul></aside>
<main id="main">{content}</main></div><footer><div class="footer-inner"><span>© 2026 Jingyuan (Angela) Yang</span></div></footer>{tracking}</body></html>'''
    target = OUT / slug
    target.mkdir(parents=True, exist_ok=True)
    (target / 'index.html').write_text(html, encoding='utf-8')
print('Built Homepage, Research, and Teaching in docs/')
print('Analytics: configured; confirm private dashboard access in Statcounter.' if analytics_ready else 'Analytics: awaiting your Statcounter project installation identifiers.')
