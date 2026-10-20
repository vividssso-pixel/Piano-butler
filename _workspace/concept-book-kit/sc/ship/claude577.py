import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 571 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 572 | 2026-10-20 | **Scales lesson 3: the degrees of the scale (`sc-deg`, `ScDeg`).** Whole picture: C major with its numbers 1̂ to 8̂; one by one: each degree with its name and her one-line reason (tonic: home, the key's own note … leading note: a semitone below the tonic, it leads home), with the tonic and the note sounding together; her turn: pick C, G, F or D, then find all seven degrees in random order, asked by name or by number alternately (wrong key: \"Not that key\"). All names and reasons are her `DEGREE_NAMES` / `DEGREE_WHY` (English and Korean) texts, unchanged. Home `p-scale` lists lessons 1-3. The Korean prompt wording (\"... 건반을 눌러요\") is mine, unverified. Built by `patch577.py` (`t577`). Checked in English and Korean: a full round solved by reading the prompt, no errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
