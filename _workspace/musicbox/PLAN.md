# The Piano Butler's Music Box: the plan (decided 26 Nov 2026)

Read this before touching any Music Box file. Everything here was decided by Sohyun on 26 Nov 2026
(her words in CLAUDE-history.md rows 1138 onward). Nothing is public; never push.

## The goal
A ladder from a complete beginner to (a) playing real classical pieces from normal notation and
(b) making a pretty accompaniment for any melody, the way the "Twinkle, ten ways" page does.
"Too simple" accompaniment is not the destination.

## Decisions
1. Six books: The Piano Butler's Music Box 1 to 6. Books 1-3 = "I can play it"; 4-6 = "I can make it beautiful".
2. Left-hand patterns are named and carried from the very first book. Names (hers):
   Roots · Block chord (all keys of the chord at once) · Waltz style (bottom key, then the top two) ·
   Broken chord (one key at a time, bottom-middle-top) · Zigzag (bottom and top rocking) ·
   Alberti bass · then Seventh chords, wide arpeggio with pedal, Minor colours, inversions and Walking bass,
   right-hand fills, Secondary dominants, Borrowed chords. Jazz ballad is at most an appendix.
3. Pace: not radical, plenty of time. A new pattern is the main pattern for THREE songs in a row
   (easy / chords change more often / new key or metre). While a pattern is new, reading does not step up;
   when reading steps up, the left hand is a pattern already known.
4. Every song page: the song's pattern is named; "Same tune, another left hand" shows one bar of this song
   in an older pattern and one bar of an older song in today's pattern (already built in Music Box 2).
5. Twinkle returns at the end of every UNIT as variations in the patterns learnt so far. Book 6 can end
   with an easy variation from Mozart's K. 265.
6. Growing songs: about six pieces come back across the books in a richer left hand each time, ending
   close to the original. The rule "never reuse a song" is lifted for these (and Twinkle) only.
   Candidates: Twinkle · Ode to Joy · Pachelbel's Canon · Für Elise · Minuet in G (graduates in Book 3) ·
   Brahms' Lullaby or Silent Night. When one returns, the left page shows one bar "last time" and one "this time".
7. Repertoire is mostly classical. Each pattern's third song should be a real piece that uses that pattern
   as written (Alberti: Mozart K. 545 or a Clementi sonatina; Waltz style: a Brahms or Chopin waltz,
   Satie's Gymnopédie; Broken chord: Bach Prelude in C, Moonlight first movement; Zigzag: Mountain King,
   Burgmüller). Folk songs and carols only where a pattern is first met. Each book: 4-5 growing songs
   in new clothes + 6-8 new songs.
8. Certain songs only: every melody is checked note by note against an open score before it goes in
   (Mutopia, Nottingham Music Database, Essen; see verify2.py, verify3.py, conv.py). If it cannot be checked,
   it is left out. The piece names above are candidates, not yet checked, except those already in the books.
9. Notation: letters in boxes -> faint shadow notes -> letters in note heads -> staff with letters ->
   letters fade (beat-box lines fade with them) -> plain notes -> bass staff -> lead sheet.
   Wherever there is a staff: key signature on every line, time signature on the first, final double barline,
   naturals where needed. Every line runs to the right edge. Clean pages.
10. A dotted note shows its one and a half boxes: the next box is split by a dashed line, hold in the first half,
    the short note in the second; tails never leave their box.

## The six books
| Book | Left hand | Reading | At the end you can play |
|---|---|---|---|
| 1 | Roots -> Block chord | letters -> shadow notes | a famous theme, one line, three chords |
| 2 | Waltz style -> Broken chord | letters in note heads -> staff | Minuet in G, the first section of Für Elise |
| 3 | Zigzag -> Alberti bass -> choosing a pattern | plain notes, bass staff, lead sheet | the opening of Mozart K. 545, Bach's Prelude in C |
| 4 | Seventh chords -> wide arpeggio and pedal -> Minor colours | normal notation | Gymnopédie, Moonlight opening, an easy Chopin prelude |
| 5 | inversions and Walking bass -> right-hand fills -> Secondary dominants | normal notation | Bach's Air, a Schubert song |
| 6 | Borrowed chords -> arranging on your own | lead sheets | a new melody, arranged by you |

## Where things stand
- Music Box 1: 27-page draft, old plan (18 songs + Twinkle). Two songs she will name still to fix. Not yet re-paced.
- Music Box 2: 38-page draft (13 songs + Twinkle), patterns named, examples built. Still on the old pacing:
  Waltz style and Zigzag get one song each. Mountain King (Zigzag) and Canon (ground bass) move to Book 3.
- Music Box 3: 27-page draft (8 folk songs + Twinkle) on the old plan; to be rebuilt with classical pieces.
- Books 4-6: not started.
- Not done anywhere: pattern card page, Twinkle variations at unit ends, shelf (index) entries for Books 2-3,
  listening page and recordings (so no QR in Books 2-3), finger numbers and a brace in Book 3.

## Next steps, in order
1. A full song list for all six books as candidates, for her to choose from, before any score is checked.
2. Re-pace Book 1, then Book 2, then rebuild Book 3; then Books 4-6.

## Files
lesson.py (renderer; GRID2 is Music Box 2+), mbox.py (Book 1 data), mbox2.py + mbfront2.py (Book 2),
conv.py + mbox3.py + mbfront3.py (Book 3), verify2.py / verify3.py (+ reports), layout.js, align.js, build.sh.
Build: `bash build.sh mcN` (Book 2), `mdN` (Book 3); every page must give overflow 0, clash 0, alignment 0, layout 0.
