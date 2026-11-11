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
  ('piano', 'C4 C4 G4 G4 A4 A4 G4*2 F4 F4 E4 E4 D4 D4 C4*2', c(28, 'yk')),
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
  ('piano', 'C4 D4 E4 C4 C4 D4 E4 C4 E4 F4 G4*2 E4 F4 G4*2 | C3 D3 E3 C3 C3 D3 E3 C3 E3 F3 G3*2 E3 F3 G3*2', c(31, 'yk')),
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
  ('piano', 'E4 D4 C4 D4 E4 E4 E4*2 D4 D4 D4*2 E4 G4 G4*2 E4 D4 C4 D4 E4 E4 E4 E4 D4 D4 E4 D4 C4*4', c(35, 'yk')),
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
  ('B', 'A very thin disguise. And one rule to remember: a sign belongs to one line or space. It changes only that line or space, in that octave, and only until the bar line. The same letter in another octave stays as it is.', c(40, 'xlate')),
  ('G', 'Hello, hello! Sorry I’m late. I’m the Guest. I pop into a bar wearing my sharp hat, or my flat one, and everyone on my line or space wears it too.', c(40, 'xlate')),
  ('P', 'And how long do you stay?', c(40, 'xlate')),
  ('G', 'Until the bar line, darling. That’s the front door. Then I’m off, and the next bar is plain again. And when I take my hat off, that’s a natural.', c(40, 'xlate'))]),
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
  ('B', 'Ah, that one catches everybody. Remember our Guest: she leaves at the bar line, and takes her hat with her. Which side of the bar line is this F?', c(40, 'ex2')),
  ('P', 'The other side. The Guest has gone home: plain F again!', c(40, 'ex2', reveal=True)),
  ('G', 'I never stay past the bar line. It’s a rule.', c(40, 'ex2', reveal=True)),
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
  ('piano', 'E5/2 D#5/2 E5/2 D#5/2 E5/2 B4/2 D5/2 C5/2 A4 | C4/2 E4/2 A4/2 B4 | E4/2 G#4/2 B4/2 C5 | E4/2 E5/2 D#5/2 E5/2 D#5/2 E5/2 B4/2 D5/2 C5/2 A4*2', c(41, 'yk')),
  ('B', 'Look closely: the sharp is written again in the new bar, because the bar line wiped it out. And later the D has a natural sign, so it’s plain D again.', c(41, 'yk')),
  ('P', 'The Guest left at the bar line and came back in the next bar. Then she took her hat off.', c(41, 'yk')),
  ('G', 'Beethoven invited me twice. I was very flattered.', c(41, 'yk')),
  ('B', 'Your mission: play E and D sharp back and forth, then find F sharp and B flat in three different places on the piano. Until next time, Clara.', c(41, 'think')),
  ('P', 'Bye, Butler!', c(41, 'think'))])])

NEW['P7'] = ('Counting intervals', [
 ('The secret', [
  ('B', 'Clara, a question before we start. Who is your best friend?', c(42, 'h:Counting intervals')),
  ('P', 'Mia! We do everything together.', c(42, 'lead')),
  ('B', 'And when you and Mia sit together in class, is anyone sitting between you?', c(42, 'lead')),
  ('P', 'No way. We sit right next to each other.', c(42, 'lead')),
  ('B', 'That is a semitone: two keys right next to each other, with nobody between. The smallest step on the piano.', c(42, 'secret')),
  ('B', 'On the white keys, two pairs are best friends like you and Mia: E and F, with no black key between them.', c(42, 'hero', lab=['#1', '#2'])),
  ('piano', 'E4 F4', c(42, 'hero', seq=['#1', '#2'])),
  ('B', 'And B and C. Nobody between: a semitone.', c(42, 'hero', lab=['#5', '#6'])),
  ('piano', 'B4 C5', c(42, 'hero', seq=['#5', '#6'])),
  ('B', 'Now C and D. Look: a black key sits between them, C sharp. That is like one classmate sitting between you and Mia. One key between: a tone. Two semitones make a tone.', c(42, 'hero', lab=['#8', '#9'])),
  ('piano', 'C4 D4', c(42, 'hero', seq=['#8', '#9'])),
  ('P', 'So every other pair of white keys has a black key in the middle. Only E–F and B–C sit together.', c(42, 'hero')),
  ('B', 'Exactly. And a semitone can also go from a white key to a black key, or black to white: still next door, nobody between.', c(42, 'rule'))]),
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
  ('piano', 'G4/2 G4/2 G4/2 Eb4*3 | F4/2 F4/2 F4/2 D4*4', c(47, 'yk')),
  ('P', 'Da-da-da-dum! It sounds like someone banging on the door.', c(47, 'yk')),
  ('B', 'Some people say it is fate knocking. G down to E flat is a third, with three keys between: a major third. Count them on your keyboard.', c(47, 'yk')),
  ('B', 'A major and a minor third are a smile and a frown: the same face, one small change at the corners.', c(47, 'think')),
  ('Q', 'And never call a fourth or a fifth major, Clara. They are perfect.', c(47, 'watch')),
  ('K', 'Like Her Majesty. Or so I’m told. Every morning.', c(47, 'watch')),
  ('B', 'Until next time, Clara.', c(47, 'watch')),
  ('P', 'Bye, Butler!', c(47, 'watch'))])])

NEW['T1'] = ('Pulse, tempo and the bar', [
 ('The secret', [
  ('B', 'Clara, put your hand on your heart.', c(50, 'lead')),
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
  ('count', {'beats': 'X x X x X x X x X x X x X x X x', 'say': '1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2'}, c(52, 'yk')),
  ('P', 'I want to clap with them!', c(52, 'yk')),
  ('B', 'One day. Remember: the beat is the stage and the notes are the actors. The stage is there before anyone walks on. So watch it move for a bar, then step in. Until next time, Clara.', c(52, 'think')),
  ('P', 'One, two, three, four. Bye, Butler!', c(52, 'think'))])])

NEW['T2'] = ('Notes and rests', [
 ('Sounds and silences', [
  ('P', 'Butler, is music just lots and lots of notes?', c(53, 'lead')),
  ('B', 'Only half of it, Clara. Music is made of two things: sounds and silences. Think of talking. A sentence needs words, and it needs little pauses too. Without the pauses it’s one long breathless rush.', c(53, 'lead')),
  ('P', 'Like my little brother telling a story.', c(53, 'lead')),
  ('B', 'Exactly like that. On paper, a sound is written as a note, and a silence is written as a rest. A rest is just as important as a note. It isn’t a break for you: it’s music you can’t hear, and you count it just as carefully.', c(53, 'lead'))]),
 ('Long and short notes', [
  ('P', 'So how do I know how long to hold a note? Do I just guess?', c(53, 'hero')),
  ('B', 'No guessing required. Its shape tells you, like the size of a cup tells you how much juice it holds. Each note is half the one above it. A semibreve lasts four beats. It splits into two minims, two beats each. A minim splits into two crotchets, one beat each.', c(53, 'hero')),
  ('P', 'Like cutting a cake in half, and in half again.', c(53, 'hero')),
  ('B', 'Precisely, and nobody fights over the pieces. Listen to one bar of each. The beat keeps going; only the notes change.', c(53, 'hero')),
  ('count', {'beats': 'X x M x X x M x X x M x', 'notes': 'C4*4 C4*2 C4*2 C4 C4 C4 C4', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, c(53, 'hero')),
  ('B', 'And here’s the other half of the secret: every note has a twin rest, a silence of exactly the same length.', c(53, 'secret'))]),
 ('Quavers', [
  ('B', 'One more halving. A crotchet splits into two quavers, half a beat each: two to every beat.', c(53, 'hero')),
  ('count', {'beats': 'X/2 R/2 x/2 R/2 M/2 R/2 x/2 R/2', 'notes': 'C4/2 C4/2 C4/2 C4/2 C4/2 C4/2 C4/2 C4/2', 'say': '1 & 2 & 3 & 4 &'}, c(53, 'hero')),
  ('P', 'For the quavers you said “and” in between.', c(53, 'sm')),
  ('B', 'Yes. Say the beat’s number, then “and” halfway to the next beat.', c(53, 'sm'))]),
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
  ('count', {'beats': 'X x M x X x M x X x M x X x M x', 'notes': 'C4 C4 G4 G4 A4 A4 G4*2 F4 F4 E4 E4 D4 D4 C4*2', 'say': '1 2 3 4 1 2 3 4 1 2 3 4 1 2 3 4'}, c(55, 'yk')),
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
  ('B', 'You already know a dotted crotchet: Beethoven’s Ode to Joy. Listen to the whole first line. Near the end, the red E is dotted: hold it through “one and two”. The quaver D falls on the “and”, and the last D takes beats three and four.', c(57, 'ex2')),
  ('count', {'beats': 'X x M x X x M x X x M x X/2 R/2 x/2 R/2 M x', 'notes': 'E4 E4 F4 G4 G4 F4 E4 D4 C4 C4 D4 E4 E4*1.5 D4/2 D4*2', 'say': '1 2 3 4 1 2 3 4 1 2 3 4 1 & 2 & 3 4'}, c(57, 'ex2', reveal=True)),
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
  ('S', 'Tickets, please! Stationmaster here. I check the time signature at the start of the line, and I keep every carriage running on time.', c(59, 'hero')),
  ('S', 'Four-four: four seats, and a crotchet in each. Count them with me.', c(59, 'hero')),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C4 C4 C4 C4 C4 C4 C4 C4', 'say': '1 2 3 4 1 2 3 4'}, c(59, 'hero')),
  ('B', 'That is the secret: the top number is how many beats, and the bottom number is which note gets one beat.', c(59, 'secret'))]),
 ('Think of a train', [
  ('B', 'In three-four every carriage has three seats. A minim books two, a crotchet one. A rest books a seat and leaves it empty, like a bag on the seat next to you. A dotted minim is a big family that fills all three.', c(59, 'pzbox')),
  ('count', {'beats': 'X x x X x x X x x', 'notes': 'C4*2 C4 C4 R C4 C4*3', 'say': '1 2 3 1 2 3 1 2 3'}, c(59, 'pzbox')),
  ('B', 'The bottom number is a secret code: two means a minim, four a crotchet, eight a quaver, sixteen a semiquaver.', c(59, 'xlate')),
  ('P', 'A code! Like spies.', c(59, 'xlate')),
  ('S', 'Like railway codes, miss. Every station knows them.', c(59, 'xlate'))]),
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
  ('S', 'Ticket accepted. All aboard!', c(60, 'ex2', reveal=True))]),
 ('Example: where does the rest go?', [
  ('B', 'Four-four, and three crotchets. Which seat is empty, and what goes there?', c(61, 'ex3')),
  ('pause', 3, c(61, 'ex3')),
  ('P', 'Seat four. A crotchet rest, sitting there quietly!', c(61, 'ex3', reveal=True)),
  ('count', {'beats': 'X x M x', 'notes': 'C4 C4 C4 R', 'say': '1 2 3 4'}, c(61, 'ex3', reveal=True))]),
 ('Changing time signature', [
  ('B', 'A new time signature can arrive right after a bar line, like a train changing to shorter carriages at a station. Here three-four becomes two-four, and two beats a bar holds until the next change.', c(61, 'xlate')),
  ('S', 'Change at this station! Two seats per carriage from here on.', c(61, 'xlate')),
  ('count', {'beats': 'X x x X x x X x X x X x', 'notes': 'C4 C4 C4 C4*2 C4 C4 C4 C4*2 C4 C4', 'say': '1 2 3 1 2 3 1 2 1 2 1 2'}, c(61, 'xlate'))]),
 ('You know this', [
  ('B', 'The Minuet from the Notebook for Anna Magdalena Bach: one two three, one two three, the step of an old court dance. That is three-four.', c(61, 'yk')),
  ('count', {'beats': 'X x x X x x X x x X x x X x x X x x X x x X x x', 'notes': 'D5 G4/2 A4/2 B4/2 C5/2 D5 G4 G4 E5 C5/2 D5/2 E5/2 F#5/2 G5 G4 G4 C5 D5/2 C5/2 B4/2 A4/2 B4 C5/2 B4/2 A4/2 G4/2 F#4 G4/2 A4/2 B4/2 G4/2 A4*3', 'say': '1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3 1 2 3'}, c(61, 'yk')),
  ('P', 'I can imagine people in big wigs bowing to each other.', c(61, 'yk')),
  ('Q', 'We still dance it at the palace. And remember, Clara: the bottom number is not a count. It names the note that gets one beat.', c(61, 'watch')),
  ('S', 'And mind the gap, miss: every carriage must be full. Count every bar.', c(61, 'watch')),
  ('B', 'Until next time, Clara.', c(61, 'watch')),
  ('P', 'Bye, Butler! Bye, Your Majesty! Bye, Stationmaster!', c(61, 'watch'))])])

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
  ('K', 'Nobody sees the King dance in five.', c(64, 'xlate')),
  ('S', 'Five-four: one carriage of three seats, one of two, coupled together. Still on time, sir.', c(64, 'xlate'))]),
 ('You know this', [
  ('B', 'Row, Row, Row Your Boat: two big beats in every bar, each a dotted crotchet. Sway twice per bar while you sing, like a boat on gentle waves.', c(64, 'yk')),
  ('count', {'beats': 'X R R M R R X R R M R R X R R M R R X R R M R R X R R M R R X R R M R R X R R M R R X R R M R R', 'notes': 'C4*3 C4*3 C4*2 D4 E4*3 E4*2 D4 E4*2 F4 G4*6 C5 C5 C5 G4 G4 G4 E4 E4 E4 C4 C4 C4 G4*2 F4 E4*2 D4 C4*6', 'say': '1 - - 2 - - 1 - - 2 - - 1 - - 2 - - 1 - - 2 - - 1 - - 2 - - 1 - - 2 - - 1 - - 2 - - 1 - - 2 - -'}, c(64, 'yk')),
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
  ('count', {'beats': 'R x X x x X x x X x x X x x', 'notes': 'R C4*0.75 C4/4 D4 C4 F4 E4*2 C4*0.75 C4/4 D4 C4 G4 F4*3', 'say': '- 3 1 2 3 1 2 3 1 2 3 1 2 3'}, c(66, 'xlate'))]),
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
  ('piano', 'D4/4 D#4/4 E4/4 C5/2 E4/4 C5/2 E4/4 C5*1.5 | C5/4 D5/4 D#5/4 E5/4 C5/4 D5/4 E5/2 B4/4 D5/2 C5*1.5', c(69, 'xlate2')),
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
  ('B', 'Listen. First without the pedal: each note stops when the finger lifts.', c(85, 'xlate')),
  ('piano', 'C4 E4 G4 C5', c(85, 'xlate')),
  ('B', 'And now with the sustain pedal down: every note keeps ringing.', c(85, 'xlate')),
  ('piano', 'Ped C4 E4 G4 C5 R*2 *', c(85, 'xlate')),
  ('B', 'The soft pedal is written u.c., una corda, and let up at t.c. The sustain pedal is written Ped.', c(85, 'xlate2'))]),
 ('Example: which pedal?', [
  ('B', 'Which pedal is Ped.? Which is u.c.? And what does t.c. ask? Pause and think.', c(86, 'ex1')),
  ('pause', 4, c(86, 'ex1')),
  ('P', 'Ped. is the soft pedal?', c(86, 'ex1', oops=True)),
  ('B', 'Not quite, Clara. The soft pedal is the left one, written u.c. Ped. is the right one, and it keeps the notes ringing.', c(86, 'ex1')),
  ('P', 'Ped. is the right pedal, u.c. the left, and t.c. means let the left pedal up.', c(86, 'ex1', reveal=True))]),
 ('Writing the sustain pedal', [
  ('B', 'Down at Ped., up at the star. Heel on the floor, press with the ball of your foot, like gently squeezing a soft sponge. Play first, then pedal.', c(86, 'xlate'))]),
 ('Example: down and up', [
  ('B', 'Where does the pedal go down, where does it change, and where does it come up?', c(86, 'ex2')),
  ('pause', 4, c(86, 'ex2')),
  ('P', 'Down on the first C, changed at the F, and up at the end.', c(86, 'ex2', reveal=True)),
  ('piano', 'Ped C4 E4 G4 C5 ^ F4 A4 C5 F5 R *', c(86, 'ex2', reveal=True))]),
 ('Changing the pedal', [
  ('B', 'At every new chord, change the pedal just after you play it: up, and straight down again. Each chord rings clean, and they still join. Forget to change, and the chords pile up like muddy footprints on a clean floor.', c(87, 'xlate')),
  ('B', 'Listen, with a clean change at each chord.', c(87, 'xlate')),
  ('piano', 'Ped [C4 E4 G4] ^ [F4 A4 C5] ^ [G4 B4 D5] ^ [C4 E4 G4] R *', c(87, 'xlate')),
  ('B', 'And here is the muddy floor: the pedal held down through every chord.', c(87, 'xlate')),
  ('piano', 'Ped [C4 E4 G4] [F4 A4 C5] [G4 B4 D5] R *', c(87, 'xlate')),
  ('P', 'Eww. It sounds like everyone talking at once.', c(87, 'xlate')),
  ('B', 'Exactly. One more thing: the pedal is written in several ways. Ped. and a star. A Ped. under every chord, where each new Ped. is a change. A line with two hooks, down where it starts and up where it ends; notches in the line are changes. The words con Ped., with pedal, or senza Ped., without. And Ped. simile: go on pedalling the same way.', c(87, 'xlate2')),
  ('B', 'Try it: play C, E and G together, press the right pedal and take your hands off. The chord keeps sounding. Lift the pedal: silence.', c(87, 'try10')),
  ('piano', 'Ped [C4 E4 G4] R*3 *', c(87, 'try10')),
  ('P', 'Magic! My hands are gone and the music is still there.', c(87, 'try10')),
  ('B', 'The sustain pedal holds a door open: every note that walks in stays in the room until you let the door shut. Until next time, Clara.', c(87, 'think')),
  ('P', 'Bye, Butler!', c(87, 'think'))])])

NEW['E5'] = ('Ornaments', [
 ('The secret', [
  ('P', 'Butler, look! Mum let me wear her necklace and a sparkly hair clip today.', c(88, 'lead')),
  ('B', 'Very elegant. You are the same Clara, but the accessories make you shine. Music has accessories too. Look at this one.', c(88, 'lead')),
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
  ('piano', 'D5/4 E5/4 D5/2 G4/2 A4/2 B4/2 C5/2 D5 G4 G4 E5 C5/2 D5/2 E5/2 F#5/2 G5 G4 G4', c(90, 'yk')),
  ('B', 'Ornaments are accessories: they make the music look lovely, but you get dressed first. Learn the plain notes in time, then put on the necklace. Until next time, Clara.', c(90, 'think')),
  ('P', 'Bye, Butler!', c(90, 'think'))])])

# ---- Part IV, Scales and keys (her 11 Nov: "다음 거 진행해줘"): audio for S1-S5 in the same storybook style ----
CM = 'C4 D4 E4 F4 G4 A4 B4 C5'
NEW['S1'] = ('Major scales', [
 ('The secret', [
  ('B', 'Clara, notes, it turns out, live in families.', c(93, 'h:Major scales')),
  ('P', 'Like my family? We are very noisy.', c(93, 'lead')),
  ('B', 'Some scales are noisy too. A scale climbs from a home note, the key note, up to the next note with the same name, using every letter once. Like a staircase from the ground floor to the first floor.', c(93, 'lead')),
  ('B', 'Here is the most famous staircase of all: C major.', c(93, 'hero')),
  ('piano', CM, c(93, 'hero', seq=['#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7'])),
  ('P', 'Do re mi fa so la ti do! I know that one.', c(93, 'hero')),
  ('B', 'Everybody does. Now look at the steps between the notes. Most of them are big steps, tones. But two of them are tiny, semitones. Like a staircase where two of the steps are only half as high.', c(93, 'hero')),
  ('P', 'I’d trip on those!', c(93, 'hero')),
  ('B', 'Read each arrow from one note to the next. C to D: a tone. D to E: a tone. E to F: a semitone, best friends. F to G, G to A, A to B: tones. And B to C: a semitone again.', c(93, 'hero', lab=['#10', '#14'])),
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
  ('B', 'Exactly. That is the secret: the key signature says, once, at the start, which notes are always sharp or flat. Think of a dress code at a party. And every party needs someone at the door.', c(99, 'secret')),
  ('D', 'Good evening. I am the Doorkeeper. I stand at the door of every line, just after the King or the Queen, and I read out tonight’s dress code.', c(99, 'secret')),
  ('D', 'Tonight: every F wears a sharp. High F, low F, every F, all night. No exceptions.', c(99, 'secret')),
  ('P', 'So the Doorkeeper’s rule lasts the whole piece, but the Guest only stays for one bar.', c(99, 'secret')),
  ('D', 'Quite right, miss. The Guest may change her hat for one bar. My rule stands until the music ends.', c(99, 'secret'))]),
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
  ('P', 'Two sharps: F sharp and C sharp. Every F and every C, high or low!', c(100, 'ex1', reveal=True)),
  ('D', 'Correct. F and C, sharps on, all night.', c(100, 'ex1', reveal=True))]),
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
  ('piano', 'D5 G4/2 A4/2 B4/2 C5/2 D5 G4 G4 E5 C5/2 D5/2 E5/2 F#5/2 G5 G4 G4 C5 D5/2 C5/2 B4/2 A4/2 B4 C5/2 B4/2 A4/2 G4/2 F#4 G4/2 A4/2 B4/2 G4/2 A4*3', c(101, 'yk')),
  ('P', 'I heard the F sharp, right before the top!', c(101, 'yk')),
  ('B', 'A dress code, written once. Only an accidental, our Guest, overrules it, and only until the bar line. And remember to glance at the key signature at the start of every line.', c(101, 'think')),
  ('D', 'I shall be at every door, miss. Do say hello as you pass.', c(101, 'think')),
  ('B', 'Until next time, Clara.', c(101, 'think')),
  ('P', 'Bye, Butler!', c(101, 'think'))])])

NEW['S4'] = ('Finding the key', [
 ('The secret', [
  ('P', 'Butler, if one key signature belongs to two keys, how do I know which one my piece is in?', c(102, 'h:Finding the key')),
  ('B', 'Ah. Now we become detectives, Clara. The key signature narrows it down to two suspects: a major key and its relative minor. Two quick rules find the major. A minor third down finds the minor. Then the music itself tells you which suspect did it.', c(102, 'lead')),
  ('P', 'Ooh, a mystery! Where’s my magnifying glass?', c(102, 'lead')),
  ('B', 'Here is the secret. For sharps: find the last sharp, then go the very next key up. For flats: the second-last flat is the key.', c(102, 'secret')),
  ('B', 'Look: three sharps. The last one is G sharp. The very next key up is A. Three sharps: A major.', c(102, 'hero')),
  ('piano', 'G#4 A4', c(102, 'hero', seq=['#5', '#6'])),
  ('P', 'The last sharp is like the last guest the Doorkeeper lets in, and the key lives one step up.', c(102, 'hero')),
  ('D', 'The last one in always holds the door for the key. Good manners.', c(102, 'hero')),
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

# ---- Part V, Chords (her 11 Nov: decisions 1, 2, 3 in order; 1 = chords audio) ----
NEW['H1'] = ('Chords and triads', [
 ('The secret', [
  ('B', 'Clara, press three or more notes at once, and you have a chord.', c(110, 'h:Chords and triads')),
  ('P', 'Like pressing lots of keys with my elbow?', c(110, 'lead')),
  ('B', 'That is a chord too, technically. A rather alarming one. But the favourite chord of all is much tidier: the triad, three notes stacked like the layers of a cake.', c(110, 'lead')),
  ('B', 'Here is the cake rule: play one, skip one, play one. Pick a note, the root: the big layer at the bottom. It holds the chord up and gives it its name.', c(110, 'secret')),
  ('B', 'Start on C. Skip one letter, D, and take E: the third. Skip again, F, and take G: the fifth. C, E, G: the triad of C.', c(110, 'two', seq=['C', 'E', 'G'])),
  ('piano', 'C4 E4 G4 | [C4 E4 G4]', c(110, 'two', seq=['C', 'E', 'G', 'G'])),
  ('P', 'Play one, skip one, play one, skip one, play one. I could do that in my sleep.', c(110, 'two')),
  ('B', 'And on the staff it looks just as tidy: each layer sits on the next line up, or the next space up. Three lines in a row, or three spaces in a row, like a neat stack of pancakes.', c(110, 'two2')),
  ('B', 'If one note breaks the pattern, it is not a stacked triad. Lines, spaces, lines, spaces: every one of these is a triad.', c(110, 'two3'))]),
 ('Solid and broken', [
  ('B', 'Played together, a chord is solid.', c(111, 'two')),
  ('piano', '[C4 E4 G4]', c(111, 'two')),
  ('B', 'Played one note at a time, it is broken.', c(111, 'two')),
  ('piano', 'C4 E4 G4 E4 C4*2', c(111, 'two')),
  ('P', 'Solid is three friends shouting hello together. Broken is each one saying it in turn.', c(111, 'two')),
  ('B', 'Exactly. And spread a broken chord up the keyboard, and it becomes an arpeggio, like a harp.', c(111, 'two')),
  ('piano', 'C3/2 E3/2 G3/2 C4/2 E4/2 G4/2 C5/2 E5/2 G5/2 C6*2', c(111, 'two'))]),
 ('Example: build a triad on G', [
  ('B', 'Build a triad on G. Start on the red dot, the root. Skip one white key and take the next. Skip again, and take the next. Pause and find them.', c(111, 'ex1')),
  ('pause', 4, c(111, 'ex1')),
  ('P', 'G, skip A, B. Skip C, D. G, B, D!', c(111, 'ex1', reveal=True)),
  ('piano', 'G4 B4 D5 | [G4 B4 D5]', c(111, 'ex1', reveal=True)),
  ('B', 'The triad of G. The same shape as C E G, just moved up the hill.', c(111, 'ex1', reveal=True))]),
 ('Example: which one is a triad?', [
  ('B', 'Three chords. Which one is a real triad? Look: are the notes all on lines, or all in spaces? Is every gap a third?', c(111, 'ex2')),
  ('pause', 5, c(111, 'ex2')),
  ('P', 'Number two. It looks cosy.', c(111, 'ex2', oops=True)),
  ('B', 'Cosy, but squashed. D to E is a second: two notes next door, a layer missing from the cake.', c(111, 'ex2')),
  ('P', 'Then number one: D, F, A, three spaces in a row!', c(111, 'ex2', reveal=True)),
  ('B', 'Right. And chord three is stacked in fourths: too far apart. Only the first one passes both tests.', c(111, 'ex2', reveal=True)),
  ('B', 'Try it: thumb on C, and press fingers one, three and five together. That is the C chord. Now slide your hand to any white key and do it again: the cake shape always works.', c(111, 'try10')),
  ('piano', '[C4 E4 G4] [D4 F4 A4] [E4 G4 B4] [F4 A4 C5] [G4 B4 D5]', c(111, 'try10'))]),
 ('Game and The Blue Danube', [
  ('B', 'Game: build one yourself. Start on G: G, B, D. Start on F: F, A, C. Your turn: start on A. Which three keys?', c(112, 'game')),
  ('pause', 4, c(112, 'game')),
  ('P', 'Start on A, skip B, take C, skip D, take E. A, C, E!', c(112, 'game', reveal=True)),
  ('piano', '[A3 C4 E4]', c(112, 'game', reveal=True)),
  ('B', 'And now, the most famous waltz in the world, The Blue Danube by Johann Strauss. Here it is in C. Listen how it simply climbs the C triad, then holds the top.', c(112, 'yk')),
  ('piano', 'C4*2 C4 E4 G4 G4*2 | G5 G5*2 E5 E5*2 | C4*2 C4 E4 G4 G4*2 | G5 G5*2 F5 F5*2', c(112, 'yk')),
  ('P', 'It sounds like people twirling in a ballroom!', c(112, 'yk')),
  ('Q', 'One of my favourites at the palace ball. The King steps on my toes every time.', c(112, 'yk')),
  ('K', 'Only on the third beat.', c(112, 'yk')),
  ('B', 'Two traps: a triad skips exactly one letter each time, never two notes next door. And the root names the chord, not the top note. Until next time, Clara.', c(112, 'watch')),
  ('P', 'Bye, Butler! Bye, Your Majesties!', c(112, 'watch'))])])

NEW['H2'] = ('Four kinds of triad', [
 ('The secret', [
  ('P', 'Butler, are all triads the same, or are there different flavours, like ice cream?', c(113, 'h:Four kinds of triad')),
  ('B', 'Four flavours, Clara. Every triad is two thirds stacked. To tell them apart, count the keys in between, black and white, the ones you do not play: root to third, then third to fifth.', c(113, 'lead')),
  ('B', 'Here is the secret: three plus two is major. Two plus three is minor.', c(113, 'secret')),
  ('B', 'Listen to all four on C. Major: three keys between, then two. Bright and sunny.', c(113, 'hero', seq=['C'])),
  ('piano', '[C4 E4 G4]', c(113, 'hero')),
  ('B', 'Minor: two, then three. Darker, softer.', c(113, 'hero')),
  ('piano', '[C4 Eb4 G4]', c(113, 'hero')),
  ('B', 'Diminished: two and two. Squeezed and tense, like a spooky film.', c(113, 'hero')),
  ('piano', '[C4 Eb4 Gb4]', c(113, 'hero')),
  ('B', 'And augmented: three and three. Stretched and dreamy, like floating in a cloud.', c(113, 'hero')),
  ('piano', '[C4 E4 G#4]', c(113, 'hero')),
  ('P', 'Sunny, rainy, spooky and dreamy!', c(113, 'hero')),
  ('B', 'A weather forecast in four chords. And their names: a letter alone means major, so C. A small m means minor: C minor. You will see them above the melody in songbooks.', c(113, 'ht'))]),
 ('Count the keys in between', [
  ('B', 'Let’s count together. Play C and E, and count the keys you skip, black and white: C sharp, D, D sharp. Three. Then E to G: F, F sharp. Two. Three plus two: major.', c(113, 'fk')),
  ('piano', 'C4 C#4 D4 D#4 E4 | E4 F4 F#4 G4 | [C4 E4 G4]', c(113, 'fk')),
  ('B', 'Any root works the same way. From D, skip three to F sharp, then two to A: D, F sharp, A. D major.', c(113, 'fk')),
  ('piano', '[D4 F#4 A4]', c(113, 'fk'))]),
 ('The white-key triads', [
  ('B', 'Now build a triad on every white key, and sort them. It always comes out the same: three major, C, F and G. Three minor, D, E and A. And one diminished, on B. No augmented at all.', c(114, 'vx')),
  ('piano', '[C4 E4 G4] [D4 F4 A4] [E4 G4 B4] [F4 A4 C5] [G4 B4 D5] [A4 C5 E5] [B4 D5 F5] [C5 E5 G5]', c(114, 'vx')),
  ('P', 'Happy, sad, sad, happy, happy, sad, spooky, happy!', c(114, 'vx')),
  ('B', 'You just heard a whole family photo. Major sounds bright and settled, like fanfares. Minor is darker, like lullabies and film tension. Diminished is tense, it wants to move. And augmented floats, unsettled, like a dream.', c(114, 'ht'))]),
 ('Example: major or minor?', [
  ('B', 'D, F, A. Major or minor? Count the keys between D and F, then between F and A. Pause and count.', c(114, 'ex1')),
  ('pause', 5, c(114, 'ex1')),
  ('P', 'D to F: D sharp, E. Two. F to A: F sharp, G, G sharp. Three. Two plus three: minor!', c(114, 'ex1', reveal=True)),
  ('piano', '[D4 F4 A4]', c(114, 'ex1', reveal=True)),
  ('B', 'D minor. Game: which kind is each of these three chords? Pause and count.', c(114, 'game')),
  ('pause', 6, c(114, 'game')),
  ('P', 'Diminished, major, and augmented.', c(114, 'game', reveal=True))]),
 ('Example: the triad on B', [
  ('B', 'Try it: C E G, then C E flat G, then C E flat G flat. Bright, dark, tense. Only the middle layer moves first, then the top one.', c(115, 'try10')),
  ('piano', '[C4 E4 G4] [C4 Eb4 G4] [C4 Eb4 Gb4]', c(115, 'try10')),
  ('B', 'Now, what kind is the triad on B? Skip a letter: B, D, F. Count the keys between.', c(115, 'ex2')),
  ('pause', 5, c(115, 'ex2')),
  ('P', 'B to D: C, C sharp, two. D to F: D sharp, E, two. Two plus two: diminished!', c(115, 'ex2', reveal=True)),
  ('piano', '[B3 D4 F4]', c(115, 'ex2', reveal=True)),
  ('B', 'B diminished, the only spooky one on the white keys.', c(115, 'ex2', reveal=True))]),
 ('You know this', [
  ('B', 'And now a very famous dark one: Beethoven’s Moonlight Sonata. The slow triplets are the notes of a C sharp minor triad, rocking gently, like moonlight on a lake.', c(115, 'yk')),
  ('piano', 'G#3/3 C#4/3 E4/3 G#3/3 C#4/3 E4/3 G#3/3 C#4/3 E4/3 G#3/3 C#4/3 E4/3 | G#3/3 C#4/3 E4/3 G#3/3 C#4/3 E4/3 G#3/3 C#4/3 E4/3 G#3/3 C#4/3 E4/3 | A3/3 C#4/3 E4/3 A3/3 C#4/3 E4/3 A3/3 D4/3 F#4/3 A3/3 D4/3 F#4/3 | G#3/3 B#3/3 F#4/3 G#3/3 C#4/3 E4/3 G#3/3 C#4/3 D#4/3 F#3/3 B#3/3 D#4/3 | E3/3 G#3/3 C#4/3 G#3/3 C#4/3 E4/3 G#3/3 C#4/3 E4/3 G#3/3 C#4/3 E4/3', c(115, 'yk')),
  ('P', 'It’s so sad. Like a lonely owl.', c(115, 'yk')),
  ('B', 'Minor is why. Remember the two gaps in the cake: major is wide, then narrow, three plus two. Minor is narrow, then wide, two plus three. Diminished, two narrow. Augmented, two wide. Until next time, Clara.', c(115, 'think')),
  ('P', 'Bye, Butler!', c(115, 'think'))])])
for _k in ('H1', 'H2'): CH[_k] = NEW[_k]

NEW['H3'] = ('Chords in a key', [
 ('The secret', [
  ('P', 'Butler, if I can build a cake on any note, how do I know which cakes belong to my piece?', c(116, 'h:Chords in a key')),
  ('B', 'Excellent question. Build a cake on every note of the scale, and you have the chords of that key: one chord living on each floor of the house. We name them with Roman numerals, by their floor. One on the first note, four on the fourth, five on the fifth.', c(116, 'lead')),
  ('P', 'Roman numerals? Like on a castle clock?', c(116, 'lead')),
  ('B', 'Precisely. Here are the seven chords of C major.', c(116, 'hero')),
  ('piano', '[C4 E4 G4] [D4 F4 A4] [E4 G4 B4] [F4 A4 C5] [G4 B4 D5] [A4 C5 E5] [B4 D5 F5] [C5 E5 G5]', c(116, 'hero')),
  ('B', 'Capital numerals are major. Small ones are minor. And small with a little circle is diminished. And here is the secret: one, four and five are the strongest. They do most of the work.', c(116, 'secret')),
  ('B', 'Their grand names: one is the tonic, the key’s own chord. Four is the subdominant. Five is the dominant. In every major key, one, four and five are major; two, three and six are minor; seven is diminished.', c(116, 'ht'))]),
 ('The three primary chords', [
  ('B', 'One, four and five are the three primary chords. Between them they hold every note of the scale: C E G, F A C, G B D. Every note has a chair to sit on.', c(116, 'two')),
  ('piano', '[C4 E4 G4] [F4 A4 C5] [G4 B4 D5] [C4 E4 G4]', c(116, 'two')),
  ('P', 'So that’s why so many songs only need three chords!', c(116, 'two')),
  ('B', 'Exactly. Three chords and the truth, as the songwriters say.', c(116, 'two'))]),
 ('In a minor key', [
  ('B', 'In the key of A minor, the three main chords are small one, A minor; small four, D minor; and capital five: E, G sharp, B. It becomes major thanks to the raised seventh of the harmonic minor, G sharp.', c(117, 'two')),
  ('piano', '[A3 C4 E4] [D4 F4 A4] [E4 G#4 B4] [A3 C4 E4]', c(117, 'two')),
  ('P', 'The G sharp again! That dog pulling on its lead.', c(117, 'two'))]),
 ('Example: I, IV and V in G major', [
  ('B', 'Find one, four and five in G major. Count up the scale from G: which notes are first, fourth and fifth? Then build a cake on each, using the key signature: one sharp, F sharp.', c(117, 'ex1')),
  ('pause', 5, c(117, 'ex1')),
  ('P', 'One is G: G B D. Four is C: C E G. Five is D: D, F sharp, A. All major!', c(117, 'ex1', reveal=True)),
  ('piano', '[G3 B3 D4] [C4 E4 G4] [D4 F#4 A4] [G3 B3 D4]', c(117, 'ex1', reveal=True)),
  ('B', 'Game: which numeral? All in C major. Count up the scale from C to find each chord’s floor.', c(117, 'game')),
  ('pause', 5, c(117, 'game')),
  ('P', 'Four, five, six and two.', c(117, 'game', reveal=True)),
  ('B', 'Try it: left hand plays C, F, G, the cakes of one, four and five, while you sing any nursery tune over them. These three fit almost every note.', c(117, 'try10'))]),
 ('Example: IV in F, V in D minor', [
  ('B', 'Find four in F major. Count up from F to the fourth note, and watch the key signature: one flat.', c(118, 'ex2')),
  ('pause', 4, c(118, 'ex2')),
  ('P', 'F, G, A, B... B!', c(118, 'ex2', oops=True)),
  ('B', 'Careful, the key signature has one flat. Which note does it change?', c(118, 'ex2')),
  ('P', 'B flat! So four is B flat, D, F. Three plus two: major.', c(118, 'ex2', reveal=True)),
  ('piano', '[Bb3 D4 F4]', c(118, 'ex2', reveal=True)),
  ('B', 'Now five in D minor. The fifth note is A: build the chord A, C, E. But in the harmonic minor, the seventh note, C, is raised. To what?', c(118, 'ex3')),
  ('pause', 3, c(118, 'ex3')),
  ('P', 'C sharp! Five in D minor is A, C sharp, E: A major.', c(118, 'ex3', reveal=True)),
  ('piano', '[A3 C#4 E4] [D4 F4 A4]', c(118, 'ex3', reveal=True)),
  ('B', 'And the chord on note six of C major? Build the cake on A.', c(118, 'ex4')),
  ('pause', 3, c(118, 'ex4')),
  ('P', 'The notes A, C, E. Two plus three: minor. So small six!', c(118, 'ex4', reveal=True)),
  ('B', 'Two traps: minor chords get small numerals. And in a minor key, never forget the raised seventh: five in the key of A minor is E, G sharp, B. Until next time, Clara.', c(118, 'watch')),
  ('P', 'Bye, Butler!', c(118, 'watch'))])])

NEW['H4'] = ('Inversions', [
 ('The secret', [
  ('P', 'Butler, can I turn a cake upside down?', c(119, 'h:Inversions')),
  ('B', 'Not without a terrible mess. But a chord, yes! Same three notes, a different one at the bottom. The chord keeps its name; only the bass changes. That is an inversion.', c(119, 'lead')),
  ('B', 'Here is the secret: move the bottom note to the top. Same chord, new bass. Start with C E G, root at the bottom: root position.', c(119, 'inv3', seq=['#0', '#1', '#2'])),
  ('piano', '[C4 E4 G4]', c(119, 'inv3')),
  ('B', 'Move C to the top: E G C. That is the first inversion.', c(119, 'inv3')),
  ('piano', '[E4 G4 C5]', c(119, 'inv3')),
  ('B', 'Move it again: G C E. The second inversion. Still C major.', c(119, 'inv3')),
  ('piano', '[G4 C5 E5]', c(119, 'inv3')),
  ('P', 'It’s like a family taking turns to sit at the bottom of the bunk bed.', c(119, 'inv3')),
  ('B', 'A very tidy family. To find the root, restack the notes every other letter, like C E G. Then the bottom layer is the root.', c(119, 'vx'))]),
 ('Why inversions?', [
  ('B', 'Why bother? Because inversions let your hand move as little as possible. Keep any note two chords share, and move the others to the nearest note of the next chord. Like moving furniture: you don’t carry the sofa across the room if it already fits.', c(119, 'p')),
  ('B', 'Game: which position? C E G, E G C, G C E. Look at the bottom note: root, third or fifth?', c(119, 'game')),
  ('pause', 4, c(119, 'game')),
  ('P', 'Root position, first inversion, second inversion.', c(119, 'game', reveal=True))]),
 ('Example: move as little as possible', [
  ('B', 'C, F, G, C, the lazy way. One: C E G. For four, keep C, move E up to F and G up to A: C F A.', c(120, 'ex1')),
  ('piano', '[C4 E4 G4] [C4 F4 A4]', c(120, 'ex1')),
  ('B', 'For five there’s no shared note. C steps down to B, F down to D, A down to G: B D G. Then one again: C E G.', c(120, 'ex1')),
  ('piano', '[B3 D4 G4] [C4 E4 G4]', c(120, 'ex1')),
  ('P', 'My hand hardly moved! It just wiggled.', c(120, 'ex1')),
  ('B', 'The laziest hand makes the smoothest music. Try it: climb the chord. C E G, then E G C, then G C E, then C E G an octave up.', c(120, 'try10')),
  ('piano', '[C4 E4 G4] [E4 G4 C5] [G4 C5 E5] [C5 E5 G5]', c(120, 'try10'))]),
 ('Example: F and G inversions', [
  ('B', 'Write F major in first inversion. Build F major in root position first. Then which layer goes to the bottom, the third or the fifth?', c(120, 'ex2')),
  ('pause', 4, c(120, 'ex2')),
  ('P', 'F A C, and the third goes to the bottom: A, C, F!', c(120, 'ex2', reveal=True)),
  ('piano', '[A3 C4 F4]', c(120, 'ex2', reveal=True)),
  ('B', 'And the second inversion of G?', c(120, 'ex3')),
  ('pause', 3, c(120, 'ex3')),
  ('P', 'G B D, with the fifth at the bottom: D G B.', c(120, 'ex3', reveal=True)),
  ('piano', '[D4 G4 B4]', c(120, 'ex3', reveal=True))]),
 ('Example: find the root', [
  ('B', 'Find the root of E G C. Restack the notes so that each skips one letter. Try starting on each note.', c(121, 'ex4')),
  ('pause', 4, c(121, 'ex4')),
  ('P', 'E G C doesn’t work, G C E doesn’t, but C E G does! The root is C.', c(121, 'ex4', reveal=True, anim='restack')),
  ('B', 'Watch the layers swap: the C on top slides down to the bottom, and the cake stands in thirds again, C, E, G. The bottom layer is the root.', c(121, 'ex4', reveal=True, anim='restack')),
  ('B', 'C major, first inversion. Now A, D, F: which position?', c(121, 'ex5')),
  ('pause', 4, c(121, 'ex5')),
  ('P', 'Restacked: D F A, D minor. A is the fifth, at the bottom: second inversion!', c(121, 'ex5', reveal=True)),
  ('piano', '[A3 D4 F4] [D4 F4 A4]', c(121, 'ex5', reveal=True))]),
 ('You know this', [
  ('B', 'Pachelbel’s Canon, the bass, here in C. In the popular version the bass walks straight down the scale: C, B, A, G, F, E, F, G. It can, because some chords are inversions: G stands on B, E minor on G, C on E.', c(121, 'yk')),
  ('piano', 'C3*2 B2*2 A2*2 G2*2 F2*2 E2*2 F2*2 G2*2 | [C3 E4 G4 C5] [B2 D4 G4 B4] [A2 C4 E4 A4] [G2 B3 E4 G4] [F2 A3 C4 F4] [E2 G3 C4 E4] [F2 A3 C4 F4] [G2 B3 D4 G4]', c(121, 'yk')),
  ('B', 'Now listen to the bass with the famous violin tune on top: mi re do ti la so la ti.', c(121, 'yk')),
  ('piano', 'C3*2 B2*2 A2*2 G2*2 F2*2 E2*2 F2*2 G2*2 || E5*2 D5*2 C5*2 B4*2 A4*2 G4*2 A4*2 B4*2', c(121, 'yk')),
  ('B', 'And the part everybody hums: so, mi fa so, mi fa so, so la ti do re mi fa.', c(121, 'yk')),
  ('piano', 'C3*2 B2*2 A2*2 G2*2 F2*2 E2*2 F2*2 G2*2 || G5 E5/2 F5/2 G5 E5/2 F5/2 G5/2 G4/2 A4/2 B4/2 C5/2 D5/2 E5/2 F5/2 E5 C5/2 D5/2 E5 E4/2 F4/2 G4/2 A4/2 G4/2 F4/2 G4/2 E4/2 F4/2 G4/2', c(121, 'yk')),
  ('P', 'That’s the wedding music! It sounds like a staircase in a palace.', c(121, 'yk')),
  ('B', 'Two traps: never name a chord from its bass note in an inversion; restack it in thirds first. And an inversion is not a new chord: E G C is still C major. Until next time, Clara.', c(121, 'watch')),
  ('P', 'Bye, Butler!', c(121, 'watch'))])])

NEW['H5'] = ('Seventh chords', [
 ('The secret', [
  ('B', 'Clara, what if our cake had one more layer?', c(122, 'h:Seventh chords')),
  ('P', 'Then it would be a better cake.', c(122, 'lead')),
  ('B', 'A different cake, anyway. Add one more layer, and the chord changes colour: dreamy, bluesy, spooky. Same rule as before: skip one note, stack the next. The new note is the seventh.', c(122, 'lead')),
  ('B', 'Build the triad, C E G. Skip one, add the next: B. Count the keys between: three, two, three. That is C major seven.', c(122, 'two')),
  ('piano', 'C4 E4 G4 B4 | [C4 E4 G4 B4]', c(122, 'two')),
  ('P', 'Ooh, that sounds like a film about a summer holiday.', c(122, 'two'))]),
 ('Five flavours', [
  ('B', 'There are five flavours, all on C. Major seven: dreamy, like bossa nova.', c(122, 'k7')),
  ('piano', '[C4 E4 G4 B4]', c(122, 'k7')),
  ('B', 'Seven: bluesy. The top goes down just one key, to B flat. Its full name is the dominant seventh: C seven, or C dominant seventh. Dominant, because in a key it lives on the fifth note, the dominant: G seven in C major.', c(122, 'k7')),
  ('piano', '[C4 E4 G4 Bb4]', c(122, 'k7')),
  ('B', 'Minor seven: mellow, like a soul ballad.', c(122, 'k7')),
  ('piano', '[C4 Eb4 G4 Bb4]', c(122, 'k7')),
  ('B', 'Half-diminished: searching, like a detective in the rain.', c(122, 'k7')),
  ('piano', '[C4 Eb4 Gb4 Bb4]', c(122, 'k7')),
  ('B', 'And diminished seven: spooky, the chord of every old film villain.', c(122, 'k7')),
  ('piano', '[C4 Eb4 Gb4 A4]', c(122, 'k7')),
  ('P', 'Mwa-ha-ha!', c(122, 'k7')),
  ('B', 'Exactly the right reaction. And on every note of C major there is a seventh too: C major seven, D minor seven, E minor seven, F major seven, G seven, A minor seven and B half-diminished.', c(122, 'vx')),
  ('piano', '[C4 E4 G4 B4] [D4 F4 A4 C5] [E4 G4 B4 D5] [F4 A4 C5 E5] [G4 B4 D5 F5] [A4 C5 E5 G5] [B4 D5 F5 A5]', c(122, 'vx'))]),
 ('Spot the difference', [
  ('B', 'One note decides it. B makes C major seven, B flat makes C seven. Everything below stays the same.', c(123, 'vx')),
  ('piano', '[C4 E4 G4 B4] [C4 E4 G4 Bb4]', c(123, 'vx')),
  ('B', 'Which seventh is G B D F? Count the keys between each layer.', c(123, 'ex1')),
  ('pause', 5, c(123, 'ex1')),
  ('P', 'Three, two, two. The bluesy one! G seven.', c(123, 'ex1', reveal=True)),
  ('piano', '[G3 B3 D4 F4] [C4 E4 G4]', c(123, 'ex1', reveal=True)),
  ('B', 'Hear how G seven wants to fall home to C? Game: name each chord. F A C E, C E G B flat, D F A C.', c(123, 'game')),
  ('pause', 5, c(123, 'game')),
  ('P', 'F major seven, C seven, D minor seven.', c(123, 'game', reveal=True)),
  ('B', 'Try it: C seven, then C major seven. One key changes the top layer: bluesy, then dreamy.', c(123, 'try10')),
  ('piano', '[C4 E4 G4 Bb4] [C4 E4 G4 B4]', c(123, 'try10'))]),
 ('Examples: build sevenths', [
  ('B', 'C major seven or C seven: which note changes? Compare the top layers.', c(124, 'ex2')),
  ('pause', 3, c(124, 'ex2')),
  ('P', 'Only the top: B, three keys between, is major seven. B flat, two between, is seven.', c(124, 'ex2', reveal=True)),
  ('B', 'Build G seven. G major is G B D. Skip one more letter above D: which, and how many keys between?', c(124, 'ex3')),
  ('pause', 4, c(124, 'ex3')),
  ('P', 'F. D to F has two between, so the bluesy one: G B D F, G seven.', c(124, 'ex3', reveal=True)),
  ('B', 'And A minor seven: A, C, E, then the next letter but one above E.', c(124, 'ex4')),
  ('pause', 3, c(124, 'ex4')),
  ('P', 'G! A C E G: two, three, two. A minor seven.', c(124, 'ex4', reveal=True)),
  ('piano', '[A3 C4 E4 G4]', c(124, 'ex4', reveal=True)),
  ('B', 'Two traps: seven alone always means the bluesy one, with the lower top. And count the seventh up from the root, not from the fifth. Until next time, Clara.', c(124, 'watch')),
  ('P', 'Bye, Butler! Mwa-ha-ha!', c(124, 'watch'))])])
for _k in ('H3', 'H4', 'H5'): CH[_k] = NEW[_k]

NEW['H6'] = ('Colour chords', [
 ('The secret', [
  ('B', 'Clara, the third of a chord is its mood: major or minor, happy or sad. Now watch what happens when we play with it.', c(125, 'h:Colour chords')),
  ('B', 'Slide it aside, take it away, or add one note, and a plain chord takes on a new colour. Five colours, all from C E G.', c(125, 'lead')),
  ('B', 'Start from C E G. Slide the E up to the next letter, F: C sus four.', c(125, 'two')),
  ('piano', '[C4 E4 G4] [C4 F4 G4]', c(125, 'two')),
  ('B', 'Or down to the letter below, D: C sus two.', c(125, 'two')),
  ('piano', '[C4 E4 G4] [C4 D4 G4]', c(125, 'two')),
  ('P', 'It sounds like it’s waiting for something. Like holding your breath.', c(125, 'two')),
  ('B', 'Exactly. With no third, the chord is neither major nor minor: it hangs in the air, like a question nobody has answered yet.', c(125, 'secret'))]),
 ('Five colours on C', [
  ('B', 'Here are all five. Sus two, open.', c(125, 'k7')),
  ('piano', '[C4 D4 G4]', c(125, 'k7')),
  ('B', 'Sus four, floating.', c(125, 'k7')),
  ('piano', '[C4 F4 G4]', c(125, 'k7')),
  ('B', 'C five, no third at all: strong.', c(125, 'k7')),
  ('piano', '[C3 G3 C4]', c(125, 'k7')),
  ('B', 'C six, with A on top: warm.', c(125, 'k7')),
  ('piano', '[C4 E4 G4 A4]', c(125, 'k7')),
  ('B', 'And C add nine, with D on top: sparkly.', c(125, 'k7')),
  ('piano', '[C4 E4 G4 D5]', c(125, 'k7')),
  ('P', 'Open, floating, strong, warm, sparkly. It’s like a paint box!', c(125, 'k7')),
  ('B', 'And now the famous shimmer. Lean, then slide back: C, sus four, C, sus two, C. Guitarists love this one.', c(125, 'vx')),
  ('piano', '[C4 E4 G4] [C4 F4 G4] [C4 E4 G4] [C4 D4 G4] [C4 E4 G4]', c(125, 'vx'))]),
 ('Spot the difference', [
  ('B', 'The same red D can do two jobs. C sus two throws the E out. C add nine keeps the E and puts the D on top.', c(126, 'vx')),
  ('piano', '[C4 D4 G4] [C4 E4 G4 D5]', c(126, 'vx')),
  ('B', 'And the power chord: just the root and the fifth, low in the left hand. Neither happy nor sad, only strong: the sound of rock guitar. C five, F five, G five, C five.', c(126, 'two')),
  ('piano', '[C2 G2 C3] [C2 G2 C3] [F2 C3 F3] [F2 C3 F3] [G2 D3 G3] [G2 D3 G3] [C2 G2 C3]', c(126, 'two')),
  ('P', 'I need sunglasses and a leather jacket for that one.', c(126, 'two')),
  ('B', 'C six or A minor seven? The same four notes, C E G A. The bottom note decides. C at the bottom is C six; A at the bottom is A minor seven.', c(126, 'two2')),
  ('piano', '[C4 E4 G4 A4] [A3 C4 E4 G4]', c(126, 'two2'))]),
 ('Examples: which colour?', [
  ('B', 'Which colour is G C D? Count the keys between, G to C, then C to D. Is there a third?', c(126, 'ex1')),
  ('pause', 5, c(126, 'ex1')),
  ('P', 'Four, then one, and no B. G sus four!', c(126, 'ex1', reveal=True)),
  ('piano', '[G3 C4 D4] [G3 B3 D4]', c(126, 'ex1', reveal=True)),
  ('B', 'Swap the C for B, and you have plain G major. Game: sus two, sus four or add nine? C D G, C F G, C E G D.', c(126, 'game')),
  ('pause', 5, c(126, 'game')),
  ('P', 'Sus two, sus four, add nine.', c(126, 'game', reveal=True)),
  ('B', 'Try it: C sus four, then C. No third, then a third: floating, then bright.', c(127, 'try10')),
  ('piano', '[C4 F4 G4] [C4 E4 G4]', c(127, 'try10'))]),
 ('Examples: build them', [
  ('B', 'Build D sus four. Start with D major, D, F sharp, A. Sus four: move the middle layer up to the next letter.', c(127, 'ex2')),
  ('pause', 4, c(127, 'ex2')),
  ('P', 'F sharp moves up to G: D, G, A.', c(127, 'ex2', reveal=True)),
  ('piano', '[D4 F#4 A4] [D4 G4 A4] [D4 F#4 A4]', c(127, 'ex2', reveal=True)),
  ('B', 'And F add nine. Keep F A C, and add the ninth: the second, an octave up. Which letter comes just after F?', c(127, 'ex3')),
  ('pause', 4, c(127, 'ex3')),
  ('P', 'G! F, A, C, G.', c(127, 'ex3', reveal=True)),
  ('piano', '[F3 A3 C4 G4]', c(127, 'ex3', reveal=True)),
  ('B', 'Think of decorating the cake: a ribbon, the sixth, or a candle, the ninth, and it’s still the same cake. A sus moves its middle layer; a power chord takes the middle layer out. Until next time, Clara.', c(127, 'think')),
  ('P', 'Bye, Butler!', c(127, 'think'))])])

NEW['H7'] = ('The tower: 9, 11, 13', [
 ('The secret', [
  ('P', 'Butler, after the seventh layer, can the cake keep growing?', c(128, 'h:The tower: 9, 11, 13')),
  ('B', 'All the way up, like a wedding cake for a giant. Keep stacking thirds and the cake grows three more layers: the ninth, the eleventh and the thirteenth. At the top you have used all seven letters.', c(128, 'lead')),
  ('B', 'Build C seven: C E G B flat. Keep skipping one letter: D, F, A. Those are the ninth, eleventh and thirteenth.', c(128, 'two')),
  ('piano', 'C3 E3 G3 Bb3 D4 F4 A4 | [C3 E3 G3 Bb3 D4 F4 A4]', c(128, 'two')),
  ('P', 'That’s a lot of cake.', c(128, 'two')),
  ('B', 'And here is the secret: take seven away to find the letter. Nine is the second, D. Eleven is the fourth, F. Thirteen is the sixth, A. Same letters, an octave up.', c(128, 'secret'))]),
 ('Five tall chords on C', [
  ('B', 'Five tall chords on C. C nine: soulful, funk and soul.', c(128, 'vx2')),
  ('piano', '[C3 E3 G3 Bb3 D4]', c(128, 'vx2')),
  ('B', 'C major nine: dreamy, film music.', c(128, 'vx2')),
  ('piano', '[C3 E3 G3 B3 D4]', c(128, 'vx2')),
  ('B', 'C minor nine: smooth, like a slow soul song.', c(128, 'vx2')),
  ('piano', '[C3 Eb3 G3 Bb3 D4]', c(128, 'vx2')),
  ('B', 'C eleven, airy, gospel.', c(128, 'vx2')),
  ('piano', '[C3 G3 Bb3 D4 F4]', c(128, 'vx2')),
  ('B', 'And C thirteen, rich: the end of a jazz song.', c(128, 'vx2')),
  ('piano', '[C3 E3 Bb3 D4 A4]', c(128, 'vx2')),
  ('P', 'They all sound like grown-up music in a café.', c(128, 'vx2'))]),
 ('Leave some out', [
  ('B', 'Ten fingers, seven layers: you choose. Keep the third and the seventh, they say what kind of chord it is, and the top note, its colour. Leave out the fifth first. Two hands play C thirteen with four notes: C in the left hand, B flat, E, A in the right.', c(129, 'two')),
  ('piano', '[C3 E3 G3 Bb3 D4 F4 A4] | [C3 Bb3 E4 A4]', c(129, 'two')),
  ('P', 'The second one is clearer! Like tidying my room.', c(129, 'two')),
  ('B', 'And with a major third, the eleventh, F, rubs against E. So C thirteen leaves out the F. C eleven does the opposite: keeps the F, leaves out the E.', c(129, 'two')),
  ('B', 'Six or thirteen? Add nine or nine? Look for the seventh. No seventh: a colour chord. A seventh: a tower chord.', c(129, 'ht'))]),
 ('Example: name a tall chord', [
  ('B', 'Name this tall chord: G B D F A. Find the root, count the first four layers, then the top.', c(129, 'ex1')),
  ('pause', 5, c(129, 'ex1')),
  ('P', 'G seven, three two two, with A on top: the ninth. G nine!', c(129, 'ex1', reveal=True)),
  ('piano', '[G2 B2 D3 F3 A3]', c(129, 'ex1', reveal=True)),
  ('B', 'Game: which floor? The ninth of C, the eleventh of C, the thirteenth of C.', c(129, 'game')),
  ('pause', 4, c(129, 'game')),
  ('P', 'D, F, A.', c(129, 'game', reveal=True)),
  ('B', 'Try it: left hand C E G, right hand B flat, then add the next letter but one above it. You just built a tall chord.', c(130, 'try10')),
  ('piano', '[C3 E3 G3 Bb3] [C3 E3 G3 Bb3 D4]', c(130, 'try10'))]),
 ('Example: build C9', [
  ('B', 'Build C nine. Build C seven, then skip one more letter above B flat.', c(130, 'ex2')),
  ('pause', 3, c(130, 'ex2')),
  ('P', 'D! C, E, G, B flat, D.', c(130, 'ex2', reveal=True)),
  ('piano', '[C3 E3 G3 Bb3 D4]', c(130, 'ex2', reveal=True)),
  ('B', 'The method: start on the root and skip one letter each time, one, three, five, seven, nine, eleven, thirteen. Stop at the number in the name. Leave out the fifth first.', c(130, 'howto')),
  ('B', 'And the traps: the ninth is just the second, an octave higher, no hunting far up. C thirteen is not C six: it has the seventh too. Until next time, Clara.', c(130, 'watch')),
  ('P', 'Bye, Butler!', c(130, 'watch'))])])

NEW['H8'] = ('Slash chords', [
 ('The secret', [
  ('P', 'Butler, my songbook says C slash E. Is that maths?', c(131, 'h:Slash chords')),
  ('B', 'Not a fraction, and not two chords. C slash E means one chord with a chosen bass note: play a C chord, with E as the lowest note.', c(131, 'lead')),
  ('B', 'Here is the secret: chord before the slash, bass note after it. C means C E G, in the right hand. E goes in the left hand, below everything. Together: C over E.', c(131, 'two')),
  ('piano', '[E2 C4 E4 G4]', c(131, 'two')),
  ('P', 'So it’s a cake on a plate. The chord is the cake, the bass is the plate.', c(131, 'secret')),
  ('B', 'A beautiful way to put it. Same cake, new plate, new view.', c(131, 'secret'))]),
 ('Four jobs', [
  ('B', 'Slash chords have four jobs. One: an inversion, for smoother changes. Two: a walk-down, a bass that steps down. Three: a pedal, the same bass held while the chords change. And four: colour, a bass from outside the chord.', c(131, 'ht')),
  ('B', 'Job two: listen to the bass walk straight down, C, B, A, G, F, while the right hand hardly moves.', c(131, 'vx')),
  ('piano', '[C3 C4 E4 G4] [B2 B3 D4 G4] [A2 A3 C4 E4] [G2 G3 C4 E4] [F2 F3 A3 C4]', c(131, 'vx')),
  ('P', 'Like walking down the stairs carrying a tray very carefully.', c(131, 'vx')),
  ('B', 'Job three: a pedal. The bass holds C while the chords change above it: C, F over C, G over C, C. It’s called a pedal after the organ’s foot pedals.', c(132, 'vx')),
  ('piano', '[C2 C4 E4 G4] [C2 C4 F4 A4] [C2 B3 D4 G4] [C2 C4 E4 G4]', c(132, 'vx')),
  ('B', 'And job four: F over G. G isn’t in the F chord, so it floats, open and unfinished. Pop and gospel players love it.', c(132, 'two')),
  ('piano', '[G2 F4 A4 C5] [C3 C4 E4 G4]', c(132, 'two'))]),
 ('Example: name the slash chord', [
  ('B', 'Name the slash chord. The right hand plays G B D. The lowest note in the left hand is B.', c(132, 'ex1')),
  ('pause', 4, c(132, 'ex1')),
  ('P', 'G slash B! G over B.', c(132, 'ex1', reveal=True)),
  ('piano', '[B2 G4 B4 D5]', c(132, 'ex1', reveal=True)),
  ('B', 'And B is in the G chord, so it’s the first inversion. Game: read the slash. G slash B, C slash G, F slash A, A minor slash C. Which note goes in the left hand?', c(132, 'game')),
  ('pause', 5, c(132, 'game')),
  ('P', 'B, G, A, and C.', c(132, 'game', reveal=True))]),
 ('Examples: play them', [
  ('B', 'Try it: right hand C E G, left hand a low E. Now try a low A under it: C over A, the very same notes as A minor seven.', c(133, 'try10')),
  ('piano', '[E2 C4 E4 G4] [A2 C4 E4 G4]', c(133, 'try10')),
  ('B', 'C slash G: which note goes in the left hand?', c(133, 'ex2')),
  ('pause', 3, c(133, 'ex2')),
  ('P', 'G! Low in the left hand, under C E G.', c(133, 'ex2', reveal=True)),
  ('piano', '[G2 C4 E4 G4]', c(133, 'ex2', reveal=True)),
  ('B', 'And walk the bass down: C, C over B, A minor. The right hand holds C E G for two chords, while the left hand walks C, B, A.', c(133, 'ex3')),
  ('piano', '[C3 C4 E4 G4] [B2 C4 E4 G4] [A2 A3 C4 E4]', c(133, 'ex3')),
  ('B', 'Three traps: chord first, bass second. E slash C would be an E chord over C. Keep the right hand above the bass. And in C slash E the right hand still plays the whole C chord. Until next time, Clara.', c(133, 'watch')),
  ('P', 'Bye, Butler!', c(133, 'watch'))])])
for _k in ('H6', 'H7', 'H8'): CH[_k] = NEW[_k]

# ---- her 11 Nov, decision 2: an opening-map narration for each Part, like Pitch's Welcome ----
NEW['TO'] = ('Opening map', [
 ('Part Two: Time', [
  ('B', 'Welcome to Part Two, Clara: Time. When, and for how long.', c(49, 'map')),
  ('P', 'Is this the part where I finally learn to count properly?', c(49, 'map')),
  ('B', 'It is. Music never stands still. Underneath it runs a steady pulse, like a heartbeat, packed into bars, like carriages on a train. And every note and every rest gets its fair share of the time.', c(49, 'map')),
  ('B', 'Everything in this part fits into the two little bars on this page. Listen.', c(49, 'map')),
  ('count', {'beats': 'X x M x X x M x', 'notes': 'C5 C5*2 R C5/2 C5/2 C5*1.5 C5/2 C5*2', 'say': '1 2 3 4 1 2 3 4'}, c(49, 'map')),
  ('P', 'Long ones, short ones, a silence, and a dot!', c(49, 'map')),
  ('B', 'Eight chapters will explain every bit of it: the pulse, notes and rests, dots and ties, time signatures, skipping six-eight, upbeats, rhythms off the beat, and the road signs that send you back. Shall we start with the pulse?', c(49, 'map')),
  ('P', 'One, two, three, four. Yes!', c(49, 'map'))])])

NEW['EO'] = ('Opening map', [
 ('Part Three: Expression', [
  ('B', 'Welcome to Part Three, Clara: Expression. How it should sound.', c(75, 'map')),
  ('B', 'The notes say what to play. Expression says how: loud or soft, smooth or short, faster or slower, ringing or dry. It’s the difference between reading a story in a flat robot voice and telling it like a storyteller.', c(75, 'map')),
  ('P', 'I am a very good storyteller. Ask my brother.', c(75, 'map')),
  ('B', 'I believe you. Listen to the three bars on this page: soft growing to loud, smooth then short, a trill, slowing down, and a pause at the end.', c(75, 'map')),
  ('piano', 'p:C4_ mp:D4_ mp:E4_ mf:F4 | f:G4! f:G4! f:G4! f:G4! | E5/4 F5/4 E5/4 F5/4 E5*1.5 mf:D5 p:C5*4', c(75, 'map')),
  ('P', 'It sounded like a whole little story!', c(75, 'map')),
  ('B', 'Five chapters: loud and soft, touch, speed words, the pedals, and the sparkle of ornaments. Shall we start with loud and soft?', c(75, 'map')),
  ('P', 'Yes, please!', c(75, 'map'))])])

NEW['SO'] = ('Opening map', [
 ('Part Four: Scales and keys', [
  ('B', 'Welcome to Part Four, Clara: Scales and keys. Notes in families.', c(92, 'map')),
  ('B', 'Notes travel in families, like ducklings following their mother. We will build the scales that whole pieces are made from, then learn to read the key a piece lives in: its signature, its home note, and its place on the circle.', c(92, 'map')),
  ('B', 'All of it is in this one scale: G major, with its one sharp.', c(92, 'map')),
  ('piano', 'G4 A4 B4 C5 D5 E5 F#5 G5 | F#5 E5 D5 C5 B4 A4 G4*2', c(92, 'map')),
  ('P', 'Up the stairs and down again. And there’s a clock at the bottom!', c(92, 'map')),
  ('B', 'The circle of fifths: the map of every key. Five chapters: major scales, minor scales, key signatures, finding the key like a detective, and the circle. Shall we begin?', c(92, 'map')),
  ('P', 'Let’s go!', c(92, 'map'))])])

NEW['HO'] = ('Opening map', [
 ('Part Five: Chords', [
  ('B', 'Welcome to Part Five, Clara: Chords. Build them.', c(109, 'map')),
  ('B', 'Press three notes at once and you have a chord. We will stack them, name them, turn them upside down, and add layers on top. And every chapter of this part is hiding in these four bars of Twinkle, Twinkle.', c(109, 'map')),
  ('piano', '[C3 E3 G3 C4] C4 G4 G4 | [E2 C3 E3 G3 A4] A4 [C3 E3 G3 G4] | [F2 F3 A3 C4 F4] F4 [C3 E3 G3 E4] E4 | [G2 C3 D3 G3 D4] [G2 B2 F3 G3 D4] [C3 E3 G3 D4 C4]', c(109, 'map')),
  ('P', 'Twinkle, Twinkle with fancy clothes on!', c(109, 'map')),
  ('B', 'Exactly. Eight chapters: triads, the four kinds, chords in a key, inversions, sevenths, colour chords, the tall tower, and slash chords. Shall we bake our first cake?', c(109, 'map')),
  ('P', 'Cake! Yes!', c(109, 'map'))])])
for _k in ('TO', 'EO', 'SO', 'HO'): CH[_k] = NEW[_k]

# ---- Part VI, Harmony in music (her 11 Nov: "다음으로 넘어가자") ----
NEW['M1'] = ('Chords from outside the key', [
 ('The secret', [
  ('B', 'Clara, today some visitors arrive.', c(136, 'h:Chords from outside the key')),
  ('P', 'Visitors? In the music?', c(136, 'lead')),
  ('G', 'Me, darling! Remember? The Guest with the sharp hat. This time I’ve brought a whole chord with me.', c(136, 'lead')),
  ('B', 'In C major, home is the white keys. So a black key in a chord is a guest. And guests never stay long: each one moves to the very next key, and shows you where the music goes next.', c(136, 'lead')),
  ('B', 'Here is the secret: sharp guests push up, flat guests sigh down. Follow them one key, and you find the next chord.', c(136, 'secret')),
  ('B', 'Listen. C sharp pushes up to D. F sharp pushes up to G. G sharp pushes up to A.', c(136, 'two')),
  ('piano', 'C#4 D4*2 | F#4 G4*2 | G#4 A4*2', c(136, 'two')),
  ('B', 'And A flat sighs down to G. E flat sighs down to D.', c(136, 'two')),
  ('piano', 'Ab4 G4*2 | Eb4 D4*2', c(136, 'two')),
  ('P', 'Like a guest who stands up when they arrive, and one who flops onto the sofa.', c(136, 'two')),
  ('G', 'I never sit still for long. One key, and I’m on my way.', c(136, 'two'))]),
 ('Sharp guests', [
  ('B', 'Exactly. A chord with C sharp, A C sharp E, leads to D minor. With F sharp, D F sharp A, leads to G. With G sharp, E G sharp B, leads to A minor.', c(136, 'gp3')),
  ('piano', '[A3 C#4 E4] [D4 F4 A4] | [D4 F#4 A4] [D4 G4 B4] | [E4 G#4 B4] [E4 A4 C5]', c(136, 'gp3')),
  ('B', 'Try it in a song: C, D, G, C. The F sharp pushes up into G, then G leads home to C.', c(136, 'two2')),
  ('piano', '[C4 E4 G4] [D4 F#4 A4] [D4 G4 B4] [C4 E4 G4]', c(136, 'two2'))]),
 ('Flat guests and the twin', [
  ('B', 'Flat guests come from a twin. C major and C minor are twins: the same home note, C, in different clothes. A flat guest is one piece of the twin’s outfit, borrowed for a moment.', c(136, 'two3')),
  ('B', 'Listen to C, F, F minor, C. The A flat sighs down to G.', c(136, 'two3')),
  ('piano', '[C4 E4 G4] [C4 F4 A4] [C4 F4 Ab4] [C4 E4 G4]', c(136, 'two3')),
  ('P', 'Ooh, that F minor sounds like the end of a sad film where everything turns out fine.', c(136, 'two3')),
  ('B', 'That is precisely what film composers use it for. Here are the twins side by side: C major at home, and C minor in darker clothes.', c(137, 'twins'))]),
 ('Example: where do the guests go?', [
  ('B', 'B, D sharp, F sharp, in C major. Find the black keys: there are two guests. Both are sharps, so where do they land? And which chord in C major holds both landing notes?', c(137, 'ex1')),
  ('pause', 5, c(137, 'ex1')),
  ('P', 'D sharp goes up to E, F sharp up to G. Both live in E minor!', c(137, 'ex1', reveal=True)),
  ('piano', '[B3 D#4 F#4] [B3 E4 G4]', c(137, 'ex1', reveal=True)),
  ('B', 'Game: where does each guest go? Find the guest, follow it one key, and name the next chord.', c(138, 'game')),
  ('pause', 6, c(138, 'game')),
  ('P', 'C sharp up to D: D minor. The A flat goes down to G, and the E flat down to D: G. F sharp up to G: G.', c(138, 'game', reveal=True))]),
 ('Try it', [
  ('B', 'Play C, F, F minor, C slowly, and hear the A flat sigh. Then C, D, G, C, and hear the F sharp push. One sighs, one pushes.', c(138, 'try10')),
  ('piano', '[C4 E4 G4] [C4 F4 A4] [C4 F4 Ab4] [C4 E4 G4] | [C4 E4 G4] [D4 F#4 A4] [D4 G4 B4] [C4 E4 G4]', c(138, 'try10')),
  ('P', 'Sigh, then push. Like getting out of bed on a Monday.', c(138, 'try10')),
  ('B', 'A surprise guest at dinner: one new face changes the whole conversation, and then everyone goes home. And one trap: in G major, F sharp is at home, not a guest. A guest is a note from outside the key you are in. Until next time, Clara.', c(138, 'think')),
  ('P', 'Bye, Butler!', c(138, 'think'))])])

NEW['M2'] = ('Cadences', [
 ('The secret', [
  ('B', 'Clara, can you read this sentence without stopping: I went to the park then I fed the ducks then I went home.', c(139, 'h:Cadences')),
  ('P', 'I need to breathe! Where are the full stops?', c(139, 'lead')),
  ('B', 'Exactly. A phrase is a musical sentence, and it needs punctuation too. The last two chords of a phrase are its cadence. They tell you: finished, taking a breath, or surprise!', c(139, 'lead')),
  ('B', 'There are four. Perfect: five to one. A full stop. Home, the end.', c(139, 'pc4')),
  ('piano', '[G3 B3 D4] [C4 E4 G4]', c(139, 'pc4')),
  ('B', 'Plagal: four to one. A soft, gentle end, like the Amen at the end of a hymn.', c(139, 'pc4')),
  ('piano', '[F3 A3 C4] [E3 G3 C4]', c(139, 'pc4')),
  ('P', 'A-a-men!', c(139, 'pc4')),
  ('B', 'Imperfect: anything to five. A comma: to be continued...', c(139, 'pc4')),
  ('piano', '[C4 E4 G4] [B3 D4 G4]', c(139, 'pc4')),
  ('B', 'And interrupted: five to six. Surprise! Not home.', c(139, 'pc4')),
  ('piano', '[G3 B3 D4] [A3 C4 E4]', c(139, 'pc4')),
  ('P', 'Huh?! That one tricked me. I was already putting my coat on.', c(139, 'pc4')),
  ('B', 'That is the secret: music has full stops and commas too. Just listen to the last two chords of a phrase.', c(139, 'secret'))]),
 ('Why G7 pulls home', [
  ('B', 'Add the seventh to five, and the full stop gets even stronger. In G seven, two notes lean towards C. The B rises to C, and the F falls to E. Two tiny steps, and you are home.', c(140, 'two')),
  ('piano', '[G3 B3 D4 F4] [C4 E4 G4]', c(140, 'two')),
  ('P', 'It works like the guests! B pushes up, F sighs down.', c(140, 'two'))]),
 ('Examples: how does it end?', [
  ('B', 'How does this phrase end? C, A minor, F, G. Find the last two chords and turn them into numerals.', c(140, 'ex1')),
  ('piano', '[C4 E4 G4] [A3 C4 E4] [F3 A3 C4] [G3 B3 D4]', c(140, 'ex1')),
  ('pause', 4, c(140, 'ex1')),
  ('P', 'F then G: four to five. It lands on five: a comma. Imperfect!', c(140, 'ex1', reveal=True)),
  ('B', 'And how does Twinkle end? Its last two chords in C are G, then C.', c(140, 'ex2')),
  ('piano', 'F4 F4 E4 E4 | [G3 B3 D4] D4 [G3 B3 D4] D4 | [C4 E4 G4 C5]', c(140, 'ex2')),
  ('pause', 3, c(140, 'ex2')),
  ('P', 'Five to one: perfect! The full stop. That’s why it sounds finished.', c(140, 'ex2', reveal=True))]),
 ('Surprise!', [
  ('B', 'G seven, then A minor. G seven leans towards home: you expect C. But the next chord is A minor. Which numeral, and which card?', c(141, 'ex3')),
  ('pause', 4, c(141, 'ex3')),
  ('P', 'Five to six: interrupted! The music turned the corner just before home.', c(141, 'ex3', reveal=True)),
  ('piano', '[G3 B3 D4 F4] [A3 C4 E4]', c(141, 'ex3', reveal=True)),
  ('B', 'Game: punctuate the phrases. Four pairs of chords. Full stop, comma, Amen, or surprise?', c(141, 'game')),
  ('pause', 6, c(141, 'game')),
  ('P', 'Amen, surprise, comma, and full stop.', c(141, 'game', reveal=True)),
  ('B', 'Two traps: not every ending on one is perfect; F to C is plagal. And imperfect ends on five, while perfect starts on five. Until next time, Clara.', c(141, 'watch')),
  ('P', 'Bye, Butler. Full stop.', c(141, 'watch'))])])
for _k in ('M1', 'M2'): CH[_k] = NEW[_k]

NEW['M3'] = ('Chords under a melody', [
 ('The secret', [
  ('B', 'Clara, the melody is the singer, and the chords are the band. Today you choose the band.', c(142, 'h:Chords under a melody')),
  ('P', 'Can I have drums?', c(142, 'lead')),
  ('B', 'Not today. But here is how to choose a chord for each bar: look at the melody’s main notes, the long ones and the ones on beats one and three, then pick the cake that holds them.', c(142, 'lead')),
  ('B', 'That is the secret. And every note of C major lives in one, four or five. C and G live in two of them, so there, let your ear choose.', c(142, 'secret'))]),
 ('Twinkle with its chords', [
  ('B', 'Twinkle, Twinkle, with its band. C C G G sit in one, C. A A in four, F, then G back in one. F F in four, E E in one. D D in five, G, and the last C in one.', c(142, 'vx')),
  ('piano', '[C3 C4] C4 [C3 G4] G4 | [F3 A4] A4 [C3 G4] | [F3 F4] F4 [C3 E4] E4 | [G3 D4] D4 [C3 C4]', c(142, 'vx')),
  ('P', 'Now it sounds like a proper song, not just a tune!', c(142, 'vx')),
  ('B', 'And the left hand can play the chord three ways. Block: all three at once.', c(142, 'vx2')),
  ('piano', '[C3 E3 G3] [C3 E3 G3] [C3 E3 G3] [C3 E3 G3]', c(142, 'vx2')),
  ('B', 'Broken: one at a time, up and down.', c(142, 'vx2')),
  ('piano', 'C3/2 E3/2 G3/2 E3/2 C3/2 E3/2 G3/2 E3/2', c(142, 'vx2')),
  ('B', 'And Alberti: low, high, middle, high. Named after Domenico Alberti, who loved it very much.', c(142, 'vx2')),
  ('piano', 'C3/2 G3/2 E3/2 G3/2 C3/2 G3/2 E3/2 G3/2', c(142, 'vx2')),
  ('P', 'Alberti sounds like a little machine humming.', c(142, 'vx2'))]),
 ('Example: choose the chord', [
  ('B', 'Choose the chord for E D C D, then E E E. In bar one, which notes fall on beats one and three? Which cake holds them? And bar two?', c(143, 'ex1')),
  ('pause', 5, c(143, 'ex1')),
  ('P', 'E and C: they both live in one, C. And E E E is in C too!', c(143, 'ex1', reveal=True)),
  ('piano', '[C3 E4] D4 [C3 C4] D4 | [C3 E4] E4 [C3 E4]', c(143, 'ex1', reveal=True)),
  ('B', 'That’s the start of Mary Had a Little Lamb. Game: pick the cake for three bars. F A F A, D B G B, G E C E.', c(143, 'gt2')),
  ('pause', 5, c(143, 'gt2')),
  ('P', 'Four, five, and one.', c(143, 'gt2', reveal=True))]),
 ('You know this', [
  ('B', 'Mozart’s Sonata in C, the famous easy one. The left hand is an Alberti bass: C G E G is just the C chord broken into low, high, middle, high. Listen to the left hand alone first.', c(143, 'yk')),
  ('piano', 'C4/2 G4/2 E4/2 G4/2 C4/2 G4/2 E4/2 G4/2 | D4/2 G4/2 F4/2 G4/2 C4/2 G4/2 E4/2 G4/2', c(143, 'yk')),
  ('B', 'And now the tune on top.', c(143, 'yk')),
  ('piano', 'C5*2 E5 G5 | B4*1.5 C5/4 D5/4 C5*2 | A5*2 G5 C6 | G5 F5/2 E5/4 F5/4 E5*2', c(143, 'yk')),
  ('P', 'That’s the tune from the music box at my grandma’s!', c(143, 'yk')),
  ('B', 'Very possibly. Picking a chord is like picking a coat for the weather: when the tune changes, change the chord. And keep the left hand softer: the melody is the star, the chords are the stage. Until next time, Clara.', c(143, 'think')),
  ('P', 'Bye, Butler!', c(143, 'think'))])])

NEW['M4'] = ('Progressions everywhere', [
 ('The secret', [
  ('B', 'Clara, a progression is a trip from chord to chord. And here’s a funny thing: a handful of trips turn up in song after song after song.', c(144, 'h:Progressions everywhere')),
  ('P', 'Like everyone in town taking the same bus route?', c(144, 'lead')),
  ('B', 'Exactly. Learn them by their numbers, and you can play them in any key. The secret: most songs take the same few trips: home, away, a pull, and home again.', c(144, 'secret')),
  ('B', 'The pop four: one, five, six, four. In C: C, G, A minor, F. Countless pop songs and ballads.', c(144, 'tripc')),
  ('piano', '[C4 E4 G4] [B3 D4 G4] [A3 C4 E4] [A3 C4 F4] | [C4 E4 G4] [B3 D4 G4] [A3 C4 E4] [A3 C4 F4]', c(144, 'tripc')),
  ('P', 'I know that! It’s in every song on the radio!', c(144, 'tripc')),
  ('B', 'Very nearly. The fifties: one, six, four, five. Old rock and roll and doo-wop.', c(144, 'tripc2')),
  ('piano', '[C4 E4 G4] [A3 C4 E4] [A3 C4 F4] [B3 D4 G4] | [C4 E4 G4] [A3 C4 E4] [A3 C4 F4] [B3 D4 G4]', c(144, 'tripc2')),
  ('B', 'The jazz three-step: two, five, one. D minor seven, G seven, C major seven.', c(144, 'tripc3')),
  ('piano', '[D4 F4 A4 C5] [D4 F4 G4 B4] [C4 E4 G4 B4]', c(144, 'tripc3')),
  ('B', 'And the canon: Pachelbel’s famous trip, and all its many children.', c(144, 'tripc4')),
  ('piano', '[C3 E4 G4] [G2 D4 G4] [A2 C4 E4] [E2 B3 E4] [F2 A3 C4] [C3 G3 C4] [F2 A3 C4] [G2 B3 D4]', c(144, 'tripc4'))]),
 ('Same trip, any key', [
  ('B', 'Change key, and the numbers stay the same. The pop four in G is G, D, E minor, C. In F: F, C, D minor, B flat.', c(144, 'ht')),
  ('piano', '[G3 B3 D4] [F#3 A3 D4] [G3 B3 E4] [G3 C4 E4]', c(144, 'ht')),
  ('B', 'And the most famous trip of all: the twelve-bar blues. Twelve bars, one chord each, and only one, four and five. Make every chord a seventh, and it gets bluesy.', c(144, 'two')),
  ('piano', '[C3 E3 G3 Bb3] [C3 E3 G3 Bb3] [C3 E3 G3 Bb3] [C3 E3 G3 Bb3] | [F3 A3 C4 Eb4] [F3 A3 C4 Eb4] [C3 E3 G3 Bb3] [C3 E3 G3 Bb3] | [G3 B3 D4 F4] [F3 A3 C4 Eb4] [C3 E3 G3 Bb3] [G3 B3 D4 F4]', c(144, 'two')),
  ('P', 'I feel like I should be wearing sunglasses and a cool hat.', c(144, 'two')),
  ('K', 'I played the blues once. The Queen asked me to stop.', c(144, 'two'))]),
 ('Example: the pop four in A', [
  ('B', 'Play the pop four in A major. Write the A major scale, three sharps, and number the notes. Find notes one, five, six and four, and build each cake. Which one is minor?', c(145, 'ex1')),
  ('pause', 6, c(145, 'ex1')),
  ('P', 'In A: A, E, F sharp minor, D. The six is minor!', c(145, 'ex1', reveal=True)),
  ('piano', '[A3 C#4 E4] [G#3 B3 E4] [F#3 A3 C#4] [F#3 A3 D4]', c(145, 'ex1', reveal=True)),
  ('B', 'Same trip, new key. Game: name the trip. C, A minor, F, G. D minor, G, C. And C, G, A minor, F.', c(145, 'game')),
  ('pause', 6, c(145, 'game')),
  ('P', 'The fifties, the jazz three-step, and the pop four!', c(145, 'game', reveal=True)),
  ('B', 'Try it: C, G, A minor, F, four beats each, round four times, and hum any tune you like over it. Watch out: the pop four and the fifties use the same four chords, in a different order. Listen to which comes second. Until next time, Clara.', c(145, 'watch')),
  ('P', 'Bye, Butler! I’m going to write a hit song.', c(145, 'watch'))])])
for _k in ('M3', 'M4'): CH[_k] = NEW[_k]

# ---- Part VII, Shape and style ----
ODE1 = 'E4 E4 F4 G4 G4 F4 E4 D4 C4 C4 D4 E4 E4*1.5 D4/2 D4*2'
ODE2 = 'E4 E4 F4 G4 G4 F4 E4 D4 C4 C4 D4 E4 D4*1.5 C4/2 C4*2'
NEW['F1'] = ('Motifs and phrases', [
 ('The secret', [
  ('B', 'Clara, a tune is built like a story.', c(148, 'h:Motifs and phrases')),
  ('P', 'With a dragon in it?', c(148, 'lead')),
  ('B', 'Sometimes. A tiny idea, the motif, is like a word. It grows into a phrase, a musical sentence. And two phrases make a question and its answer.', c(148, 'lead')),
  ('B', 'That is the secret: a motif is a word, a phrase a sentence. A question ends away from home; an answer comes home.', c(148, 'secret'))]),
 ('A motif', [
  ('B', 'Here is the most famous motif ever written. Four notes: short, short, short, long.', c(148, 'two')),
  ('piano', 'G4/2 G4/2 G4/2 Eb4*3 | F4/2 F4/2 F4/2 D4*4 | G4/2 G4/2 G4/2 Eb4/2 Ab4/2 Ab4/2 Ab4/2 G4/2 Eb5/2 Eb5/2 Eb5/2 C5*3', c(148, 'two')),
  ('P', 'Beethoven! Da-da-da-dum. Again and again!', c(148, 'two')),
  ('B', 'He builds a whole movement out of those four notes, like building a castle out of one kind of brick. A motif is short, two to six notes, and easy to recognise: its rhythm and shape keep coming back.', c(148, 'two'))]),
 ('Question and answer', [
  ('B', 'Now phrases. Ode to Joy begins with two four-bar phrases. Listen to the first. It ends on D, away from home. A question.', c(148, 'vx')),
  ('piano', ODE1, c(148, 'vx')),
  ('P', 'It sounds like it’s asking: and then?', c(148, 'vx')),
  ('B', 'And the second phrase comes home to C. The answer.', c(148, 'vx')),
  ('piano', ODE2, c(148, 'vx')),
  ('B', 'The rule: most phrases are four bars long. A question ends away from the key note; the answer comes home to it.', c(148, 'rule'))]),
 ('Examples', [
  ('B', 'Question or answer? The key is C major. What is the last note of this phrase, and is it home?', c(149, 'ex1')),
  ('pause', 4, c(149, 'ex1')),
  ('P', 'It ends on D, not C. A question!', c(149, 'ex1', reveal=True)),
  ('B', 'Now find the motif. Look at bar one: what shape and rhythm? Then bars two and three.', c(149, 'ex2')),
  ('pause', 4, c(149, 'ex2')),
  ('P', 'Step, step, long: three notes. It comes three times, each a step higher!', c(149, 'ex2', reveal=True)),
  ('piano', 'C4 D4 E4*2 | D4 E4 F4*2 | E4 F4 G4*2', c(149, 'ex2', reveal=True)),
  ('B', 'Game: each phrase is four bars long. How many phrases in a tune of eight bars? Twelve? Sixteen?', c(149, 'gt2')),
  ('pause', 4, c(149, 'gt2')),
  ('P', 'Two, three, four. Easy peasy.', c(149, 'gt2', reveal=True)),
  ('B', 'Try singing a question, and stop on the D: it hangs in the air like a ball thrown up. Then sing the answer and land on C. One trap: don’t play every note the same; each phrase has one high point to grow towards. Until next time, Clara.', c(149, 'watch')),
  ('P', 'Bye, Butler? That was a question.', c(149, 'watch')),
  ('B', 'And here is the answer: bye, Clara.', c(149, 'watch'))])])

NEW['F2'] = ('Repetition and sequence', [
 ('The secret', [
  ('B', 'Clara, composers are very thrifty. They make one idea go a long way.', c(150, 'h:Repetition and sequence')),
  ('P', 'Like my mum making soup out of leftovers?', c(150, 'lead')),
  ('B', 'Exactly like that. They say the idea again, say it again higher or lower, let another hand copy it, or say something completely new. That is the secret.', c(150, 'secret')),
  ('B', 'Four ways. Repetition: the same notes again. Sequence: the same shape, starting higher or lower. Imitation: another hand copies it. And contrast: something new.', c(150, 'ht')),
  ('B', 'A rising sequence: C D E, D E F, E F G. Like climbing stairs with the same three steps each time.', c(150, 'two')),
  ('piano', 'C4 D4 E4*2 D4 E4 F4*2 E4 F4 G4*2 F4 G4 A4*2', c(150, 'two')),
  ('B', 'And a falling one: each time one note lower.', c(150, 'two')),
  ('piano', 'A4 G4 F4*2 G4 F4 E4*2 F4 E4 D4*2 E4 D4 C4*2', c(150, 'two'))]),
 ('Examples', [
  ('B', 'Repetition or sequence? Bar one: which notes? Bar two: the same notes, or the same shape on new notes?', c(150, 'ex1')),
  ('pause', 4, c(150, 'ex1')),
  ('P', 'Same shape, a step higher each bar: a sequence!', c(150, 'ex1', reveal=True)),
  ('B', 'Which hand copies? The right hand plays C D E F G E C. The left hand waits, then?', c(151, 'ex2')),
  ('piano', 'C5 D5 E5 F5 G5 E5 C5*2 | C3 D3 E3 F3 G3 E3 C3*2', c(151, 'ex2')),
  ('pause', 3, c(151, 'ex2')),
  ('P', 'The left hand copies it, two octaves down. Like an echo in a cave!', c(151, 'ex2', reveal=True)),
  ('B', 'Imitation. And where is the contrast here? Bars one and two, then bar three?', c(151, 'ex3')),
  ('pause', 4, c(151, 'ex3')),
  ('P', 'Bars one and two repeat, and bar three brings something new: long notes on G.', c(151, 'ex3', reveal=True)),
  ('B', 'Game: name each one. Same notes. One step up. Left hand copies. New rhythm.', c(151, 'gt2')),
  ('pause', 5, c(151, 'gt2')),
  ('P', 'Repetition, sequence, imitation, contrast.', c(151, 'gt2', reveal=True))]),
 ('You know this', [
  ('B', 'Frère Jacques does nearly everything. Every bar is said twice: repetition. And sung as a round, each voice comes in two bars after the last: imitation.', c(151, 'yk')),
  ('piano', 'C4 D4 E4 C4 C4 D4 E4 C4 E4 F4 G4*2 E4 F4 G4*2 | G4/2 A4/2 G4/2 F4/2 E4 C4 G4/2 A4/2 G4/2 F4/2 E4 C4 C4 G3 C4*2 C4 G3 C4*2', c(151, 'yk')),
  ('P', 'Are you sleeping, Brother John? Ding dang dong!', c(151, 'yk')),
  ('B', 'Try it as a round with a friend. And one trap: a sequence always moves to new notes; the same notes again is just repetition. Until next time, Clara.', c(151, 'watch')),
  ('P', 'Bye, Butler! Bye, Butler!', c(151, 'watch')),
  ('B', 'Ha. Repetition.', c(151, 'watch'))])])

NEW['F3'] = ('Texture', [
 ('The secret', [
  ('B', 'Clara, run your fingers over your jumper. Feel the threads?', c(152, 'h:Texture')),
  ('P', 'It’s woolly and a bit scratchy.', c(152, 'lead')),
  ('B', 'Music has threads too. Texture is how many lines sound at once, and how they fit together: one line alone, a tune with chords, or several tunes woven together like threads in cloth.', c(152, 'lead')),
  ('B', 'That is the secret: count the lines. One line alone is monophony.', c(152, 'hero')),
  ('piano', 'C4 D4 E4 F4 G4*2 E4 C4*2', c(152, 'hero')),
  ('B', 'A tune with chords is melody and accompaniment.', c(152, 'hero')),
  ('piano', '[C3 E3 G3 C4] D4 [C3 E3 G3 E4] F4 [C3 E3 G3 G4] [C3 E3 G3 E4] [C3 E3 G3 C4]', c(152, 'hero')),
  ('B', 'And two tunes at once, each going its own way, is polyphony.', c(152, 'hero')),
  ('piano', '[C4 E5] [D4 D5] [E4 C5] [F4 B4] [G4 C5] [G4 D5] [C4 C5]', c(152, 'hero')),
  ('P', 'Polyphony sounds like two people chatting at the same time, and somehow it works.', c(152, 'hero'))]),
 ('The words', [
  ('B', 'The grand words: monophonic, one line alone. Homophonic, a tune with chords underneath. Polyphonic, two or more tunes at once. And for the accompaniment: block chords struck together, or an Alberti bass rocking low, high, middle, high.', c(152, 'ht')),
  ('B', 'Game: name the texture. A tune alone. A tune and chords. Two tunes at once.', c(152, 'game')),
  ('pause', 4, c(152, 'game')),
  ('P', 'Monophonic, homophonic, polyphonic. They all rhyme!', c(152, 'game', reveal=True))]),
 ('Examples', [
  ('B', 'Name the texture. The right hand plays a tune, and the left hand plays chords. So which word?', c(153, 'ex1')),
  ('pause', 3, c(153, 'ex1')),
  ('P', 'Homophonic: melody and accompaniment.', c(153, 'ex1', reveal=True)),
  ('B', 'And which hand has the tune here? The right hand repeats two-note chords. The left hand moves step by step.', c(153, 'ex2')),
  ('pause', 4, c(153, 'ex2')),
  ('P', 'The left hand! So it sings out, and the right hand stays soft.', c(153, 'ex2', reveal=True)),
  ('B', 'Exactly. The tune isn’t always on top, like the hero isn’t always the tallest person in the film.', c(153, 'ex2', reveal=True))]),
 ('You know this', [
  ('B', 'Mozart’s Sonata in C again: the right hand sings, the left hand rocks C G E G, an Alberti bass. The sound of the Classical style.', c(153, 'yk')),
  ('piano', 'C5*2 E5 G5 | B4*1.5 C5/4 D5/4 C5*2 | C4/2 G4/2 E4/2 G4/2 C4/2 G4/2 E4/2 G4/2 D4/2 G4/2 F4/2 G4/2 C4/2 G4/2 E4/2 G4/2', c(153, 'yk')),
  ('B', 'Two traps: never let the accompaniment cover the tune. And when there are two tunes, practise each hand alone and sing it, so neither gets lost. Until next time, Clara.', c(153, 'watch')),
  ('P', 'Bye, Butler!', c(153, 'watch'))])])
for _k in ('F1', 'F2', 'F3'): CH[_k] = NEW[_k]

TW = 'C4 C4 G4 G4 A4 A4 G4*2 F4 F4 E4 E4 D4 D4 C4*2'
NEW['F4'] = ('Changing key', [
 ('The secret', [
  ('B', 'Clara, music can go on holiday. It travels to a new key, and then it comes home again. That is a modulation.', c(154, 'h:Changing key')),
  ('P', 'Does it send a postcard?', c(154, 'lead')),
  ('B', 'In a way. The signpost is a new sharp, flat or natural that keeps coming back, and a cadence that lands in the new key.', c(154, 'lead')),
  ('B', 'That is the secret. Here, C major is home. Then F sharp appears: a visit to G major. Then F natural again: home.', c(154, 'hero')),
  ('piano', 'C4 E4 G4 E4 | F#4 A4 D5 F#5 G5*2 | F4 D4 B3 D4 C4*2', c(154, 'hero')),
  ('P', 'Off on holiday, and back home for tea.', c(154, 'hero'))]),
 ('The nearest keys', [
  ('B', 'A piece in C major usually visits the keys next door on the circle of fifths, where only one note changes. To G major, F sharp appears. To F major, B flat appears. And to the relative minor, A minor, G sharp appears.', c(154, 'ht')),
  ('B', 'Listen: bar one in C major; F sharp twice in bar two, then the phrase lands on G. Now we’re in G major.', c(154, 'vx')),
  ('piano', 'C5 B4 A4 G4 | A4 F#4 G4 F#4 | E4 F#4 G4*2', c(154, 'vx')),
  ('B', 'Where does the key change here? Find the accidental, and where the phrase lands.', c(154, 'ex1')),
  ('pause', 4, c(154, 'ex1')),
  ('P', 'B flat in bar two and again in bar three, landing on F. F major!', c(154, 'ex1', reveal=True))]),
 ('Examples', [
  ('B', 'In G major, a C sharp keeps appearing. G major has one sharp, F sharp. C sharp is one more. Which key has both?', c(155, 'ex2')),
  ('pause', 4, c(155, 'ex2')),
  ('P', 'D major, the key a fifth up!', c(155, 'ex2', reveal=True)),
  ('B', 'And here: one F sharp in a bar of C major, then F natural everywhere after. A new key, or just passing?', c(155, 'ex3')),
  ('pause', 4, c(155, 'ex3')),
  ('P', 'A new key!', c(155, 'ex3', oops=True)),
  ('B', 'Not this time. One visitor doesn’t make a move. The F sharp never comes back, and there’s no cadence in G. Just a decoration, passing through.', c(155, 'ex3')),
  ('P', 'Oh. Like a cat walking through the garden, not moving in.', c(155, 'ex3', reveal=True)),
  ('B', 'Game: where to next? C major plus F sharp. C major plus B flat. G major plus C sharp. F major plus E flat.', c(155, 'gt2')),
  ('pause', 6, c(155, 'gt2')),
  ('P', 'G major, F major, D major, and B flat major.', c(155, 'gt2', reveal=True)),
  ('B', 'A modulation is a holiday: new scenery for a while, but the piece usually comes home at the end. So watch for the old note returning. Until next time, Clara.', c(155, 'think')),
  ('P', 'Bye, Butler! Send me a postcard.', c(155, 'think'))])])

NEW['F5'] = ('Form', [
 ('The secret', [
  ('B', 'Clara, form is the map of a whole piece: which sections come, in what order, and which come back. Like a floor plan of a house.', c(156, 'h:Form')),
  ('P', 'So I don’t get lost in the music!', c(156, 'lead')),
  ('B', 'Exactly. We name the sections with letters: A for the first idea, B for the next new one, and so on. The secret: same music, same letter. New music, next letter.', c(156, 'secret')),
  ('B', 'Binary: A B, two halves. Ternary: A B A, out, away and back. Rondo: A B A C A, where A keeps coming home between new ideas. And variations: one tune, dressed differently each time.', c(156, 'hero'))]),
 ('The maps', [
  ('B', 'Binary is the shape of the old dances, like the Minuet in G: two halves, each repeated. Many short Romantic pieces are ternary. And hymns and folk songs are strophic: the same music for every verse. Pop songs go verse, chorus, verse, chorus.', c(156, 'ht')),
  ('B', 'And here is Mozart’s favourite trick: theme and variations, on the tune of Twinkle. First the plain theme.', c(156, 'lis')),
  ('piano', TW, c(156, 'lis')),
  ('B', 'Then the same tune, dressed up in quick notes.', c(156, 'lis')),
  ('piano', 'C4/4 B3/4 C4/4 B3/4 C4/4 B3/4 C4/4 B3/4 G4/4 F#4/4 G4/4 F#4/4 G4/4 F#4/4 G4/4 F#4/4 A4/4 G#4/4 A4/4 G#4/4 A4/4 G#4/4 A4/4 G#4/4 G4/4 F#4/4 G4/4 F#4/4 G4/4 F#4/4 G4/4 F#4/4 | F4/4 E4/4 F4/4 E4/4 F4/4 E4/4 F4/4 E4/4 E4/4 D#4/4 E4/4 D#4/4 E4/4 D#4/4 E4/4 D#4/4 D4/4 C#4/4 D4/4 C#4/4 D4/4 C#4/4 D4/4 C#4/4 C4*2', c(156, 'lis')),
  ('P', 'It’s Twinkle in a sparkly party dress!', c(156, 'lis'))]),
 ('Examples', [
  ('B', 'Which letter makes it ternary? A B alone is two sections. Ternary goes out, away, and...?', c(157, 'ex1')),
  ('pause', 3, c(157, 'ex1')),
  ('P', 'And back! Section A again.', c(157, 'ex1', reveal=True)),
  ('B', 'Which form is A B A C A? Which one keeps coming back?', c(157, 'ex2')),
  ('pause', 3, c(157, 'ex2')),
  ('P', 'A comes back between two new ideas: a rondo!', c(157, 'ex2', reveal=True)),
  ('B', 'Now map Twinkle itself. Bars one to four: A. Bars five to eight: new or the same? And the last four bars repeat bars one to four.', c(157, 'ex3')),
  ('piano', TW + ' | G4 G4 F4 F4 E4 E4 D4*2 G4 G4 F4 F4 E4 E4 D4*2 | ' + TW, c(157, 'ex3')),
  ('pause', 3, c(157, 'ex3')),
  ('P', 'Bars five to eight are new: B. Then A again. A B A: ternary!', c(157, 'ex3', reveal=True)),
  ('B', 'And what comes after A, A one, A two?', c(158, 'ex4')),
  ('pause', 3, c(158, 'ex4')),
  ('P', 'A three! The third variation.', c(158, 'ex4', reveal=True)),
  ('B', 'Game: name each map. Two letters, A, B. Then A, B, A. Then A, B, A, C, A. And A, A one, A two, A three.', c(158, 'game')),
  ('pause', 5, c(158, 'game')),
  ('P', 'Binary, ternary, rondo, and theme and variations.', c(158, 'game', reveal=True))]),
 ('You know this', [
  ('B', 'A clever way to learn a piece: letter the sections in pencil, and learn A first. It comes back, so it pays twice.', c(158, 'howto')),
  ('B', 'Für Elise is a rondo. The famous opening tune is section A, and it is heard three times, with two new sections in between. Raise your hand every time A returns.', c(158, 'yk')),
  ('piano', 'E5/2 D#5/2 E5/2 D#5/2 E5/2 B4/2 D5/2 C5/2 A4 | C4/2 E4/2 A4/2 B4 | E4/2 G#4/2 B4/2 C5 | E4/2 E5/2 D#5/2 E5/2 D#5/2 E5/2 B4/2 D5/2 C5/2 A4*2', c(158, 'yk')),
  ('P', 'Hand up! There it is!', c(158, 'yk')),
  ('B', 'Two traps: don’t give every phrase a new letter, same music means same letter. And section A played twice is still section A. Until next time, Clara.', c(158, 'watch')),
  ('P', 'Bye, Butler!', c(158, 'watch'))])])

NEW['F6'] = ('Styles through time', [
 ('The secret', [
  ('B', 'Clara, music changes with its time, like clothes and buildings. Four big periods cover most piano music.', c(159, 'h:Styles through time')),
  ('P', 'Like a fashion show through history!', c(159, 'lead')),
  ('B', 'Exactly that. Here is the secret: listen for the texture, the ornaments and the pedal. They tell you the century.', c(159, 'secret')),
  ('B', 'Baroque, from about sixteen hundred: Bach, Handel, Scarlatti. Harpsichord and organ, two tunes woven together, lots of ornaments, a steady beat.', c(159, 'hero')),
  ('piano', 'D5 G4/2 A4/2 B4/2 C5/2 D5 G4 G4 E5 C5/2 D5/2 E5/2 F#5/2 G5 G4 G4', c(159, 'hero')),
  ('B', 'Classical, from about seventeen fifty: Haydn, Mozart, Beethoven. The new piano, a clear tune over an Alberti bass, tidy four-bar phrases.', c(159, 'hero')),
  ('piano', 'C5*2 E5 G5 | B4*1.5 C5/4 D5/4 C5*2', c(159, 'hero')),
  ('B', 'Romantic, from about eighteen twenty: Chopin, Schumann, Liszt. Big feelings, rich chords in the pedal, time stretched with rubato.', c(159, 'hero')),
  ('piano', '[pp Eb3 Bb3 G4] p:Bb4 mf:G5*2 p:F5/2 G5/2 F5*1.5 Eb5/2 | [pp Ab2 Eb3 C4] mp:Bb4*2 G5*1.5 C5/2 C6*2', c(159, 'hero')),
  ('B', 'And Modern, from nineteen hundred to today: Debussy, Bartók, jazz and film. New scales, surprising rhythms.', c(159, 'hero')),
  ('piano', 'C5/2 D5/2 E5/2 F#5/2 G#5/2 A#5/2 [C4 E4 G#4 C5] | [D4 F#4 A#4 D5]', c(159, 'hero')),
  ('P', 'The last one is the whole-tone scale from the beginning of every chapter!', c(159, 'hero')),
  ('B', 'Well spotted! Debussy loved it.', c(159, 'hero'))]),
 ('Playing in style', [
  ('B', 'And each period wants to be played its own way. Baroque: little or no pedal, steady time, a clear, often detached touch. Classical: light pedal, steady, neat and singing. Romantic: rich pedal, rubato, deep legato. Modern: whatever the music asks.', c(159, 'ht2')),
  ('Q', 'One does not pedal Bach like Chopin, Clara. It is like wearing a ball gown to a picnic.', c(159, 'ht2'))]),
 ('Examples: which period?', [
  ('B', 'A tune over an Alberti bass, tidy four-bar phrases. Which period?', c(160, 'ex1')),
  ('pause', 3, c(160, 'ex1')),
  ('P', 'Classical: think Mozart.', c(160, 'ex1', reveal=True)),
  ('B', 'Two equal tunes, many trills, written for harpsichord?', c(160, 'ex2')),
  ('pause', 3, c(160, 'ex2')),
  ('P', 'Baroque: think Bach.', c(160, 'ex2', reveal=True)),
  ('B', 'Rubato, rich pedalled chords, huge leaps across the keyboard?', c(160, 'ex3')),
  ('pause', 3, c(160, 'ex3')),
  ('P', 'Romantic: think Chopin.', c(160, 'ex3', reveal=True)),
  ('B', 'Game: who belongs where? Bach, Mozart, Chopin, Debussy.', c(160, 'game')),
  ('pause', 4, c(160, 'game')),
  ('P', 'Baroque, Classical, Romantic, Modern. In order, like a timeline!', c(160, 'game', reveal=True)),
  ('B', 'Two traps: don’t pedal Bach like Chopin, and don’t use Romantic rubato in Mozart. Keep Classical time steady. Until next time, Clara.', c(160, 'watch')),
  ('P', 'Bye, Butler!', c(160, 'watch'))])])
for _k in ('F4', 'F5', 'F6'): CH[_k] = NEW[_k]

# ---- Part VIII, Playing and listening ----
NEW['L1'] = ('Fingering', [
 ('The secret', [
  ('B', 'Clara, we begin the last part with your fingers.', c(163, 'h:Fingering')),
  ('P', 'I have ten. I counted.', c(163, 'lead')),
  ('B', 'Excellent. Each finger has a number, the same in both hands: the thumb is one, the little finger five. And here is the secret: good fingering is planned, not guessed. Choose it once, write it in, and use it every time.', c(163, 'secret')),
  ('B', 'Thumbs are one in both hands. So the right hand counts one to five going up, and the left hand counts five to one.', c(163, 'hero'))]),
 ('Five-finger position', [
  ('B', 'Thumb on C, one finger on each key up to G: five notes without moving the hand. Many first pieces stay right here, like a cat curled up in its basket.', c(163, 'two')),
  ('piano', 'C4 D4 E4 F4 G4 F4 E4 D4 C4*2', c(163, 'two')),
  ('B', 'And to go further, thumb under, finger over. Up the scale: one, two, three, then the thumb tucks under to F, then one, two, three, four, five.', c(163, 'two2')),
  ('piano', 'C4 D4 E4 F4 G4 A4 B4 C5*2', c(163, 'two2')),
  ('B', 'Coming down: five, four, three, two, one, then finger three crosses over the thumb.', c(163, 'two2')),
  ('piano', 'C5 B4 A4 G4 F4 E4 D4 C4*2', c(163, 'two2')),
  ('P', 'The thumb is like a little tunnel under a bridge!', c(163, 'two2')),
  ('B', 'A smooth tunnel, please, no bumps. Two-minute drill: C D E F G with each hand, saying the finger numbers. Right one, two, three, four, five up; left five, four, three, two, one up. Then both together.', c(163, 'drill'))]),
 ('Examples', [
  ('B', 'Which finger plays the F in the C major scale? C, D, E are one, two, three. Then: finger four, or the thumb tucked under?', c(164, 'ex1')),
  ('pause', 4, c(164, 'ex1')),
  ('P', 'Finger four!', c(164, 'ex1', oops=True)),
  ('B', 'Then you’d run out of fingers before the top C. Count: four, five, and three more notes to go.', c(164, 'ex1')),
  ('P', 'Oh! The thumb passes under to F, and then two, three, four, five reach the top C.', c(164, 'ex1', reveal=True)),
  ('B', 'And right hand, thumb on C: which finger plays G?', c(164, 'ex2')),
  ('pause', 3, c(164, 'ex2')),
  ('P', 'Five! C D E F G is one two three four five.', c(164, 'ex2', reveal=True)),
  ('B', 'Game: name the finger. Thumb, index, middle, little.', c(164, 'gt2')),
  ('pause', 4, c(164, 'gt2')),
  ('P', 'One, two, three, five.', c(164, 'gt2', reveal=True)),
  ('B', 'Two traps: don’t change fingering every time you play; choose one and keep it. And let the thumb glide under, don’t land on it like a sack of potatoes. Until next time, Clara.', c(164, 'watch')),
  ('P', 'Bye, Butler! Five, four, three, two, one!', c(164, 'watch'))])])

NEW['L2'] = ('Practising well', [
 ('The secret', [
  ('P', 'Butler, I practise every day. I play my piece from the top, again and again and again.', c(165, 'h:Practising well')),
  ('B', 'Ah. That’s like learning to ride a bike by only riding the easy bit of the road. Practice is fixing the hard bits, slowly and correctly, then joining them back together.', c(165, 'lead')),
  ('B', 'Here is the secret: slow, small, and correct. Then a little faster. Then join the pieces. Three correct times at one speed, then one step up the ladder.', c(165, 'secret')),
  ('count', {'beats': 'X@60 x@60 x@60 x@60 X@72 x@72 x@72 x@72 X@88 x@88 x@88 x@88', 'notes': 'C4@60 E4@60 G4@60 E4@60 C4@72 E4@72 G4@72 E4@72 C4@88 E4@88 G4@88 E4@88', 'say': '1 2 3 4 1 2 3 4 1 2 3 4'}, c(165, 'hero')),
  ('P', 'Sixty, seventy-two, eighty-eight. Climbing the ladder.', c(165, 'hero'))]),
 ('A fifteen-minute plan', [
  ('B', 'A fifteen-minute plan. Two minutes: warm up with a scale. Five minutes: the hardest bars, slowly, hands separately. Five minutes: join the bars, hands together, still slow. And three minutes: play the whole section, and mark what slipped.', c(165, 'ht')),
  ('B', 'Four tools. Small chunks: one or two bars, plus the first note of the next. Hands separately. Slow, then faster. And count aloud: it keeps the rhythm honest.', c(165, 'ht2')),
  ('B', 'And a trick: for a run of even quavers, play it long, short, then short, long. When you go back to even notes, the run is suddenly easier.', c(165, 'xbox')),
  ('piano', 'C4*0.75 D4/4 E4*0.75 F4/4 G4*0.75 A4/4 B4*0.75 C5/4 | C4/4 D4*0.75 E4/4 F4*0.75 G4/4 A4*0.75 B4/4 C5*0.75 | C4/2 D4/2 E4/2 F4/2 G4/2 A4/2 B4/2 C5*2', c(165, 'xbox')),
  ('P', 'Bumpy, then bumpy the other way, then smooth!', c(165, 'xbox'))]),
 ('Examples', [
  ('B', 'Which bar first? You played it through once, and it slipped in the semiquavers of bar three. Where do you start?', c(166, 'ex1')),
  ('pause', 3, c(166, 'ex1')),
  ('P', 'Bar three, slowly. Then join bars two to four.', c(166, 'ex1', reveal=True)),
  ('B', 'And when do you speed up? At sixty you played it right, right, wrong.', c(166, 'ex2')),
  ('pause', 3, c(166, 'ex2')),
  ('P', 'Now! Two right is nearly three.', c(166, 'ex2', oops=True)),
  ('B', 'Nearly isn’t three, I’m afraid. After a mistake, start counting again: three correct in a row at sixty, then try sixty-six.', c(166, 'ex2')),
  ('P', 'Fine. Patience, patience.', c(166, 'ex2', reveal=True)),
  ('B', 'Game: good habit or not? From the top. Hardest first. Faster to fix. Slow and correct.', c(166, 'gt2')),
  ('pause', 4, c(166, 'gt2')),
  ('P', 'Hardest first, and slow and correct. The other two waste time.', c(166, 'gt2', reveal=True)),
  ('B', 'Keep a practice log: the date, one thing that got better and one that didn’t. Start tomorrow with the one that didn’t. Practice is like building a wall: lay each brick straight, and the wall stands on its own. Until next time, Clara.', c(166, 'think')),
  ('P', 'Bye, Butler!', c(166, 'think'))])])

NEW['L3'] = ('Sight-reading', [
 ('The secret', [
  ('B', 'Clara, sight-reading is playing music you have never seen before.', c(167, 'h:Sight-reading')),
  ('P', 'That sounds scary. Like reading a book in the dark.', c(167, 'lead')),
  ('B', 'Not if you bring a torch. Here is the secret: look before you play, then never stop. The beat matters more than any note. A wrong note passes by; a stop is heard by everyone.', c(167, 'secret')),
  ('B', 'Thirty seconds first. One sharp, so G major. Four-four time. It starts on G and steps up in a pattern.', c(167, 'hero')),
  ('piano', 'G4 A4 B4 C5 | A4 B4 C5 D5 | B4 C5 D5 E5 | D5 C5 B4 A4 | G4*4', c(167, 'hero'))]),
 ('The thirty-second scan', [
  ('B', 'The scan has six checks. One: the key, sharps or flats at the start. Two: the time signature, count a bar before you start. Three: the clefs and the first note in each hand. Four: the trickiest rhythm, tap it. Five: patterns, steps, skips, repeats, sequences. And six: the marks, dynamics, slurs, speed words.', c(167, 'ht')),
  ('P', 'Like a pilot checking the plane before take-off!', c(167, 'ht')),
  ('B', 'Exactly like a pilot. And then we take off and don’t stop in mid-air.', c(167, 'ht'))]),
 ('Examples', [
  ('B', 'What do you check first? The key: how many sharps? The time? And the F in bar two: F or F sharp?', c(167, 'ex1')),
  ('pause', 4, c(167, 'ex1')),
  ('P', 'G major, three-four. The F in bar two is F sharp, from the key signature. Count one, two, three, and go!', c(167, 'ex1', reveal=True)),
  ('B', 'A wrong note in bar two. Now what? Stop and fix it, or keep going?', c(167, 'ex2')),
  ('pause', 3, c(167, 'ex2')),
  ('P', 'Keep going and catch the next beat. A stop is heard much more than a wrong note.', c(167, 'ex2', reveal=True)),
  ('B', 'Spot the pattern. Bar one has a shape. Bar two?', c(168, 'ex3')),
  ('pause', 3, c(168, 'ex3')),
  ('P', 'The same shape a step higher: a sequence! So I only really need to read bar one.', c(168, 'ex3', reveal=True)),
  ('B', 'Read the shape, not every note. Game: put the checks in order. Rhythm, key, time, patterns.', c(168, 'gt2')),
  ('pause', 4, c(168, 'gt2')),
  ('P', 'Key, time, rhythm, patterns.', c(168, 'gt2', reveal=True))]),
 ('Read ahead', [
  ('B', 'And the big skill: read ahead. While you play one bar, let your eyes move to the next. Practise by covering each bar with a card as you play it.', c(168, 'howto')),
  ('B', 'Sight-reading is like reading aloud: you look a few words ahead, and if you trip on one, the sentence goes on. Three traps: choose a speed you can keep, keep your eyes on the music, not your hands, and never skip the scan. Until next time, Clara.', c(168, 'think')),
  ('P', 'Bye, Butler! One new piece a day.', c(168, 'think'))])])

NEW['L4'] = ('Listening', [
 ('The secret', [
  ('B', 'Clara, your ear is a musical instrument too.', c(169, 'h:Listening')),
  ('P', 'I can’t play my ear. I’ve tried wiggling it.', c(169, 'lead')),
  ('B', 'Ha! Not like that. You train it in small steps: clap a rhythm back, sing a tune back, then hear whether music goes up or down, is major or minor, and whether it has finished.', c(169, 'lead')),
  ('B', 'Here is the secret: sing it back first. If you can sing it, you can play it.', c(169, 'secret')),
  ('B', 'Questions for your ear: high or low? Loud or soft? Two or three beats in a bar? Major or minor? Finished or not?', c(169, 'hero'))]),
 ('Major or minor?', [
  ('B', 'Major or minor? Only the middle note changes. Listen: C E G, then C E flat G. Bright, then darker.', c(169, 'two')),
  ('piano', '[C4 E4 G4] [C4 Eb4 G4] | C4 E4 G4 | C4 Eb4 G4', c(169, 'two')),
  ('P', 'The sun went behind a cloud.', c(169, 'two'))]),
 ('Intervals by song', [
  ('B', 'And a clever trick: learn the size of a leap from a song you know. A major second: Frère Jacques.', c(169, 'ht')),
  ('piano', 'C4 D4 E4 C4', c(169, 'ht')),
  ('B', 'A major third: Oh When the Saints.', c(169, 'ht')),
  ('piano', 'C4 E4 F4 G4*4', c(169, 'ht')),
  ('B', 'A perfect fourth: Amazing Grace.', c(169, 'ht')),
  ('piano', 'G3 C4*2 E4/2 C4/2 E4*2 D4 C4*2 A3 G3*2', c(169, 'ht')),
  ('B', 'A perfect fifth: Twinkle, from the second note to the third.', c(169, 'ht')),
  ('piano', 'C4 C4 G4 G4 A4 A4 G4*2', c(169, 'ht')),
  ('B', 'A major sixth: My Bonnie Lies Over the Ocean.', c(169, 'ht')),
  ('piano', 'G3 E4 D4 C4 D4 C4 A3 G3 E3*2', c(169, 'ht')),
  ('B', 'And an octave: the first big leap of Somewhere Over the Rainbow. Just the two notes.', c(169, 'ht')),
  ('piano', 'C4*2 C5*2', c(169, 'ht')),
  ('P', 'Now I’ll hear songs everywhere in my intervals!', c(169, 'ht')),
  ('B', 'And to clap it back: someone claps two bars, you clap them straight back, keeping the beat. Then sing back a short tune, then find it on the keys.', c(169, 'howto'))]),
 ('Examples', [
  ('B', 'Finished or not? Listen to two short bars. Which one sounds finished?', c(170, 'ex1')),
  ('piano', '[G3 B3 D4] [C4 E4 G4] | [C4 E4 G4] [B3 D4 G4]', c(170, 'ex1')),
  ('pause', 3, c(170, 'ex1')),
  ('P', 'The first! It comes home to C. The second stops on G: a comma.', c(170, 'ex1', reveal=True)),
  ('B', 'Major or minor? Two chords. Which note changed?', c(170, 'ex2')),
  ('piano', '[G3 Bb3 D4] [G3 B3 D4]', c(170, 'ex2')),
  ('pause', 3, c(170, 'ex2')),
  ('P', 'First minor, then major. Only the middle note moved: B flat up to B.', c(170, 'ex2', reveal=True)),
  ('B', 'Game: which song? A fifth up, an octave up, a fourth up.', c(170, 'gt2')),
  ('pause', 4, c(170, 'gt2')),
  ('P', 'Twinkle, Somewhere Over the Rainbow, and Amazing Grace.', c(170, 'gt2', reveal=True)),
  ('B', 'And one trap: don’t guess from the hands. Close your eyes and listen. Until next time, Clara.', c(170, 'watch')),
  ('P', 'Bye, Butler! My ears are on.', c(170, 'watch'))])])

NEW['L5'] = ('Performing', [
 ('The secret', [
  ('P', 'Butler, I have to play at the school concert. My tummy feels like it’s full of butterflies.', c(171, 'h:Performing')),
  ('B', 'Ah, the butterflies. Nerves are normal, Clara: they mean you care. Playing for others is a skill you can practise, like scales. A routine before you start, and a plan for slips, make the butterflies much smaller.', c(171, 'lead')),
  ('B', 'Here is the secret: breathe, feel a bar of the beat, then begin. And after a slip, catch the next beat.', c(171, 'secret')),
  ('B', 'Four steps to the first note. Breathe out, slowly. Feel one bar of the beat in your head. Begin, calm. And at the end, bow, and smile.', c(171, 'hero')),
  ('count', {'beats': 'X x x x', 'say': '1 2 3 4'}, c(171, 'hero')),
  ('piano', 'C4 C4 G4 G4 A4 A4 G4*2', c(171, 'hero'))]),
 ('Before, during, after', [
  ('B', 'Before: warm up your hands, practise starting, not only the whole piece, and play it to a friend or your family first. At the piano: adjust the bench, feet flat, breathe out, feel one bar of the beat. If you slip: keep the beat going and catch the next beat, or the next phrase. Never go back. And after: hands in your lap for a moment, stand, bow, smile.', c(171, 'ht')),
  ('B', 'The rule: the listener follows the beat and the mood. Keep both going, and a slip is forgotten in a second.', c(171, 'rule')),
  ('Q', 'When I give a speech and forget a word, I simply carry on. Nobody notices, because I am the Queen.', c(171, 'rule')),
  ('K', 'I notice.', c(171, 'rule')),
  ('B', 'Two-minute drill: every day this week, play your piece once from the start without stopping, whatever happens, as if someone were listening.', c(171, 'drill'))]),
 ('Examples', [
  ('B', 'How do you start? You sit down, and your heart is racing. The bench, your breath, the beat?', c(172, 'ex1')),
  ('pause', 4, c(172, 'ex1')),
  ('P', 'Adjust the bench, breathe out, and feel one bar of the speed in my head. Then the first note.', c(172, 'ex1', reveal=True)),
  ('B', 'You slip in bar five: a wrong note, and your hand freezes. What now?', c(172, 'ex2')),
  ('pause', 4, c(172, 'ex2')),
  ('P', 'Keep counting, and come back in on the next beat, or at the start of the next phrase. Never go back.', c(172, 'ex2', reveal=True)),
  ('B', 'Game: help or not? Going back. Breathe first. Keep the beat. Rush to finish.', c(172, 'gt2')),
  ('pause', 4, c(172, 'gt2')),
  ('P', 'Breathe first, and keep the beat. Going back and rushing don’t help.', c(172, 'gt2', reveal=True)),
  ('B', 'Try a one-minute concert today: choose eight bars, walk to the piano, sit, breathe, feel a bar, play, bow. Do it for someone.', c(172, 'gt2')),
  ('B', 'And remember, Clara: the audience wants you to do well. They are on your side from the first note. And so am I. Until next time, Clara.', c(172, 'think')),
  ('P', 'Thank you, Butler. For everything. Bye!', c(172, 'think'))])])
for _k in ('L1', 'L2', 'L3', 'L4', 'L5'): CH[_k] = NEW[_k]

NEW['MO'] = ('Opening map', [
 ('Part Six: Harmony in music', [
  ('B', 'Welcome to Part Six, Clara: harmony in music. Put the chords to work.', c(135, 'map')),
  ('B', 'A melody is the singer; harmony is the band behind it. Here the chords start moving: guests from outside the key, endings, chords under a tune, and the trips every song takes. All of it is in these same four bars of Twinkle.', c(135, 'map')),
  ('piano', '[C3 E3 G3 C4] C4 [C3 E3 G3 G4] G4 | [F2 A3 C4 A4] A4 [E2 G3 C4 G4] | [F2 Ab3 C4 F4] F4 [C3 G3 C4 E4] E4 | [G2 C4 D4] [G2 B3 F4 D4] [C3 E3 G3 C4]', c(135, 'map')),
  ('P', 'There’s a sad chord hiding in the middle!', c(135, 'map')),
  ('B', 'F minor, a guest note from the twin. Four chapters, and a page of tips. Shall we meet our first guest?', c(135, 'map')),
  ('P', 'Yes, please!', c(135, 'map'))])])

NEW['FO'] = ('Opening map', [
 ('Part Seven: Shape and style', [
  ('B', 'Welcome to Part Seven, Clara: shape and style. How music is built.', c(147, 'map')),
  ('B', 'Step back from the notes and see the building: small ideas, repeated and moved, in sections that come and go, in the style of their time. Like looking at a house from across the street instead of staring at one brick.', c(147, 'map')),
  ('P', 'So the letters on the map are like the rooms of a house?', c(147, 'map')),
  ('B', 'Exactly. Listen to a little tune built that way: the first idea, the same idea again, something new, and then the first idea once more to come home.', c(147, 'map')),
  ('piano', 'C4 E4 D4 F4 E4 D4 C4*2 | C4 E4 D4 F4 E4 D4 C4*2 | G4 G4 A4 A4 G4 F4 E4 D4*2 | C4 E4 D4 F4 E4 D4 C4*2', c(147, 'map')),
  ('B', 'Six chapters: motifs and phrases, repetition and sequence, texture, changing key, form, and styles through time. Shall we begin with the smallest idea of all?', c(147, 'map')),
  ('P', 'Let’s go!', c(147, 'map'))])])

NEW['LO'] = ('Opening map', [
 ('Part Eight: Playing and listening', [
  ('B', 'Welcome to Part Eight, Clara: the last part. At the piano.', c(162, 'map')),
  ('B', 'Everything before this page is knowledge. This part turns it into playing: the right fingers, practice that works, reading at sight, a trained ear, and the calm to perform.', c(162, 'map')),
  ('P', 'The last part already? I don’t want the book to end.', c(162, 'map')),
  ('B', 'A book ends, but the playing never does. Look at the two hands on the page: thumbs are one in both. Five chapters, and then you are ready for the concert hall.', c(162, 'map')),
  ('piano', 'C4 D4 E4 F4 G4 F4 E4 D4 C4*2', c(162, 'map')),
  ('P', 'Ready when you are, Butler!', c(162, 'map'))])])
for _k in ('MO', 'FO', 'LO'): CH[_k] = NEW[_k]

# her 11 Nov: Before you play (Handbook pp. 18-20): posture, hand shape, finger numbers, warm-ups
NEW['B1'] = ('Before you play', [
 ('The secret', [
  ('P', 'Butler! I want to play something right now. Can I just start?', c(18, 'h:Posture and hand shape')),
  ('B', 'In one minute, Clara. First we set up the most important instrument in the room.', c(18, 'h:Posture and hand shape')),
  ('P', 'The piano?', c(18, 'lead')),
  ('B', 'You. How you sit and how you hold your hands decide how easy everything else will be. Set them up before the first note, check them every time you sit down, and soon they look after themselves.', c(18, 'lead')),
  ('B', 'Here is the secret: sit tall, forearms level with the keys, a round hand on the fingertips. Then let the weight of your arm do the work.', c(18, 'secret'))]),
 ('How to sit', [
  ('B', 'Look at the picture. One: forearms level with the keys, like a table top. The wrist neither drops nor lifts.', c(18, 'hero', lab=['1'])),
  ('B', 'Two: elbows a little in front of you, not pinned to your sides like a penguin.', c(18, 'hero', lab=['2'])),
  ('P', 'Penguins can’t play the piano anyway.', c(18, 'hero', lab=['2'])),
  ('B', 'Quite right. Three: sit on the front half of the stool, opposite Middle C. Four: feet flat on the floor, the right foot near the pedal. Five: back tall, shoulders loose, leaning a little towards the keys.', c(18, 'hero', lab=['3'])),
  ('B', 'If the stool is too low, raise it, or sit on a cushion. A telephone book works too, if anyone still has one.', c(18, 'hero', lab=['5']))]),
 ('A round hand', [
  ('B', 'Now the hands. Imagine a soft ball resting under your palm. That shape is your playing hand: knuckles up like a bridge, fingers curved, and the sound comes from the fingertip, just behind the nail.', c(18, 'two')),
  ('B', 'The thumb plays on the side of its tip, relaxed. And the wrist stays level and loose. It never rests on the wood, however tired it is.', c(18, 'ht')),
  ('P', 'So I keep my nails short too?', c(18, 'ht')),
  ('B', 'Short nails, happy keys. A long nail clicks like a tap-dancing mouse.', c(18, 'ht'))]),
 ('Finger numbers', [
  ('B', 'Every finger has a number, the same in both hands. The thumb is one, then two, three, four, and the little finger is five. Music often prints these numbers above or below the notes.', c(19, 'two')),
  ('P', 'So my left thumb is one too, even though it’s on the other side?', c(19, 'two')),
  ('B', 'Exactly. Thumbs are always one. Now six warm-ups before you play. Watch them move.', c(19, 'h:Six warm-ups')),
  ('B', 'One, rag doll: flop forward, arms hanging heavy. Shake them loose, then float the hands up onto the keys.', c(19, 'wu6', anim='warm-ragdoll')),
  ('P', 'I’m a rag doll! Floppy, floppy.', c(19, 'wu6', anim='warm-ragdoll')),
  ('B', 'Two, elbow wings: elbows free, not stuck to your body. Float them out like wings, then back.', c(19, 'wu6', anim='warm-wings')),
  ('B', 'Three, arm glide: skate the whole arm along the keys. The round hand rides to the next group of keys. The fingers ride; they don’t walk.', c(19, 'wu6', anim='warm-glide')),
  ('B', 'Four, arm drop: lift the whole arm and let it drop into a key on finger three. Firm tip, soft wrist, a round sound.', c(19, 'wu6', anim='warm-dive')),
  ('B', 'Five, knuckle bridge: your knuckles are a bridge a little car can drive over. Press one key slowly and hold for three. The bridge stays up.', c(19, 'wu6', anim='warm-bridge')),
  ('P', 'Beep beep, the car made it across!', c(19, 'wu6', anim='warm-bridge')),
  ('B', 'And six, wrist balloon: as the key goes down, a balloon lifts the wrist back up to level. The fingertip stays on the key.', c(19, 'wu6', anim='warm-balloon'))]),
 ('Examples', [
  ('B', 'Example one. Which hand is round? Look at the knuckles: up, or sunk in? Look at the tips: does the finger stand on its tip?', c(19, 'ex1')),
  ('pause', 4, c(19, 'ex1')),
  ('P', 'A! It looks so relaxed.', c(19, 'ex1', oops=True)),
  ('B', 'Relaxed, yes, but A is lying down on the job. A flat hand can’t play fast or loud. Which one could play all day?', c(19, 'ex1')),
  ('P', 'C: knuckles up, curved fingers, standing on the tips. And B’s knuckle has caved in.', c(19, 'ex1', reveal=True)),
  ('B', 'Example two. Is the stool right? Follow the forearm from the elbow to the keys. Uphill or downhill?', c(20, 'ex2')),
  ('pause', 4, c(20, 'ex2')),
  ('P', 'B is level. In A the arm goes uphill, so the stool is too low. In C it goes downhill: too high.', c(20, 'ex2', reveal=True)),
  ('B', 'Now the thirty-second check, from the stool to your fingertips. Do it every time you sit down. Do it with me now.', c(20, 'howto')),
  ('B', 'One, the stool. Sit opposite Middle C. Are your forearms level with the keys, like a table top?', c(18, 'hero', lab=['1', '3'])),
  ('pause', 3, c(18, 'hero', lab=['1', '3'])),
  ('B', 'Two, the body. Front half of the stool, both feet flat, back tall.', c(18, 'hero', lab=['3', '4', '5'])),
  ('pause', 3, c(18, 'hero', lab=['3', '4', '5'])),
  ('B', 'Three, the shoulders. Lift them up to your ears. And let them drop.', c(18, 'hero', lab=['5'])),
  ('pause', 3, c(18, 'hero', lab=['5'])),
  ('B', 'Four, the hands. A soft ball under each palm, knuckles up, standing on the fingertips. Wrists level, not resting on the wood.', c(18, 'two')),
  ('pause', 3, c(18, 'two')),
  ('B', 'And five: breathe out. Now you are ready to play.', c(20, 'howto')),
  ('P', 'Stool, body, shoulders, hands, breathe. Done in thirty seconds!', c(20, 'howto')),
  ('B', 'Try it: hold a small ball or an orange, then put your hand on the keys without changing its shape.', c(20, 'try10')),
  ('P', 'Can I eat the orange afterwards?', c(20, 'try10')),
  ('B', 'After the scales. Four traps: wrists sinking below the keys, shoulders creeping up to your ears, flat fingers or a caved-in knuckle, and sitting so close your elbows are squashed. Now, Clara, you may start.', c(20, 'watch')),
  ('P', 'Finally! Bye, Butler!', c(20, 'watch'))])])
CH['B1'] = NEW['B1']

NEW['G1'] = ('Notes outside the chord', [
 ('The secret', [
  ('P', 'Butler, in my piece the left hand plays a C chord, but the tune plays a D. Is that a wrong note?', c(175, 'lead')),
  ('B', 'Not wrong at all, Clara. Under a tune, the chord holds the main notes. The other notes are notes outside the chord: they lean on the chord for a moment, then step back into it.', c(175, 'lead')),
  ('B', 'Here is the secret: a note outside the chord moves by step. Into the chord, out of it, or both.', c(175, 'secret')),
  ('P', 'So they never jump?', c(175, 'secret')),
  ('B', 'Almost never. Think of stepping stones in a stream. The chord is the bank. You step onto a stone for a moment, then land on the bank again.', c(175, 'secret'))]),
 ('Five ways out and back', [
  ('B', 'One, the passing note. E, D, C, over a C chord. The D steps between two chord notes.', c(175, 'hero')),
  ('piano', 'E5 D5 C5*2', c(175, 'hero')),
  ('B', 'Two, the auxiliary note. C, D, C. The D steps out and comes straight back.', c(175, 'hero')),
  ('piano', 'C5 D5 C5*2', c(175, 'hero')),
  ('P', 'Like popping next door and coming straight home.', c(175, 'hero')),
  ('B', 'Three, the appoggiatura. The D lands right on the beat and leans, then sighs down to C. Its name comes from the Italian for “to lean”.', c(175, 'hero')),
  ('piano', 'D5*2 C5*2', c(175, 'hero')),
  ('B', 'Four, the suspension. Over an F chord the tune plays F. Then the chord changes to C, but the F is held over, and only then falls to E.', c(175, 'hero')),
  ('piano', 'A4 F5*2 E5', c(175, 'hero')),
  ('P', 'The F is late for the next chord.', c(175, 'hero')),
  ('B', 'Late, and then it catches up. And five, the anticipation: the opposite. Over a G chord, the C arrives early, before its own chord.', c(175, 'hero')),
  ('piano', 'B4 D5/2 C5/2 C5*2', c(175, 'hero')),
  ('P', 'Late and early. Like me and my brother in the morning.', c(175, 'hero'))]),
 ('Example: which notes are outside the chord?', [
  ('B', 'Example. The chord is C: C, E and G. The tune: G, A, B, C, then E, D, C. Which notes are not C, E or G? Pause and try.', c(176, 'ex1')),
  ('pause', 4, c(176, 'ex1')),
  ('P', 'A and B! And the D in the second bar.', c(176, 'ex1', reveal=True)),
  ('B', 'All three are passing notes. A and B climb from G up to C, and D walks from E down to C.', c(176, 'ex1', reveal=True)),
  ('piano', 'G4 A4 B4 C5 | E5 D5 C5*2', c(176, 'ex1', reveal=True))]),
 ('Game and Ode to Joy', [
  ('B', 'Game: name each red note. Passing, auxiliary, appoggiatura or suspension? Pause and try.', c(176, 'game')),
  ('pause', 5, c(176, 'game')),
  ('P', 'Passing, auxiliary, appoggiatura, suspension!', c(176, 'game', reveal=True)),
  ('B', 'And you know this one. Ode to Joy: E, E, F, G, over a C chord. The F slips between E and G: a passing note.', c(176, 'yk')),
  ('piano', 'E4 E4 F4 G4 | G4 F4 E4 D4', c(176, 'yk')),
  ('B', 'Two traps. A note outside the chord is not a mistake: it is the tune’s colour. And choose the chord for a bar by its main notes, not its passing notes. Until next time, Clara.', c(176, 'watch')),
  ('P', 'Bye, Butler!', c(176, 'watch'))])])
CH['G1'] = NEW['G1']
