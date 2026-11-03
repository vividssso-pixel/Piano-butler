# Song Lesson Book (Level 0) -- the sample lesson

Her 4 Nov 01:00: books first, a song-led set (song Lesson Book + Level Workbook + Handbook), Level 0 first, for children
starting from nothing. This folder makes one sample lesson for her to judge: `lesson-05-mary-had-a-little-lamb.pdf`
(Lesson 5 in the Level 0 list of 4 Nov; it goes with the drills room 'note-values').

One lesson, one song, three A4 pages (her 4 Nov 10:08: say and clap first, with the position; then listen and sing with the
letter boxes under it; then the chords in order; and fewer printings of the same tune):

1. Say and clap -- the words on a one-line rhythm staff, counts under them (coral where a note starts, grey dashes
   while it is held); the C position keyboard with the song's notes lit.
2. Listen and sing -- the tune with the words, the letter-name boxes of bars 1-4 under the words; a QR to the
   lesson's drills room (`drills.html?room=<id>`; drills still needs that link).
3. Play it four ways -- a legend (Way 1 the tune with right-hand fingers; Way 2 just the root, finger 5; Way 3 root and
   fifth, 5 1; Way 4 the whole chord, 5 3 1: C E G, G B D) beside the left-hand keyboards for C and G, then ONE score:
   the tune with fingers and chord letters, and under it a numbered row for each of Ways 2-4 showing only when the left
   hand plays. In the first line the dots are pictures of the chord (a third a head apart, so root-position heads
   touch; a dashed ring for the note still to come). Play together: one player Way 1, the other a left-hand row.
4. Move it to G -- same fingers, new home; the G keyboard (its one black key, F sharp); bars 1-4 in G with one sharp.
5. Check -- I can..., the ways in C (1-4) and in G (1-3: the D chord's third is F sharp), the teacher's Pass / Not yet.

The tune is printed three times (clap, sing, play) and once more in G, where it used to be printed eight times.

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
