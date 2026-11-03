"""Notes: her call on the sample lesson's frame (4 Nov 01:26-01:29). Run from the repo root:
python3 _workspace/songbook/ship/claude_songbook3.py CLAUDE.md CLAUDE-history.md"""
import sys, io, re
md, hist = sys.argv[1], sys.argv[2]
s = io.open(md, encoding='utf-8').read()
old = "waiting for her call on the format, the four ways and the level fit."
new = ("her call 4 Nov 01:29: the frame stays for every Level 0 song (listen and sing, say and clap, read it, four ways, move it, "
       "check). Keys: experience first, the rule later -- at Level 0 'Move it' goes only where the tune stays on white keys "
       "(checked per song by computing; Mary: G and F), and the five-finger rule (tone, tone, semitone, tone) comes at the end "
       "of Level 0 or in Level ½, naming what the hand already did; D, A and E (a black key) wait for it.")
assert s.count(old) == 1, 'item 1 changed; read it again'
s = s.replace(old, new); io.open(md, 'w', encoding='utf-8').write(s)
h = io.open(hist, encoding='utf-8').read().split('\n')
rows = [i for i, l in enumerate(h) if re.match(r'^\| \d+ \|', l)]
n = max(int(h[i].split('|')[1]) for i in rows) + 1
h.insert(rows[-1] + 1, f"| {n} | 2026-11-04 | **The song Lesson Book: her call on the frame (chat window, her 01:26 to 01:29).** She asked whether five-finger scales should come first so a tune can move to every white key; my answer: one rule (tone, tone, semitone, tone) beats twelve positions, taught inside the song lessons. Her 01:27: it may be too hard at the very start, leave it out for now; agreed (experience first, the rule later, as sound before symbol). Her 01:29 'yes': the frame stays for every Level 0 song; Move it goes only where the tune stays on white keys (computed per song), the rule at the end of Level 0 or in Level ½. Next: the Level 0 song list. |")
io.open(hist, 'w', encoding='utf-8').write('\n'.join(h)); print('row', n)
