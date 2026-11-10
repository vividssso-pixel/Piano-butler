# Her 10 Nov ("너무 좋아"): every chapter in the E1 style: relaxed back-and-forth, everyday comparisons, humour,
# a mistake now and then. Exec'd from scripts.py just before the next-lesson questions are added.
H22 = c(22, 'hero'); S22 = c(22, 'secret')
NEW['P1'] = ('The keyboard', [
 ('The secret', [
  ('B', 'Welcome, Clara, to our very first room: the keyboard.', c(22, 'h:The keyboard')),
  ('P', 'Wow. There are so many keys. Do I have to count them all?', H22),
  ('B', 'Eighty-eight of them. And no, you never have to count them. I promise. Counting keys is for people with no imagination.', H22),
  ('P', 'Phew.', H22),
  ('B', 'Let’s start with one fact. Left is low, like a big grumpy bear.', H22), ('piano', 'C2*2', H22),
  ('B', 'And right is high, like a little bird.', H22), ('piano', 'C6*2', H22),
  ('P', 'Bear on the left, bird on the right. Easy!', H22),
  ('B', 'Then let’s test it. Two red keys. Which one sounds higher? Take your time.', c(22, 'ex1')),
  ('pause', 3, c(22, 'ex1')),
  ('P', 'The second one. It’s further to the right, so it’s more of a bird.', c(22, 'ex1', reveal=True)),
  ('piano', 'G4 E5', c(22, 'ex1', reveal=True)),
  ('B', 'A bird it is. Right is always higher, left always lower.', c(22, 'ex1', reveal=True)),
  ('B', 'Now look at the black keys. They come in little groups: two, then three. Two, three, all the way along.', c(22, 'hero', anim='groups')),
  ('P', 'Like bumps on the road!', c(22, 'hero', anim='groups')),
  ('B', 'Bumpy, but very useful. Here is the secret of the whole keyboard. Every group has a first white key, just to its left. Next to the two black keys, it’s C. Next to the three, it’s F.', S22),
  ('P', 'Two black keys, start on C. Three black keys, start on F.', S22),
  ('B', 'Then just walk on. C, D, E, around the two.', H22),
  ('piano', 'C4 D4 E4', c(22, 'hero', seq=['C', 'D', 'E'])),
  ('B', 'F, G, A, B, around the three.', H22),
  ('piano', 'F4 G4 A4 B4', c(22, 'hero', seq=['F', 'G', 'A', 'B'])),
  ('B', 'And the pattern repeats all the way along, like the houses on a street: two, three, two, three. Every two starts on C, every three on F.', c(23, 'xlate')),
  ('piano', 'C3 F3 C4 F4 C5 F5', c(23, 'xlate', seq=['#0', '#1', '#2', '#3', '#4', '#5'])),
  ('P', 'So wherever I am, I find a group, and I know my address.', c(23, 'xlate'))]),
 ('Round and round', [
  ('P', 'Butler, what comes after G? H?', c(23, 'xlate2')),
  ('B', 'No H at all, I’m afraid. The white keys only use seven letters, A to G. After G, it’s A again. Like the days of the week: after Sunday, Monday comes round again, whether you like it or not.', c(23, 'xlate2')),
  ('piano', 'A3 B3 C4 D4 E4 F4 G4 A4 B4 C5 D5 E5 F5 G5 A5', c(23, 'xlate2', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12', '#13', '#14'])),
  ('P', 'A B C D E F G, then A again. Seven letters, round and round, like a merry-go-round.', c(23, 'xlate2')),
  ('B', 'And notice two pairs of white keys that touch, with no black key between: E and F, and B and C. Best friends, those four.', c(23, 'xlate3'))]),
 ('Backwards', [
  ('B', 'Now walk the other way, Clara. Left, down the keyboard. The letters run backwards.', c(24, 'xlate')),
  ('piano', 'A4 G4 F4 E4 D4 C4 B3 A3', c(24, 'xlate', seq=['1', '2', '3', '4', '5', '6', '7', '8'])),
  ('P', 'A, G, F, E, D, C, B, A. Ooh, that’s harder. My brain is going the wrong way.', c(24, 'xlate')),
  ('B', 'It’s like saying the alphabet backwards. Strange at first. But music goes down as often as it goes up, so practise it until backwards is as quick as forwards. Then reading new music gets much, much easier.', c(24, 'xlate'))]),
 ('Example: walk down from E', [
  ('B', 'Start on E and walk left, one white key at a time. Name each key as you go.', c(24, 'ex2')),
  ('pause', 4, c(24, 'ex2')),
  ('P', 'E, D, C, B, A!', c(24, 'ex2', reveal=True)),
  ('piano', 'E4 D4 C4 B3 A3', c(24, 'ex2', reveal=True)),
  ('B', 'Now a harder one. Fill the gaps out loud: G, something, E, something, C.', c(24, 'ex2', reveal=True)),
  ('pause', 3, c(24, 'ex2', reveal=True)),
  ('P', 'G, F, E, D, C. Done!', c(24, 'ex2', reveal=True))]),
 ('The two ends', [
  ('B', 'Now let’s visit the two ends of the piano. The very first key, bottom left, is an A. Look at the black keys there: only one, all on its own.', c(24, 'xlate2')),
  ('P', 'Only one? But the groups are two or three. Poor thing.', c(24, 'xlate2')),
  ('B', 'Well spotted. It’s a group of three that has been chopped off, like the end of a loaf of bread. Only its last bit is left: A and B. Then comes the first full group of two, and its first key is Lowest C.', c(24, 'xlate2')),
  ('piano', 'A0 B0 C1', c(24, 'xlate2', seq=['#0', '#1', 'Lowest C'])),
  ('B', 'At the top, the very last key has no black key after it at all. Look left: the last group is a group of three black keys, with F, G, A, B around it.', c(24, 'xlate2')),
  ('P', 'And after B comes... C!', c(24, 'xlate2')),
  ('B', 'Exactly. The first key of a group of two that the piano maker never finished. So the last key is a C: Highest C.', c(24, 'xlate2')),
  ('piano', 'F7 G7 A7 B7 C8', c(24, 'xlate2', seq=['#5', '#6', '#7', '#8', 'Highest C']))]),
 ('The eight Cs', [
  ('B', 'Count the Cs from the bottom and there are eight, like eight brothers and sisters. The one nearest the middle is the most famous: Middle C.', c(25, 'xlate')),
  ('piano', 'C4', c(25, 'xlate', seq=['Middle C'])),
  ('B', 'One C lower is Bass C. One higher is Treble C. Further out, Low C and High C.', c(25, 'xlate')),
  ('piano', 'C2 C3 C4 C5 C6', c(25, 'xlate', seq=['Low C', 'Bass C', 'Middle C', 'Treble C', 'High C'])),
  ('P', 'And the ones right at the ends?', c(25, 'xlate')),
  ('B', 'At the bottom, Lowest C. At the top, Very High C, and then Highest C, the very last key, the baby of the family.', c(25, 'xlate')),
  ('piano', 'C1 C7 C8', c(25, 'xlate', seq=['Lowest C', 'Very High C', 'Highest C'])),
  ('P', 'Eight Cs! But I’ll mostly use the five in the middle.', c(25, 'xlate')),
  ('B', 'Very sensible. Theory books and apps give them numbers instead, C1 to C8, with Middle C as C4. And from one C to the next is an octave: eight notes, both Cs counted.', c(25, 'xlate'))]),
 ('Example: Bass C and Treble C', [
  ('B', 'Now find Bass C and Treble C, starting from Middle C.', c(25, 'ex3')),
  ('pause', 4, c(25, 'ex3')),
  ('P', 'Walk left to the next pair of black keys: the C just left of it is Bass C. Walk right the same way: Treble C.', c(25, 'ex3', reveal=True)),
  ('piano', 'C3 C4 C5', c(25, 'ex3', reveal=True)),
  ('B', 'Lovely. Each one is an octave from Middle C, eight notes away. Next-door neighbours, one street over.', c(25, 'ex3', reveal=True))]),
 ('Example: three keys', [
  ('B', 'Three numbered keys. Name each one. And remember: no counting from the bottom.', c(26, 'ex4')),
  ('P', 'Number one is with the three black keys, so its family is F G A B. Start on F and walk on: F, G, A, B. It’s the last one.', c(26, 'ex4')),
  ('B', 'And the other two?', c(26, 'ex4')),
  ('pause', 4, c(26, 'ex4')),
  ('P', 'One is B. Two sits just right of the two black keys, the last of C D E, so E. And three is one key after F: G!', c(26, 'ex4', reveal=True)),
  ('piano', 'B4 E4 G4', c(26, 'ex4', reveal=True)),
  ('B', 'Find the group, find its first key, walk on. No counting from far away. You’re a keyboard detective now.', c(26, 'ex4', reveal=True))]),
 ('Try it', [
  ('B', 'Before you go, a tune with no white keys at all. Right hand, fingers two, three and four, on a group of three black keys.', c(26, 'yk')),
  ('P', 'Ready.', c(26, 'yk')),
  ('B', 'Four, three, two. Four, three, two. Then lots of quick ones: two two two two, three three three three. And four, three, two.', c(26, 'yk')),
  ('piano', 'A#4 G#4 F#4*2 | A#4 G#4 F#4*2 | F#4/2 F#4/2 F#4/2 F#4/2 G#4/2 G#4/2 G#4/2 G#4/2 | A#4 G#4 F#4*2', c(26, 'yk')),
  ('P', 'Hot Cross Buns! Now I’m hungry.', c(26, 'yk')),
  ('B', 'Your mission: close your eyes and slide your hand along the keys. Two bumps, the key on their left is C. Three bumps, it’s F. Like reading in the dark. Until next time, Clara.', c(26, 'think')),
  ('P', 'Bye, Butler!', c(26, 'think'))])])

NEW['P2'] = ('The staff and the clefs', [
 ('The secret', [
  ('P', 'Butler, my piece looks like a ladder fell over with lots of blobs on it.', c(27, 'lead')),
  ('B', 'Ha! That ladder is called a staff: five lines and four spaces, counted from the bottom, like floors in a building.', c(27, 'xlate', anim='lines')),
  ('P', 'And higher up the staff means higher on the piano?', c(27, 'lead')),
  ('B', 'Always. Top floor, high notes. But five lines alone don’t tell us which notes. For that we need a clef. Think of it as the key to the code.', c(27, 'hero')),
  ('B', 'And now, as promised, may I present Their Majesties, who rule these two staves.', c(27, 'hero')),
  ('Q', 'Good day, Clara. I am the Queen of the treble staff. See how my clef curls round line two, like a ribbon? That line is my G, which is why my clef is also called the G clef.', c(27, 'hero')),
  ('piano', 'G4*2', c(27, 'hero', seq=['G'])),
  ('P', 'Oh! Hello, Your Majesty.', c(27, 'hero')),
  ('K', 'And I am the King of the bass staff. My clef’s two dots hug line four, like a pair of eyes. That line is my F, so my clef is the F clef. The low notes are my kingdom.', c(27, 'hero')),
  ('piano', 'F3*2', c(27, 'hero', seq=['F'])),
  ('P', 'A Queen for the high notes and a King for the low ones! The treble clef curls round G. The bass clef’s dots hug F.', c(27, 'secret')),
  ('B', 'Perfectly put. Their Majesties are very pleased.', c(27, 'secret'))]),
 ('The grand staff', [
  ('B', 'Piano music joins the two staves with a curly brace, like two rooms with a door between them. The treble staff on top, usually for the right hand. The bass staff below, usually for the left.', c(28, 'xlate')),
  ('B', 'And Middle C sits right between them, on a little line of its own. It can be written in either staff. Same key.', c(28, 'xlate')),
  ('piano', 'C4*2', c(28, 'xlate')),
  ('Q', 'Middle C is the border between our two kingdoms.', c(28, 'xlate')),
  ('K', 'And we share it. Most of the time without arguing.', c(28, 'xlate')),
  ('Q', 'Most of the time.', c(28, 'xlate'))]),
 ('Example: which staff?', [
  ('B', 'Here is a key on the piano. Which staff would it be written on?', c(28, 'ex1', show=['Middle C'])),
  ('P', 'First I find Middle C. The question mark is to its left.', c(28, 'ex1', show=['Middle C'], lab=['Middle C'])),
  ('B', 'Left is lower. And low keys go on which staff?', c(28, 'ex1', show=['Middle C'], lab=['?'])),
  ('pause', 3, c(28, 'ex1', show=['Middle C'], lab=['?'])),
  ('P', 'The King’s staff! The bass staff, usually for the left hand.', c(28, 'ex1', reveal=True)),
  ('K', 'Welcome to my kingdom.', c(28, 'ex1', reveal=True))]),
 ('Try it', [
  ('B', 'Point to the line the treble clef curls round, and play that G. Then the line between the bass clef’s eyes, and play that F. Middle C sits between them.', c(28, 'yk')),
  ('pause', 4, c(28, 'yk')),
  ('piano', 'G4 F3 C4', c(28, 'yk')),
  ('B', 'And a tune you know. Twinkle, Twinkle leaps up to G, the Queen’s very own line.', c(28, 'yk')),
  ('piano', 'C4 C4 G4 G4 A4 A4 G4*2', c(28, 'yk', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6'])),
  ('Q', 'One of my favourites.', c(28, 'yk')),
  ('B', 'A clef is a pair of glasses. Look: the very same note on the bottom line. Through treble glasses it’s E. Through bass glasses it’s G. Always put your glasses on first. Until next time, Clara.', c(28, 'think', anim='glasses')),
  ('P', 'Bye, Butler! Bye, Your Majesties!', c(28, 'think'))])])

NEW['P3'] = ('The staff and the keyboard', [
 ('The secret', [
  ('P', 'Butler, how do the lines on the page turn into keys on the piano?', c(29, 'secret')),
  ('B', 'Here is the secret of this chapter, Clara. Every line and every space of the staff is one white key, in order. No skipping, no cheating.', c(29, 'secret')),
  ('P', 'So climbing the staff is climbing the keyboard?', c(29, 'vx')),
  ('B', 'Exactly, like a staircase lying on its side. Here are two octaves, from Bass C up to Treble C, with Middle C where the two staves meet.', c(29, 'vx')),
  ('piano', 'C3 D3 E3 F3 G3 A3 B3 C4 D4 E4 F4 G4 A4 B4 C5', c(29, 'vx', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12', '#13', '#14'])),
  ('B', 'One step on the staff, from a line to the space right next to it, is the very next white key. Up the staff is to the right. Down is to the left.', c(29, 'p2')),
  ('B', 'The black keys live in between. How they’re written comes a little later, in chapter six.', c(29, 'p'))]),
 ('Example: from the page to the key', [
  ('B', 'A note on line four of the bass staff. Which key is it?', c(30, 'ex1', show=['Middle C'])),
  ('P', 'Line four, between the King’s two eyes: F.', c(30, 'ex1', show=['Middle C', 'F'], lab=['F'])),
  ('B', 'And where is it on the piano?', c(30, 'ex1', show=['Middle C', 'F'])),
  ('pause', 3, c(30, 'ex1', show=['Middle C', 'F'])),
  ('P', 'The three black keys just below Middle C. F is the first key of that family.', c(30, 'ex1', reveal=True)),
  ('piano', 'F3*2', c(30, 'ex1', reveal=True)),
  ('K', 'My favourite F.', c(30, 'ex1', reveal=True))]),
 ('Example: mirror notes', [
  ('B', 'Now something rather lovely. Find treble G and bass F on the piano.', c(30, 'ex2', show=['Middle C'])),
  ('P', 'Treble G: the second white key of the group of three black keys just above Middle C. Bass F: the first white key of the group just below.', c(30, 'ex2', show=['Middle C'])),
  ('B', 'Now count each one from Middle C. Up to G, down to F.', c(30, 'ex2', show=['Middle C'])),
  ('pause', 4, c(30, 'ex2', show=['Middle C'])),
  ('P', 'C D E F G, five. C B A G F, five as well!', c(30, 'ex2', reveal=True)),
  ('piano', 'C4 D4 E4 F4 G4 | C4 B3 A3 G3 F3', c(30, 'ex2', reveal=True)),
  ('B', 'Mirror images. Fold the grand staff at Middle C, like folding a painting in half to make a butterfly, and treble G lands exactly on bass F.', c(30, 'ex2', reveal=True, mirror='GF')),
  ('Q', 'My G and the King’s F: the same distance up and down.', c(30, 'ex2', reveal=True, mirror='GF')),
  ('K', 'Two guards at the castle gate, with Middle C between us.', c(30, 'ex2', reveal=True, mirror='GF'))]),
 ('Example: from the key to the page', [
  ('B', 'Now the other way round. I play the third white key up from Middle C.', c(31, 'ex3', show=['Middle C'])),
  ('piano', 'C4 D4 E4', c(31, 'ex3', seq=['Middle C', '', '?'], show=['Middle C'])),
  ('P', 'C one, D two, E three. It’s E.', c(31, 'ex3', lab=['?'], show=['Middle C'])),
  ('B', 'And on the staff? Climb the same way.', c(31, 'ex3', show=['Middle C'])),
  ('P', 'Middle C on its little line, D hanging just under the staff, E on the bottom line.', c(31, 'ex3', reveal=True)),
  ('B', 'Precisely. Three steps up the staircase.', c(31, 'ex3', reveal=True))]),
 ('Try it', [
  ('B', 'Play Middle C and walk up the white keys, saying each name. Picture each one climbing the staff: line, space, line, space.', c(30, 'try10')),
  ('piano', 'C4 D4 E4 F4 G4 A4 B4 C5', c(30, 'try10', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7'])),
  ('B', 'Then Frère Jacques in both hands. The right hand plays C D E C, and the left hand copies it an octave lower, in the King’s staff.', c(31, 'yk')),
  ('piano', 'C4 D4 E4 C4 | C3 D3 E3 C3', c(31, 'yk', seq=['#0', '#1', '#2', '#3', '#0', '#1', '#2', '#3'])),
  ('P', 'It’s like an echo from the cellar!', c(31, 'yk')),
  ('B', 'The staff is a ladder laid beside the keyboard: every rung is the next white key. Until next time, Clara.', c(31, 'think')),
  ('P', 'Bye, Butler!', c(31, 'think'))])])

NEW['P4'] = ('Reading the notes', [
 ('The secret', [
  ('P', 'Butler, do I have to learn every line and space by heart? That’s like memorising a phone book.', c(32, 'lead')),
  ('B', 'Not at once, Clara. When you walk into a new town, you don’t learn every house. You find a few landmarks. Here are ours: Middle C in the middle, treble G and bass F either side.', c(32, 'hero', lab=['#19', '#2', '#15'])),
  ('piano', 'C4 G4 F3', c(32, 'hero', seq=['#19', '#2', '#15'])),
  ('B', 'From there, every line and space is simply the next letter. Listen to the whole staircase, from bass G all the way to treble F.', c(32, 'hero')),
  ('piano', 'G2/2 A2/2 B2/2 C3/2 D3/2 E3/2 F3/2 G3/2 A3/2 B3/2 C4/2 D4/2 E4/2 F4/2 G4/2 A4/2 B4/2 C5/2 D5/2 E5/2 F5/2', c(32, 'hero', seq=['#9', '#10', '#11', '#12', '#13', '#14', '#15', '#16', '#17', '#18', '#19', '#20', '#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8'])),
  ('P', 'Whee! Like a lift going up. And how do I move from a landmark?', c(32, 'xlate')),
  ('B', 'Two ways: step or skip. A step goes to the very next line or space, one letter on, like walking up one stair. A skip goes line to line, or space to space: two letters on, like taking the stairs two at a time when you’re late for dinner.', c(32, 'xlate', anim='stepskip')),
  ('piano', 'G4 A4 | G4 B4', c(32, 'xlate'))]),
 ('Words to remember', [
  ('B', 'First, two kinds of note. A line note has a line running right through its middle, like a kebab. A space note sits between two lines, touching both, like a sandwich filling.', c(33, 'xlate2')),
  ('P', 'Now I’m hungry again.', c(33, 'xlate2')),
  ('B', 'Lines and spaces are counted from the bottom. Treble lines first. Line one, E. Line two, G. Line three, B. Line four, D. Line five, F.', c(33, 'xlate3', lens='tl')),
  ('Q', 'In my staff we say: Every Good Boy Deserves Fun.', c(33, 'xlate3', lens='tl')),
  ('B', 'The four treble spaces, from the bottom: F, A, C, E.', c(33, 'xlate3', lens='ts')),
  ('Q', 'And my spaces spell face. As in, the face you make when you get it right.', c(33, 'xlate3', lens='ts')),
  ('B', 'Now the bass staff. Bass lines, from the bottom: G, B, D, F, A.', c(33, 'xlate3', lens='bl')),
  ('K', 'In my kingdom: Great Big Dragons Fly Away!', c(33, 'xlate3', lens='bl')),
  ('B', 'Last, the bass spaces: A, C, E, G.', c(33, 'xlate3', lens='bs')),
  ('K', 'My spaces: All Cows Eat Grass.', c(33, 'xlate3', lens='bs')),
  ('P', 'Dragons and cows. Your kingdom is very busy, Your Majesty.', c(33, 'xlate3')),
  ('K', 'You have no idea. The dragons keep eating the cows’ grass.', c(33, 'xlate3'))]),
 ('Example: read from the clef note', [
  ('B', 'A treble note you’re not sure of, on line four. Don’t panic. Start from a landmark: the clef note.', c(34, 'ex1')),
  ('P', 'G is line two. Skip up to line three: B. Skip again to line four.', c(34, 'ex1')),
  ('pause', 3, c(34, 'ex1')),
  ('P', 'D!', c(34, 'ex1', reveal=True)),
  ('piano', 'G4 B4 D5', c(34, 'ex1', reveal=True)),
  ('B', 'G, B, D: two skips up from the clef’s G. Two stairs at a time, and you’re there.', c(34, 'ex1', reveal=True))]),
 ('Example: a bass note', [
  ('B', 'Now down into the King’s cellar. Bass staff, line three.', c(34, 'ex1', show=[])),
  ('P', 'The dots hug line four: F. Step down to the space: E. Step down again to line three.', c(34, 'ex1', show=['F', 'E'])),
  ('piano', 'F3 E3', c(34, 'ex1', seq=['F', 'E'], show=['F', 'E'])),
  ('pause', 3, c(34, 'ex1', show=['F', 'E'], lab=['?'])),
  ('P', 'D.', c(34, 'ex1', lab=['?'], reveal=True)),
  ('piano', 'F3 E3 D3', c(34, 'ex1', seq=['F', 'E', '?'], reveal=True)),
  ('B', 'Correct. F, E, D: walking backwards down the alphabet, nice and calm.', c(34, 'ex1', reveal=True))]),
 ('Example: one line, two notes', [
  ('B', 'Here is a sneaky puzzle. Two red notes, both on the bottom line: one in the treble staff, one in the bass. Same line. Same note?', c(34, 'ex2')),
  ('P', 'Hmm. Same line, same note? Sounds fair.', c(34, 'ex2')),
  ('B', 'Read each one from its own clef. Pause and try.', c(34, 'ex2')),
  ('pause', 4, c(34, 'ex2')),
  ('P', 'Treble: G is line two. Step down, F in the space, then the bottom line is E.', c(34, 'ex2', lab=['#0'])),
  ('piano', 'E4', c(34, 'ex2', seq=['#0'])),
  ('B', 'And the bass? F is line four. Step down line by line.', c(34, 'ex2')),
  ('P', 'Then the bass one is E too! Every Good Boy.', c(34, 'ex2', oops=True)),
  ('B', 'Ah, you walked right into the trap, Clara. That sentence lives in the Queen’s house, not the King’s. Look at the clef first.', c(34, 'ex2')),
  ('P', 'Oops. Wrong house. F, D, B, G. The bottom line is G!', c(34, 'ex2', lab=['#1'], reveal=True)),
  ('piano', 'G2', c(34, 'ex2', seq=['#1'], reveal=True)),
  ('B', 'Same line, different note. It’s like the word “bat”: a cricket bat or a flying bat? You need to know where you are. So: glasses on, clef first.', c(34, 'ex2', reveal=True, anim='glasses'))]),
 ('Example: read it downwards', [
  ('B', 'Now let’s read downhill, Clara. Start on G, the clef note, and step down to Middle C. Each step down is the letter before. Pause and say them.', c(34, 'ex3', show=['G', 'steps down', 'skips down (the lines)'])),
  ('pause', 4, c(34, 'ex3', show=['G', 'steps down', 'skips down (the lines)'])),
  ('P', 'G, F, E, D, C!', c(34, 'ex3', reveal=True)),
  ('piano', 'G4 F4 E4 D4 C4', c(34, 'ex3', seq=['G', '#1', '#2', '#3', '#4'], reveal=True)),
  ('B', 'The alphabet backwards, without even blinking. Now skip down the lines from F, the top line: two letters back each time.', c(34, 'ex3', reveal=True)),
  ('pause', 3, c(34, 'ex3', reveal=True)),
  ('P', 'F, D, B, G, E!', c(34, 'ex3', reveal=True)),
  ('piano', 'F5 D5 B4 G4 E4', c(34, 'ex3', seq=['F', '#7', '#8', '#9', '#10'], reveal=True)),
  ('B', 'Every Good Boy Deserves Fun, backwards. That sounds like a spell from a wizard school. Read downwards this quickly, and new music won’t scare you at all.', c(34, 'ex3', reveal=True))]),
 ('Example: Treble C and Bass C', [
  ('B', 'Let’s find Treble C on the staff. Hint: it lives in a space.', c(35, 'ex4')),
  ('P', 'The treble spaces spell face. F, A, and space three is C!', c(35, 'ex4', lab=['?'], reveal=True)),
  ('piano', 'F4 A4 C5', c(35, 'ex4', reveal=True)),
  ('B', 'Treble C, one octave above Middle C. And in the bass spaces?', c(35, 'ex4')),
  ('P', 'All Cows. Space two is C: Bass C!', c(35, 'ex4', lab=['?'], reveal=True)),
  ('piano', 'A2 C3', c(35, 'ex4', reveal=True)),
  ('B', 'One octave below Middle C. The cows are very proud of you.', c(35, 'ex4', reveal=True))]),
 ('Try it', [
  ('B', 'So, to read a new note, make three moves. Look at the clef. Find the nearest landmark, or use the sentence. Then step or skip to it, say it, and play it.', c(33, 'xlate')),
  ('B', 'Mary Had a Little Lamb. E, D, C: line, space, and Middle C’s own little line, one step down each time.', c(35, 'yk')),
  ('piano', 'E4 D4 C4 D4 E4 E4 E4*2', c(35, 'yk', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6'])),
  ('P', 'The lamb walks downstairs and back up again.', c(35, 'yk')),
  ('B', 'Your mission: in a piece you play, find the landmarks first, then step or skip from them. Landmarks are lamp posts on a dark road. Until next time, Clara.', c(35, 'think')),
  ('P', 'Bye, Butler!', c(35, 'think'))])])

NEW['P5'] = ('Ledger lines', [
 ('The secret', [
  ('P', 'Butler, this note is floating outside the staff! Did it escape?', c(36, 'lead')),
  ('B', 'Ha! Some notes are simply too high or too low to fit. So we give them short extra lines of their own, called ledger lines. Think of them as little balconies built onto the side of the house.', c(36, 'lead')),
  ('B', 'They’re spaced just like the staff lines. And the most famous balcony note of all is Middle C. In the treble staff it hangs on the first ledger line below. In the bass staff it sits on the first ledger line above.', c(36, 'hero')),
  ('P', 'Two different places on the page, but the same key?', c(36, 'hero', lab=['Middle C'])),
  ('piano', 'C4', c(36, 'hero', seq=['Middle C'])),
  ('Q', 'In my staff, Middle C hangs on the first ledger line below.', c(36, 'hero')),
  ('K', 'In mine it sits on the first ledger line above. One key, and we both may write it.', c(36, 'hero')),
  ('Q', 'We take turns. Like sharing a bicycle.', c(36, 'hero')),
  ('B', 'Very civilised. The right hand usually reads it in the treble, the left hand in the bass.', c(36, 'hero'))]),
 ('Below and above the staff', [
  ('B', 'To read a ledger note, step out from the staff, one letter at a time. Treble, below the staff: C on the first ledger line, B under it, A on the second ledger line.', c(36, 'xlate', lens='tb')),
  ('piano', 'C4 B3 A3', c(36, 'xlate', lens='tb')),
  ('B', 'Then above the treble staff: A on the first ledger line, B over it, C on the second.', c(36, 'xlate', lens='ta')),
  ('piano', 'A5 B5 C6', c(36, 'xlate', lens='ta')),
  ('B', 'In the bass, below the staff: E on the first ledger line, D under it, C on the second.', c(37, 'xlate', lens='bb')),
  ('piano', 'E2 D2 C2', c(37, 'xlate', lens='bb')),
  ('B', 'And above the bass staff: C on the first ledger line, then D, then E on the second.', c(37, 'xlate', lens='ba')),
  ('piano', 'C4 D4 E4', c(37, 'xlate', lens='ba')),
  ('P', 'It’s like going down the ladder into a swimming pool. One rung at a time.', c(36, 'xlate')),
  ('B', 'Exactly, and never jump. Count ledger lines from the staff outwards: the first one is the one nearest the staff. Never skip a rung.', c(36, 'xlate'))]),
 ('Example: a high note', [
  ('B', 'Up to the attic. A high note on ledger lines. Start from the top line of the treble staff: F.', c(37, 'ex1', show=['F'], lab=['F'])),
  ('P', 'Then G on top of the staff, A on the first ledger line, B above it.', c(37, 'ex1', show=['F', 'G', 'A', 'B'])),
  ('piano', 'F5 G5 A5 B5', c(37, 'ex1', seq=['F', 'G', 'A', 'B'], show=['F', 'G', 'A', 'B'])),
  ('B', 'And the red note, on the second ledger line? Pause and try.', c(37, 'ex1', show=['F', 'G', 'A', 'B'], lab=['?'])),
  ('pause', 3, c(37, 'ex1', show=['F', 'G', 'A', 'B'], lab=['?'])),
  ('P', 'C! High C. Up where the birds live.', c(37, 'ex1', lab=['?'], reveal=True)),
  ('piano', 'C6', c(37, 'ex1', seq=['?'], reveal=True))]),
 ('Example: a low note', [
  ('B', 'And now down to the basement. A low note under the bass staff. Start from the bottom line: G.', c(37, 'ex2', show=['G'], lab=['G'])),
  ('P', 'Step down: F in the space below, E on the first ledger line, D under it.', c(37, 'ex2', show=['G', 'F', 'E', 'D'])),
  ('piano', 'G2 F2 E2 D2', c(37, 'ex2', seq=['G', 'F', 'E', 'D'], show=['G', 'F', 'E', 'D'])),
  ('B', 'And the red note, on the second ledger line? Pause and try.', c(37, 'ex2', show=['G', 'F', 'E', 'D'], lab=['?'])),
  ('pause', 3, c(37, 'ex2', show=['G', 'F', 'E', 'D'], lab=['?'])),
  ('P', 'C! Low C, two octaves below Middle C. Grumpy bear territory.', c(37, 'ex2', lab=['?'], reveal=True)),
  ('piano', 'C2', c(37, 'ex2', seq=['?'], reveal=True)),
  ('B', 'And look: Low C is the mirror of High C. Fold the grand staff at Middle C, and two ledger lines above the treble land right on two ledger lines below the bass.', c(37, 'ex2', reveal=True, mirror='CC'))]),
 ('The four first ledger lines', [
  ('B', 'One small warning. Not every first ledger line is a C. Above the treble staff the first ledger line is A. Below the bass staff it is E. Only Middle C belongs to both staves.', c(38, 'xlate')),
  ('P', 'So I can’t just guess C every time a balcony shows up.', c(38, 'xlate')),
  ('B', 'Guessing is how people end up in the wrong flat. Count from the staff.', c(38, 'xlate'))]),
 ('Try it', [
  ('B', 'And when notes climb even higher, music often writes them lower, with an ottava sign and a dotted line above them. It means: play those notes one octave higher, until the dotted line stops.', c(38, 'xlate2')),
  ('P', 'So the composer saves on balconies.', c(38, 'xlate2')),
  ('B', 'Precisely. Ledger lines are the staff’s ladder carried on past its ends: the same rungs, just shorter. Until next time, Clara.', c(38, 'think')),
  ('P', 'Bye, Butler!', c(38, 'think'))])])

NEW['P6'] = ('Sharps, flats and naturals', [
 ('The secret', [
  ('P', 'Butler, what are those little signs in front of some notes? This one looks like a noughts-and-crosses board.', c(39, 'lead')),
  ('B', 'That’s a sharp, Clara, and you’re not the first to say so. These signs move a note to the very next key. A sharp: one key to the right, a semitone higher. A flat: one key to the left, a semitone lower.', c(39, 'secret', anim='sharpflat')),
  ('P', 'Sharp goes up, like a pin poking you. Flat goes down, like a punctured tyre.', c(39, 'secret', anim='sharpflat')),
  ('B', 'I couldn’t have put it better. Usually that next key is black, and that’s how the black keys get their names. D sharp is just right of D. D flat is just left of it.', c(39, 'hero')),
  ('piano', 'D4 D#4 | D4 Db4', c(39, 'hero', seq=['D', 'D♯', 'D', 'D♭'])),
  ('B', 'And a natural cancels a sharp or a flat: back to the plain white key. It’s the undo button.', c(39, 'ht')),
  ('B', 'Now, where there’s no black key in between, a sharp or flat lands on a white key: E sharp is F, B sharp is C, F flat is E, and C flat is B.', c(39, 'xlate')),
  ('P', 'So E sharp is really F wearing a disguise.', c(39, 'xlate')),
  ('B', 'A very thin disguise. And one rule to remember: a sign belongs to one line or space. It changes only that line or space, in that octave, and only until the bar line. The same letter in another octave stays as it is.', c(40, 'xlate'))]),
 ('Two names for every black key', [
  ('B', 'Now, Clara, something we skipped in chapter one. The white keys have letters. But the black keys have no letters of their own. So what are they called?', c(39, 'hero')),
  ('P', 'Um. Blacky One, Blacky Two?', c(39, 'hero')),
  ('B', 'Ha! Close, but no. They borrow their names from their white neighbours. Think of a house on a street corner: it sits on two streets, so it has two addresses. Take the black key between C and D. Coming from C, it is one key to the right: C sharp. Coming from D, it is one key to the left: D flat.', c(39, 'hero')),
  ('piano', 'C4 C#4 | D4 Db4', c(39, 'hero')),
  ('P', 'C sharp and D flat. The same key, with two names!', c(39, 'hero')),
  ('B', 'Exactly. Let’s name all five, from left to right. Listen and look. C sharp, or D flat. D sharp, or E flat. F sharp, or G flat. G sharp, or A flat. And A sharp, or B flat.', c(39, 'hero', anim='blacknames')),
  ('piano', 'C#4*2 D#4*2 | F#4*2 G#4*2 A#4*2', c(39, 'hero', anim='blacknames')),
  ('P', 'Five black keys, ten names. That’s a lot of names.', c(39, 'hero', anim='blacknames')),
  ('B', 'It is. But you only need one trick: the sharp name comes from the white key on the left, and the flat name from the white key on the right. Same key, two names, like you being Clara at school and sweetie pie at Grandma’s.', c(39, 'hero', anim='blacknames')),
  ('P', 'Butler! Don’t tell anyone.', c(39, 'hero', anim='blacknames')),
  ('B', 'Your secret is safe with me. Which name do you use? Whichever one the music writes. And musicians have a grand word for two names on one key: enharmonic. You’ll hear it again in a moment.', c(39, 'hero', anim='blacknames'))]),
 ('Example: find F sharp', [
  ('B', 'Find F sharp, Clara.', c(40, 'ex1', show=[])),
  ('P', 'F is just left of the three black keys.', c(40, 'ex1', show=['F'], lab=['F'])),
  ('B', 'Sharp means right: the very next key. Black or white? Pause and put your finger on it.', c(40, 'ex1', show=['F'], lab=['?'])),
  ('pause', 3, c(40, 'ex1', show=['F'], lab=['?'])),
  ('P', 'Black! The first black key of the three.', c(40, 'ex1', lab=['?'], reveal=True)),
  ('piano', 'F4 F#4', c(40, 'ex1', seq=['F', '?'], reveal=True)),
  ('B', 'Correct: F sharp. One little hop to the right.', c(40, 'ex1', reveal=True))]),
 ('Example: find B flat', [
  ('B', 'Now B flat.', c(40, 'ex1', show=[])),
  ('P', 'B is just right of the three black keys. Flat means left.', c(40, 'ex1', show=['B'], lab=['B'])),
  ('pause', 3, c(40, 'ex1', show=['B'], lab=['?'])),
  ('P', 'The top black key of the group!', c(40, 'ex1', lab=['?'], reveal=True)),
  ('piano', 'B4 Bb4', c(40, 'ex1', seq=['B', '?'], reveal=True)),
  ('B', 'Splendid. Flat tyre, one step down.', c(40, 'ex1', reveal=True))]),
 ('Example: how long does a sign last?', [
  ('B', 'There’s a sharp sign on the first note of a bar: F sharp. Later in the same bar, the same note with no sign. Sharp or not?', c(40, 'ex2', show=['F♯', 'G'], lab=['F♯'])),
  ('pause', 3, c(40, 'ex2', show=['F♯', 'G'])),
  ('P', 'Still sharp?', c(40, 'ex2', show=['F♯', 'G'])),
  ('B', 'Yes, until the bar line. And after the bar line?', c(40, 'ex2', show=['F♯', 'G'])),
  ('P', 'Still F sharp. The sign is right there.', c(40, 'ex2', oops=True)),
  ('B', 'Ah, that one catches everybody. Think of a sign as a sticky note: it falls off at the bar line. Which side of the bar line is this F?', c(40, 'ex2')),
  ('P', 'The other side. Plain F again!', c(40, 'ex2', reveal=True)),
  ('B', 'Now a natural. B, then B flat, and it stays flat for the rest of the bar. Then a natural sign. What does it do?', c(41, 'ex3', show=['B', 'B♭'])),
  ('pause', 3, c(41, 'ex3', show=['B', 'B♭'])),
  ('P', 'It presses undo: back to the white key B.', c(41, 'ex3', lab=['?'], reveal=True)),
  ('piano', 'B4 Bb4 Bb4 B4', c(41, 'ex3', seq=['#0', '#1', '#2', '#3'], reveal=True))]),
 ('Example: one key, two names', [
  ('B', 'One more. F sharp, then G flat. Find both on the keyboard.', c(41, 'ex4', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'])),
  ('P', 'Wait. They’re the same black key!', c(41, 'ex4', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], lab=['F♯', 'G♭'])),
  ('piano', 'F#4 Gb4', c(41, 'ex4', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], seq=['F♯', 'G♭'])),
  ('B', 'Same sound, two names, like a girl called Elizabeth whose friends call her Lizzie. Remember the grand word? Enharmonic. And E sharp, one key right of E?', c(41, 'ex4', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'], lab=['E♯'])),
  ('pause', 3, c(41, 'ex4', show=['F♯', 'G♭', 'C♯', 'D♭', 'E♯'])),
  ('P', 'There’s no black key there. So E sharp is the white key F, in its disguise!', c(41, 'ex4', reveal=True)),
  ('piano', 'E4 F4', c(41, 'ex4', reveal=True))]),
 ('Try it', [
  ('B', 'Now a famous one. Beethoven’s Für Elise begins on E and the black key just left of it: D sharp. Back and forth, like a nervous knock at the door.', c(41, 'yk')),
  ('piano', 'E5/2 D#5/2 E5/2 D#5/2 E5/2 B4/2 D5/2 C5/2 A4*2', c(41, 'yk')),
  ('B', 'Look closely: the sharp is written again in the new bar, because the bar line wiped it out. And later the D has a natural sign, so it’s plain D again.', c(41, 'yk')),
  ('P', 'The sticky note fell off, and then Beethoven pressed undo.', c(41, 'yk')),
  ('B', 'Your mission: play E and D sharp back and forth, then find F sharp and B flat in three different places on the piano. Until next time, Clara.', c(41, 'think')),
  ('P', 'Bye, Butler!', c(41, 'think'))])])

NEW['P7'] = ('Counting intervals', [
 ('The secret', [
  ('B', 'Clara, today we measure distances. The smallest step on the piano is a semitone: from one key to the very next key, black or white, with nothing in between. Next-door neighbours.', c(42, 'hero')),
  ('piano', 'E4 F4', c(42, 'hero', seq=['#0', '#1'])),
  ('P', 'E to F has no black key between. A semitone.', c(42, 'hero')),
  ('B', 'Two semitones make a tone: one key in between, like having one house between you and your friend.', c(42, 'hero')),
  ('piano', 'C4 D4', c(42, 'hero', seq=['#4', '#5'])),
  ('P', 'C to D has C sharp between. A tone.', c(42, 'hero')),
  ('B', 'On the white keys most steps are tones. Only E to F and B to C are semitones, our old best friends. And a semitone can also go from white to black, or black to white.', c(42, 'rule'))]),
 ('Example: tone or semitone?', [
  ('B', 'Look between the two red keys, E and F. Is there a black key between them?', c(42, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'], lab=['E', 'F'])),
  ('pause', 3, c(42, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('P', 'No: they’re next-door keys. A semitone.', c(42, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('B', 'And C to D?', c(42, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'], lab=['C', 'D'])),
  ('P', 'C sharp is squeezed in between them: a tone.', c(42, 'ex1', reveal=True))]),
 ('Intervals: count the notes', [
  ('B', 'Now bigger distances. The distance between two notes is called an interval. To give it a number, count the notes, both ends included. C to E: C, D, E. Three notes: a third.', c(43, 'xlate')),
  ('piano', 'C4 D4 E4 | [C4 E4]', c(43, 'xlate', seq=['#7', '#8', '#9', '#9'])),
  ('B', 'Sharps and flats never change the number. From C, the numbers go: unison, second, third, fourth, fifth, sixth, seventh, octave.', c(43, 'xlate', anim='ladder')),
  ('piano', 'C4 D4 E4 F4 G4 A4 B4 C5', c(43, 'xlate', seq=['unison', '2nd', '3rd', '4th', '5th', '6th', '7th', '8ve'])),
  ('P', 'Unison? Is that a unicorn that sings?', c(43, 'xlate')),
  ('B', 'Close, but no unicorns. Uni means one, as in unicorn: unison is one sound, the same note twice.', c(43, 'xlate')),
  ('P', 'So C to G is C, D, E, F, G: a fifth.', c(43, 'xlate'))]),
 ('Example: count an interval', [
  ('B', 'F up to A. How many notes? Pause and count.', c(43, 'ex2', show=['F', 'A', 'C', 'G'])),
  ('pause', 3, c(43, 'ex2', show=['F', 'A', 'C', 'G'])),
  ('P', 'F, G, A. Three: a third.', c(43, 'ex2', show=['F', '(G)', 'A', 'C', 'G'])),
  ('piano', 'F4 G4 A4', c(43, 'ex2', seq=['F', '(G)', 'A'], show=['F', '(G)', 'A', 'C', 'G'])),
  ('B', 'And going down? C down to G.', c(43, 'ex2', show=['F', '(G)', 'A', 'C', 'G'])),
  ('P', 'Three. There are three steps from C down to G.', c(43, 'ex2', oops=True)),
  ('B', 'Ooh, so close. Count the notes, not the steps. C itself is number one. It’s like a race: the person on the starting line still counts.', c(43, 'ex2')),
  ('P', 'C, B, A, G. Four: a fourth.', c(43, 'ex2', reveal=True)),
  ('piano', 'C5 B4 A4 G4', c(43, 'ex2', seq=['C', '(B)', '(A)', 'G'], reveal=True)),
  ('B', 'Up or down, the same way: the first note is always one.', c(43, 'ex2', reveal=True))]),
 ('Example: name an interval', [
  ('B', 'E, and the C above it. Count the notes from E.', c(44, 'ex3', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('pause', 3, c(44, 'ex3', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('P', 'E one, F two, G three, A four, B five, C six. A sixth!', c(44, 'ex3', reveal=True)),
  ('piano', 'E4 F4 G4 A4 B4 C5', c(44, 'ex3', seq=['#2', '#3', '#4', '#5', '#6', '#7'], reveal=True)),
  ('B', 'And melodic or harmonic, the number is the same. C then E, one after the other, is a melodic third, like two people talking in turn. C and E together is a harmonic third, like singing at the same time.', c(44, 'ex4', lab=['melodic', 'harmonic'], reveal=True)),
  ('piano', 'C4 E4 | [C4 E4]', c(44, 'ex4', seq=['melodic', 'melodic', 'harmonic'], reveal=True))]),
 ('Try it', [
  ('B', 'Try it: thumb on C, little finger on G. Your hand covers five white keys.', c(44, 'try10')),
  ('piano', 'C4 G4', c(44, 'try10')),
  ('P', 'C up to G: five notes. A fifth! My hand is a ruler.', c(44, 'try10')),
  ('B', 'A very portable ruler. Here’s a riddle: Monday to Wednesday, how many days?', c(44, 'watch')),
  ('P', 'Two?', c(44, 'watch')),
  ('B', 'Monday, Tuesday, Wednesday: three, because you count the day you start on. Intervals count the same way. Your mission: find a semitone, a tone, a third and a fifth from any C. Until next time, Clara.', c(44, 'watch')),
  ('P', 'Bye, Butler!', c(44, 'watch'))])])

NEW['P8'] = ('Major, minor and perfect', [
 ('The secret', [
  ('B', 'Clara, here’s a mystery. Two thirds. Listen carefully.', c(45, 'lead')),
  ('piano', '[C4 E4] | [C4 Eb4]', c(45, 'lead')),
  ('P', 'The first is bright, like a sunny morning. The second is darker, like when it starts to rain at the beach.', c(45, 'lead')),
  ('B', 'Beautifully heard. Both are thirds: three notes each. To tell them apart, count the keys in between, black and white, but not the two you play.', c(45, 'secret')),
  ('B', 'C to E has three keys between: C sharp, D, D sharp. A major third.', c(45, 'hero')),
  ('piano', 'C#4 D4 D#4 | [C4 E4]', c(45, 'hero', seq=['#7', '#8', '#9', '#2'])),
  ('B', 'C to E flat has only two between, one fewer. A minor third.', c(45, 'hero', anim='majmin')),
  ('piano', 'C#4 D4 | [C4 Eb4]', c(45, 'hero', seq=['#18', '#19', '#11'])),
  ('P', 'Just one key makes all that difference?', c(45, 'rule')),
  ('B', 'One key. Like the corners of a mouth: move them a tiny bit, and a smile becomes a frown. So the rule: count the notes for the number, and count the keys in between for the size.', c(45, 'rule')),
  ('B', 'Thirds and sixths come in two sizes, major and minor. Fourths, fifths and octaves have one main size, called perfect. They are never major or minor.', c(45, 'two')),
  ('Q', 'Perfect, like me.', c(45, 'two')),
  ('K', 'Ahem.', c(45, 'two'))]),
 ('A perfect fourth', [
  ('B', 'C up to F: C, D, E, F. Four notes, a fourth. Count the keys between.', c(46, 'xlate')),
  ('piano', 'C#4 D4 D#4 E4 | [C4 F4]', c(46, 'xlate', seq=['1', '2', '3', '4', 'start'])),
  ('P', 'Four between. A perfect fourth. It sounds like the start of a wedding march.', c(46, 'xlate'))]),
 ('Example: major or minor third?', [
  ('B', 'A up to C. A, B, C: three letters, so a third. Now count the keys between. Pause and count.', c(46, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('pause', 3, c(46, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('P', 'B flat, B. Two between.', c(46, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('piano', 'Bb4 B4', c(46, 'ex1', seq=['1', '2'], show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('B', 'A major third has three between. So?', c(46, 'ex1', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('P', 'A minor third! The rainy-beach one, like C to E flat.', c(46, 'ex1', reveal=True)),
  ('piano', '[A4 C5]', c(46, 'ex1', reveal=True))]),
 ('Example: F up to A', [
  ('B', 'F up to A. F, G, A: a third. Now the keys between: they’re numbered for you.', c(46, 'ex2', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('P', 'Two between, so a minor third?', c(46, 'ex2', oops=True)),
  ('B', 'Look again, Clara. You only counted the black ones. G, the white key in the middle, is hiding, but it counts too.', c(46, 'ex2')),
  ('P', 'F sharp, G, G sharp: three. A major third!', c(46, 'ex2', reveal=True)),
  ('piano', 'F#4 G4 G#4 | [F4 A4]', c(46, 'ex2', seq=['1', '2', '3'], reveal=True)),
  ('B', 'The same sunny size as C to E.', c(46, 'ex2', reveal=True))]),
 ('Example: D up to A', [
  ('B', 'D up to A. The number first.', c(47, 'ex3', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('P', 'D, E, F, G, A: five notes, a fifth.', c(47, 'ex3', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('B', 'And six keys between. A fifth with six between is its main size. What is that called?', c(47, 'ex3', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('pause', 3, c(47, 'ex3', show=['C', 'D', 'E', 'F', 'G', 'A', 'B'])),
  ('P', 'A perfect fifth!', c(47, 'ex3', reveal=True)),
  ('piano', 'D#4 E4 F4 F#4 G4 G#4 | [D4 A4]', c(47, 'ex3', seq=['1', '2', '3', '4', '5', '6', 'start'], reveal=True))]),
 ('Try it', [
  ('B', 'And now the most famous four notes in music. Beethoven’s Fifth.', c(47, 'yk')),
  ('piano', 'G4/2 G4/2 G4/2 Eb4*3', c(47, 'yk', seq=['#0', '#1', '#2', '#3'])),
  ('P', 'Da-da-da-dum! It sounds like someone banging on the door.', c(47, 'yk')),
  ('B', 'Some people say it is fate knocking. G down to E flat is a third, with three keys between: a major third. Count them on your keyboard.', c(47, 'yk')),
  ('B', 'A major and a minor third are a smile and a frown: the same face, one small change at the corners.', c(47, 'think')),
  ('Q', 'And never call a fourth or a fifth major, Clara. They are perfect.', c(47, 'watch')),
  ('K', 'Like Her Majesty. Or so I’m told. Every morning.', c(47, 'watch')),
  ('B', 'Until next time, Clara.', c(47, 'watch')),
  ('P', 'Bye, Butler!', c(47, 'watch'))])])

NEW['T1'] = ('Pulse, tempo and the bar', [
 ('The secret', [
  ('B', 'Welcome to Part Two, Clara: time. Put your hand on your heart.', c(50, 'lead')),
  ('P', 'It’s beating. Steady, steady. Oh good, I’m alive.', c(50, 'lead')),
  ('B', 'Very reassuring. That steady beat is a pulse, and almost every piece of music has one too. Its speed is the tempo. And beats travel in little groups called bars, like carriages on a train. Beat one, the engine, is the strongest.', c(50, 'hero')),
  ('count', {'beats': 'X x x x X x x x X x x x', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, c(50, 'hero', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11'])),
  ('B', 'Here is the secret. The beat never stops, not even in a rest. Like a clock on the wall: it keeps ticking even when nobody is looking at it.', c(50, 'secret')),
  ('P', 'So in a rest I still count?', c(50, 'hero')),
  ('B', 'Always. Listen: in the second bar the notes stop, and the beat walks on.', c(50, 'hero')),
  ('count', {'beats': 'X x x x X x x x X x x x', 'notes': 'C5 C4 C4 C4 C5 C4 R R C5 C4 C4 C4', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, c(50, 'hero', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11']))]),
 ('Tempo', [
  ('B', 'Tempo is measured in beats per minute. A metronome mark at the top of the music tells you. Crotchet equals sixty means sixty beats a minute: one every second, like a grandfather clock.', c(50, 'xlate')),
  ('piano', 'X@60 x@60 x@60 x@60', c(50, 'xlate')),
  ('B', 'Crotchet equals one hundred and twenty is twice as fast. More like a puppy’s heartbeat.', c(50, 'xlate')),
  ('piano', 'X@120 x@120 x@120 x@120 X@120 x@120 x@120 x@120', c(50, 'xlate')),
  ('P', 'Twice as many ticks in the same time. That puppy needs to calm down.', c(50, 'xlate'))]),
 ('Example: feel the beat first', [
  ('B', 'This one says crotchet equals ninety-six: ninety-six beats a minute. Don’t start yet. Listen to one full bar first, counting one, two, three in your head.', c(50, 'ex1')),
  ('count', {'beats': 'X@96 x@96 x@96', 'say': '1 2 3'}, c(50, 'ex1')),
  ('B', 'Then step in on the next beat one, the way you step onto a moving escalator. Or jump into a skipping rope.', c(50, 'ex1')),
  ('count', {'beats': 'X@96 x@96 x@96 X@96 x@96 x@96 X@96 x@96 x@96 X@96 x@96 x@96', 'notes': 'R@96 R@96 R@96 C4@96 C4@96 C4@96 C4@48 C4@96 C4@32', 'say': '1 2 3 1 2 3 1 2 3 1 2 3'}, c(50, 'ex1')),
  ('P', 'The first note landed right on the beat! And I didn’t get tangled in the rope.', c(50, 'ex1', reveal=True))]),
 ('Strong and weak beats', [
  ('B', 'Now, the beats are not all equal. Two beats in a bar go strong, weak, like a march. Left, right, left, right.', c(51, 'xlate')),
  ('piano', 'X x X x X x X x', c(51, 'xlate')),
  ('B', 'Three go strong, weak, weak, like a waltz. Oom, pah, pah.', c(51, 'xlate')),
  ('piano', 'X x x X x x X x x', c(51, 'xlate')),
  ('B', 'And four go strong, weak, medium, weak, like most songs.', c(51, 'xlate')),
  ('piano', 'X x M x X x M x', c(51, 'xlate')),
  ('P', 'So Twinkle, Twinkle is in four, and Happy Birthday is in three.', c(51, 'xlate')),
  ('B', 'Exactly. Which means every birthday party is secretly a waltz. And the Radetzky March is in two.', c(51, 'xlate'))]),
 ('Example: march or waltz?', [
  ('B', 'Is this a march or a waltz? Tap a steady beat as you listen.', c(51, 'ex2')),
  ('piano', 'C3 G4 G4 C3 G4 G4 C3 G4 G4', c(51, 'ex2')),
  ('B', 'Which beats feel heavier? Count from one heavy beat to the next. Pause and count.', c(51, 'ex2')),
  ('pause', 3, c(51, 'ex2')),
  ('P', 'Heavy every three: one two three, one two three. Oom, pah, pah. A waltz!', c(51, 'ex2', reveal=True)),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'C3 G4 G4 C3 G4 G4 C3 G4 G4', 'say': '1 2 3 1 2 3 1 2 3'}, c(51, 'ex2', reveal=True)),
  ('B', 'Shall we dance? Heavy every two would have been a march.', c(51, 'ex2', reveal=True))]),
 ('Bars and bar lines', [
  ('B', 'A bar line divides the music into bars, like the lines between parking spaces. A double bar line marks the end of a section, or a change. A final bar line, thin then thick, marks the end of the piece. The full stop.', c(51, 'xlate2')),
  ('B', 'And repeat signs mean: play the passage between them again. If there’s no start sign, go back to the very beginning.', c(51, 'xlate2')),
  ('P', 'Like when my little brother says “again, again!”', c(51, 'xlate2')),
  ('B', 'Exactly. But music only asks once.', c(51, 'xlate2'))]),
 ('Counting', [
  ('B', 'Every beat is counted, even inside a long note. Here are three bars of three-four. The red number is where you play; the grey numbers are the beats you hold, like holding your breath underwater.', c(52, 'xlate')),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'C4 C4 C4 C4*2 C4 C4*3', 'say': '1 2 3 1 2 3 1 2 3'}, c(52, 'xlate')),
  ('B', 'Count aloud at one speed, a little louder on beat one. And with a metronome, start slower than you think, then speed up only when the passage is steady. The tortoise wins this race.', c(52, 'xlate'))]),
 ('Try it', [
  ('B', 'Hand on your heart again. Tap the beat and say one, two, three, four, with one a little louder. Keep going for ten seconds without speeding up.', c(52, 'try10')),
  ('count', {'beats': 'X@80 x@80 x@80 x@80 X@80 x@80 x@80 x@80 X@80 x@80 x@80 x@80', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, c(52, 'try10', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11'])),
  ('B', 'Every New Year in Vienna, a whole concert hall claps along on every beat of the Radetzky March. Thousands of people, one pulse. The tune dances freely on top.', c(52, 'yk')),
  ('count', {'beats': 'X x X x X x', 'say': '1 2 1 2 1 2'}, c(52, 'yk', seq=['#0', '#1', '#2', '#3', '#4', '#5'])),
  ('P', 'I want to clap with them!', c(52, 'yk')),
  ('B', 'One day. Remember: the beat is the stage and the notes are the actors. The stage is there before anyone walks on. So watch it move for a bar, then step in. Until next time, Clara.', c(52, 'think')),
  ('P', 'One, two, three, four. Bye, Butler!', c(52, 'think'))])])

NEW['T2'] = ('Notes and rests', [
 ('The secret', [
  ('P', 'Butler, how do I know how long to hold a note? Do I just guess?', c(53, 'lead')),
  ('B', 'No guessing required. Its shape tells you, like the size of a cup tells you how much juice it holds. Each note is half the one above it. A semibreve lasts four beats. It splits into two minims, two beats each. A minim splits into two crotchets, one beat each. And a crotchet splits into two quavers, half a beat each.', c(53, 'hero')),
  ('P', 'Like cutting a cake in half, and in half again.', c(53, 'hero')),
  ('B', 'Precisely, and nobody fights over the pieces. Listen to one bar of each. The beat keeps going; only the notes change.', c(53, 'hero')),
  ('count', {'beats': 'X x M x X x M x X x M x', 'notes': 'C4*4 C4*2 C4*2 C4 C4 C4 C4', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, c(53, 'hero')),
  ('B', 'And quavers: two to every beat.', c(53, 'hero')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2 C4/2 C4/2 C4/2 C4/2', 'say': '1 & 2 & 3 & 4 &'}, c(53, 'hero')),
  ('P', 'For the quavers you said “and” in between.', c(53, 'sm')),
  ('B', 'Yes. Say the beat’s number, then “and” halfway to the next beat. And here’s the other half of the secret: every note has a twin rest, a silence of exactly the same length.', c(53, 'secret'))]),
 ('Head, stem, flag', [
  ('B', 'A note is built like a little person. It has a head, on a line or in a space. Every note except the semibreve has a stem. Below the middle line the stem goes up, on the right of the head; on or above the middle line it goes down, on the left.', c(53, 'two')),
  ('P', 'Does a stem going down make the note shorter? Like it’s sad?', c(53, 'two')),
  ('B', 'Never. The stem only keeps the page tidy, so the notes don’t poke out of the staff. Flags change the length: each flag halves the note. And quavers side by side often hold hands with a beam instead of flags.', c(53, 'two')),
  ('P', 'So a note on the middle line has its stem going down?', c(53, 'two')),
  ('B', 'Exactly: on or above the middle line, down on the left; below it, up on the right.', c(53, 'two'))]),
 ('The semibreve rest’s special power', [
  ('B', 'Most rests last a fixed number of beats. But the semibreve rest has a superpower: it can mean a whole bar of silence, in any time signature, and then it sits in the middle of the bar. In four-four it lasts four beats, in three-four three, in two-four two. Listen to three-four: the middle bar is silent, and the beat goes on.', c(53, 'box')),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'C4 C4 C4 R*3 C4*2 C4', 'say': '1 2 3 1 2 3 1 2 3'}, c(53, 'box'))]),
 ('Every note has a twin rest', [
  ('B', 'Every note has a twin rest, the same length with no sound: semibreve, minim, crotchet, quaver, and the semiquaver, a quarter of a beat, which you’ll meet later.', c(54, 'svg')),
  ('B', 'Two rests look like identical twins. The semibreve rest hangs from the fourth line, heavy, like a coat on a hook. The minim rest sits on the middle line, like a hat.', c(54, 'svg')),
  ('P', 'Coat hangs, hat sits. I’ll never mix them up.', c(54, 'svg'))]),
 ('Pizzas', [
  ('B', 'Some books call the notes whole, half, quarter, eighth and sixteenth notes. Here is why.', c(54, 'pzbox')),
  ('B', 'Think of each beat as a pizza. A bar of four-four is four pizzas. The semibreve eats all four; a minim, two; a crotchet, one; a quaver, half a pizza. A rest is the same share, left on the plate.', c(54, 'pzbox')),
  ('P', 'So two quavers make one full pizza. Who leaves pizza on the plate?', c(54, 'pzbox')),
  ('B', 'Rests do. Very disciplined. Listen: two quavers, then a crotchet. Same-sized pizza.', c(54, 'pzbox')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4/2 C4/2 C4 C4/2 C4/2 C4', 'say': '1 & 2 & 3 & 4 &'}, c(54, 'pzbox'))]),
 ('Example: each sound and each silence', [
  ('B', 'Two bars of four-four. Name each shape, say how many beats it lasts, and add them up, rests included. Pause and try.', c(54, 'ex1')),
  ('pause', 4, c(54, 'ex1')),
  ('P', 'Minim, two. Crotchet, one. Crotchet rest, one. Four beats!', c(54, 'ex1', reveal=True)),
  ('B', 'And the second bar has the same shapes in a different order, like the same furniture moved around. Count it with me: the rests are counted too.', c(54, 'ex1', reveal=True)),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C4*2 C4 R C4 R C4*2', 'say': '1 2 3 4 1 2 3 4'}, c(54, 'ex1', reveal=True))]),
 ('How to draw notes and rests', [
  ('B', 'Now draw them yourself, Clara: it’s the quickest way to remember them. A note starts with an oval head, tilted a little, like an egg leaning on its side: filled in for a crotchet or a quaver, hollow for a minim or a semibreve.', c(55, 'xlate')),
  ('B', 'Then a stem, about three spaces tall: going up, it sits on the right of the head; going down, on the left. A quaver adds a flag at the end of the stem, always waving to the right.', c(55, 'xlate')),
  ('P', 'Egg, stem, flag.', c(55, 'xlate')),
  ('B', 'And the rests. The semibreve rest is a little block hanging under line four; the minim rest, a block sitting on line three. The crotchet rest: draw a Z, then a little c underneath. The quaver rest is a seven with a dot on top, and the semiquaver rest a seven with two.', c(55, 'xlate')),
  ('P', 'A Z and a c. I can do that! It looks like a lightning bolt.', c(55, 'xlate'))]),
 ('Example: fill the bar', [
  ('B', 'A bar of four-four is a train with four seats. How many seats does the minim take? And the crotchet? How many are left, and which rest fills them? Pause and think.', c(55, 'ex2')),
  ('pause', 4, c(55, 'ex2')),
  ('P', 'Two seats left!', c(55, 'ex2', oops=True)),
  ('B', 'Ah, you forgot a passenger. The crotchet books a seat as well.', c(55, 'ex2')),
  ('P', 'The minim takes two and the crotchet one: three. One seat left: a crotchet rest!', c(55, 'ex2', reveal=True)),
  ('count', {'beats': 'X x M x', 'notes': 'C4*2 C4 R', 'say': '1 2 3 4'}, c(55, 'ex2', reveal=True))]),
 ('You know this', [
  ('B', 'Twinkle, Twinkle: six crotchets, then a minim at the end of the line, two beats to breathe.', c(55, 'yk')),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C4 C4 G4 G4 A4 A4 G4*2', 'say': '1 2 3 4 1 2 3 4'}, c(55, 'yk')),
  ('B', 'A rest is not a gap in the music; it’s music you can’t hear. Like the pause before the punchline of a joke. Keep counting through it. Until next time, Clara.', c(55, 'yk')),
  ('P', 'One, two, three, four. Bye, Butler!', c(55, 'yk'))])])

NEW['T3'] = ('How long is a note?', [
 ('The secret', [
  ('P', 'Butler, what if I need a note longer than its shape? Can I just hold it and hope?', c(56, 'lead')),
  ('B', 'Hope is not a rhythm, Clara. Two signs stretch a note: the dot and the tie. When a crotchet is one beat, a minim lasts two. Put a dot after it, and the dot adds half of two: one more beat. Two plus one: three beats.', c(56, 'hero')),
  ('B', 'Listen: a minim, then a dotted minim. Count with me.', c(56, 'hero')),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C4*2 R*2 C4*3 R', 'say': '1 2 3 4 1 2 3 4'}, c(56, 'hero')),
  ('B', 'That’s the secret. A dot adds half. A tie glues two notes into one sound.', c(56, 'secret'))]),
 ('The dot', [
  ('B', 'A dot always adds half of its own note. A dotted crotchet is one plus a half: one and a half beats. Here it is, then a quaver, then a minim. Hold the dotted crotchet through “one and two”, and the quaver lands on the “and”.', c(56, 'xlate')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4*1.5 C4/2 C4*2', 'say': '1 & 2 & 3 & 4 &'}, c(56, 'xlate'))]),
 ('The dot, in pizzas', [
  ('B', 'Back to pizzas. A dotted minim is two pizzas, plus one more for the dot. A dotted crotchet is one pizza plus half. A dotted quaver is half a pizza plus a quarter. The dot is always half of whatever its note already has. Like a friend who always wants half of your dessert.', c(56, 'xlate'))]),
 ('Example: a dotted crotchet and a quaver', [
  ('B', 'How many beats are a dotted crotchet and a quaver together? And where does the quaver fall? Pause and try.', c(56, 'ex1')),
  ('pause', 4, c(56, 'ex1')),
  ('P', 'One and a half, plus a half: two beats. The quaver lands on the “and” of two.', c(56, 'ex1', reveal=True)),
  ('count', {'beats': 'X/2 R/2 x/2 R/2', 'notes': 'C4*1.5 C4/2', 'say': '1 & 2 &'}, c(56, 'ex1', reveal=True))]),
 ('Example: Ode to Joy', [
  ('B', 'You already know a dotted crotchet: Beethoven’s Ode to Joy. Listen to bars three and four. The red E is dotted: hold it through “one and two”. The quaver D falls on the “and”, and the last D takes beats three and four.', c(57, 'ex2')),
  ('count', {'beats': 'X x M x X/2 R/2 x/2 R/2 M x', 'notes': 'C4 C4 D4 E4 E4*1.5 D4/2 D4*2', 'say': '1 2 3 4 1 & 2 & 3 4'}, c(57, 'ex2', reveal=True)),
  ('P', 'Long, short, then long. It leans before it lands, like a gymnast at the end of a routine!', c(57, 'ex2', reveal=True))]),
 ('The double dot', [
  ('B', 'Going further: a second dot adds half of the first dot. A double-dotted minim lasts two, plus one, plus a half: three and a half beats. You won’t need it for a while, so you can tuck it away for later.', c(57, 'xlate'))]),
 ('The tie', [
  ('B', 'A tie is a curve joining two notes of the same pitch. Play the first and hold through the second, like holding a door open for the person behind you. Don’t play the second note again. And a tie can cross a bar line, which a dot cannot.', c(57, 'xlate2')),
  ('count', {'beats': 'X x X x', 'notes': 'C4 C4~ C4 C4', 'say': '1 2 1 2'}, c(57, 'xlate2')),
  ('P', 'One sound from beat two, right over the bar line to beat one.', c(57, 'xlate2'))]),
 ('Example: dot or tie?', [
  ('B', 'Which is longer: the dotted minim, or the minim tied to a crotchet? Add up each one. Pause and try.', c(57, 'ex3')),
  ('pause', 4, c(57, 'ex3')),
  ('P', 'The tied notes are longer. There are two of them!', c(57, 'ex3', oops=True)),
  ('B', 'Two notes, but one sound. Two half-sandwiches are still one sandwich. Add them up and compare.', c(57, 'ex3')),
  ('P', 'Dotted minim: two plus one, three. Tied notes: two plus one, three. The same!', c(57, 'ex3', reveal=True)),
  ('count', {'beats': 'X x x X x x', 'notes': 'C4*3 C4*2~ C4', 'say': '1 2 3 1 2 3'}, c(57, 'ex3', reveal=True)),
  ('B', 'Both last three beats. But only the tie could cross a bar line.', c(57, 'ex3', reveal=True))]),
 ('Example: which is longer?', [
  ('B', 'A dotted minim, or a minim tied to a quaver? Count the pizzas. Pause and try.', c(58, 'ex4')),
  ('pause', 4, c(58, 'ex4')),
  ('P', 'Three against two and a half. The dotted minim is longer, by half a pizza.', c(58, 'ex4', reveal=True)),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4*3 R', 'say': '1 & 2 & 3 & 4 &'}, c(58, 'ex4', reveal=True)),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4*2~ C4/2 R/2 R', 'say': '1 & 2 & 3 & 4 &'}, c(58, 'ex4', reveal=True))]),
 ('Tie or slur?', [
  ('B', 'Careful now: two curves look alike, like twins in matching jumpers. A tie joins the same pitch: play once and hold. Here, G for four beats, then E for four.', c(58, 'xlate')),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'G4*2~ G4*2 E4*2~ E4*2', 'say': '1 2 3 4 1 2 3 4'}, c(58, 'xlate')),
  ('B', 'A slur joins different pitches: play every note, smoothly joined. That smooth playing is called legato. Listen: every note sounds.', c(58, 'xlate')),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C4_ D4_ E4_ F4_ G4*4', 'say': '1 2 3 4 1 2 3 4'}, c(58, 'xlate'))]),
 ('Game: how many beats?', [
  ('B', 'Game time. With a crotchet as one beat, how long does each one last: a dotted minim, a dotted crotchet, and a minim tied to a crotchet? Pause and count.', c(58, 'game')),
  ('pause', 5, c(58, 'game')),
  ('P', 'Three. One and a half. And three again.', c(58, 'game', reveal=True)),
  ('B', 'Full marks. Have a pizza.', c(58, 'game', reveal=True))]),
 ('Try it', [
  ('B', 'Clap once, and hold for three, saying one, two, three: a dotted minim.', c(58, 'try10')),
  ('count', {'beats': 'X x x X x x', 'notes': 'C4*3 C4*3', 'say': '1 2 3 1 2 3'}, c(58, 'try10')),
  ('B', 'Then a dotted crotchet and a quaver: clap on one, hold through “and two”, and clap again on the “and”.', c(58, 'try10')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 X/2 R/2 x/2 R/2', 'notes': 'C4*1.5 C4/2 C4*1.5 C4/2', 'say': '1 & 2 & 1 & 2 &'}, c(58, 'try10'))]),
 ('Watch out', [
  ('B', 'Three traps to step around. A dot adds half of its own note, not of the next one. A curve between two different pitches is a slur, not a tie. And there are two kinds of dot: after the head, it adds length; above or below the head, it means staccato, short.', c(58, 'watch')),
  ('P', 'Same dot, different job. Like a full stop and a decimal point.', c(58, 'watch')),
  ('B', 'Very clever. A dot is a little loan of time; a tie is a bridge between two notes. Until next time, Clara.', c(58, 'watch')),
  ('P', 'One, two, three. Bye, Butler!', c(58, 'watch'))])])

NEW['T4'] = ('Time signatures', [
 ('The secret', [
  ('P', 'Butler, what are the two numbers at the start of the music? Is it a maths test?', c(59, 'lead')),
  ('B', 'Not a test, I promise. It’s the time signature, Clara. Read it like a train ticket. The top number says how many seats each carriage, each bar, has. The bottom number says which note sits in one seat.', c(59, 'hero')),
  ('B', 'Four-four: four seats, and a crotchet in each. Count the seats with me.', c(59, 'hero')),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C4 C4 C4 C4 C4 C4 C4 C4', 'say': '1 2 3 4 1 2 3 4'}, c(59, 'hero')),
  ('B', 'That is the secret: the top number is how many beats, and the bottom number is which note gets one beat.', c(59, 'secret'))]),
 ('Think of a train', [
  ('B', 'In three-four every carriage has three seats. A minim books two, a crotchet one. A rest books a seat and leaves it empty, like a bag on the seat next to you. A dotted minim is a big family that fills all three.', c(59, 'pzbox')),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'C4*2 C4 C4 R C4 C4*3', 'say': '1 2 3 1 2 3 1 2 3'}, c(59, 'pzbox')),
  ('B', 'The bottom number is a secret code: two means a minim, four a crotchet, eight a quaver, sixteen a semiquaver.', c(59, 'xlate')),
  ('P', 'A code! Like spies.', c(59, 'xlate'))]),
 ('Example: what does three-four mean?', [
  ('B', 'Three-four. How many counts in each bar, and which note gets one count? Pause and think.', c(60, 'ex1')),
  ('pause', 3, c(60, 'ex1')),
  ('P', 'Three counts, and four counts?', c(60, 'ex1', oops=True)),
  ('B', 'Ah, everybody falls into that hole once. The bottom number isn’t a count, Clara. It’s the code for the note that gets one beat.', c(60, 'ex1')),
  ('P', 'Oh. Three counts, and the four means a crotchet.', c(60, 'ex1', reveal=True)),
  ('B', 'Check the first bar: two quavers make one, then a crotchet, a crotchet. Three. Count it.', c(60, 'ex1', reveal=True)),
  ('count', {'beats': 'X/2 R/2 x x X x x', 'notes': 'C4/2 C4/2 C4 C4 C4*2 C4', 'say': '1 & 2 3 1 2 3'}, c(60, 'ex1', reveal=True))]),
 ('Simple time', [
  ('B', 'In simple time every beat splits into two, like a biscuit snapped in half. Two-four, three-four and four-four count crotchets. Four-four can also be written as a C, common time, and two-two as a C with a line through it, cut common time: two minim beats.', c(60, 'xlate')),
  ('P', 'A C with a line through it. Like a cent sign.', c(60, 'xlate')),
  ('B', 'And just as cheap to write.', c(60, 'xlate'))]),
 ('Example: which ticket?', [
  ('B', 'This carriage has three seats, and a quaver sits in each. Write the ticket. Pause and try.', c(60, 'ex2')),
  ('pause', 4, c(60, 'ex2')),
  ('P', 'Three on top. A quaver is the code eight, so eight underneath: three-eight!', c(60, 'ex2', reveal=True)),
  ('B', 'Ticket accepted. All aboard.', c(60, 'ex2', reveal=True))]),
 ('Example: where does the rest go?', [
  ('B', 'Four-four, and three crotchets. Which seat is empty, and what goes there?', c(61, 'ex3')),
  ('pause', 3, c(61, 'ex3')),
  ('P', 'Seat four. A crotchet rest, sitting there quietly!', c(61, 'ex3', reveal=True)),
  ('count', {'beats': 'X x M x', 'notes': 'C4 C4 C4 R', 'say': '1 2 3 4'}, c(61, 'ex3', reveal=True))]),
 ('Changing time signature', [
  ('B', 'A new time signature can arrive right after a bar line, like a train changing to shorter carriages at a station. Here three-four becomes two-four, and two beats a bar holds until the next change.', c(61, 'xlate')),
  ('count', {'beats': 'X x x X x x X x X x X x', 'notes': 'C4 C4 C4 C4*2 C4 C4 C4 C4*2 C4 C4', 'say': '1 2 3 1 2 3 1 2 1 2 1 2'}, c(61, 'xlate'))]),
 ('You know this', [
  ('B', 'The Minuet from the Notebook for Anna Magdalena Bach: one two three, one two three, the step of an old court dance. That is three-four.', c(61, 'yk')),
  ('count', {'beats': 'X x x X x x', 'notes': 'D5 G4/2 A4/2 B4/2 C5/2 D5 G4 G4', 'say': '1 2 3 1 2 3'}, c(61, 'yk')),
  ('P', 'I can imagine people in big wigs bowing to each other.', c(61, 'yk')),
  ('Q', 'We still dance it at the palace. And remember, Clara: the bottom number is not a count. It names the note that gets one beat.', c(61, 'watch')),
  ('B', 'Until next time, Clara.', c(61, 'watch')),
  ('P', 'Bye, Butler! Bye, Your Majesty!', c(61, 'watch'))])])

NEW['T5'] = ('Compound and irregular time', [
 ('The secret', [
  ('P', 'Butler, some pieces make me want to skip down the hallway. Why?', c(62, 'lead')),
  ('B', 'That, Clara, is compound time, and skipping is exactly the right reaction. Take six quavers. Three-four groups them in twos: three beats, like walking. Six-eight groups them in threes: two big beats, like skipping or galloping on a horse.', c(62, 'hero')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 x/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2 C4/2 C4/2', 'say': '1 & 2 & 3 &'}, c(62, 'hero')),
  ('count', {'beats': 'X/2 R/2 R/2 M/2 R/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2 C4/2 C4/2', 'say': '1 2 3 4 5 6'}, c(62, 'hero')),
  ('P', 'The same six notes, but the second time they gallop!', c(62, 'hero')),
  ('B', 'The same six notes, new groups. Here’s the secret: in compound time each beat is a dotted note, and it splits in three.', c(62, 'secret'))]),
 ('Simple or compound?', [
  ('B', 'In simple time one beat splits in two, like a biscuit snapped in half. In compound time one dotted beat splits in three, like a chocolate bar with three squares. Quick test: a top number of six, nine or twelve means compound. Divide it by three to find the beats.', c(62, 'xlate'))]),
 ('Counting six-eight', [
  ('B', 'Slowly, count all six quavers. At speed, feel only two beats, on one and four.', c(63, 'xlate')),
  ('count', {'beats': 'X x x M x x', 'notes': 'C4 C4 C4 C4 C4 C4', 'say': '1 2 3 4 5 6'}, c(63, 'xlate')),
  ('count', {'beats': 'X R R M R R X R R M R R', 'notes': 'C4 C4 C4 C4 C4 C4 C4*3 C4*3', 'say': '1 2 3 4 5 6 1 - - 4 - -'}, c(63, 'xlate')),
  ('B', 'Try it: say pine-ap-ple, pine-ap-ple, and step only on pine.', c(63, 'xlate')),
  ('P', 'Pine-ap-ple, pine-ap-ple. Now I want a fruit salad.', c(63, 'xlate'))]),
 ('Example: how many beats in nine-eight?', [
  ('B', 'Nine-eight. How many beats in a bar? Hint: does nine divide by three?', c(63, 'ex1')),
  ('pause', 3, c(63, 'ex1')),
  ('P', 'Nine beats!', c(63, 'ex1', oops=True)),
  ('B', 'Nine quavers, yes. But nobody taps their foot nine times a bar; they’d be exhausted. At speed you feel them in groups. How many groups of three?', c(63, 'ex1')),
  ('P', 'Three groups: three beats, each a dotted crotchet! Three pineapples.', c(63, 'ex1', reveal=True)),
  ('count', {'beats': 'X x x M x x M x x', 'notes': 'C4 C4 C4 C4 C4 C4 C4 C4 C4', 'say': '1 2 3 4 5 6 7 8 9'}, c(63, 'ex1', reveal=True))]),
 ('Example: is this still four-four?', [
  ('B', 'Many dances keep four-four but group the eight quavers three, three, two. Where do the accents fall? And how many times does your foot tap?', c(63, 'xlate2')),
  ('count', {'beats': 'X/2 R/2 R/2 M/2 R/2 R/2 M/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2 C4/2 C4/2 C4/2 C4/2', 'say': '1 2 3 1 2 3 1 2'}, c(63, 'xlate2')),
  ('P', 'Accents on the first, fourth and seventh quavers, but my foot still taps four even beats.', c(63, 'xlate2', reveal=True)),
  ('B', 'So it’s still four-four. Only the accents are lopsided, which is what makes people get up and dance.', c(63, 'xlate2', reveal=True))]),
 ('Irregular time', [
  ('B', 'Going further: irregular time has five or seven counts, in uneven groups, like a limping penguin that somehow never falls over. Five-four is three plus two; seven-eight can be two, two, three.', c(64, 'xlate')),
  ('count', {'beats': 'X x x M x X x x M x', 'notes': 'C4 C4 C4 C4 C4 C4 C4 C4 C4 C4', 'say': '1 2 3 1 2 1 2 3 1 2'}, c(64, 'xlate')),
  ('K', 'Five in a bar? In my day we kept to twos and threes. But I must admit, it does make one dance.', c(64, 'xlate')),
  ('P', 'I’d love to see the King dance in five.', c(64, 'xlate')),
  ('K', 'Nobody sees the King dance in five.', c(64, 'xlate'))]),
 ('You know this', [
  ('B', 'Row, Row, Row Your Boat: two big beats in every bar, each a dotted crotchet. Sway twice per bar while you sing, like a boat on gentle waves.', c(64, 'yk')),
  ('count', {'beats': 'X R R M R R X R R M R R', 'notes': 'C4*3 C4*3 C4*2 D4 E4*3', 'say': '1 - - 2 - - 1 - - 2 - -'}, c(64, 'yk')),
  ('P', 'I feel a bit seasick. In a good way.', c(64, 'yk')),
  ('B', 'And watch the bottom number: the eight means quavers. Six quavers in a bar, felt as two dotted-crotchet beats. Until next time, Clara.', c(64, 'watch')),
  ('P', 'Bye, Butler!', c(64, 'watch'))])])

NEW['T6'] = ('Rhythm: groups and upbeats', [
 ('The secret', [
  ('P', 'Butler, why are some quavers joined together? Are they friends?', c(65, 'lead')),
  ('B', 'Best friends holding hands. Those lines are beams, Clara. Beams join notes that belong together, usually one beat at a time, so you can see where each beat starts.', c(65, 'hero')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C5/2 C5/2 C5/2 C5/2 C5/2 C5/2 C5/2 C5/2', 'say': '1 & 2 & 3 & 4 &'}, c(65, 'hero')),
  ('B', 'That’s half the secret. The other half: an upbeat borrows from the last bar.', c(65, 'secret'))]),
 ('Grouping with beams', [
  ('B', 'In four-four a beam may cover beats one and two, or three and four, but never cross the middle of the bar. Think of the middle of the bar as a river: the beams may not build a bridge over it. On the left the beams show the beats. On the right, one beam hides the middle.', c(65, 'xlate')),
  ('P', 'So the middle of the bar must always show. No bridges over the river.', c(65, 'xlate'))]),
 ('Example: six quavers in three-four', [
  ('B', 'Six quavers in three-four. Why are they beamed in twos? Pause and think.', c(65, 'ex1')),
  ('pause', 3, c(65, 'ex1')),
  ('P', 'Three crotchet beats, two quavers each!', c(65, 'ex1', reveal=True)),
  ('B', 'Exactly. Beamed in threes, they’d be wearing six-eight’s clothes.', c(65, 'ex1', reveal=True)),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 x/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2 C4/2 C4/2', 'say': '1 & 2 & 3 &'}, c(65, 'ex1', reveal=True))]),
 ('The upbeat', [
  ('B', 'A piece can begin before the first full bar, like someone taking a little run-up before a jump. These notes are the upbeat, or anacrusis. Count one two silently, then play on three. The last bar is short by the same amount: one plus two makes a full bar.', c(66, 'xlate')),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'R R C4 C4 C4 C4 C4*2 R', 'say': '1 2 3 1 2 3 1 2 -'}, c(66, 'xlate')),
  ('P', 'Anacrusis. That sounds like a dinosaur.', c(66, 'xlate')),
  ('B', 'A very small, polite dinosaur that arrives early. Happy Birthday starts with one. Hap-py comes before the strong beat, and the strong beat lands on birth.', c(66, 'xlate')),
  ('count', {'beats': 'R x X x x', 'notes': 'R C4*0.75 C4/4 D4 C4 F4', 'say': '- 3 1 2 3'}, c(66, 'xlate'))]),
 ('Triplets', [
  ('B', 'A triplet is three equal notes in the time of two, marked with a little three. Like three friends squeezing onto a seat built for two. One beat cut in two is two quavers; cut in three, a triplet; cut in four, four semiquavers.', c(66, 'xlate2')),
  ('count', {'beats': 'X x M x', 'notes': 'C4/2 C4/2 C4/3 C4/3 C4/3 C4/4 C4/4 C4/4 C4/4 C4', 'say': '1 2 3 4'}, c(66, 'xlate2'))]),
 ('Example: where is the triplet?', [
  ('B', 'Find the little three. Which beat do the three quavers share?', c(67, 'ex2')),
  ('pause', 3, c(67, 'ex2')),
  ('P', 'Beat two!', c(67, 'ex2', reveal=True)),
  ('B', 'Say it: one, trip-a-let, three, four. Or one, choc-o-late, three, four, if you’re hungry. The beat never moves.', c(67, 'ex2', reveal=True)),
  ('count', {'beats': 'X x M x', 'notes': 'C4 C4/3 C4/3 C4/3 C4 C4', 'say': '1 2 3 4'}, c(67, 'ex2', reveal=True))]),
 ('Example: a bar of mixed values', [
  ('B', 'Now a bar with everything in it, like a mixed bag of sweets: a crotchet, two quavers, four semiquavers and a triplet. One beat each. Count it with me.', c(67, 'ex3')),
  ('count', {'beats': 'X x M x', 'notes': 'C4 C4/2 C4/2 C4/4 C4/4 C4/4 C4/4 C4/3 C4/3 C4/3', 'say': '1 2 3 4'}, c(67, 'ex3', reveal=True)),
  ('P', 'It sped up and slowed down, but the beat stayed the same!', c(67, 'ex3', reveal=True)),
  ('B', 'Going further: a duplet is the triplet turned inside out, two notes in the time of three, in compound time. Until next time, Clara.', c(67, 'xlate')),
  ('P', 'Bye, Butler!', c(67, 'xlate'))])])

NEW['T7'] = ('Rhythm: off the beat', [
 ('The secret', [
  ('P', 'Butler, some music seems to bounce between the beats, like a ball that won’t sit still.', c(68, 'lead')),
  ('B', 'That’s rhythm teasing the beat, Clara, like a cat batting at a string. Here a note starts on the “and”, between the beats, and is held over beat two.', c(68, 'hero')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4/2 C4 C4/2 C4 C4', 'say': '1 & 2 & 3 & 4 &'}, c(68, 'hero')),
  ('B', 'But it only works if the beat underneath stays rock-steady. The string can wiggle; the hand holding it stays still. That’s the secret.', c(68, 'secret'))]),
 ('Swing', [
  ('B', 'First, swing. Jazz and blues pieces are often marked swing. Pairs of quavers are written evenly but played long, short, like the first and last notes of a triplet. Listen: first straight, like a robot walking.', c(68, 'xlate')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2', 'say': '1 & 2 &'}, c(68, 'xlate')),
  ('B', 'Then swung, like a person strolling with their hands in their pockets.', c(68, 'xlate')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2', 'notes': 'C4*0.667 C4/3 C4*0.667 C4/3', 'say': '1 & 2 &'}, c(68, 'xlate')),
  ('P', 'Doo-ba, doo-ba. That’s much cooler.', c(68, 'xlate')),
  ('B', 'Which notes swing here? Pause and look.', c(68, 'xlate')),
  ('pause', 3, c(68, 'xlate')),
  ('P', 'Only the quaver pairs, on beats two and three. The crotchets stay even.', c(68, 'xlate', reveal=True))]),
 ('Syncopation', [
  ('B', 'Syncopation: a note starts on the “and”, and is held through the next beat. Like a hiccup in the middle of a sentence. Tap the beats: one, two. Where does the red crotchet start?', c(69, 'xlate')),
  ('pause', 3, c(69, 'ex2')),
  ('P', 'On the “and”, and it holds through beat two!', c(69, 'ex2', reveal=True)),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 X/2 R/2 x/2 R/2', 'notes': 'C4/2 C4 C4/2 C4 C4', 'say': '1 & 2 & 1 & 2 &'}, c(69, 'ex2', reveal=True)),
  ('B', 'The Entertainer, by Scott Joplin: the high C keeps landing just after the beat, like someone always arriving a moment late to the party, and making everyone laugh. That’s the bounce of ragtime.', c(69, 'xlate2')),
  ('B', 'To feel it, tap a steady beat with your foot, and clap only between the taps. If your foot starts to follow your hands, slow down.', c(69, 'howto')),
  ('P', 'My foot is very easily distracted.', c(69, 'howto')),
  ('B', 'Then your foot needs a stern talking-to. Slowly first.', c(69, 'howto'))]),
 ('Hemiola', [
  ('B', 'Hemiola: two bars of three-four felt as three big beats. It’s like a small magic trick. Count as written, one two three, one two three. Now feel each minim as one big beat. How many?', c(70, 'xlate')),
  ('count', {'beats': 'X x x X x x', 'notes': 'C4*2 C4*2 C4*2', 'say': '1 2 3 1 2 3'}, c(70, 'xlate')),
  ('P', 'Three big ones! The bars just changed shape.', c(70, 'xlate', reveal=True))]),
 ('Polyrhythm and rubato', [
  ('B', 'Going further: polyrhythm is two rhythms at once, three against two, like patting your head and rubbing your tummy. And rubato stretches the time, then gives it back. Whatever you borrow, you pay back.', c(70, 'xlate2')),
  ('P', 'Like borrowing my sister’s pencil.', c(70, 'xlate2')),
  ('B', 'And giving it back, ideally unchewed. Keep counting inside long notes, and only the quaver pairs swing. Until next time, Clara.', c(70, 'watch')),
  ('P', 'Bye, Butler!', c(70, 'watch'))])])

NEW['T8'] = ('Repeats and road signs', [
 ('The secret', [
  ('P', 'On the way to Grandma’s, Dad drives round the roundabout twice when he misses the turning. Mum always sighs.', c(71, 'lead')),
  ('B', 'Ha! Music has roundabouts and road signs too, Clara, and in music they are not mistakes: they are the map. Nobody sighs.', c(71, 'lead')),
  ('P', 'So why does the music sometimes go backwards?', c(71, 'lead')),
  ('B', 'To save writing the same bars twice. Composers are busy people. Two dots facing back mean: go back and play it again. Here you play A, B, then A, B again, then C.', c(71, 'hero')),
  ('B', 'So read the signs like a map. Jump back at the sign, stop at ⟨Fine⟩, or jump to the ⟨Coda⟩.', c(71, 'secret'))]),
 ('The signs', [
  ('B', 'Here are the road signs. Repeat signs: play the bars between them twice. First and second time bars: the first time, play the first-time bar; after the repeat, skip it and play the second-time bar. D.C., da capo, from the head: back to the very beginning. D.S., dal segno: back to the sign. Fine: the end. And Coda, the tail: when you see the words To Coda, jump to the coda sign.', c(71, 'ht')),
  ('P', 'Music has a head and a tail? Like a dog!', c(71, 'ht')),
  ('B', 'A very well-behaved dog. The rule: follow the map in order. After a jump, stop at the first ⟨Fine⟩ you meet, or jump when you see To ⟨Coda⟩.', c(71, 'rule'))]),
 ('Example: one repeat sign', [
  ('B', 'B ends with a repeat sign, and there’s no start sign. In what order do you play? Pause and try.', c(72, 'ex1')),
  ('pause', 4, c(72, 'ex1')),
  ('P', 'Back to the very start: A, B, A, B, C.', c(72, 'ex1', reveal=True))]),
 ('Example: first and second time', [
  ('B', 'First time: A, then the bar marked one. The repeat sends you back to A. Second time, which bar do you skip?', c(72, 'ex2')),
  ('pause', 4, c(72, 'ex2')),
  ('P', 'Skip B: A, B, A, C. Like taking a different exit the second time round the roundabout.', c(72, 'ex2', reveal=True)),
  ('B', 'Your father would be proud.', c(72, 'ex2', reveal=True))]),
 ('Game: how many bars?', [
  ('B', 'A quick game: each letter is one bar. Follow the signs and count every bar you play. Pause and count.', c(72, 'game')),
  ('pause', 6, c(72, 'game')),
  ('P', 'Four, six and five!', c(72, 'game', reveal=True))]),
 ('Example: D.C. al Fine', [
  ('B', 'Play straight through to D. D.C. sends you back to the head. Where do you stop?', c(73, 'ex3')),
  ('pause', 4, c(73, 'ex3')),
  ('P', 'At ⟨Fine⟩: A, B, C, D, A, B.', c(73, 'ex3', reveal=True))]),
 ('Example: D.S. al Coda', [
  ('B', 'The trickiest map of all. Play through to D, ignoring To Coda the first time. D.S. sends you back to the sign. Then play on to To Coda, and jump. Pause and try.', c(73, 'ex4')),
  ('pause', 5, c(73, 'ex4')),
  ('P', 'A, B, C, D, then B, C, and jump to E! Like a treasure map.', c(73, 'ex4', reveal=True)),
  ('Q', 'Splendid. And on the way back after a D.C. or a D.S., Clara, one does not take the repeats again, unless the music says so.', c(73, 'watch')),
  ('K', 'Otherwise we would be driving round that roundabout all day.', c(73, 'watch')),
  ('B', 'Until next time, Clara.', c(73, 'watch')),
  ('P', 'Bye, Butler! Bye, Your Majesties!', c(73, 'watch'))])])

NEW['E2'] = ('Touch: smooth, short, strong', [
 ('The secret', [
  ('P', 'This morning I tiptoed past my sleeping brother, then stamped all the way up the stairs.', c(79, 'lead')),
  ('B', 'Same feet, two different touches. And I suspect your brother woke up anyway.', c(79, 'lead')),
  ('P', 'He did. But can the same notes sound different too?', c(79, 'lead')),
  ('B', 'Completely different, Clara. Small marks tell your fingers how to touch the keys. A curve: join the notes, like pouring honey. That’s legato.', c(79, 'hero')),
  ('piano', 'E4_ D4_ C4_ D4*1.5', c(79, 'hero')),
  ('B', 'Dots: short and detached, like popcorn popping. That’s staccato.', c(79, 'hero')),
  ('piano', 'E4! D4! C4! D4!', c(79, 'hero')),
  ('P', 'Pop, pop, pop! I like that one.', c(79, 'hero')),
  ('B', 'Lines: hold the full length, leaning a little, like leaning on a friend’s shoulder. That’s tenuto. And arrows: a stronger start, the accent, like a door knock.', c(79, 'hero')),
  ('piano', 'mf:E4 mf:D4 mf:C4 mf:D4 | f:E4 p:D4 f:C4 p:D4', c(79, 'hero')),
  ('B', 'The secret in four pairs: curve, join. Dot, short. Line, hold. Arrow, strong.', c(79, 'secret'))]),
 ('Example: line, dot or arrow?', [
  ('B', 'Read the marks. How long are the first two Cs, the Gs, and the E with the arrow? Pause and think.', c(80, 'ex1')),
  ('pause', 4, c(80, 'ex1')),
  ('P', 'The Cs held their full length, the Gs short, like popcorn, and the E strong, like a knock, but still its full two beats.', c(80, 'ex1', reveal=True)),
  ('piano', 'C5 G4! G4! C5 | f:E5*2 C5*2', c(80, 'ex1', reveal=True))]),
 ('Slurs and phrases', [
  ('B', 'A curve over different notes is a slur: join them, then lift at its end, like a breath. A long slur over a whole line is a phrase: one musical sentence. You wouldn’t stop in the middle of a sentence to... breathe, would you?', c(80, 'xlate')),
  ('P', 'That was very annoying, Butler.', c(80, 'xlate')),
  ('B', 'Exactly my point. This part of Ode to Joy has two phrases. Lift your hand only at the end of each, like a singer taking a breath.', c(80, 'xlate')),
  ('piano', 'E4_ E4_ F4_ G4_ G4_ F4_ E4_ D4 | C4_ C4_ D4_ E4_ E4*1.5_ D4/2_ D4*2', c(80, 'xlate'))]),
 ('Example: which notes are short?', [
  ('B', 'Bar one has a curve. Bar two has dots, and one other mark. Which notes are short?', c(80, 'ex2')),
  ('pause', 4, c(80, 'ex2')),
  ('P', 'The two dotted Gs. The third G has an accent: strong, but full length.', c(80, 'ex2', reveal=True)),
  ('piano', 'C4_ D4_ E4_ F4 | G4! G4! f:G4 R', c(80, 'ex2', reveal=True)),
  ('B', 'Well read. An accent is loud, not short. Shouting doesn’t make a word shorter.', c(80, 'ex2', reveal=True))]),
 ('Two-note slurs', [
  ('B', 'A slur over just two notes is a little sigh, like “oh well”: drop into the first, then lift off the second, lighter and shorter. Drop, lift.', c(81, 'xlate')),
  ('piano', 'f:E4_ p:D4! | f:G4_ p:F4! | f:E4_ p:D4!', c(81, 'xlate')),
  ('P', 'Oh well. Oh well. Oh well. It sounds like someone who lost their sock.', c(81, 'xlate')),
  ('B', 'And some words describe the mood. Dolce, sweetly. Cantabile, singing. Leggiero, lightly. Maestoso, majestically.', c(81, 'xlate2')),
  ('Q', 'Maestoso is how I walk into a room.', c(81, 'xlate2')),
  ('B', 'Legato is walking: one foot leaves the ground as the other lands. Staccato is hopping on hot sand. Until next time, Clara.', c(81, 'think')),
  ('P', 'Bye, Butler!', c(81, 'think'))])])

NEW['E3'] = ('Speed words', [
 ('The secret', [
  ('P', 'When I’m late for school I run, and on Sundays I stroll.', c(82, 'lead')),
  ('B', 'Then you already know about tempo, Clara: the same walk at different speeds. Although I’d rather you weren’t late for school.', c(82, 'lead')),
  ('P', 'So how do I know how fast to play?', c(82, 'lead')),
  ('B', 'A word at the top of the music tells you, usually in Italian. Largo is very slow, like a tortoise after lunch. Adagio, slow. Andante, a walking pace. Moderato, moderate. Allegro, fast and lively. Presto, very fast, like a squirrel who has had too much coffee.', c(82, 'hero')),
  ('count', {'beats': 'X@60 x@60 x@60 x@60', 'say': '1 2 3 4'}, c(82, 'hero')),
  ('count', {'beats': 'X@92 x@92 x@92 x@92', 'say': '1 2 3 4'}, c(82, 'hero')),
  ('count', {'beats': 'X@138 x@138 x@138 x@138', 'say': '1 2 3 4'}, c(82, 'hero')),
  ('B', 'Adagio, Andante, Allegro. The numbers in the table are only a rough guide.', c(82, 'xlate'))]),
 ('The metronome mark', [
  ('B', 'Often there’s a number too. Crotchet equals seventy-six means seventy-six beats in one minute. Set a metronome to seventy-six: each click is one beat. A metronome is a very strict little friend who never gets tired.', c(83, 'xlate'))]),
 ('Example: crotchet equals sixty', [
  ('B', 'How fast is crotchet equals sixty? Pause and think.', c(83, 'ex1')),
  ('pause', 3, c(83, 'ex1')),
  ('P', 'Sixty beats! That must be very fast.', c(83, 'ex1', oops=True)),
  ('B', 'Sixty in a whole minute, Clara. How many seconds are there in a minute?', c(83, 'ex1')),
  ('P', 'Sixty beats in a minute, and a minute has sixty seconds. One beat every second! That’s a clock, not a race.', c(83, 'ex1', reveal=True)),
  ('count', {'beats': 'X@60 x@60 x@60 x@60', 'say': '1 2 3 4'}, c(83, 'ex1', reveal=True))]),
 ('Changing speed', [
  ('B', 'Words inside the music can change the speed. Ritardando: gradually slower, the beats further apart, like a wind-up toy running down. Rallentando, rall. for short, means the same. Accelerando: gradually faster. A tempo: back to the speed before. And the fermata, the pause: hold longer than written.', c(83, 'xlate2')),
  ('count', {'beats': 'X@100 x@96 x@90 x@82 X@72 x@62 x@52', 'say': '1 2 3 4 1 2 3'}, c(83, 'xlate2')),
  ('P', 'It sounds like it’s falling asleep.', c(83, 'xlate2'))]),
 ('Example: rall. and a tempo', [
  ('B', 'Where does it slow down, and where does it come back?', c(84, 'ex2')),
  ('pause', 3, c(84, 'ex2')),
  ('P', 'Bar one slows into the two Gs. At a tempo the first speed comes straight back.', c(84, 'ex2', reveal=True)),
  ('B', 'Straight back, no slow warming up. Like a cat that pretends it was never asleep.', c(84, 'ex2', reveal=True))]),
 ('Example: the fermata', [
  ('B', 'How long do you hold the minim with the fermata?', c(84, 'ex3')),
  ('pause', 3, c(84, 'ex3')),
  ('P', 'Longer than two beats, until it feels finished. Then go on.', c(84, 'ex3', reveal=True)),
  ('B', 'Like the deep breath before you blow out your birthday candles: everyone waits, and then the moment comes.', c(84, 'ex3', reveal=True)),
  ('B', 'Players often slow down into the end of Twinkle, Twinkle, then wait on the last note. A rit. is a car braking gently at the lights; a tempo is driving off again. Until next time, Clara.', c(84, 'yk')),
  ('P', 'Bye, Butler!', c(84, 'yk'))])])

NEW['E4'] = ('The pedals', [
 ('The secret', [
  ('P', 'When I clap in the big school hall, the sound keeps going after my hands stop. Like a ghost clapping back.', c(85, 'lead')),
  ('B', 'A friendly ghost, I hope. A piano can do that too, with a little help from your foot.', c(85, 'lead')),
  ('P', 'So that’s what the pedals are for! I thought they were for driving the piano.', c(85, 'lead')),
  ('B', 'Sadly, it doesn’t go anywhere. Most pianos have three pedals, Clara. The left one, the soft pedal, makes the sound gentler. The right one, the sustain pedal, keeps the notes ringing after your fingers let go.', c(85, 'hero')),
  ('B', 'Inside the piano, most strings have a felt damper resting on them, like a finger on your lips saying shh. Press a key and its damper lifts; let go, and the damper stops the string. The sustain pedal lifts every damper at once, so the strings ring on.', c(85, 'xlate')),
  ('piano', '[C4 E4 G4]', c(85, 'xlate')),
  ('B', 'The soft pedal is written u.c., una corda, and let up at t.c. The sustain pedal is written Ped.', c(85, 'xlate2'))]),
 ('Example: which pedal?', [
  ('B', 'Which pedal is Ped.? Which is u.c.? And what does t.c. ask? Pause and think.', c(86, 'ex1')),
  ('pause', 4, c(86, 'ex1')),
  ('P', 'Ped. is the soft pedal?', c(86, 'ex1', oops=True)),
  ('B', 'Not quite, Clara. The soft pedal is the left one, written u.c. Ped. is the right one, and it keeps the notes ringing.', c(86, 'ex1')),
  ('P', 'Ped. is the right pedal, u.c. the left, and t.c. means let the left pedal up.', c(86, 'ex1', reveal=True))]),
 ('Writing the sustain pedal', [
  ('B', 'Down at Ped., up at the star. Or a bracket: the notch is a quick change, up and down again. Heel on the floor, press with the ball of your foot, like gently squeezing a soft sponge. Play first, then pedal.', c(86, 'xlate'))]),
 ('Example: down and up', [
  ('B', 'Where does the pedal go down, where does it change, and where does it come up?', c(86, 'ex2')),
  ('pause', 4, c(86, 'ex2')),
  ('P', 'Down on the first C, changed at the F, and up at the end.', c(86, 'ex2', reveal=True)),
  ('piano', 'C4 E4 G4 C5 | F4 A4 C5 F5', c(86, 'ex2', reveal=True))]),
 ('Changing the pedal', [
  ('B', 'At every new chord, change the pedal just after you play it: up, and straight down again. Each chord rings clean, and they still join. Forget to change, and the chords pile up like muddy footprints on a clean floor.', c(87, 'xlate')),
  ('piano', '[C4 E4 G4] [F4 A4 C5] [G4 B4 D5] [C4 E4 G4]', c(87, 'xlate')),
  ('B', 'Try it: play C, E and G together, press the right pedal and take your hands off. The chord keeps sounding. Lift the pedal: silence.', c(87, 'try10')),
  ('P', 'Magic! My hands are gone and the music is still there.', c(87, 'try10')),
  ('B', 'The sustain pedal holds a door open: every note that walks in stays in the room until you let the door shut. Until next time, Clara.', c(87, 'think')),
  ('P', 'Bye, Butler!', c(87, 'think'))])])

NEW['E5'] = ('Ornaments', [
 ('The secret', [
  ('P', 'Grandma puts sprinkles on top of my birthday cake. The cake is the same, but it sparkles.', c(88, 'lead')),
  ('B', 'Music has sprinkles too. Look at this one.', c(88, 'lead')),
  ('P', 'What’s that little t r above the note? Is it a typo?', c(88, 'lead')),
  ('B', 'Not a typo, a trill, Clara. An ornament: a small sign that stands for a quick burst of notes around the main note. Like a bird showing off.', c(88, 'hero')),
  ('piano', 'D5/4 E5/4 D5/4 E5/4 D5/4 E5/4 D5/4 E5/4 C5*2', c(88, 'hero')),
  ('B', 'Ornaments borrow the notes next door, one letter up or down, like borrowing sugar from the neighbours. On D, the note above is E and the note below is C.', c(88, 'xlate')),
  ('piano', 'D4 E4 D4 C4 D4', c(88, 'xlate', seq=['main', 'above', 'main', 'below', 'main']))]),
 ('Written and played', [
  ('B', 'A trill goes back and forth with the note above. An upper mordent is one quick flick: note, above, note. Like a wink.', c(88, 'xlate2')),
  ('piano', 'D5/4 E5/4 D5*1.5 C5*2', c(88, 'xlate2')),
  ('B', 'A lower mordent uses the note below. And a turn goes above, note, below, note, like a little twirl in a dance.', c(89, 'xlate')),
  ('piano', 'D5/4 C5/4 D5*1.5 | E5/4 D5/4 C5/4 D5*1.25 C5*2', c(89, 'xlate'))]),
 ('Example: a lower mordent on G', [
  ('B', 'A lower mordent on G. Which next-door note does it borrow? Pause and think.', c(89, 'ex1')),
  ('pause', 3, c(89, 'ex1')),
  ('P', 'G, A, G!', c(89, 'ex1', oops=True)),
  ('B', 'That’s the upstairs neighbour, Clara: an upper mordent. A lower mordent knocks on the door downstairs.', c(89, 'ex1')),
  ('P', 'The note below G: F. G, F, G!', c(89, 'ex1', reveal=True)),
  ('piano', 'G4/4 F4/4 G4*1.5', c(89, 'ex1', reveal=True))]),
 ('Example: the trill', [
  ('B', 'Which note has the trill, and what is its next-door note above?', c(89, 'ex2')),
  ('pause', 3, c(89, 'ex2')),
  ('P', 'The E, and the note above is F. E, F, E, F, quickly, for two beats.', c(89, 'ex2', reveal=True)),
  ('B', 'Going further: in music from the time of Bach and Handel, a trill usually starts on the note above. You’ll meet that later.', c(89, 'xlate2'))]),
 ('Tiny notes', [
  ('B', 'A tiny note before the main note borrows a moment from it. With a slash, it’s crushed in as fast as you can, like a little hiccup: an acciaccatura. Without a slash, it leans, taking about half the time, like a polite bow: an appoggiatura.', c(90, 'xlate')),
  ('P', 'Those words are longer than the notes!', c(90, 'xlate')),
  ('B', 'Ha! Listen: first the hiccup, then the bow.', c(90, 'xlate')),
  ('piano', 'D5/8 C5*2 | D5 C5', c(90, 'xlate')),
  ('B', 'Now let’s add a mordent to the first D of the Minuet in G: one quick flick, and the beat doesn’t move.', c(90, 'yk')),
  ('piano', 'D5/4 E5/4 D5/2 G4/2 A4/2 B4/2 C5/2 | D5 G4 G4', c(90, 'yk')),
  ('B', 'Learn the plain notes in time first, then add the sparkle. Cake first, sprinkles after. Until next time, Clara.', c(90, 'think')),
  ('P', 'Bye, Butler!', c(90, 'think'))])])

# ---- Part IV, Scales and keys (her 11 Nov: "다음 거 진행해줘"): audio for S1-S5 in the same storybook style ----
CM = 'C4 D4 E4 F4 G4 A4 B4 C5'
NEW['S1'] = ('Major scales', [
 ('The secret', [
  ('B', 'Welcome to Part Four, Clara: scales and keys. Notes, it turns out, live in families.', c(93, 'h:Major scales')),
  ('P', 'Like my family? We are very noisy.', c(93, 'lead')),
  ('B', 'Some scales are noisy too. A scale climbs from a home note, the key note, up to the next note with the same name, using every letter once. Like a staircase from the ground floor to the first floor.', c(93, 'lead')),
  ('B', 'Here is the most famous staircase of all: C major.', c(93, 'hero')),
  ('piano', CM, c(93, 'hero', seq=['#0', '#2', '#4', '#6', '#8', '#10', '#12', '#14'])),
  ('P', 'Do re mi fa so la ti do! I know that one.', c(93, 'hero')),
  ('B', 'Everybody does. Now look at the steps between the notes. Most of them are big steps, tones. But two of them are tiny, semitones. Like a staircase where two of the steps are only half as high.', c(93, 'hero')),
  ('P', 'I’d trip on those!', c(93, 'hero')),
  ('B', 'Everyone does at first. Here is the secret, and it works on any note at all: tone, tone, semitone, tone, tone, tone, semitone.', c(93, 'secret')),
  ('P', 'Tone, tone, semitone, tone, tone, tone, semitone. It sounds like a secret knock on a door.', c(93, 'secret')),
  ('B', 'It is exactly that. Knock it right, and the door to any major key opens. A tone has one key between. A semitone has no key between: the very next key, best friends.', c(93, 'rule'))]),
 ('Example: where are the short steps?', [
  ('B', 'Play C up to C on the white keys, numbering the notes one to eight. Then look between each pair for a black key. Which pairs have nothing between them? Pause and look.', c(93, 'ex1')),
  ('pause', 4, c(93, 'ex1')),
  ('P', 'Three to four, E and F. And seven to eight, B and C. Our old best friends!', c(93, 'ex1', reveal=True)),
  ('piano', CM, c(93, 'ex1', reveal=True, seq=['#8', '#9', '#10', '#11', '#12', '#13', '#14', '#15'])),
  ('B', 'Exactly. Three-four and seven-eight: the two short steps of every major scale.', c(93, 'ex1', reveal=True))]),
 ('Example: build G major', [
  ('B', 'Now let’s build a new staircase, starting on G. Write the letters G to G: G, A, B, C, D, E, F, G.', c(94, 'ex2')),
  ('B', 'Check the top. Six to seven must be a tone, seven to eight a semitone. But E to F has nothing between: too short. So one key has to move. Which way, and what is it called now?', c(94, 'ex2')),
  ('pause', 4, c(94, 'ex2')),
  ('P', 'Move F one key right... so it’s G flat!', c(94, 'ex2', oops=True)),
  ('B', 'Right key, wrong name. Every letter appears once in a scale, and we already have a G. So it must be called F something.', c(94, 'ex2')),
  ('P', 'F sharp! G major is G, A, B, C, D, E, F sharp, G, with one sharp.', c(94, 'ex2', reveal=True)),
  ('piano', 'G4 A4 B4 C5 D5 E5 F#5 G5', c(94, 'ex2', reveal=True)),
  ('B', 'Hear how F sharp leans up into G, like someone hurrying up the last stair to get home.', c(94, 'ex2', reveal=True))]),
 ('Example: build D major', [
  ('B', 'D to D now. Check every step against the secret knock. Two steps are too short this time. Which ones?', c(94, 'ex3')),
  ('pause', 4, c(94, 'ex3')),
  ('P', 'E to F, and B to C. Move F and C one key right: F sharp and C sharp!', c(94, 'ex3', reveal=True)),
  ('piano', 'D4 E4 F#4 G4 A4 B4 C#5 D5', c(94, 'ex3', reveal=True)),
  ('B', 'D major: two sharps. You’re building staircases like a carpenter.', c(94, 'ex3', reveal=True))]),
 ('Example: build F major', [
  ('B', 'Now F to F. Check three to four: it must be a semitone. But A to B has a key between. Too big!', c(94, 'ex4')),
  ('P', 'So this time I move B one key left, to make the step smaller?', c(94, 'ex4')),
  ('B', 'And what is it called now?', c(94, 'ex4')),
  ('pause', 3, c(94, 'ex4')),
  ('P', 'B flat! F major: F, G, A, B flat, C, D, E, F. One flat.', c(94, 'ex4', reveal=True)),
  ('piano', 'F4 G4 A4 Bb4 C5 D5 E5 F5', c(94, 'ex4', reveal=True))]),
 ('Example: build A major', [
  ('B', 'One more, a big one: A to A. Two steps are too short, and the top step is too big. Fix all three by moving a key one to the right.', c(95, 'ex5')),
  ('pause', 5, c(95, 'ex5')),
  ('P', 'C sharp, F sharp and G sharp! The key of A major has three sharps.', c(95, 'ex5', reveal=True)),
  ('piano', 'A4 B4 C#5 D5 E5 F#5 G#5 A5', c(95, 'ex5', reveal=True)),
  ('B', 'Three sharps, and still the very same knock: tone, tone, semitone, tone, tone, tone, semitone.', c(95, 'ex5', reveal=True))]),
 ('Game and try it', [
  ('B', 'Game time: spot the wrong note. Each of these three scales has one note that breaks the knock. Which one, and what should it be? Pause and look.', c(95, 'game')),
  ('pause', 6, c(95, 'game')),
  ('P', 'One: F should be F sharp. Two: C should be C sharp. Three: B should be B flat.', c(95, 'game', reveal=True)),
  ('B', 'Three out of three. Now one finger, C to C, and say the knock as you go.', c(95, 'try10')),
  ('piano', CM, c(95, 'try10', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7'])),
  ('B', 'And something you know: Joy to the World. The first line is the C major scale, from the top all the way down.', c(95, 'yk')),
  ('piano', 'C5*2 B4*1.5 A4/2 G4*3 F4 E4*2 D4*2 C4*3', c(95, 'yk', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7'])),
  ('P', 'Joy to the world! It walks all the way downstairs.', c(95, 'yk')),
  ('Q', 'And mind the traps, Clara: every letter only once, and never forget the short step at the very top.', c(95, 'watch')),
  ('B', 'A major scale is a secret knock: learn the rhythm of the steps, and every door opens. Until next time, Clara.', c(95, 'watch')),
  ('P', 'Bye, Butler! Bye, Your Majesty!', c(95, 'watch'))])])

NEW['S2'] = ('Minor scales', [
 ('The secret', [
  ('P', 'Butler, my friend says minor music sounds sad. Is that true?', c(96, 'h:Minor scales')),
  ('B', 'Often a bit darker, yes. Same house, but with the curtains drawn. Here is how to find a minor scale: start from the major scale on the same key note, and move three notes, the third, the sixth and the seventh, one key down.', c(96, 'lead')),
  ('B', 'Listen. First C major, sunny.', c(96, 'hero')),
  ('piano', CM, c(96, 'hero', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7'])),
  ('B', 'Then C minor: three, six and seven one key lower.', c(96, 'hero')),
  ('piano', 'C4 D4 Eb4 F4 G4 Ab4 Bb4 C5', c(96, 'hero', seq=['#16', '#17', '#18', '#19', '#20', '#21', '#22', '#23'])),
  ('P', 'Ooh. Same home, but it’s raining now.', c(96, 'hero')),
  ('B', 'Beautifully put. That is the secret: minor is the major on the same note, with three, six and seven one key lower. We call that the natural minor.', c(96, 'secret'))]),
 ('Three kinds of minor', [
  ('B', 'Now, the minor scale has three outfits. The natural minor, as you just heard. The harmonic minor: the natural minor, with the seventh raised again. And the melodic minor: going up, six and seven raised; coming down, back to the natural minor.', c(96, 'rule')),
  ('P', 'Three outfits? Minor scales are very fashionable.', c(96, 'rule')),
  ('B', 'Very. Let’s hear them all on A. First natural: all white keys, from A to A.', c(96, 'vx')),
  ('piano', 'A3 B3 C4 D4 E4 F4 G4 A4', c(96, 'vx')),
  ('B', 'Harmonic: the seventh raised again, G sharp. Hear it lean towards home, like a dog pulling on the lead when it sees its house.', c(97, 'vx')),
  ('piano', 'A3 B3 C4 D4 E4 F4 G#4 A4', c(97, 'vx')),
  ('B', 'And melodic: going up, F sharp and G sharp; coming down, back to G and F. It puts its party shoes on to climb the stairs, and takes them off to come down.', c(97, 'vx2')),
  ('piano', 'A3 B3 C4 D4 E4 F#4 G#4 A4 | G4 F4 E4 D4 C4 B3 A3', c(97, 'vx2'))]),
 ('Example: build C natural minor', [
  ('B', 'Build C natural minor. Start from C major: C, D, E, F, G, A, B, C. The question marks are three, six and seven. Move each one key left, and name the keys you land on.', c(97, 'ex1')),
  ('pause', 5, c(97, 'ex1')),
  ('P', 'E flat, A flat and B flat. C natural minor: C, D, E flat, F, G, A flat, B flat, C.', c(97, 'ex1', reveal=True)),
  ('piano', 'C4 D4 Eb4 F4 G4 Ab4 Bb4 C5', c(97, 'ex1', reveal=True))]),
 ('Example: build A harmonic minor', [
  ('B', 'Now A harmonic minor. Start from A natural minor, all white keys. Take note seven, and raise it one key. What is it?', c(97, 'ex2')),
  ('pause', 3, c(97, 'ex2')),
  ('P', 'G sharp! A, B, C, D, E, F, G sharp, A.', c(97, 'ex2', reveal=True)),
  ('piano', 'A3 B3 C4 D4 E4 F4 G#4 A4', c(97, 'ex2', reveal=True)),
  ('B', 'Try it yourself: play C major, then play it again with E, A and B one key lower. Same home, new colour: bright, then dark.', c(97, 'try10'))]),
 ('Example: build D natural minor', [
  ('B', 'Last one. This is D major, with F sharp and C sharp. The question marks are notes three, six and seven. Move each one key left. What are they now?', c(98, 'ex3')),
  ('pause', 5, c(98, 'ex3')),
  ('P', 'F sharp goes down to F. B goes down to B flat. And C sharp goes down to C.', c(98, 'ex3', reveal=True)),
  ('piano', 'D4 E4 F4 G4 A4 Bb4 C5 D5', c(98, 'ex3', reveal=True)),
  ('B', 'D natural minor: D, E, F, G, A, B flat, C, D. One flat.', c(98, 'ex3', reveal=True))]),
 ('Game and Greensleeves', [
  ('B', 'Game: which minor? Nothing raised. The seventh raised. Sixth and seventh raised going up, lowered coming down. Name each one.', c(98, 'game')),
  ('pause', 4, c(98, 'game')),
  ('P', 'Natural, harmonic, and melodic. The one with the party shoes.', c(98, 'game', reveal=True)),
  ('B', 'And here is a very old tune: Greensleeves. A minor, with a G sharp, the raised seventh, leaning hard up to A.', c(98, 'yk')),
  ('piano', 'A4 C5*2 D5 E5*1.5 F5/2 E5 D5*2 B4 G4*1.5 A4/2 B4 C5*2 A4 A4*1.5 G#4/2 A4 B4*2 G#4 E4*2', c(98, 'yk')),
  ('P', 'It sounds like a knight riding through a misty forest.', c(98, 'yk')),
  ('K', 'It was a favourite at my great-great-great-grandfather’s court. Mind you, he played the lute rather badly.', c(98, 'yk')),
  ('B', 'Two traps to step around: only three, six and seven move, nothing else. And the melodic minor takes its party shoes off on the way down. Until next time, Clara.', c(98, 'watch')),
  ('P', 'Bye, Butler! Bye, Your Majesty!', c(98, 'watch'))])])

NEW['S3'] = ('Keys and key signatures', [
 ('The secret', [
  ('P', 'Butler, in my new piece every single F has a sharp. Did the composer have a stuck keyboard?', c(99, 'h:Keys and key signatures')),
  ('B', 'Ha! Even worse: imagine writing F sharp fifty times. So composers write it once at the start of each line instead. That is the key signature.', c(99, 'lead')),
  ('B', 'Look: one sharp, on the F line, right next to the clef. From then on, every F in the piece plays F sharp, high or low.', c(99, 'hero', seq=['#0', '#1', '#2'])),
  ('piano', 'G4 A4 B4 C5 D5 E5 F#5 G5', c(99, 'hero')),
  ('P', 'So it’s like a rule for the whole piece.', c(99, 'secret')),
  ('B', 'Exactly. That is the secret: the key signature says, once, at the start, which notes are always sharp or flat. Think of a dress code on a party invitation: written once at the top, it applies to every guest, all night.', c(99, 'secret'))]),
 ('The order of sharps and flats', [
  ('B', 'And the sharps always arrive in the same order, like children lining up for lunch: F, C, G, D, A, E, B.', c(99, 'two')),
  ('P', 'How do I remember that?', c(99, 'two')),
  ('B', 'With a little story: Father Charles Goes Down And Ends Battle.', c(99, 'two')),
  ('K', 'Father Charles was my cousin. He ended a great many battles. Mostly by falling asleep in them.', c(99, 'two')),
  ('B', 'And the flats are the sharps backwards: B, E, A, D, G, C, F. Battle Ends And Down Goes Charles’ Father.', c(99, 'sm')),
  ('P', 'Poor Charles’ father.', c(99, 'sm'))]),
 ('One signature, two keys', [
  ('B', 'Here is a surprise. Every key signature also belongs to a minor key, its relative minor. They are like two cousins who share one wardrobe: exactly the same notes. To find the relative minor, go down a minor third: two keys between, then land.', c(99, 'two2')),
  ('P', 'So C major and the key of A minor share a wardrobe?', c(99, 'two2')),
  ('B', 'They do. All white keys, both of them.', c(99, 'two2'))]),
 ('Example: which notes are sharp?', [
  ('B', 'Look at this key signature. Count the sharps, then name them in order. The first sharp is always F. Which keys turn black for the whole piece?', c(100, 'ex1')),
  ('pause', 4, c(100, 'ex1')),
  ('P', 'Two sharps: F sharp and C sharp. Every F and every C, high or low!', c(100, 'ex1', reveal=True))]),
 ('Example: the relative minor', [
  ('B', 'Find the relative minor of C major. Start on C, the key note. Count two keys between, going down: B is one, B flat is two. Then the next key is the answer.', c(100, 'ex2')),
  ('pause', 3, c(100, 'ex2')),
  ('P', 'The note A! The relative minor of C major is the key of A minor.', c(100, 'ex2', reveal=True)),
  ('B', 'And F major? Start on F. Two keys between, going down: E, then E flat. And land.', c(100, 'ex3')),
  ('pause', 3, c(100, 'ex3')),
  ('P', 'D! D minor, which shares F major’s one flat, B flat.', c(100, 'ex3', reveal=True))]),
 ('Example: which notes are flat?', [
  ('B', 'Now a flat signature. Count the flats, and name them in order. The first flat is always B.', c(101, 'ex4')),
  ('pause', 4, c(101, 'ex4')),
  ('P', 'Three flats: B flat, E flat, A flat. Every B, E and A in the piece.', c(101, 'ex4', reveal=True)),
  ('B', 'Game: what comes next? Sharps F, C, G... Flats B, E... The first flat? The second sharp?', c(101, 'gt2')),
  ('pause', 5, c(101, 'gt2')),
  ('P', 'D, then A flat. The first flat is B flat, and the second sharp is C sharp.', c(101, 'gt2', reveal=True))]),
 ('You know this', [
  ('B', 'The Minuet in G again. One sharp in the key signature: every F is F sharp, like the one just before the top G. One sharp, and the piece ends on G: G major.', c(101, 'yk')),
  ('piano', 'D5 G4/2 A4/2 B4/2 C5/2 D5 G4 G4 | E5 C5/2 D5/2 E5/2 F#5/2 G5 G4 G4', c(101, 'yk')),
  ('P', 'I heard the F sharp, right before the top!', c(101, 'yk')),
  ('B', 'A dress code, written once. Only an accidental, a word to one guest, overrules it, and only until the bar line. And remember to glance at the key signature at the start of every line. Until next time, Clara.', c(101, 'think')),
  ('P', 'Bye, Butler!', c(101, 'think'))])])

NEW['S4'] = ('Finding the key', [
 ('The secret', [
  ('P', 'Butler, if one key signature belongs to two keys, how do I know which one my piece is in?', c(102, 'h:Finding the key')),
  ('B', 'Ah. Now we become detectives, Clara. The key signature narrows it down to two suspects: a major key and its relative minor. Two quick rules find the major. A minor third down finds the minor. Then the music itself tells you which suspect did it.', c(102, 'lead')),
  ('P', 'Ooh, a mystery! Where’s my magnifying glass?', c(102, 'lead')),
  ('B', 'Here is the secret. For sharps: find the last sharp, then go the very next key up. For flats: the second-last flat is the key.', c(102, 'secret')),
  ('B', 'Look: three sharps. The last one is G sharp. The very next key up is A. Three sharps: A major.', c(102, 'hero')),
  ('piano', 'G#4 A4', c(102, 'hero', seq=['#5', '#6'])),
  ('P', 'The last sharp is like a doorman, and the key lives one step up.', c(102, 'hero')),
  ('B', 'A very good doorman. And flats: B flat, E flat, A flat. The second-last is E flat, so E flat major. One flat alone has no second-last, so just remember it: F major.', c(102, 'fk')),
  ('B', 'And to find the minor suspect: from A, two keys between, G sharp and G, then land on F sharp. Three sharps is A major or F sharp minor.', c(102, 'fk2'))]),
 ('Clue notes', [
  ('B', 'So how do we catch the culprit? Minor keys leave fingerprints. A minor key usually raises its seventh note. That raised note is the clue. The key of A minor leaves G sharps all over the place. E minor leaves D sharps. D minor, C sharps.', c(102, 'ht')),
  ('P', 'So if I find G sharps everywhere and no sharps in the signature, it’s probably A minor.', c(102, 'ht')),
  ('B', 'Elementary, my dear Clara.', c(102, 'ht'))]),
 ('Example: name the major key', [
  ('B', 'Sharps. Find the last sharp, the one furthest right. Name it, then go the very next key up.', c(103, 'ex1')),
  ('pause', 4, c(103, 'ex1')),
  ('P', 'The last sharp is C sharp. The next key up is D: D major!', c(103, 'ex1', reveal=True)),
  ('B', 'Now flats. Which flat names the key?', c(103, 'ex2')),
  ('pause', 3, c(103, 'ex2')),
  ('P', 'The last one, E flat. So E flat major!', c(103, 'ex2', oops=True)),
  ('B', 'Careful, detective. For flats it’s the second-last, not the last.', c(103, 'ex2')),
  ('P', 'B flat, E flat: the second-last is B flat. B flat major.', c(103, 'ex2', reveal=True)),
  ('B', 'Case closed.', c(103, 'ex2', reveal=True))]),
 ('Example: major or minor?', [
  ('B', 'One sharp: G major, or E minor a minor third below. Now look for a sharp that is not in the signature. Whose raised seventh is it? And look at the last note.', c(103, 'ex3')),
  ('pause', 5, c(103, 'ex3')),
  ('P', 'D sharps all over the place, and it ends on E. E minor, not G major!', c(103, 'ex3', reveal=True)),
  ('B', 'Game: name the major key. Two sharps, four sharps, one flat, three flats.', c(103, 'game')),
  ('pause', 5, c(103, 'game')),
  ('P', 'D, E, F, and E flat.', c(103, 'game', reveal=True))]),
 ('Example: a minor key from its clue', [
  ('B', 'Two flats: B flat major, or its relative minor. Count two keys between going down from B flat: A, then A flat, and land. Which minor key is it, and what is its seventh?', c(104, 'ex4')),
  ('pause', 5, c(104, 'ex4')),
  ('P', 'G minor! Its seventh is F, and if the piece is full of F sharps, it’s minor.', c(104, 'ex4', reveal=True)),
  ('B', 'Try it: three sharps. Say F, C, G, and stop. The last one is G sharp. The next key up is A. Three sharps is A major. Now try two sharps, and four.', c(104, 'try10'))]),
 ('The detective’s method', [
  ('B', 'So, the detective’s method for any new piece. One: the key signature gives you the major key, and its relative minor a minor third below. Two: look for clue notes, the minor key’s raised seventh. Three: look at the last bass note. Pieces nearly always end at home, on the key note.', c(104, 'howto')),
  ('B', 'And you know this one: Für Elise. No key signature, a G sharp as the clue, and the music keeps coming home to A.', c(104, 'yk')),
  ('piano', 'E5/2 D#5/2 E5/2 D#5/2 E5/2 B4/2 D5/2 C5/2 A4 | C4/2 E4/2 A4/2 B4 | E4/2 G#4/2 B4/2 C5 | E4/2 E5/2 D#5/2 E5/2 D#5/2 E5/2 B4/2 D5/2 C5/2 A4*2', c(104, 'yk')),
  ('P', 'It keeps landing on A. The key of A minor!', c(104, 'yk')),
  ('B', 'Well detected. The D sharp at the start is just a passing visitor; the G sharp a moment later is the real clue, and home is A.', c(104, 'yk')),
  ('B', 'Detective work: the key signature narrows it to two suspects; the clue note and the last note name the culprit. Until next time, Clara.', c(104, 'think')),
  ('P', 'Bye, Butler! Case closed.', c(104, 'think'))])])

NEW['S5'] = ('The circle of fifths', [
 ('The secret', [
  ('P', 'Butler, what is that giant clock on the page? Is it time for lunch?', c(105, 'h:The circle of fifths')),
  ('B', 'It’s always nearly time for lunch with you. But no: that is the circle of fifths, all the keys on one clock face. C major sits at twelve o’clock, with no sharps or flats.', c(105, 'lead')),
  ('B', 'Here is the secret. Go right round the clock, and each key has one more sharp. Go left, and each key has one more flat.', c(105, 'secret')),
  ('B', 'Right from C: G, one sharp. D, two. A, three. E, four. And so on.', c(105, 'hero', seq=['C', 'G', 'D', 'A', 'E'])),
  ('piano', 'C4 G4 D5 A5 E6', c(105, 'hero', seq=['C', 'G', 'D', 'A', 'E'])),
  ('P', 'Every key is one sharp more, like climbing the stairs of a lighthouse!', c(105, 'hero')),
  ('B', 'And at the bottom of the clock the two sides meet, where F sharp and G flat share one spot: the same key, two names.', c(105, 'hero', seq=['F♯', 'G♭'])),
  ('P', 'Enharmonic! I remember that grand word.', c(105, 'hero'))]),
 ('How to read the clock', [
  ('B', 'The outer ring shows the major keys. The inner ring shows their relative minors, cuddled up just inside. And outside the circle: how many sharps or flats.', c(105, 'two')),
  ('B', 'And neighbours on the clock are close friends: they share all but one note. That is why music moves between them so easily, like popping next door for a cup of tea.', c(105, 'two')),
  ('B', 'Now, why is it called the circle of fifths? Each step right is a fifth up. Count the notes: C, D, E, F, G. And G is the next key round.', c(105, 'rule')),
  ('piano', 'C4 D4 E4 F4 G4', c(105, 'rule'))]),
 ('Example: sharps and flats round the circle', [
  ('B', 'How many sharps in A major? Start at C at the top, no sharps. Go right one step at a time, and count the steps to A.', c(106, 'ex1')),
  ('pause', 4, c(106, 'ex1')),
  ('P', 'G, D, A. Three steps right: three sharps, F sharp, C sharp, G sharp.', c(106, 'ex1', reveal=True)),
  ('B', 'And how many flats in E flat major? Start at C again.', c(106, 'ex2')),
  ('pause', 4, c(106, 'ex2')),
  ('P', 'Right: G, D, A...', c(106, 'ex2', oops=True)),
  ('B', 'Whoa, wrong way round, Clara! Right adds sharps. For flats, we go left.', c(106, 'ex2')),
  ('P', 'Oops. Left: F, B flat, E flat. Three steps left: three flats, B flat, E flat, A flat.', c(106, 'ex2', reveal=True))]),
 ('Example: why do G and D sound so close?', [
  ('B', 'G major and D major are next-door neighbours on the clock. Compare their notes. Which letters are the same, and which one changes?', c(106, 'ex3')),
  ('piano', 'G4 A4 B4 C5 D5 E5 F#5 G5 | D4 E4 F#4 G4 A4 B4 C#5 D5', c(106, 'ex3')),
  ('pause', 4, c(106, 'ex3')),
  ('P', 'Six notes are the same. Only C becomes C sharp!', c(106, 'ex3', reveal=True)),
  ('B', 'One step round the circle changes just one note. Like moving to the house next door: same street, same shops, just a different number on the gate.', c(106, 'ex3', reveal=True))]),
 ('Example: the minor inside D', [
  ('B', 'Find the minor inside D. Start on D, on the outer ring. Count two keys between, going down: C sharp is one, C is two. The next key is the answer. It sits on the inner ring, just inside D.', c(107, 'ex4')),
  ('pause', 4, c(107, 'ex4')),
  ('P', 'B! B minor, D major’s relative minor. Both have two sharps.', c(107, 'ex4', reveal=True)),
  ('B', 'Game: neighbours on the clock. Right of D? Left of C? Opposite C? And inside G?', c(107, 'game')),
  ('pause', 6, c(107, 'game')),
  ('P', 'Right of D is A. Left of C is F. Opposite C is F sharp, or G flat. And inside G is E minor.', c(107, 'game', reveal=True))]),
 ('Try it', [
  ('B', 'Walk the circle with one finger: C, G, D, A, going up a fifth each time.', c(107, 'try10')),
  ('piano', 'C4 G4 D5 A5', c(107, 'try10')),
  ('P', 'I just walked three steps round the clock!', c(107, 'try10')),
  ('B', 'And to learn the circle by heart: right, out loud: C, G, D, A, E, B, F sharp. Left: C, F, B flat, E flat, A flat, D flat, G flat. And check yourself: the number of steps from C is the number of sharps or flats.', c(107, 'howto')),
  ('Q', 'The King and I recite it every morning at breakfast.', c(107, 'howto')),
  ('K', 'Mostly to stop the toast going cold. Never go the wrong way round, Clara.', c(107, 'watch')),
  ('B', 'The circle of fifths is a map of every key, with the neighbours side by side. Until next time, Clara.', c(107, 'watch')),
  ('P', 'Bye, Butler! Bye, Your Majesties!', c(107, 'watch'))])])
for _k in ('S1', 'S2', 'S3', 'S4', 'S5'): CH[_k] = NEW[_k]
