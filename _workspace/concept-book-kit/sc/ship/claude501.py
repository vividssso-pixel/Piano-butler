import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 500 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 501 | 2026-10-19 | **Key finder: a way back (her 09:25: 'no button back to Read it').** Steps 2 to 5 get a '← Back' beside Next (the last step too), and the three pills Read it / Name the key / Play its scale are now buttons that jump to step 1 / 3 / 5. Source `patch501.py`; checked by me in EN and KO (Next, Back, pill, last-step Back), no console errors. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
