# The Pitch workbook rebuilt to match Handbook Part I chapter by chapter (her 8 Nov: "the order that never needs redoing":
# handbook first, then the workbook to match it). Two pages per chapter (Learn, Use), then review, progress and answers.
# exec'd at the end of wbpitch.py, so it uses that file's helpers (ex, tbl, grid, pc, kbd, num, BOX, LINE, WL, ticks, piece, wpx).
def _wp7(inner, n, hb):
    right = 'PITCH · HANDBOOK P.\u2009' + PM.resolve('{{' + hb + '}}') if hb else 'PITCH'
    return f'''<section class="pg"{' data-end="1"' if not hb else ''}><div class="top"><span>THE PIANO BUTLER WORKBOOK</span><span>{right}</span></div><div class="rule"></div><div class="body">{inner}</div>
<div class="sign"><span style="flex:0 0 240px">Date <i></i></span></div><div class="foot"><span>{n}</span></div></section>'''
def tp(kind, topic, title, rule, inner, n, hb): return _wp7(f'<div class="kick">Pitch · {topic} · {kind}</div><h1>{title}</h1><p class="rem2"><span>Remember</span>{rule}</p>{inner}', n, hb)
def D7(x): return f'<b class="done2">{x}</b>'
def opt7(t, o): return f'<div class="row"><b>{t}</b><span class="tf">{" &nbsp;·&nbsp; ".join(o)}</span></div>'
def sent7(items): return '<div class="sent">' + ''.join(f'<p>{x}</p>' for x in items) + '</div>'
def ts(items, cols=3): return f'<div class="ts6" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(f'<div>{x}</div>' for x in items) + '</div>'
_WBH.pop('The staff and the keyboard', None); _WBH.update({'The keyboard': 'P1', 'The staff and the clefs': 'P2', 'Reading the notes': 'P4', 'Ledger lines': 'P5', 'Sharps, flats and naturals': 'P6', 'Counting intervals': 'P7', 'Major, minor and perfect': 'P8'})
WIDE = '<span class="al" style="display:inline-block;width:120px"></span>'

# ---------- 1 The keyboard ----------
Q1 = tp('Learn', 'The keyboard', 'The keyboard', 'Two black keys: start on C. Three black keys: start on F. Then walk on.', f'''
{ex(1, 'Twos and threes', 1, 'Circle every group of two black keys and every group of three. How many of each?', kbd('A', 21, 22, 88, scale=1.1) + f'<div class="add">groups of two {BOX} &nbsp; groups of three {BOX}</div>')}
{ex(2, 'Name the keys', 1, 'Find the group, then its first key, then walk on. Write the letter name of each numbered key.', k1 + anrow('123456'))}
{ex(3, 'Round and round', 1, 'Seven letters, A to G, then A again. Write the next three letters: going up on the left, going down on the right. The first is done.', tbl(['Going up', 'Going down'], [['E F G <b class="done2">A B C</b>', 'C B A <b class="done2">G F E</b>'], ['F G A ' + LINE, 'B A G ' + LINE], ['A B C ' + LINE, 'D C B ' + LINE]], ['50%', '50%']))}''', 1, 'P1')
Q2 = tp('Use', 'The keyboard', 'The keyboard', 'The eight Cs: Lowest C, Low C, Bass C, Middle C, Treble C, High C, Very High C, Highest C.', f'''
{ex(1, 'Find them all', 1, 'Colour every C on this keyboard and mark every F with a dot. How many of each?', kbd('A', 21, 22, 88, scale=1.1) + f'<div class="add">Cs {BOX} &nbsp; Fs {BOX}</div>')}
{ex(2, 'The eight Cs', 2, 'Write the names of the eight Cs, from the bottom of the piano to the top. The first is done.', tbl(['', 'Name', '', 'Name'], [['1', D7('Lowest C'), '5', LINE], ['2', LINE, '6', LINE], ['3', LINE, '7', LINE], ['4', LINE, '8', LINE]], ['8%', '42%', '8%', '42%']))}
{ex(3, 'The two ends', 2, 'Complete each sentence.', sent7([f'The first key at the bottom of the piano is {BOX} .', f'Its one black key is all that is left of a cut-off group of {BOX} black keys.', f'The last key at the top is {BOX} . It comes just after the last group of {BOX} black keys.', f'From one C to the next C there are {BOX} white keys, counting both: an octave.']))}
{ex(4, 'Play it', 1, 'Play every C from the bottom to the top, saying its name. Then every F. Tick a circle each day.', ticks())}''', 2, 'P1+1')

# ---------- 2 The staff and the clefs ----------
Q3 = tp('Learn', 'The staff and the clefs', 'The staff and the clefs', 'The treble clef curls round G, line 2. The bass clef’s two dots hug F, line 4.', f'''
{ex(1, 'The clefs', 1, 'Write the name of each clef and the note it marks.', tbl(['Clef', 'Name', 'It marks the line for'], [[gsym('𝄞', 46), LINE, LINE], [gsym('𝄢', 30), LINE, LINE]], ['16%', '42%', '42%']))}
{ex(2, 'Line or space?', 1, 'Circle line or space, then write its number (counted from the bottom).', grid([pc('t_' + n, circ('line', 'space') + ' ' + BOX, 58) for n in ('e4', 'a4', 'd5', 'c5', 'g4', 'f5')], 3))}
{ex(3, 'Treble or bass?', 1, 'Which staff would each note usually be written on?', ''.join(opt7(a, ('treble', 'bass')) for a in ('the E above Middle C', 'Bass C', 'High C', 'the lowest key on the piano', 'Treble C')))}''', 3, 'P2')
KW2, KH2 = 30, 110
k2 = kbd('C', 15, KW2, KH2, extra_h=24, shade={7: '#fbd0c2'}, marks=[num(i * KW2 + KW2 / 2, KH2 - 16, j + 1) for j, i in enumerate((2, 4, 5, 9, 11, 14))] + [f'<text x="{7 * KW2 + KW2 / 2}" y="{KH2 + 18}" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="{C}">Middle C</text>'], scale=1.1)
Q4 = tp('Use', 'The staff and the clefs', 'The staff and the clefs', 'Treble staff on top, usually the right hand; bass staff below, usually the left. Middle C sits between them.', f'''
{ex(1, 'Which staff?', 1, 'Middle C is marked. Is each numbered key written on the treble staff or the bass staff?', k2 + ts([f'<b>{i}</b><span class="tf">treble · bass</span>' for i in range(1, 7)]))}
{ex(2, 'The grand staff', 1, 'Complete each sentence.', sent7([f'Piano music joins two staves with a {WIDE} .', f'The {WIDE} staff is on top, usually for the {WIDE} hand.', f'The {WIDE} staff is below, usually for the {WIDE} hand.', f'Between them, on a short line of its own, sits {WIDE} .']))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('Middle C can be written in either staff.', 'The bass clef’s dots hug line 2.', 'Higher on the staff means higher on the keyboard.', 'Lines are counted from the top.')))}
{ex(4, 'Play it', 1, 'Point to the G line and play treble G. Point to the F line and play bass F. Then play Middle C, between them. Tick a circle each day.', ticks())}''', 4, 'P2+1')

# ---------- 3 Reading the notes ----------
Q5 = tp('Learn', 'Reading the notes', 'Reading the notes', 'Start from a note you know (treble G, bass F, Middle C), then step or skip.', f'''
{ex(1, 'The letters on the staff', 1, 'Write the letters from the bottom up. The first row is done.', '<div class="ord"><b>Treble lines</b>' + ''.join(f'<b class="done2" style="width:30px;text-align:center">{x}</b>' for x in 'EGBDF') + '</div>' + ''.join(f'<div class="ord"><b>{lab}</b>' + BOX * n + '</div>' for lab, n in (('Treble spaces', 4), ('Bass lines', 5), ('Bass spaces', 4))))}
{ex(2, 'Step or skip?', 1, 'Circle step or skip.', grid([pc(f'ss{i}', circ('step', 'skip'), 62) for i in range(6)], 3))}
{ex(3, 'Treble clef notes', 1, 'Write the letter name under each note. Start from G.', grid([pc('t_' + n, BOX, 58) for n in ('g4', 'e5', 'a4', 'c5', 'f4', 'd5', 'b4', 'e4')], 4))}''', 7, 'P4')
Q6 = tp('Use', 'Reading the notes', 'Reading the notes', 'In the bass the bottom line is G, not E: always read the clef first.', f'''
{ex(1, 'Bass clef notes', 2, 'Write the letter name under each note. Start from F.', grid([pc('b_' + n, BOX, 58) for n in ('f3', 'a2', 'c3', 'g2', 'e3', 'b2', 'd3', 'a3')], 4))}
{ex(2, 'Note words', 2, 'Each group of notes spells a word. Write it underneath.', grid([pc('w_' + w, WL, 66) for w in ('BAG', 'FACE', 'EGG', 'CAGE', 'BED', 'CAFE', 'BAD', 'CAGE_b')], 3))}
{ex(3, 'Name-it race', 2, 'Time yourself naming the treble notes on page 7 and the bass notes above, out loud. Write your time each day and watch it fall.', '<div class="race">' + ''.join(f'<span><b>Day {d}</b>{BOX}<i>sec</i></span>' for d in range(1, 8)) + '</div>')}''', 8, 'P4+1')

# ---------- 4 The staff and the keyboard ----------
KW4, KH4 = 30, 110
k4 = kbd('C', 15, KW4, KH4, extra_h=24, shade={7: '#fbd0c2'}, marks=[num(i * KW4 + KW4 / 2, KH4 - 16, j + 1) for j, i in enumerate((2, 4, 5, 9, 11, 14))] + [f'<text x="{7 * KW4 + KW4 / 2}" y="{KH4 + 18}" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="{C}">Middle C</text>'], scale=1.1)
Q7 = tp('Learn', 'The staff and the keyboard', 'The staff and the keyboard', 'Every line and every space is one white key, in order. One step on the staff is the very next white key.', f'''
{ex(1, 'Which key?', 1, 'Middle C is marked. Write the letter name of each numbered key.', k4 + anrow('123456'))}
{ex(2, 'Count from Middle C', 1, 'Count the notes, both ends included. The first is done.', tbl(['From', 'To', 'Notes'], [['Middle C', 'up to treble G', D7('5')], ['Middle C', 'down to bass F', BOX], ['Middle C', 'up to A', BOX], ['Middle C', 'down to E', BOX], ['G', 'up to the next G', BOX]], ['30%', '40%', '30%']))}
{ex(3, 'Mirror notes', 1, 'Complete each sentence.', sent7([f'Treble G and bass F are both note {BOX} from Middle C.', f'Treble G is on line {BOX} of the treble staff; bass F is on line {BOX} of the bass staff.']))}''', 5, 'P3')
Q8 = tp('Use', 'The staff and the keyboard', 'The staff and the keyboard', 'Middle C can be written in either staff: the hand that plays it chooses.', f'''
{ex(1, 'From the key to the page', 2, 'Count up from Middle C, then write the note’s name and its place on the staff. The first is done.', tbl(['Key', 'Name', 'Place on the treble staff'], [['the 2nd white key up from Middle C', D7('D'), D7('the space below the staff')], ['the 3rd white key up', BOX, LINE], ['the 5th white key up', BOX, LINE], ['the 8th white key up', BOX, LINE]], ['44%', '16%', '40%']))}
{ex(2, 'Draw it', 2, 'Draw each note as a semibreve, in the one place on the staff where it fits.', grid([pc('blank_t', t, 58) for t in ('G on a line', 'C in a space', 'E on a line', 'F in a space')] + [pc('blank_b', t, 58) for t in ('A in a space', 'B on a line', 'G on a line', 'E in a space')], 4))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('D sits in the space just below the treble staff.', 'Middle C sits on a ledger line of its own.', 'One step on the staff can skip a white key.')))}
{ex(4, 'Play it', 1, 'Play Middle C and walk up the white keys, saying each name and picturing it climbing the staff: line, space, line, space. Tick a circle each day.', ticks())}''', 6, 'P3+1')

QL = tp('Learn', 'Ledger lines', 'Ledger lines', 'Step out from the nearest staff line: line, space, line. The first ledger line is the one nearest the staff.', f'''
{ex(1, 'Ledger lines', 2, 'Name each note above or below the staff.', grid([pc(k, BOX, 66) for k in ('t_a5', 't_c4', 't_b3', 't_c6', 'b_c4', 'b_e2', 'b_b3', 'b_d4')], 4))}
{ex(2, 'Step out', 1, 'Start from the staff line given and write the next three notes going out. The first row is done.', tbl(['Start from', 'Going', 'Next three notes'], [['treble line 1, E', 'down', D7('D · Middle C · B')], ['treble line 5, F', 'up', LINE], ['bass line 1, G', 'down', LINE], ['bass line 5, A', 'up', LINE]], ['34%', '18%', '48%']))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('Ledger lines are spaced just like the staff lines.', 'The first ledger line is the one furthest from the staff.', '8va over the notes means play them an octave higher.', 'The first ledger line below the bass staff is Middle C.')))}''', 9, 'P5')
QL2 = tp('Use', 'Ledger lines', 'Ledger lines', 'Middle C has its own ledger line: below the treble staff, above the bass staff. One key, two ways.', f'''
{ex(1, 'The four first ledger lines', 1, 'Write the note on each first ledger line. The first is done.', tbl(['Where', 'Note'], [['treble, below the staff', D7('Middle C')], ['bass, above the staff', BOX], ['treble, above the staff', BOX], ['bass, below the staff', BOX]], ['60%', '40%']))}
{ex(2, 'Middle C, two ways', 1, 'Circle the right word.', ''.join(opt7(a, o) for a, o in (('In the treble staff, Middle C sits on the first ledger line…', ('below', 'above')), ('In the bass staff, Middle C sits on the first ledger line…', ('below', 'above')), ('Written in the treble and in the bass, Middle C is…', ('the same key', 'two keys')))))}
{ex(3, 'Same place, two names', 2, 'The same line or space has a different name in each clef. Write both. The first is done.', tbl(['Place', 'Treble clef', 'Bass clef'], [['line 1', '<b class="done2">E</b>', '<b class="done2">G</b>'], ['space 2', BOX, BOX], ['line 5', BOX, BOX], ['space 4', BOX, BOX]], ['30%', '35%', '35%']))}
{ex(4, 'Play it', 1, 'Play Middle C, then step down to Low C and up to High C, naming every ledger note. Tick a circle each day.', ticks())}''', 10, 'P5+1')

# ---------- 5 Sharps, flats and naturals ----------
Q9 = tp('Learn', 'Sharps, flats and naturals', 'Sharps, flats and naturals', 'Sharp: the very next key to the right, a semitone higher. Flat: the very next key to the left, a semitone lower. Natural: back to the white key.', f'''
{ex(1, 'The signs', 1, 'Write the name of each sign and what it does.', tbl(['Sign', 'Name', 'What it does'], [[gsym('♯', 28), LINE, LINE], [gsym('♭', 28), LINE, LINE], [gsym('♮', 28), LINE, LINE]], ['14%', '30%', '56%']))}
{ex(2, 'Two names for each black key', 2, 'Give each numbered black key its sharp name and its flat name.', '<div class="two" style="grid-template-columns:1fr 1.1fr;align-items:center">' + k3 + tbl(['Key', 'Sharp name', 'Flat name'], [['1', '<b class="done2">C♯</b>', '<b class="done2">D♭</b>']] + [[str(i), LINE, LINE] for i in range(2, 6)], ['18%', '41%', '41%']) + '</div>')}
{ex(3, 'Name the notes', 1, 'Write the full name of each note, with its sharp or flat.', grid([pc(k, BOX, 58) for k in ('t_f#4', 't_bb4', 't_c#5', 't_eb4', 't_g#4', 't_ab4', 'b_f#3', 'b_bb2')], 4))}''', 9, 'P6')
Q10 = tp('Use', 'Sharps, flats and naturals', 'Sharps, flats and naturals', 'A sign changes only its own line or space, in that octave, and only until the bar line.', f'''
{ex(1, 'How long does it last?', 2, 'Write the full name of each numbered note.', wpx('acc_bar', 80) + anrow('12345'))}
{ex(2, 'One key right, one key left', 2, 'Write the sharp (one key right) and the flat (one key left). Use the keyboard on page 11 if you need it. The first is done.', tbl(['Note', 'Its sharp is the key…', 'Its flat is the key…'], [['C', '<b class="done2">C♯ (black)</b>', '<b class="done2">C♭ = B (white)</b>']] + [[x, LINE, LINE] for x in ('E', 'F', 'G', 'B')], ['16%', '42%', '42%']))}
{ex(3, 'Same sound, new name', 2, 'Write another name for each note (an enharmonic).', ts([f'<b>{x}</b> = {BOX}' for x in ('C♯', 'E♭', 'G♭', 'A♯', 'E♯', 'C♭')]))}
{ex(4, 'In your music', 1, 'Find each of these in a piece you are learning.', piece(['a sharp', 'a flat', 'a natural', 'a sign wiped out by a bar line']))}''', 10, 'P6+1')

# ---------- 6 Counting intervals ----------
Q11 = tp('Learn', 'Counting intervals', 'Semitones and tones', 'A semitone is the very next key, black or white, with nothing between. Two semitones make a tone: one key between.', f'''
{ex(1, 'Tone or semitone?', 1, 'Circle T for a tone or S for a semitone. Look for a black key between.', '<div class="ts6">' + ''.join(f'<div><b>{p}</b><span class="tf">T &nbsp; S</span></div>' for p in ('E – F', 'C – D', 'B – C', 'F – G', 'A – B', 'G – A')) + '</div>')}
{ex(2, 'Up or down', 2, 'Start on the first key, move as asked, and write the key you land on.', ts([f'<b>{x}</b> {BOX}' for x in ('E up a semitone', 'F down a semitone', 'B up a semitone', 'C down a semitone', 'D up a tone', 'A down a tone')]))}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('E to F is a semitone.', 'C to D is a semitone.', 'Two semitones make a tone.', 'C to G♯ is still a 5th.')))}
{ex(4, 'Find them all', 1, 'On the keyboard, find every semitone with no black key between (two pairs in each octave). Write them.', '<div class="add">' + BOX + ' – ' + BOX + ' &nbsp; and &nbsp; ' + BOX + ' – ' + BOX + '</div>')}
{ex(5, 'Play it', 1, 'From every white key, play a semitone up, then a tone up. Say which keys are black. Tick a circle each day.', ticks())}''', 13, 'P7')
Q12 = tp('Use', 'Counting intervals', 'Counting intervals', 'Count the notes, both ends included: C D E is 3 notes, a 3rd. Sharps and flats never change the number.', f'''
{ex(1, 'Interval numbers', 1, 'Write the number of each interval (2nd, 3rd, 4th…).', grid([pc(f'iv{i}', BOX, 70) for i in range(8)], 4))}
{ex(2, 'Melodic or harmonic?', 1, 'Circle melodic (one after the other) or harmonic (together).', grid([pc(f'mh{i}', circ('melodic', 'harmonic'), 66) for i in range(4)], 4))}
{ex(3, 'Draw the note above', 2, 'Draw a note the given interval above, then write its letter name.', grid([pc(f'up{i}', f'{t} {BOX}', 64) for i, t in enumerate(('a 3rd', 'a 5th', 'a 4th', 'an 8ve', 'a 2nd', 'a 6th'))], 3))}''', 14, 'P7+1')

Q13 = tp('Learn', 'Major, minor and perfect', 'Major, minor and perfect', 'Count the keys in between, black and white, not the two you play: 3 make a major 3rd, 2 a minor 3rd.', f'''
{ex(1, 'Count the keys between', 1, 'Count every key between the two notes, black and white. The first is done.', ts([f'<b>{a}</b> {D7(d) if d else BOX} <span class="mu2">between</span>' for a, d in (('C up to E', '3'), ('C up to E♭', ''), ('F up to A', ''), ('D up to F', ''), ('C up to G', ''), ('E up to A', ''))]))}
{ex(2, 'Major or minor 3rd?', 3, 'Write how many keys are between on the line, then circle major (M) or minor (m).', grid([pc(f'th{i}', f'{BOX} &nbsp;{circ("M", "m")}', 66) for i in range(6)], 6))}
{ex(3, 'The sizes', 1, 'Complete the table: how many keys between?', tbl(['Interval', 'Keys between'], [['minor 3rd', D7('2')], ['major 3rd', BOX], ['perfect 4th', BOX], ['perfect 5th', BOX], ['minor 6th', BOX], ['major 6th', BOX], ['octave', BOX]], ['50%', '50%']))}''', 13, 'P8')
Q14 = tp('Use', 'Major, minor and perfect', 'Major, minor and perfect', '4ths, 5ths and octaves have one main size, called perfect. They are never major or minor.', f'''
{ex(1, 'Perfect, major or minor?', 2, 'Count the notes for the number, then the keys between for the size. The first is done.', tbl(['Going up', 'Number', 'Keys between', 'Name'], [['C up to G', D7('5th'), D7('6'), D7('perfect 5th')], ['D up to F', BOX, BOX, LINE], ['C up to E', BOX, BOX, LINE], ['E up to A', BOX, BOX, LINE], ['D up to A', BOX, BOX, LINE], ['E up to C', BOX, BOX, LINE]], ['20%', '20%', '22%', '38%']))}
{ex(2, 'Bright or dark?', 1, 'Someone plays a major or a minor 3rd. Circle what you hear: bright (major) or dark (minor). Swap and play for them.', '<div class="ts6">' + ''.join(f'<div><b>{i}</b><span class="tf">bright · dark</span></div>' for i in range(1, 7)) + '</div>')}
{ex(3, 'In your music', 1, 'Find each of these in a piece you are learning.', piece(['a harmonic 3rd', 'a melodic 5th', 'a minor 3rd']))}
{ex(4, 'Play it', 1, 'Play C–E, then C–E♭: bright, then dark. Then F–A, F–A♭ and G–B, G–B♭. Tick a circle each day.', ticks())}''', 14, 'P8+1')

# ---------- Review, progress, answers ----------
QR = _wp7(f'''<div class="kick">Pitch · Review</div><h1>Review</h1><p class="rem2"><span>Ten minutes</span>No help, no piano. Mark it with the answers on page 19.</p>
{ex(1, 'Name the notes', 1, 'Write the full name of each note.', grid([pc(k, BOX, 58) for k in ('r_t_e5', 'r_b_c3', 'r_t_f#4', 'r_b_g2')], 4))}
{ex(2, 'Complete it', 2, 'One word or letter in each space.', f'<div class="sent"><p>The very next key to the right of E is {BOX} .</p><p>From one C to the next C there are {BOX} white keys, counting both.</p><p>The last key at the top of the piano is called {WIDE} .</p></div>')}
{ex(3, 'True or false?', 1, 'Circle T or F.', tfrows(('E to F is a tone.', 'A sign lasts until the end of the bar.', 'C to E has 3 keys between: a major 3rd.')))}
<div class="score">Score <span class="ab"></span> / 10</div>''', 15, None)
qconcepts = [('the keyboard, the eight Cs', 'P1'), ('the staff, the clefs, the grand staff', 'P2'), ('the staff and the keyboard', 'P3'), ('reading the notes', 'P4'), ('ledger lines; Middle C two ways', 'P5'), ('sharps, flats and naturals', 'P6'), ('counting intervals; tones and semitones', 'P7'), ('major, minor and perfect', 'P8')]
QP = _wp7(f'''<div class="kick">Pitch · Progress</div><h1>My progress</h1><p class="rem2"><span>How to use</span>Tick each column when it is true. Come back to this page every few weeks.</p>
{tbl(['Concept', 'I know it', 'I can write it', 'I can play it', 'Handbook'], [[c, '<span class="cb2"></span>', '<span class="cb2"></span>', '<span class="cb2"></span>', 'p. ' + PM.resolve('{{' + k + '}}')] for c, k in qconcepts], ['36%', '15%', '17%', '17%', '15%'], 'prog')}
<div class="note2"><b>Teacher’s note</b><div class="lines"><span class="al"></span><span class="al"></span><span class="al"></span></div></div>''', 16, None)
qans = [('p. 1', 'Groups (A to G, three octaves): twos 3, threes 2 (the single black keys at each end belong to cut-off groups: count only full groups). Keys: 1 D, 2 A, 3 C, 4 E, 5 G, 6 B. Round and round: B C D · F E D · D E F · A G F.'),
        ('p. 2', 'Cs 3, Fs 3. Eight Cs: Lowest C, Low C, Bass C, Middle C, Treble C, High C, Very High C, Highest C. Ends: A, three; C (Highest C), three; 8.'),
        ('p. 3', 'Clefs: treble, line 2 = G; bass, line 4 = F. Line or space: line 1, space 2, line 4, space 3, line 2, line 5. Treble or bass: treble, bass, treble, bass, treble.'),
        ('p. 4', 'Which staff: 1 bass, 2 bass, 3 bass, 4 treble, 5 treble, 6 treble. Grand staff: brace; treble, right; bass, left; Middle C. T, F, T, F.'),
        ('p. 5', 'Keys: 1 E, 2 G, 3 A, 4 E, 5 G, 6 C (Treble C). Count: 5, 5, 6, 6, 8 (an octave). Mirror: 5; line 2, line 4.'),
        ('p. 6', 'Key to page: E, the bottom line; G, line 2; C (Treble C), space 3. True or false: T, T, F. Draw it: treble G line 2, C space 3, E line 1, F space 1; bass A space 1, B line 2, G line 1, E space 3.'),
        ('p. 7', 'Treble spaces F A C E; bass lines G B D F A; bass spaces A C E G. Step or skip: step, skip, step, skip, skip, step. Treble: G E A C F D B E.'),
        ('p. 8', 'Bass: F A C G E B D A. Words: BAG, FACE, EGG, CAGE, BED, CAFE, BAD, CAGE.'),
        ('p. 9', 'Ledger lines: A, C, B, C · C, E, B, D. Step out: G · A · B; F · E · D; B · Middle C · D. T, F (nearest), T, F (it is E).'),
        ('p. 10', 'First ledger lines: Middle C, A, E. Middle C: below, above, the same key. Two names: space 2 treble A, bass C; line 5 treble F, bass A; space 4 treble E, bass G.'),
        ('p. 11', 'Signs: sharp, the very next key to the right; flat, the very next key to the left; natural, cancels a sharp or flat. Black keys: 2 D♯/E♭, 3 F♯/G♭, 4 G♯/A♭, 5 A♯/B♭. Notes: F♯, B♭, C♯, E♭, G♯, A♭, F♯, B♭.'),
        ('p. 12', 'Bar: 1 F♯, 2 G, 3 F♯, 4 F (natural), 5 F. Sharp / flat: E♯ = F (white) / E♭ (black) · F♯ (black) / F♭ = E (white) · G♯ / G♭ (black) · B♯ = C (white) / B♭ (black). Enharmonics: D♭, D♯, F♯, B♭, F, B.'),
        ('p. 13', 'S, T, S, T, T, T. Up or down: F, E, C, B, E, G. True or false: T, F, T, T. Find them: E – F and B – C.'),
        ('p. 14', 'Numbers: 3rd, 5th, 2nd, 6th, 4th, octave, 7th, 3rd. Melodic, harmonic, harmonic, melodic. Note above: E, A, B, E, A, F.'),
        ('p. 15', 'Between: 3, 2, 3, 2, 6, 4. 3rds: 3 M, 2 m, 2 m, 3 M, 3 M, 2 m. Sizes: 3, 4, 6, 7, 8, 11.'),
        ('p. 16', 'D–F 3rd, 2, minor 3rd · C–E 3rd, 3, major 3rd · E–A 4th, 4, perfect 4th · D–A 5th, 6, perfect 5th · E–C 6th, 7, minor 6th.'),
        ('p. 17', 'E, C (Bass C), F♯, G · F, 8, Highest C · F (a semitone), T, T.')]
QA = _wp7(f'''<div class="kick">Pitch · Answers</div><h1>Answers</h1>
{tbl(['Page', 'Answers'], [[p, a] for p, a in qans], ['12%', '88%'], 'ansT')}
<p class="sm">“Draw it”, “in your music”, listening and playing have no single answer to copy: check them at the piano with your teacher, or with the online lessons.</p>''', 17, None)
pages = [Q1, Q2, Q3, Q4, Q7, Q8, Q5, Q6, QL, QL2, Q9, Q10, Q11, Q12, Q13, Q14, QR, QP, QA]
pages = [re.sub(r'<div class="foot"><span>\d+</span>', f'<div class="foot"><span>{k + 1}</span>', pg, count=1) for k, pg in enumerate(pages)]
FIRST.update({'Major or minor 3rd?': [('both', [('fill', '3'), ('ring', 'M')])], 'Which key?': [('fill', 'E')], 'Treble or bass?': [('ring', 'treble')]})
