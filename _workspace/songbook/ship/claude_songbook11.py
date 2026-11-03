"""Notes: how the left-hand chords grow through Level 0 (her 4 Nov 10:22-10:23)."""
import sys, io, re
md, hist = sys.argv[1], sys.argv[2]
s = io.open(md, encoding='utf-8').read()
old = "The classical themes get short English words of our own (the frame sings and claps words)."
new = old + (" Chords (her 10:22-10:23): one note added a stage, each stage held for 2 to 3 songs, the ways varied by rhythm "
  "(hold, beats 1 and 3, every beat), and the explanation grows one line a stage: lessons 1-4 no left-hand chord; 5-7 the root "
  "only ('a chord is named after its root'); 8 London Bridge, the left hand plays the tune; 9-11 two notes, the two ends of the "
  "hand (5 and 1); 12-15 three notes ('play, skip, play, skip, play', a page with a keyboard picture before lesson 12; stacked "
  "heads touching from here). The ranges may move once each song's chords are checked (an F chord, say).")
assert s.count(old) == 1; s = s.replace(old, new); io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: how the chords grow (chat window, her 10:22 'introduce only the root, then add one in the next songs?', 10:23 'good, and the explanations can come one at a time too').** My advice taken: one note added a stage, each stage held for 2 to 3 songs (the ways vary by rhythm, so a held stage still gives something new), one line of explanation a stage. Lessons 1-4 none; 5-7 the root; 8 the left hand plays the tune; 9-11 two notes, the ends of the hand; 12-15 three notes, with a one-page 'play, skip, play, skip, play' before lesson 12. In CLAUDE.md Next item 1. Also 10:20: letter boxes under bars 5-8 too (0ae2f8a). |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
