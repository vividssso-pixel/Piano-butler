# Fit a page's lines as big as they go (her 7 Nov: notes big, but one page): for one lesson, the jobs starting with a
# prefix get the smallest spacing (sl) for which their page still has no overflow, no clash and no alignment problem.
# Usage: python3 fit.py song prefix page [lo hi]
import json, subprocess, sys
s, pre, pg = sys.argv[1], sys.argv[2], int(sys.argv[3])
lo, hi = (float(sys.argv[4]), float(sys.argv[5])) if len(sys.argv) > 5 else (0.02, 2.0)
MODE = sys.argv[6] if len(sys.argv) > 6 else 'scale'   # scale: the lines' width on the page (1 = full); sl: Verovio's spacing
def set_sl(v):
    d = json.load(open(s + '.json'))
    for k in d['jobs']:
        if k.startswith(pre):
            if MODE == 'sl': d['jobs'][k][2]['sl'] = round(v, 3)
            else: d.setdefault('scale', {})[k] = round(v, 3)
    json.dump(d, open(s + '.json', 'w'), ensure_ascii=False, indent=0)
def ok(v):
    set_sl(v); out = subprocess.run(['bash', 'build.sh', s], capture_output=True, text=True).stdout
    over = json.loads(out.split('over ')[1].split(']')[0] + ']')
    clash = ' 0 clashes' in out
    al = subprocess.run(['node', 'align.js', f'{subprocess.os.getcwd()}/lesson-{s}.html'], capture_output=True, text=True).stdout
    bad = [l for l in al.splitlines() if l.startswith(f'p{pg} ') and l.split()[1].startswith(pre)]
    return over[pg - 1] == 0 and clash and not bad, over, bad[:2]
good = None
if MODE == 'sl':
    if ok(lo)[0]: good = lo
    else:
        for _ in range(7):
            md = (lo + hi) / 2; r = ok(md)
            if r[0]: good, hi = md, md
            else: lo = md
    if good is None: good = hi
else:   # the widest that fits
    lo, hi = (float(sys.argv[4]), float(sys.argv[5])) if len(sys.argv) > 5 else (0.4, 1.0)
    if ok(hi)[0]: good = hi
    else:
        for _ in range(6):
            md = (lo + hi) / 2; r = ok(md)
            if r[0]: good, lo = md, md
            else: hi = md
    if good is None: good = lo
r = ok(good); print(s, pre, MODE, round(good, 3), 'fits' if r[0] else 'NOT FIT', r[1], r[2])
