# Part openers as one picture (her 6 Nov, A: "one tune, taken apart"). Each part opens with a single piece of music
# that contains everything the part teaches; numbered red callouts point into it, and the legend below is the contents.
# Drawn by hand in SVG (cream on the navy opener page), so nothing depends on the engraver.
import math as _om
OCR, ODK, ORD, OPK = '#fffdf7', '#26296b', '#e4572e', '#f4a9bb'
_LET = 'CDEFGAB'
def _idx(n):   # 'F#4' -> diatonic index (C0 = 0)
    return int(n[-1]) * 7 + _LET.index(n[0])
class Staff:
    def __init__(s, x0, x1, y1, sp=12, clef='G'):   # y1: the bottom line
        s.x0, s.x1, s.y1, s.sp, s.clef = x0, x1, y1, sp, clef
        s.base = 30 if clef == 'G' else 18   # E4 on the treble's line 1, G2 on the bass's
    def y(s, n): return s.y1 - (_idx(n) - s.base) * s.sp / 2
    def lines(s, col=OCR, w=1.3): return ''.join(f'<line x1="{s.x0}" x2="{s.x1}" y1="{s.y1 - i * s.sp}" y2="{s.y1 - i * s.sp}" stroke="{col}" stroke-width="{w}" opacity=".92"/>' for i in range(5))
    def clefsym(s, col=OCR):
        if s.clef == 'G': return f'<text x="{s.x0 + 6}" y="{s.y1 + 2}" font-family="NM" font-size="{s.sp * 4.7:.0f}" fill="{col}">𝄞</text>'
        return f'<text x="{s.x0 + 6}" y="{s.y1 - s.sp * 1.05:.1f}" font-family="NM" font-size="{s.sp * 4.2:.0f}" fill="{col}">𝄢</text>'
    def ledger(s, x, n, col=OCR):
        i = _idx(n) - s.base; o = ''
        if i <= -2:
            for k in range(-2, i - 1, -2): o += f'<line x1="{x - 11}" x2="{x + 11}" y1="{s.y1 - k * s.sp / 2}" y2="{s.y1 - k * s.sp / 2}" stroke="{col}" stroke-width="1.3"/>'
        if i >= 10:
            for k in range(10, i + 1, 2): o += f'<line x1="{x - 11}" x2="{x + 11}" y1="{s.y1 - k * s.sp / 2}" y2="{s.y1 - k * s.sp / 2}" stroke="{col}" stroke-width="1.3"/>'
        return o
    def head(s, x, n, hollow=False, col=OCR):
        y = s.y(n); r = s.sp * .62
        return s.ledger(x, n, col) + f'<ellipse cx="{x}" cy="{y:.1f}" rx="{r:.1f}" ry="{r * .72:.1f}" transform="rotate(-20 {x} {y:.1f})" fill="{"none" if hollow else col}" stroke="{col}" stroke-width="2.2"/>'
    def note(s, x, n, kind='c', col=OCR, up=None):   # kind: c crotchet, m minim, q quaver, sb semibreve, dc dotted crotchet
        y = s.y(n); i = _idx(n) - s.base; up = (i < 4) if up is None else up
        o = s.head(x, n, kind in ('m', 'sb', 'dm'), col)
        if kind != 'sb':
            sx = x + (s.sp * .55 if up else -s.sp * .55); sy = y - 3.3 * s.sp if up else y + 3.3 * s.sp
            o += f'<line x1="{sx:.1f}" x2="{sx:.1f}" y1="{y:.1f}" y2="{sy:.1f}" stroke="{col}" stroke-width="1.8"/>'
            if kind == 'q': o += f'<path d="M{sx:.1f},{sy:.1f} q{10 if up else 10},{6 if up else -6} 9,{16 if up else -16}" fill="none" stroke="{col}" stroke-width="2.2"/>'
        if kind == 'dc' or kind == 'dm': o += f'<circle cx="{x + s.sp * 1.1:.1f}" cy="{y - (s.sp * .3 if i % 2 == 0 else 0):.1f}" r="2.4" fill="{col}"/>'
        return o
    def beam(s, xs, n_list, col=OCR):   # quavers beamed, stems up
        top = min(s.y(n) for n in n_list) - 3.3 * s.sp; o = ''
        for x, n in zip(xs, n_list):
            o += s.head(x, n, False, col) + f'<line x1="{x + s.sp * .55:.1f}" x2="{x + s.sp * .55:.1f}" y1="{s.y(n):.1f}" y2="{top:.1f}" stroke="{col}" stroke-width="1.8"/>'
        o += f'<line x1="{xs[0] + s.sp * .55 - 1:.1f}" x2="{xs[-1] + s.sp * .55 + 1:.1f}" y1="{top:.1f}" y2="{top:.1f}" stroke="{col}" stroke-width="{s.sp * .42:.1f}"/>'
        return o
    def rest(s, x, col=OCR): return f'<text x="{x - 6}" y="{s.y1 - s.sp * 1.2:.1f}" font-family="NM" font-size="{s.sp * 2.5:.0f}" fill="{col}">𝄽</text>'
    def bar(s, x, col=OCR, w=1.5): return f'<line x1="{x}" x2="{x}" y1="{s.y1 - 4 * s.sp}" y2="{s.y1}" stroke="{col}" stroke-width="{w}"/>'
    def end(s, x, col=OCR): return s.bar(x, col) + s.bar(x + 8, col, 4)
    def tsig(s, x, a, b, col=OCR):
        return f'<text x="{x}" y="{s.y1 - 2 * s.sp - 1:.1f}" font-family="PF" font-size="{s.sp * 2.1:.0f}" font-weight="700" fill="{col}" text-anchor="middle">{a}</text><text x="{x}" y="{s.y1 + 1:.1f}" font-family="PF" font-size="{s.sp * 2.1:.0f}" font-weight="700" fill="{col}" text-anchor="middle">{b}</text>'
    def acc(s, x, n, sym, col=OCR): return f'<text x="{x - s.sp * 1.15:.1f}" y="{s.y(n) + s.sp * .45:.1f}" font-family="AH" font-size="{s.sp * 1.5:.0f}" font-weight="700" fill="{col}" text-anchor="end">{sym}</text>'
    def tie(s, x0, x1, n, col=OCR):
        y = s.y(n) + s.sp * .8
        return f'<path d="M{x0 + 4},{y:.1f} Q{(x0 + x1) / 2},{y + s.sp * 1.3:.1f} {x1 - 4},{y:.1f}" fill="none" stroke="{col}" stroke-width="2"/>'
    def chord(s, x, notes, hollow=True, col=OCR, extra=()):   # a cake: stacked heads (no stem)
        return ''.join(s.head(x, n, hollow, col) for n in notes) + ''.join(s.head(x, n, hollow, ORD) for n in extra)
def brace(x, y0, y1, col=OCR): return f'<path d="M{x},{y0} C{x - 14},{y0 + (y1 - y0) * .25} {x - 14},{y0 + (y1 - y0) * .75} {x},{y1}" fill="none" stroke="{col}" stroke-width="2.2"/><line x1="{x}" x2="{x}" y1="{y0}" y2="{y1}" stroke="{col}" stroke-width="1.5"/>'
def call(n, x, y, tx, ty, r=12):
    return f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="{ORD}" stroke-width="1.4" stroke-dasharray="3 3"/><circle cx="{tx}" cy="{ty}" r="{r}" fill="{ORD}"/><text x="{tx}" y="{ty + 4.5}" text-anchor="middle" font-family="AH" font-size="{13 if len(str(n)) < 3 else 10.5}" font-weight="700" fill="#fff">{n}</text>'
def lab(x, y, t, col=OPK, fs=15, anchor='middle', fam='CV'): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{fam}" font-size="{fs}" font-weight="700" fill="{col}">{t}</text>'
def bracket(x0, x1, y, t, col=OCR, up=False, fs=12):
    d = -5 if up else 5
    return f'<path d="M{x0},{y - d} V{y} H{x1} V{y - d}" fill="none" stroke="{col}" stroke-width="1.4"/>' + lab((x0 + x1) / 2, y + (-9 if up else 16), t, col, fs, fam='AH')

# ---------- Part II · Time ----------
def pic_time():
    S = Staff(40, 760, 160, 12); L = S.lines() + S.clefsym() + S.tsig(104, 4, 4)
    o = L + S.note(130, 'G4') + S.bar(152)
    o += S.note(180, 'A4', 'm') + S.rest(290) + S.beam([338, 374], ['G4', 'A4']) + S.bar(410)
    o += S.note(438, 'B4', 'dc') + S.note(508, 'A4') + S.note(576, 'G4', 'q') + S.note(614, 'G4') + S.bar(650) + S.note(678, 'G4', 'dm') + S.tie(614, 678, 'G4') + S.end(740)
    yb = S.y1 + 44
    for x, t, big in [(180, '1', 1), (240, '2', 0), (290, '3', 0), (350, '4', 0), (438, '1', 1), (478, '2', 0), (542, '3', 0), (614, '4', 0), (678, '1', 1)]:
        o += f'<circle cx="{x + 4}" cy="{yb}" r="{9 if big else 5}" fill="{ORD if big else OCR}"/>' + lab(x + 4, yb + 28, t, ORD if big else OCR, 14, fam='AH')
    o += lab(512, yb + 28, '&amp;', OPK, 13, fam='AH') + lab(582, yb + 28, '&amp;', OPK, 13, fam='AH')
    # a 6/8 bar, small, lower right
    T = Staff(60, 300, yb + 116, 9, 'G'); o += T.lines(w=1) + T.tsig(78, 6, 8)
    for g in range(2):
        xs = [112 + g * 92 + k * 26 for k in range(3)]
        o += T.beam(xs, ['E5', 'E5', 'E5']).replace(f'<ellipse cx="{xs[0]}"', f'<ellipse fill-opacity="1" cx="{xs[0]}"')
        o += f'<circle cx="{xs[0]}" cy="{T.y("E5"):.1f}" r="4.6" fill="{ORD}"/>'
    o += lab(330, yb + 120, 'two beats, three quavers in each', OPK, 18, 'start')
    o += call(4, 118, S.y1 - 3 * S.sp, 100, 60) + call(2, 236, S.y('A4') - 10, 236, 50) + call(6, 360, S.y('A4') - 50, 360, 50) + call(3, 452, S.y('B4') - 12, 452, 50)
    o += call(1, 682, yb, 740, yb) + call(6, 134, S.y('G4') + 8, 100, yb) + call(7, 514, S.y('A4') + 9, 514, yb + 58) + call(3, 648, S.y('G4') + 22, 700, yb + 58) + call(5, 48, yb + 98, 48, yb + 148) + call(8, 744, S.y1 - 2 * S.sp, 780, S.y1 - 6 * S.sp)
    return f'<svg viewBox="0 0 800 {yb + 160}" style="width:100%;display:block">{o}</svg>'
LEG_T = [(1, 'Pulse, tempo and the bar', 'the steady beat underneath; beat 1 is strongest', 'T1'), (2, 'Notes and rests', 'the shape says how long; rests are counted too', 'T2'), (3, 'How long is a note?', 'a dot adds half; a tie glues two notes into one', 'T3'), (4, 'Time signatures', 'four seats in every bar, a crotchet in each', 'T4'), (5, 'Compound and irregular time', 'beats in threes; bars of five or seven', 'T5'), (6, 'Rhythm: groups and upbeats', 'beams show the beats; starting before bar 1', 'T6'), (7, 'Rhythm: off the beat', 'a note between the beats that holds on', 'T7'), (8, 'Repeats and road signs', 'repeat signs, D.C., D.S., Fine and Coda', 'T8'), ('★', 'Tips: when the rhythm slips', '', 'TT')]

# ---------- Part I · Pitch ----------
def pic_pitch():
    W, KH, ky = 36, 96, 300; whites = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4', 'C5']
    kx = lambda n: 70 + whites.index(n) * W + W / 2
    G = Staff(70, 610, 140, 12, 'G'); F = Staff(70, 610, 236, 12, 'F')
    o = G.lines() + F.lines() + G.clefsym() + F.clefsym() + brace(66, G.y1 - 4 * G.sp, F.y1) + f'<line x1="610" x2="610" y1="{G.y1 - 48}" y2="{F.y1}" stroke="{OCR}" stroke-width="1.5"/>'
    notes = [(F, 'C3', kx('C3') + 70), (F, 'F3', kx('F3') + 40), (G, 'C4', kx('C4')), (G, 'F#4', kx('F4') + W / 2), (G, 'G4', kx('G4') + 10), (G, 'A4', kx('A4') + 30)]
    for st, n, x in notes: o += st.note(x, n, 'sb')
    o += G.acc(kx('F4') + W / 2, 'F#4', '♯', ORD)
    for i, n in enumerate(whites):
        o += f'<rect x="{70 + i * W}" y="{ky}" width="{W}" height="{KH}" fill="{"#3a3d7e" if n == "C4" else "none"}" stroke="{OCR}" stroke-width="1.4"/>'
        if n[0] == 'C': o += lab(kx(n), ky + KH + 16, {'C3': 'Bass C', 'C4': 'Middle C', 'C5': 'Treble C'}[n], OCR if n != 'C4' else ORD, 12, fam='AH')
    for i, n in enumerate(whites[:-1]):
        if n[0] in 'CDFGA': o += f'<rect x="{70 + (i + 1) * W - 11}" y="{ky}" width="22" height="58" rx="2" fill="{OCR}"/>'
    for st, n, x in notes:   # the map: a dotted line from the note down to its key
        key = n.replace('#', ''); tx = kx(key) + (W / 2 if '#' in n else 0)
        o += f'<line x1="{x}" y1="{st.y(n) + 8:.1f}" x2="{tx:.1f}" y2="{ky - 2}" stroke="{OPK}" stroke-width="1.2" stroke-dasharray="3 4" opacity=".9"/>'
        o += f'<circle cx="{tx:.1f}" cy="{ky + (40 if "#" in n else 80)}" r="5" fill="{ORD if n in ("C4", "F#4") else OPK}"/>'
    o += f'<path d="M{kx("F4") + 2},{ky + 80} Q{kx("F4") + 12},{ky + 62} {kx("F4") + W / 2 - 4},{ky + 48}" fill="none" stroke="{ORD}" stroke-width="2.4" stroke-linecap="round"/>'
    o += lab(kx('C4'), ky + KH + 36, 'C: just left of the two black keys', OPK, 16)
    o += call(2, 90, G.y('G4'), 36, 50) + call(2, 92, F.y('F3'), 36, F.y1 + 10)
    o += call(3, kx('A4') + 30, G.y('A4') - 10, kx('A4') + 30, 44) + lab(kx('A4') + 48, 49, 'from G, one step up: A', OPK, 15, 'start')
    o += call(5, kx('F4') + W / 2, G.y('F#4') - 10, kx('F4') - 10, 44) + lab(kx('F4') - 28, 49, '♯: one key to the right', OPK, 15, 'end')
    o += call(4, (kx('F3') + 40 + kx('C4')) / 2 + 10, (G.y1 + F.y1) / 2 + 16, 660, (G.y1 + F.y1) / 2 + 16)
    o += call(1, kx('C5') + 10, ky + 20, 660, ky + 20)
    xc, xg, yi = kx('C4'), kx('G4') + 10, G.y1 + 26
    o += bracket(xc, xg, yi, 'C to G: a 5th', OPK, fs=12)
    o += call(6, xc - 2, yi, 40, yi) + call(7, xg + 4, yi + 12, 660, yi + 12)
    return f'<svg viewBox="0 0 700 {ky + KH + 50}" style="width:100%;display:block">{o}</svg>'
LEG_P = [(1, 'The keyboard', 'two and three black keys; C is left of the two', 'P1'), (2, 'The staff and the clefs', 'the treble clef names G, the bass clef F', 'P2'), (3, 'Reading the notes', 'start from a clef note, then step or skip', 'P3'), (4, 'The staff and the keyboard', 'every line and space is one white key', 'P4'), (5, 'Sharps, flats and naturals', 'a sharp moves one key right, a flat one key left', 'P5'), (6, 'Counting intervals', 'count the notes, both ends: C to G is a 5th', 'P6'), (7, 'Major, minor and perfect', 'count the keys between: 6 make a perfect 5th', 'P7'), ('★', 'Tips: when a note reads wrong', '', 'PT')]

# ---------- Part III · Scales and keys ----------
def pic_scales():
    S = Staff(40, 700, 150, 12); o = S.lines() + S.clefsym()
    o += f'<text x="86" y="{S.y("F5") + 5:.1f}" font-family="AH" font-size="22" font-weight="700" fill="{ORD}" text-anchor="middle">♯</text>'
    sc = ['G4', 'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5']; xs = [140 + i * 74 for i in range(8)]
    for x, n in zip(xs, sc): o += S.note(x, n, 'c', OPK if n == 'E5' else OCR)
    o += S.end(700)
    steps = 'TTSTTTS'; yb = S.y1 + 30
    for i, t in enumerate(steps):
        x0, x1 = xs[i] + 8, xs[i + 1] - 8; red = t == 'S'
        o += f'<path d="M{x0},{yb - 5} V{yb} H{x1} V{yb - 5}" fill="none" stroke="{ORD if red else OCR}" stroke-width="{2 if red else 1.3}"/>' + lab((x0 + x1) / 2, yb + 17, 'semitone' if red else 'tone', ORD if red else OCR, 11, fam='AH')
    o += lab(xs[5], S.y('E5') - 48, 'E minor starts here', OPK, 15)
    o += lab(100, yb + 52, 'last sharp F♯, next key up: G major', OPK, 16, 'start')
    o += f'<path d="M92,{S.y("F5") - 16} Q110,{S.y("F5") - 40} {xs[0] - 6},{S.y("G4") - 10}" fill="none" stroke="{ORD}" stroke-width="1.6" stroke-dasharray="3 3"/>'
    # a small circle of fifths
    cx, cy, R = 630, yb + 160, 56; MJ = ['C', 'G', 'D', 'A', 'E', 'B', 'F♯', 'D♭', 'A♭', 'E♭', 'B♭', 'F']
    o += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{OCR}" stroke-width="1.2" opacity=".7"/>'
    for i, m in enumerate(MJ):
        a = _om.radians(-90 + i * 30); x, y = cx + (R + 16) * _om.cos(a), cy + (R + 16) * _om.sin(a)
        o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="12" fill="{ORD if i == 1 else ODK}" stroke="{ORD if i == 1 else OCR}" stroke-width="1.2"/>'
        o += lab(x, y + 4.5, m, '#fff' if i == 1 else OCR, 11.5, fam='AH')
    a0, a1 = _om.radians(-76), _om.radians(-50); r2 = R + 38
    o += f'<path d="M{cx + r2 * _om.cos(a0):.1f},{cy + r2 * _om.sin(a0):.1f} A{r2},{r2} 0 0 1 {cx + r2 * _om.cos(a1):.1f},{cy + r2 * _om.sin(a1):.1f}" fill="none" stroke="{OPK}" stroke-width="2.5" stroke-linecap="round"/>' + lab(cx + 26, cy - R - 42, '+1♯', OPK, 14, fam='AH')
    o += call(1, xs[3] - 8, yb + 2, xs[3] - 8, yb + 62) + call(2, xs[5], S.y('E5') - 36, xs[5] + 60, 30)
    o += call(3, 86, S.y('F5') - 14, 60, 30) + call(4, 92, yb + 40, 60, yb + 62) + call(5, cx - R - 22, cy, cx - R - 60, cy)
    return f'<svg viewBox="0 0 760 {yb + 246}" style="width:100%;display:block">{o}</svg>'
LEG_S = [(1, 'Major scales', 'T T S T T T S: the two short steps', 'S1'), (2, 'Minor scales', 'the major with 3, 6 and 7 one key lower', 'S2'), (3, 'Keys and key signatures', 'the sharps at the start apply all the way', 'S3'), (4, 'Finding the key', 'last sharp, next key up; second-last flat', 'S4'), (5, 'The circle of fifths', 'go right: one more sharp each step', 'S5'), ('★', 'Tips: when a note sounds wrong', '', 'ST')]

# ---------- Part IV · Harmony ----------
def pic_harmony(mode='H'):   # her 6 Nov: one picture, two parts. 'H' = Chords (1-8), 'M' = Harmony in music (old 9-12 as 1-4)
    MAP = {'H': {1: 1, 2: 2, 3: 3, '4·8': '4·8', 5: 5, 6: 6, 7: 7}, 'M': {9: 1, 10: 2, 11: 3, 12: 4}}[mode]
    _c = lambda n, *a: call(MAP[n], *a) if n in MAP else ''
    _l = lambda want, *a: lab(*a) if want == mode else ''
    G = Staff(50, 780, 124, 11, 'G'); F = Staff(50, 780, 240, 11, 'F')
    o = G.lines() + F.lines() + G.clefsym() + F.clefsym() + brace(46, G.y1 - 4 * G.sp, F.y1) + G.tsig(100, 4, 4) + F.tsig(100, 4, 4)
    bars = [122, 262, 402, 542, 780]
    for x in bars[1:4]: o += G.bar(x) + F.bar(x)
    o += G.bar(780) + F.bar(780) + G.bar(788, w=4) + F.bar(788, w=4)
    mel = [[('C4', 'c'), ('C4', 'c'), ('G4', 'c'), ('G4', 'c')], [('A4', 'c'), ('A4', 'c'), ('G4', 'm')], [('F4', 'c'), ('F4', 'c'), ('E4', 'c'), ('E4', 'c')], [('D4', 'c'), ('D4', 'c'), ('C4', 'm')]]
    for b, notes in enumerate(mel):
        x0 = bars[b] + 22; w = (bars[b + 1] - bars[b] - 26) / 4; t = 0
        for n, k in notes:
            o += G.note(x0 + t * w, n, k, up=True); t += 2 if k == 'm' else 1
    chords = [(0, 0, ['C3', 'E3', 'G3'], 'C', 'I', 4, ()), (1, 0, ['F2', 'A2', 'C3'], 'F', 'IV', 2, ()), (1, 2, ['E3', 'G3', 'C4'], 'C/E', 'Ib', 2, ()), (2, 0, ['F2', 'A2', 'C3'], 'Fm', 'iv', 2, ()), (2, 2, ['C3', 'E3', 'G3'], 'C', 'I', 2, ()), (3, 0, ['G2', 'C3', 'D3'], 'Gsus4', 'Vsus4', 1, ()), (3, 1, ['G2', 'B2', 'D3', 'F3'], 'G7', 'V⁷', 1, ()), (3, 2, ['C3', 'E3', 'G3'], 'C(add9)', 'I', 2, ('D4',))]
    pos = {}; yn = G.y1 + 30; yb = F.y1 + 26
    for b, beat, notes, name, num, dur, extra in chords:
        x = bars[b] + 22 + beat * (bars[b + 1] - bars[b] - 26) / 4 + 2; pos[name + str(b) + str(beat)] = x
        o += F.chord(x, notes, dur >= 2, OCR, extra)
        if name == 'Fm' and mode == 'M': o += F.acc(x, 'A2', '♭', ORD)
        dn, dnum = ('F', 'IV') if (name == 'Fm' and mode == 'H') else (name, num)
        if dur == 1: o += f'<line x1="{x + F.sp * .55:.1f}" x2="{x + F.sp * .55:.1f}" y1="{F.y(notes[0]):.1f}" y2="{F.y(notes[-1]) - 3 * F.sp:.1f}" stroke="{OCR}" stroke-width="1.8"/>'
        o += lab(x, yn, dn, OCR, 12.5, fam='AH') + lab(x, yb, dnum, ORD if (num in ('V⁷', 'I') and b == 3) else OPK, 13, fam='AH')
    o += lab(104, yb, 'in C major:', OPK, 11, 'end', 'AH')
    xC, xF, xCE, xFm, xC2, xGs, xG7, xC9 = [pos[k] for k in ('C00', 'F10', 'C/E12', 'Fm20', 'C22', 'Gsus430', 'G731', 'C(add9)32')]
    # above: the tune, and the chords named between the staves
    o += _c(11, bars[0] + 60, G.y('G4') - 40, bars[0] + 60, 26) + _l('M', bars[0] + 78, 31, 'the tune picks the chords', OPK, 15, 'start')
    o += _c('4·8', xCE, yn - 14, xCE + 26, 26) + _c(6, xGs, yn - 14, xGs - 10, 26) + _c(5, xG7, yn - 14, xG7 + 22, 26) + _c(7, xC9 + 8, F.y('D4') - 8, xC9 + 54, 26)
    # below: the numerals row, then the trip
    ya = yb + 36
    o += _c(3, 92, yb + 4, 60, ya) + _c(1, xC, F.y('G3') + 10, xC, ya) + _c(2, xF, F.y('C3') + 10, xF, ya) + _c(9, xFm, F.y('C3') + 10, xFm, ya)
    o += _l('H', xF + 18, ya + 5, 'major', OPK, 13, 'start') + _l('M', xFm + 18, ya + 5, 'a guest note: minor', OPK, 13, 'start')
    o += _c(10, (xG7 + xC9) / 2, yb + 6, (xG7 + xC9) / 2, ya) + _l('M', (xG7 + xC9) / 2 + 16, ya + 5, 'full stop', OPK, 13, 'start')
    yt = ya + 36
    o += (f'<path d="M{xC - 14},{yt - 6} V{yt} H{xC9 + 14} V{yt - 6}" fill="none" stroke="{OPK}" stroke-width="1.3"/>' if mode == 'M' else '') + _c(12, (xC + xC9) / 2, yt, (xC + xC9) / 2, yt + 18) + _l('M', (xC + xC9) / 2 + 18, yt + 23, 'a trip from home and back', OPK, 15, 'start')
    return f'<svg viewBox="0 0 800 {yt + (36 if mode == "M" else 0)}" style="width:100%;display:block">{o}</svg>'
LEG_H = [(1, 'Chords and triads', 'three notes stacked like a layer cake', 'H1'), (2, 'Four kinds of triad', 'major 3 + 2, minor 2 + 3', 'H2'), (3, 'Chords in a key', 'Roman numerals: I, IV and V do most of the work', 'H3'), (4, 'Inversions', 'the same notes, a different one at the bottom', 'H4'), (5, 'Seventh chords', 'one more layer on top: G7', 'H5'), (6, 'Colour chords', 'sus and add: a note moved or added', 'H6'), (7, 'The tower: 9, 11, 13', 'keep skipping a letter', 'H7'), (8, 'Slash chords', 'C/E: the chord, then the bass note', 'H8'), ('★', 'Tips: when a chord sounds wrong', '', 'HT')]
LEG_M = [(1, 'Chords from outside the key', 'a guest note: A♭ in C major', 'M1'), (2, 'Cadences', 'V to I ends a phrase like a full stop', 'M2'), (3, 'Chords under a melody', 'the tune’s main notes pick the chord', 'M3'), (4, 'Progressions everywhere', 'the same few trips, in every song', 'M4'), ('★', 'Tips: when harmony goes wrong', '', 'MT')]


# ---------- Part III · Expression (her 8 Nov: the parts the Handbook still needed, in order) ----------
def pic_expr():
    S = Staff(40, 760, 170, 12); o = S.lines() + S.clefsym() + S.tsig(104, 4, 4)
    o += f'<text x="128" y="{S.y1 - 5.6 * S.sp:.0f}" font-family="PF" font-size="20" font-weight="700" fill="{OCR}">Andante</text>'
    xs = [140, 196, 252, 308]; ns = ['C4', 'E4', 'G4', 'E4']
    for x, n in zip(xs, ns): o += S.note(x, n)
    o += f'<path d="M{xs[0] + 4},{S.y("C4") + 11:.0f} Q{(xs[0] + xs[-1]) / 2},{S.y("C4") + 30:.0f} {xs[-1] + 2},{S.y("E4") + 12:.0f}" fill="none" stroke="{OCR}" stroke-width="2"/>' + S.bar(336)
    xs2 = [362, 412, 462, 512]
    for x in xs2: o += S.note(x, 'G4') + f'<circle cx="{x}" cy="{S.y("G4") + 15:.0f}" r="2.6" fill="{OCR}"/>'
    o += S.bar(540) + S.note(580, 'A4', 'm') + f'<text x="572" y="{S.y1 - 4.6 * S.sp:.0f}" font-family="PF" font-size="18" font-style="italic" font-weight="700" fill="{OCR}">tr</text>'
    o += S.note(660, 'G4', 'm') + f'<path d="M648,{S.y("G4") - 46:.0f} a12,12 0 0 1 24,0" fill="none" stroke="{OCR}" stroke-width="2.4"/><circle cx="660" cy="{S.y("G4") - 50:.0f}" r="2.4" fill="{OCR}"/>' + S.end(740)
    yd = S.y1 + 66
    o += f'<text x="132" y="{yd}" font-family="PF" font-size="24" font-style="italic" font-weight="700" fill="{OCR}">p</text><path d="M160,{yd - 9} L320,{yd - 20} M160,{yd - 9} L320,{yd + 2}" stroke="{OCR}" stroke-width="1.8" fill="none"/>'
    o += f'<text x="350" y="{yd}" font-family="PF" font-size="24" font-style="italic" font-weight="700" fill="{OCR}">f</text>'
    o += f'<text x="590" y="{S.y1 - 6.4 * S.sp:.0f}" font-family="AH" font-size="15" font-style="italic" fill="{OCR}">rit.</text>'
    yp = yd + 42
    o += f'<text x="130" y="{yp}" font-family="PF" font-size="17" font-style="italic" font-weight="700" fill="{OCR}">Ped.</text><path d="M176,{yp - 5} H520" stroke="{OCR}" stroke-width="1.5" stroke-dasharray="5 4"/><text x="528" y="{yp + 2}" font-family="AH" font-size="20" font-weight="700" fill="{OCR}">*</text>'
    o += lab(420, yp + 44, 'loud and soft, smooth and short, slower, ringing, decorated', OPK, 20)
    o += call(1, 136, yd - 6, 80, yd - 2) + call(2, 436, S.y("G4") + 18, 436, S.y1 + 40)
    o += call(2, 226, S.y("C4") + 26, 262, S.y1 + 40) + call(3, 134, S.y1 - 6 * S.sp, 96, S.y1 - 8.4 * S.sp) + call(3, 604, S.y1 - 6.8 * S.sp, 640, S.y1 - 8.4 * S.sp)
    o += call(4, 150, yp - 6, 92, yp + 26) + call(5, 580, S.y1 - 5.2 * S.sp, 540, S.y1 - 8.4 * S.sp) + call(3, 670, S.y("G4") - 56, 712, S.y1 - 8.4 * S.sp)
    return f'<svg viewBox="0 0 800 {yp + 60}" style="width:100%;display:block">{o}</svg>'
LEG_E = [(1, 'Loud and soft', 'p, f and the steps between; hairpins grow and fade', 'E1'), (2, 'Touch: smooth, short, strong', 'slurs, staccato dots, tenuto lines and accents', 'E2'), (3, 'Speed words', 'Andante, Allegro; rit. slows down, a fermata waits', 'E3'), (4, 'The pedals', 'Ped. down, * up: the right pedal keeps notes ringing', 'E4'), (5, 'Ornaments', 'trills, mordents, turns and grace notes', 'E5'), ('★', 'Tips: when your playing sounds flat', '', 'ET')]
def opener_art(kick, title, line, part, PAGE, cls=''):
    pic, leg = {'T': (pic_time, LEG_T), 'P': (pic_pitch, LEG_P), 'S': (pic_scales, LEG_S), 'H': (pic_harmony, LEG_H), 'M': (lambda: pic_harmony('M'), LEG_M), 'E': (pic_expr, LEG_E)}[part]
    rows = ''.join(f'<div><span class="ln"{" style=\"background:#f4a9bb\"" if n == "★" else ""}>{n}</span><div><b>{t}</b> <span class="pg2">p. {PAGE[k]}</span>' + (f'<br><span>{d}</span>' if d else '') + '</div></div>' for n, t, d, k in leg)
    return f'''<section class="pg part2 {cls}"><div class="pframe"><div class="pk">{kick}</div><div class="pt">{title}</div><div class="pdv"></div>
<p class="pl">{line}</p>
{pic()}
<div class="legA{" leg3" if len(leg) > 9 else ""}">{rows}</div></div></section>'''
OPENCSS = '''
.part2 .pl{margin-bottom:18px}
.legA{display:grid;grid-template-columns:1fr 1fr;gap:13px 30px;margin-top:30px;font-size:12.5px;line-height:1.4;color:#fffdf7} .legA>div{display:flex;gap:8px;align-items:flex-start} .legA b{font-size:13.5px} .legA .ln{flex:0 0 22px;height:22px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;font-size:12.5px;display:flex;align-items:center;justify-content:center;margin-top:1px} .legA .pg2{color:#f4a9bb;font-weight:700;font-size:12px;margin-left:4px} .legA>div>div>span:last-child{opacity:.85}
.legA.leg3{gap:10px 24px;font-size:12px} .legA.leg3 b{font-size:13px}
'''
