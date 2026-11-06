# Round 3, after Sohyun's references (faceless editorial people, navy line or ink, natural proportions; the little
# figure in a circle on the music map): one recurring kid -- a navy bob and a coral jumper -- in two colourways,
# "line" (navy outline, paper fill, coral jumper) and "ink" (solid navy, coral only for things), plus map badges
# and hands to match.
import math
import chars
from chars import N, C, P, F, L, svg, floor, piano, stool

def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def add(a, b, k=1): return (a[0] + b[0] * k, a[1] + b[1] * k)
def unit(v): l = math.hypot(*v) or 1; return (v[0] / l, v[1] / l)
def pts(ps): return ' '.join(f'{x:.1f},{y:.1f}' for x, y in ps)

SCHEMES = {
    'line': {'jumper': C, 'trousers': F, 'skin': P, 'hair': N, 'shoe': N},
    'ink':  {'jumper': N, 'trousers': N, 'skin': P, 'hair': N, 'shoe': N},
}

def limb(chain, w, fill, out=N, ow=2.2):
    s = f'<polyline points="{pts(chain)}" fill="none" stroke="{out}" stroke-width="{w + 2*ow}" stroke-linecap="round" stroke-linejoin="round"/>'
    if fill != out:
        s += f'<polyline points="{pts(chain)}" fill="none" stroke="{fill}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
    return s

def person(j, face=1, scheme='line'):
    K = SCHEMES[scheme]
    u = unit(sub(j['hip'], j['neck'])); p = (-u[1], u[0])
    s = ''
    # back limbs first
    if len(j['legs']) > 1: s += leg(j['legs'][1], face, K, back=True)
    if len(j['arms']) > 1: s += arm(j['arms'][1], K, back=True)
    # jumper
    nk, hp = j['neck'], j['hip']
    sh1, sh2 = add(add(nk, p, 10), u, 2), add(add(nk, p, -10), u, 2)
    h1, h2 = add(hp, p, 11.5), add(hp, p, -11.5)
    top = add(nk, u, -2.5)
    d = (f'M{sh1[0]:.1f},{sh1[1]:.1f} Q{add(sh1, u, 18)[0]:.1f},{add(sh1, u, 18)[1]:.1f} {h1[0]:.1f},{h1[1]:.1f} '
         f'L{h2[0]:.1f},{h2[1]:.1f} Q{add(sh2, u, 18)[0]:.1f},{add(sh2, u, 18)[1]:.1f} {sh2[0]:.1f},{sh2[1]:.1f} '
         f'Q{top[0]:.1f},{top[1]:.1f} {sh1[0]:.1f},{sh1[1]:.1f} Z')
    s += leg(j['legs'][0], face, K)
    s += f'<path d="{d}" fill="{K["jumper"]}" stroke="{N}" stroke-width="2.2" stroke-linejoin="round"/>'
    s += arm(j['arms'][0], K)
    # head: faceless; the bob shows which way the kid faces (hair at the back)
    hc = j['head']; ang = math.degrees(math.atan2(u[1], u[0])) - 90
    s += L(add(hc, u, 8), nk, 3.4, N)
    s += f'<g transform="translate({hc[0]:.1f} {hc[1]:.1f}) rotate({ang:.1f}) scale({face if face else 1} 1)">'
    s += f'<ellipse cx="0" cy="0" rx="8" ry="9.6" fill="{K["skin"]}" stroke="{N}" stroke-width="2.2"/>'
    s += f'<path d="M5,-8.2 C-1,-12.5 -11,-8 -10.6,1 L-10,8.6 C-7.5,10 -4,9 -2.6,6.2 C-3.4,1 -1,-4.4 5.6,-5.6 Z" fill="{K["hair"]}"/>'
    s += '</g>'
    return s

def arm(chain, K, back=False):
    sh, el, wr = chain[:3]
    s = limb([sh, el, wr], 5.2, K['jumper'])
    hand = chain[3] if len(chain) > 3 else add(wr, unit(sub(wr, el)), 4)
    s += limb([wr, hand], 3.6, K['skin'], N, 1.6)
    return s

def leg(chain, face, K, back=False):
    s = limb(chain, 5, K['trousers'])
    a = chain[-1]
    s += f'<ellipse cx="{a[0] + 4 * (face if face else 1):.1f}" cy="{a[1] + 1:.1f}" rx="6" ry="3" fill="{K["shoe"]}"/>'
    return s

# ---- scenes ----------------------------------------------------------------------------------------
def s_stand(sc):
    W, H = 130, 172
    j = {'hip': (64, 104), 'neck': (64, 63), 'head': (65, 49),
         'arms': [[(66, 66), (78, 54), (84, 38), (86, 31)], [(62, 66), (58, 86), (59, 104)]],
         'legs': [[(66, 104), (67, 131), (68, 157)], [(62, 104), (60, 131), (58, 157)]]}
    return svg(W, H, floor(W) + person(j, 1, sc))

def s_sit(sc):
    W, H = 220, 172
    j = {'hip': (76, 110), 'neck': (81, 68), 'head': (84, 53),
         'arms': [[(83, 71), (98, 91), (121, 92), (128, 98)], [(79, 72), (93, 93), (116, 94), (123, 99)]],
         'legs': [[(78, 110), (108, 111), (108, 155)], [(73, 111), (101, 113), (100, 155)]]}
    key = (f'<text x="8" y="91" font-size="8.5" font-weight="800" fill="{C}" font-family="Inter,sans-serif">key level</text>'
           f'<line x1="8" y1="96" x2="122" y2="96" stroke="{C}" stroke-width="1.3" stroke-dasharray="4 4" opacity="0.8"/>')
    return svg(W, H, floor(W) + stool() + piano() + key + person(j, 1, sc))

def s_balloon(sc):
    W, H = 220, 172
    keys = f'<rect x="112" y="104" width="76" height="10" rx="2" fill="{P}" stroke="{N}" stroke-width="2.4"/>' + ''.join(L((112 + i * 9.5, 104), (112 + i * 9.5, 114), 1.3) for i in range(1, 8))
    j = {'hip': (80, 106), 'neck': (80, 64), 'head': (82, 50),
         'arms': [[(82, 67), (103, 86), (124, 80), (130, 102)], [(78, 68), (74, 88), (75, 106)]],
         'legs': [[(82, 106), (85, 132), (87, 157)], [(78, 106), (74, 132), (71, 157)]]}
    balloon = (f'<path d="M124,80 C130,58 148,50 151,40" fill="none" stroke="{N}" stroke-width="1.6"/>'
               f'<ellipse cx="153" cy="25" rx="13" ry="16" fill="{C}"/><path d="M150,41 l3,-4 l3,4 z" fill="{C}"/><ellipse cx="148" cy="19" rx="3" ry="5" fill="#fff" opacity="0.45"/>')
    return svg(W, H, floor(W) + keys + balloon + person(j, 1, sc))

def s_dive(sc):
    W, H = 220, 172
    board = f'<rect x="6" y="70" width="62" height="7" rx="2" fill="{F}" stroke="{N}" stroke-width="3"/>' + L((18, 77), (18, 162), 3) + floor(W)
    wave = 'M90,142 q10,-7 20,0 t20,0 t20,0 t20,0 t20,0 t20,0'
    water = f'<path d="{wave} L210,162 L90,162 Z" fill="{F}"/><path d="{wave}" fill="none" stroke="{N}" stroke-width="2.6" stroke-linecap="round"/>'
    arc = f'<path d="M64,60 Q92,24 124,64" fill="none" stroke="{N}" stroke-width="1.6" stroke-dasharray="3 5" opacity="0.55"/>'
    splash = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C}"/>' for x, y, r in [(156, 130, 3.2), (166, 122, 2.6), (146, 123, 2.4), (174, 132, 2), (138, 133, 2)])
    d = (0.62, 0.78); pp = (-d[1], d[0])
    hip = (96, 60); neck = add(hip, d, 36); hd = add(neck, d, 13)
    j = {'hip': hip, 'neck': neck, 'head': hd,
         'arms': [[add(neck, pp, 3), add(add(neck, d, 20), pp, 5), add(add(neck, d, 38), pp, 4), add(add(neck, d, 44), pp, 4)],
                  [add(neck, pp, -3), add(add(neck, d, 20), pp, -2), add(add(neck, d, 38), pp, -1), add(add(neck, d, 44), pp, -1)]],
         'legs': [[add(hip, pp, 3), add(add(hip, d, -24), pp, 4), add(add(hip, d, -46), pp, 4)], [add(hip, pp, -3), add(add(hip, d, -24), pp, -3), add(add(hip, d, -46), pp, -6)]]}
    return svg(W, H, board + arc + water + splash + person(j, 1, sc))

J_STAND = {'hip': (64, 104), 'neck': (64, 63), 'head': (65, 49),
           'arms': [[(66, 66), (69, 86), (68, 104)], [(62, 66), (58, 86), (59, 104)]],
           'legs': [[(66, 104), (67, 131), (68, 157)], [(62, 104), (60, 131), (58, 157)]]}
J_SIT = {'hip': (76, 110), 'neck': (81, 68), 'head': (84, 53),
         'arms': [[(83, 71), (98, 91), (121, 92), (128, 98)], [(79, 72), (93, 93), (116, 94), (123, 99)]],
         'legs': [[(78, 110), (108, 111), (108, 155)], [(73, 111), (101, 113), (100, 155)]]}
J_BAL = {'hip': (80, 106), 'neck': (80, 64), 'head': (82, 50),
         'arms': [[(82, 67), (103, 86), (122, 70), (126, 64)], [(78, 68), (74, 88), (75, 106)]],
         'legs': [[(82, 106), (85, 132), (87, 157)], [(78, 106), (74, 132), (71, 157)]]}
def place(inner, k, src, dst):
    return f'<g transform="translate({dst[0] - src[0]*k:.2f} {dst[1] - src[1]*k:.2f}) scale({k})">{inner}</g>'
def badge(kind, sc):
    W = H = 120
    s = f'<circle cx="60" cy="60" r="52" fill="{P}"/><clipPath id="cp{kind}{sc}"><circle cx="60" cy="60" r="52"/></clipPath><g clip-path="url(#cp{kind}{sc})">'
    if kind == 'hill':
        s += f'<path d="M0,86 Q30,76 60,84 T120,80 L120,120 L0,120 Z" fill="{C}"/>'
        s += place(person(J_STAND, 1, sc), 0.36, (64, 157), (60, 84))
    if kind == 'piano':
        s += f'<path d="M0,90 Q40,84 60,88 T120,86 L120,120 L0,120 Z" fill="{C}"/>'
        s += place(stool() + piano(floor_y=162) + person(J_SIT, 1, sc), 0.42, (126, 160), (60, 89))
    if kind == 'balloon':
        s += f'<path d="M0,86 Q40,78 60,84 T120,82 L120,120 L0,120 Z" fill="{C}"/>'
        bal = (f'<path d="M126,64 C134,46 146,36 150,26" fill="none" stroke="{N}" stroke-width="2.2"/>'
               f'<ellipse cx="152" cy="12" rx="13" ry="16" fill="{C}" stroke="{N}" stroke-width="2.2"/>')
        s += place(bal + person(J_BAL, 1, sc), 0.38, (80, 157), (52, 84))
    s += '</g>' + f'<circle cx="60" cy="60" r="52" fill="none" stroke="{C}" stroke-width="3"/>'
    return svg(W, H, s)

# ---- hands to match ----------------------------------------------------------------------------------
HAND = 'M8,56 L92,52 Q112,50 130,40 Q150,30 166,46 Q178,60 176,108 Q176,114 170,113 Q166,112 164,104 Q160,74 146,66 Q128,62 112,72 L92,76 L8,78 Z'
def h_side(sc):
    W, H = 240, 140
    keys = f'<rect x="10" y="112" width="220" height="16" rx="3" fill="{P}" stroke="{N}" stroke-width="2.6"/>' + ''.join(L((10 + i * 22, 112), (10 + i * 22, 128), 1.4) for i in range(1, 10))
    ball = f'<circle cx="138" cy="84" r="20" fill="{C}"/><path d="M126,68 q8,16 0,32 M150,68 q-8,16 0,32" fill="none" stroke="#fff" stroke-width="2"/>'
    fill = P if sc == 'line' else N
    s = keys + ball + f'<path d="{HAND}" fill="{fill}" stroke="{N}" stroke-width="2.6" stroke-linejoin="round"/>'
    sleeve = C if sc == 'line' else N
    s += f'<path d="M4,53 L62,50.5 Q66,64 62,78.5 L4,80 Z" fill="{sleeve}" stroke="{N}" stroke-width="2.6" stroke-linejoin="round"/>'
    if sc == 'ink': s += L((58, 52), (58, 78), 1.6, P)
    s += f'<circle cx="171" cy="111" r="4.5" fill="{C}"/>'
    return svg(W, H, s)

def h_top(sc, sd):
    W, H = 150, 176
    R = sd == 'R'
    xs = [44, 66, 88, 110] if R else [106, 84, 62, 40]; tops = [34, 24, 32, 48]
    fill = P if sc == 'line' else N
    numc = C if sc == 'line' else P
    px0 = 30 if R else 24
    s = f'<rect x="{px0}" y="88" width="96" height="62" rx="24" fill="{fill}" stroke="{N}" stroke-width="2.6"/>'
    for x, t in zip(xs, tops): s += f'<rect x="{x-9}" y="{t}" width="18" height="{100-t}" rx="9" fill="{fill}" stroke="{N}" stroke-width="2.6"/>'
    tx = 34 if R else 116; ang = -38 if R else 38
    s += f'<g transform="rotate({ang} {tx} 118)"><rect x="{tx-10}" y="72" width="20" height="52" rx="10" fill="{fill}" stroke="{N}" stroke-width="2.6"/></g>'
    s += f'<rect x="{px0+3}" y="92" width="90" height="20" fill="{fill}"/>'
    for i, (x, t) in enumerate(zip(xs, tops)):
        s += f'<text x="{x}" y="{t+17}" text-anchor="middle" font-size="13" font-weight="900" fill="{numc}" font-family="Inter,sans-serif">{i+2}</text>'
    a = math.radians(ang); nx, ny = tx + 34 * math.sin(a), 118 - 34 * math.cos(a)
    s += f'<text x="{nx:.1f}" y="{ny+5:.1f}" text-anchor="middle" font-size="13" font-weight="900" fill="{numc}" font-family="Inter,sans-serif">1</text>'
    sleeve = C if sc == 'line' else N
    s += f'<rect x="{px0+10}" y="142" width="76" height="30" rx="6" fill="{sleeve}" stroke="{N}" stroke-width="2.6"/>'
    s += f'<text x="{px0+48}" y="{128}" text-anchor="middle" font-size="12.5" font-weight="800" fill="{N if sc == "line" else P}" font-family="Inter,sans-serif">{"Right" if R else "Left"}</text>'
    return svg(W, H, s)

for sc in ['line', 'ink']:
    for name, fn in [('stand', s_stand), ('sit', s_sit), ('balloon', s_balloon), ('dive', s_dive)]:
        open(f'svg/P{sc}-{name}.svg', 'w').write(fn(sc))
    for k in ['hill', 'piano', 'balloon']:
        open(f'svg/P{sc}-badge-{k}.svg', 'w').write(badge(k, sc))
    open(f'svg/P{sc}-hand-side.svg', 'w').write(h_side(sc))
    open(f'svg/P{sc}-hand-L.svg', 'w').write(h_top(sc, 'L'))
    open(f'svg/P{sc}-hand-R.svg', 'w').write(h_top(sc, 'R'))

rows = ''
for sc in ['line', 'ink']:
    rows += f'<h2>{sc}</h2><div class="row">' + ''.join(f'<div class="cell">{open(f"svg/P{sc}-{n}.svg").read()}</div>' for n in ['stand', 'sit', 'balloon', 'dive']) + '</div>'
    rows += '<div class="row">' + ''.join(f'<div class="cell">{open(f"svg/P{sc}-{n}.svg").read()}</div>' for n in ['badge-hill', 'badge-piano', 'badge-balloon', 'hand-side', 'hand-L', 'hand-R']) + '</div>'
open('preview3.html', 'w').write(f'<!doctype html><html><head><style>body{{font-family:Inter,sans-serif;background:#fff;color:{N};margin:16px}} h2{{margin:10px 0 6px;font-size:16px}} .row{{display:flex;gap:12px;align-items:flex-end;flex-wrap:wrap;margin-bottom:10px}} .cell{{background:{F};border-radius:12px;padding:6px}} .cell svg{{width:auto;height:190px;display:block}}</style></head><body>{rows}</body></html>')
print('ok')
