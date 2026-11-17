# Her 17 Nov ("핵심 펀칭있는 대화들만 남기면 되"): the key punchlines the 15-16 Nov rewrite dropped, one or two per
# chapter, put back where they fit the new pages. Characters keep their own recorded voices (cut from the old clips);
# the Butler and Clara lines are new in the same Kokoro voices. Unchanged lines keep their audio and marks (shifted).
import json, subprocess, sys, numpy as np, soundfile as sf
sys.path.insert(0, '/tmp/claude-0/pk'); import marks
from kokoro_onnx import Kokoro
SR = 24000; KK = Kokoro('/tmp/claude-0/tts/kokoro-v1.0.onnx', '/tmp/claude-0/tts/voices-v1.0.bin')
VOICE = {'B': ('bm_george', 0.98), 'P': ('bf_isabella', 1.06)}
ROOT = '/mnt/user-data/outputs/books/read2/'; D = '/tmp/claude-0/punch/'
CUTS = json.load(open(D + 'cuts.json'))
def load(p):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()
OLD = {}
def oldcut(text):
    f, t0, t1, who = CUTS[text]
    if f not in OLD: OLD[f] = load(D + f.replace('/', '_'))
    a = OLD[f][int(t0 * SR):int(t1 * SR)].copy(); n = int(.012 * SR); a[:n] *= np.linspace(0, 1, n); a[-n:] *= np.linspace(1, 0, n); return a, who
def say(who, text): v, sp = VOICE[who]; a, sr = KK.create(text, voice=v, speed=sp, lang='en-gb'); return np.concatenate([np.asarray(a, np.float32), np.zeros(int(SR * .5), np.float32)])
h = open(D + 'cur_index.html').read()
i = h.index('const CH = ') + 11; CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ce = i + n1
j = h.index('const REG = ') + 12; REG, n2 = json.JSONDecoder().raw_decode(h[j:]); re_ = j + n2
def edit(k, ci, inserts):
    c = next(x for x in CH if x['k'] == k); cl = c['clips'][ci]; f = cl['f'].split('?')[0]; path = ROOT + f; a = load(path); L = cl['l']
    if ci == -1: pass
    ins = {}
    for pos, lines in inserts: ins.setdefault(len(L) - 1 if pos == 'end' else pos, []).extend(lines)
    out = [a[:int(L[0]['t0'] * SR)]]; t = L[0]['t0']; res = []; new = []
    def add_new(spec, cue_ln):
        nonlocal t
        if spec[0] == 'old': x, who = oldcut(spec[1]); text = spec[1]
        else: who, text = spec; x = say(who, text)
        ln = {'who': who, 'text': text, 'cue': cue_ln['cue']}
        if 'lens' in cue_ln: ln['lens'] = cue_ln['lens']
        ln['t0'] = round(t, 2); t += len(x) / SR; ln['t1'] = round(t, 2); out.append(x); res.append(ln); new.append(ln)
    for spec in ins.get(-1, []): add_new(spec, L[0])
    for li, ln0 in enumerate(L):
        ln = dict(ln0); x = a[int(ln['t0'] * SR):int(ln['t1'] * SR)]; d = t - ln['t0']
        if 'notes' in ln: ln['notes'] = [round(v + d, 2) for v in ln['notes']]
        if 'mk' in ln: ln['mk'] = [dict(m, t=round(m['t'] + d, 2), e=round(m['e'] + d, 2)) for m in ln['mk']]
        if 'sp' in ln: ln['sp'] = [[round(s[0] + d, 2), round(s[1] + d, 2)] + list(s[2:]) if isinstance(s, list) else s for s in ln['sp']]
        ln['t0'] = round(t, 2); t += len(x) / SR; ln['t1'] = round(t, 2); out.append(x); res.append(ln)
        for spec in ins.get(li, []): add_new(spec, ln0)
    out.append(a[int(L[-1]['t1'] * SR):])
    w = np.concatenate(out); wav = D + f.replace('/', '_') + '.wav'; sf.write(wav, w, SR)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', wav, '-codec:a', 'libmp3lame', '-b:a', '64k', path], check=True)
    cl['l'] = res; cl['s'] = round(len(w) / SR)
    answered = not any(l.get('who') == 'pause' for l in res)
    for ln in res:
        if ln.get('who') == 'pause': answered = True
        if ln in new:
            mk = marks.line_marks(ln, REG=REG, audio=path, answered=answered)
            if mk: ln['mk'] = mk
            sp = marks.phrase_spans(ln, path)
            if sp and len(sp) > 1: ln['sp'] = sp
    print(k, ci, cl['t'], cl['s'], ' / '.join(f"{l['who']}:{l.get('text','')[:28]}" for l in new), flush=True)
def last(k, ci, who):
    L = next(x for x in CH if x['k'] == k)['clips'][ci]['l']; return max(n for n, l in enumerate(L) if l['who'] == who)
def nclips(k): return len(next(x for x in CH if x['k'] == k)['clips'])
P = 'P'; B = 'B'
PLAN = [
 ('P1', 0, [(1, [(B, 'Counting keys is for people with no imagination.'), (P, 'Phew.')])]),
 ('P3', 0, [(-1, [(P, 'Butler, my piece looks like a ladder fell over with lots of blobs on it.'), (B, 'Ha! That ladder has a name.')])]),
 ('P3', 1, [(3, [('old', 'Most of the time.')])]),
 ('P6', 0, [(-1, [(P, 'Butler, this note is floating outside the staff! Did it escape?'), (B, 'Ha! Not quite.')])]),
 ('P7', 1, [(0, [(P, 'So E sharp is really F wearing a disguise.'), (B, 'A very thin disguise.')])]),
 ('P10', 0, [(6, [('old', 'Ahem.')])]),
 ('T5', 2, [(3, [(B, 'Which means every birthday party is secretly a waltz.')])]),
 ('T6', 0, [(2, [(P, 'A code! Like spies.'), ('old', 'Like railway codes, miss. Every station knows them.')])]),
 ('T6', 2, [('LASTP', [('old', 'Ticket accepted. All aboard!')])]),
 ('T8', 0, [(1, [('old', 'Five in a bar? In my day we kept to twos and threes. But I must admit, it does make one dance.'), ('old', 'I’d love to see the King dance in five.'), ('old', 'Nobody sees the King dance in five.')])]),
 ('T9', 0, [(-1, [(P, 'Butler, why are some quavers joined together? Are they friends?'), (B, 'Best friends, holding hands.')])]),
 ('B3', 0, [(3, [(P, 'Music has a head and a tail? Like a dog!'), (B, 'A very well-behaved dog. Coda means tail.')])]),
 ('E1', 0, [(2, [(B, 'Everyone has a volume knob, Clara. Some people’s is stuck on loud. I shan’t name names.'), (P, 'My brother.'), (B, 'I said no names.')])]),
 ('E4', 0, [(0, [(B, 'You wouldn’t stop in the middle of a sentence to... breathe, would you?'), (P, 'That was very annoying, Butler.'), (B, 'Exactly my point.')])]),
 ('E7', 0, [(2, [('old', 'Maestoso is how I walk into a room.')])]),
 ('E8', 0, [(-1, [(P, 'I thought the pedals were for driving the piano.'), (B, 'Sadly, it doesn’t go anywhere.')])]),
 ('E10', 0, [(5, [(P, 'Those words are longer than the notes!')])]),
 ('S1', 0, [(4, [(B, 'Like a staircase where two of the steps are only half as high.'), (P, 'I’d trip on those!')])]),
 ('S2', 0, [(4, [(P, 'Three outfits? Minor scales are very fashionable.'), (B, 'Very.')])]),
 ('S2', 4, [('end', [('old', 'It was a favourite at my great-great-great-grandfather’s court. Mind you, he played the lute rather badly.')])]),
 ('S3', 0, [(-1, [(P, 'Butler, in my new piece every single F has a sharp. Did the composer have a stuck keyboard?'), (B, 'Ha! Even worse.')])]),
 ('S5', 1, [(1, [(P, 'So the clue note gives it away.'), (B, 'Elementary, my dear Clara.')])]),
 ('S6', 'LASTCLIP', [('end', [('old', 'The King and I recite it every morning at breakfast.'), ('old', 'Mostly to stop the toast going cold. Never go the wrong way round, Clara.')])]),
 ('H1', 4, [(2, [('old', 'It sounds like people twirling in a ballroom!'), ('old', 'One of my favourites at the palace ball. The King steps on my toes every time.'), ('old', 'Only on the third beat.')])]),
 ('H5', 0, [(-1, [(P, 'Butler, can I turn a cake upside down?'), (B, 'Not without a terrible mess. But a chord, yes!')])]),
 ('H6', 0, [(0, [(P, 'One more layer? Then it would be a better cake.'), (B, 'A different cake, anyway.')])]),
 ('M7', 0, [(3, [(P, 'I feel like I should be wearing sunglasses and a cool hat.'), ('old', 'I played the blues once. The Queen asked me to stop.')])]),
 ('M3', 0, [(4, [(P, 'A-a-men!')])]),
 ('F1', 0, [(0, [(P, 'With a dragon in it?'), (B, 'Sometimes.')])]),
 ('L3', 0, [(0, [(P, 'That sounds scary. Like reading a book in the dark.'), (B, 'Not if you bring a torch.')])]),
 ('L6', 0, [(1, [('old', 'I notice.')])]),
]
for k, ci, ins in PLAN:
    if ci == 'LASTCLIP': ci = nclips(k) - 1
    ins = [(last(k, ci, 'P') if pos == 'LASTP' else pos, lines) for pos, lines in ins]
    edit(k, ci, ins)
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:j] + json.dumps(REG, ensure_ascii=False) + h[re_:]
open(D + 'new_index.html', 'w').write(h)
