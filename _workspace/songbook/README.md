# Song Lesson Book (Level 0) -- the sample lesson

Her 4 Nov 01:00: books first, a song-led set (song Lesson Book + Level Workbook + Handbook), Level 0 first, for children
starting from nothing. This folder makes one sample lesson for her to judge: `lesson-06-mary-had-a-little-lamb.pdf`
(the lesson number is a placeholder until the Level 0 song list is set).

One lesson, one song, five parts:

1. Listen and sing -- the tune with the words (sound before symbol); a QR box for the recording (placeholder).
2. Say and clap -- the words on a one-line rhythm staff, counts under them: coral where a note starts, grey dashes while it is held.
3. Read it -- C position on the keys (the song's notes lit, finger numbers), the letter names of bars 1-4 in boxes, step or skip.
4. Play it four ways -- the same tune with more for the left hand each way (stars 1-4):
   Way 1 the tune (RH fingers); Way 2 one long note below (C or G); Way 3 with chords (C-G / D-G on beats 1 and 3);
   Way 4 a moving bass (5 1 3 1 / 4 1 2 1).
5. Check -- I can..., the four ways, the teacher's Pass / Not yet, and lines for the teacher's note.

Facts on the page, checked (Wikipedia, "Mary Had a Little Lamb", 4 Nov 2026): a rhyme by Sarah Josepha Hale, first printed in 1830
by Marsh, Capen & Lyon, Boston; sung today to the tune of "Merrily We Roll Along" (not Lowell Mason's 1830s setting).

## Build

    npm install                     # verovio + the three @fontsource faces (Atkinson Hyperlegible, Playfair, Noto Music)
    node engrave.mjs mary.json mary-svg.json          # Verovio: one SVG per 4-bar line and job (words, rhythm + counts, boxes, ways)
    node crop.js mary-svg.json mary-crop.json         # crop each line to its music, full width kept (Playwright)
    python3 lesson.py mary.json mary-crop.json lesson-mary.html
    node pdf.js "$PWD/lesson-mary.html" "$PWD/lesson-mary.pdf"   # prints each page's overflow; all 0 to pass
    node check.js "$PWD/lesson-mary.html"            # every label's ink clear of noteheads, stems and other labels; boxes clear of notes

A song is one JSON file (`mary.json`): bars of [pitch, duration c/m/s, syllable, word position], the chords per bar,
right-hand fingers per pitch, and the left-hand patterns for Ways 2-4. Look: the Handbook's (book-v3/book10.py) --
A4, navy #26296b and coral #e4572e on white, Atkinson Hyperlegible text, Playfair heads.
