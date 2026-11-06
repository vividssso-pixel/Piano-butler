# The hand from the side, jointed (Sohyun 2026-10-08: "the wrist and the finger joints must show; at least this
# angle", pointing at the app's HandSide diagram). Same chain and the same six poses as the app (HAND_POSES:
# segment angles from the fingertip back to the elbow, HAND_LENS), drawn in the pen-and-ink style: a sleeve on the
# forearm, a pale hand with a navy outline, white dots on the wrist, the knuckle, both finger joints and the tip.
# A joint that is wrong in this pose is coral (the app's own checks).
import math
from chars6 import limb, glove
from chars import N, C, P, L, svg

POSES = {
    'good':   [80, 55, 24, -3, -2],
    'flat':   [22, 16, 10, 4, 2],
    'bridge': [62, 38, 8, 18, 3],
    'nail':   [18, 78, 30, -8, 0],
    'low':    [80, 55, 22, -40, -18],
    'high':   [82, 60, 36, 26, 14],
}
LENS = [12, 15, 24, 46, 120]
TIP = (222, 118)

def chain(a, tip=TIP):
    pts = [tip]; x, y = tip
    for ang, ln in zip(a, LENS):
        r = math.radians(ang); x, y = x - ln * math.cos(r), y - ln * math.sin(r); pts.append((x, y))
    return pts   # tip, nail joint, middle joint, knuckle, wrist, elbow side

def checks(a, pts):
    tip, j1, j2, kn, wr, fa = pts
    return {'wrist': abs(a[4]) < 6 and -14 < a[3] <= 2, 'knuckle': kn[1] < wr[1] + 1, 'tip': a[0] > 55 and a[0] > a[1] - 5}

VB = (34, 26, 258, 126)   # one frame for every pose, so they compare at the same scale
def hand_side(pose, labels=True, faults=True, ball=False, car=False, keylabel=True, vb=None):
    a = POSES[pose]; pts = chain(a); tip, j1, j2, kn, wr, fa = pts
    ok = checks(a, pts) if faults else {'wrist': True, 'knuckle': True, 'tip': True}
    s = ''
    # the key (white) on its bed, and the key level
    s += f'<rect data-rigid="1" x="150" y="118" width="134" height="16" fill="{P}" stroke="{N}" stroke-width="2"/>' + L((206, 118), (206, 134), 1.2).replace('<line ', '<line data-rigid="1" ')
    s += f'<path data-rigid="1" d="M120,134 L290,134 L290,148 L120,148 Z" fill="{N}" stroke="{N}" stroke-width="2"/>'
    s += f'<line data-rigid="1" x1="36" y1="118" x2="150" y2="118" stroke="{C}" stroke-width="1.4" stroke-dasharray="4 4"/>'
    if keylabel and labels: s += f'<text x="38" y="113" font-size="8.5" font-weight="800" fill="{C}" font-family="Inter,sans-serif">key level</text>'
    if ball:
        bx, by = (wr[0] + kn[0]) / 2 + 6, (wr[1] + kn[1]) / 2 + 16.5
        s += f'<circle data-rigid="1" cx="{bx:.1f}" cy="{by:.1f}" r="12" fill="none" stroke="{C}" stroke-width="2.2"/><path data-rigid="1" d="M{bx-7:.1f},{by-9:.1f} q5.4,9 0,18 M{bx+7:.1f},{by-9:.1f} q-5.4,9 0,18" fill="none" stroke="{C}" stroke-width="1.2"/>'
    # forearm with a sleeve, the hand, the finger (pale, navy outline)
    s += limb([fa, wr], 17, P, N, 1.8)
    sl = (fa[0] + (wr[0] - fa[0]) * 0.62, fa[1] + (wr[1] - fa[1]) * 0.62)
    s += limb([(fa[0] - 4, fa[1]), sl], 21, N, N, 0)
    s += limb([wr, kn], 14, P, N, 1.8)
    s += limb([kn, j2, j1, tip], 7.6, P, N, 1.6)
    # a fingernail hint on the last segment
    ux, uy = tip[0] - j1[0], tip[1] - j1[1]; ln = math.hypot(ux, uy) or 1; ux, uy = ux / ln, uy / ln
    nx, ny = -uy, ux
    s += L((j1[0] + ux * 3 - nx * 2.4, j1[1] + uy * 3 - ny * 2.4), (j1[0] + ux * 8 - nx * 2.4, j1[1] + uy * 8 - ny * 2.4), 1.1)
    if car:
        s += (f'<g transform="translate({kn[0]-4:.1f} {kn[1]-11:.1f}) rotate(-8)"><rect data-rigid="1" x="-13" y="-9" width="26" height="9" rx="3.5" fill="{C}"/><rect data-rigid="1" x="-7" y="-15" width="13" height="7" rx="3" fill="{C}"/>'
              f'<circle data-rigid="1" cx="-7" cy="1" r="3.3" fill="{N}"/><circle data-rigid="1" cx="7" cy="1" r="3.3" fill="{N}"/></g>')
    # joints: white = fine, coral = the fault in this pose
    def dot(p, good, r=3.6): return f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="{r}" fill="{P if good else C}" stroke="{N}" stroke-width="1.5"/>'
    s += dot(j2, True, 2.9) + dot(j1, True if pose != 'nail' or not faults else False, 2.9)
    s += dot(wr, ok['wrist']) + dot(kn, ok['knuckle']) + dot(tip, ok['tip'])
    if labels:
        lab = lambda x, y, txt, good, anchor='middle': f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-size="9.5" font-weight="900" fill="{N if good else C}" font-family="Inter,sans-serif">{txt}</text>'
        s += lab(wr[0], wr[1] - 14, 'wrist', ok['wrist']) + lab(kn[0] + 4, kn[1] - (26 if car else 13), 'knuckle', ok['knuckle']) + lab(tip[0] + 10, tip[1] - 7, 'tip', ok['tip'], 'start')
    vb = vb or VB
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]} {vb[1]} {vb[2]} {vb[3]}" width="{vb[2]*2}" height="{vb[3]*2}">{s}</svg>'
