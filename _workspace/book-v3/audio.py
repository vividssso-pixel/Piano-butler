# "Butler explains": two-voice audio per Handbook chapter (her 7 Nov decisions): the Butler (Kokoro bm_george) and Pip, a student.
# One QR per chapter -> clips in the book's order (Secret, Examples, Try it), real piano sounds, "pause and try" gaps.
# Script lines: ('B', text) Butler · ('P', text) Pip · ('piano', 'C4 E4 G4' or chord '[C4 E4 G4]') · ('pause', seconds)
import numpy as np, soundfile as sf, os, json, subprocess, sys, re
from kokoro_onnx import Kokoro
SR = 24000
K = Kokoro('/tmp/claude-0/tts/kokoro-v1.0.onnx', '/tmp/claude-0/tts/voices-v1.0.bin')
VOICE = {'B': ('bm_george', 0.98), 'P': ('bf_isabella', 1.06)}
NOTES = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
def freq(n):
    m = re.match(r'([A-G])([#b]?)(\d)', n); k = NOTES[m.group(1)] + {'#': 1, 'b': -1, '': 0}[m.group(2)]
    return 440 * 2 ** (((int(m.group(3)) + 1) * 12 + k - 69) / 12)
def tone(fs, dur=0.55):
    t = np.arange(int(SR * (dur + 0.35))) / SR; out = np.zeros_like(t)
    for f in fs:
        for h, a in ((1, 1), (2, .45), (3, .22), (4, .12), (5, .06)):
            out += a * np.sin(2 * np.pi * f * h * t) * np.exp(-t * (2.2 + h * 1.1))
    out *= np.minimum(1, t / 0.005); return 0.22 * out / max(1, len(fs) ** .5)
def _dur(tok):
    m = re.match(r'(.+?)(?:([/*])(\d))?$', tok); n = m.group(1)
    return n, (1 / int(m.group(3)) if m.group(2) == '/' else int(m.group(3)) if m.group(2) == '*' else 1)
def piano(spec):
    parts = []
    for tok in re.findall(r'\[[^\]]+\]|\S+', spec):
        if tok.startswith('['): parts.append(tone([freq(x) for x in tok[1:-1].split()], 1.1))
        elif tok == '|': parts.append(np.zeros(int(SR * .25)))
        else:   # 'F#4/2' = half a slot (a quaver), 'F#4*2' = two slots (a minim)
            nm, mul = _dur(tok); parts.append(np.pad(tone([freq(nm)], .5 * min(mul, 1.6)), (0, int(SR * .62 * mul)))[:int(SR * .62 * mul)])
    return np.concatenate(parts + [np.zeros(int(SR * .3))])
def say(who, text):
    text = re.sub(r'\b([B-G])s\b', r"\1's", text)   # her 8 Nov: 'Cs' was read letter by letter, 'C-S'; say it 'Cees'
    v, sp = VOICE[who]; a, sr = K.create(text, voice=v, speed=sp, lang='en-gb'); return np.asarray(a, dtype=np.float32)
def render(lines, timed=None):
    out = []; t = 0.0
    for ln in lines:
        kind, val = ln[0], ln[1]; cue = ln[2] if len(ln) > 2 else None
        if kind in VOICE: seg = [say(kind, val), np.zeros(int(SR * .35))]
        elif kind == 'piano': seg = [piano(val)]
        elif kind == 'pause': seg = [np.zeros(int(SR * val))]
        else: seg = []
        dur = sum(len(x) for x in seg) / SR
        if timed is not None:
            item = {'t0': round(t, 2), 't1': round(t + dur, 2), 'who': kind}
            if kind in VOICE: item['text'] = val
            if kind == 'pause': item['text'] = 'Pause and try.'
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
            tl = []; w = render(lines, tl); allw += [w, np.zeros(int(SR * .8))]
            fn = f'{i + 1:02d}-{re.sub(r"[^a-z0-9]+", "-", ct.lower()).strip("-")}.mp3'; mp3(w, f'{d}/{fn}'); meta.append({'title': ct, 'file': fn, 'sec': round(len(w) / SR), 'lines': tl})
        mp3(np.concatenate(allw), f'{d}/{k}-all.mp3')
        json.dump({'key': k, 'title': title, 'clips': meta}, open(f'{d}/clips.json', 'w'), indent=1)
        print(k, title, sum(m['sec'] for m in meta), 's', len(meta), 'clips')
