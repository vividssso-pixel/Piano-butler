# Her 16 Nov ("point, pop up or animate as it is said, 최상으로"): fine marks for Read & listen.
# For every spoken line, find what it talks about on the page and when:
#   hi   the words on the page that the voice is saying (a highlighter stroke, phrase by phrase)
#   key  the keys a line names (C, D and E...) or a piano line plays, lit one by one at the moment they are said or heard
#   blk  the black keys when the line is about them (twos and threes)
# Times inside a line are estimated from the position in the sentence (the TTS speaks at an even pace).
# Input: pagemarks.json (pagemarks.js); output: mk lists added to the lines of CH (read2 data).
import json, re
PM = json.load(open('/tmp/claude-0/pk/pagemarks.json'))
STOP = set('a an the and or of to is it in on at so for be this that these those with as by from you your i we they he she them its are was were do does not no but then now just here there what which who how one each every all any'.split())
WHITE = 'CDEFGAB'

def norm(w): return re.sub(r'[’\'-]', '', w.lower())
def words_of(text): return [(m.group(0), m.start()) for m in re.finditer(r"[A-Za-z0-9♯♭’'-]+", text)]

def page_seq(pg):
    out = []
    for b in PM.get(str(pg), {}).get('words', []):
        for i, w in enumerate(b['ws']): out.append((b['b'], i, norm(w['w']), w['r']))
    return out

def merge_rects(rs):   # one rect per printed line
    lines = []
    for r in rs:
        for L in lines:
            if abs(L[1] - r[1]) < r[3] * 0.5: L[0], L[2] = min(L[0], r[0]), max(L[0] + L[2], r[0] + r[2]) - min(L[0], r[0]); L[3] = max(L[3], r[3]); break
        else: lines.append(list(r))
    return [[round(v, 4) for v in L] for L in lines]

def inside(r, reg, slack=0.02):
    if not reg: return True
    x, y, w, h = r; X, Y, W, H = reg
    return x + w / 2 > X - slack and x + w / 2 < X + W + slack and y + h / 2 > Y - slack and y + h / 2 < Y + H + slack

def find_text(phrase, pg, reg):
    """The run of page words that says this phrase (at least two content words, most of them)."""
    ph = [norm(w) for w, _ in words_of(phrase)]
    content = [w for w in ph if w not in STOP and (len(w) > 1 or w.upper() in WHITE)]
    if len(content) < 2: return None
    seq = page_seq(pg); best = None
    n = len(ph)
    for i in range(len(seq)):
        for L in (max(2, int(n * 0.6)), n, int(n * 1.4) + 1):
            win = seq[i:i + L]
            if not win or win[0][0] != win[-1][0] and L > n: continue
            got = [w for w in win if w[2] in content]
            uniq = len(set(w[2] for w in got)); score = uniq / len(set(content))
            inr = sum(inside(w[3], reg) for w in win) / len(win)
            if (inr >= 0.5 and uniq >= 2 and score >= 0.4) or (uniq >= 3 and score >= 0.72):   # outside the cued part: only a clear match
                a = win.index(got[0]); z = len(win) - 1 - win[::-1].index(got[-1]); run = win[a:z + 1]
                tight = uniq / len(run)
                key = (sum(inside(w[3], reg) for w in run) / len(run) >= 0.5, score, tight)
                if not best or key > best[0]: best = (key, run)
    if not best: return None
    return merge_rects([w[3] for w in best[1]])

def find_item(item, pg, reg):
    """A short list item (a chapter name, a sign's name): all its words, in order, close together on the page."""
    ws = [norm(w) for w, _ in words_of(item)]; cw = [w for w in ws if w not in STOP] or ws
    if not cw or (len(cw) == 1 and len(cw[0]) < 3): return None
    seq = page_seq(pg); best = None
    for i in range(len(seq)):
        if seq[i][2] != cw[0]: continue
        j, k = i, 0; run = []
        while j < len(seq) and k < len(cw) and j - i <= len(ws) + 2 and seq[j][0] == seq[i][0]:
            if seq[j][2] == cw[k]: k += 1
            run.append(seq[j]); j += 1
        if k == len(cw):
            sc = (inside(run[0][3], reg), -len(run))
            if not best or sc > best[0]: best = (sc, run)
    return merge_rects([w[3] for w in best[1]]) if best else None

def key_letters(kb):   # each white key's letter: printed, or worked out from where the black keys sit
    wh = kb['white']; names = [w['n'] for w in wh]
    if all(names): return names
    bl = [b['r'] for b in kb['black']]
    has = [any(abs((b[0] + b[2] / 2) - (w['r'][0] + w['r'][2])) < w['r'][2] * 0.35 for b in bl) for w in wh]   # a black key on its right edge
    pat = [l in 'CDFGA' for l in WHITE]
    for off in range(7):
        if all(has[i] == pat[(i + off) % 7] for i in range(len(wh) - 1)):
            guess = [WHITE[(i + off) % 7] for i in range(len(wh))]
            if all(n is None or n == g for n, g in zip(names, guess)): return guess
    return names

LMK = re.compile(r'\b(Very High|Very Low|Lowest|Highest|Middle|Bass|Treble|Low|High)\s+C\b')
LMK_OCT = {'Lowest': 1, 'Low': 2, 'Bass': 3, 'Middle': 4, 'Treble': 5, 'High': 6, 'Very High': 7, 'Highest': 8}
def landmarks(ph):   # char position of the C -> its name ("Middle C" names one key, not any C)
    return {mm.end() - 1: mm.group(1) for mm in LMK.finditer(ph)}
def pick_landmark(name, kbs, reg):
    best = None
    for kb in kbs:
        for w in kb['white']:
            if w.get('tag') == name + ' C':
                sc = inside(kb['r'], reg, 0.05)
                if not best or sc > best[0]: best = (sc, w['r'])
    return best[1] if best else None
def pick_keys(letters, kbs, reg, prefer_small=True):
    """Keys for a list of letters: a run of neighbours if the letters run in order, else the nearest of each."""
    cands = []
    for kb in kbs:
        names = key_letters(kb)
        if not all(l in names for l in letters): continue
        runs = []
        for s in range(len(names)):
            for d in (1, -1):
                idx = [s + d * j for j in range(len(letters))]
                if all(0 <= i < len(names) and names[i] == letters[j] for j, i in enumerate(idx)): runs.append(idx)
        mid = next((i for i, w in enumerate(kb['white']) if w.get('tag') == 'Middle C'), (len(names) - 1) / 2)
        run = min(runs, key=lambda r: abs(min(r) - mid)) if runs else None   # a run of letters: the one starting nearest Middle C
        if not run:
            run = []; last = None
            for l in letters:
                opts = [i for i, n in enumerate(names) if n == l]
                i = min(opts, key=lambda o: abs(o - last)) if last is not None else opts[len(opts) // 2]
                run.append(i); last = i
        score = (inside(kb['r'], reg, 0.05), bool(run) and all(abs(run[j + 1] - run[j]) == 1 for j in range(len(run) - 1)), -len(names) if prefer_small else len(names))
        cands.append((score, [kb['white'][i]['r'] for i in run]))
    if not cands: return None
    return max(cands, key=lambda c: c[0])[1]

NOTE = re.compile(r'([A-G])([#b♯♭]?)(\d)')
def piano_keys(spec, kbs, reg):
    notes = [m for m in NOTE.findall(spec)]
    if not notes or any(acc for _, acc, _ in notes): return None   # black-key tunes: the pop shows them
    seq = [l for l, _, _ in notes]; pitch = [int(o) * 7 + WHITE.index(l) for l, _, o in notes]
    best = None
    for kb in kbs:
        names = key_letters(kb)
        if not all(names) or not inside(kb['r'], reg, 0.05): continue
        anc = next(((i, w['tag']) for i, w in enumerate(kb['white']) if w.get('tag')), None)
        if anc:   # the picture names a C (Middle C...): every key's real pitch is known, so each note goes to its own key
            i0, nm = anc; p0 = LMK_OCT[nm[:-2]] * 7
            idx = [i0 + p - p0 for p in pitch]
            if all(0 <= i < len(names) for i in idx):
                sc = (True, 99)
                if not best or sc > best[0]: best = (sc, [(kb['white'][i]['r'], names[i]) for i in idx])
            continue
        lo = min(pitch); span = max(pitch) - lo
        if span < len(names):   # it fits: line the notes up on the matching letters, nearest the middle
            offs = [s for s in range(len(names) - span) if names[s] == WHITE[lo % 7]]
            if not offs: continue
            s = min(offs, key=lambda o: abs(o + span / 2 - len(names) / 2)); idx = [s + p - lo for p in pitch]
        else:                   # wider than the picture: lowest to the left-most such key, highest to the right-most
            idx = []
            for l, p in zip(seq, pitch):
                opts = [i for i, n in enumerate(names) if n == l]; f = (p - lo) / span if span else 0
                if not opts: idx = None; break
                idx.append(min(opts, key=lambda o: abs(o / max(1, len(names) - 1) - f)))
            if idx is None: continue
        sc = (len(names) >= span + 1, -abs(len(names) - span))
        if not best or sc > best[0]: best = (sc, [(kb['white'][i]['r'], names[i]) for i in idx])
    return best[1] if best else None

def region_notes(pg, reg):
    return [n for n in PM.get(str(pg), {}).get('notes', []) if inside(n['r'], reg, 0.03)]

def pick_notes(letters, notes, accs=None):
    """Noteheads for named letters: a run in order along one staff if there is one, else the first of each, left to right."""
    best = None
    for st in sorted(set(n['st'] for n in notes)):
        row = [n for n in notes if n['st'] == st]; names = [n['n'] + (n.get('acc') or '') for n in row] if accs and any(accs) else [n['n'] for n in row]
        if accs and any(accs): letters = [l + a for l, a in zip(letters, accs)]
        for s0 in range(len(row)):
            for d in (1, -1):
                idx = [s0 + d * j for j in range(len(letters))]
                if all(0 <= i < len(row) and names[i] == letters[j] for j, i in enumerate(idx)):
                    return [row[i] for i in idx]
        if best is None and all(l in names for l in letters):
            out = []; start = 0
            for l in letters:
                i = next((k for k in range(start, len(row)) if names[k] == l), None)
                if i is None: i = names.index(l)
                out.append(row[i]); start = i + 1
            best = out
    return best

def piano_notes(spec, notes):   # the played notes, matched by pitch, left to right
    want = [(l, {'': '', '#': '#', '♯': '#', 'b': 'b', '♭': 'b'}[acc], int(o)) for l, acc, o in NOTE.findall(spec)]
    if not want: return None
    out = []; start = 0
    for l, a, o in want:
        i = next((k for k in range(start, len(notes)) if notes[k]['n'] == l and notes[k]['o'] == o and (notes[k].get('acc') or '') == a), None)
        if i is None: return None
        out.append(notes[i]); start = i + 1
    return out

def is_article(ph, i):   # "A whole tune" is an article; "F, G, A and B", "A again", "A to G" are keys
    if ph[i] != 'A': return False
    m = re.match(r'A\s+([A-Za-z]+)', ph[i:]); nxt = m.group(1) if m else ''
    before = ph[:i].rstrip()
    if before.endswith(',') or re.search(r'\b[B-G]$', before): return False
    return bool(nxt) and nxt[0].islower() and nxt not in ('and', 'or', 'to', 'again')
def groups(kb):   # the black keys in their groups of two and three
    bl = sorted((b['r'] for b in kb['black']), key=lambda r: r[0]); ww = kb['white'][0]['r'][2] if kb['white'] else 0.02; out = []
    for r in bl:
        if out and r[0] - (out[-1][-1][0] + out[-1][-1][2]) < ww * 0.9: out[-1].append(r)
        else: out.append([r])
    return out
import subprocess, functools
@functools.lru_cache(maxsize=64)
def envelope(path):   # 10 ms RMS of the clip
    import numpy as np
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', path, '-f', 's16le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, dtype=np.int16).astype(np.float32); n = len(a) // 160
    return np.sqrt((a[:n * 160].reshape(n, 160) ** 2).mean(1)) if n else np.zeros(1)
def gaps(path, t0, t1, min_ms=120):   # silent stretches inside a line (centres, seconds)
    import numpy as np
    e = envelope(path); a, z = int(t0 * 100), min(len(e), int(t1 * 100))
    if z - a < 20: return []
    seg = e[a:z]; thr = max(120.0, float(np.percentile(seg, 60)) * 0.12); quiet = seg < thr; out = []; i = 0
    while i < len(quiet):
        if quiet[i]:
            j = i
            while j < len(quiet) and quiet[j]: j += 1
            if (j - i) * 10 >= min_ms and i > 5 and j < len(quiet) - 5: out.append(((a + i + a + j) / 2) / 100)
            i = j
        else: i += 1
    return out

_DEC = None
_AL = {}
def align(path, t0, t1, text):
    """Word start times for a spoken line, by forced alignment of its known text (PocketSphinx). Returns [(char_pos, time)] or None."""
    global _DEC
    key = (path, round(t0, 2), text)
    if key in _AL: return _AL[key]
    try:
        from pocketsphinx import Decoder
        if _DEC is None: _DEC = Decoder(samprate=16000, bestpath=False, loglevel='FATAL')
        toks = [(mm.start(), mm.group(0).lower().replace('’', "'")) for mm in re.finditer(r"[A-Za-z’']+", text)]
        keep = [(p, w) for p, w in toks if _DEC.lookup_word(w) is not None]
        if len(keep) < max(1, len(toks) * 0.6): _AL[key] = None; return None
        raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', path, '-ss', str(max(0, t0 - 0.05)), '-to', str(t1 + 0.1), '-f', 's16le', '-ac', '1', '-ar', '16000', '-'], capture_output=True).stdout
        _DEC.set_align_text(' '.join(w for _, w in keep))
        _DEC.start_utt(); _DEC.process_raw(raw, full_utt=True); _DEC.end_utt()
        seg = [s for s in _DEC.seg() if s.word not in ('<sil>', '<s>', '</s>', '[NOISE]')]
        if len(seg) != len(keep): _AL[key] = None; return None
        res = [(p, round(max(0, t0 - 0.05) + s.start_frame / 100, 2)) for (p, _), s in zip(keep, seg)]
    except Exception:
        res = None
    _AL[key] = res; return res
PUNCT = re.compile(r'[.?!:;,]')
def timer(text, t0, t1, path=None):
    al = align(path, t0, t1, text) if path else None
    if al:   # the time of the word holding (or just after) a character, shown a breath early
        def at_al(ch):
            for p, t in al:
                if p >= ch - 1: return round(max(t0, t - 0.08), 2)
            return round(t1 - 0.2, 2)
        at_al.aligned = True
        return at_al
    return timer_est(text, t0, t1, path)
def timer_est(text, t0, t1, path=None):
    """Time of a character position in a spoken line: the pauses heard in the audio are pinned to the punctuation."""
    W = {',': 5, ';': 8, ':': 8, '.': 11, '?': 11, '!': 11}
    marks = [(m.start(), W[m.group(0)]) for m in PUNCT.finditer(text) if m.end() < len(text.rstrip())]
    # weighted length: punctuation counts as extra characters (a short pause)
    def wpos(ch): return ch + sum(w for p, w in marks if p < ch)
    total = wpos(len(text)); lead, tail = t0 + 0.15, t1 - 0.25
    anchors = [(0, lead), (len(text), tail)]
    g = gaps(path, t0, t1) if path else []
    big = [p for p, w in marks if w >= 8] or [p for p, w in marks]
    if g and big:   # pin each heard pause to the nearest expected one, in order
        est = [(p, lead + (tail - lead) * wpos(p) / total) for p in big]; used = set()
        for gt in g:
            cand = [(abs(e - gt), p) for p, e in est if p not in used and abs(e - gt) < 1.2]
            if cand: d, p = min(cand); used.add(p); anchors.append((p + 1, gt))
    anchors.sort()
    def at(ch):
        for (c0, a0), (c1, a1) in zip(anchors, anchors[1:]):
            if c0 <= ch <= c1: return round(a0 + (a1 - a0) * (wpos(ch) - wpos(c0)) / max(1, wpos(c1) - wpos(c0)), 2)
        return round(tail, 2)
    return at
def tag(out, pop):
    for x in out:   # long enough to be seen (her 16 Nov audit): a highlight at least 1 s, a key or note at least 0.8 s
        x['e'] = round(max(x['e'], x['t'] + (1.0 if x['k'] == 'hi' else 0.8)), 2)
    if pop:
        for m in out: m['pop'] = pop
    return out
LETTERS = re.compile(r'\b([A-G])(?:\s+(sharp|flat)\b|([♯♭]))?(?![a-z\'’])')
def acc_of(x): return '#' if (x.group(2) == 'sharp' or x.group(3) == '♯') else 'b' if (x.group(2) == 'flat' or x.group(3) == '♭') else ''
def line_marks(ln, prev_reg_kbs=None, spec=None, REG=None, audio=None, answered=True):
    c = ln.get('cue') or {}; pg = c.get('p'); r = c.get('r', '')
    pop = None
    if r.startswith('pop'):   # a worked example: its keys light on the pop-up picture, but only once the question has been tried
        src = (ln.get('lens') or {}).get('src', ''); m0 = re.search(r'pops/([A-Z]+\d+-\d+)', src)
        if not m0 or not answered or ('pop:' + m0.group(1)) not in PM: return []
        pop = m0.group(1); reg = None; kbs = PM['pop:' + pop]['kbs']
    else:
        if not pg: return []
        reg = ((REG or {}).get(str(pg), {}).get(r) or {}).get('b')
        kbs = PM.get(str(pg), {}).get('kbs', [])
    t0, t1 = ln['t0'], ln['t1']; out = []
    if ln.get('who') == 'piano' and spec and ln.get('notes'):
        if True:
            ns = piano_notes(spec, PM['pop:' + pop].get('notes', []) if pop else region_notes(pg, reg))
            if ns:
                for t, n in zip(ln['notes'], ns): out.append({'k': 'nt', 't': round(t, 2), 'e': round(t1, 2), 'p': pg, 'r': [n['r']], 'n': n['n'] + {'#': '♯', 'b': '♭'}.get(n.get('acc') or '', '')})
        ks = piano_keys(spec, kbs, reg)
        if ks:
            for t, (k, nm) in zip(ln['notes'], ks): out.append({'k': 'key', 't': round(t, 2), 'e': round(t1, 2), 'p': pg, 'r': [k], 'n': nm, 'snd': 1})
        return tag(out, pop)
    text = ln.get('text') or ''
    if not text: return []
    at = timer(text, t0, t1, audio); END = round(t1 + 0.4, 2)
    phr = [m for m in re.finditer(r'[^.?!:;]+[.?!:;]*', text) if len(m.group(0).strip()) >= 3]
    for j, m in enumerate(phr):   # phrase by phrase; a highlight stays until the next phrase starts
        ph = m.group(0).strip()
        a, z = at(m.start()), at(m.end())
        hi = None if pop else find_text(ph, pg, reg)
        nxt = at(phr[j + 1].start()) if j + 1 < len(phr) else END
        items = [x for x in re.finditer(r'[^,]+', m.group(0))]
        if not pop and len(items) >= 3:   # a list said aloud (chapter names, signs): each item lights as it is said
            got = []
            for it in items:
                whole = it.group(0).strip(' .:;?!')
                whole = re.sub(r'^(and|or)\s+', '', whole)
                r_ = find_item(whole, pg, reg) if len(whole) >= 3 else None
                if r_: got.append((at(m.start() + it.start() + max(0, it.group(0).find(whole))), r_)); continue
                for part in re.split(r'\band\b|\bor\b', it.group(0)):
                    if not part.strip() or len(part.strip()) < 3: continue
                    r_ = find_item(part.strip(' .:;?!'), pg, reg)
                    if r_: got.append((at(m.start() + it.start() + it.group(0).find(part)), r_))
            if len(got) >= 2:
                for k_, (ta, r_) in enumerate(got): out.append({'k': 'hi', 't': ta, 'e': nxt, 'p': pg, 'r': r_})
                hi = None
        if hi: out.append({'k': 'hi', 't': a, 'e': round(max(nxt, a + 1.2), 2), 'p': pg, 'r': hi})
        lets = [(x.group(1), x.start()) for x in LETTERS.finditer(ph) if not is_article(ph, x.start())]
        accs = [acc_of(x) for x in LETTERS.finditer(ph) if not is_article(ph, x.start())]
        low = ph.lower()
        if not pop and ('black key' in low or 'twos and threes' in low):
            for want in ((2, 'two'), (3, 'three')):
                if want[1] in low or 'twos and threes' in low:
                    kb = next((k for k in kbs if len(k['black']) == want[0] and inside(k['r'], reg, 0.05)), None)
                    if kb: rs = [b['r'] for b in kb['black']]
                    else:   # a long keyboard: only its groups of that size
                        big = max((k for k in kbs if inside(k['r'], reg, 0.05)), key=lambda k: len(k['black']), default=None)
                        rs = [r for g in (groups(big) if big else []) if len(g) == want[0] for r in g]
                    if rs: out.append({'k': 'blk', 't': at(m.start() + max(0, low.find(want[1]))), 'e': nxt, 'p': pg, 'r': rs})
        if lets:
            pool = PM['pop:' + pop].get('notes', []) if pop else region_notes(pg, reg); lm2 = landmarks(ph)
            if lm2 and any(pos in lm2 for _, pos in lets):
                ns = []
                for l, pos in lets:
                    o_ = LMK_OCT.get(lm2.get(pos)); hit = next((n for n in pool if n['n'] == 'C' and n['o'] == o_), None) if o_ else None
                    ns.append(hit)
                pairs = [(x, n) for x, n in zip(zip(lets, accs), ns) if n]
                lets_n = [x for x, _ in pairs]; ns = [n for _, n in pairs]
            else:
                ns = pick_notes([l for l, _ in lets], pool, accs); lets_n = list(zip(lets, accs))
            if ns:
                for ((l, pos), a_), n in zip(lets_n, ns): out.append({'k': 'nt', 't': at(m.start() + pos), 'e': next((at(q.start()) for q in phr[j + 1:] if any(not is_article(q.group(0), x.start()) for x in LETTERS.finditer(q.group(0)))), END), 'p': pg, 'r': [n['r']], 'n': l + {'#': '♯', 'b': '♭'}.get(a_, '')})
        if lets and any(accs): lets = [x for x, a_ in zip(lets, accs) if not a_]   # a sharp or flat is a black key: not lit as its white neighbour
        if lets:
            lm = landmarks(ph); named = [(l, pos) for l, pos in lets if pos in lm]
            ks = None
            if named:   # Middle C, Treble C...: only the key that carries that name, never another C
                ks = []; keep = []
                for l, pos in lets:
                    if pos in lm:
                        r_ = pick_landmark(lm[pos], kbs, reg)
                        if r_: ks.append(r_); keep.append((l, pos))
                lets = keep
            elif len(lets) == 1:   # one letter on its own: every such key in the picture (every C), unless the picture is small
                kb_ = [k for k in kbs if inside(k['r'], reg, 0.05) and lets[0][0] in key_letters(k)]
                if kb_:
                    kb_ = min(kb_, key=lambda k: len(k['white'])); names_ = key_letters(kb_)
                    ks = [[kb_['white'][i]['r'] for i, n_ in enumerate(names_) if n_ == lets[0][0]]]
                    lets = [lets[0]]
            else: ks = pick_keys([l for l, _ in lets], kbs, reg)
            if ks:
                for (l, pos), k in zip(lets, ks): out.append({'k': 'key', 't': at(m.start() + pos), 'e': next((at(q.start()) for q in phr[j + 1:] if any(not is_article(q.group(0), x.start()) for x in LETTERS.finditer(q.group(0)))), END), 'p': pg, 'r': k if k and isinstance(k[0], list) else [k], 'n': l})   # lit until the next phrase that names keys
    return tag(out, pop)

def phrase_spans(ln, audio=None):   # [time, start, end] of each phrase, for the caption under the page
    text = ln.get('text') or ''
    if not text or ln.get('who') in ('piano', 'pause'): return None
    at = timer(text, ln['t0'], ln['t1'], audio)
    return [[at(m.start()), m.start(), m.end()] for m in re.finditer(r'[^.?!:;]+[.?!:;]*\s*', text) if m.group(0).strip()]
