# Round 9 (Sohyun 2026-10-08): "what if the butler is a person?" A grown-up butler in the siblings' own style
# (no face, just the hair, plus a neat moustache for character): tall and upright, tailcoat with tails, white shirt
# front, the coral bow tie, white gloves. Being tall, he holds the puppet bar right above the child's head (no rod),
# and in the mirror game he is simply the teacher calling the finger.
import re
import chars8
from chars5 import floor, piano, stool, place, J_SIT, kid
from chars6 import ell, dot, path, bowtie, glove, limb, metronome, boy_head
from chars import N, C, P, L, svg

HAIR = 'M50.6,18 C50,8 55,6.5 60,6.6 C66,6.5 70.5,9 70.2,17 C68.5,13 65,11.4 61,11.6 L58.6,9.4 C56,11.4 52.6,13.6 50.6,18 Z'
MOUSTACHE = 'M54.6,25.6 C56.6,23.4 59,23.8 60,25.2 C61,23.8 63.4,23.4 65.4,25.6 C63.6,27.4 61.4,27 60,26.2 C58.6,27 56.4,27.4 54.6,25.6 Z'
chars8.HAIR.add(HAIR); chars8.HAIR.add(MOUSTACHE)
FOOT = (60, 170)

def butler(arm_l=None, arm_r=None, metro=True, hand_l_open=False):
    s = ''
    # tails behind the legs
    s += path('M45,88 L39,134 L51,126 Z') + path('M75,88 L81,134 L69,126 Z')
    s += limb([(54, 96), (54, 166)], 7, N) + limb([(66, 96), (66, 166)], 7, N)
    s += ell(51.5, 169, 8, 3.6, N, 0) + ell(68.5, 169, 8, 3.6, N, 0)
    al = arm_l or [(43, 46), (39, 72), (41, 96)]
    ar = arm_r or [(77, 46), (85, 68), (71, 80)]
    lt = limb(al, 6.4, N) + glove(*al[-1], 4.6)
    if al[-1][1] >= 46: s += lt
    # coat body (cut at the waist in front), white shirt front, buttons, bow tie
    s += path('M42,42 Q37,68 44,94 L76,94 Q83,68 78,42 Q60,36 42,42 Z')
    s += path('M53,39.6 L60,74 L67,39.6 Z', fill=P, sw=1.6)
    s += dot(60, 52, 1.3) + dot(60, 60, 1.3)
    s += L((60, 30), (60, 38.6), 4.2)
    s += ell(60, 20, 9.6, 11.6)
    s += f'<path d="{HAIR}" fill="{N}"/><path d="{MOUSTACHE}" fill="{N}"/>'
    s += bowtie(60, 41.6, 0.8)
    if al[-1][1] < 46: s += lt
    s += limb(ar, 6.4, N) + glove(*ar[-1], 4.6)
    if metro and not arm_r: s += f'<g transform="translate(76 78) scale(0.8) translate(-98 -122)">{metronome(98, 122)}</g>'
    return s

def opener(who_boy=False):
    W, H, YF, DX = 256, 196, 186, 40
    k = 1.0
    kidsvg = kid(J_SIT); kidsvg = boy_head(kidsvg) if who_boy else kidsvg
    scene = f'<g transform="translate({DX} {YF - 162})">{stool()}{piano()}{kidsvg}</g>'
    head = (84 + DX, 53 + YF - 162)
    hand_local = (108, 14)
    rx = head[0] - (hand_local[0] - FOOT[0]) * k
    fig = place(butler(arm_r=[(77, 46), (95, 32), hand_local], metro=False), k, FOOT, (rx, YF))
    hand = (rx + (hand_local[0] - FOOT[0]) * k, YF - (FOOT[1] - hand_local[1]) * k)
    bar_y = hand[1] + 7
    s = L((6, YF), (W - 6, YF), 1.6, '#bdb7a6') + fig + scene
    s += f'<rect x="{head[0]-20}" y="{bar_y:.1f}" width="40" height="5" rx="2" fill="{N}"/><rect x="{head[0]-2.5}" y="{bar_y-9:.1f}" width="5" height="20" rx="2" fill="{N}"/>'
    s += glove(hand[0], hand[1], 4.6)
    s += f'<line x1="{head[0]}" y1="{bar_y+12:.1f}" x2="{head[0]}" y2="{head[1]-10}" stroke="{C}" stroke-width="1.8" stroke-dasharray="3 3.5"/>'
    return svg(W, H, s)

def mirror():
    W, H, YF = 240, 176, 164
    bro = boy_head(kid({'hip': (70, 110), 'neck': (70, 70), 'head': (72, 56),
                        'arms': [[(72, 73), (88, 76), (98, 60)], [(68, 74), (66, 94), (67, 110)]],
                        'legs': [[(72, 110), (74, 136), (75, 161)], [(68, 110), (66, 136), (64, 161)]]}))
    fig = place(butler(arm_l=[(43, 46), (30, 34), (24, 16)]), 0.96, FOOT, (182, YF))
    s = floor(W, YF + 2) + bro + fig
    s += f'<path d="M100,50 q4,-6 2,-12 M106,54 q8,-8 4,-18" fill="none" stroke="{C}" stroke-width="1.6" stroke-linecap="round"/>'
    s += chars8.label(122, 118, '"Right hand, 3!"', 'middle', 9.5)
    s += f'<path d="M144,40 l-8,-3 M144,46 l-9,1 M145,52 l-7,4" stroke="{C}" stroke-width="1.6" stroke-linecap="round"/>'
    return svg(W, H, s)

ART = {
    'human': svg(120, 178, butler()),
    'human-bust': f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="40 2 40 48" width="80" height="96">{butler(metro=False)}</svg>',
    'human-open': opener(),
    'human-mirror': mirror(),
}
PEN = {k: chars8.bake(chars8.to_pen(v), 'r9' + re.sub(r'[^a-z0-9]', '', k)[:12], chars8.field) for k, v in ART.items()}
if __name__ == '__main__':
    for k, v in PEN.items(): open(f'svg/r9-{k}.svg', 'w').write(v)
    cells = ''.join(f'<div class="cell">{v}<p>{k}</p></div>' for k, v in PEN.items())
    cells += f'<div class="cell">{open("svg/r7-butler-rabbit.svg").read()}<p>rabbit</p></div><div class="cell">{open("svg/r7-open-rabbit.svg").read()}<p>rabbit open</p></div>'
    open('preview12.html', 'w').write(f'<!doctype html><html><head><style>body{{font-family:Inter,sans-serif;margin:14px;background:#fff}} .row{{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}} .cell{{border:1px solid #eee6d6;border-radius:10px;padding:6px;background:#fffdf7}} .cell svg{{width:auto;height:330px;display:block}} p{{margin:2px 0 0;font-size:11px}}</style></head><body><div class="row">{cells}</div></body></html>')
    print('ok', len(PEN))
