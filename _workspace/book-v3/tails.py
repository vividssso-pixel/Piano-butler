# Her 17 Nov ("버틀러가 코렉트 할 때마다 마지막 소리가 어색해"): after "Correct" the piano plays the answer, and its last
# note was chopped off in 0.15 s at the end of the clip. Every clip that ends on the piano now lets its last note die
# away like a released key: an exponential release over the last 0.7 s, down to silence.
import json, subprocess, numpy as np, soundfile as sf
SR = 24000; ROOT = '/mnt/user-data/outputs/books/read2/'
h = open('/tmp/claude-0/punch/new_index.html').read(); i = h.index('const CH = ') + 11; CH, _ = json.JSONDecoder().raw_decode(h[i:])
n = 0
for c in CH:
    for cl in c.get('clips', []):
        L = cl['l']
        if not L or L[-1]['who'] != 'piano': continue
        p = ROOT + cl['f'].split('?')[0]
        a = np.frombuffer(subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', p, '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout, np.float32).copy()
        env = np.sqrt(np.convolve(a ** 2, np.ones(480) / 480, 'same'))
        loud = np.where(env > 0.004)[0]
        if not len(loud): continue
        end = loud[-1]; R = int(0.7 * SR); s0 = max(int(L[-1]['t0'] * SR), end - R)
        k = np.ones(len(a), np.float32); m = end - s0
        k[s0:end] = np.exp(np.linspace(0, -5.5, m)); k[end:] = 0
        b = a * k; wav = '/tmp/claude-0/punch/tail.wav'; sf.write(wav, b, SR)
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', wav, '-codec:a', 'libmp3lame', '-b:a', '64k', p], check=True); n += 1
print('clips given a natural release:', n)
