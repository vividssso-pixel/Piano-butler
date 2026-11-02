# The Piano Butler Handbook, Part II: Time (full draft)
import json, re, base64
R = json.load(open('/tmp/claude-0/pk/lib-notes-rows.json'))
DK, N, C, CR, G = '#1c1e4f', '#26296b', '#e4572e', '#fffdf7', '#2e8a6e'
src8 = open('/tmp/claude-0/pk/book8.py').read()
exec(src8[src8.index('src = open'):src8.index('PARTS = [')].replace("open('/mnt/user-data/outputs/house-rooms/handbook.html', 'w')", 'None and open'))
PARTS_SRC = src8[src8.index('PARTS = ['):src8.index('toc = ')]
exec(PARTS_SRC)
exec(src8[src8.index('steps = ['):src8.index('names = [')])
css8 = src8[src8.index("css = base + f'''"):src8.index("FF = ")]
exec(css8)

# glyphs: note i / rest i from the Library table rows (2*i note, 2*i+1 rest)
IDX = {'breve': 0, 'dsb': 1, 'sb': 2, 'dm': 3, 'm': 4, 'dc': 5, 'c': 6, 'dq': 7, 'q': 8, 'sq': 9}
def nt(k, h=34): return g(2 * IDX[k], h)
def rs(k, h=34): return g(2 * IDX[k] + 1, h)
def count(items, cap=''):
    """items: list of (svg, count text, width units)"""
    cells = ''.join(f'<div class="cn" style="flex:{w}"><div class="cg">{s}</div><div class="cc2">{t}</div></div>' for s, t, w in items)
    return f'<div class="count"><div class="cl">{cells}</div>{f"<div class=ccap>{cap}</div>" if cap else ""}</div>'
def row(x): return f'<div style="display:flex;gap:4px;align-items:flex-end">{x}</div>'
def bar(): return ('<span class="bl"></span>', '', 0.15)
def ts(top, bot): return f'<span class="ts"><b>{top}</b><b>{bot}</b></span>'
def tbl(head, rows, cls=''):
    return f'<table class="ht {cls}"><thead><tr>{"".join(f"<th>{h}</th>" for h in head)}</tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table>'
def lv(x): return f'<span class="lvl">{x}</span>' if x else '<span class="lvl ex">beyond Level 8</span>'
def note(title, body): return f'<div class="side"><div class="sh2">{title}</div>{body}</div>'
def watch(items): return '<div class="watch"><div class="sh2">Watch out</div>' + ''.join(f'<div class="wr"><span>✗</span><span>{t}</span></div>' for t in items) + '</div>'
def seealso(items): return '<div class="see"><span class="gl">See also</span>' + ' · '.join(f'{t} <span class="pg2">p. {p}</span>' for t, p in items) + '</div>'
def tp(inner, n): return page(inner, n, 'PART II · TIME')

# ---------- p36 Pulse and the bar ----------
P36 = tp(f'''<div class="kick">Part II · Time · 1</div><h1>Pulse and the bar</h1>
<p class="lead">Under almost every piece runs a <b>pulse</b>: a steady beat, like a heartbeat or a clock. The speed of the pulse is the <b>tempo</b>, measured in beats per minute (♩ = 60 is one beat a second). Beats are grouped into <b>bars</b>, and the first beat of each bar is the strongest.</p>
<div class="two">
<div><div class="h3">Strong and weak beats</div>
{tbl(['Beats in a bar', 'Pattern', 'Feels like'], [['2', '<b>S</b> w', 'a march: left, right'], ['3', '<b>S</b> w w', 'a waltz: one, two, three'], ['4', '<b>S</b> w <b>m</b> w', 'most songs: a lighter stress on 3']])}
<div class="fn2">S = strong · m = medium · w = weak</div></div>
<div><div class="h3">On the page</div>
{tbl(['Sign', 'Name', 'Meaning'], [['<span class="sg">|</span>', 'bar line', 'ends a bar'], ['<span class="sg">‖</span>', 'double bar line', 'ends a section'], ['<span class="sg">𝄂</span>', 'final bar line', 'ends the piece'], ['<span class="sg">𝄇</span>', 'repeat sign', 'go back and play again']])}</div></div>
<div class="h3" style="margin-top:12px">How to count</div>
{count([(nt('c'), '<b>1</b>', 1), (nt('c'), '2', 1), (nt('c'), '3', 1), bar(), (nt('m'), '<b>1</b> &nbsp;2', 2), (nt('c'), '3', 1), bar(), (nt('dm'), '<b>1</b> &nbsp;2 &nbsp;3', 3)], 'Three bars of 3/4: the counting never changes, whatever the notes do.')}
<p class="txt">Count every beat aloud, the same speed from start to end: “<b>1</b> 2 3 <b>1</b> 2 3”. Say the bar’s first beat a little louder. A metronome keeps you honest: set it slower than you think, and only speed up when a whole passage is steady.</p>
{watch(['Speeding up in easy places and slowing down in hard ones: choose the speed of the hardest bar.', 'Counting the notes instead of the beats: a long note still has its beats counted through it.'])}
{seealso([('Time signatures', 40), ('Tempo words', 70)])}
<div class="pr2"><span class="gl">Practise it</span>Workbook Level 0 · Pulse · Online: Metronome, Rhythm clock</div>''', 36)

# ---------- p38 Notes and rests (existing) + p39 How long ----------
names = [('breve', '8', 'Level 4'), ('dotted semibreve', '6', ''), ('semibreve', '4', 'Level 0'), ('dotted minim', '3', 'Level 0'), ('minim', '2', 'Level 0'), ('dotted crotchet', '1½', 'Level ½'), ('crotchet', '1', 'Level 0'), ('dotted quaver', '¾', 'Level 3'), ('quaver', '½', 'Level 0'), ('semiquaver', '¼', 'Level 2'), ('demisemiquaver', '⅛', ''), ('hemidemisemiquaver', '1/16', '')]
rows = ''.join(f'<tr><td>{g(2 * i)}</td><td>{g(2 * i + 1)}</td><td class="nmc">{n}</td><td class="bt">{b}</td><td class="lv">{lv(l)}</td></tr>' for i, (n, b, l) in enumerate(names))
P38 = tp(f'''<div class="kick">Part II · Time · 2</div><h1>Notes and rests</h1>
<p class="lead">A note’s shape shows how long it lasts. Each plain note lasts <b>half as long</b> as the one above it. Every note has a <b>rest</b> of the same length: a silence, counted just as carefully as a sound.</p>
<table class="nt"><thead><tr><th>Note</th><th>Rest</th><th>Name</th><th>Beats*</th><th>First met</th></tr></thead><tbody>{rows}</tbody></table>
<div class="fn2">* With the crotchet as one beat, as in 2/4, 3/4 and 4/4. The names used in the USA: semibreve = whole note, minim = half note, crotchet = quarter note, quaver = eighth note, semiquaver = sixteenth note.</div>''', 38)

tree = ''.join(f'<div class="trw"><span class="trl">{lab}</span><div class="trc">' + ''.join(f'<div class="tri" style="flex:1">{nt(k, 30)}</div>' for _ in range(n)) + '</div></div>' for lab, k, n in (('1 semibreve', 'sb', 1), ('2 minims', 'm', 2), ('4 crotchets', 'c', 4), ('8 quavers', 'q', 8), ('16 semiquavers', 'sq', 16)))
P39 = tp(f'''<div class="kick">Part II · Time · 2</div><h1>How long is a note?</h1>
<p class="lead">Each row lasts exactly as long as the one above it: the same bar of time, cut into halves again and again.</p>
<div class="tree">{tree}</div>
<div class="two" style="margin-top:14px">
<div><div class="h3">The dot</div><p class="txt">A dot adds <b>half the note’s value</b>. A minim (2) with a dot lasts 2 + 1 = 3; a crotchet (1) with a dot lasts 1 + ½ = 1½. A second dot adds half of that again.</p>
{count([(nt('dm'), '1 2 3', 3), bar(), (nt('dc'), '1 &nbsp;2', 1.5), (nt('q'), '&', 0.5), (nt('m'), '3 &nbsp;4', 2)], 'Count through every beat a long note covers.')}</div>
<div><div class="h3">The tie</div><p class="txt">A curved line joining two notes <b>of the same pitch</b> makes one longer sound: play the first, hold through the second. A tie can carry a note across a bar line, where a dot cannot.</p>
<div class="h3" style="margin-top:8px">Tie or slur?</div><p class="txt">The same curve over notes of <b>different</b> pitches is a <b>slur</b>: play them smoothly joined (legato). Same pitch: tie. Different pitches: slur.</p></div></div>
{note('Rests in a bar', '<p class="txt" style="margin:0">A whole bar of silence is shown with a <b>semibreve rest</b> in the middle of the bar, whatever the time signature (in 4/2, a breve rest). Shorter rests follow the beats: in 4/4, two crotchet rests on beats 3 and 4 are written as one minim rest, but on beats 2 and 3 as two crotchet rests, so the middle of the bar stays visible.</p>')}
{seealso([('Time signatures', 40), ('Rhythm', 44)])}''', 39)

# ---------- p40-41 Time signatures ----------
bottom = [['2', nt('m', 30), 'minim', lv('Level 3')], ['4', nt('c', 30), 'crotchet', lv('Level 0')], ['8', nt('q', 30), 'quaver', lv('Level 1')], ['16', nt('sq', 30), 'semiquaver', lv('')]]
simple = [[ts(2, 4), '2 crotchets', lv('Level 0')], [ts(3, 4), '3 crotchets', lv('Level 0')], [ts(4, 4) + ' <span class="sg">C</span>', '4 crotchets (C: common time)', lv('Level 0')], [ts(2, 2) + ' <span class="sg">¢</span>', '2 minims (¢: cut common time)', lv('Level 3')], [ts(3, 2), '3 minims', lv('Level 3')], [ts(3, 8), '3 quavers', lv('Level 3')]]
compound = [[ts(6, 8), '2 dotted crotchets', lv('Level 1')], [ts(9, 8), '3 dotted crotchets', lv('Level 3')], [ts(12, 8), '4 dotted crotchets', lv('Level 3')], [ts(6, 4), '2 dotted minims', lv('Level 4')], [ts(9, 4) + ' ' + ts(12, 4) + ' ' + ts(6, 16), 'rare', lv('')]]
irreg = [[ts(5, 4), '5 crotchets: 3 + 2 or 2 + 3', lv('Level 0')], [ts(7, 4), '7 crotchets: 4 + 3 or 3 + 4', lv('')], [ts(5, 8), '5 quavers: 3 + 2 or 2 + 3', lv('')], [ts(7, 8), '7 quavers: 2 + 2 + 3 or 3 + 2 + 2', lv('')]]
P40 = tp(f'''<div class="kick">Part II · Time · 3</div><h1>Time signatures</h1>
<p class="lead">Two numbers at the start of the music. The <b>top number</b> says how many counts are in each bar; the <b>bottom number</b> says which note gets one count.</p>
<div class="two"><div><div class="h3">The bottom number</div>{tbl(['Bottom', 'Note', 'One count is a', 'First met'], bottom, 'mid')}</div>
<div>{note('Simple or compound?', '<p class="txt" style="margin:0">In <b>simple time</b> each beat splits into two. In <b>compound time</b> each beat is a dotted note and splits into three. A quick test: a top number of <b>6, 9 or 12</b> means compound; divide it by 3 to find the beats (6/8 has 2 beats, 9/8 has 3, 12/8 has 4).</p>')}</div></div>
<div class="h3" style="margin-top:10px">Simple time: each beat splits in two</div>{tbl(['Time signature', 'Each bar holds', 'First met'], simple, 'mid')}
''', 40)
P41 = tp(f'''<div class="kick">Part II · Time · 3</div><h1>Compound and irregular time</h1>
<div class="h3">Compound time: each beat is a dotted note and splits in three</div>{tbl(['Time signature', 'Each bar holds', 'First met'], compound, 'mid')}
<div class="h3" style="margin-top:12px">Counting 6/8</div>
{count([(nt('q'), '<b>1</b>', 1), (nt('q'), '2', 1), (nt('q'), '3', 1), (nt('q'), '<b>4</b>', 1), (nt('q'), '5', 1), (nt('q'), '6', 1), bar(), (nt('dc'), '<b>1</b> &nbsp;2 &nbsp;3', 3), (nt('dc'), '<b>4</b> &nbsp;5 &nbsp;6', 3)], 'Slow: count all six quavers. Faster: feel two beats, on 1 and 4 (“1 & a, 2 & a”).')}
<div class="h3" style="margin-top:12px">Irregular time: five or seven, in uneven groups</div>{tbl(['Time signature', 'Each bar holds', 'First met'], irreg, 'mid')}
<p class="txt" style="margin-top:8px">The grouping can also change inside a regular bar: many dances, calypso among them, keep 4/4 but group the eight quavers <b>3 + 3 + 2</b>.</p>
{watch(['Reading 6/8 as “six beats”: at most speeds it moves in two.', 'Mixing up 3/4 and 6/8: both hold six quavers, but 3/4 groups them in twos (three beats) and 6/8 in threes (two beats).'])}
{seealso([('Pulse and the bar', 36), ('Rhythm', 44)])}
<div class="pr2"><span class="gl">Practise it</span>Workbook Level 0 · Time signatures · Online: Library › Time signatures (hear each one)</div>''', 41)

# ---------- p44 Rhythm ----------
rh = [['dot', 'adds half the note’s value; a double dot adds half and then a quarter', lv('Level ½')], ['tie', 'joins two notes of the same pitch into one sound', lv('Level ½')], ['triplet', 'three notes in the time of two', lv('Level 2')], ['duplet', 'two notes in the time of three, in compound time', lv('Level 2')],
      ['anacrusis', 'notes before the first full bar (an upbeat); the last bar is short by the same amount', lv('Level 4')], ['syncopation', 'the stress falls off the beat', lv('Level 4')], ['hemiola', 'two bars of three felt as three bars of two', lv('Level 4')], ['grouping', 'beams show the beats: in 4/4 never across the middle of the bar; in 6/8 in threes', lv('Level 4')],
      ['swing', 'pairs of quavers played long–short, like a triplet', lv('')], ['polyrhythm', 'two rhythms at once, such as three against two', lv('Level 7')], ['rubato', 'time given and taken back, for expression', lv('')]]
P44 = tp(f'''<div class="kick">Part II · Time · 4</div><h1>Rhythm</h1>
<p class="lead">Rhythm is the pattern of long and short sounds laid over the pulse. The pulse stays steady; the rhythm moves around it.</p>
{tbl(['Term', 'What it means', 'First met'], rh, 'rh')}
<div class="two" style="margin-top:12px">
<div><div class="h3">Counting smaller values</div>{tbl(['Note', 'Say'], [[row(nt('c', 28)), '1'], [row(nt('q', 28) * 2), '1 &amp;'], [row(nt('sq', 28) * 4), '1 e &amp; a'], [row(g(24, 34)), '1 trip-let (or 1 &amp; a)']], 'mid')}</div>
<div>{watch(['Rushing the short notes after a long one: keep counting inside the long note.', 'Playing a triplet as two quavers and a crotchet: three exactly equal notes.', 'Forgetting the upbeat: if the piece starts on beat 4, count “1 2 3” in silence first.'])}</div></div>
{seealso([('Notes and rests', 38), ('Time signatures', 40), ('Words for how to play', 70)])}
<div class="pr2"><span class="gl">Practise it</span>Workbook Levels 0–4 · Rhythm · Online: Rhythm clock, Rhythm sheet</div>''', 44)

css += f'''
.txt{{font-size:13.5px;line-height:1.55;color:#2f3270;margin:4px 0 8px}}
.ht{{width:100%;border-collapse:collapse;font-size:13px}} .ht th{{font-size:9.5px;font-weight:900;letter-spacing:.13em;text-transform:uppercase;color:#8a8cb0;text-align:left;padding:4px 6px;border-bottom:1.5px solid {N}}} .ht td{{border-bottom:.6px solid #e2ddd0;padding:5px 6px;vertical-align:middle}}
.ht.mid td{{padding:4px 6px}} .ht.rh td:first-child{{font-weight:800;width:92px}} .ht.rh td:last-child{{width:96px}}
.lvl{{font-size:11px;font-weight:700;color:{N};border:1px solid #c9cbe0;border-radius:10px;padding:1px 7px;white-space:nowrap}} .lvl.ex{{color:#9a9cc4;border-style:dashed;font-weight:600;font-style:italic}}
.sg{{font-family:'Playfair Display',Georgia,serif;font-size:20px;font-weight:700}}
.ts{{display:inline-flex;flex-direction:column;align-items:center;line-height:.82;font-family:'Playfair Display',Georgia,serif;font-size:17px;vertical-align:middle;margin-right:4px}}
.side{{border-left:2.5px solid {C};padding:4px 0 4px 12px;margin:8px 0}} .sh2{{font-size:10px;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:{C};margin-bottom:2px}}
.watch{{border-top:.8px solid #c9cbe0;border-bottom:.8px solid #c9cbe0;padding:8px 2px;margin:10px 0}} .wr{{display:flex;gap:8px;font-size:13px;line-height:1.5;color:#2f3270;padding:2px 0}} .wr span:first-child{{color:{C};font-weight:900}}
.see{{font-size:12.5px;color:#3d4080;margin-top:10px}} .see .gl{{margin-right:8px}} .pr2{{font-size:12.5px;color:#3d4080;margin-top:6px}} .pr2 .gl{{margin-right:8px}}
.count{{border:1px solid #d9d4c6;background:#fff;padding:8px 10px 6px;margin:6px 0}} .cl{{display:flex;align-items:flex-end;gap:2px}} .cn{{text-align:center;min-width:0}} .cg{{height:40px;display:flex;align-items:flex-end;justify-content:center}} .cc2{{font-size:12px;font-weight:700;color:{C};margin-top:3px;white-space:nowrap}}
.bl{{display:block;width:1.5px;height:44px;background:{N};margin:0 auto}} .ccap{{font-size:11px;color:#6d6f9c;margin-top:4px}}
.tree{{border:1px solid #d9d4c6;background:#fff;padding:10px 14px}} .trw{{display:flex;align-items:center;gap:12px;border-bottom:.6px solid #eee8da;padding:5px 0}} .trw:last-child{{border:0}} .trl{{flex:none;width:110px;font-size:12.5px;font-weight:700}} .trc{{flex:1;display:flex}} .tri{{text-align:center;border-left:1px dashed #e2ddd0}} .tri:first-child{{border-left:0}}
'''
FF = ''.join("@font-face{font-family:'Playfair Display';font-weight:700;font-style:%s;src:url(data:font/woff2;base64,%s) format('woff2')}" % (st, base64.b64encode(open('/tmp/claude-0/fnt/package/files/playfair-display-latin-700-%s.woff2' % st, 'rb').read()).decode()) for st in ('normal', 'italic'))
open('/mnt/user-data/outputs/house-rooms/handbook-time.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet"><style>{css}</style></head><body>{PART2}{P36}{P38}{P39}{P40}{P41}{P44}</body></html>')
print('ok')
