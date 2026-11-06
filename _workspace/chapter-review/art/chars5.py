# Chapter 1 art in the chosen style E ("ink"): a faceless kid with a navy bob, solid navy clothes,
# paper face and hands; coral only on the thing being learnt. Big hand close-ups are drawn in line
# (paper hand, navy outline, navy sleeve) to save ink. Writes svg/e-*.svg, a preview, and a3/art369.jsx.
import math, json, os
import chars3
from chars3 import add, sub, unit, pts, limb
from chars import N, C, P, F, L, svg

K = chars3.SCHEMES['ink']
SW = 2.2

# ---- the figure ------------------------------------------------------------------------------------
def head(hc, u, face, bun=False):
    ang = math.degrees(math.atan2(u[1], u[0])) - 90
    if face == 0:
        g = f'<g transform="translate({hc[0]:.1f} {hc[1]:.1f}) rotate({ang:.1f})">'
        g += f'<ellipse cx="0" cy="0" rx="8" ry="9.6" fill="{P}" stroke="{N}" stroke-width="{SW}"/>'
        g += f'<path d="M-9.4,2 C-11,-9 -5,-12.6 0,-12.4 C5,-12.6 11,-9 9.4,2 C8,-2 5,-5 0,-5.4 C-5,-5 -8,-2 -9.4,2 Z M-1.6,-11.8 C-2.6,-17.4 1,-21.6 6.4,-21 C11.6,-20.4 13.8,-14 12.8,-7.4 C11.4,-11.4 8.8,-15 5.2,-15.4 C2.8,-15.6 1.4,-14 1.6,-11.8 Z" fill="{N}"/>'
        return g + '</g>'
    g = f'<g transform="translate({hc[0]:.1f} {hc[1]:.1f}) rotate({ang:.1f}) scale({face} 1)">'
    g += f'<ellipse cx="0" cy="0" rx="8" ry="9.6" fill="{P}" stroke="{N}" stroke-width="{SW}"/>'
    if bun:
        g += f'<circle cx="-8.6" cy="-6.6" r="4.6" fill="{N}"/>'
        g += f'<path d="M5.4,-7.6 C-1,-12.6 -10,-8.6 -9.8,-1 L-9,2.6 C-6,2 -3.6,-1 -3.2,-4.2 C-1,-6 2,-6.4 5.6,-5.4 Z" fill="{N}"/>'
    else:
        g += f'<path d="M5,-8.2 C-1,-12.5 -11,-8 -10.4,1 C-10,4.6 -8.6,7.4 -7,8.4 C-7.6,4 -6,-1.6 -3.6,-4 C-1,-5.8 2.5,-6.2 5.6,-5.6 Z M-5.4,-10.6 C-8,-15.8 -15.4,-16.4 -18.4,-11 C-21,-6 -19.4,2 -16.4,6.4 C-16,0 -14.6,-6 -11,-9.4 C-9.4,-10.6 -7.6,-10.2 -6.4,-8.8 Z" fill="{N}"/>'
    return g + '</g>'

def jumper(nk, hp, coat=0):
    u = unit(sub(hp, nk)); p = (-u[1], u[0])
    end = add(hp, u, coat)
    sh1, sh2 = add(add(nk, p, 10), u, 2), add(add(nk, p, -10), u, 2)
    h1, h2 = add(end, p, 11.5 + coat * 0.15), add(end, p, -11.5 - coat * 0.15)
    top = add(nk, u, -2.5); c1, c2 = add(sh1, u, 18), add(sh2, u, 18)
    d = (f'M{sh1[0]:.1f},{sh1[1]:.1f} Q{c1[0]:.1f},{c1[1]:.1f} {h1[0]:.1f},{h1[1]:.1f} L{h2[0]:.1f},{h2[1]:.1f} '
         f'Q{c2[0]:.1f},{c2[1]:.1f} {sh2[0]:.1f},{sh2[1]:.1f} Q{top[0]:.1f},{top[1]:.1f} {sh1[0]:.1f},{sh1[1]:.1f} Z')
    return f'<path d="{d}" fill="{N}" stroke="{N}" stroke-width="{SW}" stroke-linejoin="round"/>'

def arm(ch):
    sh, el, wr = ch[:3]
    s = limb([sh, el, wr], 5.2, N)
    hand = ch[3] if len(ch) > 3 else add(wr, unit(sub(wr, el)), 4)
    return s + limb([wr, hand], 3.6, P, N, 1.6)

def leg(ch, face, shoe=True):
    s = limb(ch, 5, N)
    a = ch[-1]
    if shoe: s += f'<ellipse cx="{a[0] + 4 * (face if face else 0):.1f}" cy="{a[1] + 1:.1f}" rx="{6 if face else 4.4}" ry="3" fill="{N}"/>'
    return s

def kid(j, face=1, coat=0, bun=False):
    u = unit(sub(j['hip'], j['neck']))
    s = ''
    legs, arms = j['legs'], j['arms']
    if len(legs) > 1: s += leg(legs[1], face)
    if len(arms) > 1 and face != 0: s += arm(arms[1])
    s += leg(legs[0], face)
    s += jumper(j['neck'], j['hip'], coat)
    if face == 0 and len(arms) > 1: s += arm(arms[1])
    s += arm(arms[0])
    s += L(add(j['head'], u, 8), j['neck'], 3.4, N)
    s += head(j['head'], u, face, bun)
    return s

# ---- props -----------------------------------------------------------------------------------------
def floor(W, y=162): return L((6, y), (W - 6, y), 1.6, '#bdb7a6')
def piano(x=150, y=58, floor_y=162, key_y=98):
    s = f'<rect data-rigid="1" x="{x}" y="{y}" width="56" height="{floor_y-y}" rx="2.5" fill="{P}" stroke="{N}" stroke-width="2.4"/>'
    s += f'<rect data-rigid="1" x="{x-26}" y="{key_y}" width="30" height="8.5" rx="1.5" fill="{P}" stroke="{N}" stroke-width="2.2"/>' + ''.join(L((x - 26 + i * 7.5, key_y), (x - 26 + i * 7.5, key_y + 8.5), 1.2).replace('<line ', '<line data-rigid="1" ') for i in range(1, 4))
    return s
def stool(x1=46, x2=100, y=114, floor_y=162):
    return f'<rect x="{x1}" y="{y}" width="{x2-x1}" height="7" rx="2" fill="{P}" stroke="{N}" stroke-width="2.4"/>' + L((x1 + 7, y + 7), (x1 + 7, floor_y), 2.4) + L((x2 - 7, y + 7), (x2 - 7, floor_y), 2.4)
def keyrow(x, y, n, w=9.5, h=10):
    return f'<rect data-rigid="1" x="{x}" y="{y}" width="{n*w}" height="{h}" rx="1.5" fill="{P}" stroke="{N}" stroke-width="2.2"/>' + ''.join(L((x + i * w, y), (x + i * w, y + h), 1.2).replace('<line ', '<line data-rigid="1" ') for i in range(1, n))
def place(inner, k, src, dst): return f'<g transform="translate({dst[0] - src[0]*k:.2f} {dst[1] - src[1]*k:.2f}) scale({k})">{inner}</g>'
def keylevel(x2=122):
    return (f'<text x="8" y="91" font-size="8.5" font-weight="800" fill="{C}" font-family="Inter,sans-serif">key level</text>'
            f'<line x1="8" y1="96" x2="{x2}" y2="96" stroke="{C}" stroke-width="1.3" stroke-dasharray="4 4"/>')

J_SIT = {'hip': (76, 110), 'neck': (81, 68), 'head': (84, 53),
         'arms': [[(83, 71), (98, 91), (121, 92), (128, 98)], [(79, 72), (93, 93), (116, 94), (123, 99)]],
         'legs': [[(78, 110), (108, 111), (108, 155)], [(73, 111), (101, 113), (100, 155)]]}
SIT_BASE = stool() + piano() + kid(J_SIT)

ART = {}
def put(name, w, h, body): ART[name] = svg(w, h, body)

# 1. opener: sit tall like a puppet on a string
put('puppet', 220, 190, f'<g transform="translate(0 18)">{floor(220)}{SIT_BASE}</g>'
    + f'<line x1="84" y1="60" x2="84" y2="16" stroke="{C}" stroke-width="1.8" stroke-dasharray="3 3.5"/>'
    + f'<rect x="66" y="10" width="36" height="5" rx="2" fill="{N}"/><rect x="81.5" y="2" width="5" height="21" rx="2" fill="{N}"/>')
# 2. good sitting
put('sit', 220, 172, floor(220) + keylevel() + SIT_BASE)
# 3. not like this
chair = (f'<path d="M30,64 L38,114" stroke="{N}" stroke-width="5" stroke-linecap="round"/><rect x="34" y="110" width="58" height="9" rx="3" fill="{P}" stroke="{N}" stroke-width="2.4"/>'
         + L((40, 119), (40, 162), 2.4) + L((86, 119), (86, 162), 2.4))
put('not-sofa', 220, 172, floor(220) + chair + piano() + kid({'hip': (66, 108), 'neck': (50, 70), 'head': (45, 56),
    'arms': [[(53, 73), (84, 90), (118, 95), (125, 99)], [(49, 74), (80, 92), (114, 97)]],
    'legs': [[(68, 108), (100, 106), (104, 154)], [(64, 109), (95, 109), (97, 154)]]}))
put('not-close', 220, 172, floor(220) + stool(78, 130) + piano() + kid({'hip': (104, 110), 'neck': (106, 68), 'head': (108, 54),
    'arms': [[(108, 72), (99, 95), (121, 95), (127, 99)], [(104, 72), (96, 96), (117, 96)]],
    'legs': [[(106, 110), (128, 112), (126, 155)], [(102, 111), (124, 113), (121, 155)]]})
    + f'<path d="M92,100 q-6,-4 -4,-10 M90,104 q-9,-3 -9,-12" fill="none" stroke="{C}" stroke-width="1.6" stroke-linecap="round"/>')
put('not-swing', 220, 172, floor(220) + stool(46, 100, 100) + piano() + kid({'hip': (76, 96), 'neck': (80, 56), 'head': (83, 42),
    'arms': [[(82, 60), (96, 78), (121, 94), (127, 99)], [(78, 61), (92, 80), (117, 96)]],
    'legs': [[(78, 96), (104, 98), (100, 128)], [(73, 97), (97, 100), (92, 126)]]})
    + f'<path d="M86,136 q8,6 18,0 M84,142 q10,7 22,0" fill="none" stroke="{C}" stroke-width="1.6" stroke-linecap="round"/>')

# 4. the six warm-ups
put('ragdoll', 150, 172, floor(150) + kid({'hip': (70, 104), 'neck': (90, 72), 'head': (100, 63),
    'arms': [[(89, 75), (90, 97), (89, 117), (89, 123)], [(85, 77), (84, 99), (83, 119)]],
    'legs': [[(72, 104), (73, 131), (74, 157)], [(68, 104), (66, 131), (64, 157)]]})
    + f'<path d="M80,128 l-4,4 l4,4 l-4,4 M98,128 l4,4 l-4,4 l4,4" fill="none" stroke="{C}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')

HAND = 'M8,56 L92,52 Q112,50 130,40 Q150,30 166,46 Q178,60 176,108 Q176,114 170,113 Q166,112 164,104 Q160,74 146,66 Q128,62 112,72 L92,76 L8,78 Z'
def handbase(path=HAND, ball=True, tip=(171, 111), keys=True):
    s = ''
    if keys: s += keyrow(10, 112, 10, 22, 16)
    if ball: s += f'<circle cx="138" cy="84" r="20" fill="none" stroke="{C}" stroke-width="2.4"/><path d="M126,68 q8,16 0,32 M150,68 q-8,16 0,32" fill="none" stroke="{C}" stroke-width="1.4"/>'
    s += f'<path d="{path}" fill="{P}" stroke="{N}" stroke-width="2.6" stroke-linejoin="round"/>'
    s += f'<path d="M4,53 L62,50.5 Q66,64 62,78.5 L4,80 Z" fill="{N}" stroke="{N}" stroke-width="2.6" stroke-linejoin="round"/>'
    if tip: s += f'<circle cx="{tip[0]}" cy="{tip[1]}" r="4.2" fill="{C}"/>'
    return s
car = (f'<g transform="translate(104 37) rotate(-26)"><rect x="-13" y="-9" width="26" height="9" rx="3.5" fill="{C}"/><rect x="-7" y="-15" width="13" height="7" rx="3" fill="{C}"/>'
       f'<circle cx="-7" cy="1" r="3.3" fill="{N}"/><circle cx="7" cy="1" r="3.3" fill="{N}"/></g>')
put('bridge', 240, 140, handbase(ball=False) + car)

put('glide', 220, 160, L((6, 152), (214, 152), 1.6, '#bdb7a6') + keyrow(112, 80, 10)
    + ''.join(L((x, y), (x + 18, y), 1.8, N) for x, y in [(8, 60), (14, 72), (8, 84)])
    + kid({'hip': (64, 100), 'neck': (74, 60), 'head': (79, 46),
           'arms': [[(76, 64), (98, 74), (120, 75), (127, 79)], [(72, 64), (56, 78), (44, 90)]],
           'legs': [[(66, 100), (82, 120), (84, 140)], [(62, 100), (48, 119), (34, 133)]]})
    + f'<rect x="76" y="138" width="17" height="6" rx="3" fill="{N}"/><circle cx="79" cy="147" r="3" fill="{C}"/><circle cx="90" cy="147" r="3" fill="{C}"/>'
    + f'<g transform="rotate(-22 34 133)"><rect x="26" y="131" width="17" height="6" rx="3" fill="{N}"/><circle cx="29" cy="140" r="3" fill="{C}"/><circle cx="40" cy="140" r="3" fill="{C}"/></g>')

put('wings', 150, 172, floor(150) + kid({'hip': (75, 106), 'neck': (75, 64), 'head': (75, 49),
    'arms': [[(84, 67), (104, 76), (92, 90), (87, 92)], [(66, 67), (46, 76), (58, 90), (63, 92)]],
    'legs': [[(79, 106), (80, 132), (81, 157)], [(71, 106), (70, 132), (69, 157)]]}, face=0)
    + f'<path d="M108,66 q5,4 4,12 M112,62 q8,6 6,18 M42,66 q-5,4 -4,12 M38,62 q-8,6 -6,18" fill="none" stroke="{C}" stroke-width="1.6" stroke-linecap="round"/>'
    + f'<path d="M112,24 q6,-6 12,0 q6,-6 12,0" fill="none" stroke="{N}" stroke-width="2" stroke-linecap="round"/>')

put('balloon', 220, 172, floor(220) + keyrow(112, 104, 8)
    + f'<path d="M124,80 C130,58 148,50 151,40" fill="none" stroke="{N}" stroke-width="1.6"/><ellipse cx="153" cy="25" rx="13" ry="16" fill="{C}"/><path d="M150,41 l3,-4 l3,4 z" fill="{C}"/><ellipse cx="148" cy="19" rx="3" ry="5" fill="#fff" opacity="0.45"/>'
    + kid({'hip': (80, 106), 'neck': (80, 64), 'head': (82, 50),
           'arms': [[(82, 67), (103, 86), (124, 80), (130, 102)], [(78, 68), (74, 88), (75, 106)]],
           'legs': [[(82, 106), (85, 132), (87, 157)], [(78, 106), (74, 132), (71, 157)]]}))

d = (0.62, 0.78); pp = (-d[1], d[0]); hip = (96, 60); nk = add(hip, d, 36); hd = add(nk, d, 13)
wave = 'M90,142 q10,-7 20,0 t20,0 t20,0 t20,0 t20,0 t20,0'
put('dive', 220, 172, f'<rect x="6" y="70" width="62" height="7" rx="2" fill="{P}" stroke="{N}" stroke-width="2.6"/>' + L((18, 77), (18, 162), 2.6) + floor(220)
    + f'<path d="M64,60 Q92,24 124,64" fill="none" stroke="{N}" stroke-width="1.4" stroke-dasharray="3 5" opacity="0.6"/>'
    + f'<path d="{wave}" fill="none" stroke="{N}" stroke-width="2.4" stroke-linecap="round"/>'
    + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{C}"/>' for x, y, r in [(156, 130, 3.2), (166, 122, 2.6), (146, 123, 2.4), (174, 132, 2), (138, 133, 2)])
    + kid({'hip': hip, 'neck': nk, 'head': hd,
           'arms': [[add(nk, pp, 3), add(add(nk, d, 20), pp, 5), add(add(nk, d, 38), pp, 4), add(add(nk, d, 44), pp, 4)],
                    [add(nk, pp, -3), add(add(nk, d, 20), pp, -2), add(add(nk, d, 38), pp, -1), add(add(nk, d, 44), pp, -1)]],
           'legs': [[add(hip, pp, 3), add(add(hip, d, -24), pp, 4), add(add(hip, d, -46), pp, 4)], [add(hip, pp, -3), add(add(hip, d, -24), pp, -3), add(add(hip, d, -46), pp, -6)]]}))

# 5. the round hand and its faults (line, to save ink)
put('hand-good', 240, 140, handbase()
    + f'<text x="100" y="22" font-size="10.5" font-weight="800" fill="{N}" font-family="Inter,sans-serif">knuckles: a bridge</text><path d="M134,26 L132,34" stroke="{N}" stroke-width="1.4"/>'
    + f'<text x="184" y="104" font-size="10.5" font-weight="800" fill="{N}" font-family="Inter,sans-serif">tip</text>')
FLAT = 'M8,56 L92,54 Q130,52 176,96 Q182,104 176,108 Q170,110 164,104 Q140,82 112,74 L92,76 L8,78 Z'
put('hand-flat', 240, 140, handbase(FLAT, ball=False, tip=None) + f'<path d="M132,62 Q156,78 172,100" fill="none" stroke="{C}" stroke-width="3" stroke-linecap="round"/>')
CAVE = 'M8,56 L92,52 Q112,50 130,40 Q150,30 164,48 Q172,64 170,92 Q186,104 190,110 Q186,115 180,113 Q166,106 162,98 Q158,74 146,66 Q128,62 112,72 L92,76 L8,78 Z'
put('hand-cave', 240, 140, handbase(CAVE, ball=False, tip=None) + f'<path d="M168,90 Q178,100 190,110" fill="none" stroke="{C}" stroke-width="3" stroke-linecap="round"/>')
HIGH = 'M8,72 L70,62 Q96,30 122,22 Q146,16 156,40 Q164,62 164,106 Q164,114 158,113 Q152,112 152,104 Q148,62 136,52 Q118,50 100,70 L70,84 L8,94 Z'
put('hand-high', 240, 140, keyrow(10, 112, 10, 22, 16) + f'<path d="{HIGH}" fill="{P}" stroke="{N}" stroke-width="2.6" stroke-linejoin="round"/>'
    + f'<path d="M4,69 L62,63 Q68,76 64,85 L4,96 Z" fill="{N}" stroke="{N}" stroke-width="2.6" stroke-linejoin="round"/>' + f'<path d="M84,52 Q96,30 118,22" fill="none" stroke="{C}" stroke-width="3" stroke-linecap="round"/>')
put('hand-thumb', 160, 110, keyrow(6, 80, 6, 25, 14)
    + f'<g transform="rotate(22 80 70)"><rect x="54" y="52" width="58" height="22" rx="11" fill="{P}" stroke="{N}" stroke-width="2.6"/><path d="M98,56 q6,6 0,14" fill="none" stroke="{N}" stroke-width="1.4"/></g>'
    + f'<circle cx="104" cy="80" r="4.2" fill="{C}"/>'
    + f'<path d="M14,40 L44,40 L38,48 L20,48 Z" fill="{P}" stroke="{N}" stroke-width="2" transform="rotate(-18 29 44)"/><path d="M30,38 L30,20 L42,34 Z" fill="{C}" transform="rotate(-18 29 44)"/>')

# 6. finger numbers: line hands with navy sleeves, and the mirror game
def hand_top(sd):
    R = sd == 'R'
    xs = [44, 66, 88, 110] if R else [106, 84, 62, 40]; tops = [34, 24, 32, 48]
    px0 = 30 if R else 24
    s = f'<rect x="{px0}" y="88" width="96" height="62" rx="24" fill="{P}" stroke="{N}" stroke-width="2.6"/>'
    for x, t in zip(xs, tops): s += f'<rect x="{x-9}" y="{t}" width="18" height="{100-t}" rx="9" fill="{P}" stroke="{N}" stroke-width="2.6"/>'
    tx = 34 if R else 116; ang = -38 if R else 38
    s += f'<g transform="rotate({ang} {tx} 118)"><rect x="{tx-10}" y="72" width="20" height="52" rx="10" fill="{P}" stroke="{N}" stroke-width="2.6"/></g>'
    s += f'<rect x="{px0+3}" y="92" width="90" height="20" fill="{P}"/>'
    for i, (x, t) in enumerate(zip(xs, tops)):
        s += f'<text x="{x}" y="{t+17}" text-anchor="middle" font-size="13" font-weight="900" fill="{N}" font-family="Inter,sans-serif">{i+2}</text>'
    a = math.radians(ang); nx, ny = tx + 34 * math.sin(a), 118 - 34 * math.cos(a)
    s += f'<circle cx="{nx:.1f}" cy="{ny:.1f}" r="9" fill="{C}"/><text x="{nx:.1f}" y="{ny+4.6:.1f}" text-anchor="middle" font-size="13" font-weight="900" fill="#fff" font-family="Inter,sans-serif">1</text>'
    s += f'<rect x="{px0+10}" y="142" width="76" height="30" rx="6" fill="{N}"/>'
    s += f'<text x="{px0+48}" y="128" text-anchor="middle" font-size="12.5" font-weight="800" fill="{N}" font-family="Inter,sans-serif">{"Right" if R else "Left"}</text>'
    return svg(150, 176, s)
ART['hand-L'] = hand_top('L'); ART['hand-R'] = hand_top('R')

def palm(c, r=1):
    x, y = c
    return ''.join(L((x, y), (x + dx * r, y + dy * r), 2.4, N) for dx, dy in [(-4, -9), (-1, -11), (2, -11), (5, -9), (7, -3)]) + f'<circle cx="{x}" cy="{y}" r="4.2" fill="{P}" stroke="{N}" stroke-width="1.6"/>'
put('mirror', 240, 172, floor(240)
    + kid({'hip': (70, 106), 'neck': (70, 66), 'head': (72, 52),
           'arms': [[(72, 69), (88, 72), (98, 56)], [(68, 70), (66, 90), (67, 106)]],
           'legs': [[(72, 106), (74, 132), (75, 157)], [(68, 106), (66, 132), (64, 157)]]})
    + kid({'hip': (172, 92), 'neck': (172, 44), 'head': (170, 29),
           'arms': [[(170, 48), (150, 56), (140, 40)], [(174, 48), (176, 72), (175, 92)]],
           'legs': [[(170, 92), (168, 126), (166, 157)], [(174, 92), (176, 126), (178, 157)]]}, face=-1, coat=18, bun=True)
    + f'<line x1="104" y1="48" x2="134" y2="34" stroke="{C}" stroke-width="1.6" stroke-dasharray="3 4"/>'
    + f'<text x="118" y="104" text-anchor="middle" font-size="9.5" font-weight="800" fill="{C}" font-family="Inter,sans-serif">"Right hand, 3!"</text>')

# 7. tune icons
def mini(j, face=1, k=0.42, at=(0, 0), src=(64, 157)): return place(kid(j, face), k, src, at)
J_STAND = {'hip': (64, 104), 'neck': (64, 63), 'head': (65, 49),
           'arms': [[(66, 66), (69, 86), (68, 104)], [(62, 66), (58, 86), (59, 104)]],
           'legs': [[(66, 104), (67, 131), (68, 157)], [(62, 104), (60, 131), (58, 157)]]}
J_WAVE = {**J_STAND, 'arms': [[(66, 66), (78, 54), (84, 38), (86, 31)], [(62, 66), (58, 86), (59, 104)]]}
stairs = ''.join(f'<path d="M{8+i*10},{88-i*10} L{18+i*10},{88-i*10} L{18+i*10},{78-i*10}" fill="none" stroke="{N}" stroke-width="2.2" stroke-linejoin="round"/>' for i in range(4))
put('tune-stairs', 120, 96, L((4, 90), (116, 90), 1.4, '#bdb7a6') + f'<path d="M8,88 L8,88" />' + stairs
    + f'<path d="M48,48 L56,48 C70,48 76,86 104,88" fill="none" stroke="{C}" stroke-width="3" stroke-linecap="round"/>' + mini(J_WAVE, 1, 0.3, (52, 48)))
J_HOP = {'hip': (64, 98), 'neck': (66, 58), 'head': (68, 44),
         'arms': [[(68, 62), (78, 52), (86, 44)], [(64, 62), (54, 52), (48, 44)]],
         'legs': [[(66, 98), (68, 122), (66, 144)], [(62, 98), (52, 112), (60, 124)]]}
put('tune-hop', 120, 96, L((4, 90), (116, 90), 1.4, '#bdb7a6') + f'<path d="M16,88 Q30,52 46,88 M48,88 Q62,52 78,88" fill="none" stroke="{C}" stroke-width="2" stroke-dasharray="3 3"/>' + mini(J_HOP, 1, 0.38, (92, 72), (64, 146)))
put('tune-neighbours', 120, 96, L((4, 90), (116, 90), 1.4, '#bdb7a6') + mini(J_WAVE, 1, 0.38, (38, 90)) + mini(J_WAVE, -1, 0.38, (84, 90)).replace('scale(0.38)', 'scale(-0.38 0.38)').replace(f'translate({84 - 64*0.38:.2f}', f'translate({84 + 64*0.38:.2f}')
    + f'<path d="M54,44 q7,-6 14,0" fill="none" stroke="{C}" stroke-width="2" stroke-linecap="round"/>')

# 8. the five checks: the sitting picture, each with its own coral mark
def check(mark):
    return svg(150, 120, place(f'{floor(220)}{SIT_BASE}{mark}', 0.66, (126, 108), (75, 72)))
ART['chk-front'] = check(f'<rect x="62" y="110" width="38" height="5" rx="2" fill="{C}"/>')
ART['chk-feet'] = check(f'<line x1="94" y1="161" x2="124" y2="161" stroke="{C}" stroke-width="4" stroke-linecap="round"/>')
ART['chk-tall'] = check(f'<line x1="84" y1="42" x2="84" y2="4" stroke="{C}" stroke-width="2.4" stroke-dasharray="3 4"/>')
ART['chk-forearm'] = check(f'<line x1="90" y1="88" x2="136" y2="88" stroke="{C}" stroke-width="2.4" stroke-dasharray="4 4"/>')
ART['chk-hand'] = svg(150, 120, place(handbase(), 0.6, (120, 70), (75, 62)))

def _write():
    os.makedirs('svg', exist_ok=True)
    for k, v in ART.items(): open(f'svg/e-{k}.svg', 'w').write(v)
    cells = ''.join(f'<div class="cell">{v}<p>{k}</p></div>' for k, v in ART.items())
    open('preview5.html', 'w').write(f'<!doctype html><html><head><style>body{{font-family:Inter,sans-serif;background:#fff;color:{N};margin:14px}} .row{{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}} .cell{{border:1px solid #eee6d6;border-radius:10px;padding:6px}} .cell svg{{width:auto;height:170px;display:block}} p{{margin:2px 0 0;font-size:11px}}</style></head><body><div class="row">{cells}</div></body></html>')

    # the art for the app: plain SVG strings (width/height dropped; the page sizes them)
    import re
    js = {k: re.sub(r' width="\d+" height="\d+">', '>', v, count=1).replace('<svg xmlns="http://www.w3.org/2000/svg" ', '<svg ') for k, v in ART.items()}
    open('../a3/art369.jsx', 'w').write('// Phase 369: chapter 1 drawings in the chosen style (E, "ink": a faceless kid with a navy bob; coral only on the thing being learnt).\n'
        '// Generated from chars/chars5.py -- edit the generator, not this file.\n'
        'const PB_ART = ' + json.dumps(js, ensure_ascii=False, indent=0) + ';\n'
        'function PbArt({ name, h = 120, style }) {\n'
        '  const s = PB_ART[name]; if (!s) return null;\n'
        '  const m = /viewBox="0 0 ([\\d.]+) ([\\d.]+)"/.exec(s); const w = m ? h * (+m[1]) / (+m[2]) : h;\n'
        "  return <span className=\"pb-art\" data-art={name} style={{display:'inline-block',lineHeight:0,width:w,height:h,flex:'0 0 auto',...style}} dangerouslySetInnerHTML={{__html: s.replace('<svg ', '<svg width=\"100%\" height=\"100%\" ')}}/>;\n"
        '}\n')
    print(len(ART), 'drawings;', sum(len(v) for v in js.values()) // 1024, 'KB')

if __name__ == '__main__': _write()
