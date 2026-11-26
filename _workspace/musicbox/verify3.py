# Music Box 3: checks each page's notes back against the open score it was converted from.
import json, re, sys
sys.path.insert(0, '.')
import conv
from fractions import Fraction as Fr
SEMI = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
def mid(x): m = re.match(r"^([A-G])([#b]?)([',]*)$", x); return SEMI[m[1]] + {'#': 1, 'b': -1, '': 0}[m[2]] + 12 * m[3].count("'") - 12 * m[3].count(',')
def mine(i):
    d = json.load(open(f'md{i}.json')); out = []
    for ln in d['gig']['song_grid']:
        for b in ln:
            T = (b['r'].split() + ['-'] * d['beats'])[:d['beats']]; T = T[d['beats'] - b['pick']:] if b.get('pick') else T[:b['head']] if b.get('head') else T
            for t in T:
                parts = t.split('.') if '.' in t else [t]; n = Fr(1, len(parts))
                for x in parts:
                    tie = x.startswith('~'); x = x.lstrip('~')
                    if re.match(r"^[A-G]", x) and not tie: out.append([mid(x), n])
                    elif out: out[-1][1] += n
    return out
def source(title, to, semis, box, rng, full):
    bars, m, k = conv.load(title, to, semis); out = []; i = 0; merged = []
    while i < len(bars):
        b = bars[i]
        if 0 < i < len(bars) - 1 and b['len'] < full and bars[i + 1]['len'] == full - b['len']: merged.append([b, bars[i + 1]]); i += 2
        else: merged.append([b]); i += 1
    for grp in merged[rng[0]:rng[1]]:
        for b in grp:
            for o, p, d, tie in b['ev']:
                if p and not tie: out.append([mid(p), d / box])
                elif out: out[-1][1] += d / box
    return out
J = [("She'll be Coming Round the Mountain", 'C', None, 1, (0, 17), 4), ('Grand Old Duke of York', 'C', None, 1, (0, 9), 4), ('Blue Bells of Scotland', None, None, 1, (0, 9), 4), ("It's a Long Way to Tipperary", 'C', None, 1, (0, 33), 4),
     ('W3KOOA', None, None, Fr(1, 2), (0, 16), 3), ("John Brown's Body", 'C', None, Fr(1, 2), (0, 17), 3), ('Scotland the Brave', 'F', -2, 1, (0, 33), 4), ('Blaydon Races', 'C', None, Fr(1, 2), (0, 33), 3)]
for i, (t, to, se, box, rng, full) in enumerate(J, 1):
    a = mine(i); b = source(t, to, se, box, rng, full)
    print(f'{i} {t:38s} page {len(a):3d} notes, source {len(b):3d} | pitches {"identical" if [x[0] for x in a] == [x[0] for x in b] else "DIFFERENT"} | lengths {"identical" if [x[1] for x in a[:-1]] == [x[1] for x in b[:-1]] else "DIFFERENT"}')
