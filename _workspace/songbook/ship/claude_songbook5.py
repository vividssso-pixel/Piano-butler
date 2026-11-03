"""Notes: the Level 0 list matched to drills' rooms; the sample becomes Lesson 5 with a QR and Play together (her 4 Nov 02:12-07:58)."""
import sys, io, re
md, hist = sys.argv[1], sys.argv[2]
s = io.open(md, encoding='utf-8').read()
old = "The sample is made (4 Nov, chat window): Lesson 6, Mary had a little lamb, 4 A4 pages, in `_workspace/songbook/`"
new = "The sample is made (4 Nov, chat window): Lesson 5, Mary had a little lamb, 4 A4 pages, in `_workspace/songbook/`"
assert s.count(old) == 1; s = s.replace(old, new)
old2 = "15 Twinkle and Mozart's variations."
new2 = ("15 Twinkle and Mozart's variations. Matched to drills' 13 Level 0 rooms in their order (her 02:12 'next'): 1 Rain, Rain (posture-hands, "
  "first-steps); 2 Hot Cross Buns (pulse, note-names); 3 Au clair (hand-positions); 4 Going Home (ear-prep); 5 Mary (note-values); "
  "6 Ode to Joy (staff, reading-steps); 7 Jingle Bells (reading-steps); 8 London Bridge, left hand (whole-staff); 9 Haydn, first phrase "
  "in C position and the bang (dynamics); 10 Blue Danube (time-signatures); 11 When the Saints (time-signatures); 12 Beethoven 5 (tones, "
  "D to E flat); 13 Mountain King (tones); 14 Pachelbel; 15 Twinkle and Mozart (review). Each lesson's QR opens its room: "
  "`drills.html?room=<id>`, a small drills build still to do (her 07:58 'ok'); a printed QR cannot carry a child's own link, so the "
  "practice log counts only on a device that already holds it.")
assert s.count(old2) == 1; s = s.replace(old2, new2)
io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: what makes it different, and the next steps (chat window, her 02:00 to 07:58).** Her 'will it stand out?': my answer, not each part (famous public-domain songs, words on classical themes, five-finger moves and accompaniment ladders are in other books) but the set: the book tied to drills (a QR per lesson to its room, the practice the teacher sees) and the same song played by different Ways together. Next steps agreed: the list matched to drills' rooms (in CLAUDE.md Next item 1), the sample made Lesson 5 (note-values) with a real QR to `drills.html?room=note-values` and a Play together strip (one player Way 1, the other Way 4's left hand). Fixed in passing: the 01:17 build had lost the counts under the rhythm lines and the letter boxes (a code line cut by my own edit); check.js now fails if either is missing. The Lesson 6 PDF moved to _workspace/_to_delete/songbook. Next: the `?room=` link in drills, then the song data, melodies checked against public scores. |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
