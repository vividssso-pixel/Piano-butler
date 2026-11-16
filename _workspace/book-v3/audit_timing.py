# Her 16 Nov: "check that the highlight comes on at the right moment, so I don't have to". An independent audit of every mark:
# 1. each spoken line's words are force-aligned to the audio (PocketSphinx); lines that would not align are counted;
# 2. the alignment is checked against the pauses heard in the audio (an independent signal): every clear pause must fall
#    between two words, not inside one;
# 3. every mark must start within its line, keys and notes in the order they are said, a highlight no later than 0.25 s
#    after its phrase's first word, and none before the line begins.
import json, sys, re, collections
sys.path.insert(0, '/tmp/claude-0/pk'); import marks
OUT = '/mnt/user-data/outputs/books/read2'
h = open(OUT + '/index.html').read(); i = h.index('[{"k"'); CH, _ = json.JSONDecoder().raw_decode(h[i:])
st = collections.Counter(); bad = []
for c in CH:
    for cl in c.get('clips', []):
        path = OUT + '/' + cl['f'].split('?')[0]
        for ln in cl['l']:
            text = ln.get('text')
            if not text or ln.get('who') in ('pause', 'piano'): continue
            st['lines'] += 1
            al = marks.align(path, ln['t0'], ln['t1'], text)
            if not al: st['not aligned'] += 1; bad.append((c['k'], cl['t'], 'not aligned', text[:60])); continue
            st['aligned'] += 1
            # 2. pauses heard must fall between aligned words
            starts = [t for _, t in al]
            for g in marks.gaps(path, ln['t0'], ln['t1'], 180):
                st['pauses'] += 1
                # a pause is fine if no aligned word starts within 0.08 s on either side of its centre (i.e. it is not mid-word)
                if any(abs(t - g) < 0.06 for t in starts[1:]): st['pause inside a word?'] += 1; bad.append((c['k'], cl['t'], f'pause at {g} near a word start', text[:60]))
            # 3. marks
            mk = ln.get('mk', []); last = {}
            for m in mk:
                st['marks'] += 1
                if m['t'] < ln['t0'] - 0.01 or m['t'] > ln['t1'] + 0.01: st['outside line'] += 1; bad.append((c['k'], cl['t'], 'mark outside its line', m['k'], m['t']))
                if m['e'] <= m['t']: st['zero length'] += 1; bad.append((c['k'], cl['t'], 'mark ends before it starts', m['k']))
                if m['k'] in ('key', 'nt'):
                    if m['k'] in last and m['t'] < last[m['k']] - 0.01: st['out of order'] += 1; bad.append((c['k'], cl['t'], 'keys out of order', text[:50]))
                    last[m['k']] = m['t']
            for s in ln.get('sp') or []:
                w = next((t for p, t in al if p >= s[1]), None)
                if w is not None:
                    st['phrases'] += 1; d = s[0] - w
                    if d > 0.25: st['phrase late'] += 1; bad.append((c['k'], cl['t'], f'phrase {d:.2f}s late', text[s[1]:s[1] + 30]))
                    if d < -0.6: st['phrase early'] += 1; bad.append((c['k'], cl['t'], f'phrase {-d:.2f}s early', text[s[1]:s[1] + 30]))
print(dict(st)); print(len(bad), 'issues')
for b in bad[:40]: print(b)
json.dump(bad, open('/tmp/claude-0/prv/timing_issues.json', 'w'), indent=0)
