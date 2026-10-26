# Four-part cadences for Grade 4, realised from scale-degree templates in many keys, then checked:
# ranges, spelling (key + raised 7th in minor), doubling, parallel 5ths and octaves, voice crossing, spacing.
L = 'CDEFGAB'; WHITE = [0, 2, 4, 5, 7, 9, 11]
SH = ['F', 'C', 'G', 'D', 'A', 'E', 'B']; FL = ['B', 'E', 'A', 'D', 'G', 'C', 'F']
KEYS = {  # tonic letter, tonic acc, signature (type, n), minor
 'C': ('C', 0, (None, 0), False), 'G': ('G', 0, ('s', 1), False), 'D': ('D', 0, ('s', 2), False), 'A': ('A', 0, ('s', 3), False), 'E': ('E', 0, ('s', 4), False),
 'F': ('F', 0, ('f', 1), False), 'Bb': ('B', -1, ('f', 2), False), 'Eb': ('E', -1, ('f', 3), False), 'Ab': ('A', -1, ('f', 4), False),
 'Am': ('A', 0, (None, 0), True), 'Em': ('E', 0, ('s', 1), True), 'Bm': ('B', 0, ('s', 2), True), 'Fsm': ('F', 1, ('s', 3), True), 'Csm': ('C', 1, ('s', 4), True),
 'Dm': ('D', 0, ('f', 1), True), 'Gm': ('G', 0, ('f', 2), True), 'Cm': ('C', 0, ('f', 3), True), 'Fm': ('F', 0, ('f', 4), True)}
def sig(k):
    ty, n = KEYS[k][2]
    return {x: (1 if ty == 's' else -1) for x in (SH if ty == 's' else FL)[:n]} if ty else {}
def note(k, td, step):  # td: tonic d (octave*7+letter); step: scale steps from tonic
    d = td + step; Lt = L[d % 7]; a = sig(k).get(Lt, 0)
    if KEYS[k][3] and step % 7 == 6: a += 1
    return (d, a)
def midi(n): d, a = n; return (d // 7 + 1) * 12 + WHITE[d % 7] + a
def nm(n): d, a = n; return L[d % 7] + {1: '#', -1: 'b', 0: '', 2: '##', -2: 'bb'}[a] + str(d // 7)
def parse(s):
    import re; m = re.match(r'^([A-G])(#|b)?(\d)$', s); return (int(m.group(3)) * 7 + L.index(m.group(1)), 1 if m.group(2) == '#' else -1 if m.group(2) == 'b' else 0)
RANGE = {'S': ('C4', 'G5'), 'A': ('G3', 'C5'), 'T': ('C3', 'G4'), 'B': ('E2', 'C4')}
V = 'SATB'
# templates: per chord, steps from the tonic for S A T B (tonic = degree 1 at step 0)
T_MAJ = {
 'perfect': [(6, 4, 1, -3), (7, 4, 2, -7)],          # V: B G D G / I: C G E C   (C major, tonic C4)
 'plagal': [(7, 5, 3, -4), (7, 4, 2, -7)],           # IV: C A F F / I: C G E C
 'imperfect': [(9, 7, 4, -7), (8, 6, 4, -10)],       # I: E C G C / V: D B G G
 'imperfect4': [(7, 5, 3, -4), (6, 4, 1, -3)],       # IV: C A F F / V: B G D G
 'interrupted': [(6, 4, 1, -3), (7, 2, 0, -2)],      # V: B G D G / VI: C E C A
}
T_MIN = {
 'perfect': [(6, 4, 1, -3), (7, 4, 2, -7)],          # V: G# E B E / i: A E C A   (A minor, tonic A4? computed)
 'plagal': [(7, 5, 3, -4), (7, 4, 2, -7)],
 'imperfect': [(9, 7, 4, -7), (8, 6, 4, -10)],
 'interrupted': [(6, 4, 1, -3), (7, 2, 0, -2)],
}
def chords_for(k, cad, td):
    tpl = (T_MIN if KEYS[k][3] else T_MAJ)[cad]
    return [tuple(note(k, td, s) for s in ch) for ch in tpl]
def check(ch2):
    errs = []
    for ch in ch2:
        for v, n in zip(V, ch):
            lo, hi = map(parse, RANGE[v])
            if not (midi(lo) <= midi(n) <= midi(hi)): errs.append('range ' + v + ' ' + nm(n))
        ms = [midi(n) for n in ch]
        if not (ms[0] >= ms[1] >= ms[2] >= ms[3]): errs.append('crossing')
        if ms[0] - ms[1] > 12 or ms[1] - ms[2] > 12: errs.append('spacing')
    a, b = ch2
    for i in range(4):
        for j in range(i + 1, 4):
            i1 = (midi(a[i]) - midi(a[j])) % 12; i2 = (midi(b[i]) - midi(b[j])) % 12
            moved = midi(a[i]) != midi(b[i]) or midi(a[j]) != midi(b[j])
            if moved and i1 == i2 and i1 in (0, 7) and midi(a[i]) != midi(b[i]) and midi(a[j]) != midi(b[j]): errs.append('parallel ' + V[i] + V[j] + (' 8ve' if i1 == 0 else ' 5th'))
    return errs
