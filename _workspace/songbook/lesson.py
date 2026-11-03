# The Piano Butler Lesson Book (song-led), Level 0: one lesson from one song's data. The look is the Handbook's
# (book-v3/book10.py): the same type, colours, running head and page frame; bigger type for children.
# Usage: python3 lesson.py song.json snippets.json out.html
import json, base64, sys
SONG, V = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
N, C, MUTE, HELD = '#26296b', '#e4572e', '#6d6f9c', '#9a9cc4'
FD = 'node_modules/@fontsource/'
def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()
FF = (f"@font-face{{font-family:'AH';font-weight:400;src:url(data:font/woff2;base64,{b64(FD + 'atkinson-hyperlegible/files/atkinson-hyperlegible-latin-400-normal.woff2')}) format('woff2')}}"
      f"@font-face{{font-family:'AH';font-weight:700;src:url(data:font/woff2;base64,{b64(FD + 'atkinson-hyperlegible/files/atkinson-hyperlegible-latin-700-normal.woff2')}) format('woff2')}}"
      f"@font-face{{font-family:'PF';font-weight:700;src:url(data:font/woff2;base64,{b64(FD + 'playfair-display/files/playfair-display-latin-700-normal.woff2')}) format('woff2')}}")
LESSON, LEVEL = 5, 'Level 0'
ROOM = SONG.get('room', 'note-values')   # the drills room this lesson goes with (the QR opens it; drills needs ?room=)
import qrcode, qrcode.image.svg
def qr(url):   # a plain navy QR, drawn as one SVG path
    q = qrcode.QRCode(border=1, error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m); d = ''.join(f'M{x},{y}h1v1h-1z' for y, r in enumerate(m) for x, v in enumerate(r) if v)
    return f'<svg viewBox="0 0 {n} {n}" style="width:96px;height:96px;display:block" shape-rendering="crispEdges"><path d="{d}" fill="{N}"/></svg>'
URL = 'https://thepianobutler.com/drills.html?room=' + ROOM
def page(inner, n): return f'<section class="pg"><div class="top"><span>THE PIANO BUTLER LESSON BOOK · {LEVEL.upper()}</span><span>LESSON {LESSON} · {SONG["title"].upper()}</span></div><div class="rule"></div><div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'
def mus(k, cls=''): return f'<div class="mus {cls}" data-snip="{k}">{V[k]}</div>'
def part(n, t, how): return f'<div class="ph"><span class="pn">{n}</span><h2>{t}</h2></div><p class="how">{how}</p>'
def ticks(items, h=False): return f'<div class="ticks{" h" if h else ""}">' + ''.join(f'<span class="tk"><span class="bx"></span>{t}</span>' for t in items) + '</div>'
def way(n, t, stars, how, a, b):
    gs = ' gs' if n > 1 else ''
    return f'<div class="way{gs}"><div class="wh"><span class="wn">Way {n}</span><b>{t}</b><span class="st">{"★" * stars}{"☆" * (4 - stars)}</span></div><p class="how">{how}</p>{mus(a)}{mus(b)}</div>'

# the keyboard in C position: five white keys under the right hand, the song's notes lit, the finger numbers on them
L7 = 'cdefgab'
def trp(p, k): i = L7.index(p[0]) + k; return L7[i % 7] + str(int(p[1:]) + i // 7)
# a keyboard from middle C: the five white keys under the right hand (from `start`), the song's notes lit, the fingers on
# them; `sharp` marks the key's black key in coral, named above it
def kb(start=0, tr=0, sharp=None, width=380):
    used = {trp(p, tr)[0] for bar in SONG['bars'] for p, *_ in bar}; W, H, w = 420, 150, 42
    whites = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e']; out = ''; top = 24 if sharp is not None else 0
    for i, l in enumerate(whites):
        inpos = start <= i < start + 5; lit = inpos and l in used
        out += f'<rect x="{i * w}" y="0" width="{w}" height="{H}" rx="3" fill="{"#fbe3da" if lit else "#fff"}" stroke="{N}" stroke-width="1.5"/>'
        out += f'<text x="{i * w + w / 2}" y="{H - 12}" text-anchor="middle" font-family="AH" font-weight="700" font-size="17" fill="{N}">{l.upper()}</text>'
        if inpos: f = i - start + 1; out += f'<circle cx="{i * w + w / 2}" cy="{H - 48}" r="13" fill="{C if lit else "#fff"}" stroke="{C}" stroke-width="1.8"/><text x="{i * w + w / 2}" y="{H - 42.5}" text-anchor="middle" font-family="AH" font-weight="700" font-size="15" fill="{"#fff" if lit else C}">{f}</text>'
    for i in (0, 1, 3, 4, 5, 7, 8):
        out += f'<rect x="{(i + 1) * w - 13}" y="0" width="26" height="{H * 0.6}" rx="2" fill="{C if i == sharp else N}"/>'
        if i == sharp: out += f'<text x="{(i + 1) * w}" y="-8" text-anchor="middle" font-family="AH" font-weight="700" font-size="15" fill="{C}">F♯</text>'
    out += f'<text x="{w / 2}" y="{H + 20}" text-anchor="middle" font-family="AH" font-weight="700" font-size="12" fill="{MUTE}">middle C</text>'
    return f'<svg viewBox="-2 {-2 - top} {W + 4} {H + 28 + top}" style="width:100%;max-width:{width}px;display:block;margin:0 auto">{out}</svg>'

LHF = {'c3': 5, 'd3': 4, 'e3': 3, 'f3': 2, 'g3': 1}
def lhkb(way, ch):
    notes = [p for ps, d, f in SONG['lh'][way][ch] for p in ps]; W, H, w = 5 * 34, 108, 34; out = ''
    for i, l in enumerate('cdefg'):
        p = l + '3'; lit = p in notes
        out += f'<rect x="{i * w}" y="0" width="{w}" height="{H}" rx="2" fill="{"#fbe3da" if lit else "#fff"}" stroke="{N}" stroke-width="1.4"/>'
        out += f'<text x="{i * w + w / 2}" y="{H - 8}" text-anchor="middle" font-family="AH" font-weight="700" font-size="13" fill="{N}">{l.upper()}</text>'
        if lit: out += f'<circle cx="{i * w + w / 2}" cy="{H - 36}" r="11" fill="{C}"/><text x="{i * w + w / 2}" y="{H - 31.5}" text-anchor="middle" font-family="AH" font-weight="700" font-size="13" fill="#fff">{LHF[p]}</text>'
    for i in (0, 1, 3): out += f'<rect x="{(i + 1) * w - 10}" y="0" width="20" height="{H * 0.58}" rx="2" fill="{N}"/>'
    return f'<div class="lk"><b>{ch}</b><svg viewBox="-1 -1 {W + 2} {H + 2}" style="width:130px;display:block">{out}</svg></div>'
def lead(n, t, stars, how, way):
    keys = ''.join(lhkb(way, ch) for ch in ['C', 'G'])
    return f'<div class="way"><div class="wh"><span class="wn">Way {n}</span><b>{t}</b><span class="st">{"★" * stars}{"☆" * (4 - stars)}</span></div><div class="lw"><p class="how">{how}</p><div class="lks"><span class="lkh">Left hand</span>{keys}</div></div>{mus("L" + str(n) + "a")}{mus("L" + str(n) + "b")}</div>'

chips = ''.join(f'<span class="chip">{t}</span>' for t in ['crotchet, minim, semibreve', 'C position, then G', 'steps and a skip'])
P1 = page(f'''<div class="kick">Lesson {LESSON}</div><h1>{SONG["title"]}</h1>
<p class="lead">A rhyme by Sarah Josepha Hale, first printed in Boston in 1830, about a lamb that followed a girl to school. We sing it to the tune of <i>Merrily we roll along</i>.</p>
<div class="chips"><span class="cl">In this song</span>{chips}</div>
{part(1, 'Listen and sing', 'Listen first, pointing to each note as it sounds. Then sing.')}
{mus('sing1')}{mus('sing2')}
<div class="row2"><div>{ticks(['Listened and pointed', 'Sang it with the words', 'Sang it on the letter names'])}</div><div class="qr">{qr(URL)}<span>Scan me</span></div></div>
{part(2, 'Say and clap', 'Say the words in time, then clap them and count. Clap on the coral numbers; hold through the grey ones.')}
{mus('rhy1')}{mus('rhy2')}
{ticks(['Said it in time', 'Clapped and counted'], True)}''', 1)

P2 = page(f'''{part(3, 'Read it', 'The song uses four notes of C position. Find them on the keys, then on the staff.')}
<div class="kbw">{kb()}<p class="cap">C position: the right-hand thumb on middle C. The song’s four notes are lit.</p></div>
<p class="q"><b>Write the letter names</b> of bars 1 to 4 in the boxes. The first one is done.</p>{mus('read1')}
<div class="sk"><p class="q"><b>In bar 4 the tune goes from E to G.</b> Is that a step or a skip?</p><div class="ticks h"><span class="tk"><span class="bx"></span>a step</span><span class="tk"><span class="bx"></span>a skip</span></div></div>
{part(4, 'Play it four ways', 'Start with Way 1. Each way adds a little more for the left hand; your teacher tells you which way is yours this week.')}
<div class="tog"><span class="tgh">Play together</span><span>Two players, one song: one plays Way 1, the other the left hand of Way 4. Then swap.</span></div>
{way(1, 'The tune', 1, 'Right hand alone. The numbers are your fingers.', 'w1a', 'w1b')}''', 2)

P3 = page(f'''{lead(2, 'One long note', 2, 'The letters above the staff are the chords. Under each bar, your left hand holds one note all bar long: C with finger 5 for C, G with finger 1 for G.', 'way2')}
{lead(3, 'Two notes together', 3, 'Same chords; now two notes together on beats 1 and 3 (the dots): C and G for C, D and G for G.', 'way3')}''', 3)

P4 = page(f'''{lead(4, 'A moving bass', 4, 'Same chords; now one note a beat. The numbers are your fingers: 5 1 3 1 for C, 4 1 2 1 for G.', 'way4')}
{part(5, 'Move it to G', 'Same fingers, new home: thumb on G, and the tune moves with your hand. The chords move too: C becomes G, G becomes D.')}
<div class="mv"><div>{kb(4, 4, 3, 300)}</div><p class="cap2"><b>G position.</b> The key of G has one black key, F♯: the sharp sign at the start of the staff. This tune never needs it.</p></div>
{mus('g1', 'gl')}
<div class="chk"><div class="ch">6 · Check</div><div class="cgrid">
<div>{ticks(['I can sing it with the words', 'I can clap and count it', 'I can name its notes'])}</div>
<div>{''.join(f'<div class="wrow"><span class="wk">In {k}</span><div class="ticks h">' + ''.join(f'<span class="tk"><span class="bx"></span>Way {i}</span>' for i in range(1, 5)) + '</div></div>' for k in 'CG')}
<div class="tch"><span>Teacher</span><span class="tk"><span class="bx"></span>Pass</span><span class="tk"><span class="bx"></span>Not yet</span></div></div></div></div>''', 4)

css = f'''@page {{ size: A4; margin: 0 }} *{{box-sizing:border-box}} body{{margin:0;background:#e9e4d8;font-family:'AH',Arial,sans-serif;color:{N}}}
.pg{{width:794px;height:1123px;background:#fff;margin:0 auto 24px;position:relative;overflow:hidden;padding:42px 58px 0;page-break-after:always}}
.top{{display:flex;justify-content:space-between;font-size:9.5px;font-weight:700;letter-spacing:.16em;color:#8a8cb0}} .rule{{height:5px;border-top:1.5px solid {N};border-bottom:.6px solid {N};margin:7px 0 18px}}
.body{{height:965px;overflow:hidden}}
.foot{{position:absolute;left:0;right:0;bottom:30px;text-align:center}} .foot span{{display:inline-block;color:{N};font:700 13px 'AH',Arial;letter-spacing:.08em}}
.kick{{font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:{C}}} h1{{font-family:'PF',Georgia,serif;font-size:40px;line-height:1.1;margin:3px 0 8px;font-weight:700}}
.lead{{font-size:17px;line-height:1.5;margin:0 0 8px}} p{{font-size:16px;line-height:1.5;margin:4px 0 8px}}
.chips{{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:4px 0 12px}} .cl{{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin-right:4px}} .chip{{border:1.2px solid {N};border-radius:14px;padding:3px 12px;font-size:14px;font-weight:700}}
.ph{{display:flex;align-items:center;gap:12px;border-top:1.5px solid {N};padding-top:10px;margin-top:10px}} .pn{{width:30px;height:30px;background:{N};color:#fff;display:inline-flex;align-items:center;justify-content:center;font:700 16px 'AH'}} h2{{font-family:'PF',Georgia,serif;font-size:25px;margin:0}}
.how{{font-size:15.5px;color:#3d4080;margin:6px 0 6px}}
.mus svg{{width:100%;height:auto;display:block}} .mus text{{font-family:'AH',Arial !important}} .mus .harm text, .mus g.harm text{{font-family:'PF',Georgia,serif !important;font-weight:700}}
.mus g.fing text{{font-weight:700}} .mus .cnt{{font-family:'AH',Arial !important}}
.ticks{{display:flex;flex-direction:column;gap:8px;margin:8px 0}} .ticks.h{{flex-direction:row;gap:18px}} .tk{{display:inline-flex;align-items:center;gap:9px;font-size:15.5px;font-weight:700}} .bx{{width:20px;height:20px;border:1.8px solid {N};border-radius:4px;display:inline-block;flex:none}}
.lw{{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:18px;align-items:center}} .lks{{display:flex;align-items:flex-end;gap:12px}} .lkh{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{MUTE};writing-mode:vertical-rl;transform:rotate(180deg)}} .lk{{display:grid;justify-items:center;gap:2px}} .lk b{{font-family:'PF',Georgia,serif;font-size:18px}} .tog{{display:flex;gap:14px;align-items:baseline;border:1.5px dashed {C};border-radius:6px;padding:8px 14px;margin:6px 0 4px;font-size:15px}} .tgh{{font-size:11.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};white-space:nowrap}} .row2{{display:grid;grid-template-columns:1fr 110px;gap:16px;align-items:center}} .qr{{display:flex;flex-direction:column;align-items:center;gap:6px;font-size:12px;font-weight:700;color:{MUTE};letter-spacing:.12em;text-transform:uppercase}} .qrb{{width:96px;height:96px;border:1.5px dashed {HELD};display:flex;align-items:center;justify-content:center;color:{HELD};font-size:14px}}
.kbw{{max-width:460px;margin:6px auto 4px}} .kbw svg{{max-width:460px !important}} .sk{{display:flex;align-items:center;gap:20px;flex-wrap:wrap;margin:6px 0 4px}} .sk .ticks{{margin:0}} .two{{display:grid;grid-template-columns:1fr 1.15fr;gap:24px;align-items:start;margin-top:6px}} .cap{{font-size:13px;color:{MUTE};text-align:center}} .q{{font-size:15.5px;margin:2px 0 4px}}
.way.gs .mus{{max-width:91%;margin:0 auto}} .way{{border-top:1px solid #d9d6ea;padding-top:10px;margin-top:12px}} .wh{{display:flex;align-items:baseline;gap:12px}} .wn{{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}} .wh b{{font-family:'PF',Georgia,serif;font-size:21px}} .st{{margin-left:auto;color:{C};letter-spacing:.1em;font-size:15px}}
.chk{{border:1.5px solid {N};margin-top:8px;padding:12px 16px}} .ch{{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin-bottom:4px}} .cgrid{{display:grid;grid-template-columns:1fr 1.25fr;gap:20px}} .chk .ticks.h{{gap:12px}} .chk .tk{{white-space:nowrap}}
.mv{{display:grid;grid-template-columns:300px 1fr;gap:22px;align-items:center;margin:4px 0 2px}} .cap2{{font-size:15px;line-height:1.5;margin:0}} .gl{{max-width:91%;margin:0 auto}} .wrow{{display:flex;align-items:center;gap:10px;margin:6px 0}} .wk{{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:{C};width:38px;flex:none}} .wrow .ticks{{margin:0}} .ck2{{font-size:15.5px;font-weight:700;margin:8px 0 2px}}
.tch{{display:flex;align-items:center;gap:16px;margin-top:12px;padding-top:10px;border-top:1px dashed #c9cbe0}} .tch>span:first-child{{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{MUTE}}}
@media print {{ body{{background:#fff}} .pg{{margin:0}} }}'''
html = f'<!doctype html><html><head><meta charset="utf-8"><title>Lesson {LESSON}: {SONG["title"]}</title><style>{FF}</style><style>{css}</style></head><body>{P1}{P2}{P3}{P4}</body></html>'
open(sys.argv[3], 'w').write(html); print('ok', len(html))
