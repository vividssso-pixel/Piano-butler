# Her 17 Nov ("여기 전 퀸과 킹의 대사가 더 나았는데! 유머가 좀 사라졌어"): Reading the notes gets its jokes back, in the
# original voices (cut from the 10 Nov storybook recording): the Queen and King give their own sentences, the FACE joke,
# Clara's "Your kingdom is very busy", the King's dragons-and-grass grumble, the proud cows, the lamb on the stairs.
import json, subprocess, sys, numpy as np, soundfile as sf
sys.path.insert(0, '/tmp/claude-0/pk'); import marks
from kokoro_onnx import Kokoro
SR = 24000; K = Kokoro('/tmp/claude-0/tts/kokoro-v1.0.onnx', '/tmp/claude-0/tts/voices-v1.0.bin')
A = '/mnt/user-data/outputs/books/read2/audio/P5/'; O = '/tmp/claude-0/hum/'
def load(p):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.float32).copy()
def cut(a, t0, t1): x = a[int(t0 * SR):int(t1 * SR)].copy(); n = int(.012 * SR); x[:n] *= np.linspace(0, 1, n); x[-n:] *= np.linspace(1, 0, n); return x
def say(text): a, sr = K.create(text, voice='bm_george', speed=0.98, lang='en-gb'); return np.concatenate([np.asarray(a, np.float32), np.zeros(int(SR * .5), np.float32)])
h = open('/tmp/claude-0/rd2/index.html').read()
i = h.index('const CH = ') + len('const CH = '); CH, n1 = json.JSONDecoder().raw_decode(h[i:]); ce = i + n1
j = h.index('const REG = ') + len('const REG = '); REG, n2 = json.JSONDecoder().raw_decode(h[j:]); re_ = j + n2
c = next(x for x in CH if x['k'] == 'P5')
def build(cl, parts, name):
    out, meta, t = [np.zeros(int(SR * .2), np.float32)], [], .2
    for p in parts:
        if p[0] == 'line':   # an existing line of this clip, cut from its own audio
            ln, a = p[1], p[2]; x = cut(a, ln['t0'], ln['t1']); m = dict(ln)
            if 'notes' in m: m['notes'] = [round(t + (v - ln['t0']), 2) for v in m['notes']]
        elif p[0] == 'old':  # a line from the 10 Nov recording
            _, a, t0, t1, who, text, cue = p; x = cut(a, t0, t1); m = {'who': who, 'text': text, 'cue': cue}
        else:                # a new Butler line
            _, text, cue = p; x = say(text); m = {'who': 'B', 'text': text, 'cue': cue}
        for k in ('mk', 'sp'): m.pop(k, None)
        m['t0'] = round(t, 2); t += len(x) / SR; m['t1'] = round(t, 2); out.append(x); meta.append(m)
    w = np.concatenate(out); sf.write(O + name + '.wav', w, SR)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', O + name + '.wav', '-codec:a', 'libmp3lame', '-b:a', '64k', A + name + '.mp3'], check=True)
    cl['l'] = meta; cl['s'] = round(t); return cl
W = load(O + '02-words-to-remember.mp3'); E7 = load(O + '07-example-treble-c-and-bass-c.mp3'); T8 = load(O + '08-try-it.mp3')
cl = c['clips'][1]; cur = load(A + '02-words-to-remember.mp3'); L = cl['l']; cue = L[0]['cue']; trap = L[3]
build(cl, [('new', 'Little sentences help too, and Their Majesties each have one.', cue),
           ('old', W, 25.25, 29.47, 'Q', 'In my staff we say: Every Good Boy Deserves Fun.', cue),
           ('old', W, 34.03, 39.51, 'Q', 'And my spaces spell face. As in, the face you make when you get it right.', cue),
           ('old', W, 45.2, 49.21, 'K', 'In my kingdom: Great Big Dragons Fly Away!', cue),
           ('old', W, 53.0, 56.37, 'K', 'My spaces: All Cows Eat Grass.', cue),
           ('old', W, 56.37, 60.38, 'P', 'Dragons and cows. Your kingdom is very busy, Your Majesty.', cue),
           ('old', W, 60.38, 65.11, 'K', 'You have no idea. The dragons keep eating the cows’ grass.', cue),
           ('line', trap, cur)], '02-words-to-remember')
cl = c['clips'][5]; cur = load(A + '06-example-treble-c-and-bass-c.mp3'); L = cl['l']
build(cl, [('line', L[0], cur), ('line', L[1], cur), ('line', L[2], cur), ('new', 'Correct. The cows are very proud of you.', L[3]['cue']), ('line', L[4], cur)], '06-example-treble-c-and-bass-c')
cl = c['clips'][6]; cur = load(A + '07-try-it-mary-had-a-little-lamb.mp3'); L = cl['l']
build(cl, [('line', L[0], cur), ('line', L[1], cur), ('old', T8, 23.67, 26.72, 'P', 'The lamb walks downstairs and back up again.', L[1]['cue']), ('line', L[2], cur), ('line', L[3], cur)], '07-try-it-mary-had-a-little-lamb')
SPECS = {5: ['C5 C3'], 6: ['E4 D4 C4 D4 E4 E4 E4*2']}
for ci in (1, 5, 6):
    cl = c['clips'][ci]; path = A + cl['f'].split('?')[0].split('/', 2)[2] if cl['f'].startswith('audio/') else cl['f']
    path = '/mnt/user-data/outputs/books/read2/' + cl['f'].split('?')[0]; k = 0; answered = not any(l.get('who') == 'pause' for l in cl['l'])
    for ln in cl['l']:
        if ln.get('who') == 'pause': answered = True
        spec = None
        if ln.get('who') == 'piano': sp_ = SPECS.get(ci, []); spec = sp_[k] if k < len(sp_) else None; k += 1
        mk = marks.line_marks(ln, spec=spec, REG=REG, audio=path, answered=answered)
        if mk: ln['mk'] = mk
        sp = marks.phrase_spans(ln, path)
        if sp and len(sp) > 1: ln['sp'] = sp
    print(ci, cl['t'], cl['s'], [(l['who'], l['t0'], len(l.get('mk', []))) for l in cl['l']])
h = h[:i] + json.dumps(CH, ensure_ascii=False) + h[ce:j] + json.dumps(REG, ensure_ascii=False) + h[re_:]
open('/tmp/claude-0/hum/index.html', 'w').write(h)
