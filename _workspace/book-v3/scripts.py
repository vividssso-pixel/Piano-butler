# Scripts for "Butler explains", Part I Pitch. Follow each chapter's order: picture and secret, Examples, Try it.
# B = the Butler, P = Pip (a student). Every Example asks first; the answer comes after a pause, as in the book.
def c(p, r, **k): d = {'p': p, 'r': r}; d.update(k); return d
def idx(a, b): return ['#%d' % i for i in range(a, b)]
W = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
NEW = {
'P2': ('The staff and the clefs', [
 ('The secret', [
  ('B', 'Pip, music is written on a staff: five lines and four spaces, counted from the bottom.', c(27, 'lead')), ('P', 'Higher on the staff means higher on the piano?', c(27, 'lead')),
  ('B', 'Always. But five lines alone do not tell us the notes. For that we need a clef: the key to the code.', c(27, 'hero')),
  ('B', 'Look closely. The treble clef curls round line two. That line is G.', c(27, 'hero')), ('piano', 'G4', c(27, 'hero', seq=['G'])),
  ('B', 'The bass clef has two dots, and they hug line four. That line is F.', c(27, 'hero')), ('piano', 'F3', c(27, 'hero', seq=['F'])),
  ('P', 'The treble clef curls round G. The bass clef’s dots hug F.', c(27, 'secret')),
  ('B', 'Piano music joins the two staves with a brace: treble on top, usually the right hand; bass below, usually the left. Middle C sits between them, on a short line of its own.', c(27, 'two')), ('piano', 'C4', c(27, 'two'))]),
 ('Ledger lines', [
  ('P', 'What about notes above or below the staff?', c(27, 'h:Ledger lines: the staff carried on')),
  ('B', 'They sit on short extra lines called ledger lines, spaced just like the staff lines. Step on from the nearest staff line: line, space, line, space.', c(28, 'two')),
  ('B', 'In the treble: A, B, C below the staff, and A, B, C above it.', c(28, 'two')), ('piano', 'A3 B3 C4 | A5 B5 C6', c(28, 'two', seq=idx(0, 6))),
  ('B', 'In the bass: E, D, C below, and C, D, E above.', c(28, 'two')), ('piano', 'E2 D2 C2 | C4 D4 E4', c(28, 'two', seq=idx(6, 12))),
  ('P', 'That is a lot of little lines.', c(28, 'two2')),
  ('B', 'So a very high passage is often written lower, with an ottava sign and a dotted line above it: play those notes one octave higher, until the dotted line stops. Under the staff, it means an octave lower.', c(28, 'two2'))]),
 ('Example: one line, two notes', [
  ('B', 'Here is a puzzle. Two red notes, both on the bottom line: one in the treble staff, one in the bass. Same line. Same note?', c(28, 'ex1')),
  ('P', 'I think so?', c(28, 'ex1')), ('B', 'Read each from its clef. Pause and try.', c(28, 'ex1')), ('pause', 4, c(28, 'ex1')),
  ('P', 'Treble: G is line two. Step down, F in the space, then the bottom line is E.', c(28, 'ex1', lab=['#0'])), ('piano', 'E4', c(28, 'ex1', seq=['#0'])),
  ('B', 'And the bass? F is line four. Step down line by line.', c(28, 'ex1')), ('P', 'F, D, B, G. The bottom line is G!', c(28, 'ex1', lab=['#1'], reveal=True)), ('piano', 'G2', c(28, 'ex1', seq=['#1'], reveal=True)),
  ('B', 'Same line, different note. Always read the clef first.', c(28, 'ex1', reveal=True))]),
 ('Example: which staff?', [
  ('B', 'Now a key on the piano. Which staff would it be written on?', c(28, 'ex2', show=['Middle C'])),
  ('P', 'First I find Middle C. The question mark is to its left.', c(28, 'ex2', show=['Middle C'], lab=['Middle C'])),
  ('B', 'Left is lower. And low keys go on which staff? Pause and think.', c(28, 'ex2', show=['Middle C'], lab=['?'])), ('pause', 3, c(28, 'ex2', show=['Middle C'], lab=['?'])),
  ('P', 'The bass staff, usually for the left hand!', c(28, 'ex2', reveal=True)), ('B', 'Quite right.', c(28, 'ex2', reveal=True))]),
 ('Example: a high note', [
  ('B', 'A high note on ledger lines. Start from the top line of the treble staff: F.', c(29, 'ex3', show=['F'], lab=['F'])),
  ('P', 'Then G on top of the staff, A on the first ledger line, B above it.', c(29, 'ex3', show=['F', 'G', 'A', 'B'])), ('piano', 'F5 G5 A5 B5', c(29, 'ex3', seq=['F', 'G', 'A', 'B'], show=['F', 'G', 'A', 'B'])),
  ('B', 'And the red note, on the second ledger line? Pause and try.', c(29, 'ex3', show=['F', 'G', 'A', 'B'], lab=['?'])), ('pause', 3, c(29, 'ex3', show=['F', 'G', 'A', 'B'], lab=['?'])),
  ('P', 'C! High C.', c(29, 'ex3', lab=['?'], reveal=True)), ('piano', 'C6', c(29, 'ex3', seq=['?'], reveal=True)),
  ('B', 'Two ledger lines up: High C, two octaves above Middle C.', c(29, 'ex3', reveal=True))]),
 ('Try it', [
  ('B', 'Point to the line the treble clef curls round, and play that G. Then the line between the bass clef’s dots, and play that F. Middle C sits between them.', c(29, 'try10')), ('pause', 4, c(29, 'try10')), ('piano', 'G4 F3 C4', c(29, 'try10')),
  ('B', 'And a tune you know. Twinkle, Twinkle starts on Middle C and leaps up to G, the treble clef’s very own line.', c(29, 'yk')), ('piano', 'C4 C4 G4 G4 A4 A4 G4*2', c(29, 'yk', seq=idx(0, 7))),
  ('B', 'Your mission: before you play any piece, find the G line and the F line. A clef is a pair of glasses: put on the right pair first.', c(29, 'watch'))])]),
'P3': ('Reading the notes', [
 ('The secret', [
  ('P', 'Do I have to learn every line and space by heart?', c(30, 'lead')),
  ('B', 'Not at once. Start from a note you always know: treble G, bass F, or Middle C.', c(30, 'hero')), ('piano', 'G4 F3 C4', c(30, 'hero', seq=['G', 'F', 'Middle C'])),
  ('P', 'And then?', c(30, 'rule')),
  ('B', 'Then step or skip. A step goes to the very next line or space: one letter on. A skip goes line to line, or space to space: two letters on.', c(30, 'rule')), ('piano', 'G4 A4 | G4 B4', c(30, 'rule'))]),
 ('Words to remember', [
  ('B', 'If you like little sentences, here are four. Treble lines: E G B D F. Every Good Boy Deserves Fun.', c(30, 'two')), ('piano', 'E4 G4 B4 D5 F5', c(30, 'two', seq=idx(0, 5))),
  ('B', 'The treble spaces spell a word: F A C E, face.', c(30, 'two')), ('piano', 'F4 A4 C5 E5', c(30, 'two', seq=idx(5, 9))),
  ('B', 'Bass lines: G B D F A. Great Big Dragons Fly Away.', c(30, 'two2')), ('piano', 'G2 B2 D3 F3 A3', c(30, 'two2', seq=idx(0, 5))),
  ('B', 'Bass spaces: A C E G. All Cows Eat Grass.', c(30, 'two2')), ('piano', 'A2 C3 E3 G3', c(30, 'two2', seq=idx(5, 9)))]),
 ('Example: read from the clef note', [
  ('B', 'A treble note you are not sure of, on line four. Start from the clef note.', c(31, 'ex1')),
  ('P', 'G is line two. Skip up to line three: B. Skip again to line four.', c(31, 'ex1')), ('pause', 3, c(31, 'ex1')),
  ('P', 'D!', c(31, 'ex1', reveal=True)), ('piano', 'G4 B4 D5', c(31, 'ex1', reveal=True)), ('B', 'G, B, D: two skips up from the clef’s G.', c(31, 'ex1', reveal=True))]),
 ('Example: a bass note', [
  ('B', 'Now the bass staff, line three.', c(31, 'ex2', show=[])),
  ('P', 'The dots hug line four: F. Step down to the space: E. Step down again to line three.', c(31, 'ex2', show=['F', 'E'])), ('piano', 'F3 E3', c(31, 'ex2', seq=['F', 'E'], show=['F', 'E'])), ('pause', 3, c(31, 'ex2', show=['F', 'E'], lab=['?'])),
  ('P', 'D.', c(31, 'ex2', lab=['?'], reveal=True)), ('piano', 'F3 E3 D3', c(31, 'ex2', seq=['F', 'E', '?'], reveal=True)), ('B', 'Correct. F, E, D.', c(31, 'ex2', reveal=True))]),
 ('Example: Treble C and Bass C', [
  ('B', 'Find Treble C on the staff. These notes sit in the spaces.', c(31, 'ex3')),
  ('P', 'The treble spaces spell face. F, A, and space three is C!', c(31, 'ex3', lab=['?'], reveal=True)), ('piano', 'F4 A4 C5', c(31, 'ex3', reveal=True)),
  ('B', 'Treble C, one octave above Middle C. And in the bass spaces?', c(32, 'ex4')),
  ('P', 'All Cows. Space two is C: Bass C!', c(32, 'ex4', lab=['?'], reveal=True)), ('piano', 'A2 C3', c(32, 'ex4', reveal=True)),
  ('B', 'One octave below Middle C. The same Cs you found on the keyboard.', c(32, 'ex4', reveal=True))]),
 ('Try it', [
  ('B', 'Say the treble lines up and down, as fast as you can without a slip. E G B D F. F D B G E.', c(31, 'try10')), ('pause', 5, c(31, 'try10')),
  ('B', 'Then Mary Had a Little Lamb. E, D, C: line, space, ledger line, one step down each time.', c(32, 'yk')), ('piano', 'E4 D4 C4 D4 E4 E4 E4*2', c(32, 'yk', seq=idx(0, 7))),
  ('B', 'Your mission: in a piece you play, find the clef notes first, then step or skip from them. The clef notes are lamp posts on a dark road.', c(32, 'think'))])]),
'P4': ('The staff and the keyboard', [
 ('The secret', [
  ('B', 'Pip, every line and every space of the grand staff is one white key, in order.', c(33, 'lead')), ('P', 'So climbing the staff is climbing the keyboard?', c(33, 'vx')),
  ('B', 'Exactly. Here are two octaves, from Bass C up to Treble C, with Middle C where the two staves meet.', c(33, 'vx')),
  ('piano', 'C3 D3 E3 F3 G3 A3 B3 C4 D4 E4 F4 G4 A4 B4 C5', c(33, 'vx', seq=idx(0, 15))),
  ('B', 'Middle C can be written in either staff: on a ledger line below the treble, or above the bass. Same key; the hand that plays it chooses.', c(33, 'p')),
  ('B', 'One step on the staff, line to space, is the very next white key. The black keys sit in between: they come in the next chapter.', c(33, 'rule'))]),
 ('Example: from the page to the key', [
  ('B', 'A note on line four of the bass staff. Which key is it?', c(34, 'ex1', show=['Middle C'])),
  ('P', 'Line four, between the clef’s dots: F.', c(34, 'ex1', show=['Middle C', 'F'], lab=['F'])),
  ('B', 'And where is it on the piano? Pause and find it.', c(34, 'ex1', show=['Middle C', 'F'])), ('pause', 3, c(34, 'ex1', show=['Middle C', 'F'])),
  ('P', 'The three black keys just below Middle C. F is the first key of that family.', c(34, 'ex1', reveal=True)), ('piano', 'F3', c(34, 'ex1', reveal=True))]),
 ('Example: mirror notes', [
  ('B', 'Here is something lovely. Find treble G and bass F on the piano.', c(34, 'ex2', show=['Middle C'])),
  ('P', 'Treble G: the second key of the three black keys just above Middle C. Bass F: the first key of the three just below.', c(34, 'ex2', show=['Middle C'])),
  ('B', 'Now count each from Middle C. Up to G, down to F. Pause and count.', c(34, 'ex2', show=['Middle C'])), ('pause', 4, c(34, 'ex2', show=['Middle C'])),
  ('P', 'C D E F G: five. C B A G F: five as well!', c(34, 'ex2', reveal=True)), ('piano', 'C4 D4 E4 F4 G4 | C4 B3 A3 G3 F3', c(34, 'ex2', reveal=True)),
  ('B', 'Mirror images, the same distance either side of Middle C.', c(34, 'ex2', reveal=True))]),
 ('Example: from the key to the page', [
  ('B', 'I play the third white key up from Middle C.', c(34, 'ex3', show=['Middle C'])), ('piano', 'C4 D4 E4', c(34, 'ex3', seq=['Middle C', '', '?'], show=['Middle C'])),
  ('P', 'C one, D two, E three. It is E.', c(34, 'ex3', lab=['?'], show=['Middle C'])),
  ('B', 'And on the staff?', c(34, 'ex3', show=['Middle C'])), ('P', 'Middle C on its ledger line, D in the space under the staff, E on the bottom line.', c(34, 'ex3', reveal=True)), ('B', 'Precisely.', c(34, 'ex3', reveal=True))]),
 ('Try it', [
  ('B', 'Play Middle C and walk up the white keys, saying each name, and picture each one climbing the staff: line, space, line, space.', c(35, 'try10')), ('piano', 'C4 D4 E4 F4 G4 A4 B4 C5', c(35, 'try10', seq=idx(0, 8))),
  ('B', 'Then Frère Jacques in both hands. The right hand plays C D E C; the left hand plays the same letters one octave lower, in the bass clef.', c(35, 'yk')), ('piano', 'C4 D4 E4 C4 | C3 D3 E3 C3', c(35, 'yk', seq=idx(0, 4) + idx(0, 4))),
  ('B', 'The staff is a ladder laid beside the keyboard: every rung is the next white key.', c(35, 'think'))])]),
'P5': ('Sharps, flats and naturals', [
 ('The secret', [
  ('P', 'What are those little signs in front of some notes?', c(36, 'lead')),
  ('B', 'Signs that move a note to the very next key. A sharp: one key to the right. A flat: one key to the left.', c(36, 'secret')),
  ('B', 'Usually that next key is black, and that is how the black keys get their names. D sharp is just right of D. D flat is just left of it.', c(36, 'hero')), ('piano', 'D4 D#4 | D4 Db4', c(36, 'hero', seq=['D', 'D♯', 'D', 'D♭'])),
  ('B', 'And a natural cancels a sharp or flat: back to the white key.', c(36, 'ht'))]),
 ('Example: find F sharp', [
  ('B', 'Find F sharp, Pip.', c(36, 'ex1', show=[])), ('P', 'F is just left of the three black keys.', c(36, 'ex1', show=['F'], lab=['F'])),
  ('B', 'Sharp means right: the very next key. Black or white? Pause and put your finger on it.', c(36, 'ex1', show=['F'], lab=['?'])), ('pause', 3, c(36, 'ex1', show=['F'], lab=['?'])),
  ('P', 'Black! The first black key of the three.', c(36, 'ex1', lab=['?'], reveal=True)), ('piano', 'F4 F#4', c(36, 'ex1', seq=['F', '?'], reveal=True)), ('B', 'Correct: F sharp.', c(36, 'ex1', reveal=True))]),
 ('Example: find B flat', [
  ('B', 'Now B flat.', c(37, 'ex2', show=[])), ('P', 'B is just right of the three black keys. Flat means left.', c(37, 'ex2', show=['B'], lab=['B'])), ('pause', 3, c(37, 'ex2', show=['B'], lab=['?'])),
  ('P', 'The top black key of the group!', c(37, 'ex2', lab=['?'], reveal=True)), ('piano', 'B4 Bb4', c(37, 'ex2', seq=['B', '?'], reveal=True)), ('B', 'Splendid.', c(37, 'ex2', reveal=True))]),
 ('Example: how long does a sign last?', [
  ('B', 'A sharp on the first note of a bar: F sharp. Later in the same bar, the same note with no sign. Sharp or not?', c(37, 'ex3', show=['F♯', 'G'], lab=['F♯'])), ('pause', 3, c(37, 'ex3', show=['F♯', 'G'])),
  ('P', 'Still sharp?', c(37, 'ex3', show=['F♯', 'G'])), ('B', 'Yes, until the bar line. And after the bar line?', c(37, 'ex3', show=['F♯', 'G'])),
  ('P', 'Plain F again!', c(37, 'ex3', reveal=True)), ('B', 'A sign lasts to the end of its bar. Now a natural: B, then B flat, and it stays flat for the rest of the bar. Then a natural sign. What does it do?', c(37, 'ex4', show=['B', 'B♭'])), ('pause', 3, c(37, 'ex4', show=['B', 'B♭'])),
  ('P', 'It cancels the flat: back to the white key B.', c(37, 'ex4', lab=['?'], reveal=True)), ('piano', 'B4 Bb4 Bb4 B4', c(37, 'ex4', seq=idx(0, 4), reveal=True))]),
 ('Example: one key, two names', [
  ('B', 'One more. F sharp, then G flat. Find both on the keyboard.', c(38, 'ex5', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'])),
  ('P', 'They are the same black key!', c(38, 'ex5', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], lab=['F♯', 'G♭'])), ('piano', 'F#4 Gb4', c(38, 'ex5', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], seq=['F♯', 'G♭'])),
  ('B', 'Same sound, two names: we call them enharmonic. And E sharp, one key right of E?', c(38, 'ex5', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], lab=['E♯'])), ('pause', 3, c(38, 'ex5', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'])),
  ('P', 'There is no black key there. So E sharp is the white key F!', c(38, 'ex5', reveal=True)), ('piano', 'E4 F4', c(38, 'ex5', reveal=True))]),
 ('Try it', [
  ('B', 'Beethoven’s Für Elise begins on E and the black key just left of it: D sharp. The sharp is written again in the new bar, because the bar line wiped it out.', c(38, 'yk')), ('piano', 'E5/2 D#5/2 E5/2 D#5/2 E5/2 B4/2 D5/2 C5/2 A4*2', c(38, 'yk')),
  ('B', 'Your mission: play E and D sharp back and forth, then find F sharp and B flat in three different places on the piano. A sign is a sticky note: it falls off at the bar line.', c(38, 'think'))])]),
'P6': ('Counting intervals', [
 ('The secret', [
  ('B', 'Pip, how far apart are two notes? That distance is an interval.', c(39, 'lead')), ('P', 'How do I measure it?', c(39, 'lead')),
  ('B', 'Count the notes, both ends included. C to E: C, D, E. Three notes: a third.', c(39, 'hero')), ('piano', 'C4 D4 E4 | [C4 E4]', c(39, 'hero', seq=['#7', '#8', '#9', '#9'])),
  ('B', 'And sharps and flats never change the number.', c(39, 'rule')),
  ('B', 'From C, the numbers go: unison, second, third, fourth, fifth, sixth, seventh, octave.', c(39, 'vx')), ('piano', 'C4 D4 E4 F4 G4 A4 B4 C5', c(39, 'vx', seq=['unison', '2nd', '3rd', '4th', '5th', '6th', '7th', '8ve'])),
  ('P', 'So C to G is C, D, E, F, G: a fifth.', c(39, 'vx', lab=['5th']))]),
 ('Tones and semitones', [
  ('B', 'The smallest step on the piano is a semitone: from any key to the very next key, black or white.', c(39, 'two')), ('piano', 'E4 F4', c(39, 'two', seq=['#0', '#1'])),
  ('B', 'Two semitones make a tone.', c(39, 'two')), ('piano', 'C4 D4', c(39, 'two', seq=['#4', '#5'])),
  ('P', 'E to F and B to C have no black key between: semitones. C to D has one between: a tone.', c(39, 'two')), ('B', 'Precisely.', c(39, 'two'))]),
 ('Example: count an interval', [
  ('B', 'F up to A. How many notes? Pause and count.', c(40, 'ex1', show=['F', 'A', 'C', 'G'])), ('pause', 3, c(40, 'ex1', show=['F', 'A', 'C', 'G'])),
  ('P', 'F, G, A. Three: a third.', c(40, 'ex1', show=['F', '(G)', 'A', 'C', 'G'])), ('piano', 'F4 G4 A4', c(40, 'ex1', seq=['F', '(G)', 'A'], show=['F', '(G)', 'A', 'C', 'G'])),
  ('B', 'And going down? C down to G.', c(40, 'ex1', show=['F', '(G)', 'A', 'C', 'G'])), ('P', 'C, B, A, G. Four: a fourth.', c(40, 'ex1', reveal=True)), ('piano', 'C5 B4 A4 G4', c(40, 'ex1', seq=['C', '(B)', '(A)', 'G'], reveal=True)),
  ('B', 'The same way, up or down: the first note is one.', c(40, 'ex1', reveal=True))]),
 ('Example: tone or semitone?', [
  ('B', 'Look between the two red keys, E and F. Is there a black key between them?', c(40, 'ex2', show=W, lab=['E', 'F'])),
  ('P', 'No: they are next-door keys. A semitone.', c(40, 'ex2', show=W)), ('B', 'And C to D?', c(40, 'ex2', show=W, lab=['C', 'D'])),
  ('P', 'C sharp is between them: a tone.', c(40, 'ex2', reveal=True))]),
 ('Example: name an interval', [
  ('B', 'E, and the C above it. Count the notes from E.', c(40, 'ex3', show=W)), ('pause', 3, c(40, 'ex3', show=W)),
  ('P', 'E one, F two, G three, A four, B five, C six. A sixth!', c(40, 'ex3', reveal=True)), ('piano', 'E4 F4 G4 A4 B4 C5', c(40, 'ex3', seq=idx(2, 8), reveal=True)),
  ('B', 'Melodic or harmonic, the number is the same. C then E, one after the other, is a melodic third. C and E together, a harmonic third.', c(41, 'ex4', lab=['melodic', 'harmonic'], reveal=True)), ('piano', 'C4 E4 | [C4 E4]', c(41, 'ex4', seq=['melodic', 'melodic', 'harmonic'], reveal=True))]),
 ('Try it', [
  ('B', 'Thumb on C, finger five on G: your hand is a ruler, and that is a fifth. Thumb to finger three: a third.', c(40, 'try10')), ('piano', '[C4 G4] | [C4 E4]', c(40, 'try10')),
  ('B', 'Twinkle, Twinkle begins with a leap.', c(41, 'yk')), ('piano', 'C4 C4 G4 G4', c(41, 'yk', seq=['1', '1', '5', '5'])), ('P', 'C up to G: five notes. A fifth!', c(41, 'yk')),
  ('B', 'Monday to Wednesday is three days, not two: you count the day you start on. Intervals count the same way. Your mission: find a third, a fifth and an octave from any C.', c(41, 'think'))])]),
'P7': ('Major, minor and perfect', [
 ('The secret', [
  ('B', 'Pip, two thirds can sound different. Listen.', c(42, 'lead')), ('piano', '[C4 E4] | [C4 Eb4]', c(42, 'lead')), ('P', 'The first is bright. The second is darker.', c(42, 'lead')),
  ('B', 'Both are thirds: three notes each. To tell them apart, count the keys in between, black and white, but not the two you play.', c(42, 'secret')),
  ('B', 'C to E has three keys between: C sharp, D, D sharp. A major third.', c(42, 'hero')), ('piano', 'C#4 D4 D#4', c(42, 'hero', seq=idx(7, 10))),
  ('B', 'C to E flat has only two between, one fewer. A minor third.', c(42, 'hero')), ('piano', 'C#4 D4', c(42, 'hero', seq=idx(18, 20))),
  ('B', 'Thirds and sixths come in two sizes, major and minor. Fourths, fifths and octaves have one main size, called perfect. They are never major or minor.', c(42, 'two'))]),
 ('Example: major or minor third?', [
  ('B', 'C up to the red black key, E flat. A third. Now count the keys between. Pause and count.', c(42, 'ex1', show=W)), ('pause', 3, c(42, 'ex1', show=W)),
  ('P', 'C sharp, D. Two between.', c(42, 'ex1', show=W)), ('B', 'A major third has three between. So?', c(42, 'ex1', show=W)),
  ('P', 'A minor third!', c(42, 'ex1', reveal=True)), ('piano', '[C4 Eb4]', c(42, 'ex1', reveal=True))]),
 ('Example: F up to A', [
  ('B', 'F up to A. F, G, A: a third. Now the keys between: they are numbered.', c(43, 'ex2', show=W)),
  ('P', 'F sharp, G, G sharp: three. A major third!', c(43, 'ex2', reveal=True)), ('piano', 'F#4 G4 G#4 | [F4 A4]', c(43, 'ex2', seq=['1', '2', '3'], reveal=True)),
  ('B', 'The same size as C to E.', c(43, 'ex2', reveal=True))]),
 ('Example: D up to A', [
  ('B', 'D up to A. The number first.', c(43, 'ex3', show=W)), ('P', 'D, E, F, G, A: five notes, a fifth.', c(43, 'ex3', show=W)),
  ('B', 'And six keys between. A fifth with six between is its main size. What is that called?', c(43, 'ex3', show=W)), ('pause', 3, c(43, 'ex3', show=W)),
  ('P', 'A perfect fifth!', c(43, 'ex3', reveal=True)), ('piano', '[D4 A4]', c(43, 'ex3', reveal=True))]),
 ('Example: E up to C', [
  ('B', 'E up to C. E, F, G, A, B, C: a sixth. A major sixth has eight between. Count this one.', c(44, 'ex4', show=W)), ('pause', 4, c(44, 'ex4', show=W)),
  ('P', 'Seven! One fewer: a minor sixth.', c(44, 'ex4', reveal=True)), ('piano', '[E4 C5]', c(44, 'ex4', reveal=True))]),
 ('Try it', [
  ('B', 'Play C and E, then C and E flat. Bright, then dark. One key makes the difference.', c(44, 'try10')), ('piano', '[C4 E4] | [C4 Eb4]', c(44, 'try10')),
  ('B', 'And Beethoven’s Fifth: da-da-da-dum. G down to E flat is a third, with three keys between: a major third.', c(44, 'yk')), ('piano', 'G4/2 G4/2 G4/2 Eb4*3', c(44, 'yk', seq=idx(0, 4))),
  ('B', 'A major and a minor third are a smile and a frown: the same face, one small change at the corners. Until next time, Pip.', c(44, 'think')), ('P', 'Goodbye!', c(44, 'think'))])]),
}

CH = {
'P1': ('The keyboard', [
 ('The secret', [
  ('B', 'Good day. I am your Piano Butler, and this is Pip.', {'p': 22, 'r': 'h:The keyboard'}), ('P', 'Hello! Today is the keyboard, right? There are so many keys. Do I have to count them all?', {'p': 22, 'r': 'hero'}),
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
  ('B', 'Pip, find G for me. Do not count from the bottom.', {'p': 24, 'r': 'ex1', 'show': []}), ('P', 'Hmm. G lives with F, G, A and B, so I look for three black keys.', {'p': 24, 'r': 'ex1', 'show': []}),
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
  ('B', 'Pip, put your hand on your heart.', c(47, 'lead')), ('P', 'It is beating. Steady, steady.', c(47, 'lead')),
  ('B', 'That steady beat is a pulse, and almost every piece of music has one. Its speed is the tempo. Beats travel in groups called bars, and beat one is the strongest.', c(47, 'hero')),
  ('piano', 'X x x x X x x x X x x x', c(47, 'hero', seq=idx(0, 12))),
  ('B', 'Here is the secret. The beat never stops, not even in a rest. Feel it before you play.', c(47, 'secret')),
  ('P', 'So in a rest I still count?', c(47, 'hero')), ('B', 'Always. Listen: in the second bar the notes stop, and the beat goes on.', c(47, 'hero')),
  ('piano', 'C5 C4 C4 C4 C5 C4 R R C5 C4 C4 C4', c(47, 'hero', seq=idx(0, 12)))]),
 ('Tempo', [
  ('B', 'Tempo is measured in beats per minute. A metronome mark at the top of the music shows it. Crotchet equals sixty means sixty beats a minute: one every second.', c(47, 'two')),
  ('piano', 'X@60 x@60 x@60 x@60', c(47, 'two')), ('B', 'Crotchet equals one hundred and twenty is twice as fast.', c(47, 'two')),
  ('piano', 'X@120 x@120 x@120 x@120 X@120 x@120 x@120 x@120', c(47, 'two')),
  ('P', 'Twice as many ticks in the same time.', c(47, 'two'))]),
 ('Strong and weak beats', [
  ('B', 'The beats are not all the same. Two beats in a bar go strong, weak, like a march.', c(47, 'two')), ('piano', 'X x X x X x X x', c(47, 'two')),
  ('B', 'Three go strong, weak, weak, like a waltz.', c(47, 'two')), ('piano', 'X x x X x x X x x', c(47, 'two')),
  ('B', 'And four go strong, weak, medium, weak, like most songs.', c(47, 'two')), ('piano', 'X x M x X x M x', c(47, 'two')),
  ('P', 'So Twinkle, Twinkle is in four, and Happy Birthday is in three.', c(48, 'ht')), ('B', 'Exactly. And the Radetzky March is in two.', c(48, 'ht'))]),
 ('Bars and bar lines', [
  ('B', 'A bar line divides the music into bars. A double bar line marks the end of a section, or a change. A final bar line, thin then thick, marks the end of the piece.', c(47, 'ht')),
  ('B', 'And repeat signs: play the passage between them again. If there is no start sign, go back to the beginning.', c(47, 'ht'))]),
 ('Counting', [
  ('B', 'Every beat is counted, even inside a long note. Here are three bars of three-four. The red number is where you play; the grey numbers are the beats you hold.', c(48, 'vx')),
  ('piano', 'X x x X x x X x x', c(48, 'vx', seq=idx(0, 9))),
  ('B', 'Count aloud at one speed, a little louder on beat one. With a metronome, start slower than you think, and speed up only when the passage is steady.', c(48, 'p'))]),
 ('Example: march or waltz?', [
  ('B', 'Is this a march or a waltz? Tap a steady beat as you listen.', c(48, 'ex1')), ('piano', 'C3 G4 G4 C3 G4 G4 C3 G4 G4', c(48, 'ex1', seq=idx(0, 9))),
  ('B', 'Which beats feel heavier? Count from one heavy beat to the next. Pause and count.', c(48, 'ex1')), ('pause', 3, c(48, 'ex1')),
  ('P', 'Heavy every three: one two three, one two three. A waltz!', c(48, 'ex1', reveal=True)), ('B', 'Every two would be a march.', c(48, 'ex1', reveal=True))]),
 ('Example: feel the beat first', [
  ('B', 'This one says crotchet equals ninety-six: ninety-six beats a minute. Do not start yet. Listen to one full bar, counting one, two, three in your head.', c(48, 'ex2')),
  ('piano', 'X@96 x@96 x@96', c(48, 'ex2', seq=['#1', '#2', '#3'])),
  ('B', 'Then step in on the next beat one, the way you step onto a moving escalator.', c(48, 'ex2')),
  ('piano', 'X@96 x@96 x@96 C4@96 E4@96 G4@96 C5@96 G4@96 E4@96', c(48, 'ex2', seq=['#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9'])),
  ('P', 'The first note landed right on the beat!', c(48, 'ex2', reveal=True))]),
 ('Try it', [
  ('B', 'Hand on your heart. Tap the beat and say one, two, three, four, with one a little louder. Keep going for ten seconds without slowing down.', c(49, 'try10')),
  ('piano', 'X@80 x@80 x@80 x@80 X@80 x@80 x@80 x@80 X@80 x@80 x@80 x@80', c(49, 'try10', seq=idx(0, 12))),
  ('B', 'At the New Year concert in Vienna, the audience claps along on every beat of the Radetzky March. That steady clap is the pulse; the tune moves freely over it.', c(49, 'yk')),
  ('piano', 'X x X x X x', c(49, 'yk', seq=idx(0, 6))),
  ('B', 'The beat is the stage and the notes are the actors: the stage is there before anyone walks on. So watch it move for a bar, then step in. Until next time, Pip.', c(49, 'think')), ('P', 'One, two, three, four. Goodbye!', c(49, 'think'))])])

CH['T1'] = NEW['T1']
