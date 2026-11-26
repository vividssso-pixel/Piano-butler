# Music Box 2: fourteen pages. Every melody here was checked against an open score before it went in (see SOURCES).
# Usage: python3 mbox2.py  -> mc1.json ... mc14.json
import json, copy
base = json.load(open('mb19.json'))
def B(r, lp='', ch='', f='', l='', show='', pick=0):
    d = {'r': r, 'w': ''}
    if pick: d['pick'] = pick
    if lp: d['lp'] = lp
    if l: d['l'] = l
    if ch: d['ch'] = ch
    if f: d['f'] = f
    if show: d['show'] = show
    return d
Cc, Fc, Gc = 'C+E+G', 'C+F+A', 'B+D+G'
TICKS = ['Left hand alone', 'Right hand alone', 'Hands together', 'Three times through']
S = []
def song(title, beats, stage, job, lcap, rcap, how, ready, lkb, rkb, lines, unit='q', counts=None, src='', ticks=None, composer=''):
    S.append(dict(title=title, beats=beats, stage=stage, job=job, lcap=lcap, rcap=rcap, how=how, ready=ready, lkb=lkb, rkb=rkb, lines=lines, unit=unit, counts=counts, src=src, ticks=ticks or TICKS, composer=composer))

# 1 ------------------------------------------------------------------ UNIT 1: letters inside the notes
song('All My Little Ducklings', 4, 'heads',
 'Welcome to Music Box 2. Two new things today. The letters now sit <b>inside the notes</b>. And the left hand plays its first whole chord: <b>three keys at once</b>.',
 'The C chord: C, E and G together, fingers 5, 3 and 1. F alone with finger 2. G alone with the thumb.',
 'Thumb on middle C. A is one key past your little finger: reach for it, then come back.',
 'A black note lasts one box. A white note with a stem lasts two. A white note with no stem fills the whole bar. Press the chord on beat 1 and hold it down.',
 'all three keys of the C chord go down at the same moment.',
 ['c', 5, '5 . 3 2 1'], ['c', 6, '1 2 3 4 5 x'],
 [[B('C D E F', l=Cc, ch='C', f='1 2 3 4'), B('G - G -', l=Cc, ch='C', f='5'), B('A A A A', l='F', ch='F', f='5'), B('G - - -', l=Cc, ch='C', f='5')],
  [B('A A A A', l='F', ch='F', f='5'), B('G - - -', l=Cc, ch='C', f='5'), B('F F F F', l='G', ch='G', f='4'), B('E - E -', l=Cc, ch='C', f='3')],
  [B('D D D D', l='G', ch='G', f='2'), B('C - - -', l=Cc, ch='C', f='1')]],
 src='Essen folk-song collection (Alle meine Entchen)', composer='Traditional, Germany')

# 2
P4 = B('r r r C.D', f='- - - 1.2', pick=1)
song('Oh! Susanna', 4, 'heads',
 'One new chord: <b>G</b>. And the song starts <b>before</b> bar 1, with two quick notes on beat 4. Count 1 2 3 out loud, then play C D on <i>four-and</i>.',
 'New: the G chord, B D G (5 3 1). From the C chord, the two lower fingers each step down one key. The thumb stays on G.',
 'Thumb on middle C. Reach finger 5 to A, as in Song 1.',
 'Two notes joined by a beam share one box: say <i>four-and</i>. A dot after a note makes it longer: hold it into the next box, and the small note after it comes on <i>and</i>.',
 'you can change from C to G and back without looking down.',
 ['b', 6, '5 x 3 x 2 1'], ['c', 6, '1 2 3 4 5 x'],
 [[P4, B('E G G -.A', l=Cc, ch='C', f='3 5 - -.5'), B('G E C D', l=Cc, ch='C', f='5 3 1 2'), B('E E D C', l=Cc, ch='C', f='3 - 2 1'), B('D - - C.D', l=Gc, ch='G', f='2 - - 1.2')],
  [B('E G G -.A', l=Cc, ch='C', f='3 5'), B('G E C D', l=Cc, ch='C', f='5 3 1 2'), B('E E D D', lp=f'{Cc} - {Gc} -', ch='C - G -', f='3 - 2 -'), B('C - - -', l=Cc, ch='C', f='1')],
  [B('F - F -', l='F', ch='F', f='4'), B('A A - A', l='F', ch='F', f='5'), B('G G E C', l=Cc, ch='C', f='5 - 3 1'), B('D - - C.D', l=Gc, ch='G', f='2 - - 1.2')],
  [B('E G G -.A', l=Cc, ch='C', f='3 5'), B('G E C D', l=Cc, ch='C', f='5 3 1 2'), B('E E D D', lp=f'{Cc} - {Gc} -', ch='C - G -', f='3 - 2 -'), B('C - - -', l=Cc, ch='C', f='1')]],
 src='Nottingham Music Database (Oh Susanna)', composer='Stephen Foster, 1848')

# 3
song('Little Brown Jug', 4, 'heads',
 'The last of the three chords: <b>F</b>. Now you own C, F and G, and with these three you can play hundreds of songs. Here they come in a row: C, F, G, C.',
 'New: the F chord, C F A (5 2 1). From the C chord, finger 5 stays on C. The other two step up.',
 'Start with the thumb on E. A coral arrow ↑ on a note means the <b>higher</b> key of that name. In bar 4 the thumb jumps up to high C; in bar 5 it jumps back to E.',
 'Say the chord names out loud as you change: <i>C, F, G, C</i>. Lines 1 and 2 are the verse. Lines 3 and 4 are the chorus: its first bar tumbles down the C chord from the top.',
 'you can play C, F, G, C four times round with the left hand alone, eyes closed.',
 ['c', 6, '5 . x 2 x 1'], ['e', 8, '1 2 3 4 5 x x x'],
 [[B('E G G -', l=Cc, ch='C', f='1 3'), B('F A A -', l=Fc, ch='F', f='2 4'), B('B.B B A B', l=Gc, ch='G', f='5.5 5 4 5'), B("C' D' E' -", l=Cc, ch='C', f='1 2 3')],
  [B('E G G -', l=Cc, ch='C', f='1 3'), B('F A A -', l=Fc, ch='F', f='2 4'), B('B.B B A B', l=Gc, ch='G', f='5.5 5 4 5'), B("D' C' C' -", l=Cc, ch='C', f='2 1')],
  [B("E' C' G E", l=Cc, ch='C', f='5 3 2 1'), B('F A A -', l=Fc, ch='F', f='2 4'), B('B.B B A B', l=Gc, ch='G', f='5.5 5 4 5'), B("C' D' E' -", l=Cc, ch='C', f='1 2 3')],
  [B("E' C' G E", l=Cc, ch='C', f='5 3 2 1'), B('F A A -', l=Fc, ch='F', f='2 4'), B('B.B B A B', l=Gc, ch='G', f='5.5 5 4 5'), B("D' C' C' -", l=Cc, ch='C', f='2 1')]],
 src='Nottingham Music Database (Little Brown Jug)', composer='Joseph Winner, 1869')

# 4
song('Deck the Halls', 4, 'heads',
 'Same three chords, but now they sometimes change <b>in the middle of a bar</b>. Look ahead: when you see a new chord on beat 3, get the fingers ready on beat 2.',
 'C, F and G, as before. Nothing new for the fingers; something new for the eyes.',
 'Little finger starts on G. In bars 4 and 8, finger 2 steps <b>over</b> the thumb to play B, the key below middle C: an arrow ↓ marks it. An arrow ↑ marks the high C.',
 'Four lines. Lines 1, 2 and 4 start the same way, so you only have three bars to learn fresh. Find them first.',
 'the chord changes on beat 3 arrive on time, not late.',
 ['b', 7, 'x 5 x 3 x 1 x'], ['b', 9, 'x 1 2 3 4 5 x x x'],
 [[B('G -.F E D', l=Cc, ch='C', f='5 -.4 3 2'), B('C D E C', l=Cc, ch='C', f='1 2 3 1'), B('D.E F.D E -.D', lp=f'{Gc} - {Cc} -', ch='G - C -', f='2.3 4.2 3 -.2'), B('C B, C -', lp=f'{Cc} {Gc} {Cc} -', ch='C G C', f='1 2 1')],
  [B('G -.F E D', l=Cc, ch='C', f='5 -.4 3 2'), B('C D E C', l=Cc, ch='C', f='1 2 3 1'), B('D.E F.D E -.D', lp=f'{Gc} - {Cc} -', ch='G - C -', f='2.3 4.2 3 -.2'), B('C B, C -', lp=f'{Cc} {Gc} {Cc} -', ch='C G C', f='1 2 1')],
  [B('D -.E F D', l=Gc, ch='G', f='2 -.3 4 2'), B('E -.F G D', l=Cc, ch='C', f='3 -.4 5 2'), B("E.F G A.B C'", lp=f'{Cc} - {Fc} -', ch='C - F -', f='1.2 3 1.2 3'), B('B A G -', l=Gc, ch='G', f='2 1 2')],
  [B('G -.F E D', l=Cc, ch='C', f='5 -.4 3 2'), B('C D E C', l=Cc, ch='C', f='1 2 3 1'), B('A.A A.A G -.F', lp=f'{Fc} - {Cc} -', ch='F - C -', f='5.5 5.5 4 -.3'), B('E D C -', lp=f'{Cc} {Gc} {Cc} -', ch='C G C', f='3 2 1')]],
 src='Nottingham Music Database (Nos Galan), bars 1 to 12', composer='Traditional, Wales')

# 5
W = lambda c: {'C': 'C E+G E+G', 'F': 'C F+A F+A', 'G': 'B D+G D+G'}[c]
def N(r, c, f=''): return B(r, lp=W(c), ch=c, f=f)
song('The First Noel', 3, 'heads',
 'Three beats in a bar, and a new way to play a chord: <b>bottom key first, then the top two, twice</b>. Low, high, high. This is a waltz left hand.',
 'The same chords, split in two. Beat 1: the bottom key alone, finger 5. Beats 2 and 3: the top two keys together.',
 'This tune is the C scale. Going up, after E the <b>thumb tucks under</b> to F. Coming down, after F finger 3 steps <b>over</b> to E. An arrow ↑ marks the high C.',
 'Count <b>1 2 3</b>. The song starts on beat 3 with two quick notes. Lean a little on beat 1; keep beats 2 and 3 light.',
 'the left hand keeps low, high, high going while you say the count out loud.',
 ['b', 7, 'x 5 x 3 x 1 x'], ['c', 8, '1 2 3 1 2 3 4 5'],
 [[B('r r E.D', f='- - 3.2', pick=1), N('C -.D E.F', 'C', '1 -.2 3.1'), N('G - A.B', 'C', '2 - 3.4'), N("C' B A", 'F', '5 4 3'), N('G - A.B', 'C', '2 - 3.4')],
  [N("C' B A", 'F', '5 4 3'), N('G A B', 'G', '2 3 4'), N("C' G F", 'C', '5 2 1'), N('E - E.D', 'C', '3 - 3.2')],
  [N('C -.D E.F', 'C', '1 -.2 3.1'), N("G - C'.B", 'C', '2 - 5.4'), N('A - A', 'F', '3'), N('G - G', 'C', '2')],
  [N("C' B A", 'F', '5 4 3'), N('G A B', 'G', '2 3 4'), N("C' G F", 'C', '5 2 1'), B('E - -', l=Cc, ch='C', f='3')]],
 src='Mutopia Project (The First Noel, soprano)', composer='Traditional, England')

# 6 ------------------------------------------------------------------ UNIT 2: the notes climb onto five lines
Gg, Cg, Dg = 'G+B+D', 'G+C+E', 'F#+A+D'
song('Good King Wenceslas', 4, 'staff',
 'The boxes have turned into <b>five lines</b>. A note higher on the lines is a key further to the right. The letters are still inside, so you cannot get lost. And home has moved: this song lives on <b>G</b>.',
 'G chord: G B D (5 3 1). C chord: G C E (5 2 1), the bottom key stays. D chord: F♯ A D (5 3 1), finger 5 slips down to the black key.',
 'Two places for the hand. Low place: thumb on D, and finger 3 plays the black key F♯. High place: thumb on G. The numbers show each jump.',
 '<b>Play line 1 twice</b>, then go on. Watch the shape of the tune: up, down or the same line. The ♯ before a note means the black key just to its right. In this song every F is F♯.',
 'you can point to any note and say whether the next one goes up, down or stays.',
 ['f', 7, '. 5 x 3 x 1 x', {'0': ' '}], ['d', 8, '1 2 . 4 5 x x x', {'2': '3'}],
 [[B('G G G A', l=Gg, ch='G', f='4 - - 5'), B('G G D -', l=Gg, ch='G', f='4 - 1'), B('E D E F#', lp=f'{Cg} - - {Dg}', ch='C - - D', f='2 1 2 3'), B('G - G -', l=Gg, ch='G', f='4')],
  [B("D' C' B A", lp=f'{Gg} - {Dg} -', ch='G - D -', f='5 4 3 2'), B('B A G -', lp=f'{Gg} {Dg} {Gg} -', ch='G D G', f='3 2 1'), B('E D E F#', lp=f'{Cg} - - {Dg}', ch='C - - D', f='2 1 2 3'), B('G - G -', l=Gg, ch='G', f='4')],
  [B('D D E F#', lp=f'{Gg} - {Cg} {Dg}', ch='G - C D', f='1 - 2 3'), B('G G A -', lp=f'{Gg} - {Dg} -', ch='G - D -', f='4 - 5'), B("D' C' B A", lp=f'{Gg} - {Dg} -', ch='G - D -', f='5 4 3 2'), B("G - C' -", lp=f'{Gg} - {Cg} -', ch='G - C -', f='1 - 4')],
  [B('G - - -', l=Gg, ch='G', f='1')]],
 src='Nottingham Music Database (GKW); Mutopia Project', composer='Tune from 1582; words J. M. Neale, 1853')

# 7
BR = lambda c: {'C': 'C E G', 'F': 'C F A', 'G': 'B D G'}[c]
def R(r, c, f=''): return B(r, lp=BR(c), ch=c, f=f)
song('Silent Night', 3, 'staff',
 'The left hand opens the chord like a fan: <b>one key on each beat</b>, bottom, middle, top. The same three chords you know, played one finger at a time.',
 'C: C E G. F: C F A. G: B D G. Fingers 5, then 3 (or 2 for F), then 1. Keep the hand still; only the fingers move.',
 'Three places. Lines 1 to 4: thumb on E for the low bars, thumb on G for the high ones. Line 5 climbs: thumb on B. The numbers show each change.',
 'Slow and rocking. A dot after a note makes it longer: hold it past the next beat, then the short note slips in just before the beat after.',
 'the left hand rocks 5, 3, 1 without a bump while the right hand holds a long note.',
 ['b', 7, 'x 5 x 3 x 1 x'], ['c', 11, 'x x 1 2 3 4 5 x x x x', None, 290],
 [[R('G -.A G', 'C', '3 -.4 3'), R('E - -', 'C', '1'), R('G -.A G', 'C', '3 -.4 3'), R('E - -', 'C', '1')],
  [R("D' - D'", 'G', '5'), R('B - -', 'G', '3'), R("C' - C'", 'C', '4'), R('G - -', 'C', '1')],
  [R('A - A', 'F', '2'), R("C' -.B A", 'F', '4 -.3 2'), R('G -.A G', 'C', '3 -.4 3'), R('E - -', 'C', '1')],
  [R('A - A', 'F', '2'), R("C' -.B A", 'F', '4 -.3 2'), R('G -.A G', 'C', '3 -.4 3'), R('E - -', 'C', '1')],
  [R("D' - D'", 'G', '3'), R("F' -.D' B", 'G', '5 -.3 1'), R("C' - -", 'C', '2'), R("E' - -", 'C', '4')],
  [R("C' -.G E", 'C', '5 -.2 1'), R('G -.F D', 'G', '5 -.4 2'), R('C - -', 'C', '1'), B('~C - -', lp='C - -', ch='C')]],
 src='Mutopia Project (Stille Nacht, soprano); Essen folk-song collection', composer='Franz Gruber, 1818')

# 8
BG = lambda c: {'G': 'G B D', 'C': 'G C E', 'D': 'F# A D', 'Em': 'G B E'}[c]
def Q(r, c, f=''): return B(r, lp=BG(c), ch=c, f=f)
song('Daisy Bell', 3, 'staff',
 'Home is G again, and the left-hand fan from Silent Night moves there with you. One new colour on the way: <b>E minor</b>, the G chord with its top key moved up one.',
 'G: G B D. C: G C E. D: F♯ A D. New, Em: G B E. One key on each beat, bottom to top.',
 'High place: thumb on G. Low place: thumb on D, finger 3 on F♯. Most notes last a whole bar, so you have time to find the next place.',
 'A white note with a dot fills a whole bar of three. While the right hand waits on it, listen to the left hand walk up the chord.',
 'you can hear the Em bar sound a little sadder than the bars around it.',
 ['f', 7, '. 5 x 3 x 1 x', {'0': ' '}], ['d', 8, '1 2 . 4 5 x x x', {'2': '3'}],
 [[Q("D' - -", 'G', '5'), Q('B - -', 'G', '3'), Q('G - -', 'G', '1'), Q('D - -', 'G', '1')],
  [Q('E F# G', 'C', '2 3 4'), Q('E - G', 'C', '2 - 4'), Q('D - -', 'G', '1'), Q('~D - -', 'G')],
  [Q('A - -', 'D', '5'), Q("D' - -", 'D', '5'), Q('B - -', 'G', '3'), Q('G - -', 'Em', '1')],
  [Q('E F# G', 'C', '2 3 4'), Q('A - B', 'C', '2 - 3'), Q('A - -', 'D', '2'), B('~A - -', l=Dg, ch='D')]],
 src='Nottingham Music Database (Daisy Daisy), first half', composer='Harry Dacre, 1892')

# 9
song('Minuet in G', 3, 'staff',
 'Until now the left hand played chords. Today it plays <b>a tune of its own</b>, one long note in a bar, while the right hand dances on top. Two tunes at once: this is how Bach wrote.',
 'Fingers 5 4 3 2 1 on G A B C D. Bar 1: the G chord for two beats, then A. Now and then the little finger reaches below G: for F♯, and for a low D or G. An arrow ↓ marks the low one.',
 'Start with finger 5 on high D, thumb on G. In bar 3 the thumb moves up to C; in bar 4 it reaches back down to G.',
 'Beamed notes are quick: two in one beat. Learn the right hand two bars at a time. Bars 1 and 2 ask a question; bars 3 and 4 answer it one step higher. Lines 3 and 4 are lines 1 and 2 again with a new ending.',
 'you can play the left hand of lines 1 and 2 without looking at the page.',
 ['d', 8, 'x . . 5 4 3 2 1', {'2': ' '}], ['f', 9, '. 1 2 3 4 5 x . x', {'0': ' ', '7': ' '}],
 [[B("D' G.A B.C'", lp='G+B+D - A', ch='G', f='5 1.2 3.4'), B("D' G G", lp='B - -', f='5 1 1'), B("E' C'.D' E'.F#'", lp='C - -', ch='C', f='3 1.2 3.4'), B("G' G G", lp='B - -', ch='G', f='5 1 1')],
  [B("C' D'.C' B.A", lp='A - -', f='4 5.4 3.2'), B("B C'.B A.G", lp='G - -', ch='G', f='3 4.3 2.1'), B('F# G.A B.G', lp='D B G', ch='D', f='1 2.3 4.2'), B('A - -', lp='D D↓.C B.A', ch='D', f='3')],
  [B("D' G.A B.C'", lp='B - A', ch='G', f='5 1.2 3.4'), B("D' G G", lp='G B G', f='5 1 1'), B("E' C'.D' E'.F#'", lp='C - -', ch='C', f='3 1.2 3.4'), B("G' G G", lp='B C.B A.G', ch='G', f='5 1 1')],
  [B("C' D'.C' B.A", lp='A - F#', f='4 5.4 3.2'), B("B C'.B A.G", lp='G - B', ch='G', f='3 4.3 2.1'), B('A B.A G.F#', lp='C D D↓', ch='D', f='3 4.3 2.1'), B('G - -', lp='G - G↓', ch='G', f='2')]],
 src='Mutopia Project (BWV Anh. 114), bars 1 to 16, both hands', composer='Christian Petzold, in Anna Magdalena Bach’s notebook')

# 10 ----------------------------------------------------------------- UNIT 3: the letters fade
Am, C2, G2, F2, E2 = 'A+C+E', 'G+C+E', 'G+B+D', 'A+C+F', 'G#+B+E'
def H(r, c1, c2=None, n1='', n2='', f='', show=''):
    return B(r, lp=f'{c1} - - {c2} - -' if c2 else f'{c1} - - - - -', ch=f'{n1} - - {n2} - -' if c2 else n1, f=f, show=show)
song('Greensleeves', 6, 'bare',
 'Most of the letters have gone: now only the <b>first note of each bar</b> carries one. Read the rest by its shape, step or skip, up or down. And home is a new kind of place: <b>A minor</b>, a darker colour.',
 'Am: A C E (5 3 1). C: G C E. G: G B D. F: A C F. E: G♯ B E, with finger 5 on the black key. Two chords in a bar, each held for three counts.',
 'The hand shifts a little in almost every bar: trust the numbers. Two black keys appear, G♯ and F♯: the ♯ sits just before the note it changes.',
 'Six quick counts in a bar, felt as two big swings: <b>1</b> 2 3 <b>4</b> 5 6. A dotted note with a tiny note after it goes <i>looong-short</i>.',
 'you can name any note in line 1 without counting up from the letter.',
 ['g', 7, 'x 5 x 3 x 1 x', {'0': ' '}], ['e', 9, 'x x x x x x x x x', {'1': ' ', '2': ' '}],
 [[B('r r r r r A', f='- - - - - 1', pick=1), H("C' - D' E' -.F' E'", Am, C2, 'Am', 'C', '2 - 3 4 -.5 4', 'C')],
  [H("D' - B G -.A B", G2, None, 'G', f='5 - 3 1 -.2 3', show='D'), H("C' - A A -.G# A", Am, F2, 'Am', 'F', '5 - 3 3 -.2 3', 'C')],
  [H('B - - E - A', E2, None, 'E', f='4 - - 1 - 1', show='B'), H("C' - D' E' -.F' E'", Am, C2, 'Am', 'C', '2 - 3 4 -.5 4', 'C')],
  [H("D' - B G -.A B", G2, None, 'G', f='5 - 3 1 -.2 3', show='D'), H("C' -.B A G# -.F# G#", Am, E2, 'Am', 'E', '5 -.4 3 2 -.1 2', 'C')],
  [B('A - - A - r', lp=f'{Am} - - - - -', ch='Am', f='3', show='A')]],
 unit='e', src='Mutopia Project (Greensleeves, soprano), first half, moved from E minor to A minor', composer='Traditional, England, 1500s')

# 11
song('Canon', 4, 'bare',
 'Eight bass notes that go <b>round and round</b>: C G A E, F C F G. The whole piece is built on them. Now only the first note of each line has a letter.',
 'One key at a time, two beats each. Say the eight letters until you know them by heart; then your eyes are free for the right hand.',
 'Line 1: finger 5 on high E, walking down. The numbers show where the hand moves. Line 3 is the same idea in quick notes.',
 'The coral names show the chord each bass note belongs to. Am and Em are <b>minor</b> chords: the darker cousins of C and G. You will use them in the last song.',
 'the left hand can go round the eight notes while you talk.',
 ['c', 6, '5 . 3 2 1 x'], ['c', 10, 'x x x x x x x x x x', None, 280],
 [[B("E' D' C' B", lp='C - G -', ch='C - G -', f='5 4 3 2'), B('A G A B', lp='A - E -', ch='Am - Em -', f='2 1 2 3')],
  [B("C' B A G", lp='F - C -', ch='F - C -', f='4 3 2 1', show='C'), B('F E F D', lp='F - G -', ch='F - G -', f='3 2 3 1')],
  [B('C.E G.F E.C E.D', lp='C - G -', ch='C - G -', f='1.3 5.4 3.1 3.2', show='C'), B('C - - -', l=Cc, ch='C', f='1')]],
 src='Mutopia Project (Canon per 3 violini e basso), bars 3 to 7, moved from D to C', composer='Johann Pachelbel, late 1600s')

# 12
song('In the Hall of the Mountain King', 4, 'bare',
 'A troll tune that tiptoes. The left hand rocks between two keys, <b>bottom and top of the chord</b>: A E A E. No middle key at all, and it still sounds complete.',
 'Bars 1 to 3: A with finger 5, E with the thumb. Bar 4: the whole hand moves up, C with 5 and G with the thumb.',
 'Thumb on A. In bar 2 two notes turn black: D♯ (finger 4) and B♭ (finger 2). A ♭ means the black key just to the left.',
 'Short and light, like footsteps. Play the four bars four times: first as quiet as you can, then each time a little louder and a little faster.',
 'bar 2 comes out with the right black keys three times in a row.',
 ['a', 7, '5 . 5 . 1 . 1'], ['a', 8, '1 2 3 4 5 . x x', {'0': '2', '3': '4'}],
 [[B("A.B C'.D' E'.C' E'", lp='A E A E', ch='Am', f='1.2 3.4 5.3 5'), B("D#'.B D#' D'.Bb D'", lp='A E A E', f='4.2 4 4.2 4', show='D# Bb D')],
  [B("A.B C'.D' E'.C' E'.A'", lp='A E A E', ch='Am', f='1.2 3.4 5.3 2.5', show='A'), B("G'.E' C'.E' G' -", lp='C G C G', ch='C', f='4.2 1.2 4')]],
 src='Mutopia Project (Grieg, Op. 46 No. 4), bars 2 to 5, moved from B minor to A minor', composer='Edvard Grieg, 1875')

# 13
RR = 'r r r r r r'
song('Für Elise', 6, 'bare',
 'The most famous piano tune of all, as Beethoven wrote it. The two hands <b>pass the music to each other</b>: the left hand runs up three keys, and the right hand carries on from where it stopped.',
 'Bottom, middle, top. A, E, A with fingers 5, 2, 1. Then E, E, G♯ with 5, 1, 2. The arrow means the lower key of that name.',
 'Fingers 5 and 4 rock between E and the black key D♯. Then the hand walks down to A. After each left-hand run, the right hand answers from the thumb.',
 'The boxes are very quick now: six in a bar, count <b>1 and 2 and 3 and</b>. Play so slowly that the left-hand run and the right-hand answer sound like one hand.',
 'nobody listening could tell where one hand stops and the other begins.',
 ['e', 11, 'x . . x . . . x . . x', {'9': ' '}, 290], ['c', 10, 'x . x . . x x x x x', {'4': ' ', '8': ' '}, 280],
 [[B("r r r r E' D#'", f='- - - - 5 4', pick=2), B("E' D#' E' B D' C'", f='5 4 5 2 4 3', show='D#'), B('A - r C E A', lp='A↓ E A r r r', ch='Am', f='1 - - 1 2 4')],
  [B('B - r E G# B', lp='E↓ E G♯ r r r', ch='E', f='5 - - 1 2 4', show='B G#'), B("C' - r E E' D#'", lp='A↓ E A r r r', ch='Am', f='5 - - 1 5 4', show='C'), B("E' D#' E' B D' C'", f='5 4 5 2 4 3')],
  [B('A - r C E A', lp='A↓ E A r r r', ch='Am', f='1 - - 1 2 4', show='A'), B("B - r E C' B", lp='E↓ E G♯ r r r', ch='E', f='5 - - 1 3 2'), B('A - - - r r', lp='A↓ E A r r r', ch='Am', f='1')]],
 unit='s', counts=['1', '&', '2', '&', '3', '&'], src='Mutopia Project (Beethoven, WoO 59), bars 1 to 8', composer='Ludwig van Beethoven, 1810')

# 14
V = {'C': 'C E+G', 'Em': 'B E+G', 'F': 'C F+A', 'Dm': 'D F+A', 'Am': 'C E+A', 'G': 'B D+G'}
def T(r, a, b, f='', show=''): return B(r, lp=f'{V[a]} {V[b]}', ch=f'{a} - {b} -', f=f, show=show)
A1 = [T('C C G G', 'C', 'Em', '1 - 4 -'), T('A A G -', 'F', 'C', '5 - 4'), T('F F E E', 'Dm', 'Am', '3 - 2 -'), T('D D C -', 'G', 'C', '1 - 1')]
song('Twinkle, Now', 4, 'bare',
 'You ended Music Box 1 with Twinkle and two keys in a bar. Here is the same tune with everything this book gave you: whole chords, split low and high, and the <b>minor colours</b> Am, Dm and Em slipped in between.',
 'Six chords, two in a bar. Beat 1: the bottom key. Beat 2: the top two together. C, F and G you know; Em, Dm and Am each change just one key.',
 'Thumb on middle C, finger 4 on G, finger 5 reaches A. In bar 4 the thumb slides to D, then back to C.',
 'Only one letter is left on the whole page. First play it with C, F and G only, the Music Box 1 way. Then with the colours. Hear what each minor chord does to the same tune.',
 'you can play it for someone, ask which bar they liked best, and tell them the name of its chord.',
 ['b', 7, 'x x x x x x x'], ['c', 6, '1 2 3 4 5 x'],
 [A1,
  [T('G G F F', 'C', 'Dm', '5 - 4 -'), T('E E D -', 'Am', 'G', '3 - 2'), T('G G F F', 'Em', 'Dm', '5 - 4 -'), T('E E D -', 'Am', 'G', '3 - 2')],
  [T('C C G G', 'C', 'Em', '1 - 4 -'), T('A A G -', 'F', 'C', '5 - 4'), T('F F E E', 'Dm', 'Am', '3 - 2 -'), B('D D C -', lp=f'{V["G"]} {Cc} -', ch='G - C -', f='1 - 1')]],
 src='Traditional tune (Ah! vous dirai-je, maman), as in Music Box 1', composer='Traditional, France, 1700s', ticks=['With C, F and G only', 'With the colours', 'From memory', 'For someone'])

WAYS = {
 1: ['Play the chord again on beat 3: twice in a bar instead of once.', 'Move the right hand up to the next C: the same keys, eight keys higher. Baby ducks.'],
 2: ['Left hand on beats 1 and 3: a chord twice in a bar, like a banjo.', 'Sing the tune while the left hand plays alone.'],
 3: ['Left hand: the bottom key on beat 1, the top two keys on beat 3.', 'Loud like a brass band; then as soft as a secret.'],
 4: ['Hold one chord for the whole bar, even where two are written. Which bars now sound wrong?', 'Line 3 softly, line 4 loudly.'],
 5: ['Left hand: hold all three keys for the whole bar instead of low, high, high. Which do you like better?', 'Right hand eight keys higher, like a music box.'],
 6: ['Left hand: play only the bottom key of each chord. Is it still the same song?', 'March it: a left-hand chord on every beat.'],
 7: ['Left hand: hold the whole chord for the bar, as in Song 1. Then the fan again. Hear the difference.', 'Play the fan and hum the tune instead of playing it.'],
 8: ['Left hand low, high, high (the waltz from Song 5) instead of the fan.', 'Play the Em bar as plain G. What is missing?'],
 9: ['Play the left hand and sing the right hand.', 'Right hand loud, left hand soft. Then swap.'],
 10: ['Left hand as a fan: bottom, middle, top, one key on each quick count.', 'Play every E chord with white G instead of G♯. Hear why the black key matters.'],
 11: ['Left hand plays whole chords instead of single keys. Build each from its bottom key: every other white key.', 'Play bars 1 and 2 while a friend plays bars 3 and 4. They fit. That is what canon means: the same tune, starting later.'],
 12: ['Both hands eight keys lower: trolls live underground.', 'Left hand plays its two keys together on every beat instead of rocking.'],
 13: ['Keep the left hand\'s three keys held down after you play them, so the chord rings under the answer.', 'From memory, two bars at a time, eyes on the keys.'],
 14: ['Left hand as a fan, one key at a time: bottom, middle, top, middle.', 'Make it yours: in any bar, swap a minor colour back to C, F or G, and keep the ones you like.'],
}
GROUP = {7: [6, 6, 6, 6], 10: [3, 2, 2, 2], 11: [4, 2]}
for i, s in enumerate(S, 1):
    if i in GROUP:
        flat = [b for ln in s['lines'] for b in ln]; s['lines'] = []
        for n in GROUP[i]: s['lines'].append(flat[:n]); flat = flat[n:]
        assert not flat
    d = copy.deepcopy(base); g = d['gig']; last = i == len(S)
    d.update(id=f'mc{i}', title=s['title'], lesson=i, beats=s['beats'], book="THE PIANO BUTLER'S MUSIC BOX 2", label='End of Music Box 2' if last else f'Song {i}')
    d['composer'] = {'name': s['composer'], 'years': '', 'stamp': ''}
    d['page0'] = 3 + 2 * (i - 1)
    for k in ('shapes', 'ways', 'ways2', 'lkb_from'): g.pop(k, None)
    g.update(mb2=s['stage'], unit=s['unit'], job=s['job'], tool_cap=s['lcap'], r_cap=s['rcap'], song_how=s['how'], ready=s['ready'], lkb=s['lkb'], rkb=s['rkb'],
             song_grid=s['lines'], ways_txt=WAYS[i], ticks=s['ticks'], simple=1, grid=1, song_title=s['title'], src=s['src'])
    if s['counts']: g['counts'] = s['counts']
    else: g.pop('counts', None)
    json.dump(d, open(f'mc{i}.json', 'w'), ensure_ascii=False)
json.dump([[s['title'], s['composer'], s['src']] for s in S], open('mc-sources.json', 'w'), ensure_ascii=False, indent=1)
print(len(S), 'songs')
