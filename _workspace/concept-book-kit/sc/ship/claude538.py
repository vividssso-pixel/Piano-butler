import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 535 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 536 | 2026-10-19 | **The 'Which notes change?' question says what it asks (her 14:18 note).** More practice chip is now 'Which notes?' (KO 어떤 음?); the question reads 'Which notes get a sharp in this key?' or 'Which notes get a flat in this key?' (KO 이 조에서 샵(♯)/플랫(♭)이 붙는 음은?) instead of 'Which notes does this key signature change?'. Source `patch538.py`; checked by me, EN and KO, no console errors. Open: the extras (Which notes?, Coral note, Accidentals, Written right) are the book's old drills and may read the same way; I will check each with her. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
