import sys
p = sys.argv[1]
lines = open(p, encoding='utf-8').read().split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| 700 |')]
assert len(idx) == 1
rows = [
"| 701 | 2026-10-27 | **Things to make, batch 1 (Build BI; board call 25).** My beat band (Pulse): two bars of claps, stamps, pats and rests (body percussion made from the click's noise and a low thump), four or three beats, looped slow, walking or fast, beat 1 the thick strong box, Surprise me. Question and answer (Steps and skips): the piano asks two bars in C position (six questions, each ending away from home), the child answers in the same rhythm on C D E F G, then hears both; ending on C sounds finished. Four-chord loop (Chords): I, IV, V, vi in C go round under a little band (bass on 1 and 3, the chord on every beat), four ready loops or tap a box to change it; the chord's notes lit as the safe ones, every note kept to hear back. Each in its room's Toolbox and on the Home. Source patch728.py; test bi728.js. |",
"| 702 | 2026-10-27 | **Things to make, batch 2 (Build BJ; board call 25).** Loud and soft, your way (Dynamics): the first line of Ode to Joy plays while the child taps pp to ff; each note keeps its sign, drawn as bars whose height is the loudness (the Dynamics room's own volumes), then heard back. Drive the tempo (Tempo): Twinkle goes round while the child presses Faster or Slower (or slides); the Italian word and the metronome mark follow, from the Tempo room's own speeds (Largo 40 to Presto 200), and the change is named accelerando or ritardando. Bright or dark? (Minor scales): the child plays a tune on C D E F G (or loads Ode to Joy) and hears it with the bright 3rd (E) or the darker one (E♭), the room's own words. A tune is now played note by note on the audio clock (liveTune), so speed and loudness can change as it plays. Source patch729.py; test bj729.js. chsweep 46 chapters 0 errors, booksweep 0 errors, regression 329 lessons, 54 drills, 0 errors. Local commit only, not pushed. |",
]
for r in reversed(rows): lines.insert(idx[0] + 1, r)
open(p, 'w', encoding='utf-8').write('\n'.join(lines)); print('ok')
