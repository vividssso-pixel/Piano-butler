# Round 7b (Sohyun 2026-10-08): "the tortoise looks like an alien -- draw it differently so I can compare again;
# the rabbit is fine as a character". The first tortoise was a front view (round head on a long neck, big round
# spectacles, a flat disc of a shell). This one is a profile, the way a tortoise is easiest to recognise:
#   * a high domed shell with hexagonal plates and growth rings (engraving style), shaded with hatching underneath;
#   * a pale belly plate in front with its seams; stumpy scaly legs with toenails; a short pointed tail;
#   * a wrinkled neck, an oval head with a hooked beak-like mouth and a calm, heavy-lidded eye (never in a hurry);
#   * white gloves, the coral bow tie, the metronome.
import math, re
import chars8, chars10
from chars6 import ell, dot, path, bowtie, glove, limb, metronome
from chars import N, C, P, L, svg

H = 'url(#HATCH)'
def poly(ps, fill=P, sw=2, stroke=N):
    return f'<path d="M{" L".join(f"{x:.1f},{y:.1f}" for x, y in ps)} Z" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>'
def inset(ps, k):
    cx = sum(x for x, _ in ps) / len(ps); cy = sum(y for _, y in ps) / len(ps)
    return [(cx + (x - cx) * k, cy + (y - cy) * k) for x, y in ps]

def tortoise2(arm_r=None, metro=True):
    cx = 80; s = ''
    # tail, legs (stumpy, scaly, toenails)
    s += path(f'M{cx-30},{168} L{cx-44},{178} L{cx-28},{176} Z', fill=P, sw=2)
    for x in (cx - 16, cx + 8):
        s += path(f'M{x-7},{164} L{x-8},{194} C{x-8},{200} {x+12},{201} {x+13},{196} L{x+8},{164} Z', fill=P, sw=2.2)
        s += path(f'M{x-5},{176} q3,2 6,0 M{x+1},{184} q3,2 6,0 M{x-5},{190} q3,2 6,0', fill='none', sw=1)
        s += ''.join(L((x + 3 + dx, 197.6), (x + 5 + dx, 200.4), 1.3) for dx in (0, 4.5, 9))
    # the carapace: a high dome over the back
    dome = f'M{cx+4},{84} C{cx-24},{80} {cx-46},{112} {cx-44},{140} C{cx-42},{162} {cx-26},{176} {cx-2},{176} C{cx+6},{150} {cx+10},{112} {cx+4},{84} Z'
    s += path(dome, fill=P, sw=2.4)
    # shading under the dome
    s += path(f'M{cx-44},{140} C{cx-42},{162} {cx-26},{176} {cx-2},{176} C{cx+1},{168} {cx+2},{162} {cx+3},{156} C{cx-14},{164} {cx-34},{158} {cx-44},{140} Z', fill=H, sw=0, stroke='none')
    # plates: a row along the spine and a row on the flank, each with a growth ring; a rim of small edge plates
    spine = [[(cx-6, 92), (cx-20, 94), (cx-26, 108), (cx-14, 116), (cx-2, 108)],
             [(cx-14, 116), (cx-26, 108), (cx-36, 120), (cx-34, 134), (cx-20, 138), (cx-10, 128)],
             [(cx-20, 138), (cx-34, 134), (cx-39, 148), (cx-30, 160), (cx-18, 156)]]
    flank = [[(cx-2, 108), (cx-14, 116), (cx-10, 128), (cx+3, 128)],
             [(cx-10, 128), (cx-20, 138), (cx-18, 156), (cx-4, 158), (cx+3, 140)]]
    for pl in spine + flank:
        s += poly(pl, 'none', 1.8) + poly(inset(pl, 0.55), 'none', 1)
    s += path(f'M{cx-30},{168} C{cx-20},{173} {cx-10},{172} {cx-2},{170}', fill='none', sw=1.4)
    s += ''.join(L((cx - 28 + i * 7, 166 + (0 if i < 2 else 1) + i * 0.6), (cx - 30 + i * 7, 173 - i * 0.3), 1.2) for i in range(4))
    # the belly plate in front, pale, with its seams
    s += path(f'M{cx+4},{84} C{cx+10},{112} {cx+6},{150} {cx-2},{176} C{cx+14},{174} {cx+26},{152} {cx+26},{128} C{cx+26},{104} {cx+18},{88} {cx+4},{84} Z', fill=P, sw=2.4)
    s += path(f'M{cx+8},{106} Q{cx+17},{104} {cx+25},{110} M{cx+8},{128} Q{cx+17},{126} {cx+26},{130} M{cx+5},{150} Q{cx+14},{149} {cx+22},{153}', fill='none', sw=1.3)
    # neck: short and wrinkled, leaning forward; then the head
    s += path(f'M{cx+5},{92} C{cx+6},{78} {cx+12},{70} {cx+20},{64} L{cx+30},{72} C{cx+24},{78} {cx+22},{86} {cx+22},{96} Z', fill=P, sw=2.2)
    s += path(f'M{cx+9},{86} q6,-1 11,3 M{cx+11},{78} q6,-1 10,3 M{cx+15},{71} q5,0 8,3', fill='none', sw=1)
    s += f'<g transform="rotate(-3 {cx+28} {58})">' + path(f'M{cx+14},{58} C{cx+14},{49} {cx+22},{46} {cx+30},{46} C{cx+40},{46} {cx+46},{52} {cx+46},{58} C{cx+46},{64} {cx+40},{68} {cx+30},{68} C{cx+21},{68} {cx+14},{65} {cx+14},{58} Z', fill=P, sw=2.4)
    # beak-like mouth with a small hook, a nostril, a calm heavy-lidded eye
    s += path(f'M{cx+46},{59.5} Q{cx+44.5},{63} {cx+40},{63} Q{cx+33},{63.4} {cx+28.6},{60.6}', fill='none', sw=1.7)
    s += path(f'M{cx+28.6},{60.6} q-1.4,-0.6 -2,-2', fill='none', sw=1.3)
    s += dot(cx + 43, 53.6, 1.2)
    s += f'<ellipse cx="{cx+32.4}" cy="{55}" rx="2.3" ry="2.6" fill="{N}"/>'
    s += path(f'M{cx+28.6},{53.2} Q{cx+32.4},{50.2} {cx+36.4},{53.2}', fill='none', sw=1.6)
    s += path(f'M{cx+27.6},{48.6} Q{cx+31.6},{46.4} {cx+35.6},{48}', fill='none', sw=1.1)
    s += '</g>'
    s += bowtie(cx + 16, 92, 0.9)
    # the near arm: stumpy and scaly, a white glove
    ar = arm_r or [(cx + 12, 104), (cx + 22, 124), (cx + 33, 118)]
    s += limb(ar, 9, P) + glove(*ar[-1], 5.6)
    s += path(f'M{ar[0][0]+2},{ar[0][1]+8} q3,2 6,1', fill='none', sw=1)
    if metro and not arm_r: s += metronome(cx + 39, 114)
    return s

chars10.B['tortoise2'] = dict(fn=tortoise2, k=0.94, rx=56, arm=[(92, 104), (110, 98), (122, 84)], top=44)
ART = {
    'tortoise2': svg(160, 210, tortoise2()),
    'tortoise2-bust': f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="82 40 50 60" width="100" height="120">{tortoise2(metro=False)}</svg>',
    'tortoise2-open': chars10.opener('tortoise2', 'girl'),
}
PEN = {k: chars8.bake(chars8.to_pen(v), 'r7b' + re.sub(r'[^a-z0-9]', '', k)[:12], chars8.field) for k, v in ART.items()}
if __name__ == '__main__':
    for k, v in PEN.items(): open(f'svg/r7b-{k}.svg', 'w').write(v)
    cells = ''.join(f'<div class="cell">{v}<p>{k}</p></div>' for k, v in PEN.items())
    cells += f'<div class="cell">{open("svg/r7-butler-rabbit.svg").read()}<p>rabbit</p></div>'
    open('preview11.html', 'w').write(f'<!doctype html><html><head><style>body{{font-family:Inter,sans-serif;margin:14px;background:#fff}} .row{{display:flex;gap:10px;flex-wrap:wrap;align-items:flex-end}} .cell{{border:1px solid #eee6d6;border-radius:10px;padding:6px;background:#fffdf7}} .cell svg{{width:auto;height:380px;display:block}} p{{margin:2px 0 0;font-size:11px}}</style></head><body><div class="row">{cells}</div></body></html>')
    print('ok', len(PEN))
