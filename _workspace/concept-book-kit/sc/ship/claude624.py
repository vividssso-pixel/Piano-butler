import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 610 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 611 | 2026-10-21 | **Scale finder: pastel groups, and the staff finger numbers follow the group colours.** Her decisions (2026-10-21): she prefers the lighter pastel coral/blue to the stronger version, and the finger numbers above the staff must take the same group colours. The finder keyboards are back to the pale lesson fills (coral `#fad0c2`, blue `#cddcf7`) with the finger numbers in the group colour (coral `#c0431f` for 1-2-3, blue `#3b4fa8` for 1-2-3-4, navy for the rest); the finger numbers and thumb rings above the staff use the same colours (new staff option `fingerCols`). Built by `patch621.py` (`t624`). Checked C major and F-sharp minor with the staff shown: no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
