# The sentences light their notes on p. 29 word by word: Every Good Boy Deserves Fun on the treble lines, FACE on the
# treble spaces, Great Big Dragons Fly Away on the bass lines, All Cows Eat Grass on the bass spaces.
import sys, json, re; sys.path.insert(0, '/tmp/claude-0/pk'); import marks
P = '/tmp/claude-0/hum/index.html'; h = open(P).read()
i = h.index('const CH = ') + 11; CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ce = i + n1
c = next(x for x in CH if x['k'] == 'P5'); cl = c['clips'][1]; path = '/mnt/user-data/outputs/books/read2/' + cl['f'].split('?')[0]
reg = [0.073, 0.1026, 0.8539, 0.4808]; pool = marks.region_notes(29, reg)
def notes(clef, names, x0, x1): return [next(n for n in pool if n['clef'] == clef and n['n'] == nm and x0 <= n['r'][0] < x1) for nm in names]
SETS = {'Every Good Boy Deserves Fun': ('G', 'EGBDF', 0, .56), 'Great Big Dragons Fly Away': ('F', 'GBDFA', 0, .56), 'All Cows Eat Grass': ('F', 'ACEG', .56, 1)}
for ln in cl['l']:
    t = ln.get('text', ''); at = marks.timer(t, ln['t0'], ln['t1'], path); mk = []
    for phrase, (clef, nm, x0, x1) in SETS.items():
        p = t.find(phrase)
        if p < 0: continue
        ws = [m for m in re.finditer(r'[A-Z][a-z]*', phrase)]
        for w, n in zip(ws, notes(clef, nm, x0, x1)): mk.append({'k': 'nt', 't': at(p + w.start()), 'e': round(ln['t1'] + .4, 2), 'p': 29, 'r': [n['r']], 'n': n['n']})
    if 'spell face' in t:
        p = t.find('face'); [mk.append({'k': 'nt', 't': at(p), 'e': round(ln['t1'] + .4, 2), 'p': 29, 'r': [n['r']], 'n': n['n']}) for n in notes('G', 'FACE', .56, 1)]
    if mk: ln['mk'] = mk; print(ln['who'], t[:40], len(mk), [m['t'] for m in mk])
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:]; open(P, 'w').write(h)
