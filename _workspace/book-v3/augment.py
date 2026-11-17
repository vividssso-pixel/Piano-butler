# Her 18 Nov ("켜지는 건반 ... 잘 보고 정리"): two gaps found in every part after Pitch, filled the same way as in Pitch.
# 1. Sharps and flats never lit on a keyboard (only white keys did): each one said aloud now lights its black key, on the
#    keyboard the line already lights, as it is said. 2. A chord played at once lit only its first key: all its notes light.
import json, sys, re
sys.path.insert(0, '/tmp/claude-0/pk'); import marks
PM = marks.PM; P = '/tmp/claude-0/sw/index.html'; h = open(P).read(); ROOT = '/mnt/user-data/outputs/books/read2/'
i = h.index('const CH = ') + 11; CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ce = i + n1
W = 'CDEFGAB'
LET = re.compile(r'\b([A-G])(?:\s+(sharp|flat)|([♯♭]))?(?![a-z’\'])')
def kbs_of(m):
    src = ('pop:' + m['pop']) if m.get('pop') else str(m.get('p')); return PM.get(src, {}).get('kbs', [])
def find_kb(m):
    r = m['r'][0]
    for kb in kbs_of(m):
        for kind in ('white', 'black'):
            if any([round(v, 3) for v in k['r']] == [round(v, 3) for v in r] for k in kb[kind]): return kb
    return None
def black_for(kb, letter, acc):
    names = marks.key_letters(kb); ws = kb['white']
    if not names or not all(names): return []
    out = []
    for ix, n in enumerate(names):
        if n != letter: continue
        if acc == '#':
            if letter in 'EB': out.append(ws[ix + 1]['r'] if ix + 1 < len(ws) else None); continue
            x = ws[ix]['r'][0] + ws[ix]['r'][2]
        else:
            if letter in 'CF': out.append(ws[ix - 1]['r'] if ix > 0 else None); continue
            x = ws[ix]['r'][0]
        if not kb['black']: continue
        b = min(kb['black'], key=lambda b: abs(b['r'][0] + b['r'][2] / 2 - x))
        if abs(b['r'][0] + b['r'][2] / 2 - x) < ws[ix]['r'][2] * .6: out.append(b['r'])
    return [r for r in out if r]
added = chords = 0
for c in CH:
    if re.match(r'P\d', c['k']): continue   # Pitch was checked line by line
    for cl in c.get('clips', []):
        path = ROOT + cl['f'].split('?')[0]
        for li, ln in enumerate(cl['l']):
            keys = [m for m in ln.get('mk', []) if m['k'] == 'key']
            if not keys: continue
            kb = find_kb(keys[0])
            if not kb: continue
            if ln['who'] == 'piano':
                if len(ln.get('notes', [])) == 1 and len(keys) == 1:   # a chord: take its notes from the answer just before
                    prev = next((p for p in reversed(cl['l'][:li]) if p.get('text') and p['who'] != 'pause' and len(LET.findall(p['text'])) >= 2), None)
                    if not prev: continue
                    lets = [(x.group(1), '#' if (x.group(2) == 'sharp' or x.group(3) == '♯') else 'b' if (x.group(2) == 'flat' or x.group(3) == '♭') else '') for x in LET.finditer(prev['text'])]
                    names = marks.key_letters(kb)
                    if not names or not all(names) or len(lets) < 2 or len(lets) > 5: continue
                    start = keys[0]['r'][0]; got = []
                    ix0 = next((n for n, w in enumerate(kb['white']) if [round(v, 3) for v in w['r']] == [round(v, 3) for v in start]), None)
                    if ix0 is None: continue
                    pos = ix0
                    for l, a in lets[1:]:   # the chord climbs from its first key: each next letter, upwards
                        nxt = next((n for n in range(pos + 1, len(names)) if names[n] == l), None)
                        if nxt is None: got = None; break
                        pos = nxt; r = kb['white'][nxt]['r'] if not a else (black_for({'white': kb['white'][nxt:nxt + 2], 'black': kb['black'], 'r': kb['r']}, l, a) or [None])[0]
                        if r: got.append((r, l + {'#': '♯', 'b': '♭'}.get(a, '')))
                    if got:
                        for r, n in got: ln['mk'].append(dict(keys[0], r=[r], n=n))
                        chords += 1
                continue
            if not ln.get('text'): continue
            # a comparison ("the same shape as C E G", "like C to E") is not the picture's notes: it does not light
            cmp_ = [mm.start() for mm in re.finditer(r'\b(same [a-z ]*as|as|like)\s+(?=[A-G]\b)', ln['text'])]
            if cmp_ and keys:
                atc = marks.timer(ln['text'], ln['t0'], ln['t1'], path); t0c = min(atc(p) for p in cmp_)
                end = re.search(r'[.!?]', ln['text'][min(cmp_):]); t1c = atc(min(cmp_) + end.start()) if end else ln['t1'] + 1
                before = len(ln['mk']); ln['mk'] = [m for m in ln['mk'] if not (m['k'] == 'key' and t0c - .05 <= m['t'] <= t1c + .05)]
                if len(ln['mk']) < before: print('comparison unlit:', c['k'], ln['text'][:60])
                keys = [m for m in ln.get('mk', []) if m['k'] == 'key']
                if not keys: continue
            at = marks.timer(ln['text'], ln['t0'], ln['t1'], path); have = {m.get('n') for m in keys}
            for x in LET.finditer(ln['text']):
                a = '#' if (x.group(2) == 'sharp' or x.group(3) == '♯') else 'b' if (x.group(2) == 'flat' or x.group(3) == '♭') else ''
                if not a: continue
                nm = x.group(1) + ('♯' if a == '#' else '♭')
                if nm in have: continue
                rs = black_for(kb, x.group(1), a)
                if not rs: continue
                ln['mk'].append(dict(keys[0], k='key', t=round(at(x.start()), 2), r=[rs[0]], n=nm)); have.add(nm); added += 1
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:]; open(P, 'w').write(h)
print('black keys added', added, '· chords completed', chords)
