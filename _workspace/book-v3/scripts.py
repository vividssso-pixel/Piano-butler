# Scripts for "Butler explains", Part I Pitch. Follow each chapter's order: picture and secret, Examples, Try it.
# B = the Butler, P = Clara (a student). Every Example asks first; the answer comes after a pause, as in the book.
def c(p, r, **k): d = {'p': p, 'r': r}; d.update(k); return d
def idx(a, b): return ['#%d' % i for i in range(a, b)]
W = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
NEW = {
'P2': ('The staff and the clefs', [
 ('The secret', [
  ('B', 'Clara, music is written on a staff: five lines and four spaces, counted from the bottom.', c(27, 'lead')), ('P', 'Higher on the staff means higher on the piano?', c(27, 'lead')),
  ('B', 'Always. But five lines alone do not tell us the notes. For that we need a clef: the key to the code.', c(27, 'hero')),
  ('B', 'Look closely. The treble clef curls round line two. That line is G.', c(27, 'hero')), ('piano', 'G4', c(27, 'hero', seq=['G'])),
  ('B', 'The bass clef has two dots, and they hug line four. That line is F.', c(27, 'hero')), ('piano', 'F3', c(27, 'hero', seq=['F'])),
  ('P', 'The treble clef curls round G. The bass clef’s dots hug F.', c(27, 'secret'))]),
 ('The grand staff', [
  ('B', 'Piano music joins two staves with a brace. The treble staff is on top, usually for the right hand. The bass staff is below, usually for the left.', c(27, 'two')),
  ('B', 'And Middle C sits between them, on a short line of its own. It can be written in either staff: the same key.', c(27, 'two')), ('piano', 'C4', c(27, 'two'))]),
 ('Example: which staff?', [
  ('B', 'Here is a key on the piano. Which staff would it be written on?', c(28, 'ex1', show=['Middle C'])),
  ('P', 'First I find Middle C. The question mark is to its left.', c(28, 'ex1', show=['Middle C'], lab=['Middle C'])),
  ('B', 'Left is lower. And low keys go on which staff? Pause and think.', c(28, 'ex1', show=['Middle C'], lab=['?'])), ('pause', 3, c(28, 'ex1', show=['Middle C'], lab=['?'])),
  ('P', 'The bass staff, usually for the left hand!', c(28, 'ex1', reveal=True)), ('B', 'Quite right. High keys go on the treble staff.', c(28, 'ex1', reveal=True))]),
 ('Try it', [
  ('B', 'Point to the line the treble clef curls round, and play that G. Then the line between the bass clef’s dots, and play that F. Middle C sits between them.', c(28, 'gt2')), ('pause', 4, c(28, 'gt2')), ('piano', 'G4 F3 C4', c(28, 'gt2')),
  ('B', 'And a tune you know. Twinkle, Twinkle leaps up to G, the treble clef’s very own line.', c(28, 'yk')), ('piano', 'C4 C4 G4 G4 A4 A4 G4*2', c(28, 'yk', seq=idx(0, 7))),
  ('B', 'A clef is a pair of glasses: the same five lines read as different notes, depending on which pair you put on. Until next time.', c(28, 'think'))])]),
'P3': ('The staff and the keyboard', [
 ('The secret', [
  ('B', 'Clara, here is the secret of this chapter. Every line and every space of the staff is one white key, in order.', c(29, 'secret')),
  ('P', 'So climbing the staff is climbing the keyboard?', c(29, 'vx')),
  ('B', 'Exactly. Here are two octaves, from Bass C up to Treble C, with Middle C where the two staves meet.', c(29, 'vx')),
  ('piano', 'C3 D3 E3 F3 G3 A3 B3 C4 D4 E4 F4 G4 A4 B4 C5', c(29, 'vx', seq=idx(0, 15))),
  ('B', 'One step on the staff, from a line to the space next to it, is the very next white key. Up the staff is to the right; down is to the left.', c(29, 'rule')),
  ('B', 'The black keys sit in between. How they are written comes in chapter five.', c(29, 'p'))]),
 ('Example: from the page to the key', [
  ('B', 'A note on line four of the bass staff. Which key is it?', c(30, 'ex1', show=['Middle C'])),
  ('P', 'Line four, between the clef’s dots: F.', c(30, 'ex1', show=['Middle C', 'F'], lab=['F'])),
  ('B', 'And where is it on the piano? Pause and find it.', c(30, 'ex1', show=['Middle C', 'F'])), ('pause', 3, c(30, 'ex1', show=['Middle C', 'F'])),
  ('P', 'The three black keys just below Middle C. F is the first key of that family.', c(30, 'ex1', reveal=True)), ('piano', 'F3', c(30, 'ex1', reveal=True))]),
 ('Example: mirror notes', [
  ('B', 'Here is something lovely. Find treble G and bass F on the piano.', c(30, 'ex2', show=['Middle C'])),
  ('P', 'Treble G: the second key of the three black keys just above Middle C. Bass F: the first key of the three just below.', c(30, 'ex2', show=['Middle C'])),
  ('B', 'Now count each from Middle C. Up to G, down to F. Pause and count.', c(30, 'ex2', show=['Middle C'])), ('pause', 4, c(30, 'ex2', show=['Middle C'])),
  ('P', 'C D E F G: five. C B A G F: five as well!', c(30, 'ex2', reveal=True)), ('piano', 'C4 D4 E4 F4 G4 | C4 B3 A3 G3 F3', c(30, 'ex2', reveal=True)),
  ('B', 'Mirror images, the same distance either side of Middle C.', c(30, 'ex2', reveal=True))]),
 ('Example: from the key to the page', [
  ('B', 'I play the third white key up from Middle C.', c(30, 'ex3', show=['Middle C'])), ('piano', 'C4 D4 E4', c(30, 'ex3', seq=['Middle C', '', '?'], show=['Middle C'])),
  ('P', 'C one, D two, E three. It is E.', c(30, 'ex3', lab=['?'], show=['Middle C'])),
  ('B', 'And on the staff? Climb the same way.', c(30, 'ex3', show=['Middle C'])), ('P', 'Middle C on its little line, D in the space just under the staff, E on the bottom line.', c(30, 'ex3', reveal=True)), ('B', 'Precisely.', c(30, 'ex3', reveal=True))]),
 ('Try it', [
  ('B', 'Play Middle C and walk up the white keys, saying each name, and picture each one climbing the staff: line, space, line, space.', c(31, 'try10')), ('piano', 'C4 D4 E4 F4 G4 A4 B4 C5', c(31, 'try10', seq=idx(0, 8))),
  ('B', 'Then Frère Jacques in both hands. The right hand plays C D E C; the left hand plays the same letters one octave lower, in the bass clef.', c(31, 'yk')), ('piano', 'C4 D4 E4 C4 | C3 D3 E3 C3', c(31, 'yk', seq=idx(0, 4) + idx(0, 4))),
  ('B', 'The staff is a ladder laid beside the keyboard: every rung is the next white key.', c(31, 'think'))])]),
'P4': ('Reading the notes', [
 ('The secret', [
  ('P', 'Do I have to learn every line and space by heart?', c(32, 'lead')),
  ('B', 'Not at once. Start from a note you always know: Middle C in the middle, treble G and bass F either side.', c(32, 'hero', lab=['#19', '#2', '#15'])),
  ('piano', 'C4 G4 F3', c(32, 'hero', seq=['#19', '#2', '#15'])),
  ('B', 'Every line and space is the next letter. Listen to the whole staircase, from bass G to treble F.', c(32, 'hero')),
  ('piano', 'G2/2 A2/2 B2/2 C3/2 D3/2 E3/2 F3/2 G3/2 A3/2 B3/2 C4/2 D4/2 E4/2 F4/2 G4/2 A4/2 B4/2 C5/2 D5/2 E5/2 F5/2', c(32, 'hero', seq=idx(9, 21) + idx(0, 9))),
  ('P', 'And how do I move?', c(32, 'rule')),
  ('B', 'Step or skip. A step goes to the very next line or space: one letter on. A skip goes line to line, or space to space: two letters on.', c(32, 'rule')), ('piano', 'G4 A4 | G4 B4', c(32, 'rule'))]),
 ('Words to remember', [
  ('B', 'If you like little sentences, here are four. Treble lines: E G B D F. Every Good Boy Deserves Fun. The treble spaces spell a word: face.', c(32, 'ht')),
  ('B', 'Bass lines: G B D F A. Great Big Dragons Fly Away. Bass spaces: A C E G. All Cows Eat Grass.', c(32, 'ht'))]),
 ('Example: read from the clef note', [
  ('B', 'A treble note you are not sure of, on line four. Start from the clef note.', c(33, 'ex1')),
  ('P', 'G is line two. Skip up to line three: B. Skip again to line four.', c(33, 'ex1')), ('pause', 3, c(33, 'ex1')),
  ('P', 'D!', c(33, 'ex1', reveal=True)), ('piano', 'G4 B4 D5', c(33, 'ex1', reveal=True)), ('B', 'G, B, D: two skips up from the clef’s G.', c(33, 'ex1', reveal=True))]),
 ('Example: a bass note', [
  ('B', 'Now the bass staff, line three.', c(33, 'ex2', show=[])),
  ('P', 'The dots hug line four: F. Step down to the space: E. Step down again to line three.', c(33, 'ex2', show=['F', 'E'])), ('piano', 'F3 E3', c(33, 'ex2', seq=['F', 'E'], show=['F', 'E'])), ('pause', 3, c(33, 'ex2', show=['F', 'E'], lab=['?'])),
  ('P', 'D.', c(33, 'ex2', lab=['?'], reveal=True)), ('piano', 'F3 E3 D3', c(33, 'ex2', seq=['F', 'E', '?'], reveal=True)), ('B', 'Correct. F, E, D.', c(33, 'ex2', reveal=True))]),
 ('Example: one line, two notes', [
  ('B', 'Here is a puzzle. Two red notes, both on the bottom line: one in the treble staff, one in the bass. Same line. Same note?', c(33, 'ex3')),
  ('P', 'I think so?', c(33, 'ex3')), ('B', 'Read each from its clef. Pause and try.', c(33, 'ex3')), ('pause', 4, c(33, 'ex3')),
  ('P', 'Treble: G is line two. Step down, F in the space, then the bottom line is E.', c(33, 'ex3', lab=['#0'])), ('piano', 'E4', c(33, 'ex3', seq=['#0'])),
  ('B', 'And the bass? F is line four. Step down line by line.', c(33, 'ex3')), ('P', 'F, D, B, G. The bottom line is G!', c(33, 'ex3', lab=['#1'], reveal=True)), ('piano', 'G2', c(33, 'ex3', seq=['#1'], reveal=True)),
  ('B', 'Same line, different note. Always read the clef first.', c(33, 'ex3', reveal=True))]),
 ('Example: Treble C and Bass C', [
  ('B', 'Find Treble C on the staff. These notes sit in the spaces.', c(34, 'ex4')),
  ('P', 'The treble spaces spell face. F, A, and space three is C!', c(34, 'ex4', lab=['?'], reveal=True)), ('piano', 'F4 A4 C5', c(34, 'ex4', reveal=True)),
  ('B', 'Treble C, one octave above Middle C. And in the bass spaces?', c(34, 'ex5')),
  ('P', 'All Cows. Space two is C: Bass C!', c(34, 'ex5', lab=['?'], reveal=True)), ('piano', 'A2 C3', c(34, 'ex5', reveal=True)),
  ('B', 'One octave below Middle C. Now say the treble lines up and down, as fast as you can without a slip.', c(34, 'try10')), ('pause', 4, c(34, 'try10'))]),
 ('Try it', [
  ('B', 'To read a new note, make three moves. Look at the clef. Find the nearest note you know, or use the sentence. Then step or skip to it, say it, and play it.', c(35, 'howto')),
  ('B', 'Mary Had a Little Lamb. E, D, C: line, space, and Middle C’s own little line, one step down each time.', c(35, 'yk')), ('piano', 'E4 D4 C4 D4 E4 E4 E4*2', c(35, 'yk', seq=idx(0, 7))),
  ('B', 'Your mission: in a piece you play, find the clef notes first, then step or skip from them. The clef notes are lamp posts on a dark road. Until next time, Clara.', c(35, 'think')), ('P', 'Goodbye!', c(35, 'think'))])]),
'P5': ('Ledger lines', [
 ('The secret', [
  ('B', 'Clara, some notes are too high or too low for the staff. They sit on short extra lines called ledger lines.', c(36, 'lead')),
  ('P', 'Little lines just for one note?', c(36, 'lead')),
  ('B', 'Exactly, spaced just like the staff lines. And the most famous ledger note of all is Middle C. In the treble staff it hangs on the first ledger line below. In the bass staff it sits on the first ledger line above.', c(36, 'hero')),
  ('P', 'Two different places on the page, but the same key?', c(36, 'hero', lab=['Middle C'])), ('piano', 'C4', c(36, 'hero', seq=['Middle C'])),
  ('B', 'One key, two ways to write it. The right hand reads it in the treble, the left hand in the bass.', c(36, 'hero'))]),
 ('Below and above the staff', [
  ('B', 'Read ledger notes by stepping out from the staff, one letter at a time. In the treble, stepping out: C, B, A below the staff, and A, B, C above it.', c(36, 'two')), ('piano', 'C4 B3 A3 | A5 B5 C6', c(36, 'two', seq=idx(0, 6))),
  ('B', 'In the bass: E, D, C below, and C, D, E above.', c(36, 'two')), ('piano', 'E2 D2 C2 | C4 D4 E4', c(36, 'two', seq=idx(6, 12))),
  ('B', 'The rule: count ledger lines from the staff outwards. The first ledger line is the one nearest the staff. Never skip one.', c(36, 'rule'))]),
 ('Example: a high note', [
  ('B', 'A high note on ledger lines. Start from the top line of the treble staff: F.', c(37, 'ex1', show=['F'], lab=['F'])),
  ('P', 'Then G on top of the staff, A on the first ledger line, B above it.', c(37, 'ex1', show=['F', 'G', 'A', 'B'])), ('piano', 'F5 G5 A5 B5', c(37, 'ex1', seq=['F', 'G', 'A', 'B'], show=['F', 'G', 'A', 'B'])),
  ('B', 'And the red note, on the second ledger line? Pause and try.', c(37, 'ex1', show=['F', 'G', 'A', 'B'], lab=['?'])), ('pause', 3, c(37, 'ex1', show=['F', 'G', 'A', 'B'], lab=['?'])),
  ('P', 'C! High C.', c(37, 'ex1', lab=['?'], reveal=True)), ('piano', 'C6', c(37, 'ex1', seq=['?'], reveal=True))]),
 ('Example: a low note', [
  ('B', 'Now a low note under the bass staff. Start from the bottom line: G.', c(37, 'ex2', show=['G'], lab=['G'])),
  ('P', 'Step down: F in the space below, E on the first ledger line, D under it.', c(37, 'ex2', show=['G', 'F', 'E', 'D'])), ('piano', 'G2 F2 E2 D2', c(37, 'ex2', seq=['G', 'F', 'E', 'D'], show=['G', 'F', 'E', 'D'])),
  ('B', 'And the red note, on the second ledger line? Pause and try.', c(37, 'ex2', show=['G', 'F', 'E', 'D'], lab=['?'])), ('pause', 3, c(37, 'ex2', show=['G', 'F', 'E', 'D'], lab=['?'])),
  ('P', 'C! Low C, two octaves below Middle C.', c(37, 'ex2', lab=['?'], reveal=True)), ('piano', 'C2', c(37, 'ex2', seq=['?'], reveal=True))]),
 ('Example: Middle C, two ways', [
  ('B', 'Here is the tricky one. Middle C in the treble staff, and Middle C in the bass staff. They look like two different notes. Are they different keys? Pause and think.', c(37, 'ex3', show=['Middle C', 'A', 'B', 'C', 'D', 'E'])), ('pause', 3, c(37, 'ex3', show=['Middle C', 'A', 'B', 'C', 'D', 'E'])),
  ('P', 'No. It is the same key, just written from the other side.', c(37, 'ex3', reveal=True)), ('piano', 'C4 | C4', c(37, 'ex3', reveal=True)),
  ('B', 'And watch out for the other first ledger lines. Above the treble staff the first ledger line is A. Below the bass staff it is E. Only Middle C belongs to both staves.', c(38, 'xlate'))]),
 ('Try it', [
  ('B', 'When notes go even higher, music often writes them lower, with an ottava sign and a dotted line above them: play those notes one octave higher, until the dotted line stops.', c(38, 'xlate2')),
  ('B', 'Now say the ledger notes. Treble: C, B, A below; A, B, C above. Point to each one, say it, then play it.', c(37, 'try10')), ('pause', 4, c(37, 'try10')),
  ('B', 'Ledger lines are the staff’s ladder carried on past its ends: the same rungs, just shorter. Until next time, Clara.', c(38, 'think')), ('P', 'Goodbye!', c(38, 'think'))])]),
'P6': ('Sharps, flats and naturals', [
 ('The secret', [
  ('P', 'What are those little signs in front of some notes?', c(39, 'lead')),
  ('B', 'Signs that move a note to the very next key. A sharp: one key to the right, a semitone higher. A flat: one key to the left, a semitone lower.', c(39, 'secret')),
  ('B', 'Usually that next key is black, and that is how the black keys get their names. D sharp is just right of D. D flat is just left of it.', c(39, 'hero')), ('piano', 'D4 D#4 | D4 Db4', c(39, 'hero', seq=['D', 'D♯', 'D', 'D♭'])),
  ('B', 'And a natural cancels a sharp or flat: back to the white key.', c(39, 'ht')),
  ('B', 'One rule to remember. A sign belongs to one note: it changes only that line or space, in that octave, and only until the bar line. The same letter in another octave stays as it is.', c(39, 'rule'))]),
 ('Example: find F sharp', [
  ('B', 'Find F sharp, Clara.', c(39, 'ex1', show=[])), ('P', 'F is just left of the three black keys.', c(39, 'ex1', show=['F'], lab=['F'])),
  ('B', 'Sharp means right: the very next key. Black or white? Pause and put your finger on it.', c(39, 'ex1', show=['F'], lab=['?'])), ('pause', 3, c(39, 'ex1', show=['F'], lab=['?'])),
  ('P', 'Black! The first black key of the three.', c(39, 'ex1', lab=['?'], reveal=True)), ('piano', 'F4 F#4', c(39, 'ex1', seq=['F', '?'], reveal=True)), ('B', 'Correct: F sharp.', c(39, 'ex1', reveal=True))]),
 ('Example: find B flat', [
  ('B', 'Now B flat.', c(40, 'ex2', show=[])), ('P', 'B is just right of the three black keys. Flat means left.', c(40, 'ex2', show=['B'], lab=['B'])), ('pause', 3, c(40, 'ex2', show=['B'], lab=['?'])),
  ('P', 'The top black key of the group!', c(40, 'ex2', lab=['?'], reveal=True)), ('piano', 'B4 Bb4', c(40, 'ex2', seq=['B', '?'], reveal=True)), ('B', 'Splendid.', c(40, 'ex2', reveal=True))]),
 ('Example: how long does a sign last?', [
  ('B', 'A sharp on the first note of a bar: F sharp. Later in the same bar, the same note with no sign. Sharp or not?', c(40, 'ex3', show=['F♯', 'G'], lab=['F♯'])), ('pause', 3, c(40, 'ex3', show=['F♯', 'G'])),
  ('P', 'Still sharp?', c(40, 'ex3', show=['F♯', 'G'])), ('B', 'Yes, until the bar line. And after the bar line?', c(40, 'ex3', show=['F♯', 'G'])),
  ('P', 'Plain F again!', c(40, 'ex3', reveal=True)), ('B', 'A sign lasts to the end of its bar. Now a natural: B, then B flat, and it stays flat for the rest of the bar. Then a natural sign. What does it do?', c(40, 'ex4', show=['B', 'B♭'])), ('pause', 3, c(40, 'ex4', show=['B', 'B♭'])),
  ('P', 'It cancels the flat: back to the white key B.', c(40, 'ex4', lab=['?'], reveal=True)), ('piano', 'B4 Bb4 Bb4 B4', c(40, 'ex4', seq=idx(0, 4), reveal=True))]),
 ('Example: one key, two names', [
  ('B', 'One more. F sharp, then G flat. Find both on the keyboard.', c(41, 'ex5', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'])),
  ('P', 'They are the same black key!', c(41, 'ex5', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], lab=['F♯', 'G♭'])), ('piano', 'F#4 Gb4', c(41, 'ex5', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], seq=['F♯', 'G♭'])),
  ('B', 'Same sound, two names: we call them enharmonic. And E sharp, one key right of E?', c(41, 'ex5', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], lab=['E♯'])), ('pause', 3, c(41, 'ex5', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'])),
  ('P', 'There is no black key there. So E sharp is the white key F!', c(41, 'ex5', reveal=True)), ('piano', 'E4 F4', c(41, 'ex5', reveal=True))]),
 ('Try it', [
  ('B', 'Beethoven’s Für Elise begins on E and the black key just left of it: D sharp. The sharp is written again in the new bar, because the bar line wiped it out. And later in that bar the D has a natural sign, so it is plain D again.', c(41, 'yk')), ('piano', 'E5/2 D#5/2 E5/2 D#5/2 E5/2 B4/2 D5/2 C5/2 A4*2', c(41, 'yk')),
  ('B', 'Your mission: play E and D sharp back and forth, then find F sharp and B flat in three different places on the piano. A sign is a sticky note: it falls off at the bar line.', c(41, 'think'))])]),
'P7': ('Counting intervals', [
 ('The secret', [
  ('B', 'Clara, the smallest step on the piano is a semitone: from one key to the very next key, black or white, with nothing in between.', c(42, 'hero')), ('piano', 'E4 F4', c(42, 'hero', seq=['#0', '#1'])),
  ('P', 'E to F has no black key between. A semitone.', c(42, 'hero')),
  ('B', 'Two semitones make a tone: one key in between.', c(42, 'hero')), ('piano', 'C4 D4', c(42, 'hero', seq=['#4', '#5'])),
  ('P', 'C to D has C sharp between. A tone.', c(42, 'hero')),
  ('B', 'On the white keys most steps are tones. Only E to F and B to C are semitones. And a semitone can also go from white to black, or black to white.', c(42, 'rule'))]),
 ('Example: tone or semitone?', [
  ('B', 'Look between the two red keys, E and F. Is there a black key between them?', c(42, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'], lab=['E', 'F'])), ('pause', 3, c(42, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('P', 'No: they are next-door keys. A semitone.', c(42, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])), ('B', 'And C to D?', c(42, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'], lab=['C', 'D'])),
  ('P', 'C sharp is between them: a tone.', c(42, 'ex1', reveal=True))]),
 ('Intervals: count the notes', [
  ('B', 'Now bigger distances. The distance between two notes is an interval, and to give it a number, count the notes, both ends included. C to E: C, D, E. Three notes: a third.', c(43, 'xlate')), ('piano', 'C4 D4 E4 | [C4 E4]', c(43, 'xlate', seq=['#7', '#8', '#9', '#9'])),
  ('B', 'Sharps and flats never change the number. From C, the numbers go: unison, second, third, fourth, fifth, sixth, seventh, octave.', c(43, 'xlate')), ('piano', 'C4 D4 E4 F4 G4 A4 B4 C5', c(43, 'xlate', seq=['unison', '2nd', '3rd', '4th', '5th', '6th', '7th', '8ve'])),
  ('P', 'So C to G is C, D, E, F, G: a fifth.', c(43, 'xlate'))]),
 ('Example: count an interval', [
  ('B', 'F up to A. How many notes? Pause and count.', c(43, 'ex2', show=['F', 'A', 'C', 'G'])), ('pause', 3, c(43, 'ex2', show=['F', 'A', 'C', 'G'])),
  ('P', 'F, G, A. Three: a third.', c(43, 'ex2', show=['F', '(G)', 'A', 'C', 'G'])), ('piano', 'F4 G4 A4', c(43, 'ex2', seq=['F', '(G)', 'A'], show=['F', '(G)', 'A', 'C', 'G'])),
  ('B', 'And going down? C down to G.', c(43, 'ex2', show=['F', '(G)', 'A', 'C', 'G'])), ('P', 'C, B, A, G. Four: a fourth.', c(43, 'ex2', reveal=True)), ('piano', 'C5 B4 A4 G4', c(43, 'ex2', seq=['C', '(B)', '(A)', 'G'], reveal=True)),
  ('B', 'The same way, up or down: the first note is one. And your hand is a ruler: thumb on C, little finger on G, is a fifth.', c(43, 'try10'))]),
 ('Example: name an interval', [
  ('B', 'E, and the C above it. Count the notes from E.', c(44, 'ex3', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])), ('pause', 3, c(44, 'ex3', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('P', 'E one, F two, G three, A four, B five, C six. A sixth!', c(44, 'ex3', reveal=True)), ('piano', 'E4 F4 G4 A4 B4 C5', c(44, 'ex3', seq=idx(2, 8), reveal=True)),
  ('B', 'Melodic or harmonic, the number is the same. C then E, one after the other, is a melodic third. C and E together, a harmonic third.', c(44, 'ex4', lab=['melodic', 'harmonic'], reveal=True)), ('piano', 'C4 E4 | [C4 E4]', c(44, 'ex4', seq=['melodic', 'melodic', 'harmonic'], reveal=True))]),
 ('Try it', [
  ('B', 'Twinkle, Twinkle begins with a leap.', c(44, 'yk')), ('piano', 'C4 C4 G4 G4', c(44, 'yk', seq=['1', '1', '5', '5'])), ('P', 'C up to G: five notes. A fifth!', c(44, 'yk')),
  ('B', 'Monday to Wednesday is three days, not two: you count the day you start on. Intervals count the same way. Your mission: find a semitone, a tone, a third and a fifth from any C.', c(44, 'watch'))])]),
'P8': ('Major, minor and perfect', [
 ('The secret', [
  ('B', 'Clara, two thirds can sound different. Listen.', c(45, 'lead')), ('piano', '[C4 E4] | [C4 Eb4]', c(45, 'lead')), ('P', 'The first is bright. The second is darker.', c(45, 'lead')),
  ('B', 'Both are thirds: three notes each. To tell them apart, count the keys in between, black and white, but not the two you play.', c(45, 'secret')),
  ('B', 'C to E has three keys between: C sharp, D, D sharp. A major third.', c(45, 'hero')), ('piano', 'C#4 D4 D#4', c(45, 'hero', seq=idx(7, 10))),
  ('B', 'C to E flat has only two between, one fewer. A minor third.', c(45, 'hero')), ('piano', 'C#4 D4', c(45, 'hero', seq=idx(18, 20))),
  ('B', 'Thirds and sixths come in two sizes, major and minor. Fourths, fifths and octaves have one main size, called perfect. They are never major or minor.', c(45, 'two'))]),
 ('Example: major or minor third?', [
  ('B', 'C up to the red black key, E flat. A third. Now count the keys between. Pause and count.', c(45, 'ex1', show=W)), ('pause', 3, c(45, 'ex1', show=W)),
  ('P', 'C sharp, D. Two between.', c(45, 'ex1', show=W)), ('B', 'A major third has three between. So?', c(45, 'ex1', show=W)),
  ('P', 'A minor third!', c(45, 'ex1', reveal=True)), ('piano', '[C4 Eb4]', c(45, 'ex1', reveal=True))]),
 ('Example: F up to A', [
  ('B', 'F up to A. F, G, A: a third. Now the keys between: they are numbered.', c(46, 'ex2', show=W)),
  ('P', 'F sharp, G, G sharp: three. A major third!', c(46, 'ex2', reveal=True)), ('piano', 'F#4 G4 G#4 | [F4 A4]', c(46, 'ex2', seq=['1', '2', '3'], reveal=True)),
  ('B', 'The same size as C to E.', c(46, 'ex2', reveal=True))]),
 ('Example: D up to A', [
  ('B', 'D up to A. The number first.', c(46, 'ex3', show=W)), ('P', 'D, E, F, G, A: five notes, a fifth.', c(46, 'ex3', show=W)),
  ('B', 'And six keys between. A fifth with six between is its main size. What is that called?', c(46, 'ex3', show=W)), ('pause', 3, c(46, 'ex3', show=W)),
  ('P', 'A perfect fifth!', c(46, 'ex3', reveal=True)), ('piano', '[D4 A4]', c(46, 'ex3', reveal=True))]),
 ('Example: E up to C', [
  ('B', 'E up to C. E, F, G, A, B, C: a sixth. A major sixth has eight between. Count this one.', c(47, 'ex4', show=W)), ('pause', 4, c(47, 'ex4', show=W)),
  ('P', 'Seven! One fewer: a minor sixth.', c(47, 'ex4', reveal=True)), ('piano', '[E4 C5]', c(47, 'ex4', reveal=True))]),
 ('Try it', [
  ('B', 'Play C and E, then C and E flat. Bright, then dark. One key makes the difference.', c(47, 'try10')), ('piano', '[C4 E4] | [C4 Eb4]', c(47, 'try10')),
  ('B', 'And Beethoven’s Fifth: da-da-da-dum. G down to E flat is a third, with three keys between: a major third.', c(47, 'yk')), ('piano', 'G4/2 G4/2 G4/2 Eb4*3', c(47, 'yk', seq=idx(0, 4))),
  ('B', 'A major and a minor third are a smile and a frown: the same face, one small change at the corners. Until next time, Clara.', c(47, 'think')), ('P', 'Goodbye!', c(47, 'think'))])]),
}

CH = {
'P1': ('The keyboard', [
 ('The secret', [
  ('B', 'Good day. I am your Piano Butler, and this is Clara.', {'p': 22, 'r': 'h:The keyboard'}), ('P', 'Hello! Today is the keyboard, right? There are so many keys. Do I have to count them all?', {'p': 22, 'r': 'hero'}),
  ('B', 'Never. Let us start with one fact. Left is low.', {'p': 22, 'r': 'hero'}), ('piano', 'C2', {'p': 22, 'r': 'hero'}), ('B', 'Right is high.', {'p': 22, 'r': 'hero'}), ('piano', 'C6', {'p': 22, 'r': 'hero'}),
  ('P', 'Low on the left, high on the right. Easy.', {'p': 22, 'r': 'hero'}), ('B', 'Now look at the black keys. They come in little groups: two, then three. Two, three, all the way along.', {'p': 22, 'r': 'hero'}),
  ('P', 'Like bumps on a road.', {'p': 22, 'r': 'hero'}), ('B', 'Exactly. Here is the secret. Every group has a first white key, just to its left. Next to the two black keys, the first key is C. Next to the three, it is F.', {'p': 22, 'r': 'secret'}),
  ('P', 'Two black keys: start on C. Three black keys: start on F.', {'p': 22, 'r': 'secret'}), ('B', 'Then walk on. C, D, E around the two.', {'p': 22, 'r': 'hero'}), ('piano', 'C4 D4 E4', {'p': 22, 'r': 'hero', 'seq': ['C', 'D', 'E']}), ('B', 'F, G, A, B around the three.', {'p': 22, 'r': 'hero'}), ('piano', 'F4 G4 A4 B4', {'p': 22, 'r': 'hero', 'seq': ['F', 'G', 'A', 'B']}),
  ('B', 'And the pattern repeats all the way along: two, three, two, three. Every two starts on C, every three starts on F.', {'p': 22, 'r': 'hero2'}), ('piano', 'C3 F3 C4 F4 C5 F5', {'p': 22, 'r': 'hero2', 'seq': ['#0', '#1', '#2', '#3', '#4', '#5']}),
  ('P', 'So wherever I am, I find a group and I know where I am.', {'p': 22, 'r': 'hero2'})]),
 ('Round and round', [
  ('P', 'But what comes after G? Is there an H?', {'p': 23, 'r': 'keep'}),
  ('B', 'No H at all. The white keys use only seven letters, A to G. After G, the next key is A again, like the days of the week: Sunday comes round again after Saturday.', {'p': 23, 'r': 'keep'}),
  ('piano', 'A3 B3 C4 D4 E4 F4 G4 A4 B4 C5 D5 E5 F5 G5 A5', {'p': 23, 'r': 'keep', 'seq': ['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12', '#13', '#14']}),
  ('P', 'A B C D E F G, then A again. Seven letters, round and round.', {'p': 23, 'r': 'keep'}),
  ('B', 'Now the two ends of the piano. The very first key, bottom left, is an A. Look at the black keys there: only one, on its own.', {'p': 23, 'r': 'two'}),
  ('P', 'Only one? But the groups are two or three.', {'p': 23, 'r': 'two'}),
  ('B', 'Well spotted. It is a group of three that has been cut off. Only its end is left: A and B. Then comes the first full group of two, and its first key is Lowest C.', {'p': 23, 'r': 'two'}), ('piano', 'A0 B0 C1', {'p': 23, 'r': 'two', 'seq': ['#0', '#1', 'Lowest C']}),
  ('B', 'At the top, the very last key has no black key after it at all. Look left: the last group is three black keys, F, G, A, B.', {'p': 23, 'r': 'two'}),
  ('P', 'And after B comes C!', {'p': 23, 'r': 'two'}),
  ('B', 'Exactly. The first key of a new group of two that was never built. So the last key is a C: Highest C.', {'p': 23, 'r': 'two'}), ('piano', 'F7 G7 A7 B7 C8', {'p': 23, 'r': 'two', 'seq': ['#5', '#6', '#7', '#8', 'Highest C']})]),
 ('The eight Cs', [
  ('B', 'Count the Cs from the bottom and there are eight. Some have names. The C nearest the middle is Middle C.', {'p': 23, 'r': 'keep2'}), ('piano', 'C4', {'p': 23, 'r': 'keep2', 'seq': ['Middle C']}),
  ('B', 'One C lower is Bass C. One C higher is Treble C. Further out: Low C and High C.', {'p': 23, 'r': 'keep2'}), ('piano', 'C2 C3 C4 C5 C6', {'p': 23, 'r': 'keep2', 'seq': ['Low C', 'Bass C', 'Middle C', 'Treble C', 'High C']}),
  ('P', 'And the ones at the very ends?', {'p': 23, 'r': 'keep2'}), ('B', 'At the bottom, Lowest C. At the top, Very High C, and then Highest C, the very last key.', {'p': 23, 'r': 'keep2'}), ('piano', 'C1 C7 C8', {'p': 23, 'r': 'keep2', 'seq': ['Lowest C', 'Very High C', 'Highest C']}),
  ('P', 'Eight Cs! But the five in the middle are the ones I will use most.', {'p': 23, 'r': 'keep2'}),
  ('B', 'Exactly. Theory books and apps give them numbers instead: C1 to C8, with Middle C as C4. And from one C to the next is an octave: eight notes, both Cs counted.', {'p': 23, 'r': 'keep2'})]),
 ('Example: find G', [
  ('B', 'Clara, find G for me. Do not count from the bottom.', {'p': 24, 'r': 'ex1', 'show': []}), ('P', 'Hmm. G lives with F, G, A and B, so I look for three black keys.', {'p': 24, 'r': 'ex1', 'show': []}),
  ('B', 'And the first key of that family?', {'p': 24, 'r': 'ex1', 'show': []}), ('P', 'F, just left of the three.', {'p': 24, 'r': 'ex1', 'lab': ['F'], 'show': ['F']}), ('B', 'Now walk on one key. Pause and find it yourself.', {'p': 24, 'r': 'ex1', 'lab': ['?'], 'show': ['F']}), ('pause', 4, {'p': 24, 'r': 'ex1', 'lab': ['?'], 'show': ['F']}),
  ('P', 'G! The key after F.', {'p': 24, 'r': 'ex1', 'lab': ['?'], 'reveal': True}), ('piano', 'F4 G4', {'p': 24, 'r': 'ex1', 'seq': ['F', '?'], 'reveal': True}), ('B', 'No need to start from C and count five. Find the group, find its first key, walk on.', {'p': 24, 'r': 'ex1', 'reveal': True})]),
 ('Example: find E', [
  ('B', 'Now E.', {'p': 24, 'r': 'ex2', 'show': []}), ('P', 'E is in C D E, so two black keys. Start on C, then C, D, E.', {'p': 24, 'r': 'ex2', 'show': []}), ('piano', 'C4 D4 E4', {'p': 24, 'r': 'ex2', 'seq': ['C', '', '?'], 'show': ['C', 'D']}),
  ('B', 'And where does E sit?', {'p': 24, 'r': 'ex2', 'lab': ['?'], 'show': ['C', 'D']}), ('P', 'Just right of the two black keys. The last of its family.', {'p': 24, 'r': 'ex2', 'lab': ['?'], 'reveal': True}), ('B', 'Splendid.', {'p': 24, 'r': 'ex2', 'reveal': True})]),
 ('Try it', [
  ('B', 'Before you go, a tune with no white keys at all. Right hand, fingers two, three and four on a group of three black keys.', {'p': 26, 'r': 'yk'}),
  ('P', 'Ready.', {'p': 26, 'r': 'yk'}), ('B', 'Four, three, two. Four, three, two. Then quickly, two to a beat: two two two two, three three three three. And four, three, two.', {'p': 26, 'r': 'yk'}),
  ('piano', 'A#4 G#4 F#4*2 | A#4 G#4 F#4*2 | F#4/2 F#4/2 F#4/2 F#4/2 G#4/2 G#4/2 G#4/2 G#4/2 | A#4 G#4 F#4*2', {'p': 26, 'r': 'yk'}), ('P', 'Hot Cross Buns!', {'p': 26, 'r': 'yk'}),
  ('B', 'Your mission: close your eyes and slide your hand along the keys. Two bumps, the key to their left is C. Three bumps, it is F. Until next time.', {'p': 26, 'r': 'think'})
])]),
**NEW,
}

NEW['T1'] = ('Pulse, tempo and the bar', [
 ('The secret', [
  ('B', 'Clara, put your hand on your heart.', c(50, 'lead')), ('P', 'It is beating. Steady, steady.', c(50, 'lead')),
  ('B', 'That steady beat is a pulse, and almost every piece of music has one. Its speed is the tempo. Beats travel in groups called bars, and beat one is the strongest.', c(50, 'hero')),
  ('count', {'beats': 'X x x x X x x x X x x x', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, c(50, 'hero', seq=idx(0, 12))),
  ('B', 'Here is the secret. The beat never stops, not even in a rest. Feel it before you play.', c(50, 'secret')),
  ('P', 'So in a rest I still count?', c(50, 'hero')), ('B', 'Always. Listen: in the second bar the notes stop, and the beat goes on.', c(50, 'hero')),
  ('count', {'beats': 'X x x x X x x x X x x x', 'notes': 'C5 C4 C4 C4 C5 C4 R R C5 C4 C4 C4', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, c(50, 'hero', seq=idx(0, 12)))]),
 ('Tempo', [
  ('B', 'Tempo is measured in beats per minute. A metronome mark at the top of the music shows it. Crotchet equals sixty means sixty beats a minute: one every second.', c(50, 'two')),
  ('piano', 'X@60 x@60 x@60 x@60', c(50, 'two')), ('B', 'Crotchet equals one hundred and twenty is twice as fast.', c(50, 'two')),
  ('piano', 'X@120 x@120 x@120 x@120 X@120 x@120 x@120 x@120', c(50, 'two')),
  ('P', 'Twice as many ticks in the same time.', c(50, 'two'))]),
 ('Strong and weak beats', [
  ('B', 'The beats are not all the same. Two beats in a bar go strong, weak, like a march.', c(50, 'two')), ('piano', 'X x X x X x X x', c(50, 'two')),
  ('B', 'Three go strong, weak, weak, like a waltz.', c(50, 'two')), ('piano', 'X x x X x x X x x', c(50, 'two')),
  ('B', 'And four go strong, weak, medium, weak, like most songs.', c(50, 'two')), ('piano', 'X x M x X x M x', c(50, 'two')),
  ('P', 'So Twinkle, Twinkle is in four, and Happy Birthday is in three.', c(51, 'ht')), ('B', 'Exactly. And the Radetzky March is in two.', c(51, 'ht'))]),
 ('Bars and bar lines', [
  ('B', 'A bar line divides the music into bars. A double bar line marks the end of a section, or a change. A final bar line, thin then thick, marks the end of the piece.', c(50, 'ht')),
  ('B', 'And repeat signs: play the passage between them again. If there is no start sign, go back to the beginning.', c(50, 'ht'))]),
 ('Counting', [
  ('B', 'Every beat is counted, even inside a long note. Here are three bars of three-four. The red number is where you play; the grey numbers are the beats you hold.', c(51, 'vx')),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'C4 C4 C4 C4*2 C4 C4*3', 'say': '1 2 3 1 2 3 1 2 3'}, c(51, 'vx', seq=idx(0, 9))),
  ('B', 'Count aloud at one speed, a little louder on beat one. With a metronome, start slower than you think, and speed up only when the passage is steady.', c(51, 'p'))]),
 ('Example: march or waltz?', [
  ('B', 'Is this a march or a waltz? Tap a steady beat as you listen.', c(51, 'ex1')), ('piano', 'C3 G4 G4 C3 G4 G4 C3 G4 G4', c(51, 'ex1', seq=idx(0, 9))),
  ('B', 'Which beats feel heavier? Count from one heavy beat to the next. Pause and count.', c(51, 'ex1')), ('pause', 3, c(51, 'ex1')),
  ('P', 'Heavy every three: one two three, one two three. A waltz!', c(51, 'ex1', reveal=True)), ('count', {'beats': 'X x x X x x X x x', 'notes': 'C3 G4 G4 C3 G4 G4 C3 G4 G4', 'say': '1 2 3 1 2 3 1 2 3'}, c(51, 'ex1', seq=idx(0, 9), reveal=True)), ('B', 'Every two would be a march.', c(51, 'ex1', reveal=True))]),
 ('Example: feel the beat first', [
  ('B', 'This one says crotchet equals ninety-six: ninety-six beats a minute. Do not start yet. Listen to one full bar, counting one, two, three in your head.', c(51, 'ex2')),
  ('count', {'beats': 'X@96 x@96 x@96', 'say': '1 2 3'}, c(51, 'ex2')),
  ('B', 'Then step in on the next beat one, the way you step onto a moving escalator.', c(51, 'ex2')),
  ('count', {'beats': 'X@96 x@96 x@96 X@96 x@96 x@96 X@96 x@96 x@96 X@96 x@96 x@96', 'notes': 'R@96 R@96 R@96 C4@96 C4@96 C4@96 C4@48 C4@96 C4@32', 'say': '1 2 3 1 2 3 1 2 3 1 2 3'}, c(51, 'ex2', seq=['', '', '', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9'])),
  ('P', 'The first note landed right on the beat!', c(51, 'ex2', reveal=True))]),
 ('Try it', [
  ('B', 'Hand on your heart. Tap the beat and say one, two, three, four, with one a little louder. Keep going for ten seconds without slowing down.', c(52, 'try10')),
  ('count', {'beats': 'X@80 x@80 x@80 x@80 X@80 x@80 x@80 x@80 X@80 x@80 x@80 x@80', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, c(52, 'try10', seq=idx(0, 12))),
  ('B', 'At the New Year concert in Vienna, the audience claps along on every beat of the Radetzky March. That steady clap is the pulse; the tune moves freely over it.', c(52, 'yk')),
  ('count', {'beats': 'X x X x X x', 'say': '1 2 1 2 1 2'}, c(52, 'yk', seq=idx(0, 6))),
  ('B', 'The beat is the stage and the notes are the actors: the stage is there before anyone walks on. So watch it move for a bar, then step in. Until next time, Clara.', c(52, 'think')), ('P', 'One, two, three, four. Goodbye!', c(52, 'think'))])])

CH['T1'] = NEW['T1']
