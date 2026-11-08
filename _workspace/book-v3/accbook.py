# The Butler's Accompaniment Book, Levels 1-3 (her 8 Nov: "next"). Practical accompaniment: a tune plus three chords, made lovely.
# Lessons 1 and 4 come from the sample (acc.py); the rest are new. Two pages per lesson.
import json as _aj
exec(open('/tmp/claude-0/pk/acc.py').read())   # harmony helpers, the sample lessons L1 (Find the chord) and L2 (Your left hand joins in)
AV = _aj.load(open('/tmp/claude-0/pk/ex/accout.json'))
def kx(k, h=120, cap='', red=()):
    s = AV[k].replace('<svg ', f'<svg style="max-height:{h}px" ', 1)
    for n in red:
        for c in ('note', 'chord'): s = s.replace(f'<g id="{n}" class="{c}">', f'<g id="{n}" class="{c}" style="fill:#e4572e;color:#e4572e">', 1)
    return '<figure class="vx"><div class="vs">' + s + '</div>' + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>'
EV = _aj.load(open('/tmp/claude-0/pk/ex/eout.json'))
def ex(k, h=80, cap=''): return '<figure class="vx"><div class="vs">' + EV[k].replace('<svg ', f'<svg style="max-height:{h}px" ', 1) + '</div>' + (f'<figcaption>{cap}</figcaption>' if cap else '') + '</figure>'
_TAIL.update({'mkit': 2, 'drill': 1})
def makeit(t, extra=''): return f'<div class="mkit"><div class="bh">Make it yours</div><p>{t}</p>{extra}</div>'
def big(t, fs=22): return f'<div style="font:700 {fs}px AH,Arial;color:#26296b;text-align:center;line-height:1.4">{t}</div>'
LEVEL = {1: 'LEVEL 1 · FIND THE CHORD', 2: 'LEVEL 1 · FIND THE CHORD', 3: 'LEVEL 1 · FIND THE CHORD', 4: 'LEVEL 2 · THE LEFT HAND JOINS IN', 5: 'LEVEL 2 · THE LEFT HAND JOINS IN', 6: 'LEVEL 2 · THE LEFT HAND JOINS IN', 7: 'LEVEL 3 · MAKE IT MOVE', 8: 'LEVEL 3 · MAKE IT MOVE', 9: 'LEVEL 3 · MAKE IT MOVE'}
def bpage(inner, n, lab): return page(inner, n, lab).replace('THE PIANO BUTLER HANDBOOK', 'THE BUTLER’S ACCOMPANIMENT BOOK')
def lesson(no, text, n):
    text = text.replace("head('Lesson 1',", "head('Lesson 1',").replace("head('Lesson 2', 'Your left hand joins in'", "head('Lesson 4', 'Your left hand joins in'")
    a, b = text.split('<!--SPLIT-->')
    A = bpage(a, n, LEVEL[no]).replace('<section class="pg">', f'<section class="pg" data-flow="AL{no}">', 1)
    B = bpage(f'<div class="kick fk2">Lesson {no} · continued</div>' + b, n + 1, LEVEL[no]).replace('<section class="pg">', f'<section class="pg" data-flow="BL{no}">', 1)
    return A + B   # her rule: blocks flow from the second page back to fill the first (the Handbook's FLOWJS)
L1 = f"""{head('Lesson 1', 'Find the chord', 'Most simple tunes need only <b>three chords</b>. Count up the scale of C: C is note 1, F note 4, G note 5, so we call their chords <b>I</b>, <b>IV</b> and <b>V</b>. Your job is to choose one for each bar; the tune tells you which.')}
{hero('<div class="c3"><div>' + cakeman(('C', 'E', 'G'), (), 120, 'C') + '<b>I</b></div><div>' + cakeman(('F', 'A', 'C'), (), 120, 'F') + '<b>IV</b></div><div>' + cakeman(('G', 'B', 'D'), (), 120, 'G') + '<b>V</b></div></div>', 'The three cakes of C major')}
{rule('<b>Main notes</b> are the ones on beats 1 and 3, and the long ones. Find the cake that holds them. If two cakes fit, let your ear choose.')}
<!--SPLIT-->
{inaction('Choose a chord for each bar', qtag(kx('k_mary_q1')), ['<b>Bar 1:</b> the main notes are E and C. Which cake holds both?', '<b>Bar 3:</b> D D D. Which cake has a D in it?', '<b>Bars 2 and 4:</b> E E E, then E G G.'], 'Bars 1, 2 and 4 take <b>C</b> (C E G); bar 3 takes <b>G</b> (G B D).')}
{inaction('When two cakes fit', qtag(kx('k_two', 100) + '<div class="pair" style="justify-content:center;gap:20px">' + guestman(('C', 'E', 'G'), (), 50, 'C') + guestman(('G', 'B', 'D'), (), 50, 'G') + '</div>'), ['<b>Bar 4 leans on G.</b> Which cakes have a G in them?', '<b>Look at its other notes:</b> E. Which of the two cakes has an E?', '<b>Listen:</b> which sounds like coming home?'], 'G is in both cakes, but E is only in C: <b>C</b>, and it sounds like home after the G of bar 3.')}
{youknow('Mary Had a Little Lamb, with its chords', kx('k_mary_a', 92) + kx('k_mary_b', 92), 'Only <b class="co">two chords</b>, C and G, carry the whole tune. The chord names sit <b>above</b> the first note of each bar.', 'Play the tune and say the chord name at each bar.')}
{game('Which cake holds the bar?', qitems(['E D C D', 'D D D', 'G G G', 'F A F A'], 4), 'All in C major. Pick I (C), IV (F) or V (G) for each bar.', '1 C · 2 G · 3 C or G (G is in both: let your ear choose) · 4 F.')}
{game('Your turn: Twinkle', qitems(['C C G G', 'A A G', 'F F E E', 'D D C'], 4), 'Twinkle in C major. Choose I, IV or V for each half bar.', '1 C · 2 F, then C · 3 F, then C · 4 G, then C.')}
{try10(guestman(('G', 'B', 'D'), (), 64, 'G'), 'Find D in the cakes.', 'D is only in the G cake. B too. So whenever a bar leans on D or B, G is your chord.')}
{watch(['Choosing a chord for every note: one chord per bar (sometimes two) is plenty; the short notes between don’t need to belong to it.'])}
"""
L4 = f"""{head('Lesson 4', 'Your left hand joins in', 'Now the left hand plays the chord you chose. Start tiny: one note. When it feels easy, add a note. Then the whole cake. Same chord, three sizes.')}
{hero(kx('k_step3', 120), 'Same chord, three sizes')}
{tbl(['Step', 'The left hand plays', 'Sounds', 'Good for'], [['1', 'the bottom layer, called the <b>root</b>', 'light, simple', 'lullabies, first tries'], ['2', 'root and top layer (C and G)', 'strong, open', 'marches, folk songs'], ['3', 'the whole cake', 'full, warm', 'hymns, ballads, the last chord']], ['10%', '38%', '22%', '30%'])}
{two(kx('k_step1', 90, 'Step 1: the root.'), kx('k_step2', 90, 'Step 2: root and top.'))}
{rule('Pick the step that feels easy, play the tune with it, then move up one step. Nobody hears which step you use; everybody hears whether it is <b>steady</b>.')}
<!--SPLIT-->
{inaction('Make it pulse', qtag(kx('k_pulse_q')), ['<b>Choose the chords</b> for bars 2–4 (Lesson 1).', '<b>Bar 1</b> plays the root on every beat. Fill in bars 2–4 the same way.', '<b>How many notes</b> in each bar?'], 'C, G, C: <b>C C C C · G G G G · C C C C</b>, four roots in every bar.')}
{inaction('Step 2 on G', qtag(guestman(('G', '?', '?'), (), 64, 'G')), ['<b>Build the G cake:</b> skip one, take the next.', '<b>Step 2</b> keeps only two layers. Which two?', '<b>Play them</b> low in the left hand.'], 'The root and the top layer: <b>G and D</b>.')}
{drill('Left hand alone, step 1 then step 3: C for four beats, G for four beats, C for four beats. Ten times, steady.')}
{howto('Practise it in three rounds', ['<b>Round 1:</b> left hand alone, step 1, counting 1 2 3 4.', '<b>Round 2:</b> right hand tune with left hand step 1.', '<b>Round 3:</b> the same with step 2, then step 3.'])}
{game('Which step?', qitems(['a lullaby', 'a march', 'a hymn'], 3), 'Choose step 1, 2 or 3 for each.', '1 step 1 · 2 step 2 · 3 step 3 (any step can work: these are the usual choices).')}
{try10(guestman(('C', 'E', 'G'), (), 64, 'C'), 'Hold C, sing Mary.', 'Left hand holds C E G while you sing the first two bars. Then G B D for bar 3. You are accompanying!')}
{watch(['Rushing at the chord change: the new chord lands on beat 1, not before.', 'Playing the left hand as loud as the tune: the tune is the singer, the left hand the band.'])}
{thinkt('A band starts small: first the drummer, then the bass, then the whole band. Your left hand is all three, one step at a time.')}"""
SYM = [['<b>C</b>', 'C major', 'C E G'], ['<b>Am</b>', 'A minor (small m)', 'A C E'], ['<b>G7</b>', 'G seventh: one more layer', 'G B D F'], ['<b>F</b>', 'F major', 'F A C']]
L2n = f"""{head('Lesson 2', 'Read the chord symbols', 'Songbooks write the chords as letters above the tune: <b>chord symbols</b>. A letter alone is a major chord; a small <b>m</b> makes it minor; a <b>7</b> adds one more layer. Each symbol lasts until the next one.')}
{hero(kx('k_tw_lead', 120), 'Letters above the tune: the chords')}
{tbl(['Symbol', 'Say it', 'Notes (play one, skip one)'], SYM, ['18%', '42%', '40%'])}
{rule('A symbol <b>holds</b> until the next symbol. No new symbol at a bar line: keep the same chord.')}
<!--SPLIT-->
{inaction('How long does each chord last?', qtag(kx('k_tw_lead', 96)), ['<b>Bar 1:</b> one symbol. How many beats?', '<b>Bars 2–4:</b> two symbols in each bar. Where does the second one sit?', '<b>So</b> how many beats for each?'], 'C for the whole of bar 1 (4 beats); after that every chord lasts <b>2 beats</b>: F C, F C, G C.')}
{inaction('Spell Am', guestman(('A', '?', '?'), (), 72, 'Am'), ['<b>Start on A</b>, the bottom layer.', '<b>Skip one letter</b>, take the next. Then again.', '<b>The small m</b>: major or minor?'], '<b>A C E</b>: the A minor chord. On white keys, the cakes on C, F and G are major; on D, E and A they are minor. The symbol tells you which.')}
{inaction('What comes after the G?', qtag(kx('k_mary_q4', 92)), ['<b>Bar 3</b> says G. Which notes does the tune use?', '<b>Bar 4</b> has a ? Its main notes are E and G.', '<b>Which cake</b> holds E and G?'], 'Bar 3 is G (D D D); bar 4 goes home to <b>C</b>: C E G holds both E and G.')}
{game('Spell the chord', qitems(['G', 'Dm', 'F', 'Em'], 4), 'Write the three notes of each chord.', '1 G B D · 2 D F A · 3 F A C · 4 E G B.')}
{try10(big('C · Am · G7 · F'), 'Play the four symbols.', 'Play each chord as a whole cake, right hand: C, Am, G7, F. Say its name as you play it.')}
{watch(['Reading Am as A major: the small m means minor.', 'Changing chord at every bar line: a symbol lasts until the next one.', 'Playing G7 as plain G: the 7 adds one more layer, F, on top.', 'Playing every symbol as a loud block: the chords are the band, the tune is the singer.'])}
{makeit('Write the chord symbols above Mary Had a Little Lamb from memory (one per bar), then check them on page 2 and play them as whole cakes, right hand.')}
{thinkt('Chord symbols are a shopping list: they say what to buy, not how to cook it. How you play them is your recipe, and the next lessons are the cookbook.')}"""
KEYS = [['<b>C major</b>', 'C E G', 'F A C', 'G B D'], ['<b>G major</b>', 'G B D', 'C E G', 'D F♯ A'], ['<b>F major</b>', 'F A C', 'B♭ D F', 'C E G']]
L3n = f"""{head('Lesson 3', 'Three chords in G and F', 'Every major key has its own I, IV and V. In G major they are G, C and D; in F major F, B♭ and C. Find them the same way: from the home note, count up to the 4th and the 5th.')}
{hero('<div class="c3"><div>' + cakeman(('G', 'B', 'D'), (), 110, 'G') + '<b>I</b></div><div>' + cakeman(('C', 'E', 'G'), (), 110, 'C') + '<b>IV</b></div><div>' + cakeman(('D', 'F♯', 'A'), (1,), 110, 'D') + '<b>V</b></div></div>', 'The three cakes of G major')}
{tbl(['Key', 'I', 'IV', 'V'], KEYS, ['28%', '24%', '24%', '24%'])}
{rule('I is the home note, IV the 4th note up, V the 5th. Keep the key’s sharp or flat: the D chord in G major has <b>F♯</b>; the B♭ chord in F major has <b>B♭</b>.')}
<!--SPLIT-->
{inaction('Mary in G major', qtag(kx('k_mary_g', 92)), ['<b>The key:</b> one sharp, G major. Its cakes are G, C, D.', '<b>Bars 1 and 2</b> lean on B and G; <b>bar 4</b> on B and D. Which cake?', '<b>Bar 3:</b> A A A. Which cake has an A?'], '<b>G G D G</b>: the same plan as in C (I I V I), moved to G.')}
{inaction('Mary in F major', qtag(kx('k_mary_f', 92)), ['<b>The key:</b> one flat, F major. Its cakes are F, B♭, C.', '<b>Bars 1 and 2</b> lean on A and F; <b>bar 4</b> on A and C.', '<b>Bar 3:</b> G G G. Which cake has a G?'], '<b>F F C F</b>: again I I V I.')}
{inaction('Which key?', qtag(big('G · C · F &nbsp;&nbsp;|&nbsp;&nbsp; D · G · C &nbsp;&nbsp;|&nbsp;&nbsp; C · F · B♭', 20)), ['<b>Each group</b> is one key’s I, IV and V.', '<b>Find the chord</b> whose 4th and 5th are the other two: that is I.', '<b>Name</b> each key.'], '<b>C major</b> (C F G), <b>G major</b> (G C D), <b>F major</b> (F B♭ C): I names the key.')}
{howto('Find I, IV and V in any major key', ['<b>I:</b> the key’s home note (the key’s name).', '<b>IV and V:</b> count up its scale to the 4th and 5th notes.', '<b>Build each cake</b> with the key’s sharps or flats.'])}
{game('I, IV or V?', qitems(['V in G', 'IV in F', 'IV in C', 'IV in G'], 4), 'Name the chord.', '1 D · 2 B♭ · 3 F · 4 C.')}
{try10(guestman(('D', 'F♯', 'A'), (1,), 64, 'D'), 'I IV V I in G.', 'Right hand, whole cakes: G, C, D, G. Do you hear the F♯ in D?')}
{watch(['Forgetting the F♯ in the D chord (key of G).', 'Forgetting the B♭ in the B♭ chord (key of F).', 'Reading the key signature once and then forgetting it: it holds for the whole piece.'])}
{drill('I IV V I in each key, whole cakes in the right hand: C F G C · G C D G · F B♭ C F.')}
{makeit('Play Mary in all three keys, C, G and F, and say the chord names aloud as you play the tune. Which key suits your voice best for singing along?')}
{thinkt('A new key is a new house: the rooms are in the same places (I, IV, V); only the address changes.')}"""
PATS = [['whole bar', 'one long note or chord', 'calm, slow songs'], ['two per bar', 'on beats 1 and 3', 'walking songs'], ['four per bar', 'every beat', 'marches, bright songs'], ['root and 5th', 'C G C G (bottom and top layers)', 'country, folk, a bouncy bass']]
L5n = f"""{head('Lesson 5', 'Keep the beat', 'The left hand is the band’s drummer. Once the chords are right, give them a steady pattern: one long note, then two, then four. The tune stays the same; the feeling changes.')}
{hero(kx('k_pat3', 120), 'Semibreve, minims, crotchets: the band speeds up')}
{tbl(['Pattern', 'The left hand plays', 'Feels like'], PATS, ['24%', '40%', '36%'])}
{rule('Choose one pattern for a whole verse. Change it only at a new section. Before the tune starts, play <b>one bar</b> of your pattern on chord I: the singer hears the speed and the key.')}
<!--SPLIT-->
{inaction('Count the left hand', qtag(kx('k_mary_min', 96)), ['<b>Count 1 2 3 4</b> in each bar.', '<b>The left hand</b> plays on which counts?', '<b>How many notes</b> in each bar?'], 'Two minims in each bar, on <b>1 and 3</b>: a walking feel.')}
{inaction('Root and 5th', qtag(kx('k_rf', 96)), ['<b>Bars 1, 2, 4:</b> which two notes take turns?', '<b>Bar 3</b> (G): which two?', '<b>Which layers</b> of the cake are they?'], 'C and G, then <b>G and D</b>: the bottom and top layers of each cake, taking turns.')}
{inaction('Which pattern fits?', qtag(big('a lullaby &nbsp;·&nbsp; a march &nbsp;·&nbsp; a folk dance', 20)), ['<b>A lullaby</b> rocks gently: long or short notes?', '<b>A march</b> steps on every beat.', '<b>A folk dance</b> bounces.'], 'Lullaby: <b>whole bar</b> · march: <b>four per bar</b> · folk dance: <b>root and 5th</b>.')}
{howto('Practise a pattern', ['<b>Left hand alone</b>, counting aloud, until the pattern runs by itself.', '<b>Add the tune</b> slowly; the left hand never stops.', '<b>Try the same pattern</b> on another tune you know.'])}
{game('How many left-hand notes?', qitems(['whole bar, 4 bars', 'two per bar, 4 bars', 'four per bar, 2 bars', 'root and 5th, 2 bars'], 4), 'Count the left-hand notes.', '1 4 · 2 8 · 3 8 · 4 8.')}
{try10(big('C G C G · G D G D'), 'Mary with a bounce.', 'Play Mary with root and 5th: C G C G, and G D G D in bar 3. Keep the left hand lighter than the tune.')}
{watch(['Speeding up when the left hand gets busy: a metronome helps.', 'Changing pattern in the middle of a line: wait for a new section.'])}
{makeit('Play Twinkle four ways: whole bar, two per bar, four per bar, root and 5th. Choose the one you like best and write it above the music.')}
{thinkt('The same song can wear slippers, walking shoes or dancing shoes. The left-hand pattern is the shoes.')}"""
L6n = f"""{head('Lesson 6', 'Changing chords on time', 'The hardest moment is the change. The left hand must land on the new chord exactly on beat 1. The trick: look one bar ahead, and move during the last beat.')}
{hero(kx('k_mary_min', 120, 'Let go during beat 4 of bar 2; land on G on beat 1 of bar 3.', red=('n11', 'n15')), 'Move on beat 4, land on beat 1')}
{h3('Plan the move')}
<p>Every new root can be reached two ways: up or down. Choose the nearer one, so the hand barely moves. From G to C, for example: up is G A B C (three steps), down is G F E D C (four). Go <b>up</b>.</p>
{kx('k_moves', 100, 'Three roots, three small moves.')}
{rule('Look one bar ahead. <b>Move on beat 4, land on beat 1.</b> A late chord is heard; a plain one is not.')}
<!--SPLIT-->
{inaction('When do you move?', qtag(kx('k_mary_root', 92)), ['<b>Find the change:</b> C to G, between which bars?', '<b>On which beat</b> do you start to move?', '<b>On which beat</b> must you land?'], 'During <b>beat 4 of bar 2</b> move, and land on G on beat 1 of bar 3.')}
{inaction('Up or down to G?', qtag(big('from C: &nbsp; G above &nbsp; or &nbsp; G below?', 20)), ['<b>Up:</b> C D E F G, how many steps?', '<b>Down:</b> C B A G, how many?', '<b>Choose</b> the smaller move.'], '<b>Down</b>: three steps (C B A G) beats four steps up.')}
{inaction('Plan F, then G', qtag(big('C &nbsp;→&nbsp; F &nbsp;→&nbsp; G', 22)), ['<b>C to F:</b> up or down is nearer?', '<b>F to G:</b> one step up, or a long way down?', '<b>Play</b> the plan.'], 'C, <b>up</b> to F, then <b>up one step</b> to G: the hand walks, it never jumps.')}
{game('Up or down?', qitems(['C → F', 'C → G', 'F → G', 'G (below) → C'], 4), 'Choose the nearer move for the root.', '1 up · 2 down · 3 up · 4 up.')}
{try10(big('C → F → C → G → C'), 'Eyes ahead.', 'Play Mary with roots. On every beat 4, say the next chord’s name aloud, then move.')}
{howto('Practise the change', ['<b>Left hand alone:</b> play each root for four beats, moving on beat 4.', '<b>Add the tune</b> slowly; keep the left hand landing on beat 1.', '<b>Speed up</b> only when every change is on time.'])}
{watch(['Moving on beat 1: the chord arrives late.', 'Looking at the left hand: keep your eyes on the music, one bar ahead.', 'Jumping a long way for every chord: choose the nearer root, up or down.'])}
{drill('Left hand roots only: C F C G C, saying the next chord aloud on every beat 4. Ten times without a stop.')}
{makeit('Make a change map for Twinkle: write each chord change, the beat you move on, and up or down. Then try G7 instead of G in bar 7 of Mary: one more layer, the same root.')}
{thinkt('Like stepping onto an escalator: you lift your foot before the step arrives. ')}"""
L7n = f"""{head('Lesson 7', 'Broken chords', 'A broken chord plays the cake one layer at a time instead of all at once. The tune keeps singing; the left hand ripples underneath.')}
{hero(kx('k_broken', 130, 'A whole bar: bottom, middle, top, middle. Half a bar: two notes each, bottom and top.'), 'Bottom, middle, top, middle')}
{tbl(['Pattern', 'On C', 'Feels like'], [['up and back', 'C E G E', 'flowing, gentle'], ['up and hold', 'C E G (held)', 'calm, open'], ['spread', 'C G C G (wide)', 'a big, warm sound']], ['30%', '34%', '36%'])}
{kx('k_brk_pats', 100, 'Up and back, up and hold, spread.')}
{rule('Keep the bottom note a little stronger: it names the chord. The other layers stay soft and even.')}
<!--SPLIT-->
{inaction('Spell it broken', qtag(guestman(('F', 'A', 'C'), (), 64, 'F')), ['<b>Bottom, middle, top</b>: name them.', '<b>Then back</b> to the middle.', '<b>Write</b> the four notes.'], '<b>F A C A</b>: up and back.')}
{inaction('Which chord is broken here?', qtag(kx('k_brk_q', 80)), ['<b>Read the notes</b> in the bass clef.', '<b>Stack them</b>: bottom, middle, top.', '<b>Which cake</b> is it?'], 'G B D B: the <b>G chord</b>, broken up and back.')}
{inaction('Half a bar each', qtag(kx('k_broken', 92)), ['<b>Bar 2</b> has two chords, F then C.', '<b>How many beats</b> for each?', '<b>So</b> how many notes of each broken chord?'], 'Two beats each: <b>F C</b>, then <b>C G</b>, the bottom and top of each cake.')}
{game('Break these', qitems(['C', 'G', 'Am', 'F'], 4), 'Write each chord up and back.', '1 C E G E · 2 G B D B · 3 A C E C · 4 F A C A.')}
{try10(big('C E G E'), 'Ripple and sing.', 'Play Twinkle with broken chords, up and back, while you hum the tune. Then add the right hand.')}
{watch(['Every note the same loudness: lean a little on the bottom note.', 'Rushing the ripple: four even notes, one on each beat.'])}
{makeit('Invent your own broken pattern, for example bottom, top, middle, top, and play Mary with it. Give your pattern a name.')}
{thinkt('A broken chord is a cake served slice by slice: the same cake, just easier to enjoy.')}"""
L8n = f"""{head('Lesson 8', 'The waltz', 'In 3/4 the left hand dances: <b>oom-pah-pah</b>. The bottom layer on beat 1, the top two layers together on beats 2 and 3.')}
{hero(kx('k_oompah', 120), 'Oom on 1, pah pah on 2 and 3')}
{tbl(['Chord', 'Oom (beat 1)', 'Pah pah (beats 2, 3)'], [['<b>C</b>', 'C', 'E G'], ['<b>F</b>', 'F', 'A C'], ['<b>G</b>', 'G', 'B D']], ['30%', '30%', '40%'])}
{rule('<b>Upbeat:</b> a tune may start before beat 1, like “A-” in Amazing Grace. No chord yet: the left hand waits and comes in on beat 1 of the first full bar.')}
{rule('Beat 1 low and a little stronger; beats 2 and 3 light and short, like a skip.')}
<!--SPLIT-->
{inaction('Find the missing chord', qtag(kx('k_waltz_lead', 90)), ['<b>Amazing Grace</b> in C major, 3/4. It starts on an upbeat: no chord yet.', '<b>The bar with ?</b> leans on C and A.', '<b>Which cake</b> holds C and A?'], '<b>F</b> (F A C): “sweet the”. Then home to C.')}
{inaction('Write the oom-pah-pah', qtag(guestman(('G', 'B', 'D'), (), 64, 'G')), ['<b>Oom:</b> the bottom layer.', '<b>Pah pah:</b> the other two layers, together.', '<b>Write</b> beat by beat.'], '<b>G · B D · B D</b>.')}
{inaction('Oom-pah or oom-pah-pah?', qtag(big('2/4 &nbsp;&nbsp; 3/4 &nbsp;&nbsp; 4/4', 22)), ['<b>Count</b> the beats in each bar.', '<b>Oom</b> always takes beat 1.', '<b>How many pahs</b> follow?'], '2/4: oom-pah · 3/4: <b>oom-pah-pah</b> · 4/4: oom-pah-oom-pah.')}
{game('Waltz it', qitems(['C', 'F', 'G', 'Am'], 4), 'Write oom · pah pah for each chord.', '1 C · E G · 2 F · A C · 3 G · B D · 4 A · C E.')}
{youknow('Amazing Grace, with its waltz', kx('k_waltz', 120), 'The left hand waits through the upbeat, then dances <b class="co">oom-pah-pah</b> on C, C, F, C.', 'Sing the words while your left hand plays.')}
{try10(big('oom · pah · pah'), 'Dance first.', 'Say “oom-pah-pah” and step on “oom”. Then play C, F, G, C with the left hand only.')}
{watch(['A heavy pah: beats 2 and 3 are lighter than beat 1.', 'Rushing the change: the new oom lands on beat 1.'])}
{drill('Oom-pah-pah on C, F, G, C, two bars each, with a metronome at a slow speed. Keep the pahs light.')}
{makeit('Play Amazing Grace with oom-pah-pah, then end with a rolled C chord: play C E G from the bottom up, quickly, and hold it.')}
{thinkt('A waltz is a dancer: one big step, two little ones, round and round.')}"""
L9n = f"""{head('Lesson 9', 'Alberti bass', 'Low, high, middle, high: the <b>Alberti bass</b> keeps quavers rocking under a slow tune. Mozart loved it, and it makes the plainest melody sound elegant.')}
{hero(kx('k_alb', 120), 'Low, high, middle, high')}
{tbl(['Chord', 'Alberti (two beats)', 'The order'], [['<b>C</b>', 'C G E G', 'bottom, top, middle, top'], ['<b>F</b>', 'F C A C', 'bottom, top, middle, top'], ['<b>G</b>', 'G D B D', 'bottom, top, middle, top']], ['18%', '36%', '46%'])}
{kx('k_alb_pats', 100, 'C, F and G as Alberti bass.')}
{rule('Keep the quavers <b>even and soft</b>; let only the bottom note lean a little. The tune always sings louder.')}
<!--SPLIT-->
{inaction('Write it for F', qtag(guestman(('F', 'A', 'C'), (), 64, 'F')), ['<b>Bottom</b>, then <b>top</b>.', '<b>Middle</b>, then <b>top</b> again.', '<b>Write</b> the four notes.'], '<b>F C A C</b>.')}
{inaction('Count the rocks', qtag(kx('k_alb', 92)), ['<b>Count the quavers</b> in bar 1.', '<b>One rock</b> is four quavers.', '<b>How many rocks</b> in a bar?'], 'Eight quavers: <b>two rocks</b> per bar of 4/4.')}
{youknow('Mozart, Sonata in C, K. 545', ex('f_alb', 80), 'The right hand sings; the left hand rocks <b class="co">C G E G</b>, then D G F G (a G7 chord, its notes rearranged): the most famous Alberti bass of all.', 'Play the left hand alone, softly and evenly.')}
{game('Rock these', qitems(['C', 'G', 'Am', 'F'], 4), 'Write each chord as an Alberti bass.', '1 C G E G · 2 G D B D · 3 A E C E · 4 F C A C.')}
{try10(big('C G E G'), 'Slow rocks first.', 'Play C G E G slowly, four times, with a steady pulse. Then F C A C, G D B D. Then put Ode to Joy on top.')}
{watch(['Loud quavers: the Alberti bass whispers.', 'Uneven rocks: practise with a metronome, slowly.', 'Using it for a fast, busy tune: Alberti suits slow, singing melodies.'])}
{drill('Alberti on C, F, G, C, one bar each, slowly and evenly. Then twice as fast, still soft.')}
{makeit('Play Twinkle with an Alberti bass in C, then in G (G D B D, C G E G, D A F♯ A).')}
{thinkt('An Alberti bass is a rocking chair: steady, gentle, never in a hurry. If the chair speeds up, the tune can’t settle.')}"""
LV = [['<b>1</b>', 'Find the chord', 'I, IV and V; chord symbols; three keys', '1–3'], ['<b>2</b>', 'The left hand joins in', 'root, 5th, whole cake; steady patterns; changes on time', '4–6'], ['<b>3</b>', 'Make it move', 'broken chords, the waltz, Alberti bass', '7–9'],
      ['<b>4</b>', 'Smooth hands', 'inversions; the shared note stays', 'later'], ['<b>5</b>', 'Colours', 'sus, add9, 6, maj7', 'later'], ['<b>6</b>', 'Style patterns', 'ballad, pop, march, bossa nova, stride', 'later'], ['<b>7</b>', 'Reharmonise', 'new chords for an old tune', 'later'], ['<b>8</b>', 'Lead sheets', 'intros, endings, accompanying a singer', 'later']]
INTRO = bpage(f"""<div class="kick">The Butler’s Accompaniment Book</div><h1>A tune and three chords</h1>
<p class="lead">Give me a melody and three chords, and I will make it sound lovely. This book teaches the left hand (and later both hands) to accompany any simple tune: first find the chords, then give them a pattern, then make them move.</p>
{h3('Every lesson')}
<div class="steps3"><div><span class="rn">1</span><b>See it</b><span>One picture shows the new pattern.</span></div><div><span class="rn">2</span><b>Work it out</b><span>Examples ask; you answer, then check the result line.</span></div><div><span class="rn">3</span><b>Play it on a tune</b><span>A tune everyone knows, in its simplest form.</span></div></div>
{h3('The levels')}
{tbl(['Level', 'Title', 'What you learn', 'Lessons'], LV, ['10%', '26%', '46%', '18%'])}
{howto('How to practise a lesson', ['<b>Hands separately:</b> the tune alone, then the left hand alone, counting aloud.', '<b>Together, slowly:</b> the tune sings, the left hand stays softer.', '<b>Make it yours:</b> try the pattern on another tune you know.'])}
<p class="sm"><b>Tunes in Levels 1–3:</b> Mary Had a Little Lamb, Twinkle, Twinkle, Little Star, Ode to Joy, Au clair de la lune, Amazing Grace, and Mozart’s Sonata in C. All are free to play and share.</p>
<p class="sm">You need to read notes in both clefs and know what a chord is: the Handbook explains chords (p. {PM.PAGE['H1']}), chords in a key (p. {PM.PAGE['H3']}) and chords under a melody (p. {PM.PAGE['M3']}).</p>""", 1, 'INTRODUCTION')
css += '.mkit{border:2px dashed #e4572e;border-radius:10px;padding:8px 14px;margin:10px 0;background:#fff7f3} .mkit .bh{font-size:11px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:#e4572e} .mkit p{margin:2px 0 0;font-size:15px;color:#26296b}'
css += '.steps3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px} .steps3>div{display:flex;flex-direction:column;gap:3px;font-size:14px;line-height:1.45;color:#3d4080} .steps3 b{font-size:15px;color:#26296b} .rn{display:inline-flex;width:24px;height:24px;border-radius:50%;background:#e4572e;color:#fff;font-weight:700;align-items:center;justify-content:center;font-size:13px} .vs .harm text,.vs g.harm{font-family:AH,Arial;font-weight:700}'
L1 = L1 + "\n" + makeit('Choose chords for Au clair de la lune: C C C D | E (2) D (2) | C E D D | C (4). Write one chord per bar, or two where the bar changes, then play it.')
L4 = L4 + "\n" + makeit('Accompany a song you know: first with step 1, then step 3. Which step makes it sound fullest?')
LS = [L1, L2n, L3n, L4, L5n, L6n, L7n, L8n, L9n]
PAGES = INTRO + ''.join(lesson(i + 1, t, 2 + 2 * i) for i, t in enumerate(LS))
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{OPENCSS}</style></head><body>{PAGES}{_flowjs}</body></html>'
open('/mnt/user-data/outputs/house-rooms/accompaniment-book.html', 'w').write(html)
print('ok accompaniment book', len(LS), 'lessons')
