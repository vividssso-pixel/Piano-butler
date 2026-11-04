# The Piano Butler Workbook, Time (expanded): two pages per topic (Learn, Use), stars for difficulty, review, progress, answers
exec(open('/tmp/claude-0/pk/wbtime.py').read())   # helpers, css, W (snippets), old pages
N_ = N
def star(n): return '★' * n + '<span class="so">' + '★' * (3 - n) + '</span>'
def ex(n, title, stars, how, body):
    return f'<div class="ex2"><div class="eh"><span class="en">{n}</span><b>{title}</b><span class="el">{star(stars)}</span></div><p class="how">{how}</p>{body}</div>'
def tp(kind, topic, title, rule, inner, n, hb):
    hb = hb + 12   # Part II now starts at p. 48
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
def pizza(n, fill=0, R=34):   # a circle cut into n equal slices; the first `fill` slices coloured red
    cx = cy = R + 3; s = f'<svg viewBox="0 0 {2 * R + 6} {2 * R + 6}" style="width:{2 * R + 6}px;height:{2 * R + 6}px;display:block;margin:0 auto">'
    if n == 1:
        s += f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="{C if fill else "#fff"}" fill-opacity="{0.85 if fill else 1}" stroke="{N_}" stroke-width="2"/>'
    else:
        for i in range(n):
            a0, a1 = -_m.pi / 2 + 2 * _m.pi * i / n, -_m.pi / 2 + 2 * _m.pi * (i + 1) / n
            x0, y0, x1, y1 = cx + R * _m.cos(a0), cy + R * _m.sin(a0), cx + R * _m.cos(a1), cy + R * _m.sin(a1)
            s += f'<path d="M{cx},{cy} L{x0:.1f},{y0:.1f} A{R},{R} 0 0 1 {x1:.1f},{y1:.1f} Z" fill="{C if i < fill else "#fff"}" fill-opacity="0.85" stroke="{N_}" stroke-width="1.6"/>'
    return s + '</svg>'
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
items = [('sb', 'semibreve', '4'), ('c', '', ''), ('m', '', ''), ('q', '', ''), ('dm', '', ''), ('sq', '', '')]
rows = [[gcell('n', k, 38), f'<b>{n}</b>' if n else LINE, f'<b>{b}</b>' if b else BOX, gcell('r', k, 38) if n else BOX] for k, n, b in items]
NTB = '<table class="ht nt"><colgroup><col style="width:14%"><col style="width:40%"><col style="width:18%"><col style="width:28%"></colgroup><thead><tr><th>Note</th><th>Name</th><th>Beats</th><th>Rest</th></tr></thead><tbody>' + ''.join('<tr>' + ''.join(f'<td class="g">{c}</td>' if i in (0, 3) else f'<td>{c}</td>' for i, c in enumerate(r)) + '</tr>' for r in rows) + '</tbody></table>'
PIZZA = ex(3, 'Why a whole note?', 1, 'Think of a pizza. The semibreve is the whole pizza: 4 beats, so it is also called a <b>whole note</b>. Colour one slice of each pizza, then write its other name and its beats. The first is done.', '<div class="pz">' + ''.join(f'<div>{pizza(n, n if d else 0) if n == 1 else pizza(n, 0)}<span class="pzn">{gin("n", k)} {nm}</span><span class="pzl">{("<b class=done2>" + oc + "</b>") if d else WL}</span><span class="pzl">{("<b class=done2>" + bt + "</b>") if d else WL + " beats"}</span></div>' for n, nm, _g, k, oc, bt, d in ((1, 'semibreve', 'n', 'sb', 'whole note', '4 beats', True), (2, 'minim', 'n', 'm', '', '', False), (4, 'crotchet', 'n', 'c', '', '', False), (8, 'quaver', 'n', 'q', '', '', False))) + '</div>')
A2 = tp('Learn', 'Notes and rests', 'Notes and rests', 'Each plain note lasts half as long as the one above it; every note has a rest of the same length.', f'''
{ex(1, 'Name, beats and rest', 1, 'Write each note’s name and beats (crotchet = 1 beat), then draw the rest of the same length. The first row is done.', NTB)}
{ex(2, 'Draw it', 2, 'Draw one note for each length (crotchet = 1 beat).', '<div class="mm4">' + ''.join(f'<div><span class="drw"></span><span class="mmk">{t}</span></div>' for t in ('2 beats', '½ beat', '3 beats', '4 beats')) + '</div>')}
{PIZZA}''', 3, 38)
heads = [(70, 62), (130, 50), (190, 26), (250, 32), (310, 56), (370, 20), (430, 68), (490, 38), (550, 44)]
B2 = tp('Use', 'Notes and rests', 'Notes and rests', 'Below the middle line, stems go up on the right; above it, down on the left.', f'''
{ex(1, 'Rests on the staff', 1, 'Draw a semibreve rest in the first bar (it hangs below the fourth line) and a minim rest in the second (it sits on the middle line).', staff('', 2))}
{ex(2, 'Draw the stems', 2, 'Turn every head into a crotchet: add a stem going the right way. The first is done.', staff('', 1, heads=heads, stems=[0]))}
{ex(3, 'Finish with a rest', 2, 'Each bar is short. Complete it with one rest.', grid([cell(k, 'rest ' + BOX, 64) for k in ('wra', 'wrb', 'wrc', 'wrd')], 4))}
{ex(4, 'Which did you hear?', 2, 'Someone claps one rhythm from each row (or play it in the online Library). Circle A, B or C.', opts(('wa1', 'wa2', 'wa3')) + opts(('wa4', 'wa5', 'wa6')))}''', 4, 38)

# ---------- 3 How long ----------
sums = [(['m', 'c'], '3'), (['c', 'q'], ''), (['dm', 'c'], ''), (['sb', 'm'], ''), (['dc', 'q'], ''), (['q', 'q', 'q', 'q'], '')]
srows = ''.join('<div class="sum">' + ' <span class="pl">+</span> '.join(gin('n', k, 34) for k in ks) + ' <span class="pl">=</span> ' + (f'<b class="done">{a}</b>' if a else BOX) + ' <span class="mu2">beats</span></div>' for ks, a in sums)
A3 = tp('Learn', 'How long is a note?', 'How long is a note?', 'A dot adds half the note’s value; a tie joins two notes of the same pitch into one sound.', f'''
{ex(1, 'Note sums', 1, 'Add up the beats (crotchet = 1 beat). The first one is done.', f'<div class="sums">{srows}</div>')}
{ex(2, 'Complete the bar', 2, 'Each bar is one note short. Count the beats you have, then find what is missing. The first is done: 4/4 needs 4 beats; minim 2 + crotchet 1 = 3, so <b>1 beat</b> is missing: a crotchet.', grid([cell('wf1', 'one note <b class="done2">crotchet</b>', 64)] + [cell(k, 'one note ' + BOX, 64) for k in ('wf2', 'wf3', 'wf4', 'wf5', 'wf6')], 3))}
{ex(3, 'Dots and ties: count it', 2, 'Write a count in every box.', wx('wc44', 84))}''', 5, 40)
B3 = tp('Use', 'How long is a note?', 'How long is a note?', 'A tie can cross a bar line; a dot cannot.', f'''
{ex(1, 'Tie or dot?', 2, 'Each tie makes one sound. Write the one dotted note that lasts the same.', grid([cell(k, 'dotted note ' + BOX, 60) for k in ('wti1', 'wti2', 'wti3')], 3))}
{ex(2, 'Spot the mistake', 2, 'One bar does not add up to four beats. Circle it and correct it.', wx('wmis2', 70))}
{ex(3, 'Clap and count', 1, 'Clap the dotted rhythms, counting the “&” inside each dotted crotchet. Tick a circle each time it is steady.', wx('wl2', 66) + ticks())}
{ex(4, 'In your music', 1, 'Find each of these in a piece you are learning.', piece(['a dotted minim', 'a dotted crotchet', 'a tie', 'a rest of one whole bar']))}''', 6, 40)

# ---------- 4 Time signatures ----------
sc = [ts(3, 4), ts(6, 8), ts(2, 2), ts(9, 8), ts(4, 4), ts(12, 8), ts(3, 8), ts(6, 4)]
scrows = ''.join(f'<div class="scc">{x}<span class="sel">simple · compound</span><span class="add">beats {BOX}</span></div>' for x in sc)
A4 = tp('Learn', 'Time signatures', 'Time signatures', 'Top number: how many counts in a bar. Bottom number: which note is one count.', f'''
{ex(1, 'Which time signature?', 1, 'Each line is one full bar. Write a time signature that fits.', grid([cell(k, 'time signature ' + BOX, 60) for k in ('wt1', 'wt2', 'wt3', 'wt4', 'wt5', 'wt6')], 3))}
{ex(2, 'Simple or compound?', 2, 'Circle simple or compound, then write how many beats are in each bar.', f'<div class="scg">{scrows}</div>')}
{ex(3, 'What does it mean?', 1, 'Complete each sentence.', '<div class="sent"><p>In 3/4 there are ' + BOX + ' beats in a bar, and each beat is a ' + LINE.replace('al', 'al inl') + '.</p><p>In 6/8 there are ' + BOX + ' beats in a bar, and each beat is a ' + LINE.replace('al', 'al inl') + '.</p><p>C means the same as ' + BOX + ' ; ¢ means the same as ' + BOX + ' .</p></div>')}''', 7, 42)
B4 = tp('Use', 'Time signatures', 'Time signatures', 'In compound time each beat is a dotted note, divided into three.', f'''
{ex(1, 'Add the bar lines', 2, 'Draw a bar line after every full bar, and a final bar line at the end.', wx('wb1', 50) + wx('wb2', 50) + wx('wb3', 50))}
{ex(2, 'Beam them', 3, 'The same six quavers in two time signatures. Join them with beams to show the beats: in twos for 3/4, in threes for 6/8.', grid([cell('wbm2', '3 beats', 64), cell('wbm1', '2 beats', 64)], 2))}
{ex(3, 'Make your own', 3, 'Write one bar of 6/8 and one bar of 3/4 with six quavers each, beamed correctly. Clap both and feel the difference.', staff('6/8', 1) + staff('3/4', 1))}''', 8, 42)

# ---------- 5 Rhythm ----------
A5 = tp('Learn', 'Rhythm', 'Rhythm', 'Beams join the notes of one beat, so the beats stay visible.', f'''
{ex(1, 'Good grouping?', 2, 'Circle ✓ if the grouping shows the beats, ✗ if it hides one.', grid([cell(k, '✓ &nbsp; ✗', 64) for k in ('wg1', 'wg2', 'wg3', 'wg4')], 2))}
{ex(2, 'Count it', 2, 'Write a count in every box: a triplet, then a syncopation.', '<div class="two" style="grid-template-columns:1fr 1fr">' + wx('wtr', 80) + wx('wsy', 80) + '</div>')}
{ex(3, 'The upbeat', 2, 'This piece starts on beat 3. Write a count in every box. Then: how many beats does the last bar need?', wx('wan', 70) + f'<div class="add">beats in the last bar {BOX}</div>')}
{ex(4, 'Clap the upbeat', 1, 'Clap the piece in exercise 3 with a metronome: count “1 2” silently, clap on 3. Tick a circle each time the last bar is exactly two beats.', ticks())}''', 9, 46)
B5 = tp('Use', 'Rhythm', 'Rhythm', 'Swing: pairs of quavers written evenly, played long–short.', f'''
{ex(1, 'Swing', 1, 'Which line shows how swung quavers are played? Circle A or B, then play both and hear the difference.', '<div class="op3" style="grid-template-columns:1fr 1fr">' + ''.join(f'<div class="opc"><span class="ol">{l}</span>{wx(k, 60)}</div>' for l, k in (('A', 'wsw1'), ('B', 'wsw2'))) + '</div>')}
{ex(2, 'Clap and count', 2, 'Clap each line with a metronome while counting aloud. Tick a circle each day it is steady.', ''.join(f'<div class="cl2"><div class="clh"><span class="lv3">{l}</span>{ticks()}</div>{wx(k, 64)}</div>' for k, l in (('wl6', '6/8'), ('wl3', 'triplets and semiquavers'), ('wl4', 'syncopation'))))}
{ex(3, 'In your music', 1, 'Find each of these in a piece you are learning.', piece(['an upbeat (anacrusis)', 'a triplet', 'a syncopation', 'swing marked at the top']))}''', 10, 48)

# ---------- Review, progress, answers ----------
rsum = ''.join('<div class="sum">' + ' <span class="pl">+</span> '.join(gin('n', k, 32) for k in ks) + ' <span class="pl">=</span> ' + BOX + '</div>' for ks in (['dm', 'q', 'q'], ['dc', 'q', 'm']))
R = wpage(f'''<div class="kick">Time · Review</div><h1>Review</h1><p class="rem2"><span>Ten minutes</span>No help, no piano. Mark it with the answers on page 13.</p>
{ex(1, 'Name the notes', 1, 'Write the name of each note.', '<div class="nm4">' + ''.join(f'<div>{gcell("n", k, 40)}{LINE}</div>' for k in ('m', 'q', 'dc', 'sb')) + '</div>')}
{ex(2, 'How many beats?', 1, 'Crotchet = 1 beat.', f'<div class="sums">{rsum}</div>')}
{ex(3, 'Time signatures', 2, 'Write a time signature for each bar, then circle the compound ones.', grid([cell(k, 'time signature ' + BOX, 56) for k in ('wt3', 'wt5', 'wt6')], 3))}
{ex(4, 'Count it', 2, 'Write a count in every box.', wx('wrev', 74))}
{ex(5, 'True or false?', 2, 'Circle T or F.', ''.join(f'<div class="row">{t}<span class="tf">T &nbsp; F</span></div>' for t in ('A tie joins two notes of different pitches.', '6/8 has two beats in a bar.', 'In 4/4, a beam may cross the middle of the bar.')))}
<div class="score">Score <span class="ab"></span> / 20</div>''', 11, None)
concepts = ['pulse, tempo and strong beats', 'bar lines and repeat signs', 'note and rest values', 'dots and ties', 'simple time signatures', 'compound time (6/8)', 'grouping with beams', 'upbeats', 'triplets', 'syncopation and swing']
PR = wpage(f'''<div class="kick">Time · Progress</div><h1>My progress</h1><p class="rem2"><span>How to use</span>Tick each column when it is true. Come back to this page every few weeks.</p>
{tbl(['Concept', 'I know it', 'I can write it', 'I can play it', 'Handbook'], [[c, '<span class="cb2"></span>', '<span class="cb2"></span>', '<span class="cb2"></span>', f'p. {p}'] for c, p in zip(concepts, (48, 48, 50, 52, 54, 56, 58, 58, 58, 60))], ['40%', '15%', '15%', '15%', '15%'], 'prog')}
<div class="note2"><b>Teacher’s note</b><div class="lines"><span class="al"></span><span class="al"></span><span class="al"></span></div></div>''', 12, None)
ans = [('p. 1', 'Slow to fast: 60, 76, 92, 120. Strong beats on 1; in 4/4 medium on 3. Signs: bar line, double bar line, final bar line, repeat signs. Count: 1 2 3 · 1–2 3 · 1–2–3. How fast does it feel: any answer; slower to faster is usual.'),
       ('p. 2', 'Mistake: bar 3 has 4 beats.'),
       ('p. 3', 'Draw it: minim, quaver, dotted minim, semibreve. Table: crotchet 1, minim 2, quaver ½, dotted minim 3, semiquaver ¼. Pizza: minim = half note, 2 beats; crotchet = quarter note, 1 beat; quaver = eighth note, ½ beat.'),
       ('p. 4', 'Stems: up on the right below the middle line, down on the left above it, either on it. Rests: minim, crotchet, minim, crotchet.'),
       ('p. 5', 'Sums: 1½, 4, 6, 2, 2. Complete: crotchet, crotchet, crotchet, quaver, quaver, quaver.'),
       ('p. 6', 'Tie or dot: dotted minim, dotted crotchet, dotted semibreve. Mistake: bar 2 has 5 beats.'),
       ('p. 7', 'Time signatures: 3/4, 2/4, 6/8, 4/4, 5/4, 9/8. Compound: 6/8, 9/8, 12/8, 6/4 (beats 2, 3, 4, 2). Simple: 3/4 (3), 2/2 (2), 4/4 (4), 3/8 (3). 3/4: 3 crotchet beats; 6/8: 2 dotted-crotchet beats; C = 4/4, ¢ = 2/2.'),
       ('p. 8', 'Beams: 3/4 in three pairs; 6/8 in two groups of three.'),
       ('p. 9', 'Grouping: ✓ ✗ ✓ ✗. Triplet: 1 & a 2. Syncopation: 1 & & 1 2. Upbeat: 3 · 1 2 3 · 1–2; the last bar needs 2 beats.'),
       ('p. 10', 'Swing is played as B.'),
       ('p. 11', 'minim, quaver, dotted crotchet, semibreve · 4, 4 · 6/8, 5/4, 9/8 (compound: 6/8 and 9/8) · 1–2 & 3 · 1–2–3 · F, T, F.')]
AN = wpage(f'''<div class="kick">Time · Answers</div><h1>Answers</h1>
{tbl(['Page', 'Answers'], [[p, a] for p, a in ans], ['12%', '88%'], 'ansT')}
<p class="sm">Pages with “make your own”, “in your music” and clapping have no single answer: check them at the piano with your teacher, or with the online lessons.</p>''', 13, None)

css += f'''
.so{{color:#d9d4c6}} .el{{color:{GOLD if False else '#c9a24f'};font-size:13px;letter-spacing:1px}}
.rem2{{display:flex;gap:12px;align-items:baseline;font-size:14.5px;margin:-2px 0 4px;color:#3d4080}} .rem2 span{{flex:none;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:{C}}}
.op3{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-bottom:8px}} .opc{{position:relative}} .opc .vx{{margin:0;padding-left:30px}} .ol{{position:absolute;left:10px;top:50%;transform:translateY(-50%);font-weight:700;font-size:16px;color:{C};z-index:1}}
.sent p{{font-size:15px;margin:6px 0;display:flex;align-items:center;gap:8px;flex-wrap:wrap}} .al.inl{{display:inline-block;width:150px;height:20px}}
.mm4{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}} .mm4>div{{display:flex;flex-direction:column;align-items:center;gap:3px;padding:0 6px}} .mmk{{font-weight:700;font-size:15px}} .drw{{display:block;width:70px;height:70px}} .nm4{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}} .nm4>div{{text-align:center}}
.tf{{margin-left:auto;font-weight:700;letter-spacing:.1em;color:{MUTE}}} .row{{display:flex;align-items:center;gap:10px;font-size:15px;padding:5px 0;border-bottom:.6px solid #e2ddd0}}
.score{{margin-top:14px;text-align:right;font-weight:700;font-size:16px;display:flex;justify-content:flex-end;align-items:center;gap:8px}}
.prog td{{padding:9px 8px;font-size:15px}} .cb2{{display:inline-block;width:20px;height:20px;border:1.6px solid {N_}}}
.note2{{margin-top:20px}} .note2 b{{font-size:15px}} .lines .al{{height:34px}}
.fills>.fc{{display:flex;flex-direction:column}} .fills>.fc>.add{{margin-top:auto;justify-content:center;text-align:center;gap:6px}} .wl{{display:inline-block;width:64px;height:26px;border-bottom:1.6px solid #26296b}} .fills>.fc>figure.vx{{border:0;background:none;box-shadow:none;height:auto;flex:0 0 auto;padding:4px 0}} .fills>.fc>.add{{margin-top:6px !important}} .fills{{row-gap:18px}} .mm4+.mm4{{margin-top:0}} .ex2 .mm4 .ab{{height:24px}} .ex2>.tk,.ex2>.tk2{{justify-content:flex-end;margin-top:8px}} .pz{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:6px}} .pz>div{{display:flex;flex-direction:column;align-items:center;gap:6px}} .pzn{{display:flex;align-items:center;gap:6px;font-weight:700;font-size:14px}} .pzl{{display:flex;align-items:flex-end;gap:6px;font-size:13px;color:#6d6f9c;min-height:26px}} .fills{{align-items:stretch}} .fills>.fc>.add{{margin-top:auto !important}} .mm4 .drw{{width:96px;height:72px;border:1.4px dashed #b9bbd3;border-radius:6px}} .mm4.mm3{{grid-template-columns:repeat(3,1fr)}} .feel{{display:flex;align-items:center;gap:6px;font-weight:700}} .ansT td{{font-size:13.5px;line-height:1.45;padding:6px 8px;vertical-align:top}} .ansT td:first-child{{font-weight:700;color:{C}}}
'''
pages = [A1, B1, A2, B2, A3, B3, A4, B4, A5, B5, R, PR, AN]
open('/mnt/user-data/outputs/house-rooms/workbook-time2.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{"".join(pages)}</body></html>')
print('ok', len(pages))
