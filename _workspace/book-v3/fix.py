# Her 18 Nov ("여기서 피아노 소리도 짤려"): the last note of an example's piano answer was cut short (0.9 s, then my
# fade took it away). Each one now rings on and dies away naturally: the note as recorded, then its own sound stretched
# out and fading to silence over about a second and a half.
import json, subprocess, numpy as np, soundfile as sf, librosa
SR = 24000; R2 = '/mnt/user-data/outputs/books/read2/'
def load(p): return np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout, np.float32).copy()
def chx(path):
    h = open(path).read(); i = h.index('const CH = ') + 11; CH, n = json.JSONDecoder().raw_decode(h[i:]); return h, i, n, CH
OH, _, _, OCH = chx('old_index.html'); P = '/tmp/claude-0/sw/index.html'; h, i, n1, CH = chx(P); ce = i + n1
dam = json.load(open('/tmp/claude-0/sw/damaged.json'))
swap = lambda f: f.replace('audio/P7/', 'audio/@@/').replace('audio/P8/', 'audio/P7/').replace('audio/@@/', 'audio/P8/')
done = 0
for k, f, gap in dam:
    if gap < 0: continue
    of = swap(f)
    ocl = next((cl for c in OCH for cl in c.get('clips', []) if cl['f'].split('?')[0] == of), None)
    cl = next(cl for c in CH for cl in c.get('clips', []) if cl['f'].split('?')[0] == f)
    if not ocl: print('no old clip', f); continue
    op = ocl['l'][-1]; cp = cl['l'][-1]
    old = load(of.replace('/', '_')); seg = old[int(op['t0'] * SR):int(op['t1'] * SR)]
    lo = op['notes'][-1] - op['t0']; L = op['t1'] - op['notes'][-1]
    a0, a1 = lo + min(.25, L * .3), lo + max(.3, L - .3)   # the steady part of the last note, before the old fade
    keep = seg[:int((lo + max(.35, L - .45)) * SR)]
    body = seg[int(a0 * SR):int(a1 * SR)]
    st = librosa.effects.time_stretch(body.astype(np.float32), rate=(a1 - a0) / 1.6)
    st = st * np.exp(np.linspace(0, -6.5, len(st)))
    x = int(.06 * SR); st[:x] *= np.linspace(0, 1, x); keep[-x:] *= np.linspace(1, 0, x)
    # match the level at the join
    lvl = np.sqrt(np.mean(keep[-int(.1 * SR):-x] ** 2)) / max(1e-6, np.sqrt(np.mean(st[x:x + int(.1 * SR)] ** 2)))
    st *= lvl
    piano = np.concatenate([keep[:-x], keep[-x:] + st[:x], st[x:], np.zeros(int(.3 * SR), np.float32)])
    cur = load(R2 + f); new = np.concatenate([cur[:int(cp['t0'] * SR)], piano])
    sf.write('/tmp/claude-0/tails/t.wav', new, SR)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', '/tmp/claude-0/tails/t.wav', '-codec:a', 'libmp3lame', '-b:a', '64k', R2 + f], check=True)
    cp['t1'] = round(cp['t0'] + len(piano) / SR, 2); cl['s'] = round(len(new) / SR)
    for m in cp.get('mk', []): m['e'] = max(m['e'], round(cp['t1'] - .2, 2))
    done += 1
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:]; open(P, 'w').write(h); print('last notes ring out in', done, 'clips')
