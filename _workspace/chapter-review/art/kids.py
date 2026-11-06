# The two siblings (Sohyun 2026-10-08, final):
#   * the girl: long straight hair with a headband, a white blouse (collar with a small ribbon, white sleeves) under
#     a short A-line pinafore dress with a pleated hem (a school-uniform feel), bare legs with knee-high socks;
#   * the boy: plain short hair (no tuft), jumper and trousers (the first design she liked).
# KID() emits both children in one drawing: the one for this page is shown, the other is display="none", so the
# Lesson Book can print every page with one child (?kid=girl / ?kid=boy) by CSS alone.
import math
import chars5
from chars6 import ell, path, limb, boy_head
from chars3 import add, sub, unit
from chars import N, C, P, L

SW = 2.2
LONG_SIDE = ('M4.6,-8.6 C-2,-13 -11.6,-9 -11.2,1 C-11,8 -11.8,16 -12.6,23.4 C-9.8,25 -6.2,24.8 -3.6,23.4 '
             'C-4.6,15 -4.8,8 -3.8,2.2 C-3,-2.2 0,-5.4 5.8,-5.8 Z')
LONG_FRONT = ('M-9.6,6 C-11.4,-9 -5,-12.8 0,-12.6 C5,-12.8 11.4,-9 9.6,6 L10.8,18.6 C8.8,20 6.4,19.6 5.4,18 L5.6,4 '
              'C5.4,-1 3.6,-4.6 0,-5.4 C-3.6,-4.6 -5.4,-1 -5.6,4 L-5.4,18 C-6.4,19.6 -8.8,20 -10.8,18.6 Z')
BAND_SIDE = 'M1.9,-10.4 C-0.4,-7.8 -2.4,-4.2 -3.4,0.4 L-5.9,0 C-4.9,-5 -2.6,-8.8 -0.4,-11.6 Z'
BAND_FRONT = 'M-9.3,-4.2 C-6,-10.6 6,-10.6 9.3,-4.2 L8,-2.2 C5,-7.8 -5,-7.8 -8,-2.2 Z'
SHORT_SIDE = 'M6.4,-6.4 C3,-12.6 -9,-12 -9.6,-1.6 C-9.4,1.6 -8.6,3 -7.4,3.4 C-6.6,0 -5,-3.4 -1.6,-4.4 C1.6,-5.4 4.4,-5.2 6.4,-6.4 Z'
SHORT_FRONT = 'M-8.6,-1 C-9.6,-9.6 -4.6,-12.6 0,-12.4 C4.6,-12.6 9.6,-9.6 8.6,-1 C7,-4.4 4,-5.6 0,-5.4 C-4,-5.6 -7,-4.4 -8.6,-1 Z'
HAIR = {LONG_SIDE, LONG_FRONT, BAND_SIDE, BAND_FRONT, SHORT_SIDE, SHORT_FRONT}

def head_girl(hc, u, face):
    ang = math.degrees(math.atan2(u[1], u[0])) - 90
    sc = f' scale({face} 1)' if face else ''
    g = f'<g transform="translate({hc[0]:.1f} {hc[1]:.1f}) rotate({ang:.1f}){sc}">'
    g += f'<ellipse cx="0" cy="0" rx="8" ry="9.6" fill="{P}" stroke="{N}" stroke-width="{SW}"/>'
    g += f'<path d="{LONG_FRONT if face == 0 else LONG_SIDE}" fill="{N}"/>'
    g += f'<path d="{BAND_FRONT if face == 0 else BAND_SIDE}" fill="{P}" stroke="{N}" stroke-width="1.1" stroke-linejoin="round"/>'
    return g + '</g>'

def torso_path(nk, hp):
    u = unit(sub(hp, nk)); p = (-u[1], u[0])
    sh1, sh2 = add(add(nk, p, 10), u, 2), add(add(nk, p, -10), u, 2)
    h1, h2 = add(hp, p, 11.5), add(hp, p, -11.5)
    top = add(nk, u, -2.5); c1, c2 = add(sh1, u, 18), add(sh2, u, 18)
    return (f'M{sh1[0]:.1f},{sh1[1]:.1f} Q{c1[0]:.1f},{c1[1]:.1f} {h1[0]:.1f},{h1[1]:.1f} L{h2[0]:.1f},{h2[1]:.1f} '
            f'Q{c2[0]:.1f},{c2[1]:.1f} {sh2[0]:.1f},{sh2[1]:.1f} Q{top[0]:.1f},{top[1]:.1f} {sh1[0]:.1f},{sh1[1]:.1f} Z'), (h1, h2)

def hull(points):
    pts_ = sorted(set((round(x, 1), round(y, 1)) for x, y in points))
    def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for q in pts_:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], q) <= 0: lo.pop()
        lo.append(q)
    for q in reversed(pts_):
        while len(up) >= 2 and cross(up[-2], up[-1], q) <= 0: up.pop()
        up.append(q)
    return lo[:-1] + up[:-1]

def skirt(j, hem=0.62, flare=7.5):
    _, (h1, h2) = torso_path(j['neck'], j['hip'])
    ps = [h1, h2]
    for lg in j['legs']:
        hip, knee = lg[0], lg[1]
        t = unit(sub(knee, hip)); n = (-t[1], t[0])
        hm = add(hip, sub(knee, hip), hem)
        ps += [add(hm, n, flare), add(hm, n, -flare)]
    hp = hull(ps)
    return f'<path d="M{" L".join(f"{x},{y}" for x, y in hp)} Z" fill="{N}" stroke="{N}" stroke-width="{SW}" stroke-linejoin="round"/>'

def collar(nk, hp):
    u = unit(sub(hp, nk)); p = (-u[1], u[0]); s = ''
    for sx in (1, -1):
        a = add(nk, p, sx * 0.8); b = add(add(nk, p, sx * 8.4), u, 0.6); c = add(add(nk, p, sx * 6.6), u, 6.6); d0 = add(add(nk, p, sx * 1.4), u, 5.4)
        s += (f'<path d="M{a[0]:.1f},{a[1]:.1f} Q{b[0]:.1f},{b[1]:.1f} {c[0]:.1f},{c[1]:.1f} Q{d0[0]:.1f},{d0[1]:.1f} {a[0]:.1f},{a[1]:.1f} Z" '
              f'fill="{P}" stroke="{N}" stroke-width="1.1" stroke-linejoin="round"/>')
    c0 = add(nk, u, 4.6)
    s += (f'<path d="M{c0[0]:.1f},{c0[1]:.1f} l{p[0]*3.4 + u[0]*-1.8:.1f},{p[1]*3.4 + u[1]*-1.8:.1f} l{u[0]*3.6:.1f},{u[1]*3.6:.1f} Z '
          f'M{c0[0]:.1f},{c0[1]:.1f} l{-p[0]*3.4 + u[0]*-1.8:.1f},{-p[1]*3.4 + u[1]*-1.8:.1f} l{u[0]*3.6:.1f},{u[1]*3.6:.1f} Z" fill="{P}" stroke="{N}" stroke-width="1" stroke-linejoin="round"/>')
    return s

def shoe(a, face):
    return f'<ellipse cx="{a[0] + 4 * (face if face else 0):.1f}" cy="{a[1] + 1:.1f}" rx="{6 if face else 4.4}" ry="3" fill="{N}"/>'
def leg_girl(ch, face):
    """bare legs with knee-high socks"""
    hip, knee, ank = ch[:3]
    return limb(ch, 5, P) + limb([add(knee, sub(ank, knee), 0.16), ank], 5.4, N) + shoe(ank, face)
def arm_girl(ch):
    sh, el, wr = ch[:3]
    hand = ch[3] if len(ch) > 3 else add(wr, unit(sub(wr, el)), 4)
    return limb([sh, el, wr], 5.2, P) + limb([wr, hand], 3.6, P, N, 1.6)   # white blouse sleeves

def dress(j, hem=0.46, flare=9):
    """one piece, A-line: narrow at the shoulders, flaring to a short pleated hem above the knee"""
    nk, hp = j['neck'], j['hip']
    u = unit(sub(hp, nk)); p = (-u[1], u[0])
    sh1, sh2 = add(add(nk, p, 5.6), u, 3), add(add(nk, p, -5.6), u, 3)
    w1, w2 = add(add(nk, p, 10.5), u, 17), add(add(nk, p, -10.5), u, 17)
    ps = [sh1, sh2, w1, w2, add(hp, p, 12), add(hp, p, -12)]
    hems = []
    for lg in j['legs']:
        hip, knee = lg[0], lg[1]
        t = unit(sub(knee, hip)); n = (-t[1], t[0])
        hm = add(hip, sub(knee, hip), hem)
        ps += [add(hm, n, flare), add(hm, n, -flare)]
        hems.append((hm, t, n))
    hp_ = hull(ps)
    s = f'<path d="M{" L".join(f"{x},{y}" for x, y in hp_)} Z" fill="{N}" stroke="{N}" stroke-width="{SW}" stroke-linejoin="round"/>'
    # pleats: short pale folds rising from the hem
    hm, t, n = hems[0]
    for k in (-0.62, -0.2, 0.2, 0.62):
        a = add(add(hm, n, flare * k), t, -1.6); b = add(a, t, -8)
        s += L(a, b, 1.3, P)
    return s

def girl(j, face=1):
    u = unit(sub(j['hip'], j['neck']))
    legs, arms = j['legs'], j['arms']
    s = ''
    if len(legs) > 1: s += leg_girl(legs[1], face)
    if len(arms) > 1 and face != 0: s += arm_girl(arms[1])
    s += leg_girl(legs[0], face)
    d, _ = torso_path(j['neck'], j['hip'])
    s += f'<path d="{d}" fill="{P}" stroke="{N}" stroke-width="{SW}" stroke-linejoin="round"/>'   # the white blouse
    s += dress(j)
    if face == 0 and len(arms) > 1: s += arm_girl(arms[1])
    s += arm_girl(arms[0])
    s += L(add(j['head'], u, 8), j['neck'], 3.4, N)
    s += collar(j['neck'], j['hip'])
    s += head_girl(j['head'], u, face)
    return s

def boy(j, face=1):
    return boy_head(chars5.kid(j, face))

def KID(j, face=1, who='girl'):
    hid = ' display="none"'
    return (f'<g data-who="girl"{"" if who == "girl" else hid}>{girl(j, face)}</g>'
            f'<g data-who="boy"{"" if who == "boy" else hid}>{boy(j, face)}</g>')
