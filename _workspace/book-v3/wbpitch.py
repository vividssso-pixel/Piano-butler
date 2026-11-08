# The Piano Butler Workbook, Pitch: Learn and Use pages per topic (matching Handbook Part I), review, progress, answers
import json, sys, re
exec(open('/tmp/claude-0/pk/wbtime2.py').read())   # helpers + css from the Time workbook (rewrites its own html, harmless)
sys.path.insert(0, '/tmp/claude-0/pk')
from kb import keyboard
WP = json.load(open('/tmp/claude-0/pk/wp/wpout_v.json'))

def wpx(k, h=70, spx=None):
    s = WP[k]
    m = re.search(r'data-sh="([\d.]+)"', s); vb = re.search(r'viewBox="[-\d.]+ [-\d.]+ ([\d.]+) ([\d.]+)"', s)
    if spx and m and float(m.group(1)) > 0:   # every staff in a grid drawn at the same size: staff height = spx pixels
        H = float(vb.group(2)) / float(m.group(1)) * spx
        svg = s.replace('<svg ', '<svg data-spx="%d" style="height:%dpx;width:auto;max-width:100%%" ' % (spx, round(H)), 1)
    else:
        svg = s.replace('<svg ', '<svg style="width:100%%;height:auto;max-height:%dpx" ' % h, 1)
    return '<figure class="vx px"><div class="vs">' + svg + '</div></figure>'
def pc(k, lab, h=70): return f'<div class="fc">{wpx(k, 84, 26)}<div class="add">{lab.replace(BOX, WL)}</div></div>'
def _hbl(hb):   # her 5 Nov (A): topics 1-5 are Part I Pitch (pp. 22-31), 6-12 Part III Scales and keys (pp. 50-63)
    return ('PITCH · HANDBOOK P. ' + str(22 + 2 * (hb - 22))) if hb < 27 else ('PITCH · HANDBOOK P. ' + str(50 + 2 * (hb - 27))) if hb < 29 else ('SCALES AND KEYS · HANDBOOK P. ' + str(50 + 2 * (hb - 27)))
def wpage2(inner, n, hb, lab='PITCH'):
    return f'''<section class="pg"{' data-end="1"' if not hb else ''}><div class="top"><span>THE PIANO BUTLER WORKBOOK</span><span>{_hbl(hb) if hb else lab}</span></div><div class="rule"></div><div class="body">{inner}</div>
<div class="sign"><span style="flex:0 0 240px">Date <i></i></span></div><div class="foot"><span>{n}</span></div></section>'''
def tq(kind, topic, title, rule, inner, n, hb):
    return wpage2(f'<div class="kick">{"Pitch" if hb < 29 else "Scales and keys"} · {topic} · {kind}</div><h1>{title}</h1><p class="rem2"><span>Remember</span>{rule}</p>{inner}', n, hb)
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
{ex(1, 'Find them all', 1, 'Colour every C on this keyboard and mark every F with a dot. How many of each?', kbd('A', 21, 22, 88, scale=1.1) + f'<div class="add">Cs {BOX} &nbsp; Fs {BOX}</div>')}
{ex(2, 'Tone or semitone?', 2, 'Use the keyboard above. Circle T for a tone (two semitones) or S for a semitone (the very next key).', '<div class="ts6">' + ''.join(f'<div><b>{p}</b><span class="tf">T &nbsp; S</span></div>' for p in ('E – F', 'C – D', 'B – C', 'F – G', 'A – B', 'G – A')) + '</div>')}
{ex(3, 'Octaves', 1, 'Complete each sentence.', f'<div class="sent"><p>From one C to the next C there are {BOX} white keys, counting both.</p><p>From one C to the next C there are {BOX} semitones.</p><p>The C nearest the middle of the piano is called {LINE.replace("al", "al inl")}.</p></div>')}
{ex(4, 'Up or down', 2, 'Start on the first key, move as asked, and write the key you land on.', '<div class="ts6">' + ''.join(f'<div><b>{x}</b> {BOX}</div>' for x in ('E up a semitone', 'F down a semitone', 'B up a semitone', 'C down a semitone', 'D up a tone', 'A down a tone')) + '</div>')}
{ex(5, 'Play it', 1, 'Play every C from the bottom of the piano to the top, saying “low”, “middle” or “high” as you go. Then every F. Tick a circle each day.', ticks())}''', 2, 22)

# ---------- 2 Staff and reading the notes (Handbook pp. 23–24) ----------
A2 = tq('Learn', 'Reading the notes', 'The staff and the notes', 'Count lines and spaces from the bottom. Treble lines E G B D F, spaces F A C E; bass lines G B D F A, spaces A C E G.', f'''
{ex(1, 'The clefs', 1, 'Write the name of each clef and the note it marks.', tbl(['Clef', 'Name', 'It marks the line for'], [[gsym('𝄞', 46), LINE, LINE], [gsym('𝄢', 30), LINE, LINE]], ['16%', '42%', '42%']))}
{ex(2, 'Line or space?', 1, 'Circle line or space, then write its number (counted from the bottom).', grid([pc('t_' + n, circ('line', 'space') + ' ' + BOX, 58) for n in ('e4', 'a4', 'd5', 'c5', 'g4', 'f5')], 3))}
{ex(3, 'The letters on the staff', 1, 'Write the letters from the bottom up. The first row is done.', '<div class="ord"><b>Treble lines</b>' + ''.join(f'<b class="done2" style="width:30px;text-align:center">{x}</b>' for x in 'EGBDF') + '</div>' + ''.join(f'<div class="ord"><b>{lab}</b>' + BOX * n + '</div>' for lab, n in (('Treble spaces', 4), ('Bass lines', 5), ('Bass spaces', 4))))}''', 3, 23)
B2 = tq('Use', 'Reading the notes', 'The staff and the notes', 'A step goes from a line to the next space; a skip jumps line to line or space to space.', f'''
{ex(1, 'Note words', 2, 'Each group of notes spells a word. Write it underneath.', grid([pc('w_' + w, WL, 66) for w in ('BAG', 'FACE', 'EGG', 'CAGE', 'BED', 'CAFE', 'BAD', 'CAGE_b')], 2))}
{ex(2, 'Step or skip?', 1, 'Circle step or skip.', grid([pc(f'ss{i}', circ('step', 'skip'), 62) for i in range(6)], 3))}''', 4, 24)
C2 = tq('Practise', 'Reading the notes', 'The staff and the notes', 'Find a landmark note first (middle C, treble G, bass F), then step or skip from it.', f'''
{ex(1, 'Treble clef notes', 1, 'Write the letter name under each note.', grid([pc('t_' + n, BOX, 58) for n in ('g4', 'e5', 'a4', 'c5', 'f4', 'd5', 'b4', 'e4')], 4))}
{ex(2, 'Bass clef notes', 2, 'Write the letter name under each note. Careful: the same place has a different name in the bass clef.', grid([pc('b_' + n, BOX, 58) for n in ('f3', 'a2', 'c3', 'g2', 'e3', 'b2', 'd3', 'a3')], 4))}
{ex(3, 'Same place, two names', 2, 'The same line or space has a different name in each clef. Write both. The first is done.', tbl(['Place', 'Treble clef', 'Bass clef'], [['line 1', '<b class="done2">E</b>', '<b class="done2">G</b>'], ['space 2', BOX, BOX], ['line 5', BOX, BOX]], ['30%', '35%', '35%']))}''', 5, 24)
D2 = tq('Practise', 'Reading the notes', 'The staff and the notes', 'Every note has one place: a line or a space. Draw it right in the middle of its line or space.', f'''
{ex(1, 'Ledger lines', 2, 'Name each note above or below the staff.', grid([pc(k, BOX, 66) for k in ('t_a5', 't_c4', 't_b3', 't_c6', 'b_c4', 'b_e2', 'b_b3', 'b_d4')], 4))}
{ex(2, 'Draw it', 2, 'Draw each note as a semibreve, in the one place on the staff where it fits.', grid([pc('blank_t', t, 58) for t in ('G on a line', 'C in a space', 'E on a line', 'F in a space')] + [pc('blank_b', t, 58) for t in ('A in a space', 'B on a line', 'G on a line', 'E in a space')], 4))}
{ex(3, 'Name-it race', 2, 'Time yourself naming the eight treble and eight bass notes on page 5, out loud. Write your time each day and watch it fall.', '<div class="race">' + ''.join(f'<span><b>Day {d}</b>{BOX}<i>sec</i></span>' for d in range(1, 8)) + '</div>')}''', 6, 23)

# ---------- 3 Sharps, flats and naturals (Handbook p. 25) ----------
KB3 = 40
bk = [(0, 1), (1, 2), (3, 3), (4, 4), (5, 5)]
k3 = kbd('C', 7, KB3, 120, bdots=(), marks=[num((i + 1) * KB3, 120 * 0.6 - 12, t, fill='#fff', col=N_) for i, t in bk], scale=1.15)
A3 = tq('Learn', 'Sharps, flats and naturals', 'Sharps, flats and naturals', 'A sharp raises a note a semitone, a flat lowers it, a natural cancels either.', f'''
{ex(1, 'The signs', 1, 'Write the name of each sign and what it does.', tbl(['Sign', 'Name', 'What it does'], [[gsym('♯', 28), LINE, LINE], [gsym('♭', 28), LINE, LINE], [gsym('♮', 28), LINE, LINE]], ['14%', '30%', '56%']))}
{ex(2, 'Two names for each black key', 2, 'Give each numbered black key its sharp name and its flat name.', '<div class="two" style="grid-template-columns:1fr 1.1fr;align-items:center">' + k3 + tbl(['Key', 'Sharp name', 'Flat name'], [['1', '<b class="done2">C♯</b>', '<b class="done2">D♭</b>']] + [[str(i), LINE, LINE] for i in range(2, 6)], ['18%', '41%', '41%']) + '</div>')}
{ex(3, 'Name the notes', 1, 'Write the full name of each note, with its sharp or flat.', grid([pc(k, BOX, 58) for k in ('t_f#4', 't_bb4', 't_c#5', 't_eb4', 't_g#4', 't_ab4', 'b_f#3', 'b_bb2')], 4))}''', 7, 26)
B3 = tq('Use', 'Sharps, flats and naturals', 'Sharps, flats and naturals', 'An accidental lasts until the bar line; the next bar starts fresh.', f'''
{ex(1, 'How long does it last?', 2, 'Write the full name of each numbered note.', wpx('acc_bar', 80) + anrow('12345'))}
{ex(2, 'A semitone away', 2, 'Write the note a semitone higher and a semitone lower. Use the keyboard on page 7 if you need it.', tbl(['Note', 'A semitone higher', 'A semitone lower'], [['C', '<b class="done2">C♯</b>', '<b class="done2">B</b>']] + [[x, LINE, LINE] for x in ('E', 'F', 'B', 'G')], ['20%', '40%', '40%']))}
{ex(3, 'Same sound, new name', 2, 'Write another name for each note (an enharmonic).', '<div class="ts6">' + ''.join(f'<div><b>{x}</b> = {BOX}</div>' for x in ('C♯', 'E♭', 'G♭', 'A♯', 'E♯', 'C♭')) + '</div>')}
{ex(4, 'In your music', 1, 'Find each of these in a piece you are learning.', piece(['a sharp', 'a flat', 'a natural', 'an accidental cancelled by a bar line']))}''', 8, 26)

# ---------- 4 Intervals (Handbook p. 26) ----------
A4 = tq('Learn', 'Intervals', 'Tones, semitones and intervals', 'Count letter names, both ends included: C up to E is a 3rd (C D E).', f'''
{ex(1, 'Interval numbers', 1, 'Write the number of each interval (2nd, 3rd, 4th…).', grid([pc(f'iv{i}', BOX, 70) for i in range(8)], 4))}
{ex(2, 'Melodic or harmonic?', 1, 'Circle melodic (one after the other) or harmonic (together).', grid([pc(f'mh{i}', circ('melodic', 'harmonic'), 66) for i in range(4)], 4))}
{ex(3, 'Count the semitones', 2, 'Count every key from the first note to the second, black and white. The first is done.', '<div class="ts6">' + ''.join(f'<div><b>{a}</b> {BOX if not d else "<b class=done2>" + d + "</b>"} <span class="mu2">semitones</span></div>' for a, d in (('C up to E', '4'), ('C up to G', ''), ('E up to F', ''), ('D up to F', ''), ('C up to C', ''), ('F up to B', ''))) + '</div>')}
{ex(4, 'Your hand measures it', 1, 'Thumb on C, one finger on each white key above it. Write the interval each finger makes with the thumb.', '<div class="ts6">' + ''.join(f'<div><b>finger {f}</b> {BOX}</div>' for f in (2, 3, 4, 5)) + '</div>')}''', 9, 27)
B4 = tq('Use', 'Intervals', 'Tones, semitones and intervals', 'A major 3rd is four semitones; a minor 3rd is three.', f'''
{ex(1, 'Draw the note above', 2, 'Draw a note the given interval above, then write its letter name.', grid([pc(f'up{i}', f'{t} {BOX}', 64) for i, t in enumerate(('a 3rd', 'a 5th', 'a 4th', 'an octave', 'a 2nd', 'a 6th'))], 3))}
{ex(2, 'Major or minor 3rd?', 3, 'Count the semitones, then circle major or minor.', grid([pc(f'th{i}', f'{BOX} &nbsp;{circ("M", "m")}', 66) for i in range(6)], 6))}
{ex(3, 'Higher, lower or the same?', 1, 'Someone plays two notes, one after the other. Circle what the second does. Swap and play for them.', '<div class="ts6">' + ''.join(f'<div><b>{i}</b><span class="tf">higher · lower · same</span></div>' for i in range(1, 7)) + '</div>')}
{ex(4, 'In your music', 1, 'Find each of these in a piece you are learning.', piece(['a harmonic 3rd', 'a melodic 5th', 'five notes moving by step']))}''', 10, 28)

# ---------- 5 Scales and keys (Handbook pp. 27–28) ----------
A5 = tq('Learn', 'Scales', 'Scales and keys', 'Every major scale has the same pattern: T T S T T T S.', f'''
{ex(1, 'Fix the scale', 2, 'This should be G major, but one note is missing its sharp. Add it, then answer.', wpx('g_noacc', 92) + f'<div class="add">the note that needs a sharp {BOX} &nbsp; semitones between degrees {BOX} – {BOX} and {BOX} – {BOX}</div>')}
{ex(2, 'The major pattern', 1, 'Write T or S between each pair of degrees.', '<div class="tsp">' + ''.join(f'<span class="dg">{i}</span>' + (f'<span class="ab{" dn" if i < 3 else ""}">{"T" if i < 3 else ""}</span>' if i < 8 else '') for i in range(1, 9)) + '</div>')}
{ex(3, 'Degree names', 1, 'Write the name of each degree.', tbl(['Degree', 'Name', 'Degree', 'Name'], [['1', '<b class="done2">tonic</b>', '2', LINE], ['5', LINE, '3', LINE], ['4', LINE, '6', LINE], ['7', LINE, '', '']], ['12%', '38%', '12%', '38%']))}
{ex(4, 'Relative minor', 2, 'Each major key shares its key signature with a minor key, three semitones lower.', '<div class="ts6">' + ''.join(f'<div><b>{a}</b> → {BOX if not d else "<b class=done2>" + d + "</b>"} <span class="mu2">minor</span></div>' for a, d in (('C major', 'A'), ('G major', ''), ('F major', ''), ('D major', ''), ('B♭ major', ''), ('E♭ major', ''))) + '</div>')}''', 11, 29)
B5 = tq('Use', 'Scales', 'Scales and keys', 'The order of sharps: F C G D A E B. The order of flats is the same, backwards.', f'''
{ex(1, 'Name the key', 2, 'Write the major key and its relative minor for each key signature.', grid([pc('ks' + k, f'major {BOX} &nbsp; minor {BOX}', 56) for k in ('1s', '1f', '2s', '2f', '3s', '3f')], 3, 'ksg'))}
{ex(2, 'Which minor?', 3, 'Three forms of A minor, going up. Write natural, harmonic or melodic under each.', ''.join(f'<div class="opc mrow"><span class="ol">{l}</span>{wpx(k, 64)}<span class="al mf"></span></div>' for l, k in (('A', 'mf_a'), ('B', 'mf_b'), ('C', 'mf_c'))))}
{ex(3, 'In order', 1, 'Write the order of sharps and the order of flats.', '<div class="ord"><b>Sharps</b>' + BOX * 7 + '</div><div class="ord"><b>Flats</b>' + BOX * 7 + '</div>')}
{ex(4, 'Play it', 1, 'Play each scale one octave, hands separately. Tick a circle each day it is even and correct.', '<div class="ts6">' + ''.join(f'<div><b>{s}</b>{ticks(4)}</div>' for s in ('G major', 'F major', 'A harmonic minor')) + '</div>')}''', 12, 31)

# ---------- Review, progress, answers (her 5 Nov: one set for Pitch, one for Scales and keys) ----------
R = wpage2(f'''<div class="kick">Pitch · Review</div><h1>Review</h1><p class="rem2"><span>Ten minutes</span>No help, no piano. Mark it with the answers on page 13.</p>
{ex(1, 'Name the notes', 1, 'Write the full name of each note.', grid([pc(k, BOX, 58) for k in ('r_t_e5', 'r_b_c3', 'r_t_f#4', 'r_b_g2')], 4))}
{ex(2, 'Complete it', 2, 'One word or letter in each space.', f'<div class="sent"><p>A semitone higher than E is {BOX} .</p><p>From C to the next C there are {BOX} white keys, counting both.</p><p>A natural sign {LINE.replace("al", "al inl")} a sharp or flat.</p></div>')}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('E to F is a tone.', 'An accidental lasts until the end of the bar.', 'A flat lowers a note by a semitone.')))}
<div class="score">Score <span class="ab"></span> / 10</div>''', 11, None)
concepts = [('the keyboard and the musical alphabet', 22), ('tones and semitones', 22), ('the staff and the clefs', 24), ('treble clef notes', 26), ('bass clef notes', 26), ('ledger lines', 26), ('the staff and the keyboard', 28), ('sharps, flats and naturals', 30), ('enharmonic names', 30), ('interval numbers', 50), ('major, minor and perfect intervals', 52)]
PR = wpage2(f'''<div class="kick">Pitch · Progress</div><h1>My progress</h1><p class="rem2"><span>How to use</span>Tick each column when it is true. Come back to this page every few weeks.</p>
{tbl(['Concept', 'I know it', 'I can write it', 'I can play it', 'Handbook'], [[c, '<span class="cb2"></span>', '<span class="cb2"></span>', '<span class="cb2"></span>', f'p. {p}'] for c, p in concepts], ['36%', '15%', '17%', '17%', '15%'], 'prog')}
<div class="note2"><b>Teacher’s note</b><div class="lines"><span class="al"></span><span class="al"></span><span class="al"></span></div></div>''', 12, None)
ans = [('p. 1', 'Groups (A to G, three octaves): twos 3, threes 2 (count whole groups only: a single black key at each end is part of a cut-off group). Keys: 1 D, 2 A, 3 C, 4 E, 5 G, 6 B. Alphabet: B C D · D C B · E F G · A G F.'),
       ('p. 2', 'Cs 3, Fs 3. T/S: S, T, S, T, T, T. Octave: 8 white keys, 12 semitones, middle C. Up or down: F, E, C, B, E, G.'),
       ('p. 3', 'Clefs: treble (G clef), line 2 = G; bass (F clef), line 4 = F. Line or space: line 1, space 2, line 4, space 3, line 2, line 5. Letters: treble spaces F A C E; bass lines G B D F A; bass spaces A C E G.'),
       ('p. 4', 'Words: BAG, FACE, EGG, CAGE, BED, CAFE, BAD, CAGE. Step or skip: step, skip, step, skip, skip, step.'), ('p. 5', 'Treble: G E A C F D B E. Bass clef: F A C G E B D A. Two names: space 2 treble A, bass C; line 5 treble F, bass A.'),
       ('p. 6', 'Ledger lines: A, C, B, C · C, E, B, D. Draw it: treble G line 2, C space 3, E line 1, F space 1; bass A space 1, B line 2, G line 1, E space 3.'),
       ('p. 7', 'Signs: sharp, raises a semitone; flat, lowers a semitone; natural, cancels a sharp or flat. Black keys: 2 D♯/E♭, 3 F♯/G♭, 4 G♯/A♭, 5 A♯/B♭. Notes: F♯, B♭, C♯, E♭, G♯, A♭, F♯, B♭.'),
       ('p. 8', 'Bar: 1 F♯, 2 G, 3 F♯, 4 F (natural), 5 F. Semitone higher / lower: E: F / E♭ · F: F♯ / E · B: C / B♭ · G: G♯ / G♭ (enharmonic names also correct). Enharmonics: D♭, D♯, F♯, B♭, F, B.'),
       ('p. 9', 'Numbers: 3rd, 5th, 2nd, 6th, 4th, octave, 7th, 3rd. Melodic, harmonic, harmonic, melodic. Semitones: 4, 7, 1, 3, 12, 6. Hand: 2nd, 3rd, 4th, 5th.'),
       ('p. 10', 'Note above: E, A, B, E, A, F. 3rds: 4 M, 3 m, 3 m, 4 M, 4 M, 3 m.'),
       ('p. 11', 'E, C, F♯, G · F, 8, cancels · F, T, T.')]
AN = wpage2(f'''<div class="kick">Pitch · Answers</div><h1>Answers</h1>
{tbl(['Page', 'Answers'], [[p, a] for p, a in ans], ['12%', '88%'], 'ansT')}
<p class="sm">“Draw it”, “in your music”, listening and playing have no single answer to copy: check them at the piano with your teacher, or with the online lessons.</p>''', 13, None)
SL = 'SCALES AND KEYS'
R3 = wpage2(f'''<div class="kick">Scales and keys · Review</div><h1>Review</h1><p class="rem2"><span>Ten minutes</span>No help, no piano. Mark it with the answers on page 5.</p>
{ex(1, 'Intervals and keys', 2, 'Write the interval number for the first two; the major key for the last two.', grid([pc('r_iv0', 'interval ' + BOX, 66), pc('r_iv1', 'interval ' + BOX, 66), pc('r_ks0', 'major ' + BOX, 66), pc('r_ks1', 'major ' + BOX, 66)], 4, 'lab2'))}
{ex(2, 'Complete it', 2, 'One word, letter or number in each space.', f'<div class="sent"><p>The relative minor of G major is {BOX} minor.</p><p>In a major scale the semitones fall between degrees 3–4 and {BOX} .</p><p>The major key with one sharp is {BOX} major.</p></div>')}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('A key signature applies to every line of the piece.', 'C up to E is a 3rd.', 'A minor 3rd is four semitones.')))}
<div class="score">Score <span class="ab"></span> / 10</div>''', 3, None, SL)
concepts3 = [('major scales', 54), ('scale degree names', 54), ('minor scales', 56), ('key signatures', 58), ('finding the key', 60), ('the circle of fifths', 62)]
PR3 = wpage2(f'''<div class="kick">Scales and keys · Progress</div><h1>My progress</h1><p class="rem2"><span>How to use</span>Tick each column when it is true. Come back to this page every few weeks.</p>
{tbl(['Concept', 'I know it', 'I can write it', 'I can play it', 'Handbook'], [[c, '<span class="cb2"></span>', '<span class="cb2"></span>', '<span class="cb2"></span>', f'p. {p}'] for c, p in concepts3], ['36%', '15%', '17%', '17%', '15%'], 'prog')}
<div class="note2"><b>Teacher’s note</b><div class="lines"><span class="al"></span><span class="al"></span><span class="al"></span></div></div>''', 4, None, SL)
ans3 = [('p. 1', 'F needs a sharp (F♯); semitones 3–4 and 7–8. Pattern: T T S T T T S. Degrees: 2 supertonic, 3 mediant, 4 subdominant, 5 dominant, 6 submediant, 7 leading note. Relative minors: E, D, B, G, C.'),
       ('p. 2', 'Keys: G / E minor · F / D minor · D / B minor · B♭ / G minor · A / F♯ minor · E♭ / C minor. Minor forms: A harmonic, B natural, C melodic. Sharps F C G D A E B; flats B E A D G C F.'),
       ('p. 3', '5th, 3rd, D major, F major · E, 7–8, G · T, T, F.')]
AN3 = wpage2(f'''<div class="kick">Scales and keys · Answers</div><h1>Answers</h1>
{tbl(['Page', 'Answers'], [[p, a] for p, a in ans3], ['12%', '88%'], 'ansT')}
<p class="sm">“Draw it”, “in your music”, listening and playing have no single answer to copy: check them at the piano with your teacher, or with the online lessons.</p>''', 5, None, SL)

css += f'''
.anrow{{display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-top:6px}} .anrow span{{display:flex;align-items:center;gap:6px;font-size:14px}} .anrow b{{color:{C}}}
.ts6{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px 20px}} .ts6>div{{display:flex;align-items:center;gap:8px;font-size:15px;padding:5px 0;border-bottom:.6px solid #e2ddd0}} .ts6 .tf{{margin-left:auto}}
.fc .px{{margin:0;padding:4px 3px;height:auto;min-height:0}} .fc .px .vs{{width:100%;display:flex;justify-content:center}} .fills{{gap:8px}} .fc .add{{text-align:center}} .ab.wide{{width:86px}} .ksg .add{{line-height:2}}
.tsp{{display:flex;align-items:center;justify-content:center;gap:6px}} .dg{{font-weight:700;font-size:17px;width:22px;text-align:center}} .tsp .ab{{width:30px;height:28px;display:inline-flex;align-items:center;justify-content:center;font-weight:700}} .tsp .dn{{color:{C}}}
.mrow{{display:grid;grid-template-columns:1fr 150px;align-items:center;gap:14px;margin-bottom:6px}} .mrow .vx{{padding-left:4px}} .al.mf{{height:24px}}
.ord{{display:flex;align-items:center;gap:8px;margin:6px 0}} .ord b{{width:110px}}
.row .tk{{margin-left:auto}} .ts6 .tk{{margin-left:auto}} .ts6 b{{white-space:nowrap}}
.px .vs svg{{width:100%;height:auto}} .px text{{font-family:'AH',Arial !important;fill:#26296b !important;font-weight:700}} .kbf{{display:flex;justify-content:center}}
.race{{display:grid;grid-template-columns:repeat(7,1fr);gap:8px}} .race span{{display:flex;flex-direction:column;align-items:center;gap:2px;padding:2px}} .race .ab{{height:22px}} .race i{{font-style:normal;font-size:12px;color:{MUTE}}}
.fills>.fc{{display:flex;flex-direction:column}} .fills>.fc>.px{{flex:1;display:flex;align-items:center;justify-content:center}} .fills>.fc>.add{{margin-top:auto}}
.fills>.fc>.px{{flex:1;display:flex;align-items:center;justify-content:center;padding:2px 4px}} .fills>.fc>.add{{justify-content:center;text-align:center;gap:6px;flex-wrap:wrap}} .wl{{display:inline-block;width:64px;height:26px;border-bottom:1.6px solid #26296b}} .fills>.fc>.add .wl:only-child, .fills>.fc>.add:not(:has(.wl ~ .wl)) .wl.hasdone{{width:72%}} .lab2 .add .wl{{display:block;margin:2px auto 0}} .ab.wide{{display:none}}
.fills>.fc>figure.vx{{border:0;background:none;box-shadow:none;height:auto;flex:1 1 auto;padding:0;display:flex;align-items:center}} .fills>.fc>.add{{margin-top:auto !important;padding-top:2px}} .fills>.fc>figure .vs{{display:flex;align-items:center;justify-content:center;width:100%;height:100%}} .fills>.fc>figure svg{{display:block;margin:0 auto}} .fills{{row-gap:10px}}
'''
pages = [A1, B1, A2, B2, C2, D2, A3, B3, A4, B4, R, PR, AN]
import re as _re3
pages3 = [_re3.sub(r'<div class="foot"><span>\d+</span>', f'<div class="foot"><span>{k + 1}</span>', p) for k, p in enumerate([A5, B5])] + [R3, PR3, AN3]
FITJS = '''<script>
// Fit every exercise cell's staff to its drawn content (staff, clef, notes), with a small even margin, so it fills the cell, centred.
(async function(){ try { await document.fonts.ready; } catch (e) {}
  document.querySelectorAll('.fills .fc > figure svg:not(svg svg)').forEach(s => { try {
    const M = s.getScreenCTM().inverse(); let x0 = 1e9, y0 = 1e9, x1 = -1e9, y1 = -1e9;
    s.querySelectorAll('g.staff > path, g.clef use, g.note use, g.note path, g.chord use, g.ledgerLines path, g.keySig use, g.accid use, g.notehead use').forEach(e => { const r = e.getBoundingClientRect(); if (!r.width && !r.height) return;
      [[r.left, r.top], [r.right, r.bottom]].forEach(([x, y]) => { const q = new DOMPoint(x, y).matrixTransform(M); x0 = Math.min(x0, q.x); y0 = Math.min(y0, q.y); x1 = Math.max(x1, q.x); y1 = Math.max(y1, q.y); }); });
    if (x1 <= x0) return; const m = (y1 - y0) * 0.12;
    s.setAttribute('viewBox', [x0 - m, y0 - m, x1 - x0 + 2 * m, y1 - y0 + 2 * m].map(v => v.toFixed(1)).join(' '));
    s.setAttribute('overflow', 'hidden'); } catch (e) {} });
  document.body.dataset.fitted = '1'; })();
</script>'''
SIZEJS = '''<script>
// Every staff in one exercise grid drawn at the same size: as large as data-spx, but no wider than its cell (from each picture's own staff height, data-sh).
document.querySelectorAll('.fills').forEach(g => { const ss = [...g.querySelectorAll('svg[data-spx][data-sh]')].filter(s => +s.dataset.sh > 0); if (!ss.length) return;
  ss.forEach(s => { s.style.width = '10px'; s.style.height = '10px'; s.style.maxWidth = 'none'; });   // measure the free cell widths first
  const CW = new Map(ss.map(s => [s, s.closest('.fc').getBoundingClientRect().width - 8]));
  let want = Math.min(...ss.map(s => +s.dataset.spx));
  ss.forEach(s => { const vb = s.viewBox.baseVal; want = Math.min(want, CW.get(s) * s.dataset.sh / vb.width); });
  const set = (s, H) => { const vb = s.viewBox.baseVal; s.style.height = H.toFixed(1) + 'px'; s.style.width = (H * vb.width / vb.height).toFixed(1) + 'px'; s.style.maxWidth = 'none'; };
  const lines = s => { let a = 1e9, z = -1e9; s.querySelectorAll('g.staff > path').forEach(e => { const r = e.getBoundingClientRect(); a = Math.min(a, r.top); z = Math.max(z, r.bottom); }); return z - a; };
  ss.forEach(s => set(s, want * s.viewBox.baseVal.height / s.dataset.sh));
  ss.forEach(s => { const h = lines(s); if (h > 0) set(s, parseFloat(s.style.height) * want / h); });   // correct by the staff actually drawn
  const over = Math.max(...ss.map(s => parseFloat(s.style.width) / CW.get(s)));
  if (over > 1) ss.forEach(s => set(s, parseFloat(s.style.height) / over));
  g.dataset.staff = lines(ss[0]).toFixed(2);
});
// grids on the same page with the same number of columns share one staff size (the smaller), so treble and bass match
document.querySelectorAll('section.pg').forEach(pg => { const by = {}; pg.querySelectorAll('.fills[data-staff]').forEach(g => { const s0 = g.querySelector('svg[data-spx]'); const k = g.style.gridTemplateColumns + '|' + Math.round(s0.viewBox.baseVal.width / 10); (by[k] = by[k] || []).push(g); });
  Object.values(by).forEach(gs => { const m = Math.min(...gs.map(g => +g.dataset.staff)); gs.forEach(g => { const f = m / +g.dataset.staff; if (f < 0.999) g.querySelectorAll('svg[data-spx]').forEach(s => { const H = parseFloat(s.style.height) * f, vb = s.viewBox.baseVal; s.style.height = H.toFixed(1) + 'px'; s.style.width = (H * vb.width / vb.height).toFixed(1) + 'px'; }); }); }); });
// line up the staves in a grid: every staff starts at the same height and every picture takes the same room
document.querySelectorAll('.fills[data-staff]').forEach(g => { const ss = [...g.querySelectorAll('svg[data-spx]')]; const m = ss.map(s => { const R = s.getBoundingClientRect(); let a = 1e9, z = -1e9; s.querySelectorAll('g.staff > path').forEach(e => { const r = e.getBoundingClientRect(); a = Math.min(a, r.top); z = Math.max(z, r.bottom); }); return a < 1e9 ? [a - R.top, R.bottom - z] : null; });
  const T = Math.max(...m.filter(Boolean).map(x => x[0])), B = Math.max(...m.filter(Boolean).map(x => x[1]));
  ss.forEach((s, i) => { if (!m[i]) return; s.style.marginTop = (T - m[i][0]).toFixed(1) + 'px'; s.style.marginBottom = (B - m[i][1]).toFixed(1) + 'px'; s.closest('.vs').style.alignItems = 'flex-start'; }); });
</script>'''
import sys as _s; _s.path.insert(0, '/tmp/claude-0/pk'); import importlib, firstdone; importlib.reload(firstdone)
FIRST = {'Name the keys': [('fill', 'D')], 'Tone or semitone?': [('ring', 'S')], 'Up or down': [('fill', 'F')], 'Line or space?': [('both', [('ring', 'line'), ('fill', '1')])], 'Treble clef notes': [('fill', 'G')], 'Note words': [('fill', 'BAG')], 'Bass clef notes': [('fill', 'F')], 'Step or skip?': [('ring', 'step')], 'Ledger lines': [('fill', 'A')], 'Name the notes': [('fill', 'F♯')], 'Interval numbers': [('fill', '3rd')], 'Melodic or harmonic?': [('ring', 'melodic')], 'Draw the note above': [('fill', 'E')], 'Name the key': [('fill', 'G')]}
exec(open('/tmp/claude-0/pk/wbpitch7.py').read())   # her 8 Nov: the Pitch workbook rebuilt chapter by chapter to match Handbook Part I
open('/mnt/user-data/outputs/house-rooms/workbook-pitch.html', 'w').write(_LG(firstdone.apply(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{"".join(pages)}{SIZEJS}</body></html>', FIRST).replace('</style></head>', firstdone.CSS + '</style></head>', 1)))
open('/mnt/user-data/outputs/house-rooms/workbook-scales.html', 'w').write(_LG(firstdone.apply(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{"".join(pages3)}{SIZEJS}</body></html>', FIRST).replace('</style></head>', firstdone.CSS + '</style></head>', 1)))
print('ok', len(pages), len(pages3))
