# The Piano Butler Workbook, Pitch: Learn and Use pages per topic (matching Handbook Part I), review, progress, answers
import json, sys, re
exec(open('/tmp/claude-0/pk/wbtime2.py').read())   # helpers + css from the Time workbook (rewrites its own html, harmless)
sys.path.insert(0, '/tmp/claude-0/pk')
from kb import keyboard
WP = json.load(open('/tmp/claude-0/pk/wp/wpout_c.json'))

def wpx(k, h=70):
    svg = WP[k].replace('<svg ', '<svg style="width:100%%;height:auto;max-height:%dpx" ' % h, 1)
    return '<figure class="vx px"><div class="vs">' + svg + '</div></figure>'
def pc(k, lab, h=70): return f'<div class="fc">{wpx(k, 70 if k.startswith(('ks', 'blank')) else 96)}<div class="add">{lab}</div></div>'
def wpage2(inner, n, hb):
    return f'''<section class="pg"><div class="top"><span>THE PIANO BUTLER WORKBOOK</span><span>PITCH · HANDBOOK P. {hb}</span></div><div class="rule"></div><div class="body">{inner}</div>
<div class="sign"><span>Date <i></i></span><span>Practised <i class="s"></i> times</span><span>Checked <i></i></span></div><div class="foot"><span>{n}</span></div></section>'''
def tq(kind, topic, title, rule, inner, n, hb):
    return wpage2(f'<div class="kick">Pitch · {topic} · {kind}</div><h1>{title}</h1><p class="rem2"><span>Remember</span>{rule}</p>{inner}', n, hb)
def kbd(start, n, W, H, extra_h=0, **kw):
    s = keyboard(start, n, W, H, **kw)
    if extra_h:   # room under the keys for numbers drawn in marks
        m = re.search(r'viewBox="(-?\d+) (-?\d+) ([\d.]+) ([\d.]+)" style="([^"]*)height:(\d+)px', s)
        vh = float(m.group(4)) + extra_h; ph = round(int(m.group(6)) * vh / float(m.group(4)))
        s = s.replace(m.group(0), f'viewBox="{m.group(1)} {m.group(2)} {m.group(3)} {vh:.0f}" style="{m.group(5)}height:{ph}px')
    return '<figure class="vx kbf">' + s + '</figure>'
def num(x, y, t, fill=C, col='#fff', r=8):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/><text x="{x}" y="{y + 3.6}" text-anchor="middle" font-family="AH,Arial" font-size="10.5" font-weight="700" fill="{col}">{t}</text>'
def anrow(labels): return '<div class="anrow">' + ''.join(f'<span><b>{l}</b>{BOX}</span>' for l in labels) + '</div>'
def tfrows(items): return ''.join(f'<div class="row">{t}<span class="tf">T &nbsp; F</span></div>' for t in items)
def circ(a, b): return f'{a} &nbsp;·&nbsp; {b}'

# ---------- 1 The keyboard (Handbook p. 22) ----------
KW, KH = 30, 110
k1 = kbd('C', 14, KW, KH, extra_h=26, marks=[num(i * KW + KW / 2, KH + 16, j + 1) for j, i in enumerate((1, 5, 7, 9, 11, 13))], scale=1.1)
A1 = tq('Learn', 'The keyboard', 'The keyboard', 'Left is lower, right is higher. C sits just left of every group of two black keys.', f'''
{ex(1, 'Twos and threes', 1, 'Circle every group of two black keys and every group of three. How many of each?', kbd('A', 21, 22, 88, scale=1.1) + f'<div class="add">groups of two {BOX} &nbsp; groups of three {BOX}</div>')}
{ex(2, 'Name the keys', 1, 'Write the letter name of each numbered key.', k1 + anrow('123456'))}
{ex(3, 'The musical alphabet', 1, 'Write the next three letters: going up the keyboard on the left, going down on the right. The first is done.', tbl(['Going up', 'Going down'], [['E F G <b class="done2">A B C</b>', 'C B A <b class="done2">G F E</b>'], ['F G A ' + LINE, 'G F E ' + LINE], ['B C D ' + LINE, 'D C B ' + LINE]], ['50%', '50%']))}''', 1, 22)
B1 = tq('Use', 'The keyboard', 'The keyboard', 'E–F and B–C have no black key between them: they are semitones.', f'''
{ex(1, 'Find them all', 1, 'Colour every C on this keyboard, then mark every F with a dot.', kbd('A', 21, 22, 88, scale=1.1) + f'<div class="add">Cs {BOX} &nbsp; Fs {BOX}</div>')}
{ex(2, 'Tone or semitone?', 2, 'Use the keyboard above. Circle T for a tone (two semitones) or S for a semitone (the very next key).', '<div class="ts6">' + ''.join(f'<div><b>{p}</b><span class="tf">T &nbsp; S</span></div>' for p in ('E – F', 'C – D', 'B – C', 'F – G', 'A – B', 'G – A')) + '</div>')}
{ex(3, 'Octaves', 1, 'Complete each sentence.', f'<div class="sent"><p>From one C to the next C there are {BOX} white keys, counting both.</p><p>From one C to the next C there are {BOX} semitones.</p><p>The C nearest the middle of the piano is called {LINE.replace("al", "al in")}.</p></div>')}
{ex(4, 'Play it', 1, 'Play every C from the bottom of the piano to the top, saying “low”, “middle” or “high” as you go. Then every F. Tick a circle each day.', ticks())}''', 2, 22)

# ---------- 2 Staff and reading the notes (Handbook pp. 23–24) ----------
A2 = tq('Learn', 'Reading the notes', 'The staff and the notes', 'Count lines and spaces from the bottom. Treble lines E G B D F, spaces F A C E; bass lines G B D F A, spaces A C E G.', f'''
{ex(1, 'The clefs', 1, 'Write the name of each clef and the note it marks.', tbl(['Clef', 'Name', 'It marks the line for'], [[gsym('𝄞', 46), LINE, LINE], [gsym('𝄢', 30), LINE, LINE]], ['16%', '42%', '42%']))}
{ex(2, 'Line or space?', 1, 'Circle line or space, then write its number (counted from the bottom).', grid([pc('t_' + n, circ('line', 'space') + ' ' + BOX, 58) for n in ('e4', 'a4', 'd5', 'c5', 'g4', 'f5')], 6))}
{ex(3, 'Treble clef notes', 1, 'Write the letter name under each note.', grid([pc('t_' + n, BOX, 58) for n in ('g4', 'e5', 'a4', 'c5', 'f4', 'd5', 'b4', 'e4')], 8))}
{ex(4, 'Bass clef notes', 2, 'Write the letter name under each note. Careful: the same place has a different name in the bass clef.', grid([pc('b_' + n, BOX, 58) for n in ('f3', 'a2', 'c3', 'g2', 'e3', 'b2', 'd3', 'a3')], 8))}''', 3, 23)
B2 = tq('Use', 'Reading the notes', 'The staff and the notes', 'A step goes from a line to the next space; a skip jumps line to line or space to space.', f'''
{ex(1, 'Note words', 2, 'Each group of notes spells a word. Write it underneath.', grid([pc('w_' + w, '<span class="ab wide"></span>', 66) for w in ('BAG', 'FACE', 'EGG', 'CAGE', 'BED', 'CAFE', 'BAD', 'CAGE_b')], 4))}
{ex(2, 'Ledger lines', 2, 'Name each note above or below the staff.', grid([pc(k, BOX, 66) for k in ('t_a5', 't_c4', 't_b3', 't_c6', 'b_c4', 'b_e2', 'b_b3', 'b_d4')], 8))}''', 4, 24)
C2 = tq('Practise', 'Reading the notes', 'The staff and the notes', 'Find a landmark note first (middle C, treble G, bass F), then step or skip from it.', f'''
{ex(1, 'Draw it', 2, 'Draw each note as a semibreve, in the one place on the staff where it fits.', grid([pc('blank_t', t, 58) for t in ('G on a line', 'C in a space', 'E on a line', 'F in a space')] + [pc('blank_b', t, 58) for t in ('A in a space', 'B on a line', 'G on a line', 'E in a space')], 4))}
{ex(2, 'Step or skip?', 1, 'Circle step or skip.', grid([pc(f'ss{i}', circ('step', 'skip'), 62) for i in range(6)], 6))}
{ex(3, 'Name-it race', 2, 'Time yourself naming all sixteen notes on page 3, out loud. Write your time each day and watch it fall.', '<div class="race">' + ''.join(f'<span><b>Day {d}</b>{BOX}<i>sec</i></span>' for d in range(1, 8)) + '</div>')}''', 5, 24)

# ---------- 3 Sharps, flats and naturals (Handbook p. 25) ----------
KB3 = 40
bk = [(0, 1), (1, 2), (3, 3), (4, 4), (5, 5)]
k3 = kbd('C', 7, KB3, 120, bdots=(), marks=[num((i + 1) * KB3, 120 * 0.6 - 12, t, fill='#fff', col=N_) for i, t in bk], scale=1.15)
A3 = tq('Learn', 'Sharps, flats and naturals', 'Sharps, flats and naturals', 'A sharp raises a note a semitone, a flat lowers it, a natural cancels either.', f'''
{ex(1, 'The signs', 1, 'Write the name of each sign and what it does.', tbl(['Sign', 'Name', 'What it does'], [[gsym('♯', 28), LINE, LINE], [gsym('♭', 28), LINE, LINE], [gsym('♮', 28), LINE, LINE]], ['14%', '30%', '56%']))}
{ex(2, 'Two names for each black key', 2, 'Give each numbered black key its sharp name and its flat name.', '<div class="two" style="grid-template-columns:1fr 1.1fr;align-items:center">' + k3 + tbl(['Key', 'Sharp name', 'Flat name'], [['1', '<b class="done2">C♯</b>', '<b class="done2">D♭</b>']] + [[str(i), LINE, LINE] for i in range(2, 6)], ['18%', '41%', '41%']) + '</div>')}
{ex(3, 'Name the notes', 1, 'Write the full name of each note, with its sharp or flat.', grid([pc(k, BOX, 58) for k in ('t_f#4', 't_bb4', 't_c#5', 't_eb4', 't_g#4', 't_ab4', 'b_f#3', 'b_bb2')], 8))}''', 6, 25)
B3 = tq('Use', 'Sharps, flats and naturals', 'Sharps, flats and naturals', 'An accidental lasts until the bar line; the next bar starts fresh.', f'''
{ex(1, 'How long does it last?', 2, 'Write the full name of each numbered note.', wpx('acc_bar', 80) + anrow('12345'))}
{ex(2, 'A semitone away', 2, 'Write the note a semitone higher and a semitone lower. Use the keyboard on page 6 if you need it.', tbl(['Note', 'A semitone higher', 'A semitone lower'], [['C', '<b class="done2">C♯</b>', '<b class="done2">B</b>']] + [[x, LINE, LINE] for x in ('E', 'F', 'B', 'G')], ['20%', '40%', '40%']))}
{ex(3, 'Same sound, new name', 2, 'Write another name for each note (an enharmonic).', '<div class="ts6">' + ''.join(f'<div><b>{x}</b> = {BOX}</div>' for x in ('C♯', 'E♭', 'G♭', 'A♯', 'E♯', 'C♭')) + '</div>')}
{ex(4, 'In your music', 1, 'Find each of these in a piece you are learning.', piece(['a sharp', 'a flat', 'a natural', 'an accidental cancelled by a bar line']))}''', 7, 25)

# ---------- 4 Intervals (Handbook p. 26) ----------
A4 = tq('Learn', 'Intervals', 'Tones, semitones and intervals', 'Count letter names, both ends included: C up to E is a 3rd (C D E).', f'''
{ex(1, 'Interval numbers', 1, 'Write the number of each interval (2nd, 3rd, 4th…).', grid([pc(f'iv{i}', BOX, 70) for i in range(8)], 8))}
{ex(2, 'Melodic or harmonic?', 1, 'Circle melodic (one after the other) or harmonic (together).', grid([pc(f'mh{i}', circ('melodic', 'harmonic'), 66) for i in range(4)], 4))}
{ex(3, 'Count the semitones', 2, 'Count every key from the first note to the second, black and white. The first is done.', '<div class="ts6">' + ''.join(f'<div><b>{a}</b> {BOX if not d else "<b class=done2>" + d + "</b>"} <span class="mu2">semitones</span></div>' for a, d in (('C up to E', '4'), ('C up to G', ''), ('E up to F', ''), ('D up to F', ''), ('C up to C', ''), ('F up to B', ''))) + '</div>')}''', 8, 26)
B4 = tq('Use', 'Intervals', 'Tones, semitones and intervals', 'A major 3rd is four semitones; a minor 3rd is three.', f'''
{ex(1, 'Draw the note above', 2, 'Draw a note the given interval above, then write its letter name.', grid([pc(f'up{i}', f'{t} {BOX}', 64) for i, t in enumerate(('a 3rd', 'a 5th', 'a 4th', 'an octave', 'a 2nd', 'a 6th'))], 6))}
{ex(2, 'Major or minor 3rd?', 3, 'Count the semitones, then circle major or minor.', grid([pc(f'th{i}', f'{BOX} &nbsp;{circ("M", "m")}', 66) for i in range(6)], 6))}
{ex(3, 'Higher, lower or the same?', 1, 'Someone plays two notes, one after the other. Circle what the second does. Swap and play for them.', '<div class="ts6">' + ''.join(f'<div><b>{i}</b><span class="tf">higher · lower · same</span></div>' for i in range(1, 7)) + '</div>')}
{ex(4, 'In your music', 1, 'Find each of these in a piece you are learning.', piece(['a harmonic 3rd', 'a melodic 5th', 'an octave', 'five notes moving by step']))}''', 9, 26)

# ---------- 5 Scales and keys (Handbook pp. 27–28) ----------
A5 = tq('Learn', 'Scales and keys', 'Scales and keys', 'Every major scale has the same pattern: T T S T T T S.', f'''
{ex(1, 'Fix the scale', 2, 'This should be G major, but one note is missing its sharp. Add it, then answer.', wpx('g_noacc', 92) + f'<div class="add">the note that needs a sharp {BOX} &nbsp; semitones between degrees {BOX} – {BOX} and {BOX} – {BOX}</div>')}
{ex(2, 'The major pattern', 1, 'Write T or S between each pair of degrees.', '<div class="tsp">' + ''.join(f'<span class="dg">{i}</span>' + (f'<span class="ab{" dn" if i < 3 else ""}">{"T" if i < 3 else ""}</span>' if i < 8 else '') for i in range(1, 9)) + '</div>')}
{ex(3, 'Degree names', 1, 'Write the name of each degree.', tbl(['Degree', 'Name', 'Degree', 'Name'], [['1', '<b class="done2">tonic</b>', '2', LINE], ['5', LINE, '3', LINE], ['4', LINE, '6', LINE], ['7', LINE, '', '']], ['12%', '38%', '12%', '38%']))}
{ex(4, 'Relative minor', 2, 'Each major key shares its key signature with a minor key, three semitones lower.', '<div class="ts6">' + ''.join(f'<div><b>{a}</b> → {BOX if not d else "<b class=done2>" + d + "</b>"} <span class="mu2">minor</span></div>' for a, d in (('C major', 'A'), ('G major', ''), ('F major', ''), ('D major', ''), ('B♭ major', ''), ('E♭ major', ''))) + '</div>')}''', 10, 27)
B5 = tq('Use', 'Scales and keys', 'Scales and keys', 'The order of sharps: F C G D A E B. The order of flats is the same, backwards.', f'''
{ex(1, 'Name the key', 2, 'Write the major key and its relative minor for each key signature.', grid([pc('ks' + k, f'major {BOX} &nbsp; minor {BOX}', 56) for k in ('1s', '1f', '2s', '2f', '3s', '3f')], 3, 'ksg'))}
{ex(2, 'Which minor?', 3, 'Three forms of A minor, going up. Write natural, harmonic or melodic under each.', ''.join(f'<div class="opc mrow"><span class="ol">{l}</span>{wpx(k, 44)}<span class="al mf"></span></div>' for l, k in (('A', 'mf_a'), ('B', 'mf_b'), ('C', 'mf_c'))))}
{ex(3, 'In order', 1, 'Write the order of sharps and the order of flats.', '<div class="ord"><b>Sharps</b>' + BOX * 7 + '</div><div class="ord"><b>Flats</b>' + BOX * 7 + '</div>')}
{ex(4, 'Play it', 1, 'Play each scale one octave, hands separately. Tick a circle each day it is even and correct.', '<div class="ts6">' + ''.join(f'<div><b>{s}</b>{ticks(4)}</div>' for s in ('G major', 'F major', 'A harm. minor')) + '</div>')}''', 11, 28)

# ---------- Review, progress, answers ----------
R = wpage2(f'''<div class="kick">Pitch · Review</div><h1>Review</h1><p class="rem2"><span>Ten minutes</span>No help, no piano. Mark it with the answers on page 14.</p>
{ex(1, 'Name the notes', 1, 'Write the full name of each note.', grid([pc(k, BOX, 58) for k in ('r_t_e5', 'r_b_c3', 'r_t_f#4', 'r_b_g2')], 4))}
{ex(2, 'Intervals and keys', 2, 'Write the interval number for the first two; the major key for the last two.', grid([pc('r_iv0', 'interval ' + BOX, 66), pc('r_iv1', 'interval ' + BOX, 66), pc('r_ks0', 'major ' + BOX, 66), pc('r_ks1', 'major ' + BOX, 66)], 4))}
{ex(3, 'Complete it', 2, 'One word or letter in each box.', f'<div class="sent"><p>A semitone higher than E is {BOX} .</p><p>From C to the next C there are {BOX} white keys, counting both.</p><p>A natural sign {LINE.replace("al", "al in")} a sharp or flat.</p><p>The relative minor of G major is {BOX} minor.</p></div>')}
{ex(4, 'True or false?', 1, 'Circle T or F.', tfrows(('E to F is a tone.', 'A key signature applies to every line of the piece.', 'An accidental lasts until the end of the bar.')))}
<div class="score">Score <span class="ab"></span> / 15</div>''', 12, 22)
concepts = [('the keyboard and the musical alphabet', 22), ('tones and semitones', 26), ('the staff and the clefs', 23), ('treble clef notes', 24), ('bass clef notes', 24), ('ledger lines', 23), ('sharps, flats and naturals', 25), ('enharmonic names', 25), ('interval numbers', 26), ('major and minor 3rds', 26), ('major scales', 27), ('minor scales', 27), ('key signatures', 28)]
PR = wpage2(f'''<div class="kick">Pitch · Progress</div><h1>My progress</h1><p class="rem2"><span>How to use</span>Tick each column when it is true. Come back to this page every few weeks.</p>
{tbl(['Concept', 'I know it', 'I can write it', 'I can play it', 'Handbook'], [[c, '<span class="cb2"></span>', '<span class="cb2"></span>', '<span class="cb2"></span>', f'p. {p}'] for c, p in concepts], ['40%', '15%', '15%', '15%', '15%'], 'prog')}
<div class="note2"><b>Teacher’s note</b><div class="lines"><span class="al"></span><span class="al"></span><span class="al"></span></div></div>''', 13, 22)
ans = [('p. 1', 'Groups (A to G, three octaves): twos 3, threes 2 (the last group of three is cut off at the right). Keys: 1 D, 2 A, 3 C, 4 E, 5 G, 6 B. Alphabet: B C D · D C B · E F G · A G F.'),
       ('p. 2', 'Cs 3, Fs 3. T/S: S, T, S, T, T, T. Octave: 8 white keys, 12 semitones, middle C.'),
       ('p. 3', 'Clefs: treble (G clef), line 2 = G; bass (F clef), line 4 = F. Line or space: line 1, space 2, line 4, space 3, line 2, line 5. Treble: G E A C F D B E. Bass: F A C G E B D A.'),
       ('p. 4', 'Words: BAG, FACE, EGG, CAGE, BED, CAFE, BAD, CAGE. Ledger lines: A, C, B, C · C, E, B, D.'), ('p. 5', 'Draw it: treble G line 2, C space 3, E line 1, F space 1; bass A space 1, B line 2, G line 1, E space 3. Step or skip: step, skip, step, skip, skip, step.'),
       ('p. 6', 'Signs: sharp, raises a semitone; flat, lowers a semitone; natural, cancels a sharp or flat. Black keys: 2 D♯/E♭, 3 F♯/G♭, 4 G♯/A♭, 5 A♯/B♭. Notes: F♯, B♭, C♯, E♭, G♯, A♭, F♯, B♭.'),
       ('p. 7', 'Bar: 1 F♯, 2 G, 3 F♯, 4 F (natural), 5 F. Semitone higher / lower: E: F / E♭ · F: F♯ / E · B: C / B♭ · G: G♯ / G♭ · D: D♯ / D♭ (enharmonic names also correct). Enharmonics: D♭, D♯, F♯, B♭, F, B.'),
       ('p. 8', 'Numbers: 3rd, 5th, 2nd, 6th, 4th, octave, 7th, 3rd. Melodic, harmonic, harmonic, melodic. Semitones: 7, 1, 3, 12, 6.'),
       ('p. 9', 'Note above: E, A, B (or B♭), E, A, F. 3rds: 4 M, 3 m, 3 m, 4 M, 4 M, 3 m.'),
       ('p. 10', 'F needs a sharp (F♯); semitones 3–4 and 7–8. Pattern: T T S T T T S. Degrees: 2 supertonic, 3 mediant, 4 subdominant, 5 dominant, 6 submediant, 7 leading note. Relative minors: E, D, B, G, C.'),
       ('p. 11', 'Keys: G / E minor · F / D minor · D / B minor · B♭ / G minor · A / F♯ minor · E♭ / C minor. Minor forms: A harmonic, B natural, C melodic. Sharps F C G D A E B; flats B E A D G C F.'),
       ('p. 12', 'E, C, F♯, G · 5th, 3rd, D major, F major · F, 8, cancels, E · F, T, T.')]
AN = wpage2(f'''<div class="kick">Pitch · Answers</div><h1>Answers</h1>
{tbl(['Page', 'Answers'], [[p, a] for p, a in ans], ['12%', '88%'], 'ansT')}
<p class="sm">“Draw it”, “in your music”, listening and playing have no single answer to copy: check them at the piano with your teacher, or with the online lessons.</p>''', 14, 22)

css += f'''
.anrow{{display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-top:6px}} .anrow span{{display:flex;align-items:center;gap:6px;font-size:14px}} .anrow b{{color:{C}}}
.ts6{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px 20px}} .ts6>div{{display:flex;align-items:center;gap:8px;font-size:15px;padding:5px 0;border-bottom:.6px solid #e2ddd0}} .ts6 .tf{{margin-left:auto}}
.fc .px{{margin:0;padding:4px 3px;height:auto;min-height:0}} .fc .px .vs{{width:100%;display:flex;justify-content:center}} .fills{{gap:8px}} .fc .add{{text-align:center}} .ab.wide{{width:86px}} .ksg .add{{line-height:2}}
.tsp{{display:flex;align-items:center;justify-content:center;gap:6px}} .dg{{font-weight:700;font-size:17px;width:22px;text-align:center}} .tsp .ab{{width:30px;height:28px;display:inline-flex;align-items:center;justify-content:center;font-weight:700}} .tsp .dn{{color:{C}}}
.mrow{{display:grid;grid-template-columns:1fr 200px;align-items:center;gap:14px;margin-bottom:6px}} .mrow .vx{{padding-left:30px}} .al.mf{{height:24px}}
.ord{{display:flex;align-items:center;gap:8px;margin:6px 0}} .ord b{{width:64px}}
.row .tk{{margin-left:auto}} .ts6 .tk{{margin-left:auto}} .ts6 b{{white-space:nowrap}}
.px .vs svg{{width:100%;height:auto}} .px text{{font-family:'AH',Arial !important;fill:#26296b !important;font-weight:700}} .kbf{{display:flex;justify-content:center}}
.race{{display:grid;grid-template-columns:repeat(7,1fr);gap:8px}} .race span{{display:flex;flex-direction:column;align-items:center;gap:6px;border:1px solid #e2ddd0;background:#fff;padding:10px 4px}} .race i{{font-style:normal;font-size:12px;color:{MUTE}}}
'''
pages = [A1, B1, A2, B2, C2, A3, B3, A4, B4, A5, B5, R, PR, AN]
open('/mnt/user-data/outputs/house-rooms/workbook-pitch.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{"".join(pages)}</body></html>')
print('ok', len(pages))
