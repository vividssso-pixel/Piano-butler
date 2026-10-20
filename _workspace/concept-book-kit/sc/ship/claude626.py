import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 612 |')]
assert len(idx) == 1
lines.insert(idx[0] + 1, "| 613 | 2026-10-21 | **Scale finder: major and minor shown together on the circle (two rings, new design).** Her decision (2026-10-21): she liked the two-ring structure (major outside, relative minor inside) and only disliked the earlier design, so no Major/Minor chips. The dial now has the major keys on the outer ring (bigger circles) and their relative minors on the inner ring (larger labels than before), turning together; the coral capsule at the top holds the chosen pair; tap any circle on either ring to choose that key (the chosen one is navy, its partner has a coral outline); the centre shows the name, major/minor and the key signature. Below the dial only two buttons remain (\"one ♭ more\" / \"one ♯ more\") plus the search box. Built by `patch623.py` (`t626`). Checked the dial at 390 px for C major and for F-sharp minor (tapped on the inner ring): no console errors. Local commit only, not pushed. |")
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
