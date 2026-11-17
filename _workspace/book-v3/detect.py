# Find the keyboards drawn in a pop-up picture: the outline, the black keys, the white keys between the separators, and
# each white key's letter from the pattern of black keys (two then three). Boxes as fractions of the picture.
import numpy as np
from PIL import Image
NAVY = np.array([38, 41, 107])
PAT = 'CDEFGAB'; HASB = {'C': 1, 'D': 1, 'E': 0, 'F': 1, 'G': 1, 'A': 1, 'B': 0}
def runs(b):
    out, s = [], None
    for i, v in enumerate(b):
        if v and s is None: s = i
        if not v and s is not None: out.append((s, i)); s = None
    if s is not None: out.append((s, len(b)))
    return out
def detect(path):
    im = np.asarray(Image.open(path).convert('RGB')).astype(int); H, W = im.shape[:2]
    navy = (np.abs(im - NAVY).sum(2) < 90)
    # horizontal navy lines at least 150 px long
    lines = []
    for y in range(H):
        for a, b in runs(navy[y]):
            if b - a >= 150: lines.append((y, a, b))
    kbs = []
    used = set()
    for (y0, a0, b0) in lines:
        if (y0, a0) in used: continue
        for (y1, a1, b1) in lines:
            if y1 - y0 < 70 or y1 - y0 > 420 or abs(a1 - a0) > 6 or abs(b1 - b0) > 6: continue
            x0, x1 = min(a0, a1), max(b0, b1); h = y1 - y0
            # vertical outline at both sides
            if navy[y0:y1, x0:x0 + 2].mean() < .8 or navy[y0:y1, x1 - 2:x1].mean() < .8: continue
            # black keys: columns filled navy from the top for at least 40% of the height
            top = navy[y0 + 3:y0 + int(h * .4), x0 + 4:x1 - 4].mean(0) > .95
            blacks = []
            for s, e in runs(top):
                if e - s < 6: continue
                xs, xe = x0 + 4 + s, x0 + 4 + e
                rowfill = navy[y0:y1, xs + 2:xe - 2].mean(1)   # the black key ends where its full width stops being navy
                yb = y0 + 3 + next((k for k, v in enumerate(rowfill[3:]) if v < .8), h)
                blacks.append((xs, y0, xe, yb))
            if not blacks: continue
            yb = max(b[3] for b in blacks)
            band = navy[yb + 4:y1 - 4, x0:x1]
            if band.shape[0] < 8: continue
            sep = band.mean(0) > .6
            cols = [(x0 + (s + e) // 2) for s, e in runs(sep)]
            cols = sorted(set([x0] + cols + [x1]))
            whites = [(cols[k], cols[k + 1]) for k in range(len(cols) - 1) if cols[k + 1] - cols[k] > 12]
            if len(whites) < 3: continue
            # letters from where the black keys sit
            bnd = [whites[k][1] for k in range(len(whites) - 1)]
            has = [any(b[0] < x < b[2] for b in blacks) for x in bnd]
            fits = [s for s in range(7) if all(HASB[PAT[(s + k) % 7]] == has[k] for k in range(len(has)))]
            if len(fits) != 1: continue
            s = fits[0]
            fr = lambda x0_, y0_, x1_, y1_: [round(x0_ / W, 4), round(y0_ / H, 4), round((x1_ - x0_) / W, 4), round((y1_ - y0_) / H, 4)]
            kbs.append({'r': fr(x0, y0, x1, y1), 'white': [{'r': fr(a, y0, b, y1), 'n': PAT[(s + k) % 7]} for k, (a, b) in enumerate(whites)],
                        'black': [{'r': fr(*b)} for b in blacks]})
            used.add((y0, a0)); break
    # keep distinct keyboards (no box inside another)
    out = []
    for kb in kbs:
        if not any(abs(kb['r'][0] - o['r'][0]) < .01 and abs(kb['r'][1] - o['r'][1]) < .03 for o in out): out.append(kb)
    return out
if __name__ == '__main__':
    import sys, json
    for p in sys.argv[1:]:
        k = detect(p); print(p, len(k), [''.join(w['n'] for w in kb['white']) + f" b{len(kb['black'])}" for kb in k])
