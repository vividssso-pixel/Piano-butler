# Drawings for the chapter 1 guide page (tools/lessons/svg/posture-hands/), the same pen-and-ink drawings as the
# Lesson Book (chars8.py), with three small changes for the page's smaller sizes:
#   - every label gets a paper-coloured halo, so lines never run through the words;
#   - on the big sitting picture, "wrist" moves a little left, clear of the piano;
#   - the five fault hands drop the "key level" words (the dashed line stays; the good hand keeps the words).
#   python3 guide374.py <out-dir>
import os, re, sys
import chars8 as c8
from handside import hand_side

out = sys.argv[1] if len(sys.argv) > 1 else '../guide/tools/lessons/svg/posture-hands'
os.makedirs(out, exist_ok=True)


def halo(s):
    return re.sub(r'<text ', '<text stroke="#fffdf7" stroke-width="2.4" stroke-linejoin="round" paint-order="stroke" ', s)


def pen(k, uid=None):
    return c8.PEN[k] if uid is None else c8.bake(c8.to_pen(c8.ART[k]), uid, c8.field)


# "wrist" on the sitting picture: from x 130 (touching the piano's edge) to x 126, with a shorter leader
sit = c8.ART['sit']
a, b = '<text x="130" y="80"', 'M129,78 L123,88'
assert sit.count(a) == 1 and sit.count(b) == 1
c8.ART['sit-guide'] = sit.replace(a, '<text x="126" y="80"').replace(b, 'M125.5,78.5 L123,86')

PICS = {
    'hero': pen('puppet'), 'sit-good': pen('sit-guide', 'psit'),
    'sit-low': pen('q-sit-low'), 'sit-high': pen('q-sit-high'), 'sit-close': pen('q-sit-close'), 'sit-far': pen('q-sit-far'),
    'move-1': pen('ragdoll'), 'move-2': pen('wings'), 'move-3': pen('glide'), 'move-4': pen('dive'), 'move-5': pen('bridge'), 'move-6': pen('balloon'),
    'hand-0': pen('hand-good'), 'thumb': pen('hand-thumb'),
    'numbers-0': pen('hand-L'), 'numbers-1': pen('hand-R'), 'walk-L': pen('keys-hand-L'), 'walk-R': pen('keys-hand-R'),
}
for i, pose in enumerate(['flat', 'bridge', 'nail', 'low', 'high'], 1):
    PICS['hand-%d' % i] = c8.bake(c8.to_pen(hand_side(pose, labels=True, faults=True, keylabel=False)), 'g' + pose, c8.field)

for name, s in PICS.items():
    open(os.path.join(out, name + '.svg'), 'w', encoding='utf-8').write(halo(s))
print(len(PICS), 'drawings ->', out)
