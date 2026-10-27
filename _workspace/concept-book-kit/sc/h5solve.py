# A small four-part voice-leading solver for the Grade 5 harmony room: every progression it prints obeys the rules checked below.
import itertools, json, sys
L = 'CDEFGAB'; WHITE = [0, 2, 4, 5, 7, 9, 11]
SHARPS = ['F', 'C', 'G', 'D', 'A', 'E', 'B']; FLATS = ['B', 'E', 'A', 'D', 'G', 'C', 'F']
KEYS = {  # tonic letter, accidental, (type, n), minor
  'C': ('C', 0, (None, 0), 0), 'G': ('G', 0, ('sharp', 1), 0), 'D': ('D', 0, ('sharp', 2), 0), 'A': ('A', 0, ('sharp', 3), 0),
  'F': ('F', 0, ('flat', 1), 0), 'Bb': ('B', -1, ('flat', 2), 0), 'Eb': ('E', -1, ('flat', 3), 0),
  'Am': ('A', 0, (None, 0), 1), 'Em': ('E', 0, ('sharp', 1), 1), 'Dm': ('D', 0, ('flat', 1), 1), 'Gm': ('G', 0, ('flat', 2), 1), 'Bm': ('B', 0, ('sharp', 2), 1),
}
RANGE = {'S': (60, 79), 'A': (55, 72), 'T': (48, 67), 'B': (40, 60)}
def sig(k):
    ty, n = KEYS[k][2]; out = {}
    if ty: [out.__setitem__(x, 1 if ty == 'sharp' else -1) for x in (SHARPS if ty == 'sharp' else FLATS)[:n]]
    return out
def td(k, octv=3): return octv * 7 + L.index(KEYS[k][0])
def note(k, step, base):   # (d, acc): step scale steps above the tonic at d=base
    d = base + step; let = L[d % 7]; a = sig(k).get(let, 0)
    if KEYS[k][3] and step % 7 == 6: a += 1
    return (d, a)
def midi(n): d, a = n; return (d // 7 + 1) * 12 + WHITE[d % 7] + a
def name(n): d, a = n; return L[d % 7] + {1: '#', -1: 'b', 0: '', 2: '##', -2: 'bb'}[a] + str(d // 7)
def tone_of(k, n, deg):   # 0 root, 2 third, 4 fifth of the chord on deg, or None
    x = ((n[0] - td(k, 0)) - (deg - 1)) % 7
    return x if x in (0, 2, 4) else None
def is_lead(k, n): return (n[0] - td(k, 0)) % 7 == 6
def cands(k, deg, inv):
    out = []; base = td(k, 0)
    btone = [0, 2, 4][inv]
    for oc in range(1, 6):
        for t in (0, 2, 4):
            pass
    tones = []
    for d in range(14, 50):   # every chord note in a wide range
        x = ((d - base) - (deg - 1)) % 7
        if x in (0, 2, 4): tones.append(note(k, d - base, base))
    basses = [n for n in tones if tone_of(k, n, deg) == btone and RANGE['B'][0] <= midi(n) <= RANGE['B'][1]]
    def inr(v, n): return RANGE[v][0] <= midi(n) <= RANGE[v][1]
    for B in basses:
        for T in tones:
            if not inr('T', T) or midi(T) <= midi(B): continue
            for A in tones:
                if not inr('A', A) or midi(A) <= midi(T) or midi(A) - midi(T) > 12: continue
                for S in tones:
                    if not inr('S', S) or midi(S) <= midi(A) or midi(S) - midi(A) > 12: continue
                    ch = {'S': S, 'A': A, 'T': T, 'B': B}
                    if ok_chord(k, deg, inv, ch): out.append(ch)
    return out
def ok_chord(k, deg, inv, ch, final=False):
    ts = [tone_of(k, ch[v], deg) for v in 'SATB']
    cnt = {x: ts.count(x) for x in (0, 2, 4)}
    if sum(1 for v in 'SATB' if is_lead(k, ch[v])) > 1: return False   # the leading note never doubled
    if inv == 2: return cnt[4] == 2 and cnt[0] == 1 and cnt[2] == 1   # the 6-4: the bass (the 5th) doubled
    if deg == 7: return cnt[0] == 1 and cnt[2] == 2 and cnt[4] == 1   # VIIb: the bass (the 3rd) doubled, the leading note once
    if inv == 0:
        if cnt[0] == 2 and cnt[2] == 1 and cnt[4] == 1: return True
        if deg == 6 and cnt[0] == 1 and cnt[2] == 2 and cnt[4] == 1: return True   # VI: the 3rd may be doubled (before V)
        return final and deg == 1 and cnt[0] == 3 and cnt[2] == 1   # a final tonic may leave out its 5th
    return cnt[0] >= 1 and cnt[2] >= 1 and cnt[4] >= 1   # first inversion: complete, any doubling but the leading note
def mint(a, b):   # melodic interval: (letters, semitones)
    return (b[0] - a[0], midi(b) - midi(a))
def aug_step(a, b):
    dl, ds = mint(a, b); return abs(dl) == 1 and abs(ds) == 3
def ok_move(k, c1, d1, i1, c2, d2, i2):
    V = 'SATB'
    for x, y in itertools.combinations(V, 2):
        p, q = midi(c1[x]) - midi(c1[y]), midi(c2[x]) - midi(c2[y])
        mv = c1[x] != c2[x] or c1[y] != c2[y]
        if mv and p % 12 == q % 12 and p % 12 in (0, 7) and (c1[x] != c2[x] and c1[y] != c2[y]): return False   # parallel (or contrary) 5ths and 8ves
    for v in V:
        if aug_step(c1[v], c2[v]): return False
        if abs(midi(c2[v]) - midi(c1[v])) > (12 if v == 'B' else 7): return False
        if abs(midi(c2[v]) - midi(c1[v])) == 6: return False   # no tritone leap
    sb1, sb2 = midi(c1['S']), midi(c2['S'])   # hidden 5ths/8ves in the outer voices, the soprano leaping
    bb1, bb2 = midi(c1['B']), midi(c2['B'])
    if (sb2 - sb1) * (bb2 - bb1) > 0 and (sb2 - bb2) % 12 in (0, 7) and abs(sb2 - sb1) > 2: return False
    for v, up in (('S', 'A'), ('A', 'T'), ('T', 'B')):   # no overlap
        if midi(c2[v]) < midi(c1[up]) or midi(c2[up]) > midi(c1[v]): return False
    for v in V:   # the leading note rises to the tonic (an inner voice in V-I may fall to the 5th)
        if is_lead(k, c1[v]) and d1 in (5, 7) and d2 == 1:
            st = c2[v][0] - c1[v][0]
            if st == 1: continue
            if v in 'AT' and d1 == 5 and st == -2: continue
            return False
    if i1 == 2 and d2 == 5:   # the cadential 6-4: the 6th and the 4th fall a step, the bass stays
        for v in 'SAT':
            tn = tone_of(k, c1[v], 1)
            if tn in (0, 2) and c2[v][0] - c1[v][0] != -1: return False
            if tn == 4 and c2[v] != c1[v]: return False
        if midi(c2['B']) % 12 != midi(c1['B']) % 12: return False
    return True
def cost(seq):
    c = 0
    for a, b in zip(seq, seq[1:]):
        for v in 'SAT': c += abs(midi(b[v]) - midi(a[v])) * (1 if v == 'S' else 1.4)
        c += abs(midi(b['B']) - midi(a['B'])) * 0.3
    c += abs(midi(seq[0]['S']) - 70) * 0.3
    return c
def solve(k, prog):   # prog: [(deg, inv), ...]; the last is the final chord
    cs = [cands(k, d, i) for d, i in prog]
    cs[-1] = [c for c in cands_final(k, *prog[-1])]
    best = None
    def rec(j, seq, cst):
        nonlocal best
        if best and cst >= best[0]: return
        if j == len(prog):
            tot = cost(seq) + (0 if tone_of(k, seq[-1]['S'], 1) == 0 else 3)
            if not best or tot < best[0]: best = (tot, list(seq))
            return
        for c in cs[j]:
            if seq and not ok_move(k, seq[-1], prog[j - 1][0], prog[j - 1][1], c, prog[j][0], prog[j][1]): continue
            rec(j + 1, seq + [c], cst)
    rec(0, [], 0)
    return best[1] if best else None
def cands_final(k, deg, inv):
    out = []
    for c in cands_loose(k, deg, inv):
        if ok_chord(k, deg, inv, c, final=True): out.append(c)
    return out
def cands_loose(k, deg, inv):
    base = td(k, 0); tones = []
    for d in range(14, 50):
        x = ((d - base) - (deg - 1)) % 7
        if x in (0, 2, 4): tones.append(note(k, d - base, base))
    inr = lambda v, n: RANGE[v][0] <= midi(n) <= RANGE[v][1]
    btone = [0, 2, 4][inv]; out = []
    for B in [n for n in tones if tone_of(k, n, deg) == btone and inr('B', n)]:
        for T in tones:
            if not inr('T', T) or midi(T) <= midi(B): continue
            for A in tones:
                if not inr('A', A) or midi(A) <= midi(T) or midi(A) - midi(T) > 12: continue
                for S in tones:
                    if not inr('S', S) or midi(S) <= midi(A) or midi(S) - midi(A) > 12: continue
                    out.append({'S': S, 'A': A, 'T': T, 'B': B})
    return out
if __name__ == '__main__':
    MAJ = ['C', 'G', 'D', 'A', 'F', 'Bb', 'Eb']; MIN = ['Am', 'Em', 'Dm', 'Gm', 'Bm']
    res = {}
    for k in MAJ + MIN:
        mn = KEYS[k][3]
        progs = {
          'c64': [(1, 2), (5, 0), (1, 0)], 'b64': [(1, 1), (5, 0), (1, 0)], 'r64': [(1, 0), (5, 0), (1, 0)],
          'iv': [(4, 0), (5, 0), (1, 0)], 'ivb': [(4, 1), (5, 0), (1, 0)],
          'vii': [(1, 0), (7, 1), (1, 1)],
        }
        if mn: progs['vi'] = [(6, 0), (5, 0), (1, 0)]
        else: progs['iib'] = [(2, 1), (5, 0), (1, 0)]
        res[k] = {}
        for nm, pr in progs.items():
            sol = solve(k, pr)
            res[k][nm] = [' '.join(name(c[v]) for v in 'SATB') for c in sol] if sol else None
            if not sol: print('NO SOLUTION', k, nm, file=sys.stderr)
    print(json.dumps(res, indent=1))
