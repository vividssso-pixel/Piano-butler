# Her 18 Nov ("예제들 ... 좀 더 잘 보이게 줌인", "다른 예제들도 포함해서"): every pop-up picture is cut to its content (the card's
# white margins and empty space go), so the example fills the frame and reads larger. The question and answer pictures of
# one example share one cut, and every mark on them moves with it.
import json, os, re, numpy as np
from PIL import Image
R2 = '/mnt/user-data/outputs/books/read2/pops/'; PAD = 16
PMF = '/tmp/claude-0/pk/pagemarks.json'; PM = json.load(open(PMF))
P = '/tmp/claude-0/sw/index.html'; h = open(P).read(); i = h.index('const CH = ') + 11; CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ce = i + n1
bases = {}
for f in os.listdir(R2):
    if f.endswith('.webp'): bases.setdefault(re.sub(r'(-q)?\.webp$', '', f), []).append(f)
CUT = {}
for b, fs in sorted(bases.items()):
    box = None; size = None
    for f in fs:
        im = np.asarray(Image.open(R2 + f).convert('L')).astype(int); H, W = im.shape
        if size and size != (W, H): box = None; break
        size = (W, H); ys, xs = np.where(im < 200)
        if not len(xs): continue
        bb = [xs.min(), ys.min(), xs.max(), ys.max()]
        box = bb if box is None else [min(box[0], bb[0]), min(box[1], bb[1]), max(box[2], bb[2]), max(box[3], bb[3])]
    if not box: continue
    W, H = size; x0, y0 = max(0, box[0] - PAD), max(0, box[1] - PAD); x1, y1 = min(W, box[2] + PAD + 1), min(H, box[3] + PAD + 1)
    if (x1 - x0) * (y1 - y0) > .92 * W * H: continue   # nothing to gain
    for f in fs: Image.open(R2 + f).convert('RGB').crop((x0, y0, x1, y1)).save(R2 + f, quality=90)
    CUT[b] = (x0 / W, y0 / H, (x1 - x0) / W, (y1 - y0) / H)
def tr(r, c):
    cx, cy, cw, chh = c; return [round((r[0] - cx) / cw, 4), round((r[1] - cy) / chh, 4), round(r[2] / cw, 4), round(r[3] / chh, 4)]
for b, c in CUT.items():
    e = PM.get('pop:' + b)
    if not e: continue
    for kb in e.get('kbs', []):
        kb['r'] = tr(kb['r'], c)
        for k in kb.get('white', []) + kb.get('black', []): k['r'] = tr(k['r'], c)
    for n in e.get('notes', []): n['r'] = tr(n['r'], c)
moved = 0
for cc in CH:
    for cl in cc.get('clips', []):
        for ln in cl['l']:
            for m in ln.get('mk', []):
                c = CUT.get(m.get('pop'))
                if c and m.get('r'): m['r'] = [tr(r, c) for r in m['r']]; moved += 1
json.dump(PM, open(PMF, 'w')); json.dump(CUT, open('/tmp/claude-0/sw/cuts.json', 'w'))
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:]; open(P, 'w').write(h)
print('pictures cut', len(CUT), '· marks moved', moved)
