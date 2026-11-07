# The Piano Butler Handbook, Part I: Pitch
import json, sys
src10 = open('/tmp/claude-0/pk/book10.py').read()
exec(src10.split("flow = ''.join(")[0])
css = eval("f'''" + src10[src10.index("css = f'''") + 10:src10.index("'''\nhtml =")] + "'''")
sys.path.insert(0, '/tmp/claude-0/pk')
from kb import keyboard, black_groups
P = {k: _ledger(v) for k, v in json.load(open('/tmp/claude-0/vrv/pout.json')).items()}
def pxh(k, ids, h):   # a big staff picture with chosen notes in red (chapter heroes)
    s = P[k].replace('<svg ', '<svg style="max-height:%dpx;width:auto;max-width:100%%" ' % h, 1)
    for n in ids: s = s.replace(f'<g id="{n}" class="note">', f'<g id="{n}" class="note" style="fill:#e4572e;color:#e4572e">', 1)
    s = _re2.sub(r'(<g id="[^"]*" class="keySig")', r'\1 style="fill:#e4572e;color:#e4572e"', s, count=1)
    return '<div class="vs hs">' + s.replace('font-family="Times,serif"', 'font-family="AH,Arial" font-weight="700"') + '</div>'
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
{hero(keyboard('C', 15, 44, 192, brackets=[(a, b, ('2 black keys' if k == 2 else '3 black keys'), True) for a, b, k in g14], label=True, shade={i: ('#fbd0c2' if i % 7 == 0 else ('#fdeee8' if i % 7 < 3 else '#eef0f8')) for i in range(15)}, marks=[f'<circle cx="{i * 44 + 22}" cy="152" r="13" fill="#e4572e"/>' for i in (0, 7, 14)], scale=1.0), 'Every C sits just left of the two black keys')}
{two(h3('The white keys') + '<p>Seven letters, <b>A B C D E F G</b>, then the letters start again, like the days of the week. <b>C D E</b> sit around each group of two black keys (C just left of it), <b>F G A B</b> around each group of three (F just left of it): the two tints on the picture.</p>',
     h3('Middle C and octaves') + '<p><b>Middle C</b> is the C nearest the middle of the keyboard. From one C to the next is an <b>octave</b>: eight white keys, counting both. Octaves are numbered from the bottom: middle C is <b>C4</b>, the C below it C3, the C above C5; every key up to the next B shares the number (D4, E4 … B4).</p>')}
{tbl(['Term', 'Meaning', 'First met'], [['pitch', 'how high or low a sound is', 'Level 0'], ['register', 'a part of the keyboard: low, middle or high', 'Level 0'], ['semitone', 'from one key to the very next key, black or white', 'Level 0'], ['tone', 'two semitones', 'Level 0'], ['octave', 'from one note to the next with the same name (8 white keys, 12 semitones)', 'Level 0']], ['20%', '60%', '20%'])}
{inaction('Find G4 on the keyboard', kbx('C', 15, 28, 100, label=True, shade={7: '#fde6dd', 11: '#fde6dd'}, marks=[f'<circle cx="{(7 + i) * 28 + 14}" cy="71" r="8" fill="#fff" stroke="#26296b" stroke-width="1.8"/><text x="{(7 + i) * 28 + 14}" y="74.6" text-anchor="middle" font-family="AH,Arial" font-size="10" font-weight="700" fill="#26296b">{i + 1}</text>' for i in range(5)], scale=1.0), ['<b>Find middle C (C4):</b> the C just left of the two black keys nearest the middle.', '<b>Count up the letters</b>, one white key each: C D E F G is five keys.', '<b>Same octave</b>, so the number stays 4.'], 'The key: <b>G4</b>. One octave higher, the next G, is G5.')}
<!--SPLIT-->
{youknow('Amazing Grace, on the black keys only', '<figure class="vx kbf">' + keyboard('C', 8, 30, 92, label=True, marks=[f'<circle cx="{x * 30}" cy="40" r="8" fill="#e4572e"/>' for x in (1, 2, 4, 5, 6)], scale=1.0) + '</figure>', 'The whole tune fits on the <b class="co">five black keys</b>: D♭ G♭ B♭ G♭ B♭ A♭ G♭ E♭ D♭. The groups of two and three are a little melody machine.', 'Start on the lower key of a pair of black keys and find the tune by ear.')}
{inaction('Find F♯4', kbx('C', 8, 34, 100, label=True, shade={3: '#fde6dd', 4: '#fde6dd'}, marks=['<circle cx="136" cy="44" r="10" fill="#e4572e"/>'], scale=0.8), ['<b>Find F4:</b> the white key just left of the group of three black keys above middle C.', '<b>Sharp means up:</b> move one key to the right.', '<b>The very next key</b> is black: that is F♯.'], 'F♯4 is the <b>black key</b> just right of F4, the first of the group of three.')}
{watch(['Calling every black key a sharp: each one has a flat name too (p. {{P5}}).'])}
{inaction('Find C3, C4 and C5', kbx('C', 15, 28, 100, label=True, shade={0: '#fde6dd', 7: '#fde6dd', 14: '#fde6dd'}, marks=[f'<circle cx="{i * 28 + 14}" cy="56" r="9" fill="#e4572e"/>' for i in (0, 7, 14)], scale=0.8), ['<b>Find middle C (C4):</b> just left of the two black keys in the middle.', '<b>Count seven white keys down:</b> C3.', '<b>Count seven white keys up:</b> C5.'], 'Every C sits just left of a group of <b>two</b> black keys, an octave apart.')}
{thinkt('The black keys are like the little bumps on F and J of a computer keyboard: feel them and you know where you are without looking.')}
{game('Name the key', '<div class="gm4" style="grid-template-columns:repeat(3,1fr)">' + ''.join(f'<div>{kbx("C", 8, 22, 64, label=False, marks=[f"<circle cx=\"{x}\" cy=\"{y}\" r=\"7\" fill=\"#e4572e\"/>"], scale=1.0)}<b>{n}</b></div>' for n, x, y in (('1', 22 * 2.5, 50), ('2', 22 * 6, 26), ('3', 22 * 4.5, 50))) + '</div>', 'Each keyboard starts on C. Use the groups of black keys to name the red key.', '1 E (right of the two) · 2 the black key between A and B: A♯ or B♭ · 3 G (in the group of three).')}
{try10(kbx('C', 8, 24, 70, label=True, shade={0: '#fde6dd', 7: '#fde6dd'}, scale=1.0), 'Play every C on the piano.', 'Start at the bottom and work up, saying “C” each time: left of the two black keys, every time. Then every F: left of the three.')}
{inaction('Find B♭3', kbx('F', 8, 34, 100, label=True, shade={3: '#fde6dd'}, marks=['<circle cx="102" cy="44" r="10" fill="#e4572e"/>'], scale=1.0), ['<b>Find middle C (C4)</b>, then the white key just below it: <b>B3</b>.', '<b>Flat means down:</b> one key to the left.', '<b>The very next key</b> is black: the top key of the group of three.'], 'B♭3 is the <b>top black key</b> of the group of three just below middle C.')}
{foot('The staff and the clefs p. {{P2}} · The staff and the keyboard p. {{P4}}', 'Workbook Pitch 1 · Online: Library › Keyboard')}""", 22)

clefs = [[gsym('𝄞', 46), '<b>treble clef</b> (G clef)', 'curls round the line for G (line 2)', 'Level 0'], [gsym('𝄢', 30), '<b>bass clef</b> (F clef)', 'its two dots sit either side of the line for F (line 4)', 'Level 0']]
P23 = ppage(f"""{head('Part I · Pitch · 2', 'The staff and the clefs', 'Music lives on a <b>staff</b> (or stave): five lines and four spaces, counted from the <b>bottom</b>. Higher on the staff means higher in sound. The <b>clef</b> at the start is the code: it says which note each line and space stands for.')}
{hero(pxh('hero_clef', ('n2', 'n5'), 190), 'The treble clef curls round G · the bass clef’s dots hug F')}
{tbl(['Clef', 'Name', 'How it shows its note', 'First met'], clefs, ['12%', '28%', '44%', '16%'])}
<div class="ocl"><div class="ocf">{px('alto', 64, '<b>Alto clef</b>: middle C on line 3. Used by the viola.')}{px('tenor', 64, '<b>Tenor clef</b>: middle C on line 4. Cello, bassoon and trombone, up high.')}</div><p class="sm"><b>Other clefs.</b> C clefs: the line through the centre of the clef is middle C. Piano music never uses them, but pianists meet them in theory exams and when reading the viola or cello part in chamber music or a score (Level 2).</p></div>
{two(h3('The grand staff') + '<p>Piano music uses two staves joined by a brace: the treble staff, usually for the right hand, above the bass staff, usually for the left. <b>Middle C</b> sits between them on a short line of its own, and can be written in either staff.</p>', px('gs_c', 100, 'Middle C in the treble staff (left) and in the bass staff (right): the same key.'), '1fr 1fr')}
{h3('Ledger lines')}
{two(px('ledger', 80, 'Treble: A, B, C below; A, B, C above.'), px('ledger_b', 80, 'Bass: E, D, C below; C, D, E above.'))}
<p>Notes above or below the staff sit on short extra lines called <b>ledger lines</b>, spaced like the staff lines.</p>
{two(h3('Octave signs') + tbl(['Sign', 'Meaning'], [['<b>8va</b>', 'an octave higher, as far as the dotted line'], ['<b>8vb</b>', 'an octave lower'], ['<b>loco</b>', 'back where it is written']], ['26%', '74%']), '<p class="sm" style="margin-top:34px">First met: Level ½. Octave signs save writing many ledger lines: a high passage stays on the staff, with 8va above it.</p>', '1.4fr 1fr')}
<!--SPLIT-->
{inaction('Which staff does this note belong to?', kbx('C', 15, 28, 92, label=True, shade={i: ('#eef0f8' if i < 7 else '#fdeee8') for i in range(15)}, marks=['<circle cx="210" cy="54" r="10" fill="#e4572e"/>'], scale=1.0), ['<b>Below middle C</b> (blue): the bass staff, usually the left hand.', '<b>Above middle C</b> (pink): the treble staff, usually the right hand.', '<b>Middle C itself</b> (the red dot): either staff, whichever hand plays it.'], 'Low keys: <b>bass clef</b>. High keys: <b>treble clef</b>. The two staves meet at middle C.')}
{youknow('Twinkle, Twinkle, Little Star', ykfig('yk_twk', ('n3','n4','n7'), 70), 'The treble clef curls round <b class="co">line 2: G</b>, the very note Twinkle leaps up to. Middle C hangs on its own ledger line below.', 'Point to the G line, then play C C G G A A G.')}
{watch(['Reading bass-clef notes as if they were treble: check the clef on every line.'])}
{thinkt('A clef is a pair of glasses: the same five lines read as different notes, depending on which pair you put on.')}
{game('Treble or bass?', qitems(['a note two keys above middle C', 'the lowest key on the piano', 'middle C', 'a high, high note'], 4), 'Which staff would each note be written on?', '1 treble · 2 bass · 3 either: it sits between the two · 4 treble, with ledger lines or 8va.')}
{try10(px('gs_c', 70), 'Point, then play.', 'Point to the line the treble clef curls round and play that G. Point to the line between the bass clef’s dots and play that F. Middle C sits between them.')}
{inaction('Read a high note on ledger lines', ykfig('ex_hi', ('n5',), 96), ['<b>The top line</b> of the treble staff is F.', '<b>Step up:</b> G sits on top of the staff, A on the first ledger line.', '<b>Keep stepping:</b> B above it, C on the second ledger line.'], 'Two ledger lines above the treble staff: <b>C6</b>, two octaves above middle C.')}
{inaction('One line, two notes', '<div style="display:flex;justify-content:center;gap:24px">' + ykfig('tr_lines', ('n1',), 56) + ykfig('bs_lines', ('n1',), 56) + '</div>', ['<b>Treble clef:</b> the bottom line is E.', '<b>Bass clef:</b> the same bottom line is G.', '<b>Same line, new note:</b> the clef decides.'], 'Always read the <b>clef</b> first: it tells you what every line means.')}
{foot('Reading the notes p. {{P3}} · The staff and the keyboard p. {{P4}}', 'Workbook Pitch 2 · Online: Library › Staff and clefs')}""", 23)

rhy = [['Treble lines', 'E G B D F', '<i>Every Good Boy Deserves Fun</i>'], ['Treble spaces', 'F A C E', 'spells <i>FACE</i>'], ['Bass lines', 'G B D F A', '<i>Great Big Dragon Flies Away</i>'], ['Bass spaces', 'A C E G', '<i>All Cows Eat Grass</i>']]
P24 = ppage(f"""{head('Part I · Pitch · 3', 'Reading the notes', 'Each line and space has one letter name. Learn them in two ways: by the patterns below, and by a few <b>landmark notes</b> you can find instantly and count from.')}
{hero(pxh('hero_lm', ('n3', 'n6', 'n9'), 210), 'Find a landmark, then count')}
<p>Find the three red <b>landmark notes</b> first: bass F, middle C, treble G. Every other note is a <b>step</b> (line to space) or a <b>skip</b> (line to line) away from one of them.</p>
{two(px('tr_lines', 92, 'Treble clef: the lines'), px('tr_spaces', 92, 'Treble clef: the spaces'))}
{two(px('bs_lines', 92, 'Bass clef: the lines'), px('bs_spaces', 92, 'Bass clef: the spaces'))}
{tbl(['Staff', 'Notes, bottom to top', 'To remember'], rhy, ['24%', '30%', '46%'])}
{inaction('Read a note you are not sure of', px('ia_read', 78), ['<b>The clef:</b> treble.', '<b>A landmark:</b> the G the clef curls round, on line 2.', '<b>Skip up</b> line to line, one letter jumped each time: G, B, D.'], 'The note on line 4 is <b>D</b>.')}
<!--SPLIT-->
{thinkt('Landmark notes are like lamp posts on a dark road: walk from one to the next and you are never lost.')}
{youknow('Mary Had a Little Lamb', ykfig('yk_mary', ('n1','n2','n3'), 96), 'E D C: <b class="co">line, space, ledger line</b>, one step down each time. Read the shape and the tune walks down with it.', 'Read the notes aloud before you play them.')}
{watch(['Naming bass-clef notes with treble names: in the bass, the bottom line is G, not E.', 'Counting ledger lines from the wrong end: start from the staff and count outwards.'])}
{game('Fill the gap', qitems(['E G _ D F', 'F A _ E', 'G B D _ A', 'A C E _'], 4), 'Treble lines, treble spaces, bass lines, bass spaces: one letter is missing from each.', '1 B · 2 C · 3 F · 4 G.')}
{try10(px('tr_lines', 64), 'Say the treble lines up and down.', '“E G B D F”, then “F D B G E”, out loud, as fast as you can without a slip. Then the spaces: “F A C E”.')}
{inaction('Read a ledger-line note', px('ledger', 86), ['<b>Start at the staff edge:</b> the top line of the treble staff is F.', '<b>Step up</b> one note at a time: G (space), A (first ledger line).', '<b>Below the staff</b> count down the same way: D, C, B, A.'], 'Ledger lines are the staff carried on: count by steps from the nearest line.')}
{inaction('Read a bass-clef note from F', ykfig('ex_bf', ('n3',), 84), ['<b>The bass clef’s dots</b> sit either side of line 4: that line is F.', '<b>Step down</b> to the space below: E.', '<b>One more step</b> to line 3: D.'], 'Bass line 3 is <b>D</b>: two steps down from the clef’s F.')}
{inaction('Read a treble space note', px('tr_spaces', 80), ['<b>Start from the clef’s G</b> on line 2.', '<b>Step up</b> to the space above it: A.', '<b>Skip up</b> to the next space: C.'], 'Space 3 of the treble staff is <b>C</b>: one of the landmark notes.')}
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
{game('How many white keys?', qitems(['middle C up to A', 'middle C down to E', 'G up to the next G'], 3), 'Count both ends. The staff climbs the same way: one line or space per white key.', '1 six (C D E F G A) · 2 six (C B A G F E) · 3 eight: an octave.')}
{try10(kbx('C', 8, 24, 70, label=True, shade={0: '#fde6dd', 7: '#fde6dd'}, scale=1.0), 'Play middle C, then walk up.', 'Say each white key as you play it, C D E F G A B C, and picture each one climbing the staff: line, space, line, space.')}
{inaction('Landmarks either side of middle C', px('landmarks', 98), ['<b>Find middle C</b> on the map: between the two staves.', '<b>Treble G</b> is five white keys above it.', '<b>Bass F</b> is five white keys below it.'], 'The landmarks sit at the same distance either side of middle C.')}
{inaction('From the key to the page', kbx('C', 8, 34, 84, label=True, shade={0: '#eef0f8', 2: '#fde6dd'}, marks=['<circle cx="85" cy="52" r="10" fill="#e4572e"/>'], scale=1.0), ['<b>The key:</b> E, two white keys above middle C.', '<b>On the staff,</b> step up from middle C: D in the space below the staff, E on the bottom line.', '<b>So the note sits</b> on the treble’s bottom line.'], 'E4 is the <b>bottom line</b> of the treble staff.')}
{inaction('Where the two staves meet', kbx('A', 6, 34, 72, label=True, shade={1: '#fde6dd', 2: '#fde6dd', 3: '#fde6dd'}, scale=1.0), ['<b>The bass staff’s top line</b> is A3.', '<b>The treble staff’s bottom line</b> is E4.', '<b>The keys between,</b> B3 C4 D4, sit just outside each staff (C4 on its own ledger line).'], 'B, C and D in the middle can be written in <b>either staff</b>: the hand that plays them chooses.')}
{foot('The keyboard p. {{P1}} · Reading the notes p. {{P3}}', 'Workbook Pitch 1–2 · Online: Library › Staff and clefs')}""", 25)

acc = [[gsym('♯', 28), 'sharp', 'raises a note by a semitone', 'Level 0'], [gsym('♭', 28), 'flat', 'lowers a note by a semitone', 'Level 0'], [gsym('♮', 28), 'natural', 'cancels a sharp or flat', 'Level ½'], [gsym('𝄪', 16), 'double sharp', 'raises by two semitones', 'Level 4'], [gsym('𝄫', 28), 'double flat', 'lowers by two semitones', 'Level 4']]
P26 = ppage(f"""{head('Part I · Pitch · 5', 'Sharps, flats and naturals', 'A sharp, flat or natural in front of a note (an <b>accidental</b>) nudges it, usually by a semitone. <b>Sharp</b>: one key right, usually black. <b>Flat</b>: one key left.')}
{hero(keyboard('C', 5, 64, 190, label=True, shade={1: '#eef0f8'}, marks=[f'<circle cx="{1.5 * 64}" cy="150" r="13" fill="#fff" stroke="#26296b" stroke-width="2.4"/>', f'<circle cx="{2 * 64}" cy="72" r="13" fill="#e4572e"/>', f'<circle cx="{1 * 64}" cy="72" r="13" fill="#e4572e"/>', f'<text x="{2 * 64}" y="40" text-anchor="middle" font-family="AH,Arial" font-size="17" font-weight="700" fill="#fff">D♯</text>', f'<text x="{1 * 64}" y="40" text-anchor="middle" font-family="AH,Arial" font-size="17" font-weight="700" fill="#fff">D♭</text>', f'<path d="M{1.5 * 64 + 8},132 Q{1.75 * 64},100 {2 * 64 - 4},90" fill="none" stroke="#e4572e" stroke-width="3.5" stroke-linecap="round" marker-end="url(#ah)"/>', f'<path d="M{1.5 * 64 - 8},132 Q{1.25 * 64},100 {1 * 64 + 4},90" fill="none" stroke="#e4572e" stroke-width="3.5" stroke-linecap="round" marker-end="url(#ah)"/>', '<defs><marker id="ah" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#e4572e"/></marker></defs>'], scale=1.0), '♯ one key right · ♭ one key left')}
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
{game('Which key is it?', qitems(['C♯', 'E♭', 'B♯', 'F♭'], 4), 'Sharp: one key to the right. Flat: one key to the left. Which key do you press?', '1 the black key right of C · 2 the black key left of E · 3 the white key C · 4 the white key E.')}
{try10(kbx('C', 8, 24, 70, label=True, shade={1: '#fde6dd'}, scale=1.0), 'Play D, D♯, D♭.', 'D, then one key right (the black key), then one key left of D (another black key). Say the names as you play.')}
{inaction('How long does the sharp last?', px('acc_bar', 86), ['<b>The first note:</b> F♯.', '<b>Later in the bar:</b> F is still F♯.', '<b>After the bar line:</b> F is plain F again.'], 'An accidental lasts <b>until the bar line</b>, then the key signature rules again.')}
{inaction('A natural cancels the flat', px('acc_nat', 84), ['<b>B</b>: the white key.', '<b>B♭</b>: one key to the left, and it stays flat for the rest of the bar.', '<b>B♮</b>: the natural cancels the flat, back to the white key.'], 'A natural <b>cancels</b> a sharp or flat until the bar line.')}
{foot('Keys and key signatures p. {{S3}}', 'Workbook Pitch 3 · Online: Library › Signs')}""", 26)


# ---------- her 6 Nov: one big picture opens each Scales chapter ----------
def _num(cx, cy, t, red):
    return f'<circle cx="{cx}" cy="{cy}" r="14" fill="{"#e4572e" if red else "#fff"}" stroke="{"#e4572e" if red else "#26296b"}" stroke-width="2.2"/><text x="{cx}" y="{cy + 5.5}" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="{"#fff" if red else "#26296b"}">{t}</text>'
def hero_third():   # C to E on the keyboard: count the letters 1 2 3
    W = 60
    marks = [_num(i * W + W / 2, 128, i + 1, i in (0, 2)) for i in range(3)]
    marks.append(f'<path d="M{W / 2},96 Q{1.5 * W},70 {2.5 * W},96" fill="none" stroke="#e4572e" stroke-width="3" stroke-dasharray="6 5"/>')
    return keyboard('C', 7, W, 170, label=True, shade={0: '#fbd0c2', 1: '#fdeee8', 2: '#fbd0c2'}, marks=marks, scale=1.0)
def hero_stairs():   # C major as a staircase: tones are wide steps, the two semitones narrow and red
    steps = 'TTSTTTS'; x, y, o = 20, 226, ''
    names = 'C D E F G A B C'.split()
    for i in range(8):
        w = 70
        o += f'<rect x="{x}" y="{y}" width="{w}" height="{290 - y}" fill="#eef0f8" stroke="#26296b" stroke-width="2"/>' + (f'<rect x="{x}" y="{y - 4}" width="{w}" height="9" fill="#e4572e"/>' if i and steps[i - 1] == 'S' else '') + f'<text x="{x + w / 2}" y="{y + 26}" text-anchor="middle" font-family="PF,serif" font-size="22" font-weight="700" fill="#26296b">{names[i]}</text>'
        if i < 7:
            s = steps[i] == 'S'; dy = 13 if s else 28
            o += f'<text x="{x + w + w / 2}" y="{y - dy - 12}" text-anchor="middle" font-family="AH,Arial" font-size="17" font-weight="700" fill="{"#e4572e" if s else "#6d6f9c"}">{"S" if s else "T"}</text>'
            y -= dy
        x += w
    return f'<svg viewBox="0 0 {x + 20} 296" style="width:100%;max-width:640px">{o}</svg>'
def hero_minor():   # A to A on the white keys, then the 7th raised: G♯
    W = 56
    marks = [_num(i * W + W / 2, 140, i + 1, i in (0, 7)) for i in range(8)]
    marks.append(f'<circle cx="{7 * W}" cy="66" r="13" fill="#e4572e"/><text x="{7 * W}" y="36" text-anchor="middle" font-family="AH,Arial" font-size="16" font-weight="700" fill="#fff">G♯</text>')
    marks.append(f'<path d="M{6.5 * W},122 Q{6.6 * W},92 {7 * W - 10},78" fill="none" stroke="#e4572e" stroke-width="3.5" stroke-linecap="round"/><path d="M{7 * W - 21},80 L{7 * W - 9},77 L{7 * W - 14},89" fill="none" stroke="#e4572e" stroke-width="3" stroke-linecap="round"/>')
    return keyboard('A', 8, W, 180, label=True, shade={6: '#fdeee8'}, marks=marks, scale=1.0)
def hero_findkey():   # three sharps: the last one is G♯; one key up is A
    W = 64
    marks = [f'<circle cx="{3 * W}" cy="66" r="14" fill="#e4572e"/>', f'<text x="{3 * W}" y="34" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="#fff">G♯</text>',
             _num(3.5 * W, 132, 'A', True), f'<path d="M{3 * W + 8},84 Q{3.3 * W},104 {3.5 * W - 4},114" fill="none" stroke="#e4572e" stroke-width="3.5" stroke-linecap="round"/>']
    kb = keyboard('E', 5, W, 170, label=True, shade={3: '#fbd0c2'}, marks=marks, scale=1.0)
    return f'<div style="display:flex;align-items:center;justify-content:center;gap:26px;flex-wrap:wrap"><div style="text-align:center">{ringks("ks_3s", -1, 150)}<div class="hl">last sharp: G♯</div></div><svg viewBox="0 0 40 30" style="width:40px"><path d="M4,15 L32,15 M24,7 L33,15 L24,23" fill="none" stroke="#e4572e" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg><div style="width:330px">{kb}</div></div>'
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
{hero(hero_third(), 'C to E: count the letters, 1 2 3, a 3rd')}
{two(px('tones', 78, 'E–F and B–C are semitones; C–D and F–G are tones.'), px('mel_harm', 78, 'Melodic: one note after the other. Harmonic: together.'))}
{h3('Counting the number')}
{ykfig('ex_iv', ('n1', 'n5', 'n7', 'n8'), 78).replace('</div></figure>', '</div><figcaption>From <b class="co">D</b> up to <b class="co">A</b> (the red notes): D E F G A is five letters, so the interval is a 5th, whether the notes come one after the other or together.</figcaption></figure>')}
{h3('Interval numbers from C')}
{px('intv', 88)}
{inaction('How far apart are these notes?', px('ia_iv', 90), ['<b>Call the first note 1:</b> F is 1.', '<b>Count every letter to the second note:</b> F G A is 3 letters: a 3rd.', '<b>Going down works the same:</b> C B A G is 4 letters: a 4th.'], 'F up to A is a <b>3rd</b>; C down to G is a <b>4th</b>. Sharps and flats never change the number.')}
<p class="sm"><b>Your hand is a ruler:</b> thumb on C, little finger on G: five fingers on five white keys, a 5th.</p>
<!--SPLIT-->
{youknow('Twinkle, Twinkle, Little Star', ykfig('yk_twk5', ('n1','n3'), 70), 'The leap from the first “twinkle” to the second is C up to G: C D E F G, <b class="co">five letters, a 5th</b>.', 'Sing the first two notes of any song, then count the letters between them.')}
{inaction('Name an interval on the keyboard', kbx('C', 8, 34, 100, label=True, shade={2: '#fde6dd', 7: '#fde6dd'}, marks=[], scale=1.0), ['<b>Find both notes:</b> E and the C above it.', '<b>Count the letters:</b> E F G A B C is six.', '<b>Both ends count:</b> so the interval is a 6th.'], 'E up to C is a <b>6th</b>.')}
{watch(['Counting only the gaps, not the notes: always count both ends.', 'Letting a sharp or flat change the number: C to G♯ is still a 5th.'])}
{inaction('Melodic or harmonic?', px('mel_harm', 86), ['<b>The first bar:</b> C then E, one after the other.', '<b>The second bar:</b> C and E together.', '<b>Count both:</b> C D E, a 3rd each time.'], 'The same 3rd: <b>melodic</b> when played one after the other, <b>harmonic</b> when played together.')}
{thinkt('Monday to Wednesday is three days, not two: you count the day you start on. Intervals count the same way.')}
{game('Count the letters', qitems(['C up to G', 'D up to F', 'E up to the next E', 'G up to A'], 4), 'Count every letter, both ends included. What is each interval called?', '1 a 5th (C D E F G) · 2 a 3rd · 3 an octave (8) · 4 a 2nd.')}
{try10(kbx('C', 8, 24, 70, label=True, shade={0: '#fde6dd', 4: '#fde6dd'}, scale=1.0), 'Thumb on C, finger 5 on G.', 'Your hand is a ruler: thumb to little finger on white keys is a 5th. Play it, then thumb to finger 3: a 3rd.')}
{inaction('Count an interval going down', kbx('C', 8, 34, 100, label=True, shade={0: '#fde6dd', 5: '#fde6dd'}, scale=1.0), ['<b>Start on the top note:</b> A is 1.', '<b>Count every letter down</b> to C: A G F E D C.', '<b>Six letters:</b> a 6th.'], 'A down to C is a <b>6th</b>, the same as C up to A.')}
{foot('Major, minor and perfect p. {{P7}} · Major scales p. {{S1}}', 'Workbook Pitch 4 · Online: Library › Intervals')}""", 27)

iv = [['unison', '', '0 (perfect)', '', 'Level 1'], ['2nd', '1 (minor)', '2 (major)', '', 'Level 1'], ['3rd', '3 (minor)', '4 (major)', '', 'Level ½'], ['4th', '', '5 (perfect)', '6 (augmented)', 'Level 1'], ['5th', '6 (diminished)', '7 (perfect)', '', 'Level 1'], ['6th', '8 (minor)', '9 (major)', '', 'Level 2'], ['7th', '10 (minor)', '11 (major)', '', 'Level 2'], ['octave', '', '12 (perfect)', '', 'Level 1']]
P28 = ppage(f"""{head('Part I · Pitch · 7', 'Major, minor and perfect', 'Two intervals with the same number can differ in size. C–E and C–E♭ are both 3rds, but one is a semitone wider. The <b>quality</b> (major, minor, perfect…) comes from counting <b>semitones</b>.')}
{hero(two(ivkb(4, 'From <b class="co">C</b> to <b class="co">E</b>: count every key, black and white. 4 semitones: a major 3rd.'), ivkb(3, 'From <b class="co">C</b> to <b class="co">E♭</b>: 3 semitones, one fewer: a minor 3rd.')), 'One semitone less: a major 3rd becomes minor')}
{h3('Size in semitones')}
{tbl(['Number', 'Smaller', 'Main', 'Wider', 'First met'], iv, ['16%', '22%', '22%', '22%', '18%'])}
<div class="ladder"><div><b>2nds, 3rds, 6ths, 7ths</b><span>diminished ‹ <b>minor</b> ‹ <b>major</b> ‹ augmented</span></div><div><b>unisons, 4ths, 5ths, octaves</b><span>diminished ‹ <b>perfect</b> ‹ augmented</span></div></div>
<p class="sm">Each step on the ladder is one semitone. Six semitones (an augmented 4th or diminished 5th) is the tritone. Turned upside down, an interval’s numbers add to 9 and major and minor swap: a major 3rd becomes a minor 6th.</p>
<!--SPLIT-->
{inaction('Major or minor 3rd?', kbx('C', 8, 34, 100, label=True, shade={0: '#fde6dd'}, marks=['<circle cx="68" cy="44" r="10" fill="#e4572e"/>'], scale=1.0), ['<b>Count the letters:</b> C D E is three, so it is a 3rd.', '<b>Count the semitones:</b> C to C♯, D, E♭ is three.', '<b>Three semitones</b> make a minor 3rd; four would be major.'], 'C to E♭: a <b>minor 3rd</b>.')}
{thinkt('A major and a minor 3rd are a smile and a frown: the same face, one small change at the corners.')}
{youknow('Beethoven, Symphony No. 5', ykfig('yk_b5', ('n2','n3','n4','n5'), 96), 'Da-da-da-DUM: G down to <b class="co">E♭</b> is four semitones, a <b>major 3rd</b>. Three semitones would be minor.', 'Count the keys from G down to E♭: F♯, F, E, E♭.')}
{watch(['Counting white keys only: count every key, black and white.', 'Calling a 4th or 5th “major”: they are perfect.'])}
{game('Perfect, major or minor?', qitems(['C–G', 'D–F', 'C–A', 'E–A'], 4), 'Count the letters for the number, then the semitones for the size.', '1 perfect 5th (7) · 2 minor 3rd (3) · 3 major 6th (9) · 4 perfect 4th (5).')}
{try10(kbx('C', 8, 24, 70, label=True, shade={0: '#fde6dd', 2: '#fde6dd'}, scale=1.0), 'Play C–E, then C–E♭.', 'Bright, then dark. One key makes the difference: the major 3rd has four semitones, the minor 3rd three.')}
{inaction('Tone or semitone?', px('tones', 66), ['<b>E to F:</b> the very next key, no black key between: a semitone.', '<b>C to D:</b> one key between (C♯): a tone.', '<b>B to C</b> and <b>F to G</b>: check the same way.'], 'E–F and B–C are semitones; C–D and F–G are tones.')}
{inaction('Name D up to A', kbx('C', 8, 34, 100, label=True, shade={1: '#fde6dd', 5: '#fde6dd'}, scale=1.0), ['<b>The number:</b> D E F G A, five letters, a 5th.', '<b>The size:</b> count every key from D to A, black and white: 7 semitones.', '<b>7 semitones</b> is the main size of a 5th: perfect.'], 'D up to A is a <b>perfect 5th</b>.')}
{inaction('Name E up to C', kbx('C', 8, 34, 100, label=True, shade={2: '#fde6dd', 7: '#fde6dd'}, scale=1.0), ['<b>The number:</b> E F G A B C, six letters, a 6th.', '<b>The size:</b> 8 semitones from E to C.', '<b>A major 6th</b> has 9, so 8 is one smaller: minor.'], 'E up to C is a <b>minor 6th</b>.')}
{foot('Counting intervals p. {{P6}} · Chords: Harmony (later)', 'Workbook Pitch 4 · Online: Library › Intervals')}""", 28)

forms = [['major', 'T T S T T T S', 'Level ½'], ['natural minor', 'T S T T S T T', 'Level ½'], ['harmonic minor', 'T S T T S T+S S', 'Level ½'], ['melodic minor (up)', 'T S T T T T S; down as the natural minor', 'Level 2'], ['chromatic', 'every semitone', 'Level 2'], ['pentatonic (black keys)', 'T T T+S T T+S', 'Level 0']]
deg = [['1', 'tonic'], ['2', 'supertonic'], ['3', 'mediant'], ['4', 'subdominant'], ['5', 'dominant'], ['6', 'submediant'], ['7', 'leading note']]
P29 = ppage(f"""{head('Part I · Pitch · 8', 'Major scales', 'Climb from a key note to the next one with the same name, following a fixed recipe of tones (T) and semitones (S): that is a <b>scale</b>. The recipe, not the starting note, makes it major or minor.')}
{hero(hero_stairs(), 'Tone, tone, semitone, tone, tone, tone, semitone: the two short steps are 3–4 and 7–8')}
{tbl(['Scale', 'Steps', 'First met'], forms, ['30%', '50%', '20%'])}
{two(h3('Every step has a name') + '<p class="degs">' + ' · '.join(f'<b>{a}</b> {b}' for a, b in deg) + '</p>', h3('Major or minor?') + '<p>The same key note can start a major or a minor scale: C major and C minor. The pattern decides. Major sounds bright and settled; minor, darker.</p>')}
<!--SPLIT-->
{inaction('Build D major', px('ia_sc1', 70) + px('ia_sc2', 70), ['<b>Write the eight letters</b> from D to D, every letter once.', '<b>Check the steps</b> against T T S T T T S: E–F is too small, B–C is too small.', '<b>Raise F and C</b> a semitone to fix them.'], 'D major: <b>D E F♯ G A B C♯ D</b>, two sharps.')}
{thinkt('A scale is a staircase with two short steps. Wherever you build it, the short steps sit in the same places: between 3 and 4, and between 7 and 8.')}
{youknow('Joy to the World', ykfig('yk_joy', ('n1','n2','n3','n4','n5','n6','n7','n8'), 70), 'The first line is the <b class="co">C major scale</b>, top to bottom: C B A G F E D C.', 'Play C major down from the top C and sing “Joy to the world” over it.')}
{inaction('Build F major', '', ['<b>Write the letters</b> from F to F: F G A B C D E F.', '<b>Check the steps</b> against T T S T T T S: A to B is a tone, but it must be a semitone.', '<b>Lower B</b> to B♭: now A to B♭ is a semitone and B♭ to C a tone.'], 'F major: <b>F G A B♭ C D E F</b>, one flat.')}
{watch(['Using the same letter twice: every letter appears once (F♯, not G♭, in G major).', 'Forgetting the semitone between 7 and 8: the leading note pulls up to the key note.'])}
{howto('Practise a scale', ['<b>Hands separately,</b> slowly, saying the finger numbers aloud.', '<b>Fingering for C, G, D, A and E major</b> (right hand): 1 2 3, thumb under, 1 2 3 4 5.', '<b>Listen for evenness:</b> every note the same length and loudness.', '<b>Then hands together,</b> one octave, then two.'])}
{game('Spot the wrong note', qitems(['G A B C D E F G', 'D E F♯ G A B C D', 'F G A B C D E F'], 3), 'Each major scale has one note that breaks the T T S T T T S pattern. Which, and what should it be?', '1 F should be F♯ · 2 C should be C♯ · 3 B should be B♭.')}
{try10(kbx('C', 8, 24, 70, label=True, shade={2: '#fde6dd', 3: '#fde6dd', 6: '#fde6dd', 7: '#fde6dd'}, scale=1.0), 'One finger, C to C.', 'Play the white keys from C up to C and say “tone, tone, semitone, tone, tone, tone, semitone” as you go. Feel the two short steps.')}
{inaction('Where are the semitones?', px('c_maj', 86), ['<b>Number the degrees</b> 1 to 8 from C.', '<b>Look for no black key between:</b> E–F and B–C.', '<b>Those are degrees 3–4 and 7–8.</b>'], 'Every major scale has its semitones between <b>3–4</b> and <b>7–8</b>.')}
{foot('Minor scales p. {{S2}} · Keys and key signatures p. {{S3}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Scales')}""", 29)

keys = [['C major', 'A minor', '—', 'Level ½'], ['G major', 'E minor', '1♯', 'Level ½'], ['D major', 'B minor', '2♯', 'Level 1'], ['A major', 'F♯ minor', '3♯', 'Level 3'], ['E major', 'C♯ minor', '4♯', 'Level 4'], ['B major', 'G♯ minor', '5♯', 'Level 4'], ['F major', 'D minor', '1♭', 'Level ½'], ['B♭ major', 'G minor', '2♭', 'Level 1'], ['E♭ major', 'C minor', '3♭', 'Level 3'], ['A♭ major', 'F minor', '4♭', 'Level 4'], ['D♭ major', 'B♭ minor', '5♭', 'Level 4']]
P29b = ppage(f"""{head('Part I · Pitch · 9', 'Minor scales', 'Every minor scale starts from the natural minor, the notes of its relative major from the 6th degree up. Two small changes give the harmonic and melodic forms, which sound stronger at the top.')}
{hero(hero_minor(), 'From A on the white keys · then raise the 7th: G♯')}
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
{game('Which minor?', qitems(['nothing raised', 'the 7th raised', '6th and 7th raised going up, lowered coming down'], 3), 'Three forms of the minor scale. Name each one.', '1 natural · 2 harmonic · 3 melodic.')}
{try10(kbx('A', 8, 24, 70, label=True, shade={6: '#fde6dd'}, scale=1.0), 'A to A on the white keys.', 'That is A natural minor: dark from the first note. Play it again with G♯ instead of G: harmonic minor, and the top pulls home.')}
{inaction('Natural or harmonic minor?', px('a_har', 86), ['<b>Start on A</b> and read up to A.', '<b>Look at the 7th:</b> G♯, raised.', '<b>Nothing else changes</b> from the natural minor.'], 'A raised 7th only: the <b>harmonic minor</b>.')}
{inaction('Build D natural minor', kbx('D', 8, 34, 100, label=True, marks=['<circle cx="170" cy="44" r="10" fill="#e4572e"/>'], scale=1.0), ['<b>Find its relative major:</b> three semitones up from D is F.', '<b>F major has one flat:</b> B♭.', '<b>Play F major’s notes from D to D:</b> D E F G A B♭ C D.'], 'D natural minor: <b>D E F G A B♭ C D</b>, with the same key signature as F major.')}
{foot('Major scales p. {{S1}} · Keys and key signatures p. {{S3}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Scales')}""", 30)

P30 = ppage(f"""{head('Part I · Pitch · 10', 'Keys and key signatures', 'Why write F♯ fifty times? The <b>key signature</b> at the start of each line says it once, for the whole piece. Its sharps or flats always line up in the same order.')}
{hero(pxh('hero_ks', ('n1', 'n4', 'n6'), 150), 'One sharp at the start: every F plays F♯')}
{two(px('sharps', 88, 'Sharps: F C G D A E B. The key note is a semitone above the last sharp.'), px('flats', 88, 'Flats: B E A D G C F. From two flats, the second-last flat names the key.'))}
<p class="sm">To remember the order: <b>F</b>ather <b>C</b>harles <b>G</b>oes <b>D</b>own <b>A</b>nd <b>E</b>nds <b>B</b>attle; backwards for the flats: <b>B</b>attle <b>E</b>nds <b>A</b>nd <b>D</b>own <b>G</b>oes <b>C</b>harles’ <b>F</b>ather.</p>
{tbl(['Major', 'Relative minor', 'Signature', 'First met'], keys, ['28%', '28%', '20%', '24%'])}
<p class="sm">Six and seven sharps or flats (F♯, C♯, G♭, C♭ major and their minors) come at Levels 4–6.</p>
{two('<svg viewBox="0 0 300 120" style="width:100%;max-width:300px;display:block;margin:0 auto"><circle cx="78" cy="60" r="50" fill="#fff" stroke="#26296b" stroke-width="3"/><circle cx="78" cy="60" r="42" fill="none" stroke="#26296b" stroke-width="1"/><text x="78" y="56" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="#26296b">A major</text><text x="78" y="74" text-anchor="middle" font-family="AH,Arial" font-size="11" fill="#6d6f9c">front</text><circle cx="222" cy="60" r="50" fill="#fdeee8" stroke="#e4572e" stroke-width="3"/><circle cx="222" cy="60" r="42" fill="none" stroke="#e4572e" stroke-width="1"/><text x="222" y="56" text-anchor="middle" font-family="AH,Arial" font-size="15" font-weight="700" fill="#e4572e">F♯ minor</text><text x="222" y="74" text-anchor="middle" font-family="AH,Arial" font-size="11" fill="#6d6f9c">back</text><text x="150" y="66" text-anchor="middle" font-family="AH,Arial" font-size="22" fill="#26296b">⇄</text></svg>', h3('One signature, two keys') + '<p>Every key signature belongs to <b>one major key and one minor key</b>, like the two sides of a coin: three sharps are A major or F♯ minor. The minor is the <b>relative minor</b>, three semitones below the major.</p>', '1fr 1.3fr')}
<p class="think"><span>Think of it</span>A dress code on a party invitation: written once at the top, it applies to every guest all night. Only an accidental, a word to one guest, overrules it, and only until the bar line.</p>
<!--SPLIT-->
{inaction('Name the keys', ringks('ks_2s', -1, 84), ['<b>Count:</b> two sharps, F♯ and C♯.', '<b>The last sharp</b> is C♯; one semitone up is D.', '<b>The relative minor,</b> three semitones below D, is B.'], 'Two sharps: <b>D major</b> or <b>B minor</b>.')}
{youknow('Minuet in G', ykfig('yk_minuet2', ('n5',), 84), 'One sharp in the key signature: every F is <b class="co">F♯</b>, like the one just before the top G. That sharp is why it is in G major.', 'Find every F in the piece and play it as F♯.')}
{watch(['Writing a key signature in the wrong order: sharps always F C G D A E B.', 'Forgetting that a signature names two keys: a major and its relative minor.', 'Reading it once and forgetting it: glance at the key signature at the start of every line.'])}
{game('How many sharps or flats?', qitems(['G major', 'D major', 'A major', 'F major'], 4), 'Use the table on p. {{S3}}: how many sharps or flats does each key have?', '1 one sharp · 2 two · 3 three · 4 one flat.')}
{try10(px('sharps', 60), 'Say the sharps in order.', '“Father Charles Goes Down And Ends Battle”: F C G D A E B. Then backwards for the flats: B E A D G C F.')}
{inaction('Read a flat key signature', ringks('ks_3f', -2, 84), ['<b>Count the flats:</b> three, B♭ E♭ A♭.', '<b>The second-last flat</b> is E♭: the key note.', '<b>Its relative minor,</b> three semitones down, is C minor.'], 'Three flats: <b>E♭ major</b> or <b>C minor</b>.')}
{inaction('Read four sharps', px('ks_4s', 64), ['<b>Name the sharps:</b> F♯ C♯ G♯ D♯.', '<b>The last sharp is D♯;</b> one key up is E.', '<b>Two keys share it:</b> E major, and its relative minor, C♯ minor.'], 'Four sharps: <b>E major</b> or <b>C♯ minor</b>.')}
{howto('Write a key signature', ['<b>Sharps</b> always come in the same order, F C G D A E B, each on its own line or space.', '<b>Flats</b> come in the reverse order, B E A D G C F.', '<b>Write it again</b> at the start of every line, in both staves.'])}
{foot('Major scales p. {{S1}} · Finding the key p. {{S4}} · The circle of fifths p. {{S5}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Keys')}""", 31)

P31 = ppage(f"""{head('Part I · Pitch · 11', 'Finding the key', 'A key signature names two keys, a major and its relative minor. Two quick rules (and one to remember) find the major; one more finds the minor; then the music itself tells you which of the two it is.')}
{hero(hero_findkey(), 'Last sharp, one key up: A major')}
<div class="fk"><div class="fkf">{ringks('ks_3f', -2, 118)}</div><div><b>Flats: the second-last flat is the key.</b><br>B♭ <b class="co">E♭</b> A♭ → <b class="co">E♭ major</b>. One flat alone is F major.</div></div>
<div class="fk"><div class="fkf">{kbx('F', 6, 40, 120, label=True, shade={2: '#eef0f8'}, marks=[f'<text x="{x}" y="{y}" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="{c}">{t}</text>' for x, y, t, c in ((100, 100, '0', '#26296b'), (80, 62, '1', '#fff'), (60, 100, '2', '#26296b'), (40, 62, '3', '#fff'))] + ['<circle cx="40" cy="58" r="11" fill="#e4572e"/><text x="40" y="62" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="#fff">3</text>'], scale=1.0)}</div><div><b>Major to minor: three semitones down.</b><br>A, G♯, G, <b class="co">F♯</b> → <b class="co">F♯ minor</b>, the relative minor of A major (count every key, black and white).</div></div>
{inaction('What key is this tune in?', px('ex_key', 92), ['<b>The key signature:</b> one sharp, so G major or its relative, E minor.', '<b>The clue notes:</b> D♯ keeps appearing. D♯ is the raised 7th of E minor; G major has no D♯.', '<b>The last note:</b> E, the key note of E minor.'], 'The key: <b>E minor</b>. Check it the same way with any piece you play.')}
<!--SPLIT-->
{youknow('Für Elise (Beethoven)', ykfig('yk_elise2', ('n1','n9'), 70), 'No key signature, a <b class="co">G♯</b> as the clue, and the music keeps coming home to <b class="co">A</b>: <b>A minor</b>.', 'Play A, then G♯ A: hear the G♯ lean into home.')}
{h3('Minor keys and their clue notes')}
{tbl(['Minor key', 'Signature', 'Clue note (raised 7th)'], [['A minor', 'none', '<b class="co">G♯</b>'], ['E minor', '1♯', '<b class="co">D♯</b>'], ['D minor', '1♭', '<b class="co">C♯</b>'], ['B minor', '2♯', '<b class="co">A♯</b>'], ['G minor', '2♭', '<b class="co">F♯</b>']], ['34%', '28%', '38%'])}
{inaction('Major or minor? No sharps or flats', kbx('C', 8, 34, 100, label=True, shade={5: '#fde6dd'}, marks=['<circle cx="170" cy="44" r="10" fill="#e4572e"/>'], scale=1.0), ['<b>The signature:</b> none, so C major or A minor.', '<b>The clue notes:</b> G♯ appears. G♯ is the raised 7th of A minor.', '<b>The last note:</b> A.'], 'No sharps or flats, G♯ clues, ending on A: <b>A minor</b>.')}
{thinkt('Detective work: the key signature narrows it to two suspects; the clue note and the last note name the culprit.')}
{game('Name the major key', qitems(['2 sharps', '4 sharps', '1 flat', '3 flats'], 4), 'Sharps: the last sharp, one key up. Flats: the second-last flat is the key (one flat alone is F).', '1 D · 2 E · 3 F · 4 E♭.')}
{try10(px('ks_3s', 64), 'Three sharps, stop, step up.', 'Say “F C G”, stop: the last one is G♯. One key up is A. Three sharps is A major. Try it with two and four.')}
{inaction('Read two flats', px('ks_2f', 64), ['<b>Name the flats:</b> B♭ and E♭.', '<b>The second-last flat</b> is B♭.', '<b>Its relative minor</b> is three semitones below: G.'], 'Two flats: <b>B♭ major</b> or <b>G minor</b>.')}
{howto('Find the key of a new piece', ['<b>The key signature:</b> name the major key and its relative minor.', '<b>The clue notes:</b> look for the minor key’s raised 7th.', '<b>The last bass note:</b> pieces nearly always end on the key note.'])}
{inaction('Find a minor key from its clue', px('ks_2f', 64), ['<b>Two flats:</b> B♭ major or G minor.', '<b>G minor’s 7th note is F;</b> raised, it becomes F♯.', '<b>F♯s</b> through the piece and an ending on G mean G minor.'], 'Two flats plus F♯s: <b>G minor</b>.')}
{foot('Keys and key signatures p. {{S3}} · The circle of fifths p. {{S5}}', 'Workbook Pitch 5 · Online: Scale finder, Library › Keys')}""", 32)


def circle():
    import math
    MAJ = ['C', 'G', 'D', 'A', 'E', 'B/C♭', 'F♯/G♭', 'C♯/D♭', 'A♭', 'E♭', 'B♭', 'F']; MIN = ['a', 'e', 'b', 'f♯', 'c♯', 'g♯/a♭', 'd♯/e♭', 'a♯/b♭', 'f', 'c', 'g', 'd']   # her 6 Nov: the 7♯ and 7♭ keys show too
    SIG = ['', '1♯', '2♯', '3♯', '4♯', '5♯/7♭', '6♯/6♭', '7♯/5♭', '4♭', '3♭', '2♭', '1♭']
    cx, cy, R1, R2, R3 = 230, 230, 200, 140, 95; s = f'<circle cx="{cx}" cy="{cy}" r="{R1 + 20}" fill="#fff" stroke="#26296b" stroke-width="2"/><circle cx="{cx}" cy="{cy}" r="{R2 + 26}" fill="none" stroke="#c9cbe0" stroke-width="1.2"/><circle cx="{cx}" cy="{cy}" r="{R3 + 22}" fill="none" stroke="#c9cbe0" stroke-width="1.2"/>'
    for i in range(12):
        a = math.radians(i * 30 - 90); c, sn = math.cos(a), math.sin(a)
        s += f'<line x1="{cx + c * (R3 + 22)}" y1="{cy + sn * (R3 + 22)}" x2="{cx + c * (R1 + 20)}" y2="{cy + sn * (R1 + 20)}" stroke="#e8e4f2" stroke-width="1"/>' if False else ''
        s += f'<text x="{cx + c * R1}" y="{cy + sn * R1 + 7}" text-anchor="middle" font-family="AH,Arial" font-size="{15 if "/" in MAJ[i] else 21}" font-weight="700" fill="{"#e4572e" if i == 0 else "#26296b"}">{MAJ[i]}</text>'
        s += f'<text x="{cx + c * R2}" y="{cy + sn * R2 + 6}" text-anchor="middle" font-family="AH,Arial" font-size="{13 if "/" in MIN[i] else 16}" font-weight="700" fill="#6d6f9c">{MIN[i]}</text>'
        s += f'<text x="{cx + c * R3}" y="{cy + sn * R3 + 5}" text-anchor="middle" font-family="AH,Arial" font-size="12" fill="#6d6f9c">{SIG[i]}</text>'
    s += f'<text x="{cx}" y="{cy - 4}" text-anchor="middle" font-family="AH,Arial" font-size="11" font-weight="700" letter-spacing="1.5" fill="#6d6f9c">MAJOR</text><text x="{cx}" y="{cy + 12}" text-anchor="middle" font-family="AH,Arial" font-size="11" letter-spacing="1.5" fill="#6d6f9c">minor · signature</text>'
    return f'<figure class="vx cof"><svg viewBox="0 0 460 460" style="width:100%;max-width:284px;height:auto;display:block;margin:0 auto">{s}</svg></figure>'
def circle_hero():   # her 6 Nov (A): the two-band wheel, as in the app's Scale finder. Majors outside, minors inside; sharp keys warm, flat keys cool
    import math
    NV, CO, C = '#26296b', '#e4572e', 200
    MJ = ['C', 'G', 'D', 'A', 'E', 'B/C♭', 'F♯/G♭', 'C♯/D♭', 'A♭', 'E♭', 'B♭', 'F']
    MN = ['Am', 'Em', 'Bm', 'F♯m', 'C♯m', 'G♯m/A♭m', 'D♯m/E♭m', 'A♯m/B♭m', 'Fm', 'Cm', 'Gm', 'Dm']
    SG = ['', '1♯', '2♯', '3♯', '4♯', '5♯/7♭', '6♯/6♭', '7♯/5♭', '4♭', '3♭', '2♭', '1♭']
    pol = lambda r, i: (C + r * math.cos(math.radians(-90 + i * 30)), C + r * math.sin(math.radians(-90 + i * 30)))
    def wedge(r0, r1, i, fill, stroke, sw):
        a0, a1 = math.radians(-90 + i * 30 - 15), math.radians(-90 + i * 30 + 15); q = lambda r, a: f'{C + r * math.cos(a):.1f},{C + r * math.sin(a):.1f}'
        return f'<path d="M{q(r1, a0)} A{r1},{r1} 0 0 1 {q(r1, a1)} L{q(r0, a1)} A{r0},{r0} 0 0 0 {q(r0, a0)} Z" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    def tx(x, y, t, fs, fill, fam, cols=None):
        if '/' in t:
            a, b = t.split('/'); c1, c2 = cols or (fill, fill)
            return tx(x, y - fs * .42, a, fs * .7, c1, fam) + tx(x, y + fs * .48, b, fs * .7, c2, fam)
        return f'<text x="{x:.1f}" y="{y + fs * .35:.1f}" text-anchor="middle" font-family="{fam}" font-size="{fs}" font-weight="700" fill="{fill}">{t}</text>'
    s = ''
    for i in range(12):
        base = '#f4f1e8' if i in (0, 6) else '#fbe3da' if i < 6 else '#e6e7f3'
        s += wedge(118, 182, i, NV if i == 0 else base, '#fff', 3) + wedge(68, 118, i, CO if i == 0 else '#fff', '#efe9dc', 2)
        x, y = pol(150, i); s += tx(x, y, MJ[i], 24, '#fff' if i == 0 else NV, 'PF,serif')
        x, y = pol(93, i); s += tx(x, y, MN[i], 14, '#fff' if i == 0 else NV, 'AH,Arial')
        if SG[i]:
            x, y = pol(204, i); s += tx(x, y, SG[i], 14, CO if i < 6 else NV, 'AH,Arial', (CO, NV))
    s += f'<circle cx="{C}" cy="{C}" r="66" fill="#fff"/>' + tx(C, C - 14, 'C', 36, NV, 'PF,serif') + tx(C, C + 14, 'MAJOR', 10, '#7c7ea8', 'AH,Arial') + tx(C, C + 32, 'A minor inside', 11, CO, 'AH,Arial')
    a0, a1, R = math.radians(-84), math.radians(-64), 226
    s += f'<path d="M{C + R * math.cos(a0):.1f},{C + R * math.sin(a0):.1f} A{R},{R} 0 0 1 {C + R * math.cos(a1):.1f},{C + R * math.sin(a1):.1f}" fill="none" stroke="{CO}" stroke-width="5" stroke-linecap="round"/>'
    hx, hy = C + R * math.cos(a1), C + R * math.sin(a1)
    s += f'<path d="M{hx - 13:.1f},{hy - 7:.1f} L{hx + 2:.1f},{hy + 2:.1f} L{hx - 7:.1f},{hy + 14:.1f}" fill="none" stroke="{CO}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>'
    s += tx(C + 246 * math.cos(math.radians(-76)), C + 246 * math.sin(math.radians(-76)), '+1♯', 16, CO, 'AH,Arial')
    return f'<svg viewBox="-34 -46 468 486" style="width:100%;max-width:430px;display:block;margin:0 auto">{s}</svg>'
P32 = ppage(f"""{head('Part I · Pitch · 12', 'The circle of fifths', 'All the keys on one clock face. Going round clockwise, each key is a <b>5th higher</b> than the last and has <b>one more sharp</b> (or one fewer flat). Anticlockwise, each is a 4th higher, a 5th lower, with one more flat.')}
{hero(circle_hero(), 'Clockwise, one more sharp each step')}
{h3('How to read the clock') + '<p><b>Outer ring:</b> major keys. <b>Middle ring:</b> their relative minors (small letters). <b>Inner ring:</b> the key signature.</p>' + h3('Neighbours are close') + '<p>Keys next to each other share all but one note, so music moves between them easily: from C major to G major or F major, or to the relative minor. These are the <b>related keys</b>.</p>'}
{h3('Six jobs for one circle')}
<div class="uses"><div><b>Key signatures</b><span>Count the steps from C: clockwise for sharps, anticlockwise for flats.</span></div><div><b>Relative minors</b><span>Look straight in from any major key.</span></div><div><b>The main chords</b><span>A key’s two neighbours give its other main chords: in C, the chords of F and G.</span></div><div><b>Cadences</b><span>The strongest close, V to I, is one step anticlockwise: G to C.</span></div><div><b>Changing key</b><span>Pieces usually move one step round, or to the relative minor.</span></div><div><b>Scale practice</b><span>Go round the circle: one new sharp or flat each time.</span></div></div>
{inaction('Why do G major and D major sound so close?', '', ['<b>Find both:</b> D is one step clockwise from G.', '<b>Compare the scales:</b> G major has C; D major has C♯.', '<b>Count:</b> six notes the same, one different.'], 'Neighbours share six of their seven notes, so music moves between them easily.')}
<p class="think"><span>Think of it</span>Like a colour wheel: neighbours blend, opposites clash. C and G sit side by side; C and F♯ sit opposite.</p>
<!--SPLIT-->
{youknow('Passacaglia (Handel), the bass', ykfig('yk_pass', ('n1','n2','n3','n4','n5','n6','n7','n8'), 80), 'Each bass note is a <b class="co">5th below</b> the one before (or a 4th above): G C F B♭ E♭ A D G, one step round the circle each chord (except E♭ to A, a slightly smaller 5th that keeps the music in G minor).', 'Play the bass line slowly and hear it pull towards the last G.')}
{inaction('Find A major’s key signature', '', ['<b>Start at C</b> at the top of the circle: no sharps.', '<b>Go clockwise:</b> G, D, A is three steps.', '<b>Three steps,</b> three sharps: F♯, C♯, G♯.'], 'A major has <b>three sharps</b>.')}
{h3('The first steps round the circle')}
{tbl(['Steps', 'Clockwise (sharps)', 'Anticlockwise (flats)'], [['1', 'G major: F♯', 'F major: B♭'], ['2', 'D major: F♯ C♯', 'B♭ major: B♭ E♭'], ['3', 'A major: F♯ C♯ G♯', 'E♭ major: B♭ E♭ A♭']], ['16%', '42%', '42%'])}
{watch(['Going the wrong way round: clockwise adds sharps, anticlockwise adds flats.', 'Forgetting the relative minors on the middle ring.'])}
{game('Neighbours on the clock', qitems(['right of D', 'left of C', 'opposite C', 'inside G'], 4), 'Clockwise is right. Inside each major sits its relative minor.', '1 A · 2 F · 3 F♯ / G♭ · 4 E minor.')}
{try10(kbx('C', 8, 24, 70, label=True, shade={0: '#fde6dd', 4: '#fde6dd'}, scale=1.0), 'Walk the circle: C G D A E.', 'Play each key note with one finger, a 5th up each time (drop an octave when you run out of hand). You just walked four steps clockwise.')}
{h3('C major’s neighbours')}
{tbl(['Key', 'Where on the circle', 'Why it matters'], [['G major', 'one step clockwise', 'the dominant: the strongest pull home'], ['F major', 'one step anticlockwise', 'the subdominant: a gentle move away'], ['A minor', 'straight in from C', 'the relative minor: the same notes'], ['E minor, D minor', 'in from G and F', 'the relatives of the neighbours']], ['24%', '32%', '44%'])}
{howto('Learn the circle by heart', ['<b>Clockwise, out loud:</b> C G D A E B F♯. Each is a 5th above the last.', '<b>Anticlockwise:</b> C F B♭ E♭ A♭ D♭ G♭. Each is a 5th below.', '<b>Check yourself:</b> the number of steps from C is the number of sharps or flats.'])}
{foot('Keys and key signatures p. {{S3}} · Finding the key p. {{S4}} · Chords: Harmony (later)', 'Workbook Pitch 5 · Online: Scale finder, Library › Related keys')}""", 33)

css += '''
.degs{font-size:14px;line-height:1.7} .tq{border:0;padding:0;margin:6px 0} .sixf .vs svg text{font-family:'AH',Arial} .sixf{border:0} .six{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin:8px 0 10px} .six>div{border:1.5px solid #26296b;border-radius:6px;padding:10px 12px;display:flex;flex-direction:column;gap:4px;font-size:14px;line-height:1.45} .six b{font-family:'PF',serif;font-size:22px;color:#e4572e} .six i{font-style:normal;font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#6d6f9c;margin-top:auto;padding-top:4px;border-top:1px solid #e2ddd0} .uses{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin:4px 0 6px} .uses>div{border:1px solid #e2ddd0;border-top:3px solid #26296b;padding:7px 9px;font-size:13px;line-height:1.4;display:flex;flex-direction:column;gap:2px} .uses b{font-size:13.5px} .co{color:#e4572e} .ocl{display:grid;grid-template-columns:1.3fr 1fr;gap:16px;align-items:center;margin:6px 0} .ocf{display:grid;grid-template-columns:1fr 1fr;gap:8px} .ocf .vx{margin:0} .think{display:flex;gap:10px;align-items:baseline;font-size:14px;margin:8px 0;color:#3d4080} .think span{flex:none;font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#2e8a6e} .fk{display:grid;grid-template-columns:1fr 1.25fr;gap:18px;align-items:center;border-bottom:1px solid #e2ddd0;padding:8px 0;font-size:14.5px;line-height:1.5} .fk .vx{margin:0} .inact{border:1.5px solid #e4572e;border-radius:4px;padding:7px 14px 8px;margin:10px 0;background:#fff} .inact .bh{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e} .inact .it{font-size:16px;display:block;margin:2px 0 4px} .inact .vx{border:0;margin:0;padding:4px 0} .inact .px .vs svg{max-height:96px!important;min-height:70px} /* her 6 Nov: Example pictures bigger */ .inact .px text{fill:#e4572e !important} .isteps{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;font-size:13.5px;line-height:1.45;margin-top:2px} .isteps>div{display:flex;gap:8px} .in{flex:none;width:22px;height:22px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;font-size:12.5px;display:flex;align-items:center;justify-content:center} .ires{margin-top:6px;padding-top:6px;border-top:1px solid #f0d8cf;font-size:15px} .tip{border-left:3px solid #e4572e;background:#fdf6f2;padding:10px 16px 12px;margin:16px 0 0} .tip .bh{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e} .tip .tt{display:block;font-size:16px;margin:2px 0 6px} .tip table{background:transparent} .tip td,.tip th{white-space:nowrap} .tw td,.tw th{white-space:normal !important;vertical-align:top} .howto{border-left:3px solid #e4572e;background:#fdf6f2;padding:8px 14px;margin:12px 0;font-size:14px} .howto .bh{font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:#e4572e} .howto b{font-size:15px} .howto ol{margin:4px 0 0;padding-left:20px} .howto li{margin:2px 0} .rules{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;font-size:13.5px;line-height:1.45;margin:8px 0 6px} .ladder{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:10px 0 4px;font-size:14px} .ladder div{display:flex;flex-direction:column;border:1px solid #e2ddd0;padding:8px 10px} .ladder span{color:#4a4d86} .mapf .vs svg{max-width:100%} .kbl{font-family:'AH',Arial} .lmr{display:grid;grid-template-columns:1fr 1.25fr;gap:18px;align-items:center;margin:8px 0} .lmr>div:first-child{font-size:14.5px;line-height:1.55} .lmr .vx{margin:0}
.px .vs svg{width:100%;height:auto} .px text{font-family:'AH',Arial !important;fill:#26296b !important;font-weight:700} .px text.hl{fill:#e4572e !important} .kbf{display:flex;justify-content:center}
'''
import re as _re
PAGES = (P22, P23, P24, P25, P26, P27, P28, P29, P29b, P30, P31, P32)
# her 5 Nov (A): four parts. Part I Pitch keeps topics 1-5 (pp. 22-31, tips p. 32); topics 6-12 become Part III Scales and keys (pp. 50-63, tips p. 64)
_KEYS = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'S1', 'S2', 'S3', 'S4', 'S5']
_remap = lambda t: t
def _scales(t):   # Part III wording for topics 8-12 (her 6 Nov: topics 6-7, the intervals, stay in Part I)
    t = _re.sub(r'Part I · Pitch · (\d+)', lambda m: f'Part III · Scales and keys · {int(m.group(1)) - 7}', t)
    t = t.replace('PART I · PITCH', 'PART III · SCALES AND KEYS').replace('Workbook Pitch 5', 'Workbook Scales and keys 1')
    return t.replace('Chords: Harmony (later)', f'Chords in a key p. {PM.PAGE["H3"]}').replace('Online: Scale finder, Library', 'Online: Library')
_P1 = ''.join(assemble(k, pg) for k, pg in zip(_KEYS[:7], PAGES[:7])).replace('Chords: Harmony (later)', f'Chords and triads p. {PM.PAGE["H1"]}')
_P3 = _scales(''.join(assemble(k, pg) for k, pg in zip(_KEYS[7:], PAGES[7:])))

# ---------- Part I ends with its own tips page ----------
PT1 = ppage(f"""{head('Part I · Pitch · Tips', 'When a note reads wrong', 'Most misread notes come from a handful of slips. Name the slip first, then fix only that note: playing the whole line again rarely finds it.')}
<div class="tip tw"><div class="bh">Tip</div><b class="tt">What you notice, what to check</b>
{tbl(['What you notice', 'Check', 'Turn to'], [['The left hand reads like the right', '<b class="co">the clef</b>: bass lines are G B D F A, not E G B D F', 'p. {{P2}}'], ['You land an octave too high or too low', '<b class="co">a landmark</b>: middle C, treble G or bass F', 'p. {{P3}}'], ['Notes above or below the staff slow you down', '<b class="co">the ledger lines</b>: count them from the nearest landmark', 'p. {{P3}}'], ['A sharp or flat vanishes, or stays too long', '<b class="co">the bar line</b>: an accidental lasts only to the end of its bar', 'p. {{P5}}'], ['You play the black key on the wrong side', '<b class="co">the direction</b>: a sharp goes right (up), a flat goes left (down)', 'p. {{P5}}'], ['Two notes sound too close or too far apart', '<b class="co">the interval</b>: count the letters, then the keys between', 'p. {{P6}}']], ['38%', '46%', '16%'])}
</div>
{inaction('Same key, two names', kbx('C', 8, 34, 100, label=True, shade={3: '#fde6dd', 4: '#fde6dd'}, marks=['<circle cx="136" cy="44" r="10" fill="#e4572e"/>'], scale=1.0), ['<b>From F, go one key right:</b> the red black key is <b>F♯</b>.', '<b>From G, go one key left:</b> you reach the same red key, <b>G♭</b>.', '<b>One key, two names:</b> the music decides which name it uses.'], 'If F♯ and G♭ both look odd, check the key: the name follows the notes around it, the key stays the same.')}
{howto('Three checks before you read a new line', ['<b>The clefs:</b> which staff is treble, which is bass?', '<b>The landmarks:</b> find middle C, treble G and bass F, and read the other notes from them.', '<b>The accidentals:</b> mark each sharp, flat or natural, and see where its bar ends.'])}
{thinkt('Like reading a map: find the big landmarks first, then the streets around them. A note far from any landmark is the one most often misread.')}""", PM.PAGE['PT'])

def _slip():
    svg = ringsvg(P['slip'], 0).replace('<g id="n7" class="note">', '<g id="n7" class="note" style="fill:#e4572e;color:#e4572e">', 1)
    return '<figure class="vx px"><div class="vs">' + svg.replace('<svg ', '<svg style="max-height:96px" ', 1) + '</div></figure>'
PT = ppage(f"""{head('Part III · Scales and keys · Tips', 'When a note sounds wrong', 'You read the note right, yet it sounds sour. The slip is usually in the key, not the note. Name the slip first, then fix only that note.')}
<div class="tip tw"><div class="bh">Tip</div><b class="tt">What you notice, what to check</b>
{tbl(['What you notice', 'Check', 'Turn to'], [['A note sounds sour, though you read it right', '<b class="co">the key signature</b>: is this note sharp or flat all the way through?', 'p. {{S3}}'], ['A key with many sharps or flats feels lost', '<b class="co">the circle</b>: clockwise adds a sharp, anticlockwise a flat', 'p. {{S5}}'], ['A minor tune sounds wrong near the end', '<b class="co">the raised 7th</b>: harmonic and melodic minor sharpen it', 'p. {{S2}}'], ['A scale sounds wrong in the middle', '<b class="co">the semitone steps</b>: 3–4 and 7–8 in every major scale', 'p. {{S1}}'], ['A sharp is missing from the key signature', '<b class="co">the order of sharps</b>: F C G D A E B', 'p. {{S3}}'], ['You are not sure which major key it is', '<b class="co">the last sharp</b>: the key is one note above it', 'p. {{S4}}']], ['38%', '46%', '16%'])}
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
OPEN2_OLD = _opener('Part I · Which note', 'Pitch', 'High or low? That is the first question every note answers. Start with the keys under your fingers, then find where they live on the staff and how sharps and flats move them.',
    [('Keyboard', 'high and low, the patterns'), ('Staff', 'lines, spaces and clefs'), ('Reading the notes', 'every note on the staff'), ('Sharps and flats', 'the black keys')],
    [(t, PM.PAGE[k]) for t, k in (('The keyboard', 'P1'), ('The staff and the clefs', 'P2'), ('Reading the notes', 'P3'), ('The staff and the keyboard', 'P4'), ('Sharps, flats and naturals', 'P5'), ('Tips: when a note reads wrong', 'PT'))])
OPEN3_OLD = _opener('Part III · The ground under the chords', 'Scales and keys', 'Notes travel in families. Measure the distance between two notes, build the scales that whole pieces are made from, then learn to read the key a piece lives in.',
    [('Intervals', 'the distance between notes'), ('Scales', 'major and minor'), ('Keys', 'signatures and the circle')],
    [(t, PM.PAGE[k]) for t, k in (('Counting intervals', 'P6'), ('Major, minor and perfect', 'P7'), ('Major scales', 'S1'), ('Minor scales', 'S2'), ('Keys and key signatures', 'S3'), ('Finding the key', 'S4'), ('The circle of fifths', 'S5'), ('Tips: when a note sounds wrong', 'ST'))])
exec(open('/tmp/claude-0/pk/openart.py').read())
OPEN2 = opener_art('Part I · Which note', 'Pitch', 'High or low? That is the first question every note answers. Start with the keys under your fingers, find where they live on the staff, see how sharps and flats move them, then measure how far apart two notes are. Everything in this part is in this one picture.', 'P', PM.PAGE)
OPEN3 = opener_art('Part III · The ground under the chords', 'Scales and keys', 'Notes travel in families. Build the scales that whole pieces are made from, then learn to read the key a piece lives in: its signature, its home note, its place on the circle. All of it is in one scale.', 'S', PM.PAGE)
def _write(name, body):
    html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{OPENCSS}</style></head><body>{body}{_flowjs}</body></html>'
    open('/mnt/user-data/outputs/house-rooms/' + name, 'w').write(html)
_write('handbook-pitch.html', OPEN2 + _remap(_P1) + PT1)
_write('handbook-scales.html', OPEN3 + _remap(_P3) + PT)
print('ok')
