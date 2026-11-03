"""Notes: the Level 0 song list, her 4 Nov 01:31-01:34 (mix, famous, public domain, sorted by position and difficulty)."""
import sys, io, re
md, hist = sys.argv[1], sys.argv[2]
s = io.open(md, encoding='utf-8').read()
old = "D, A and E (a black key) wait for it."
new = old + (" Level 0 song list, draft (her 01:31-01:34: mix classical and folk, famous and public domain, sorted by position "
  "then difficulty; melodies checked against public scores when set): 1 Rain, Rain, Go Away; 2 Hot Cross Buns; 3 Au clair de la "
  "lune; 4 Mary had a little lamb; 5 Dvorak, Going Home (New World, Largo); 6 Beethoven, Ode to Joy; 7 Strauss, The Blue Danube; "
  "8 When the Saints; 9 Jingle Bells; 10 London Bridge (left hand, D to A); 11 Beethoven, Symphony No. 5; 12 Grieg, In the Hall of "
  "the Mountain King; 13 Haydn, Surprise Symphony; 14 Pachelbel, Canon (left-hand bass, a duet); 15 Twinkle and Mozart's variations. "
  "The classical themes get short English words of our own (the frame sings and claps words). Level ½: Grieg's Morning, "
  "Brahms's Lullaby, Lightly Row.")
assert s.count(old) == 1; s = s.replace(old, new); io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The Level 0 song list, draft (chat window, her 01:31 to 01:34).** A folk list, then a classical one (public domain, famous, what a child should know), then her 'sort by position and difficulty' and 'mix them: famous and out of copyright'. Fifteen songs by position (black keys; right hand C position with 3-4 notes, then all five; left hand; new positions, a black key, minor; the hand leaving its position), one new difficulty a lesson, classical and folk taking turns; the list is in CLAUDE.md Next item 1. Move it only in lessons 3 to 10. Classical themes need words of our own. Next: the words, then the order checked against drills' Level 0 rooms. |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
