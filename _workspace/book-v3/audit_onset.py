# Part of the timing audit (her 16 Nov): where an aligned word start falls in a quiet stretch, how long until the sound
# really resumes (= how early that mark can appear). Marks are already shown 0.08 s early on purpose.
import json, sys, numpy as np
sys.path.insert(0, '/tmp/claude-0/pk'); import marks
OUT = '/mnt/user-data/outputs/books/read2'
h = open(OUT + '/index.html').read(); i = h.index('[{"k"'); CH, _ = json.JSONDecoder().raw_decode(h[i:])
errs = []; n = 0
for c in CH:
    for cl in c.get('clips', []):
        path = OUT + '/' + cl['f'].split('?')[0]
        for ln in cl['l']:
            t = ln.get('text')
            if not t or ln.get('who') in ('pause', 'piano'): continue
            al = marks.align(path, ln['t0'], ln['t1'], t); e = marks.envelope(path)
            if not al: continue
            thr = max(120.0, float(np.percentile(e[int(ln['t0'] * 100):int(ln['t1'] * 100)], 60)) * 0.12)
            for _, ws in al[1:]:
                n += 1; a = int(ws * 100); seg = e[max(0, a - 30):a + 30]
                if len(seg) < 60 or seg[30] >= thr: continue
                k = next((j for j in range(30, 60) if seg[j] >= thr), None)
                if k is not None: errs.append((k - 30) / 100)
errs = np.array(errs)
print(n, 'word starts;', len(errs), 'sit in a quiet stretch; the sound resumes after: median', np.median(errs), 'p90', np.percentile(errs, 90), 'max', errs.max())
