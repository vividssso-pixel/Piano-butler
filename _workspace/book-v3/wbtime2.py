# The Piano Butler Workbook, Time (expanded): two pages per topic (Learn, Use), stars for difficulty, review, progress, answers
exec(open('/tmp/claude-0/pk/wbtime.py').read())   # helpers, css, W (snippets), old pages
N_ = N
import sys as _sy2, re as _re2; _sy2.path.insert(0, '/tmp/claude-0/pk'); import importlib as _il2, pagemap as PM; _il2.reload(PM)
WMINCSS = """
/* her 5 Nov: the Workbook keeps the Handbook's minimum sizes: nothing under 14px except tiny labels */
.ht{font-size:15px!important} .ht td{font-size:15px!important} .ansT td{font-size:14px!important} .ansS td{font-size:13px!important;padding-top:4px!important;padding-bottom:4px!important;line-height:1.38!important} .fc .add,.add{font-size:14.5px!important} .mu2{font-size:14px!important} .pzl{font-size:14px!important}
.add:has(.wl ~ .wl) .wl{width:50px!important} .rem2{font-size:15px!important} .how{font-size:15px!important;margin:2px 0 6px!important} .row{font-size:15px!important} .sent p{font-size:15px!important}
"""
import base64 as _b64h, os as _osh
_WBH = {'Pulse and the bar': 'T1', 'Notes and rests': 'T2', 'How long is a note?': 'T3', 'Time signatures': 'T4', 'Compound and irregular time': 'T5', 'Groups and upbeats': 'T6', 'Off the beat': 'T7',
        'The keyboard': 'P1', 'Reading the notes': 'P3', 'Sharps, flats and naturals': 'P6', 'Scales': 'S1',
        'Chords and triads': 'H1', 'Four kinds of triad': 'H2', 'Chords in a key': 'H3', 'Seventh chords': 'H5', 'Colour chords': 'H6', 'The tower': 'H7', 'Slash chords': 'H8', 'Chords from outside the key': 'M1', 'Cadences': 'M2', 'Chords under a melody': 'M3'}
def _wbheroes(h):   # her 6 Nov: each Learn page shows the Handbook chapter's opening picture beside its Remember line (heroes/ from heroshot.js)
    def rep(m):
        k = _WBH.get(m.group(2).split(' · ')[1].strip()) if m.group(2).count(' · ') >= 2 else None; f = f'/tmp/claude-0/pk/heroes/{k}.png' if k else None
        if not f or not _osh.path.exists(f): return m.group(0)
        img = 'data:image/png;base64,' + _b64h.b64encode(open(f, 'rb').read()).decode()
        mh = {'T2': 64, 'H1': 66, 'H2': 82, 'H7': 92, 'P7': 76}.get(k, 108)   # a smaller picture where the page is already full
        return f'<div class="wbhd"><div>{m.group(1)}</div><img src="{img}" alt="" style="max-height:{mh}px;max-width:{32 if k == 'P7' else 46}%"></div><p class="rem2">{m.group(4)}</p>'
    h = _re2.sub(r'(<div class="kick">([^<]*?)</div><h1>.*?</h1>)<p class="rem2">(?P<x>)(.*?)</p>', lambda m: rep(m) if m.group(2).endswith('· Learn') else m.group(0), h, flags=_re2.S)
    return h.replace('</style></head>', '.wbhd{display:flex;align-items:flex-end;justify-content:space-between;gap:14px;margin-bottom:4px} .wbhd>div{flex:1;min-width:0} .wbhd img{height:auto;max-height:108px;max-width:46%;object-fit:contain;flex:0 1 auto;margin-bottom:2px}</style></head>', 1)
def _LG(h):   # workbook pages still name Handbook pages in the pre-5-Nov numbering; map them to the live page map
    h = h.replace('</style></head>', WMINCSS + '</style></head>', 1)
    h = _wbheroes(h)
    return _re2.sub(r'\b([Pp]\.(?: |&nbsp;|\u00a0))(\d\d)\b', lambda m: m.group(1) + str(PM.legacy(int(m.group(2))) if int(m.group(2)) >= 22 else m.group(2)), h)
def star(n): return '★' * n + '<span class="so">' + '★' * (3 - n) + '</span>'
def ex(n, title, stars, how, body):
    return f'<div class="ex2"><div class="eh"><span class="en">{n}</span><b>{title}</b><span class="el">{star(stars)}</span></div><p class="how">{how}</p>{body}</div>'
def tp(kind, topic, title, rule, inner, n, hb):
    hb = hb - 2   # Part II now starts at p. 34 (her 5 Nov, four parts)
    return wpage(f'<div class="kick">Time · {topic} · {kind}</div><h1>{title}</h1><p class="rem2"><span>Remember</span>{rule}</p>{inner}', n, hb)
def staff(ts='', bars=2, h=74, heads=None, stems=None):
    W_ = 600; y0 = 14; s = ''.join(f'<line x1="10" x2="{W_ - 10}" y1="{y0 + i * 12}" y2="{y0 + i * 12}" stroke="{N_}" stroke-width="1.3"/>' for i in range(5))
    x0 = 10
    if ts:
        a, b = ts.split('/'); s += f'<text x="26" y="{y0 + 22}" text-anchor="middle" font-family="PF" font-size="26" font-weight="700" fill="{N_}">{a}</text><text x="26" y="{y0 + 46}" text-anchor="middle" font-family="PF" font-size="26" font-weight="700" fill="{N_}">{b}</text>'; x0 = 44
    for k in range(1, bars + 1):
        x = x0 + (W_ - 10 - x0) * k / bars
        s += f'<line x1="{x:.0f}" x2="{x:.0f}" y1="{y0}" y2="{y0 + 48}" stroke="{N_}" stroke-width="{4 if k == bars else 1.3}"/>'
    for i, (x, y) in enumerate(heads or []):
        s += f'<ellipse cx="{x}" cy="{y}" rx="7.2" ry="5.2" transform="rotate(-20 {x} {y})" fill="{N_}"/>'
        if stems and i in stems: s += f'<line x1="{x + 6.5}" x2="{x + 6.5}" y1="{y - 1}" y2="{y - 36}" stroke="{C}" stroke-width="1.6"/>'
    return f'<figure class="vx"><svg viewBox="0 0 {W_} 76" style="width:100%;height:auto;display:block">{s}</svg></figure>'
def opts(keys, h=56):
    return '<div class="op3">' + ''.join(f'<div class="opc"><span class="ol">{"ABC"[i]}</span>{wx(k, h)}</div>' for i, k in enumerate(keys)) + '</div>'
def grid(cells, cols=3, cls=''): return f'<div class="fills {cls}" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(cells) + '</div>'
WL = '<span class="wl"></span>'   # centred writing line (her 4 Nov)
def cell(k, lab, h=70): return f'<div class="fc">{wx(k, max(h, 78))}<div class="add">{lab.replace(BOX, WL)}</div></div>'
import math as _m
def pizza(n, fill=0, R=34, rest=False):   # a circle cut into n equal slices; the first `fill` slices red (a rest: shaded with lines)
    cx = cy = R + 3; s = f'<svg viewBox="0 0 {2 * R + 6} {2 * R + 6}" style="width:{2 * R + 6}px;height:{2 * R + 6}px;display:block;margin:0 auto"><defs><pattern id="hz" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="5" height="5" fill="#fff"/><line x1="0" y1="0" x2="0" y2="5" stroke="{N_}" stroke-width="1.4"/></pattern></defs>'; FC = 'url(#hz)' if rest else C
    if n == 1:
        s += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{FC if fill else "#fff"}" fill-opacity="{0.85 if fill and not rest else 1}" stroke="{N_}" stroke-width="2"/>'
    else:
        sl = sorted([(-_m.pi / 2 + 2 * _m.pi * j / n, -_m.pi / 2 + 2 * _m.pi * (j + 1) / n) for j in range(n)], key=lambda a: (round(_m.cos((a[0] + a[1]) / 2), 3), round(_m.sin((a[0] + a[1]) / 2), 3)))   # left to right, like counting
        for i, (a0, a1) in enumerate(sl):
            x0, y0, x1, y1 = cx + R * _m.cos(a0), cy + R * _m.sin(a0), cx + R * _m.cos(a1), cy + R * _m.sin(a1)
            s += f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} Z" fill="{FC if i < fill else "#fff"}" fill-opacity="{1 if rest else 0.85}" stroke="{N_}" stroke-width="1.6"/>'
    return s + '</svg>'
def wcarriage(seats, x0):   # a bar as a carriage; seats = [(kind, n, key)]: 'n' booked note, 'r' booked rest, 'x' empty seats to book, 'd' booked as the worked example
    W = 54; n_all = sum(t[1] for t in seats); w = n_all * W + 16
    o = f'<rect x="{x0}" y="18" width="{w}" height="62" rx="10" fill="#fff" stroke="{N_}" stroke-width="2"/><circle cx="{x0 + 22}" cy="88" r="7" fill="{N_}"/><circle cx="{x0 + w - 22}" cy="88" r="7" fill="{N_}"/>'
    x = x0 + 8
    for kind, n, k in seats:
        if kind == 'x':
            o += f'<rect x="{x + 3}" y="30" width="{n * W - 6}" height="40" rx="6" fill="#fff" stroke="{N_}" stroke-width="1.4" stroke-dasharray="4 3"/>'
        else:
            fill = '#f2b9a5' if kind in 'nd' else 'url(#hz3)'
            o += f'<rect x="{x + 3}" y="30" width="{n * W - 6}" height="40" rx="6" fill="{fill}" stroke="{C if kind == "d" else N_}" stroke-width="{2 if kind == "d" else 1.4}"/>'
            g = (NT if kind in 'nd' else RS)[k]
            o += f'<text x="{x + 18}" y="{60 if kind != "r" else 57}" font-family="NM" font-size="{26 if kind != "r" else 24}" fill="{C if kind == "d" else N_}">{g}</text>'
        for j in range(1, n): o += f'<line x1="{x + j * W}" x2="{x + j * W}" y1="34" y2="66" stroke="{N_}" stroke-width="1" stroke-dasharray="3 3" opacity=".45"/>'
        x += n * W
    o += ''.join(f'<text x="{x0 + 8 + j * W + W / 2}" y="12" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="{C}">{j + 1}</text>' for j in range(n_all))
    return o, w
def wtrain(bars, ts='3/4'):
    top, bot = ts.split('/')
    o = '<defs><pattern id="hz3" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="#fff"/><line x1="0" y1="0" x2="0" y2="6" stroke="#26296b" stroke-width="1.4"/></pattern></defs>'
    o += f'<path d="M4,80 L4,30 Q4,18 16,18 L60,18 Q72,18 72,30 L72,80 Z" fill="{N_}"/><text x="38" y="47" text-anchor="middle" font-family="PF,serif" font-size="27" font-weight="700" fill="#fff">{top}</text><text x="38" y="73" text-anchor="middle" font-family="PF,serif" font-size="27" font-weight="700" fill="#fff">{bot}</text><circle cx="20" cy="88" r="7" fill="{N_}"/><circle cx="56" cy="88" r="7" fill="{N_}"/><line x1="72" x2="86" y1="60" y2="60" stroke="{N_}" stroke-width="3"/>'
    x = 86
    for i, b in enumerate(bars):
        c, w = wcarriage(b, x); o += c; x += w
        if i < len(bars) - 1: o += f'<line x1="{x}" x2="{x + 14}" y1="60" y2="60" stroke="{N_}" stroke-width="3"/>'; x += 14
    return f'<svg viewBox="0 0 {x + 4} 100" style="width:100%;height:auto;display:block;margin:4px auto">{o}</svg>'
def tfrows(items): return ''.join(f'<div class="row">{t}<span class="tf">T &nbsp; F</span></div>' for t in items)
def piece(rows): return tbl(['Find in a piece you are learning', 'Piece', 'Bar'], [[r, LINE, BOX] for r in rows], ['46%', '38%', '16%'])

# ---------- 1 Pulse ----------
A1 = tp('Learn', 'Pulse and the bar', 'Pulse and the bar', 'Beats are grouped into bars; beat 1 of every bar is the strongest.', f'''
{ex(1, 'Strong beats', 1, 'Each dot is one beat. Circle the strong beat in every bar. In 4/4, also underline the medium beat.', beats_row('2/4', 2) + beats_row('3/4', 3) + beats_row('4/4', 4))}
{ex(2, 'Name the signs', 1, 'Write the name of each sign and what it tells you.', tbl(['Sign', 'Name', 'It tells you'], [[bars('bar'), LINE, LINE], [bars('dbl'), LINE, LINE], [bars('fin'), LINE, LINE], [bars('repeat'), LINE, LINE]], ['18%', '32%', '50%']))}
{ex(3, 'Count it', 2, 'Write a count in every box: the beat you play, then the beats you hold. The first bar is done.', wx('wc34', 86))}
{ex(4, 'Slow to fast', 1, 'Number the marks from the slowest (1) to the fastest (4).', '<div class="mm4">' + ''.join(f'<div><span class="mmk">{gin("n", "c")} = {v}</span>{BOX}</div>' for v in (120, 60, 92, 76)) + '</div>')}
{ex(5, 'How fast does it feel?', 1, 'About <b>60</b> is slow (a clock’s tick); about <b>120</b> is fast. Try a metronome and write the number that feels like each.', '<div class="mm4 mm3">' + ''.join(f'<div><span class="mmk">{t}</span><span class="feel">{gin("n", "c")} = {BOX}</span></div>' for t in ('a slow walk', 'marching', 'running')) + '</div>')}''', 1, 36)
B1 = tp('Use', 'Pulse and the bar', 'Pulse and the bar', 'A long note still has every one of its beats counted.', f'''
{ex(1, 'Add the bar lines', 2, 'Draw a bar line after every full bar and a final bar line at the end.', wx('wbar2', 56) + wx('wbar3', 56))}
{ex(2, 'Spot the mistake', 2, 'One bar has the wrong number of beats. Circle it and write how many beats it has.', wx('wmis1', 70) + f'<div class="add">beats in the wrong bar {BOX}</div>')}
{ex(3, 'Make your own', 3, 'Write two bars of 3/4 using crotchets and minims. Clap them while counting, then play them on one note.', staff('3/4', 2))}
{ex(4, 'Clap and count', 1, 'Set a metronome to <span class="mm">' + gin("n", "c") + ' = 60</span>. Clap on the notes, open your hands on the rests, count aloud. Tick a circle each time it is steady.', wx('wr1', 66) + ticks())}''', 2, 36)

# ---------- 2 Notes and rests ----------
items = [('sb', 'semibreve', '4'), ('c', '', ''), ('m', '', ''), ('q', '', ''), ('sq', '', '')]
rows = [[gcell('n', k, 38), f'<b>{n}</b>' if n else LINE, f'<b>{b}</b>' if b else BOX, gcell('r', k, 38) if n else BOX] for k, n, b in items]
NTB = '<table class="ht nt"><colgroup><col style="width:14%"><col style="width:40%"><col style="width:18%"><col style="width:28%"></colgroup><thead><tr><th>Note</th><th>Name</th><th>Beats</th><th>Rest</th></tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td class="g">{c}</td>' if i in (0, 3) else f'<td>{c}</td>' for i, c in enumerate(r)) + '</tr>' for r in rows) + '</tbody></table>'
PIZZA = ex(3, 'Why a whole note?', 1, 'One pizza = one beat. The note that fills all four pizzas of a 4/4 bar is the <b>whole note</b>; shorter notes cut one pizza into pieces. Colour each share, write the other name and the beats.', '<div class="pzr">' + ''.join(f'<div class="pzrow"><span class="pzn">{gin("n", k)} {nm}</span><span class="pzs">{"".join(pizza(cut, (cut if i < full else 0) if d else 0, 15) for i in range(4))}</span><span class="pzl">{("<b class=done2>" + oc + "</b>") if d else WL}</span><span class="pzl">{("<b class=done2>" + bt + "</b>") if d else WL + " beats"}</span></div>' for k, nm, cut, full, part, oc, bt, d in (('sb', 'semibreve', 1, 4, 0, 'whole note', '4 beats', True), ('m', 'minim', 1, 2, 0, '', '', False), ('c', 'crotchet', 1, 1, 0, '', '', False), ('q', 'quaver', 2, 0, 1, '', '', False), ('sq', 'semiquaver', 4, 0, 1, '', '', False))) + '</div>')
A2 = tp('Learn', 'Notes and rests', 'Notes and rests', 'Each plain note lasts half as long as the one above it; every note has a rest of the same length.', f'''
{ex(1, 'Name, beats and rest', 1, 'Write each note’s name and beats (crotchet = 1 beat), then draw the rest of the same length. The first row is done.', NTB)}
{ex(2, 'Draw it', 2, 'Draw one note for each length (crotchet = 1 beat).', '<div class="mm4">' + ''.join(f'<div><span class="drw"></span><span class="mmk">{t}</span></div>' for t in ('2 beats', '½ beat', '1 beat', '4 beats')) + '</div>')}
{PIZZA}''', 3, 38)
heads = [(70, 62), (130, 50), (190, 26), (250, 32), (310, 56), (370, 20), (430, 68), (490, 38), (550, 44)]
RESTPZ = ex(4, 'Rests are empty slices', 1, 'A rest is silence that lasts as long as its note. Shade each rest’s share of the pizzas with lines, then write its beats. The first is done.', '<div class="pzr">' + ''.join(f'<div class="pzrow"><span class="pzn">{gin("r", k)} {nm}</span><span class="pzs">{"".join(pizza(cut, (cut if i < full else 0) if d else 0, 15, True) for i in range(4))}</span><span class="pzl">{("<b class=done2>" + bt + "</b>") if d else WL + " beats"}</span><span></span></div>' for k, nm, cut, full, bt, d in (('sb', 'semibreve rest', 1, 4, '4 beats', True), ('m', 'minim rest', 1, 2, '', False), ('c', 'crotchet rest', 1, 1, '', False), ('q', 'quaver rest', 2, 0, '', False))) + '</div>')
B2 = tp('Use', 'Notes and rests', 'Notes and rests', 'Below the middle line, stems go up on the right; on or above it, down on the left.', f'''
{ex(1, 'Rests on the staff', 1, 'Draw a semibreve rest in the first bar (it hangs below the fourth line) and a minim rest in the second (it sits on the middle line).', staff('', 2))}
{ex(2, 'Draw the stems', 2, 'Turn every head into a crotchet: add a stem going the right way. The first is done.', staff('', 1, heads=heads, stems=[0]))}
{ex(3, 'Finish with a rest', 2, 'Each bar is short. Complete it with one rest.', grid([cell(k, 'rest ' + BOX, 64) for k in ('wra', 'wrb', 'wrc', 'wrd')], 4))}
{RESTPZ}''', 4, 38)

# ---------- 3 How long ----------
sums = [(['m', 'c'], '3'), (['c', 'q'], ''), (['dm', 'c'], ''), (['sb', 'm'], ''), (['dc', 'q'], ''), (['q', 'q', 'q', 'q'], '')]
srows = ''.join('<div class="sum">' + ' <span class="pl">+</span> '.join(gin('n', k, 34) for k in ks) + ' <span class="pl">=</span> ' + (f'<b class="done">{a}</b>' if a else BOX) + ' <span class="mu2">beats</span></div>' for ks, a in sums)
A3 = tp('Learn', 'How long is a note?', 'How long is a note?', 'A dot adds half the note’s value; a tie joins two notes of the same pitch into one sound.', f'''
{ex(1, 'Note sums', 1, 'Add up the beats (crotchet = 1 beat). The first one is done.', f'<div class="sums">{srows}</div>')}
{ex(2, 'Complete the bar', 2, 'Each bar is one note short. Count the beats you have, then find what is missing. The first is done: 4/4 needs 4 beats; minim 2 + crotchet 1 = 3, so <b>1 beat</b> is missing: a crotchet.', grid([cell('wf1', 'one note <b class="done2">crotchet</b>', 64)] + [cell(k, 'one note ' + BOX, 64) for k in ('wf2', 'wf3', 'wf4', 'wf5', 'wf6')], 3))}
{ex(3, 'Ode to Joy: count it', 2, 'Bars 3–4 of Beethoven’s Ode to Joy (Handbook p. 39). Write a count in every box, then sing it as you clap. The first is done.', wx('wc44', 84))}''', 5, 40)
B3 = tp('Use', 'How long is a note?', 'How long is a note?', 'A tie can cross a bar line; a dot cannot.', f'''
{ex(1, 'Tie or dot?', 2, 'Each tie makes one sound. Write the one dotted note that lasts the same.', grid([cell(k, 'dotted note ' + BOX, 60) for k in ('wti1', 'wti2', 'wti3')], 3))}
{ex(2, 'Spot the mistake', 2, 'One bar does not add up to four beats. Circle it and write how many beats it has.', wx('wmis2', 70) + f'<div class="add">beats in the wrong bar {BOX}</div>')}
{ex(3, 'Clap and count', 1, 'Clap the dotted rhythms, counting the “&” inside each dotted crotchet. Tick a circle each time it is steady.', wx('wl2', 66) + ticks())}
{ex(4, 'In your music', 1, 'Find each of these in a piece you are learning.', piece(['a dotted minim', 'a dotted crotchet', 'a tie', 'a rest of one whole bar']))}''', 6, 40)

# ---------- 4 Time signatures ----------
sc = [ts(3, 4), ts(6, 8), ts(2, 2), ts(9, 8), ts(4, 4), ts(12, 8), ts(3, 8), ts(6, 4)]
scrows = ''.join(f'<div class="scc">{x}<span class="sel">simple · compound</span><span class="add">beats {BOX}</span></div>' for x in sc)
A4 = tp('Learn', 'Time signatures', 'Time signatures', 'Top number: how many counts in a bar. Bottom number: which note is one count.', f'''
{ex(1, 'Which time signature?', 1, 'Each line is one full bar. Write a time signature that fits.', grid([cell(k, 'time signature ' + BOX, 60) for k in ('wt1', 'wt2', 'wt3', 'wt4', 'wt5', 'wt6')], 3))}
{ex(2, 'Simple or compound?', 2, 'Circle simple or compound, then write how many beats are in each bar.', f'<div class="scg">{scrows}</div>')}
{ex(3, 'What does it mean?', 1, 'Complete each sentence.', '<div class="sent"><p>In 3/4 there are ' + BOX + ' beats in a bar, and each beat is a ' + LINE.replace('al', 'al inl') + '.</p><p>In 6/8 there are ' + BOX + ' beats in a bar, and each beat is a ' + LINE.replace('al', 'al inl') + '.</p><p>C means the same as ' + BOX + ' ; ¢ means the same as ' + BOX + ' .</p></div>')}''', 7, 42)
TRAINEX = ex(3, 'Book every seat', 2, 'Each carriage is one bar of the time signature on the engine. Draw one note or rest in the dashed seats so every seat is booked. The first is done.', wtrain([[('n', 2, 'm'), ('d', 1, 'c')], [('n', 1, 'c'), ('x', 2, '')], [('r', 1, 'c'), ('x', 2, '')]], '3/4') + wtrain([[('n', 2, 'm'), ('x', 2, '')], [('n', 1, 'c'), ('n', 1, 'c'), ('x', 2, '')]], '4/4'))
B4 = tp('Use', 'Time signatures', 'Time signatures', 'In compound time each beat is a dotted note, divided into three.', f'''
{ex(1, 'Add the bar lines', 2, 'Draw a bar line after every full bar, and a final bar line at the end.', wx('wb1', 50) + wx('wb2', 50))}
{ex(2, 'Beam them', 3, 'The same six quavers in two time signatures. Join them with beams to show the beats: in twos for 3/4, in threes for 6/8.', grid([cell('wbm2', '3 beats', 64), cell('wbm1', '2 beats', 64)], 2))}
{TRAINEX}''', 8, 42)

# ---------- 5 Compound and irregular time ----------
A5 = tp('Learn', 'Compound and irregular time', 'Compound and irregular time', 'In 6/8 each beat is a dotted crotchet, split into three: count 1 2 3 4 5 6, feel two.', f'''
{ex(1, 'Count 6/8', 1, 'Write a count in every box. The first is done.', wx('w68c', 80))}
{ex(2, '3/4 or 6/8?', 2, 'Both bars hold six quavers. Look at the beams and write the time signature.', grid([cell('w3a', 'time signature ' + BOX, 60), cell('w6a', 'time signature ' + BOX, 60)], 2))}
{ex(3, 'Uneven bars', 2, 'Count 5/4 as 3 + 2 and 7/8 as 2 + 2 + 3: write the count in every box. The first of each is done.', '<div class="two" style="grid-template-columns:1fr 1fr">' + wx('w54c', 80) + wx('w78c', 80) + '</div>')}
{ex(4, 'Beats in compound time', 1, 'Complete each line: how many dotted-crotchet beats in a bar?', '<div class="ts6">' + ''.join(f'<div><b style="display:inline-block;width:38px">{t}</b> {BOX} <span class="mu2">beats</span></div>' for t in ('6/8', '9/8', '12/8')) + '</div>')}
{ex(5, 'Feel two', 1, 'Clap six quavers counting 1 2 3 4 5 6, then clap again saying only “1” and “4”. Tick a circle each time the two beats feel steady.', ticks())}''', 9, 44)
B5 = tp('Use', 'Compound and irregular time', 'Compound and irregular time', 'Many dances keep 4/4 but group its eight quavers 3 + 3 + 2.', f'''
{ex(1, 'Add the bar lines', 2, 'Draw a bar line after every full bar and a final bar line at the end.', wx('w98b', 50) + wx('w54b', 50))}
{ex(2, '3 + 3 + 2', 2, 'Write the count in every box (1 2 3 1 2 3 1 2), then tap it, louder on each 1. Tick a circle each time it is steady.', wx('w332c', 80) + ticks())}
{ex(3, 'Clap and count', 2, 'Clap with a metronome, counting six quavers, feeling two beats. Tick a circle each day it is steady.', wx('wl6', 64) + ticks())}
{ex(4, 'In your music', 1, 'Find each of these in a piece you are learning or listening to.', piece(['a piece in 6/8', 'a bar of quavers beamed in threes', 'a piece in 5/4 or 7/8 (listen: Take Five)']))}''', 10, 44)

# ---------- 6 Groups and upbeats ----------
PZB = '<div class="pzr">' + ''.join(f'<div class="pzrow"><span class="pzn">{nm}</span><span class="pzs">{pizza(cut, cut if d else 0, 15)}</span><span class="pzl">{("<b class=done2>" + fr + "</b>") if d else WL}</span><span class="pzl">{("<b class=done2>" + cn + "</b>") if d else WL}</span></div>' for nm, cut, fr, cn, d in (('two quavers', 2, 'half a beat each', '1 &', True), ('a triplet', 3, '', '', False), ('four semiquavers', 4, '', '', False))) + '</div>'
A6 = tp('Learn', 'Groups and upbeats', 'Groups and upbeats', 'Beams show the beats: they join the notes of one beat, or in 4/4 of beats 1–2 or 3–4, never across the middle.', f'''
{ex(1, 'Good grouping?', 2, 'Circle ✓ if the grouping shows the beats, ✗ if it hides one.', grid([cell(k, '✓ &nbsp; ✗', 64) for k in ('wg1', 'wg2', 'wg3', 'wg4')], 2))}
{ex(2, 'Cut the beat', 1, 'One beat is one pizza. Colour each one, then write how much of a beat each note gets and how you count it. The first is done.', PZB)}
{ex(3, 'Count it', 2, 'Write a count in every box: a triplet (1 & a), then semiquavers (1 e & a). The first of each is done.', wx('wtr', 96) + wx('wsq', 96))}''', 11, 46)
B6 = tp('Use', 'Groups and upbeats', 'Groups and upbeats', 'An upbeat and the last bar together make one full bar.', f'''
{ex(1, 'The upbeat', 2, 'This piece starts on beat 3 (done for you). Write a count in every other box. Then: how many beats does the last bar need?', wx('wan', 70) + f'<div class="add">beats in the last bar {BOX}</div>')}
{ex(2, 'Clap the upbeat', 1, 'Clap the piece in exercise 1 with a metronome: count “1 2” silently, clap on 3. Tick a circle each time the last bar is exactly two beats.', ticks())}
{ex(3, 'Clap and count', 2, 'Triplets and semiquavers: clap with a metronome while counting aloud. Tick a circle each day it is steady.', wx('wl3', 64) + ticks())}
{ex(4, 'In your music', 1, 'Find each of these in a piece you are learning.', piece(['an upbeat (anacrusis)', 'a triplet', 'four semiquavers in one beat']))}''', 12, 46)

# ---------- 7 Off the beat ----------
A7 = tp('Learn', 'Off the beat', 'Off the beat', 'Syncopation: a note that starts between the beats and is held across the next one.', f'''
{ex(1, 'Find the off-beat notes', 2, 'Tap the beat. Circle every note that starts on an “&”, between the beats.', wx('woff', 76))}
{ex(2, 'Count a syncopation', 2, 'Write a count in every box. Keep the beat in your foot. The first is done.', wx('wsy', 80))}
{ex(3, 'Swing', 1, 'Which line shows how swung quavers are played? Circle A or B, then play both and hear the difference.', '<div class="op3" style="grid-template-columns:1fr 1fr">' + ''.join(f'<div class="opc"><span class="ol">{l}</span>{wx(k, 60 if l == "A" else 76)}</div>' for l, k in (('A', 'wsw1'), ('B', 'wsw2'))) + '</div>')}
{ex(4, 'Foot and hands', 1, 'Tap the beat with your foot and clap only on the “&”s. Then swap: clap the beats, tap the “&”s. Tick a circle each time it holds together.', ticks())}
{ex(5, 'True or false?', 1, 'Circle T or F.', tfrows(('A syncopated note starts between the beats.', 'Swing quavers are written long–short.', 'In syncopation the beat stops for a moment.')))}''', 13, 48)
B7 = tp('Use', 'Off the beat', 'Off the beat', 'Hemiola: two bars of 3/4 felt as three big beats.', f'''
{ex(1, 'Hemiola', 3, 'Count it in 3/4 in the boxes, then clap it feeling three minims across the two bars.', wx('whem', 80))}
{ex(2, 'Clap and count', 2, 'Clap the syncopations with a metronome, counting aloud. Tick a circle each day it is steady.', wx('wl4', 64) + ticks())}
{ex(3, 'In your music', 1, 'Find each of these in a piece you are learning or listening to.', piece(['a syncopation', 'Swing written at the top']))}
{ex(4, 'Swing it', 2, 'Play a C major scale in swing quavers (“doo-ba, doo-ba”), then straight. Tick a circle each day.', ticks())}
{ex(5, 'Listen for it', 1, 'Listen to each one and tick it when you hear what is listed.', ''.join(f'<div class="row"><b>{t}</b><span style="color:#6d6f9c">{h}</span>{ticks(1)}</div>' for t, h in (('Joplin, The Entertainer', 'syncopation'), ('Miller, In the Mood', 'swing'), ('Bernstein, America', 'hemiola'))))}''', 14, 48)

# ---------- 8 Repeats and road signs (her 11 Nov: "응 추가해줘", the audit found no pages for it) ----------
def rmap(cells): return '<div class="rmap">' + ''.join(f'<span class="rb{" sg" if c[:1] in "|:" else ""}">{c}</span>' for c in cells) + '</div>'
def rrow(lab, cells, ans=LINE): return f'<div class="rrow"><span class="rl">{lab}</span>{rmap(cells)}<span class="rans">{ans}</span></div>'
A8 = tp('Learn', 'Repeats and road signs', 'Repeats and road signs', 'Follow the signs in order. After D.C. or D.S., stop at the first Fine, or jump at To Coda.', f"""
{ex(1, 'What does it mean?', 1, 'Write what each sign tells you to do.', tbl(['Sign', 'What it tells you'], [['<b>:‖ (repeat sign)</b>', LINE], ['<b>1. and 2. (time bars)</b>', LINE], ['<b>D.C.</b>', LINE], ['<b>D.S.</b>', LINE], ['<b>Fine</b>', LINE], ['<b>To Coda</b>', LINE]], ['34%', '66%']))}
{ex(2, 'Write the order', 2, 'Each letter is one bar. Write the letters in the order you play them.', rrow('1', ['A', 'B :‖', 'C']) + rrow('2', ['‖: A', '1. B :‖', '2. C']) + rrow('3', ['A', 'B Fine', 'C', 'D.C. al Fine']))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('With no start sign, a repeat goes back to the very beginning.', 'After a D.C., you play the repeats again.', 'D.S. sends you back to the sign.', 'Fine means the end.')))}
{ex(4, 'Say it in Italian', 1, 'Write the letter of the English meaning next to each Italian word.', tbl(['da capo', 'dal segno', 'Fine', 'Coda'], [[BOX] * 4], ['25%'] * 4, 'bld nocap') + '<p class="how" style="margin-top:8px"><b>A</b> the end &nbsp;·&nbsp; <b>B</b> from the sign &nbsp;·&nbsp; <b>C</b> the tail &nbsp;·&nbsp; <b>D</b> from the head</p>')}""", 15, 50)
B8 = tp('Use', 'Repeats and road signs', 'Repeats and road signs', 'Read the map once before you play: find every sign, then follow them in order.', f"""
{ex(1, 'How many bars?', 2, 'Each letter is one bar. Follow the signs and count every bar you play.', rrow('1', ['‖: A', 'B', 'C :‖', 'D'], BOX) + rrow('2', ['A', '𝄋 B', 'C Fine', 'D', 'D.S. al Fine'], BOX) + rrow('3', ['𝄋 A', 'B To Coda', 'C', 'D.S. al Coda', '⊕ E'], BOX))}
{ex(2, 'Write the order', 3, 'Write the letters of map 3 above in the order you play them.', '<div class="al" style="height:30px;margin:8px 0"></div>')}
{ex(3, 'Make a map', 2, 'Write your own map of five bars with one repeat sign and a 1st and 2nd time bar. Then write the order you play it.', '<div class="al" style="height:30px;margin:8px 0"></div><div class="al" style="height:30px;margin:8px 0"></div>')}
{ex(4, 'In your music', 1, 'Find each of these in a piece you are learning.', piece(['a repeat sign', 'a 1st and 2nd time bar', 'D.C. or D.S.', 'Fine or Coda']))}
{ex(5, 'Play it', 1, 'Play a piece with repeats from start to finish, following every road sign without stopping. Tick a circle each day.', ticks())}""", 16, 50)

# ---------- Review, progress, answers ----------
rsum = ''.join('<div class="sum">' + ' <span class="pl">+</span> '.join(gin('n', k, 32) for k in ks) + ' <span class="pl">=</span> ' + BOX + '</div>' for ks in (['dm', 'q', 'q'], ['dc', 'q', 'm']))
R = wpage(f'''<div class="kick">Time · Review</div><h1>Review</h1><p class="rem2"><span>Ten minutes</span>No help, no piano. Mark it with the answers on page 19: one mark for each answer.</p>
{ex(1, 'Name the notes', 1, 'Write the name of each note.', '<div class="nm4">' + ''.join(f'<div>{gcell("n", k, 40)}{LINE}</div>' for k in ('m', 'q', 'dc', 'sb')) + '</div>')}
{ex(2, 'How many beats?', 1, 'Crotchet = 1 beat.', f'<div class="sums">{rsum}</div>')}
{ex(3, 'Time signatures', 2, 'Write a time signature for each bar, then circle the compound ones.', grid([cell(k, 'time signature ' + BOX, 56) for k in ('wt3', 'wt5', 'wt6')], 3))}
{ex(4, 'Count it', 2, 'Write a count in every box.', wx('wrev', 74))}
{ex(5, 'True or false?', 2, 'Circle T or F.', ''.join(f'<div class="row">{t}<span class="tf">T &nbsp; F</span></div>' for t in ('A tie joins two notes of different pitches.', '6/8 has two beats in a bar.', 'In 4/4, a beam may cross the middle of the bar.')))}
<div class="score">Score <span class="ab"></span> / 18</div>''', 17, None)
concepts = ['pulse, tempo and strong beats', 'bar lines and repeat signs', 'note and rest values', 'dots and ties', 'simple time signatures', 'compound time (6/8)', 'irregular time (5/4, 7/8)', 'grouping with beams', 'triplets and semiquavers', 'upbeats', 'syncopation', 'swing', 'hemiola', 'repeat signs and 1st/2nd time bars', 'D.C., D.S., Fine and Coda']
PR = wpage(f'''<div class="kick">Time · Progress</div><h1>My progress</h1><p class="rem2"><span>How to use</span>Tick each column when it is true. Come back to this page every few weeks.</p>
{tbl(['Concept', 'I know it', 'I can write it', 'I can play it', 'Handbook'], [[c, '<span class="cb2"></span>', '<span class="cb2"></span>', '<span class="cb2"></span>', f'p. {p}'] for c, p in zip(concepts, (34, 34, 36, 38, 40, 42, 42, 44, 44, 44, 46, 46, 46, 48, 48))], ['36%', '15%', '17%', '17%', '15%'], 'prog')}
<div class="note2"><b>Teacher’s note</b><div class="lines"><span class="al"></span><span class="al"></span><span class="al"></span></div></div>''', 18, None)
ans = [('p. 1', 'Slow to fast: 4, 1, 3, 2 (60 slowest, 120 fastest). Strong beats on 1; in 4/4 medium on 3. Signs: bar line, double bar line, final bar line, repeat signs. Count: 1 2 3 · 1–2 3 · 1–2–3. How fast does it feel: any answer; slower to faster is usual.'),
       ('p. 2', 'Bar lines: 2/4 after notes 2, 3, 5, 7 and 8, final bar line after note 11; 3/4 after notes 2, 5 and 6, final bar line after note 8. Mistake: bar 3 has 4 beats.'),
       ('p. 3', 'Draw it: minim, quaver, crotchet, semibreve. Table: crotchet 1, crotchet rest; minim 2, minim rest; quaver ½, quaver rest; semiquaver ¼, semiquaver rest. Why a whole note: minim = half note, 2 beats; crotchet = quarter note, 1 beat; quaver = eighth note, ½ beat; semiquaver = sixteenth note, ¼ beat.'),
       ('p. 4', 'Stems: up on the right below the middle line, down on the left on or above it. Finish with a rest: minim, crotchet, minim, crotchet. Empty slices: minim rest 2 beats (2 pizzas), crotchet rest 1 beat (1 pizza), quaver rest ½ beat (half a pizza).'),
       ('p. 5', 'Sums: 3, 1½, 4, 6, 2, 2. Complete: crotchet, crotchet, crotchet, quaver, quaver, quaver. Ode to Joy: 1 2 3 4 · 1–2 & 3–4.'),
       ('p. 6', 'Tie or dot: dotted minim, dotted crotchet, dotted semibreve. Mistake: bar 2 has 5 beats.'),
       ('p. 7', 'Time signatures: 3/4, 2/4, 6/8 (3/4 also fits), 4/4, 5/4, 9/8. Compound: 6/8, 9/8, 12/8, 6/4 (beats 2, 3, 4, 2). Simple: 3/4 (3), 2/2 (2), 4/4 (4), 3/8 (3). 3/4: 3 crotchet beats; 6/8: 2 dotted-crotchet beats; C = 4/4, ¢ = 2/2.'),
       ('p. 8', 'Bar lines: 3/4 after notes 3, 5 and 6, final bar line after note 9; 4/4 after notes 3 and 7, final bar line after note 8. Beams: 3/4 in three pairs; 6/8 in two groups of three. Seats: 3/4 carriage 1 a crotchet, carriage 2 a minim, carriage 3 a minim (or a minim rest); 4/4 carriage 1 a minim (or a minim rest), carriage 2 a minim (or a minim rest).'),
       ('p. 9', '6/8: 1 2 3 4 5 6 · 1 4. Beams: 3/4 (pairs), 6/8 (threes). 5/4: 1 2 3 1 2. 7/8: 1 2 1 2 1 2 3. Compound beats: 6/8 2, 9/8 3, 12/8 4.'),
       ('p. 10', 'Bar lines: 9/8 after the 3rd and 8th notes; 5/4 after the 4th and 9th notes. 3 + 3 + 2: 1 2 3 1 2 3 1 2.'),
       ('p. 11', 'Grouping: ✓ ✗ ✓ ✗. Pizza: a triplet, a third of a beat each, 1 & a; four semiquavers, a quarter each, 1 e & a. Triplet: 1 & a 2. Semiquavers: 1 e & a 2 · 1 e & a 2.'),
       ('p. 12', 'Upbeat: 3 · 1 2 3 · 1–2; the last bar needs 2 beats.'),
       ('p. 13', 'Off the beat: bar 1 notes 3 and 4; bar 2 note 2; bar 3 notes 2 and 3. Syncopation: 1 & & 1 2. Swing is played as B. True or false: T, F, F.'),
       ('p. 14', 'Hemiola: 1–2 3 · 1 2–3; felt as three minims.'),
       ('p.\u200915', 'Signs: go back and play again (to the start sign, or the beginning); first time play bar 1., after the repeat skip it and play 2.; D.C. back to the beginning; D.S. back to the sign; Fine the end; To Coda jump to the coda. Order: A B A B C · A B A C · A B C A B. True or false: T, F, T, T. Italian: D, B, A, C.'),
       ('p.\u200916', 'How many bars: 7 (A B C A B C D), 6 (A B C D B C), 6 (A B C A B E). Map 3 in order: A B C A B E.'),
       ('p.\u200917', 'minim, quaver, dotted crotchet, semibreve · 4, 4 · 6/8 (3/4 also fits), 5/4, 9/8 (compound: 6/8 and 9/8) · 1–2 & 3 · 1–2–3 · F, T, F.')]
AN = wpage(f'''<div class="kick">Time · Answers</div><h1>Answers</h1>
{tbl(['Page', 'Answers'], [[p, a] for p, a in ans], ['12%', '88%'], 'ansT ansS')}
<p class="sm">Pages with “make your own”, “in your music” and clapping have no single answer: check them at the piano with your teacher, or with the online lessons.</p>''', 19, None)

css += f'''
.so{{color:#d9d4c6}} .el{{color:{GOLD if False else '#c9a24f'};font-size:13px;letter-spacing:1px}}
.rem2{{display:flex;gap:12px;align-items:baseline;font-size:14.5px;margin:-2px 0 4px;color:#3d4080}} .rem2 span{{flex:none;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}}
.op3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-bottom:8px}} .opc{{position:relative}} .opc .vx{{margin:0;padding-left:30px}} .ol{{position:absolute;left:10px;top:50%;transform:translateY(-50%);font-weight:700;font-size:16px;color:{C};z-index:1}}
.sent p{{font-size:15px;margin:6px 0;display:flex;align-items:center;gap:8px;flex-wrap:wrap}} .al.inl{{display:inline-block;width:150px;height:20px}}
.mm4{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}} .mm4>div{{display:flex;flex-direction:column;align-items:center;gap:3px;padding:0 6px}} .mmk{{font-weight:700;font-size:15px}} .drw{{display:block;width:70px;height:70px}} .nm4{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}} .nm4>div{{text-align:center}}
.tf{{margin-left:auto;font-weight:700;letter-spacing:.1em;color:{MUTE}}} .row{{display:flex;align-items:center;gap:10px;font-size:15px;padding:5px 0;border-bottom:.6px solid #e2ddd0}}
.score{{margin-top:14px;text-align:right;font-weight:700;font-size:16px;display:flex;justify-content:flex-end;align-items:center;gap:8px}}
.prog th{{white-space:nowrap}} .prog td{{padding:9px 8px;font-size:15px}} .cb2{{display:inline-block;width:20px;height:20px;border:1.6px solid {N_}}}
.note2{{margin-top:20px}} .note2 b{{font-size:15px}} .lines .al{{height:34px}}
.fills>.fc{{display:flex;flex-direction:column}} .fills>.fc>.add{{margin-top:auto;justify-content:center;text-align:center;gap:6px}} .wl{{display:inline-block;width:64px;height:26px;border-bottom:1.6px solid #26296b}} .fills>.fc>figure.vx{{border:0;background:none;box-shadow:none;height:auto;flex:0 0 auto;padding:4px 0}} .fills>.fc>.add{{margin-top:6px !important}} .fills{{row-gap:18px}} .mm4+.mm4{{margin-top:0}} .ex2 .mm4 .ab{{height:24px}} .ex2>.tk,.ex2>.tk2{{justify-content:flex-end;margin-top:8px}} .pzr{{display:flex;flex-direction:column;gap:2px;margin-top:4px}} .pzrow{{display:grid;grid-template-columns:1.1fr 1.6fr 1fr 1fr;align-items:center;gap:12px;padding:1px 0;border-bottom:.6px solid #e2ddd0}} .pzs{{display:flex;gap:8px}} .pzs svg{{margin:0 !important}} .pz{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:6px}} .pz>div{{display:flex;flex-direction:column;align-items:center;gap:6px}} .pzn{{display:flex;align-items:center;gap:6px;font-weight:700;font-size:14px}} .pzl{{display:flex;align-items:flex-end;gap:6px;font-size:13px;color:#6d6f9c;min-height:26px}} .fills{{align-items:stretch}} .fills>.fc>.add{{margin-top:auto !important}} .mm4 .drw{{width:96px;height:72px;border:1.4px dashed #b9bbd3;border-radius:6px}} .mm4.mm3{{grid-template-columns:repeat(3,1fr)}} .row .tk{{margin:0 0 0 auto}} .row b{{min-width:230px}} .feel{{display:flex;align-items:center;gap:6px;font-weight:700}} .ansT td{{font-size:13px;line-height:1.4;padding:4px 8px;vertical-align:top}} .ansT td:first-child{{font-weight:700;color:{C}}}
.rrow{{display:grid;grid-template-columns:28px 1fr 190px;align-items:center;gap:12px;margin:9px 0}} .rl{{font-weight:700;color:{C}}} .rmap{{display:flex;gap:6px;flex-wrap:wrap}} .rb{{border:1.6px solid #26296b;border-radius:6px;padding:7px 10px;font-weight:700;font-size:15px;min-width:44px;text-align:center}} .rans{{display:flex;align-items:center}} .rans .al{{width:100%}}
'''
pages = [A1, B1, A2, B2, A3, B3, A4, B4, A5, B5, A6, B6, A7, B7, A8, B8, R, PR, AN]
import sys as _s; _s.path.insert(0, '/tmp/claude-0/pk'); import importlib, firstdone; importlib.reload(firstdone)
FIRST = {'Which time signature?': [('fill', '3/4')], 'Finish with a rest': [('fill', 'minim rest')], 'Tie or dot?': [('fill', 'dotted minim')], 'Simple or compound?': [('both', [('ring', 'simple'), ('fill', '3')])], '3/4 or 6/8?': [('fill', '3/4')], 'Beats in compound time': [('fill', '2')], 'Good grouping?': [('ring', '✓')], 'Slow to fast': [('fill', '4')]}
open('/mnt/user-data/outputs/house-rooms/workbook-time2.html', 'w').write(_LG(firstdone.apply(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{"".join(pages)}</body></html>', FIRST).replace('</style></head>', firstdone.CSS + '</style></head>', 1)))
print('ok', len(pages))
