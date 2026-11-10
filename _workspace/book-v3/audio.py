# "Butler explains": two-voice audio per Handbook chapter (her 7 Nov decisions): the Butler (Kokoro bm_george) and Pip, a student.
# One QR per chapter -> clips in the book's order (Secret, Examples, Try it), real piano sounds, "pause and try" gaps.
# Script lines: ('B', text) Butler · ('P', text) Pip · ('piano', 'C4 E4 G4' or chord '[C4 E4 G4]') · ('pause', seconds)
import numpy as np, soundfile as sf, os, json, subprocess, sys, re
from kokoro_onnx import Kokoro
SR = 24000
K = Kokoro('/tmp/claude-0/tts/kokoro-v1.0.onnx', '/tmp/claude-0/tts/voices-v1.0.bin')
VOICE = {'C': ('bf_emma', 1.0), 'B': ('bm_george', 0.98), 'P': ('bf_isabella', 1.06), 'Q': ('bf_lily', 0.86), 'K': ('bm_lewis', 0.88)}
SHIFT = {'K': 0.92}   # her 9 Nov: the King below the Butler; the Queen is Lily, slow and calm, unshifted (a pitched-up voice sounded like a child)   # her 9 Nov: the Queen (treble) and the King (bass) visit now and then
NOTES = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
def freq(n):
    m = re.match(r'([A-G])([#b]?)(\d)', n); k = NOTES[m.group(1)] + {'#': 1, 'b': -1, '': 0}[m.group(2)]
    return 440 * 2 ** (((int(m.group(3)) + 1) * 12 + k - 69) / 12)
_FS = None; _PC = {}
def _pnote(m, dur):   # her 10 Nov: a real piano (FluidSynth, FluidR3 grand), not the synth bell; cached per key and length
    global _FS
    k = (m, round(dur, 2))
    if k not in _PC:
        if _FS is None:
            import fluidsynth
            _FS = fluidsynth.Synth(samplerate=float(SR)); sid = _FS.sfload('/usr/share/sounds/sf2/FluidR3_GM.sf2'); _FS.program_select(0, sid, 0, 0)
        _FS.get_samples(int(SR * .05))
        _FS.noteon(0, m, 96); x = _FS.get_samples(int(SR * dur)); _FS.noteoff(0, m); y = _FS.get_samples(int(SR * .35))
        _PC[k] = np.concatenate([x, y]).astype(np.float32).reshape(-1, 2).mean(1) / 4500.0
    return _PC[k]
def tone(fs, dur=0.55):
    ms = [int(round(69 + 12 * np.log2(f / 440))) for f in fs]
    xs = [_pnote(m, dur) for m in ms]; L = max(len(x) for x in xs); out = np.zeros(L)
    for x in xs: out[:len(x)] += x
    return out / max(1, len(fs) ** .5)
def _dur(tok):   # 'F#4/2' half a slot, 'F#4*2' two slots, 'X@96' one beat at 96 a minute
    m = re.match(r'(.+?)(?:([/*@])(\d+(?:\.\d+)?))?$', tok.rstrip('~')); n = m.group(1); op, v = m.group(2), m.group(3)
    return n, (1 / float(v) if op == '/' else float(v) if op == '*' else (60 / float(v)) / .62 if op == '@' else 1)
def untie(spec):   # Time 3: 'C4*2~ C4' is one sound of 3 slots (a tie); the lens still draws both notes
    out = []; carry = 0
    for tok in spec.split():
        n, mul = _dur(tok)
        if tok.endswith('~'): carry += mul; continue
        out.append(f'{n}*{carry + mul:g}' if carry else tok); carry = 0
    return ' '.join(out)
def click(level):   # her 10 Nov: the beat as a soft heartbeat (lub-dub), not a tick; X strong (beat 1), M medium, x weak
    def thump(f, dur, decay):
        t = np.arange(int(SR * dur)) / SR
        return (np.sin(2 * np.pi * f * t * (1 - .25 * t / dur)) + .5 * np.sin(2 * np.pi * 2 * f * t) + .25 * np.sin(2 * np.pi * 3 * f * t)) * np.exp(-t * decay) * np.minimum(1, t / .004)
    lub = thump(88, .16, 28); dub = .45 * thump(108, .12, 34)
    w = np.zeros(int(SR * .32)); w[:len(lub)] += lub; i = int(SR * .13); w[i:i + len(dub)] += dub
    return w * {'X': .95, 'M': .7, 'x': .55}[level]
DYNG = {'pp': .22, 'p': .38, 'mp': .55, 'mf': .72, 'f': .95, 'ff': 1.25}
def piano(spec):
    parts = []
    for tok in re.findall(r'\[[^\]]+\]|\S+', spec):
        if tok.startswith('['):
            xs = tok[1:-1].split(); g = DYNG.get(xs[0], None)
            if g: xs = xs[1:]
            parts.append((g or 1.0) * tone([freq(x) for x in xs], 1.1))
        elif tok == '|': parts.append(np.zeros(int(SR * .25)))
        else:   # 'F#4/2' = half a slot (a quaver), 'F#4*2' = two slots (a minim); 'pp:C4' a dynamic, 'C4!' staccato
            g = 1.0
            if ':' in tok: dn, tok = tok.split(':', 1); g = DYNG.get(dn, 1.0)
            st = tok.endswith('!'); tok = tok.rstrip('!')
            nm, mul = _dur(tok); L = int(SR * .62 * mul)
            if nm not in ('X', 'M', 'x', 'R'): parts.append(g * np.pad(tone([freq(nm)], .1 if st else .5 * min(mul, 1.6)), (0, L))[:L]); continue
            if nm in ('X', 'M', 'x'): parts.append(np.pad({'X': .55, 'M': .38, 'x': .28}[nm] * tone([freq('C5')], .12), (0, L))[:L])   # her 10 Nov: no heartbeat; a beat on its own is a light piano tap
            elif nm == 'R': parts.append(np.zeros(L))
            else: parts.append(np.pad(tone([freq(nm)], .5 * min(mul, 1.6)), (0, L))[:L])
    return np.concatenate(parts + [np.zeros(int(SR * .3))])
def say(who, text):
    text = re.sub(r'\b([B-G])s\b', r"\1's", text)   # her 8 Nov: 'Cs' was read letter by letter, 'C-S'; say it 'Cees'
    v, sp = VOICE[who]; a, sr = K.create(text, voice=v, speed=sp, lang='en-gb'); a = np.asarray(a, dtype=np.float32)
    if who in SHIFT: a = lower(a, SHIFT[who])   # her 9 Nov: the Queen clearly high, the King clearly low
    return a
def lower(a, r):   # pitch down by ratio r, same length (ffmpeg asetrate + atempo)
    import tempfile; d = tempfile.mkdtemp(); sf.write(d + '/i.wav', a, SR)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', d + '/i.wav', '-af', f'asetrate={SR}*{r},aresample={SR},atempo={1 / r:.4f}', d + '/o.wav'], check=True)
    return sf.read(d + '/o.wav', dtype='float32')[0]
_WORD = {}
NUMW = {'1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six', '&': 'and'}
_CNT = {}
_CW = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '&': 'and', 'e': 'ee', 'a': 'uh'}
def _stretch(a, r):   # speed up by ratio r, same pitch (ffmpeg atempo), so a word fits its beat without being cut off
    if r <= 1.02: return a
    import tempfile; d = tempfile.mkdtemp(); sf.write(d + '/i.wav', a, SR)
    f = ','.join(['atempo=2.0'] * int(np.log2(r)) + [f'atempo={r / 2 ** int(np.log2(r)):.4f}'])
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', d + '/i.wav', '-af', f, d + '/o.wav'], check=True)
    return sf.read(d + '/o.wav', dtype='float32')[0]
def word(w, slot=.62):   # her 10 Nov: count the beats "one, two, three, four" in a separate, smooth voice (Emma): whole words, gently sped up to fit the beat, never cut off
    k = (w, round(slot, 2))
    if k not in _CNT:
        if w not in _CNT:
            a = say('C', _CW.get(w, w) + ',')
            j = np.where(np.abs(a) > 0.012)[0]; a = a[max(0, j[0] - 120):j[-1] + 240] if len(j) else a
            _CNT[w] = a
        a = _CNT[w]; fit = SR * slot * .82
        a = _stretch(a, len(a) / fit)
        f = np.minimum(1, np.arange(len(a)) / 80.0) * np.minimum(1, (len(a) - np.arange(len(a))) / 300.0)
        _CNT[k] = a * f * (.6 if w in ('&', 'e', 'a') else .75)
    return _CNT[k]
def _phrase(words):   # her 10 Nov: say the whole count as one flowing phrase ("one, two, three, four"), then cut it at the quiet points between words
    a = say('C', ', '.join(_CW.get(w, w) for w in words) + '.')
    j = np.where(np.abs(a) > 0.012)[0]; a = a[j[0]:j[-1] + 240] if len(j) else a
    n = len(words); fr = int(SR * .01); e = np.array([np.abs(a[i:i + fr]).mean() for i in range(0, max(1, len(a) - fr), fr)])
    cuts = [0]
    for k in range(1, n):   # the quietest moment near where the k-th word should end
        c = int(len(e) * k / n); lo, hi = max(cuts[-1] + 5, c - 18), min(len(e) - 5, c + 18)
        cuts.append(lo + int(np.argmin(e[lo:hi])) if hi > lo else c)
    cuts.append(len(e))
    return [a[cuts[i] * fr:cuts[i + 1] * fr] for i in range(n)]
def count(spec):   # {'beats': beat tokens (timing only, no sound), 'notes': piano tokens (optional), 'say': '1 2 3 …' one word per beat, '-' for silence}
    toks = spec['beats'].split(); times = []; t = 0.0
    for tok in toks: times.append(t); t += .62 * _dur(tok)[1]
    tracks = []   # her 10 Nov: no heartbeat / click under the beat
    if spec.get('notes'): tracks.append(piano(untie(spec['notes'])) * 1.15)   # the melody in front
    else: tracks.append(piano(spec['beats']))   # no tune: the beat as light piano taps (beat 1 a little stronger)
    v = np.zeros(int(SR * (t + 1)))
    sw = spec.get('say', '').split(); slots = [.62 * _dur(x)[1] for x in toks]
    idx = [i for i, w in enumerate(sw) if w != '-' and i < len(times)]
    if idx:
        segs = _phrase([sw[i] for i in idx])
        for i, a in zip(idx, segs):
            fit = SR * max(slots[i], .3) * .9
            if len(a) > fit: a = _stretch(a, len(a) / fit)
            f = np.minimum(1, np.arange(len(a)) / 60.0) * np.minimum(1, (len(a) - np.arange(len(a))) / 200.0)
            a = a * f * .42; k = int(SR * times[i]); v[k:k + len(a)] += a[:len(v) - k]
    tracks.append(v)
    L = max(len(x) for x in tracks); out = np.zeros(L)
    for x in tracks: out[:len(x)] += x
    return out, times
def render(lines, timed=None):
    out = []; t = 0.0
    for ln in lines:
        kind, val = ln[0], ln[1]; cue = ln[2] if len(ln) > 2 else None
        if kind in VOICE: seg = [say(kind, val), np.zeros(int(SR * .35))]
        elif kind == 'piano': seg = [piano(val)]
        elif kind == 'pause': seg = [np.zeros(int(SR * val))]
        elif kind == 'count': cw, ctimes = count(val); seg = [cw]
        else: seg = []
        dur = sum(len(x) for x in seg) / SR
        if timed is not None:
            item = {'t0': round(t, 2), 't1': round(t + dur, 2), 'who': kind}
            if kind in VOICE: item['text'] = val
            if kind == 'pause': item['text'] = 'Pause and try.'
            if kind == 'count': item['who'] = 'piano'; item['notes'] = [round(t + x, 2) for x in ctimes]
            if kind == 'piano':   # one note every 0.62 s (a chord or bar gap counts as its own slot)
                toks = re.findall(r'\[[^\]]+\]|\S+', val); tt = t; item['notes'] = []
                for tok in toks:
                    step = 1.45 if tok.startswith('[') else (.25 if tok == '|' else .62 * _dur(tok)[1])
                    if tok != '|': item['notes'].append(round(tt, 2))
                    tt += step
            if cue: item['cue'] = cue
            timed.append(item)
        out += seg; t += dur
    return np.concatenate(out)
def mp3(wav, path):
    tmp = path[:-4] + '.wav'; sf.write(tmp, wav, SR)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', tmp, '-codec:a', 'libmp3lame', '-qscale:a', '4', path], check=True); os.remove(tmp)
if __name__ == '__main__':
    from scripts import CH
    keys = sys.argv[1:] or list(CH)
    OUT = '/mnt/user-data/outputs/audio'
    for k in keys:
        title, clips = CH[k]; d = f'{OUT}/{k}'; os.makedirs(d, exist_ok=True); allw = []; meta = []
        for i, (ct, lines) in enumerate(clips):
            if ct == 'The secret': ct = title   # her 8 Nov: the first clip is named after the chapter
            tl = []; w = render(lines, tl); allw += [w, np.zeros(int(SR * .8))]
            fn = f'{i + 1:02d}-{re.sub(r"[^a-z0-9]+", "-", ct.lower()).strip("-")}.mp3'; mp3(w, f'{d}/{fn}'); meta.append({'title': ct, 'file': fn, 'sec': round(len(w) / SR), 'lines': tl})
        mp3(np.concatenate(allw), f'{d}/{k}-all.mp3')
        json.dump({'key': k, 'title': title, 'clips': meta}, open(f'{d}/clips.json', 'w'), indent=1)
        print(k, title, sum(m['sec'] for m in meta), 's', len(meta), 'clips')
