# Split the Handbook and Workbook into one PDF per chapter, plus a card gallery like printables.html
import os, subprocess, html
from pypdf import PdfReader, PdfWriter
O = '/mnt/user-data/outputs/books-latest/'
SRC = {'hbP': '/mnt/user-data/outputs/handbook-part1-pitch.pdf', 'hbT': '/mnt/user-data/outputs/handbook-part2-time.pdf', 'wbP': '/mnt/user-data/outputs/workbook-pitch.pdf', 'wbT': '/mnt/user-data/outputs/workbook-time.pdf'}
# chapter: (part, n, title, blurb, handbook pages in its PDF (1-based), printed pp, workbook pages, workbook printed pp)
CH = [
 ('Pitch', 1, 'The keyboard', 'High and low, white-key names, the groups of two and three black keys, octaves.', 'hbP', [2], '22', 'wbP', [1, 2], '1–2'),
 ('Pitch', 2, 'The staff and the notes', 'Lines and spaces, treble and bass clefs, ledger lines, reading every note.', 'hbP', [3, 4], '23–24', 'wbP', [3, 4, 5], '3–5'),
 ('Pitch', 3, 'Sharps, flats and naturals', 'Accidentals, how long they last, two names for one key.', 'hbP', [5], '25', 'wbP', [6, 7], '6–7'),
 ('Pitch', 4, 'Tones, semitones and intervals', 'Counting the distance between notes: numbers and qualities.', 'hbP', [6], '26', 'wbP', [8, 9], '8–9'),
 ('Pitch', 5, 'Scales and keys', 'Major and minor scales, degree names, key signatures.', 'hbP', [7, 8], '27–28', 'wbP', [10, 11], '10–11'),
 ('Time', 1, 'Pulse and the bar', 'The steady beat, tempo, strong beats and bar lines.', 'hbT', [2], '36', 'wbT', [1, 2], '1–2'),
 ('Time', 2, 'Notes and rests', 'Every note value and its rest, and their other names.', 'hbT', [3], '37', 'wbT', [3, 4], '3–4'),
 ('Time', 3, 'How long is a note?', 'Adding values, dots and ties.', 'hbT', [4], '38', 'wbT', [5, 6], '5–6'),
 ('Time', 4, 'Time signatures', 'Simple, compound and irregular time.', 'hbT', [5, 6], '39–40', 'wbT', [7, 8], '7–8'),
 ('Time', 5, 'Rhythm', 'Grouping, upbeats, triplets, syncopation and swing.', 'hbT', [7, 8], '41–42', 'wbT', [9, 10], '9–10'),
]
EXTRA = [('hb', 'Pitch', 'Part I opener', 'hbP', [1], 'The map of Part I and its contents.'), ('hb', 'Time', 'Part II opener', 'hbT', [1], 'The map of Part II and its contents.'),
         ('wb', 'Pitch', 'Review, progress and answers', 'wbP', [12, 13, 14], 'A ten-minute review, the progress chart and every answer.'), ('wb', 'Time', 'Review, progress and answers', 'wbT', [11, 12, 13], 'A ten-minute review, the progress chart and every answer.')]
R = {k: PdfReader(v) for k, v in SRC.items()}
def slug(x): return ''.join(c if c.isalnum() else '-' for c in x.lower()).strip('-').replace('--', '-')
def cut(src, pages, path):
    os.makedirs(os.path.dirname(path), exist_ok=True); w = PdfWriter()
    for p in pages: w.add_page(R[src].pages[p - 1])
    w.write(path)
def thumb(src, page, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    subprocess.run(['pdftoppm', '-jpeg', '-jpegopt', 'quality=82', '-r', '60', '-f', str(page), '-l', str(page), '-singlefile', SRC[src], path[:-4]], check=True)
cards = {'hb': {'Pitch': [], 'Time': []}, 'wb': {'Pitch': [], 'Time': []}}
PARTN = {'Pitch': 'Part I · Pitch', 'Time': 'Part II · Time'}
for part, n, title, blurb, hs, hp, hpp, ws, wp, wpp in CH:
    base = f'{"1" if part == "Pitch" else "2"}-{n}-{slug(title)}'
    hf = f'1 Handbook/{PARTN[part].replace(" · ", " ")}/handbook-{base}.pdf'; wf = f'2 Workbook/{part}/workbook-{base}.pdf'
    cut(hs, hp, O + hf); cut(ws, wp, O + wf); thumb(hs, hp[0], O + f'_thumbs/hb-{base}.jpg'); thumb(ws, wp[0], O + f'_thumbs/wb-{base}.jpg')
    cards['hb'][part].append((f'Chapter {n} · {part}', title, blurb, hf, f'_thumbs/hb-{base}.jpg', f'p. {hpp}' if '–' not in hpp else f'pp. {hpp}', len(hp)))
    cards['wb'][part].append((f'Chapter {n} · {part}', title, blurb, wf, f'_thumbs/wb-{base}.jpg', f'Workbook {part} pp. {wpp}', len(wp)))
for kind, part, title, src, pages, blurb in EXTRA:
    base = f'{"1" if part == "Pitch" else "2"}-0-{slug(title)}' if kind == 'hb' else f'{"1" if part == "Pitch" else "2"}-9-{slug(title)}'
    f = (f'1 Handbook/{PARTN[part].replace(" · ", " ")}/handbook-{base}.pdf' if kind == 'hb' else f'2 Workbook/{part}/workbook-{base}.pdf')
    cut(src, pages, O + f); thumb(src, pages[0], O + f'_thumbs/{kind}-{base}.jpg')
    c = (part, title, blurb, f, f'_thumbs/{kind}-{base}.jpg', '', len(pages))
    (cards[kind][part].insert(0, c) if kind == 'hb' else cards[kind][part].append(c))
E = lambda x: html.escape(x, quote=True)
def card(c):
    lab, title, blurb, f, th, pp, n = c
    return f'''<div class="card"><a class="sheet" href="{E(f)}" target="_blank"><img src="{E(th)}" alt="" loading="lazy"></a><div class="txt"><div class="topic">{E(lab)}</div><h3>{E(title)}</h3><p>{E(blurb)}</p>
<div class="foot"><span class="meta">{n} {"page" if n == 1 else "pages"}{" · " + E(pp) if pp else ""}</span><a class="btn" href="{E(f)}" target="_blank">Open</a></div></div></div>'''
def sec(kind, name, sub):
    out = f'<section class="sec"><div class="sec-h"><h2>{name}</h2><span class="count">{sub}</span></div>'
    for part in ('Pitch', 'Time'):
        out += f'<div class="stage"><div class="stage-h">{PARTN[part] if kind == "hb" else part}</div><div class="grid">' + ''.join(card(c) for c in cards[kind][part]) + '</div></div>'
    return out + '</section>'
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Books, chapter by chapter</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=Playfair+Display:wght@800;900&display=swap" rel="stylesheet">
<style>:root{{--cream:#faf6ec;--paper:#fffefa;--navy:#26296b;--navy-soft:#4a4d86;--muted:#6d6f9c;--line:#e8e1d0;--coral:#e4572e;--cut:#8a6a2c}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--cream);color:var(--navy);font-family:Inter,-apple-system,sans-serif;line-height:1.55}}
.wrap{{max-width:1100px;margin:0 auto;padding:28px 20px 72px}} h1,h2,h3{{font-family:'Playfair Display',Georgia,serif;margin:0}}
h1{{font-size:clamp(38px,6vw,60px);font-weight:900;line-height:1.02}} .lead{{font-size:17px;color:var(--navy-soft);margin:12px 0 0;max-width:40em}}
.jump{{display:flex;gap:10px;margin:20px 0 0;flex-wrap:wrap}} .jump a{{text-decoration:none;font-weight:700;font-size:14px;border:1.5px solid var(--navy);border-radius:999px;padding:7px 14px;background:var(--paper);color:var(--navy)}}
.sec{{margin-top:46px}} .sec-h{{display:flex;align-items:baseline;justify-content:space-between;gap:12px;flex-wrap:wrap;border-bottom:1.5px solid var(--navy);padding-bottom:8px}} .sec-h h2{{font-size:clamp(28px,4vw,38px);font-weight:900}} .count{{font-size:14px;color:var(--muted);font-weight:600}}
.stage{{margin-top:26px}} .stage-h{{font-family:'Playfair Display',serif;font-size:24px;font-weight:800;margin-bottom:14px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(100%,230px),1fr));gap:26px 22px}} .card{{display:flex;flex-direction:column}}
.sheet{{display:block;background:#fff;border:1px solid var(--line);border-radius:4px;overflow:hidden;transition:transform .15s}} .sheet:hover{{transform:translateY(-3px)}} .sheet img{{display:block;width:100%;height:auto}}
.txt{{padding:12px 2px 0;display:flex;flex-direction:column;flex:1}} .topic{{font-size:12.5px;font-weight:700;color:var(--coral)}} h3{{font-size:20px;font-weight:800;margin:2px 0 6px;line-height:1.2}} .card p{{font-size:14px;color:var(--navy-soft);margin:0 0 8px}}
.foot{{margin-top:auto;display:flex;align-items:center;justify-content:space-between;gap:10px}} .meta{{font-size:12.5px;color:var(--muted);font-weight:600}} .btn{{text-decoration:none;background:var(--coral);color:#fff;font-weight:700;font-size:14px;border-radius:999px;padding:7px 15px}}
</style></head><body><div class="wrap"><h1>The books, chapter by chapter</h1><p class="lead">Drafts. Every chapter of The Piano Butler Handbook and Workbook as its own PDF. The whole books come later.</p>
<div class="jump"><a href="#hb">The Handbook</a><a href="#wb">The Workbook</a><a href="3 Activities and games/rhythm-activities-games.pdf" target="_blank">Rhythm activities and games</a><a href="3 Activities and games/pitch-games.pdf" target="_blank">Pitch games</a></div>
<div id="hb">{sec("hb", "The Handbook", "Part I and Part II, one PDF per chapter")}</div><div id="wb">{sec("wb", "The Workbook", "Learn and Use pages per chapter")}</div></div></body></html>'''
open(O + 'index.html', 'w').write(page)
print(sum(len(v) for k in cards.values() for v in k.values()), 'cards')
