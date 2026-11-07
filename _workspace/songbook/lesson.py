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
URL = 'https://thepianobutler.com/listen.html#' + ''.join(c for c in SONG.get('id', '') if not c.isdigit())   # the listening page plays this song (her 5 Nov 00:21)
def page(inner, n): return f'<section class="pg"><div class="top"><span>THE PIANO BUTLER LESSON BOOK · {LEVEL.upper()}</span><span>{SONG.get('label', 'Lesson ' + str(LESSON)).upper()} · {SONG["title"].upper()}</span></div><div class="rule"></div><div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'
def mus(k, cls=''):   # a shorter last line keeps the same size of note: its width in proportion to its bars
    w = SONG.get('widths', {}).get(k); st = f' style="max-width:{w * 100:.1f}%"' if w else ''
    z = SONG.get('scale', {}).get(k); st = f' style="width:100%;max-width:{z * 100:.1f}%;margin-left:auto;margin-right:auto"' if z else st   # a smaller line, centred
    tag = SONG.get('tags', {}).get(k)   # a hand-position label over the line (her 5 Nov 14:22)
    return (f'<div class="htag">{tag}</div>' if tag else '') + f'<div class="mus {cls}" data-snip="{k}"{st}>{V[k]}</div>'
def part(n, t, how): return f'<div class="ph"><span class="pn">{n}</span><h2>{t}</h2></div><p class="how">{how}</p>'
def ticks(items, h=False): return f'<div class="ticks{" h" if h else ""}">' + ''.join(f'<span class="tk"><span class="bx"></span>{t}</span>' for t in items) + '</div>'
def way(n, t, stars, how, a, b):
    gs = ' gs' if n > 1 else ''
    return f'<div class="way{gs}"><div class="wh"><span class="wn">Way {n}</span><b>{t}</b><span class="st">{"★" * stars}{"☆" * (4 - stars)}</span></div><p class="how">{how}</p>{mus(a)}{mus(b)}</div>'

# the keyboard in C position: five white keys under the right hand, the song's notes lit, the finger numbers on them
L7 = 'cdefgab'
def trp(p, k):   # 'cs5' (a sharp) keeps its octave; a chord 'c4+e4+g4' moves note by note
    if '+' in p: return '+'.join(trp(q, k) for q in p.split('+'))
    i = L7.index(p[0]) + k; return L7[i % 7] + str(int(p.lstrip('abcdefgs')) + i // 7)
# a keyboard from middle C: the five white keys under the right hand (from `start`), the song's notes lit, the fingers on
# them; `sharp` marks the key's black key in coral, named above it
def kb(start=0, tr=0, sharp=None, width=380, fmap=None, frm=None):
    used = {trp(p, tr)[0] for bar in SONG['bars'] for p, *_ in bar if p != 'r'}; H, w = 150, 42
    W7 = ['c', 'd', 'e', 'f', 'g', 'a', 'b']; f0 = W7.index(frm or SONG.get('_kb_from') or 'c')   # a keyboard may start on another key (the left hand's G position: G to F)
    whites = (W7[f0:] + W7 + W7)[:SONG.get('kb_whites', 7)]; out = ''; top = 24 if sharp is not None else 0   # C to B is enough (her 4 Nov 13:35)
    W = len(whites) * w; width = width * len(whites) / 10 * 1.05
    for i, l in enumerate(whites):
        inpos = start <= i < start + 5; lit = inpos and l in used
        if fmap is not None: lit = l in fmap and (l in used or SONG.get('_kb_all')) or l in (SONG.get('_kb_extra') or [])   # the hand's own keys lit (thumb on D: D to A); a chord's keys all lit
        out += f'<rect x="{i * w}" y="0" width="{w}" height="{H}" rx="3" fill="{"#fbe3da" if lit else "#fff"}" stroke="{N}" stroke-width="1.5"/>'
        out += f'<text x="{i * w + w / 2}" y="{H - 12}" text-anchor="middle" font-family="AH" font-weight="700" font-size="17" fill="{N}">{l.upper()}</text>'
        if fmap is not None: inpos = l in fmap; lit = l not in (SONG.get('kb_open') or [])   # a stretch key gets an open circle
        if inpos: f = fmap[l] if fmap else i - start + 1; out += f'<circle cx="{i * w + w / 2}" cy="{H + 19}" r="13" fill="{C if lit else "#fff"}" stroke="{C}" stroke-width="1.8"/><text x="{i * w + w / 2}" y="{H + 24.5}" text-anchor="middle" font-family="AH" font-weight="700" font-size="15" fill="{"#fff" if lit else C}">{f}</text>'
    for i in [i for i in range(len(whites) - 1) if whites[i] in 'cdfga']:   # a black key after C, D, F, G and A
        out += f'<rect x="{(i + 1) * w - 13}" y="0" width="26" height="{H * 0.6}" rx="2" fill="{C if i == sharp else N}"/>'
        if i == sharp: out += f'<text x="{(i + 1) * w}" y="-8" text-anchor="middle" font-family="AH" font-weight="700" font-size="15" fill="{C}">{whites[i].upper()}♯</text>'
    out += f'<text x="1" y="{H + 50}" text-anchor="start" font-family="AH" font-weight="700" font-size="12" fill="{MUTE}">{SONG.get("kb_c", "middle C")}</text>'   # the finger numbers under the keys, clear of the black keys (her 4 Nov 19:58)
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
    if kind == 'r':   # a crotchet rest
        return (f'<svg viewBox="0 0 30 50" style="width:{24 * s}px;height:{40 * s}px"><path d="M11 5 L19 15 Q13 20 14 25 L20 33 Q12 30 11 35 Q11 41 16 45 Q6 41 8 34 Q10 29 15 31 L9 24 Q14 19 13 14 Z" fill="{N}"/></svg>')
    head = f'<ellipse cx="14" cy="40" rx="9" ry="6.3" transform="rotate(-22 14 40)" fill="{N if kind == "c" else "#fff"}" stroke="{N}" stroke-width="{0 if kind == "c" else 2.6}"/>'
    if kind == 'd': head += f'<circle cx="28" cy="38" r="2.6" fill="{N}"/>'; kind = 'm'   # a dotted minim: a minim and its dot
    stem = '' if kind == 's' else f'<line x1="22.3" y1="38" x2="22.3" y2="6" stroke="{N}" stroke-width="2.2"/>'
    return f'<svg viewBox="0 0 34 50" style="width:{27 * s}px;height:{40 * s}px">{head}{stem}</svg>'
def beats(n): return '<span class="bd">' + '<i></i>' * n + '</span>'
def halves(): return '<span class="bd hv"><i></i><i></i></span>'   # two quavers: one beat's dot cut in half (her 4 Nov 13:23)
vals = ''.join(f'<div class="nv">{note(k, 1.15)}<div><b>{nm}</b><span>{n} beat{"s" if n > 1 else ""}</span>{halves() if k == "qq" else beats(n)}</div></div>' for k, nm, n in SONG.get('value_names', [('c', 'crotchet', 1), ('m', 'minim', 2), ('s', 'semibreve', 4)]) if k in SONG.get('values', 'cms'))
TIME = SONG.get("time_html", "<p><b>Top 4:</b> four beats in every bar.</p><p><b>Bottom 4:</b> a crotchet is one beat.</p>")
TSN = ('<div class="tsn"><span>%s</span><span>%s</span></div>' % tuple(SONG.get('meter', '4/4').split('/'))) if SONG.get("time_label", "The time") == "The time" else ''
tsig = f"""<div class="ts">{TSN}<div class="tsx">{TIME}</div></div>"""

POS = SONG.get('pos_html') or ('<div class="pos"><div>' + kb(width=340) + '</div><div><p class="cap2"><b>Your hand: C position.</b> Right thumb on middle C, a finger on each key up to G. The song’s notes are lit.</p>'
  '<p class="cap2"><b>Steps and a skip.</b> Most notes move by a step, to the next key. Only once does the tune skip a key: E up to G.</p></div></div>')
exec(open('early.py').read())
KBS = lambda w: '<div class="kbs">' + ''.join(f'<div><div class="kbl">{t}</div>{kb(width=w, fmap=fm, sharp=(x[0] if x and x[0] is not None else None), frm=(x[1] if len(x) > 1 else None))}</div>' for t, fm, *x in SONG['kbs']) + '</div>'   # a third item: the black key to mark (3 = F sharp)
if SONG.get('pos_nokb'): POS = '<div class="posx">' + SONG['pos'] + '</div>'   # a long song: the keyboard waits for page 3
elif 'pos' in SONG and not SONG.get('pos_html'): POS = '<div class="pos"><div>' + (blackkb(330) if SONG.get('black_pos') else KBS(SONG.get('kb_w', 300)) if SONG.get('kbs') else kb(width=SONG.get('kb_w', 300), fmap=SONG.get('fmap'))) + '</div><div>' + SONG['pos'] + '</div></div>'
# her 5 Nov 21:19: the five ideas for teaching it like your own child -- a wow moment, a spot-the-mistake game, a turtle-to-bird ladder, make it yours, a 5-minute menu
STAR = '<svg width="26" height="26" viewBox="0 0 26 26"><path d="M13 2.5l3.1 6.6 7.2.9-5.3 5 1.4 7.1L13 18.6l-6.4 3.5 1.4-7.1-5.3-5 7.2-.9z" fill="none" stroke="#e4572e" stroke-width="2" stroke-linejoin="round"/></svg>'
WOW = f'<div class="wow">{STAR}<div><div class="wowh">The wow moment</div><p>{SONG["wow"]}</p></div></div>' if SONG.get('wow') else ''
TRICK = f'<div class="tog"><span class="tgh">Spot the mistake</span><span>{SONG["trick"]}</span></div>' if SONG.get('trick') else ''
TURTLE = '<svg width="34" height="22" viewBox="0 0 34 22"><path d="M5 15 Q7 4 17 4 Q27 4 29 15 Z" fill="none" stroke="#26296b" stroke-width="2" stroke-linejoin="round"/><path d="M11 15v4M23 15v4M29 13h3.5" stroke="#26296b" stroke-width="2" stroke-linecap="round"/><circle cx="32" cy="11.5" r="1.6" fill="#26296b"/></svg>'
BIRD = '<svg width="34" height="22" viewBox="0 0 34 22"><path d="M3 9 Q10 3 16 12 Q22 3 31 7" fill="none" stroke="#e4572e" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M16 12v6" stroke="#e4572e" stroke-width="2" stroke-linecap="round"/></svg>'
LSTEPS = SONG.get('ladder', ['With letters', 'No letters', 'With the band', 'Fast'])
def ladder(rows):   # one row per way of playing: colour a step each time you climb
    head = '<div class="lad lhd"><span></span>' + TURTLE + ''.join(f'<span class="lst">{t}</span>' for t in LSTEPS) + BIRD + '</div>'
    return head + ''.join(f'<div class="lad"><span class="lrn">{r}</span><span></span>' + ''.join('<span class="lsq"></span>' for _ in LSTEPS) + '<span></span></div>' for r in rows)
P2T = SONG.get('p2_ticks', ['Listened and pointed', 'Sang it with the words', 'Wrote the letter names', 'Found the skip'])
LINES = lambda pre: ''.join(mus(k) + '<div class="sp"></div>' for k in sorted(k for k in V if k.startswith(pre) and k[len(pre):].isdigit()))
SUB = lambda t, how: f'<div class="sub"><span>{t}</span></div><p class="how">{how}</p>'
LISTEN = f'<div class="listen">{qr(URL, 52)}<div><div class="lh2">Listen first</div><p>Scan the code: listen to the whole song once, then hum along the second time.</p></div></div>'
if SONG.get('p1_tight'): LISTEN = LISTEN.replace('listen to the whole song once, then hum along the second time.', 'listen once, then hum along.')
# p1_tight (her 7 Nov 00:51, '조정해줘'): a long song's page 1 gives its room to the notes -- no chip row, and Listen first and the wow moment side by side
TOP1 = (f'<div class="lw2">{LISTEN}{WOW}</div>' if SONG.get('p1_tight') else f'<div class="chips"><span class="cl">In this song</span>{chips}</div>\n' + LISTEN)
P1 = page(f'''<div class="kick">Lesson {LESSON}</div><h1>{SONG["title"]}</h1>
<p class="lead">{LEAD}</p>
{TOP1}
<div class="sp"></div>{part(1, 'Meet the song', SONG.get('sing_how', 'Listen, pointing to each note as it sounds. Then sing it with the words.'))}
{POS}
<div class="sp"></div>{LINES('sing')}
{'' if SONG.get('p1_tight') else WOW}<div class="end">{ticks(SONG.get('sing_ticks', ['Listened and pointed', 'Sang it with the words']), True)}</div>''', 1)

NAMES = LINES('name') if not SONG.get('names_row') else '<div class="trow">' + ''.join(mus(k) for k in sorted(k for k in V if k.startswith('name') and k[4:].isdigit())) + '</div>'
# New in this song: one picture, one line, and where the Handbook takes it further (her 4 Nov 22:08)
NW = SONG.get('new')
NEW = (f'<div class="nws"><div class="nws-p">{KBS(NW["kbw"]) if NW.get("kbs") else NW["pic"]}</div><div class="nws-t"><div class="nws-h">New in this song</div><p>{NW["text"]}</p>'
       + (f'<p class="nws-b">More in the Handbook: {NW["hb"]}</p>' if NW.get('hb') else '') + '</div></div>') if NW else ''
P2 = page(f'''{part(2, 'Take it apart', 'The same song, one piece at a time: first its rhythm, then its notes.')}
{NEW}
{SUB('The rhythm', SONG.get('rhy_how', 'Say the words in time, then clap them and count: clap on the coral numbers, hold through the grey ones.'))}
<div class="mat"><div class="mh">{SONG.get("time_label", "The time")}</div>{tsig}<div class="mh">The notes</div><div class="nvs">{vals}</div></div>
<div class="sp"></div>{LINES('rhy')}
{(SUB('The notes', SONG.get('names_how', 'Write the letter name of every note in the boxes; the first one is done.')) + '<div class="sp"></div>' + NAMES) if NAMES else ''}
{('<div class="sp"></div>' + TRICK) if TRICK else ''}<div class="end">{ticks(SONG.get('p2_ticks', ['Said it in time', 'Clapped and counted', 'Wrote the letter names']), True)}</div>''', 2)

exec(open('early.py').read())
def STRIP(names):   # the bars as names only, big: the first lead sheet's seed (her 6 Nov 14:54: the chords from the left hand)
    cells = ''.join(f'<div class="sc">{n}</div>' for n in names)
    return f'<div class="strip" style="grid-template-columns:repeat({SONG.get("strip_cols", 4)},1fr)">{cells}</div>'
def chord_page():   # her 6 Nov 14:24: page 3 unpacks the chords one at a time (meet the chord, find it in the song, play it), the road to the lead sheet
    C = SONG['chord_page']
    def ckb(t, fm, extra):
        SONG['_kb_all'] = 1; SONG['_kb_extra'] = extra; SONG['_kb_from'] = C.get('kb_from'); kc = SONG.get('kb_c'); SONG['kb_c'] = C.get('kb_c', kc or 'middle C'); h = f'<div><div class="kbl">{t}</div>{kb(width=C.get("kb_w", 230), fmap=fm)}</div>'; SONG['_kb_all'] = 0; SONG['_kb_extra'] = None; SONG['_kb_from'] = None; SONG['kb_c'] = kc or 'middle C'; return h
    kbs = '<div class="kbs">' + ''.join(ckb(t, fm, ex) for t, fm, ex in C['kbs']) + '</div>'
    return page(f'''{part(3, C.get('title', 'The chords'), C['how'])}
<div class="sp"></div>{SUB(C.get('meet_title', 'Meet the chord'), C['meet'])}{('<div class="pos"><div>' + kbs + '</div><div>' + C['meet_note'] + '</div></div>') if C.get('meet_note') else kbs}
<div class="sp"></div>{SUB(C.get('find_title', 'Find it in the song'), C['find'])}{''.join(mus(k) for k in C['find_jobs'])}
<div class="sp"></div>{SUB(C.get('play_title', 'Play the chords'), C['play'])}{''.join(mus(k) for k in C.get('play_jobs', []))}{STRIP(C['strip']) if C.get('strip') else ''}
<div class="sp"></div>{LADCHK()}''', 3)
def lead_page():   # her 7 Nov 13:11: page 3 is a lead sheet in every lesson, with a left-hand pattern that grows
    L = SONG['lead_page']; P = L.get('pattern')
    roots = sorted({x[0] for bar in SONG['leadch'] for x in bar}, key=lambda c: 'CDEFGAB'.index(c[0]))
    names = '<div class="lnames">' + ''.join(f'<span class="lcn">{r}</span>' for r in roots) + '</div>'
    if P:
        box = (f'<div class="lpat"><div class="lpt"><div class="kick">{P["title"]}</div><p class="cap2">{P["how"]}</p>{names}</div>'
               f'<div class="lpm">{mus(L["pjob"])}</div></div>')
    else:
        box = (f'<div class="lpat"><div class="lpt"><div class="kick">The names</div><p class="cap2">A name tells the band which chord to play under the tune. '
               f'Your left hand learns to play them from Lesson 4.</p></div><div class="lpt">{names}</div></div>')
    steps = '<div class="lsteps">' + ''.join(f'<div class="lst"><span class="pn">{i + 1}</span><span>{t}</span></div>' for i, t in enumerate(L['steps'])) + '</div>'
    return page(f"""{part(3, 'Lead sheet', L['how'])}
<div class="sp"></div>{box}
<div class="sp"></div>{''.join(mus(k) for k in L['jobs'])}
<div class="sp"></div>{steps}
<div class="sp"></div>{LADCHK()}""", 3)
if SONG.get('kind') == 'ready': P3 = ''
elif SONG.get('lead_page'): P3 = lead_page()
elif SONG.get('chord_page'): P3 = chord_page()
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
.htag{{font-size:11.5px;font-weight:700;letter-spacing:.06em;color:{C};margin:4px 0 -8px 2px;line-height:1.2}}
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
.wow{{display:flex;gap:12px;align-items:center;border-left:3px solid {C};padding:4px 12px;margin:6px 0 0}} .wow p{{margin:0;font-size:15px;line-height:1.45}} .wowh{{font-size:11.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}}
.lad{{display:grid;grid-template-columns:118px 34px repeat({len(LSTEPS)},1fr) 34px;gap:6px;align-items:center;margin:3px 0}} .lad.lhd{{margin-bottom:2px}} .lst{{font-size:11px;font-weight:700;color:{MUTE};text-align:center;line-height:1.15}} .lrn{{font-size:14px;font-weight:700}} .lsq{{height:22px;border:1.8px solid {N};border-radius:4px}}
.yrs{{display:grid;grid-template-columns:1fr 1fr;gap:24px;border-top:1px solid #d9d6ea;padding-top:10px}} .yrs .ticks{{gap:6px;margin:4px 0 0}} .yrs .tk{{font-size:14.5px}} .menu ol{{margin:2px 0 6px;padding-left:20px;font-size:14.5px;line-height:1.55}} .days{{display:flex;gap:9px}} .dy{{display:flex;flex-direction:column;align-items:center;gap:2px;font-size:11px;font-weight:700;color:{MUTE}}}
.posx{{margin:2px 0 4px}} .posx p{{margin:2px 0}}
.lpat{{display:grid;grid-template-columns:1fr 1.15fr;gap:18px;align-items:center;border:1.5px solid rgba(38,41,107,.18);border-radius:10px;padding:10px 14px}} .lpat .kick{{margin-bottom:2px}} .lpat p{{margin:2px 0 6px}}
.lnames{{display:flex;gap:8px;flex-wrap:wrap}} .lcn{{font:700 20px 'AH',Arial;color:#26296b;border:1.5px solid #26296b;border-radius:8px;min-width:40px;text-align:center;padding:3px 8px}}
.lsteps{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}} .lst{{display:flex;gap:8px;align-items:flex-start;font-size:14px;line-height:1.35}} .lst .pn{{flex:none}}
.mus g.harm text{{font-family:'AH',Arial,sans-serif!important;font-weight:700;fill:#26296b}}
.lw2{{display:grid;grid-template-columns:1fr 1.5fr;gap:14px;align-items:stretch}} .lw2>.listen,.lw2>.wow{{margin:0}}
[hidden]{{display:none!important}}
.strip{{display:grid;grid-template-columns:repeat(4,1fr);border-left:2px solid {N};margin:8px 0 0}} .sc{{border-right:2px solid {N};border-top:1.5px solid #d9d6ea;border-bottom:1.5px solid #d9d6ea;padding:8px 0;text-align:center;font-family:'Playfair Display',serif;font-weight:700;font-size:30px;color:{N}}}
@media print {{ body{{background:#fff}} .pg{{margin:0}} }}''' + EARLY_CSS
def own_tune(bars):   # her 4 Nov 15:00: make your own -- the rhythm given, a box under each note for its letter
    cells = ''
    for i, bar in enumerate(bars):
        cells += f'<div class="ob" style="flex:{len(bar) + 1}">' + ''.join(f'<div class="on">{note(k, 1.25)}<span class="obx"></span></div>' for k in bar) + '</div>'
    return f'<div class="own">{cells}</div>'
P4 = ''
if SONG.get('more'):
    M = SONG['more']
    T = SONG.get('more_task'); NO_OWN = SONG.get('no_own')   # her 4 Nov 21:25: make-your-own only in the first lessons; later another activity
    TASK = (f'<div class="sp"></div>' + SUB(T['title'], T['how']) + '<div class="sp"></div>' + (lambda ms: f'<div class="trow">{ms}</div>' if T.get('row') else ms)(''.join(mus(k, 'ghost' if T.get('kind') == 'draw' else '') for k in T.get('jobs', ['task1'])))) if T else (
        "<div class=\"sp\"></div>" + SUB('Your own tune', SONG.get('more_own_how', 'Write a letter in each box, then play your tune. Give it a name:') + ' <span class=\"ib\" style=\"width:180px\"></span>') + '<div class="sp"></div>' + own_tune(SONG.get('more_own', [])))
    if NO_OWN and not T: TASK = ''   # her 5 Nov 13:47: no make-your-own here
    Y = SONG.get('yours'); MN = SONG.get('menu')
    YOURS = ('<div class="sp"></div><div class="yrs">' + (f'<div><div class="sh">Make it yours</div><p class="cap2">{Y["how"]}</p>{ticks(Y["pick"])}</div>' if Y else '')
             + (f'<div class="menu"><div class="sh">5 minutes at home</div><ol>' + ''.join(f'<li>{m}</li>' for m in MN) + '</ol><div class="days">' + ''.join(f'<span class="dy"><span class="bx"></span>{d}</span>' for d in 'MTWTFSS') + '</div></div>' if MN else '') + '</div>') if (Y or MN) else ''
    P4 = page(f'''{part('+', 'More to play', SONG.get('more_how', 'The same keys, the same fingers, the same note values: two new tunes. Then make your own.'))}
<div class="sp"></div>{SUB(M[0]['title'], M[0].get('how', 'Sing it on the words, then play it.'))}
<div class="sp"></div>{''.join(mus(k) for k in sorted((k for k in V if k.startswith('moreA') and k[5:].isdigit()), key=lambda k: int(k[5:])))}
{('<div class="sp"></div>' + SUB(M[1]['title'], M[1].get('how', 'Say the words in rhythm first, then play it.')) + '<div class="sp"></div>' + ''.join(mus(k) for k in sorted((k for k in V if k.startswith('moreB') and k[5:].isdigit()), key=lambda k: int(k[5:])))) if len(M) > 1 and any(k.startswith('moreB') for k in V) else ''}
{TASK}
{YOURS}
<div class="sp"></div><div class="end">{ticks(SONG.get('more_ticks', ['Played the first tune', 'Played the second tune', 'Played my own tune']), True)}</div>''', 4)
BODY = ready_pages() if SONG.get('kind') == 'ready' else P1 + P2 + P3 + P4
html = f'<!doctype html><html><head><meta charset="utf-8"><title>Lesson {LESSON}: {SONG["title"]}</title><style>{FF}</style><style>{css}</style></head><body>{BODY}</body></html>'
open(sys.argv[3], 'w').write(html); print('ok', len(html))
