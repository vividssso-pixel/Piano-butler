# Her 17 Nov: new narration for "Piano finger numbers and fingering": clip 2 "Plan your fingering" (was: thumb under,
# finger over) and clip 3 "Example: left hand or right?" (was: which finger plays the F, a scale question).
# Same voices as the rest of the book (Kokoro: the Butler bm_george 0.98, Clara bf_isabella 1.06, en-gb), half a second
# after each line, the example pause 4 s, the piano taken from this chapter's own recording (C D E F G).
import json, subprocess, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
K = Kokoro('/tmp/claude-0/tts/kokoro-v1.0.onnx', '/tmp/claude-0/tts/voices-v1.0.bin'); SR = 24000
VOICE = {'B': ('bm_george', 0.98), 'P': ('bf_isabella', 1.06)}
A2 = '/mnt/user-data/outputs/books/read2/audio/L1/'
def say(who, text):
    v, sp = VOICE[who]; a, sr = K.create(text, voice=v, speed=sp, lang='en-gb'); assert sr == SR; return np.asarray(a, np.float32)
def load(path, t0, t1):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', path, '-ss', str(t0), '-to', str(t1), '-f', 'f32le', '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.float32).copy(); n = int(SR * .25); a[-n:] *= np.linspace(1, 0, n); return a
PIANO = load(A2 + '01-finger-numbers-and-fingering.mp3', 25.87, 29.25)   # C D E F G, the first five notes of the five-finger run
P_NOTES = [0.0, 0.62, 1.24, 1.86, 2.48]
def build(name, lines, lead=0.2):
    out = [np.zeros(int(SR * lead), np.float32)]; t = lead; meta = []
    for who, text, cue in lines:
        if who == 'pause':
            a = np.zeros(int(SR * 4.0), np.float32); meta.append({'t0': round(t, 2), 't1': round(t + 4.0, 2), 'who': 'pause', 'text': text, 'cue': cue})
        elif who == 'piano':
            a = np.concatenate([PIANO, np.zeros(int(SR * .3), np.float32)]); meta.append({'t0': round(t, 2), 't1': round(t + len(a) / SR, 2), 'who': 'piano', 'notes': [round(t + x, 2) for x in P_NOTES], 'cue': cue})
        else:
            a = np.concatenate([say(who, text), np.zeros(int(SR * .5), np.float32)]); meta.append({'t0': round(t, 2), 't1': round(t + len(a) / SR, 2), 'who': who, 'text': text, 'cue': cue})
        out.append(a); t += len(a) / SR
    w = np.concatenate(out); sf.write('/tmp/claude-0/tts/' + name + '.wav', w, SR)
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', '/tmp/claude-0/tts/' + name + '.wav', '-codec:a', 'libmp3lame', '-b:a', '64k', A2 + name + '.mp3'], check=True)
    return meta, round(t)
C2 = {'p': 128, 'r': 'h:Plan your fingering'}; TR = {'p': 128, 'r': 'trap'}; EX = {'p': 127, 'r': 'pop2'}
clips = {}
clips['02-plan-your-fingering'] = ('Plan your fingering', build('02-plan-your-fingering', [
    ('B', 'A finger number belongs to the music, not to the key, Clara. The same C can be finger one in one bar and finger three in the next.', C2),
    ('P', 'Then how do I know which finger to use?', C2),
    ('B', 'If the fingering is printed, follow it: the plan is already made for you. If not, plan it before you play. Look ahead: where must the hand be for the highest and the lowest notes? Choose fingers that get it there without twisting.', C2),
    ('B', 'More than five notes in a row? Plan where the hand moves, at a rest or a gap. And for a leap, move the whole hand; do not stretch the fingers apart.', C2),
    ('B', 'Then write your plan in pencil and play it the same way every time.', C2),
    ('B', 'Two traps. Mixing up the hands: both thumbs are one, so from C up the left hand plays five, four, three, two, one. And changing your fingering every time you play.', TR)]))
clips['03-example-left-hand-or-right'] = ('Example: left hand or right?', build('03-example-left-hand-or-right', [
    ('B', 'Put your left hand on C D E F G, little finger on C. Which finger plays the G? Pause and try.', EX),
    ('pause', 'Pause and try.', EX),
    ('P', 'The thumb! In the left hand the thumb is on the right, so G is one.', EX),
    ('B', 'That’s right.', EX),
    ('piano', '', EX)]))
json.dump(clips, open('/tmp/claude-0/tts/l1_clips.json', 'w'), indent=1)
for k, (t, (m, s)) in clips.items(): print(k, s, 's', len(m), 'lines')
