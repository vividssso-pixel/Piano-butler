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
URL = ('https://thepianobutler.com/musicbox.html#' if SONG.get('book', '').endswith('MUSIC BOX') else 'https://thepianobutler.com/listen.html#') + ''.join(c for c in SONG.get('id', '') if not c.isdigit())   # the listening page plays this song (her 5 Nov 00:21)
def page(inner, n): return f'<section class="pg"><div class="top"><span>{SONG.get('book') or ('THE PIANO BUTLER LESSON BOOK · ' + LEVEL.upper())}</span><span>{SONG.get('label', 'Lesson ' + str(LESSON)).upper()} · {SONG["title"].upper()}</span></div><div class="rule"></div><div class="body">{inner}</div><div class="foot"><span>{n}</span></div></section>'
def mus(k, cls=''):   # a shorter last line keeps the same size of note: its width in proportion to its bars
    w = SONG.get('widths', {}).get(k); st = f' style="max-width:{w * 100:.1f}%"' if w else ''
    z = SONG.get('scale', {}).get(k); st = f' style="width:100%;max-width:{z * 100:.1f}%;margin-left:auto;margin-right:auto"' if z else st   # a smaller line, centred
    tag = SONG.get('tags', {}).get(k)   # a hand-position label over the line (her 5 Nov 14:22)
    return (f'<div class="htag">{tag}</div>' if tag else '') + f'<div class="mus {cls}{" brace" if "grpSym" in V[k] else ""}" data-snip="{k}"{st}>{V[k]}</div>'
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
    arr = SONG.get('_kb_arrows') or []
    for x0, x1 in zip(arr, arr[1:]):   # 2.0: the pattern drawn on the keys, a coral arc from each key to the next
        if x0 in whites and x1 in whites:
            ax, bx = whites.index(x0) * w + w / 2, whites.index(x1) * w + w / 2; my = H * 0.8
            out += f'<path d="M{ax} {my} Q{(ax + bx) / 2} {my - 26} {bx + (6 if bx < ax else -6)} {my - 3}" fill="none" stroke="{C}" stroke-width="2.6" stroke-linecap="round"/>'
            d = -1 if bx < ax else 1; out += f'<path d="M{bx} {my} l{-d * 10} -3 l{d * 2} -9 z" fill="{C}"/>'
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
TRICK = ((f'<div class="trk"><div class="tog"><span class="tgh">Spot the mistake</span><span>{SONG["trick"]}</span></div>{mus("oops1")}</div>') if 'oops1' in V else f'<div class="tog"><span class="tgh">Spot the mistake</span><span>{SONG["trick"]}</span></div>') if SONG.get('trick') else ''   # printed (her 7 Nov: a book for self-learners too)
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
TOP1 = (f'<div class="lw2">{LISTEN}{WOW}</div>' if SONG.get('p1_tight') else f'<div class="chips"><span class="cl">In this song</span>{chips}</div>\n' + (f'<div class="lw2">{LISTEN}{WOW}</div>' if WOW else LISTEN))   # the wow beside Listen first, so page 1 keeps its song (7 Nov)
P1 = page(f'''<div class="kick">Lesson {LESSON}</div><h1>{SONG["title"]}</h1>
<p class="lead">{LEAD}</p>
{TOP1}
<div class="sp"></div>{part(1, 'Meet the song', SONG.get('sing_how', 'Listen, pointing to each note as it sounds. Then sing it with the words.'))}
{POS}
<div class="sp"></div>{LINES('sing')}
<div class="end">{ticks(SONG.get('sing_ticks', ['Listened and pointed', 'Sang it with the words']), True)}</div>''', 1)

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
elif SONG.get('v2') or SONG.get('mock') or SONG.get('v3') or SONG.get('v4'): P3 = ''
else: P3 = page(f'''{part(3, 'Play it four ways', 'Each way adds a little more for the left hand. Start with way 1; move on when it feels easy.')}
<div class="lg"><div class="lgl">{legend}</div><div class="lks"><span class="lkh">Left hand</span>{lhkb('way2', 'C', both=True)}</div></div>
<div class="sp"></div>{mus('play1')}<div class="sp"></div>{mus('play2')}<div class="sp"></div>
<div class="tog"><span class="tgh">Play together</span><span>Two players, one song: one plays Way 1, the other a left-hand row. Then swap.</span></div>
<div class="chk end"><div class="ch">4 · Check</div><div class="cgrid">
<div>{ticks(['I can say and clap it', 'I can sing it with the words', 'I can name its notes'])}</div>
<div><div class="ck2">I can play it:</div><div class="ticks h">{''.join(f'<span class="tk"><span class="bx"></span>Way {i}</span>' for i in range(1, 5))}</div>
<div class="tch"><span>Listen back</span><span class="tk"><span class="bx"></span>I recorded it</span><span class="tk"><span class="bx"></span>It sounded right</span></div></div></div></div>''', 3)

css = f'''@page {{ size: A4; margin: 0 }} *{{box-sizing:border-box}} body{{margin:0;background:#e9e4d8;font-family:'AH',Arial,sans-serif;color:{N}}}
.pg{{width:794px;height:1123px;background:#fff;margin:0 auto 24px;position:relative;overflow:hidden;padding:42px 58px 0;page-break-after:always}}
.top{{display:flex;justify-content:space-between;font-size:9.5px;font-weight:700;letter-spacing:.16em;color:#8a8cb0}} .rule{{height:5px;border-top:1.5px solid {N};border-bottom:.6px solid {N};margin:7px 0 18px}}
.body{{height:965px;overflow:hidden;display:flex;flex-direction:column}} .body>.end{{margin-top:auto}}
.body>.end:not(:last-child){{margin-top:14px;margin-bottom:22px}} .sp{{flex:1 1 0;min-height:30px;max-height:64px}}
.body .mus+.mus{{margin-top:36px}} .body>.ph{{margin-top:6px}} .body>.mus{{margin-top:6px}}
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
.mus svg{{width:100%;height:auto;display:block}}
.mus.brace{{padding-left:3px}} .mus text{{font-family:'AH',Arial !important}} .mus .harm text, .ticks.h{{flex-wrap:wrap;row-gap:6px}}
.mus[data-snip]{{margin-left:auto;margin-right:auto;width:100%;box-sizing:border-box}}
p, .how, .cap2, .lead, .tog span, .lst span{{text-wrap:pretty}}
.mus g.harm text{{font-family:'PF',Georgia,serif !important;font-weight:700}}
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
.lnames{{display:flex;gap:8px;flex-wrap:wrap}} .lcn{{font:700 20px 'AH',Arial;color:#fff;background:#e4572e;border:1.5px solid #e4572e;border-radius:8px;min-width:40px;text-align:center;padding:3px 8px}}
.lsteps{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}} .lst{{display:flex;gap:8px;align-items:flex-start;font-size:14px;line-height:1.35}} .lst .pn{{flex:none}}
.mus g.harm text{{font-family:'AH',Arial,sans-serif!important;font-weight:700;fill:{N}}} .mus g.harm rect.hbox{{fill:#fff;stroke:{N};stroke-width:22}}
.trk{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:18px;align-items:center;border:1.5px dashed rgba(228,87,46,.55);border-radius:10px;padding:8px 14px}} .trk .tog{{margin:0;border:0;padding:0;display:block}} .trk .tog .tgh{{display:block;margin-bottom:3px}}
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
GLYPH = {   # the pattern glyphs: one small picture per pattern, the same all book long (navy line, coral arrow)
 'down3': '<svg width="58" height="40" viewBox="0 0 58 40"><circle cx="9" cy="9" r="5.5" fill="#26296b"/><circle cx="29" cy="20" r="5.5" fill="#26296b"/><circle cx="49" cy="31" r="5.5" fill="#26296b"/><path d="M13 13 L24 18.5 M33 24 L44 29.5" stroke="#e4572e" stroke-width="2.4" stroke-linecap="round"/></svg>',
}
def gl(k, s=1): return GLYPH[k].replace('width="58" height="40"', f'width="{58 * s:.0f}" height="{40 * s:.0f}"')
if SONG.get('v2'):
    X = SONG['v2']; G = X['glyph']
    PATBOX = (f'<div class="pat"><div>{(lambda: (SONG.update({"_kb_arrows": X["arrows"]}), kb(width=300, fmap=SONG.get("fmap")), SONG.update({"_kb_arrows": None}))[1])()}</div>'
              f'<div class="patt"><div class="pathd">{gl(G)}<div><div class="kick">Pattern of the lesson</div><div class="patn">{X["name"]}</div></div></div>'
              f'<p class="cap2">{X["pat_how"]}</p><p class="cap2">{X["hand"]}</p></div></div>')
    P1 = page(f"""<div class="kick">Lesson {LESSON}</div><h1>{SONG["title"]}</h1>
<p class="lead">{LEAD}</p>
<div class="lw2">{LISTEN}{WOW}</div>
<div class="sp"></div>{part(1, 'Meet the song', X['sing_how'])}
{PATBOX}
<div class="sp"></div>{LINES('sing')}
<div class="end">{ticks(X['p1_ticks'], True)}</div>""", 1)
    P2 = page(f"""{part(2, 'Take it apart', X['p2_how'])}
<div class="sp"></div>{SUB('Spot the pattern', X['spot'])}<div class="spot">{gl(G, 1.2)}<span>How many times?</span><span class="ib"></span></div>
<div class="sp"></div>{SUB('Clap it', X['clap'])}<div class="mat"><div class="mh">The notes</div><div class="nvs">{vals}</div></div>
<div class="sp"></div>{SUB('Name it, fix it', X['fix'])}<div class="sp"></div>{mus('oops1')}
<div class="sp"></div><div class="end">{ticks(X['p2_ticks'], True)}</div>""", 2)
    roots = sorted({x[0] for bar in SONG['leadch'] for x in bar}, key=lambda c: 'CDEFGAB'.index(c[0]))
    def YRS2(): MN = SONG.get('menu'); return (f'<div class="sp"></div><div class="yrs"><div><div class="sh">Make it yours <span class="opt">if you like</span></div><p class="cap2">{X["yours"]}</p></div>'
        f'<div class="menu"><div class="sh">5 minutes at home</div><ol>' + ''.join(f'<li>{m}</li>' for m in MN) + '</ol><div class="days">' + ''.join(f'<span class="dy"><span class="bx"></span>{d}</span>' for d in 'MTWTFSS') + '</div></div></div>')
    MOVE = ''.join(f'<div><div class="kbl">{t}</div>{(lambda: (SONG.update({"_kb_arrows": ar, "_kb_all": 1}), kb(width=330, fmap=fm), SONG.update({"_kb_arrows": None, "_kb_all": 0}))[1])()}</div>' for t, fm, ar in X['move'])
    P3 = page(f"""{part(3, X['p3_title'], X['p3_how'])}
<div class="sp"></div>{SUB('The names', X['names'])}<div class="lnames big">{''.join(f'<span class="lcn">{r}</span>' for r in roots)}</div>
<div class="sp"></div>{SUB('Move the pattern', X['move_how'])}<div class="kbs mv2">{MOVE}</div>
<div class="sp"></div><div class="lsteps">{''.join(f'<div class="lst"><span class="pn">{i + 1}</span><span>{t}</span></div>' for i, t in enumerate(X['steps']))}</div>
{'' if X.get('more_how') else YRS2()}
<div class="end">{ticks(X['p3_ticks'], True)}</div>""", 3)
    M = SONG['more'][0]; Y = SONG.get('yours'); MN = SONG.get('menu')
    P4 = '' if not X.get('more_how') else page(f"""{part('+', 'More to play', X['more_how'])}
<div class="sp"></div>{SUB(M['title'], M.get('how', ''))}<div class="seen">{gl(G, .8)}<span>{X['seen']}</span></div>
<div class="sp"></div>{''.join(mus(k) for k in sorted((k for k in V if k.startswith('moreA') and k[5:].isdigit()), key=lambda k: int(k[5:])))}
<div class="sp"></div><div class="yrs"><div><div class="sh">Make it yours <span class="opt">if you like</span></div><p class="cap2">{X['yours']}</p></div>
<div class="menu"><div class="sh">5 minutes at home</div><ol>{''.join(f'<li>{m}</li>' for m in MN)}</ol><div class="days">{''.join(f'<span class="dy"><span class="bx"></span>{d}</span>' for d in 'MTWTFSS')}</div></div></div>
<div class="sp"></div><div class="end">{ticks(X['more_ticks'], True)}</div>""", 4)
    css += f""".pat{{display:grid;grid-template-columns:auto 1fr;gap:26px;align-items:center;margin:6px 0 4px}} .patt .cap2{{margin:4px 0}} .pathd{{display:flex;gap:12px;align-items:center;margin-bottom:4px}}
.patn{{font-family:'PF',Georgia,serif;font-size:22px;font-weight:700;line-height:1.15}} .spot{{display:flex;align-items:center;gap:14px;font-size:16px;font-weight:700;margin:6px 0 0}} .spot .ib{{width:60px;height:38px}}
.lnames.big .lcn{{font-size:26px;min-width:56px;padding:6px 12px}} .mv2{{gap:28px;flex-wrap:wrap}} .seen{{display:flex;align-items:center;gap:10px;font-size:14px;font-weight:700;color:{MUTE};margin:4px 0 0}}
.lsteps .lst{{color:{N};text-align:left;font-size:15.5px;font-weight:400;line-height:1.4}} .opt{{font-size:10.5px;color:{MUTE};letter-spacing:.12em;margin-left:6px}}"""
if SONG.get('mock'):   # her 8 Nov 13:15: show A, B, C and D so she can choose
    CHIP = lambda t, big=False: f'<span class="lcn{" bigc" if big else ""}">{t}</span>'
    FLAG = '<p class="mnote">Pieces named are examples to check against their scores before printing.</p>'
    def OPT(letter, title, idea, body, where):
        return page(f"""<div class="kick">Option {letter}</div><h1 class="mh1">{title}</h1><p class="lead">{idea}</p>
<div class="mwhere"><b>Where it goes:</b> {where}</div><div class="sp"></div>{body}<div class="sp"></div>{FLAG}""", letter)
    OA = OPT('A', 'The ladder box', 'One small box, the same four steps every time the left hand learns something new: the name, the sound, how it looks, where it lives.',
      f"""<div class="mlab">As it would look in Lesson 9 (the whole chord)</div>
<div class="abox"><div class="acell"><div class="anum">1</div><div class="ah">The name</div>{CHIP('C', True)}<p class="cap2">Read only the name.</p></div>
<div class="acell"><div class="anum">2</div><div class="ah">The sound</div>{qr(URL, 64)}<p class="cap2">Hear it with the band.</p></div>
<div class="acell w"><div class="anum">3</div><div class="ah">How it looks</div><div class="amus">{mus('m_blk')}</div><p class="cap2">C, E and G together: three keys, one sound.</p></div>
<div class="acell"><div class="anum">4</div><div class="ah">Where it lives</div><p class="afam">Chopin<br><i>Prelude in C minor</i></p><p class="cap2">Whole chords, slow and grand.</p></div></div>
<div class="sp"></div><div class="mlab">Every lesson after: the same box, one new pattern</div>
<div class="minis">{''.join(f'<div class="mini"><span class="mn">L{l}</span>{CHIP(c)}<span>{t}</span></div>' for l, c, t in [(3, 'C', 'the root'), (5, 'F', 'three roots'), (7, 'C', 'root + fifth'), (9, 'C', 'the whole chord')])}</div>""",
      'Part 3 of each lesson, above the steps. Nothing else changes.')
    CARD = lambda name, k, piece, comp, got: f"""<div class="card{' got' if got else ''}"><div class="ctop"><span class="cn">{name}</span>{'<span class="stamp">collected</span>' if got else '<span class="stamp e">Lesson 9</span>'}</div><div class="cmus">{mus(k)}</div><div class="clive">Lives in</div><div class="cpiece"><b>{comp}</b><br><i>{piece}</i></div></div>"""
    OB = OPT('B', 'Pattern cards', 'Each left-hand pattern is a card to collect. The card shows the name, how it looks, and a famous piece built on it. The listening page plays that piece.',
      f"""<div class="mlab">The cards page, at the back beside the Composer Passport</div>
<div class="cards">{CARD('The root', 'm_root', 'Boléro (the drum and bass)', 'Ravel', True)}{CARD('Root + fifth', 'm_r5', 'Symphony No. 9, the opening', 'Beethoven', True)}{CARD('The whole chord', 'm_blk', 'Prelude in C minor', 'Chopin', False)}{CARD('Broken chord', 'm_brk', 'Prelude in C', 'J. S. Bach', False)}</div>
<div class="sp"></div><div class="mlab">In the lesson: one line</div><div class="bline">{CHIP('C')}<span>New card: <b>the whole chord</b>. Play it, then stick it in at the back and listen to where it lives.</span></div>""",
      'A cards page at the back (2 pages for Level 0); in each lesson only one line.')
    OC = OPT('C', 'Same sound, two clothes', 'Half a page: on the left, the chord name the way band players read it; on the right, the same sound written out the way a classical score shows it.',
      f"""<div class="mlab">As it would look in Lesson 9</div>
<div class="ctwo"><div class="cside"><div class="ch2">Band players read</div><div class="cstrip">{''.join(f'<span class="cbar">{CHIP(c)}</span>' for c in 'CCGC')}</div><p class="cap2">Only the names. The left hand chooses how to play them.</p></div>
<div class="cmid">=</div><div class="cside"><div class="ch2">A classical score writes</div><div class="cmus2">{mus('m_brk')}</div><p class="cap2">The same C, every note written: Bach's Prelude in C is made of this shape, bar after bar.</p></div></div>
<div class="sp"></div><div class="mlab">Then: play the right-hand side yourself, and hear that it is the same C</div>""",
      'Part 3, half a page, from Lesson 7 (when the left hand has a shape to compare).')
    ST = [('The root', 'Ravel, Boléro', 1), ('Three roots', 'folk songs everywhere', 1), ('Root + fifth', 'Beethoven, Symphony No. 9', 1), ('The whole chord', 'Chopin, Prelude in C minor', 0), ('Broken chord', 'Bach, Prelude in C', 0), ('Oom-pah-pah', 'Strauss, The Blue Danube', 0)]
    pos = [(90, 80), (320, 80), (550, 80), (550, 300), (320, 300), (90, 300)]   # a snake: left to right, down, right to left
    svg = '<svg viewBox="0 0 680 400" style="width:100%;display:block"><path d="M90 80 H668 V300 H90" fill="none" stroke="#26296b" stroke-width="2" stroke-dasharray="6 6"/>'
    for (x, y), (nm, pc, done) in zip(pos, ST):
        svg += f'<circle cx="{x}" cy="{y}" r="22" fill="{"#e4572e" if done else "#fff"}" stroke="#e4572e" stroke-width="2.5"/>'
        svg += f'<text x="{x}" y="{y + 52}" text-anchor="middle" font-family="PF" font-weight="700" font-size="19" fill="#26296b">{nm}</text>'
        svg += f'<text x="{x}" y="{y + 72}" text-anchor="middle" font-family="AH" font-size="14" fill="#6d6f9c">{pc}</text>'
    svg += '</svg>'
    OD = OPT('D', 'The pattern map', 'One page at the back: every left-hand pattern of Level 0 as a stop on a road, with a famous piece beside each. In the lesson: colour in your new stop.',
      f"""<div class="mlab">The map page (coral = coloured in so far)</div><div class="dmap">{svg}</div>
<div class="sp"></div><div class="mlab">In the lesson: one line</div><div class="bline">{CHIP('C')}<span>On the map, colour in <b>the whole chord</b>.</span></div>""",
      'One page at the back; in each lesson only one line.')
    BODY = OA + OB + OC + OD
    if SONG.get('mock2'):   # her 8 Nov 13:27: 'if you made it for yourself': four new ideas, a page each
        def IDEA(n, title, idea, body, why):
            return page(f"""<div class="kick">Idea {n}</div><h1 class="mh1">{title}</h1><p class="lead">{idea}</p><div class="sp"></div>{body}<div class="sp"></div><div class="why"><b>Why it works:</b> {why}</div>""", n)
        MV = lambda n, g, t, w: f'<div class="mv"><span class="mvn">{n}</span>{g}<div><b>{t}</b><span>{w}</span></div></div>'
        DOWN = gl('down3', .8); RUN = '<svg width="46" height="32" viewBox="0 0 58 40"><circle cx="9" cy="28" r="5.5" fill="#26296b"/><circle cx="22" cy="28" r="5.5" fill="#26296b"/><circle cx="37" cy="14" r="5.5" fill="#26296b"/><circle cx="50" cy="14" r="5.5" fill="#26296b"/></svg>'
        I1 = IDEA(1, 'The Move Book', 'Like a chess opening book. Level 0 teaches about twelve moves; every song is written as a game made of moves you already know. A song you cannot read yet, you can still play from its moves.',
          f"""<div class="mlab">The moves so far</div><div class="mvs">{MV(1, DOWN, 'Three steps down', 'E D C')}{MV(2, RUN, 'Same, then a step up', 'C C C C D D D D')}</div>
<div class="sp"></div><div class="mlab">Hot Cross Buns, as a game</div><div class="game"><span>1.</span>{DOWN}<span>2.</span>{DOWN}<span>3.</span>{RUN}<span>4.</span>{DOWN}</div>
<div class="sp"></div>{mus('m_hcb')}<p class="cap2 cen" style="margin-top:10px">The first two moves, as notes. Read the moves first, the notes second.</p>
<div class="sp"></div><div class="bline"><span>Next song: <b>Mary</b> opens with move 1: you know its first three notes before you start.</span></div>""",
          'The book becomes a vocabulary, not a list of pieces. Each new song costs less to learn, and the child sees it.')
        def VAR(n, t, how, k=None): return f'<div class="var"><span class="varn">{n}</span><div class="vart"><b>{t}</b><span>{how}</span></div>' + (f'<div class="varm">{mus(k)}</div>' if k else '<div></div>') + '</div>'
        I2 = IDEA(2, 'One tune, ten lessons', 'Mozart wrote twelve variations on Twinkle. Here the whole of Level 0 is one theme: each lesson the child learns one new thing by making a new variation of the same tune. At the end they own a piece: My Variations on Hot Cross Buns.',
          f"""<div class="mlab">The theme</div>{mus('m_hcb')}
<div class="sp"></div><div class="mlab">The variations, one a lesson</div>
{VAR('Var. 1', 'The giant', 'every note twice as long: minim, semibreve', 'm_giant')}{VAR('Var. 2', 'The mouse', 'every note twice as fast: quavers', 'm_fast')}
{VAR('Var. 3', 'The left hand joins', 'C under every bar')}{VAR('Var. 6', 'In the dark', 'one note lower: minor')}{VAR('Var. 10', 'The waltz', 'in three, with the left hand: ONE two three')}""",
          'One tune the child knows by heart frees all attention for the new idea. The finished set is a real piece to perform, and the Mozart link comes for free.')
        ROWS = [('Melody', [1] * 8, 'L1'), ('Bass: the root', [0] * 4 + [1] * 4, 'L3'), ('Chords', [0] * 8, 'L7'), ('Drums', [0] * 8, 'always the band')]
        desk = '<div class="desk">' + ''.join(f'<div class="drow"><span class="dl">{n}</span>' + ''.join(f'<span class="dc{" me" if v else ""}">{"YOU" if v else ""}</span>' for v in bars) + f'<span class="dw">{w}</span></div>' for n, bars, w in ROWS) + '</div>'
        I3 = IDEA(3, 'Take over the band', 'Every song is a band of four layers on the listening page: melody, bass, chords, drums. The book is the mixing desk. Each lesson the child takes one layer away from the band and plays it themselves, until the band only drums.',
          f"""<div class="mlab">Lesson 3, Mary: who plays what</div>{desk}
<div class="sp"></div><div class="ctwo"><div class="cside"><div class="ch2">Your part today</div><p class="cap2">Melody all through, and the bass from bar 5: one key, the chord's own letter.</p></div><div class="cmid">+</div><div class="cside"><div class="ch2">The band's part</div><p class="cap2">Scan the code and switch the bass off: now you are the bass player.</p>{qr(URL, 54)}</div></div>""",
          'Accompaniment stops being an exercise; it is a job in a band. Progress is visible as YOU boxes filling the desk.')
        I4 = IDEA(4, 'Case files', 'Each lesson is a short detective case. A sound has gone missing from a famous piece; the clues are a pattern, a rhythm and a chord name. The child plays the clues, names the culprit, and stamps the case solved.',
          f"""<div class="case"><div class="caseh"><span>Case 9</span><b>The three-note chord</b><span class="solved">solved</span></div>
<div class="clues"><div class="clue"><div class="ah">Clue 1 · The sound</div>{qr(URL, 60)}<p class="cap2">Listen: three notes ring at once.</p></div>
<div class="clue"><div class="ah">Clue 2 · The shape</div><div class="amus">{mus('m_blk')}</div></div>
<div class="clue"><div class="ah">Clue 3 · The name</div>{CHIP('C', True)}</div></div>
<div class="mlab">The suspects: which piece is built on it?</div><div class="sus"><span>Bach, Prelude in C</span><span class="pick">Chopin, Prelude in C minor</span><span>Ravel, Boléro</span></div></div>""",
          'Children read to solve, not to obey. Every case ends with a famous piece in their ears and a stamp in the book.')
        BODY = I1 + I2 + I3 + I4
        css += f""".mvs{{display:grid;grid-template-columns:1fr 1fr;gap:12px}} .mv{{display:flex;align-items:center;gap:12px;border:1.5px solid {N};border-radius:10px;padding:10px 14px}} .mv b{{display:block;font-family:'PF',serif;font-size:18px}} .mv span{{font-size:14px;color:{MUTE}}} .mvn{{width:26px;height:26px;background:{N};color:#fff;font:700 14px 'AH';display:flex;align-items:center;justify-content:center;flex:none}}
.game{{display:flex;align-items:center;gap:10px;flex-wrap:wrap;font:700 18px 'PF';border-top:1px solid rgba(38,41,107,.2);border-bottom:1px solid rgba(38,41,107,.2);padding:10px 0}} .cen{{text-align:center}}
.var{{display:grid;grid-template-columns:64px 1fr 1.1fr;gap:12px;align-items:center;border-top:1px solid rgba(38,41,107,.15);padding:8px 0}} .varn{{font:700 14px 'AH';color:{C}}} .vart b{{display:block;font-family:'PF',serif;font-size:18px}} .vart span{{font-size:14px;color:{MUTE}}}
.desk{{display:grid;gap:6px}} .drow{{display:grid;grid-template-columns:130px repeat(8,1fr) 110px;gap:4px;align-items:center}} .dl{{font-weight:700;font-size:14px}} .dc{{height:34px;border:1.5px solid rgba(38,41,107,.3);border-radius:6px;font:700 11px 'AH';color:#fff;display:flex;align-items:center;justify-content:center}} .dc.me{{background:{C};border-color:{C}}} .dw{{font-size:12px;color:{MUTE};padding-left:6px}}
.case{{border:2px solid {N};border-radius:12px;padding:14px 16px}} .caseh{{display:flex;align-items:center;gap:12px;margin-bottom:10px}} .caseh span:first-child{{font:700 12px 'AH';letter-spacing:.16em;text-transform:uppercase;color:{C}}} .caseh b{{font-family:'PF',serif;font-size:22px;flex:1}} .solved{{border:2.5px solid {C};color:{C};font:700 13px 'AH';letter-spacing:.2em;text-transform:uppercase;padding:4px 10px;transform:rotate(-6deg)}}
.clues{{display:grid;grid-template-columns:1fr 1.4fr 1fr;gap:10px;margin-bottom:12px}} .clue{{border:1px dashed rgba(38,41,107,.4);border-radius:8px;padding:10px;display:flex;flex-direction:column;gap:6px;align-items:flex-start}} .sus{{display:flex;gap:10px;flex-wrap:wrap}} .sus span{{border:1.5px solid {N};border-radius:16px;padding:5px 12px;font-size:14px}} .sus .pick{{border-color:{C};outline:2.5px solid {C};outline-offset:2px}}
.why{{font-size:15px;border-left:3px solid {C};padding:4px 12px;color:#3d4080}}"""
    css += f""".mh1{{font-size:34px}} .mwhere{{font-size:14.5px;color:{MUTE};border-left:3px solid {C};padding:2px 10px;margin-top:6px}} .mlab{{font-size:11.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin:6px 0 8px}} .mnote{{font-size:12.5px;color:{MUTE}}}
.lcn.bigc{{font-size:40px;padding:8px 18px;display:inline-block;margin:6px 0}} .lcn{{display:inline-block}}
.abox{{padding:4px;display:grid;grid-template-columns:1fr 1fr 1.6fr 1.2fr;border:1.5px solid {N};border-radius:10px}} .acell{{padding:12px;border-right:1px solid rgba(38,41,107,.18);display:flex;flex-direction:column;gap:6px;align-items:flex-start}} .acell:last-child{{border-right:0}}
.anum{{width:24px;height:24px;background:{N};color:#fff;font:700 13px 'AH';display:flex;align-items:center;justify-content:center}} .ah{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{C}}} .amus{{width:100%}} .afam{{font-family:'PF',serif;font-size:18px;line-height:1.25;margin:4px 0}}
.minis{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}} .mini{{display:flex;align-items:center;gap:8px;border:1px solid rgba(38,41,107,.2);border-radius:8px;padding:8px;font-size:14px}} .mn{{font-weight:700;color:{MUTE}}}
.cards{{display:grid;grid-template-columns:1fr 1fr;gap:16px}} .card{{border:1.5px solid {N};border-radius:12px;padding:12px 14px;background:#fff}} .card.got{{background:#fbe3da33}} .ctop{{display:flex;justify-content:space-between;align-items:center}} .cn{{font-family:'PF',serif;font-size:20px;font-weight:700}}
.stamp{{font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#fff;background:{C};border-radius:10px;padding:2px 8px}} .stamp.e{{background:#fff;color:{MUTE};border:1px solid {MUTE}}} .cmus{{margin:6px auto;max-width:70%}} .clive{{font-size:10.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{C}}} .cpiece{{font-size:15px;line-height:1.35}}
.bline{{display:flex;align-items:center;gap:12px;border:1.5px dashed rgba(228,87,46,.6);border-radius:10px;padding:10px 14px;font-size:15.5px}}
.ctwo{{display:grid;grid-template-columns:1fr 40px 1.2fr;align-items:center;gap:8px}} .cside{{border:1.5px solid rgba(38,41,107,.25);border-radius:10px;padding:12px 14px}} .ch2{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{C};margin-bottom:8px}} .cmid{{font:700 34px 'PF';text-align:center}}
.cstrip{{display:grid;grid-template-columns:repeat(4,1fr);border-left:2px solid {N}}} .cbar{{border-right:2px solid {N};padding:14px 0;text-align:center}} .cmus2{{width:100%}} .dmap{{border:1.5px solid rgba(38,41,107,.2);border-radius:12px;padding:10px}}"""
if SONG.get('v3'):   # her 8 Nov 13:34: the whole approach changed -- every song is built from blocks; swap one block and it is your variation
    GLYPH['chord'] = '<svg width="58" height="40" viewBox="0 0 58 40"><circle cx="29" cy="8" r="5.5" fill="#26296b"/><circle cx="29" cy="20" r="5.5" fill="#26296b"/><circle cx="29" cy="32" r="5.5" fill="#26296b"/><path d="M17 4 v32 M41 4 v32" stroke="#e4572e" stroke-width="2.4" stroke-linecap="round"/></svg>'
    GLYPH['broken'] = '<svg width="58" height="40" viewBox="0 0 58 40"><circle cx="9" cy="32" r="5.5" fill="#26296b"/><circle cx="29" cy="20" r="5.5" fill="#26296b"/><circle cx="49" cy="8" r="5.5" fill="#26296b"/><path d="M13 29 L24 23 M33 17 L44 11" stroke="#e4572e" stroke-width="2.4" stroke-linecap="round"/></svg>'
    CHIP = lambda t, big=False: f'<span class="lcn{" bigc" if big else ""}">{t}</span>'
    STEP = lambda n, t, how: f'<div class="stp"><span class="stpn">{n}</span><div><div class="stpt">{t}</div><p class="how">{how}</p></div></div>'
    BRICKS = lambda cells: '<div class="bricks">' + ''.join(f'<div class="brk">{c}</div>' for c in cells) + '</div>'
    BC = f'<span class="bk">{gl("broken", .55)}<span>C E G</span></span>'
    ROWS = [('Melody', 'L1'), ('Bass: the root', 'L3'), ('Chords', 'new today'), ('Drums', 'the band')]
    DESK = '<div class="desk sm">' + ''.join(f'<div class="drow"><span class="dl">{nm}</span>' + ''.join(f'<span class="dc{" me" if i < 3 else ""}{" nw" if i == 2 else ""}">{"YOU" if i < 3 else ""}</span>' for _ in range(8)) + f'<span class="dw">{w}</span></div>' for i, (nm, w) in enumerate(ROWS)) + '</div>'
    def kbL(fm, frm, lab):
        SONG.update({'_kb_from': frm, 'kb_c': lab, '_kb_all': 1}); h = kb(width=290, fmap=fm); SONG.update({'_kb_from': None, 'kb_c': 'middle C', '_kb_all': 0}); return h
    P1 = page(f"""<div class="kick">Lesson {LESSON}</div><h1>{SONG["title"]}</h1>
<p class="lead">{LEAD}</p>
<div class="lw2">{LISTEN}{WOW}</div>
<div class="sp"></div>{STEP(1, 'A new block: the whole chord', 'Three keys at once, read from one name. Your left hand, below middle C.')}
<div class="nb"><div class="nbg">{gl('chord', 1.1)}</div><div class="nbc"><div class="nbk">{mus('brkC')}</div><p class="cap2">C E G together, fingers 5 3 1.</p></div>
<div class="nbc"><div class="nbk">{mus('brkG')}</div><p class="cap2">The same shape, slid down to G B D.</p></div></div>
<div class="sp"></div>{STEP(2, 'Build the song from blocks', 'The tune opens with a block you know: C E G, broken, one after another. The boxed names say when your chord block changes.')}
{BRICKS([BC, '', '', '', BC, '', '', ''][:4])}{mus('sing1')}<div class="sp"></div>{BRICKS([BC, '', '', ''])}{mus('sing2')}
<div class="sp"></div><div class="end">{ticks(['Played the chord blocks', 'Played the tune', 'Both together, slowly'], True)}</div>""", 1)
    BARS = '<div class="bang">' + ''.join(f'<div class="bb"><span class="bbn">{i}</span><span class="bbx"></span></div>' for i in range(1, 9)) + '</div>'
    P2 = page(f"""{STEP(3, 'Swap one block: your surprise', 'Haydn put his BANG in bar 8, to wake up the listeners. Move the BANG block somewhere else, and the song is your variation.')}
<div class="sp"></div><div class="mlab">Where does your BANG go? Mark one bar</div>{BARS}
<div class="swaps"><div class="sw"><div class="ah">Swap the loud block</div><p class="cap2">Haydn: soft, softer, BANG. Yours: loud first, then a whisper?</p></div>
<div class="sw"><div class="ah">Swap the chord block</div><p class="cap2">Play the tune over held roots (Lesson 7) instead of whole chords. Which sounds bigger?</p></div>
<div class="sw"><div class="ah">Name it</div><p class="cap2">Your variation needs a title:</p><span class="ib" style="width:170px"></span></div></div>
<div class="sp"></div><div class="mlab">Your band so far: who plays what</div>{DESK}
<div class="sp"></div><div class="yrs"><div><div class="sh">My Variations</div><p class="cap2">Add this one to your list at the back. In Lesson 10 you play them all, one after another: your own piece.</p></div>
<div class="menu"><div class="sh">5 minutes at home</div><ol><li>The chord blocks: C, then G</li><li>The tune with the band</li><li>Both hands, slowly</li><li>Your variation</li></ol><div class="days">{''.join(f'<span class="dy"><span class="bx"></span>{d}</span>' for d in 'MTWTFSS')}</div></div></div>
<div class="sp"></div><div class="end">{ticks(['Made my variation', 'Played it to someone'], True)}</div>""", 2)
    BODY = P1   # her 8 Nov 13:43: the first page is enough, nothing extra
    css += f""".stp{{display:flex;gap:12px;align-items:flex-start;border-top:1.5px solid {N};padding-top:10px}} .stpn{{width:30px;height:30px;background:{C};color:#fff;font:700 16px 'AH';display:flex;align-items:center;justify-content:center;flex:none;border-radius:50%}} .stpt{{font-family:'PF',serif;font-size:23px;font-weight:700}} .stp .how{{margin:2px 0 0}}
.nb{{display:grid;grid-template-columns:auto 1fr 1fr;gap:18px;align-items:center;border:1.5px solid rgba(38,41,107,.2);border-radius:10px;padding:8px 14px;margin-top:4px}} .nbk{{display:flex;align-items:center;gap:10px}} .nbk .mus{{flex:none;width:150px!important;max-width:150px;margin:0}} .lcn.bigc{{font-size:30px;padding:6px 14px;display:inline-block}} .lcn{{display:inline-block}}
.bricks{{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin:6px 0 -6px 60px}} .brk{{min-height:28px}} .bk{{display:inline-flex;align-items:center;gap:6px;border:1.5px solid {C};border-radius:8px;padding:4px 9px;font:700 13px 'AH';color:{N}}}
.mlab{{font-size:11.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C};margin:6px 0 8px}} .ah{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{C}}}
.bang{{display:grid;grid-template-columns:repeat(8,1fr);border-left:2px solid {N}}} .bb{{border-right:2px solid {N};display:flex;flex-direction:column;align-items:center;gap:6px;padding:8px 0}} .bbn{{font:700 13px 'AH';color:{MUTE}}} .bbx{{width:34px;height:34px;border:2px solid {N};border-radius:8px}} .bb:last-child .bbx{{background:#fbe3da;border-color:{C}}}
.swaps{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:14px}} .sw{{border:1.5px dashed rgba(228,87,46,.6);border-radius:10px;padding:10px 12px}}
.desk{{display:grid;gap:5px}} .drow{{display:grid;grid-template-columns:130px repeat(8,1fr) 90px;gap:4px;align-items:center}} .dl{{font-weight:700;font-size:13.5px}} .dc{{height:28px;border:1.5px solid rgba(38,41,107,.3);border-radius:6px;font:700 10.5px 'AH';color:#fff;display:flex;align-items:center;justify-content:center}} .dc.me{{background:{N};border-color:{N}}} .dc.nw{{background:{C};border-color:{C}}} .dw{{font-size:12px;color:{MUTE};padding-left:6px}}"""
if SONG.get('v4'):   # her 10 Nov: the accompaniment book as a book of jobs -- a real reason to play, one tool, then the same tool on more songs
    import re as _re
    def LS(line):   # a lead-sheet line: [C]word puts a boxed chord name over the word
        out = ''
        for m in _re.finditer(r'(\[([^\]]+)\])?([^\[]+)', line):
            ch = m.group(2)
            for i, w in enumerate(_re.findall(r'\s*\S+\s*', m.group(3))):   # word by word, so a long line wraps
                w = w.replace(' ', '\u00a0')
                out += f'<span class="cw"><span class="ch">{ch}</span>{w}</span>' if (ch and i == 0) else f'<span class="cw">{w}</span>'
        return f'<div class="lsl">{out}</div>'
    STEP = lambda n, t, how: f'<div class="stp"><span class="stpn">{n}</span><div><div class="stpt">{t}</div><p class="how">{how}</p></div></div>'
    def kbR(fm):
        SONG.update({'_kb_all': 1}); h = kb(width=240, fmap=fm); SONG.update({'_kb_all': 0}); return h
    def kbL(fm):
        SONG.update({'_kb_all': 1, 'kb_c': 'below middle C'}); h = kb(width=240, fmap=fm); SONG.update({'_kb_all': 0, 'kb_c': 'middle C'}); return h
    def GRID(lines, meter, words=True, rh=True, cls=''):   # her 10 Nov 22:19: both hands as letters in beat boxes, so the count is visible
        out = ''
        for li, bars in enumerate(lines):
            row = lambda f: ''.join(''.join(f(b, i) for i in range(meter)) for b in bars)
            tok = lambda s, i: (s.split() + ['-'] * meter)[i] if s else ''
            c = lambda b, i: ' b0' if i == 0 else ''
            half = lambda t: ('<span class="hbx">' + ''.join(f'<span>{x}</span>' for x in t.split('.')) + '</span>') if '.' in t else t
            cell = lambda t, k, b0: f'<td class="{k}{b0}">' + ('<span class="lhn">L.H.</span>' if t.startswith('<') else '<i class="hold"></i>' if t == '-' else '<i class="rst"></i>' if t == 'r' else half(t)) + '</td>'   # r: a rest, an empty box with a quiet dot
            cnt = '<tr class="cnt"><th></th>' + row(lambda b, i: f'<td class="cn{c(b, i)}">{i + 1}</td>') + '</tr>'
            FM = SONG.get('gig', {}).get('rfing', {'C': 1, 'D': 2, 'E': 3, 'F': 4, 'G': 5})   # her 22:37: finger numbers on top, the count between letters and words
            fg = lambda t: '' if t in ('-', '', 'r') or t.startswith('<') else '.'.join(str(FM.get(x, '')) for x in t.split('.'))
            if rh and 'big' in cls:
                r = '<tr class="mbfr"><th></th>' + row(lambda b, i: f'<td class="mbfn{c(b, i)}">{half(fg(tok(b.get("r", ""), i)))}</td>') + '</tr>'
                r += '<tr class="rh"><th>R.H.</th>' + row(lambda b, i: cell(tok(b.get('r', ''), i), 'rl', c(b, i))) + '</tr>' + ('<tr class="cnt"><th></th>' + row(lambda b, i: f'<td class="cn mbcm{c(b, i)}">' + (half(f'{i + 1}.&') if '.' in tok(b.get('r', ''), i) else str(i + 1)) + '</td>') + '</tr>')
            else:
                r = '' if ('sm' in cls or (li and ('big' not in cls or 'mid' in cls))) else cnt
                if rh: r += '<tr class="rh"><th>R.H.</th>' + row(lambda b, i: cell(tok(b.get('r', ''), i), 'rl', c(b, i))) + '</tr>'
            if rh and words: r += '<tr class="wd"><th></th>' + row(lambda b, i: f'<td class="w{c(b, i)}">{half(tok(b.get("w", ""), i)) if tok(b.get("w", ""), i) != "-" else ""}</td>') + '</tr>'
            if 'sm' in cls: r += '<tr class="lh"><th></th>' + ''.join(f'<td class="ll b0 span" colspan="{meter}"><span class="ch2">{b["l"]}</span><i class="hold"></i></td>' for b in bars) + '</tr>'   # a small card: the chord holds the whole bar
            else: r += '<tr class="lh"><th>L.H.</th>' + row(lambda b, i: f'<td class="ll{c(b, i)}">' + ((f'<span class="ch2 two">{b["l"].split("+")[1]}<br>{b["l"].split("+")[0]}</span>' if '+' in b['l'] else f'<span class="ch2">{b["l"]}</span>') if i == 0 and b.get('l') else f'<b class="hk2">{tok(b.get("r", ""), i)[1:]}</b>' if tok(b.get('r', ''), i).startswith('<') else '<i class="hold"></i>' if (b.get('l') or (i and tok(b.get('r', ''), i) == '-' and any(tok(b.get('r', ''), j).startswith('<') for j in range(i)))) else '') + '</td>') + '</tr>'
            out += f'<table class="bgt {cls}">{r}</table>'
        return out
    half = lambda t: ('<span class="hbx">' + ''.join(f'<span>{x}</span>' for x in t.split('.')) + '</span>') if '.' in t else t
    FIFTH = {'C': 'G', 'F': 'C', 'G': 'D'}
    def WAYS(ways, how, roots=('C', 'G')):   # her 10 Nov 23:13: the root alone, in new rhythms, before the fifth joins -- one song, several left hands
        cards = ''
        for t, pat in ways:
            toks = sum((pat.translate(str.maketrans('CG', r + FIFTH[r])).split() for r in roots), [])   # the same way on each chord: C, (F,) G
            nb = len(toks) // len(roots)
            cn = ''.join(f'<td class="cn{" b0" if i % nb == 0 else ""}">' + (half(f'{i % nb + 1}.&') if '.' in x else str(i % nb + 1)) + '</td>' for i, x in enumerate(toks))
            ll = ''.join(f'<td class="ll{" b0" if i % nb == 0 else ""}">' + ('<i class="hold"></i>' if x == '-' else '<i class="rst"></i>' if x == 'r' else ('<span class="hbx">' + ''.join(f'<span>{"<i class=" + chr(34) + "rst" + chr(34) + "></i>" if y == "r" else "<b class=" + chr(34) + "hk" + chr(34) + ">" + y + "</b>"}</span>' for y in x.split('.')) + '</span>') if '.' in x else f'<span class="ch2 two">{x.split("+")[1]}<br>{x.split("+")[0]}</span>' if '+' in x else f'<span class="ch2">{x}</span>') + '</td>' for i, x in enumerate(toks))
            t, sub = (t + '|').split('|')[:2]
            cards += f'<div class="way"><div class="wayt">{t}<span class="ways2">{sub}</span></div><table class="bgt wy"><tr class="cnt">{cn}</tr><tr class="lh">{ll}</tr></table></div>'
        return f'<div class="mb-ways"><p class="how">{how}</p><div class="ways">{cards}</div></div>'
    G = SONG['gig']
    LSH = ''.join(f'<div>{"".join(LS(l) for l in col)}</div>' for col in G.get('song', []))
    P1 = page(f"""<div class="kick">Lesson {LESSON} · The job</div><h1>{SONG['title']}</h1>
<div class="job"><div><div class="ah">The job</div><p class="jobt">{G['job']}</p></div><div class="jobq">{qr(URL, 52)}<span>Hear it with the band</span></div></div>
<div class="sp"></div>{STEP(1, 'The tool: ' + G['tool'], G['tool_how'])}
<div class="tool"><div>{kbL(G['fmap'])}</div><div class="toolm">{GRID([G['tool_grid']], SONG['beats'], rh=False, cls='tg') if G.get('grid') else mus('tool')}<p class="cap2">{G['tool_cap']}</p></div></div>
<div class="sp"></div>{STEP(2, 'The song: ' + G['song_title'], G['song_how'])}
{('<div class="gsong">' + GRID(G['song_grid'], SONG['beats']) + '</div>') if G.get('grid') else '<div class="lsheet">' + LSH + '</div>'}{('<p class="cap2 nxt">' + G['note'] + '</p>') if G.get('note') else ''}
<div class="sp"></div>{STEP(3, 'Same tool, three more songs', G.get('more_how', 'Sing the first line, play the boxes, then carry on to the end.'))}
{('<div class="gmore">' + ''.join(f'<div class="gm"><div class="lmt">{t}</div>{GRID([l[:2], l[2:]], SONG["beats"], words=False, cls="sm")}</div>' for t, l in G['more']) + '</div>') if G.get('grid') else '<div class="lmore">' + ''.join(f'<div class="lm"><div class="lmt">{t}</div>{LS(l)}</div>' for t, l in G['more']) + '</div>'}
<div class="sp"></div><div class="real"><span class="ah">The real test</span><span>{G['real']}</span></div>
<div class="end">{ticks(G['ticks'], True)}</div>""", LESSON)
    if G.get('simple'):   # her 10 Nov 22:29: the Music Box opens here -- no numbers, no extra songs, the whole song big: 'oh, I can do this'
        P1 = page(f"""<div class="kick">{SONG['label']}</div><h1>{SONG['title']}</h1>
<div class="mb-intro"><p>{G['job']}</p><div class="jobq">{qr(URL, 48)}<span>Hear it first</span></div></div>
<div class="mb-hands"><div><div class="ah">Left hand</div>{kbL(G['fmap'])}<p class="cap2">{G['tool_cap']}</p></div><div><div class="ah">Right hand</div>{kbR(G['rmap'])}<p class="cap2">{G['r_cap']}</p></div></div>
<div class="sp"></div><div class="mb-song"><div class="ah">The song</div><p class="how">{G['song_how']}</p>{GRID(G['song_grid'], SONG['beats'], cls='big' + (' mid' if len(G['song_grid']) > 3 else ' tri' if len(G['song_grid']) == 3 else ''))}</div>
<div class="sp"></div><div class="end">{ticks(G['ticks'], True)}</div>""", LESSON)
        if G.get('ways'):
            W = G['ways']
            P1 += page(f"""<div class="kick">{SONG['label']} · The left hand, again</div><h1>{G.get('ways_title', 'Four new ways')}</h1>
<div class="mb-intro"><p>{G['ways_job']}</p></div>
<div class="sp"></div>{WAYS(W, G.get('ways_how', ''), G.get('ways_roots', ('C', 'G')))}
<div class="sp"></div><div class="say"><div class="ah">Say it, tap it, play it</div><p>Say the name of the way out loud in time. Tap it on your knee with the left hand. Then play it with the song.</p></div>
<div class="sp"></div><div class="end">{ticks([w[0].split('|')[0] for w in W], True)}</div>""", LESSON)
    BODY = P1
    css += f""".mb-intro{{display:flex;justify-content:space-between;align-items:center;gap:20px;border-top:1.5px solid {N};border-bottom:1.5px solid {N};padding:10px 0}} .mb-intro p{{font-size:19px;margin:0}}
.mb-hands{{display:grid;grid-template-columns:1fr 1fr;gap:28px}} .mb-hands>div{{display:grid;gap:10px;justify-items:start;align-content:start}} .mb-hands .cap2{{margin:0}} .pg:has(.mid) .mb-hands svg{{width:136px!important}} .pg:has(.mid) .mb-intro{{padding:6px 0}} .pg:has(.mid) .mb-hands>div{{gap:6px}} .pg:has(.mid) .mb-hands .ah{{margin-bottom:16px}} .mb-song{{display:grid;gap:8px}} .mb-song .how{{margin:0}} .bgt.big .rl{{font-size:32px;height:62px}} .bgt.big .w{{font-size:13.5px;height:22px}} .bgt.big .ll{{height:62px}} .bgt.big .ch2{{font-size:21px;padding:2px 5px}} .bgt.big .cn{{font-size:12.5px;height:20px}} .bgt.big+.bgt.big{{margin-top:30px}} .bgt.big th{{width:44px}} .lhn{{font:700 11px 'AH';letter-spacing:.06em;color:{MUTE}}} .hk2{{font:700 26px 'AH';color:{N}}} .bgt.big.mid .hk2{{font-size:18px;line-height:.9;display:inline-block}} .lhn{{line-height:1;display:inline-block}} .ch2.two{{line-height:1.05;padding:3px 5px!important;font-size:16px!important}} .bgt.wy .ll{{height:58px!important}} .bgt.big .ll:has(.two){{height:64px}} .bgt.big .ch2.two{{font-size:17px!important}} .mb-ways{{display:grid;gap:8px}} .mb-ways .how{{margin:4px 0 0}} .ways{{display:grid;grid-template-columns:1fr;gap:14px}} .way{{display:grid!important;grid-template-columns:190px 1fr;align-items:center;gap:16px}} .wayt{{flex-direction:column;align-items:flex-start!important;gap:2px!important}} .way{{border:1px solid rgba(38,41,107,.2);border-radius:10px;padding:12px 14px 14px}} .wayt{{font-family:'PF',serif;font-weight:700;font-size:22px;margin-bottom:4px;display:flex;justify-content:space-between;align-items:baseline;gap:6px}} .ways2{{font:600 14px 'AH';color:{MUTE};font-style:normal;white-space:nowrap}} .wayt{{white-space:nowrap}} .bgt.wy .ll{{height:52px}} .bgt.wy .cn{{height:22px;font-size:12.5px}} .bgt.wy .ch2{{font-size:18px;padding:1px 4px}} .hk{{font:700 18px 'AH';color:{N}}} .say{{border-top:1.5px solid {N};padding-top:10px}} .say p{{font-size:17px;margin:6px 0 0}} .bgt.wy .hbx{{width:calc(100% - 10px)}} .rst{{display:block;margin:0 auto;width:7px;height:7px;border-radius:50%;border:1.5px solid rgba(38,41,107,.35)}} .bgt.big.tri .rl{{font-size:27px;height:36px}} .bgt.big.tri .ll{{height:40px}} .bgt.big.tri .w{{height:17px}} .bgt.big.tri .mbfn{{height:17px}} .bgt.big.tri .ch2{{font-size:19px;padding:1px 5px}} .bgt.big.tri+.bgt.big.tri{{margin-top:8px}} .bgt .mbfn{{font:700 13px 'AH';color:{C};height:22px;vertical-align:bottom}} .bgt .mbcm{{vertical-align:middle!important;height:24px!important;border-top:1px solid rgba(38,41,107,.1);font-size:12.5px}} .bgt.big.mid .mbfn{{height:14px;font-size:11.5px}} .hbx{{display:flex;width:calc(100% - 12px);margin:0 auto;line-height:1}} .hbx>span{{flex:1;display:flex;align-items:center;justify-content:center}} .hbx>span+span{{border-left:1px dashed rgba(38,41,107,.3)}} .rl .hbx{{font-size:.78em}} .w .hbx{{font-size:.92em}} .bgt.big.mid .rl{{font-size:24px;height:31px}} .bgt.big.mid .mbcm{{height:20px!important;font-size:11.5px}} .bgt.big.mid .mbcm .hbx{{font-size:9.5px}} .bgt.big.mid .w{{height:13px;font-size:12px}} .bgt.big.mid .ll{{height:34px}} .bgt.big.mid .cn{{height:17px}} .bgt.big.mid .ch2{{font-size:16px;padding:0 5px}} .bgt.big.mid+.bgt.big.mid{{margin-top:4px}} .pg:has(.mid) .mb-song{{gap:5px}} .pg:has(.mid) .mb-song .how{{margin-top:4px!important}}
"""
    css += f""".job{{display:grid;grid-template-columns:1fr auto;gap:18px;align-items:center;border:1.5px solid {C};border-radius:12px;padding:10px 16px}} .jobt{{font-size:17px;margin:4px 0 0}} .jobq{{display:flex;flex-direction:column;align-items:center;gap:4px;white-space:nowrap;font-size:11.5px;color:{MUTE}}}
.ah{{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:{C}}}
.stp{{display:flex;gap:12px;align-items:flex-start;border-top:1.5px solid {N};padding-top:10px}} .stpn{{width:30px;height:30px;background:{C};color:#fff;font:700 16px 'AH';display:flex;align-items:center;justify-content:center;flex:none;border-radius:50%}} .stpt{{font-family:'PF',serif;font-size:23px;font-weight:700}} .stp .how{{margin:2px 0 0}}
.tool{{display:grid;grid-template-columns:auto 1fr;gap:24px;align-items:center;margin-top:4px}} .toolm .mus{{margin-left:0!important}}
.lsheet{{display:grid;grid-template-columns:repeat(auto-fit,minmax(0,1fr));gap:4px 24px;margin:2px 0 0 42px}} .lsheet>div{{display:grid;gap:2px}} .lsl{{display:flex;flex-wrap:wrap;align-items:flex-end;font-size:17.5px;line-height:1.12}} .cw{{position:relative;padding-top:21px;white-space:pre}} .ch{{position:absolute;left:0;top:0;text-transform:none;letter-spacing:0;font:700 14px 'AH';color:{N};border:1.5px solid {N};border-radius:4px;padding:0 6px;line-height:1.3}} .ch.e{{visibility:hidden}}
.nxt{{margin-left:42px;color:{MUTE}}} .lmore{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-left:42px}} .lm{{border:1px solid rgba(38,41,107,.2);border-radius:8px;padding:8px 10px}} .lm .lsl{{font-size:14.5px;row-gap:2px}} .lm .cw{{padding-top:20px}} .lm .cw{{white-space:normal}} .toolm .cap2{{margin-top:6px}} .lm .ch{{font-size:13px}} .lmt{{font-family:'PF',serif;font-weight:700;font-size:16px;margin-bottom:2px}}
.bgt{{border-collapse:collapse;table-layout:fixed;width:100%}} .bgt th{{width:40px;font:700 11px 'AH';letter-spacing:.08em;color:{MUTE};text-align:left;padding:0}} .bgt td{{text-align:center;padding:0;border-left:1px solid rgba(38,41,107,.14)}} .bgt td.b0{{border-left:2px solid {N}}} .bgt tr td:last-child{{border-right:2px solid {N}}}
.bgt .cn{{font-size:11px;color:{MUTE};height:16px;vertical-align:bottom}} .bgt .rl{{font:700 21px 'AH';height:31px;border-top:1px solid rgba(38,41,107,.14)}} .bgt .w{{font-size:11.5px;letter-spacing:-.01em;color:{MUTE};height:17px;vertical-align:top}} .bgt .ll{{height:36px;border-top:1px solid rgba(38,41,107,.14);border-bottom:1px solid rgba(38,41,107,.14)}}
.ch2{{display:inline-block;font:700 17px 'AH';border:1.5px solid {N};border-radius:4px;padding:0 5px;line-height:1.35}} .hold{{display:block;margin:0 auto;width:60%;border-top:2px solid rgba(38,41,107,.3)}}
.gsong{{display:grid;gap:8px;margin-left:42px}} .tg{{width:auto}} .tg td{{width:44px}} .gmore{{display:grid;gap:8px;margin-left:42px}} .gm{{display:grid;grid-template-columns:150px 1fr;align-items:center;gap:8px}} .gm .lmt{{font-size:15px;margin:0}} .bgt.sm .rl{{font-size:17px;height:28px}} .bgt.sm .ll{{height:32px}} .bgt.sm .ch2{{font-size:14px;padding:0 6px}} .gmore{{grid-template-columns:repeat(3,minmax(0,1fr));gap:12px!important}} .gm{{display:block!important;border:1px solid rgba(38,41,107,.2);border-radius:8px;padding:6px 10px 8px}} .gm .lmt{{margin-bottom:2px!important}} .bgt.sm th{{display:none}} .bgt.sm .hold{{width:45%}} .bgt.sm .ch2{{font-size:14px!important;padding:0 5px!important}} .bgt .span{{text-align:left;padding-left:6px;white-space:nowrap}} .bgt .span .hold{{display:inline-block;vertical-align:middle;width:calc(100% - 34px);margin-left:5px}} .gm{{padding:6px 5px 8px!important}} .gmore{{gap:7px!important}} .pg:has(.gsong) .sp{{min-height:6px!important}} .bgt.sm+.bgt.sm{{margin-top:6px}}
.pg:has(.job) .sp{{min-height:12px}} .real{{display:flex;gap:14px;align-items:center;border:1.5px dashed rgba(228,87,46,.6);border-radius:10px;padding:10px 14px;font-size:16px}}"""
BODY = ready_pages() if SONG.get('kind') == 'ready' else BODY if (SONG.get('mock') or SONG.get('v3') or SONG.get('v4')) else P1 + P2 + P3 + P4
PAGINATE = r"""<script>
// Pages grow, the music never shrinks (her 7 Nov 14:11). Each part starts on its own page (14:34: '3번이 페이지 중간에 오지 않게').
// Inside a part, the blocks go in groups: a heading or a tune's name with its words and its lines. A group that does not fit
// goes to the next page whole; a tune too tall for any page is cut between its lines, about half and half.
function paginate(){
  const fits = b => b.scrollHeight <= b.clientHeight + 0.5;
  const starts = k => k.matches('.ph, .sub, .kick');
  // a tune a little too tall for a page alone: its lines a little smaller (never below 85%) rather than cut
  const shrink = g => { const ms = g.filter(k => k.matches('.mus')), b = ms.length && ms[0].closest('.body'); if (!b) return false; const w = ms.map(m => m.getBoundingClientRect().width), w0 = ms.map(m => m.style.maxWidth);
    for (let f = 0.98; f >= 0.85; f -= 0.01) { ms.forEach((m, i) => m.style.maxWidth = (w[i] * f) + 'px'); if (fits(b)) return true; }
    ms.forEach((m, i) => m.style.maxWidth = w0[i]); return false; };
  const newPage = pg => { const nx = pg.cloneNode(true), nb = nx.querySelector('.body'); nb.innerHTML = ''; nb.classList.add('cont'); pg.after(nx); return nx; };
  for (const pg0 of [...document.querySelectorAll('.pg')]) {
    const body0 = pg0.querySelector('.body'); if (fits(body0)) continue;
    // case by case (her 15:55-15:56): a part that runs over by a little is drawn a little smaller to keep it on one page,
    // never below 85% of its size; more than that, and it goes on to the next page at full size
    { const ms = [...body0.querySelectorAll('.mus')], w0 = ms.map(m => m.style.maxWidth);
      const over = body0.scrollHeight - body0.clientHeight, mh = ms.reduce((h, m) => h + m.getBoundingClientRect().height, 0);
      const lo = body0.querySelector(':scope > .ph .pn') && body0.querySelector(':scope > .ph .pn').textContent.trim() === '+' ? 0.8 : 0.85;   // More to play: down to 80%
      if (ms.length) {   // always try: the spacers close up a little too (her 16:52: no half-empty last pages)
        body0.querySelectorAll(':scope > .sp').forEach(k => k.style.minHeight = '16px');
        for (let f = 0.98; f >= lo; f -= 0.01) { ms.forEach(m => { const r = m.parentElement.getBoundingClientRect().width, cur = m.getBoundingClientRect().width; m.dataset.w = m.dataset.w || cur; m.style.maxWidth = (m.dataset.w * f) + 'px'; }); if (fits(body0)) break; }
        if (fits(body0)) continue;
        ms.forEach((m, i) => { m.style.maxWidth = w0[i]; delete m.dataset.w; }); body0.querySelectorAll(':scope > .sp').forEach(k => k.style.minHeight = ''); } }
    const items = [...body0.children], groups = [];
    for (const k of items) { if (!groups.length || (starts(k) && groups[groups.length - 1].some(x => !x.matches('.sp')))) groups.push([]); groups[groups.length - 1].push(k); }
    body0.innerHTML = ''; let pg = pg0, cur = body0;
    const put = (g) => { g.forEach(k => cur.append(k)); };
    const take = (g) => { g.forEach(k => k.remove()); };
    const fresh = () => { pg = newPage(pg); cur = pg.querySelector('.body'); };
    const lone = () => !cur.children.length;
    for (let g of groups) {
      put(g); if (fits(cur)) continue; take(g);
      if (!g.some(k => k.matches('.mus, .trk, .lpat')) && g.reduce((h, k) => h + k.getBoundingClientRect().height, 0) < 160) {
        const sps = [...cur.querySelectorAll(':scope > .sp')]; sps.forEach(k => k.style.minHeight = '12px'); put(g); if (fits(cur)) continue; take(g); sps.forEach(k => k.style.minHeight = ''); }
      const used = () => [...cur.children].filter(k => !k.matches('.sp')).reduce((h, k) => h + k.getBoundingClientRect().height, 0) / cur.clientHeight;   // spacers stretch, so they do not count
      let most = false;   // the page is less than half full: fill it, cutting the group between its lines, rather than leave it empty
      if (!lone() && used() < 0.5 && g.some(k => k.matches('.mus'))) most = true;
      else if (!lone()) { fresh(); put(g); if (fits(cur) || shrink(g)) continue; take(g); }
      else { put(g); if (shrink(g)) continue; take(g); }
      // too tall for a page: cut between its lines. On a page already started, only if at least half the tune stays there;
      // on a new page, about half and half. What is left goes on a new page, whole if it fits (a little smaller if need be).
      while (g.length) {
        const lines = g.map((k, i) => k.matches('.mus') ? i : -1).filter(i => i >= 0), L = lines.length;
        let done = false;
        if (L > 1) for (let n = most ? L - 1 : Math.ceil(L / 2); n >= Math.ceil(L / 2); n--) { const a = g.slice(0, lines[n - 1] + 1); put(a); if (fits(cur) || shrink(a)) { g = g.slice(lines[n - 1] + 1); done = true; break; } take(a); }
        if (!done) { if (most || !lone()) { most = false; fresh(); put(g); if (fits(cur) || shrink(g)) { g = []; break; } take(g); continue; } put(g); g = []; break; }
        most = false;
        while (g.length && g[0].matches('.sp')) g.shift().remove();
        if (!g.length) break;
        fresh(); put(g); if (fits(cur) || shrink(g)) { g = []; break; } take(g);
        if (!g.some(k => k.matches('.mus'))) {   // only the ticks are left: close up the last page's spacers rather than give them a page
          put(g); g = []; break; }
      }
    }
  }
  document.querySelectorAll('.pg').forEach(pg => { const b = pg.querySelector('.body'); while (b.firstElementChild && b.firstElementChild.matches('.sp') && b.classList.contains('cont')) b.firstElementChild.remove(); });
  document.querySelectorAll('.pg .foot span').forEach((f, i) => f.textContent = i + 1);
  window.__paged = 1;
}
(document.fonts ? document.fonts.ready : Promise.resolve()).then(() => requestAnimationFrame(paginate));
</script>"""
html = f'<!doctype html><html><head><meta charset="utf-8"><title>Lesson {LESSON}: {SONG["title"]}</title><style>{FF}</style><style>{css}</style></head><body>{BODY}{PAGINATE}</body></html>'
open(sys.argv[3], 'w').write(html); print('ok', len(html))
