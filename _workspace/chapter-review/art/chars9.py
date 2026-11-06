# Round 7 (Sohyun 2026-10-08): "would a tortoise butler feel weightier than the rabbit?" and "draw the boy and the
# girl so they are easier to tell apart".
#   * The tortoise butler: the shell is his tailcoat (hatched) and the belly plate is his white shirt front, so he is
#     dressed for service by nature. Round spectacles, white gloves, the coral bow tie, a metronome.
#   * The girl: two pigtails with paper bows, a dress (bodice + A-line skirt, hatched), dark tights.
#   * The boy: a short crop (no tuft) with ears showing, a striped vest over a white shirt, dark shorts, bare knees
#     and dark socks -- the knee joint is easy to see.
# Same pen-and-ink bake as chars8. Writes svg/r7-*.svg and preview9.html.
import math, re, os
import chars5, chars8
from chars5 import floor, piano, stool, keylevel, place, J_SIT
from chars6 import ell, dot, path, bowtie, glove, limb, metronome, J_FRONT
from chars3 import add, sub, unit, pts
from chars import N, C, P, L, svg

SW = 2.2
# ---- heads ------------------------------------------------------------------------------------------------
G_SIDE = 'M5,-8.2 C-1,-12.5 -11,-8 -10.6,0 L-10,3 C-8,1.6 -6,-1.2 -3.6,-4 C-1,-5.8 2.5,-6.2 5.6,-5.6 Z'
G_TAIL = 'M-8.4,-1.6 C-14.6,-1 -18.4,6 -16,13.4 C-14.2,9.6 -11.6,5.4 -7.8,3.6 Z'
G_FRONT = 'M-9.4,2 C-11,-9 -5,-12.6 0,-12.4 C5,-12.6 11,-9 9.4,2 C8,-2 5,-5 0,-5.4 C-5,-5 -8,-2 -9.4,2 Z'
G_TAILS = ('M-8.8,-3.4 C-15,-2.6 -17.6,4.6 -15.6,10.6 C-13.8,6.8 -11.6,3.2 -8.4,1.8 Z '
           'M8.8,-3.4 C15,-2.6 17.6,4.6 15.6,10.6 C13.8,6.8 11.6,3.2 8.4,1.8 Z')
B_SIDE = 'M6.4,-6.4 C3,-12.6 -9,-12 -9.6,-1.6 C-9.4,1.6 -8.6,3 -7.4,3.4 C-6.6,0 -5,-3.4 -1.6,-4.4 C1.6,-5.4 4.4,-5.2 6.4,-6.4 Z'
B_FRONT = 'M-8.6,-1 C-9.6,-9.6 -4.6,-12.6 0,-12.4 C4.6,-12.6 9.6,-9.6 8.6,-1 C7,-4.4 4,-5.6 0,-5.4 C-4,-5.6 -7,-4.4 -8.6,-1 Z'
for h in (G_SIDE, G_TAIL, G_FRONT, G_TAILS, B_SIDE, B_FRONT): chars8.HAIR.add(h)

def bow(x, y, s=1, rot=0):
    return (f'<g transform="translate({x} {y}) rotate({rot}) scale({s})"><path d="M0,0 L-3.8,-2.8 L-3.8,2.8 Z M0,0 L3.8,-2.8 L3.8,2.8 Z" fill="{P}" stroke="{N}" stroke-width="1.1" stroke-linejoin="round"/>'
            f'<circle cx="0" cy="0" r="1.2" fill="{N}"/></g>')

def head2(hc, u, face, who):
    ang = math.degrees(math.atan2(u[1], u[0])) - 90
    sc = f' scale({face} 1)' if face else ''
    g = f'<g transform="translate({hc[0]:.1f} {hc[1]:.1f}) rotate({ang:.1f}){sc}">'
    if who == 'girl':
        g += f'<path d="{G_TAILS if face == 0 else G_TAIL}" fill="{N}"/>'
    g += f'<ellipse cx="0" cy="0" rx="8" ry="9.6" fill="{P}" stroke="{N}" stroke-width="{SW}"/>'
    if who == 'girl':
        if face == 0: g += f'<path d="{G_FRONT}" fill="{N}"/>' + bow(-9.2, -3, 0.9, -20) + bow(9.2, -3, 0.9, 20)
        else: g += f'<path d="{G_SIDE}" fill="{N}"/>' + bow(-9.4, -1.4, 0.95, 70)
    else:
        if face == 0:
            g += f'<path d="{B_FRONT}" fill="{N}"/>' + ell(-8.6, 1, 1.8, 2.8, P, 1.2) + ell(8.6, 1, 1.8, 2.8, P, 1.2)
        else:
            g += f'<path d="{B_SIDE}" fill="{N}"/>' + ell(-1.6, 0.6, 1.9, 2.8, P, 1.2)
    return g + '</g>'

# ---- bodies -----------------------------------------------------------------------------------------------
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

def shoe(a, face):
    return f'<ellipse cx="{a[0] + 4 * (face if face else 0):.1f}" cy="{a[1] + 1:.1f}" rx="{6 if face else 4.4}" ry="3" fill="{N}"/>'

def leg_girl(ch, face): return limb(ch, 5, N) + shoe(ch[-1], face)
def leg_boy(ch, face):
    hip, knee, ank = ch[:3]
    s = limb(ch, 5, P)                                                  # bare leg
    s += limb([hip, add(hip, sub(knee, hip), 0.62)], 7.4, N)            # shorts
    s += limb([add(knee, sub(ank, knee), 0.34), ank], 5.4, N)           # sock
    return s + shoe(ank, face)

def arm2(ch, who):
    sh, el, wr = ch[:3]
    hand = ch[3] if len(ch) > 3 else add(wr, unit(sub(wr, el)), 4)
    s = limb([sh, el, wr], 5.2, N if who == 'girl' else P)
    return s + limb([wr, hand], 3.6, P, N, 1.6)

def vest(nk, hp):
    d, _ = torso_path(nk, hp)
    u = unit(sub(hp, nk)); p = (-u[1], u[0]); Ln = math.dist(nk, hp)
    s = f'<path d="{d}" fill="{P}" stroke="{N}" stroke-width="{SW}" stroke-linejoin="round"/>'
    for t in (0.3, 0.48, 0.66, 0.84):
        c = add(nk, u, Ln * t); w = 8.4 + 2 * t
        s += L(add(c, p, w), add(c, p, -w), 2.6)
    # a white shirt collar at the neck
    s += f'<path d="M{add(nk, p, -5)[0]:.1f},{add(nk, p, -5)[1]:.1f} L{add(nk, u, 5)[0]:.1f},{add(nk, u, 5)[1]:.1f} L{add(nk, p, 5)[0]:.1f},{add(nk, p, 5)[1]:.1f}" fill="{P}" stroke="{N}" stroke-width="1.4" stroke-linejoin="round"/>'
    return s

def kid2(j, face=1, who='girl'):
    u = unit(sub(j['hip'], j['neck']))
    s = ''
    legs, arms = j['legs'], j['arms']
    leg = leg_girl if who == 'girl' else leg_boy
    if len(legs) > 1: s += leg(legs[1], face)
    if len(arms) > 1 and face != 0: s += arm2(arms[1], who)
    s += leg(legs[0], face)
    if who == 'girl':
        d, _ = torso_path(j['neck'], j['hip'])
        s += f'<path d="{d}" fill="{N}" stroke="{N}" stroke-width="{SW}" stroke-linejoin="round"/>' + skirt(j)
    else:
        s += vest(j['neck'], j['hip'])
    if face == 0 and len(arms) > 1: s += arm2(arms[1], who)
    s += arm2(arms[0], who)
    s += L(add(j['head'], u, 8), j['neck'], 3.4, N)
    s += head2(j['head'], u, face, who)
    return s

# ---- the tortoise butler ----------------------------------------------------------------------------------
TCX = 80
def tortoise(arm_l=None, arm_r=None, metro=True):
    cx = TCX
    s = ''
    # legs: short and sturdy, with a few scales and three toes
    for sx in (-1, 1):
        x = cx + sx * 15
        s += limb([(x, 164), (x + sx * 1, 196)], 11, P)
        s += ell(x + sx * 3, 199, 10, 4.4, P, 2.2)
        s += ''.join(L((x + sx * 3 + dx, 197), (x + sx * 3 + dx, 201), 1.1) for dx in (-5, 0, 5))
        s += path(f'M{x-3},{176} q3,2 6,0 M{x-3},{184} q3,2 6,0', fill='none', sw=1.1)
    # the shell: his tailcoat (hatched), a scalloped rim
    s += path(f'M{cx},{80} C{cx+46},{80} {cx+52},{124} {cx+46},{150} C{cx+42},{170} {cx+24},{178} {cx},{178} C{cx-24},{178} {cx-42},{170} {cx-46},{150} C{cx-52},{124} {cx-46},{80} {cx},{80} Z')
    al = arm_l or [(cx - 30, 98), (cx - 38, 122), (cx - 33, 140)]
    ar = arm_r or [(cx + 30, 98), (cx + 40, 118), (cx + 24, 128)]
    raised_l = al[-1][1] < 98
    if not raised_l: s += limb(al, 8.5, P) + glove(*al[-1], 5.4)
    # the belly plate: his white shirt front, with the plate seams
    s += path(f'M{cx},{86} C{cx+24},{86} {cx+30},{118} {cx+28},{140} C{cx+26},{160} {cx+14},{170} {cx},{170} C{cx-14},{170} {cx-26},{160} {cx-28},{140} C{cx-30},{118} {cx-24},{86} {cx},{86} Z', fill=P)
    s += L((cx, 92), (cx, 168), 1.5)
    s += path(f'M{cx-27},{112} Q{cx},{118} {cx+27},{112} M{cx-28},{136} Q{cx},{142} {cx+28},{136} M{cx-22},{156} Q{cx},{162} {cx+22},{156}', fill='none', sw=1.5)
    # a short, sturdy neck with wrinkles, a broad head, round spectacles, a kind smile
    s += path(f'M{cx-9},{87} L{cx-8},{68} L{cx+8},{68} L{cx+9},{87} Z', fill=P)
    s += path(f'M{cx-6.5},{74} q6.5,2.4 13,0 M{cx-7},{80} q7,2.4 14,0', fill='none', sw=1.1)
    s += path(f'M{cx-18},{58} C{cx-18},{46} {cx-10},{42} {cx},{42} C{cx+10},{42} {cx+18},{46} {cx+18},{58} C{cx+18},{67} {cx+10},{71} {cx},{71} C{cx-10},{71} {cx-18},{67} {cx-18},{58} Z', fill=P)
    s += f'<circle cx="{cx-7}" cy="{55}" r="5.4" fill="none" stroke="{N}" stroke-width="1.6"/><circle cx="{cx+7}" cy="{55}" r="5.4" fill="none" stroke="{N}" stroke-width="1.6"/>'
    s += L((cx - 1.6, 54), (cx + 1.6, 54), 1.4) + L((cx - 12.4, 54), (cx - 17, 52.6), 1.2) + L((cx + 12.4, 54), (cx + 17, 52.6), 1.2)
    s += dot(cx - 7, 55.4, 1.9) + dot(cx + 7, 55.4, 1.9)
    s += path(f'M{cx-6},{64} Q{cx},{68} {cx+6},{64}', fill='none', sw=1.6)
    s += bowtie(cx, 87)
    if raised_l: s += limb(al, 8.5, P) + glove(*al[-1], 5.4)
    s += limb(ar, 8.5, P) + glove(*ar[-1], 5.4)
    if metro and not arm_r: s += metronome(cx + 22, 120)
    return s
TORT_FOOT = (TCX, 203)

def tortoise_head():
    cx = 30; s = ''
    s += path(f'M{cx-8},{70} L{cx-7},{56} L{cx+7},{56} L{cx+8},{70} Z', fill=P)
    s += path(f'M{cx-18},{40} C{cx-18},{28} {cx-10},{24} {cx},{24} C{cx+10},{24} {cx+18},{28} {cx+18},{40} C{cx+18},{49} {cx+10},{53} {cx},{53} C{cx-10},{53} {cx-18},{49} {cx-18},{40} Z', fill=P)
    s += f'<circle cx="{cx-7}" cy="37" r="5.4" fill="none" stroke="{N}" stroke-width="1.6"/><circle cx="{cx+7}" cy="37" r="5.4" fill="none" stroke="{N}" stroke-width="1.6"/>'
    s += L((cx - 1.6, 36), (cx + 1.6, 36), 1.4) + dot(cx - 7, 37.4, 1.9) + dot(cx + 7, 37.4, 1.9)
    s += path(f'M{cx-6},{46} Q{cx},{50} {cx+6},{46}', fill='none', sw=1.6)
    s += bowtie(cx, 69, 0.85)
    return svg(60, 78, s)

# ---- the opener with either butler ------------------------------------------------------------------------
def opener(butler='tortoise', who='girl'):
    W, H, YF, DX = 270, 214, 204, 58
    scene = f'<g transform="translate({DX} {YF - 162})">{stool()}{piano()}{kid2(J_SIT, 1, who)}</g>'
    head = (84 + DX, 53 + YF - 162)
    if butler == 'tortoise':
        k = 0.8; rx = 50; paw_local = (TCX + 40, 70)
        fig = tortoise(arm_r=[(TCX + 30, 100), (TCX + 44, 86), paw_local], metro=False); foot = TORT_FOOT
    else:
        k = 0.86; rx = 56; paw_local = (chars8.RCX + 30, 58)
        fig = chars8.rabbit(arm_r=[(chars8.RCX + 17, 98), (chars8.RCX + 31, 80), paw_local], metro=False); foot = chars8.RABBIT_FOOT
    rab = place(fig, k, foot, (rx, YF))
    paw = (rx + (paw_local[0] - foot[0]) * k, YF - (foot[1] - paw_local[1]) * k)
    bar_y = head[1] - 46; tip = (head[0], bar_y - 9)
    s = L((6, YF), (W - 6, YF), 1.6, '#bdb7a6') + rab + scene
    s += f'<path d="M{paw[0]:.1f},{paw[1]+2:.1f} Q{(paw[0]+tip[0])/2:.1f},{tip[1]-14:.1f} {tip[0]:.1f},{tip[1]:.1f}" fill="none" stroke="{N}" stroke-width="2.6" stroke-linecap="round"/>'
    s += glove(paw[0], paw[1], 4.6)
    s += L((tip[0], tip[1]), (tip[0], bar_y), 1.2)
    s += f'<rect x="{head[0]-20}" y="{bar_y}" width="40" height="5" rx="2" fill="{N}"/><rect x="{head[0]-2.5}" y="{bar_y-6}" width="5" height="18" rx="2" fill="{N}"/>'
    s += f'<line x1="{head[0]}" y1="{bar_y+12}" x2="{head[0]}" y2="{head[1]-10}" stroke="{C}" stroke-width="1.8" stroke-dasharray="3 3.5"/>'
    return svg(W, H, s)

def stand2(who):
    return svg(120, 172, floor(120) + kid2(J_FRONT, 0, who))
def sit2(who):
    body = floor(220) + keylevel() + stool() + piano() + kid2(J_SIT, 1, who) + chars8.joints(J_SIT, coral=('elbow', 'wrist'))
    return svg(220, 172, body)

ART = {
    'butler-rabbit': svg(160, 210, chars8.rabbit()),
    'butler-tortoise': svg(160, 210, tortoise()),
    'head-rabbit': chars8.rabbit_head(),
    'head-tortoise': tortoise_head(),
    'open-rabbit': opener('rabbit'),
    'open-tortoise': opener('tortoise'),
    'old-girl': open('svg/k-girl.svg').read(),
    'old-boy': open('svg/k-boy.svg').read(),
    'new-girl': stand2('girl'),
    'new-boy': stand2('boy'),
    'old-girl-sit': open('svg/k-girl-joints.svg').read(),
    'old-boy-sit': open('svg/k-boy-joints.svg').read(),
    'new-girl-sit': sit2('girl'),
    'new-boy-sit': sit2('boy'),
}
PEN = {k: chars8.bake(chars8.to_pen(v), 'r7' + re.sub(r'[^a-z0-9]', '', k)[:12], chars8.field) for k, v in ART.items()}
if __name__ == '__main__':
    for k, v in PEN.items(): open(f'svg/r7-{k}.svg', 'w').write(v)
    cells = ''.join(f'<div class="cell">{v}<p>{k}</p></div>' for k, v in PEN.items())
    open('preview9.html', 'w').write(f'<!doctype html><html><head><style>body{{font-family:Inter,sans-serif;margin:14px;background:#fff}} .row{{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}} .cell{{border:1px solid #eee6d6;border-radius:10px;padding:6px;background:#fffdf7}} .cell svg{{width:auto;height:260px;display:block}} p{{margin:2px 0 0;font-size:11px}}</style></head><body><div class="row">{cells}</div></body></html>')
    print('ok', len(PEN))
