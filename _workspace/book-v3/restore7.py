# Her 17 Nov ("a"): the jokes the 15-16 Nov rewrite lost come back, each where it belongs (story-recall plan):
# T2 pizza, T10 polite dinosaur, E1 mouse to dragon (and the pizza menu), H9 a wedding cake for a giant, H10 cake on a
# plate, F6 Twinkle in a party dress, L1 the thumb's tunnel (as the Extra pointer to the scales). Same voices as the book
# (Kokoro: the Butler bm_george 0.98, Clara bf_isabella 1.06, en-gb, half a second after each line). Unchanged lines keep
# their audio and their marks (shifted); new lines get marks measured fresh.
import json, subprocess, sys, numpy as np, soundfile as sf
sys.path.insert(0, '/tmp/claude-0/pk'); import marks
from kokoro_onnx import Kokoro
SR = 24000; KK = Kokoro('/tmp/claude-0/tts/kokoro-v1.0.onnx', '/tmp/claude-0/tts/voices-v1.0.bin')
VOICE = {'B': ('bm_george', 0.98), 'P': ('bf_isabella', 1.06)}
ROOT = '/mnt/user-data/outputs/books/read2/'; SRC = sys.argv[1]; OUT = sys.argv[2]
def load(p):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()
def say(who, text): v, sp = VOICE[who]; a, sr = KK.create(text, voice=v, speed=sp, lang='en-gb'); return np.concatenate([np.asarray(a, np.float32), np.zeros(int(SR * .5), np.float32)])
h = open(SRC).read()
i = h.index('const CH = ') + 11; CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ce = i + n1
j = h.index('const REG = ') + 12; REG, n2 = json.JSONDecoder().raw_decode(h[j:]); re_ = j + n2
def edit(k, ci, plan):
    """plan: list of ('keep', idx) | ('say', who, text, cue_from_idx)"""
    c = next(x for x in CH if x['k'] == k); cl = c['clips'][ci]; f = cl['f'].split('?')[0]; path = ROOT + f; a = load(path); L = cl['l']
    out = [a[:int(L[0]['t0'] * SR)]]; t = L[0]['t0']; new = []
    for p in plan:
        if p[0] == 'keep':
            ln = dict(L[p[1]]); x = a[int(ln['t0'] * SR):int(ln['t1'] * SR)]; d = t - ln['t0']
            for key in ('notes',): 
                if key in ln: ln[key] = [round(v + d, 2) for v in ln[key]]
            if 'mk' in ln: ln['mk'] = [dict(m, t=round(m['t'] + d, 2), e=round(m['e'] + d, 2)) for m in ln['mk']]
            if 'sp' in ln: ln['sp'] = [[round(s[0] + d, 2), round(s[1] + d, 2)] + list(s[2:]) if isinstance(s, list) else s for s in ln['sp']]
        else:
            _, who, text, src = p; x = say(who, text); ln = {'who': who, 'text': text, 'cue': L[src]['cue']}
            if 'lens' in L[src]: ln['lens'] = L[src]['lens']
            new.append(ln)
        ln['t0'] = round(t, 2); t += len(x) / SR; ln['t1'] = round(t, 2); out.append(x); p_ = ln
        p[-1:] if False else None
        cl.setdefault('_new', []).append(ln)
    tail_from = L[-1]['t1']; out.append(a[int(tail_from * SR):])
    w = np.concatenate(out); wav = '/tmp/claude-0/hum/' + f.replace('/', '_') + '.wav'; sf.write(wav, w, SR)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', wav, '-codec:a', 'libmp3lame', '-b:a', '64k', path], check=True)
    cl['l'] = cl.pop('_new'); cl['s'] = round(len(w) / SR)
    answered = not any(l.get('who') == 'pause' for l in cl['l'])
    for ln in cl['l']:
        if ln.get('who') == 'pause': answered = True
        if ln in new:
            mk = marks.line_marks(ln, REG=REG, audio=path, answered=answered)
            if mk: ln['mk'] = mk
            sp = marks.phrase_spans(ln, path)
            if sp and len(sp) > 1: ln['sp'] = sp
    print(k, cl['t'], cl['s'], [(l['who'], l['t0'], len(l.get('mk', []))) for l in cl['l']])
edit('T2', 0, [('keep', 0), ('say', 'P', 'Who leaves pizza on the plate?', 1),
               ('say', 'B', 'Rests do. Very disciplined. A rest is the same share, left empty. Remember: same name, same length. A rest is its note’s silent twin.', 2),
               ('keep', 3), ('keep', 4), ('keep', 5)])
edit('T10', 0, [('keep', 0), ('say', 'P', 'Anacrusis? That sounds like a dinosaur.', 1), ('say', 'B', 'A very small, polite dinosaur that arrives early.', 1), ('keep', 2), ('keep', 3), ('keep', 4)])
edit('E1', 0, [('keep', 0), ('say', 'P', 'Italian words? Like on a pizza menu?', 0), ('say', 'B', 'Rather like a pizza menu, yes. Though I’m afraid you can’t eat these. I’ve tried.', 0),
               ('keep', 1), ('keep', 2),
               ('say', 'B', 'Remember: six steps, from mouse to dragon. Pianissimo, piano, mezzo-piano, mezzo-forte, forte, fortissimo. Mezzo means half.', 3),
               ('keep', 4), ('keep', 5), ('keep', 6)])
edit('H9', 0, [('keep', 0), ('say', 'B', 'All the way up, like a wedding cake for a giant.', 1), ('keep', 2), ('keep', 3)])
edit('H10', 0, [('keep', 0), ('say', 'P', 'So it’s a cake on a plate. The chord is the cake, the bass is the plate.', 0),
                ('say', 'B', 'A beautiful way to put it. Same cake, new plate, new view.', 0), ('keep', 1), ('keep', 2), ('keep', 3)])
edit('F6', 0, [('keep', 0), ('keep', 1), ('keep', 2), ('say', 'P', 'Like Twinkle in a sparkly party dress!', 2), ('say', 'B', 'Exactly. Same tune, new outfit every time.', 2)])
edit('L1', 1, [('keep', 0), ('keep', 1), ('keep', 2), ('keep', 3),
               ('say', 'B', 'And one extra for later: in a scale, the thumb passes under the hand to keep going.', 3),
               ('say', 'P', 'The thumb is like a little tunnel under a bridge!', 3),
               ('say', 'B', 'A smooth tunnel, please, no bumps. You will build it with the scales.', 3),
               ('keep', 4), ('keep', 5)])
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:j] + json.dumps(REG, ensure_ascii=False) + h[re_:]
open(OUT, 'w').write(h)
