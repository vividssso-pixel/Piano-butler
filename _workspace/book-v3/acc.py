# The Butler's Accompaniment Book: a two-lesson sample (her 7 Nov: practical accompaniment, simple tunes made lovely)
exec(open('/tmp/claude-0/pk/harmony.py').read())
def apage(inner, n): return page(inner, n, 'SAMPLE · LEVEL 1').replace('THE PIANO BUTLER HANDBOOK', 'THE BUTLER’S ACCOMPANIMENT BOOK')
def step(n, k, cap): return f'<div class="stp"><span class="sn">Step {n}</span>{px(k, 140)}<p>{cap}</p></div>'
css += """
.stp{border:2px solid #e3e1ee;border-radius:10px;padding:8px 12px;margin:6px 0} .stp .sn{display:inline-block;background:#e4572e;color:#fff;font-weight:700;font-size:12px;border-radius:10px;padding:2px 10px} .stp p{margin:2px 0 0;font-size:14px} .stp .vx{border:0;margin:0}
.c3{display:flex;justify-content:center;gap:26px} .c3>div{text-align:center} .c3 b{display:block;font-family:PF,serif;font-size:20px;color:#26296b}
"""
L1 = (f"""{head('Lesson 1', 'Find the chord', 'Most simple tunes need only <b>three chords</b>: I, IV and V. Your job is to choose one for each bar. The tune tells you which: look at its main notes and pick the cake that holds them.')}
{hero('<div class="c3"><div>' + cakeman(('C', 'E', 'G'), (), 120, 'C') + '<b>I</b></div><div>' + cakeman(('F', 'A', 'C'), (), 120, 'F') + '<b>IV</b></div><div>' + cakeman(('G', 'B', 'D'), (), 120, 'G') + '<b>V</b></div></div>', 'The three cakes of C major: between them they hold every note of the scale')}
{rule('<b>Main notes</b> are the ones on beat 1 and beat 3, and the long ones. Find the cake that holds them. If two cakes fit, let your ear choose.')}
{inaction('Choose a chord for each bar', ask(px('acc_q', 100), (), False), ['<b>Bar 1:</b> the main notes are E and C. Which cake holds both?', '<b>Bar 3:</b> D D D. Which cake has a D in it?', '<b>Write a chord name</b> where each ? is.'], 'Bars 1, 2 and 4 take <b>C</b> (C E G holds E, C and G). Bar 3 takes <b>G</b> (G B D holds D).')}
{youknow('Mary Had a Little Lamb, with its chords', ask(px('acc_mary', 110), (), True) + '<p class="mel" style="font-size:18px;word-spacing:6px">C | C | G | C | C | C | G | C</p>', 'Only <b class="co">two chords</b>, C and G, carry the whole tune. The chord names sit under the first note of each bar.', 'Play the tune with your right hand and say the chord name at the start of each bar.')}
<!--SPLIT-->
{inaction('When two cakes fit', '<div class="pair" style="justify-content:center;gap:20px">' + guestman(('C', 'E', 'G'), (2,), 70, 'C') + guestman(('G', 'B', 'D'), (0,), 70, 'G') + '</div>', ['<b>The bar is G G G.</b> Which cakes have a G in them?', '<b>Look at the bar before</b> and the bar after: which chord are they?', '<b>Play both</b> and choose: staying put, or moving?'], 'Both C and G hold G. After a C bar, staying on <b>C</b> sounds calm; moving to <b>G</b> sounds like the tune is going somewhere. Both are right: you choose the mood.')}
{game('Which cake holds the bar?', qitems(['E D C D', 'D D D', 'G G G', 'F A F A'], 4), 'All in C major. Pick I (C), IV (F) or V (G) for each bar.', '1 C · 2 G · 3 C or G (G is in both: let your ear choose) · 4 F.')}
{game('Your turn: Twinkle', qitems(['C C G G', 'A A G', 'F F E E', 'D D C'], 4), 'Twinkle in C major. Choose I, IV or V for each half bar.', '1 C · 2 F, then C · 3 F, then C · 4 G, then C.')}
{watch(['Choosing a chord for every single note: one chord per bar (sometimes two) is plenty.', 'Using the passing notes: the short notes between the main ones can belong to any chord.'])}
{thinkt('Like choosing shoes for an outfit: you look at the big pieces, not every button.')}
{try10(guestman(('G', 'B', 'D'), (), 70, 'G'), 'Find D in the cakes.', 'D is only in the G cake. B too. So whenever a bar leans on D or B, G is your chord.')}""")
L2 = (f"""{head('Lesson 2', 'Your left hand joins in', 'Now the left hand plays the chord you chose. Start tiny: one note. When it feels easy, add a note. Then the whole cake. Same chord, three sizes.')}
{step(1, 'acc_root', 'Just the <b>bottom layer</b>: the chord’s own name note, held for the whole bar.')}
{step(2, 'acc_five', 'Add the <b>top layer</b>: bottom and top together (C and G). Strong and open.')}
{step(3, 'acc_block', 'The <b>whole cake</b>: all three notes at once. Full and warm.')}
{rule('Pick the step that feels easy, play the tune with it, then move up one step. Nobody hears which step you use; everybody hears whether it is <b>steady</b>.')}
{tbl(['Step', 'Sounds', 'Good for'], [['1 · bottom layer', 'light, simple', 'lullabies, first tries'], ['2 · bottom + top', 'strong, open', 'marches, folk songs'], ['3 · whole cake', 'full, warm', 'hymns, ballads, the last chord']], ['30%', '30%', '40%'])}
<!--SPLIT-->
{inaction('Make it pulse', qtag(px('acc_pulse', 96)), ['<b>Choose the chords</b> for Mary (Lesson 1): C C G C.', '<b>Play the bottom layer</b> on every beat instead of holding it. How many notes in each bar?', '<b>Keep the right hand</b> playing the tune on top.'], 'Four even notes per bar: <b>C C C C</b>, then G G G G in bar 3. The left hand is now the drummer, and the tune sounds alive.')}
{inaction('Step 2 on G', guestman(('G', '?', '?'), (), 72, 'G'), ['<b>Build the G cake:</b> skip one, take the next.', '<b>Step 2</b> keeps only two layers. Which two?', '<b>Play them</b> low in the left hand.'], 'The bottom and top layers: <b>G and D</b>. The middle B can wait for step 3.')}
{howto('Practise it in three rounds', ['<b>Round 1:</b> left hand alone, step 1, counting 1 2 3 4.', '<b>Round 2:</b> right hand tune with left hand step 1.', '<b>Round 3:</b> the same with step 2, then step 3.'])}
{watch(['Rushing at the chord change: the left hand moves on beat 1, not before.', 'Playing the left hand as loud as the tune: the tune is the singer, the left hand the band.'])}
{thinkt('A band starts small: first the drummer, then the bass, then the whole band. Your left hand is all three, one step at a time.')}
{try10(guestman(('C', 'E', 'G'), (), 70, 'C'), 'Hold C, sing Mary.', 'Left hand holds C E G while you sing the first two bars. Then switch to G B D for bar 3. You are accompanying!')}""")
def split2(t, n, kick):
    a, b = t.split('<!--SPLIT-->')
    return apage(a, n) + apage(f'<div class="kick">{kick} · continued</div>' + b, n + 1)
PAGES = split2(L1, 1, 'Lesson 1') + split2(L2, 3, 'Lesson 2')
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{FF}</style><style>{css}{MINCSS}{OPENCSS}</style></head><body>{PAGES}{_flowjs}</body></html>'
open('/mnt/user-data/outputs/house-rooms/accompaniment-sample.html', 'w').write(html)
print('ok acc')
