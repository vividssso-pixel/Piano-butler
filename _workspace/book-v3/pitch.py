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

import re as _re2
def ringsvg(svg, idx):   # the accidental to look at is coral and circled (her 4 Nov)
    ks = [m for m in _re2.finditer(r'<g id="[^"]+" class="keyAccid">\s*<use xlink:href="#([^"]+)" x="(\d+)" y="(\d+)"', svg)]
    m = ks[idx]; flat = m.group(1).startswith('E260'); x, y = int(m.group(2)), int(m.group(3))
    cy = y - 50 if flat else y; cx = x + (75 if flat else 90); gid = m.group(0).split('"')[1]
    svg = svg[:m.start()] + m.group(0).replace('class="keyAccid">', 'class="keyAccid" fill="#e4572e">') + svg[m.end():]
    return svg.replace('<g id="' + gid + '"', '<circle cx="%d" cy="%d" r="205" fill="none" stroke="#e4572e" stroke-width="34"/><g id="' % (cx, cy) + gid + '"', 1)
def ringks(k, idx, h=66, cap=''):
    svg = ringsvg(P[k], idx)
    mo = _re2.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg); W = float(mo.group(1))
    mi = _re2.search(r'class="definition-scale" color="black" viewBox="0 0 ([\d.]+) ([\d.]+)"', svg); f = float(mi.group(1)) / W
    svg = svg.replace(mo.group(0), 'viewBox="0 0 110 86"', 1).replace(mi.group(0), 'class="definition-scale" color="black" viewBox="0 %g %g %g"' % (8 * f, 110 * f, 86 * f), 1).replace('overflow="visible"', 'overflow="hidden"', 1)
    svg = svg.replace('<svg ', '<svg style="max-height:%dpx" ' % h, 1)
    return '<figure class="vx px"><div class="vs">' + svg + '</div>' + ('<figcaption>' + cap + '</figcaption>' if cap else '') + '</figure>'
P['ex_key'] = ringsvg(P['ex_key'], 0)
def ppage(inner, n): return page(inner, n, 'PART I · PITCH')
def kbx(*a, **k): return '<figure class="vx kbf">' + keyboard(*a, **k) + '</figure>'
NC = '#26296b'
def inaction(title, fig, steps, result): return '<div class="inact"><div class="bh">Example</div><b class="it">' + title + '</b>' + fig + '<div class="isteps">' + ''.join(f'<div><span class="in">{i + 1}</span><span>{t}</span></div>' for i, t in enumerate(steps)) + '</div><div class="ires">' + result + '</div></div>'
def howto(title, steps): return '<div class="howto"><div class="bh">How to</div><b>' + title + '</b><ol>' + ''.join(f'<li>{x}</li>' for x in steps) + '</ol></div>'
flow = ''.join(f'<div class="fl"><b>{a}</b><span>{b}</span></div>' + ('<span class="fa">›</span>' if i < 5 else '') for i, (a, b) in enumerate([('Keyboard', 'high and low, the patterns'), ('Staff', 'lines, spaces and clefs'), ('Reading the notes', 'every note on the staff'), ('Sharps and flats', 'the black keys'), ('Intervals', 'the distance between notes'), ('Scales and keys', 'notes in families')]))
TOC = [('The keyboard', 22), ('The staff and the clefs', 23), ('Reading the notes', 24), ('The staff and the keyboard', 25), ('Sharps, flats and naturals', 26), ('Counting intervals', 27), ('Major, minor and perfect', 28), ('Major scales', 29), ('Minor scales', 30), ('Keys and key signatures', 31), ('Finding the key', 32), ('The circle of fifths', 33), ('Tips: when a note sounds wrong', 46)]
OPEN = f"""<section class="pg part2"><div class="pframe"><div class="pk">Part I · Which note</div><div class="pt">Pitch</div><div class="pdv"></div>
<p class="pl">High or low? That is the first question every note answers. Start with the keys under your fingers, find where they live on the staff, then meet the note families (scales and keys) that whole pieces are built from.</p>
<div class="flow">{flow}</div>
<div class="pin"><div class="pih">In this part</div>{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span>{p}</span></div>' for x, p in TOC)}</div></div></section>"""


def six_q():
    svg = open('/tmp/claude-0/pk/six/six.svg').read().replace('<svg ', '<svg style="width:100%;max-height:205px" ', 1)
    return f'<figure class="vx px tq sixf"><div class="vs">{svg}</div></figure>'
SIX = [('Who?', 'Finger 3, the middle finger, plays the red note.', 'Playing (later)'), ('When?', 'On beat 1 of bar 2, and it stays for two beats.', 'Part II · Time'), ('Where?', 'E: the white key just right of two black keys.', 'Part I · Pitch'),
       ('What?', 'A note of the C major chord, marked C above it.', 'Harmony (later)'), ('How?', 'Softly (p) and smoothly, under the curved slur.', 'Expression (later)'), ('Why?', 'It ends the phrase (the slur), so it lands gently.', 'Shape and style (later)')]
P21 = page(f"""{head('Before you start', 'Every note answers six questions', 'Who, when, where, what, how and why: the six questions of any good story. A note on the page answers all six at once, and each part of this book answers one of them.')}
{six_q()}
<div class="six">{''.join(f'<div><b>{q}</b><span>{a}</span><i>{p}</i></div>' for q, a, p in SIX)}</div>
<p class="think"><span>Think of it</span>Like a news report: who, when, where, what, how and why. Leave one out and the story is not clear; leave one out in a piece and the note is not right. Finger numbers are the “who”, so they matter as much as the note itself.</p>
<div class="tip"><div class="bh">Tip</div><b class="tt">When a passage won’t come right, ask which question it is</b>
{tbl(['What you notice', 'Question', 'Turn to'], [['You stumble in the same place every time', '<b class="co">Who?</b> the finger', 'Playing and listening'], ['It rushes, drags or the counting slips', '<b class="co">When?</b> the rhythm', 'Part II · Time'], ['A note sounds wrong', '<b class="co">Where?</b> the note name', 'Part I · Pitch'], ['A chord sounds odd or thin', '<b class="co">What?</b> the harmony', 'Harmony'], ['It is correct but flat and dull', '<b class="co">How?</b> the expression', 'Expression'], ['It does not seem to go anywhere', '<b class="co">Why?</b> the shape', 'Shape and style']], ['44%', '28%', '28%'])}
<p class="sm" style="margin:6px 0 0">The same six questions work for any music you meet: a pop song, a hymn, a film theme or a sonata.</p></div>""", 21, 'BEFORE YOU START')

g14 = black_groups('C', 14)
P22 = ppage(f"""{head('Part I · Pitch · 1', 'The keyboard', 'Keys to the <b>left</b> sound <b>lower</b>; keys to the <b>right</b> sound <b>higher</b>. The black keys come in groups of <b>two</b> and <b>three</b>, and that pattern repeats all the way along: it is how you find every note.')}
{kbx('C', 14, 30, 88, brackets=[(a, b, ('2 black keys' if k == 2 else '3 black keys'), True) for a, b, k in g14], label=True, shade={i: ('#fdeee8' if i % 7 < 3 else '#eef0f8') for i in range(14)}, marks=[f'<line x1="{x * 30}" x2="{x * 30}" y1="0" y2="88" stroke="#26296b" stroke-width="3.4"/>' for x in (3, 7, 10)], scale=1.0)}
{two(h3('The white keys') + '<p>Seven letters, <b>A B C D E F G</b>, then the letters start again, like the days of the week. <b>C D E</b> sit around each group of two black keys (C just left of it), <b>F G A B</b> around each group of three (F just left of it): the two tints on the picture.</p>',
     h3('Middle C and octaves') + '<p><b>Middle C</b> is the C nearest the middle of the keyboard. From one C to the next is an <b>octave</b>: eight white keys, counting both. Octaves are numbered from the bottom: middle C is <b>C4</b>, the C below it C3, the C above C5; every key up to the next B shares the number (D4, E4 … B4).</p>')}
{tbl(['Term', 'Meaning', 'First met'], [['pitch', 'how high or low a sound is', 'Level 0'], ['register', 'a part of the keyboard: low, middle or high', 'Level 0'], ['semitone', 'from one key to the very next key, black or white', 'Level 0'], ['tone', 'two semitones', 'Level 0'], ['octave', 'from one note to the next with the same name (8 white keys, 12 semitones)', 'Level 0']], ['20%', '60%', '20%'])}
{inaction('Find G4 on the keyboard', kbx('C', 15, 28, 100, label=True, shade={7: '#fde6dd', 11: '#fde6dd'}, marks=[f'<circle cx="{(7 + i) * 28 + 14}" cy="71" r="8" fill="#fff" stroke="#26296b" stroke-width="1.8"/><text x="{(7 + i) * 28 + 14}" y="74.6" text-anchor="middle" font-family="AH,Arial" font-size="10" font-weight="700" fill="#26296b">{i + 1}</text>' for i in range(5)], scale=1.0), ['<b>Find middle C (C4):</b> the C just left of the two black keys nearest the middle.', '<b>Count up the letters</b>, one white key each: C D E F G is five keys.', '<b>Same octave</b>, so the number stays 4.'], 'The key: <b>G4</b>. One octave higher, the next G, is G5.')}
<!--SPLIT-->
{youknow('Amazing Grace, on the black keys only', '<figure class="vx kbf">' + keyboard('C', 8, 30, 92, label=True, marks=[f'<circle cx="{x * 30}" cy="40" r="8" fill="#e4572e"/>' for x in (1, 2, 4, 5, 6)], scale=1.0) + '</figure>', 'The whole tune fits on the <b class="co">five black keys</b>: D♭ G♭ B♭ G♭ B♭ A♭ G♭ E♭ D♭. The groups of two and three are a little melody machine.', 'Start on the lower key of a pair of black keys and find the tune by ear.')}
{inaction('Find F♯4', kbx('C', 8, 34, 100, label=True, shade={3: '#fde6dd', 4: '#fde6dd'}, marks=['<circle cx="136" cy="44" r="10" fill="#e4572e"/>'], scale=0.8), ['<b>Find F4:</b> the white key just left of the group of three black keys above middle C.', '<b>Sharp means up:</b> move one key to the right.', '<b>The very next key</b> is black: that is F♯.'], 'F♯4 is the <b>black key</b> just right of F4, the first of the group of three.')}
{watch(['Counting octaves from the left end of the piano: octave numbers always change at C, not A.', 'Calling every black key a sharp: each one has a flat name too (p. {{P5}}).'])}
{inaction('Find C3, C4 and C5', kbx('C', 15, 28, 100, label=True, shade={0: '#fde6dd', 7: '#fde6dd', 14: '#fde6dd'}, marks=[f'<circle cx="{i * 28 + 14}" cy="56" r="9" fill="#e4572e"/>' for i in (0, 7, 14)], scale=0.8), ['<b>Find middle C (C4):</b> just left of the two black keys in the middle.', '<b>Count seven white keys down:</b> C3.', '<b>Count seven white keys up:</b> C5.'], 'Every C sits just left of a group of <b>two</b> black keys, an octave apart.')}
{thinkt('The black keys are like the little bumps on F and J of a computer keyboard: feel them and you know where you are without looking.')}
{foot('The staff and the clefs p. {{P2}} · The staff and the keyboard p. {{P4}}', 'Workbook Pitch 1 · Online: Library › Keyboard')}""", 22)

clefs = [[gsym('𝄞', 46), '<b>treble clef</b> (G clef)', 'curls round the line for G (line 2)', 'Level 0'], [gsym('𝄢', 30), '<b>bass clef</b> (F clef)', 'its two dots sit either side of the line for F (line 4)', 'Level 0']]
P23 = ppage(f"""{head('Part I · Pitch · 2', 'The staff and the clefs', 'Music lives on a <b>staff</b> (or stave): five lines and four spaces, counted from the <b>bottom</b>. Higher on the staff means higher in sound. The <b>clef</b> at the start is the code: it says which note each line and space stands for.')}
{tbl(['Clef', 'Name', 'How it shows its note', 'First met'], clefs, ['12%', '28%', '44%', '16%'])}
<div class="ocl"><div class="ocf">{px('alto', 64, '<b>Alto clef</b>: middle C on line 3. Used by the viola.')}{px('tenor', 64, '<b>Tenor clef</b>: middle C on line 4. Cello, bassoon and trombone, up high.')}</div><p class="sm"><b>Other clefs.</b> C clefs: the line through the centre of the clef is middle C. Piano music never uses them, but pianists meet them in theory exams and when reading the viola or cello part in chamber music or a score (Level 2).</p></div>
{two(h3('The grand staff') + '<p>Piano music uses two staves joined by a brace: the treble staff, usually for the right hand, above the bass staff, usually for the left. <b>Middle C</b> sits between them on a short line of its own, and can be written in either staff.</p>', px('gs_c', 100, 'Middle C in the treble staff (left) and in the bass staff (right): the same key.'), '1fr 1fr')}
{h3('Ledger lines')}
{two(px('ledger', 80, 'Treble: A, B, C below; A, B, C above.'), px('ledger_b', 80, 'Bass: E, D, C below; C, D, E above.'))}
<p>Notes above or below the staff sit on short extra lines called <b>ledger lines</b>, spaced like the staff lines.</p>
{two(h3('Octave signs') + tbl(['Sign', 'Meaning'], [['<b>8va</b>', 'an octave higher, as far as the dotted line'], ['<b>8vb</b>', 'an octave lower'], ['<b>15ma</b>', 'two octaves higher (Level 4)'], ['<b>loco</b>', 'back where it is written']], ['26%', '74%']), '<p class="sm" style="margin-top:34px">First met: Level ½. Octave signs save writing many ledger lines: a high passage stays on the staff, with 8va above it.</p>', '1.4fr 1fr')}
<!--SPLIT-->
{inaction('Which staff does this note belong to?', kbx('C', 15, 28, 92, label=True, shade={i: ('#eef0f8' if i < 7 else '#fdeee8') for i in range(15)}, marks=['<circle cx="210" cy="54" r="10" fill="#e4572e"/>'], scale=1.0), ['<b>Below middle C</b> (blue): the bass staff, usually the left hand.', '<b>Above middle C</b> (pink): the treble staff, usually the right hand.', '<b>Middle C itself</b> (the red dot): either staff, whichever hand plays it.'], 'Low keys: <b>bass clef</b>. High keys: <b>treble clef</b>. The two staves meet at middle C.')}
{youknow('Twinkle, Twinkle, Little Star', ykfig('yk_twk', ('n3','n4','n7'), 70), 'The treble clef curls round <b class="co">line 2: G</b>, the very note Twinkle leaps up to. Middle C hangs on its own ledger line below.', 'Point to the G line, then play C C G G A A G.')}
{watch(['Reading bass-clef notes as if they were treble: check the clef on every line.', 'Thinking middle C has two keys because it can be written in two places.'])}
{thinkt('A clef is a pair of glasses: the same five lines read as different notes, depending on which pair you put on.')}
{foot('Reading the notes p. {{P3}} · The staff and the keyboard p. {{P4}}', 'Workbook Pitch 2 · Online: Library › Staff and clefs')}""", 23)

rhy = [['Treble lines', 'E G B D F', '<i>Every Good Boy Deserves Fun</i>'], ['Treble spaces', 'F A C E', 'spells <i>FACE</i>'], ['Bass lines', 'G B D F A', '<i>Great Big Dragon Flies Away</i>'], ['Bass spaces', 'A C E G', '<i>All Cows Eat Grass</i>']]
P24 = ppage(f"""{head('Part I · Pitch · 3', 'Reading the notes', 'Each line and space has one letter name. Learn them in two ways: by the patterns below, and by a few <b>landmark notes</b> you can find instantly and count from.')}
{two(px('tr_lines', 92, 'Treble clef: the lines'), px('tr_spaces', 92, 'Treble clef: the spaces'))}
{two(px('bs_lines', 92, 'Bass clef: the lines'), px('bs_spaces', 92, 'Bass clef: the spaces'))}
{tbl(['Staff', 'Notes, bottom to top', 'To remember'], rhy, ['24%', '30%', '46%'])}
{h3('Landmark notes')}
<p>Find these first. Every other note is a <b>step</b> (line to space) or a <b>skip</b> (line to line) away.</p>
<div class="lmr"><div><b>Treble clef</b><br>Middle C on its ledger line below; the G the clef curls round (line 2); the C in the third space.</div>{px('lm_t', 80)}</div>
<div class="lmr"><div><b>Bass clef</b><br>The C in the second space; the F between the clef’s dots (line 4); middle C on its ledger line above.</div>{px('lm_b', 80)}</div>
{inaction('Read a note you are not sure of', px('ia_read', 78), ['<b>The clef:</b> treble.', '<b>A landmark:</b> the G the clef curls round, on line 2.', '<b>Skip up</b> line to line, one letter jumped each time: G, B, D.'], 'The note on line 4 is <b>D</b>.')}
<!--SPLIT-->
{thinkt('Landmark notes are like lamp posts on a dark road: walk from one to the next and you are never lost.')}
{youknow('Mary Had a Little Lamb', ykfig('yk_mary', ('n1','n2','n3'), 96), 'E D C: <b class="co">line, space, ledger line</b>, one step down each time. Read the shape and the tune walks down with it.', 'Read the notes aloud before you play them.')}
{watch(['Naming bass-clef notes with treble names: in the bass, the bottom line is G, not E.', 'Counting ledger lines from the wrong end: start from the staff and count outwards.'])}
{inaction('Read a ledger-line note', px('ledger', 86), ['<b>Start at the staff edge:</b> the top line of the treble staff is F.', '<b>Step up</b> one note at a time: G (space), A (first ledger line).', '<b>Below the staff</b> count down the same way: D, C, B, A.'], 'Ledger lines are the staff carried on: count by steps from the nearest line.')}
{foot('The staff and the clefs p. {{P2}} · The staff and the keyboard p. {{P4}}', 'Workbook Pitch 2 · Online: Library › Staff and clefs')}""", 24)

P25 = ppage(f"""{head('Part I · Pitch · 4', 'The staff and the keyboard', 'Every line and space of the grand staff is one white key. Read from left to right, the notes climb the staff exactly as the keys climb the keyboard: two octaves from C3 to C5, with middle C in red where the two staves meet.')}
<figure class="vx px mapf"><div class="vs">{P['map'].replace('<svg ', '<svg style="max-height:520px" ', 1)}</div></figure>
{two(h3('What the map shows') + '<p>Each step up the staff (line to space, space to line) is the next <b>white</b> key. The black keys have no line or space of their own: they are written with a sharp or a flat on a white key’s line or space (p. {{P5}}).</p>',
     h3('Two ways to write one key') + '<p>Middle C can sit on a ledger line below the treble staff or above the bass staff. Both mean the same key; the music chooses the staff of the hand that plays it.</p>')}
<!--SPLIT-->
{inaction('From the page to the key', px('lm_b', 80), ['<b>Name the note on the staff:</b> line 4 of the bass staff, between the clef’s dots, is F.', '<b>Count down from middle C:</b> C B A G F, the fifth white key down.', '<b>Play it</b> with the left hand: that is F3.'], 'The bass-clef F is <b>F3</b>, five white keys below middle C.')}
{thinkt('The staff is a ladder laid on its side beside the keyboard: each rung, a line or a space, is the next white key.')}
{youknow('Frère Jacques, in both hands', ykfig('yk_frere', ('n5','n6','n7','n8'), 104), 'The left hand plays the <b class="co">same letters</b>, C D E C, one octave lower, written in the bass clef.', 'Play it right hand, then left hand, then both together.')}
{watch(['Thinking the black keys have their own lines: they borrow a white key’s line or space with a sharp or flat.'])}
{inaction('Landmarks either side of middle C', px('landmarks', 104), ['<b>Find middle C</b> on the map: between the two staves.', '<b>Treble G</b> is five white keys above it.', '<b>Bass F</b> is five white keys below it.'], 'The landmarks sit at the same distance either side of middle C.')}
{foot('The keyboard p. {{P1}} · Reading the notes p. {{P3}}', 'Workbook Pitch 1–2 · Online: Library › Staff and clefs')}""", 25)

acc = [[gsym('♯', 28), 'sharp', 'raises a note by a semitone', 'Level 0'], [gsym('♭', 28), 'flat', 'lowers a note by a semitone', 'Level 0'], [gsym('♮', 28), 'natural', 'cancels a sharp or flat', 'Level ½'], [gsym('𝄪', 16), 'double sharp', 'raises by two semitones', 'Level 4'], [gsym('𝄫', 28), 'double flat', 'lowers by two semitones', 'Level 4']]
P26 = ppage(f"""{head('Part I · Pitch · 5', 'Sharps, flats and naturals', 'A sharp, flat or natural in front of a note (an <b>accidental</b>) nudges it, usually by a semitone. <b>Sharp</b>: one key right, usually black. <b>Flat</b>: one key left.')}
{tbl(['Sign', 'Name', 'What it does', 'First met'], acc, ['12%', '22%', '46%', '20%'])}
{h3('Sharp till the bar line')}
{two(px('acc_bar', 90, 'The sharp still counts later in the bar; after the bar line, F is F again.'), px('acc_nat', 90, 'A natural cancels the flat for the rest of the bar.'))}
<div class="rules"><div><b>Only that line or space.</b> A sharp on the F in the first space does not change the F an octave higher.</div><div><b>A tie carries it on.</b> A note tied across the bar line keeps its accidental.</div><div><b>Reminders.</b> A courtesy accidental, sometimes in brackets, just reminds you after a bar line.</div></div>
{h3('One key, two names')}
{two('<p>Every black key has two names: the key between F and G is both <b>F♯</b> and <b>G♭</b>. Notes that sound the same but are written differently are <b>enharmonic</b>. White keys can have sharp or flat names too: <b>E♯</b> is F, <b>C♭</b> is B.</p>', kbx('C', 7, 46, 150, label=True, marks=[f'<text x="{(i + 1) * 46}" y="{y}" text-anchor="middle" font-family="AH,Arial" font-size="10.5" font-weight="700" fill="#fff">{t}</text>' for i, (s1, f1) in zip((0, 1, 3, 4, 5), (('C♯', 'D♭'), ('D♯', 'E♭'), ('F♯', 'G♭'), ('G♯', 'A♭'), ('A♯', 'B♭'))) for y, t in ((62, s1), (77, f1))], scale=1.0), '1fr 1fr')}
<p class="think"><span>Think of it</span>A key signature is the principal’s notice on the school board: it speaks to every student, every day. An accidental is a teacher stopping at one student’s desk: the message is for that note only, and it lasts until the next bar line.</p>
<!--SPLIT-->
{inaction('One key, two names', px('enh', 80), ['<b>The first bar:</b> F♯, then G♭.', '<b>Find them:</b> both are the black key between F and G.', '<b>The last bar:</b> no black key sits above E, so E♯ is the white key F.'], 'Same key, different names: these are <b>enharmonic</b> notes.')}
{youknow('Für Elise (Beethoven)', ykfig('yk_elise', ('n2','n4'), 70), 'E, <b class="co">D♯</b>, E, <b class="co">D♯</b>: a semitone down and back. The sharp is written again in the new bar, because the bar line wiped it out.', 'Play E and D♯ back and forth: the black key just left of E.')}
{watch(['Forgetting that an accidental lasts until the bar line.', 'Carrying an accidental into the next bar: after the bar line, the key signature rules again.'])}
{inaction('How long does the sharp last?', px('acc_bar', 86), ['<b>The first note:</b> F♯.', '<b>Later in the bar:</b> F is still F♯.', '<b>After the bar line:</b> F is plain F again.'], 'An accidental lasts <b>until the bar line</b>, then the key signature rules again.')}
{foot('Keys and key signatures p. {{S5}}', 'Workbook Pitch 3 · Online: Library › Signs')}""", 26)

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
def ivkb(n, cap, W=36, H=120):   # her 5 Nov: show where the interval starts and ends: both end keys red, the keys between tinted, a bracket from end to end
    WH = 'CDEFGAB'; keys = []
    for i in range(10):
        keys.append(('w', i))
        if WH[i % 7] in 'CDFGA': keys.append(('b', i))
    t, i = keys[n]; shade = {j: '#fdf1ec' for j in range(0, i + 1)}; shade[0] = '#f6c2b0'
    marks = []
    if t == 'w': shade[i] = '#f6c2b0'; xe = (i + 0.5) * W
    else:
        BW, BH = W * 0.58, H * 0.6; xe = (i + 1) * W
        marks.append(f'<rect x="{xe - BW / 2:.1f}" y="0" width="{BW:.1f}" height="{BH:.1f}" rx="1.5" fill="#e4572e"/>')
    marks += [m.replace('fill="#e4572e"', 'fill="#26296b"') if ' y="84"' in m else m.replace('fill="#e4572e"', 'fill="#fff"') for m in semis('C', n, hi=(0, n))]
    a, b = (0.5 * W - 3) / W, (xe + 3) / W - 1
    return kbx('C', 7, W, H, label=True, shade=shade, marks=marks, brackets=[(a, b, f'{n} semitones', True)], scale=1.0) + f'<p class="sm">{cap}</p>'
P27 = ppage(f"""{head('Part I · Pitch · 6', 'Counting intervals', 'How far apart are two notes? That gap is an <b>interval</b>. The very next key is a <b>semitone</b>; two make a <b>tone</b>. To number it, count the letter names, both ends included.')}
{two(px('tones', 78, 'E–F and B–C are semitones; C–D and F–G are tones.'), px('mel_harm', 78, 'Melodic: one note after the other. Harmonic: together.'))}
{h3('Counting the number')}
{ykfig('ex_iv', ('n1', 'n5', 'n7', 'n8'), 78).replace('</div></figure>', '</div><figcaption>From <b class="co">D</b> up to <b class="co">A</b> (the red notes): D E F G A is five letters, so the interval is a 5th, whether the notes come one after the other or together.</figcaption></figure>')}
{h3('Interval numbers from C')}
{px('intv', 88)}
{inaction('How far apart are these notes?', px('ia_iv', 90), ['<b>Call the first note 1:</b> F is 1.', '<b>Count every letter to the second note:</b> F G A is 3 letters: a 3rd.', '<b>Going down works the same:</b> C B A G is 4 letters: a 4th.'], 'F up to A is a <b>3rd</b>; C down to G is a <b>4th</b>. Sharps and flats never change the number.')}
<p class="sm"><b>Your hand is a ruler:</b> thumb on C, little finger on G: five fingers on five white keys, a 5th.</p>
<!--SPLIT-->
{youknow('Twinkle, Twinkle, Little Star', ykfig('yk_twk5', ('n1','n3'), 70), 'The leap from “twin-” to “kle” is C up to G: C D E F G, <b class="co">five letters, a 5th</b>.', 'Sing the first two notes of any song, then count the letters between them.')}
{inaction('Name an interval on the keyboard', kbx('C', 8, 34, 100, label=True, shade={2: '#fde6dd', 7: '#fde6dd'}, marks=[], scale=1.0), ['<b>Find both notes:</b> E and the C above it.', '<b>Count the letters:</b> E F G A B C is six.', '<b>Both ends count:</b> so the interval is a 6th.'], 'E up to C is a <b>6th</b>.')}
{watch(['Counting only the gaps, not the notes: always count both ends.', 'Letting a sharp or flat change the number: C to G♯ is still a 5th.'])}
{inaction('Melodic or harmonic?', px('mel_harm', 86), ['<b>The first bar:</b> C then E, one after the other.', '<b>The second bar:</b> C and E together.', '<b>Count both:</b> C D E, a 3rd each time.'], 'The same 3rd: <b>melodic</b> when played one after the other, <b>harmonic</b> when played together.')}
{thinkt('Monday to Wednesday is three days, not two: you count the day you start on. Intervals count the same way.')}
{foot('Major, minor and perfect p. {{S2}} · Major scales p. {{S3}}', 'Workbook Pitch 4 · Online: Library › Intervals')}""", 27)

iv = [['unison', '', '0 (perfect)', '', 'Level 1'], ['2nd', '1 (minor)', '2 (major)', '', 'Level 1'], ['3rd', '3 (minor)', '4 (major)', '', 'Level ½'], ['4th', '', '5 (perfect)', '6 (augmented)', 'Level 1'], ['5th', '6 (diminished)', '7 (perfect)', '', 'Level 1'], ['6th', '8 (minor)', '9 (major)', '', 'Level 2'], ['7th', '10 (minor)', '11 (major)', '', 'Level 2'], ['octave', '', '12 (perfect)', '', 'Level 1']]
P28 = ppage(f"""{head('Part I · Pitch · 7', 'Major, minor and perfect', 'Two intervals with the same number can differ in size. C–E and C–E♭ are both 3rds, but one is a semitone wider. The <b>quality</b> (major, minor, perfect…) comes from counting <b>semitones</b>.')}
{two(ivkb(4, 'From <b class="co">C</b> to <b class="co">E</b>: count every key, black and white. 4 semitones: a major 3rd.'), ivkb(3, 'From <b class="co">C</b> to <b class="co">E♭</b>: 3 semitones, one fewer: a minor 3rd.'))}
{px('q3', 92)}
{h3('Size in semitones')}
{tbl(['Number', 'Smaller', 'Main', 'Wider', 'First met'], iv, ['16%', '22%', '22%', '22%', '18%'])}
<div class="ladder"><div><b>2nds, 3rds, 6ths, 7ths</b><span>diminished ‹ <b>minor</b> ‹ <b>major</b> ‹ augmented</span></div><div><b>unisons, 4ths, 5ths, octaves</b><span>diminished ‹ <b>perfect</b> ‹ augmented</span></div></div>
<p class="sm">Each step on the ladder is one semitone. Six semitones (an augmented 4th or diminished 5th) is the tritone. Turned upside down, an interval’s numbers add to 9 and major and minor swap: a major 3rd becomes a minor 6th.</p>
<!--SPLIT-->
{inaction('Major or minor 3rd?', kbx('C', 8, 34, 100, label=True, shade={0: '#fde6dd'}, marks=['<circle cx="68" cy="44" r="10" fill="#e4572e"/>'], scale=1.0), ['<b>Count the letters:</b> C D E is three, so it is a 3rd.', '<b>Count the semitones:</b> C to C♯, D, E♭ is three.', '<b>Three semitones</b> make a minor 3rd; four would be major.'], 'C to E♭: a <b>minor 3rd</b>.')}
{thinkt('A major and a minor 3rd are a smile and a frown: the same face, one small change at the corners.')}
{youknow('Beethoven, Symphony No. 5', ykfig('yk_b5', ('n2','n3','n4','n5'), 96), 'Da-da-da-DUM: G down to <b class="co">E♭</b> is four semitones, a <b>major 3rd</b>. Three semitones would be minor.', 'Count the keys from G down to E♭: F♯, F, E, E♭.')}
{watch(['Counting white keys only: count every key, black and white.', 'Calling a 4th or 5th “major”: they are perfect.'])}
{inaction('Tone or semitone?', px('tones', 66), ['<b>E to F:</b> the very next key, no black key between: a semitone.', '<b>C to D:</b> one key between (C♯): a tone.', '<b>B to C</b> and <b>F to G</b>: check the same way.'], 'E–F and B–C are semitones; C–D and F–G are tones.')}
{foot('Counting intervals p. {{S1}} · Chords: Harmony (later)', 'Workbook Pitch 4 · Online: Library › Intervals')}""", 28)

forms = [['major', 'T T S T T T S', 'Level ½'], ['natural minor', 'T S T T S T T', 'Level ½'], ['harmonic minor', 'T S T T S T+S S', 'Level ½'], ['melodic minor (up)', 'T S T T T T S; down as the natural minor', 'Level 2'], ['chromatic', 'every semitone', 'Level 2'], ['pentatonic (black keys)', 'T T T+S T T+S', 'Level 0']]
deg = [['1', 'tonic'], ['2', 'supertonic'], ['3', 'mediant'], ['4', 'subdominant'], ['5', 'dominant'], ['6', 'submediant'], ['7', 'leading note']]
P29 = ppage(f"""{head('Part I · Pitch · 8', 'Major scales', 'Climb from a key note to the next one with the same name, following a fixed recipe of tones (T) and semitones (S): that is a <b>scale</b>. The recipe, not the starting note, makes it major or minor.')}
{px('c_maj', 70, 'C major: T T S T T T S. The semitones fall between 3–4 and 7–8.')}
{tbl(['Scale', 'Steps', 'First met'], forms, ['30%', '50%', '20%'])}
{two(h3('Every step has a name') + '<p class="degs">' + ' · '.join(f'<b>{a}</b> {b}' for a, b in deg) + '</p>', h3('Major or minor?') + '<p>The same key note can start a major or a minor scale: C major and C minor. The pattern decides. Major sounds bright and settled; minor, darker.</p>')}
{inaction('Build D major', px('ia_sc1', 70) + px('ia_sc2', 70), ['<b>Write the eight letters</b> from D to D, every letter once.', '<b>Check the steps</b> against T T S T T T S: E–F is too small, B–C is too small.', '<b>Raise F and C</b> a semitone to fix them.'], 'D major: <b>D E F♯ G A B C♯ D</b>, two sharps.')}
<!--SPLIT-->
{thinkt('A scale is a staircase with two short steps. Wherever you build it, the short steps sit in the same places: between 3 and 4, and between 7 and 8.')}
{youknow('Joy to the World', ykfig('yk_joy', ('n1','n2','n3','n4','n5','n6','n7','n8'), 70), 'The first line is the <b class="co">C major scale</b>, top to bottom: C B A G F E D C.', 'Play C major down from the top C and sing “Joy to the world” over it.')}
{inaction('Build F major', '', ['<b>Write the letters</b> from F to F: F G A B C D E F.', '<b>Check the steps</b> against T T S T T T S: A to B is a tone, but it must be a semitone.', '<b>Lower B</b> to B♭: now A to B♭ is a semitone and B♭ to C a tone.'], 'F major: <b>F G A B♭ C D E F</b>, one flat.')}
{watch(['Using the same letter twice: every letter appears once (F♯, not G♭, in G major).', 'Forgetting the semitone between 7 and 8: the leading note pulls up to the key note.'])}
{howto('Practise a scale', ['<b>Hands separately,</b> slowly, saying the finger numbers aloud.', '<b>Fingering for C, G, D, A and E major</b> (right hand): 1 2 3, thumb under, 1 2 3 4 5.', '<b>Listen for evenness:</b> every note the same length and loudness.', '<b>Then hands together,</b> one octave, then two.'])}
{inaction('Where are the semitones?', px('c_maj', 86), ['<b>Number the degrees</b> 1 to 8 from C.', '<b>Look for no black key between:</b> E–F and B–C.', '<b>Those are degrees 3–4 and 7–8.</b>'], 'Every major scale has its semitones between <b>3–4</b> and <b>7–8</b>.')}
{foot('Minor scales p. {{S4}} · Keys and key signatures p. {{S5}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Scales')}""", 29)

keys = [['C major', 'A minor', '—', 'Level ½'], ['G major', 'E minor', '1♯', 'Level ½'], ['D major', 'B minor', '2♯', 'Level 1'], ['A major', 'F♯ minor', '3♯', 'Level 3'], ['E major', 'C♯ minor', '4♯', 'Level 4'], ['B major', 'G♯ minor', '5♯', 'Level 4'], ['F major', 'D minor', '1♭', 'Level ½'], ['B♭ major', 'G minor', '2♭', 'Level 1'], ['E♭ major', 'C minor', '3♭', 'Level 3'], ['A♭ major', 'F minor', '4♭', 'Level 4'], ['D♭ major', 'B♭ minor', '5♭', 'Level 4']]
P29b = ppage(f"""{head('Part I · Pitch · 9', 'Minor scales', 'Every minor scale starts from the natural minor, the notes of its relative major from the 6th degree up. Two small changes give the harmonic and melodic forms, which sound stronger at the top.')}
{h3('A minor in three forms')}
{px('a_nat', 84, 'Natural: the notes of C major, from A to A. T S T T S T T.')}
{px('a_har', 84, 'Harmonic: the 7th raised a semitone (<b class="co">G♯</b>). The gap F–G♯ is a tone and a half.')}
{px('a_mel', 84, 'Melodic: the 6th and 7th raised going up (<b class="co">F♯ G♯</b>), lowered coming down (<b class="co">G♮ F♮</b>).')}
{two(h3('Relative minor') + '<p>Same key signature, three semitones below the major: C major and A minor share every note.</p>', h3('Parallel minor') + '<p>Same key note, different signature: C major (no sharps or flats) and C minor (three flats).</p>')}
<p class="think"><span>Think of it</span>The relative minor is the same clothes worn by a different person: the same notes, a new key note. The parallel minor is the same person in different clothes: the same key note, some notes changed.</p>
<!--SPLIT-->
{inaction('Build E harmonic minor', '', ['<b>Borrow G major’s notes</b> starting on E: E F♯ G A B C D E.', '<b>Raise the 7th:</b> D becomes D♯.', '<b>Check the gap</b> C to D♯: a tone and a half.'], 'E harmonic minor: <b>E F♯ G A B C D♯ E</b>.')}
{youknow('Greensleeves', ykfig('yk_green', ('n4','n7'), 70), 'A minor, with a <b class="co">G♯</b>: the raised 7th of the harmonic minor, leaning hard up to A.', 'Play it once with G♯, once with G: hear the pull disappear.')}
{inaction('Find the relative minor of F major', kbx('C', 8, 34, 100, label=True, shade={1: '#fde6dd', 3: '#fde6dd'}, marks=[], scale=1.0), ['<b>Start on F,</b> the key note.', '<b>Count three semitones down:</b> E, E♭, D.', '<b>Check the signature:</b> D minor has one flat, B♭, like F major.'], 'The relative minor of F major is <b>D minor</b>.')}
{watch(['Raising the 7th in the key signature: it is written as an accidental each time.', 'Playing the melodic minor’s raised notes on the way down.'])}
{inaction('Natural or harmonic minor?', px('a_har', 86), ['<b>Start on A</b> and read up to A.', '<b>Look at the 7th:</b> G♯, raised.', '<b>Nothing else changes</b> from the natural minor.'], 'A raised 7th only: the <b>harmonic minor</b>.')}
{foot('Major scales p. {{S3}} · Keys and key signatures p. {{S5}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Scales')}""", 30)

P30 = ppage(f"""{head('Part I · Pitch · 10', 'Keys and key signatures', 'Why write F♯ fifty times? The <b>key signature</b> at the start of each line says it once, for the whole piece. Its sharps or flats always line up in the same order.')}
{two(px('sharps', 88, 'Sharps: F C G D A E B. The key note is a semitone above the last sharp.'), px('flats', 88, 'Flats: B E A D G C F. From two flats, the second-last flat names the key.'))}
<p class="sm">To remember the order: <b>F</b>ather <b>C</b>harles <b>G</b>oes <b>D</b>own <b>A</b>nd <b>E</b>nds <b>B</b>attle; backwards for the flats: <b>B</b>attle <b>E</b>nds <b>A</b>nd <b>D</b>own <b>G</b>oes <b>C</b>harles’ <b>F</b>ather.</p>
{tbl(['Major', 'Relative minor', 'Signature', 'First met'], keys, ['28%', '28%', '20%', '24%'])}
<p class="sm">Six and seven sharps or flats (F♯, C♯, G♭, C♭ major and their minors) come at Levels 4–6.</p>
{two('<svg viewBox="0 0 300 120" style="width:100%;max-width:300px;display:block;margin:0 auto"><circle cx="78" cy="60" r="50" fill="#fff" stroke="#26296b" stroke-width="3"/><circle cx="78" cy="60" r="42" fill="none" stroke="#26296b" stroke-width="1"/><text x="78" y="56" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="#26296b">A major</text><text x="78" y="74" text-anchor="middle" font-family="AH,Arial" font-size="11" fill="#6d6f9c">front</text><circle cx="222" cy="60" r="50" fill="#fdeee8" stroke="#e4572e" stroke-width="3"/><circle cx="222" cy="60" r="42" fill="none" stroke="#e4572e" stroke-width="1"/><text x="222" y="56" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="#e4572e">F♯ minor</text><text x="222" y="74" text-anchor="middle" font-family="AH,Arial" font-size="11" fill="#6d6f9c">back</text><text x="150" y="66" text-anchor="middle" font-family="AH,Arial" font-size="22" fill="#26296b">⇄</text></svg>', h3('One signature, two keys') + '<p>Every key signature belongs to <b>one major key and one minor key</b>, like the two sides of a coin: three sharps are A major or F♯ minor. The minor is the <b>relative minor</b>, three semitones below the major.</p>', '1fr 1.3fr')}
<p class="think"><span>Think of it</span>A dress code on a party invitation: written once at the top, it applies to every guest all night. Only an accidental, a word to one guest, overrules it, and only until the bar line.</p>
<!--SPLIT-->
{inaction('Name the keys', ringks('ks_2s', -1, 92), ['<b>Count:</b> two sharps, F♯ and C♯.', '<b>The last sharp</b> is C♯; one semitone up is D.', '<b>The relative minor,</b> three semitones below D, is B.'], 'Two sharps: <b>D major</b> or <b>B minor</b>.')}
{youknow('Minuet in G', ykfig('yk_minuet2', ('n5',), 84), 'One sharp in the key signature: every F is <b class="co">F♯</b>, like the one just before the top G. That sharp is why it is in G major.', 'Find every F in the piece and play it as F♯.')}
{watch(['Writing a key signature in the wrong order: sharps always F C G D A E B.', 'Forgetting that a signature names two keys: a major and its relative minor.', 'Reading it once and forgetting it: glance at the key signature at the start of every line.'])}
{inaction('Read a flat key signature', ringks('ks_3f', -2, 92), ['<b>Count the flats:</b> three, B♭ E♭ A♭.', '<b>The second-last flat</b> is E♭: the key note.', '<b>Its relative minor,</b> three semitones down, is C minor.'], 'Three flats: <b>E♭ major</b> or <b>C minor</b>.')}
{foot('Major scales p. {{S3}} · Finding the key p. {{S6}} · The circle of fifths p. {{S7}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Keys')}""", 31)

P31 = ppage(f"""{head('Part I · Pitch · 11', 'Finding the key', 'A key signature names two keys, a major and its relative minor. Two quick rules (and one to remember) find the major; one more finds the minor; then the music itself tells you which of the two it is.')}
<div class="fk"><div class="fkf">{ringks('ks_3s', -1, 118)}</div><div><b>Sharps: the last sharp, then one semitone up.</b><br>Last sharp <b class="co">G♯</b> → up a semitone → <b>A major</b>.</div></div>
<div class="fk"><div class="fkf">{ringks('ks_3f', -2, 118)}</div><div><b>Flats: the second-last flat is the key.</b><br>B♭ <b class="co">E♭</b> A♭ → <b class="co">E♭ major</b>. One flat alone is F major.</div></div>
<div class="fk"><div class="fkf">{kbx('F', 6, 40, 120, label=True, shade={2: '#eef0f8'}, marks=[f'<text x="{x}" y="{y}" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="{c}">{t}</text>' for x, y, t, c in ((100, 100, '0', '#26296b'), (80, 62, '1', '#fff'), (60, 100, '2', '#26296b'), (40, 62, '3', '#fff'))] + ['<circle cx="40" cy="58" r="11" fill="#e4572e"/><text x="40" y="62" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="#fff">3</text>'], scale=1.0)}</div><div><b>Major to minor: three semitones down.</b><br>A, G♯, G, <b class="co">F♯</b> → <b class="co">F♯ minor</b>, the relative minor of A major (count every key, black and white).</div></div>
{inaction('What key is this tune in?', px('ex_key', 92), ['<b>The key signature:</b> one sharp, so G major or its relative, E minor.', '<b>The clue notes:</b> D♯ keeps appearing. D♯ is the raised 7th of E minor; G major has no D♯.', '<b>The last note:</b> E, the key note of E minor.'], 'The key: <b>E minor</b>. Check it the same way with any piece you play.')}
<!--SPLIT-->
{youknow('Für Elise (Beethoven)', ykfig('yk_elise2', ('n1','n9'), 70), 'No key signature, a <b class="co">G♯</b> as the clue, and the music keeps coming home to <b class="co">A</b>: <b>A minor</b>.', 'Play A, then G♯ A: hear the G♯ lean into home.')}
{h3('Minor keys and their clue notes')}
{tbl(['Minor key', 'Signature', 'Clue note (raised 7th)'], [['A minor', 'none', '<b class="co">G♯</b>'], ['E minor', '1♯', '<b class="co">D♯</b>'], ['D minor', '1♭', '<b class="co">C♯</b>'], ['B minor', '2♯', '<b class="co">A♯</b>'], ['G minor', '2♭', '<b class="co">F♯</b>']], ['34%', '28%', '38%'])}
{inaction('Major or minor? No sharps or flats', kbx('C', 8, 34, 100, label=True, shade={5: '#fde6dd'}, marks=['<circle cx="170" cy="44" r="10" fill="#e4572e"/>'], scale=1.0), ['<b>The signature:</b> none, so C major or A minor.', '<b>The clue notes:</b> G♯ appears. G♯ is the raised 7th of A minor.', '<b>The last note:</b> A.'], 'No sharps or flats, G♯ clues, ending on A: <b>A minor</b>.')}
{thinkt('Detective work: the key signature narrows it to two suspects; the clue note and the last note name the culprit.')}
{foot('Keys and key signatures p. {{S5}} · The circle of fifths p. {{S7}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Keys')}""", 32)


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
    return f'<figure class="vx cof"><svg viewBox="0 0 460 460" style="width:100%;max-width:284px;height:auto;display:block;margin:0 auto">{s}</svg></figure>'
P32 = ppage(f"""{head('Part I · Pitch · 12', 'The circle of fifths', 'All the keys on one clock face. Going round clockwise, each key is a <b>5th higher</b> than the last and has <b>one more sharp</b> (or one fewer flat). Anticlockwise, each is a 4th higher, a 5th lower, with one more flat.')}
{two(circle(), h3('How to read the clock') + '<p><b>Outer ring:</b> major keys. <b>Middle ring:</b> their relative minors (small letters). <b>Inner ring:</b> the key signature.</p>' + h3('Neighbours are close') + '<p>Keys next to each other share all but one note, so music moves between them easily: from C major to G major or F major, or to the relative minor. These are the <b>related keys</b>.</p>' , '1.1fr 1fr')}
{h3('Six jobs for one circle')}
<div class="uses"><div><b>Key signatures</b><span>Count the steps from C: clockwise for sharps, anticlockwise for flats.</span></div><div><b>Relative minors</b><span>Look straight in from any major key.</span></div><div><b>The main chords</b><span>A key’s two neighbours give its other main chords: in C, the chords of F and G.</span></div><div><b>Cadences</b><span>The strongest close, V to I, is one step anticlockwise: G to C.</span></div><div><b>Changing key</b><span>Pieces usually move one step round, or to the relative minor.</span></div><div><b>Scale practice</b><span>Go round the circle: one new sharp or flat each time.</span></div></div>
{inaction('Why do G major and D major sound so close?', '', ['<b>Find both:</b> D is one step clockwise from G.', '<b>Compare the scales:</b> G major has C; D major has C♯.', '<b>Count:</b> six notes the same, one different.'], 'Neighbours share six of their seven notes, so music moves between them easily.')}
<p class="think"><span>Think of it</span>Like a colour wheel: neighbours blend, opposites clash. C and G sit side by side; C and F♯ sit opposite.</p>
<!--SPLIT-->
{youknow('Passacaglia (Handel), the bass', ykfig('yk_pass', ('n1','n2','n3','n4','n5','n6','n7','n8'), 80), 'Each bass note is a <b class="co">5th below</b> the one before (or a 4th above): G C F B♭ E♭ A D G, one step round the circle each chord.', 'Play the bass line slowly and hear it pull towards the last G.')}
{inaction('Find A major’s key signature', '', ['<b>Start at C</b> at the top of the circle: no sharps.', '<b>Go clockwise:</b> G, D, A is three steps.', '<b>Three steps,</b> three sharps: F♯, C♯, G♯.'], 'A major has <b>three sharps</b>.')}
{h3('The first steps round the circle')}
{tbl(['Steps', 'Clockwise (sharps)', 'Anticlockwise (flats)'], [['1', 'G major: F♯', 'F major: B♭'], ['2', 'D major: F♯ C♯', 'B♭ major: B♭ E♭'], ['3', 'A major: F♯ C♯ G♯', 'E♭ major: B♭ E♭ A♭']], ['16%', '42%', '42%'])}
{watch(['Going the wrong way round: clockwise adds sharps, anticlockwise adds flats.', 'Forgetting the relative minors on the middle ring.'])}
{h3('C major’s neighbours')}
{tbl(['Key', 'Where on the circle', 'Why it matters'], [['G major', 'one step clockwise', 'the dominant: the strongest pull home'], ['F major', 'one step anticlockwise', 'the subdominant: a gentle move away'], ['A minor', 'straight in from C', 'the relative minor: the same notes'], ['E minor, D minor', 'in from G and F', 'the relatives of the neighbours']], ['24%', '32%', '44%'])}
{foot('Keys and key signatures p. {{S5}} · Finding the key p. {{S6}} · Chords: Harmony (later)', 'Workbook Pitch 5 · Online: Scale finder, Library › Related keys')}""", 33)

css += '''
.degs{font-size:14px;line-height:1.7} .tq{border:0;padding:0;margin:6px 0} .sixf .vs svg text{font-family:'AH',Arial} .sixf{border:0} .six{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin:8px 0 10px} .six>div{border:1.5px solid #26296b;border-radius:6px;padding:10px 12px;display:flex;flex-direction:column;gap:4px;font-size:14px;line-height:1.45} .six b{font-family:'PF',serif;font-size:22px;color:#e4572e} .six i{font-style:normal;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#6d6f9c;margin-top:auto;padding-top:4px;border-top:1px solid #e2ddd0} .uses{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin:4px 0 6px} .uses>div{border:1px solid #e2ddd0;border-top:3px solid #26296b;padding:7px 9px;font-size:13px;line-height:1.4;display:flex;flex-direction:column;gap:2px} .uses b{font-size:13.5px} .co{color:#e4572e} .ocl{display:grid;grid-template-columns:1.3fr 1fr;gap:16px;align-items:center;margin:6px 0} .ocf{display:grid;grid-template-columns:1fr 1fr;gap:8px} .ocf .vx{margin:0} .think{display:flex;gap:10px;align-items:baseline;font-size:14px;margin:8px 0;color:#3d4080} .think span{flex:none;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#2e8a6e} .fk{display:grid;grid-template-columns:1fr 1.25fr;gap:18px;align-items:center;border-bottom:1px solid #e2ddd0;padding:8px 0;font-size:14.5px;line-height:1.5} .fk .vx{margin:0} .inact{border:1.5px solid #e4572e;border-radius:4px;padding:9px 14px 10px;margin:10px 0;background:#fff} .inact .bh{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e} .inact .it{font-size:16px;display:block;margin:2px 0 4px} .inact .vx{border:0;margin:0;padding:4px 0} .inact .px text{fill:#e4572e !important} .isteps{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;font-size:13.5px;line-height:1.45;margin-top:6px} .isteps>div{display:flex;gap:8px} .in{flex:none;width:22px;height:22px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;font-size:12.5px;display:flex;align-items:center;justify-content:center} .ires{margin-top:10px;padding-top:8px;border-top:1px solid #f0d8cf;font-size:15px} .tip{border-left:3px solid #e4572e;background:#fdf6f2;padding:10px 16px 12px;margin:16px 0 0} .tip .bh{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e} .tip .tt{display:block;font-size:16px;margin:2px 0 6px} .tip table{background:transparent} .tip td,.tip th{white-space:nowrap} .tw td,.tw th{white-space:normal !important;vertical-align:top} .howto{border-left:3px solid #e4572e;background:#fdf6f2;padding:8px 14px;margin:12px 0;font-size:14px} .howto .bh{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e} .howto b{font-size:15px} .howto ol{margin:4px 0 0;padding-left:20px} .howto li{margin:2px 0} .rules{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;font-size:13.5px;line-height:1.45;margin:8px 0 6px} .ladder{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:10px 0 4px;font-size:14px} .ladder div{display:flex;flex-direction:column;border:1px solid #e2ddd0;padding:8px 10px} .ladder span{color:#4a4d86} .mapf .vs svg{max-width:100%} .kbl{font-family:'AH',Arial} .lmr{display:grid;grid-template-columns:1fr 1.25fr;gap:18px;align-items:center;margin:8px 0} .lmr>div:first-child{font-size:14.5px;line-height:1.55} .lmr .vx{margin:0}
.px .vs svg{width:100%;height:auto} .px text{font-family:'AH',Arial !important;fill:#26296b !important;font-weight:700} .px text.hl{fill:#e4572e !important} .kbf{display:flex;justify-content:center}
'''
import re as _re
PAGES = (P22, P23, P24, P25, P26, P27, P28, P29, P29b, P30, P31, P32)
# her 5 Nov (A): four parts. Part I Pitch keeps topics 1-5 (pp. 22-31, tips p. 32); topics 6-12 become Part III Scales and keys (pp. 50-63, tips p. 64)
_KEYS = ['P1', 'P2', 'P3', 'P4', 'P5', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7']
_remap = lambda t: t
def _scales(t):   # Part III wording for topics 6-12
    t = _re.sub(r'Part I · Pitch · (\d+)', lambda m: f'Part III · Scales and keys · {int(m.group(1)) - 5}', t)
    t = t.replace('PART I · PITCH', 'PART III · SCALES AND KEYS').replace('Workbook Pitch 4', 'Workbook Scales and keys 1').replace('Workbook Pitch 5', 'Workbook Scales and keys 2')
    return t.replace('Chords: Harmony (later)', f'Chords in a key p. {PM.PAGE["H3"]}').replace('Online: Scale finder, Library', 'Online: Library')
_P1 = ''.join(assemble(k, pg) for k, pg in zip(_KEYS[:5], PAGES[:5]))
_P3 = _scales(''.join(assemble(k, pg) for k, pg in zip(_KEYS[5:], PAGES[5:])))

# ---------- Part I ends with its own tips page ----------
PT1 = ppage(f"""{head('Part I · Pitch · Tips', 'When a note reads wrong', 'Most misread notes come from a handful of slips. Name the slip first, then fix only that note: playing the whole line again rarely finds it.')}
<div class="tip tw"><div class="bh">Tip</div><b class="tt">What you notice, what to check</b>
{tbl(['What you notice', 'Check', 'Turn to'], [['The left hand reads like the right', '<b class="co">the clef</b>: bass lines are G B D F A, not E G B D F', 'p. {{P2}}'], ['You land an octave too high or too low', '<b class="co">a landmark</b>: middle C, treble G or bass F', 'p. {{P3}}'], ['Notes above or below the staff slow you down', '<b class="co">the ledger lines</b>: count them from the nearest landmark', 'p. {{P3}}'], ['A sharp or flat vanishes, or stays too long', '<b class="co">the bar line</b>: an accidental lasts only to the end of its bar', 'p. {{P5}}'], ['You play the black key on the wrong side', '<b class="co">the direction</b>: a sharp goes right (up), a flat goes left (down)', 'p. {{P5}}']], ['38%', '46%', '16%'])}
</div>
{inaction('Same key, two names', kbx('C', 8, 34, 100, label=True, shade={3: '#fde6dd', 4: '#fde6dd'}, marks=['<circle cx="136" cy="44" r="10" fill="#e4572e"/>'], scale=1.0), ['<b>From F, go one key right:</b> the red black key is <b>F♯</b>.', '<b>From G, go one key left:</b> you reach the same red key, <b>G♭</b>.', '<b>One key, two names:</b> the music decides which name it uses.'], 'If F♯ and G♭ both look odd, check the key: the name follows the notes around it, the key stays the same.')}
{howto('Three checks before you read a new line', ['<b>The clefs:</b> which staff is treble, which is bass?', '<b>The landmarks:</b> find middle C, treble G and bass F, and read the other notes from them.', '<b>The accidentals:</b> mark each sharp, flat or natural, and see where its bar ends.'])}
{thinkt('Like reading a map: find the big landmarks first, then the streets around them. A note far from any landmark is the one most often misread.')}""", PM.PAGE['PT'])

def _slip():
    svg = ringsvg(P['slip'], 0).replace('<g id="n7" class="note">', '<g id="n7" class="note" style="fill:#e4572e;color:#e4572e">', 1)
    return '<figure class="vx px"><div class="vs">' + svg.replace('<svg ', '<svg style="max-height:96px" ', 1) + '</div></figure>'
PT = ppage(f"""{head('Part III · Scales and keys · Tips', 'When a note sounds wrong', 'You read the note right, yet it sounds sour. The slip is usually in the key, not the note. Name the slip first, then fix only that note.')}
<div class="tip tw"><div class="bh">Tip</div><b class="tt">What you notice, what to check</b>
{tbl(['What you notice', 'Check', 'Turn to'], [['A note sounds sour, though you read it right', '<b class="co">the key signature</b>: is this note sharp or flat all the way through?', 'p. {{S5}}'], ['Two notes sound too close or too far apart', '<b class="co">the interval</b>: count the letters, then the keys between', 'p. {{S1}}'], ['A minor tune sounds wrong near the end', '<b class="co">the raised 7th</b>: harmonic and melodic minor sharpen it', 'p. {{S4}}'], ['A scale sounds wrong in the middle', '<b class="co">the semitone steps</b>: 3–4 and 7–8 in every major scale', 'p. {{S3}}'], ['A sharp is missing from the key signature', '<b class="co">the order of sharps</b>: F C G D A E B', 'p. {{S5}}'], ['You are not sure which major key it is', '<b class="co">the last sharp</b>: the key is one note above it', 'p. {{S6}}']], ['38%', '46%', '16%'])}
</div>
{inaction('Find the slip', _slip(), ['<b>Read the key signature:</b> one sharp, on the top line, F (ringed).', '<b>The red note sits on that line</b>, so the sharp belongs to it too.', '<b>No natural cancels it</b>, so this F is F♯, here and all through the piece.'], 'Play <b>F♯</b>, the black key. Plain F is the most common slip in G major.')}
{howto('Three checks before you play', ['<b>The key signature:</b> say its sharps or flats aloud.', '<b>The key:</b> name it from the last sharp or the last-but-one flat, then check the last note.', '<b>The scale:</b> play it once, so your fingers know which black keys belong.'])}
{thinkt('Like proofreading: a spelling mistake jumps out once you know which words you usually get wrong. Keep a short list of your own slips, and check those first.')}""", PM.PAGE['ST'])
PT = _scales(PT)

_q = "'" * 3
_flowjs = src10[src10.index('FLOWJS = ' + _q) + 12:src10.index('</script>' + _q) + 9]
def _opener(kick, title, line, boxes, toc):
    fl = ''.join(f'<div class="fl"><b>{a}</b><span>{b}</span></div>' + ('<span class="fa">›</span>' if i < len(boxes) - 1 else '') for i, (a, b) in enumerate(boxes))
    return f"""<section class="pg part2"><div class="pframe"><div class="pk">{kick}</div><div class="pt">{title}</div><div class="pdv"></div>
<p class="pl">{line}</p>
<div class="flow">{fl}</div>
<div class="pin"><div class="pih">In this part</div>{''.join(f'<div class="tr"><span>{x}</span><span class="dots"></span><span>{p}</span></div>' for x, p in toc)}</div></div></section>"""
OPEN2 = _opener('Part I · Which note', 'Pitch', 'High or low? That is the first question every note answers. Start with the keys under your fingers, then find where they live on the staff and how sharps and flats move them.',
    [('Keyboard', 'high and low, the patterns'), ('Staff', 'lines, spaces and clefs'), ('Reading the notes', 'every note on the staff'), ('Sharps and flats', 'the black keys')],
    [(t, PM.PAGE[k]) for t, k in (('The keyboard', 'P1'), ('The staff and the clefs', 'P2'), ('Reading the notes', 'P3'), ('The staff and the keyboard', 'P4'), ('Sharps, flats and naturals', 'P5'), ('Tips: when a note reads wrong', 'PT'))])
OPEN3 = _opener('Part III · The ground under the chords', 'Scales and keys', 'Notes travel in families. Measure the distance between two notes, build the scales that whole pieces are made from, then learn to read the key a piece lives in.',
    [('Intervals', 'the distance between notes'), ('Scales', 'major and minor'), ('Keys', 'signatures and the circle')],
    [(t, PM.PAGE[k]) for t, k in (('Counting intervals', 'S1'), ('Major, minor and perfect', 'S2'), ('Major scales', 'S3'), ('Minor scales', 'S4'), ('Keys and key signatures', 'S5'), ('Finding the key', 'S6'), ('The circle of fifths', 'S7'), ('Tips: when a note sounds wrong', 'ST'))])
def _write(name, body):
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}</style></head><body>{body}{_flowjs}</body></html>'
    open('/mnt/user-data/outputs/house-rooms/' + name, 'w').write(html)
_write('handbook-pitch.html', OPEN2 + _remap(_P1) + PT1)
_write('handbook-scales.html', OPEN3 + _remap(_P3) + PT)
print('ok')
