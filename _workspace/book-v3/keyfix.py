# Her 18 Nov (going through Pitch): the keys that light must be the keys being talked about. Fixes found by checking
# every Pitch line's spoken letters against its lit keys: harmonic answers lit only their first key; "to A" was read as
# the article "a"; black keys (E flat, B flat, C sharp, D sharp) never lit on unlabelled keyboards; "finger three"
# never moved to E; "the same size as C to E" lit C and E on the F-A picture; "F is the first key" lit only Middle C.
import json, sys, re
sys.path.insert(0, '/tmp/claude-0/pk'); import marks
PM = marks.PM; P = '/tmp/claude-0/punch/new_index.html'; h = open(P).read()
i = h.index('const CH = ') + 11; CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ce = i + n1
ROOT = '/mnt/user-data/outputs/books/read2/'
def clip(k, ci): return next(x for x in CH if x['k'] == k)['clips'][ci]
def kb_of(src, near=None):
    kbs = PM[src]['kbs']
    if near is None: return kbs[0]
    return min(kbs, key=lambda kb: abs(kb['r'][0] + kb['r'][2] / 2 - near[0]) + abs(kb['r'][1] - near[1]))
def white(kb, n, nth=0): return [w for w in kb['white'] if w.get('n') == n][nth]['r']
def black_after(kb, n, nth=0):   # the black key just right of white key n
    w = white(kb, n, nth); x = w[0] + w[2]
    return min(kb['black'], key=lambda b: abs(b['r'][0] + b['r'][2] / 2 - x))['r']
def at(cl, ln, phrase): return marks.timer(ln['text'], ln['t0'], ln['t1'], ROOT + cl['f'].split('?')[0])(ln['text'].index(phrase))
def key(t, e, r, n, pop=None, p=None):
    m = {'k': 'key', 't': round(t, 2), 'e': round(e, 2), 'p': p, 'r': [r], 'n': n}
    if pop: m['pop'] = pop
    return m
def line(cl, who, has): return next(l for l in cl['l'] if l['who'] == who and has in l.get('text', ''))
def piano(cl): return [l for l in cl['l'] if l['who'] == 'piano'][-1]
END = lambda l: round(l['t1'] + .4, 2)
# P9 try it: thumb to finger three is C to E
cl = clip('P9', 5); ln = line(cl, 'B', 'finger three'); kb = kb_of('pop:P9-4'); t3 = at(cl, ln, 'Thumb to finger three')
for m in ln['mk']:
    if m.get('n') == 'G': m['e'] = round(t3, 2)
ln['mk'] += [key(t3, END(ln), white(kb, 'C'), 'C', 'P9-4', 35), key(t3 + .9, END(ln), white(kb, 'E'), 'E', 'P9-4', 35)]
# P10 examples: both keys of each answer; the black key B flat; no C to E on the F-A picture
def both(k, ci, pop, a, b, page=37):
    cl = clip(k, ci); kb = kb_of('pop:' + pop); pl = piano(cl); t = pl['notes'][0]
    pl['mk'] = [key(t, END(pl), white(kb, a), a, pop, page), key(t, END(pl), white(kb, b, -1 if b == 'C' else 0), b, pop, page)]
    return cl, kb
cl, kb = both('P10', 1, 'P10-2', 'A', 'C'); ln = line(cl, 'P', 'B flat'); tb = at(cl, ln, 'B flat')
ln['mk'] = [m for m in ln['mk'] if not (m.get('n') == 'B' and m['t'] > tb - .05)] + [key(tb, END(ln), black_after(kb, 'A'), 'B♭', 'P10-2', 37), key(at(cl, ln, 'and B:'), END(ln), white(kb, 'B'), 'B', 'P10-2', 37)]
cl, kb = both('P10', 2, 'P10-3', 'F', 'A'); ln = line(cl, 'P', 'major third')
ln['mk'] = [key(ln['t0'], END(ln), white(kb, 'F'), 'F', 'P10-3', 37), key(ln['t0'], END(ln), white(kb, 'A'), 'A', 'P10-3', 37)]
cl, kb = both('P10', 3, 'P10-4', 'D', 'A'); ln = line(cl, 'P', 'D to A'); ln['mk'].append(key(at(cl, ln, 'A is'), END(ln), white(kb, 'A'), 'A', 'P10-4', 37))
# P10 opening (p. 37): C to E flat lights its E flat
cl = clip('P10', 0); ln = line(cl, 'B', 'C to E flat'); cs = [m for m in ln['mk'] if m.get('n') == 'C']
kb2 = kb_of('37', (cs[-1]['r'][0][0], cs[-1]['r'][0][1])); ln['mk'].append(key(at(cl, ln, 'E flat'), END(ln), black_after(kb2, 'D'), 'E♭', None, 37))
# P7 Für Elise and the P4 example show staves: light the notes themselves
def note(src, n, acc=''):
    return next(x for x in PM[src]['notes'] if x['n'] == n and (x.get('acc') or '') == acc)['r']
def nt(t, e, r, n, pop, p): return {'k': 'nt', 't': round(t, 2), 'e': round(e, 2), 'p': p, 'r': [r], 'n': n, 'pop': pop}
cl = clip('P7', 6); ln = cl['l'][0]
try: ln['mk'].append(nt(at(cl, ln, 'D sharp'), END(ln), note('pop:P7-5', 'D', '#'), 'D♯', 'P7-5', 32))
except StopIteration: print('no D sharp note on P7-5:', [(x['n'], x.get('acc')) for x in PM['pop:P7-5']['notes']])
cl = clip('P4', 1); ln = line(cl, 'P', 'F is the first')
ln['mk'] = [m for m in ln['mk'] if m.get('n') != 'C'] + [nt(ln['t0'], END(ln), note('pop:P4-1', 'F'), 'F', 'P4-1', 27)]
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:]; open(P, 'w').write(h); print('key fixes applied')
