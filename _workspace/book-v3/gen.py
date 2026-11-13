# Free printable landing pages: one page per sheet, one PDF and one preview per sheet.
import json, subprocess, os, html
from pypdf import PdfReader, PdfWriter
SRC = '/mnt/user-data/outputs/house-rooms/'
OUT = '/mnt/user-data/outputs/printables-site/'
for d in ('', 'pdf', 'img'): os.makedirs(OUT + 'printables/' + d, exist_ok=True)
I = json.load(open('/tmp/claude-0/pk/pp/items.json'))
def esc(x): return html.escape(x, quote=True)
def build(it):
    s = it['slug']; r = PdfReader(SRC + it['src']); w = PdfWriter(); w.add_page(r.pages[it['page'] - 1])
    w.add_metadata({'/Title': it['title'] + ' · Piano Butler (free printable)'}); w.write(f'{OUT}printables/pdf/{s}.pdf')
    subprocess.run(['pdftoppm', '-jpeg', '-jpegopt', 'quality=86', '-r', '110', '-f', str(it['page']), '-l', str(it['page']), '-singlefile', SRC + it['src'], f'{OUT}printables/img/{s}'], check=True)
    same = [x for x in I if x['topic'] == it['topic'] and x['slug'] != s][:4]
    more = ''.join(f'<a class="mini" href="{x["slug"]}.html"><img src="img/{x["slug"]}.jpg" alt="" loading="lazy"><span>{esc(x["title"])}</span></a>' for x in same)
    steps = ''.join(f'<li>{esc(t)}</li>' for t in it['how'])
    facts = ''.join(f'<div><b>{k}</b><span>{esc(v)}</span></div>' for k, v in (('Level', it['level']), ('Players', it['players']), ('Time', it['time']), ('You need', it['need'])))
    txt = subprocess.run(['pdftotext', '-f', str(it['page']), '-l', str(it['page']), SRC + it['src'], '-'], capture_output=True, text=True).stdout
    ans = ' The answers are printed upside down at the bottom.' if 'Answer' in txt else ''
    url = f'https://thepianobutler.com/printables/{s}.html'
    ld = {"@context": "https://schema.org", "@type": "LearningResource", "name": it['title'], "description": it['desc'], "learningResourceType": "Worksheet", "educationalLevel": it['level'], "isAccessibleForFree": True, "inLanguage": "en", "url": url, "image": f'https://thepianobutler.com/printables/img/{s}.jpg', "publisher": {"@type": "Organization", "name": "Piano Butler", "url": "https://thepianobutler.com"}}
    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="color-scheme" content="light only">
<title>{esc(it['seo_title'])} | Piano Butler</title>
<meta name="description" content="{esc(it['desc'])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="noindex, nofollow"><!-- draft: switch to index, follow when Sohyun approves this sheet -->
<meta property="og:type" content="article"><meta property="og:url" content="{url}"><meta property="og:title" content="{esc(it['seo_title'])}"><meta property="og:description" content="{esc(it['desc'])}"><meta property="og:image" content="https://thepianobutler.com/printables/img/{s}.jpg"><meta property="og:site_name" content="Piano Butler"><meta name="twitter:card" content="summary_large_image">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-D232EW4QWF"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-D232EW4QWF');</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:wght@700;800;900&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(ld)}</script>
<style>
:root{{--cream:#ffffff;--paper:#fffefa;--navy:#26296b;--navy-soft:#4a4d86;--muted:#6d6f9c;--line:#cfcfe2;--coral:#e4572e;--cut:#8a6a2c}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--cream);color:var(--navy);font-family:Inter,-apple-system,'Segoe UI',sans-serif;line-height:1.55}}
a{{color:inherit}} a:focus-visible{{outline:2px solid var(--coral);outline-offset:3px;border-radius:6px}}
.wrap{{max-width:1040px;margin:0 auto;padding:24px 20px 64px}}
.crumb{{font-size:13px;color:var(--muted)}} .crumb a{{text-decoration:none}} .crumb a:hover{{color:var(--navy)}}
.top{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:34px;align-items:start;margin-top:18px}}
.sheet{{background:#fff;border:1px solid var(--line);border-radius:4px;box-shadow:0 6px 20px rgba(38,41,107,.08);overflow:hidden}} .sheet img{{display:block;width:100%;height:auto}}
.topic{{font-size:13px;font-weight:800;color:var(--coral);letter-spacing:.02em}}
h1,h2{{font-family:'Playfair Display',Georgia,serif;margin:0}} h1{{font-size:clamp(34px,5vw,52px);font-weight:900;line-height:1.05;margin:4px 0 12px}}
.lead{{font-size:17px;color:var(--navy-soft);margin:0 0 18px}}
.facts{{display:grid;grid-template-columns:1fr 1fr;border-top:1.5px solid var(--navy);border-bottom:1px solid var(--line);margin-bottom:20px}} .facts div{{padding:10px 4px;border-bottom:1px solid var(--line);display:flex;flex-direction:column}} .facts b{{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}} .facts span{{font-weight:700}}
.btn{{display:inline-flex;align-items:center;gap:8px;text-decoration:none;background:var(--coral);color:#fff;font-weight:800;font-size:16px;border-radius:999px;padding:12px 22px}} .btn:hover{{background:#c8461f}}
.small{{font-size:13px;color:var(--muted);margin-top:10px}}
.how{{margin-top:38px;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:34px}} .how h2{{font-size:28px;font-weight:900;margin-bottom:10px}} .how ol{{margin:0;padding-left:20px}} .how li{{margin:6px 0}}
.tip{{border:1.6px dashed var(--cut);border-radius:14px;padding:14px 16px;background:var(--paper);font-size:15px;color:var(--navy-soft)}} .tip b{{color:var(--navy)}}
.more{{margin-top:44px;border-top:1.5px solid var(--navy);padding-top:18px}} .more h2{{font-size:26px;font-weight:900;margin-bottom:14px}}
.minis{{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}} .mini{{text-decoration:none;display:flex;flex-direction:column;gap:6px;font-weight:700;font-size:14px}} .mini img{{width:100%;border:1px solid var(--line);border-radius:3px;background:#fff}}
.note{{margin-top:44px;padding-top:16px;border-top:1px solid var(--line);font-size:13px;color:var(--muted)}}
@media(max-width:760px){{.top,.how{{grid-template-columns:1fr}} .minis{{grid-template-columns:1fr 1fr}}}}
</style>
</head>
<body><div class="wrap">
<div class="crumb"><a href="../index.html">Piano Butler</a> › <a href="../printables.html">Free printables</a> › {esc(it['topic_name'])}</div>
<div class="top">
  <a class="sheet" href="pdf/{s}.pdf" aria-label="Open the printable PDF"><img src="img/{s}.jpg" alt="{esc(it['alt'])}" width="910" height="1286"></a>
  <div>
    <div class="topic">FREE PRINTABLE · {esc(it['topic_name']).upper()}</div>
    <h1>{esc(it['title'])}</h1>
    <p class="lead">{esc(it['lead'])}</p>
    <div class="facts">{facts}</div>
    <a class="btn" href="pdf/{s}.pdf" download>Download the PDF <span aria-hidden="true">↓</span></a>
    <p class="small">One A4 page. Free for personal and classroom use: please don’t sell or re-upload it, share this page’s link instead.{ans}</p>
  </div>
</div>
<div class="how"><div><h2>How to use it</h2><ol>{steps}</ol></div><div><h2>Make it easier or harder</h2><div class="tip"><b>Easier:</b> {esc(it['easier'])}<br><br><b>Harder:</b> {esc(it['harder'])}</div></div></div>
{f'<div class="more"><h2>More {esc(it["topic_name"].lower())} printables</h2><div class="minis">{more}</div></div>' if more else ''}
<div class="note">© Piano Butler. Made by a piano teacher for lessons and home practice. <a href="../printables.html">All free printables</a></div>
</div></body></html>'''
    open(f'{OUT}printables/{s}.html', 'w').write(page)
import sys
for it in I:
    if it['slug'] in sys.argv[1:] or 'all' in sys.argv[1:]: build(it); print('built', it['slug'])
