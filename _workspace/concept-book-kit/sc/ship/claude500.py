import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 499 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 500 | 2026-10-19 | **The staff moves with the zigzag; 'Free play' renamed (her 09:22).** While 'Say the order' runs, each sharp on the staff is numbered 1 to 7 to match the dots on the keyboard, and the newest one is the stronger colour. 'Free play' / '자유롭게' is now 'Explore' / '더 둘러보기' in the Key finder and Scale finder (and the Toolbox blurbs that named it). Source `patch500.py`; checked by me with a mid-run screenshot, no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
