import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: a teacher duet in the lesson (chat window, her 10:29 'can we make an accompaniment to play together?', 10:30 'put it in small; the audio too').** The sample's page 3 now has, under Play together, a small Teacher part made from the song's data (mary.json `duet`): two treble staves the teacher plays an octave higher, the right hand a music-box pattern on the chord's notes a beat each (C E G E; B D G D), the left hand two notes a half bar, one chord in each hand at the end; it sits above the child's hands, so any Way fits under it. The legend of the four ways moved to page 2 to make room. Next: the audio, a play-along with count-in at three speeds, for the QR. |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
