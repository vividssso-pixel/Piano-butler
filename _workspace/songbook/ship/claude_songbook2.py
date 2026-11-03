"""Notes: the sample lesson gains 'Move it to G' (her 4 Nov 01:17). Run from the repo root:
python3 _workspace/songbook/ship/claude_songbook2.py CLAUDE-history.md"""
import sys, io, re
hist = sys.argv[1]
h = io.open(hist, encoding='utf-8').read()
mine = [l for l in h.split('\n') if l.startswith('| ') and 'The song Lesson Book: the sample lesson (chat window' in l]
assert len(mine) == 1, len(mine)
old = "Waiting for her call. |"
assert mine[0].endswith(old)
new = ("Then her 01:17 ('learn the whole key with it, turning the keys; several ideas from one song'): 5 Move it to G, same "
       "fingers and a new home (the G keyboard with the key's one black key, F sharp; bars 1 to 4 in G with one sharp and the "
       "same finger numbers, new notes to read; the chords moved, C to G and G to D), and the Check's four ways in C and in G; "
       "the teacher's note lines out to make room. The tune uses only C D E G, so in G it never meets F sharp and in F never B "
       "flat. Her 01:19: rhythm, pitch, key and chords together as the groundwork of sight-reading. Waiting for her call. |")
h = h.replace(mine[0], mine[0][:-len(old)] + new)
io.open(hist, 'w', encoding='utf-8').write(h)
print('history row updated')
