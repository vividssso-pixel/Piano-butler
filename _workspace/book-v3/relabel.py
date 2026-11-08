# Part III Expression was inserted after Time (her 8 Nov), so Scales, Chords and Harmony in music move up one number.
# Runs after the generators, on their HTML, once per build.
import re
H = '/mnt/user-data/outputs/house-rooms/'
MAP = {'III': 'IV', 'IV': 'V', 'V': 'VI'}
for f in ('handbook-scales', 'handbook-harmony', 'handbook-harmony2'):
    p = H + f + '.html'; s = open(p).read()
    s = re.sub(r'\b(Part|PART|Parts|PARTS) (III|IV|V)\b(?!I)', lambda m: f'{m.group(1)} {MAP[m.group(2)]}', s)
    open(p, 'w').write(s)
print('relabelled')
