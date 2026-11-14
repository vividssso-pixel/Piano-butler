# Shared drawing kit for the Level book room scenes (her 14 Nov: "첫번째 비기너 방 다 만들어줘 먼저").
# One drawing per room gives the moving picture, the film and the simpler printed still.
import json, math, re
N, C, PK, T = '#26296b', '#e4572e', '#f4a9bb', '#f6f6fb'
P = json.load(open('/tmp/claude-0/lvl/pieces.json')); ART = json.load(open('/tmp/claude-0/lvl/pb-art.json'))
def inner(svg): return svg[svg.index('>') + 1:svg.rindex('</svg>')]
RAB = inner(ART['rabbit'])
CR, MI, SB, BR = '\U0001D15F', '\U0001D15E', '\U0001D15D', '\U0001D15C'
HATCH = f'<defs><pattern id="hcl" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="7" height="7" fill="#fffdf7"/><line x1="0" y1="0" x2="0" y2="7" stroke="{N}" stroke-width="2.2"/></pattern></defs>'
def wall(chand=True, win=True):
    o = [f'<rect width="1280" height="600" fill="{T}"/>', HATCH]
    o.append('<g class="deco">' + ''.join(f'<path d="M{x} {y - 5} l5 5 -5 5 -5 -5 z" fill="#e2e2ef"/>' for y in range(60, 470, 36) for x in range(18 + (y // 36 % 2) * 22, 1280, 44)) + '</g>')
    o.append(f'<rect width="1280" height="16" fill="{N}"/><rect y="16" width="1280" height="2" fill="#fff"/>' + ''.join(f'<rect x="{6 + k * 16}" y="24" width="8" height="8" fill="{N}"/>' for k in range(80)) + f'<rect y="38" width="1280" height="2" fill="{N}"/>')
    if win:
        o.append(f'<g class="deco" transform="translate(48 118) scale(.7)"><rect x="70" y="110" width="220" height="320" fill="{N}"/><circle cx="220" cy="180" r="26" fill="#fff"/><circle cx="232" cy="172" r="24" fill="{N}"/>'
                 + ''.join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#fff"/>' for x, y in ((110, 150), (150, 230), (250, 260), (120, 330), (200, 300), (260, 380)))
                 + f'<rect x="70" y="110" width="220" height="320" fill="none" stroke="#fff" stroke-width="10"/><line x1="180" x2="180" y1="110" y2="430" stroke="#fff" stroke-width="7"/><line x1="70" x2="290" y1="270" y2="270" stroke="#fff" stroke-width="7"/>'
                 + f'<path d="M40 86 Q80 260 70 450 L108 450 Q118 260 104 86 Z" fill="{C}"/><path d="M320 86 Q280 260 290 450 L252 450 Q242 260 256 86 Z" fill="{C}"/><rect x="30" y="76" width="300" height="20" rx="4" fill="{N}"/><rect x="62" y="436" width="236" height="14" fill="{N}"/></g>')
    if chand:
        o.append(f'<g class="deco"><line x1="640" x2="640" y1="40" y2="96" stroke="{N}" stroke-width="3"/><path d="M560 120 Q640 160 720 120" fill="none" stroke="{N}" stroke-width="4"/><circle cx="640" cy="104" r="10" fill="{N}"/>'
                 + ''.join(f'<rect x="{x - 4}" y="{y - 22}" width="8" height="22" fill="#fff" stroke="{N}" stroke-width="2"/><path id="fl{k}" d="M{x} {y - 40} q7 10 0 16 q-7 -6 0 -16 z" fill="{C}"/>' for k, (x, y) in enumerate(((560, 120), (600, 136), (640, 142), (680, 136), (720, 120)))) + '</g>')
    o.append(f'<rect y="470" width="1280" height="130" fill="#fff"/><rect y="466" width="1280" height="6" fill="{N}"/><g class="deco">' + ''.join(f'<rect x="{20 + k * 160}" y="490" width="130" height="92" fill="none" stroke="{N}" stroke-width="2" stroke-opacity=".55"/>' for k in range(8)) + '</g>')
    return ''.join(o)
def floor(): return f'<rect y="600" width="1280" height="120" fill="#fff"/>' + ''.join(f'<rect x="{c * 40}" y="{600 + r * 40}" width="40" height="40" fill="{N}"/>' for r in range(3) for c in range(32) if (r + c) % 2 == 0) + f'<rect y="598" width="1280" height="4" fill="{N}"/>'
def plate(x, y, emblem, year, place, line):   # an oval portrait whose picture gives way to the history card in "How it ended"
    return (f'<g transform="translate({x} {y})"><ellipse rx="72" ry="90" fill="#fff" stroke="{N}" stroke-width="5"/><ellipse rx="62" ry="80" fill="none" stroke="{N}" stroke-width="1.6"/><g id="emb">{emblem}</g>'
            f'<g id="hist" opacity="0"><text y="-14" text-anchor="middle" font-family="Playfair Display,serif" font-weight="900" font-size="{30 if len(year) < 6 else 24}" fill="{N}">{year}</text><text y="16" text-anchor="middle" font-family="Playfair Display,serif" font-style="italic" font-size="18" fill="{C}">{place}</text><text y="42" text-anchor="middle" font-family="Playfair Display,serif" font-style="italic" font-size="13" fill="{N}">{line}</text></g></g>')
def door(): return (f'<g><rect x="1166" y="250" width="110" height="350" fill="{N}"/><rect id="glow" x="1176" y="260" width="90" height="340" fill="#ffd9a8" opacity="0"/>'
                    f'<g id="leaf" transform="translate(1176 0)"><rect x="0" y="260" width="90" height="340" fill="#fff" stroke="{N}" stroke-width="3"/><rect x="12" y="276" width="66" height="130" fill="none" stroke="{N}" stroke-width="2"/><rect x="12" y="424" width="66" height="156" fill="none" stroke="{N}" stroke-width="2"/><circle cx="74" cy="430" r="5" fill="{C}"/></g></g>')
def lone(): return f'<g id="lone" opacity="0"><ellipse cx="0" cy="0" rx="12" ry="9" transform="rotate(-20)" fill="#ffd9a8"/><rect x="9" y="-46" width="4" height="46" fill="#ffd9a8"/></g>'
def dim(): return f'<rect id="dim" width="1280" height="720" fill="{N}" opacity="0" pointer-events="none"/>'
def notes(n=10, col=N): return ''.join(f'<g id="nt{k}" opacity="0"><ellipse cx="0" cy="0" rx="11" ry="8" transform="rotate(-20)" fill="{col}"/><rect x="8" y="-44" width="3.5" height="44" fill="{col}"/></g>' for k in range(n))
def butler(x, s=1.42, y=None): return f'<g id="butler" transform="translate({x} {600 - 207 * s if y is None else y}) scale({s})">{RAB}</g>'
def piece(k, x, s, y=600, gid=None): return f'<g id="{gid or k}" transform="translate({x} {y}) scale({s})">{P[k]}</g>'
def chair(x): return f'<path d="M{x - 40} 600 L{x - 34} 520 L{x + 34} 520 L{x + 40} 600" fill="none" stroke="{N}" stroke-width="4"/><path d="M{x - 30} 520 L{x - 26} 420 Q{x} 404 {x + 26} 420 L{x + 30} 520" fill="#fff" stroke="{N}" stroke-width="4"/><rect x="{x - 46}" y="512" width="92" height="12" rx="4" fill="{N}"/>'
def piano_front(cx=640, gid='piano'):   # the upright, seen from the front, centred on cx
    d = cx - 735
    keys = ''.join(f'<rect x="{606 + k * 18 + d}" y="472" width="18" height="40" fill="#fff" stroke="{N}" stroke-width="1.5"/>' for k in range(14)) + ''.join(f'<rect x="{606 + k * 18 + 12 + d}" y="472" width="11" height="24" fill="{N}"/>' for k in range(13) if k % 7 not in (2, 6))
    return (f'<g id="{gid}"><rect x="{590 + d}" y="300" width="290" height="176" rx="6" fill="{N}"/><rect x="{580 + d}" y="290" width="310" height="16" rx="4" fill="{N}"/><rect x="{616 + d}" y="320" width="238" height="120" rx="4" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2"/>'
            f'<path d="M{640 + d} 360 q40 -30 80 0 q40 30 80 0" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2"/>{keys}<rect x="{596 + d}" y="512" width="278" height="20" fill="{N}"/><rect x="{606 + d}" y="532" width="16" height="68" fill="{N}"/><rect x="{848 + d}" y="532" width="16" height="68" fill="{N}"/>'
            + ''.join(f'<rect x="{x + d - 3}" y="262" width="6" height="28" fill="#fff" stroke="{N}" stroke-width="2"/><rect x="{x + d - 10}" y="286" width="20" height="5" fill="{N}"/><path id="pf{k}" d="M{x + d} 246 q6 9 0 14 q-6 -5 0 -14 z" fill="{C}"/>' for k, x in enumerate((612, 858))) + '</g>')
def stool(cx=640, gid='stool'): d = cx - 735; return f'<g id="{gid}"><rect x="{680 + d}" y="552" width="110" height="14" rx="4" fill="{N}"/><rect x="{690 + d}" y="566" width="10" height="34" fill="{N}"/><rect x="{770 + d}" y="566" width="10" height="34" fill="{N}"/></g>'
def clara_sit(cx=640, gid='clara'):   # from behind, seated on the stool at the front piano
    d = cx - 735; P_ = lambda s: re.sub(r'(-?\d+(?:\.\d+)?) (-?\d+(?:\.\d+)?)', lambda m: f'{float(m.group(1)) + d:g} {m.group(2)}', s)
    paths = ['M714 466 Q684 478 676 500 Q678 510 690 508 Q698 490 720 482 Z', 'M756 466 Q786 478 794 500 Q792 510 780 508 Q772 490 750 482 Z', 'M708 462 Q735 452 762 462 L782 552 Q735 562 688 552 Z', 'M714 418 Q716 392 735 390 Q754 392 756 418 Q760 440 754 462 Q735 470 716 462 Q710 440 714 418 Z']
    halo = '<g fill="none" stroke="#fff" stroke-width="10" stroke-linejoin="round">' + ''.join(f'<path d="{P_(p)}"/>' for p in paths) + '</g>'
    body = (f'<path d="{P_(paths[0])}" fill="#fffdf7" stroke="{N}" stroke-width="4" stroke-linejoin="round"/><path d="{P_(paths[1])}" fill="#fffdf7" stroke="{N}" stroke-width="4" stroke-linejoin="round"/>'
            f'<path d="{P_(paths[2])}" fill="url(#hcl)" stroke="{N}" stroke-width="4.5" stroke-linejoin="round"/><path d="{P_(paths[3])}" fill="{N}"/>'
            f'<path d="M{722 + d} 398 l-12 -8 l2 16 z M{748 + d} 398 l12 -8 l-2 16 z" fill="{PK}" stroke="{N}" stroke-width="2" stroke-linejoin="round"/><circle cx="{735 + d}" cy="398" r="5" fill="{PK}" stroke="{N}" stroke-width="2"/>')
    return f'<g id="{gid}">{halo}{body}</g>'
def clara_stand(x=592, gid='clara', arm='down'):   # standing, from behind; x is the centre; arm: 'down', 'up' (towards the left), 'both'
    d = x - 592
    legs = f'<rect x="{572 + d}" y="520" width="14" height="70" rx="6" fill="#fffdf7" stroke="{N}" stroke-width="4"/><rect x="{598 + d}" y="520" width="14" height="70" rx="6" fill="#fffdf7" stroke="{N}" stroke-width="4"/><ellipse cx="{576 + d}" cy="594" rx="14" ry="7" fill="{N}"/><ellipse cx="{608 + d}" cy="594" rx="14" ry="7" fill="{N}"/>'
    down = lambda sx: f'<path d="M{566 + d if sx < 0 else 618 + d} 436 Q{548 + d if sx < 0 else 636 + d} 470 {552 + d if sx < 0 else 632 + d} 500 Q{558 + d if sx < 0 else 626 + d} 506 {564 + d if sx < 0 else 620 + d} 500 Q{566 + d if sx < 0 else 618 + d} 472 {578 + d if sx < 0 else 606 + d} 444 Z" fill="#fffdf7" stroke="{N}" stroke-width="4" stroke-linejoin="round"/>'
    up = f'<path d="M{566 + d} 436 Q{536 + d} 420 {512 + d} 394 Q{506 + d} 386 {514 + d} 382 Q{540 + d} 404 {574 + d} 420 Z" fill="#fffdf7" stroke="{N}" stroke-width="4" stroke-linejoin="round"/>'
    upR = f'<path d="M{618 + d} 436 Q{648 + d} 420 {672 + d} 394 Q{678 + d} 386 {670 + d} 382 Q{644 + d} 404 {610 + d} 420 Z" fill="#fffdf7" stroke="{N}" stroke-width="4" stroke-linejoin="round"/>'
    arms = (up + down(1)) if arm == 'up' else (up + upR) if arm == 'both' else (down(-1) + down(1))
    dress = f'<path d="M{566 + d} 426 Q{592 + d} 416 {618 + d} 426 L{640 + d} 530 Q{592 + d} 542 {544 + d} 530 Z" fill="url(#hcl)" stroke="{N}" stroke-width="4.5" stroke-linejoin="round"/>'
    head = (f'<g id="{gid}h"><path d="M{572 + d} 384 Q{574 + d} 358 {592 + d} 356 Q{610 + d} 358 {612 + d} 384 Q{616 + d} 404 {610 + d} 424 Q{592 + d} 432 {574 + d} 424 Q{568 + d} 404 {572 + d} 384 Z" fill="{N}" stroke="#fff" stroke-width="6" paint-order="stroke"/>'
            f'<path d="M{580 + d} 364 l-12 -8 l2 16 z M{604 + d} 364 l12 -8 l-2 16 z" fill="{PK}" stroke="{N}" stroke-width="2" stroke-linejoin="round"/><circle cx="{592 + d}" cy="364" r="5" fill="{PK}" stroke="{N}" stroke-width="2"/></g>')
    return f'<g id="{gid}">{legs}{dress}{arms}{head}</g>'
def clock(x, y0=150, gid='clock'):   # a long-case clock: face at the top, a pendulum in the window
    return (f'<g id="{gid}"><rect x="{x - 48}" y="{y0}" width="96" height="{600 - y0}" rx="6" fill="#fff" stroke="{N}" stroke-width="4"/><path d="M{x - 56} {y0} L{x} {y0 - 30} L{x + 56} {y0} Z" fill="{N}"/>'
            f'<circle cx="{x}" cy="{y0 + 54}" r="38" fill="#fff" stroke="{N}" stroke-width="4"/>' + ''.join(f'<circle cx="{x + 30 * math.sin(a * math.pi / 6):.1f}" cy="{y0 + 54 - 30 * math.cos(a * math.pi / 6):.1f}" r="2.6" fill="{N}"/>' for a in range(12))
            + f'<line id="{gid}hh" x1="{x}" y1="{y0 + 54}" x2="{x}" y2="{y0 + 34}" stroke="{N}" stroke-width="4" stroke-linecap="round"/><line id="{gid}mh" x1="{x}" y1="{y0 + 54}" x2="{x + 24}" y2="{y0 + 54}" stroke="{N}" stroke-width="3" stroke-linecap="round"/><circle cx="{x}" cy="{y0 + 54}" r="4" fill="{C}"/>'
            f'<rect x="{x - 30}" y="{y0 + 110}" width="60" height="{600 - y0 - 160}" rx="4" fill="{T}" stroke="{N}" stroke-width="2"/><g id="{gid}pd"><line x1="{x}" y1="{y0 + 112}" x2="{x}" y2="{y0 + 112 + (600 - y0 - 230)}" stroke="{N}" stroke-width="3"/><circle cx="{x}" cy="{y0 + 112 + (600 - y0 - 230)}" r="14" fill="{C}"/></g></g>')
def bigtext(x, y, s, size=200, gid=None, font='NM', fill=None, extra=''): return f'<text {f"id={chr(34)}{gid}{chr(34)} " if gid else ""}x="{x}" y="{y}" text-anchor="middle" font-family="{font}" font-size="{size}" fill="{fill or N}" {extra}>{s}</text>'
PRELUDE = r'''
const ph = (t, a, b) => Math.max(0, Math.min(1, (t - a) / (b - a)));
const S = id => document.getElementById(id);
const L0 = TL.lines, F = (re, from) => L0.find(l => l.text && re.test(l.text) && (from === undefined || l.t0 >= from)), PI = L0.filter(l => l.who === 'piano');
const K = { intro: L0[0].t0, tryA: (F(/^Now, at the piano/) || {}).t0 || 1e9, end: (F(/^And here is how it ended/) || {}).t0 || 1e9, tease: F(/^Behind the next door/).t0, dur: TL.dur };
K.endBody = (L0.find(l => l.t0 > K.end && l.who === 'N') || {}).t0 || K.end; K.door = (L0.find(l => l.t0 > K.tease + .1 && l.who === 'N') || {}).t0 || K.tease;
K.quote = (L0.find(l => l.who !== 'N' && l.text && l.t0 < K.tryA && !/^Now, at the piano/.test(l.text)) || {}).t0 || 1e9; K.cue = PI.length ? PI[0].t0 : 1e9; K.lone = PI.length ? PI[PI.length - 1].t0 : K.dur;
const opener = t => t >= K.intro && t < K.tryA, ending = t => t >= K.end && t < K.tease;
function common(t) {
  for (let k = 0; k < 5; k++) { const f = S('fl' + k); if (f) { f.style.transformBox = 'fill-box'; f.style.transformOrigin = 'center bottom'; f.setAttribute('transform', `scale(1 ${1 + .1 * Math.sin(t * 6 + k * 1.7)})`); } }
  for (let k = 0; k < 2; k++) { const f = S('pf' + k); if (f) { f.style.transformBox = 'fill-box'; f.style.transformOrigin = 'center bottom'; f.setAttribute('transform', `scale(1 ${1 + .12 * Math.sin(t * 8 + k)})`); } }
  const hs = S('hist'), em = S('emb'); if (hs) { const h = t >= K.endBody && t < K.tease ? ph(t, K.endBody, K.endBody + 1.1) : 0; hs.setAttribute('opacity', h); em.setAttribute('opacity', 1 - h); }
  S('dim').setAttribute('opacity', t >= K.tease ? .5 * ph(t, K.tease, K.tease + 1.7) : 0);
  const op = t >= K.tease ? ph(t, K.door, K.door + 3.5) : 0; const lf = S('leaf'); if (lf) { lf.setAttribute('transform', `translate(1176 0) scale(${1 - .72 * op} 1)`); S('glow').setAttribute('opacity', op * .95); }
  const lo = S('lone'); if (lo) { const q = ph(t, K.lone - 1.5, K.dur); lo.setAttribute('opacity', t >= K.lone - 1.5 && t >= K.tease ? Math.sin(Math.PI * q) : 0); lo.setAttribute('transform', `translate(${1221 - 300 * q} ${430 - 120 * q + 18 * Math.sin(q * 9)})`); }
  const sub = document.getElementById('sub'); if (sub) { const l = L0.find(l => l.text && t >= l.t0 && t < l.t1 + .25); sub.textContent = l ? l.text.replace(/[⟨⟩]/g, '') : ''; sub.style.opacity = l ? 1 : 0; }
  const ttl = document.getElementById('ttl'); if (ttl) ttl.style.opacity = t < K.intro - .4 ? 1 : Math.max(0, 1 - (t - K.intro + .4) / .6);
}
function notesFX(t, n, x0, w, y0, rise, rate, dark) { for (let k = 0; k < 10; k++) { const g = S('nt' + k); if (!g) continue; if (k >= n) { g.setAttribute('opacity', 0); continue; }
  const p = (t * rate + k / n) % 1; g.setAttribute('transform', `translate(${x0 + (k * 53) % w + 14 * Math.sin(t * 2 + k)} ${y0 - p * rise}) rotate(${10 * Math.sin(t * 3 + k)})`); g.setAttribute('opacity', (1 - p) * (dark || 1)); } }
'''
def film(svg, js, room, title, sub):
    f = open('/tmp/claude-0/anim/film.html').read()
    i = f.index('<svg id="scene"'); j = f.index('</svg>', i) + 6; f = f[:i] + svg + f[j:]
    f = re.sub(r'<small>.*?</small><b>.*?</b><i>.*?</i>', f'<small>The Piano Butler · Beginner · Room {room}</small><b>{title}</b><i>{sub}</i>', f, count=1)
    i = f.index('<script>') + 8; j = f.index('</script>', i); return f[:i] + js + f[j:]
def scene(parts): return '<svg id="scene" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">' + ''.join(parts) + '</svg>'
