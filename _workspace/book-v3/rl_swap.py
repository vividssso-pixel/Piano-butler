# Her 18 Nov: Read & listen follows the book's new order. Tones and semitones becomes Pitch 7 (p. 32), Sharps, flats and
# naturals Pitch 8 (pp. 33-34). Tones and semitones no longer names C sharp (the signs come next) and points to the next
# chapter; Sharps, flats and naturals starts from the semitone, and the Guest is explained, then speaks, after the
# bar-line rule. The opener lists the chapters in the new order. Keys, audio folders, pop-ups, pages and marks follow.
import json, subprocess, sys, os, shutil, re, numpy as np, soundfile as sf
sys.path.insert(0, '/tmp/claude-0/pk'); import marks
from kokoro_onnx import Kokoro
SR = 24000; KK = Kokoro('/tmp/claude-0/tts/kokoro-v1.0.onnx', '/tmp/claude-0/tts/voices-v1.0.bin')
VOICE = {'B': ('bm_george', 0.98), 'P': ('bf_isabella', 1.06)}
R2 = '/mnt/user-data/outputs/books/read2/'; P = '/tmp/claude-0/sw/index.html'
h = open('/tmp/claude-0/punch/new_index.html').read()
i = h.index('const CH = ') + 11; CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ce = i + n1
j = h.index('const REG = ') + 12; REG, n2 = json.JSONDecoder().raw_decode(h[j:]); re_ = j + n2
def load(p):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()
def say(who, text): v, sp = VOICE[who]; a, sr = KK.create(text, voice=v, speed=sp, lang='en-gb'); return np.concatenate([np.asarray(a, np.float32), np.zeros(int(SR * .5), np.float32)])
def ch(k): return next(x for x in CH if x['k'] == k)
NEWLINES = []
def rebuild(cl, seq):
    """seq items: ('keep', ln, audio) | ('say', who, text, cue, lens) | ('cut', ln, audio)"""
    f = cl['f'].split('?')[0]; a = load(R2 + f); L = cl['l']
    out = [a[:int(L[0]['t0'] * SR)]]; t = L[0]['t0']; res = []
    for it in seq:
        if it[0] in ('keep', 'cut'):
            ln = dict(it[1]); src = it[2]; x = src[int(ln['t0'] * SR):int(ln['t1'] * SR)].copy(); d = t - ln['t0']
            if 'notes' in ln: ln['notes'] = [round(v + d, 2) for v in ln['notes']]
            if 'mk' in ln: ln['mk'] = [dict(m, t=round(m['t'] + d, 2), e=round(m['e'] + d, 2)) for m in ln['mk']]
            ln.pop('sp', None)
            if it[0] == 'cut': n = int(.012 * SR); x[:n] *= np.linspace(0, 1, n); x[-n:] *= np.linspace(1, 0, n); ln.pop('mk', None)
        else:
            _, who, text, cue, lens = it; x = say(who, text); ln = {'who': who, 'text': text, 'cue': cue}
            if lens: ln['lens'] = lens
        if ln['who'] != 'piano' and it[0] != 'keep': NEWLINES.append(ln)
        ln['t0'] = round(t, 2); t += len(x) / SR; ln['t1'] = round(t, 2); out.append(x); res.append(ln)
    out.append(a[int(L[-1]['t1'] * SR):]); w = np.concatenate(out)
    wav = '/tmp/claude-0/sw/' + f.replace('/', '_') + '.wav'; sf.write(wav, w, SR)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', wav, '-codec:a', 'libmp3lame', '-b:a', '64k', R2 + f], check=True)
    cl['l'] = res; cl['s'] = round(len(w) / SR)
# --- Tones and semitones (old P8)
T = ch('P8'); c = T['clips'][0]; L = c['l']; A = load(R2 + c['f'].split('?')[0])
rebuild(c, [('keep', L[0], A), ('keep', L[1], A), ('keep', L[2], A), ('keep', L[3], A), ('keep', L[4], A),
            ('say', 'B', 'Everywhere else a black key sits between: C to D has a black key between, so it is a tone.', L[5]['cue'], None), ('keep', L[6], A),
            ('say', 'B', 'And each black key is a semitone from both of its white neighbours, so it can take its name from either side. That is the next chapter.', L[5]['cue'], None),
            ('keep', L[7], A)])
c = T['clips'][1]; L = c['l']; A = load(R2 + c['f'].split('?')[0])
rebuild(c, [('keep', L[0], A), ('keep', L[1], A), ('say', 'P', 'E to F has nothing between: a semitone. C to D has a black key between: a tone.', L[2]['cue'], L[2].get('lens')), ('keep', L[3], A), ('keep', L[4], A)])
# --- Sharps, flats and naturals (old P7): the Guest moves after the rule, with what she is
S = ch('P7'); c0 = S['clips'][0]; L0 = c0['l']; A0 = load(R2 + c0['f'].split('?')[0]); guest = L0[1]
rebuild(c0, [('say', 'B', 'The black keys have no letters of their own, Clara. Each one is a semitone from two white neighbours, and borrows a name from either, with a sharp or a flat.', L0[0]['cue'], None),
             ('keep', L0[2], A0), ('keep', L0[3], A0), ('keep', L0[4], A0)])
c1 = S['clips'][1]; L1 = c1['l']; A1 = load(R2 + c1['f'].split('?')[0])
first = L1[0]['text'].replace('A semitone is the smallest step: the very next key, black or white.', 'Remember the semitone: the very next key, black or white.')
assert first != L1[0]['text']
rebuild(c1, [('say', 'B', first, L1[0]['cue'], None), ('keep', L1[1], A1), ('keep', L1[2], A1), ('keep', L1[3], A1),
             ('say', 'B', 'Think of it like this. A sharp or flat written in the music is a Guest who visits for one bar. The sign is her hat: a sharp lifts the note to the very next key on the right, a flat lowers it to the very next key on the left. Every note on that line or space in the bar wears the hat too.', L1[3]['cue'], None),
             ('cut', dict(guest, cue=L1[3]['cue']), A0), ('keep', L1[4], A1), ('keep', L1[5], A1)])
# --- the opener lists the chapters in the new order
O = ch('O1'); c = O['clips'][0]; L = c['l']; A = load(R2 + c['f'].split('?')[0])
t4 = L[4]['text'].replace('ledger lines, sharps, flats and naturals, tones and semitones,', 'ledger lines, tones and semitones, sharps, flats and naturals,'); assert t4 != L[4]['text']
rebuild(c, [('keep', L[0], A), ('keep', L[1], A), ('keep', L[2], A), ('keep', L[3], A), ('say', 'B', t4, L[4]['cue'], None), ('keep', L[5], A)])
json.dump({'CH': CH, 'REG': REG, 'NEW': [id(x) for x in NEWLINES]}, open('/tmp/claude-0/sw/stage1.json', 'w'), ensure_ascii=False)
# --- rename: keys, titles, order; files; pages
def mv(a, b): os.makedirs(os.path.dirname(b), exist_ok=True); shutil.move(a, b)
for d in ('audio',):
    mv(R2 + 'audio/P7', R2 + 'audio/Pswap'); mv(R2 + 'audio/P8', R2 + 'audio/P7'); mv(R2 + 'audio/Pswap', R2 + 'audio/P8')
for f in sorted(os.listdir(R2 + 'pops')):
    m = re.match(r'P([78])-(.*)', f)
    if m: mv(R2 + 'pops/' + f, R2 + 'pops/tmp_' + ('P8-' if m.group(1) == '7' else 'P7-') + m.group(2))
for f in sorted(os.listdir(R2 + 'pops')):
    if f.startswith('tmp_'): mv(R2 + 'pops/' + f, R2 + 'pops/' + f[4:])
shutil.copy('/tmp/claude-0/rb/P8-1-new.webp', R2 + 'pops/P7-1.webp')   # the tones answer: "C–D has a black key between"
PG = {'P8': {34: 32}, 'P7': {32: 33, 33: 34}}
def ren(s): return re.sub(r'(audio/|pops/)P([78])([/-])', lambda m: m.group(1) + 'P' + ('8' if m.group(2) == '7' else '7') + m.group(3), s)
for k, nk, title in (('P7', 'P8', '8 · Sharps, flats and naturals'), ('P8', 'P7', '7 · Tones and semitones')):
    c = ch(k); c['_nk'] = nk; c['t'] = title
    if 'pages' in c: c['pages'] = [PG[k].get(p, p) for p in c['pages']]
    for cl in c['clips']:
        cl['f'] = ren(cl['f'])
        for ln in cl['l']:
            if ln.get('cue', {}).get('p') in PG[k]: ln['cue'] = dict(ln['cue'], p=PG[k][ln['cue']['p']])
            if ln.get('lens', {}).get('src'): ln['lens'] = dict(ln['lens'], src=ren(ln['lens']['src']))
            for m in ln.get('mk', []):
                if m.get('p') in PG[k]: m['p'] = PG[k][m['p']]
                if m.get('pop'): m['pop'] = 'P' + ('8' if m['pop'][1] == '7' else '7') + m['pop'][2:] if re.match(r'P[78]-', m['pop']) else m['pop']
# sharps clip 2 lines (the rule, the Guest, the trap) are on p. 34; the semitone part stays on p. 33
for ln in ch('P7')['clips'][1]['l']:
    if ln['cue'].get('r') in ('rule', 'trap'): ln['cue'] = dict(ln['cue'], p=34)
for c in CH:
    if '_nk' in c: c['k'] = c.pop('_nk')
a = next(n for n, c in enumerate(CH) if c['k'] == 'P8'); b = next(n for n, c in enumerate(CH) if c['k'] == 'P7'); CH[a], CH[b] = CH[b], CH[a]
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:j] + json.dumps(REG, ensure_ascii=False) + h[re_:]
open(P, 'w').write(h); print('stage 1 done: audio edited, keys and files swapped')
