# Round 8 (Sohyun 2026-10-08): the tortoise "looks like an alien"; she wants a gentleman who never hurries.
# Three new butler candidates in the same pen-and-ink style, each with the new siblings in the page-1 scene:
#   * Badger: Mr Badger of the old riverbank stories -- broad, solid, wise; the striped face reads well in hatching.
#   * Crane: the scholar-gentleman bird; stands tall (perfect posture), patient; its own colours are navy, white
#     and a red crown, the brand's palette. The black tail feathers fall like tailcoat tails.
#   * Elephant: the gentle giant who never forgets; big ears, a trunk curled like a bow.
import math, re
import chars8, chars9
from chars5 import floor, piano, stool, place, J_SIT
from chars6 import ell, dot, path, bowtie, glove, limb, metronome
from chars9 import kid2
from chars import N, C, P, L, svg

def coat(cx, top, bot, half=24, bulge=31):
    s = path(f'M{cx-half},{top} Q{cx-bulge},{top+30} {cx-half-3},{bot} L{cx-half-9},{bot+14} L{cx-14},{bot} L{cx+14},{bot} L{cx+half+9},{bot+14} L{cx+half+3},{bot} Q{cx+bulge},{top+30} {cx+half},{top} Q{cx},{top-6} {cx-half},{top} Z')
    s += path(f'M{cx-10},{top-1} L{cx},{top+38} L{cx+10},{top-1} Z', fill=P, sw=1.6)
    s += dot(cx - 11, top + 40, 1.9, P) + dot(cx - 11, top + 50, 1.9, P)
    return s

# ---- badger ----------------------------------------------------------------------------------------------
def badger(arm_r=None, metro=True):
    cx = 80; s = ''
    s += limb([(cx - 11, 154), (cx - 11, 195)], 8, N) + limb([(cx + 11, 154), (cx + 11, 195)], 8, N)
    s += ell(cx - 13, 199, 11, 4.6, N, 0) + ell(cx + 13, 199, 11, 4.6, N, 0)
    al = [(cx - 24, 110), (cx - 33, 134), (cx - 28, 152)]
    ar = arm_r or [(cx + 24, 110), (cx + 34, 130), (cx + 21, 141)]
    s += limb(al, 8, N) + glove(*al[-1], 5.6)
    s += coat(cx, 104, 158)
    # ears, head (a broad wedge tapering to the snout), the two dark stripes through the eyes
    s += ell(cx - 21, 64, 6.5, 6) + ell(cx + 21, 64, 6.5, 6)
    s += path(f'M{cx},{57} C{cx+20},{57} {cx+27},{67} {cx+25},{79} C{cx+23},{91} {cx+11},{103} {cx},{104} C{cx-11},{103} {cx-23},{91} {cx-25},{79} C{cx-27},{67} {cx-20},{57} {cx},{57} Z', fill=P)
    for sx in (-1, 1):
        s += path(f'M{cx+sx*2.6},{98} C{cx+sx*5},{88} {cx+sx*9},{78} {cx+sx*9.5},{58.4} L{cx+sx*17.5},{60.6} C{cx+sx*16},{76} {cx+sx*11},{90} {cx+sx*6},{100} Z')
        s += f'<circle cx="{cx+sx*9}" cy="{79}" r="3.3" fill="{P}" stroke="{N}" stroke-width="1.2"/>' + dot(cx + sx * 9, 79.4, 1.7)
    s += ell(cx, 100, 5.2, 3.6, N, 0)
    s += path(f'M{cx-3},{105.5} Q{cx},{107.5} {cx+3},{105.5}', fill='none', sw=1.2)
    s += bowtie(cx, 108)
    s += limb(ar, 8, N) + glove(*ar[-1], 5.6)
    if metro and not arm_r: s += metronome(cx + 25, 132)
    return s

# ---- crane (in profile, facing right) ----------------------------------------------------------------------
def crane(arm_r=None, metro=True):
    cx = 80; s = ''
    for x, dx in ((73, -1), (85, 2)):
        s += path(f'M{x},{140} L{x+dx+3},{170} L{x+dx},{197}', fill='none', sw=3.4)
        s += L((x + dx, 197), (x + dx + 11, 199), 2.4) + L((x + dx, 197), (x + dx - 8, 199.5), 2.4)
        s += dot(x + dx + 3, 170, 2.6)
    # the tail feathers: black, falling like tailcoat tails
    s += path(f'M{cx-10},{106} C{cx-27},{114} {cx-40},{140} {cx-39},{166} L{cx-31},{156} L{cx-28},{170} L{cx-21},{156} L{cx-16},{166} C{cx-13},{146} {cx-6},{126} {cx-3},{116} Z')
    # body: an upright white egg
    s += path(f'M{cx+2},{84} C{cx+22},{84} {cx+26},{112} {cx+22},{130} C{cx+19},{144} {cx+9},{150} {cx},{150} C{cx-12},{150} {cx-21},{140} {cx-21},{122} C{cx-21},{100} {cx-12},{84} {cx+2},{84} Z', fill=P)
    # neck: a long dark S, the white nape behind it
    s += path(f'M{cx-2},{92} C{cx-2},{78} {cx+10},{70} {cx+8},{56} C{cx+7},{48} {cx+4},{44} {cx+5},{38} L{cx+15},{38} C{cx+15},{46} {cx+18},{50} {cx+18},{58} C{cx+19},{74} {cx+8},{80} {cx+10},{92} Z')
    # head: white cheek, dark face and throat, red crown, long beak
    s += ell(cx + 11, 33, 9.4, 8.2)
    s += path(f'M{cx+5},{35} C{cx+9},{41} {cx+17},{42} {cx+20},{36} C{cx+17},{38} {cx+12},{37} {cx+9},{33} Z')
    s += ell(cx + 10, 25.6, 4.6, 2.6, C, 0)
    s += path(f'M{cx+19},{30.6} L{cx+43},{36} L{cx+19},{36.6} Z', fill=P, sw=1.8)
    s += f'<circle cx="{cx+14}" cy="{31.4}" r="2.6" fill="{P}" stroke="{N}" stroke-width="1.1"/>' + dot(cx + 14.4, 31.6, 1.4)
    s += bowtie(cx + 10, 92, 0.85)
    # the near wing is the arm: white, with dark feather tips for fingers
    ar = arm_r or [(cx + 4, 100), (cx + 15, 122), (cx + 26, 116)]
    s += limb(ar, 8.5, P)
    ex, ey = ar[-1]; ux, uy = ar[-1][0] - ar[-2][0], ar[-1][1] - ar[-2][1]; ln = math.hypot(ux, uy); ux, uy = ux / ln, uy / ln
    for a in (-0.5, 0, 0.5):
        c, si = math.cos(a), math.sin(a); vx, vy = ux * c - uy * si, ux * si + uy * c
        s += limb([(ex, ey), (ex + vx * 8, ey + vy * 8)], 3.2, N)
    if metro and not arm_r: s += metronome(cx + 33, 114)
    return s

# ---- elephant --------------------------------------------------------------------------------------------
def elephant(arm_r=None, metro=True):
    cx = 80; s = ''
    s += limb([(cx - 13, 154), (cx - 13, 194)], 11, N) + limb([(cx + 13, 154), (cx + 13, 194)], 11, N)
    s += ell(cx - 14, 198, 11.5, 5, N, 0) + ell(cx + 14, 198, 11.5, 5, N, 0)
    al = [(cx - 25, 110), (cx - 34, 134), (cx - 29, 152)]
    ar = arm_r or [(cx + 25, 110), (cx + 35, 130), (cx + 22, 141)]
    s += limb(al, 8.5, N) + glove(*al[-1], 6)
    s += coat(cx, 104, 158, 25, 32)
    # ears: big and soft, behind the head
    for sx in (-1, 1):
        s += path(f'M{cx+sx*12},{56} C{cx+sx*30},{40} {cx+sx*50},{50} {cx+sx*46},{72} C{cx+sx*44},{88} {cx+sx*30},{98} {cx+sx*14},{90} Z', fill=P)
        s += path(f'M{cx+sx*17},{62} C{cx+sx*30},{54} {cx+sx*42},{60} {cx+sx*39},{74}', fill='none', sw=1.2)
    s += path(f'M{cx},{46} C{cx+18},{46} {cx+22},{60} {cx+20},{74} C{cx+19},{84} {cx+12},{90} {cx+8},{92} L{cx-8},{92} C{cx-12},{90} {cx-19},{84} {cx-20},{74} C{cx-22},{60} {cx-18},{46} {cx},{46} Z', fill=P)
    s += dot(cx - 8.5, 70, 2.1) + dot(cx + 8.5, 70, 2.1)
    s += path(f'M{cx-12},{65} q3.5,-2.4 7,0 M{cx+5},{65} q3.5,-2.4 7,0', fill='none', sw=1.2)
    # small tusks, then the trunk curling up to one side like a bow
    s += path(f'M{cx-8},{88} q-1,6 -6,8 q2,-5 1,-8 Z M{cx+8},{88} q1,6 6,8 q-2,-5 -1,-8 Z', fill=P, sw=1.3)
    s += bowtie(cx, 109)
    s += limb([(cx, 82), (cx, 97), (cx + 3, 104), (cx + 10, 104), (cx + 13, 98)], 8.4, P)
    s += path(f'M{cx-4},{88} q4,1.6 8,0 M{cx-4},{94} q4,1.6 8,0', fill='none', sw=1)
    s += limb(ar, 8.5, N) + glove(*ar[-1], 6)
    if metro and not arm_r: s += metronome(cx + 26, 132)
    return s

FOOT = (80, 203)
B = {
    'badger':   dict(fn=badger, k=0.94, rx=52, arm=[(104, 110), (118, 94), (122, 74)], top=52),
    'crane':    dict(fn=crane, k=0.9, rx=50, arm=[(84, 100), (98, 86), (108, 66)], top=20),
    'elephant': dict(fn=elephant, k=0.86, rx=56, arm=[(105, 110), (119, 94), (123, 74)], top=40),
}
def standing(name):
    b = B[name]; return svg(160, 210, b['fn']())
def bust(name):
    b = B[name]; body = b['fn']()
    box = {'badger': (44, 50, 72, 70), 'crane': (54, 16, 72, 86), 'elephant': (28, 40, 104, 80)}[name]
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{box[0]} {box[1]} {box[2]} {box[3]}" width="{box[2]*2}" height="{box[3]*2}">{body}</svg>'
def opener(name, who='girl'):
    W, H, YF, DX = 270, 214, 204, 58
    b = B[name]
    scene = f'<g transform="translate({DX} {YF - 162})">{stool()}{piano()}{kid2(J_SIT, 1, who)}</g>'
    head = (84 + DX, 53 + YF - 162)
    paw_local = b['arm'][-1]; k, rx = b['k'], b['rx']
    fig = place(b['fn'](arm_r=b['arm'], metro=False), k, FOOT, (rx, YF))
    paw = (rx + (paw_local[0] - FOOT[0]) * k, YF - (FOOT[1] - paw_local[1]) * k)
    bar_y = head[1] - 46; tip = (head[0], bar_y - 9)
    s = L((6, YF), (W - 6, YF), 1.6, '#bdb7a6') + fig + scene
    s += f'<path d="M{paw[0]:.1f},{paw[1]+2:.1f} Q{(paw[0]+tip[0])/2:.1f},{min(tip[1], paw[1])-14:.1f} {tip[0]:.1f},{tip[1]:.1f}" fill="none" stroke="{N}" stroke-width="2.6" stroke-linecap="round"/>'
    s += glove(paw[0], paw[1], 4.6) if name != 'crane' else ''
    s += L((tip[0], tip[1]), (tip[0], bar_y), 1.2)
    s += f'<rect x="{head[0]-20}" y="{bar_y}" width="40" height="5" rx="2" fill="{N}"/><rect x="{head[0]-2.5}" y="{bar_y-6}" width="5" height="18" rx="2" fill="{N}"/>'
    s += f'<line x1="{head[0]}" y1="{bar_y+12}" x2="{head[0]}" y2="{head[1]-10}" stroke="{C}" stroke-width="1.8" stroke-dasharray="3 3.5"/>'
    return svg(W, H, s)

ART = {}
for n in B:
    ART[f'{n}'] = standing(n); ART[f'{n}-bust'] = bust(n); ART[f'{n}-open'] = opener(n, 'girl' if n != 'crane' else 'boy')
PEN = {k: chars8.bake(chars8.to_pen(v), 'r8' + re.sub(r'[^a-z0-9]', '', k)[:12], chars8.field) for k, v in ART.items()}
if __name__ == '__main__':
    for k, v in PEN.items(): open(f'svg/r8-{k}.svg', 'w').write(v)
    cells = ''.join(f'<div class="cell">{v}<p>{k}</p></div>' for k, v in PEN.items())
    open('preview10.html', 'w').write(f'<!doctype html><html><head><style>body{{font-family:Inter,sans-serif;margin:14px;background:#fff}} .row{{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}} .cell{{border:1px solid #eee6d6;border-radius:10px;padding:6px;background:#fffdf7}} .cell svg{{width:auto;height:300px;display:block}} p{{margin:2px 0 0;font-size:11px}}</style></head><body><div class="row">{cells}</div></body></html>')
    print('ok', len(PEN))
