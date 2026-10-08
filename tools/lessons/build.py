# Builds one public lesson guide page: lessons/<slug>.html
#   python3 tools/lessons/build.py <chapter-id>          (draft: yellow DRAFT marks allowed)
#   python3 tools/lessons/build.py <chapter-id> --final  (refuses while any DRAFT mark is left)
# The page body is hand-written in tools/lessons/src/<chapter-id>.html (one per chapter, checked by Sohyun);
# drawings are SVGs (the Lesson Book's own, from the art generator), in tools/lessons/svg/<chapter-id>/, placed with {{svg:name}};
# {{beats:1 2 3 - | 3 2 1 -}} draws a row of beat circles like the Lesson Book's tunes.
import html, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SITE = 'https://thepianobutler.com/'

ch = sys.argv[1]
final = '--final' in sys.argv
src = open(os.path.join(HERE, 'src', ch + '.html'), encoding='utf-8').read()
m = re.match(r'\s*<!--meta\s*(\{.*?\})\s*-->', src, re.S)
if not m:
    sys.exit('src/' + ch + '.html must start with a <!--meta {...} --> block')
meta = json.loads(m.group(1))
body = src[m.end():]


def svg(name):
    s = open(os.path.join(HERE, 'svg', ch, name + '.svg'), encoding='utf-8').read().strip()
    s = re.sub(r'<metadata>.*?</metadata>', '', s, flags=re.S)                  # file transfers can add a provenance blob; never ship it
    s = re.sub(r'\s+xmlns:c2pa="[^"]*"', '', s)
    s = re.sub(r'^<svg([^>]*?)\sstyle="[^"]*"', r'<svg\1', s, count=1)          # the app's inline size goes; CSS sizes it here
    s = re.sub(r'^<svg([^>]*?)\swidth="[^"]*"', r'<svg\1', s, count=1)
    s = re.sub(r'^<svg', '<svg class="pic" aria-hidden="true" focusable="false"', s, count=1)
    # many drawings share one page: give every id (hatch patterns etc.) the drawing's name, so two never clash
    s = re.sub(r'\bid="([^"]+)"', lambda x: 'id="%s-%s"' % (name, x.group(1)), s)
    s = re.sub(r'url\(#([^)]+)\)', lambda x: 'url(#%s-%s)' % (name, x.group(1)), s)
    s = re.sub(r'href="#([^"]+)"', lambda x: 'href="#%s-%s"' % (name, x.group(1)), s)
    return s


def beats(seq):
    # a row of beat circles like the Lesson Book's tunes: numbers are fingers, - holds for one more beat, | is a bar line
    xs = seq.split()
    say = ', '.join({'-': 'hold', '|': 'bar line'}.get(x, x) for x in xs)
    cell = lambda x: '<i class="h"></i>' if x == '-' else '<i>' + html.escape(x) + '</i>'
    bars = ['<span class="bt">' + ''.join(cell(x) for x in bar.split()) + '</span>' for bar in seq.split('|')]   # a bar never breaks across lines
    return '<span class="beats" role="img" aria-label="%s">%s</span>' % (html.escape(say), '<i class="bar"></i>'.join(bars))


body = re.sub(r'\{\{beats:([^}]+)\}\}', lambda x: beats(x.group(1)), body)
body = re.sub(r'\{\{svg:([\w-]+)\}\}', lambda x: svg(x.group(1)), body)
drafts = len(re.findall(r'class="[^"]*\bdraft\b', body))
if final and drafts:
    sys.exit('Not final: %d DRAFT mark(s) left in src/%s.html' % (drafts, ch))

esc = lambda s: html.escape(s, quote=True)
url = SITE + 'lessons/' + meta['slug'] + '.html'
ld = {
    '@context': 'https://schema.org', '@type': 'LearningResource', 'name': meta['h1'], 'headline': meta['title'],
    'description': meta['description'], 'url': url, 'inLanguage': 'en', 'isAccessibleForFree': True,
    'educationalLevel': 'Beginner', 'learningResourceType': 'Lesson guide', 'audience': {'@type': 'EducationalAudience', 'educationalRole': 'teacher'},
    'teaches': meta['teaches'], 'dateModified': meta['updated'],
    'publisher': {'@type': 'Organization', 'name': 'Piano Butler', 'url': SITE},
    'image': SITE + meta['image'],
}
if meta.get('author'):
    ld['author'] = {'@type': 'Person', 'name': meta['author']}

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="color-scheme" content="light only">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpath d='M3 6 L16 16 L3 26 Z' fill='none' stroke='%2326296b' stroke-width='2.4' stroke-linejoin='round'/%3E%3Cpath d='M29 6 L16 16 L29 26 Z' fill='none' stroke='%2326296b' stroke-width='2.4' stroke-linejoin='round'/%3E%3Ccircle cx='16' cy='16' r='2.6' fill='%23e4572e'/%3E%3C/svg%3E">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6523454944716812" crossorigin="anonymous"></script>
<title>{esc(meta['title'])}</title>
<meta name="description" content="{esc(meta['description'])}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(meta['title'])}">
<meta property="og:description" content="{esc(meta['description'])}">
<meta property="og:image" content="{SITE}{meta['image']}">
<meta property="og:locale" content="en_AU">
<meta property="og:site_name" content="Piano Butler">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(meta['title'])}">
<meta name="twitter:description" content="{esc(meta['description'])}">
<meta name="twitter:image" content="{SITE}{meta['image']}">
<meta name="author" content="{esc(meta.get('author', 'Piano Butler'))}">
<meta name="robots" content="{'index, follow' if final else 'noindex, nofollow'}">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-D232EW4QWF"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-D232EW4QWF');
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
  :root {{ --cream:#faf6ec; --paper:#fffefa; --navy:#26296b; --navy-soft:#4a4d86; --muted:#6d6f9c; --line:#e8e1d0; --coral:#e4572e; --good:#2f8a6c; --brass:#b8801f; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; background:var(--cream); color:var(--navy); font-family:Inter,-apple-system,'Segoe UI',sans-serif; line-height:1.6; font-size:16.5px; }}
  a {{ color:inherit; }}
  a:focus-visible, .btn:focus-visible {{ outline:2px solid var(--coral); outline-offset:3px; border-radius:6px; }}
  .wrap {{ max-width:860px; margin:0 auto; padding:26px 20px 72px; }}
  .crumbs {{ font-size:13px; color:var(--muted); margin-bottom:26px; }}
  .crumbs a {{ text-decoration:none; }}
  .crumbs a:hover {{ color:var(--navy); text-decoration:underline; }}
  h1, h2, h3 {{ font-family:'Playfair Display',Georgia,serif; letter-spacing:-0.005em; margin:0; line-height:1.15; }}
  .kicker {{ font-size:14px; font-weight:700; color:var(--coral); margin-bottom:6px; }}
  h1 {{ font-size:clamp(36px,6vw,56px); font-weight:900; }}
  .lead {{ font-size:19px; color:var(--navy-soft); margin:14px 0 0; max-width:36em; }}
  .byline {{ font-size:13px; color:var(--muted); margin-top:10px; }}
  .hero-pic {{ margin:18px 0 0; max-width:560px; }}
  .note {{ margin:30px 0 0; background:var(--paper); border:1px solid var(--line); border-left:4px solid var(--navy); border-radius:4px 12px 12px 4px; padding:16px 20px; }}
  .note .who {{ font-family:'Playfair Display',Georgia,serif; font-weight:800; font-size:19px; margin-bottom:4px; }}
  .note p {{ margin:6px 0 0; color:var(--navy-soft); }}
  section {{ margin-top:52px; }}
  h2 {{ font-size:clamp(28px,4vw,36px); font-weight:900; margin-bottom:10px; }}
  h3 {{ font-size:20px; font-weight:800; margin:0 0 4px; }}
  section > p {{ max-width:40em; color:var(--navy-soft); }}
  .pair {{ display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1fr); gap:26px; align-items:center; margin-top:14px; }}
  .fig {{ background:#fff; border:1px solid var(--line); border-radius:12px; padding:12px; }}
  .pic {{ display:block; width:100%; height:auto; }}
  ul.points {{ list-style:none; padding:0; margin:0; }}
  ul.points li {{ position:relative; padding:0 0 0 28px; margin:0 0 12px; }}
  ul.points li::before {{ content:''; position:absolute; left:4px; top:7px; width:12px; height:9px; border-radius:50%; background:var(--navy); transform:rotate(-20deg); }}
  ul.points b {{ color:var(--navy); }}
  .jump {{ display:flex; flex-wrap:wrap; gap:8px; margin:16px 0 0; }}
  .jump a {{ text-decoration:none; font-weight:700; font-size:14px; border:1.5px solid var(--navy); border-radius:999px; padding:6px 14px; background:var(--paper); }}
  .jump a:hover {{ background:var(--navy); color:#fff; }}
  .grid {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(min(100%, 240px), 1fr)); gap:16px; margin-top:16px; }}
  .grid.four {{ grid-template-columns:repeat(4, minmax(0,1fr)); }}
  .note.tip {{ margin:0; align-self:stretch; }}
  .card {{ background:var(--paper); border:1px solid var(--line); border-radius:12px; padding:12px 14px 14px; }}
  .card .pic {{ background:#fff; border-radius:8px; margin-bottom:8px; }}
  .card h3 {{ font-family:Inter,sans-serif; font-size:16px; font-weight:800; }}
  .card h3 .x {{ color:var(--coral); }}
  .card p {{ margin:4px 0 0; font-size:14.5px; color:var(--navy-soft); line-height:1.5; }}
  .card p b {{ color:var(--navy); }}
  ol.moves {{ padding:0; margin:16px 0 0; list-style:none; counter-reset:mv; display:grid; grid-template-columns:repeat(auto-fill, minmax(min(100%, 250px), 1fr)); gap:14px; }}
  ol.moves li {{ counter-increment:mv; background:var(--paper); border:1px solid var(--line); border-radius:12px; padding:12px 14px 12px 50px; position:relative; font-size:14.5px; color:var(--navy-soft); line-height:1.5; }}
  ol.moves li::before {{ content:counter(mv); position:absolute; left:14px; top:12px; width:24px; height:24px; border-radius:50%; background:var(--navy); color:#fff; font-weight:800; font-size:13px; display:flex; align-items:center; justify-content:center; }}
  ol.moves li b {{ display:block; color:var(--navy); font-size:15.5px; }}
  .grid.even .card .pic {{ height:170px; }}
  .beats {{ display:flex; flex-wrap:wrap; gap:4px; align-items:center; margin-top:8px; }}
  .beats i {{ width:24px; height:24px; border-radius:50%; border:1.8px solid var(--navy); background:#fff; color:var(--navy); font-style:normal; font-weight:800; font-size:12.5px; display:inline-flex; align-items:center; justify-content:center; }}
  .beats i.h {{ border:1.5px dashed #a99e85; background:transparent; }}
  .beats i.bar {{ width:1.6px; border:0; border-radius:0; background:var(--navy); opacity:.5; margin:0 3px; }}
  .beats .bt {{ display:inline-flex; gap:4px; }}
  ol.moves.tunes {{ grid-template-columns:1fr; gap:10px; }}
  ol.moves.tunes li {{ display:flex; flex-wrap:wrap; align-items:center; justify-content:space-between; gap:8px 18px; }}
  ol.moves.tunes .beats {{ margin-top:0; }}
  .hands {{ display:flex; gap:18px; justify-content:center; flex-wrap:wrap; }}
  .hands .pic {{ width:min(180px, 44%); }}
  .names {{ display:flex; flex-wrap:wrap; gap:8px; margin-top:12px; }}
  .names span {{ border:1.5px solid var(--navy); border-radius:999px; padding:3px 12px; font-size:14px; font-weight:700; background:var(--paper); }}
  .check {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(min(100%, 340px), 1fr)); gap:10px 26px; margin-top:12px; }}
  .check h3 {{ font-family:Inter,sans-serif; font-size:13px; font-weight:800; color:var(--coral); margin:10px 0 4px; }}
  .check ul {{ list-style:none; margin:0; padding:0; }}
  .check li {{ display:flex; gap:10px; align-items:flex-start; padding:6px 0; border-bottom:1px solid var(--line); font-size:15px; }}
  .check li::before {{ content:''; flex:0 0 auto; width:15px; height:15px; border:1.6px solid var(--navy); border-radius:3px; margin-top:4px; background:#fff; }}
  .sheet {{ display:grid; grid-template-columns:minmax(0,220px) minmax(0,1fr); gap:24px; align-items:center; background:var(--paper); border:1px solid var(--line); border-radius:14px; padding:18px; margin-top:14px; }}
  .sheet img {{ display:block; width:100%; height:auto; border:1px solid var(--line); border-radius:3px; background:#fff; }}
  .sheet p {{ margin:6px 0 12px; color:var(--navy-soft); }}
  .btn {{ display:inline-block; text-decoration:none; background:var(--coral); color:#fff; font-weight:700; font-size:15px; border-radius:999px; padding:9px 18px; }}
  .btn:hover {{ background:#c8461f; }}
  .btn.ghost {{ background:transparent; color:var(--navy); border:1.5px solid var(--navy); margin-left:8px; }}
  .btn.ghost:hover {{ background:var(--navy); color:#fff; }}
  .app {{ background:var(--navy); color:#fff; border-radius:16px; padding:24px 24px 26px; }}
  .app h2 {{ color:#fff; }}
  .app p {{ color:#d9dbf2; max-width:40em; margin:6px 0 16px; }}
  .faq h3 {{ font-family:Inter,sans-serif; font-size:17px; font-weight:800; margin-top:18px; }}
  .faq p {{ margin:4px 0 0; max-width:40em; color:var(--navy-soft); }}
  .next {{ margin-top:56px; padding-top:18px; border-top:1.5px solid var(--navy); display:flex; flex-wrap:wrap; justify-content:space-between; gap:12px 24px; align-items:baseline; }}
  .next a {{ font-weight:700; }}
  .next .lab {{ font-size:13px; color:var(--muted); display:block; }}
  footer {{ margin-top:28px; font-size:13px; color:var(--muted); }}
  footer a {{ color:var(--navy); font-weight:600; }}
  .draft {{ background:#fff1a8; outline:1.5px dashed #c9a400; outline-offset:2px; border-radius:3px; }}
  .draft::before {{ content:'DRAFT '; font-size:11px; font-weight:800; color:#8a6d00; letter-spacing:.04em; }}
  @media (max-width:700px) {{
    .pair, .sheet {{ grid-template-columns:1fr; }}
    .grid.four {{ grid-template-columns:repeat(2, minmax(0,1fr)); gap:10px; }}
    .grid.four .card {{ padding:8px 10px 10px; }}
    .grid.four .card p {{ font-size:13.5px; }}
    .sheet img {{ max-width:240px; }}
    .btn.ghost {{ margin:10px 0 0; }}
  }}
  @media print {{ .btn, .app, .crumbs, .jump {{ display:none; }} body {{ background:#fff; }} .card, .sheet, .pair, .fig, .note, ol.moves li, .check > div, .faq h3 {{ break-inside:avoid; }} h2, h3 {{ break-after:avoid; }} section {{ margin-top:34px; }} }}
</style>
</head>
<body>
<div class="wrap">
{body.strip()}
</div>
</body>
</html>
'''
out = os.path.join(ROOT, 'lessons', meta['slug'] + '.html')
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, 'w', encoding='utf-8').write(page)
print('lessons/%s.html  %d KB  %s  (%d draft mark%s)' % (meta['slug'], len(page.encode()) // 1024, 'FINAL' if final else 'draft', drafts, '' if drafts == 1 else 's'))
