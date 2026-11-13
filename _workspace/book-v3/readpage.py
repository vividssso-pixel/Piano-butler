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
        n = int(os.path.basename(f)[3:6]); Image.open(f).save(f'{OUT}/pages/p{n:03d}.webp', 'WEBP', quality=70, method=5)   # her 12 Nov: the draft now starts at p. 1 (front matter pp. 1-16)
else:
    for f in glob.glob('/tmp/claude-0/read/pages/*.webp'): shutil.copy(f, OUT + '/pages/')
LAST = max(int(os.path.basename(f)[1:4]) for f in glob.glob(OUT + '/pages/*.webp'))
TIPS = {L[-1][3]: L[-1][1] for L in (OA.LEG_P, OA.LEG_T, OA.LEG_E, OA.LEG_S, OA.LEG_H, OA.LEG_M, OA.LEG_F, OA.LEG_L)}
PNAME = dict(CB.PARTS)
CH = [{'k': 'GD', 'part': 'Before you play', 't': 'How to read this book', 'pages': [17]}, {'k': 'B1', 'part': 'Before you play', 't': 'Posture and hand shape', 'pages': [18, 19, 20]}]   # her 11 Nov; 12 Nov: the guide page, p. 17
for p, name, k in PM.PARTS:
    part = PNAME[p]
    CH.append({'k': p + 'O', 'part': part, 't': 'Opening map', 'pages': [PM.PAGE[p + 'O']]})
    for i in range(1, k + 1):
        key = f'{p}{i}'; a, n = PM.pages_of(key)
        CH.append({'k': key, 'part': part, 't': f'{i} · {CB.TITLES[key]}', 'pages': list(range(a, a + n))})
    if PM.TIPS.get(p): CH.append({'k': p + 'T', 'part': part, 't': TIPS[p + 'T'], 'pages': [PM.PAGE[p + 'T']]})
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
# her 11 Nov (p. 72): an example covers its labels until the voice says them, but the question itself must stay in view:
# the bar letters and road signs of a map, tempo and time signatures, rall. / a tempo, the start mark, the note glyphs.
_GIVEN_ALL = {('20', 'ex2'), ('72', 'ex1'), ('72', 'ex2'), ('73', 'ex3'), ('73', 'ex4')}
_GIVEN_TXT = {'You play:', 'start', 'Fine', 'D.C. al Fine', 'D.S. al Coda', 'To Coda', 'rall.', 'a tempo', '= 96', '𝅘𝅥', '𝅗𝅥', '𝅘𝅥𝅮', '𝅘𝅥𝅭', '𝅝'}
def _given(pg, key, L):
    if (pg, key) in _GIVEN_ALL or L[0] in _GIVEN_TXT: return True
    if pg == '63' and key == 'ex1' and L[0] in ('9', '8'): return True   # the 9/8 being asked about
    return 50 <= int(pg) <= 73 and len(L) > 2 and L[2] == 'rgb(255, 255, 255)' and L[0].isdigit()   # time-signature digits
for c in CH:
    for k in c.get('clips', []):
        for ln in k['l']:
            pg = str(ln.get('cue', {}).get('p', ''))
            if pg and pg in RG and pg not in REG:
                seen = {}; REG[pg] = {}
                for b in RG[pg]:
                    seen[b['key']] = seen.get(b['key'], 0) + 1; key = b['key'] + (str(seen[b['key']]) if seen[b['key']] > 1 else '')
                    REG[pg][key] = {'b': b['box'], 'l': [[L[0], L[1], int(_given(pg, key, L))] for L in b['labs']], 'r': b.get('res')}
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
    if not page or not text or ln.get('who') not in ('B', 'P', 'Q', 'K', 'D', 'G', 'S') or str(c.get('r', '')).startswith('ex'): return []
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
for c in CH:   # her 9 Nov: animations that make an idea click (black-key groups lighting in turn, ...)
    for k in c.get('clips', []):
        for ln in k['l']:
            a_ = (ln.get('cue') or {}).get('anim')
            if a_: ln['lens'] = {'k': a_, 'at': [], 'full': True}; ln.pop('hits', None)
            pat = {'blacknames': r'[A-G] sharp', 'sharpflat': r'A (sharp|flat):'}.get(a_)
            if pat and _re.search(pat, ln.get('text') or ''):   # her 11 Nov: each pair of names lights as it is said
                text = ln['text']; sg = _segs(OUT + '/' + k['f'], ln['t0'], ln['t1'])
                s0, s1 = (sg[0][0], sg[-1][1]) if sg else (ln['t0'], ln['t1'] - 0.55)
                wt = [1 + (4 if ch == ',' else 7 if ch in '.:!?' else 0) for ch in text]; cum = [0]
                for w_ in wt: cum.append(cum[-1] + w_)
                ln['lens']['at'] = [round(s0 - ln['t0'] + (s1 - s0) * cum[m.start()] / cum[-1] - 0.1, 2) for m in _re.finditer(pat, text)][:5]
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
    if c['k'] not in _S.CH or c['k'].startswith(('T', 'B')): continue   # her 11 Nov: the moving staff and keys in every Part (Time has its own rhythm lens)
    sc = [ls for _, ls in _S.CH[c['k']][1]]
    for k, sl in zip(c.get('clips', []), sc):
        if len(sl) != len(k['l']): print('lens: line mismatch', c['k'], k['t']); continue
        for ln, src in zip(k['l'], sl):
            cue = ln.get('cue') or {}
            if ln.get('who') != 'piano' or ln.get('lens') or src[0] != 'piano' or '||' in src[1] or 'Ped' in src[1].split(): continue
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
# her 11 Nov: every chapter ends with two separate next steps: print its Workbook pages (paper), and a 10-question drill (screen)
# (chapter: [(drill id, drill name, level or 0)]); the workbook file is the chapter's own PDF from the Books page
DRILL = {
    'B1': [('posture-hands', 'Posture & Hand Shape', 0)],
    'G1': [('hb-nonchord', 'Notes outside the Chord', 0)],
    'P1': [('note-names', 'The Musical Alphabet', 1)], 'P2': [('whole-staff', 'Line and Space Names', 1)], 'P3': [('whole-staff', 'Find it on the keys', 7)],
    'P4': [('whole-staff', 'Landmark hop', 5), ('reading-steps', 'Steps & Skips', 2)], 'P5': [('ledger-lines', 'Ledger Lines', 3)], 'P6': [('accidentals', 'Accidentals', 1)],
    'P7': [('intervals', 'Intervals: count it', 1)], 'P8': [('intervals', 'Major or perfect?', 9)],
    'T1': [('pulse', 'Pulse & Counting', 1)], 'T2': [('note-values', 'Notes & Rests', 1)], 'T3': [('note-values', 'Dotted crotchets & quavers', 7)], 'T4': [('time-signatures', 'Time Signatures', 1)],
    'T5': [('six-eight', '3/4 or 6/8?', 3)], 'T6': [('rhythm', 'Rhythm Patterns', 1)], 'T7': [('hb-offbeat', 'Off the Beat', 0)], 'T8': [('signs', 'All the roads', 8)],
    'E1': [('dynamics', 'Dynamics', 1)], 'E2': [('dynamics', 'Articulation', 4)], 'E3': [('tempo', 'Tempo words', 2)], 'E4': [('hb-pedals', 'The Pedals', 0)], 'E5': [('hb-ornaments', 'Ornaments', 0)],
    'S1': [('scales', 'Build the scale', 3)], 'S2': [('minor-scales', 'Minor Scales', 0)], 'S3': [('key-signatures', 'Name the major key', 13)],
    'S4': [('key-signatures', 'Which key is the piece in?', 17)], 'S5': [('key-signatures', 'Sharps and flats: name the key', 15)],
    'H1': [('chords', 'Stack a triad', 1)], 'H2': [('chords', 'Major or minor?', 3)], 'H3': [('chords', 'I, IV or V', 8)], 'H4': [('harmony-3', 'Root position or first inversion?', 4)],
    'H5': [('hb-sevenths', 'Seventh Chords', 0)], 'H6': [('hb-colour', 'Colour Chords', 0)], 'H7': [('hb-tower', 'The Tower: 9, 11, 13', 0)], 'H8': [('hb-slash', 'Slash Chords', 0)],
    'M1': [('hb-guest', 'Chords from Outside the Key', 0)], 'M2': [('harmony-4', 'Which cadence?', 3)], 'M3': [('hb-melchords', 'Chords under a Melody', 0)], 'M4': [('hb-progressions', 'Progressions', 0)],
    'F1': [('melody', 'Question or answer?', 4)], 'F2': [('melody', 'Repetition or sequence?', 7)], 'F3': [('hb-texture', 'Texture', 0)], 'F4': [('hb-modulation', 'Changing Key', 0)],
    'F5': [('form', 'Binary or ternary?', 5)], 'F6': [('styles', 'Which period?', 3)],
    'L1': [('hand-positions', 'Hand Positions', 1)], 'L2': [('hb-practice', 'Practising Well', 0)], 'L3': [('reading-steps', 'Name the next note', 3)], 'L4': [('listen-write', 'Ear Training', 0)], 'L5': [('hb-performing', 'Performing', 0)],
}
_WBF = {'B': 'Before you play', 'P': 'Pitch', 'T': 'Time', 'E': 'Expression', 'S': 'Scales and keys', 'H': 'Chords and harmony', 'M': 'Chords and harmony', 'F': 'Shape and style', 'L': 'Playing and listening', 'G': 'Going further'}
_WBN = {'B': 0, 'P': 1, 'T': 2, 'E': 3, 'S': 4, 'H': 5, 'M': 6, 'F': 7, 'L': 8, 'G': 9}
import urllib.parse as _up
def _wb(key):
    p, i = key[0], int(key[1:]); d = '/mnt/user-data/outputs/books-latest/2 Workbook/' + _WBF[p]
    pre = f'workbook-{_WBN[p]}-{1 if p == "S" else i}-'
    f = [x for x in sorted(os.listdir(d)) if x.startswith(pre)] if os.path.isdir(d) else []
    if not f: return None
    pages = str(i) if p == 'S' else f'{2 * i - 1}–{2 * i}'
    return ['Claude outputs/Books - latest/2 Workbook/' + _up.quote(_WBF[p]) + '/' + f[0], ('p. ' if p == 'S' else 'pp. ') + pages, _WBF[p]]
for c in CH:
    if c['k'] in DRILL: c['nx'] = {'wb': _wb(c['k']), 'dr': DRILL[c['k']]}

shutil.copy('/tmp/claude-0/pk/read_warm.js', OUT + '/warm.js')
def _penlib():   # her 12 Nov: the app's own pen drawings (stool, elbows, hand), taken from drills.src.html each build so they never drift
    s = open('/tmp/claude-0/dr/drills.src.html').read().split('\n'); f = lambda pre: next(i for i, l in enumerate(s) if l.startswith(pre))
    a, b = f("const PEN_N = '#26296b'"), f("if (typeof module !== 'undefined' && module.exports) module.exports = { penPlace")
    c, d, h1, h2 = f('const penWho ='), f('const penLimbPair ='), f('const HAND_POSES = {'), f('const HAND_LENS =')
    pe = next(l for l in s if l.startswith('const pEase ='))
    return "const t = (en) => en; const LANG = 'en';\n" + pe + '\n' + '\n'.join(s[a:b] + s[c:d + 1] + s[h1:h2]) + '\nwindow.PEN_FING = ' + json.dumps({k: v.replace('<svg ', '<svg style="width:100%;height:auto;display:block" ', 1) for k, v in json.load(open('/tmp/claude-0/pk/posture_svgs.json')).items() if k.startswith('3:')}) + ';\n' + open('/tmp/claude-0/pk/read_penui.js').read()
open(OUT + '/pen.js', 'w').write(_penlib())   # her 11 Nov: the warm-up drawings for the lens
DATA = json.dumps(CH, ensure_ascii=False)
REGD = json.dumps(REG, ensure_ascii=False)
HTML = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="robots" content="noindex">
<title>Read and Listen</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Playfair+Display:wght@700;800&display=swap">
<style>
/* Layout: a reading desk. The page fills the left; the Butler's clips sit beside it (below it on a phone). */
:root{--bg:#ffffff;--panel:#ffffff;--ink:#26296b;--soft:#5a5d8f;--line:#e3e1ee;--accent:#e4572e;--accentbg:#fdece5;--paper:#ffffff;
 --display:'Playfair Display',Georgia,serif;--body:'Atkinson Hyperlegible',system-ui,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#14153a;--panel:#1e2050;--ink:#eceefe;--soft:#b3b5dc;--line:#33366e;--accent:#ff7a52;--accentbg:#3a2620;--paper:#f7f6f1;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#14153a;--panel:#1e2050;--ink:#eceefe;--soft:#b3b5dc;--line:#33366e;--accent:#ff7a52;--accentbg:#3a2620;--paper:#f7f6f1;color-scheme:dark}
html,body{margin:0} #veil{position:absolute;inset:0;pointer-events:none} #veil .vl{position:absolute;background:rgba(251,250,246,.93);border-radius:3px;display:flex;align-items:center;justify-content:center;font:italic 700 12px Georgia,serif;color:#a3a5c6;letter-spacing:.04em} .embed .top,.embed .prac{display:none!important} .embed .desk{padding-top:4px}
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
.hl{position:absolute;border:3px solid var(--accent);border-radius:8px;box-shadow:0 0 0 9999px rgba(20,22,60,.18);} .hl.fog{box-shadow:0 0 0 9999px rgba(255,255,255,.94)} .cov{position:absolute;background:#fff;border-radius:3px;pointer-events:none} .cov.res{background:#fff7f3;border:1.5px dashed #e4572e;display:flex;align-items:center;justify-content:center;font:700 clamp(9px,1.4vw,14px) var(--body);color:#e4572e} .hl{transition:all .5s ease;pointer-events:none}
.sub mark,#sub mark{background:#fde3d8;color:#26296b;border-radius:3px;padding:0 2px} .mk{position:absolute;width:3.2%;aspect-ratio:1;border-radius:50%;border:3px solid var(--accent);background:rgba(228,87,46,.25);transform:translate(-50%,-50%);pointer-events:none;animation:pop .35s ease}
@keyframes pop{from{transform:translate(-50%,-50%) scale(.4);opacity:0}to{transform:translate(-50%,-50%) scale(1);opacity:1}}
.sub{min-height:3.2em;margin-top:10px;background:var(--panel);border:1.5px solid var(--line);border-radius:12px;padding:8px 12px;font-size:15.5px}
.sub b{color:var(--accent);margin-right:6px} .sub:empty{display:none}
.ctl{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:0 0 10px} .ctl .btn{padding:6px 12px;font-size:14px} .ctl .sp{font-size:12.5px;padding:4px 7px;border-radius:999px} .ctl .sp.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.prac{margin-top:12px;border:1.5px solid var(--line);border-radius:12px;padding:10px 12px;display:flex;flex-direction:column;gap:6px} .prac .ph{font-size:11px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--accent)} .prac a{display:block;font-weight:700;font-size:14.5px;color:var(--ink);text-decoration:none;border:1.5px solid var(--line);border-radius:9px;padding:7px 10px;background:var(--bg)} .prac a b{display:block;font-size:11.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--soft)} .prac a span{display:block} .prac a.ndr{border-color:var(--accent)} .prac a.ndr b{color:var(--accent)} .prac a:hover{border-color:var(--accent)} .prac .nhint{margin:2px 0 0;font-size:12.5px;color:var(--soft)}
#lens:not(:empty){position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(255,255,255,.82);z-index:3;pointer-events:none}   /* her 9 Nov: one place to look - the lens in the middle, the page faded behind */
.lens{position:relative;width:90%;background:#fff;border:4px solid var(--accent);border-radius:22px;box-shadow:0 10px 30px rgba(20,22,60,.28);padding:6px 10px 2px;animation:lz .35s ease;z-index:3;pointer-events:none} .seek{margin:8px 0 10px} .seek .sr{display:flex;align-items:center;gap:8px} .seek input{flex:1;accent-color:#e4572e} .seek #tm{font:600 12px var(--body);color:#5a5d8f;min-width:76px;text-align:right} .seek .sb{display:flex;flex-wrap:wrap;gap:4px;margin-top:6px} .seek .sb .btn{font-size:12px;padding:4px 8px} .lens .lh{display:flex;align-items:center;gap:6px;font:700 clamp(10px,1.6vw,14px) var(--body);letter-spacing:.12em;text-transform:uppercase;color:#e4572e} .lens svg{display:block;width:100%;height:auto}
#lens .penl{pointer-events:auto;max-width:620px;max-height:96%;overflow:auto} .penw{padding:4px 2px 8px} .penw .pdraw{max-width:470px;margin:0 auto;background:#f6f6fb;border-radius:12px;padding:4px} .penw .pfront{max-width:300px} .penw .pfing{max-width:240px} .penw .pdraw svg{width:100%;height:auto;display:block} .pchips{display:flex;flex-wrap:wrap;gap:4px;margin:4px 0 6px} .pch{font:600 12.5px var(--body);border:1.5px solid #d9d7e8;background:#fff;color:#26296b;border-radius:14px;padding:3px 9px;cursor:pointer} .pch.on{background:#26296b;color:#fff;border-color:#26296b} .pch .px{color:#e4572e} .psl{display:grid;grid-template-columns:1fr 1fr;gap:4px 14px;margin:6px 0} .psl label{display:flex;flex-direction:column;font:700 12px var(--body);color:#26296b} .psl input{accent-color:#e4572e;width:100%} .pck{display:flex;flex-direction:column;gap:3px;font:13px/1.35 var(--body);color:#26296b} .pck>div{background:#f6f6fb;border-radius:7px;padding:4px 8px} .pck .ok b{color:#2e8a6e} .pck .no b{color:#c8361b} .pck span{color:#6d6f9c}
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
 <section class="reader"><a class="sheet" id="zoom" target="_blank" rel="noopener" title="Open the page full size"><div class="stage" id="stage"><img id="img" alt=""><div id="veil"></div><div id="ov"></div></div><div id="lens"></div></a><div class="sub" id="sub"></div>
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
  drawVeil();
}
// her 11 Nov: in a house room that teaches one step, the parts of the page for later steps are veiled ("later"); the Library shows the whole page
const ROWS = (new URLSearchParams(location.search).get('rows') || '').split(',').filter(Boolean);
const ROWWORDS = ['semibreve', 'minims', 'crotchets', 'quavers'];
function drawVeil() {
  const v = document.getElementById('veil'); if (!v) return; v.innerHTML = '';
  const c = CH[ci]; if (!c.slice) return; const pgn = c.pages[pi], R = REG[pgn]; if (!R) return;
  const keep = new Set(); c.clips.forEach(k => (k.l || []).forEach(l => { if (l.cue && l.cue.p === pgn) keep.add(l.cue.r); (l.hits || []).forEach(h => { if (h[4]) keep.add(h[4]); }); }));
  const box = (x, y, w, h) => `<div class="vl" style="left:${x * 100}%;top:${y * 100}%;width:${w * 100}%;height:${h * 100}%">later</div>`;
  let o = '';
  for (const [key, reg] of Object.entries(R)) {
    if (key === 'kick' || key.startsWith('h:') || key.startsWith('kick')) continue;
    const [x, y, w, h] = reg.b;
    if (!keep.has(key)) { o += box(x - .004, y - .003, w + .008, h + .006); continue; }
    if (!ROWS.length) continue;
    const heads = reg.l.filter(L => ROWWORDS.some(wd => L[0].endsWith(wd))).sort((a, b) => a[1][1] - b[1][1]);
    heads.forEach((L, i) => { const wd = ROWWORDS.find(w2 => L[0].endsWith(w2)); if (ROWS.includes(wd)) return;
      const top = L[1][1] - L[1][3] * 0.9, bot = i + 1 < heads.length ? heads[i + 1][1][1] - heads[i + 1][1][3] * 0.9 : y + h; o += box(x - .004, top, w + .008, bot - top); });
  }
  v.innerHTML = o;
}
function site(p) { const local = location.protocol === 'file:' || /thepianobutler\.com$/.test(location.hostname); return (local ? '../../' : 'https://thepianobutler.com/') + p; }
function drawSide() {
  const c = CH[ci];
  side.innerHTML = `<div class="kick">${c.part}</div><h2>${c.t}</h2>` + (c.clips ? `<button class="play" id="all"><svg width="18" height="18" viewBox="0 0 18 18"><path d="M4 2l12 7-12 7z" fill="currentColor"/></svg>${playing >= 0 ? 'Playing…' : c.slice ? 'Listen to this part' : 'Listen to the whole chapter'}</button><div class="ctl"><button class="btn" id="pp">${audio.paused ? '▶ Resume' : '❚❚ Pause'}</button>${[0.8, 1, 1.2, 1.5].map(v => `<button class="btn sp${v === rate ? ' on' : ''}" data-v="${v}">${v}×</button>`).join('')}</div><div class="seek"><div class="sr"><input type="range" id="sk" min="0" max="1000" value="0" aria-label="Position in this clip"${playing < 0 ? ' disabled' : ''}><span id="tm">0:00</span></div><div class="sb"><button class="btn" id="lprev" title="Previous line">⏮ Line</button><button class="btn" id="lagain" title="Hear this line again">↺ Again</button><button class="btn" id="b10">−10 s</button><button class="btn" id="f10">+10 s</button><button class="btn" id="lnext" title="Next line">Line ⏭</button></div></div><div class="clips">` +
    c.clips.map((k, i) => `<button class="clip${i === playing ? ' on' : ''}" data-i="${i}"><span class="n">${i + 1}</span><span>${k.t}</span><span class="s">${Math.floor(k.s / 60)}:${String(k.s % 60).padStart(2, '0')}</span></button>`).join('') + '</div>'
    : `<p class="none">No audio for this chapter yet. The pages are all here.</p>`) + (c.nx ? `<div class="prac"><div class="ph">Next steps</div>${c.nx.wb ? `<a class="nwb" href="${site(c.nx.wb[0].replace(/ /g, '%20'))}" target="_blank" rel="noopener"><b>1 · Workbook</b><span>Print ${c.nx.wb[1]} · ${c.nx.wb[2]}</span></a>` : ''}${c.nx.dr.map((d, i) => `<a class="ndr" href="${site('drills.html')}?drill=${d[0]}&tab=drill${d[2] ? '&level=' + d[2] : ''}" target="_blank" rel="noopener"><b>${c.nx.wb ? 2 + i : 1 + i} · Drill</b><span>${d[1]} · 10 questions</span></a>`).join('')}<p class="nhint">Workbook today, on paper. The drill tomorrow, and again the day after.</p></div>` : '') + `<label class="follow"><input type="checkbox" id="fol" ${follow ? 'checked' : ''}> Follow on the page</label><p class="who">The Butler explains, Clara asks. Each Example asks first, then pauses so you can try.</p>`;
  const fo = document.getElementById('fol'); if (fo) fo.onchange = () => { follow = fo.checked; };
  if (c.clips) { const pp = document.getElementById('pp'); pp.disabled = playing < 0; pp.onclick = () => { if (audio.paused) { audio.play().catch(() => {}); } else audio.pause(); drawSide(); };
    side.querySelectorAll('.sp').forEach(b => b.onclick = () => { rate = +b.dataset.v; audio.playbackRate = rate; drawSide(); });
    const L = () => (playing >= 0 ? CH[ci].clips[playing].l : []), li = () => { const t = audio.currentTime; let i = L().findIndex(x => t < x.t1); return i < 0 ? L().length - 1 : i; };
    const go = t => { if (playing < 0) return; audio.currentTime = Math.max(0, Math.min(t, (audio.duration || 1e9) - .05)); if (audio.paused) audio.play().catch(() => {}); };
    const sk = document.getElementById('sk'); sk.oninput = () => { if (audio.duration) go(sk.value / 1000 * audio.duration); };
    document.getElementById('b10').onclick = () => go(audio.currentTime - 10); document.getElementById('f10').onclick = () => go(audio.currentTime + 10);
    document.getElementById('lagain').onclick = () => { const l = L()[li()]; if (l) go(l.t0); };
    document.getElementById('lprev').onclick = () => { const i = li(), l = L(); if (!l.length) return; const cur = l[i]; go((audio.currentTime - cur.t0 > 1.2 || i === 0) ? cur.t0 : l[i - 1].t0); };
    document.getElementById('lnext').onclick = () => { const i = li(), l = L(); if (i + 1 < l.length) go(l[i + 1].t0); };
    document.getElementById('all').onclick = () => { chain = true; play(0); }; side.querySelectorAll('.clip').forEach(b => b.onclick = () => { chain = false; play(+b.dataset.i); }); }
}
function fmt(t) { t = Math.max(0, Math.floor(t || 0)); return Math.floor(t / 60) + ':' + String(t % 60).padStart(2, '0'); }
audio.addEventListener('timeupdate', () => { const sk = document.getElementById('sk'), tm = document.getElementById('tm'); if (!sk || !audio.duration) return; if (document.activeElement !== sk) sk.value = Math.round(audio.currentTime / audio.duration * 1000); tm.textContent = fmt(audio.currentTime) + ' / ' + fmt(audio.duration); });
function play(i) {
  const k = CH[ci].clips[i]; playing = i; audio.src = k.f; audio.playbackRate = rate; audio.play().catch(() => {});
  const p = CH[ci].pages.indexOf(k.p); if (p >= 0) { pi = p; showPage(); } drawSide(); mediaMeta();
}
// her 11 Nov: keep playing with the phone locked or the browser in the background, with play/pause/next on the lock screen
function mediaMeta() {
  if (!('mediaSession' in navigator) || playing < 0) return; const c = CH[ci], k = c.clips[playing];
  try { navigator.mediaSession.metadata = new MediaMetadata({ title: k.t, artist: 'The Piano Butler', album: c.t, artwork: [{ src: new URL('pages/p' + pad(k.p) + '.webp', location.href).href, sizes: '1000x1415', type: 'image/webp' }] }); } catch (e) {}
}
if ('mediaSession' in navigator) {
  const H = (a, f) => { try { navigator.mediaSession.setActionHandler(a, f); } catch (e) {} };
  H('play', () => { audio.play().catch(() => {}); }); H('pause', () => { audio.pause(); });
  H('previoustrack', () => { if (playing > 0) play(playing - 1); else audio.currentTime = 0; });
  H('nexttrack', () => { if (playing >= 0 && playing + 1 < CH[ci].clips.length) play(playing + 1); });
  H('seekbackward', (d) => { audio.currentTime = Math.max(0, audio.currentTime - ((d && d.seekOffset) || 10)); });
  H('seekforward', (d) => { audio.currentTime = Math.min(audio.duration || 1e9, audio.currentTime + ((d && d.seekOffset) || 10)); });
  H('seekto', (d) => { if (d && d.seekTime != null) audio.currentTime = d.seekTime; });
  audio.addEventListener('play', () => { navigator.mediaSession.playbackState = 'playing'; });
  audio.addEventListener('pause', () => { navigator.mediaSession.playbackState = 'paused'; });
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
  if (L.k === 'groups') return drawGroups(L);
  if (L.k === 'lines') return drawLinesAnim();
  if (L.k === 'stepskip') return drawStepSkip();
  if (L.k === 'sharpflat') return drawSharpFlat(L);
  if (L.k === 'blacknames') return drawBlackNames(L);
  if (L.k === 'ladder') return drawLadder();
  if (L.k === 'majmin') return drawMajMin();
  if (L.k === 'glasses') return drawGlasses();
  if (L.k === 'restack') return drawRestack();
  if (L.k.indexOf('warm-') === 0) return drawWarm(L.k.slice(5));
  if (L.k.indexOf('pen-') === 0) return drawPen(L.k.slice(4));
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
function drawAuto(L, t) {   // her 11 Nov: long tunes crowded the staff. Show about eight notes at a time, breaking at a bar line where possible
  const n0 = L.items.length; if (n0 <= 10) return drawAuto0(L, t);
  const br = L.bar || [], wins = []; let s0 = 0;
  while (s0 < n0) { let e = Math.min(n0, s0 + 8);
    if (e < n0) { for (let j = e; j > s0 + 4; j--) if (br[j] !== br[j - 1]) { e = j; break; } }
    if (n0 - e < 3) e = n0; wins.push([s0, e]); s0 = e; }
  const cur = L.at.filter(v => v <= t).length - 1; let wi = wins.findIndex(([a, e]) => cur >= a && cur < e); if (wi < 0) wi = 0;
  const [a, e] = wins[wi];
  return drawAuto0({ ...L, items: L.items.slice(a, e), at: L.at.slice(a, e), bar: br.slice(a, e) }, t);
}
function drawAuto0(L, t) {
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
function drawRhy(L, t) {   // her 11 Nov: long examples crowded the lens (notes on top of bar lines). Show two bars at a time, the bars being played, and move on
  const N0 = L.n || L.beats.length, BR = (L.bars || [0]).slice().sort((x, y) => x - y);
  if (N0 <= 8 || BR.length < 3) return drawRhy0(L, t);
  const st = BR[0] > 0 ? [0, ...BR] : BR, wins = []; let w0 = st[0];
  for (let i = 1; i <= st.length; i++) { const e = i < st.length ? st[i] : N0; if (e - w0 > 8.001 && st[i - 1] > w0) { wins.push([w0, st[i - 1]]); w0 = st[i - 1]; } }
  wins.push([w0, N0]);
  const cur = L.beats.filter(b => b[0] <= t).length - 1, cp = cur < 0 ? 0 : (L.beats[cur][3] == null ? cur : L.beats[cur][3]);
  let wi = wins.findIndex(([a, e]) => cp >= a - 1e-6 && cp < e - 1e-6); if (wi < 0) wi = cur < 0 ? 0 : wins.length - 1;
  const [a, e] = wins[wi], inW = p => p >= a - 1e-6 && p < e - 1e-6;
  const beats = L.beats.map((b, i) => [b[0], b[1], b[2], (b[3] == null ? i : b[3])]).filter(b => inW(b[3])).map(b => [b[0], b[1], b[2], b[3] - a]);
  const sub = { ...L, beats, notes: (L.notes || []).filter(n => inW(n[1])).map(n => [n[0], n[1] - a, Math.min(n[2], e - n[1]), n[3], n[4]]), ands: (L.ands || []).filter(x => inW(x[1])).map(x => [x[0], x[1] - a, x[2]]),
    bars: st.filter(x => x >= a - 1e-6 && x < e - 1e-6).map(x => x - a), n: e - a, win: `bars ${st.filter(x => x < a - 1e-6).length + 1}–${st.filter(x => x < e - 1e-6).length} of ${st.length}`, last: wi === wins.length - 1 };
  return drawRhy0(sub, t);
}
function drawRhy0(L, t) {
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
  g += `<line x1="${X(N) - 4}" x2="${X(N) - 4}" y1="${top}" y2="${bot}" stroke="${INK}" stroke-width="2"/>` + (L.last === false ? '' : `<line x1="${X(N) + 1}" x2="${X(N) + 1}" y1="${top}" y2="${bot}" stroke="${INK}" stroke-width="5"/>`);
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
    // short notes: beam all of one beat together (two beams for semiquavers, a 3 over a triplet), a lone one gets a flag
    const q = stems.filter(s => s[2] <= 0.75); const groups = [];
    q.forEach(s => { const g0 = groups[groups.length - 1], L0 = g0 && g0[g0.length - 1];
      if (L0 && s[0] === L0[0] + 1 && Math.floor(s[4] + 1e-6) === Math.floor(L0[4] + 1e-6)) g0.push(s); else groups.push([s]); });
    groups.forEach(G => { const hot = G.some(s => s[3] === ACC), col = hot ? ACC : G[0][3];
      if (G.length === 1) { const s0 = G[0]; g += gl(s0[2] <= 0.26 ? 'E242' : 'E240', s0[1] - 1, LY - SPc * 3.4, s0[3]); return; }
      const x1 = G[0][1] - 1, w = G[G.length - 1][1] - G[0][1] + 2;
      g += `<rect x="${x1}" y="${LY - SPc * 3.4}" width="${w}" height="${SPc * .5}" fill="${col}"/>`;
      if (G.every(s => s[2] <= 0.26)) g += `<rect x="${x1}" y="${LY - SPc * 3.4 + SPc * .8}" width="${w}" height="${SPc * .5}" fill="${col}"/>`;
      if (G.length === 3 && G.every(s => Math.abs(s[2] - 1 / 3) < .02)) g += `<text x="${x1 + w / 2}" y="${LY - SPc * 3.4 - 6}" text-anchor="middle" font-size="14" font-style="italic" font-weight="700" fill="${col}" ${F}>3</text>`; });
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
  const head = (hasN ? '♪ The beat and the notes' : '♪ The beat') + (L.win ? ' · ' + L.win : '');
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

function drawGroups(L) {   // the black keys light up group by group: every two starts on C, every three on F
  const key = 'groups'; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const N = 21, W = 26, H = 120, BH = 74, INK = '#26296b', ACC = '#e4572e', F = 'font-family="Atkinson Hyperlegible,sans-serif"';
  let g = '', bl = '', lab = '', d = 0;
  for (let i = 0; i < N; i++) g += `<rect x="${i * W}" y="0" width="${W}" height="${H}" fill="#fff" stroke="${INK}" stroke-width="1.4"/>`;
  for (let o = 0; o < 3; o++) {
    const b = o * 7;
    [[b, b + 1, 'two', ACC, b, 'C'], [b + 3, b + 5, 'three', '#5b6fd6', b + 3, 'F']].forEach(([s0, s1, nm, col, fk, ln], gi) => {
      const delay = (o * 2 + gi) * .55 + .3;
      for (let k = s0; k <= s1; k++) bl += `<rect x="${(k + 1) * W - W * .3}" y="0" width="${W * .6}" height="${BH}" rx="2" fill="${INK}"><animate attributeName="fill" from="${INK}" to="${col}" begin="${delay}s" dur=".3s" fill="freeze"/></rect>`;
      lab += `<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="${delay + .25}s" dur=".3s" fill="freeze"/><rect x="${fk * W + 1}" y="${BH + 4}" width="${W - 2}" height="${H - BH - 6}" fill="${col}" opacity=".22"/><text x="${fk * W + W / 2}" y="${H - 10}" text-anchor="middle" font-size="16" font-weight="700" fill="${col}" ${F}>${ln}</text></g>`;
    });
  }
  const svg = `<svg viewBox="-6 -30 ${N * W + 12} ${H + 40}" role="img" aria-label="Black keys in groups of two and three; C starts each two, F each three"><text x="0" y="-12" font-size="14" font-weight="700" fill="${ACC}" ${F}>two black keys: start on C</text><text x="${N * W}" y="-12" text-anchor="end" font-size="14" font-weight="700" fill="#5b6fd6" ${F}>three black keys: start on F</text>${g}${lab}${bl}</svg>`;
  lensShell(key, '♪ Two, three, two, three …', svg);
}

function drawLinesAnim() {   // lines 1-5 rise from the bottom, then spaces 1-4
  const key = 'lines'; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const INK = '#26296b', ACC = '#e4572e', F = 'font-family="Atkinson Hyperlegible,sans-serif"', SP = 26, Y = st => 30 + (8 - st) * SP / 2;
  let g = '';
  for (let k = 0; k < 5; k++) { const d = .3 + k * .45, y = Y(2 * k);
    g += `<line x1="120" x2="520" y1="${y}" y2="${y}" stroke="${INK}" stroke-width="2.2"/><g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="${d}s" dur=".25s" fill="freeze"/><line x1="120" x2="520" y1="${y}" y2="${y}" stroke="${ACC}" stroke-width="4"><animate attributeName="stroke" from="${ACC}" to="${INK}" begin="${d + .4}s" dur=".4s" fill="freeze"/></line><text x="108" y="${y + 6}" text-anchor="end" font-size="17" font-weight="700" fill="${INK}" ${F}>line ${k + 1}</text></g>`; }
  for (let k = 0; k < 4; k++) { const d = 2.7 + k * .45, y = Y(2 * k + 1);
    g += `<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="${d}s" dur=".25s" fill="freeze"/><rect x="122" y="${y - SP / 2 + 3}" width="396" height="${SP - 6}" fill="${ACC}" opacity=".14"/><text x="532" y="${y + 6}" font-size="17" font-weight="700" fill="${ACC}" ${F}>space ${k + 1}</text></g>`; }
  lensShell(key, '♪ Five lines, four spaces: from the bottom', `<svg viewBox="0 0 640 ${Y(0) + 26}" role="img" aria-label="Lines 1 to 5 and spaces 1 to 4, counted from the bottom">${g}</svg>`);
}
function drawPen(spec) {   // her 12 Nov: the app's moving posture and hand drawings; the voice sets the pose, the reader can press or drag
  if (!window.PEN) { if (!window.__penLoading) { window.__penLoading = 1; const sc = document.createElement('script'); sc.src = 'pen.js'; document.head.appendChild(sc); } return; }
  const [kind, target] = spec.split(':'), key = 'pen-' + kind;
  if (lensEl.dataset.k !== key || !lensEl.querySelector('.penw')) { lensEl.dataset.k = key; lensEl.dataset.p = '';
    lensShell(key, '♪ ' + ({ sit: 'Set up the stool · press or drag', front: 'Elbows, from the front · drag', hand: 'The hand from the side · press a shape', fing: 'Finger numbers · press a number' })[kind], '<div class="penw"></div>');
    lensEl.querySelector('.lens').classList.add('penl'); PEN.mount(kind, lensEl.querySelector('.penw')); }
  if (lensEl.dataset.p !== target) { lensEl.dataset.p = target; PEN.go(kind, target); }
}
function drawWarm(id) {   // her 11 Nov: the app's warm-up drawings, moving while the Butler explains them (frames in warm.js, loaded once)
  if (!window.WARM) { if (!window.__warmLoading) { window.__warmLoading = 1; const sc = document.createElement('script'); sc.src = 'warm.js'; document.head.appendChild(sc); } return; }
  const W = window.WARM[id]; if (!W) return; const key = 'warm-' + id;
  if (lensEl.dataset.k !== key) { lensEl.dataset.k = key; lensEl.dataset.t = ''; lensShell(key, '♪ ' + ({ ragdoll: 'Rag doll', wings: 'Elbow wings', glide: 'Arm glide', dive: 'Arm drop', bridge: 'Knuckle bridge', balloon: 'Wrist balloon' })[id], '<div class="wv" style="display:flex;justify-content:center"></div>'); }
  const ph = performance.now() % W.ms; let i = 0; while (i + 1 < W.f.length && W.f[i + 1][0] <= ph) i++;
  if (lensEl.dataset.t === String(i)) return; lensEl.dataset.t = String(i);
  const box = lensEl.querySelector('.wv'); if (box) box.innerHTML = W.f[i][1].replace('<svg ', '<svg style="width:100%;max-width:340px;max-height:240px;height:auto" ');
}
function drawRestack() {   // her 11 Nov: E G C restacked in thirds: the C on top slides to the bottom, and the layers line up as C E G
  const key = 'restack'; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const INK = '#26296b', ACC = '#e4572e', F = 'font-family="Atkinson Hyperlegible,sans-serif"';
  const tile = (lab, col, ys, xs) => `<g><animateTransform attributeName="transform" type="translate" values="${xs.map((x, i) => x + ' ' + ys[i]).join(';')}" keyTimes="0;.25;.55;.8;1" dur="4.4s" repeatCount="indefinite"/><rect x="-60" y="-22" width="120" height="44" rx="10" fill="${col}" stroke="${INK}" stroke-width="2.4"/><text x="0" y="9" text-anchor="middle" font-size="26" font-weight="700" fill="${INK}" ${F}>${lab}</text></g>`;
  // slots: top 50, middle 100, bottom 150 (y of the centre); C goes out to the side, down, and back in
  let g = tile('C', '#fde3d8', [50, 50, 150, 150, 50], [300, 420, 420, 300, 300]) + tile('G', '#eef0f8', [100, 100, 50, 50, 100], [300, 300, 300, 300, 300]) + tile('E', '#eef0f8', [150, 150, 100, 100, 150], [300, 300, 300, 300, 300]);
  g += `<text x="120" y="56" text-anchor="middle" font-size="16" font-weight="700" fill="${INK}" ${F}>E G C</text><text x="120" y="78" text-anchor="middle" font-size="13" fill="#5a5d8f" ${F}>not in thirds</text>`;
  g += `<text x="480" y="56" text-anchor="middle" font-size="16" font-weight="700" fill="${ACC}" ${F}>C E G</text><text x="480" y="78" text-anchor="middle" font-size="13" fill="#5a5d8f" ${F}>in thirds: C is the root</text>`;
  lensShell(key, '♪ Restack it in thirds', `<svg viewBox="0 0 600 190" role="img" aria-label="E G C restacked as C E G">${g}</svg>`);
}
function drawGlasses() {   // the same note on the bottom line: through treble glasses it is E, through bass glasses G
  const key = 'glasses'; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const INK = '#26296b', ACC = '#e4572e', F = 'font-family="Atkinson Hyperlegible,sans-serif"', SP = 24, Y = st => 34 + (8 - st) * SP / 2, H = SP / 2;
  let g = ''; for (let k = 0; k < 5; k++) g += `<line x1="40" x2="560" y1="${Y(2 * k)}" y2="${Y(2 * k)}" stroke="${INK}" stroke-width="2.2"/>`;
  g += `<ellipse cx="300" cy="${Y(0)}" rx="15" ry="11" transform="rotate(-20 300 ${Y(0)})" fill="${ACC}"/>`;
  const sw = (on) => `<animate attributeName="opacity" values="${on ? '1;1;0;0;1' : '0;0;1;1;0'}" keyTimes="0;.45;.5;.95;1" dur="3.2s" repeatCount="indefinite"/>`;
  g += `<g>${sw(true)}<path d="${GCLEF}" transform="translate(56 ${Y(2)}) scale(${H * 2 / 250} ${-H * 2 / 250})" fill="${INK}"/><text x="340" y="${Y(0) + 8}" font-size="30" font-weight="700" fill="${ACC}" ${F}>E</text><text x="420" y="${Y(8) - 12}" font-size="15" fill="#5a5d8f" ${F}>treble glasses</text></g>`;
  g += `<g opacity="0">${sw(false)}<path d="${FCLEF}" transform="translate(56 ${Y(6)}) scale(${H * 2 / 250} ${-H * 2 / 250})" fill="${INK}"/><text x="340" y="${Y(0) + 8}" font-size="30" font-weight="700" fill="${ACC}" ${F}>G</text><text x="420" y="${Y(8) - 12}" font-size="15" fill="#5a5d8f" ${F}>bass glasses</text></g>`;
  lensShell(key, '♪ Same line, different glasses', `<svg viewBox="0 0 600 ${Y(0) + 34}" role="img" aria-label="The bottom line is E in the treble clef and G in the bass clef">${g}</svg>`);
}

function drawStepSkip() {   // a note steps to the next line/space, then skips line to line
  const key = 'stepskip'; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const INK = '#26296b', ACC = '#e4572e', BL = '#5b6fd6', F = 'font-family="Atkinson Hyperlegible,sans-serif"', SP = 26, Y = st => 30 + (8 - st) * SP / 2;
  let g = ''; for (let k = 0; k < 5; k++) g += `<line x1="40" x2="600" y1="${Y(2 * k)}" y2="${Y(2 * k)}" stroke="${INK}" stroke-width="2.2"/>`;
  g += `<path d="${GCLEF}" transform="translate(52 ${Y(2)}) scale(${SP / 250} ${-SP / 250})" fill="${INK}"/>`;
  const nh = (x, st, col, extra = '') => `<ellipse cx="${x}" cy="${Y(st)}" rx="16" ry="12" transform="rotate(-20 ${x} ${Y(st)})" fill="${col}" ${extra}/>`;
  // step: G (line 2) -> A (space 2)
  g += nh(200, 2, INK) + `<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin=".6s" dur=".3s" fill="freeze"/>${nh(270, 3, ACC)}<path d="M200 ${Y(2) - 20} Q235 ${Y(3) - 56} 270 ${Y(3) - 18}" fill="none" stroke="${ACC}" stroke-width="3"/><text x="235" y="${Y(8) - 10}" text-anchor="middle" font-size="18" font-weight="700" fill="${ACC}" ${F}>step: G → A</text></g>`;
  // skip: G (line 2) -> B (line 3)
  g += nh(400, 2, INK) + `<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="2s" dur=".3s" fill="freeze"/>${nh(490, 4, BL)}<path d="M400 ${Y(2) - 20} Q445 ${Y(4) - 64} 490 ${Y(4) - 18}" fill="none" stroke="${BL}" stroke-width="3"/><text x="445" y="${Y(8) - 10}" text-anchor="middle" font-size="18" font-weight="700" fill="${BL}" ${F}>skip: G → B</text></g>`;
  lensShell(key, '♪ Step or skip', `<svg viewBox="0 0 640 ${Y(0) + 24}" role="img" aria-label="A step goes to the next line or space; a skip goes line to line">${g}</svg>`);
}

function drawSharpFlat(Lz) {   // her 11 Nov: no looping back and forth. Once, in time with the words: the sharp slides right and stays, then the flat slides left and stays
  const key = 'sharpflat'; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const INK = '#26296b', ACC = '#e4572e', BL = '#5b6fd6', F = 'font-family="Atkinson Hyperlegible,sans-serif"', W = 70, H = 190, BH = 118, N = 5;
  let g = ''; const L = 'CDEFG';
  for (let i = 0; i < N; i++) g += `<rect x="${i * W}" y="40" width="${W}" height="${H}" fill="${i === 1 ? '#eef0fb' : '#fff'}" stroke="${INK}" stroke-width="1.6"/><text x="${i * W + W / 2}" y="${40 + H - 12}" text-anchor="middle" font-size="18" font-weight="700" fill="${INK}" ${F}>${L[i]}</text>`;
  [0, 1, 3].forEach(i => g += `<rect x="${(i + 1) * W - W * .3}" y="40" width="${W * .6}" height="${BH}" rx="3" fill="${INK}"/>`);
  const dy = 40 + H - 50, by = 40 + BH - 26, T1 = (Lz && Lz.at && Lz.at.length === 2) ? Lz.at[0] : 6.6, T2 = (Lz && Lz.at && Lz.at.length === 2) ? Lz.at[1] : 9.9;
  g += `<circle cx="${1.5 * W}" cy="${dy}" r="14" fill="${INK}" opacity=".35"/>`;   // D stays marked
  g += `<circle cx="${1.5 * W}" cy="${dy}" r="14" fill="${ACC}" opacity="0"><set attributeName="opacity" to="1" begin="${T1}s" fill="freeze"/><animate attributeName="cx" from="${1.5 * W}" to="${2 * W}" begin="${T1}s" dur=".7s" fill="freeze"/><animate attributeName="cy" from="${dy}" to="${by}" begin="${T1}s" dur=".7s" fill="freeze"/></circle>`;
  g += `<text x="${2 * W + 8}" y="26" text-anchor="middle" font-size="20" font-weight="700" fill="${ACC}" opacity="0" ${F}>♯ one key right: D♯<animate attributeName="opacity" from="0" to="1" begin="${T1 + .5}s" dur=".4s" fill="freeze"/></text>`;
  g += `<circle cx="${1.5 * W}" cy="${dy}" r="14" fill="${BL}" opacity="0"><set attributeName="opacity" to="1" begin="${T2}s" fill="freeze"/><animate attributeName="cx" from="${1.5 * W}" to="${W}" begin="${T2}s" dur=".7s" fill="freeze"/><animate attributeName="cy" from="${dy}" to="${by}" begin="${T2}s" dur=".7s" fill="freeze"/></circle>`;
  g += `<text x="${W - 8}" y="${40 + H + 34}" text-anchor="middle" font-size="20" font-weight="700" fill="${BL}" opacity="0" ${F}>♭ one key left: D♭<animate attributeName="opacity" from="0" to="1" begin="${T2 + .5}s" dur=".4s" fill="freeze"/></text>`;
  lensShell(key, '♪ Sharp right, flat left', `<svg viewBox="-30 0 ${N * W + 60} ${H + 84}" role="img" aria-label="A sharp moves D one key right to D sharp; a flat moves it one key left to D flat">${g}</svg>`);
}
function drawBlackNames(Lz) {   // her 11 Nov: every black key has two names; they appear one by one as the Butler says them, and stay
  const key = 'blacknames'; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const INK = '#26296b', ACC = '#e4572e', BL = '#5b6fd6', F = 'font-family="Atkinson Hyperlegible,sans-serif"', W = 64, H = 200, BH = 124, N = 7, Y0 = 70;
  const L = 'CDEFGAB', BK = [[0, 'C♯', 'D♭'], [1, 'D♯', 'E♭'], [3, 'F♯', 'G♭'], [4, 'G♯', 'A♭'], [5, 'A♯', 'B♭']];
  const AT = (Lz && Lz.at && Lz.at.length === 5) ? Lz.at : [3.0, 6.0, 8.6, 11.2, 13.8];
  let g = '';
  for (let i = 0; i < N; i++) g += `<rect x="${i * W}" y="${Y0}" width="${W}" height="${H}" fill="#fff" stroke="${INK}" stroke-width="1.6"/><text x="${i * W + W / 2}" y="${Y0 + H - 12}" text-anchor="middle" font-size="18" font-weight="700" fill="${INK}" ${F}>${L[i]}</text>`;
  BK.forEach(([i, sh, fl], n) => { const x = (i + 1) * W, t = AT[n];
    g += `<rect x="${x - W * .3}" y="${Y0}" width="${W * .6}" height="${BH}" rx="3" fill="${INK}"><animate attributeName="fill" from="${INK}" to="${ACC}" begin="${t}s" dur=".3s" fill="freeze"/><animate attributeName="fill" from="${ACC}" to="#4a4e9c" begin="${t + 1.6}s" dur=".4s" fill="freeze"/></rect>`;
    g += `<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="${t}s" dur=".3s" fill="freeze"/><text x="${x}" y="${Y0 - 36}" text-anchor="middle" font-size="19" font-weight="700" fill="${ACC}" ${F}>${sh}</text><text x="${x}" y="${Y0 - 12}" text-anchor="middle" font-size="19" font-weight="700" fill="${BL}" ${F}>${fl}</text></g>`; });
  g += `<text x="${N * W / 2}" y="${Y0 + H + 30}" text-anchor="middle" font-size="17" fill="${INK}" opacity="0" ${F}>one key, two names: ♯ from the left neighbour, ♭ from the right<animate attributeName="opacity" from="0" to="1" begin="${AT[4] + 1.5}s" dur=".5s" fill="freeze"/></text>`;
  lensShell(key, '♪ Every black key has two names', `<svg viewBox="-20 0 ${N * W + 40} ${Y0 + H + 44}" role="img" aria-label="The five black keys and their two names: C sharp or D flat, D sharp or E flat, F sharp or G flat, G sharp or A flat, A sharp or B flat">${g}</svg>`);
}
function drawLadder() {   // interval numbers climb from C: 1 (unison) to 8 (octave), one key at a time
  const key = 'ladder'; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const INK = '#26296b', ACC = '#e4572e', F = 'font-family="Atkinson Hyperlegible,sans-serif"', W = 62, H = 170, BH = 104, N = 8, D = 0.55;
  const L = 'CDEFGABC', NM = ['unison', '2nd', '3rd', '4th', '5th', '6th', '7th', 'octave'];
  let g = '';
  for (let i = 0; i < N; i++) g += `<rect x="${i * W}" y="60" width="${W}" height="${H}" fill="${i === 0 ? '#fde3d8' : '#fff'}" stroke="${INK}" stroke-width="1.6"/><text x="${i * W + W / 2}" y="${60 + H - 12}" text-anchor="middle" font-size="17" font-weight="700" fill="${INK}" ${F}>${L[i]}</text>`;
  [0, 1, 3, 4, 5].forEach(i => g += `<rect x="${(i + 1) * W - W * .3}" y="60" width="${W * .6}" height="${BH}" rx="3" fill="${INK}"/>`);
  for (let i = 0; i < N; i++) { const t = (i * D).toFixed(2);
    g += `<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="${t}s" dur=".2s" fill="freeze"/><rect x="${i * W + 2}" y="${60 + BH + 4}" width="${W - 4}" height="${H - BH - 32}" fill="${ACC}" opacity=".22"/><circle cx="${i * W + W / 2}" cy="${60 + BH + 26}" r="15" fill="${ACC}"/><text x="${i * W + W / 2}" y="${60 + BH + 32}" text-anchor="middle" font-size="17" font-weight="700" fill="#fff" ${F}>${i + 1}</text><text x="${i * W + W / 2}" y="${i % 2 ? 22 : 44}" text-anchor="middle" font-size="15" font-weight="700" fill="${ACC}" ${F}>${NM[i]}</text></g>`; }
  lensShell(key, '♪ Count the notes from C', `<svg viewBox="-10 0 ${N * W + 20} ${H + 70}" role="img" aria-label="Interval numbers from C: unison, 2nd, 3rd up to octave">${g}</svg>`);
}
function drawMajMin() {   // C to E has 3 keys between; slide E down to E flat and only 2 are left
  const key = 'majmin'; if (lensEl.dataset.k === key) return; lensEl.dataset.k = key;
  const INK = '#26296b', ACC = '#e4572e', BL = '#5b6fd6', F = 'font-family="Atkinson Hyperlegible,sans-serif"', W = 70, H = 190, BH = 118, N = 5, T = 6;
  const L = 'CDEFG'; let g = '';
  for (let i = 0; i < N; i++) g += `<rect x="${i * W}" y="50" width="${W}" height="${H}" fill="#fff" stroke="${INK}" stroke-width="1.6"/><text x="${i * W + W / 2}" y="${50 + H - 12}" text-anchor="middle" font-size="18" font-weight="700" fill="${INK}" ${F}>${L[i]}</text>`;
  g += `<rect x="1" y="51" width="${W - 2}" height="${H - 2}" fill="${ACC}" opacity=".3"/>`;
  [0, 1, 3].forEach(i => g += `<rect x="${(i + 1) * W - W * .3}" y="50" width="${W * .6}" height="${BH}" rx="3" fill="${INK}"/>`);
  const kt = (a) => `keyTimes="0;.08;.12;.5;.58;.95;1" dur="${T}s" repeatCount="indefinite"`;
  // in-between keys: C# (1), D (2), D# (3: gone once E becomes E flat)
  [[W - 0 , 50 + 70, 1, 1], [1.5 * W, 50 + H - 46, 2, 1], [2 * W, 50 + 70, 3, 0]].forEach(([x, y, n, stays], j) => {
    const on = (j * .1 + .1).toFixed(2), on2 = (j * .1 + .12).toFixed(2);
    g += `<g opacity="0"><animate attributeName="opacity" values="0;0;1;1;${stays ? 1 : 0};${stays ? 1 : 0};0" keyTimes="0;${on};${on2};.5;.58;.95;1" dur="${T}s" repeatCount="indefinite"/><circle cx="${x}" cy="${y}" r="14" fill="#fff" stroke="${ACC}" stroke-width="2.5"/><text x="${x}" y="${y + 6}" text-anchor="middle" font-size="16" font-weight="700" fill="${ACC}" ${F}>${n}</text></g>`; });
  // the top note: E (white) slides left onto E flat (the black key)
  g += `<rect y="${50 + H - 80}" width="${W - 8}" height="30" rx="8" fill="${ACC}" opacity=".85"><animate attributeName="x" values="${2 * W + 4};${2 * W + 4};${2 * W + 4};${2 * W + 4};${2 * W - W * .3 + 4 - 0};${2 * W - W * .3 + 4};${2 * W + 4}" ${kt()}/><animate attributeName="y" values="${50 + H - 80};${50 + H - 80};${50 + H - 80};${50 + H - 80};${50 + 30};${50 + 30};${50 + H - 80}" ${kt()}/><animate attributeName="width" values="${W - 8};${W - 8};${W - 8};${W - 8};${W * .6 - 8};${W * .6 - 8};${W - 8}" ${kt()}/></rect>`;
  g += `<text x="${N * W / 2}" y="30" text-anchor="middle" font-size="20" font-weight="700" fill="${ACC}" ${F}>C to E: 3 between, a major 3rd<animate attributeName="opacity" values="0;0;1;1;0;0;0" keyTimes="0;.3;.34;.5;.54;.95;1" dur="${T}s" repeatCount="indefinite"/></text>`;
  g += `<text x="${N * W / 2}" y="30" text-anchor="middle" font-size="20" font-weight="700" fill="${BL}" opacity="0" ${F}>C to E♭: 2 between, a minor 3rd<animate attributeName="opacity" values="0;0;0;0;1;1;0" keyTimes="0;.3;.5;.56;.62;.95;1" dur="${T}s" repeatCount="indefinite"/></text>`;
  lensShell(key, '♪ One key fewer between', `<svg viewBox="-20 0 ${N * W + 40} ${H + 60}" role="img" aria-label="C to E has three keys between; E slides down to E flat and only two are left">${g}</svg>`);
}
function tick() {
  if (playing < 0) return; const k = CH[ci].clips[playing], t = audio.currentTime; const ln = k.l.find(x => t >= x.t0 && t < x.t1);
  if (!ln) { requestAnimationFrame(tick); return; }
  drawLens(follow ? ln.lens : null, t);
  const hit = ln.hits ? ln.hits.filter(h => h[0] <= t).pop() : null; let txt = ln.text || ''; if (hit) txt = txt.slice(0, hit[2]) + '<mark>' + txt.slice(hit[2], hit[3]) + '</mark>' + txt.slice(hit[3]);
  sub.innerHTML = ln.text ? `<b>${({B: 'Butler', P: 'Clara', Q: '♕ Queen', K: '♔ King', D: 'Doorkeeper', G: 'Guest', S: 'Stationmaster'})[ln.who] || ''}</b>${txt}` : (ln.who === 'piano' ? '<b>♪</b>listen' : '');
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
        const covers = exm ? reg.l.filter(L => !L[2] && !vis.has(L[0])).map(L => `<div class="cov" style="left:${L[1][0] * 100 - .3}%;top:${L[1][1] * 100 - .2}%;width:${L[1][2] * 100 + .6}%;height:${L[1][3] * 100 + .4}%"></div>`).join('') + (reg.r ? `<div class="cov res" style="left:${reg.r[0] * 100}%;top:${reg.r[1] * 100}%;width:${reg.r[2] * 100}%;height:${reg.r[3] * 100}%">Answer coming…</div>` : '') : '';
        ov.innerHTML = covers + `<div class="hl${/^ex/.test(c.r) ? ' fog' : ''}" style="left:${x * 100 - .6}%;top:${y * 100 - .4}%;width:${w * 100 + 1.2}%;height:${h * 100 + .8}%"></div>` +
          marks.map(m => findLab(reg, m)).filter(Boolean).map(L => `<div class="mk" style="left:${(L[1][0] + L[1][2] / 2) * 100}%;top:${(L[1][1] + L[1][3] / 2) * 100}%;width:${Math.max(3.2, L[1][2] * 100 + 2.4)}%"></div>`).join(''); }
    }
  } else if (!c || !follow) { stage.style.transform = ''; ov.innerHTML = ''; ov.dataset.k = ''; }
  requestAnimationFrame(tick);
}
audio.onplay = () => { requestAnimationFrame(tick); drawSide(); }; audio.onpause = () => { if (playing >= 0) drawSide(); };
audio.onended = () => { const c = CH[ci]; if (chain && playing + 1 < c.clips.length) play(playing + 1); else { if (playing === c.clips.length - 1) { try { parent.postMessage({ pb: 'read-done', ch: c.k }, '*'); } catch (e) {} } playing = -1; drawSide(); clearFollow(); } };
function go(i, p = 0) { audio.pause(); playing = -1; if (typeof clearFollow === 'function') clearFollow(); ci = i; pi = p; sel.value = i; showPage(); drawSide(); history.replaceState(null, '', '#' + CH[i].k); window.scrollTo(0, 0); }
sel.onchange = () => go(+sel.value);
document.getElementById('prev').onclick = () => { if (pi > 0) { pi--; showPage(); } else if (ci > 0) go(ci - 1, CH[ci - 1].pages.length - 1); };
document.getElementById('next').onclick = () => { if (pi < CH[ci].pages.length - 1) { pi++; showPage(); } else if (ci < CH.length - 1) go(ci + 1); };
document.addEventListener('keydown', e => { if (e.target.tagName === 'SELECT') return; if (e.key === 'ArrowRight') document.getElementById('next').click(); if (e.key === 'ArrowLeft') document.getElementById('prev').click(); });
const start = CH.findIndex(c => c.k === (location.hash.slice(1) || new URLSearchParams(location.search).get('ch') || 'P1'));
// her 11 Nov: inside a house room (drills.html) the chapter plays right there: no header, no next steps (the room has them), and the room learns our height
const EMBED = new URLSearchParams(location.search).get('embed') === '1';
if (EMBED) { document.documentElement.classList.add('embed'); const tell = () => { try { parent.postMessage({ pb: 'read-h', h: document.documentElement.scrollHeight }, '*'); } catch (e) {} }; try { new ResizeObserver(tell).observe(document.body); } catch (e) {} setInterval(tell, 1500); tell(); }
// her 11 Nov: a house room plays a slice of its chapter (?clips=1,2,5): only those clips, on their pages, with a link to the whole chapter
const SLICE = (new URLSearchParams(location.search).get('clips') || '').split(',').map(Number).filter(n => n > 0);
if (SLICE.length && start >= 0 && CH[start].clips) {
  const c = CH[start], keep = SLICE.filter(n => n <= c.clips.length).map(n => c.clips[n - 1]);
  if (keep.length) {
    const pg = new Set(); keep.forEach(k => { const cp = (k.l || []).filter(l => l.cue && l.cue.p).map(l => l.cue.p); if (cp.length) cp.forEach(x => pg.add(x)); else pg.add(k.p); });   // the pages the voice actually points at
    c.part = c.part + ' · ' + (keep.length < c.clips.length ? 'this room’s part' : 'whole chapter'); c.clips = keep; c.pages = [...pg].sort((a, b) => a - b); c.slice = true;   // a slice may borrow a page from another chapter (the dotted minim, p. 56)
  }
}
go(start >= 0 ? start : 0);
</script></body></html>'''
open(OUT + '/index.html', 'w').write(HTML.replace('__DATA__', DATA).replace('__REG__', REGD))
print('ok read page', len(CH), 'sections,', sum(1 for c in CH if c.get('clips')), 'with audio, last page', LAST)
