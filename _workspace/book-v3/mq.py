# A wooden artist's mannequin, drawn from joint angles (degrees, 0 = right, 90 = down; SVG y down)
import math
N, C, WOOD, JOINT, CR = '#26296b', '#e4572e', '#f1e4c8', '#e2cfa6', '#fffdf7'

def P(p, a, l): r = math.radians(a); return (p[0] + l * math.cos(r), p[1] + l * math.sin(r))
def f(v): return f'{v:.1f}'
def ik(S, T, l1, l2, bend=1):
    dx, dy = T[0] - S[0], T[1] - S[1]; d = min(math.hypot(dx, dy), l1 + l2 - 0.01)
    a = math.atan2(dy, dx); c = (l1 * l1 + d * d - l2 * l2) / (2 * l1 * d); c = max(-1, min(1, c))
    b = a + bend * math.acos(c); return (S[0] + l1 * math.cos(b), S[1] + l1 * math.sin(b))
def limb(p, q, w):
    d = f'M{f(p[0])} {f(p[1])} L{f(q[0])} {f(q[1])}'
    return (f'<path d="{d}" stroke="{N}" stroke-width="{w + 3.2}" stroke-linecap="round" fill="none"/>'
            f'<path d="{d}" stroke="{WOOD}" stroke-width="{w}" stroke-linecap="round" fill="none"/>')
def joint(p, r): return f'<circle cx="{f(p[0])}" cy="{f(p[1])}" r="{r}" fill="{JOINT}" stroke="{N}" stroke-width="1.5"/>'
def head(p, a):
    return (f'<ellipse cx="{f(p[0])}" cy="{f(p[1])}" rx="11.5" ry="13.5" transform="rotate({a + 90:.0f} {f(p[0])} {f(p[1])})" fill="{WOOD}" stroke="{N}" stroke-width="2.4"/>')

def seg(p, q, ry, sw=2.2):
    cx, cy = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2; L = math.hypot(q[0] - p[0], q[1] - p[1]); a = math.degrees(math.atan2(q[1] - p[1], q[0] - p[0]))
    return f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(L / 2 + 1.5)}" ry="{ry}" transform="rotate({a:.1f} {f(cx)} {f(cy)})" fill="{WOOD}" stroke="{N}" stroke-width="{sw}"/>'
def oval(c, rx, ry, a, sw=2.4):
    return f'<ellipse cx="{f(c[0])}" cy="{f(c[1])}" rx="{rx}" ry="{ry}" transform="rotate({a:.1f} {f(c[0])} {f(c[1])})" fill="{WOOD}" stroke="{N}" stroke-width="{sw}"/>'
def U(a): r = math.radians(a); return (math.cos(r), math.sin(r))
def add(p, u, k, v=None, m=0): return (p[0] + u[0] * k + (v[0] * m if v else 0), p[1] + u[1] * k + (v[1] * m if v else 0))

def taper(p, q, r1, r2, sw=2.2, fill=None):
    L = math.hypot(q[0] - p[0], q[1] - p[1]) or 1; d = ((q[0] - p[0]) / L, (q[1] - p[1]) / L); n = (-d[1], d[0])
    a = (p[0] + n[0] * r1, p[1] + n[1] * r1); b = (q[0] + n[0] * r2, q[1] + n[1] * r2)
    c = (q[0] - n[0] * r2, q[1] - n[1] * r2); e = (p[0] - n[0] * r1, p[1] - n[1] * r1)
    return (f'<path d="M{f(a[0])} {f(a[1])} L{f(b[0])} {f(b[1])} A{r2} {r2} 0 0 0 {f(c[0])} {f(c[1])} L{f(e[0])} {f(e[1])} A{r1} {r1} 0 0 0 {f(a[0])} {f(a[1])}Z" '
            f'fill="{fill or WOOD}" stroke="{N}" stroke-width="{sw}" stroke-linejoin="round"/>')
def smooth(pts, closed=True):
    n = len(pts); d = f'M{f(pts[0][0])} {f(pts[0][1])}'
    for i in range(n if closed else n - 1):
        p0, p1, p2, p3 = pts[(i - 1) % n], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6); c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f' C{f(c1[0])} {f(c1[1])} {f(c2[0])} {f(c2[1])} {f(p2[0])} {f(p2[1])}'
    return d + ('Z' if closed else '')
def shape(pts, sw=2.4): return f'<path d="{smooth(pts)}" fill="{WOOD}" stroke="{N}" stroke-width="{sw}" stroke-linejoin="round"/>'
def U(a): r = math.radians(a); return (math.cos(r), math.sin(r))
def loc(o, u, v, k, m): return (o[0] + u[0] * k + v[0] * m, o[1] + u[1] * k + v[1] * m)
# a head: an egg, the chin narrower, in its own frame (k along the face axis, m sideways)
HEAD = [(-11, 0), (-8, 8.5), (0, 10.5), (9, 9), (14, 4), (15.5, 0), (14, -4), (9, -9), (0, -10.5), (-8, -8.5)]
def headp(c, a, face=0):
    u = U(a); v = (-u[1], u[0]); return shape([loc(c, u, v, k, m) for k, m in HEAD], 2.3)

def side(H, torso=-84, ua=78, fa=-2, hand=24, th=0, sh=92, foot=0, neck=None, far=True, wr=None):
    """Side view, facing right. One torso outline: the back curves, the chest comes forward, the waist narrows, the seat rounds behind."""
    u = U(torso); v = (-u[1], u[0])
    if v[0] < 0: v = (-v[0], -v[1])     # v: the front
    W = loc(H, u, v, 24, 0); NB = loc(H, u, v, 64, 1); S = loc(H, u, v, 55, 1)
    na = neck if neck is not None else torso; hc = loc(NB, U(na), (-U(na)[1], U(na)[0]), 15, 0)
    if wr: Wr = (S[0] + wr[0], S[1] + wr[1]); E = ik(S, Wr, 42, 40, 1)
    else: E = P(S, ua, 42); Wr = P(E, fa, 40)
    T = P(Wr, hand, 14)
    K = P(H, th, 46); A = P(K, sh, 43); F = P(A, foot, 16)
    TOR = [(-7, 2), (-4, 10), (8, 10), (20, 7.5), (30, 9.5), (44, 12.5), (56, 9.5), (64, 5), (66, -1), (62, -9), (50, -11), (38, -9.5), (26, -8.5), (14, -12), (2, -15), (-6, -9)]
    out = ''
    if far:
        out += '<g opacity="0.38">' + taper(H, K, 9, 6.5) + taper(K, A, 6, 4) + taper(A, F, 3.8, 3) + taper(S, E, 6, 4.5) + taper(E, Wr, 4.5, 3.2) + taper(Wr, T, 3.4, 2.6) + '</g>'
    out += taper(H, K, 9.5, 6.5) + taper(K, A, 6.2, 4.2) + taper(A, F, 4, 3)
    out += shape([loc(H, u, v, k, m * 1.4) for k, m in TOR])
    a, b = loc(H, u, v, 25, -11.8), loc(H, u, v, 25, 10.8); out += f'<path d="M{f(a[0])} {f(a[1])} L{f(b[0])} {f(b[1])}" stroke="{N}" stroke-width="1.3"/>'   # the waist seam
    out += taper(NB, loc(NB, U(na), (0, 0), 6, 0), 4, 3.5, 2) + headp(hc, na)
    out += joint(K, 4.8) + joint(A, 3.4)
    out += taper(S, E, 6.5, 4.6) + taper(E, Wr, 4.8, 3.3) + taper(Wr, T, 3.6, 2.6) + joint(S, 5.6) + joint(E, 4.2) + joint(Wr, 3.2)
    return out, dict(H=H, W=W, S=S, E=E, Wr=Wr, T=T, K=K, A=A, F=F, hd=hc)

FRONT = [(0, 0), (8, 1), (26, 7), (29, 13), (25, 24), (24, 36), (19, 50), (15, 60), (17, 70), (21, 80), (18, 90), (8, 95), (0, 96)]
def front_upper(cx, top, L=(-40, 118), R=(40, 118), bendL=-1, bendR=1, hand=90):
    """Front view, upper body behind a keyboard: broad shoulders, a chest tapering to the waist, the hips."""
    y0 = top + 30; half = FRONT[1:-1]
    pts = [(cx + x, y0 + y) for x, y in FRONT] + [(cx - x, y0 + y) for x, y in reversed(half)]
    out = shape(pts)
    out += f'<path d="M{cx - 15} {y0 + 61} Q{cx} {y0 + 65} {cx + 15} {y0 + 61}" fill="none" stroke="{N}" stroke-width="1.3"/>'
    out += taper((cx, y0 - 9), (cx, y0 + 3), 4.2, 5, 2) + headp((cx, top + 12), 90)
    pts_ = {}
    for nm, S0, tg, bd in (('L', (cx - 25, y0 + 9), L, bendL), ('R', (cx + 25, y0 + 9), R, bendR)):
        Wr = (cx + tg[0], top + tg[1]); E = ik(S0, Wr, 40, 38, bd); T = P(Wr, hand, 12)
        out += taper(S0, E, 6.8, 4.8) + taper(E, Wr, 5, 3.4) + taper(Wr, T, 3.8, 2.8) + joint(S0, 5.8) + joint(E, 4.2) + joint(Wr, 3.2)
        pts_[nm] = dict(S=S0, E=E, Wr=Wr, T=T)
    return out, pts_

def stool(x1, x2, y, ground):
    return (f'<rect x="{f(x1)}" y="{f(y)}" width="{f(x2 - x1)}" height="8" rx="2" fill="{CR}" stroke="{N}" stroke-width="2.2"/>'
            f'<path d="M{f(x1 + 6)} {f(y + 8)} V{f(ground)} M{f(x2 - 6)} {f(y + 8)} V{f(ground)}" stroke="{N}" stroke-width="2.4"/>')
def piano_side(kx, ky, ground):
    return (f'<rect x="{f(kx + 26)}" y="{f(ky - 120)}" width="62" height="{f(ground - ky + 120)}" fill="{CR}" stroke="{N}" stroke-width="2.4"/>'
            f'<rect x="{f(kx - 16)}" y="{f(ky)}" width="{f(42 + 2)}" height="9" fill="#fff" stroke="{N}" stroke-width="2.2"/>'
            f'<path d="M{f(kx - 10)} {f(ky)} v5 M{f(kx - 2)} {f(ky)} v5 M{f(kx + 6)} {f(ky)} v5 M{f(kx + 14)} {f(ky)} v5" stroke="{N}" stroke-width="1.2"/>')
def ground_line(x1, x2, y): return f'<path d="M{x1} {y} H{x2}" stroke="#9a9cc4" stroke-width="2"/>'
def keyline(x1, x2, y): return f'<path d="M{f(x1)} {f(y)} H{f(x2)}" stroke="{C}" stroke-width="1.5" stroke-dasharray="4 3"/>'
def keyboard_front(x1, x2, y, h=34):
    n = int((x2 - x1) / 14); s = f'<rect x="{f(x1)}" y="{f(y)}" width="{f(n * 14)}" height="{h}" fill="#fff" stroke="{N}" stroke-width="2.2"/>'
    for i in range(1, n): s += f'<path d="M{f(x1 + i * 14)} {f(y)} v{h}" stroke="{N}" stroke-width="1"/>'
    for i in range(n - 1):
        if i % 7 in (0, 1, 3, 4, 5): s += f'<rect x="{f(x1 + i * 14 + 9)}" y="{f(y)}" width="9" height="{h * 0.6:.1f}" fill="{N}"/>'
    return s

def seated(x0=0, y0=0, **kw):
    H = (x0 + 110, y0 + 190); s, p = side(H, **kw)
    ground = p['A'][1] + 6
    return s, p, ground

def svg(inner, vb): return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg">{inner}</svg>'

def scene_seated(ky_off=0, hip_dx=0, hip_dy=0, label=True, **kw):
    """The good set-up (or a fault), with stool and piano."""
    H = (110 + hip_dx, 190 + hip_dy)
    body, p = side(H, **kw)
    ground = 280
    s = ground_line(20, 330, ground) + stool(H[0] - 34, H[0] + 22, H[1] + 10, ground)
    kx, ky = p['T'][0], p['T'][1] + 1 + ky_off
    s += piano_side(kx, ky, ground)
    if label: s += keyline(30, kx - 18, ky + 1) + f'<text x="32" y="{f(ky - 4)}" font-family="Inter,Arial" font-size="11" font-weight="700" fill="{C}">key level</text>'
    return s + body
