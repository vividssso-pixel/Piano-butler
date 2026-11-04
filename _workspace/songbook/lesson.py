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
LESSON, LEVEL = SONG.get('lesson', 5), 'Level 0'
ROOM = SONG.get('room', 'note-values')   # the drills room this lesson goes with (the QR opens it; drills needs ?room=)
import qrcode, qrcode.image.svg
def qr(url, px=96):   # a plain navy QR, drawn as one SVG path
    q = qrcode.QRCode(border=1, error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m); d = ''.join(f'M{x},{y}h1v1h-1z' for y, r in enumerate(m) for x, v in enumerate(r) if v)
    return f'<svg viewBox="0 0 {n} {n}" style="width:{px}px;height:{px}px;display:block" shape-rendering="crispEdges"><path d="{d}" fill="{N}"/></svg>'
URL = 'https://thepianobutler.com/drills.html?room=' + ROOM
def page(inner, n): return f'<section class="pg"><div class="top"><span>THE PIANO BUTLER LESSON BOOK · {LEVEL.upper()}</span><span>{SONG.get('label', 'Lesson ' + str(LESSON)).upper()} · {SONG["title"].upper()}</span></div><div class="rule"></div><div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'
def mus(k, cls=''):   # a shorter last line keeps the same size of note: its width in proportion to its bars
    w = SONG.get('widths', {}).get(k); st = f' style="max-width:{w * 100:.1f}%"' if w else ''
    return f'<div class="mus {cls}" data-snip="{k}"{st}>{V[k]}</div>'
def part(n, t, how): return f'<div class="ph"><span class="pn">{n}</span><h2>{t}</h2></div><p class="how">{how}</p>'
def ticks(items, h=False): return f'<div class="ticks{" h" if h else ""}">' + ''.join(f'<span class="tk"><span class="bx"></span>{t}</span>' for t in items) + '</div>'
def way(n, t, stars, how, a, b):
    gs = ' gs' if n > 1 else ''
    return f'<div class="way{gs}"><div class="wh"><span class="wn">Way {n}</span><b>{t}</b><span class="st">{"★" * stars}{"☆" * (4 - stars)}</span></div><p class="how">{how}</p>{mus(a)}{mus(b)}</div>'

# the keyboard in C position: five white keys under the right hand, the song's notes lit, the finger numbers on them
L7 = 'cdefgab'
def trp(p, k): i = L7.index(p[0]) + k; return L7[i % 7] + str(int(p.lstrip('abcdefgs')) + i // 7)   # 'cs5' (a sharp) keeps its octave
# a keyboard from middle C: the five white keys under the right hand (from `start`), the song's notes lit, the fingers on
# them; `sharp` marks the key's black key in coral, named above it
def kb(start=0, tr=0, sharp=None, width=380, fmap=None):
    used = {trp(p, tr)[0] for bar in SONG['bars'] for p, *_ in bar}; H, w = 150, 42
    whites = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'c', 'd', 'e'][:SONG.get('kb_whites', 7)]; out = ''; top = 24 if sharp is not None else 0   # C to B is enough (her 4 Nov 13:35)
    W = len(whites) * w; width = width * len(whites) / 10 * 1.05
    for i, l in enumerate(whites):
        inpos = start <= i < start + 5; lit = inpos and l in used
        if fmap is not None: lit = l in fmap and l in used   # the hand's own keys lit (thumb on D: D to A)
        out += f'<rect x="{i * w}" y="0" width="{w}" height="{H}" rx="3" fill="{"#fbe3da" if lit else "#fff"}" stroke="{N}" stroke-width="1.5"/>'
        out += f'<text x="{i * w + w / 2}" y="{H - 12}" text-anchor="middle" font-family="AH" font-weight="700" font-size="17" fill="{N}">{l.upper()}</text>'
        if fmap is not None: inpos = l in fmap; lit = l not in (SONG.get('kb_open') or [])   # a stretch key gets an open circle
        if inpos: f = fmap[l] if fmap else i - start + 1; out += f'<circle cx="{i * w + w / 2}" cy="{H + 19}" r="13" fill="{C if lit else "#fff"}" stroke="{C}" stroke-width="1.8"/><text x="{i * w + w / 2}" y="{H + 24.5}" text-anchor="middle" font-family="AH" font-weight="700" font-size="15" fill="{"#fff" if lit else C}">{f}</text>'
    for i in [i for i in (0, 1, 3, 4, 5, 7, 8) if i < len(whites) - 1]:
        out += f'<rect x="{(i + 1) * w - 13}" y="0" width="26" height="{H * 0.6}" rx="2" fill="{C if i == sharp else N}"/>'
        if i == sharp: out += f'<text x="{(i + 1) * w}" y="-8" text-anchor="middle" font-family="AH" font-weight="700" font-size="15" fill="{C}">F♯</text>'
    out += f'<text x="1" y="{H + 50}" text-anchor="start" font-family="AH" font-weight="700" font-size="12" fill="{MUTE}">middle C</text>'   # the finger numbers under the keys, clear of the black keys (her 4 Nov 19:58)
    return f'<svg viewBox="-2 {-2 - top} {W + 4} {H + 58 + top}" style="width:{width:.0f}px;max-width:100%;display:block">{out}</svg>'

# a left-hand keyboard from G below to G (the C chord under C to G, the G chord's hand moved down to G), the way's notes for
# that chord lit with their fingers
def lhkb(way, ch, both=False):
    pats = [SONG['lh'][way][c][0] for c in (['C', 'G'] if both else [ch])]
    fing = {p: str(f).split()[k] for ps, d, f in pats for k, p in enumerate(ps)}
    keys = ['c3', 'd3', 'e3', 'f3', 'g3']; W, H, w = len(keys) * 30, 104, 30; out = ''
    for i, p in enumerate(keys):
        lit = p in fing
        out += f'<rect x="{i * w}" y="0" width="{w}" height="{H}" rx="2" fill="{"#fbe3da" if lit else "#fff"}" stroke="{N}" stroke-width="1.2"/>'
        out += f'<text x="{i * w + w / 2}" y="{H - 7}" text-anchor="middle" font-family="AH" font-weight="700" font-size="12" fill="{N}">{p[0].upper()}</text>'
        if lit: out += f'<circle cx="{i * w + w / 2}" cy="{H - 31}" r="10" fill="{C}"/><text x="{i * w + w / 2}" y="{H - 26.5}" text-anchor="middle" font-family="AH" font-weight="700" font-size="13" fill="#fff">{fing[p]}</text>'
    for i in (0, 1, 3): out += f'<rect x="{(i + 1) * w - 8}" y="0" width="16" height="{H * 0.56}" rx="2" fill="{N}"/>'
    return f'<div class="lk"><svg viewBox="-1 -1 {W + 2} {H + 2}" style="width:150px;display:block">{out}</svg><span class="lkc">roots: C 5, G 1</span></div>'

LEAD = SONG.get('lead', 'A rhyme by Sarah Josepha Hale, first printed in Boston in 1830, about a lamb that followed a girl to school. We sing it to the tune of <i>Merrily we roll along</i>.')
chips = ''.join(f'<span class="chip">{t}</span>' for t in SONG.get('chips', ['4/4', 'crotchet, minim, semibreve', 'C position', 'steps and a skip', 'chords C and G']))
WAYS = [(1, 'The tune', 'Right hand alone. The numbers above the notes are your fingers.'),
        (2, 'Hold the root', 'Left hand, row 2. A chord is named after its root: C with finger 5, G with finger 1. Hold it all bar.'),
        (3, 'Root on 1 and 3', 'Row 3: the same root, played on beats 1 and 3.'),
        (4, 'Root on every beat', 'Row 4: the root on every beat, while the right hand plays the tune.')]
legend = ''.join(f'<div class="wl"><span class="wn">Way {n}</span><span class="st">{"★" * n}{"☆" * (4 - n)}</span><b>{t}</b><span class="wd">{d}</span></div>' for n, t, d in WAYS)

# note pictures for the values in the song (drawn, so no font is needed): a head, hollow from the minim, a stem below the semibreve
def note(kind, s=1.0):
    if kind == 'qq':   # two quavers on one beam
        hd = lambda cx: f'<ellipse cx="{cx}" cy="40" rx="9" ry="6.3" transform="rotate(-22 {cx} 40)" fill="{N}"/>'
        return (f'<svg viewBox="0 0 54 50" style="width:{43 * s}px;height:{40 * s}px">{hd(14)}{hd(40)}'
                f'<line x1="22.3" y1="38" x2="22.3" y2="6" stroke="{N}" stroke-width="2.2"/><line x1="48.3" y1="38" x2="48.3" y2="6" stroke="{N}" stroke-width="2.2"/>'
                f'<rect x="21.2" y="4" width="28.2" height="6" fill="{N}"/></svg>')
    head = f'<ellipse cx="14" cy="40" rx="9" ry="6.3" transform="rotate(-22 14 40)" fill="{N if kind == "c" else "#fff"}" stroke="{N}" stroke-width="{0 if kind == "c" else 2.6}"/>'
    stem = '' if kind == 's' else f'<line x1="22.3" y1="38" x2="22.3" y2="6" stroke="{N}" stroke-width="2.2"/>'
    return f'<svg viewBox="0 0 30 50" style="width:{24 * s}px;height:{40 * s}px">{head}{stem}</svg>'
def beats(n): return '<span class="bd">' + '<i></i>' * n + '</span>'
def halves(): return '<span class="bd hv"><i></i><i></i></span>'   # two quavers: one beat's dot cut in half (her 4 Nov 13:23)
vals = ''.join(f'<div class="nv">{note(k, 1.15)}<div><b>{nm}</b><span>{n} beat{"s" if n > 1 else ""}</span>{halves() if k == "qq" else beats(n)}</div></div>' for k, nm, n in SONG.get('value_names', [('c', 'crotchet', 1), ('m', 'minim', 2), ('s', 'semibreve', 4)]) if k in SONG.get('values', 'cms'))
TIME = SONG.get("time_html", "<p><b>Top 4:</b> four beats in every bar.</p><p><b>Bottom 4:</b> a crotchet is one beat.</p>")
TSN = '<div class="tsn"><span>4</span><span>4</span></div>' if SONG.get("time_label", "The time") == "The time" else ''
tsig = f"""<div class="ts">{TSN}<div class="tsx">{TIME}</div></div>"""

POS = SONG.get('pos_html') or ('<div class="pos"><div>' + kb(width=340) + '</div><div><p class="cap2"><b>Your hand: C position.</b> Right thumb on middle C, a finger on each key up to G. The song’s notes are lit.</p>'
  '<p class="cap2"><b>Steps and a skip.</b> Most notes move by a step, to the next key. Only once does the tune skip a key: E up to G.</p></div></div>')
exec(open('early.py').read())
KBS = lambda w: '<div class="kbs">' + ''.join(f'<div><div class="kbl">{t}</div>{kb(width=w, fmap=fm)}</div>' for t, fm in SONG['kbs']) + '</div>'
if 'pos' in SONG: POS = '<div class="pos"><div>' + (blackkb(330) if SONG.get('black_pos') else KBS(SONG.get('kb_w', 300)) if SONG.get('kbs') else kb(width=SONG.get('kb_w', 300), fmap=SONG.get('fmap'))) + '</div><div>' + SONG['pos'] + '</div></div>'
P2T = SONG.get('p2_ticks', ['Listened and pointed', 'Sang it with the words', 'Wrote the letter names', 'Found the skip'])
LINES = lambda pre: ''.join(mus(k) + '<div class="sp"></div>' for k in sorted(k for k in V if k.startswith(pre) and k[len(pre):].isdigit()))
SUB = lambda t, how: f'<div class="sub"><span>{t}</span></div><p class="how">{how}</p>'
P1 = page(f'''<div class="kick">Lesson {LESSON}</div><h1>{SONG["title"]}</h1>
<p class="lead">{LEAD}</p>
<div class="chips"><span class="cl">In this song</span>{chips}</div>
<div class="listen">{qr(URL, 52)}<div><div class="lh2">Listen first</div><p>Scan the code: listen to the whole song once, then hum along the second time.</p></div></div>
<div class="sp"></div>{part(1, 'Meet the song', SONG.get('sing_how', 'Listen, pointing to each note as it sounds. Then sing it with the words.'))}
{POS}
<div class="sp"></div>{LINES('sing')}
<div class="end">{ticks(SONG.get('sing_ticks', ['Listened and pointed', 'Sang it with the words']), True)}</div>''', 1)

NAMES = LINES('name') if not SONG.get('names_row') else '<div class="trow">' + ''.join(mus(k) for k in sorted(k for k in V if k.startswith('name') and k[4:].isdigit())) + '</div>'
# New in this song: one picture, one line, and where the Handbook takes it further (her 4 Nov 22:08)
NW = SONG.get('new')
NEW = (f'<div class="nws"><div class="nws-p">{KBS(NW["kbw"]) if NW.get("kbs") else NW["pic"]}</div><div class="nws-t"><div class="nws-h">New in this song</div><p>{NW["text"]}</p>'
       + f'<p class="nws-b">More in the Handbook: {NW["hb"]}</p></div></div>') if NW else ''
P2 = page(f'''{part(2, 'Take it apart', 'The same song, one piece at a time: first its rhythm, then its notes.')}
{NEW}
{SUB('The rhythm', 'Say the words in time, then clap them and count: clap on the coral numbers, hold through the grey ones.')}
<div class="mat"><div class="mh">{SONG.get("time_label", "The time")}</div>{tsig}<div class="mh">The notes</div><div class="nvs">{vals}</div></div>
<div class="sp"></div>{LINES('rhy')}
{(SUB('The notes', SONG.get('names_how', 'Write the letter name of every note in the boxes; the first one is done.')) + '<div class="sp"></div>' + NAMES) if NAMES else ''}
<div class="end">{ticks(SONG.get('p2_ticks', ['Said it in time', 'Clapped and counted', 'Wrote the letter names']), True)}</div>''', 2)

exec(open('early.py').read())
if SONG.get('kind') == 'ready': P3 = ''
elif 'basics' in SONG: P3 = basics_page()
else: P3 = page(f'''{part(3, 'Play it four ways', 'Each way adds a little more for the left hand. Your teacher tells you which is yours this week.')}
<div class="lg"><div class="lgl">{legend}</div><div class="lks"><span class="lkh">Left hand</span>{lhkb('way2', 'C', both=True)}</div></div>
<div class="sp"></div>{mus('play1')}<div class="sp"></div>{mus('play2')}<div class="sp"></div>
<div class="tog"><span class="tgh">Play together</span><span>Two players, one song: one plays Way 1, the other a left-hand row. Then swap.</span></div>
<div class="chk end"><div class="ch">4 · Check</div><div class="cgrid">
<div>{ticks(['I can say and clap it', 'I can sing it with the words', 'I can name its notes'])}</div>
<div><div class="ck2">I can play it:</div><div class="ticks h">{''.join(f'<span class="tk"><span class="bx"></span>Way {i}</span>' for i in range(1, 5))}</div>
<div class="tch"><span>Teacher</span><span class="tk"><span class="bx"></span>Pass</span><span class="tk"><span class="bx"></span>Not yet</span></div></div></div></div>''', 3)

css = f'''@page {{ size: A4; margin: 0 }} *{{box-sizing:border-box}} body{{margin:0;background:#e9e4d8;font-family:'AH',Arial,sans-serif;color:{N}}}
.pg{{width:794px;height:1123px;background:#fff;margin:0 auto 24px;position:relative;overflow:hidden;padding:42px 58px 0;page-break-after:always}}
.top{{display:flex;justify-content:space-between;font-size:9.5px;font-weight:700;letter-spacing:.16em;color:#8a8cb0}} .rule{{height:5px;border-top:1.5px solid {N};border-bottom:.6px solid {N};margin:7px 0 18px}}
.body{{height:965px;overflow:hidden;display:flex;flex-direction:column}} .body>.end{{margin-top:auto}} .sp{{flex:1 1 0;min-height:10px;max-height:64px}} .body>.ph{{margin-top:6px}} .body>.mus{{margin-top:6px}}
.foot{{position:absolute;left:0;right:0;bottom:30px;text-align:center}} .foot span{{display:inline-block;color:{N};font:700 13px 'AH',Arial;letter-spacing:.08em}}
.kick{{font-size:12px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:{C}}} h1{{font-family:'PF',Georgia,serif;font-size:40px;line-height:1.1;margin:3px 0 8px;font-weight:700}}
.lead{{font-size:17px;line-height:1.5;margin:0 0 8px}} p{{font-size:16px;line-height:1.5;margin:4px 0 8px}}
.listen{{display:flex;align-items:center;gap:16px;border:1.5px solid {C};border-radius:12px;padding:6px 16px;margin:2px 0}} .listen p{{margin:2px 0 0;font-size:14.5px;line-height:1.45}} .lh2{{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}}
.sub{{display:flex;align-items:center;gap:10px;margin:8px 0 0}} .sub span{{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}} .sub::after{{content:'';flex:1;height:1px;background:rgba(38,41,107,.18)}}
.bd.hv{{gap:3px}} .bd.hv i{{height:10px}} .bd.hv i:first-child{{border-radius:99px 0 0 99px;width:5px}} .bd.hv i:last-child{{border-radius:0 99px 99px 0;width:5px}}
.own{{display:flex;border-left:2px solid {N};border-right:4px double {N};margin:0 4px}} .ob{{flex:1;display:flex;justify-content:space-around;gap:6px;align-items:flex-end;border-right:1.5px solid {N};padding:6px 8px 10px}} .ob:last-child{{border-right:0}}
.on{{display:flex;flex-direction:column;align-items:center;gap:8px}} .obx{{width:34px;height:34px;border:2px solid {N};border-radius:8px;display:block}}
.mus.ghost .lhead, .mus.ghost .lname, .mus.ghost g.stem, .mus.ghost g.beam, .mus.ghost .lledger, .mus.ghost g.fing, .mus.ghost g.dots{{opacity:0}}
.trow{{display:flex;gap:28px;align-items:flex-end}} .trow>.mus{{flex:1 1 0;min-width:0;max-width:none!important}}
.nws-p{{flex:0 0 auto}} .nws-t{{flex:1 1 0;min-width:0}} .nws{{display:flex;gap:18px;align-items:center;border:1.5px solid rgba(38,41,107,.22);border-radius:10px;padding:10px 16px;margin:8px 0 2px}} .nws-p svg{{display:block}}
.nws-h{{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin-bottom:3px}} .nws-t p{{margin:0;font-size:15px;line-height:1.45}} .nws-t p.nws-b{{margin-top:4px;font-size:13px;color:{MUTE}}}
.kbs{{display:flex;gap:16px}} .kbl{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{MUTE};margin-bottom:4px}}
.chips{{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:4px 0 12px}} .cl{{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin-right:4px}} .chip{{border:1.2px solid {N};border-radius:14px;padding:3px 12px;font-size:14px;font-weight:700}}
.ph{{display:flex;align-items:center;gap:12px;border-top:1.5px solid {N};padding-top:10px;margin-top:10px}} .pn{{width:30px;height:30px;background:{N};color:#fff;display:inline-flex;align-items:center;justify-content:center;font:700 16px 'AH'}} h2{{font-family:'PF',Georgia,serif;font-size:25px;margin:0}}
.how{{font-size:15.5px;color:#3d4080;margin:6px 0 6px}}
.mus svg{{width:100%;height:auto;display:block}} .mus text{{font-family:'AH',Arial !important}} .mus .harm text, .mus g.harm text{{font-family:'PF',Georgia,serif !important;font-weight:700}}
.mus g.fing text{{font-weight:700}} .mus .cnt{{font-family:'AH',Arial !important}}
.ticks{{display:flex;flex-direction:column;gap:8px;margin:8px 0}} .ticks.h{{flex-direction:row;gap:18px}} .tk{{display:inline-flex;align-items:center;gap:9px;font-size:15.5px;font-weight:700}} .bx{{width:20px;height:20px;border:1.8px solid {N};border-radius:4px;display:inline-block;flex:none}}
.lw{{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:18px;align-items:center}} .lks{{display:flex;align-items:flex-end;gap:12px}} .lkh{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{MUTE};writing-mode:vertical-rl;transform:rotate(180deg)}} .lk{{display:grid;justify-items:center;gap:2px}} .lk b{{font-family:'PF',Georgia,serif;font-size:18px}} .pos{{display:grid;grid-template-columns:auto 1fr;gap:28px;align-items:center;margin:8px 0 10px}} .lg{{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:18px;align-items:center;margin-top:6px}} .lgl{{display:grid;gap:7px}} .wl{{display:grid;grid-template-columns:52px 64px 132px minmax(0,1fr);align-items:baseline;gap:8px;font-size:14.5px}} .wl b{{font-family:'PF',Georgia,serif;font-size:17px}} .wl .st{{margin:0;font-size:13px}} .wd{{color:#3d4080;line-height:1.4}} .sh{{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin:2px 0 6px}} .lks{{flex-direction:column;align-items:center}} .mat{{display:grid;grid-template-columns:auto auto;gap:10px 18px;align-items:center;justify-content:start;border:1.2px solid #d9d6ea;padding:16px 18px;margin:14px 0 22px}} .mh{{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}} .ts{{display:flex;align-items:center;gap:16px}} .tsn{{display:flex;flex-direction:column;align-items:center;font-family:'PF',Georgia,serif;font-weight:700;font-size:34px;line-height:.82}} .tsx p{{margin:0;font-size:15px}} .nvs{{display:flex;gap:26px}} .nv{{display:flex;align-items:center;gap:8px}} .nv b{{display:block;font-size:15px}} .nv span{{font-size:13px;color:#3d4080}} .bd{{display:flex;gap:3px;margin-top:3px}} .bd i{{width:8px;height:8px;border-radius:50%;background:{C};display:block}} .ib{{display:inline-block;width:46px;height:30px;border:1.8px solid {N};border-radius:4px;vertical-align:middle;margin-left:6px}} .lkc{{font-size:12px;font-weight:700;color:{MUTE};margin-top:4px}} .duet{{border:1.5px dashed {C};border-radius:6px;padding:8px 14px 4px;margin:6px 0 4px}} .dh{{display:flex;gap:14px;align-items:baseline;font-size:14.5px}} .dl{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{MUTE};margin:4px 0 -4px}} .dm{{max-width:84%;margin:0 auto}} .tog{{display:flex;gap:14px;align-items:baseline;border:1.5px dashed {C};border-radius:6px;padding:8px 14px;margin:6px 0 4px;font-size:15px}} .tgh{{font-size:11.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};white-space:nowrap}} .row2{{display:grid;grid-template-columns:1fr 110px;gap:16px;align-items:center}} .qr{{display:flex;flex-direction:column;align-items:center;gap:6px;font-size:12px;font-weight:700;color:{MUTE};letter-spacing:.12em;text-transform:uppercase}} .qrb{{width:96px;height:96px;border:1.5px dashed {HELD};display:flex;align-items:center;justify-content:center;color:{HELD};font-size:14px}}
.kbw{{max-width:460px;margin:6px auto 4px}} .kbw svg{{max-width:460px !important}} .sk{{display:flex;align-items:center;gap:20px;flex-wrap:wrap;margin:6px 0 4px}} .sk .ticks{{margin:0}} .two{{display:grid;grid-template-columns:1fr 1.15fr;gap:24px;align-items:start;margin-top:6px}} .cap{{font-size:13px;color:{MUTE};text-align:center}} .q{{font-size:15.5px;margin:2px 0 4px}}
.way.gs .mus{{max-width:91%;margin:0 auto}} .way{{border-top:1px solid #d9d6ea;padding-top:10px;margin-top:12px}} .wh{{display:flex;align-items:baseline;gap:12px}} .wn{{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}} .wh b{{font-family:'PF',Georgia,serif;font-size:21px}} .st{{margin-left:auto;color:{C};letter-spacing:.1em;font-size:15px}}
.chk{{border:1.5px solid {N};margin-top:8px;padding:12px 16px}} .ch{{font-size:12px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin-bottom:4px}} .cgrid{{display:grid;grid-template-columns:1fr 1.25fr;gap:20px}} .chk .ticks.h{{gap:12px}} .chk .tk{{white-space:nowrap}}
.mv{{display:grid;grid-template-columns:260px 1fr;gap:22px;align-items:center;margin:4px 0 2px}} .cap2{{font-size:15px;line-height:1.5;margin:0}} .gl{{max-width:91%;margin:0 auto}} .wrow{{display:flex;align-items:center;gap:10px;margin:6px 0}} .wk{{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:{C};width:38px;flex:none}} .wrow .ticks{{margin:0}} .ck2{{font-size:15.5px;font-weight:700;margin:8px 0 2px}}
.tch{{display:flex;align-items:center;gap:16px;margin-top:12px;padding-top:10px;border-top:1px dashed #c9cbe0}} .tch>span:first-child{{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{MUTE}}}
@media print {{ body{{background:#fff}} .pg{{margin:0}} }}''' + EARLY_CSS
def own_tune(bars):   # her 4 Nov 15:00: make your own -- the rhythm given, a box under each note for its letter
    cells = ''
    for i, bar in enumerate(bars):
        cells += f'<div class="ob" style="flex:{len(bar) + 1}">' + ''.join(f'<div class="on">{note(k, 1.25)}<span class="obx"></span></div>' for k in bar) + '</div>'
    return f'<div class="own">{cells}</div>'
P4 = ''
if SONG.get('more'):
    M = SONG['more']
    T = SONG.get('more_task')   # her 4 Nov 21:25: make-your-own only in the first lessons; later another activity
    TASK = (f'<div class="sp"></div>' + SUB(T['title'], T['how']) + '<div class="sp"></div>' + (lambda ms: f'<div class="trow">{ms}</div>' if T.get('row') else ms)(''.join(mus(k, 'ghost' if T.get('kind') == 'draw' else '') for k in T.get('jobs', ['task1'])))) if T else (
        "<div class=\"sp\"></div>" + SUB('Your own tune', SONG.get('more_own_how', 'Write a letter in each box, then play your tune. Give it a name:') + ' <span class=\"ib\" style=\"width:180px\"></span>') + '<div class="sp"></div>' + own_tune(SONG.get('more_own', [])))
    P4 = page(f'''{part('+', 'More to play', SONG.get('more_how', 'The same keys, the same fingers, the same note values: two new tunes. Then make your own.'))}
<div class="sp"></div>{SUB(M[0]['title'], M[0].get('how', 'Sing it on the words, then play it.'))}
<div class="sp"></div>{mus('moreA1')}{mus('moreA2')}
<div class="sp"></div>{SUB(M[1]['title'], M[1].get('how', 'Say the words in rhythm first, then play it.'))}
<div class="sp"></div>{mus('moreB1')}{mus('moreB2')}
{TASK}
<div class="sp"></div><div class="end">{ticks(SONG.get('more_ticks', ['Played the first tune', 'Played the second tune', 'Played my own tune']), True)}</div>''', 4)
BODY = ready_pages() if SONG.get('kind') == 'ready' else P1 + P2 + P3 + P4
html = f'<!doctype html><html><head><meta charset="utf-8"><title>Lesson {LESSON}: {SONG["title"]}</title><style>{FF}</style><style>{css}</style></head><body>{BODY}</body></html>'
open(sys.argv[3], 'w').write(html); print('ok', len(html))
