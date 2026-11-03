# Song Lesson Book (Level 0) -- the sample lesson

Her 4 Nov 01:00: books first, a song-led set (song Lesson Book + Level Workbook + Handbook), Level 0 first, for children
starting from nothing. This folder makes one sample lesson for her to judge: `lesson-05-mary-had-a-little-lamb.pdf`
(Lesson 5 in the Level 0 list of 4 Nov; it goes with the drills room 'note-values').

One lesson, one song, three A4 pages (her 4 Nov 10:08 and 10:16):

1. Say and clap -- what the song is made of first: the time (4/4: four beats in a bar, a crotchet a beat) and the note
   values it uses (crotchet 1, minim 2, semibreve 4, with beat dots); then the words on a one-line rhythm staff with
   the counts (coral where a note starts, grey while it is held).
2. Listen and sing -- the tune with the words, the letter-name boxes of bars 1-4 under the words; C position on the
   keys (the song's notes lit); steps and the one skip (E up to G: in which bar?); a QR to the lesson's drills room
   (`drills.html?room=<id>`; drills still needs that link).
3. Play it four ways -- root only at this stage (her 10:16): Way 1 the tune; Way 2 hold the root (C with 5, G with 1,
   in C position); Way 3 the root on beats 1 and 3; Way 4 the root on every beat. A legend, a small left-hand keyboard,
   then ONE score: the tune with right-hand fingers and chord letters, a numbered row under it for each of Ways 2-4
   with only finger numbers and hold lines. Play together.
4. Check.

Move it (transposing) is left out for now (her 10:16: later, it looked too much); the code still has the G line (g1, g2).
The tune is printed three times (clap, sing, play).

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
