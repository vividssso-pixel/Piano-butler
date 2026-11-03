# Song Lesson Book (Level 0) -- the sample lesson

Her 4 Nov 01:00: books first, a song-led set (song Lesson Book + Level Workbook + Handbook), Level 0 first, for children
starting from nothing. This folder makes one sample lesson for her to judge: `lesson-05-mary-had-a-little-lamb.pdf`
(Lesson 5 in the Level 0 list of 4 Nov; it goes with the drills room 'note-values').

One lesson, one song, six parts:

1. Listen and sing -- the tune with the words (sound before symbol); a QR to the lesson's drills room
   (`drills.html?room=<id>`; drills still needs that link).
2. Say and clap -- the words on a one-line rhythm staff, counts under them: coral where a note starts, grey dashes while it is held.
3. Read it -- C position on the keys (the song's notes lit, finger numbers), the letter names of bars 1-4 in boxes, step or skip.
4. Play it four ways -- the same tune with more for the left hand each way (stars 1-4). Ways 2-4 are lead sheets (her
   4 Nov 09:21): the tune with the chord letters, and under each bar only when the left hand plays (a held note's finger
   and a line, dots for two notes together, a finger a beat), beside two small left-hand keyboards for C and G. The bass
   clef waits for its own room (lesson 8).
   Root first (her 09:25): Way 2 just the root (finger 5, the hand moves down for G), Way 3 root and fifth (5 1), Way 4
   the whole chord in root position (5 3 1: C E G, G B D). In the first line the dots are pictures of the chord: its notes
   stacked a third a head apart, so root-position heads touch, and a dashed ring where the third is still to come.
   In G only Ways 1-3 (the D chord's third is F sharp).
   The ways (before 09:25):
   Way 1 the tune (RH fingers); Way 2 one long note below (C or G); Way 3 with chords (C-G / D-G on beats 1 and 3);
   Way 4 a moving bass (5 1 3 1 / 4 1 2 1). Play together: one player Way 1, the other Way 4's left hand.
5. Move it to G (her 4 Nov 01:17: learn the whole key, turn the keys) -- same fingers, new home: the G keyboard (G position,
   the key's one black key F sharp), bars 1-4 in G with one sharp and the same finger numbers (new notes to read), the chords
   moved (C to G, G to D). This tune uses only C D E G, so in G it never meets F sharp and in F never B flat: a first song for
   turning the keys.
6. Check -- I can..., the four ways in C and in G, the teacher's Pass / Not yet.

Facts on the page, checked (Wikipedia, "Mary Had a Little Lamb", 4 Nov 2026): a rhyme by Sarah Josepha Hale, first printed in 1830
by Marsh, Capen & Lyon, Boston; sung today to the tune of "Merrily We Roll Along" (not Lowell Mason's 1830s setting).

## Build

    pip install qrcode; npm install  # verovio + the three @fontsource faces (Atkinson Hyperlegible, Playfair, Noto Music)
    node engrave.mjs mary.json mary-svg.json          # Verovio: one SVG per 4-bar line and job (words, rhythm + counts, boxes, ways)
    node crop.js mary-svg.json mary-crop.json         # crop each line to its music, full width kept (Playwright)
    python3 lesson.py mary.json mary-crop.json lesson-mary.html
    node pdf.js "$PWD/lesson-mary.html" "$PWD/lesson-mary.pdf"   # prints each page's overflow; all 0 to pass
    node check.js "$PWD/lesson-mary.html"            # every label's ink clear of noteheads, stems and other labels; boxes clear of notes;
                                                     # the counts and the answer boxes must be there

A song is one JSON file (`mary.json`): bars of [pitch, duration c/m/s, syllable, word position], the chords per bar,
right-hand fingers per pitch, and the left-hand patterns for Ways 2-4. Look: the Handbook's (book-v3/book10.py) --
A4, navy #26296b and coral #e4572e on white, Atkinson Hyperlegible text, Playfair heads.
