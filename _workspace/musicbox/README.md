# The Butler's Music Box (working files)

Her 10 Nov 2026 direction: the first songbook as letters in beat boxes, both hands, one song a page.

Rows, top to bottom:
- right-hand finger numbers
- right-hand letters
- the count (1 2 3 4; "1 &" in a split box)
- the words
- left-hand chord, boxed

Grid tokens:
- `-` holds the note.
- `C.C` splits a box into two quavers.
- `r` is a rest: an empty box with a dot.

## Files

- `mbox.py` writes `mb1.json` to `mb9.json`. Song 2 is `let1.json`.
- `bash build.sh mbN` builds `lesson-mbN.html` and `lesson-mbN.pdf`. Then run `node align.js` and `node layout.js`; both should report 0.
- `python3 mbaudio.py ../../listen.html ../../musicbox.html` builds the Music Box listening page from the Lesson Book's `listen.html`.
  - It uses the book's own tunes and chords. The Lesson Book's `listen.html` is not changed.
  - "Piano" plays the student's left hand, one key a bar.
  - Band and Ensemble reuse the old styles over the new chords.
- `lesson.py` (the v4 `gig` mode with `grid` + `simple`), `engrave.mjs` (fixStems for ellipse heads and chords with dots, fixDots) and `crop.js`: the pipeline as of 10 Nov.

The QR codes point to `thepianobutler.com/musicbox.html#<id>`.

Tunes and chord placings are traditional and written from memory. Sohyun checks them by ear, especially:
- When the Saints, bars 9–16
- Au Clair, bar 2
