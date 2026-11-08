# The Handbook check, printed (her 8 Nov): 'Where do I start?' Three questions per chapter; the score says skip, skim or study.
import json, html as _h
exec(open('/tmp/claude-0/pk/book10.py').read())   # fonts, css, helpers (rewrites the Time draft, harmless)
BANK = json.load(open('/tmp/claude-0/pk/checkbank.json'))
L3 = 'ABC'
def top(): return '<div class="top"><span>THE PIANO BUTLER HANDBOOK</span><span>WHERE DO I START?</span></div><div class="rule"></div>'
def sec(inner, n=0, end=False): return f'<section class="pg"{" data-end=\"1\"" if end else ""}>{top()}<div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'
LEG = ('<div class="leg3">'
       '<div class="lg g"><b>3 right</b><span>Skip it</span><i>You know this chapter. Glance at its secret and move on.</i></div>'
       '<div class="lg y"><b>2 right</b><span>Skim it</span><i>Read the chapter’s opening picture and Examples; check the one you missed.</i></div>'
       '<div class="lg r"><b>0 or 1 right</b><span>Study it</span><i>Start here: read the whole chapter and do its workbook pages.</i></div></div>')
def qblock(c, sample=False):
    qs = ''.join(f'<div class="cq"><span class="qn">{i + 1}</span><span class="qt">{_h.escape(q["q"])}</span><span class="qo">' + ''.join(f'<span class="op{" pick" if sample and j == q["a"] else ""}"><b>{L3[j]}</b>{_h.escape(o)}</span>' for j, o in enumerate(q['o'])) + '</span></div>' for i, q in enumerate(c['qs']))
    return (f'<div class="cb"><div class="ch"><span class="ck">{c["key"][0]}{c["key"][1:]}</span><b>{_h.escape(c["title"])}</b><span class="hp">Handbook p.&#8202;{c["page"]}</span></div>{qs}'
            f'<div class="sc"><span>Right:</span><span class="ab">{"3" if sample else ""}</span><span class="of">/ 3</span><span class="arr">3 skip · 2 skim · 0–1 study p.&#8202;{c["page"]}</span></div></div>')
SAMPLE = {'key': 'Ex', 'title': 'Sample chapter: the musical alphabet', 'page': 22, 'qs': [{'q': 'After G, the musical alphabet goes on with…', 'o': ['H', 'A', 'C'], 'a': 1}, {'q': 'How many different letter names are there?', 'o': ['7', '8', '12'], 'a': 0}, {'q': 'Going down from C, the next letter is…', 'o': ['D', 'A', 'B'], 'a': 2}]}
INTRO = sec(f'''<div class="kick">The Handbook check</div><h1>Where do I start?</h1>
<p class="lead">The Handbook is not a course you must read from page 1. It is a map of everything a pianist reads, hears and plays. This check finds the chapters you already know and the ones to study, so you start exactly where you are.</p>
{h3('How it works')}
<div class="steps3"><div><span class="rn">1</span><b>Choose a part</b><span>New to music? Start with Part I. Otherwise begin with the part you need, or do all eight, one part at a time (about 5 minutes each).</span></div>
<div><span class="rn">2</span><b>Answer three questions</b><span>for each chapter: circle A, B or C. No book, no piano, no guessing: if you don’t know, leave it.</span></div>
<div><span class="rn">3</span><b>Mark and map it</b><span>Check with the answers on the last pages, write your score, then colour the chapter on your map (page {{MAP}}).</span></div></div>
{h3('What your score means')}
{LEG}
{h3('An example')}
{qblock(SAMPLE, True)}
<div class="note2" style="margin-top:8px"><b>For teachers</b><p class="sm" style="margin:2px 0 0">Give one part as a ten-minute warm-up at the first lesson. The map shows at a glance which chapters to set, and repeating the check each term shows progress chapter by chapter.</p></div>
<p class="sm">Online: the same check marks itself and draws your map: Library › Handbook check.</p>''', 1)
POOL = ''.join((f'<h3 class="ph" data-part="1">{c["part"]}</h3>' if i == 0 or BANK[i - 1]['part'] != c['part'] else '') + qblock(c) for i, c in enumerate(BANK))
ANS = '<div class="ansg">' + ''.join(f'<div><b>{c["key"]}</b>' + ' '.join(f'{i + 1}{L3[q["a"]]}' for i, q in enumerate(c['qs'])) + '</div>' for c in BANK) + '</div>'
def mapgrid():
    o = ''
    for part in dict.fromkeys(c['part'] for c in BANK):
        cs = [c for c in BANK if c['part'] == part]
        o += f'<div class="mp"><div class="mph">{part}</div>' + ''.join(f'<div class="mc"><span class="mk">{c["key"]}</span><span class="mt">{_h.escape(c["title"])}</span><span class="mpg">p.&#8202;{c["page"]}</span><span class="dots"><i class="g"></i><i class="y"></i><i class="r"></i></span></div>' for c in cs) + '</div>'
    return f'<div class="mapg">{o}</div>'
CSS2 = '''
.leg3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:6px 0 10px} .lg{border-radius:8px;padding:9px 12px;display:flex;flex-direction:column;gap:2px} .lg b{font-size:13px;letter-spacing:.06em;text-transform:uppercase} .lg span{font-family:PF,serif;font-weight:700;font-size:22px;color:#26296b} .lg i{font-style:normal;font-size:13.5px;line-height:1.4;color:#3d4080}
.lg.g{background:#e3f1e6} .lg.g b{color:#2f7d4a} .lg.y{background:#fdf1d6} .lg.y b{color:#a56a00} .lg.r{background:#fde3d8} .lg.r b{color:#e4572e}
.steps3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px} .steps3>div{display:flex;flex-direction:column;gap:3px;font-size:14px;line-height:1.45;color:#3d4080} .steps3 b{font-size:15px;color:#26296b} .rn{display:inline-flex;width:24px;height:24px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;align-items:center;justify-content:center;font-size:13px}
.ph{margin:4px 0 4px!important;font-size:18px;color:#e4572e;border-bottom:2px solid #e4572e;padding-bottom:3px}
.cb{border:1.5px solid #e3e1ee;border-radius:8px;padding:7px 12px 6px;margin:0 0 8px;break-inside:avoid;background:#fff}
.ch{display:flex;align-items:baseline;gap:8px;border-bottom:1px solid #eeece4;padding-bottom:3px;margin-bottom:3px} .ch b{font-size:15.5px;color:#26296b} .ck{font-weight:700;font-size:12px;color:#fff;background:#26296b;border-radius:4px;padding:1px 6px} .hp{margin-left:auto;font-size:12.5px;color:#6d6f9c;font-weight:700}
.cq{display:grid;grid-template-columns:18px 1fr;column-gap:6px;font-size:14px;line-height:1.35;padding:3px 0} .qn{font-weight:700;color:#e4572e} .qt{color:#26296b} .qo{grid-column:2;display:flex;flex-wrap:wrap;gap:2px 18px;margin-top:2px}
.op{display:inline-flex;align-items:center;gap:6px;color:#3d4080} .op b{display:inline-flex;width:20px;height:20px;border-radius:50%;border:1.5px solid #9a9cc4;align-items:center;justify-content:center;font-size:11.5px;color:#26296b}
.op.pick b{border-color:#e4572e;background:#e4572e;color:#fff}
.sc{display:flex;align-items:center;gap:8px;margin-top:4px;padding-top:4px;border-top:1px dashed #e3e1ee;font-size:13.5px;color:#26296b} .sc .ab{width:30px;height:24px;border:1.5px solid #26296b;border-radius:4px;display:inline-flex;align-items:center;justify-content:center;font-weight:700;color:#e4572e} .sc .arr{margin-left:auto;font-size:12.5px;color:#6d6f9c;font-weight:700}
.ansg{display:grid;grid-template-columns:repeat(4,1fr);gap:4px 14px;font-size:14px;margin-top:6px} .ansg div{border-bottom:.6px solid #e2ddd0;padding:3px 0;color:#3d4080;word-spacing:4px} .ansg b{display:inline-block;width:30px;color:#26296b;word-spacing:0}
.mapg{display:grid;grid-template-columns:1fr 1fr;gap:6px 18px} .mp{break-inside:avoid} .mph{font-weight:700;font-size:13px;color:#e4572e;letter-spacing:.04em;margin:4px 0 2px;border-bottom:1.5px solid #e4572e}
.mc{display:grid;grid-template-columns:28px 1fr auto 70px;align-items:center;gap:6px;font-size:12.5px;padding:2px 0;border-bottom:.6px solid #eeece4} .mk{font-weight:700;color:#26296b} .mt{color:#3d4080} .mpg{color:#6d6f9c;font-size:11.5px} .dots{display:flex;gap:5px;justify-content:flex-end} .dots i{width:14px;height:14px;border-radius:50%;border:1.5px solid} .dots .g{border-color:#2f7d4a} .dots .y{border-color:#d29b2a} .dots .r{border-color:#e4572e}
.mkey{display:flex;gap:18px;font-size:13px;color:#3d4080;margin:4px 0 8px} .mkey span{display:inline-flex;align-items:center;gap:6px} .mkey i{width:14px;height:14px;border-radius:50%;border:1.5px solid;display:inline-block}
'''
PAGJS = '''<script>
// Lay the chapter blocks into pages: each page is filled block by block; a part heading never ends a page.
(async function () { try { await document.fonts.ready; } catch (e) {}
  const pool = document.getElementById('pool'), tpl = document.getElementById('tpl'), anchor = document.getElementById('after');
  let page = null, body = null;
  const fresh = () => { page = tpl.content.firstElementChild.cloneNode(true); anchor.parentNode.insertBefore(page, anchor); body = page.querySelector('.body'); };
  const over = () => { const lim = page.querySelector('.foot').getBoundingClientRect().top - 24; let m = 0; [...body.children].forEach(c => m = Math.max(m, c.getBoundingClientRect().bottom)); return m > lim; };
  fresh();
  [...pool.children].forEach(el => { body.appendChild(el); if (over() && body.children.length > 2) { body.removeChild(el); const last = body.lastElementChild; const carry = last && last.classList.contains('ph') ? last : null; if (carry) body.removeChild(carry); fresh(); if (carry) body.appendChild(carry); body.appendChild(el); } });
  pool.remove(); tpl.remove();
  document.querySelectorAll('section.pg').forEach((s, i) => { s.querySelector('.foot span').textContent = i + 1; });
  const map = [...document.querySelectorAll('section.pg')].findIndex(s => s.querySelector('.mapg')) + 1;
  document.querySelectorAll('.mapref').forEach(e => e.textContent = map);
  document.body.dataset.flowed = '1';
})();
</script>'''
INTRO = INTRO.replace('page {MAP}', 'page <span class="mapref"></span>')
END = (sec(f'<div class="kick">The Handbook check</div><h1>Answers</h1><p class="lead">One line per chapter: question number and letter. Count your right answers and write the score in the chapter’s box.</p>{ANS}', 0, True)
       + sec(f'<div class="kick">The Handbook check</div><h1>My map</h1><p class="lead">Colour one circle for each chapter you check. Green chapters you can skip; yellow ones skim; red ones are where you start. Check again in a few months and watch the map turn green.</p><div class="mkey"><span><i style="border-color:#2f7d4a"></i>skip it (3)</span><span><i style="border-color:#d29b2a"></i>skim it (2)</span><span><i style="border-color:#e4572e"></i>study it (0–1)</span></div>{mapgrid()}', 0, True))
html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{CSS2}</style></head><body>{INTRO}'
        f'<template id="tpl">{sec("", 0)}</template><div id="pool" style="position:absolute;left:-9999px;width:700px">{POOL}</div><div id="after"></div>{END}{PAGJS}</body></html>')
open('/mnt/user-data/outputs/house-rooms/handbook-check.html', 'w').write(html)
print('ok check booklet')
