# The Piano Butler Handbook, Part I: Pitch
import json, sys
src10 = open('/tmp/claude-0/pk/book10.py').read()
exec(src10.split("flow = ''.join(")[0])
css = eval("f'''" + src10[src10.index("css = f'''") + 10:src10.index("'''\nhtml =")] + "'''")
sys.path.insert(0, '/tmp/claude-0/pk')
from kb import keyboard, black_groups
P = json.load(open('/tmp/claude-0/vrv/pout.json'))
def px(k, h=110, cap=''):
    svg = P[k].replace('<svg ', '<svg style="max-height:%dpx" ' % h, 1)
    return '<figure class="vx px"><div class="vs">' + svg + '</div>' + ('<figcaption>' + cap + '</figcaption>' if cap else '') + '</figure>'
def ppage(inner, n): return page(inner, n, 'PART I · PITCH')
def kbx(*a, **k): return '<figure class="vx kbf">' + keyboard(*a, **k) + '</figure>'
NC = '#26296b'
def howto(title, steps): return '<div class="howto"><div class="bh">How to</div><b>' + title + '</b><ol>' + ''.join(f'<li>{x}</li>' for x in steps) + '</ol></div>'
flow = ''.join(f'<div class="fl"><span class="fln">{i + 1}</span><b>{a}</b><span>{b}</span></div>' + ('<span class="fa">›</span>' if i < 5 else '') for i, (a, b) in enumerate([('Keyboard', 'high and low, the patterns'), ('Staff', 'lines, spaces and clefs'), ('Note names', 'reading every note'), ('Sharps and flats', 'the black keys'), ('Intervals', 'the distance between notes'), ('Scales and keys', 'notes in families')]))
TOC = [('The keyboard', 22), ('The staff and the clefs', 23), ('Reading the notes', 24), ('The staff and the keyboard', 25), ('Sharps, flats and naturals', 26), ('Counting intervals', 27), ('Major, minor and perfect', 28), ('Scales', 29), ('Keys and key signatures', 30), ('The circle of fifths', 31)]
OPEN = f"""<section class="pg part2"><div class="pframe"><div class="pk">Part I</div><div class="pt">Pitch</div><div class="pdv"></div>
<p class="pl">Every note is higher or lower than another. This part starts with the keyboard you can see and touch, moves to the staff where those keys are written, and ends with the families of notes, scales and keys, that whole pieces are built from.</p>
<div class="flow">{flow}</div>
<div class="pin"><div class="pih">In this part</div>{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span>{p}</span></div>' for x, p in TOC)}</div></div></section>"""

g14 = black_groups('C', 14)
P22 = ppage(f"""{head('Part I · Pitch · 1', 'The keyboard', 'Keys to the <b>left</b> sound <b>lower</b>; keys to the <b>right</b> sound <b>higher</b>. The black keys come in groups of <b>two</b> and <b>three</b>, and that pattern repeats all the way along: it is how you find every note.')}
{kbx('C', 14, 30, 120, brackets=[(a, b, ('2 black keys' if k == 2 else '3 black keys'), True) for a, b, k in g14], label=True, shade={i: ('#fdeee8' if i % 7 < 3 else '#eef0f8') for i in range(14)}, marks=[f'<line x1="{x * 30}" x2="{x * 30}" y1="0" y2="120" stroke="#26296b" stroke-width="3.4"/>' for x in (3, 7, 10)], scale=1.25)}
{two(h3('The white keys') + '<p>Seven letters, <b>A B C D E F G</b>, then the letters start again. <b>C D E</b> sit around each group of two black keys (C just left of it), <b>F G A B</b> around each group of three (F just left of it): the two tints on the picture.</p>',
     h3('Middle C and octaves') + '<p><b>Middle C</b> is the C nearest the middle of the keyboard. From one C to the next is an <b>octave</b>: eight white keys, counting both. Octaves are numbered from the bottom: middle C is <b>C4</b>, the C below it C3, the C above C5; every key up to the next B shares the number (D4, E4 … B4).</p>')}
{tbl(['Term', 'Meaning', 'First met'], [['pitch', 'how high or low a sound is', 'Level 0'], ['register', 'a part of the keyboard: low, middle or high', 'Level 0'], ['semitone', 'from one key to the very next key, black or white', 'Level 0'], ['tone', 'two semitones', 'Level 0'], ['octave', 'from one note to the next with the same name (8 white keys, 12 semitones)', 'Level 0']], ['20%', '60%', '20%'])}
{howto('find any key, for example G4', ['Find middle C (C4): the C just left of the two black keys nearest the middle.', 'Say the letters up from it, one white key each: C D E F G.', 'Still in the same octave, so it is G4. One octave higher is G5.'])}
{foot('The staff p. 23 · The staff and the keyboard p. 25 · Semitones p. 27', 'Workbook Pitch 1 · Online: Keyboard patterns, Musical alphabet')}""", 22)

clefs = [[gsym('𝄞', 46), '<b>treble clef</b> (G clef)', 'curls round the line for G (line 2)', 'Level 0'], [gsym('𝄢', 30), '<b>bass clef</b> (F clef)', 'its two dots sit either side of the line for F (line 4)', 'Level 0'], [gsym('𝄡', 34), '<b>alto clef</b> (C clef)', 'its centre marks middle C, on line 3', 'Level 2']]
P23 = ppage(f"""{head('Part I · Pitch · 2', 'The staff and the clefs', 'Music is written on a <b>staff</b> (or stave) of five lines and four spaces. Lines and spaces are counted from the <b>bottom</b>. Higher notes sit higher on the staff. A <b>clef</b> at the start tells you which notes the lines and spaces stand for.')}
{tbl(['Clef', 'Name', 'How it shows its note', 'First met'], clefs, ['12%', '28%', '44%', '16%'])}
{two(h3('The grand staff') + '<p>Piano music uses two staves joined by a brace: the treble staff, usually for the right hand, above the bass staff, usually for the left. <b>Middle C</b> sits between them on a short line of its own, and can be written in either staff.</p>', px('gs_c', 118, 'Middle C in the treble staff (left) and in the bass staff (right): the same key.'), '1fr 1fr')}
{h3('Ledger lines')}
<p>Notes above or below the staff sit on short extra lines called <b>ledger lines</b>, spaced exactly like the staff lines. Count on from the staff as if the lines went on.</p>
{two(px('ledger', 64, 'Treble: A, B, C below; A, B, C above.'), px('ledger_b', 64, 'Bass: E, D, C below; C, D, E above.'))}
{h3('Octave signs')}
{tbl(['Sign', 'Meaning', 'First met'], [['<b>8va</b>', 'play an octave higher than written, as far as the dotted line goes', 'Level ½'], ['<b>8vb</b>', 'play an octave lower', 'Level ½'], ['<b>15ma</b>', 'play two octaves higher', 'Level 4'], ['<b>loco</b>', 'back where it is written', 'Level ½']], ['16%', '64%', '20%'])}
{foot('Reading the notes p. 24 · The staff and the keyboard p. 25', 'Workbook Pitch 2 · Online: Library › Staff and clefs')}""", 23)

rhy = [['Treble lines', 'E G B D F', '<i>Every Good Boy Deserves Fun</i>'], ['Treble spaces', 'F A C E', 'spells <i>FACE</i>'], ['Bass lines', 'G B D F A', '<i>Great Big Dragon Flies Away</i>'], ['Bass spaces', 'A C E G', '<i>All Cows Eat Grass</i>']]
P24 = ppage(f"""{head('Part I · Pitch · 3', 'Reading the notes', 'Each line and space has one letter name. Learn them in two ways: by the patterns below, and by a few <b>landmark notes</b> you can find instantly and count from.')}
{two(px('tr_lines', 80, 'Treble clef: the lines'), px('tr_spaces', 80, 'Treble clef: the spaces'))}
{two(px('bs_lines', 80, 'Bass clef: the lines'), px('bs_spaces', 80, 'Bass clef: the spaces'))}
{tbl(['Staff', 'Notes, bottom to top', 'To remember'], rhy, ['24%', '30%', '46%'])}
{h3('Landmark notes')}
<p>Find these first; every other note is a <b>step</b> (line to the next space, or space to the next line) or a <b>skip</b> (line to line, space to space) away.</p>
<div class="lmr"><div><b>Treble clef</b><br>Middle C on its ledger line below; the G the clef curls round (line 2); the C in the third space.</div>{px('lm_t', 70)}</div>
<div class="lmr"><div><b>Bass clef</b><br>The C in the second space; the F between the clef’s dots (line 4); middle C on its ledger line above.</div>{px('lm_b', 70)}</div>
{howto('read a note you are not sure of', ['Check the clef first.', 'Find the nearest landmark note.', 'Step or skip from it, saying the letters: a skip jumps one letter (G, B), a step goes to the next (G, A).'])}""", 24)

P25 = ppage(f"""{head('Part I · Pitch · 4', 'The staff and the keyboard', 'Every line and space of the grand staff is one white key. Read from left to right, the notes climb the staff exactly as the keys climb the keyboard: two octaves from C3 to C5, with middle C in coral where the two staves meet.')}
<figure class="vx px mapf"><div class="vs">{P['map'].replace('<svg ', '<svg style="max-height:520px" ', 1)}</div></figure>
{two(h3('What the map shows') + '<p>Each step up the staff (line to space, space to line) is the next <b>white</b> key. The black keys have no line or space of their own: they are written with a sharp or a flat on a white key’s line or space (p. 26).</p>',
     h3('Two ways to write one key') + '<p>Middle C can sit on a ledger line below the treble staff or above the bass staff. Both mean the same key; the music chooses the staff of the hand that plays it.</p>')}
{foot('The keyboard p. 22 · Reading the notes p. 24', 'Workbook Pitch 1–2 · Online: Library › Staff and clefs')}""", 25)

acc = [[gsym('♯', 28), 'sharp', 'raises a note by a semitone', 'Level 0'], [gsym('♭', 28), 'flat', 'lowers a note by a semitone', 'Level 0'], [gsym('♮', 28), 'natural', 'cancels a sharp or flat', 'Level ½'], [gsym('𝄪', 16), 'double sharp', 'raises by two semitones', 'Level 4'], [gsym('𝄫', 28), 'double flat', 'lowers by two semitones', 'Level 4']]
P26 = ppage(f"""{head('Part I · Pitch · 5', 'Sharps, flats and naturals', 'An <b>accidental</b> written before a note changes its pitch by a semitone. On the keyboard, a sharp usually means the black key to the right, a flat the black key to the left.')}
{tbl(['Sign', 'Name', 'What it does', 'First met'], acc, ['12%', '22%', '46%', '20%'])}
{h3('An accidental lasts for the bar')}
{two(px('acc_bar', 90, 'The sharp still counts later in the bar; after the bar line, F is F again.'), px('acc_nat', 90, 'A natural cancels the flat for the rest of the bar.'))}
<div class="rules"><div><b>Only that line or space.</b> A sharp on the F in the first space does not change the F an octave higher.</div><div><b>A tie carries it on.</b> A note tied across the bar line keeps its accidental.</div><div><b>Reminders.</b> A courtesy accidental, sometimes in brackets, just reminds you after a bar line.</div></div>
{h3('One key, two names')}
{two('<p>Every black key has two names: the key between F and G is both <b>F♯</b> and <b>G♭</b>. Notes that sound the same but are written differently are <b>enharmonic</b>. White keys can have sharp or flat names too: <b>E♯</b> is F, <b>C♭</b> is B.</p>', kbx('C', 7, 46, 150, label=True, marks=[f'<text x="{(i + 1) * 46}" y="{y}" text-anchor="middle" font-family="AH,Arial" font-size="10.5" font-weight="700" fill="#fff">{t}</text>' for i, (s1, f1) in zip((0, 1, 3, 4, 5), (('C♯', 'D♭'), ('D♯', 'E♭'), ('F♯', 'G♭'), ('G♯', 'A♭'), ('A♯', 'B♭'))) for y, t in ((62, s1), (77, f1))], scale=1.0), '1fr 1fr')}
{foot('Keys and key signatures p. 30', 'Workbook Pitch 3 · Online: Library › Signs')}""", 26)

def semis(start, n, hi=(), W=36):   # numbered semitones from a key: 0 on the start, 1, 2 … on every key in turn
    WH = 'CDEFGAB'; s0 = WH.index(start); keys = []
    for i in range(10):
        L = WH[(s0 + i) % 7]; keys.append(('w', i))
        if L in 'CDFGA': keys.append(('b', i))
    out = []
    for k, (t, i) in enumerate(keys[:n + 1]):
        x = (i + 0.5) * W if t == 'w' else (i + 1) * W; y = 84 if t == 'w' else 60
        col = '#e4572e' if k in hi else ('#26296b' if t == 'w' else '#fff')
        out.append(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="{col}">{k}</text>')
    return out
P27 = ppage(f"""{head('Part I · Pitch · 6', 'Counting intervals', 'An <b>interval</b> is the distance between two notes. A <b>semitone</b> is the very next key; a <b>tone</b> is two semitones. An interval’s <b>number</b> comes from counting letter names, both ends included.')}
{two(px('tones', 90, 'E–F and B–C are semitones; C–D and F–G are tones.'), px('mel_harm', 90, 'Melodic: one note after the other. Harmonic: together.'))}
{h3('Counting the number')}
{px('ex_iv', 100, 'D up to A: D E F G A is five letters, so the interval is a 5th, whether the notes come one after the other or together.')}
{h3('Interval numbers from C')}
{px('intv', 104)}
{howto('name an interval’s number', ['Say the lower note’s letter as 1.', 'Count up the letters to the higher note: line, space, line …', 'The last number is the interval: the same note is a unison (1), 3 letters a 3rd, 5 letters a 5th, 8 letters an octave. Sharps and flats do not change the number.'])}
{foot('Major, minor and perfect p. 28 · Scales p. 29', 'Workbook Pitch 4 · Online: Library › Intervals')}""", 27)

iv = [['unison', '0', '', '', 'Level 1'], ['2nd', '1 (minor)', '2 (major)', '', 'Level 1'], ['3rd', '3 (minor)', '4 (major)', '', 'Level ½'], ['4th', '', '5 (perfect)', '6 (augmented)', 'Level 1'], ['5th', '6 (diminished)', '7 (perfect)', '', 'Level 1'], ['6th', '8 (minor)', '9 (major)', '', 'Level 2'], ['7th', '10 (minor)', '11 (major)', '', 'Level 2'], ['octave', '', '12 (perfect)', '', 'Level 1']]
P28 = ppage(f"""{head('Part I · Pitch · 7', 'Major, minor and perfect', 'Two intervals with the same number can differ in size. C–E and C–E♭ are both 3rds, but one is a semitone wider. The <b>quality</b> (major, minor, perfect…) comes from counting <b>semitones</b>.')}
{two(kbx('C', 7, 36, 120, label=True, marks=semis('C', 4, hi=(0, 4)), scale=1.0) + '<p class="sm">C to E: count every key, black and white. 4 semitones: a major 3rd.</p>', kbx('C', 7, 36, 120, label=True, marks=semis('C', 3, hi=(0, 3)), scale=1.0) + '<p class="sm">C to E♭: 3 semitones: a minor 3rd.</p>')}
{px('q3', 92)}
{h3('Size in semitones')}
{tbl(['Number', 'Smaller', 'Main', 'Wider', 'First met'], iv, ['16%', '22%', '22%', '22%', '18%'])}
<div class="ladder"><div><b>2nds, 3rds, 6ths, 7ths</b><span>diminished ‹ <b>minor</b> ‹ <b>major</b> › augmented</span></div><div><b>unisons, 4ths, 5ths, octaves</b><span>diminished ‹ <b>perfect</b> › augmented</span></div></div>
<p class="sm">Each step on the ladder is one semitone. Six semitones (an augmented 4th or diminished 5th) is the tritone. Turned upside down, an interval’s numbers add to 9 and major and minor swap: a major 3rd becomes a minor 6th.</p>
{foot('Counting intervals p. 27 · Chords p. 50', 'Workbook Pitch 4 · Online: Library › Intervals')}""", 28)

forms = [['major', 'T T S T T T S', 'Level ½'], ['natural minor', 'T S T T S T T', 'Level ½'], ['harmonic minor', 'T S T T S T+S S', 'Level ½'], ['melodic minor (up)', 'T S T T T T S; down as the natural minor', 'Level 2'], ['chromatic', 'every semitone', 'Level 2'], ['pentatonic (black keys)', 'T T T+S T T+S', 'Level 0']]
deg = [['1', 'tonic'], ['2', 'supertonic'], ['3', 'mediant'], ['4', 'subdominant'], ['5', 'dominant'], ['6', 'submediant'], ['7', 'leading note']]
P29 = ppage(f"""{head('Part I · Pitch · 8', 'Scales', 'A <b>scale</b> is a ladder of notes from one key note up to the next, in a fixed pattern of tones (T) and semitones (S). The pattern, not the starting note, makes a scale major or minor.')}
{px('c_maj', 44, 'C major: T T S T T T S. The semitones fall between 3–4 and 7–8.')}
{tbl(['Scale', 'Steps', 'First met'], forms, ['30%', '50%', '20%'])}
{h3('A minor in three forms')}
{px('a_nat', 40, 'Natural: the notes of C major, from A to A.')}
{px('a_har', 40, 'Harmonic: the 7th raised a semitone (G♯).')}
{px('a_mel', 40, 'Melodic: 6th and 7th raised going up, lowered coming down.')}
{two(h3('Degree names') + '<p class="degs">' + ' · '.join(f'<b>{a}</b> {b}' for a, b in deg) + '</p>', h3('Minor partners') + '<p><b>Relative</b>: same signature, 3 semitones lower (C major, A minor). <b>Parallel</b>: same key note (C major, C minor).</p>')}
{howto('build any major scale', ['Write the eight letters from the key note up, every letter once.', 'Check each step against T T S T T T S on the keyboard; add a sharp or flat where a step is wrong. G major: G A B C D E F♯ G.'])}""", 29)

keys = [['C major', 'A minor', '—', 'Level ½'], ['G major', 'E minor', '1♯', 'Level ½'], ['D major', 'B minor', '2♯', 'Level 1'], ['A major', 'F♯ minor', '3♯', 'Level 3'], ['E major', 'C♯ minor', '4♯', 'Level 4'], ['B major', 'G♯ minor', '5♯', 'Level 4'], ['F major', 'D minor', '1♭', 'Level ½'], ['B♭ major', 'G minor', '2♭', 'Level 1'], ['E♭ major', 'C minor', '3♭', 'Level 3'], ['A♭ major', 'F minor', '4♭', 'Level 4'], ['D♭ major', 'B♭ minor', '5♭', 'Level 4']]
P30 = ppage(f"""{head('Part I · Pitch · 9', 'Keys and key signatures', 'A <b>key signature</b> at the start of each line lists the sharps or flats the piece uses throughout, so they do not have to be written before every note. They always appear in the same order.')}
{two(px('sharps', 84, 'Sharps: F C G D A E B. The key note is a semitone above the last sharp.'), px('flats', 84, 'Flats: B E A D G C F. From two flats, the second-last flat names the key.'))}
<p class="sm">To remember the order: <b>F</b>ather <b>C</b>harles <b>G</b>oes <b>D</b>own <b>A</b>nd <b>E</b>nds <b>B</b>attle; backwards for the flats: <b>B</b>attle <b>E</b>nds <b>A</b>nd <b>D</b>own <b>G</b>oes <b>C</b>harles’ <b>F</b>ather.</p>
{tbl(['Major', 'Relative minor', 'Signature', 'First met'], keys, ['28%', '28%', '20%', '24%'])}
<p class="sm">Six and seven sharps or flats (F♯, C♯, G♭, C♭ major and their minors) come at Levels 4–6.</p>
{howto('find the key of a piece', ['Read the key signature: it gives two keys, a major and its relative minor.', 'Look at the last bass note: it is usually the key note.', 'Look for the raised 7th of the minor (G♯ in A minor): if it keeps appearing, the piece is minor.'])}
{foot('Scales p. 29 · The circle of fifths p. 31', 'Workbook Pitch 5 · Online: Scale finder, Library › Keys')}""", 30)

def circle():
    import math
    MAJ = ['C', 'G', 'D', 'A', 'E', 'B', 'F♯/G♭', 'D♭', 'A♭', 'E♭', 'B♭', 'F']; MIN = ['a', 'e', 'b', 'f♯', 'c♯', 'g♯', 'd♯/e♭', 'b♭', 'f', 'c', 'g', 'd']
    SIG = ['', '1♯', '2♯', '3♯', '4♯', '5♯', '6♯/6♭', '5♭', '4♭', '3♭', '2♭', '1♭']
    cx, cy, R1, R2, R3 = 230, 230, 200, 140, 95; s = f'<circle cx="{cx}" cy="{cy}" r="{R1 + 20}" fill="#fff" stroke="#26296b" stroke-width="2"/><circle cx="{cx}" cy="{cy}" r="{R2 + 26}" fill="none" stroke="#c9cbe0" stroke-width="1.2"/><circle cx="{cx}" cy="{cy}" r="{R3 + 22}" fill="none" stroke="#c9cbe0" stroke-width="1.2"/>'
    for i in range(12):
        a = math.radians(i * 30 - 90); c, sn = math.cos(a), math.sin(a)
        s += f'<line x1="{cx + c * (R3 + 22)}" y1="{cy + sn * (R3 + 22)}" x2="{cx + c * (R1 + 20)}" y2="{cy + sn * (R1 + 20)}" stroke="#e8e4f2" stroke-width="1"/>' if False else ''
        s += f'<text x="{cx + c * R1}" y="{cy + sn * R1 + 7}" text-anchor="middle" font-family="AH,Arial" font-size="{15 if "/" in MAJ[i] else 21}" font-weight="700" fill="{"#e4572e" if i == 0 else "#26296b"}">{MAJ[i]}</text>'
        s += f'<text x="{cx + c * R2}" y="{cy + sn * R2 + 6}" text-anchor="middle" font-family="AH,Arial" font-size="{13 if "/" in MIN[i] else 16}" font-weight="700" fill="#6d6f9c">{MIN[i]}</text>'
        s += f'<text x="{cx + c * R3}" y="{cy + sn * R3 + 5}" text-anchor="middle" font-family="AH,Arial" font-size="12" fill="#6d6f9c">{SIG[i]}</text>'
    s += f'<text x="{cx}" y="{cy - 4}" text-anchor="middle" font-family="AH,Arial" font-size="11" font-weight="700" letter-spacing="1.5" fill="#6d6f9c">MAJOR</text><text x="{cx}" y="{cy + 12}" text-anchor="middle" font-family="AH,Arial" font-size="11" letter-spacing="1.5" fill="#6d6f9c">minor · signature</text>'
    return f'<figure class="vx cof"><svg viewBox="0 0 460 460" style="width:100%;max-width:380px;height:auto;display:block;margin:0 auto">{s}</svg></figure>'
P31 = ppage(f"""{head('Part I · Pitch · 10', 'The circle of fifths', 'All the keys on one clock face. Going round clockwise, each key is a <b>5th higher</b> than the last and has <b>one more sharp</b> (or one fewer flat). Anticlockwise, each is a 4th higher, a 5th lower, with one more flat.')}
{two(circle(), h3('Reading the circle') + '<p><b>Outer ring:</b> major keys. <b>Middle ring:</b> their relative minors (small letters). <b>Inner ring:</b> the key signature.</p>' + h3('Neighbours are close') + '<p>Keys next to each other share all but one note, so music moves between them easily: from C major to G major or F major, or to the relative minor. These are the <b>related keys</b>.</p>' + h3('At the bottom') + '<p>Six sharps and six flats meet: F♯ major and G♭ major are the same keys on the piano, written two ways.</p>', '1.1fr 1fr')}
{howto('use the circle', ['To find a key signature: count the steps from C, clockwise for sharps, anticlockwise for flats.', 'To find related keys: look one step either side, and straight in for the relative minor.', 'To practise scales in a smart order: go round the circle, one new sharp or flat at a time.'])}
{foot('Keys and key signatures p. 30 · Chords p. 50', 'Workbook Pitch 5 · Online: Scale finder, Library › Related keys')}""", 31)

css += '''
.degs{font-size:14px;line-height:1.7} .howto{border-left:3px solid #e4572e;background:#fdf6f2;padding:8px 14px;margin:12px 0;font-size:14px} .howto .bh{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e} .howto b{font-size:15px} .howto ol{margin:4px 0 0;padding-left:20px} .howto li{margin:2px 0} .rules{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;font-size:13.5px;line-height:1.45;margin:8px 0 6px} .ladder{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:10px 0 4px;font-size:14px} .ladder div{display:flex;flex-direction:column;border:1px solid #e2ddd0;padding:8px 10px} .ladder span{color:#4a4d86} .mapf .vs svg{max-width:100%} .kbl{font-family:'AH',Arial} .lmr{display:grid;grid-template-columns:1fr 1.25fr;gap:18px;align-items:center;margin:8px 0} .lmr>div:first-child{font-size:14.5px;line-height:1.55} .lmr .vx{margin:0}
.px .vs svg{width:100%;height:auto} .px text{font-family:'AH',Arial !important;fill:#26296b !important;font-weight:700} .kbf{display:flex;justify-content:center}
'''
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{OPEN}{P22}{P23}{P24}{P25}{P26}{P27}{P28}{P29}{P30}{P31}</body></html>'
open('/mnt/user-data/outputs/house-rooms/handbook-pitch.html', 'w').write(html)
print('ok')
