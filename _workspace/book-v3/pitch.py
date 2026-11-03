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

flow = ''.join(f'<div class="fl"><span class="fln">{i + 1}</span><b>{a}</b><span>{b}</span></div>' + ('<span class="fa">›</span>' if i < 5 else '') for i, (a, b) in enumerate([('Keyboard', 'high and low, the patterns'), ('Staff', 'lines, spaces and clefs'), ('Note names', 'reading every note'), ('Sharps and flats', 'the black keys'), ('Intervals', 'the distance between notes'), ('Scales and keys', 'notes in families')]))
TOC = [('The keyboard', 22), ('The staff and the clefs', 23), ('Reading the notes', 24), ('Sharps, flats and naturals', 25), ('Tones, semitones and intervals', 26), ('Scales', 27), ('Keys and key signatures', 28)]
OPEN = f'''<section class="pg part2"><div class="pframe"><div class="pk">Part I</div><div class="pt">Pitch</div><div class="pdv"></div>
<p class="pl">Every note is higher or lower than another. This part starts with the keyboard you can see and touch, moves to the staff where those keys are written, and ends with the families of notes, scales and keys, that whole pieces are built from.</p>
<div class="flow">{flow}</div>
<div class="pin"><div class="pih">In this part</div>{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span>{p}</span></div>' for x, p in TOC)}</div></div></section>'''

g14 = black_groups('C', 14)
P22 = ppage(f'''{head('Part I · Pitch · 1', 'The keyboard', 'Keys to the <b>left</b> sound <b>lower</b>; keys to the <b>right</b> sound <b>higher</b>. The black keys come in groups of <b>two</b> and <b>three</b>, and that pattern repeats all the way along: it is how you find every note.')}
{kbx('C', 14, 30, 120, brackets=[(a, b, ('2' if k == 2 else '3'), True) for a, b, k in g14], label=True, shade={0: '#fde6dd'}, scale=1.25)}
{two(h3('The white keys') + '<p>The white keys are named with seven letters, <b>A B C D E F G</b>, then the letters start again. <b>C</b> is the white key just left of each group of two black keys; <b>F</b> is just left of each group of three.</p>',
     h3('Middle C and octaves') + '<p><b>Middle C</b> is the C nearest the middle of the keyboard, usually right in front of you. From one C to the next is an <b>octave</b>: eight white keys, counting both. A full piano has 88 keys, from A at the bottom to C at the top.</p>')}
{h3('Words to know')}
{tbl(['Term', 'Meaning', 'First met'], [['pitch', 'how high or low a sound is', 'Level 0'], ['octave', 'the distance from one note to the next with the same name (8 white keys)', 'Level 0'], ['semitone', 'from one key to the very next key, black or white', 'Level 0'], ['tone', 'two semitones', 'Level 0'], ['register', 'a part of the keyboard: low, middle or high', 'Level 0']], ['20%', '60%', '20%'])}
{watch(['Finding C by counting from the bottom: find a group of two black keys and look just to the left.', 'Calling every white-to-white step a tone: E–F and B–C have no black key between them, so they are semitones.'])}
{foot('The staff p. 23 · Tones and semitones p. 26', 'Workbook Level 0 · Keyboard · Online: Keyboard patterns, Musical alphabet')}''', 22)

clefs = [[gl('𝄞', 40), '<b>treble clef</b> (G clef)', 'curls round the line for G (line 2)', 'Level 0'], [gl('𝄢', 34), '<b>bass clef</b> (F clef)', 'its two dots sit either side of the line for F (line 4)', 'Level 0'], [gl('𝄡', 34), '<b>alto clef</b> (C clef)', 'its centre marks middle C, on line 3', 'Level 2']]
P23 = ppage(f'''{head('Part I · Pitch · 2', 'The staff and the clefs', 'Music is written on a <b>staff</b> (or stave) of five lines and four spaces. Lines and spaces are counted from the <b>bottom</b>. Higher notes sit higher on the staff. A <b>clef</b> at the start tells you which notes the lines and spaces stand for.')}
{tbl(['Clef', 'Name', 'How it shows its note', 'First met'], clefs, ['12%', '28%', '44%', '16%'])}
{two(h3('The grand staff') + '<p>Piano music uses two staves joined by a brace: the treble staff, usually for the right hand, above the bass staff, usually for the left. <b>Middle C</b> sits between them on a short line of its own, and can be written in either staff.</p>', px('gs_c', 190), '1fr 1fr')}
{two(h3('Ledger lines') + '<p>Notes above or below the staff are written on short extra lines called <b>ledger lines</b>, spaced exactly like the staff lines.</p>' + px('ledger', 96),
     h3('Octave signs') + tbl(['Sign', 'Meaning'], [['<b>8va</b>', 'play an octave higher than written; a dotted line shows how long'], ['<b>8vb</b>', 'play an octave lower'], ['<b>15ma</b>', 'play two octaves higher'], ['<b>loco</b>', 'back where it is written']], ['26%', '74%']) + '<p class="sm">Level ½. Octave signs save writing many ledger lines.</p>')}
{foot('Reading the notes p. 24', 'Workbook Level 0 · The staff · Online: Library › Staff and clefs')}''', 23)

rhy = [['Treble lines', 'E G B D F', '<i>Every Good Boy Deserves Fun</i>'], ['Treble spaces', 'F A C E', 'spells <i>FACE</i>'], ['Bass lines', 'G B D F A', '<i>Great Big Dragon Flies Away</i>'], ['Bass spaces', 'A C E G', '<i>All Cows Eat Grass</i>']]
P24 = ppage(f'''{head('Part I · Pitch · 3', 'Reading the notes', 'Each line and space has one letter name. Learn them in two ways: by the patterns below, and by a few <b>landmark notes</b> you can find instantly and count from.')}
{two(px('tr_lines', 100, 'Treble clef: the lines'), px('tr_spaces', 100, 'Treble clef: the spaces'))}
{two(px('bs_lines', 100, 'Bass clef: the lines'), px('bs_spaces', 100, 'Bass clef: the spaces'))}
{tbl(['Staff', 'Notes, bottom to top', 'To remember'], rhy, ['24%', '30%', '46%'])}
{h3('Landmark notes')}
{two('<p>Find these first: middle C, the G the treble clef curls round, the F between the bass clef’s dots. Any other note is a step or a skip away. A <b>step</b> moves from a line to the next space (or space to line); a <b>skip</b> jumps from line to line or space to space.</p>', px('landmarks', 160), '1fr 1.2fr')}
{watch(['Reading the bass clef with treble names: the same position has a different name in each clef.', 'Counting lines from the top: always count from the bottom.'])}''', 24)

acc = [[gl('♯', 30), 'sharp', 'raises a note by a semitone', 'Level 0'], [gl('♭', 30), 'flat', 'lowers a note by a semitone', 'Level 0'], [gl('♮', 30), 'natural', 'cancels a sharp or flat', 'Level ½'], [gl('𝄪', 30), 'double sharp', 'raises by two semitones', 'Level 4'], [gl('𝄫', 30), 'double flat', 'lowers by two semitones', 'Level 4']]
P25 = ppage(f'''{head('Part I · Pitch · 4', 'Sharps, flats and naturals', 'An <b>accidental</b> written before a note changes its pitch by a semitone. On the keyboard, a sharp usually means the black key to the right, a flat the black key to the left.')}
{tbl(['Sign', 'Name', 'What it does', 'First met'], acc, ['12%', '22%', '46%', '20%'])}
{h3('An accidental lasts for the bar')}
{two(px('acc_bar', 96, 'The sharp still counts later in the bar; after the bar line, F is F again.'), px('acc_nat', 96, 'A natural cancels the flat for the rest of the bar.'))}
{h3('One key, two names')}
{two('<p>Every black key has two names: the key between F and G is both <b>F♯</b> and <b>G♭</b>. Notes that sound the same but are written differently are <b>enharmonic</b>. White keys can have sharp or flat names too: <b>E♯</b> is F, <b>C♭</b> is B.</p>', kbx('C', 7, 34, 110, label=True, marks=[f'<text x="{1 * 34}" y="-6" text-anchor="middle" font-family="AH" font-size="12" font-weight="700" fill="#e4572e">C♯ D♭</text>', f'<text x="{4 * 34}" y="-6" text-anchor="middle" font-family="AH" font-size="12" font-weight="700" fill="#e4572e">F♯ G♭</text>']).replace('viewBox="-2 -2', 'viewBox="-2 -20'), '1fr 1fr')}
{watch(['Forgetting that an accidental carries on through the bar.', 'Thinking every sharp is a black key: E♯ and B♯ are white keys.'])}
{foot('Keys and key signatures p. 28', 'Workbook Levels 0–½ · Accidentals · Online: Library › Signs')}''', 25)

iv = [['unison', '0', '', '', 'Level 1'], ['2nd', '1 (minor)', '2 (major)', '', 'Level 1'], ['3rd', '3 (minor)', '4 (major)', '', 'Level ½'], ['4th', '', '5 (perfect)', '6 (augmented)', 'Level 1'], ['5th', '6 (diminished)', '7 (perfect)', '', 'Level 1'], ['6th', '8 (minor)', '9 (major)', '', 'Level 2'], ['7th', '10 (minor)', '11 (major)', '', 'Level 2'], ['octave', '', '12 (perfect)', '', 'Level 1']]
P26 = ppage(f'''{head('Part I · Pitch · 5', 'Tones, semitones and intervals', 'A <b>semitone</b> is the very next key; a <b>tone</b> is two semitones. An <b>interval</b> is the distance between two notes. Its <b>number</b> comes from counting letter names, both ends included; its <b>quality</b> from counting semitones.')}
{two(px('tones', 96, 'E–F and B–C are semitones; C–D and F–G are tones.'), px('mel_harm', 96, 'Melodic: one note after the other. Harmonic: together.'))}
{h3('Interval numbers from C')}
{px('intv', 110)}
{h3('Size in semitones')}
{tbl(['Number', 'Smaller', 'Main', 'Wider', 'First met'], iv, ['16%', '22%', '22%', '22%', '18%'])}
<p class="sm">Augmented: a semitone wider than major or perfect. Diminished: a semitone narrower than minor or perfect (Level 5). Six semitones is the tritone. Turned upside down, the numbers add to 9 and major and minor swap.</p>
{foot('Scales p. 27 · Chords p. 50', 'Workbook Levels 1–2 · Intervals · Online: Library › Intervals')}''', 26)

forms = [['major', 'T T S T T T S', 'Level ½'], ['natural minor', 'T S T T S T T', 'Level ½'], ['harmonic minor', 'T S T T S T+S S', 'Level ½'], ['melodic minor (up)', 'T S T T T T S; down as the natural minor', 'Level 2'], ['chromatic', 'every semitone', 'Level 2'], ['pentatonic (black keys)', 'T T T+S T T+S', 'Level 0']]
deg = [['1', 'tonic'], ['2', 'supertonic'], ['3', 'mediant'], ['4', 'subdominant'], ['5', 'dominant'], ['6', 'submediant'], ['7', 'leading note']]
P27 = ppage(f'''{head('Part I · Pitch · 6', 'Scales', 'A <b>scale</b> is a ladder of notes from one key note up to the next, in a fixed pattern of tones (T) and semitones (S). The pattern, not the starting note, makes a scale major or minor.')}
{px('c_maj', 80, 'C major: T T S T T T S. The semitones fall between 3–4 and 7–8.')}
{tbl(['Scale', 'Steps', 'First met'], forms, ['30%', '50%', '20%'])}
{h3('A minor in three forms')}
{px('a_nat', 62, 'Natural: the notes of C major, from A to A.')}
{px('a_har', 62, 'Harmonic: the 7th raised a semitone (G♯).')}
{px('a_mel', 62, 'Melodic: 6th and 7th raised going up, lowered coming down.')}
{two(h3('Degree names') + '<p class="degs">' + ' · '.join(f'<b>{a}</b> {b}' for a, b in deg) + '</p>', h3('Relative major and minor') + '<p>Every major key shares its notes and key signature with a minor key three semitones lower: its <b>relative minor</b>. C major and A minor; G major and E minor.</p>')}''', 27)

keys = [['C major', 'A minor', '—', 'Level ½'], ['G major', 'E minor', '1♯', 'Level ½'], ['D major', 'B minor', '2♯', 'Level 1'], ['A major', 'F♯ minor', '3♯', 'Level 3'], ['E major', 'C♯ minor', '4♯', 'Level 4'], ['B major', 'G♯ minor', '5♯', 'Level 4'], ['F major', 'D minor', '1♭', 'Level ½'], ['B♭ major', 'G minor', '2♭', 'Level 1'], ['E♭ major', 'C minor', '3♭', 'Level 3'], ['A♭ major', 'F minor', '4♭', 'Level 4'], ['D♭ major', 'B♭ minor', '5♭', 'Level 4']]
P28 = ppage(f'''{head('Part I · Pitch · 7', 'Keys and key signatures', 'A <b>key signature</b> at the start of each line lists the sharps or flats the piece uses throughout, so they do not have to be written before every note. They always appear in the same order.')}
{two(px('sharps', 90, 'Sharps: F C G D A E B. The key note is a semitone above the last sharp.'), px('flats', 90, 'Flats: B E A D G C F. From two flats, the second-last flat names the key.'))}
{tbl(['Major', 'Relative minor', 'Signature', 'First met'], keys, ['28%', '28%', '20%', '24%'])}
<p class="sm">Six and seven sharps or flats (F♯, C♯, G♭, C♭ major and their minors) come at Levels 4–6.</p>
{watch(['Forgetting the key signature halfway down the page: it applies to every line and every octave.', 'Naming a minor key from its signature alone: check the last note and look for a raised 7th.'])}
{foot('Scales p. 27 · Related keys p. 30', 'Workbook Levels ½–4 · Keys · Online: Scale finder, Library › Keys')}''', 28)

css += '''
.degs{font-size:14px;line-height:1.7}
.px .vs svg{width:100%;height:auto} .px text{font-family:'AH',Arial !important;fill:#26296b !important;font-weight:700} .kbf{display:flex;justify-content:center}
'''
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}</style></head><body>{OPEN}{P22}{P23}{P24}{P25}{P26}{P27}{P28}</body></html>'
open('/mnt/user-data/outputs/house-rooms/handbook-pitch.html', 'w').write(html)
print('ok')
