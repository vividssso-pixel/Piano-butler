# Read & listen for the restructured Handbook (her 16 Nov). Same player as readpage.py; new pages, new narration
# (outputs/audio2), regions measured on the new pages (newregions.json), worked examples shown as pop-ups.
# Before you play (pp. 17-20) keeps its pages, audio and drawings from the live Read & listen.
import json, os, re, glob, shutil, subprocess, sys
sys.path.insert(0, '/tmp/claude-0/pk')
OUT = '/mnt/user-data/outputs/books/read2'; A2 = '/mnt/user-data/outputs/audio2'
os.makedirs(OUT + '/pages', exist_ok=True)
if '--pages' in sys.argv:
    tmp = '/tmp/claude-0/read2pg'; os.makedirs(tmp, exist_ok=True)
    subprocess.run(['pdftoppm', '-jpeg', '-jpegopt', 'quality=80', '-scale-to-x', '1000', '-scale-to-y', '-1', '/mnt/user-data/outputs/pilot/full/handbook-new-draft.pdf', tmp + '/pg'], check=True)
    from PIL import Image
    for f in sorted(glob.glob(tmp + '/pg-*.jpg')):
        n = int(re.search(r'pg-(\d+)', f).group(1)); Image.open(f).save(f'{OUT}/pages/p{n:03d}.webp', 'WEBP', quality=72, method=5)
LAST = max(int(os.path.basename(f)[1:4]) for f in glob.glob(OUT + '/pages/*.webp'))
OLD = open('/mnt/user-data/uploads/Piano Butler/books/read/index.html').read()
OCH = json.loads(re.search(r'const CH = (\[.*?\]); const REG = ', OLD, re.S).group(1))
OREG = json.loads(re.search(r'const REG = (\{.*?\});\n', OLD, re.S).group(1))
NM = json.load(open('/tmp/claude-0/pk/newmap.json'))
PARTNAME = {'pitch': 'Part I · Pitch', 'time': 'Part II · Time', 'expression': 'Part IV · Expression', 'scales': 'Part V · Scales and keys', 'chords': 'Part VI · Chords',
            'harmony': 'Part VII · Harmony in music', 'shape': 'Part VIII · Shape and style', 'play': 'Part IX · Playing and listening', 'further': 'Part X · Going further'}
OPEN = {'I0': 'O1', 'T0': 'O2', 'B0': 'O3', 'IV0': 'O4', 'V0': 'O5', 'VI0': 'O6', 'VII0': 'O7', 'VIII0': 'O8', 'IX0': 'O9', 'X0': 'O10'}
CH = [{'k': 'W', 'part': 'Welcome', 't': 'Welcome', 'pages': [1]}] + [c for c in OCH if c['k'] in ('GD', 'B1')]
for c in CH:   # the old Before-you-play key B1 now belongs to Bar lines: rename it BP, with its own audio folder
    if c['k'] == 'B1' and c['part'] == 'Before you play':
        c['k'] = 'BP'
        for k in c.get('clips', []): k['src'] = k['f']; k['f'] = k['f'].replace('audio/B1/', 'audio/BP/')
for part, pp in NM.items():
    for x in pp:
        k = x['k']; pn = PARTNAME[part] if not k.startswith('B') else 'Part III · Bars and repeats'
        if x['h1']:
            if k in OPEN: CH.append({'k': OPEN[k], 'part': pn, 't': 'Part opener', 'pages': [x['pg']]})
            else: CH.append({'k': k, 'part': pn, 't': f"{re.sub(r'[A-Z]+', '', k)} · {x['h1']}", 'pages': [x['pg']]})
        else: CH[-1]['pages'].append(x['pg'])
CH.append({'k': 'GL', 'part': 'At the end', 't': 'Glossary and index', 'pages': list(range(CH[-1]['pages'][-1] + 1, LAST + 1))})
POPS = set(os.path.basename(f)[:-5] for f in glob.glob(OUT + '/pops/*.webp'))
for c in CH:
    if c['k'] in ('GD', 'BP'):   # unchanged pages: their clips and drawings come from the live build
        if c['k'] == 'BP' and c.get('clips'):   # clip 1 re-recorded: the box is called Remember now
            m = json.load(open(f'{A2}/BP1/clips.json'))['clips'][0]; k0 = c['clips'][0]
            os.makedirs(f'{OUT}/audio/BP', exist_ok=True); shutil.copy(f'{A2}/BP1/{m["file"]}', f'{OUT}/audio/BP/01-before-you-play.mp3')
            k0.pop('src', None); k0['s'] = m['sec']; k0['l'] = m['lines']; c['clips'] = [k0] + c['clips'][1:]
        for k in c.get('clips', [])[(1 if c['k'] == 'BP' else 0):]:
            src = '/mnt/user-data/outputs/audio/' + k.pop('src', k['f'])[len('audio/'):]
            os.makedirs(os.path.dirname(f'{OUT}/{k["f"]}'), exist_ok=True)
            if os.path.exists(src): shutil.copy(src, f'{OUT}/{k["f"]}')
        continue
    j = f'{A2}/{c["k"]}/clips.json'
    if not os.path.exists(j): continue
    meta = json.load(open(j)); d = f'{OUT}/audio/{c["k"]}'; os.makedirs(d, exist_ok=True); c['clips'] = []
    for m in meta['clips']:
        shutil.copy(f'{A2}/{c["k"]}/{m["file"]}', d)
        L = m['lines']; ask = True
        for ln in L:   # a worked example: the question picture until the pause is over, then the answer
            r = (ln.get('cue') or {}).get('r', '')
            if r.startswith('pop'):
                base = f'{c["k"]}-{r[3:]}'; q = base + '-q'
                ln['lens'] = {'k': 'pop', 'src': f'pops/{q if ask and q in POPS else base}.webp'}
            if ln.get('who') == 'pause': ask = False
        pg = sorted({ln['cue']['p'] for ln in L if ln.get('cue')}) or c['pages']
        c['clips'].append({'t': m['title'], 'f': f'audio/{c["k"]}/{m["file"]}', 's': m['sec'], 'p': pg[0], 'l': L})
os.makedirs(OUT + '/pops', exist_ok=True)
RG = json.load(open('/tmp/claude-0/pk/newregions.json'))
REG = {pg: {k: {'b': b, 'l': [], 'r': None} for k, b in v.items()} for pg, v in RG.items()}
# Cues were written against the chapter's planned pages; the final layout can move a section to the other page.
# Point each cue at the page that really holds it: a clip named after a section goes to that heading; any other
# region is looked up across the chapter's pages.
def _w(t): return {w for w in re.findall(r'[a-z0-9]+', t.lower()) if len(w) > 2 and w not in ('the', 'and', 'example', 'try')}
for c in CH:
    if c['k'] in ('GD', 'BP') or not c.get('clips'): continue
    heads = [(pg, k) for pg in c['pages'] for k in REG.get(str(pg), {}) if k.startswith('h:')]
    for clip in c['clips']:
        tw = _w(clip['t']); best = max(heads, key=lambda h: len(tw & _w(h[1][2:])), default=None)
        hit = best if best and tw and len(tw & _w(best[1][2:])) >= max(1, len(tw) // 2) else None
        for ln in clip['l']:
            cu = ln.get('cue')
            if not cu or cu['r'].startswith('pop'): continue
            if hit and cu['r'] == 'more': cu['p'], cu['r'] = hit
            elif cu['r'] not in REG.get(str(cu['p']), {}):
                alt = [pg for pg in c['pages'] if cu['r'] in REG.get(str(pg), {})]
                if alt: cu['p'] = alt[0]
                elif str(cu['p']) not in map(str, c['pages']): cu['p'] = c['pages'][0]
            if cu['r'] not in REG.get(str(cu['p']), {}):   # e.g. cards rather than a table: the nearest thing on the page
                cu['r'] = next((k for k in ('picture', 'more', 'body') if k in REG.get(str(cu['p']), {})), cu['r'])
        clip['p'] = next((ln['cue']['p'] for ln in clip['l'] if ln.get('cue')), clip['p'])
for pg in ('17', '18', '19', '20'):
    if pg in OREG: REG[pg] = OREG[pg]
# her 16 Nov: fine marks (words, keys, black keys) on the chapters measured so far (pagemarks.json)
import sys as _s; _s.path.insert(0, '/tmp/claude-0/tts'); import importlib as _il
from marks import line_marks, phrase_spans, PM as _PM
import scripts_new as _SN
MARKED = {'P1'}
for c in CH:
    if c['k'] not in MARKED or not c.get('clips'): continue
    sc = _SN.CH[c['k']][1]
    for ci_, cl in enumerate(c['clips']):
        specs = [t for who, t, *_ in sc[ci_][1] if who == 'piano'] if ci_ < len(sc) and isinstance(sc[ci_][1], list) else []
        k = 0; asked = any(l.get('who') == 'pause' for l in cl['l']); answered = not asked
        for ln in cl['l']:
            spec = None
            if ln.get('who') == 'pause': answered = True
            if ln.get('who') == 'piano' and k < len(specs): spec = specs[k]; k += 1
            mk = line_marks(ln, spec=spec, REG=REG, audio=OUT + '/' + cl['f'], answered=answered)
            if mk: ln['mk'] = mk
            sp = phrase_spans(ln, OUT + '/' + cl['f'])
            if sp and len(sp) > 1: ln['sp'] = sp

for f in ('pen.js', 'warm.js'):
    s = '/mnt/user-data/uploads/Piano Butler/books/read/' + f
    if os.path.exists(s): shutil.copy(s, OUT)
src = open('/tmp/claude-0/pk/readpage.py').read()
HTML = re.search(r"HTML = r'''(.*?)'''\nopen\(OUT", src, re.S).group(1)
POPJS = "  if (L.k === 'pop') { if (lensEl.dataset.k !== L.src) { lensEl.dataset.k = L.src; lensEl.dataset.t = ''; lensEl.innerHTML = `<div class=\"lens popl\"><img src=\"${L.src}\" alt=\"Worked example\" style=\"width:100%;height:auto;display:block\"></div>`; } return; }\n"
HTML = HTML.replace("  if (L.k === 'auto') return drawAuto(L, t);", POPJS + "  if (L.k === 'auto') return drawAuto(L, t);", 1)
HTML = HTML.replace("#lens .penl{", "#lens .popl{width:94%;max-width:720px;padding:6px} #lens .penl{", 1)
HTML = HTML.replace("'P1'));", "'W'));", 1)
assert 'k === \'pop\'' in HTML
from marks_player import splice as _splice; HTML = _splice(HTML)
from bust import bust   # her 16 Nov: ?v= on every asset so a rebuild shows at once
open(OUT + '/index.html', 'w').write(bust(HTML.replace('__DATA__', json.dumps(CH, ensure_ascii=False)).replace('__REG__', json.dumps(REG, ensure_ascii=False))))
print('read2:', len(CH), 'sections,', sum(1 for c in CH if c.get('clips')), 'with audio, last page', LAST)
