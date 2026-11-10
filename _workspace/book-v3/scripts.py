# Scripts for "Butler explains", Part I Pitch. Follow each chapter's order: picture and secret, Examples, Try it.
# B = the Butler, P = Clara (a student). Every Example asks first; the answer comes after a pause, as in the book.
def c(p, r, **k): d = {'p': p, 'r': r}; d.update(k); return d
def idx(a, b): return ['#%d' % i for i in range(a, b)]
W = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
NEW = {
'P2': ('The staff and the clefs', [
 ('The secret', [
  ('B', 'Clara, music is written on a staff: five lines and four spaces, counted from the bottom.', c(27, 'xlate', anim='lines')), ('P', 'Higher on the staff means higher on the piano?', c(27, 'lead')),
  ('B', 'Always. But five lines alone do not tell us the notes. For that we need a clef: the key to the code.', c(27, 'hero')),
  ('B', 'Look closely. And now, as I promised, may I present Their Majesties, who rule these two staves.', c(27, 'hero')),
  ('Q', 'Good day, Clara. I am the Queen of the treble staff. See how my clef curls round line two? That line is my G, which is why my clef is also called the G clef.', c(27, 'hero')), ('piano', 'G4', c(27, 'hero', seq=['G'])),
  ('K', 'And I am the King of the bass staff. My clef’s two dots hug line four. That line is my F, so my clef is the F clef, and the low notes are my kingdom.', c(27, 'hero')), ('piano', 'F3', c(27, 'hero', seq=['F'])),
  ('P', 'A Queen for the high notes and a King for the low ones! The treble clef curls round G. The bass clef’s dots hug F.', c(27, 'secret'))]),
 ('The grand staff', [
  ('B', 'Piano music joins two staves with a brace. The treble staff is on top, usually for the right hand. The bass staff is below, usually for the left.', c(28, 'xlate')),
  ('B', 'And Middle C sits between them, on a short line of its own. It can be written in either staff: the same key.', c(28, 'xlate')), ('piano', 'C4', c(28, 'xlate')),
  ('Q', 'Middle C is the border between our two kingdoms.', c(28, 'xlate')), ('K', 'And we share it. Either of us may write it.', c(28, 'xlate'))]),
 ('Example: which staff?', [
  ('B', 'Here is a key on the piano. Which staff would it be written on?', c(28, 'ex1', show=['Middle C'])),
  ('P', 'First I find Middle C. The question mark is to its left.', c(28, 'ex1', show=['Middle C'], lab=['Middle C'])),
  ('B', 'Left is lower. And low keys go on which staff? Pause and think.', c(28, 'ex1', show=['Middle C'], lab=['?'])), ('pause', 3, c(28, 'ex1', show=['Middle C'], lab=['?'])),
  ('P', 'The bass staff, usually for the left hand!', c(28, 'ex1', reveal=True)), ('B', 'Quite right. High keys go on the treble staff.', c(28, 'ex1', reveal=True))]),
 ('Try it', [
  ('B', 'Point to the line the treble clef curls round, and play that G. Then the line between the bass clef’s dots, and play that F. Middle C sits between them.', c(28, 'yk')), ('pause', 4, c(28, 'yk')), ('piano', 'G4 F3 C4', c(28, 'yk')),
  ('B', 'And a tune you know. Twinkle, Twinkle leaps up to G, the treble clef’s very own line.', c(28, 'yk')), ('piano', 'C4 C4 G4 G4 A4 A4 G4*2', c(28, 'yk', seq=idx(0, 7))),
  ('B', 'A clef is a pair of glasses. Look: the very same note on the bottom line. Through treble glasses it is E; through bass glasses it is G. Until next time, Clara.', c(28, 'think', anim='glasses')), ('P', 'Goodbye!', c(28, 'think'))])]),
'P3': ('The staff and the keyboard', [
 ('The secret', [
  ('B', 'Clara, here is the secret of this chapter. Every line and every space of the staff is one white key, in order.', c(29, 'secret')),
  ('P', 'So climbing the staff is climbing the keyboard?', c(29, 'vx')),
  ('B', 'Exactly. Here are two octaves, from Bass C up to Treble C, with Middle C where the two staves meet.', c(29, 'vx')),
  ('piano', 'C3 D3 E3 F3 G3 A3 B3 C4 D4 E4 F4 G4 A4 B4 C5', c(29, 'vx', seq=idx(0, 15))),
  ('B', 'One step on the staff, from a line to the space next to it, is the very next white key. Up the staff is to the right; down is to the left.', c(29, 'p2')),
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
  ('B', 'Mirror images. Fold the grand staff at Middle C, like folding a painting in half, and treble G lands exactly on bass F.', c(30, 'ex2', reveal=True, mirror='GF')),
  ('Q', 'My G and the King’s F: the same distance up and down.', c(30, 'ex2', reveal=True, mirror='GF')), ('K', 'Two guards at the castle gate, with Middle C between us.', c(30, 'ex2', reveal=True, mirror='GF'))]),
 ('Example: from the key to the page', [
  ('B', 'I play the third white key up from Middle C.', c(31, 'ex3', show=['Middle C'])), ('piano', 'C4 D4 E4', c(31, 'ex3', seq=['Middle C', '', '?'], show=['Middle C'])),
  ('P', 'C one, D two, E three. It is E.', c(31, 'ex3', lab=['?'], show=['Middle C'])),
  ('B', 'And on the staff? Climb the same way.', c(31, 'ex3', show=['Middle C'])), ('P', 'Middle C on its little line, D in the space just under the staff, E on the bottom line.', c(31, 'ex3', reveal=True)), ('B', 'Precisely.', c(31, 'ex3', reveal=True))]),
 ('Try it', [
  ('B', 'Play Middle C and walk up the white keys, saying each name, and picture each one climbing the staff: line, space, line, space.', c(30, 'try10')), ('piano', 'C4 D4 E4 F4 G4 A4 B4 C5', c(30, 'try10', seq=idx(0, 8))),
  ('B', 'Then Frère Jacques in both hands. The right hand plays C D E C; the left hand plays the same letters one octave lower, in the bass clef.', c(31, 'yk')), ('piano', 'C4 D4 E4 C4 | C3 D3 E3 C3', c(31, 'yk', seq=idx(0, 4) + idx(0, 4))),
  ('B', 'The staff is a ladder laid beside the keyboard: every rung is the next white key.', c(31, 'think'))])]),
'P4': ('Reading the notes', [
 ('The secret', [
  ('P', 'Do I have to learn every line and space by heart?', c(32, 'lead')),
  ('B', 'Not at once. Start from a note you always know: Middle C in the middle, treble G and bass F either side.', c(32, 'hero', lab=['#19', '#2', '#15'])),
  ('piano', 'C4 G4 F3', c(32, 'hero', seq=['#19', '#2', '#15'])),
  ('B', 'Every line and space is the next letter. Listen to the whole staircase, from bass G to treble F.', c(32, 'hero')),
  ('piano', 'G2/2 A2/2 B2/2 C3/2 D3/2 E3/2 F3/2 G3/2 A3/2 B3/2 C4/2 D4/2 E4/2 F4/2 G4/2 A4/2 B4/2 C5/2 D5/2 E5/2 F5/2', c(32, 'hero', seq=idx(9, 21) + idx(0, 9))),
  ('P', 'And how do I move?', c(32, 'xlate')),
  ('B', 'Step or skip. A step goes to the very next line or space: one letter on. A skip goes line to line, or space to space: two letters on.', c(32, 'xlate', anim='stepskip')), ('piano', 'G4 A4 | G4 B4', c(32, 'xlate'))]),
 ('Words to remember', [
  ('B', 'First, two kinds of note. A line note has a line running through its middle. A space note sits between two lines, touching both.', c(33, 'xlate2')),
  ('B', 'Lines and spaces are counted from the bottom. Treble lines first. Line one, E. Line two, G. Line three, B. Line four, D. Line five, F.', c(33, 'xlate3', lens='tl')),
  ('Q', 'In my staff we say: Every Good Boy Deserves Fun.', c(33, 'xlate3', lens='tl')),
  ('B', 'The four treble spaces, from the bottom: F, A, C, E.', c(33, 'xlate3', lens='ts')),
  ('Q', 'And my spaces spell face.', c(33, 'xlate3', lens='ts')),
  ('B', 'Now the bass staff. Bass lines, from the bottom: G, B, D, F, A.', c(33, 'xlate3', lens='bl')),
  ('K', 'In my kingdom: Great Big Dragons Fly Away!', c(33, 'xlate3', lens='bl')),
  ('B', 'Last, the bass spaces: A, C, E, G.', c(33, 'xlate3', lens='bs')),
  ('K', 'My spaces: All Cows Eat Grass.', c(33, 'xlate3', lens='bs')), ('P', 'I will never forget the dragons.', c(33, 'xlate3'))]),
 ('Example: read from the clef note', [
  ('B', 'A treble note you are not sure of, on line four. Start from the clef note.', c(34, 'ex1')),
  ('P', 'G is line two. Skip up to line three: B. Skip again to line four.', c(34, 'ex1')), ('pause', 3, c(34, 'ex1')),
  ('P', 'D!', c(34, 'ex1', reveal=True)), ('piano', 'G4 B4 D5', c(34, 'ex1', reveal=True)), ('B', 'G, B, D: two skips up from the clef’s G.', c(34, 'ex1', reveal=True))]),
 ('Example: a bass note', [
  ('B', 'Now the bass staff, line three.', c(34, 'ex1', show=[])),
  ('P', 'The dots hug line four: F. Step down to the space: E. Step down again to line three.', c(34, 'ex1', show=['F', 'E'])), ('piano', 'F3 E3', c(34, 'ex1', seq=['F', 'E'], show=['F', 'E'])), ('pause', 3, c(34, 'ex1', show=['F', 'E'], lab=['?'])),
  ('P', 'D.', c(34, 'ex1', lab=['?'], reveal=True)), ('piano', 'F3 E3 D3', c(34, 'ex1', seq=['F', 'E', '?'], reveal=True)), ('B', 'Correct. F, E, D.', c(34, 'ex1', reveal=True))]),
 ('Example: one line, two notes', [
  ('B', 'Here is a puzzle. Two red notes, both on the bottom line: one in the treble staff, one in the bass. Same line. Same note?', c(34, 'ex2')),
  ('P', 'I think so?', c(34, 'ex2')), ('B', 'Read each from its clef. Pause and try.', c(34, 'ex2')), ('pause', 4, c(34, 'ex2')),
  ('P', 'Treble: G is line two. Step down, F in the space, then the bottom line is E.', c(34, 'ex2', lab=['#0'])), ('piano', 'E4', c(34, 'ex2', seq=['#0'])),
  ('B', 'And the bass? F is line four. Step down line by line.', c(34, 'ex2')), ('P', 'F, D, B, G. The bottom line is G!', c(34, 'ex2', lab=['#1'], reveal=True)), ('piano', 'G2', c(34, 'ex2', seq=['#1'], reveal=True)),
  ('B', 'Same line, different note. Always read the clef first.', c(34, 'ex2', reveal=True, anim='glasses'))]),
 ('Example: read it downwards', [
  ('B', 'Now read downwards, Clara. Start on G, the clef note, and step down to Middle C. Each step down is the letter before. Pause and say them.', c(34, 'ex3', show=['G', 'steps down', 'skips down (the lines)'])),
  ('pause', 4, c(34, 'ex3', show=['G', 'steps down', 'skips down (the lines)'])),
  ('P', 'G, F, E, D, C!', c(34, 'ex3', reveal=True)), ('piano', 'G4 F4 E4 D4 C4', c(34, 'ex3', seq=['G', '#1', '#2', '#3', '#4'], reveal=True)),
  ('B', 'The alphabet backwards. Now skip down the lines from F, the top line: two letters back each time.', c(34, 'ex3', reveal=True)),
  ('pause', 3, c(34, 'ex3', reveal=True)),
  ('P', 'F, D, B, G, E!', c(34, 'ex3', reveal=True)), ('piano', 'F5 D5 B4 G4 E4', c(34, 'ex3', seq=['F', '#7', '#8', '#9', '#10'], reveal=True)),
  ('B', 'Every Good Boy Deserves Fun, backwards. Reading down this fast is half of good sight-reading.', c(34, 'ex3', reveal=True))]),
 ('Example: Treble C and Bass C', [
  ('B', 'Find Treble C on the staff. These notes sit in the spaces.', c(35, 'ex4')),
  ('P', 'The treble spaces spell face. F, A, and space three is C!', c(35, 'ex4', lab=['?'], reveal=True)), ('piano', 'F4 A4 C5', c(35, 'ex4', reveal=True)),
  ('B', 'Treble C, one octave above Middle C. And in the bass spaces?', c(35, 'ex4')),
  ('P', 'All Cows. Space two is C: Bass C!', c(35, 'ex4', lab=['?'], reveal=True)), ('piano', 'A2 C3', c(35, 'ex4', reveal=True)),
  ('B', 'One octave below Middle C.', c(35, 'ex4', reveal=True))]),
 ('Try it', [
  ('B', 'To read a new note, make three moves. Look at the clef. Find the nearest note you know, or use the sentence. Then step or skip to it, say it, and play it.', c(33, 'xlate')),
  ('B', 'Mary Had a Little Lamb. E, D, C: line, space, and Middle C’s own little line, one step down each time.', c(35, 'yk')), ('piano', 'E4 D4 C4 D4 E4 E4 E4*2', c(35, 'yk', seq=idx(0, 7))),
  ('B', 'Your mission: in a piece you play, find the clef notes first, then step or skip from them. The clef notes are lamp posts on a dark road. Until next time, Clara.', c(35, 'think')), ('P', 'Goodbye!', c(35, 'think'))])]),
'P5': ('Ledger lines', [
 ('The secret', [
  ('B', 'Clara, some notes are too high or too low for the staff. They sit on short extra lines called ledger lines.', {'p': 36, 'r': 'lead'}),
  ('P', 'Little lines just for one note?', {'p': 36, 'r': 'lead'}),
  ('B', 'Exactly, spaced just like the staff lines. And the most famous ledger note of all is Middle C. In the treble staff it hangs on the first ledger line below. In the bass staff it sits on the first ledger line above.', {'p': 36, 'r': 'hero'}),
  ('P', 'Two different places on the page, but the same key?', {'p': 36, 'r': 'hero', 'lab': ['Middle C']}),
  ('piano', 'C4', {'p': 36, 'r': 'hero', 'seq': ['Middle C']}),
  ('Q', 'In my staff, Middle C hangs on the first ledger line below.', {'p': 36, 'r': 'hero'}),
  ('K', 'In mine it sits on the first ledger line above. One key, and we both may write it.', {'p': 36, 'r': 'hero'}),
  ('B', 'One key, two ways to write it. The right hand reads it in the treble, the left hand in the bass.', {'p': 36, 'r': 'hero'})]),
 ('Below and above the staff', [
  ('B', 'Read ledger notes by stepping out from the staff, one letter at a time. Treble, below the staff: C on the first ledger line, B under it, A on the second ledger line.', {'p': 36, 'r': 'xlate', 'lens': 'tb'}),
  ('piano', 'C4 B3 A3', {'p': 36, 'r': 'xlate', 'lens': 'tb'}),
  ('B', 'Then above the treble staff: A on the first ledger line, B over it, C on the second.', {'p': 36, 'r': 'xlate', 'lens': 'ta'}),
  ('piano', 'A5 B5 C6', {'p': 36, 'r': 'xlate', 'lens': 'ta'}),
  ('B', 'In the bass, below the staff: E on the first ledger line, D under it, C on the second.', {'p': 37, 'r': 'xlate', 'lens': 'bb'}),
  ('piano', 'E2 D2 C2', {'p': 37, 'r': 'xlate', 'lens': 'bb'}),
  ('B', 'And above the bass staff: Middle C on the first ledger line, then D, then E on the second.', {'p': 37, 'r': 'xlate', 'lens': 'ba'}),
  ('piano', 'C4 D4 E4', {'p': 37, 'r': 'xlate', 'lens': 'ba'}),
  ('B', 'The rule: count ledger lines from the staff outwards. The first ledger line is the one nearest the staff. Never skip one.', {'p': 36, 'r': 'xlate'})]),
 ('Example: a high note', [
  ('B', 'A high note on ledger lines. Start from the top line of the treble staff: F.', {'p': 37, 'r': 'ex1', 'show': ['F'], 'lab': ['F']}),
  ('P', 'Then G on top of the staff, A on the first ledger line, B above it.', {'p': 37, 'r': 'ex1', 'show': ['F', 'G', 'A', 'B']}),
  ('piano', 'F5 G5 A5 B5', {'p': 37, 'r': 'ex1', 'seq': ['F', 'G', 'A', 'B'], 'show': ['F', 'G', 'A', 'B']}),
  ('B', 'And the red note, on the second ledger line? Pause and try.', {'p': 37, 'r': 'ex1', 'show': ['F', 'G', 'A', 'B'], 'lab': ['?']}),
  ('pause', 3, {'p': 37, 'r': 'ex1', 'show': ['F', 'G', 'A', 'B'], 'lab': ['?']}),
  ('P', 'C! High C.', {'p': 37, 'r': 'ex1', 'lab': ['?'], 'reveal': True}),
  ('piano', 'C6', {'p': 37, 'r': 'ex1', 'seq': ['?'], 'reveal': True})]),
 ('Example: a low note', [
  ('B', 'Now a low note under the bass staff. Start from the bottom line: G.', {'p': 37, 'r': 'ex2', 'show': ['G'], 'lab': ['G']}),
  ('P', 'Step down: F in the space below, E on the first ledger line, D under it.', {'p': 37, 'r': 'ex2', 'show': ['G', 'F', 'E', 'D']}),
  ('piano', 'G2 F2 E2 D2', {'p': 37, 'r': 'ex2', 'seq': ['G', 'F', 'E', 'D'], 'show': ['G', 'F', 'E', 'D']}),
  ('B', 'And the red note, on the second ledger line? Pause and try.', {'p': 37, 'r': 'ex2', 'show': ['G', 'F', 'E', 'D'], 'lab': ['?']}),
  ('pause', 3, {'p': 37, 'r': 'ex2', 'show': ['G', 'F', 'E', 'D'], 'lab': ['?']}),
  ('P', 'C! Low C, two octaves below Middle C.', {'p': 37, 'r': 'ex2', 'lab': ['?'], 'reveal': True}),
  ('piano', 'C2', {'p': 37, 'r': 'ex2', 'seq': ['?'], 'reveal': True}),
  ('B', 'And look: Low C is the mirror of High C. Fold the grand staff at Middle C, and two ledger lines above the treble land on two ledger lines below the bass.', {'p': 37, 'r': 'ex2', 'reveal': True, 'mirror': 'CC'})]),
 ('The four first ledger lines', [
  ('B', 'And watch out for the other first ledger lines. Above the treble staff the first ledger line is A. Below the bass staff it is E. Only Middle C belongs to both staves.', {'p': 38, 'r': 'xlate'})]),
 ('Try it', [
  ('B', 'When notes go even higher, music often writes them lower, with an ottava sign and a dotted line above them: play those notes one octave higher, until the dotted line stops.', {'p': 38, 'r': 'xlate2'}),
  ('B', 'Ledger lines are the staff’s ladder carried on past its ends: the same rungs, just shorter. Until next time, Clara.', {'p': 38, 'r': 'think'}),
  ('P', 'Goodbye!', {'p': 38, 'r': 'think'})])]),
'P6': ('Sharps, flats and naturals', [
 ('The secret', [
  ('P', 'What are those little signs in front of some notes?', c(39, 'lead')),
  ('B', 'Signs that move a note to the very next key. A sharp: one key to the right, a semitone higher. A flat: one key to the left, a semitone lower.', c(39, 'secret', anim='sharpflat')),
  ('B', 'Usually that next key is black, and that is how the black keys get their names. D sharp is just right of D. D flat is just left of it.', c(39, 'hero')), ('piano', 'D4 D#4 | D4 Db4', c(39, 'hero', seq=['D', 'D♯', 'D', 'D♭'])),
  ('B', 'And a natural cancels a sharp or flat: back to the white key.', c(39, 'ht')),
  ('B', 'And where there is no black key between, a sharp or flat lands on a white key: E sharp is F, B sharp is C, F flat is E, and C flat is B.', c(39, 'xlate')),
  ('B', 'One rule to remember. A sign belongs to one note: it changes only that line or space, in that octave, and only until the bar line. The same letter in another octave stays as it is.', c(40, 'xlate'))]),
 ('Example: find F sharp', [
  ('B', 'Find F sharp, Clara.', c(40, 'ex1', show=[])), ('P', 'F is just left of the three black keys.', c(40, 'ex1', show=['F'], lab=['F'])),
  ('B', 'Sharp means right: the very next key. Black or white? Pause and put your finger on it.', c(40, 'ex1', show=['F'], lab=['?'])), ('pause', 3, c(40, 'ex1', show=['F'], lab=['?'])),
  ('P', 'Black! The first black key of the three.', c(40, 'ex1', lab=['?'], reveal=True)), ('piano', 'F4 F#4', c(40, 'ex1', seq=['F', '?'], reveal=True)), ('B', 'Correct: F sharp.', c(40, 'ex1', reveal=True))]),
 ('Example: find B flat', [
  ('B', 'Now B flat.', c(40, 'ex1', show=[])), ('P', 'B is just right of the three black keys. Flat means left.', c(40, 'ex1', show=['B'], lab=['B'])), ('pause', 3, c(40, 'ex1', show=['B'], lab=['?'])),
  ('P', 'The top black key of the group!', c(40, 'ex1', lab=['?'], reveal=True)), ('piano', 'B4 Bb4', c(40, 'ex1', seq=['B', '?'], reveal=True)), ('B', 'Splendid.', c(40, 'ex1', reveal=True))]),
 ('Example: how long does a sign last?', [
  ('B', 'A sharp on the first note of a bar: F sharp. Later in the same bar, the same note with no sign. Sharp or not?', c(40, 'ex2', show=['F♯', 'G'], lab=['F♯'])), ('pause', 3, c(40, 'ex2', show=['F♯', 'G'])),
  ('P', 'Still sharp?', c(40, 'ex2', show=['F♯', 'G'])), ('B', 'Yes, until the bar line. And after the bar line?', c(40, 'ex2', show=['F♯', 'G'])),
  ('P', 'Plain F again!', c(40, 'ex2', reveal=True)), ('B', 'A sign lasts to the end of its bar. Now a natural: B, then B flat, and it stays flat for the rest of the bar. Then a natural sign. What does it do?', c(41, 'ex3', show=['B', 'B♭'])), ('pause', 3, c(41, 'ex3', show=['B', 'B♭'])),
  ('P', 'It cancels the flat: back to the white key B.', c(41, 'ex3', lab=['?'], reveal=True)), ('piano', 'B4 Bb4 Bb4 B4', c(41, 'ex3', seq=idx(0, 4), reveal=True))]),
 ('Example: one key, two names', [
  ('B', 'One more. F sharp, then G flat. Find both on the keyboard.', c(41, 'ex4', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'])),
  ('P', 'They are the same black key!', c(41, 'ex4', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], lab=['F♯', 'G♭'])), ('piano', 'F#4 Gb4', c(41, 'ex4', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], seq=['F♯', 'G♭'])),
  ('B', 'Same sound, two names: we call them enharmonic. And E sharp, one key right of E?', c(41, 'ex4', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], lab=['E♯'])), ('pause', 3, c(41, 'ex4', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'])),
  ('P', 'There is no black key there. So E sharp is the white key F!', c(41, 'ex4', reveal=True)), ('piano', 'E4 F4', c(41, 'ex4', reveal=True))]),
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
  ('B', 'Sharps and flats never change the number. From C, the numbers go: unison, second, third, fourth, fifth, sixth, seventh, octave.', c(43, 'xlate', anim='ladder')), ('piano', 'C4 D4 E4 F4 G4 A4 B4 C5', c(43, 'xlate', seq=['unison', '2nd', '3rd', '4th', '5th', '6th', '7th', '8ve'])),
  ('P', 'So C to G is C, D, E, F, G: a fifth.', c(43, 'xlate'))]),
 ('Example: count an interval', [
  ('B', 'F up to A. How many notes? Pause and count.', c(43, 'ex2', show=['F', 'A', 'C', 'G'])), ('pause', 3, c(43, 'ex2', show=['F', 'A', 'C', 'G'])),
  ('P', 'F, G, A. Three: a third.', c(43, 'ex2', show=['F', '(G)', 'A', 'C', 'G'])), ('piano', 'F4 G4 A4', c(43, 'ex2', seq=['F', '(G)', 'A'], show=['F', '(G)', 'A', 'C', 'G'])),
  ('B', 'And going down? C down to G.', c(43, 'ex2', show=['F', '(G)', 'A', 'C', 'G'])), ('P', 'C, B, A, G. Four: a fourth.', c(43, 'ex2', reveal=True)), ('piano', 'C5 B4 A4 G4', c(43, 'ex2', seq=['C', '(B)', '(A)', 'G'], reveal=True)),
  ('B', 'The same way, up or down: the first note is one.', c(43, 'ex2', reveal=True))]),
 ('Example: name an interval', [
  ('B', 'E, and the C above it. Count the notes from E.', c(44, 'ex3', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])), ('pause', 3, c(44, 'ex3', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('P', 'E one, F two, G three, A four, B five, C six. A sixth!', c(44, 'ex3', reveal=True)), ('piano', 'E4 F4 G4 A4 B4 C5', c(44, 'ex3', seq=idx(2, 8), reveal=True)),
  ('B', 'Melodic or harmonic, the number is the same. C then E, one after the other, is a melodic third. C and E together, a harmonic third.', c(44, 'ex4', lab=['melodic', 'harmonic'], reveal=True)), ('piano', 'C4 E4 | [C4 E4]', c(44, 'ex4', seq=['melodic', 'melodic', 'harmonic'], reveal=True))]),
 ('Try it', [
  ('B', 'Try it: thumb on C, little finger on G. Your hand covers five white keys.', c(44, 'try10')), ('piano', 'C4 G4', c(44, 'try10')), ('P', 'C up to G: five notes. A fifth!', c(44, 'try10')),
  ('B', 'Monday to Wednesday is three days, not two: you count the day you start on. Intervals count the same way. Your mission: find a semitone, a tone, a third and a fifth from any C.', c(44, 'watch'))])]),
'P8': ('Major, minor and perfect', [
 ('The secret', [
  ('B', 'Clara, two thirds can sound different. Listen.', c(45, 'lead')), ('piano', '[C4 E4] | [C4 Eb4]', c(45, 'lead')), ('P', 'The first is bright. The second is darker.', c(45, 'lead')),
  ('B', 'Both are thirds: three notes each. To tell them apart, count the keys in between, black and white, but not the two you play.', c(45, 'secret')),
  ('B', 'C to E has three keys between: C sharp, D, D sharp. A major third.', c(45, 'hero')), ('piano', 'C#4 D4 D#4 | [C4 E4]', c(45, 'hero', seq=idx(7, 10) + ['#2'])),
  ('B', 'C to E flat has only two between, one fewer. A minor third.', c(45, 'hero', anim='majmin')), ('piano', 'C#4 D4 | [C4 Eb4]', c(45, 'hero', seq=idx(18, 20) + ['#11'])),
  ('B', 'So the rule: count the notes for the number, and count the keys in between for the size.', c(45, 'rule')),
  ('B', 'Thirds and sixths come in two sizes, major and minor. Fourths, fifths and octaves have one main size, called perfect. They are never major or minor.', c(45, 'two'))]),
 ('A perfect fourth', [
  ('B', 'C up to F: C, D, E, F. Four notes, a fourth. Count the keys between.', c(46, 'xlate')), ('piano', 'C#4 D4 D#4 E4 | [C4 F4]', c(46, 'xlate', seq=['1', '2', '3', '4', 'start'])),
  ('P', 'Four between. A perfect fourth.', c(46, 'xlate'))]),
 ('Example: major or minor third?', [
  ('B', 'A up to C. A, B, C: three letters, so a third. Now count the keys between. Pause and count.', c(46, 'ex1', show=W)), ('pause', 3, c(46, 'ex1', show=W)),
  ('P', 'B flat, B. Two between.', c(46, 'ex1', show=W)), ('piano', 'Bb4 B4', c(46, 'ex1', seq=['1', '2'], show=W)), ('B', 'A major third has three between. So?', c(46, 'ex1', show=W)),
  ('P', 'A minor third! Dark, like C to E flat.', c(46, 'ex1', reveal=True)), ('piano', '[A4 C5]', c(46, 'ex1', reveal=True))]),
 ('Example: F up to A', [
  ('B', 'F up to A. F, G, A: a third. Now the keys between: they are numbered.', c(46, 'ex2', show=W)),
  ('P', 'F sharp, G, G sharp: three. A major third!', c(46, 'ex2', reveal=True)), ('piano', 'F#4 G4 G#4 | [F4 A4]', c(46, 'ex2', seq=['1', '2', '3'], reveal=True)),
  ('B', 'The same size as C to E.', c(46, 'ex2', reveal=True))]),
 ('Example: D up to A', [
  ('B', 'D up to A. The number first.', c(47, 'ex3', show=W)), ('P', 'D, E, F, G, A: five notes, a fifth.', c(47, 'ex3', show=W)),
  ('B', 'And six keys between. A fifth with six between is its main size. What is that called?', c(47, 'ex3', show=W)), ('pause', 3, c(47, 'ex3', show=W)),
  ('P', 'A perfect fifth!', c(47, 'ex3', reveal=True)), ('piano', 'D#4 E4 F4 F#4 G4 G#4 | [D4 A4]', c(47, 'ex3', seq=['1', '2', '3', '4', '5', '6', 'start'], reveal=True))]),
 ('Try it', [
  ('B', 'Beethoven’s Fifth: da-da-da-dum. G down to E flat is a third, with three keys between: a major third. Count them on your keyboard.', c(47, 'yk')), ('piano', 'G4/2 G4/2 G4/2 Eb4*3', c(47, 'yk', seq=idx(0, 4))),
  ('B', 'A major and a minor third are a smile and a frown: the same face, one small change at the corners.', c(47, 'think')),
  ('Q', 'And never call a fourth or a fifth major, Clara. They are perfect.', c(47, 'watch')),
  ('B', 'Until next time, Clara.', c(47, 'watch')), ('P', 'Goodbye!', c(47, 'watch'))])]),
}

CH = {
'P1': ('The keyboard', [
 ('The secret', [
  ('B', 'Clara, our first room: the keyboard.', {'p': 22, 'r': 'h:The keyboard'}),
  ('P', 'There are so many keys. Do I have to count them all?', {'p': 22, 'r': 'hero'}),
  ('B', 'Never. Let us start with one fact. Left is low.', {'p': 22, 'r': 'hero'}),
  ('piano', 'C2', {'p': 22, 'r': 'hero'}),
  ('B', 'Right is high.', {'p': 22, 'r': 'hero'}),
  ('piano', 'C6', {'p': 22, 'r': 'hero'}),
  ('P', 'Low on the left, high on the right. Easy.', {'p': 22, 'r': 'hero'}),
  ('B', 'Try it at once. Two red keys: which one sounds higher? Pause and think.', {'p': 22, 'r': 'ex1'}),
  ('pause', 3, {'p': 22, 'r': 'ex1'}),
  ('P', 'The second one. It is further to the right.', {'p': 22, 'r': 'ex1', 'reveal': True}),
  ('piano', 'G4 E5', {'p': 22, 'r': 'ex1', 'reveal': True}),
  ('B', 'Right is always higher, left always lower.', {'p': 22, 'r': 'ex1', 'reveal': True}),
  ('B', 'Now look at the black keys. They come in little groups: two, then three. Two, three, all the way along.', {'p': 22, 'r': 'hero', 'anim': 'groups'}),
  ('P', 'Like bumps on a road.', {'p': 22, 'r': 'hero', 'anim': 'groups'}),
  ('B', 'Exactly. Here is the secret. Every group has a first white key, just to its left. Next to the two black keys, the first key is C. Next to the three, it is F.', {'p': 22, 'r': 'secret'}),
  ('P', 'Two black keys: start on C. Three black keys: start on F.', {'p': 22, 'r': 'secret'}),
  ('B', 'Then walk on. C, D, E around the two.', {'p': 22, 'r': 'hero'}),
  ('piano', 'C4 D4 E4', {'p': 22, 'r': 'hero', 'seq': ['C', 'D', 'E']}),
  ('B', 'F, G, A, B around the three.', {'p': 22, 'r': 'hero'}),
  ('piano', 'F4 G4 A4 B4', {'p': 22, 'r': 'hero', 'seq': ['F', 'G', 'A', 'B']}),
  ('B', 'And the pattern repeats all the way along: two, three, two, three. Every two starts on C, every three starts on F.', {'p': 23, 'r': 'xlate'}),
  ('piano', 'C3 F3 C4 F4 C5 F5', {'p': 23, 'r': 'xlate', 'seq': ['#0', '#1', '#2', '#3', '#4', '#5']}),
  ('P', 'So wherever I am, I find a group and I know where I am.', {'p': 23, 'r': 'xlate'})]),
 ('Round and round', [
  ('P', 'But what comes after G? Is there an H?', {'p': 23, 'r': 'xlate2'}),
  ('B', 'No H at all. The white keys use only seven letters, A to G. After G, the next key is A again, like the days of the week: Sunday comes round again after Saturday.', {'p': 23, 'r': 'xlate2'}),
  ('piano', 'A3 B3 C4 D4 E4 F4 G4 A4 B4 C5 D5 E5 F5 G5 A5', {'p': 23, 'r': 'xlate2', 'seq': ['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12', '#13', '#14']}),
  ('P', 'A B C D E F G, then A again. Seven letters, round and round.', {'p': 23, 'r': 'xlate2'}),
  ('B', 'And notice two pairs that touch: between E and F, and between B and C, there is no black key at all.', {'p': 23, 'r': 'xlate3'})]),
 ('Backwards', [
  ('B', 'Now walk the other way, Clara: left, down the keyboard. The letters run backwards.', {'p': 24, 'r': 'xlate'}),
  ('piano', 'A4 G4 F4 E4 D4 C4 B3 A3', {'p': 24, 'r': 'xlate', 'seq': ['1', '2', '3', '4', '5', '6', '7', '8']}),
  ('P', 'A, G, F, E, D, C, B, A. That is harder!', {'p': 24, 'r': 'xlate'}),
  ('B', 'It is, at first. But music goes down as often as it goes up, so say the letters backwards until it is as quick as forwards. It makes reading music, and sight-reading, much easier.', {'p': 24, 'r': 'xlate'})]),
 ('Example: walk down from E', [
  ('B', 'Start on E and walk left, one white key at a time. Name each key. Pause and try.', {'p': 24, 'r': 'ex2'}),
  ('pause', 4, {'p': 24, 'r': 'ex2'}),
  ('P', 'E, D, C, B, A!', {'p': 24, 'r': 'ex2', 'reveal': True}),
  ('piano', 'E4 D4 C4 B3 A3', {'p': 24, 'r': 'ex2', 'reveal': True}),
  ('B', 'Now fill the gaps out loud: G, something, E, something, C. Pause and say it.', {'p': 24, 'r': 'ex2', 'reveal': True}),
  ('pause', 3, {'p': 24, 'r': 'ex2', 'reveal': True}),
  ('P', 'G, F, E, D, C.', {'p': 24, 'r': 'ex2', 'reveal': True})]),
 ('The two ends', [
  ('B', 'Now the two ends of the piano. The very first key, bottom left, is an A. Look at the black keys there: only one, on its own.', {'p': 24, 'r': 'xlate2'}),
  ('P', 'Only one? But the groups are two or three.', {'p': 24, 'r': 'xlate2'}),
  ('B', 'Well spotted. It is a group of three that has been cut off. Only its end is left: A and B. Then comes the first full group of two, and its first key is Lowest C.', {'p': 24, 'r': 'xlate2'}),
  ('piano', 'A0 B0 C1', {'p': 24, 'r': 'xlate2', 'seq': ['#0', '#1', 'Lowest C']}),
  ('B', 'At the top, the very last key has no black key after it at all. Look left: the last group is three black keys, F, G, A, B.', {'p': 24, 'r': 'xlate2'}),
  ('P', 'And after B comes C!', {'p': 24, 'r': 'xlate2'}),
  ('B', 'Exactly. The first key of a new group of two that was never built. So the last key is a C: Highest C.', {'p': 24, 'r': 'xlate2'}),
  ('piano', 'F7 G7 A7 B7 C8', {'p': 24, 'r': 'xlate2', 'seq': ['#5', '#6', '#7', '#8', 'Highest C']})]),
 ('The eight Cs', [
  ('B', 'Count the Cs from the bottom and there are eight. Some have names. The C nearest the middle is Middle C.', {'p': 25, 'r': 'xlate'}),
  ('piano', 'C4', {'p': 25, 'r': 'xlate', 'seq': ['Middle C']}),
  ('B', 'One C lower is Bass C. One C higher is Treble C. Further out: Low C and High C.', {'p': 25, 'r': 'xlate'}),
  ('piano', 'C2 C3 C4 C5 C6', {'p': 25, 'r': 'xlate', 'seq': ['Low C', 'Bass C', 'Middle C', 'Treble C', 'High C']}),
  ('P', 'And the ones at the very ends?', {'p': 25, 'r': 'xlate'}),
  ('B', 'At the bottom, Lowest C. At the top, Very High C, and then Highest C, the very last key.', {'p': 25, 'r': 'xlate'}),
  ('piano', 'C1 C7 C8', {'p': 25, 'r': 'xlate', 'seq': ['Lowest C', 'Very High C', 'Highest C']}),
  ('P', 'Eight Cs! But the five in the middle are the ones I will use most.', {'p': 25, 'r': 'xlate'}),
  ('B', 'Exactly. Theory books and apps give them numbers instead: C1 to C8, with Middle C as C4. And from one C to the next is an octave: eight notes, both Cs counted.', {'p': 25, 'r': 'xlate'})]),
 ('Example: Bass C and Treble C', [
  ('B', 'Now find Bass C and Treble C, starting from Middle C. Pause and try.', {'p': 25, 'r': 'ex3'}),
  ('pause', 4, {'p': 25, 'r': 'ex3'}),
  ('P', 'Walk left to the next pair of black keys: the C just left of it is Bass C. Walk right the same way: Treble C.', {'p': 25, 'r': 'ex3', 'reveal': True}),
  ('piano', 'C3 C4 C5', {'p': 25, 'r': 'ex3', 'reveal': True}),
  ('B', 'Each is one octave from Middle C, eight notes away.', {'p': 25, 'r': 'ex3', 'reveal': True})]),
 ('Example: three keys', [
  ('B', 'Three numbered keys. Name each one, and do not count from the bottom.', {'p': 26, 'r': 'ex4'}),
  ('P', 'Number one is with three black keys, so its family is F G A B. Start on F and walk on: F, G, A, B. It is the last one.', {'p': 26, 'r': 'ex4'}),
  ('B', 'And the other two? Pause and find them.', {'p': 26, 'r': 'ex4'}),
  ('pause', 4, {'p': 26, 'r': 'ex4'}),
  ('P', 'One is B. Two sits just right of the two black keys: the last of C D E, so E. And three is one key after F: G!', {'p': 26, 'r': 'ex4', 'reveal': True}),
  ('piano', 'F4 G4 A4 B4', {'p': 26, 'r': 'ex4', 'reveal': True}),
  ('B', 'Find the group, find its first key, walk on. No counting from far away.', {'p': 26, 'r': 'ex4', 'reveal': True})]),
 ('Try it', [
  ('B', 'Before you go, a tune with no white keys at all. Right hand, fingers two, three and four on a group of three black keys.', {'p': 26, 'r': 'yk'}),
  ('P', 'Ready.', {'p': 26, 'r': 'yk'}),
  ('B', 'Four, three, two. Four, three, two. Then twice as fast: two two two two, three three three three. And four, three, two.', {'p': 26, 'r': 'yk'}),
  ('piano', 'A#4 G#4 F#4*2 | A#4 G#4 F#4*2 | F#4/2 F#4/2 F#4/2 F#4/2 G#4/2 G#4/2 G#4/2 G#4/2 | A#4 G#4 F#4*2', {'p': 26, 'r': 'yk'}),
  ('P', 'Hot Cross Buns!', {'p': 26, 'r': 'yk'}),
  ('B', 'Your mission: close your eyes and slide your hand along the keys. Two bumps, the key to their left is C. Three bumps, it is F. Until next time.', {'p': 26, 'r': 'think'})])]),
**NEW,
}

NEW['T1'] = ('Pulse, tempo and the bar', [
 ('The secret', [
  ('B', 'Clara, put your hand on your heart.', {'p': 50, 'r': 'lead'}),
  ('P', 'It is beating. Steady, steady.', {'p': 50, 'r': 'lead'}),
  ('B', 'That steady beat is a pulse, and almost every piece of music has one. Its speed is the tempo. Beats travel in groups called bars, and beat one is the strongest.', {'p': 50, 'r': 'hero'}),
  ('count', {'beats': 'X x x x X x x x X x x x', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, {'p': 50, 'r': 'hero', 'seq': ['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11']}),
  ('B', 'Here is the secret. The beat never stops, not even in a rest. Feel it before you play.', {'p': 50, 'r': 'secret'}),
  ('P', 'So in a rest I still count?', {'p': 50, 'r': 'hero'}),
  ('B', 'Always. Listen: in the second bar the notes stop, and the beat goes on.', {'p': 50, 'r': 'hero'}),
  ('count', {'beats': 'X x x x X x x x X x x x', 'notes': 'C5 C4 C4 C4 C5 C4 R R C5 C4 C4 C4', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, {'p': 50, 'r': 'hero', 'seq': ['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11']})]),
 ('Tempo', [
  ('B', 'Tempo is measured in beats per minute. A metronome mark at the top of the music shows it. Crotchet equals sixty means sixty beats a minute: one every second.', {'p': 50, 'r': 'xlate'}),
  ('piano', 'X@60 x@60 x@60 x@60', {'p': 50, 'r': 'xlate'}),
  ('B', 'Crotchet equals one hundred and twenty is twice as fast.', {'p': 50, 'r': 'xlate'}),
  ('piano', 'X@120 x@120 x@120 x@120 X@120 x@120 x@120 x@120', {'p': 50, 'r': 'xlate'}),
  ('P', 'Twice as many ticks in the same time.', {'p': 50, 'r': 'xlate'})]),
 ('Example: feel the beat first', [
  ('B', 'This one says crotchet equals ninety-six: ninety-six beats a minute. Do not start yet. Listen to one full bar, counting one, two, three in your head.', {'p': 50, 'r': 'ex1'}),
  ('count', {'beats': 'X@96 x@96 x@96', 'say': '1 2 3'}, {'p': 50, 'r': 'ex1'}),
  ('B', 'Then step in on the next beat one, the way you step onto a moving escalator.', {'p': 50, 'r': 'ex1'}),
  ('count', {'beats': 'X@96 x@96 x@96 X@96 x@96 x@96 X@96 x@96 x@96 X@96 x@96 x@96', 'notes': 'R@96 R@96 R@96 C4@96 C4@96 C4@96 C4@48 C4@96 C4@32', 'say': '1 2 3 1 2 3 1 2 3 1 2 3'}, {'p': 50, 'r': 'ex1'}),
  ('P', 'The first note landed right on the beat!', {'p': 50, 'r': 'ex1', 'reveal': True})]),
 ('Strong and weak beats', [
  ('B', 'The beats are not all the same. Two beats in a bar go strong, weak, like a march.', {'p': 51, 'r': 'xlate'}),
  ('piano', 'X x X x X x X x', {'p': 51, 'r': 'xlate'}),
  ('B', 'Three go strong, weak, weak, like a waltz.', {'p': 51, 'r': 'xlate'}),
  ('piano', 'X x x X x x X x x', {'p': 51, 'r': 'xlate'}),
  ('B', 'And four go strong, weak, medium, weak, like most songs.', {'p': 51, 'r': 'xlate'}),
  ('piano', 'X x M x X x M x', {'p': 51, 'r': 'xlate'}),
  ('P', 'So Twinkle, Twinkle is in four, and Happy Birthday is in three.', {'p': 51, 'r': 'xlate'}),
  ('B', 'Exactly. And the Radetzky March is in two.', {'p': 51, 'r': 'xlate'})]),
 ('Example: march or waltz?', [
  ('B', 'Is this a march or a waltz? Tap a steady beat as you listen.', {'p': 51, 'r': 'ex2'}),
  ('piano', 'C3 G4 G4 C3 G4 G4 C3 G4 G4', {'p': 51, 'r': 'ex2'}),
  ('B', 'Which beats feel heavier? Count from one heavy beat to the next. Pause and count.', {'p': 51, 'r': 'ex2'}),
  ('pause', 3, {'p': 51, 'r': 'ex2'}),
  ('P', 'Heavy every three: one two three, one two three. A waltz!', {'p': 51, 'r': 'ex2', 'reveal': True}),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'C3 G4 G4 C3 G4 G4 C3 G4 G4', 'say': '1 2 3 1 2 3 1 2 3'}, {'p': 51, 'r': 'ex2', 'reveal': True}),
  ('B', 'Every two would be a march.', {'p': 51, 'r': 'ex2', 'reveal': True})]),
 ('Bars and bar lines', [
  ('B', 'A bar line divides the music into bars. A double bar line marks the end of a section, or a change. A final bar line, thin then thick, marks the end of the piece.', {'p': 51, 'r': 'xlate2'}),
  ('B', 'And repeat signs: play the passage between them again. If there is no start sign, go back to the beginning.', {'p': 51, 'r': 'xlate2'})]),
 ('Counting', [
  ('B', 'Every beat is counted, even inside a long note. Here are three bars of three-four. The red number is where you play; the grey numbers are the beats you hold.', {'p': 52, 'r': 'xlate'}),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'C4 C4 C4 C4*2 C4 C4*3', 'say': '1 2 3 1 2 3 1 2 3'}, {'p': 52, 'r': 'xlate'}),
  ('B', 'Count aloud at one speed, a little louder on beat one. With a metronome, start slower than you think, and speed up only when the passage is steady.', {'p': 52, 'r': 'xlate'})]),
 ('Try it', [
  ('B', 'Hand on your heart. Tap the beat and say one, two, three, four, with one a little louder. Keep going for ten seconds without slowing down.', {'p': 52, 'r': 'try10'}),
  ('count', {'beats': 'X@80 x@80 x@80 x@80 X@80 x@80 x@80 x@80 X@80 x@80 x@80 x@80', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, {'p': 52, 'r': 'try10', 'seq': ['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11']}),
  ('B', 'At the New Year concert in Vienna, the audience claps along on every beat of the Radetzky March. That steady clap is the pulse; the tune moves freely over it.', {'p': 52, 'r': 'yk'}),
  ('count', {'beats': 'X x X x X x', 'say': '1 2 1 2 1 2'}, {'p': 52, 'r': 'yk', 'seq': ['#0', '#1', '#2', '#3', '#4', '#5']}),
  ('B', 'The beat is the stage and the notes are the actors: the stage is there before anyone walks on. So watch it move for a bar, then step in. Until next time, Clara.', {'p': 52, 'r': 'think'}),
  ('P', 'One, two, three, four. Goodbye!', {'p': 52, 'r': 'think'})])])
CH['T1'] = NEW['T1']

NEW['T2'] = ('Notes and rests', [
 ('The secret', [
  ('P', 'How do I know how long to hold a note?', {'p': 53, 'r': 'lead'}),
  ('B', 'Its shape tells you, Clara. Each note is half the one above it. A semibreve lasts four beats. It splits into two minims, two beats each. A minim splits into two crotchets, one beat each. And a crotchet splits into two quavers, half a beat each.', {'p': 53, 'r': 'hero'}),
  ('B', 'Listen to one bar of each. The beat keeps going; only the notes change.', {'p': 53, 'r': 'hero'}),
  ('count', {'beats': 'X x M x X x M x X x M x', 'notes': 'C4*4 C4*2 C4*2 C4 C4 C4 C4', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, {'p': 53, 'r': 'hero'}),
  ('B', 'And quavers: two to every beat.', {'p': 53, 'r': 'hero'}),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2 C4/2 C4/2 C4/2 C4/2', 'say': '1 & 2 & 3 & 4 &'}, {'p': 53, 'r': 'hero'}),
  ('P', 'For the quavers you said "and" in between.', {'p': 53, 'r': 'sm'}),
  ('B', 'Yes. Say the beat’s number, then "and" halfway to the next beat. And here is the other half of the secret: every note has a twin rest, a silence of exactly the same length.', {'p': 53, 'r': 'secret'})]),
 ('Head, stem, flag', [
  ('B', 'A note has a head, on a line or in a space. Every note except the semibreve has a stem. Below the middle line the stem goes up, on the right of the head; on or above the middle line it goes down, on the left.', {'p': 53, 'r': 'two'}),
  ('P', 'Does a stem going down make the note shorter?', {'p': 53, 'r': 'two'}),
  ('B', 'Never. The stem only keeps the page tidy. Flags change the length: each flag halves the note. And quavers side by side are joined by a beam instead of flags.', {'p': 53, 'r': 'two'}),
  ('P', 'So a note on the middle line has its stem going down?', {'p': 53, 'r': 'two'}),
  ('B', 'Exactly: on or above the middle line, down on the left; below it, up on the right.', {'p': 53, 'r': 'two'})]),
 ('Every note has a twin rest', [
  ('B', 'Every note has a twin rest, the same length with no sound: semibreve, minim, crotchet, quaver, and the semiquaver, a quarter of a beat, which you will meet later.', {'p': 53, 'r': 'svg'}),
  ('B', 'Two rests look alike. The semibreve rest hangs from the fourth line, heavy, like a coat on a hook. The minim rest sits on the middle line, like a hat.', {'p': 53, 'r': 'svg'})]),
 ('The semibreve rest’s special power', [
  ('B', 'Most rests last a fixed number of beats. The semibreve rest can also mean a whole bar of silence, in any time signature, and then it sits in the middle of the bar. In four-four it lasts four beats, in three-four three, in two-four two. Listen to three-four: the middle bar is silent, and the beat goes on.', {'p': 54, 'r': 'box'}),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'C4 C4 C4 R*3 C4*2 C4', 'say': '1 2 3 1 2 3 1 2 3'}, {'p': 54, 'r': 'box'})]),
 ('Pizzas', [
  ('B', 'Some books call the notes whole, half, quarter, eighth and sixteenth notes. Here is why.', {'p': 54, 'r': 'pzbox'}),
  ('B', 'Think of each beat as a pizza. A bar of four-four is four pizzas. The semibreve fills all four; a minim, two; a crotchet, one; a quaver, half a pizza. A rest is the same share, left empty.', {'p': 54, 'r': 'pzbox'}),
  ('P', 'So two quavers make one full pizza.', {'p': 54, 'r': 'pzbox'}),
  ('B', 'Listen: two quavers, then a crotchet. Same-sized pizza.', {'p': 54, 'r': 'pzbox'}),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4/2 C4/2 C4 C4/2 C4/2 C4', 'say': '1 & 2 & 3 & 4 &'}, {'p': 54, 'r': 'pzbox'})]),
 ('Example: each sound and each silence', [
  ('B', 'Two bars of four-four. Name each shape, say how many beats it lasts, and add them up, rests included. Pause and try.', {'p': 54, 'r': 'ex1'}),
  ('pause', 4, {'p': 54, 'r': 'ex1'}),
  ('P', 'Minim, two. Crotchet, one. Crotchet rest, one. Four beats!', {'p': 54, 'r': 'ex1', 'reveal': True}),
  ('B', 'And the second bar has the same shapes in a different order. Count it with me: the rests are counted too.', {'p': 54, 'r': 'ex1', 'reveal': True}),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C4*2 C4 R C4 R C4*2', 'say': '1 2 3 4 1 2 3 4'}, {'p': 54, 'r': 'ex1', 'reveal': True})]),
 ('Game: pizza match', [
  ('B', 'A quick game. Match each note, A to D, with its pizzas, one to four. One pizza is one beat. Pause and match.', {'p': 55, 'r': 'game'}),
  ('pause', 5, {'p': 55, 'r': 'game'}),
  ('P', 'A, the semibreve, is four pizzas: number three. B, the minim, two: number one. C, the crotchet: number four. D, the quaver, half a pizza: number two.', {'p': 55, 'r': 'game', 'reveal': True})]),
 ('Try it', [
  ('B', 'Clap once and hold for two: a minim. Then rest for three, four. Then four crotchets, then a semibreve: clap, and hold all four beats. Say the counts out loud.', {'p': 55, 'r': 'try10'}),
  ('count', {'beats': 'X x M x X x M x X x M x', 'notes': 'C4*2 R*2 C4 C4 C4 C4 C4*4', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, {'p': 55, 'r': 'try10'})]),
 ('Example: fill the bar', [
  ('B', 'A bar of four-four is a train with four seats. How many seats does the minim take? And the crotchet? How many are left, and which rest fills them? Pause and think.', {'p': 55, 'r': 'ex2'}),
  ('pause', 4, {'p': 55, 'r': 'ex2'}),
  ('P', 'The minim takes two and the crotchet one: three. One seat left: a crotchet rest!', {'p': 55, 'r': 'ex2', 'reveal': True}),
  ('count', {'beats': 'X x M x', 'notes': 'C4*2 C4 R', 'say': '1 2 3 4'}, {'p': 55, 'r': 'ex2', 'reveal': True})]),
 ('You know this', [
  ('B', 'Twinkle, Twinkle: six crotchets, then a minim at the end of the line, two beats to breathe.', {'p': 55, 'r': 'yk'}),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C4 C4 G4 G4 A4 A4 G4*2', 'say': '1 2 3 4 1 2 3 4'}, {'p': 55, 'r': 'yk'}),
  ('B', 'A rest is not a gap in the music; it is music you can’t hear. Keep counting through it. Until next time, Clara.', {'p': 55, 'r': 'yk'}),
  ('P', 'One, two, three, four. Goodbye!', {'p': 55, 'r': 'yk'})])])
CH['T2'] = NEW['T2']

NEW['T3'] = ('How long is a note?', [
 ('The secret', [
  ('P', 'What if I need a note longer than its shape?', {'p': 56, 'r': 'lead'}),
  ('B', 'Two signs stretch it, Clara: the dot and the tie. When a crotchet is one beat, a minim lasts two. Put a dot after it, and the dot adds half of two: one more beat. Two plus one: three beats.', {'p': 56, 'r': 'hero'}),
  ('B', 'Listen: a minim, then a dotted minim. Count with me.', {'p': 56, 'r': 'hero'}),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C4*2 R*2 C4*3 R', 'say': '1 2 3 4 1 2 3 4'}, {'p': 56, 'r': 'hero'}),
  ('B', 'That is the secret. A dot adds half. A tie glues two notes into one sound.', {'p': 56, 'r': 'secret'})]),
 ('The dot', [
  ('B', 'A dot always adds half of its own note. A dotted crotchet is one plus a half: one and a half beats. Here it is, then a quaver, then a minim. Hold the dotted crotchet through "one and two", and the quaver lands on the "and".', {'p': 56, 'r': 'xlate'}),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4*1.5 C4/2 C4*2', 'say': '1 & 2 & 3 & 4 &'}, {'p': 56, 'r': 'xlate'})]),
 ('The dot, in pizzas', [
  ('B', 'In pizzas: a dotted minim is two pizzas, plus one more for the dot. A dotted crotchet is one pizza plus half. A dotted quaver is half a pizza plus a quarter. The dot is always half of whatever its note is worth.', {'p': 56, 'r': 'xlate'})]),
 ('Example: a dotted crotchet and a quaver', [
  ('B', 'How many beats are a dotted crotchet and a quaver together? And where does the quaver fall? Pause and try.', {'p': 56, 'r': 'ex1'}),
  ('pause', 4, {'p': 56, 'r': 'ex1'}),
  ('P', 'One and a half, plus a half: two beats. The quaver lands on the "and" of two.', {'p': 56, 'r': 'ex1', 'reveal': True}),
  ('count', {'beats': 'X/2 R/2 x/2 R/2', 'notes': 'C4*1.5 C4/2', 'say': '1 & 2 &'}, {'p': 56, 'r': 'ex1', 'reveal': True})]),
 ('Example: Ode to Joy', [
  ('B', 'You already know a dotted crotchet: Beethoven’s Ode to Joy. Listen to bars three and four. The red E is dotted: hold it through "one and two". The quaver D falls on the "and", and the last D takes beats three and four.', {'p': 57, 'r': 'ex2'}),
  ('count', {'beats': 'X x M x X/2 R/2 x/2 R/2 M x', 'notes': 'C4 C4 D4 E4 E4*1.5 D4/2 D4*2', 'say': '1 2 3 4 1 & 2 & 3 4'}, {'p': 57, 'r': 'ex2', 'reveal': True}),
  ('P', 'Long, short, then long. It leans before it lands!', {'p': 57, 'r': 'ex2', 'reveal': True})]),
 ('The double dot', [
  ('B', 'Going further: a second dot adds half of the first dot. A double-dotted minim lasts two, plus one, plus a half: three and a half beats. You will not need it for a while.', {'p': 57, 'r': 'xlate'})]),
 ('The tie', [
  ('B', 'A tie is a curve joining two notes of the same pitch. Play the first and hold through the second. Never play the second again. And a tie can cross a bar line, which a dot cannot.', {'p': 57, 'r': 'xlate2'}),
  ('count', {'beats': 'X x X x', 'notes': 'C4 C4~ C4 C4', 'say': '1 2 1 2'}, {'p': 57, 'r': 'xlate2'}),
  ('P', 'One sound from beat two, right over the bar line to beat one.', {'p': 57, 'r': 'xlate2'})]),
 ('Example: dot or tie?', [
  ('B', 'Which is longer: the dotted minim, or the minim tied to a crotchet? Add up each one. Pause and try.', {'p': 57, 'r': 'ex3'}),
  ('pause', 4, {'p': 57, 'r': 'ex3'}),
  ('P', 'Dotted minim: two plus one, three. Tied notes: two plus one, three. The same!', {'p': 57, 'r': 'ex3', 'reveal': True}),
  ('count', {'beats': 'X x x X x x', 'notes': 'C4*3 C4*2~ C4', 'say': '1 2 3 1 2 3'}, {'p': 57, 'r': 'ex3', 'reveal': True}),
  ('B', 'Both last three beats. But only the tie could cross a bar line.', {'p': 57, 'r': 'ex3', 'reveal': True})]),
 ('Example: which is longer?', [
  ('B', 'A dotted minim, or a minim tied to a quaver? Count the pizzas. Pause and try.', {'p': 58, 'r': 'ex4'}),
  ('pause', 4, {'p': 58, 'r': 'ex4'}),
  ('P', 'Three against two and a half. The dotted minim is longer, by half a beat.', {'p': 58, 'r': 'ex4', 'reveal': True}),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4*3 R', 'say': '1 & 2 & 3 & 4 &'}, {'p': 58, 'r': 'ex4', 'reveal': True}),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4*2~ C4/2 R/2 R', 'say': '1 & 2 & 3 & 4 &'}, {'p': 58, 'r': 'ex4', 'reveal': True})]),
 ('Tie or slur?', [
  ('B', 'Careful: two curves look alike. A tie joins the same pitch: play once and hold. Here, G for four beats, then E for four.', {'p': 58, 'r': 'xlate'}),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'G4*2~ G4*2 E4*2~ E4*2', 'say': '1 2 3 4 1 2 3 4'}, {'p': 58, 'r': 'xlate'}),
  ('B', 'A slur joins different pitches: play every note, smoothly joined. That smooth playing is called legato. Listen: every note sounds.', {'p': 58, 'r': 'xlate'}),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C4 D4 E4 F4 G4*4', 'say': '1 2 3 4 1 2 3 4'}, {'p': 58, 'r': 'xlate'})]),
 ('Game: how many beats?', [
  ('B', 'Game time. With a crotchet as one beat, how long does each one last: a dotted minim, a dotted crotchet, and a minim tied to a crotchet? Pause and count.', {'p': 58, 'r': 'game'}),
  ('pause', 5, {'p': 58, 'r': 'game'}),
  ('P', 'Three. One and a half. And three again.', {'p': 58, 'r': 'game', 'reveal': True})]),
 ('Try it', [
  ('B', 'Clap once, and hold for three, saying one, two, three: a dotted minim.', {'p': 58, 'r': 'try10'}),
  ('count', {'beats': 'X x x X x x', 'notes': 'C4*3 C4*3', 'say': '1 2 3 1 2 3'}, {'p': 58, 'r': 'try10'}),
  ('B', 'Then a dotted crotchet and a quaver: clap on one, hold through "and two", and clap again on the "and".', {'p': 58, 'r': 'try10'}),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 X/2 R/2 x/2 R/2', 'notes': 'C4*1.5 C4/2 C4*1.5 C4/2', 'say': '1 & 2 & 1 & 2 &'}, {'p': 58, 'r': 'try10'})]),
 ('Watch out', [
  ('B', 'Three traps. A dot adds half of its own note, not of the next one. A curve between two different pitches is a slur, not a tie. And there are two kinds of dot: after the head, it adds length; above or below the head, it means staccato, short.', {'p': 58, 'r': 'watch'}),
  ('B', 'A dot is a little loan of time; a tie is a bridge between two notes. Until next time, Clara.', {'p': 58, 'r': 'watch'}),
  ('P', 'One, two, three. Goodbye!', {'p': 58, 'r': 'watch'})])])
CH['T3'] = NEW['T3']

NEW['PO'] = ('Welcome', [
 ('The secret', [
  ('B', 'Good day, and welcome. I am the Piano Butler. I look after everything a pianist needs to read and understand music, and I explain it, one chapter at a time.', c(21, 'map')),
  ('P', 'Hello! I am Clara. I can play a few tunes, but I want to know what all the signs on the page mean.', c(21, 'map')),
  ('B', 'Then you have come to the right place, Miss Clara. You shall be my pupil. I explain, you try, and every chapter ends with something to play.', c(21, 'map')),
  ('B', 'You will also meet Their Majesties. The Queen of the Treble rules the high notes, and the King of the Bass rules the low ones. They are rather particular about their lines, so you will be introduced properly in chapter two.', c(21, 'map')),
  ('P', 'A real Queen and King? I had better practise my bow.', c(21, 'map')),
  ('B', 'Very wise. And whenever I name something on the page, look for it: it lights up as I say it.', c(21, 'map'))]),
 ('Part One: Pitch', [
  ('B', 'Part One is Pitch: high or low. We start with the keys under your fingers, then find where they live on the staff, see how sharps and flats move them, and finish by measuring how far apart two notes are.', c(21, 'map')),
  ('P', 'All of that in one picture?', c(21, 'map')),
  ('B', 'All of it, in this one picture: eight chapters, and a page of tips at the end. Shall we begin with the keyboard?', c(21, 'map')),
  ('P', 'Yes, please!', c(21, 'map'))])])
CH['PO'] = NEW['PO']

# ---- Time 4–8 (her 9 Nov: "응 순서대로 해줘": the same pass, with audio) ----
NEW['T4'] = ('Time signatures', [
 ('The secret', [
  ('P', 'What are the two numbers at the start of the music?', c(59, 'lead')),
  ('B', 'The time signature, Clara. Read it like a train ticket. The top number says how many seats each carriage, each bar, has. The bottom number says which note sits in one seat.', c(59, 'hero')),
  ('B', 'Four-four: four seats, and a crotchet in each. Count the seats with me.', c(59, 'hero')),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C4 C4 C4 C4 C4 C4 C4 C4', 'say': '1 2 3 4 1 2 3 4'}, c(59, 'hero')),
  ('B', 'That is the secret: the top number is how many beats, and the bottom number is which note gets one beat.', c(59, 'secret'))]),
 ('Think of a train', [
  ('B', 'In three-four every carriage has three seats. A minim books two, a crotchet one. A rest books a seat and leaves it empty. A dotted minim fills all three.', c(59, 'pzbox')),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'C4*2 C4 C4 R C4 C4*3', 'say': '1 2 3 1 2 3 1 2 3'}, c(59, 'pzbox')),
  ('B', 'The bottom number is a code: two means a minim, four a crotchet, eight a quaver, sixteen a semiquaver.', c(59, 'xlate'))]),
 ('Example: what does three-four mean?', [
  ('B', 'Three-four. How many counts in each bar, and which note gets one count? Pause and think.', c(60, 'ex1')),
  ('pause', 3, c(60, 'ex1')),
  ('P', 'Three counts, and the four means a crotchet.', c(60, 'ex1', reveal=True)),
  ('B', 'Check the first bar: two quavers make one, then a crotchet, a crotchet. Three. Count it.', c(60, 'ex1', reveal=True)),
  ('count', {'beats': 'X/2 R/2 x x X x x', 'notes': 'C4/2 C4/2 C4 C4 C4*2 C4', 'say': '1 & 2 3 1 2 3'}, c(60, 'ex1', reveal=True))]),
 ('Simple time', [
  ('B', 'In simple time every beat splits into two. Two-four, three-four and four-four count crotchets. Four-four is also written as a C, common time, and two-two as a C with a line through it, cut common time: two minim beats.', c(60, 'xlate'))]),
 ('Example: which ticket?', [
  ('B', 'This carriage has three seats, and a quaver sits in each. Write the ticket. Pause and try.', c(60, 'ex2')),
  ('pause', 4, c(60, 'ex2')),
  ('P', 'Three on top. A quaver is eight, so eight underneath: three-eight!', c(60, 'ex2', reveal=True))]),
 ('Example: where does the rest go?', [
  ('B', 'Four-four, and three crotchets. Which seat is empty, and what goes there?', c(61, 'ex3')),
  ('pause', 3, c(61, 'ex3')),
  ('P', 'Seat four. A crotchet rest!', c(61, 'ex3', reveal=True)),
  ('count', {'beats': 'X x M x', 'notes': 'C4 C4 C4 R', 'say': '1 2 3 4'}, c(61, 'ex3', reveal=True))]),
 ('Changing time signature', [
  ('B', 'A new time signature can arrive right after a bar line. Here three-four becomes two-four, and two beats a bar holds until the next one.', c(61, 'xlate')),
  ('count', {'beats': 'X x x X x x X x X x X x', 'notes': 'C4 C4 C4 C4*2 C4 C4 C4 C4*2 C4 C4', 'say': '1 2 3 1 2 3 1 2 1 2 1 2'}, c(61, 'xlate'))]),
 ('You know this', [
  ('B', 'The Minuet from the Notebook for Anna Magdalena Bach: one two three, one two three, the step of the dance. That is three-four.', c(61, 'yk')),
  ('count', {'beats': 'X x x X x x', 'notes': 'D5 G4/2 A4/2 B4/2 C5/2 D5 G4 G4', 'say': '1 2 3 1 2 3'}, c(61, 'yk')),
  ('Q', 'And remember, Clara: the bottom number is not a count. It names the note that gets one beat.', c(61, 'watch')),
  ('B', 'Until next time, Clara.', c(61, 'watch')), ('P', 'Goodbye!', c(61, 'watch'))])])
CH['T4'] = NEW['T4']

NEW['T5'] = ('Compound and irregular time', [
 ('The secret', [
  ('P', 'Some pieces feel like skipping. Why?', c(62, 'lead')),
  ('B', 'That is compound time, Clara. Take six quavers. Three-four groups them in twos: three beats. Six-eight groups them in threes: two big beats.', c(62, 'hero')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 x/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2 C4/2 C4/2', 'say': '1 & 2 & 3 &'}, c(62, 'hero')),
  ('count', {'beats': 'X/2 R/2 R/2 M/2 R/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2 C4/2 C4/2', 'say': '1 2 3 4 5 6'}, c(62, 'hero')),
  ('B', 'The same six notes, new groups. The secret: in compound time each beat is a dotted note, and it splits in three.', c(62, 'secret'))]),
 ('Simple or compound?', [
  ('B', 'In simple time one beat splits in two. In compound time one dotted beat splits in three. Quick test: a top number of six, nine or twelve means compound. Divide it by three to find the beats.', c(62, 'xlate'))]),
 ('Counting six-eight', [
  ('B', 'Slowly, count all six quavers. At speed, feel only two beats, on one and four.', c(63, 'xlate')),
  ('count', {'beats': 'X x x M x x', 'notes': 'C4 C4 C4 C4 C4 C4', 'say': '1 2 3 4 5 6'}, c(63, 'xlate')),
  ('count', {'beats': 'X R R M R R X R R M R R', 'notes': 'C4 C4 C4 C4 C4 C4 C4*3 C4*3', 'say': '1 2 3 4 5 6 1 - - 4 - -'}, c(63, 'xlate')),
  ('B', 'Try it: say pine-ap-ple on every beat, and step only on pine.', c(63, 'xlate'))]),
 ('Example: how many beats in nine-eight?', [
  ('B', 'Nine-eight. Does nine divide by three? How many groups of three?', c(63, 'ex1')),
  ('pause', 3, c(63, 'ex1')),
  ('P', 'Three groups: three beats, each a dotted crotchet!', c(63, 'ex1', reveal=True)),
  ('count', {'beats': 'X x x M x x M x x', 'notes': 'C4 C4 C4 C4 C4 C4 C4 C4 C4', 'say': '1 2 3 4 5 6 7 8 9'}, c(63, 'ex1', reveal=True))]),
 ('Example: is this still four-four?', [
  ('B', 'Many dances keep four-four but group the eight quavers three, three, two. Where do the accents fall? And how many times does your foot tap?', c(63, 'xlate2')),
  ('count', {'beats': 'X/2 R/2 R/2 M/2 R/2 R/2 M/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2 C4/2 C4/2 C4/2 C4/2', 'say': '1 2 3 1 2 3 1 2'}, c(63, 'xlate2')),
  ('P', 'Accents on one, four and seven, but my foot still taps four times.', c(63, 'xlate2', reveal=True)),
  ('B', 'So it is still four-four. Only the accents are uneven.', c(63, 'xlate2', reveal=True))]),
 ('Irregular time', [
  ('B', 'Going further: irregular time has five or seven counts, in uneven groups. Five-four is three plus two; seven-eight can be two, two, three.', c(64, 'xlate')),
  ('count', {'beats': 'X x x M x X x x M x', 'notes': 'C4 C4 C4 C4 C4 C4 C4 C4 C4 C4', 'say': '1 2 3 1 2 1 2 3 1 2'}, c(64, 'xlate')),
  ('K', 'Five in a bar? In my day we kept to twos and threes. But I must admit, it does make one dance.', c(64, 'xlate'))]),
 ('You know this', [
  ('B', 'Row, Row, Row Your Boat: two big beats in every bar, each a dotted crotchet. Sway twice per bar while you sing.', c(64, 'yk')),
  ('count', {'beats': 'X R R M R R X R R M R R', 'notes': 'C4*3 C4*3 C4*2 D4 E4*3', 'say': '1 - - 2 - - 1 - - 2 - -'}, c(64, 'yk')),
  ('B', 'And watch the bottom number: six-eight counts quavers, not crotchets. Until next time, Clara.', c(64, 'watch')), ('P', 'Goodbye!', c(64, 'watch'))])])
CH['T5'] = NEW['T5']

NEW['T6'] = ('Rhythm: groups and upbeats', [
 ('The secret', [
  ('P', 'Why are some quavers joined together?', c(65, 'lead')),
  ('B', 'Those lines are beams, Clara. One beam, one beat: they join the notes that share a beat, so you can see where each beat starts.', c(65, 'hero')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C5/2 C5/2 C5/2 C5/2 C5/2 C5/2 C5/2 C5/2', 'say': '1 & 2 & 3 & 4 &'}, c(65, 'hero')),
  ('B', 'That is half the secret. The other half: an upbeat borrows from the last bar.', c(65, 'secret'))]),
 ('Grouping with beams', [
  ('B', 'In four-four a beam may cover beats one and two, or three and four, but never cross the middle of the bar. On the left the beams show the beats. On the right, one beam hides the middle.', c(65, 'xlate')),
  ('P', 'So the middle of the bar must always show.', c(65, 'xlate'))]),
 ('Example: six quavers in three-four', [
  ('B', 'Six quavers in three-four. Why are they beamed in twos? Pause and think.', c(65, 'ex1')),
  ('pause', 3, c(65, 'ex1')),
  ('P', 'Three crotchet beats, two quavers each!', c(65, 'ex1', reveal=True)),
  ('B', 'Beamed in threes, they would look like six-eight.', c(65, 'ex1', reveal=True)),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 x/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2 C4/2 C4/2', 'say': '1 & 2 & 3 &'}, c(65, 'ex1', reveal=True))]),
 ('The upbeat', [
  ('B', 'A piece can begin before the first full bar. These notes are the upbeat, or anacrusis. Count one two silently, then play on three. The last bar is short by the same amount: one plus two makes a full bar.', c(66, 'xlate')),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'R R C4 C4 C4 C4 C4*2 R', 'say': '1 2 3 1 2 3 1 2 -'}, c(66, 'xlate')),
  ('B', 'Happy Birthday starts with an upbeat. Hap-py comes before the strong beat, and the strong beat lands on birth.', c(66, 'xlate')),
  ('count', {'beats': 'R x X x x', 'notes': 'C4*0.75 C4/4 D4 C4 F4', 'say': '- 3 1 2 3'}, c(66, 'xlate'))]),
 ('Triplets', [
  ('B', 'A triplet is three equal notes in the time of two, marked with a little three. One beat cut in two is two quavers; cut in three, a triplet; cut in four, four semiquavers.', c(66, 'xlate2')),
  ('count', {'beats': 'X x M x', 'notes': 'C4/2 C4/2 C4/3 C4/3 C4/3 C4/4 C4/4 C4/4 C4/4 C4', 'say': '1 2 3 4'}, c(66, 'xlate2'))]),
 ('Example: where is the triplet?', [
  ('B', 'Find the little three. Which beat do the three quavers share?', c(67, 'ex2')),
  ('pause', 3, c(67, 'ex2')),
  ('P', 'Beat two!', c(67, 'ex2', reveal=True)),
  ('B', 'Say it: one, two and a, three, four. The beat never moves.', c(67, 'ex2', reveal=True)),
  ('count', {'beats': 'X x M x', 'notes': 'C4 C4/3 C4/3 C4/3 C4 C4', 'say': '1 2 3 4'}, c(67, 'ex2', reveal=True))]),
 ('Example: a bar of mixed values', [
  ('B', 'Now a bar with everything: a crotchet, two quavers, four semiquavers and a triplet. One beat each. Count it with me.', c(67, 'ex3')),
  ('count', {'beats': 'X x M x', 'notes': 'C4 C4/2 C4/2 C4/4 C4/4 C4/4 C4/4 C4/3 C4/3 C4/3', 'say': '1 2 3 4'}, c(67, 'ex3', reveal=True)),
  ('B', 'Going further: a duplet is the triplet turned inside out, two notes in the time of three, in compound time. Until next time, Clara.', c(67, 'xlate')), ('P', 'Goodbye!', c(67, 'xlate'))])])
CH['T6'] = NEW['T6']

NEW['T7'] = ('Rhythm: off the beat', [
 ('The secret', [
  ('P', 'Some music seems to bounce between the beats.', c(68, 'lead')),
  ('B', 'That is rhythm teasing the beat, Clara. Here a note starts on the and, between the beats, and is held over beat two.', c(68, 'hero')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4 C4/2 C4 C4 C4/2 C4', 'say': '1 & 2 & 3 & 4 &'}, c(68, 'hero')),
  ('B', 'It only works if the beat underneath stays rock-steady. That is the secret.', c(68, 'secret'))]),
 ('Swing', [
  ('B', 'First, swing. Jazz and blues pieces are often marked swing. Pairs of quavers are written evenly but played long, short, like the first and last notes of a triplet.', c(68, 'xlate')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2', 'say': '1 & 2 &'}, c(68, 'xlate')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2', 'notes': 'C4*0.667 C4/3 C4*0.667 C4/3', 'say': '1 & 2 &'}, c(68, 'xlate')),
  ('B', 'Which notes swing here? Pause and look.', c(68, 'xlate')), ('pause', 3, c(68, 'xlate')),
  ('P', 'Only the quaver pairs, on beats two and three. The crotchets stay even.', c(68, 'xlate', reveal=True))]),
 ('Syncopation', [
  ('B', 'Syncopation: a note starts on the and, and is held through the next beat. Tap the beats: one, two. Where does the red crotchet start?', c(69, 'xlate')),
  ('pause', 3, c(69, 'ex2')),
  ('P', 'On the and, and it holds through beat two!', c(69, 'ex2', reveal=True)),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 X/2 R/2 x/2 R/2', 'notes': 'C4/2 C4 C4/2 C4 C4', 'say': '1 & 2 & 1 & 2 &'}, c(69, 'ex2', reveal=True)),
  ('B', 'The Entertainer, by Scott Joplin: the high C keeps landing just after the beat. That is the bounce of ragtime.', c(69, 'xlate2')),
  ('B', 'To feel it, tap a steady beat with your foot, and clap only between the taps. If your foot starts to follow your hands, slow down.', c(69, 'howto'))]),
 ('Hemiola', [
  ('B', 'Hemiola: two bars of three-four felt as three big beats. Count as written, one two three, one two three. Now feel each minim as one big beat. How many?', c(70, 'xlate')),
  ('count', {'beats': 'X x x X x x', 'notes': 'C4*2 C4*2 C4*2', 'say': '1 2 3 1 2 3'}, c(70, 'xlate')),
  ('P', 'Three big ones!', c(70, 'xlate', reveal=True))]),
 ('Polyrhythm and rubato', [
  ('B', 'Going further: polyrhythm is two rhythms at once, three against two. And rubato stretches the time, then gives it back. Whatever you borrow, you pay back.', c(70, 'xlate2')),
  ('B', 'Keep counting inside long notes, and only the quaver pairs swing. Until next time, Clara.', c(70, 'watch')), ('P', 'Goodbye!', c(70, 'watch'))])])
CH['T7'] = NEW['T7']

NEW['T8'] = ('Repeats and road signs', [
 ('The secret', [
  ('P', 'Why does the music sometimes go backwards?', c(71, 'lead')),
  ('B', 'To save writing the same bars twice, Clara. Two dots facing back mean: go back and play it again. Here you play A, B, then A, B again, then C.', c(71, 'hero')),
  ('B', 'Read the signs like a map. Jump back at the sign, stop at Fine, or jump to the Coda.', c(71, 'secret'))]),
 ('The signs', [
  ('B', 'Repeat signs: play the bars between them twice. First and second time bars: the first time, play bar one; after the repeat, skip it and play bar two. D.C., da capo, from the head: back to the very beginning. D.S., dal segno: back to the sign. Fine: the end. And Coda, the tail: at To Coda, jump to the coda sign.', c(71, 'ht')),
  ('B', 'The rule: follow the map in order. After a jump, stop at the first Fine you meet, or jump at To Coda.', c(71, 'rule'))]),
 ('Example: one repeat sign', [
  ('B', 'B ends with a repeat sign, and there is no start sign. In what order do you play? Pause and try.', c(72, 'ex1')),
  ('pause', 4, c(72, 'ex1')),
  ('P', 'Back to the very start: A, B, A, B, C.', c(72, 'ex1', reveal=True))]),
 ('Example: first and second time', [
  ('B', 'First time: A, then the bar marked one. The repeat sends you back to A. Second time, which bar do you skip?', c(72, 'ex2')),
  ('pause', 4, c(72, 'ex2')),
  ('P', 'Skip B: A, B, A, C.', c(72, 'ex2', reveal=True))]),
 ('Game: how many bars?', [
  ('B', 'A quick game: each letter is one bar. Follow the signs and count every bar you play. Pause and count.', c(72, 'game')),
  ('pause', 6, c(72, 'game')),
  ('P', 'Four, six and five!', c(72, 'game', reveal=True))]),
 ('Example: D.C. al Fine', [
  ('B', 'Play straight through to D. D.C. sends you back to the head. Where do you stop?', c(73, 'ex3')),
  ('pause', 4, c(73, 'ex3')),
  ('P', 'At Fine: A, B, C, D, A, B.', c(73, 'ex3', reveal=True))]),
 ('Example: D.S. al Coda', [
  ('B', 'Play through to D, ignoring To Coda the first time. D.S. sends you back to the sign. Then play on to To Coda, and jump. Pause and try.', c(73, 'ex4')),
  ('pause', 5, c(73, 'ex4')),
  ('P', 'A, B, C, D, then B, C, and jump to E!', c(73, 'ex4', reveal=True)),
  ('Q', 'Splendid. And on the way back after a D.C., Clara, one does not take the repeats again, unless the music says so.', c(73, 'watch')),
  ('B', 'Until next time, Clara.', c(73, 'watch')), ('P', 'Goodbye!', c(73, 'watch'))])])
CH['T8'] = NEW['T8']

# ---- Part III Expression 1–5 (her 10 Nov: "응": the same pass, with audio) ----
NEW['E1'] = ('Loud and soft', [
 ('The secret', [
  ('P', 'Can music whisper?', c(76, 'lead')),
  ('B', 'It can whisper, chat or shout, Clara. Small Italian words tell you which: the dynamics. Six steps, from very soft to very loud.', c(76, 'hero')),
  ('B', 'Pianissimo, very soft. Piano, soft. Mezzo-piano, half soft. Mezzo-forte, half loud. Forte, loud. Fortissimo, very loud.', c(76, 'hero')),
  ('piano', 'pp:C4 p:C4 mp:C4 mf:C4 f:C4 ff:C4', c(76, 'hero')),
  ('B', 'P is soft, f is loud, and m, mezzo, means half. And a sign lasts until the next one arrives.', c(76, 'xlate'))]),
 ('Example: mp or mf?', [
  ('B', 'Which is louder: mp or mf? Pause and think.', c(76, 'ex1')), ('pause', 3, c(76, 'ex1')),
  ('P', 'Mezzo-forte, half loud. It is louder than half soft.', c(76, 'ex1', reveal=True)),
  ('piano', 'mp:E4 mp:E4 | mf:E4 mf:E4', c(76, 'ex1', reveal=True))]),
 ('Growing and fading', [
  ('B', 'Music can also change little by little. Crescendo: getting louder. Diminuendo: getting softer. Written as a word, or as a hairpin that opens or closes.', c(76, 'xlate2')),
  ('piano', 'p:C4 p:D4 mp:E4 mp:F4 mf:G4 mf:A4 f:B4 f:C5 ff:C5*2', c(76, 'xlate2')),
  ('B', 'Sforzando: one note made suddenly strong. Forte-piano: loud, then soft at once. See them as shapes: up, down, a spike, and a drop.', c(77, 'xlate'))]),
 ('Example: sfz or fp?', [
  ('B', 'Two tunes. One has a sudden strong note, the other is loud then soft at once. Which is which? Pause and look.', c(77, 'ex2')), ('pause', 4, c(77, 'ex2')),
  ('P', 'A is sforzando: one strong note. B is forte-piano: loud, then soft.', c(77, 'ex2', reveal=True)),
  ('piano', 'p:C5 p:G4 p:E4 p:G4 ff:C5*2 | f:C5 pp:C5 pp:G4*2', c(77, 'ex2', reveal=True))]),
 ('Example: the hairpins', [
  ('B', 'Follow the hairpins. Where does it start, and what happens?', c(77, 'ex3')), ('pause', 3, c(77, 'ex3')),
  ('P', 'It starts piano, grows into forte, then fades.', c(77, 'ex3', reveal=True)),
  ('piano', 'p:C4 mp:C4 mf:G4 f:G4 | f:A4 mf:A4 p:G4*2', c(77, 'ex3', reveal=True))]),
 ('Example: the loudest note', [
  ('B', 'Now find the loudest note. Start mezzo-piano and follow the hairpin.', c(78, 'ex4')), ('pause', 4, c(78, 'ex4')),
  ('P', 'The first A in bar two, at forte. Then it fades all the way to piano.', c(78, 'ex4', reveal=True))]),
 ('Try it', [
  ('B', 'Try it: play Middle C six ways, from pianissimo to fortissimo. Use the weight of your arm, not by hitting harder. Then come back down.', c(78, 'try10')),
  ('piano', 'pp:C4 p:C4 mp:C4 mf:C4 f:C4 ff:C4 | f:C4 mf:C4 mp:C4 p:C4 pp:C4', c(78, 'try10')),
  ('B', 'Haydn wrote a famous joke. The tune tiptoes along softly, comes again even softer, and then the whole orchestra crashes in with one fortissimo chord. The Surprise Symphony.', c(78, 'yk')),
  ('piano', 'p:C4/2 p:C4/2 p:E4/2 p:E4/2 p:G4/2 p:G4/2 p:E4 | pp:C4/2 pp:C4/2 pp:E4/2 pp:E4/2 [ff G3 B3 D4 G4]', c(78, 'yk')),
  ('P', 'I jumped!', c(78, 'yk')),
  ('B', 'And remember: louder is not faster. Until next time, Clara.', c(78, 'watch')), ('P', 'Goodbye!', c(78, 'watch'))])])
CH['E1'] = NEW['E1']

NEW['E2'] = ('Touch: smooth, short, strong', [
 ('The secret', [
  ('P', 'Can the same notes sound different?', c(79, 'lead')),
  ('B', 'Completely different, Clara. Small marks tell your fingers how to touch the keys. A curve: join them, legato.', c(79, 'hero')),
  ('piano', 'E4 D4 C4 D4', c(79, 'hero')),
  ('B', 'Dots: short and detached, staccato.', c(79, 'hero')), ('piano', 'E4! D4! C4! D4!', c(79, 'hero')),
  ('B', 'Lines: hold the full length, leaning a little, tenuto. And arrows: a stronger start, the accent.', c(79, 'hero')),
  ('piano', 'mf:E4 mf:D4 mf:C4 mf:D4 | f:E4 p:D4 f:C4 p:D4', c(79, 'hero')),
  ('B', 'The secret in four words: curve, join. Dot, short. Line, hold. Arrow, strong.', c(79, 'secret'))]),
 ('Example: line, dot or arrow?', [
  ('B', 'Read the marks. How long are the first two Cs, the Gs, and the E with the arrow? Pause and think.', c(80, 'ex1')), ('pause', 4, c(80, 'ex1')),
  ('P', 'The Cs held their full length, the Gs short, the E strong.', c(80, 'ex1', reveal=True)),
  ('piano', 'C5 G4! G4! C5 | f:E5*2 C5*2', c(80, 'ex1', reveal=True))]),
 ('Slurs and phrases', [
  ('B', 'A curve over different notes is a slur: join them, then lift at its end, like a breath. A long slur over a whole line is a phrase: one musical sentence.', c(80, 'xlate')),
  ('B', 'Ode to Joy has two long phrases. Lift your hand only at the end of each, like a singer taking a breath.', c(80, 'xlate')),
  ('piano', 'E4 E4 F4 G4 G4 F4 E4 D4 C4 C4 D4 E4 E4*1.5 D4/2 D4*2', c(80, 'xlate'))]),
 ('Example: which notes are short?', [
  ('B', 'Bar one has a curve. Bar two has dots, and one other mark. Which notes are short?', c(80, 'ex2')), ('pause', 4, c(80, 'ex2')),
  ('P', 'The two dotted Gs. The third G has an accent: strong, but full length.', c(80, 'ex2', reveal=True)),
  ('piano', 'C4 D4 E4 F4 | G4! G4! f:G4 R', c(80, 'ex2', reveal=True))]),
 ('Two-note slurs', [
  ('B', 'A slur over just two notes is a little sigh: drop into the first, then lift off the second, lighter and shorter. Drop, lift.', c(81, 'xlate')),
  ('piano', 'f:E4 p:D4! | f:G4 p:F4! | f:E4 p:D4!', c(81, 'xlate')),
  ('B', 'And some words describe the mood: dolce, sweetly. Cantabile, singing. Leggiero, lightly. Maestoso, majestically.', c(81, 'xlate2')),
  ('B', 'Legato is walking: one foot leaves the ground as the other lands. Staccato is hopping on hot sand. Until next time, Clara.', c(81, 'think')), ('P', 'Goodbye!', c(81, 'think'))])])
CH['E2'] = NEW['E2']

NEW['E3'] = ('Speed words', [
 ('The secret', [
  ('P', 'How do I know how fast to play?', c(82, 'lead')),
  ('B', 'A word at the top of the music tells you, Clara, usually in Italian. Largo is very slow. Adagio, slow. Andante, a walking pace. Moderato, moderate. Allegro, fast and lively. Presto, very fast.', c(82, 'hero')),
  ('count', {'beats': 'X@60 x@60 x@60 x@60', 'say': '1 2 3 4'}, c(82, 'hero')),
  ('count', {'beats': 'X@92 x@92 x@92 x@92', 'say': '1 2 3 4'}, c(82, 'hero')),
  ('count', {'beats': 'X@138 x@138 x@138 x@138', 'say': '1 2 3 4'}, c(82, 'hero')),
  ('B', 'Adagio, Andante, Allegro. The numbers in the table are only a rough guide.', c(82, 'xlate'))]),
 ('The metronome mark', [
  ('B', 'Often there is a number too. Crotchet equals seventy-six means seventy-six beats in one minute. Set a metronome to seventy-six: each click is one beat.', c(83, 'xlate'))]),
 ('Example: crotchet equals sixty', [
  ('B', 'How fast is crotchet equals sixty? Pause and think.', c(83, 'ex1')), ('pause', 3, c(83, 'ex1')),
  ('P', 'Sixty beats in a minute, and a minute has sixty seconds. One beat every second!', c(83, 'ex1', reveal=True)),
  ('count', {'beats': 'X@60 x@60 x@60 x@60', 'say': '1 2 3 4'}, c(83, 'ex1', reveal=True))]),
 ('Changing speed', [
  ('B', 'Words inside the music change the speed. Ritardando: gradually slower, the beats further apart. Accelerando: gradually faster. A tempo: back to the speed before. And the fermata, the pause: hold longer than written.', c(83, 'xlate2')),
  ('count', {'beats': 'X@100 x@96 x@90 x@82 X@72 x@62 x@52', 'say': '1 2 3 4 1 2 3'}, c(83, 'xlate2'))]),
 ('Example: rall. and a tempo', [
  ('B', 'Where does it slow down, and where does it come back?', c(84, 'ex2')), ('pause', 3, c(84, 'ex2')),
  ('P', 'Bar one slows into the two Gs. At a tempo the first speed comes straight back.', c(84, 'ex2', reveal=True))]),
 ('Example: the fermata', [
  ('B', 'How long do you hold the minim with the fermata?', c(84, 'ex3')), ('pause', 3, c(84, 'ex3')),
  ('P', 'Longer than two beats, until it feels finished. Then go on.', c(84, 'ex3', reveal=True)),
  ('B', 'Players often slow down into the end of Twinkle, Twinkle, then wait on the last note. A rit. is a car braking gently at the lights; a tempo is driving off again. Until next time, Clara.', c(84, 'yk')),
  ('P', 'Goodbye!', c(84, 'yk'))])])
CH['E3'] = NEW['E3']

NEW['E4'] = ('The pedals', [
 ('The secret', [
  ('P', 'What are the pedals for?', c(85, 'lead')),
  ('B', 'Most pianos have three, Clara. The left one, the soft pedal, makes the sound gentler. The right one, the sustain pedal, keeps the notes ringing after your fingers let go.', c(85, 'hero')),
  ('B', 'Inside the piano, each string has a felt damper resting on it. Let go of a key and the damper stops the string. The sustain pedal lifts every damper at once, so the strings ring on.', c(85, 'xlate')),
  ('piano', '[C4 E4 G4]', c(85, 'xlate')),
  ('B', 'The soft pedal is written u.c., una corda, and let up at t.c. The sustain pedal is written Ped.', c(85, 'xlate2'))]),
 ('Example: which pedal?', [
  ('B', 'Which pedal is Ped.? Which is u.c.? And what does t.c. ask? Pause and think.', c(86, 'ex1')), ('pause', 4, c(86, 'ex1')),
  ('P', 'Ped. is the right pedal, u.c. the left, and t.c. means let the left pedal up.', c(86, 'ex1', reveal=True))]),
 ('Writing the sustain pedal', [
  ('B', 'Down at Ped., up at the star. Or a bracket: the notch is a quick change, up and down again. Heel on the floor, press with the ball of your foot. Play first, then pedal.', c(86, 'xlate'))]),
 ('Example: down and up', [
  ('B', 'Where does the pedal go down, where does it change, and where does it come up?', c(86, 'ex2')), ('pause', 4, c(86, 'ex2')),
  ('P', 'Down on the first C, changed at the F, and up at the end.', c(86, 'ex2', reveal=True)),
  ('piano', 'C4 E4 G4 C5 | F4 A4 C5 F5', c(86, 'ex2', reveal=True))]),
 ('Changing the pedal', [
  ('B', 'At every new chord, change the pedal just after you play it: up, and straight down again. Each chord rings clean, and they still join.', c(87, 'xlate')),
  ('piano', '[C4 E4 G4] [F4 A4 C5] [G4 B4 D5] [C4 E4 G4]', c(87, 'xlate')),
  ('B', 'Try it: play C, E and G together, press the right pedal and take your hands off. The chord keeps sounding. Lift the pedal: silence.', c(87, 'try10')),
  ('B', 'The sustain pedal holds a door open: every note that walks in stays in the room until you let the door shut. Until next time, Clara.', c(87, 'think')), ('P', 'Goodbye!', c(87, 'think'))])])
CH['E4'] = NEW['E4']

NEW['E5'] = ('Ornaments', [
 ('The secret', [
  ('P', 'What is that little tr above the note?', c(88, 'lead')),
  ('B', 'A trill, Clara. An ornament: a small sign that stands for a quick burst of notes around the main note.', c(88, 'hero')),
  ('piano', 'D5/4 E5/4 D5/4 E5/4 D5/4 E5/4 D5/4 E5/4 C5*2', c(88, 'hero')),
  ('B', 'Ornaments borrow the notes next door, one letter up or down. On D, the note above is E and the note below is C.', c(88, 'xlate')),
  ('piano', 'D4 E4 D4 C4 D4', c(88, 'xlate', seq=['main', 'above', 'main', 'below', 'main']))]),
 ('Written and played', [
  ('B', 'A trill goes back and forth with the note above. An upper mordent is one quick flick: note, above, note.', c(88, 'xlate2')),
  ('piano', 'D5/4 E5/4 D5*1.5 C5*2', c(88, 'xlate2')),
  ('B', 'A lower mordent uses the note below. And a turn goes above, note, below, note.', c(89, 'xlate')),
  ('piano', 'D5/4 C5/4 D5*1.5 | E5/4 D5/4 C5/4 D5/4 D5 C5*2', c(89, 'xlate'))]),
 ('Example: a lower mordent on G', [
  ('B', 'A lower mordent on G. Which next-door note does it borrow? Pause and think.', c(89, 'ex1')), ('pause', 3, c(89, 'ex1')),
  ('P', 'The note below G: F. G, F, G!', c(89, 'ex1', reveal=True)),
  ('piano', 'G4/4 F4/4 G4*1.5', c(89, 'ex1', reveal=True))]),
 ('Example: the trill', [
  ('B', 'Which note has the trill, and what is its next-door note above?', c(89, 'ex2')), ('pause', 3, c(89, 'ex2')),
  ('P', 'The E, and the note above is F. E, F, E, F, quickly, for two beats.', c(89, 'ex2', reveal=True)),
  ('B', 'Going further: in music from the time of Bach and Handel, a trill usually starts on the note above. Your teacher will tell you.', c(89, 'xlate2'))]),
 ('Tiny notes', [
  ('B', 'A tiny note before the main note borrows a moment from it. With a slash, it is crushed in as fast as you can: an acciaccatura. Without a slash, it leans, taking about half the time: an appoggiatura.', c(90, 'xlate')),
  ('pause', 3, c(90, 'xlate')),
  ('piano', 'D5/8 C5*2 | D5 C5', c(90, 'xlate')),
  ('B', 'Here the Minuet in G starts with a mordent on the first D: one quick flick, and the beat does not move.', c(90, 'yk')),
  ('piano', 'D5/4 E5/4 D5/2 G4/2 A4/2 B4/2 C5/2 | D5 G4 G4', c(90, 'yk')),
  ('B', 'Learn the plain notes in time first, then add the sparkle. Until next time, Clara.', c(90, 'think')), ('P', 'Goodbye!', c(90, 'think'))])])
CH['E5'] = NEW['E5']
