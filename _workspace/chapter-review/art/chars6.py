# Round 5: a storybook cast. Four butler candidates (rabbit, penguin, owl, cat) in the same ink style,
# the two siblings (a girl with a bob, a boy with short hair), and the posture picture with joints marked.
import math
import chars5
from chars5 import kid, add, sub, unit, limb, floor, stool, piano, keylevel, J_SIT
from chars import N, C, P, L, svg

def ell(cx, cy, rx, ry, fill=P, sw=2.4, rot=0, stroke=N):
    t = f' transform="rotate({rot} {cx} {cy})"' if rot else ''
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{t}/>'
def dot(x, y, r=2.2, c=N): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
def path(d, fill=N, sw=2.4, stroke=N): return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>'
def bowtie(x, y, s=1): return f'<path d="M{x-9*s},{y-5*s} L{x},{y} L{x-9*s},{y+5*s} Z M{x+9*s},{y-5*s} L{x},{y} L{x+9*s},{y+5*s} Z" fill="{C}" stroke="{C}" stroke-width="1.2" stroke-linejoin="round"/>' + dot(x, y, 2.4 * s, C)
def glove(x, y, r=5): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{P}" stroke="{N}" stroke-width="2"/>'

def tailcoat(cx=80, top=94, bot=152):
    s = path(f'M{cx-18},{top} Q{cx-24},{top+30} {cx-20},{bot} L{cx-26},{bot+12} L{cx-12},{bot} L{cx+12},{bot} L{cx+26},{bot+12} L{cx+20},{bot} Q{cx+24},{top+30} {cx+18},{top} Q{cx},{top-6} {cx-18},{top} Z')
    s += path(f'M{cx-8},{top-1} L{cx},{top+34} L{cx+8},{top-1} Z', fill=P, sw=1.6)
    s += dot(cx - 9, top + 36, 1.8, P) + dot(cx - 9, top + 46, 1.8, P)
    return s

def legs(cx=80, top=150, bot=196, feet=(9, 4)):
    s = limb([(cx - 8, top), (cx - 8, bot)], 6, N) + limb([(cx + 8, top), (cx + 8, bot)], 6, N)
    s += ell(cx - 10, bot + 2, feet[0], feet[1], N, 0) + ell(cx + 10, bot + 2, feet[0], feet[1], N, 0)
    return s

def arms_hold(cx=80, top=96):
    left = limb([(cx - 17, top + 2), (cx - 27, top + 26), (cx - 22, top + 44)], 7, N) + glove(cx - 22, top + 46)
    right = limb([(cx + 17, top + 2), (cx + 28, top + 22), (cx + 16, top + 32)], 7, N) + glove(cx + 14, top + 33)
    return left, right

def metronome(x, y):
    return (path(f'M{x-9},{y+12} L{x-5},{y-14} L{x+5},{y-14} L{x+9},{y+12} Z', fill=P, sw=2) + L((x, y + 8), (x + 6, y - 18), 1.8, C) + dot(x + 3.6, y - 8, 2.6, C))

def rabbit(face_y=7):
    cx = 80; s = legs(feet=(11, 4.5)); lt, rt = arms_hold()
    s += lt + tailcoat()
    d = face_y
    s += ell(70, 30 + d, 6.5, 22, P, 2.4, -8) + ell(91, 27 + d, 6.5, 23, P, 2.4, 10) + L((70.5, 18 + d), (69.5, 42 + d), 1.4) + L((90, 14 + d), (92, 38 + d), 1.4)
    s += ell(cx, 68 + d, 16, 18) + dot(73, 66 + d) + dot(87, 66 + d) + path(f'M{cx-2.6},{73+d} L{cx+2.6},{73+d} L{cx},{76+d} Z', fill=N, sw=1)
    s += ''.join(L((cx + sx * 5, 76 + d + dy), (cx + sx * 15, 74 + d + dy * 2), 1) for sx in (-1, 1) for dy in (0, 2.5))
    s += path(f'M{cx-10},{92} L{cx},{100} L{cx+10},{92}', fill='none', sw=2)   # the shirt collar meets the chin
    s += bowtie(cx, 96) + rt + metronome(98, 122)
    return svg(160, 210, s)

def rabbit_head():
    """the butler's head alone, for the REMEMBER line"""
    cx = 30; s = ''
    s += ell(22, 20, 5.2, 17, P, 2.2, -8) + ell(38, 18, 5.2, 18, P, 2.2, 10)
    s += ell(cx, 46, 14, 15) + dot(24, 44, 2) + dot(36, 44, 2) + path(f'M{cx-2.2},{50} L{cx+2.2},{50} L{cx},{52.6} Z', fill=N, sw=1)
    s += ''.join(L((cx + sx * 4, 53 + dy), (cx + sx * 13, 51 + dy * 2), 0.9) for sx in (-1, 1) for dy in (0, 2.4))
    s += bowtie(cx, 66, 0.8)
    return svg(60, 74, s)

def penguin():
    cx = 80
    s = ell(cx - 11, 199, 10, 4, N, 0) + ell(cx + 11, 199, 10, 4, N, 0)
    s += path(f'M{cx},{36} C{cx+30},{36} {cx+38},{110} {cx+32},{160} Q{cx+26},{196} {cx},{196} Q{cx-26},{196} {cx-32},{160} C{cx-38},{110} {cx-30},{36} {cx},{36} Z')
    s += path(f'M{cx},{86} C{cx+18},{90} {cx+22},{140} {cx+18},{168} Q{cx+10},{188} {cx},{188} Q{cx-10},{188} {cx-18},{168} C{cx-22},{140} {cx-18},{90} {cx},{86} Z', fill=P, sw=0)
    s += path(f'M{cx-16},{60} C{cx-16},{48} {cx-4},{46} {cx},{54} C{cx+4},{46} {cx+16},{48} {cx+16},{60} C{cx+16},{72} {cx+6},{78} {cx},{80} C{cx-6},{78} {cx-16},{72} {cx-16},{60} Z', fill=P, sw=0)
    s += dot(cx - 7, 60) + dot(cx + 7, 60) + path(f'M{cx-4},{66} L{cx+4},{66} L{cx},{72} Z', fill=N, sw=1)
    s += path(f'M{cx-30},{100} Q{cx-48},{130} {cx-40},{150} Q{cx-34},{132} {cx-28},{122} Z')
    s += path(f'M{cx+30},{100} Q{cx+46},{116} {cx+34},{132} Q{cx+28},{124} {cx+26},{116} Z')
    s += bowtie(cx, 86)
    s += ell(cx + 32, 134, 18, 4, P, 2) + path(f'M{cx+22},{132} L{cx+26},{116} L{cx+40},{118} L{cx+38},{132} Z', fill=P, sw=1.6) + ''.join(L((cx + 27, 121 + k * 3.5), (cx + 37, 122 + k * 3.5), 1) for k in range(3))
    return svg(160, 210, s)

def owl():
    cx = 80; s = legs(feet=(8, 3.6)); lt, rt = arms_hold()
    s += lt + tailcoat()
    s += path(f'M{cx-20},{50} L{cx-24},{30} L{cx-10},{44} Z', fill=N, sw=2) + path(f'M{cx+20},{50} L{cx+24},{30} L{cx+10},{44} Z', fill=N, sw=2)
    s += ell(cx, 64, 22, 22, N, 2.4)
    s += ell(cx - 9, 62, 8, 8) + ell(cx + 9, 62, 8, 8) + dot(cx - 8, 63, 3) + dot(cx + 10, 63, 3)
    s += path(f'M{cx-2.6},{72} L{cx+2.6},{72} L{cx},{78} Z', fill=P, sw=1.2)
    s += bowtie(cx, 94) + rt
    s += path(f'M{cx+6},{120} L{cx+20},{116} L{cx+34},{120} L{cx+34},{136} L{cx+20},{132} L{cx+6},{136} Z', fill=P, sw=2) + L((cx + 20, 116), (cx + 20, 132), 1.4)
    return svg(160, 210, s)

def cat():
    cx = 80; s = legs(feet=(8, 3.6)); lt, rt = arms_hold()
    s += path(f'M{cx+22},{150} C{cx+46},{148} {cx+50},{120} {cx+40},{108}', fill='none', sw=7)
    s += lt + tailcoat()
    s += path(f'M{cx-15},{60} L{cx-16},{38} L{cx-3},{52} Z', fill=P, sw=2.4) + path(f'M{cx+15},{60} L{cx+16},{38} L{cx+3},{52} Z', fill=P, sw=2.4)
    s += ell(cx, 66, 17, 16)
    s += path(f'M{cx-9},{64} q2.4,-3 4.8,0', fill='none', sw=2) + path(f'M{cx+4.2},{64} q2.4,-3 4.8,0', fill='none', sw=2)
    s += path(f'M{cx-2.4},{70} L{cx+2.4},{70} L{cx},{73} Z', fill=N, sw=1)
    s += ''.join(L((cx + sx * 5, 73 + dy), (cx + sx * 17, 71 + dy * 2), 1) for sx in (-1, 1) for dy in (0, 2.5))
    s += bowtie(cx, 94) + rt + L((cx + 12, 128), (cx + 40, 104), 2) + dot(cx + 40, 104, 2.4, C)
    return svg(160, 210, s)

# ---- the siblings ------------------------------------------------------------------------------------
def boy_head(svgtxt):
    # swap the bob for short hair with a little tuft (profile and front)
    bob_side = 'M5,-8.2 C-1,-12.5 -11,-8 -10.4,1 C-10,4.6 -8.6,7.4 -7,8.4 C-7.6,4 -6,-1.6 -3.6,-4 C-1,-5.8 2.5,-6.2 5.6,-5.6 Z M-5.4,-10.6 C-8,-15.8 -15.4,-16.4 -18.4,-11 C-21,-6 -19.4,2 -16.4,6.4 C-16,0 -14.6,-6 -11,-9.4 C-9.4,-10.6 -7.6,-10.2 -6.4,-8.8 Z'
    short_side = 'M6.4,-6.4 C3,-12.6 -9,-12 -9.6,-1.6 C-9.4,1.6 -8.6,3 -7.4,3.4 C-6.6,0 -5,-3.4 -1.6,-4.4 C1.6,-5.4 4.4,-5.2 6.4,-6.4 Z'
    bob_front = 'M-9.4,2 C-11,-9 -5,-12.6 0,-12.4 C5,-12.6 11,-9 9.4,2 C8,-2 5,-5 0,-5.4 C-5,-5 -8,-2 -9.4,2 Z M-1.6,-11.8 C-2.6,-17.4 1,-21.6 6.4,-21 C11.6,-20.4 13.8,-14 12.8,-7.4 C11.4,-11.4 8.8,-15 5.2,-15.4 C2.8,-15.6 1.4,-14 1.6,-11.8 Z'
    short_front = 'M-8.6,-1 C-9.6,-9.6 -4.6,-12.6 0,-12.4 C4.6,-12.6 9.6,-9.6 8.6,-1 C7,-4.4 4,-5.6 0,-5.4 C-4,-5.6 -7,-4.4 -8.6,-1 Z'
    return svgtxt.replace(bob_side, short_side).replace(bob_front, short_front)

J_FRONT = {'hip': (60, 106), 'neck': (60, 64), 'head': (60, 49),
           'arms': [[(69, 67), (74, 88), (73, 106)], [(51, 67), (46, 88), (47, 106)]],
           'legs': [[(64, 106), (65, 132), (66, 157)], [(56, 106), (55, 132), (54, 157)]]}
def stand(boy=False):
    j = J_FRONT; u = unit(sub(j['hip'], j['neck']))
    body = floor(120)
    for lg in j['legs']: body += chars5.leg(lg, 0)
    body += chars5.jumper(j['neck'], j['hip'])
    for a in j['arms']:   # a thin paper edge keeps the arms apart from the jumper
        body += limb(a[:3], 9.6, P, P, 0) + chars5.arm(a)
    body += L(add(j['head'], u, 8), j['neck'], 3.4, N) + chars5.head(j['head'], u, 0)
    return svg(120, 172, boy_head(body) if boy else body)

def joints(j, coral=()):
    """white dots on the joints; the ones this page checks in coral"""
    pts = {'shoulder': j['arms'][0][0], 'elbow': j['arms'][0][1], 'wrist': j['arms'][0][2], 'hip': j['legs'][0][0], 'knee': j['legs'][0][1], 'ankle': j['legs'][0][2]}
    s = ''
    for k, p in pts.items():
        c = C if k in coral else P
        s += f'<circle cx="{p[0]:.1f}" cy="{p[1]:.1f}" r="3.1" fill="{c}" stroke="{N}" stroke-width="1.2"/>'
    return s
def sit_joints(boy=False):
    body = floor(220) + keylevel() + stool() + piano() + kid(J_SIT) + joints(J_SIT, coral=('elbow', 'wrist'))
    body += (f'<text x="88" y="84" font-size="8.5" font-weight="800" fill="{C}" font-family="Inter,sans-serif">elbow</text>'
             f'<text x="114" y="85" font-size="8.5" font-weight="800" fill="{C}" font-family="Inter,sans-serif">wrist</text>')
    return svg(220, 172, boy_head(body) if boy else body)

ART = {'b-rabbit': rabbit(), 'b-rabbit-head': rabbit_head(), 'b-penguin': penguin(), 'b-owl': owl(), 'b-cat': cat(),
       'k-girl': stand(), 'k-boy': stand(True), 'k-girl-joints': sit_joints(), 'k-boy-joints': sit_joints(True)}
def _write():
    for k, v in ART.items(): open(f'svg/{k}.svg', 'w').write(v)
    cells = ''.join(f'<div class="cell">{v}<p>{k}</p></div>' for k, v in ART.items())
    open('preview6.html', 'w').write(f'<!doctype html><html><head><style>body{{font-family:Inter,sans-serif;margin:14px}} .row{{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}} .cell{{border:1px solid #eee6d6;border-radius:10px;padding:6px}} .cell svg{{width:auto;height:230px;display:block}} p{{margin:2px 0 0;font-size:11px}}</style></head><body><div class="row">{cells}</div></body></html>')
    print('ok')

if __name__ == '__main__': _write()
