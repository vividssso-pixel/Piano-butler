import json, re, base64
from kb import keyboard, black_groups
SL = json.load(open('/tmp/claude-0/pk/ch2-lesson-svgs.json'))
SW = json.load(open('/tmp/claude-0/pk/ch2-work-svgs.json'))
N, C, G, CR, GOLD = '#26296b', '#e4572e', '#2e8a6e', '#fffdf7', '#c9a24f'
src = open('/tmp/claude-0/pk/book2.py').read()
base = src[src.index("css = f'''") + 10:src.index("'''\nfonts")].replace('{{', '{').replace('}}', '}').replace('{N}', N).replace('{C}', C).replace('{CR}', CR)

def dehalo(svg):
    def fix(m):
        a, body = m.group(1), m.group(2); sc = re.search(r'stroke="([^"]+)"', a).group(1)
        halo = re.sub(r'fill="[^"]+"', f'fill="{sc}"', a).replace(' paint-order="stroke"', '')
        top = re.sub(r' stroke(-width|-linejoin)?="[^"]*"', '', a).replace(' paint-order="stroke"', '')
        return f'<text{halo}>{body}</text><text{top}>{body}</text>'
    return re.sub(r'<text([^>]*paint-order="stroke"[^>]*)>([^<]*)</text>', fix, svg)
def sv(S, i, h=None, w=None):
    st = 'display:block;margin:0 auto;max-width:100%;' + (f'height:{h}px;' if h else '') + (f'width:{w}px;' if w else '')
    return dehalo(S[i]['html']).replace('width="100%" height="100%"', f'style="{st}"', 1)

def bowtie(col, knot, s=64):
    return (f'<svg viewBox="0 0 40 24" style="width:{s}px;height:{s * 0.6:.0f}px;display:block;margin:0 auto"><path d="M2 3 L18 12 L2 21 Z" fill="none" stroke="{col}" stroke-width="1.8" stroke-linejoin="round"/>'
            f'<path d="M38 3 L22 12 L38 21 Z" fill="none" stroke="{col}" stroke-width="1.8" stroke-linejoin="round"/><circle cx="20" cy="12" r="2.4" fill="{knot}"/></svg>')
def num(i): return f'<span class="nm">{i}</span>'
def page(inner, n, chk=True):
    foot = '<div class="sign"><span>Date <i></i></span><span>Practised <i class="s"></i> times</span><span>Checked <i></i></span></div>' if chk else ''
    return f'''<section class="pg"><div class="top"><span>PIANO BUTLER · WORKBOOK · LEVEL 0</span><span>CHAPTER 2 · KEYBOARD PATTERNS</span></div><div class="rule"></div>
<div class="body">{inner}</div>{foot}<div class="foot"><span>{n}</span></div></section>'''
def act(n, title, how, inner, ex=False):
    return f'<div class="act"><div class="ah"><span class="an">{n}</span><b>{title}</b></div><p class="how">{how}</p>{inner}</div>'

COVER = f'''<section class="pg cover"><div class="cframe">
<div class="ctop">PIANO BUTLER</div>
<div class="cmid">{bowtie(CR, C, 92)}<div class="cbook">Workbook</div><div class="clvl">Level 0</div><div class="cdiv"></div>
<div class="csub">The keyboard, the pulse, the names of the notes and the first steps in reading music.</div></div>
<div class="cown"><span>This book belongs to</span><i></i></div>
<div class="cfoot">Prepared by the Piano Butler · with the online lessons at thepianobutler.com</div></div></section>'''

SUM = page(f'''
<div class="kick">Chapter 2</div><h1 class="big">Keyboard Patterns</h1>
<p class="lead">The black keys are arranged in groups of two and three. This pattern repeats across the whole keyboard, and it is how you find every note.</p>
<div class="frame">{keyboard('C', 14, 26, 104, scale=1.5, brackets=[(a, b, ('2' if k == 2 else '3'), True) for a, b, k in black_groups('C', 14)])}</div>
<div class="h3">Key points</div>
<div class="row">{num(1)}<span>Black keys come in <b>groups of two</b> and <b>groups of three</b>, alternating.</span></div>
<div class="row">{num(2)}<span>Three white keys surround each group of two; four white keys surround each group of three. Seven white keys, then the pattern repeats.</span></div>
<div class="row">{num(3)}<span><b>Middle C</b> is the white key just left of the group of two nearest the centre. Notes go lower to the left and higher to the right.</span></div>
<div class="sumfoot"><div class="qr"><div class="qrbox">QR</div><div><b>The lesson, online</b><span>Animated examples, sound and the chapter quiz.<br>thepianobutler.com/drills · Chapter 2</span></div></div>
<div class="plan"><div class="h3 sm">Pages in this chapter</div>{''.join(f'<div class="pr"><span>{t}</span><span class="pp">p. {p}</span><span class="cb"></span></div>' for t, p in (('Groups of black keys', 3), ('White keys in each group', 4), ('The whole keyboard', 5), ('Fingers 2, 3, 4', 6), ('Review', 7)))}</div></div>
''', 2, chk=False)

def wh(start, dot, ans=''):
    ex = bool(ans)
    return f'<div class="wh{" ex" if ex else ""}">{"<span class=exl>Example</span>" if ex else ""}{keyboard(start, 7, 22, 70, scale=1.3, dots=(dot,))}<span class="box">{ans}</span></div>'
g16 = black_groups('C', 21)
P3 = page(f'''
<div class="kick">Step 1</div><h1>Groups of black keys</h1>
{act(1, 'Mark the groups', 'Draw a bracket under every group of black keys and write 2 or 3. The first one is done.', '<div class="frame plain">' + keyboard('C', 21, 22, 86, scale=1.3, brackets=[(a, b, ('2' if k == 2 else '3') if n == 0 else '', n == 0) for n, (a, b, k) in enumerate(g16)]) + '</div>')}
{act(2, 'Count', 'Colour each group of two in one colour and each group of three in another. Then count them.', '<div class="frame plain">' + keyboard('A', 24, 20, 80, scale=1.25) + '</div><div class="counts"><span>Groups of two <i></i></span><span>Groups of three <i></i></span></div>')}
{act(3, 'Higher or lower?', 'At the piano, someone plays two notes, one after the other. Was the second higher or lower? Ten rounds; tick each correct answer.', '<div class="tally"><span>Correct</span><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div>')}
''', 3)

P4 = page(f'''
<div class="kick">Step 2</div><h1>White keys in each group</h1>
{act(1, 'Shade the white keys', 'Shade the three white keys around every group of two in one colour, and the four around every group of three in another. The first group is done.', '<div class="frame plain">' + keyboard('C', 21, 22, 86, scale=1.3, shade={0: '#fde6dd', 1: '#fde6dd', 2: '#fde6dd'}) + '</div>')}
{act(2, 'Which group?', 'Is the marked white key beside a group of two or a group of three? Write 2 or 3.', '<div class="whg">' + wh('C', 1, '2') + wh('C', 5) + wh('C', 0) + wh('C', 3) + wh('C', 6) + wh('C', 2) + '</div>')}
''', 4)
css = base + f'''
.cover{{background:{N};padding:34px}} .cframe{{position:absolute;inset:34px;border:1.5px solid rgba(255,253,247,.75);outline:.6px solid rgba(255,253,247,.5);outline-offset:-8px;color:{CR};display:flex;flex-direction:column;align-items:center;padding:56px 60px 40px}}
.ctop{{font-size:12px;font-weight:800;letter-spacing:.42em;opacity:.85}} .cmid{{margin-top:auto;text-align:center}}
.cbook{{font-family:'Playfair Display',Georgia,serif;font-size:66px;font-weight:700;margin-top:26px;line-height:1}} .clvl{{font-family:'Playfair Display',Georgia,serif;font-style:italic;font-size:30px;color:#f4a9bb;margin-top:12px}}
.cdiv{{width:120px;height:5px;border-top:1px solid {CR};border-bottom:1px solid {CR};margin:26px auto;opacity:.7}} .csub{{font-size:14.5px;line-height:1.6;max-width:420px;margin:0 auto;opacity:.88}}
.cown{{margin-top:auto;width:100%;display:flex;align-items:flex-end;gap:12px;font-size:12px;letter-spacing:.06em;opacity:.85}} .cown i{{flex:1;border-bottom:1px solid rgba(255,253,247,.7);height:20px}}
.cfoot{{margin-top:26px;font-size:10.5px;letter-spacing:.12em;opacity:.6;text-transform:uppercase}}
.nm{{flex:none;width:22px;font:700 15px Georgia,serif;color:{C}}}
.sumfoot{{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:22px;border-top:1.5px solid {N};padding-top:14px}}
.qr{{display:flex;gap:12px;align-items:flex-start}} .qrbox{{flex:none;width:78px;height:78px;border:1.5px solid {N};display:flex;align-items:center;justify-content:center;font-size:11px;color:#8a8cb0;background:#fff}} .qr b{{display:block;font-family:'Playfair Display',Georgia,serif;font-size:16px}} .qr span{{font-size:12.5px;line-height:1.5;color:#3d4080}}
.h3.sm{{font-size:15px;margin:0 0 4px}} .pr{{display:flex;align-items:center;gap:10px;font-size:13.5px;border-bottom:.6px solid #e2ddd0;padding:4px 0}} .pr span:first-child{{flex:1}} .pp{{color:#8a8cb0;font-size:12px}}
.act{{border-top:1.5px solid {N};padding-top:9px;margin-bottom:16px}} .ah{{display:flex;align-items:center;gap:10px}} .an{{font:700 15px Georgia,serif;color:{C}}} .ah b{{font-family:'Playfair Display',Georgia,serif;font-size:19px}}
.how{{font-size:13.5px;line-height:1.5;color:#3d4080;margin:4px 0 8px}} .frame.plain{{outline:none;border:1px solid #d9d4c6;background:#fff;padding:12px}}
.counts{{display:flex;gap:30px;justify-content:flex-end;font-size:13.5px;margin-top:8px}} .counts i{{display:inline-block;width:42px;height:28px;border:1.5px solid {N};background:#fff;vertical-align:middle;margin-left:6px}}
.tally{{display:flex;align-items:center;gap:8px;font-size:13px;color:#3d4080}} .tally span{{margin-right:8px}} .tally i{{width:26px;height:26px;border:1.5px solid #c9cbe0;border-radius:50%;display:inline-block}}
.whg{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}} .wh{{position:relative;border:1px solid #d9d4c6;background:#fff;padding:20px 8px 10px;text-align:center}} .wh.ex{{border-color:{C};background:#fdf0ec}}
.exl{{position:absolute;left:8px;top:5px;font-size:10px;font-weight:900;letter-spacing:.14em;text-transform:uppercase;color:{C}}}
.wh .box{{display:inline-block;margin-top:8px;width:34px;height:30px;border:1.5px solid {N};background:#fff;font:700 18px Georgia,serif;color:{C};line-height:28px}}
.sign{{position:absolute;left:60px;right:60px;bottom:62px;display:flex;gap:24px;border-top:.8px solid #c9cbe0;padding-top:9px;font-size:11.5px;color:#6d6f9c}} .sign span{{display:flex;align-items:flex-end;gap:6px;flex:1}} .sign i{{flex:1;border-bottom:1px solid #b9bbd3;height:14px}} .sign i.s{{flex:none;width:34px}}
'''
FF = ''.join("@font-face{font-family:'Playfair Display';font-weight:700;font-style:%s;src:url(data:font/woff2;base64,%s) format('woff2')}" % (st, base64.b64encode(open('/tmp/claude-0/fnt/package/files/playfair-display-latin-700-%s.woff2' % st, 'rb').read()).decode()) for st in ('normal', 'italic'))
open('/mnt/user-data/outputs/house-rooms/workbook-ch2.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><style>{css}</style></head><body>{COVER}{SUM}{P3}{P4}</body></html>')
print('ok')
