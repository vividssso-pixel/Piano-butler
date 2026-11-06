import json, numpy as np, soundfile as sf, sys
from kokoro_onnx import Kokoro
VOICE = sys.argv[1] if len(sys.argv) > 1 else 'bf_emma'
SPEED = 1.0
k = Kokoro('/tmp/tts/kokoro-v1.0.int8.onnx', '/tmp/tts/voices-v1.0.bin')
SR = 24000
cache = {}
def say(txt):
    if txt not in cache:
        a, sr = k.create(txt, voice=VOICE, speed=SPEED, lang='en-gb' if VOICE.startswith('b') else 'en-us')
        assert sr == SR
        # trim silence at both ends
        idx = np.where(np.abs(a) > 0.01)[0]
        a = a[max(0, idx[0] - 240): idx[-1] + 2400] if len(idx) else a
        cache[txt] = a
    return cache[txt]
voice = []  # (t, audio)
t = 0.4
def speak(txt, gap=0.35):
    global t
    st = t; a = say(txt); voice.append((st, a)); t = st + len(a) / SR + gap; return st
scenes = []
# title
st = t; speak('Ledger lines.', 0.25); speak('Little ladders out of the staff.', 0.6)
t = max(t, 4.0); scenes.append({'id': 'title', 'from': 0, 'to': t}); t += 0.3
def staff_scene(sid, staff, cap1, notes, cap2, tail=0.8):
    global t
    sc = {'id': sid, 'staff': staff, 'from': t - 0.2, 'caps': [], 'notes': []}
    t += 0.3
    sc['caps'].append([t - 0.1, cap1]); speak(cap1, 0.45)
    for txt, step, letter, name, w in notes:
        st = speak(txt, 0.3)
        ln = len(say(txt)) / SR
        at = st + ln - 0.55 if (sid in ('sky', 'sea')) else st + 0.1
        n = [round(at, 2), step, letter]
        if name or w: n.append(name)
        if w: n.append(w)
        sc['notes'].append(n)
    if cap2:
        t += 0.2; c2 = t; sc['caps'].append([c2 - 0.1, cap2]); speak(cap2, 0.5)
        sc['arrowAt'] = round(c2, 2)
    t += tail; sc['to'] = t; scenes.append(sc); t += 0.3
staff_scene('sky', 'treble', 'Up into the sky.', [
  ('Start on the top line: F.', 10, 'F', None, None), ('The space above: G.', 11, 'G', None, None), ('Ladder one: A.', 12, 'A', None, None),
  ('The next space: B.', 13, 'B', None, None), ('Ladder two: high C.', 14, 'C', 'high C', None)], 'Line, space, ladder. One letter a step.')
staff_scene('sea', 'bass', 'Down into the sea.', [
  ('Start on the bottom line: G.', -10, 'G', None, None), ('The space below: F.', -11, 'F', None, None), ('Ladder one: E.', -12, 'E', None, None),
  ('The next space: D.', -13, 'D', None, None), ('Ladder two: low C.', -14, 'C', 'low C', None)], 'The same pattern, going down.')
staff_scene('middle', 'grand', 'Middle C sits on its own ladder.', [
  ('Under the treble staff,', 0, 'C', 'middle C', 't'), ('or over the bass staff.', 0, 'C', 'middle C', 'b')], 'One key, written two ways.', 1.2)
staff_scene('fivec', 'grand', 'Five Cs, from the sea to the sky.', [
  ('Low C.', -14, 'C', 'low C', 'b'), ('Bass C.', -7, 'C', 'bass C', 'b'), ('Middle C.', 0, 'C', 'middle C', 't'), ('Treble C.', 7, 'C', 'treble C', 't'), ('High C.', 14, 'C', 'high C', 't')], None, 1.2)
# end
end = {'id': 'end', 'from': t - 0.2}
t += 0.2; speak('When you draw a ladder:', 0.3)
items = []
for txt in ['make it a little wider than the note,', 'the same distance apart as the staff lines,', 'with no gaps back to the staff.']:
    items.append(round(t, 2)); speak(txt, 0.3)
t += 0.4; end['ctaAt'] = round(t, 2); speak('Now try the drill.', 0.4)
t += 1.6; end['to'] = t; end['itemsAt'] = items; scenes.append(end)
dur = round(t + 0.2, 2)
tl = {'fps': 25, 'duration': dur, 'scenes': scenes}
json.dump(tl, open('timeline.json', 'w'), indent=1)
vo = np.zeros(int(dur * SR) + SR)
for st, a in voice:
    i = int(st * SR); vo[i:i + len(a)] += a
sf.write('voice.wav', vo[:int(dur * SR)], SR)
print('duration', dur, 'voice', VOICE)
