# "Read & listen" (her 8 Nov): the Handbook online, page by page, with the Butler's audio for each chapter that has it.
# Writes /mnt/user-data/outputs/books/read/ : index.html, pages/pNNN.webp (from the merged Handbook PDF), audio/<key>/ clips.
import json, os, glob, shutil, subprocess, sys
sys.path.insert(0, '/tmp/claude-0/pk'); import pagemap as PM, openart as OA, checkbank as CB
OUT = '/mnt/user-data/outputs/books/read'
os.makedirs(OUT + '/pages', exist_ok=True)
if '--pages' in sys.argv:   # re-render the page images from the merged PDF (pdf page + 20 = printed page)
    tmp = '/tmp/claude-0/read/pages'; os.makedirs(tmp, exist_ok=True)
    for f in glob.glob(tmp + '/*'): os.remove(f)
    subprocess.run(['pdftoppm', '-jpeg', '-jpegopt', 'quality=72', '-scale-to-x', '1000', '-scale-to-y', '-1', '/mnt/user-data/outputs/books/handbook-draft.pdf', tmp + '/pg'], check=True)
    from PIL import Image
    for f in sorted(glob.glob(tmp + '/pg-*.jpg')):
        n = int(os.path.basename(f)[3:6]) + 20; Image.open(f).save(f'{OUT}/pages/p{n:03d}.webp', 'WEBP', quality=70, method=5)
else:
    for f in glob.glob('/tmp/claude-0/read/pages/*.webp'): shutil.copy(f, OUT + '/pages/')
LAST = max(int(os.path.basename(f)[1:4]) for f in glob.glob(OUT + '/pages/*.webp'))
TIPS = {L[-1][3]: L[-1][1] for L in (OA.LEG_P, OA.LEG_T, OA.LEG_E, OA.LEG_S, OA.LEG_H, OA.LEG_M, OA.LEG_F, OA.LEG_L)}
PNAME = dict(CB.PARTS)
CH = []
for p, name, k in PM.PARTS:
    part = PNAME[p]
    CH.append({'k': p + 'O', 'part': part, 't': 'Opening map', 'pages': [PM.PAGE[p + 'O']]})
    for i in range(1, k + 1):
        key = f'{p}{i}'; a, n = PM.pages_of(key)
        CH.append({'k': key, 'part': part, 't': f'{i} · {CB.TITLES[key]}', 'pages': list(range(a, a + n))})
    CH.append({'k': p + 'T', 'part': part, 't': TIPS[p + 'T'], 'pages': [PM.PAGE[p + 'T']]})
CH.append({'k': 'X', 'part': 'At the end', 't': 'Putting it together', 'pages': [PM.PAGE['X'], PM.PAGE['X'] + 1]})
CH.append({'k': 'GL', 'part': 'At the end', 't': 'Glossary and index', 'pages': list(range(PM.PAGE['X'] + 2, LAST + 1))})
# audio: clips.json per chapter; clip 1 sits on the chapter's first page, the last on its last page, the rest on page 2
for c in CH:
    j = f'/mnt/user-data/outputs/audio/{c["k"]}/clips.json'
    if not os.path.exists(j): continue
    meta = json.load(open(j)); d = f'{OUT}/audio/{c["k"]}'; os.makedirs(d, exist_ok=True)
    n = len(meta['clips']); pg = c['pages']
    c['clips'] = []
    for i, m in enumerate(meta['clips']):
        shutil.copy(f'/mnt/user-data/outputs/audio/{c["k"]}/{m["file"]}', d)
        at = pg[0] if i == 0 else (pg[-1] if i == n - 1 else pg[min(1, len(pg) - 1)])
        c['clips'].append({'t': m['title'], 'f': f'audio/{c["k"]}/{m["file"]}', 's': m['sec'], 'p': at, 'l': m.get('lines', [])})
RG = json.load(open('/tmp/claude-0/pk/regions.json')) if os.path.exists('/tmp/claude-0/pk/regions.json') else {}
REG = {}
for c in CH:
    for k in c.get('clips', []):
        for ln in k['l']:
            pg = str(ln.get('cue', {}).get('p', ''))
            if pg and pg in RG and pg not in REG:
                seen = {}; REG[pg] = {}
                for b in RG[pg]:
                    seen[b['key']] = seen.get(b['key'], 0) + 1; key = b['key'] + (str(seen[b['key']]) if seen[b['key']] > 1 else '')
                    REG[pg][key] = {'b': b['box'], 'l': b['labs'], 'r': b.get('res')}
# her 8 Nov: as each term is spoken, mark its key on the page there and then. Kokoro gives no word timings, so a term's
# moment is estimated from where it sits in the line (speech runs evenly enough over a short sentence).
import re as _re
_LAST = {}
_ALIAS = {'♯': ['sharp'], '♭': ['flat'], '♮': ['natural'], '2nd': ['second'], '3rd': ['third'], '4th': ['fourth'], '5th': ['fifth'], '6th': ['sixth'], '7th': ['seventh'], '8ve': ['octave'], 'unison': ['unison'],
          'melodic': ['melodic'], 'harmonic': ['harmonic'], 'Treble clef': ['treble clef'], 'Bass clef': ['bass clef']}
def _spoken(nm):   # how a label is said aloud: 'F♯' -> 'F sharp', '3rd' -> 'third'
    out = [nm] if _re.search('[A-Z]', nm) and nm != '?' else []
    m = _re.match(r'^([A-G])([♯♭♮])$', nm)
    if m: out.append(m.group(1) + {'♯': ' sharp', '♭': ' flat', '♮': ' natural'}[m.group(2)])
    return out + _ALIAS.get(nm, [])
def _hits(ln):   # her 8 Nov: every key, note or sign the voice names is marked the moment it is said, anywhere on the page
    c = ln.get('cue') or {}; page = REG.get(str(c.get('p', ''))) or {}; text = ln.get('text') or ''
    if not page or not text or ln.get('who') not in ('B', 'P', 'Q', 'K') or str(c.get('r', '')).startswith('ex'): return []
    order = [c.get('r')] + [k for k in page if k != c.get('r') and not k.startswith('ex') and k in page]
    used = [False] * len(text); out = []
    for rk in order:
        reg = page.get(rk)
        if not reg: continue
        names = sorted({(sp, L[0]) for L in reg['l'] for sp in _spoken(L[0]) if rk == c.get('r') or len(sp) > 2}, key=lambda x: len(x[0]), reverse=True)   # single letters only in the picture being talked about
        for sp, nm in names:
            for m in _re.finditer(r'(?<![A-Za-z])' + _re.escape(sp) + r'(?![A-Za-z0-9])', text):
                if any(used[m.start():m.end()]): continue
                if sp == 'A':   # the article "A" opens a sentence and is followed by a lower-case word
                    pre = text[:m.start()].rstrip()
                    if (pre == '' or pre[-1] in '.!?') and _re.match(r'A [a-z]', text[m.start():]): continue
                for q in range(m.start(), m.end()): used[q] = True
                out.append((m.start(), m.end(), nm, rk))
    out.sort(); d = max(0.3, ln['t1'] - ln['t0'] - 0.35); L = max(1, len(text))
    cx = lambda rk, i: page[rk]['l'][i][1][0] + page[rk]['l'][i][1][2] / 2
    occ = [[i for i, x in enumerate(page[rk]['l']) if x[0] == nm] for _, _, nm, rk in out]
    pick = [o[0] if len(o) == 1 else None for o in occ]
    for n in range(len(out)):   # a repeated name: take the one nearest its neighbours in the same picture
        if pick[n] is None:
            rk = out[n][3]
            near = [pick[m] for m in sorted(range(len(out)), key=lambda m: abs(m - n)) if m != n and pick[m] is not None and out[m][3] == rk]
            ref = cx(rk, near[0]) if near else _LAST.get((c.get('p'), rk))
            pick[n] = min(occ[n], key=lambda i: abs(cx(rk, i) - ref)) if ref is not None else occ[n][0]
    for n in range(len(out)): _LAST[(c.get('p'), out[n][3])] = cx(out[n][3], pick[n])
    return [[round(ln['t0'] + d * a / L - 0.12, 2), '#' + str(pick[n]), a, b, rk] for n, (a, b, nm, rk) in enumerate(out)]
for c in CH:
    for k in c.get('clips', []):
        for ln in k['l']:
            h = _hits(ln)
            if h: ln['hits'] = h
# her 8 Nov (p. 32): as each letter is said, a lens over the page shows that staff large, lighting line 1, line 2 ... in turn.
exec(open('/tmp/claude-0/pk/seg.py').read().replace('def segs', 'def _segs'))
LENS = {'tl': 'EGBDF', 'ts': 'FACE', 'bl': 'GBDFA', 'bs': 'ACEG', 'tb': 'CBA', 'ta': 'ABC', 'bb': 'EDC', 'ba': 'CDE'}
for c in CH:
    for k in c.get('clips', []):
        prev = None
        for ln in k['l']:
            lk = (ln.get('cue') or {}).get('lens')
            if lk and ln.get('who') == 'piano':   # the notes played light up one by one
                ln['lens'] = {'k': lk, 'at': [round(v - 0.03, 2) for v in ln.get('notes', [])][:len(LENS[lk])], 'full': True}
            elif lk:
                text = ln.get('text') or ''; want = LENS[lk]; at = []; pos = 0
                toks = [(m.start(), m.group(0)) for m in _re.finditer(r'\b[A-Z][a-z]*', text)]
                for ch in want:
                    nx = next(((a, w) for a, w in toks if a >= pos and w[0] == ch), None)
                    if not nx: at = []; break
                    at.append(nx[0]); pos = nx[0] + 1
                if 'Line one' in text: at = [m.start() for m in _re.finditer(r'Line \w+', text)]   # light line 1 as "Line one" is said
                sg = _segs(OUT + '/' + k['f'], ln['t0'], ln['t1'])   # the real speech span, with pauses weighted at commas and stops
                s0, s1 = (sg[0][0], sg[-1][1]) if sg else (ln['t0'], ln['t1'] - 0.35)
                wt = [1 + (4 if ch == ',' else 7 if ch in '.:!?' else 0) for ch in text]; cum = [0]
                for w_ in wt: cum.append(cum[-1] + w_)
                def tm(a):
                    return s0 + (s1 - s0) * cum[a] / cum[-1] - 0.08
                ln['lens'] = {'k': lk, 'at': [round(tm(a), 2) for a in at], 'full': prev == lk}
                ln.pop('hits', None)
            prev = lk
for c in CH:   # her 9 Nov: fold the grand staff at Middle C and the two notes meet, like a decalcomania
    for k in c.get('clips', []):
        for ln in k['l']:
            m = (ln.get('cue') or {}).get('mirror')
            if m: ln['lens'] = {'k': 'mirror', 'm': m, 'at': [], 'full': True}; ln.pop('hits', None)
# her 9 Nov: "apply it everywhere you can". Every piano phrase in Pitch gets a lens: the notes on the staff and their keys
# below, lit one by one as they sound. Not in Examples before the answer (it would give it away), not in Time (rhythm, not pitch).
sys.path.insert(0, '/tmp/claude-0/tts'); import importlib; _S = importlib.import_module('scripts')
# Time chapters: a rhythm lens. The beats in boxes (1 2 3 …, beat one strongest), the notes above in real note values,
# each with a bar showing how long it lasts; the current beat and note light up as they sound.
def _durs(tok):
    m = _re.match(r'(.+?)(?:([/*@])(\d+(?:\.\d+)?))?$', tok.rstrip('~')); n_, op, v = m.group(1), m.group(2), m.group(3)
    return n_, .62 * (1 / float(v) if op == '/' else float(v) if op == '*' else (60 / float(v)) / .62 if op == '@' else 1)
for c in CH:
    if c['k'] not in _S.CH or not c['k'].startswith('T'): continue
    sc = [ls for _, ls in _S.CH[c['k']][1]]
    for k, sl in zip(c.get('clips', []), sc):
        if len(sl) != len(k['l']): print('rhythm lens: line mismatch', c['k'], k['t']); continue
        for ln, src in zip(k['l'], sl):
            cue = ln.get('cue') or {}
            if ln.get('who') != 'piano' or src[0] not in ('count', 'piano'): continue
            if str(cue.get('r', '')).startswith('ex') and not cue.get('reveal'): continue
            if src[0] == 'count': bt, nt, say = src[1]['beats'].split(), (src[1].get('notes') or '').split(), (src[1].get('say') or '').split()
            else:
                toks = src[1].split()
                if not all(_durs(x)[0] in ('X', 'M', 'x') for x in toks): continue   # a tune, not a beat
                bt, nt, say = toks, [], []
            on = [i for i, x in enumerate(bt) if _durs(x)[0] != 'R']   # 'R' between clicks = the "&" halfway
            cum = [0.0]
            for x in bt: cum.append(cum[-1] + _durs(x)[1])
            bsec = (cum[on[1]] - cum[on[0]]) if len(on) > 1 else _durs(bt[0])[1]
            beats = []; ands = []; num = 0
            for i, x in enumerate(bt):
                lv = _durs(x)[0]; w = say[i] if i < len(say) else ''
                if lv == 'R': ands.append([round(ln['t0'] + cum[i] - .03, 2), round(cum[i] / bsec, 3), w or '&']); continue
                num = 1 if lv == 'X' or not beats else num + 1
                beats.append([round(ln['t0'] + cum[i] - .03, 2), lv, w or str(num), round(cum[i] / bsec, 3)])
            notes = []; t_ = ln['t0']; pos = 0.0
            for x in nt:
                nm, sec = _durs(x); d = round(sec / bsec, 3)
                notes.append([round(t_ - .03, 2), round(pos, 3), d, 1 if nm == 'R' else 0, 1 if x.endswith('~') else 0]); t_ += sec; pos += d
            bars = [b[3] for b in beats if b[1] == 'X'] or [0]
            ln['lens'] = {'k': 'rhy', 'beats': beats, 'ands': ands, 'notes': notes, 'bars': bars, 'n': round(cum[-1] / bsec, 3), 'at': [b[0] for b in beats], 'full': True}
for c in CH:
    if c['k'] not in _S.CH or not c['k'].startswith('P'): continue
    sc = [ls for _, ls in _S.CH[c['k']][1]]
    for k, sl in zip(c.get('clips', []), sc):
        if len(sl) != len(k['l']): print('lens: line mismatch', c['k'], k['t']); continue
        for ln, src in zip(k['l'], sl):
            cue = ln.get('cue') or {}
            if ln.get('who') != 'piano' or ln.get('lens') or src[0] != 'piano': continue
            if str(cue.get('r', '')).startswith('ex') and not cue.get('reveal'): continue
            allt = _re.findall(r'\[[^\]]+\]|\S+', src[1]); bars = []; bn = 0
            for t_ in allt:
                if t_ == '|': bn += 1
                else: bars.append(bn)
            toks = [t_ for t_ in allt if t_ != '|']
            items = []
            for tok, tt, br in zip(toks, ln.get('notes', []), bars):
                ns = tok[1:-1].split() if tok.startswith('[') else [_re.sub(r'[/*@]\d+$', '', tok)]
                ns = [n_ for n_ in ns if _re.match(r'^[A-G][#b]?\d$', n_)]
                if ns: items.append([ns, round(tt - 0.03, 2), br])
            if items: ln['lens'] = {'k': 'auto', 'items': [x[0] for x in items], 'at': [x[1] for x in items], 'bar': [x[2] for x in items], 'kb': c['k'] == 'P1', 'full': True}   # chapter 1 comes before the staff: keys only
PRACT = {   # chapter: (workbook pages in the merged workbook draft, [(drill id, drill name, extra query)])
    'P1': ((1, 2), [('first-steps', 'Keyboard Patterns', ''), ('note-names', 'The Musical Alphabet', '')]),
    'P2': ((3, 4), [('staff', 'The Staff & the Two Clefs', '')]),
    'P3': ((5, 6), [('staff', 'The Staff & the Two Clefs', ''), ('whole-staff', 'Line and Space Names', '')]),
    'P4': ((7, 8), [('whole-staff', 'Line and Space Names', ''), ('reading-steps', 'Steps & Skips', '')]),
    'P5': ((9, 10), [('ledger-lines', 'Ledger Lines', '')]),
    'P6': ((11, 12), [('accidentals', 'Accidentals', ''), ('tones', 'Tones & Semitones', '')]),
    'P7': ((13, 14), [('intervals', 'Intervals', ''), ('tones', 'Tones & Semitones', '')]),
    'P8': ((15, 16), [('intervals', 'Intervals', '')]),
}
for c in CH:
    if c['k'] in PRACT: c['pr'] = PRACT[c['k']]
DATA = json.dumps(CH, ensure_ascii=False)
REGD = json.dumps(REG, ensure_ascii=False)
HTML = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex">
<title>Read and Listen</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Playfair+Display:wght@700;800&display=swap">
<style>
/* Layout: a reading desk. The page fills the left; the Butler's clips sit beside it (below it on a phone). */
:root{--bg:#f3f1ea;--panel:#ffffff;--ink:#26296b;--soft:#5a5d8f;--line:#e3e1ee;--accent:#e4572e;--accentbg:#fdece5;--paper:#ffffff;
 --display:'Playfair Display',Georgia,serif;--body:'Atkinson Hyperlegible',system-ui,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#14153a;--panel:#1e2050;--ink:#eceefe;--soft:#b3b5dc;--line:#33366e;--accent:#ff7a52;--accentbg:#3a2620;--paper:#f7f6f1;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#14153a;--panel:#1e2050;--ink:#eceefe;--soft:#b3b5dc;--line:#33366e;--accent:#ff7a52;--accentbg:#3a2620;--paper:#f7f6f1;color-scheme:dark}
html,body{margin:0}
body{background:var(--bg);color:var(--ink);font-family:var(--body);font-size:16px;line-height:1.45;padding-top:env(safe-area-inset-top,0px)}
.top{display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px;padding-block:14px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));border-bottom:1px solid var(--line);background:var(--panel)}
.brand{font-family:var(--display);font-weight:800;font-size:20px;margin-right:auto}
.brand small{display:block;font-family:var(--body);font-weight:700;font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
select{font:inherit;font-size:15px;color:var(--ink);background:var(--panel);border:1.5px solid var(--line);border-radius:10px;padding:8px 10px;max-width:100%}
.desk{display:grid;grid-template-columns:minmax(0,1fr) 320px;gap:18px;max-width:1180px;margin:0 auto;padding-block:16px 40px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
@media (max-width:880px){.desk{grid-template-columns:minmax(0,1fr)}}
.reader{min-width:0;width:100%;max-width:calc((100vh - 190px) / 1.414);justify-self:center} @media (max-width:880px){.reader{max-width:100%}}
.sheet{background:var(--paper);border-radius:4px;box-shadow:0 2px 10px rgba(20,22,60,.12);overflow:hidden;aspect-ratio:210/297;max-width:100%;display:flex;align-items:center;justify-content:center}
.sheet{position:relative} .stage{position:relative;width:100%;transform-origin:0 0;transition:transform .6s ease}
.sheet img{width:100%;height:auto;display:block}
.hl{position:absolute;border:3px solid var(--accent);border-radius:8px;box-shadow:0 0 0 9999px rgba(20,22,60,.18);} .hl.fog{box-shadow:0 0 0 9999px rgba(246,245,240,.94)} .cov{position:absolute;background:#fff;border-radius:3px;pointer-events:none} .cov.res{background:#fff7f3;border:1.5px dashed #e4572e;display:flex;align-items:center;justify-content:center;font:700 clamp(9px,1.4vw,14px) var(--body);color:#e4572e} .hl{transition:all .5s ease;pointer-events:none}
.sub mark,#sub mark{background:#fde3d8;color:#26296b;border-radius:3px;padding:0 2px} .mk{position:absolute;width:3.2%;aspect-ratio:1;border-radius:50%;border:3px solid var(--accent);background:rgba(228,87,46,.25);transform:translate(-50%,-50%);pointer-events:none;animation:pop .35s ease}
@keyframes pop{from{transform:translate(-50%,-50%) scale(.4);opacity:0}to{transform:translate(-50%,-50%) scale(1);opacity:1}}
.sub{min-height:3.2em;margin-top:10px;background:var(--panel);border:1.5px solid var(--line);border-radius:12px;padding:8px 12px;font-size:15.5px}
.sub b{color:var(--accent);margin-right:6px} .sub:empty{display:none}
.ctl{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:0 0 10px} .ctl .btn{padding:6px 12px;font-size:14px} .ctl .sp{font-size:12.5px;padding:4px 7px;border-radius:999px} .ctl .sp.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.prac{margin-top:12px;border:1.5px solid var(--line);border-radius:12px;padding:10px 12px;display:flex;flex-direction:column;gap:6px} .prac .ph{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)} .prac a{display:block;font-weight:700;font-size:14.5px;color:var(--ink);text-decoration:none;border:1.5px solid var(--line);border-radius:9px;padding:7px 10px;background:var(--bg)} .prac a.dr{border-color:var(--accent)} .prac a:hover{border-color:var(--accent)}
#lens:not(:empty){position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(246,245,240,.82);z-index:3;pointer-events:none}   /* her 9 Nov: one place to look - the lens in the middle, the page faded behind */
.lens{position:relative;width:90%;background:#fff;border:4px solid var(--accent);border-radius:22px;box-shadow:0 10px 30px rgba(20,22,60,.28);padding:6px 10px 2px;animation:lz .35s ease;z-index:3;pointer-events:none} .lens .lh{display:flex;align-items:center;gap:6px;font:700 clamp(10px,1.6vw,14px) var(--body);letter-spacing:.12em;text-transform:uppercase;color:#e4572e} .lens svg{display:block;width:100%;height:auto}
#lens .fold{opacity:.55;animation:fold 1.8s ease-in-out .5s forwards} #lens .meet{animation:meet .5s ease 2.3s forwards}
@keyframes fold{from{transform:scaleY(1)}to{transform:scaleY(-1)}} @keyframes meet{to{opacity:1}}
@keyframes lz{from{transform:scale(.85);opacity:0}to{transform:scale(1);opacity:1}}
.follow{display:flex;align-items:center;gap:8px;font-size:14px;color:var(--soft);margin-top:8px}
.nav{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:10px}
button{font:inherit;cursor:pointer;color:var(--ink)}
.btn{background:var(--panel);border:1.5px solid var(--line);border-radius:10px;padding:8px 14px;font-weight:700}
.btn:disabled{opacity:.4;cursor:default}
.pgno{font-variant-numeric:tabular-nums;color:var(--soft);font-size:14px}
button:focus-visible,select:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.side{background:var(--panel);border:1.5px solid var(--line);border-radius:14px;padding:14px;align-self:start;position:sticky;top:12px}
.side h2{font-family:var(--display);font-size:22px;margin:0 0 2px;text-wrap:balance}
.kick{font-size:11px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.play{display:flex;align-items:center;gap:10px;width:100%;background:var(--accent);color:#fff;border:0;border-radius:12px;padding:11px 14px;font-weight:700;margin:12px 0 8px}
.play svg{flex:none}
.clips{display:grid;gap:6px}
.clip{display:grid;grid-template-columns:26px 1fr auto;align-items:center;gap:8px;text-align:left;background:transparent;border:1.5px solid var(--line);border-radius:10px;padding:8px 10px}
.clip .n{width:24px;height:24px;border-radius:50%;border:1.5px solid var(--soft);display:inline-flex;align-items:center;justify-content:center;font-size:12px;font-weight:700}
.clip .s{font-size:12.5px;color:var(--soft);font-variant-numeric:tabular-nums}
.clip.on{border-color:var(--accent);background:var(--accentbg)} .clip.on .n{background:var(--accent);border-color:var(--accent);color:#fff}
audio{width:100%;margin-top:10px}
.none{color:var(--soft);font-size:14.5px;margin:10px 0 0}
.who{font-size:13px;color:var(--soft);margin-top:12px;border-top:1px solid var(--line);padding-top:10px}
@media (prefers-reduced-motion:reduce){*{scroll-behavior:auto} .stage,.hl{transition:none}}
</style></head><body>
<header class="top"><div class="brand"><small>The Piano Butler Handbook</small>Read and listen</div><label class="sr" for="ch" style="position:absolute;left:-9999px">Chapter</label><select id="ch"></select></header>
<main class="desk">
 <section class="reader"><a class="sheet" id="zoom" target="_blank" rel="noopener" title="Open the page full size"><div class="stage" id="stage"><img id="img" alt=""><div id="ov"></div></div><div id="lens"></div></a><div class="sub" id="sub"></div>
  <div class="nav"><button class="btn" id="prev">‹ Page</button><span class="pgno" id="pgno"></span><button class="btn" id="next">Page ›</button></div></section>
 <aside class="side" id="side"></aside>
</main>
<script>
const CH = __DATA__; const REG = __REG__;
const sel = document.getElementById('ch'), img = document.getElementById('img'), side = document.getElementById('side');
let ci = 0, pi = 0, playing = -1, chain = false, rate = 1;
const audio = new Audio(); audio.preload = 'none';
const parts = [...new Set(CH.map(c => c.part))];
sel.innerHTML = parts.map(p => `<optgroup label="${p}">` + CH.map((c, i) => c.part === p ? `<option value="${i}">${c.t}${c.clips ? ' ♪' : ''}</option>` : '').join('') + '</optgroup>').join('');
const pad = n => String(n).padStart(3, '0');
function showPage() {
  const c = CH[ci], n = c.pages[pi];
  img.src = `pages/p${pad(n)}.webp`; document.getElementById('zoom').href = img.src; img.alt = `Handbook page ${n}`;
  document.getElementById('pgno').textContent = `p. ${n} · ${pi + 1} of ${c.pages.length}`;
  document.getElementById('prev').disabled = ci === 0 && pi === 0; document.getElementById('next').disabled = ci === CH.length - 1 && pi === c.pages.length - 1;
  const nx = CH[ci + 1]; if (nx) { const im = new Image(); im.src = `pages/p${pad(nx.pages[0])}.webp`; }
}
function site(p) { const local = location.protocol === 'file:' || /thepianobutler\.com$/.test(location.hostname); return (local ? '../../' : 'https://thepianobutler.com/') + p; }
function drawSide() {
  const c = CH[ci];
  side.innerHTML = `<div class="kick">${c.part}</div><h2>${c.t}</h2>` + (c.clips ? `<button class="play" id="all"><svg width="18" height="18" viewBox="0 0 18 18"><path d="M4 2l12 7-12 7z" fill="currentColor"/></svg>${playing >= 0 ? 'Playing…' : 'Listen to the whole chapter'}</button><div class="ctl"><button class="btn" id="pp">${audio.paused ? '▶ Resume' : '❚❚ Pause'}</button>${[0.8, 1, 1.2, 1.5].map(v => `<button class="btn sp${v === rate ? ' on' : ''}" data-v="${v}">${v}×</button>`).join('')}</div><div class="clips">` +
    c.clips.map((k, i) => `<button class="clip${i === playing ? ' on' : ''}" data-i="${i}"><span class="n">${i + 1}</span><span>${k.t}</span><span class="s">${Math.floor(k.s / 60)}:${String(k.s % 60).padStart(2, '0')}</span></button>`).join('') + '</div>'
    : `<p class="none">No audio for this chapter yet. The pages are all here.</p>`) + (c.pr ? `<div class="prac"><div class="ph">Practise it</div><a href="${site('books/workbook-draft.pdf')}#page=${c.pr[0][0]}" target="_blank" rel="noopener">Workbook pp. ${c.pr[0][0]}–${c.pr[0][1]}</a>${c.pr[1].map(d => `<a class="dr" href="${site('drills.html')}?drill=${d[0]}${d[2] || '&tab=learn'}" target="_blank" rel="noopener">Drill: ${d[1]}</a>`).join('')}</div>` : '') + `<label class="follow"><input type="checkbox" id="fol" ${follow ? 'checked' : ''}> Follow on the page</label><p class="who">The Butler explains, Clara asks. Each Example asks first, then pauses so you can try.</p>`;
  const fo = document.getElementById('fol'); if (fo) fo.onchange = () => { follow = fo.checked; };
  if (c.clips) { const pp = document.getElementById('pp'); pp.disabled = playing < 0; pp.onclick = () => { if (audio.paused) { audio.play().catch(() => {}); } else audio.pause(); drawSide(); };
    side.querySelectorAll('.sp').forEach(b => b.onclick = () => { rate = +b.dataset.v; audio.playbackRate = rate; drawSide(); });
    document.getElementById('all').onclick = () => { chain = true; play(0); }; side.querySelectorAll('.clip').forEach(b => b.onclick = () => { chain = false; play(+b.dataset.i); }); }
}
function play(i) {
  const k = CH[ci].clips[i]; playing = i; audio.src = k.f; audio.playbackRate = rate; audio.play().catch(() => {});
  const p = CH[ci].pages.indexOf(k.p); if (p >= 0) { pi = p; showPage(); } drawSide();
}
let follow = true;
const stage = document.getElementById('stage'), ov = document.getElementById('ov'), sub = document.getElementById('sub');
function clearFollow() { if (typeof drawLens === 'function') drawLens(null); ov.innerHTML = ''; stage.style.transform = ''; sub.textContent = ''; }
function findLab(reg, name) { if (/^#\d+$/.test(name)) return reg.l[+name.slice(1)]; const m = reg.l.filter(x => x[0] === name); if (m.length < 2) return m[0]; const q = reg.l.find(x => x[0] === '?'); if (!q) return m[0]; return m.reduce((a, b) => Math.abs(b[1][0] - q[1][0]) < Math.abs(a[1][0] - q[1][0]) ? b : a); }

const GCLEF = "M441 -245c-23 -4 -48 -6 -76 -6c-59 0 -102 7 -130 20c-88 42 -150 93 -187 154c-26 44 -43 103 -48 176c0 6 -1 13 -1 19c0 54 15 111 45 170c29 57 65 106 110 148s96 85 153 127c-3 16 -8 46 -13 92c-4 43 -5 73 -5 89c0 117 16 172 69 257c34 54 64 82 89 82 c21 0 43 -30 69 -92s39 -115 41 -159v-15c0 -109 -21 -162 -67 -241c-13 -20 -63 -90 -98 -118c-13 -9 -25 -19 -37 -29l31 -181c8 1 18 2 28 2c58 0 102 -12 133 -35c59 -43 92 -104 98 -184c1 -7 1 -15 1 -22c0 -123 -87 -209 -181 -248c8 -57 17 -110 25 -162 c5 -31 6 -58 6 -80c0 -30 -5 -53 -14 -70c-35 -64 -88 -99 -158 -103c-5 0 -11 -1 -16 -1c-37 0 -72 10 -108 27c-50 24 -77 59 -80 105v11c0 29 7 55 20 76c18 28 45 42 79 44h6c49 0 93 -42 97 -87v-9c0 -51 -34 -86 -105 -106c17 -24 51 -36 102 -36c62 0 116 43 140 85 c9 16 13 41 13 74c0 20 -1 42 -5 67c-8 53 -18 106 -26 159zM461 939c-95 0 -135 -175 -135 -286c0 -24 2 -48 5 -71c50 39 92 82 127 128c40 53 60 100 60 140v8c-4 53 -22 81 -55 81h-2zM406 119l54 -326c73 25 110 78 110 161c0 7 0 15 -1 23c-7 95 -57 142 -151 142h-12 zM382 117c-72 -2 -128 -47 -128 -120v-7c2 -46 43 -99 75 -115c-3 -2 -7 -5 -10 -10c-70 33 -116 88 -123 172v11c0 68 44 126 88 159c23 17 49 29 78 36l-29 170c-21 -13 -52 -37 -92 -73c-50 -44 -86 -84 -109 -119c-45 -69 -67 -130 -67 -182v-13c5 -68 35 -127 93 -176 s125 -73 203 -73c25 0 50 3 75 9c-19 111 -36 221 -54 331z";
const FCLEF = "M582 -120c0 32 26 58 58 58s58 -26 58 -58s-26 -58 -58 -58s-58 26 -58 58zM582 120c0 32 26 58 58 58s58 -26 58 -58s-26 -58 -58 -58s-58 26 -58 58zM158 96c51 0 73 -14 88 -49l16 -39c0 -17 -2 -30 -7 -40c-3 -11 -10 -21 -19 -31c-17 -18 -49 -43 -84 -43 c-55 0 -77 13 -112 44c-24 21 -35 55 -35 100c0 46 14 81 32 112c30 52 71 79 137 93l36 6l26 2c154 0 235 -68 274 -182c11 -32 18 -68 18 -107c0 -103 -26 -182 -68 -250c-89 -145 -234 -230 -412 -288l-30 -5c-9 0 -14 3 -14 8c3 10 5 11 10 16c35 15 70 30 96 44l78 43 c96 57 162 136 197 258c9 33 17 60 22 100c3 22 5 35 6 39c-7 69 -16 115 -23 140s-4 22 -16 40c-8 12 -19 23 -31 34c-24 21 -62 44 -118 44c-48 0 -84 -8 -113 -28c-28 -19 -42 -44 -42 -73v-16c2 -5 3 -9 4 -11c24 22 52 39 84 39z";
// lens specs: [title, subtitle, clef, [[letter, staff step (0 = line 1, 8 = line 5, -2 = first ledger line below), label, word]]]
const LN = ['Line 1', '', 'Line 2', '', 'Line 3', '', 'Line 4', '', 'Line 5'], SPC = [0, 'Space 1', 0, 'Space 2', 0, 'Space 3', 0, 'Space 4'];
const LENSD = { tl: ['Treble staff', 'lines, from the bottom', 't', [['E', 0, 'Every'], ['G', 2, 'Good'], ['B', 4, 'Boy'], ['D', 6, 'Deserves'], ['F', 8, 'Fun']]],
  ts: ['Treble staff', 'spaces, from the bottom', 't', [['F', 1], ['A', 3], ['C', 5], ['E', 7]]],
  bl: ['Bass staff', 'lines, from the bottom', 'b', [['G', 0, 'Great'], ['B', 2, 'Big'], ['D', 4, 'Dragons'], ['F', 6, 'Fly'], ['A', 8, 'Away']]],
  bs: ['Bass staff', 'spaces, from the bottom', 'b', [['A', 1, 'All'], ['C', 3, 'Cows'], ['E', 5, 'Eat'], ['G', 7, 'Grass']]],
  tb: ['Treble staff', 'below, stepping out', 't', [['C', -2, '1st ledger line', 'Middle C'], ['B', -3, 'under it'], ['A', -4, '2nd ledger line']]],
  ta: ['Treble staff', 'above, stepping out', 't', [['A', 10, '1st ledger line'], ['B', 11, 'over it'], ['C', 12, '2nd ledger line']]],
  bb: ['Bass staff', 'below, stepping out', 'b', [['E', -2, '1st ledger line'], ['D', -3, 'under it'], ['C', -4, '2nd ledger line']]],
  ba: ['Bass staff', 'above, stepping out', 'b', [['C', 10, '1st ledger line', 'Middle C'], ['D', 11, 'over it'], ['E', 12, '2nd ledger line']]] };
const lensEl = document.getElementById('lens');
function drawLens(L, t) {
  if (!L) { if (lensEl.dataset.k) { lensEl.innerHTML = ''; lensEl.dataset.k = ''; lensEl.dataset.t = ''; } return; }
  if (L.k === 'auto') return drawAuto(L, t);
  if (L.k === 'rhy') return drawRhy(L, t);
  if (L.k === 'mirror') return drawMirror(L);
  const [name, subt, clef, items] = LENSD[L.k]; const n = items.length;
  const cnt = L.at.length ? L.at.filter(v => v <= t).length : n; const shown = L.full ? n : cnt, cur = cnt - 1;
  const key = L.k + shown + ':' + cur; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const ACC = '#e4572e', INK = '#26296b', F = 'font-family="Atkinson Hyperlegible,sans-serif"';
  const steps = items.map(x => x[1]), lo = Math.min(0, ...steps), hi = Math.max(8, ...steps);
  const H = 15, top = 62 + (hi - 8 > 0 ? 0 : 0), Y = st => top + (hi - st) * H;   // y of a staff step
  const W = 600, botY = Y(lo), VH = botY + 66;
  const x0 = 170, dx = n > 1 ? (540 - x0) / (n - 1) : 0, X = i => x0 + i * dx;
  let g = '';
  const c = items[cur] || null;
  if (c && c[1] % 2 && c[1] > 0 && c[1] < 8) g += `<rect x="96" y="${Y(c[1]) - H + 2}" width="490" height="${2 * H - 4}" fill="${ACC}" opacity=".16"/>`;
  for (let st = 0; st <= 8; st += 2) { const on = c && c[1] === st; g += `<line x1="20" x2="586" y1="${Y(st)}" y2="${Y(st)}" stroke="${on ? ACC : INK}" stroke-width="${on ? 5 : 2.2}"/>`; }
  g += `<line x1="20" x2="20" y1="${Y(8)}" y2="${Y(0)}" stroke="${INK}" stroke-width="2.2"/>`;
  g += clef === 't' ? `<path d="${GCLEF}" transform="translate(30 ${Y(2)}) scale(${H * 2 / 250} ${-H * 2 / 250})" fill="${INK}"/>` : `<path d="${FCLEF}" transform="translate(30 ${Y(6)}) scale(${H * 2 / 250} ${-H * 2 / 250})" fill="${INK}"/>`;
  const labY = botY + 34;
  for (let i = 0; i < n; i++) {
    const [lt, st, lab0, word] = items[i], x = X(i), y = Y(st), lab = lab0 || (st % 2 ? SPC[st] : LN[st]);
    if (i >= shown) { g += `<text x="${x}" y="${labY}" text-anchor="middle" font-size="15" fill="#c9c8d8" ${F}>${lab}</text>`; continue; }
    const on = i === cur, col = on ? ACC : INK;
    const leds = []; if (st < 0) for (let k = -2; k >= st; k -= 2) leds.push(k); if (st > 8) for (let k = 10; k <= st; k += 2) leds.push(k);
    leds.forEach(k => { const lon = on && k === st; g += `<line x1="${x - 30}" x2="${x + 30}" y1="${Y(k)}" y2="${Y(k)}" stroke="${lon ? ACC : INK}" stroke-width="${lon ? 5 : 2.6}"/>`; });
    g += `<ellipse cx="${x}" cy="${y}" rx="${on ? 17 : 14}" ry="${on ? 12.5 : 10.5}" transform="rotate(-20 ${x} ${y})" fill="${on ? ACC : '#fff'}" stroke="${col}" stroke-width="3.2"/>`;
    g += `<text x="${x}" y="${Y(hi) - 24}" text-anchor="middle" font-size="${on ? 30 : 24}" font-weight="700" fill="${col}" ${F} stroke="#fff" stroke-width="5" paint-order="stroke">${lt}</text>`;
    g += `<text x="${x}" y="${labY}" text-anchor="middle" font-size="15" font-weight="${on ? 700 : 400}" fill="${on ? ACC : '#5a5d8f'}" ${F}>${lab}</text>`;
    if (word) g += `<text x="${x}" y="${labY + 22}" text-anchor="middle" font-size="16" font-style="italic" font-weight="${on ? 700 : 400}" fill="${col}" ${F}>${word}</text>`;
  }
  if (L.k === 'ts' && shown === n) g += `<text x="586" y="${labY + 22}" text-anchor="end" font-size="16" font-style="italic" font-weight="700" fill="${ACC}" ${F}>F A C E = FACE</text>`;
  const svg = `<svg viewBox="0 0 ${W} ${VH}" role="img" aria-label="${name}, ${subt}">${g}</svg>`;
  if (lensEl.dataset.t === L.k && lensEl.firstChild) { lensEl.firstChild.lastChild.outerHTML = svg; return; }   // same staff: redraw quietly, no pop (her 8 Nov: no blinking)
  lensEl.dataset.t = L.k;
  lensEl.innerHTML = `<div class="lens"><div class="lh"><svg width="16" height="16" viewBox="0 0 16 16" style="width:16px"><circle cx="6.5" cy="6.5" r="5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M10.5 10.5l4 4" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>${name} · ${subt}</div>${svg}</div>`;
}

// auto lens: the notes being played, on the staff (treble, bass, or both) with their keys underneath
const DI = { C: 0, D: 1, E: 2, F: 3, G: 4, A: 5, B: 6 }, SEMI = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };
const pn = n => { const m = n.match(/^([A-G])([#b]?)(\d)$/); return { L: m[1], acc: m[2], o: +m[3], d: +m[3] * 7 + DI[m[1]], midi: (+m[3] + 1) * 12 + SEMI[m[1]] + (m[2] === '#' ? 1 : m[2] === 'b' ? -1 : 0) }; };
function lensShell(key, head, svg) {
  if (lensEl.dataset.t === key && lensEl.firstChild) { lensEl.firstChild.lastChild.outerHTML = svg; return; }
  lensEl.dataset.t = key;
  lensEl.innerHTML = `<div class="lens"><div class="lh"><svg width="16" height="16" viewBox="0 0 16 16" style="width:16px"><circle cx="6.5" cy="6.5" r="5" fill="none" stroke="currentColor" stroke-width="2.2"/><path d="M10.5 10.5l4 4" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>${head}</div>${svg}</div>`;
}
function drawAuto(L, t) {
  const cols = L.items.map(c => c.map(pn)), n = cols.length;
  { const st = {}; let pb = -1; cols.forEach((col, i) => { const b = (L.bar || [])[i] || 0; if (b !== pb) { for (const k in st) delete st[k]; pb = b; }   // a sign lasts to the bar line: show ♮ when it is cancelled
      col.forEach(p => { const k = p.L + p.o, was = st[k] || ''; p.nat = !p.acc && was !== ''; st[k] = p.acc; }); }); }
  const cnt = L.at.filter(v => v <= t).length, cur = cnt - 1;
  const key = 'auto' + L.at[0] + ':' + cur; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const all = cols.flat(), dmin = Math.min(...all.map(x => x.d)), dmax = Math.max(...all.map(x => x.d));
  const staff = dmin >= 28 ? 't' : dmax <= 28 ? 'b' : 'g';
  const lines = staff === 't' ? [30, 32, 34, 36, 38] : staff === 'b' ? [18, 20, 22, 24, 26] : [18, 20, 22, 24, 26, 30, 32, 34, 36, 38];
  const lo = Math.min(dmin, lines[0]), hi = Math.max(dmax, lines[lines.length - 1]);
  const H = staff === 'g' ? 9 : 12, ACC = '#e4572e', INK = '#26296b', GR = '#cfcfe0', F = 'font-family="Atkinson Hyperlegible,sans-serif"';
  const fs = n > 14 ? 14 : n > 9 ? 18 : 24, topY = 30 + fs, Y = d => topY + (hi - d) * H, botY = Y(lo);
  let g = ''; const KB = !!L.kb;
  if (!KB) lines.forEach(d => g += `<line x1="20" x2="586" y1="${Y(d)}" y2="${Y(d)}" stroke="${INK}" stroke-width="2"/>`);
  if (!KB && staff !== 'b') g += `<path d="${GCLEF}" transform="translate(28 ${Y(32)}) scale(${H * 2 / 250} ${-H * 2 / 250})" fill="${INK}"/>`;
  if (!KB && staff !== 't') g += `<path d="${FCLEF}" transform="translate(28 ${Y(24)}) scale(${H * 2 / 250} ${-H * 2 / 250})" fill="${INK}"/>`;
  if (!KB) g += `<line x1="20" x2="20" y1="${Y(lines[lines.length - 1])}" y2="${Y(lines[0])}" stroke="${INK}" stroke-width="2"/>`;
  const x0 = 110, x1 = 560, dx = n > 1 ? Math.min(90, (x1 - x0) / (n - 1)) : 0, X = i => (n > 1 ? x0 + ((x1 - x0) - dx * (n - 1)) / 2 : (x0 + x1) / 2) + i * dx;
  const lw = n > 1 ? Math.max(20, Math.min(26, dx * .42 + 8)) : 26;   // her 9 Nov: a lone Middle C lost its ledger line under the head
  cols.forEach((col, i) => {
    const x = X(i), on = i === cur, done = i < cur, c = on ? ACC : done ? INK : GR;
    if (!KB) col.forEach(p => {
      const leds = []; const top = staff === 'b' ? 26 : 38, bot = staff === 't' ? 30 : 18;
      for (let k = top + 2; k <= p.d; k += 2) leds.push(k); for (let k = bot - 2; k >= p.d; k -= 2) leds.push(k);
      if (staff === 'g' && p.d === 28) leds.push(28);
      leds.forEach(k => g += `<line x1="${x - lw}" x2="${x + lw}" y1="${Y(k)}" y2="${Y(k)}" stroke="${INK}" stroke-width="${on && k === p.d ? 3.4 : 2.4}"/>`);
      const rx = (on ? 1.15 : 1) * H * 1.1, ry = (on ? 1.15 : 1) * H * .82;
      g += `<ellipse cx="${x}" cy="${Y(p.d)}" rx="${rx}" ry="${ry}" transform="rotate(-20 ${x} ${Y(p.d)})" fill="${on ? ACC : '#fff'}" stroke="${c}" stroke-width="${H > 10 ? 3 : 2.4}"/>`;
      if (p.acc || p.nat) g += `<text x="${x - rx - 4}" y="${Y(p.d) + H * .7}" text-anchor="end" font-size="${H * 2.2}" fill="${c}" ${F}>${p.acc === '#' ? '♯' : p.acc === 'b' ? '♭' : '♮'}</text>`;
    });
    const nm = col.map(p => p.L + (p.acc === '#' ? '♯' : p.acc === 'b' ? '♭' : '')).join(' ');
    g += `<text x="${x}" y="${topY - fs * .55}" text-anchor="middle" font-size="${on ? fs * 1.2 : fs}" font-weight="700" fill="${on ? ACC : done ? INK : GR}" ${F}>${nm}</text>`;
  });
  // keyboard under the staff
  const ms = all.map(p => p.midi), wh = m => [0, 2, 4, 5, 7, 9, 11].includes(((m % 12) + 12) % 12);
  let a = Math.min(...ms), b = Math.max(...ms); while (!wh(a)) a--; while (!wh(b)) b++;
  let whites = []; for (let m = a; m <= b; m++) if (wh(m)) whites.push(m);
  while (whites.length < 10) { let m = whites[0] - 1; while (!wh(m)) m--; whites.unshift(m); if (whites.length < 10) { m = whites[whites.length - 1] + 1; while (!wh(m)) m++; whites.push(m); } }
  const kw = Math.min(40, 560 / whites.length), kx0 = 300 - kw * whites.length / 2, KY = KB ? topY + 6 : botY + 26, KH = KB ? 90 : 62;
  const curM = new Set(cur >= 0 ? cols[cur].map(p => p.midi) : []), doneM = new Set(cols.slice(0, Math.max(0, cur)).flat().map(p => p.midi));
  const LET = ['C', '', 'D', '', 'E', 'F', '', 'G', '', 'A', '', 'B'];
  whites.forEach((m, i) => { const on = curM.has(m), dn = doneM.has(m), x = kx0 + i * kw;
    g += `<rect x="${x}" y="${KY}" width="${kw}" height="${KH}" fill="${on ? ACC : dn ? '#fbd9cc' : '#fff'}" stroke="${INK}" stroke-width="1.6"/>`;
    if (on || dn || LET[m % 12] === 'C') g += `<text x="${x + kw / 2}" y="${KY + KH - 8}" text-anchor="middle" font-size="${Math.min(15, kw * .5)}" font-weight="700" fill="${on ? '#fff' : dn ? ACC : '#9a9cc0'}" ${F}>${LET[m % 12]}</text>`; });
  whites.forEach((m, i) => { const bm = m + 1; if (wh(bm) || i === whites.length - 1) return; const on = curM.has(bm), dn = doneM.has(bm), x = kx0 + (i + 1) * kw - kw * .3;
    g += `<rect x="${x}" y="${KY}" width="${kw * .6}" height="${KH * .62}" rx="2" fill="${on ? ACC : dn ? '#e99a80' : INK}" stroke="${INK}" stroke-width="1.2"/>`; });
  const VH = KY + KH + 10;
  const head = KB ? '♪ The keys' : '♪ ' + (staff === 't' ? 'Treble staff' : staff === 'b' ? 'Bass staff' : 'Grand staff') + ' and keys';
  lensShell('auto' + L.at[0], head, `<svg viewBox="0 0 600 ${VH}" role="img" aria-label="${head}">${g}</svg>`);
}

const GL = {"E0A3": "M278 64c0 22 -17 39 -43 39c-12 0 -26 -3 -41 -10c-85 -43 -165 -94 -165 -156c5 -25 15 -32 49 -32c67 11 200 95 200 159zM0 -36c0 68 73 174 200 174c66 0 114 -39 114 -97c0 -84 -106 -173 -218 -173c-64 0 -96 32 -96 96z", "E0A2": "M198 133c102 0 207 -45 207 -133c0 -92 -118 -133 -227 -133c-101 0 -178 46 -178 133c0 88 93 133 198 133zM293 -21c0 14 -3 29 -8 44c-7 20 -18 38 -33 54c-20 21 -43 31 -68 31l-20 -2c-15 -5 -27 -14 -36 -28c-4 -9 -6 -17 -8 -24s-3 -16 -3 -27c0 -15 3 -34 9 -57 s18 -41 34 -55c15 -15 36 -23 62 -23c4 0 10 1 18 2c19 5 32 15 40 30s13 34 13 55z", "E0A4": "M0 -39c0 68 73 172 200 172c66 0 114 -37 114 -95c0 -84 -106 -171 -218 -171c-64 0 -96 30 -96 94z", "E240": "M179 -646c15 29 29 55 46 102c18 49 30 108 30 138c0 105 -80 173 -168 200c-18 5 -47 9 -87 16v190h22c8 0 33 -61 71 -95c4 -3 -2 3 61 -56c62 -58 122 -137 122 -241c0 -38 -13 -106 -35 -163c-20 -51 -43 -99 -66 -132c-6 -5 -10 -7 -13 -7s-5 2 -5 5l4 10 c1 3 14 25 18 33z", "E4E5": "M107 292c-13 24 -30 49 -52 71c-1 1 0 2 0 3l-2 2c3 3 4 4 6 4c12 0 26 -7 40 -20s44 -40 89 -81c26 -24 28 -29 46 -47c4 -4 8 -9 10 -14c6 -8 8 -16 8 -27c0 -19 -12 -40 -36 -61c-28 -23 -49 -38 -61 -73c-4 -11 -7 -27 -10 -50c13 -43 34 -83 59 -121 c31 -47 59 -79 101 -129c-8 0 -26 7 -54 20l-62 29l-21 6l-23 1c-25 0 -45 -10 -60 -30l-4 -14l-1 -12c0 -33 20 -56 39 -78c8 -9 17 -18 26 -26c17 -15 27 -24 28 -30l-3 -3c-11 5 -19 10 -25 15c-9 3 -37 21 -45 26c-24 14 -45 32 -63 51c-19 21 -37 44 -37 71 c0 63 27 95 80 95c41 0 86 -18 136 -52c-19 26 -37 48 -55 66c-23 23 -48 44 -73 65c-28 23 -47 40 -58 53s-17 26 -18 39c75 64 113 125 113 183c0 27 -7 48 -18 68z", "E4E6": "M0 123c7 34 33 56 69 60c29 -3 43 -9 53 -29c4 -8 7 -15 10 -22c0 -21 -1 -25 -11 -35c-5 -8 -18 -14 -40 -20l12 -3l15 -1c44 0 97 26 122 56c10 11 18 26 24 42c7 1 15 2 22 3l-140 -424h-36l111 330c-10 -6 -27 -12 -53 -16l-52 -8h-10l-20 1c-1 0 -8 3 -21 6 c-37 9 -55 28 -55 60z", "E4E4": "M0 10v105c0 9 1 10 10 10h280c9 0 10 -1 10 -10v-105c0 -9 -1 -10 -10 -10h-280c-9 0 -10 1 -10 10z", "E4E3": "M0 -115v105c0 9 1 10 10 10h280c9 0 10 -1 10 -10v-105c0 -9 -1 -10 -10 -10h-280c-9 0 -10 1 -10 10z"};
function drawRhy(L, t) {
  const B = L.beats, N = L.n || B.length, NT = L.notes, AN = L.ands || [];
  const cb = B.filter(b => b[0] <= t).length - 1, cn = NT.filter(n => n[0] <= t).length - 1, ca = AN.filter(a => a[0] <= t).length - 1;
  const key = 'rhy' + B[0][0] + ':' + cb + ':' + cn + ':' + ca; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const ACC = '#e4572e', INK = '#26296b', GR = '#cfcfe0', F = 'font-family="Atkinson Hyperlegible,sans-serif"';
  const X0 = 56, W = 520, bw = W / N, X = b => X0 + b * bw;
  const hasN = NT.length > 0, LY = 92, BY = hasN ? 150 : 70;
  const SPc = 13, sc = SPc * 4 / 1000;   // glyph em = 4 staff spaces
  const gl = (id, x, y, col) => `<path d="${GL[id]}" transform="translate(${x} ${y}) scale(${sc} ${-sc})" fill="${col}"/>`;
  let g = '';
  // bar lines through both rows
  const top = hasN ? LY - 58 : BY - 34, bot = BY + 34;
  L.bars.forEach(i => { if (i > 0) g += `<line x1="${X(i) - 4}" x2="${X(i) - 4}" y1="${top}" y2="${bot}" stroke="${INK}" stroke-width="2"/>`; });
  g += `<line x1="${X(N) - 4}" x2="${X(N) - 4}" y1="${top}" y2="${bot}" stroke="${INK}" stroke-width="2"/><line x1="${X(N) + 1}" x2="${X(N) + 1}" y1="${top}" y2="${bot}" stroke="${INK}" stroke-width="5"/>`;
  if (hasN) {
    g += `<line x1="${X0 - 14}" x2="${X(N) - 4}" y1="${LY}" y2="${LY}" stroke="${INK}" stroke-width="1.8"/>`;
    g += `<text x="${X0 - 18}" y="${LY - 22}" text-anchor="end" font-size="12" fill="#5a5d8f" ${F}>notes</text>`;
    const stems = [];
    NT.forEach((n, i) => {
      const [tt, pos, d, rest] = n, x = X(pos) + 6, on = i === cn, done = i < cn, col = on ? ACC : done ? INK : '#9a9cc0';
      // how long: a bar under the note
      g += `<rect x="${X(pos) + 2}" y="${LY + 16}" width="${Math.max(6, d * bw - 10)}" height="8" rx="4" fill="${rest ? 'none' : on ? ACC : done ? '#c9cbe6' : '#ecebf4'}" stroke="${rest ? (on ? ACC : GR) : 'none'}" stroke-dasharray="${rest ? '3 3' : ''}"/>`;
      if (rest) {
        const bi = L.bars.indexOf(pos), blen = bi >= 0 ? ((L.bars[bi + 1] ?? N) - pos) : 0, whole = d >= 4 || (bi >= 0 && Math.abs(blen - d) < 1e-3 && d > 1);
        const id = whole ? 'E4E3' : d >= 2 ? 'E4E4' : d >= 1 ? 'E4E5' : 'E4E6';
        if (whole) { g += gl(id, X(pos) + d * bw / 2 - 12, LY, col); return; }   // a whole bar of silence: semibreve rest, centred
        g += gl(id, x, LY, col); if (d === 3 || d === 1.5) g += `<circle cx="${x + 26}" cy="${LY - 6}" r="2.6" fill="${col}"/>`;
        return;
      }
      const id = d >= 4 ? 'E0A2' : d >= 2 ? 'E0A3' : 'E0A4';
      g += gl(id, x, LY, col);
      if (d < 4) { const sx = x + SPc * 1.18 - 1; g += `<line x1="${sx}" x2="${sx}" y1="${LY - 2}" y2="${LY - SPc * 3.4}" stroke="${col}" stroke-width="2.2"/>`; stems.push([i, sx, d, col, pos]); }
      if (d === 3 || d === 1.5 || d === 0.75) g += `<circle cx="${x + SPc * 1.6}" cy="${LY - 6}" r="2.8" fill="${col}"/>`;
    });
    NT.forEach((n, i) => { if (!n[4] || !NT[i + 1]) return; const x1 = X(n[1]) + 6 + SPc * .6, x2 = X(NT[i + 1][1]) + 6 + SPc * .6, on = i === cn || i + 1 === cn, col = on ? ACC : i < cn ? INK : '#9a9cc0';   // a tie: one sound across both notes
      g += `<path d="M${x1 + 4} ${LY + 7} Q${(x1 + x2) / 2} ${LY + 17} ${x2 - 4} ${LY + 7}" fill="none" stroke="${col}" stroke-width="2.6" stroke-linecap="round"/>`; });
    // quavers: beam two in the same beat, otherwise a flag
    const q = stems.filter(s => s[2] <= 0.75); const used = new Set();
    q.forEach((s, j) => { const nx = q[j + 1]; if (used.has(s[0])) return;
      if (nx && nx[0] === s[0] + 1 && Math.floor(nx[4] + 1e-6) === Math.floor(s[4] + 1e-6)) { used.add(s[0]); used.add(nx[0]); g += `<rect x="${s[1] - 1}" y="${LY - SPc * 3.4}" width="${nx[1] - s[1] + 2}" height="${SPc * .5}" fill="${s[3] === ACC || nx[3] === ACC ? ACC : s[3]}"/>`; }
      else { used.add(s[0]); g += gl('E240', s[1] - 1, LY - SPc * 3.4, s[3]); } });
  }
  // the beat: one box per beat, beat one strongest
  g += `<text x="${X0 - 18}" y="${BY + 5}" text-anchor="end" font-size="12" fill="#5a5d8f" ${F}>beat</text>`;
  const clickOnly = !hasN && B.some(b => b[1] !== 'X');
  B.forEach((b, i) => {
    const [tt, lv, num, ps] = b, x = X(ps == null ? i : ps) + Math.min(bw / 2, 22) - 4, on = i === cb && !(ca >= 0 && AN[ca][0] > b[0]), done = i < cb;
    const k = Math.max(.72, Math.min(1, bw / (AN.length ? 64 : 42))), r = (lv === 'X' ? 17 : lv === 'M' ? 14 : 11.5) * k;   // shrink when the bar is crowded
    g += `<circle cx="${x}" cy="${BY}" r="${on ? r + 2 : r}" fill="${on ? ACC : done ? '#fbd9cc' : '#fff'}" stroke="${on ? ACC : INK}" stroke-width="${lv === 'X' ? 3 : 1.8}"/>`;
    g += `<text x="${x}" y="${BY + (lv === 'X' ? 7 : 5)}" text-anchor="middle" font-size="${(lv === 'X' ? 19 : 15) * Math.max(.7, k)}" font-weight="700" fill="${on ? '#fff' : INK}" ${F}>${num === '-' ? '' : num}</text>`;
    if (clickOnly) g += `<text x="${x}" y="${BY + 36}" text-anchor="middle" font-size="12" fill="${on ? ACC : '#5a5d8f'}" ${F}>${lv === 'X' ? 'strong' : lv === 'M' ? 'medium' : 'weak'}</text>`;
  });
  AN.forEach((a, j) => { const on = j === ca && a[0] >= B[cb][0], x = X(a[1]) + Math.min(bw / 2, 22) - 4;
    g += `<text x="${x}" y="${BY + 6}" text-anchor="middle" font-size="${(on ? 22 : 17) * Math.min(1, bw / 64 + .3)}" font-weight="700" fill="${on ? ACC : j < ca ? INK : '#9a9cc0'}" ${F}>${a[2]}</text>`; });
  const VH = BY + (clickOnly ? 48 : 40);
  const head = hasN ? '♪ The beat and the notes' : '♪ The beat';
  lensShell('rhy' + B[0][0], head, `<svg viewBox="0 0 600 ${VH}" role="img" aria-label="${head}">${g}</svg>`);
}

function drawMirror(L) {   // the grand staff folds at Middle C: the top note lands on its mirror note below
  const key = 'mirror' + L.m; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const P = { GF: [32, 24, 'Treble G', 'Bass F', 'note 5 up from Middle C', 'note 5 down from Middle C'], CC: [42, 14, 'High C', 'Low C', 'two ledger lines above', 'two ledger lines below'] }[L.m];
  const [dt, db, lt, lb, st, sb] = P, ACC = '#e4572e', INK = '#26296b', F = 'font-family="Atkinson Hyperlegible,sans-serif"';
  const H = 10, hi = Math.max(40, dt + 2), lo = Math.min(16, db - 2), Y = d => 20 + (hi - d) * H, MC = Y(28), X0 = 30, X1 = 470, NX = 290;
  const staff = (ds, col, w) => ds.map(d => `<line x1="${X0}" x2="${X1}" y1="${Y(d)}" y2="${Y(d)}" stroke="${col}" stroke-width="${w}"/>`).join('');
  const leds = (d, col) => { let o = ''; if (d > 38) for (let k = 40; k <= d; k += 2) o += `<line x1="${NX - 22}" x2="${NX + 22}" y1="${Y(k)}" y2="${Y(k)}" stroke="${col}" stroke-width="2.2"/>`; if (d < 18) for (let k = 16; k >= d; k -= 2) o += `<line x1="${NX - 22}" x2="${NX + 22}" y1="${Y(k)}" y2="${Y(k)}" stroke="${col}" stroke-width="2.2"/>`; return o; };
  const head = (d, fill, col) => `<ellipse cx="${NX}" cy="${Y(d)}" rx="12" ry="9" transform="rotate(-20 ${NX} ${Y(d)})" fill="${fill}" stroke="${col}" stroke-width="3"/>`;
  let g = staff([30, 32, 34, 36, 38], INK, 2) + staff([18, 20, 22, 24, 26], INK, 2);
  g += `<path d="${GCLEF}" transform="translate(${X0 + 8} ${Y(32)}) scale(${H * 2 / 250} ${-H * 2 / 250})" fill="${INK}"/><path d="${FCLEF}" transform="translate(${X0 + 8} ${Y(24)}) scale(${H * 2 / 250} ${-H * 2 / 250})" fill="${INK}"/>`;
  g += `<line x1="${X0 - 30}" x2="${X1 + 20}" y1="${MC}" y2="${MC}" stroke="${ACC}" stroke-width="2" stroke-dasharray="6 5"/><text x="${X1 + 6}" y="${MC + 5}" font-size="15" font-weight="700" fill="${ACC}" ${F}>fold</text>`;
  g += `<line x1="${NX - 60}" x2="${NX - 36}" y1="${MC}" y2="${MC}" stroke="${INK}" stroke-width="2.2"/><ellipse cx="${NX - 48}" cy="${MC}" rx="11" ry="8" transform="rotate(-20 ${NX - 48} ${MC})" fill="#fff" stroke="${INK}" stroke-width="2.6"/>`;
  g += leds(dt, INK) + head(dt, '#fff', INK) + leds(db, INK) + head(db, '#fff', INK);
  g += `<text x="${NX + 26}" y="${Y(dt) + 5}" font-size="17" font-weight="700" fill="${INK}" ${F} stroke="#fff" stroke-width="5" paint-order="stroke">${lt}</text><text x="${NX + 26}" y="${Y(db) + 5}" font-size="17" font-weight="700" fill="${INK}" ${F} stroke="#fff" stroke-width="5" paint-order="stroke">${lb}</text>`;
  g += `<text x="${NX + 26}" y="${Y(dt) + 22}" font-size="13" fill="#5a5d8f" ${F} stroke="#fff" stroke-width="5" paint-order="stroke">${st}</text><text x="${NX + 26}" y="${Y(db) + 22}" font-size="13" fill="#5a5d8f" ${F} stroke="#fff" stroke-width="5" paint-order="stroke">${sb}</text>`;
  // the folding copy of the top half
  g += `<g class="fold" style="transform-box:view-box;transform-origin:0 ${MC}px">${staff([30, 32, 34, 36, 38], ACC, 1.6)}${leds(dt, ACC)}${head(dt, ACC, ACC)}</g>`;
  g += `<g class="meet" style="opacity:0">${head(db, ACC, ACC)}<text x="${NX}" y="${Y(lo) + 6}" text-anchor="middle" font-size="17" font-weight="700" fill="${ACC}" ${F}>they meet: mirror notes</text></g>`;
  const VH = Y(lo) + 20;
  lensShell(key, '♪ Fold the grand staff at Middle C', `<svg viewBox="0 0 ${X1 + 50} ${VH}" role="img" aria-label="${lt} and ${lb} are mirror notes either side of Middle C">${g}</svg>`);
}
function tick() {
  if (playing < 0) return; const k = CH[ci].clips[playing], t = audio.currentTime; const ln = k.l.find(x => t >= x.t0 && t < x.t1);
  if (!ln) { requestAnimationFrame(tick); return; }
  drawLens(follow ? ln.lens : null, t);
  const hit = ln.hits ? ln.hits.filter(h => h[0] <= t).pop() : null; let txt = ln.text || ''; if (hit) txt = txt.slice(0, hit[2]) + '<mark>' + txt.slice(hit[2], hit[3]) + '</mark>' + txt.slice(hit[3]);
  sub.innerHTML = ln.text ? `<b>${({B: 'Butler', P: 'Clara', Q: '♕ Queen', K: '♔ King'})[ln.who] || ''}</b>${txt}` : (ln.who === 'piano' ? '<b>♪</b>listen' : '');
  const c = ln.cue;
  if (c && follow) {
    const pidx = CH[ci].pages.indexOf(c.p); if (pidx >= 0 && pidx !== pi) { pi = pidx; showPage(); }
    const hr = hit && hit[4] ? hit[4] : c.r; const reg = (REG[c.p] || {})[hr];
    if (reg) {
      const [x, y, w, h] = reg.b; const S = Math.min(2.2, Math.max(1, 0.94 / w));
      const tx = Math.min(0, Math.max(1 - S, 0.5 - S * (x + w / 2))), ty = Math.min(0, Math.max(1 - S, 0.42 - S * (y + h / 2)));
      stage.style.transform = `translate(${tx * 100}%, ${ty * 100}%) scale(${S})`;
      lensEl.classList.toggle('bot', S * (y + h / 2) + ty < 0.5);   // keep the lens off the part of the page being read
      let marks = []; if (c.lab && hr === c.r) marks = c.lab; if (hit) marks = [hit[1]]; if (c.seq && ln.notes) { const i = ln.notes.filter(v => v <= t).length - 1; if (i >= 0) marks = [c.seq[Math.min(i, c.seq.length - 1)]]; }
      const exm = /^ex/.test(c.r) && !c.reveal; const vis = new Set([...(c.show || []), ...marks, '?']);
      const key = c.p + hr + marks.join(',') + (exm ? 'x' + [...vis].join('') : ''); if (ov.dataset.k !== key) { ov.dataset.k = key;
        const covers = exm ? reg.l.filter(L => !vis.has(L[0])).map(L => `<div class="cov" style="left:${L[1][0] * 100 - .3}%;top:${L[1][1] * 100 - .2}%;width:${L[1][2] * 100 + .6}%;height:${L[1][3] * 100 + .4}%"></div>`).join('') + (reg.r ? `<div class="cov res" style="left:${reg.r[0] * 100}%;top:${reg.r[1] * 100}%;width:${reg.r[2] * 100}%;height:${reg.r[3] * 100}%">Answer coming…</div>` : '') : '';
        ov.innerHTML = covers + `<div class="hl${/^ex/.test(c.r) ? ' fog' : ''}" style="left:${x * 100 - .6}%;top:${y * 100 - .4}%;width:${w * 100 + 1.2}%;height:${h * 100 + .8}%"></div>` +
          marks.map(m => findLab(reg, m)).filter(Boolean).map(L => `<div class="mk" style="left:${(L[1][0] + L[1][2] / 2) * 100}%;top:${(L[1][1] + L[1][3] / 2) * 100}%;width:${Math.max(3.2, L[1][2] * 100 + 2.4)}%"></div>`).join(''); }
    }
  } else if (!c || !follow) { stage.style.transform = ''; ov.innerHTML = ''; ov.dataset.k = ''; }
  requestAnimationFrame(tick);
}
audio.onplay = () => { requestAnimationFrame(tick); drawSide(); }; audio.onpause = () => { if (playing >= 0) drawSide(); };
audio.onended = () => { const c = CH[ci]; if (chain && playing + 1 < c.clips.length) play(playing + 1); else { playing = -1; drawSide(); clearFollow(); } };
function go(i, p = 0) { audio.pause(); playing = -1; if (typeof clearFollow === 'function') clearFollow(); ci = i; pi = p; sel.value = i; showPage(); drawSide(); history.replaceState(null, '', '#' + CH[i].k); window.scrollTo(0, 0); }
sel.onchange = () => go(+sel.value);
document.getElementById('prev').onclick = () => { if (pi > 0) { pi--; showPage(); } else if (ci > 0) go(ci - 1, CH[ci - 1].pages.length - 1); };
document.getElementById('next').onclick = () => { if (pi < CH[ci].pages.length - 1) { pi++; showPage(); } else if (ci < CH.length - 1) go(ci + 1); };
document.addEventListener('keydown', e => { if (e.target.tagName === 'SELECT') return; if (e.key === 'ArrowRight') document.getElementById('next').click(); if (e.key === 'ArrowLeft') document.getElementById('prev').click(); });
const start = CH.findIndex(c => c.k === (location.hash.slice(1) || new URLSearchParams(location.search).get('ch') || 'P1'));
go(start >= 0 ? start : 0);
</script></body></html>'''
open(OUT + '/index.html', 'w').write(HTML.replace('__DATA__', DATA).replace('__REG__', REGD))
print('ok read page', len(CH), 'sections,', sum(1 for c in CH if c.get('clips')), 'with audio, last page', LAST)
