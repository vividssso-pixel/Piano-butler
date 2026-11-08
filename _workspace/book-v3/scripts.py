# Scripts for "Butler explains", Part I Pitch. Follow each chapter's order: picture and secret, Examples, Try it.
# B = the Butler, P = Pip (a student). Every Example asks first; the answer comes after a pause, as in the book.
CH = {
'P1': ('The keyboard', [
 ('The secret', [
  ('B', 'Good day. I am your Piano Butler, and this is Pip.', {'p': 22, 'r': 'h:The keyboard'}), ('P', 'Hello! Today is the keyboard, right? There are so many keys. Do I have to count them all?', {'p': 22, 'r': 'hero'}),
  ('B', 'Never. Let us start with one fact. Left is low.', {'p': 22, 'r': 'hero'}), ('piano', 'C2', {'p': 22, 'r': 'hero'}), ('B', 'Right is high.', {'p': 22, 'r': 'hero'}), ('piano', 'C6', {'p': 22, 'r': 'hero'}),
  ('P', 'Low on the left, high on the right. Easy.', {'p': 22, 'r': 'hero'}), ('B', 'Now look at the black keys. They come in little groups: two, then three. Two, three, all the way along.', {'p': 22, 'r': 'hero'}),
  ('P', 'Like bumps on a road.', {'p': 22, 'r': 'hero'}), ('B', 'Exactly. Here is the secret. Every group has a first white key, just to its left. Next to the two black keys, the first key is C. Next to the three, it is F.', {'p': 22, 'r': 'secret'}),
  ('P', 'Two black keys: start on C. Three black keys: start on F.', {'p': 22, 'r': 'secret'}), ('B', 'Then walk on. C D E around the two.', {'p': 22, 'r': 'hero'}), ('piano', 'C4 D4 E4', {'p': 22, 'r': 'hero', 'seq': ['C', 'D', 'E']}), ('B', 'F G A B around the three.', {'p': 22, 'r': 'hero'}), ('piano', 'F4 G4 A4 B4', {'p': 22, 'r': 'hero', 'seq': ['F', 'G', 'A', 'B']}),
  ('P', 'And after G? Is there an H?', {'p': 22, 'r': 'two'}), ('B', 'No H at all. After G we start again at A, like the days of the week: Sunday comes round again after Saturday.', {'p': 22, 'r': 'two'}), ('piano', 'A4 B4 C5 D5 E5 F5 G5 A5', {'p': 22, 'r': 'two', 'seq': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A…']}),
  ('P', 'Seven letters, round and round.', {'p': 22, 'r': 'two'})]),
 ('The eight Cs', [
  ('B', 'Some Cs have names. The C nearest the middle is Middle C.', {'p': 23, 'r': 'hero', 'lab': ['Middle C']}), ('piano', 'C4', {'p': 23, 'r': 'hero', 'seq': ['Middle C']}),
  ('B', 'One C lower is Bass C. One C higher is Treble C. Further out: Low C and High C.', {'p': 23, 'r': 'hero'}), ('piano', 'C2 C3 C4 C5 C6', {'p': 23, 'r': 'hero', 'seq': ['Low C', 'Bass C', 'Middle C', 'Treble C', 'High C']}),
  ('P', 'And the ones at the very ends?', {'p': 23, 'r': 'hero'}), ('B', 'At the bottom, Lowest C. At the top, Very High C, and then Highest C, the very last key on the piano.', {'p': 23, 'r': 'hero'}), ('piano', 'C1 C7 C8', {'p': 23, 'r': 'hero', 'seq': ['Lowest C', 'Very High C', 'Highest C']}),
  ('P', 'Eight Cs! But the five in the middle are the ones I will use most.', {'p': 23, 'r': 'hero'}),
  ('B', 'Exactly. Theory books and apps give them numbers instead: C1 to C8, with Middle C as C4. And from one C to the next is an octave: eight notes, both Cs counted.', {'p': 22, 'r': 'two'})]),
 ('Example: find G', [
  ('B', 'Pip, find G for me. Do not count from the bottom.', {'p': 23, 'r': 'ex1', 'show': []}), ('P', 'Hmm. G lives with F, G, A and B, so I look for three black keys.', {'p': 23, 'r': 'ex1', 'show': []}),
  ('B', 'And the first key of that family?', {'p': 23, 'r': 'ex1', 'show': []}), ('P', 'F, just left of the three.', {'p': 23, 'r': 'ex1', 'lab': ['F'], 'show': ['F']}), ('B', 'Now walk on one key. Pause and find it yourself.', {'p': 23, 'r': 'ex1', 'lab': ['?'], 'show': ['F']}), ('pause', 4, {'p': 23, 'r': 'ex1', 'lab': ['?'], 'show': ['F']}),
  ('P', 'G! The key after F.', {'p': 23, 'r': 'ex1', 'lab': ['?'], 'reveal': True}), ('piano', 'F4 G4', {'p': 23, 'r': 'ex1', 'seq': ['F', '?'], 'reveal': True}), ('B', 'No need to start from C and count five. Find the group, find its first key, walk on.', {'p': 23, 'r': 'ex1', 'reveal': True})]),
 ('Example: find E', [
  ('B', 'Now E.', {'p': 23, 'r': 'ex2', 'show': []}), ('P', 'E is in C D E, so two black keys. Start on C, then C, D, E.', {'p': 23, 'r': 'ex2', 'show': []}), ('piano', 'C4 D4 E4', {'p': 23, 'r': 'ex2', 'seq': ['C', 'D', '?'], 'show': ['C', 'D']}),
  ('B', 'And where does E sit?', {'p': 23, 'r': 'ex2', 'lab': ['?'], 'show': ['C', 'D']}), ('P', 'Just right of the two black keys. The last of its family.', {'p': 23, 'r': 'ex2', 'lab': ['?'], 'reveal': True}), ('B', 'Splendid.', {'p': 23, 'r': 'ex2', 'reveal': True})]),
 ('Try it', [
  ('B', 'Before you go, a tune with no white keys at all. Right hand, fingers two, three and four on a group of three black keys.', {'p': 25, 'r': 'yk'}),
  ('P', 'Ready.', {'p': 25, 'r': 'yk'}), ('B', 'Four, three, two. Four, three, two. Two, two, two, two. Three, three, three, three. Four, three, two.', {'p': 25, 'r': 'yk'}),
  ('piano', 'A#4 G#4 F#4 | A#4 G#4 F#4 | F#4 F#4 F#4 F#4 G#4 G#4 G#4 G#4 | A#4 G#4 F#4', {'p': 25, 'r': 'yk'}), ('P', 'Hot Cross Buns!', {'p': 25, 'r': 'yk'}),
  ('B', 'Your mission: close your eyes and slide your hand along the keys. Two bumps, the key to their left is C. Three bumps, it is F. Until next time.', {'p': 25, 'r': 'think'})
])]),
'P2': ('The staff and the clefs', [
 ('The secret', [
  ('B', 'Pip, music is written on a staff: five lines and four spaces, counted from the bottom.'), ('P', 'Higher on the staff means higher on the piano?'),
  ('B', 'Always. But five lines alone do not tell us the notes. For that we need a clef: the key to the code.'),
  ('B', 'The treble clef curls round line two. That line is G.'), ('piano', 'G4'), ('B', 'The bass clef has two dots, and they hug line four. That line is F.'), ('piano', 'F3'),
  ('P', 'The treble clef curls round G. The bass clef’s dots hug F.'), ('B', 'Piano music joins the two staves with a brace: treble on top, usually the right hand; bass below, usually the left. Middle C sits between them, on a little line of its own.'), ('piano', 'C4')]),
 ('Example: one line, two notes', [
  ('B', 'Here is a puzzle. A note on the bottom line of the treble staff, and a note on the bottom line of the bass staff. Same line. Same note?'),
  ('P', 'I think so?'), ('B', 'Read each from its clef. Pause and try.'), ('pause', 4),
  ('P', 'Treble: G is line two, so step down, F in the space, then the bottom line is E.'), ('piano', 'E4'),
  ('B', 'And the bass? F is line four. Step down line by line.'), ('P', 'F, D, B, G. The bottom line is G!'), ('piano', 'G2'),
  ('B', 'Same line, different note. Always read the clef first.')]),
 ('Ledger lines', [
  ('P', 'What about notes above the staff?'), ('B', 'They sit on short extra lines, ledger lines. Step on from the staff: the top line of the treble staff is F. Then G on top, A on the first ledger line.'),
  ('piano', 'F5 G5 A5 B5 C6'), ('B', 'Two ledger lines up is High C.')]),
 ('Try it', [
  ('B', 'Point to the line the treble clef curls round, and play that G. Then the line between the bass clef’s dots, and play that F.'), ('pause', 4), ('piano', 'G4 F3 C4'),
  ('B', 'Middle C sits right between them. Your mission: look at any piece you play, and find the G line and the F line before you start. A clef is a pair of glasses: put on the right pair first.')])]),
'P3': ('Reading the notes', [
 ('The secret', [
  ('P', 'Do I have to learn every line and space by heart?'), ('B', 'Not at once. Start from a note you always know: treble G, bass F, or Middle C. Then step or skip.'),
  ('P', 'What is the difference?'), ('B', 'A step goes to the very next line or space: one letter on. A skip goes line to line, or space to space: two letters on.'),
  ('piano', 'G4 A4 | G4 B4')]),
 ('Example: read from the clef note', [
  ('B', 'A treble note on line four. Start from the clef note.'), ('P', 'G is line two. Skip up to line three: B. Skip again to line four...'), ('pause', 3),
  ('P', 'D!'), ('piano', 'G4 B4 D5'), ('B', 'G, B, D: two skips up from the clef’s G.')]),
 ('Example: a bass note', [
  ('B', 'Now the bass staff, line three.'), ('P', 'F is line four. Step down to the space: E. Step down again to line three...'), ('pause', 3),
  ('P', 'D.'), ('piano', 'F3 E3 D3'), ('B', 'Correct. F, E, D.')]),
 ('Words to remember', [
  ('B', 'If you like, there are little sentences. Treble lines: E G B D F, Every Good Boy Deserves Fun. Treble spaces spell FACE.'),
  ('B', 'Bass lines: G B D F A, Great Big Dragons Fly Away. Bass spaces: A C E G, All Cows Eat Grass.'), ('P', 'So the bass space two is C. Bass C!'), ('piano', 'C3')]),
 ('Try it', [
  ('B', 'Say the treble lines up and down, as fast as you can without a slip. E G B D F. F D B G E.'), ('pause', 5),
  ('B', 'Your mission: in a piece you play, find the clef notes first, then read each note by stepping or skipping from them. The clef notes are lamp posts on a dark road.')])]),
'P4': ('The staff and the keyboard', [
 ('The secret', [
  ('B', 'Pip, every line and every space of the staff is one white key, in order.'), ('P', 'So climbing the staff is climbing the keyboard?'),
  ('B', 'Exactly. From Bass C to Treble C, two octaves, with Middle C where the two staves meet.'), ('piano', 'C3 D3 E3 F3 G3 A3 B3 C4 D4 E4 F4 G4 A4 B4 C5'),
  ('B', 'One step on the staff, line to space, is the very next white key.')]),
 ('Example: mirror notes', [
  ('B', 'Here is something lovely. Find treble G and bass F on the piano.'), ('P', 'Treble G is just above Middle C: the second key of the three black keys. Bass F is just below: the first key of the three below.'),
  ('B', 'Now count each from Middle C. Up to G. Down to F. Pause and count.'), ('pause', 4),
  ('P', 'C D E F G: five. C B A G F: five as well!'), ('piano', 'C4 D4 E4 F4 G4 | C4 B3 A3 G3 F3'), ('B', 'Mirror images, the same distance either side of Middle C.')]),
 ('Example: from the key to the page', [
  ('B', 'I play the third white key up from Middle C.'), ('piano', 'C4 D4 E4'), ('P', 'C, D, E. E is note three.'),
  ('B', 'And on the staff?'), ('P', 'Middle C on its ledger line, D in the space under the staff, E on the bottom line.'), ('B', 'Precisely.')]),
 ('Try it', [
  ('B', 'Play Middle C and walk up the white keys, saying each name, and picture each one climbing the staff: line, space, line, space.'), ('pause', 5),
  ('B', 'Then Frère Jacques: the right hand plays C D E C; the left hand plays the same letters one octave lower, written in the bass clef.'), ('piano', 'C4 D4 E4 C4 | C3 D3 E3 C3'),
  ('B', 'The staff is a ladder laid beside the keyboard. Every rung is the next white key.')])]),
'P5': ('Sharps, flats and naturals', [
 ('The secret', [
  ('P', 'What are those little signs in front of some notes?'), ('B', 'Signs that move a note to the very next key. A sharp: one key to the right. A flat: one key to the left.'),
  ('B', 'Usually that next key is black. That is how the black keys get their names.'), ('piano', 'F4 F#4 | B4 Bb4'), ('B', 'And a natural cancels a sharp or flat: back to the white key.')]),
 ('Example: find F sharp', [
  ('B', 'Find F sharp, Pip.'), ('P', 'F is just left of the three black keys. Sharp means right...'), ('pause', 3),
  ('P', 'The very next key: the first black key of the three!'), ('piano', 'F4 F#4'), ('B', 'Correct.')]),
 ('Example: find B flat', [
  ('B', 'Now B flat.'), ('P', 'B is just right of the three black keys. Flat means left, so the top black key of the group.'), ('piano', 'B4 Bb4'),
  ('B', 'Splendid.')]),
 ('How long does a sign last?', [
  ('B', 'A sharp on the first note of a bar. Later in the same bar, the same note with no sign. Sharp or not?'), ('pause', 3),
  ('P', 'Still sharp?'), ('B', 'Yes. Until the bar line. After the bar line, it is plain again.'), ('P', 'A sticky note that falls off at the bar line.'), ('B', 'Very good.')]),
 ('Try it', [
  ('B', 'Beethoven’s Für Elise begins on E and the black key just left of it: D sharp.'), ('piano', 'E5 D#5 E5 D#5 E5 B4 D5 C5 A4'),
  ('B', 'Your mission: play E and D sharp back and forth, then find F sharp and B flat in three different places on the piano.')])]),
'P6': ('Counting intervals', [
 ('The secret', [
  ('B', 'Pip, how far apart are two notes? That distance is an interval.'), ('P', 'How do I measure it?'),
  ('B', 'Count the notes, both ends included. C to E: C, D, E. Three notes: a third.'), ('piano', 'C4 D4 E4 | [C4 E4]'),
  ('P', 'So C to G is C, D, E, F, G: a fifth.'), ('piano', 'C4 G4'), ('B', 'Exactly. And sharps and flats never change the number.')]),
 ('Example: count an interval', [
  ('B', 'F up to A. How many?'), ('pause', 3), ('P', 'F, G, A. Three: a third.'), ('piano', 'F4 A4'),
  ('B', 'And going down? C down to G.'), ('P', 'C, B, A, G. Four: a fourth.'), ('piano', 'C5 G4'), ('B', 'The same way, up or down.')]),
 ('Tones and semitones', [
  ('B', 'The smallest step on the piano is a semitone: from any key to the very next key, black or white.'), ('piano', 'E4 F4'),
  ('B', 'Two semitones make a tone.'), ('piano', 'C4 D4'), ('P', 'E to F has no black key between: a semitone. C to D has one between: a tone.'), ('B', 'Precisely.')]),
 ('Try it', [
  ('B', 'Twinkle, Twinkle begins with a leap.'), ('piano', 'C4 C4 G4 G4'), ('P', 'C up to G: five notes. A fifth!'),
  ('B', 'Your mission: find a third, a fifth and an octave from any C, and listen to how each one sounds.')])]),
'P7': ('Major, minor and perfect', [
 ('The secret', [
  ('B', 'Pip, two thirds can sound different. Listen.'), ('piano', '[C4 E4] | [C4 Eb4]'), ('P', 'The first is bright. The second is darker.'),
  ('B', 'To tell them apart, count the keys in between: black and white, but not the two you play.'),
  ('B', 'C to E has three keys between: C sharp, D, D sharp. A major third. C to E flat has two between: a minor third.')]),
 ('Example: the perfect fifth', [
  ('B', 'C up to G. How many keys between?'), ('pause', 4), ('P', 'C sharp, D, D sharp, E, F, F sharp. Six!'), ('piano', 'C4 G4'),
  ('B', 'Six keys between: a perfect fifth. And a perfect fourth has four between.')]),
 ('Example: major or minor third?', [
  ('B', 'D up to F.'), ('P', 'D sharp and E between. Two keys.'), ('B', 'So?'), ('P', 'A minor third!'), ('piano', 'D4 F4'), ('B', 'Splendid.')]),
 ('Try it', [
  ('B', 'Play C and E together, then C and E flat. Bright, then darker.'), ('piano', '[C4 E4] | [C4 Eb4]'),
  ('B', 'Your mission: from three different notes, build a major third, three keys between, and a minor third, two keys between. Listen each time. Until next time, Pip.'), ('P', 'Goodbye!')])]),
}
