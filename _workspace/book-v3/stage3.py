# Stage 3: Für Elise's D sharp (lost when the lines were measured again) and the black keys of "find F sharp and B flat".
import json, sys, re
sys.path.insert(0, '/tmp/claude-0/pk'); import marks
PM = marks.PM; P = '/tmp/claude-0/sw/index.html'; h = open(P).read(); ROOT = '/mnt/user-data/outputs/books/read2/'
i = h.index('const CH = ') + 11; CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ce = i + n1
c = next(x for x in CH if x['k'] == 'P8')
cl = next(x for x in c['clips'] if x['t'].startswith('Try it')); ln = cl['l'][0]; path = ROOT + cl['f'].split('?')[0]
e0 = next(m for m in ln.get('mk', []) if m.get('n') == 'E'); pop = e0['pop']
d = next(x for x in PM['pop:' + pop]['notes'] if x['n'] == 'D' and x.get('acc') == '#')
t = marks.timer(ln['text'], ln['t0'], ln['t1'], path)(ln['text'].index('D sharp'))
ln['mk'].append({'k': 'nt', 't': round(t, 2), 'e': round(ln['t1'] + .4, 2), 'p': e0['p'], 'r': [d['r']], 'n': 'D♯', 'pop': pop})
cl = next(x for x in c['clips'] if 'find F sharp' in x['t']); path = ROOT + cl['f'].split('?')[0]
for ln in cl['l']:
    src = (ln.get('lens') or {}).get('src', ''); mm = re.search(r'pops/(P\d+-\d+)', src)
    if ln['who'] in ('P', 'piano') and mm and not mm.group(1).endswith('-q'):
        pop = mm.group(1); kbs = PM['pop:' + pop]['kbs']; print(pop, [[w.get('n') for w in kb['white']] for kb in kbs], ln.get('text', '')[:80], ln.get('notes'))
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:]; open(P, 'w').write(h); print('stage 3 done')
h = open(P).read(); i = h.index('const CH = ') + 11; CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ce = i + n1
c = next(x for x in CH if x['k'] == 'P8'); cl = next(x for x in c['clips'] if 'find F sharp' in x['t']); path = ROOT + cl['f'].split('?')[0]
kb = PM['pop:P8-1']['kbs'][0]; ws = kb['white']
def blk_after(ix): x = ws[ix]['r'][0] + ws[ix]['r'][2]; return min(kb['black'], key=lambda b: abs(b['r'][0] + b['r'][2] / 2 - x))['r']
FS, BF = blk_after(3), blk_after(5)
for ln in cl['l']:
    src = (ln.get('lens') or {}).get('src', '')
    if 'P8-1.webp' not in src or '-q' in src: continue
    if ln['who'] == 'P':
        at = marks.timer(ln['text'], ln['t0'], ln['t1'], path); e = round(ln['t1'] + .4, 2)
        ln['mk'] = (ln.get('mk') or []) + [{'k': 'key', 't': round(at(ln['text'].index('F sharp')), 2), 'e': e, 'p': 33, 'r': [FS], 'n': 'F♯', 'pop': 'P8-1'},
                                           {'k': 'key', 't': round(at(ln['text'].index('B flat')), 2), 'e': e, 'p': 33, 'r': [BF], 'n': 'B♭', 'pop': 'P8-1'}]
    if ln['who'] == 'piano':
        e = round(ln['t1'] + .4, 2); ln['mk'] = [{'k': 'key', 't': ln['notes'][0], 'e': e, 'p': 33, 'r': [FS], 'n': 'F♯', 'pop': 'P8-1', 'snd': 1}, {'k': 'key', 't': ln['notes'][1], 'e': e, 'p': 33, 'r': [BF], 'n': 'B♭', 'pop': 'P8-1', 'snd': 1}]
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:]; open(P, 'w').write(h); print('black keys of example 1 lit')
