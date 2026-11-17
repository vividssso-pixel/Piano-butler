# Stage 2: the new pages' regions; marks measured again on the moved pages (text lines), piano marks moved key by key
# to the same key of the same keyboard on the new page; the black key between C and D lit where it is mentioned.
import json, sys, re
sys.path.insert(0, '/tmp/claude-0/pk'); import marks
OLD = json.load(open('/tmp/claude-0/pk/pagemarks.bak.json')); NEW = marks.PM
P = '/tmp/claude-0/sw/index.html'; h = open(P).read()
i = h.index('const CH = ') + 11; CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ce = i + n1
j = h.index('const REG = ') + 12; REG, n2 = json.JSONDecoder().raw_decode(h[j:]); re_ = j + n2
R = json.load(open('/tmp/claude-0/sw/regs.json'))
for pg, o in R.items():
    d = {k: {'b': v, 'l': [], 'r': None} for k, v in o.items()}
    if pg == '32': d['rule'] = d['more']
    if pg == '33': d['table'] = d['more']
    if pg == '34': d['rule'] = d['remember']
    REG[pg] = d
ROOT = '/mnt/user-data/outputs/books/read2/'
def ch(k): return next(x for x in CH if x['k'] == k)
for ln in ch('P8')['clips'][1]['l']:   # the semitone part of "One line, one bar" is on p. 33
    if ln['cue'].get('r') == 'more': ln['cue'] = dict(ln['cue'], p=33)
KBMAP = {('34', 32): [(0, 0), (1, 1), (2, 2)], ('32', 33): [(0, 0)], ('33', 34): []}
def remap(m, oldpg):
    """a key mark on old page oldpg -> the same key of the matching keyboard on the new page"""
    newpg = m['p']; ok = OLD.get(oldpg, {}).get('kbs', []); nk = NEW.get(str(newpg), {}).get('kbs', [])
    r0 = m['r'][0]
    for oi, ni in KBMAP.get((oldpg, newpg), []):
        for kind in ('white', 'black'):
            for x, key in enumerate(ok[oi][kind]):
                if [round(v, 3) for v in key['r']] == [round(v, 3) for v in r0]:
                    return dict(m, r=[nk[ni][kind][x]['r']])
    return None
OLDPG = {'P7': {32: '34'}, 'P8': {33: '32', 34: '33'}}
for k in ('P7', 'P8'):
    for cl in ch(k)['clips']:
        path = ROOT + cl['f'].split('?')[0]; answered = not any(l.get('who') == 'pause' for l in cl['l'])
        for ln in cl['l']:
            if ln.get('who') == 'pause': answered = True
            if ln['who'] == 'piano':
                keep = []
                for m in ln.get('mk', []):
                    if m.get('pop'): keep.append(m); continue
                    op = OLDPG[k].get(m['p'])
                    if k == 'P8' and m['p'] == 34: op = '32'
                    nm = remap(m, op) if op else None
                    if nm: keep.append(nm)
                ln['mk'] = keep
                continue
            ln.pop('mk', None); ln.pop('sp', None)
            mk = marks.line_marks(ln, REG=REG, audio=path, answered=answered) or []
            if 'a black key between' in ln.get('text', '') and 'C to D' in ln['text']:
                # light the black key between C and D on the line's own picture
                pop = (ln.get('lens') or {}).get('src', ''); mm = re.search(r'pops/(P\d+-\d+)', pop)
                src = ('pop:' + mm.group(1)) if mm else str(ln['cue']['p'])
                kbs = NEW[src]['kbs']; t = marks.timer(ln['text'], ln['t0'], ln['t1'], path)(ln['text'].index('a black key between'))
                for kb in kbs:
                    ws = kb['white']; names = [w.get('n') for w in ws]
                    if 'C' in names and 'D' in names and names.index('D') == names.index('C') + 1:
                        x = ws[names.index('C')]['r'][0] + ws[names.index('C')]['r'][2]
                        b = min(kb['black'], key=lambda b: abs(b['r'][0] + b['r'][2] / 2 - x))
                        mk.append({'k': 'key', 't': round(t, 2), 'e': round(ln['t1'] + .4, 2), 'p': ln['cue']['p'], 'r': [b['r']], 'n': 'C♯/D♭', **({'pop': mm.group(1)} if mm else {})}); break
            if mk: ln['mk'] = mk
            sp = marks.phrase_spans(ln, path)
            if sp and len(sp) > 1: ln['sp'] = sp
        print(k, cl['t'], [(l['who'], len(l.get('mk', []))) for l in cl['l']])
o = ch('O1')['clips'][0]; path = ROOT + o['f'].split('?')[0]
for ln in o['l']:
    if 'Ten chapters' in ln.get('text', ''):
        ln.pop('mk', None); mk = marks.line_marks(ln, REG=REG, audio=path); 
        if mk: ln['mk'] = mk
        print('O1 chapters line marks', len(mk or []))
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:j] + json.dumps(REG, ensure_ascii=False) + h[re_:]
open(P, 'w').write(h); print('stage 2 done')
