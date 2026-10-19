import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 516 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 517 | 2026-10-19 | **Find the major key by tapping, and the drill as its own button (her 12:02 notes).** In the Major key lessons the 'What key has N sharps (flats)?' screen no longer uses the F♯ / C♯ chips: she taps on the staff or on the keyboard. Sharps: first the last ♯ (it gets a ring and lights its key), then the major key a half step up; flats: the second-to-last ♭, which is the key. Wrong taps flash (outlined key or a faint sign on the staff); on success the staff shows the key note with the half-step arrow. On the concept page the drill is no longer a numbered row: a full-width navy 'Start the drill' button sits under the lessons (Key signatures and Scales). Source `patch517.py`; checked by me, EN and KO, no console errors. Note: staff taps need the exact step (about 6 px at phone width); the keyboard always works. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
