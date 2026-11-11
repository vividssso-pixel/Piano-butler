# her 11 Nov: every Handbook "Practise it" box names the real Workbook pages for its chapter (the workbooks were
# reorganised into one Learn + one Use page per chapter, so the old "Workbook Level 0 · Pulse" names no longer exist).
# Runs last in the build, on the generated Handbook HTML.
import re, sys
sys.path.insert(0, '/tmp/claude-0/pk'); import pagemap as PM
H = '/mnt/user-data/outputs/house-rooms/'
BOOK = {'P': 'Pitch', 'T': 'Time', 'E': 'Expression', 'S': 'Scales and keys', 'H': 'Chords and harmony', 'M': 'Chords and harmony', 'F': 'Shape and style', 'L': 'Playing and listening'}
def wbpages(key):
    p, i = key[0], int(key[1:])
    if p == 'S': return str(i)                     # Scales: one page per chapter (1-5)
    if p == 'M': i += 8                            # Harmony in music follows the 8 Chords chapters in the Chords and harmony workbook
    return f'{2 * i - 1}–{2 * i}'
CH = {}
for p, _, n in PM.PARTS:
    for i in range(1, n + 1):
        a, k = PM.pages_of(f'{p}{i}')
        for pg in range(a, a + k): CH[pg] = f'{p}{i}'
def fix(sec):
    m = re.search(r'<div class="foot"><span>(\d+)</span>', sec) or re.search(r'class="foot[^"]*"[^>]*>\s*<span>(\d+)</span>', sec)
    if not m or int(m.group(1)) not in CH: return sec
    key = CH[int(m.group(1))]; pages = wbpages(key)
    ref = f'Workbook p{"p" if "–" in pages else ""}.\u00a0{pages}'   # the workbook of this Part (BOOK); the name is left out so the box stays one line
    def rep(mm):
        body = mm.group(2); on = body.find('Online')
        rest = body[on:] if on >= 0 else ''
        return mm.group(1) + ref + (' · ' + rest if rest else '') + mm.group(3)
    return re.sub(r'(<span class="lab">Practise it</span>)(.*?)(</div>)', rep, sec, flags=re.S)
n = 0
for f in ('handbook-pitch', 'handbook-time2', 'handbook-expression', 'handbook-scales', 'handbook-harmony', 'handbook-harmony2', 'handbook-shape', 'handbook-play'):
    s = open(H + f + '.html').read()
    parts = re.split(r'(?=<section )', s)
    out = ''.join(fix(x) for x in parts); n += out.count('Workbook p')
    open(H + f + '.html', 'w').write(out)
print('wbref', n)
