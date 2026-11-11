# her 11 Nov: the app's six warm-up drawings, moving, for Read & listen (frames captured from drills.html?tool=arm-moves)
import json, re
F = json.load(open('/tmp/claude-0/pk/warm_frames.json'))
MS = {'ragdoll': 4200, 'wings': 3600, 'glide': 4400, 'dive': 2400, 'bridge': 3000, 'balloon': 3200}
rnd = lambda s: re.sub(r'(\d+\.\d)\d+', r'\1', re.sub(r' style="[^"]*"', '', s, count=1))
out = {k: {'ms': MS[k], 'f': [[t, rnd(svg)] for i, (t, svg) in enumerate(v) if i % 2 == 0]} for k, v in F.items()}
js = 'window.WARM=' + json.dumps(out, separators=(',', ':')) + ';'
open('/tmp/claude-0/pk/read_warm.js', 'w').write(js); print(len(js))
