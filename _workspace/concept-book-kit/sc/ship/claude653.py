import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 631 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 632 | 2026-10-22 | **Keys and staff section 5 fixes (her 14:43-14:44 feedback).** (1) The Octaves lesson overlapped 'Every key has its place' (same C, 12 keys), so it is removed from Pitch and range; the word 'octave' now closes section 1's last step. (2) 'Long and short' try question was unclear: bars now show a note symbol, tapping a bar only plays it, and the answer is chosen with 'The left bar / The right bar' after hearing both. (3) The range lesson now plays each instrument with its own sound (bowed strings, flute, reed, brass, voice, piano for keyboards) from a plain WebAudio synth; **she should listen and say whether the timbres are close enough** (I cannot hear them). The kq-octave code stays unused until the old-code cleanup. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
