# The Piano Butler Handbook, Parts VII Shape and style and VIII Playing and listening (her 8 Nov: finish the Handbook, in order).
exec(open('/tmp/claude-0/pk/expr.py').read())   # helpers, ex(), dsym() (rewrites the Time and Expression drafts, harmless)
def fpage(inner, n): return page(inner, n, 'PART VII · SHAPE AND STYLE')
def lpage(inner, n): return page(inner, n, 'PART VIII · PLAYING AND LISTENING')
SECRETS.update({'F1': 'A motif is a word, a phrase a sentence: a question ends away from home, an answer comes home.',
                'F2': 'Again, again higher, again in the other hand, or something new.',
                'F3': 'Count the lines: one alone, a tune with chords, or tunes woven together.',
                'F4': 'A new sharp or flat that keeps coming back, then a cadence: you are in a new key.',
                'F5': 'Same music, same letter. New music, next letter.',
                'F6': 'Listen for the texture, the ornaments and the pedal: they tell you the century.',
                'L1': 'Thumbs are 1 in both hands. Choose a fingering once, write it in, keep it.',
                'L2': 'Slow, small, and correct; then a little faster; then join the pieces.',
                'L3': 'Look before you play, then never stop: the beat matters more than any note.',
                'L4': 'Sing it back first: if you can sing it, you can play it.',
                'L5': 'Breathe, feel a bar of the beat, then begin. After a slip, catch the next beat.'})
def blocks(letters, q=None, W=72, H=58, cols=None):   # form letters as a row of blocks; q: index to replace with '?'
    n = len(letters); Wt = n * (W + 10) + 10
    o = f'<svg viewBox="0 0 {Wt} {H + 20}" style="width:100%;max-width:{Wt}px;height:auto;display:block;margin:0 auto">'
    for i, L in enumerate(letters):
        x = 10 + i * (W + 10); new = L[0] != 'A'
        if q is not None and i == q:
            o += f'<rect x="{x}" y="10" width="{W}" height="{H}" rx="8" fill="#fff3ee" stroke="{R_}" stroke-width="2" stroke-dasharray="5 4"/><text x="{x + W / 2}" y="{10 + H / 2 + 10}" text-anchor="middle" font-family="AH,Arial" font-size="28" font-weight="700" fill="{R_}">?</text>'
        else:
            o += f'<rect x="{x}" y="10" width="{W}" height="{H}" rx="8" fill="{"#fde3d8" if new else "#e9e9f5"}" stroke="{N_}" stroke-width="1.6"/><text x="{x + W / 2}" y="{10 + H / 2 + 11}" text-anchor="middle" font-family="PF,serif" font-size="30" font-weight="700" fill="{R_ if new else N_}">{L}</text>'
    return o + '</svg>'
def bigq(t, fs=24): return qtagT(f'<div style="font:700 {fs}px AH,Arial;color:#26296b;text-align:center;line-height:1.35">{t}</div>')

# ---------- heroes ----------
def hero_build():
    o = '<svg viewBox="0 0 620 220" style="width:100%;max-width:580px;height:auto;display:block;margin:0 auto">'
    def brick(x, y, col=R_): return f'<rect x="{x}" y="{y}" width="50" height="26" rx="4" fill="{col}"/>'
    o += brick(40, 30) + f'<text x="65" y="80" text-anchor="middle" font-family="AH,Arial" font-size="14" font-weight="700" fill="{N_}">motif</text><text x="65" y="98" text-anchor="middle" font-family="AH,Arial" font-size="12" fill="#5a5d8f">a word</text>'
    for i in range(4): o += brick(150 + i * 54, 30, R_ if i % 2 == 0 else '#f6c2ad')
    o += f'<path d="M150,22 Q257,-4 364,22" fill="none" stroke="{N_}" stroke-width="2"/><text x="257" y="80" text-anchor="middle" font-family="AH,Arial" font-size="14" font-weight="700" fill="{N_}">phrase</text><text x="257" y="98" text-anchor="middle" font-family="AH,Arial" font-size="12" fill="#5a5d8f">a sentence, about 4 bars</text>'
    for r in range(2):
        for i in range(4): o += f'<rect x="{400 + i * 52}" y="{120 + r * 34}" width="48" height="26" rx="4" fill="{R_ if i % 2 == 0 else "#f6c2ad"}"/>'
        o += f'<path d="M400,{114 + r * 34} Q502,{98 + r * 34} 604,{114 + r * 34}" fill="none" stroke="{N_}" stroke-width="1.6"/>'
    o += f'<text x="502" y="206" text-anchor="middle" font-family="AH,Arial" font-size="14" font-weight="700" fill="{N_}">section: question + answer</text>'
    o += f'<path d="M100,43 H140 M372,43 Q400,43 400,110" fill="none" stroke="#9a9cc4" stroke-width="1.6" stroke-dasharray="4 4"/>'
    return o + '</svg>'
def stairs(kind):   # a three-note motif as dots: 'rep', 'seq', 'imit', 'con'
    o = '<svg viewBox="0 0 150 90" style="width:130px;height:auto;display:block;margin:0 auto">'
    def mot(x, y, col=R_): return ''.join(f'<circle cx="{x + k * 14}" cy="{y - k * 8}" r="5" fill="{col}"/>' for k in range(3))
    if kind == 'rep': o += mot(14, 60) + mot(84, 60)
    if kind == 'seq': o += mot(14, 70) + mot(84, 50)
    if kind == 'imit': o += f'<line x1="6" y1="45" x2="144" y2="45" stroke="#c9cbe0"/>' + mot(14, 36) + mot(84, 82, N_)
    if kind == 'con': o += mot(14, 60) + f'<rect x="84" y="40" width="44" height="14" rx="7" fill="{N_}"/>'
    return o + '</svg>'
def hero_tex():
    rows = [('one line', 'monophony'), ('a tune with chords', 'melody and accompaniment'), ('a tune over broken chords', 'Alberti bass, arpeggios'), ('two tunes at once', 'polyphony')]
    o = '<svg viewBox="0 0 620 250" style="width:100%;max-width:580px;height:auto;display:block;margin:0 auto">'
    for r, (a, b) in enumerate(rows):
        y = 26 + r * 60
        o += f'<text x="0" y="{y + 6}" font-family="AH,Arial" font-size="15" font-weight="700" fill="{N_}">{a}</text><text x="0" y="{y + 24}" font-family="AH,Arial" font-size="12" fill="#5a5d8f">{b}</text>'
        o += f'<path d="M240,{y} q30,-16 60,0 t60,0 t60,0 t60,0 t60,0 t60,0" fill="none" stroke="{R_}" stroke-width="3"/>'
        if r == 1: o += ''.join(f'<rect x="{248 + k * 90}" y="{y + 14}" width="40" height="22" rx="3" fill="#c9cbe0"/>' for k in range(4))
        if r == 2: o += f'<path d="M240,{y + 30} l15,-12 l15,8 l15,-8 l15,12 l15,-12 l15,8 l15,-8 l15,12 l15,-12 l15,8 l15,-8 l15,12 l15,-12 l15,8 l15,-8 l15,12 l15,-12 l15,8 l15,-8 l15,12 l15,-12 l15,8 l15,-8 l15,12" fill="none" stroke="{N_}" stroke-width="2"/>'
        if r == 3: o += f'<path d="M240,{y + 24} q30,14 60,0 t60,0 t60,0 t60,0 t60,0 t60,0" fill="none" stroke="{N_}" stroke-width="3"/>'
    return o + '</svg>'
def hero_trip():
    o = '<svg viewBox="0 0 620 170" style="width:100%;max-width:560px;height:auto;display:block;margin:0 auto">'
    def house(x, t, sub, col):
        return (f'<path d="M{x},{90} L{x + 60},{40} L{x + 120},{90} V{150} H{x} Z" fill="{col}" stroke="{N_}" stroke-width="2"/>'
                f'<text x="{x + 60}" y="{116}" text-anchor="middle" font-family="PF,serif" font-size="18" font-weight="700" fill="{N_}">{t}</text><text x="{x + 60}" y="{136}" text-anchor="middle" font-family="AH,Arial" font-size="12" fill="#5a5d8f">{sub}</text>')
    o += house(20, 'C major', 'home', '#e9e9f5') + house(250, 'G major', 'a visit', '#fde3d8') + house(480, 'C major', 'home again', '#e9e9f5')
    o += f'<path d="M150,100 Q200,70 244,100" fill="none" stroke="{R_}" stroke-width="2.5" marker-end="url(#ah)"/><path d="M380,100 Q430,70 474,100" fill="none" stroke="{R_}" stroke-width="2.5"/>'
    o += f'<text x="197" y="66" text-anchor="middle" font-family="CV,cursive" font-size="20" font-weight="700" fill="{R_}">F♯ appears</text><text x="427" y="66" text-anchor="middle" font-family="CV,cursive" font-size="20" font-weight="700" fill="{R_}">F♮ again</text>'
    return o + '</svg>'
def hero_forms():
    rows = [('binary', 'AB'), ('ternary', 'ABA'), ('rondo', 'ABACA'), ('variations', ['A', 'A¹', 'A²', 'A³'])]
    o = '<svg viewBox="0 0 620 250" style="width:100%;max-width:560px;height:auto;display:block;margin:0 auto">'
    for r, (n, L) in enumerate(rows):
        y = 10 + r * 60
        o += f'<text x="0" y="{y + 32}" font-family="AH,Arial" font-size="16" font-weight="700" fill="{N_}">{n}</text>'
        for i, l in enumerate(list(L)):
            x = 130 + i * 92; new = l[0] != 'A'
            o += f'<rect x="{x}" y="{y}" width="84" height="46" rx="7" fill="{"#fde3d8" if new else "#e9e9f5"}" stroke="{N_}" stroke-width="1.5"/><text x="{x + 42}" y="{y + 32}" text-anchor="middle" font-family="PF,serif" font-size="24" font-weight="700" fill="{R_ if new else N_}">{l}</text>'
    return o + '</svg>'
def hero_time():
    P_ = [('Baroque', 1600, 1750, 'Bach · Handel · Scarlatti'), ('Classical', 1750, 1820, 'Haydn · Mozart · Beethoven'), ('Romantic', 1820, 1900, 'Chopin · Schumann · Liszt'), ('Modern', 1900, 2025, 'Debussy · Bartók · jazz · film')]
    X = lambda yr: 20 + (yr - 1600) * 580 / 425
    o = '<svg viewBox="0 0 620 170" style="width:100%;max-width:600px;height:auto;display:block;margin:0 auto">'
    for i, (n, a, b, c) in enumerate(P_):
        o += f'<rect x="{X(a):.0f}" y="40" width="{X(b) - X(a) - 3:.0f}" height="40" rx="5" fill="{["#e9e9f5", "#fde3d8", "#f6c2ad", "#c9cbe0"][i]}"/><text x="{(X(a) + X(b)) / 2:.0f}" y="66" text-anchor="middle" font-family="PF,serif" font-size="17" font-weight="700" fill="{N_}">{n}</text>'
        o += f'<text x="{(X(a) + X(b)) / 2:.0f}" y="{104 + (i % 2) * 22}" text-anchor="middle" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">{c}</text>'
    for yr in (1600, 1700, 1800, 1900, 2000): o += f'<text x="{X(yr):.0f}" y="30" text-anchor="middle" font-family="AH,Arial" font-size="12" font-weight="700" fill="{N_}">{yr}</text><line x1="{X(yr):.0f}" y1="34" x2="{X(yr):.0f}" y2="40" stroke="{N_}"/>'
    return o + '</svg>'

# ---------- VII.1 Motifs and phrases ----------
F1 = fpage(f'''{head('Part VII · Shape and style · 1', 'Motifs and phrases', 'A tune is built like a story. A tiny idea, the <b>motif</b>, grows into a <b>phrase</b>, a musical sentence; two phrases make a question and its answer. Spot the building blocks and a page of notes turns into a few ideas.')}
{hero(hero_build(), 'Words, sentences, paragraphs')}
{h3('A motif')}
{two(ex('f_b5', 76), '<p>Four notes, short-short-short-long: Beethoven builds the whole first movement of his Fifth Symphony from them. A motif is short (2 to 6 notes) and easy to recognise: its <b>rhythm</b> and its <b>shape</b> come back again and again.</p>')}
{h3('Phrases: question and answer')}
{ex('f_ode8', 72, 'Ode to Joy: two 4-bar phrases. The first ends on D, away from home (a question); the second comes home to C (an answer).', red=('n15', 'n30'))}
{rule('Most phrases are <b>4 bars</b> long. A question phrase ends away from the key note; the answer comes home to it.')}
<!--SPLIT-->
{inact('Question or answer?', qtagT(ex('f_ode4', 72, red=('n15',))), ['<b>The key is C major.</b> What is the home note?', '<b>The last note</b> of this phrase is…?', '<b>Is it home?</b>'], 'It ends on D, not C: a <b>question</b>. The answer phrase that follows ends on C.')}
{inact('Find the motif', qtagT(ex('f_motq', 70)), ['<b>Look at bar 1:</b> what shape and rhythm?', '<b>Bars 2 and 3:</b> the same shape?', '<b>Where</b> does each start?'], 'Step, step, long: three notes. It comes <b>three times</b>, each a step higher.')}
{youknow('Beethoven, Symphony No. 5', ex('f_b5', 62, red=('n2', 'n3', 'n4', 'n5')), '“Da-da-da-<b class="co">DUM</b>”: the most famous motif ever written. Listen to the first minute and count how many times it comes back.', 'Tap the rhythm on the lid, then sing it a step lower.')}
{game('How many phrases?', qitems(['8 bars', '12 bars', '16 bars'], 3), 'Each phrase is 4 bars long. How many phrases in a tune of…', '1 two · 2 three · 3 four.')}
{try10(ex('f_ode8', 50), 'Sing a question, then an answer.', 'Sing the question and stop on the D: it hangs in the air. Now sing the answer and land on C.')}
{watch(['Playing every note the same: each phrase has one high point to grow towards.'])}
{foot('Slurs and phrases p. {{E2+1}} · Cadences p. {{M2}}', 'Online: Library › Phrases')}''', 144)

# ---------- VII.2 Repetition and sequence ----------
RS = [['<b>repetition</b>', 'the same notes again'], ['<b>sequence</b>', 'the same shape, starting higher or lower'], ['<b>imitation</b>', 'another hand or voice copies the idea'], ['<b>contrast</b>', 'something new: a different shape or rhythm']]
F2 = fpage(f'''{head('Part VII · Shape and style · 2', 'Repetition and sequence', 'Composers make one idea go a long way. They say it again, say it again higher or lower, let another hand copy it, or say something completely new.')}
{hero('<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;text-align:center">' + ''.join(f'<div>{stairs(k)}<b style="font:700 15px AH,Arial;color:#26296b">{t}</b></div>' for k, t in (('rep', 'again'), ('seq', 'again, higher'), ('imit', 'copied below'), ('con', 'something new'))) + '</div>', 'Four ways to use one idea')}
{tbl(['Name', 'What happens'], RS, ['30%', '70%'])}
{two(ex('f_seq', 70, 'A rising sequence: C D E, D E F, E F G.'), ex('f_seqdown', 70, 'A falling sequence: each step one note lower.'))}
<!--SPLIT-->
{drill('Take any three-note motif and play it as a sequence, starting on every white key from C up to the next C, then back down.')}
{inact('Repetition or sequence?', qtagT(ex('f_seq2', 70, red=('n4', 'n5', 'n6'))), ['<b>Bar 1:</b> which notes?', '<b>Bar 2:</b> the same notes, or the same shape on new notes?', '<b>Bar 3?</b>'], 'Same shape, a step higher each bar: a <b>sequence</b>.')}
{inact('Which hand copies?', qtagT(ex('f_imit', 100)), ['<b>The right hand</b> starts with C D E F G E C.', '<b>The left hand</b> waits a bar. Then?', '<b>Same notes</b>, how many octaves lower?'], 'The left hand <b>imitates</b> the right one bar later, two octaves down.')}
{inact('Where is the contrast?', qtagT(ex('f_contr', 70, red=('n9', 'n10'))), ['<b>Bars 1 and 2:</b> same or different?', '<b>Bar 3:</b> what changes, the notes or the rhythm?', '<b>Bar 4?</b>'], 'Bars 1–2 repeat; <b>bar 3</b> brings something new: long notes on G.')}
{youknow('Frère Jacques', ex('f_frere', 62), 'Every bar is said <b class="co">twice</b>: repetition. Sung as a round, each voice enters two bars after the last: imitation.', 'Sing it as a round with a friend.')}
{game('Which way?', qitems(['same notes', 'one step up', 'left hand copies', 'new rhythm'], 4), 'Name each one.', '1 repetition · 2 sequence · 3 imitation · 4 contrast.')}
{try10(stairs('seq'), 'Make a sequence.', 'Play C D E, then D E F, then E F G with fingers 1 2 3. Now go down: G F E, F E D, E D C.')}
{watch(['Calling any repeat a sequence: a sequence moves to new notes.'])}
{foot('Motifs and phrases p. {{F1}} · Texture p. {{F3}}', 'Online: Library › Patterns')}''', 146)

# ---------- VII.3 Texture ----------
TEX = [['<b>monophonic</b>', 'one line alone, or in octaves (unison)'], ['<b>homophonic</b>', 'a tune with chords underneath: melody and accompaniment'], ['<b>polyphonic</b> (contrapuntal)', 'two or more tunes at once, each its own'], ['<b>Alberti bass</b>', 'a broken chord rocking low–high–middle–high'], ['<b>block chords</b>', 'all the chord notes struck together']]
F3 = fpage(f'''{head('Part VII · Shape and style · 3', 'Texture', 'Texture is how many lines sound at once, and how they fit together: one line alone, a tune with chords, or several tunes woven together like threads in cloth.')}
{hero(hero_tex(), 'Thin or thick: count the threads')}
{tbl(['Word', 'What you hear'], TEX, ['34%', '66%'])}
{two(ex('f_homo', 92, 'Melody and block chords.'), ex('f_poly', 92, 'Polyphony: two tunes, each with its own rhythm.'))}
<!--SPLIT-->
{inact('Name the texture', qtagT(ex('f_homo2', 90)), ['<b>The right hand:</b> a tune or chords?', '<b>The left hand:</b> a tune or chords?', '<b>So</b> which word?'], 'A tune over chords: <b>homophonic</b>, melody and accompaniment.')}
{inact('Which hand has the tune?', qtagT(ex('f_lh', 90)), ['<b>The right hand</b> repeats two-note chords.', '<b>The left hand</b> moves step by step.', '<b>Which one</b> should sing out?'], 'The <b>left hand</b> has the tune: play it louder, keep the right-hand chords soft.')}
{youknow('Mozart, Sonata in C, K. 545', ex('f_alb', 86), 'The right hand sings; the left hand rocks <b class="co">C G E G</b>: an Alberti bass, the sound of the Classical style.', 'Play only the left hand, softly and evenly.')}
{game('One line or more?', qitems(['a tune alone', 'a tune and chords', 'two tunes at once'], 3), 'Name the texture.', '1 monophonic · 2 homophonic · 3 polyphonic.')}
{watch(['Letting the accompaniment cover the tune: tune louder, chords softer.', 'Losing one of two tunes: practise each hand alone and sing it.'])}
{foot('Chords under a melody p. {{M3}} · Styles p. {{F6}}', 'Online: Library › Texture')}''', 148)

# ---------- VII.4 Changing key ----------
NEAR = [['<b>G major</b>', 'F♯ appears', 'the key a 5th up (one more sharp)'], ['<b>F major</b>', 'B♭ appears', 'the key a 4th up (one more flat)'], ['<b>A minor</b>', 'G♯ appears', 'the relative minor (same key signature)']]
F4 = fpage(f'''{head('Part VII · Shape and style · 4', 'Changing key', 'Music can travel to a new key and come home again: a <b>modulation</b>. The signpost is a new sharp, flat or natural that keeps coming back, and a cadence that lands in the new key.')}
{hero(hero_trip(), 'A trip away, and home again')}
{h3('The nearest keys')}
<p>A piece in C major usually visits the keys next door on the circle of fifths (p. {{{{S5}}}}): only one note changes.</p>
{tbl(['From C major to', 'The signpost', 'Why it is close'], NEAR, ['26%', '26%', '48%'])}
{ex('f_mod', 74, 'Bar 1 in C major; F♯ twice in bar 2, then the phrase lands on G: now G major.', red=('n6', 'n8', 'n13'))}
<!--SPLIT-->
{inact('Where does the key change?', qtagT(ex('f_modF', 70)), ['<b>Find the accidental.</b>', '<b>Which major key</b> has one flat, B♭?', '<b>Where</b> does the phrase land?'], 'B♭ in bar 2 and again in bar 3, landing on F: <b>F major</b>.')}
{inact('Which nearby key?', bigq('In G major,<br>a C♯ keeps appearing'), ['<b>G major</b> has one sharp, F♯.', '<b>C♯ is one more sharp.</b>', '<b>Which key</b> has F♯ and C♯?'], '<b>D major</b>, the key a 5th up: one more sharp.')}
{inact('A new key, or just passing?', bigq('One F♯ in a bar of C major,<br>then F♮ everywhere after', 21), ['<b>Does the F♯ come back?</b>', '<b>Is there a cadence</b> in G?', '<b>So</b>, a new key?'], 'No: one passing F♯ is a decoration. A modulation <b>keeps</b> its new note and lands with a cadence.')}
{game('Where to next?', qitems(['C major + F♯', 'C major + B♭', 'G major + C♯', 'F major + E♭'], 4), 'Which nearby key has the music moved to?', '1 G major · 2 F major · 3 D major · 4 B♭ major.')}
{try10(ex('f_mod', 64), 'Hear the pull.', 'Play the four bars twice: once with F♮ in bar 2, once with F♯. With the F♯, the G at the end sounds like a new home.')}
{thinkt('A modulation is a holiday: new scenery for a while, but the piece usually comes home at the end.')}
{watch(['Taking one passing accidental as a new key: it must keep coming back.', 'Missing the way home: most pieces end in the key they began in, so watch for the old note returning.'])}
{foot('The circle of fifths p. {{S5}} · Cadences p. {{M2}}', 'Online: Library › Keys')}''', 150)

# ---------- VII.5 Form ----------
FORMS = [['<b>binary</b>', 'A B', 'two halves, each often repeated', 'Baroque dances: minuets, gigues'], ['<b>ternary</b>', 'A B A', 'out, away, and back', 'many short Romantic pieces'],
         ['<b>rondo</b>', 'A B A C A', 'A keeps coming back between new ideas', 'Beethoven, Für Elise'], ['<b>theme and variations</b>', 'A A¹ A² A³', 'one tune, dressed differently each time', 'Mozart’s variations on “Twinkle”'],
         ['<b>strophic</b>', 'A A A', 'the same music for every verse', 'hymns, folk songs'], ['<b>verse and chorus</b>', 'V C V C', 'the chorus words stay the same', 'pop songs']]
F5 = fpage(f'''{head('Part VII · Shape and style · 5', 'Form', 'Form is the map of a whole piece: which sections come, in what order, and which come back. Letters name them: <b>A</b> for the first idea, <b>B</b> for the next new one, and so on.')}
{hero(hero_forms(), 'The map of a piece, in letters')}
{tbl(['Form', 'Letters', 'Shape', 'You know it from'], FORMS, ['24%', '16%', '32%', '28%'])}
{rule('Same music, <b>same letter</b>. New music, the next letter. A little changed: add a small number (A¹).')}
<!--SPLIT-->
{inact('Which letter makes it ternary?', blocks(['A', 'B', '?'], 2), ['<b>A B</b> alone: two sections.', '<b>Ternary</b> goes out, away and…?', '<b>Which letter</b> fills the box?'], '<b>A</b>. A B is binary; A B <b>A</b> is ternary.')}
{inact('Which form?', qtagT(blocks(['A', 'B', 'A', 'C', 'A'])), ['<b>Count the sections.</b>', '<b>Which one keeps coming back?</b>', '<b>What comes between?</b>'], 'A returns between two new ideas: a <b>rondo</b>.')}
{inact('Map Twinkle', qtagT(ex('f_tw12', 70)), ['<b>Bars 1–4:</b> call them A.', '<b>Bars 5–8:</b> new or the same?', '<b>The last four bars</b> (not shown) repeat bars 1–4.'], 'Bars 5–8 are new: B. Then A again: <b>A B A</b>, ternary.')}
{inact('What comes next?', blocks(['A', 'A¹', 'A²', '?'], 3), ['<b>A</b> is the theme.', '<b>A¹ and A²</b>: the same tune, dressed differently.', '<b>The next one</b> is called…?'], '<b>A³</b>: a third variation. Theme and variations keep one tune and change its clothes.')}
{extra('Sonata form', '<p>The big first movements of sonatas and symphonies: an <b>exposition</b> (two themes, the second in a new key), a <b>development</b> (the themes taken apart and moved through keys), and a <b>recapitulation</b> (both themes again, now at home).</p>')}
{youknow('Beethoven, Für Elise', blocks(['A', 'B', 'A', 'C', 'A'], None, 60, 46), 'The famous opening tune is <b class="co">A</b>. It is heard three times, with two new sections in between: a rondo.', 'Listen and raise your hand every time A returns.')}
{listen([('Petzold', 'Minuet in G (Notebook for Anna Magdalena Bach; once thought to be Bach’s)', 'binary: two halves, each repeated'), ('Beethoven', 'Für Elise', 'rondo: A B A C A'), ('Mozart', 'Twelve Variations on “Ah vous dirai-je, Maman”', 'theme and variations, on the tune of Twinkle')])}
{game('Name the form', qitems(['A B', 'A B A', 'A B A C A', 'A A¹ A² A³'], 4), 'Name each map.', '1 binary · 2 ternary · 3 rondo · 4 theme and variations.')}
{try10(blocks(['A', '?', '?'], None, 50, 40), 'Map a piece you play.', 'Give every 4-bar phrase a letter. Same music, same letter. What form is it?')}
{howto('Learn a piece by its map', ['<b>Letter the sections</b> in pencil.', '<b>Learn A first</b>: it comes back, so it pays twice.', '<b>Then the new sections</b>, and practise the joins between them.'])}
{thinkt('Form is the floor plan of a house: once you know the rooms, you never get lost in it.')}
{watch(['Giving every phrase a new letter: same music, same letter.', 'Counting a repeat as a new section: A played twice is still A.'])}
{foot('Repeats and road signs p. {{T8}} · Changing key p. {{F4}}', 'Online: Library › Form')}''', 152)

# ---------- VII.6 Styles ----------
STY = [['<b>Baroque</b><br><span class="sm">1600–1750</span>', 'harpsichord and organ; two or more tunes woven together; many ornaments; loud or soft in blocks; a steady beat throughout'],
       ['<b>Classical</b><br><span class="sm">1750–1820</span>', 'the new piano; a clear tune with an Alberti bass; tidy 4-bar phrases; crescendos and contrasts'],
       ['<b>Romantic</b><br><span class="sm">1820–1900</span>', 'big feelings; rich chords and the pedal; rubato; the whole keyboard, from very soft to very loud'],
       ['<b>Modern</b><br><span class="sm">1900–today</span>', 'new scales and harmonies, surprising rhythms; impressionism, jazz, minimalism, film music']]
F6 = fpage(f'''{head('Part VII · Shape and style · 6', 'Styles through time', 'Music changes with its time, like clothes and buildings. Four big periods cover most piano music. Each has a sound you can learn to recognise, and a way it likes to be played.')}
{hero(hero_time(), 'Four centuries, four sounds')}
{tbl(['Period', 'Listen for'], STY, ['24%', '76%'])}
{h3('Playing in style')}
{tbl(['', 'Pedal', 'Time', 'Touch'], [['<b>Baroque</b>', 'little or none', 'steady', 'clear, often detached'], ['<b>Classical</b>', 'light', 'steady', 'neat, even, singing tune'], ['<b>Romantic</b>', 'rich', 'rubato', 'deep, legato'], ['<b>Modern</b>', 'as marked', 'as marked', 'whatever the music asks']], ['22%', '26%', '22%', '30%'])}
<!--SPLIT-->
{inact('Which period?', bigq('A tune over an Alberti bass,<br>tidy 4-bar phrases', 21), ['<b>Alberti bass:</b> which period did it belong to?', '<b>Tidy phrases</b>, question and answer.', '<b>So?</b>'], '<b>Classical</b>: think Mozart.')}
{inact('Which period?', bigq('Two equal tunes, many trills,<br>written for harpsichord', 21), ['<b>Two tunes woven together</b>: which texture?', '<b>Harpsichord</b>, before the piano.', '<b>So?</b>'], '<b>Baroque</b>: think Bach.')}
{inact('Which period?', bigq('Rubato, rich pedalled chords,<br>huge leaps across the keyboard', 21), ['<b>Rubato</b>: time stretched for feeling.', '<b>Rich chords</b> held in the pedal.', '<b>So?</b>'], '<b>Romantic</b>: think Chopin.')}
{listen([('Notebook for Anna Magdalena Bach', 'Minuet in G (Petzold)', 'two lines, a steady dance'), ('Mozart', 'Sonata in C, K. 545', 'Alberti bass, clear phrases'), ('Chopin', 'Nocturnes', 'a singing tune, rubato, pedal')])}
{game('Who belongs where?', qitems(['Bach', 'Mozart', 'Chopin', 'Debussy'], 4), 'Match each composer to a period.', '1 Baroque · 2 Classical · 3 Romantic · 4 Modern.')}
{watch(['Pedalling Bach like Chopin: Baroque music needs little or no pedal.', 'Romantic rubato in Mozart: keep Classical time steady.'])}
{foot('Ornaments p. {{E5}} · The pedals p. {{E4}}', 'Online: Library › Styles')}''', 155)

FT = fpage(f'''{head('Part VII · Shape and style · Tips', 'When a piece goes nowhere', 'Every note can be right and the piece still wander. The fix is to see the shape: where the phrases go, what comes back, and where the high point is.')}
{box('Tip', '<b class="it">What you notice, what to check</b>' + tbl(['What you notice', 'Check', 'Turn to'], [['Every bar sounds the same', '<b>the phrases:</b> where does each one grow?', 'p. {{F1}}'], ['It feels like a list of notes', '<b>the motif</b> and its sequences', 'p. {{F2}}'], ['The tune is lost', '<b>the texture:</b> which line sings?', 'p. {{F3}}'], ['A passage suddenly feels strange', '<b>a new key:</b> look for the new accidental', 'p. {{F4}}'], ['You lose your place', '<b>the form:</b> letter the sections', 'p. {{F5}}'], ['It sounds out of style', '<b>the period:</b> pedal, time and touch', 'p. {{F6}}']], ['38%', '48%', '14%']))}
{h3('Four ways to find the shape')}
<div class="fixes">{''.join(f'<div><span class="rn">{i + 1}</span><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate([('Pencil the phrases', 'Draw a curve over each phrase and mark its high point.'), ('Letter the sections', 'Write A, B, A in the margin. Practise each section on its own.'), ('Sing the tune', 'Sing the top line while you play the rest softly.'), ('Listen to a recording', 'Follow the score and hear the shape before you play it.')]))}</div>
{inact('Where is the high point?', qtagT(ex('f_tw4', 70)), ['<b>Sing it.</b>', '<b>Which note</b> is highest?', '<b>Grow to it</b>, then let the phrase fall.'], 'The <b>As in bar 2</b>: grow to them, then fall home to C.')}
{thinkt('A map does not make the journey, but it stops you getting lost.')}''', PM.PAGE['FT'])

# ---------- VIII.1 Fingering ----------
from openart import pic_play as _pp
def hand_pic(): return _pp(False).replace('#fffdf7', '#26296b').replace('#f4a9bb', '#5a5d8f').replace('style="width:100%;display:block"', 'style="width:100%;max-width:540px;display:block;margin:0 auto"')
L1 = lpage(f'''{head('Part VIII · Playing and listening · 1', 'Fingering', 'Each finger has a number, the same in both hands: the thumb is 1, the little finger 5. Good fingering is planned, not guessed: choose it once, write it in, and use it every time.')}
{hero(hand_pic(), 'Thumbs are 1 in both hands')}
{h3('Five-finger position')}
{two(ex('l_five', 74), '<p>Thumb on C, one finger on each key up to G: five notes without moving the hand. Many first pieces stay in one position.</p>')}
{h3('Thumb under, finger over')}
{two(ex('l_scale', 74, 'Up the scale: 1 2 3, thumb under to F, then 1 2 3 4 5.'), ex('l_cross', 74, 'Down: 5 4 3 2 1, then 3 crosses over the thumb.'))}
<!--SPLIT-->
{inact('Which finger plays the F?', qtagT(ex('l_fq', 72, red=('n4',))), ['<b>C D E</b> are 1 2 3.', '<b>The F:</b> finger 4, or the thumb tucked under?', '<b>Then</b> how do you reach the top C?'], 'The <b>thumb</b> passes under to F; then 2 3 4 5 reach the top C.')}
{inact('Which finger plays G?', bigq('Right hand,<br>thumb on C'), ['<b>Thumb on C</b> is 1.', '<b>Count up</b> one finger per key: D, E, F, G.', '<b>So G</b> is…?'], 'Finger <b>5</b>: C D E F G is 1 2 3 4 5.')}
{drill('Play C D E F G with each hand, saying the finger numbers: right 1 2 3 4 5 up, left 5 4 3 2 1 up. Then both hands together.')}
<p class="sm"><b>Left hand, C major up:</b> 5 4 3 2 1, then 3 crosses over to A, then 2 1. <b>Down:</b> 1 2 3, thumb under to F, then 1 2 3 4 5.</p>
{game('Name the finger', qitems(['thumb', 'index', 'middle', 'little'], 4), 'Give the finger number.', '1 one · 2 two · 3 three · 4 five.')}
{try10(ex('l_five', 46), 'Five fingers, five keys.', 'Right hand on C D E F G. Play up and down, saying the finger numbers aloud. Then the left hand: 5 4 3 2 1 from C up.')}
{watch(['Changing fingering every time you play: choose one, write it in, keep it.', 'Landing heavily on the thumb as it passes under: let it glide.'])}
{foot('The keyboard p. {{P1}} · Major scales p. {{S1}}', 'Online: Scales with fingering')}''', 160)

# ---------- VIII.2 Practising well ----------
PLAN = [['<b>2 min</b>', 'warm up: a scale or five-finger exercise'], ['<b>5 min</b>', 'the hardest bars, slowly, hands separately'], ['<b>5 min</b>', 'join the bars, hands together, still slow'], ['<b>3 min</b>', 'play the whole section; mark what slipped']]
def ladder():
    o = '<svg viewBox="0 0 560 170" style="width:100%;max-width:520px;height:auto;display:block;margin:0 auto">'
    for i, n in enumerate((60, 66, 72, 80, 88, 96)):
        x = 20 + i * 90; y = 130 - i * 20
        o += f'<rect x="{x}" y="{y}" width="80" height="{150 - y}" rx="4" fill="{R_ if i == 5 else ("#f08b6b" if i > 2 else "#f6c2ad")}"/><text x="{x + 40}" y="{y - 8}" text-anchor="middle" font-family="AH,Arial" font-size="16" font-weight="700" fill="{N_}">♩={n}</text>'
    return o + f'<text x="20" y="166" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">three correct times at one speed, then one step up</text></svg>'
L2 = lpage(f'''{head('Part VIII · Playing and listening · 2', 'Practising well', 'Practice is not playing a piece again and again from the top. It is fixing the hard bits, slowly and correctly, then joining them back together.')}
{hero(ladder(), 'Slow and correct, one step at a time')}
{h3('A fifteen-minute plan')}
{tbl(['Time', 'What you do'], PLAN, ['20%', '80%'])}
{h3('Four tools')}
{tbl(['Tool', 'How'], [['<b>small chunks</b>', 'one bar, or two, plus the first note of the next'], ['<b>hands separately</b>', 'each hand alone until it is easy, then together'], ['<b>slow, then faster</b>', 'the metronome ladder: three correct times, then one notch up'], ['<b>count aloud</b>', 'say the beats: it keeps the rhythm honest']], ['30%', '70%'])}
<!--SPLIT-->
{inact('Which bar first?', qtagT(ex('l_hard', 70, red=('n9', 'n10', 'n11', 'n12', 'n13', 'n14', 'n15', 'n16'))), ['<b>Play it through once.</b> Where did it slip?', '<b>The semiquavers</b> in bar 3: hardest?', '<b>Start there</b>, slowly.'], 'Bar 3, the semiquavers: practise the <b>hardest bar first</b>, slowly, then join bars 2–4.')}
{inact('When do you speed up?', bigq('♩&#8202;=&#8202;60: right, right, wrong'), ['<b>How many correct</b> in a row do you need?', '<b>After a mistake</b>, start counting again.', '<b>Then</b> one notch up.'], 'Not yet: three <b>correct</b> in a row at 60, then try 66.')}
{game('Good habit or not?', qitems(['from the top', 'hardest first', 'faster to fix', 'slow, correct'], 4), 'Which help?', '2 and 4 help; 1 and 3 waste time.')}
{try10('<div style="font:700 28px AH,Arial;color:#26296b;text-align:center">60 → 66 → 72</div>', 'Climb the ladder.', 'Pick one hard bar. Play it three times correctly at a slow speed, then one notch faster. Stop when it slips twice.')}
{extra('Practise in rhythms', '<p>For a run of even quavers, play it long–short, then short–long, slowly. When you go back to even notes, the run is suddenly easier: every note has been the “long” one.</p>')}
{howto('Keep a practice log', ['<b>Write the date</b> and what you practised.', '<b>Note one thing</b> that got better and one that did not.', '<b>Start tomorrow</b> with the one that did not.'])}
{thinkt('Practice is like building a wall: lay each brick straight and the wall stands on its own.')}
{watch(['Practising mistakes: playing fast and wrong teaches your fingers the wrong notes.', 'Only playing what you already know: spend most time on the hard bits.'])}
{foot('Speed words p. {{E3}} · Fingering p. {{L1}}', 'Online: Metronome · Practice log')}''', 162)

# ---------- VIII.3 Sight-reading ----------
SCAN = [['<b>1 key</b>', 'sharps or flats at the start'], ['<b>2 time</b>', 'the time signature: count a bar before you start'], ['<b>3 clefs and notes</b>', 'the first note in each hand; the lowest and highest'], ['<b>4 rhythm</b>', 'the trickiest rhythm: tap it'], ['<b>5 patterns</b>', 'steps, skips, repeats, sequences'], ['<b>6 marks</b>', 'dynamics, slurs, speed words']]
L3 = lpage(f'''{head('Part VIII · Playing and listening · 3', 'Sight-reading', 'Sight-reading is playing music you have never seen. The secret is a short look first, then keeping the beat going whatever happens: a wrong note passes, a stop is heard by everyone.')}
{hero(ex('l_sr', 90, 'Thirty seconds first: one sharp (G major), 4/4, starts on G, steps up in a pattern.'), 'Look first, then never stop')}
{h3('The thirty-second scan')}
{tbl(['Check', 'Look for'], SCAN, ['30%', '70%'])}
<!--SPLIT-->
{inact('What do you check first?', qtagT(ex('l_sr2', 72)), ['<b>The key:</b> how many sharps?', '<b>The time:</b> how many beats?', '<b>The F in bar 2:</b> F or F♯?'], 'G major, 3/4. The F in bar 2 is <b>F♯</b>, from the key signature. Count “1 2 3” and go.')}
{inact('A wrong note in bar 2: now what?', bigq('Stop and fix it,<br>or keep going?', 22), ['<b>Is the beat</b> still going?', '<b>What does a listener</b> notice more?', '<b>So?</b>'], '<b>Keep going</b>: catch the next beat. A stop is heard far more than a wrong note.')}
{inact('Spot the pattern', qtagT(ex('l_sr', 70)), ['<b>Bar 1:</b> what shape?', '<b>Bar 2:</b> the same shape, where?', '<b>So</b>, how much do you really need to read?'], 'A <b>sequence</b>: bar 2 is bar 1 a step higher. Read the shape, not every note.')}
{game('Scan order', qitems(['rhythm', 'key', 'time', 'patterns'], 4), 'Put the four checks in the order of the scan.', 'key · time · rhythm · patterns.')}
{try10(ex('l_sr', 46), 'One new piece a day.', 'Pick something easy: scan for thirty seconds, then play it once, slowly, without stopping. Only then go back.')}
{howto('Read ahead', ['<b>While you play</b> one bar, let your eyes move to the next.', '<b>Practise it:</b> cover each bar with a card as you play it.', '<b>Read shapes</b> (steps, skips, chords), not single notes.'])}
{thinkt('Sight-reading is like reading aloud: you look a few words ahead, and if you trip on one, the sentence goes on.')}
{watch(['Choosing a speed you cannot keep: sight-read slowly.', 'Looking down at your hands: keep your eyes on the music.', 'Skipping the scan: thirty seconds of looking saves many wrong notes.'])}
{foot('Reading the notes p. {{P4}} · Repetition and sequence p. {{F2}}', 'Online: Sight-reading trainer')}''', 164)

# ---------- VIII.4 Listening ----------
SONGS = [['major 2nd', 'Frère Jacques (Frè-re)'], ['major 3rd', 'Oh When the Saints (Oh when)'], ['perfect 4th', 'Amazing Grace (A-ma)'], ['perfect 5th', 'Twinkle (twin-kle <b>TWIN</b>: the 2nd to the 3rd note)'], ['major 6th', 'My Bonnie (My Bon-)'], ['octave', 'Somewhere over the Rainbow (Some-where)']]
def ear():
    o = '<svg viewBox="0 0 560 160" style="width:100%;max-width:520px;height:auto;display:block;margin:0 auto">'
    o += f'<path d="M80,40 C80,10 140,10 140,50 C140,80 110,85 110,110 C110,135 80,135 80,120" fill="none" stroke="{N_}" stroke-width="5" stroke-linecap="round"/><path d="M98,50 C98,35 122,35 122,55" fill="none" stroke="{N_}" stroke-width="4" stroke-linecap="round"/>'
    for k, (a, b) in enumerate((('high or low? loud or soft?', 30), ('2 or 3 beats in a bar?', 64), ('major or minor?', 98), ('finished or not?', 132))):
        o += f'<path d="M170,{b} q20,-12 40,0 t40,0" fill="none" stroke="{R_}" stroke-width="2.5"/><text x="270" y="{b + 5}" font-family="AH,Arial" font-size="16" font-weight="700" fill="{N_}">{a}</text>'
    return o + '</svg>'
L4 = lpage(f'''{head('Part VIII · Playing and listening · 4', 'Listening', 'Your ear is a musical instrument too. Train it in small steps: clap a rhythm back, sing a tune back, then hear whether music goes up or down, is major or minor, and whether it has finished.')}
{hero(ear(), 'Questions for your ear')}
{h3('Major or minor?')}
{two(ex('l_maj', 74, 'C E G, then C E♭ G: bright, then darker.'), '<p>Only the middle note changes. Major usually sounds bright and open, minor darker or sadder. Sing the middle note of each and hear it drop.</p>')}
{h3('Intervals by song')}
{tbl(['Interval', 'The first two notes of…'], SONGS, ['30%', '70%'])}
<!--SPLIT-->
{inact('Finished or not?', qtagT(ex('l_cad', 80)), ['<b>Bar 1</b> ends on which chord?', '<b>Bar 2</b> ends on which chord?', '<b>Which ending</b> sounds finished?'], 'Bar 1 ends <b>home</b> on C (a perfect cadence: finished); bar 2 stops on G (imperfect: not finished).')}
{inact('Major or minor?', qtagT(ex('l_min', 66)), ['<b>Play the first chord.</b> Bright or dark?', '<b>The second?</b>', '<b>Which note</b> changed?'], 'First <b>minor</b>, then <b>major</b>: only the middle note moved, B♭ up to B.')}
{howto('Clap it back', ['<b>Someone claps</b> a rhythm of two bars.', '<b>You clap it back</b> straight away, keeping the beat.', '<b>Then sing back</b> a short tune, then find it on the keys.'])}
{game('Which song?', qitems(['5th up', 'octave up', '4th up'], 3), 'Name a song with that leap near the start.', '1 Twinkle · 2 Somewhere over the Rainbow · 3 Amazing Grace.')}
{try10(ex('l_min', 64), 'Bright or dark?', 'Ask someone to play major or minor chords in any order. Say “bright” or “dark” for each. Ten in a row?')}
{watch(['Guessing from the hands: close your eyes and listen.'])}
{foot('Intervals p. {{P7}} · Cadences p. {{M2}}', 'Online: Ear trainer')}''', 166)

# ---------- VIII.5 Performing ----------
STEPS = [['<b>Before</b>', 'warm up your hands; practise starting, not only the whole piece; play it to a friend or family first'], ['<b>At the piano</b>', 'adjust the bench; feet flat; breathe out; feel one bar of the beat in your head'],
         ['<b>If you slip</b>', 'keep the beat going; catch the next beat or the next phrase; never go back'], ['<b>After</b>', 'hands in your lap for a moment, stand, bow, smile']]
def stage():
    o = '<svg viewBox="0 0 560 170" style="width:100%;max-width:520px;height:auto;display:block;margin:0 auto">'
    for i, (t, s) in enumerate((('breathe', 'out, slowly'), ('feel the beat', 'one bar in your head'), ('begin', 'first note, calm'), ('bow', 'and smile'))):
        x = 20 + i * 135; y = 120 - i * 26
        o += f'<rect x="{x}" y="{y}" width="125" height="{150 - y}" rx="4" fill="{["#e9e9f5", "#fde3d8", "#f6c2ad", R_][i]}"/><text x="{x + 62}" y="{y - 22}" text-anchor="middle" font-family="AH,Arial" font-size="16" font-weight="700" fill="{N_}">{t}</text><text x="{x + 62}" y="{y - 6}" text-anchor="middle" font-family="AH,Arial" font-size="12.5" fill="#5a5d8f">{s}</text>'
    return o + '</svg>'
L5 = lpage(f'''{head('Part VIII · Playing and listening · 5', 'Performing', 'Playing for others is a skill you can practise, like scales. Nerves are normal: they mean you care. A routine before you start and a plan for slips make them much smaller.')}
{hero(stage(), 'Four steps to the first note')}
{tbl(['When', 'What you do'], STEPS, ['22%', '78%'])}
{rule('The listener follows the <b>beat</b> and the <b>mood</b>. Keep both going and a slip is forgotten in a second.')}
<!--SPLIT-->
{inact('How do you start?', bigq('You sit down.<br>Your heart is racing.', 22), ['<b>The bench:</b> right height, right distance?', '<b>Your breath:</b> in, then out slowly.', '<b>The beat:</b> what do you hear first?'], 'Adjust, breathe out, and <b>feel one bar</b> of the speed in your head. Then the first note.')}
{inact('You slip in bar 5: what now?', bigq('Bar 5: a wrong note,<br>and your hand freezes', 22), ['<b>Do you stop</b> and start again?', '<b>Where is the beat</b> now?', '<b>Where can you rejoin?</b>'], 'Keep counting and come back in on the <b>next beat</b>, or at the start of the next phrase. Never go back.')}
{drill('Every day this week, play your piece once from the start without stopping, whatever happens, as if someone were listening.')}
{howto('Practise performing', ['<b>Choose three starting places</b> in your piece and practise starting from each.', '<b>Play it through once a day</b> without stopping, whatever happens.', '<b>Play to someone</b>: a friend, family, a phone camera.'])}
{game('Help or not?', qitems(['going back', 'breathe first', 'keep the beat', 'rush to finish'], 4), 'Which help a performance?', '2 and 3 help; 1 and 4 do not.')}
{try10('<div style="font:700 24px AH,Arial;color:#26296b;text-align:center">breathe · beat · play · bow</div>', 'A one-minute concert.', 'Choose eight bars. Walk to the piano, sit, breathe, feel a bar, play, bow. Do it for someone today.')}
{extra('Playing from memory', '<p>Learn it in sections and know where each starts. Memory works best when it is <b>four kinds at once</b>: the sound, the feel in your fingers, the look of the page, and knowing the chords and the form.</p>')}
{thinkt('The audience wants you to do well: they are on your side from the first note.')}
{watch(['Starting before you are ready: breathe and feel the beat first.', 'Apologising with your face after a slip: keep going and nobody minds.'])}
{foot('Practising well p. {{L2}} · Expression p. {{E1}}', 'Online: Practice log')}''', 168)

LT = lpage(f'''{head('Part VIII · Playing and listening · Tips', 'When practice isn’t working', 'You practise every day and it is not getting better. Usually the practice, not the player, needs fixing: too fast, too long, or always from the top.')}
{box('Tip', '<b class="it">What you notice, what to check</b>' + tbl(['What you notice', 'Check', 'Turn to'], [['You stumble in the same place every time', '<b>the fingering:</b> write one in and keep it', 'p. {{L1}}'], ['It is fine slowly, wrong at speed', '<b>the ladder:</b> three correct, then one notch up', 'p. {{L2}}'], ['You play it from the top every time', '<b>small chunks</b>, hardest first', 'p. {{L2}}'], ['New pieces take forever to learn', '<b>the scan:</b> key, time, rhythm, patterns', 'p. {{L3}}'], ['You cannot hear your own mistakes', '<b>listening:</b> record yourself, sing it', 'p. {{L4}}'], ['It falls apart in front of people', '<b>a routine</b> and practising starts', 'p. {{L5}}']], ['38%', '48%', '14%']))}
{h3('Four ways to unstick practice')}
<div class="fixes">{''.join(f'<div><span class="rn">{i + 1}</span><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate([('Halve the speed', 'Whatever speed you use, try half. Correct and slow beats fast and wrong.'), ('Shorten the chunk', 'If two bars fail, try one. If one fails, try one beat.'), ('Take a break', 'Ten short sessions beat one long one. Your brain keeps learning between them.'), ('Ask a question', 'Write down what goes wrong, and take it to your teacher.')]))}</div>
{inact('Ten minutes left: what do you play?', bigq('One bar you keep missing,<br>and a whole piece you know', 21), ['<b>Which needs the time more?</b>', '<b>How many minutes</b> on the hard bar?', '<b>And</b> the last minutes?'], 'About <b>seven minutes</b> on the hard bar, slowly, then play the whole piece once at the end, for joy.')}
{thinkt('Practice does not make perfect: perfect practice does. Slow and correct is the fastest way.')}''', PM.PAGE['LT'])

def _out(fn, opener, pages, tips, prefix):
    body = ''.join(assemble(f'{prefix}{i + 1}', pg) for i, pg in enumerate(pages)) + tips
    open(f'/mnt/user-data/outputs/house-rooms/{fn}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{OPENCSS}</style></head><body>{opener}{body}{FLOWJS}</body></html>')
_out('handbook-shape', _oa('Part VII · How music is built', 'Shape and style', 'Step back from the notes and see the building: small ideas, repeated and moved, in sections that come and go, in the style of their time. Everything in this part is on this map.', 'F', PM.PAGE), (F1, F2, F3, F4, F5, F6), FT, 'F')
_out('handbook-play', _oa('Part VIII · At the piano', 'Playing and listening', 'Everything before this page is knowledge. This part turns it into playing: the right fingers, practice that works, reading at sight, a trained ear, and the calm to perform.', 'L', PM.PAGE), (L1, L2, L3, L4, L5), LT, 'L')
print('ok shape, play')
