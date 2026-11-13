# her 14 Nov ("응", "영상", "둘 다 보여줘"): Beginner Room 8 as an illustrated, moving scene. One drawing serves the book page
# (a still at a chosen moment), the screen version (moves with the audio) and the video (filmed frame by frame).
import json, math
N, C, PK, T = '#26296b', '#e4572e', '#f4a9bb', '#f6f6fb'
P = json.load(open('/tmp/claude-0/lvl/pieces.json')); ART = json.load(open('/tmp/claude-0/lvl/pb-art.json'))
TL = json.load(open('/tmp/claude-0/anim/e1.json'))
def inner(svg): return svg[svg.index('>') + 1:svg.rindex('</svg>')]
RAB = inner(ART['rabbit'])
import re
SIT = json.load(open('/tmp/claude-0/pk/posture_svgs.json'))['1:Just right']
SIT = re.sub(r'<text[^>]*>key level</text>', '', SIT); SIT = re.sub(r'<line[^>]*stroke-dasharray="4 4"[^>]*>(</line>)?', '', SIT)
SIT = inner(SIT)
o = []
# wall and its paper: small diamonds in a lattice
o.append(f'<rect width="1280" height="600" fill="{T}"/>')
o.append('<g class="deco">' + ''.join(f'<path d="M{x} {y - 5} l5 5 -5 5 -5 -5 z" fill="#e2e2ef"/>' for y in range(60, 470, 36) for x in range(18 + (y // 36 % 2) * 22, 1280, 44)) + '</g>')
o.append(f'<rect width="1280" height="16" fill="{N}"/><rect y="16" width="1280" height="2" fill="#fff"/>' + ''.join(f'<rect x="{6 + k * 16}" y="24" width="8" height="8" fill="{N}"/>' for k in range(80)) + f'<rect y="38" width="1280" height="2" fill="{N}"/>')
# window with night sky and curtains
o.append(f'<g id="win" class="deco"><rect x="70" y="110" width="220" height="320" fill="{N}"/><circle cx="220" cy="180" r="26" fill="#fff"/><circle cx="232" cy="172" r="24" fill="{N}"/>'
         + ''.join(f'<circle cx="{x}" cy="{y}" r="2.2" fill="#fff" class="star"/>' for x, y in ((110, 150), (150, 230), (250, 260), (120, 330), (200, 300), (260, 380), (95, 400)))
         + f'<rect x="70" y="110" width="220" height="320" fill="none" stroke="#fff" stroke-width="10"/><line x1="180" x2="180" y1="110" y2="430" stroke="#fff" stroke-width="7"/><line x1="70" x2="290" y1="270" y2="270" stroke="#fff" stroke-width="7"/>'
         + f'<rect x="70" y="110" width="220" height="320" fill="none" stroke="{N}" stroke-width="3"/>'
         + f'<path d="M40 86 Q80 260 70 450 L108 450 Q118 260 104 86 Z" fill="{C}"/><path d="M320 86 Q280 260 290 450 L252 450 Q242 260 256 86 Z" fill="{C}"/>'
         + f'<rect x="30" y="76" width="300" height="20" rx="4" fill="{N}"/><rect x="62" y="436" width="236" height="14" fill="{N}"/></g>')
# portrait on the wall: a G clef in an oval frame; in the ending it becomes Cristofori's plate
o.append(f'<g transform="translate(1010 200)"><ellipse rx="70" ry="88" fill="#fff" stroke="{N}" stroke-width="5"/><ellipse rx="60" ry="78" fill="none" stroke="{N}" stroke-width="1.6"/>'
         + f'<g id="clefp"><text x="-2" y="44" text-anchor="middle" font-family="NM" font-size="132" fill="{N}">𝄞</text></g>'
         + f'<g id="cristo" opacity="0"><text y="-12" text-anchor="middle" font-family="Playfair Display,serif" font-weight="900" font-size="34" fill="{N}">c. 1700</text><text y="20" text-anchor="middle" font-family="Playfair Display,serif" font-style="italic" font-size="19" fill="{C}">Florence</text><text y="46" text-anchor="middle" font-family="Playfair Display,serif" font-style="italic" font-size="14" fill="{N}">piano e forte</text></g></g>')
# chandelier
o.append(f'<g class="deco"><line x1="640" x2="640" y1="40" y2="96" stroke="{N}" stroke-width="3"/><path d="M560 120 Q640 160 720 120" fill="none" stroke="{N}" stroke-width="4"/><circle cx="640" cy="104" r="10" fill="{N}"/>'
         + ''.join(f'<rect x="{x - 4}" y="{y - 22}" width="8" height="22" fill="#fff" stroke="{N}" stroke-width="2"/><path id="fl{k}" d="M{x} {y - 40} q7 10 0 16 q-7 -6 0 -16 z" fill="{C}"/>' for k, (x, y) in enumerate(((560, 120), (600, 136), (640, 142), (680, 136), (720, 120)))) + '</g>')
# wainscot and dado
o.append(f'<rect y="470" width="1280" height="130" fill="#fff"/><rect y="466" width="1280" height="6" fill="{N}"/>' + '<g class="deco">' + ''.join(f'<rect x="{20 + k * 160}" y="490" width="130" height="92" fill="none" stroke="{N}" stroke-width="2" stroke-opacity=".55"/>' for k in range(8)) + '</g>')
# floor
o.append(f'<rect y="600" width="1280" height="120" fill="#fff"/>' + ''.join(f'<rect x="{c * 40}" y="{600 + r * 40}" width="40" height="40" fill="{N}"/>' for r in range(3) for c in range(32) if (r + c) % 2 == 0) + f'<rect y="598" width="1280" height="4" fill="{N}"/>')
# audience: the Queen and the King on chairs
def chair(x): return f'<path d="M{x - 40} 600 L{x - 34} 520 L{x + 34} 520 L{x + 40} 600" fill="none" stroke="{N}" stroke-width="4"/><path d="M{x - 30} 520 L{x - 26} 420 Q{x} 404 {x + 26} 420 L{x + 30} 520" fill="#fff" stroke="{N}" stroke-width="4"/><rect x="{x - 46}" y="512" width="92" height="12" rx="4" fill="{N}"/>'
o.append(chair(390) + chair(500))
o.append(f'<g id="queen" transform="translate(390 514) scale(1.85)">{P["VIC_QUEEN"]}</g><g id="king" transform="translate(500 514) scale(1.75)">{P["VIC_KING"]}</g>')
# Clara at the piano, side view: the app's drawing, scaled so that its floor meets ours
o.append(f'<g id="clara" transform="translate(560 254.6) scale(2.2)">{SIT}</g>')
o.append(''.join(f'<rect x="{x - 3}" y="337" width="6" height="28" fill="#fff" stroke="{N}" stroke-width="2"/><rect x="{x - 10}" y="362" width="20" height="5" fill="{N}"/><path id="pf{k}" d="M{x} 321 q6 9 0 14 q-6 -5 0 -14 z" fill="{C}"/>' for k, x in enumerate((888, 958))))
o.append('<g id="piano"></g>')
# the Butler with the tea tray
o.append(f'<g id="butler" transform="translate(1032 395) scale(1.0)">{RAB}</g>')
o.append(f'<g id="tray"><rect x="996" y="488" width="120" height="8" rx="3" fill="{N}"/>' + ''.join(f'<g class="cup" id="cup{k}"><path d="M{1006 + k * 34} 466 h24 v12 a12 12 0 0 1 -24 0 Z" fill="#fff" stroke="{N}" stroke-width="2.5"/><path d="M{1030 + k * 34} 470 a5 5 0 0 1 0 10" fill="none" stroke="{N}" stroke-width="2.5"/><rect x="{1002 + k * 34}" y="484" width="32" height="4" rx="2" fill="{N}"/></g>' for k in range(3)) + '</g>')
# sound: the dynamic sign and the notes
o.append(f'<text id="dyn" x="840" y="236" text-anchor="middle" font-family="Playfair Display,serif" font-style="italic" font-weight="900" font-size="120" fill="{C}" opacity="0">f</text><text id="dynw" x="840" y="276" text-anchor="middle" font-family="Atkinson Hyperlegible,sans-serif" font-weight="700" font-size="22" letter-spacing="3" fill="{C}" opacity="0"></text>')
o.append(''.join(f'<g id="nt{k}" opacity="0"><ellipse cx="0" cy="0" rx="11" ry="8" transform="rotate(-20)" fill="{N}"/><rect x="8" y="-44" width="3.5" height="44" fill="{N}"/></g>' for k in range(10)))
o.append(f'<rect id="dim" width="1280" height="720" fill="{N}" opacity="0" pointer-events="none"/>')
# the door at the right, and its light
o.append(f'<g><rect x="1196" y="300" width="80" height="300" fill="{N}"/><rect id="glow" x="1204" y="310" width="64" height="290" fill="#ffd9a8" opacity="0"/>'
         + f'<g id="leaf" transform="translate(1204 0)"><rect x="0" y="310" width="64" height="290" fill="#fff" stroke="{N}" stroke-width="3"/><rect x="9" y="324" width="46" height="110" fill="none" stroke="{N}" stroke-width="2"/><rect x="9" y="452" width="46" height="130" fill="none" stroke="{N}" stroke-width="2"/><circle cx="52" cy="452" r="4.5" fill="{C}"/></g></g>')
# a single note that floats out of the door at the very end
o.append(f'<g id="lone" opacity="0"><ellipse cx="0" cy="0" rx="12" ry="9" transform="rotate(-20)" fill="#ffd9a8"/><rect x="9" y="-46" width="4" height="46" fill="#ffd9a8"/></g>')
SVG = '<svg id="scene" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">' + ''.join(o) + '</svg>'
open('/tmp/claude-0/anim/scene.svg', 'w').write(SVG)
JS = r'''
const TL = __TL__;
const ph = (t, a, b) => Math.max(0, Math.min(1, (t - a) / (b - a)));
const S = id => document.getElementById(id);
const CR = { clara: [560, 254.6, 2.2], queen: [390, 514, 1.85], king: [500, 514, 1.75] };
const L0 = TL.lines, F = (re) => L0.find(l => l.text && re.test(l.text)), PI = L0.filter(l => l.who === 'piano');
const K = { intro: L0[0].t0, rattle: F(/cups rattle/).t0, ask: F(/This time/).t0, ch1: PI[0].t0, ch2: PI[0].t0 + 1.45, tryA: F(/^Now, at the piano/).t0,
  end: F(/^And here is how it ended/).t0, again: F(/^So Clara plays it again/).t0, cristo: F(/Cristofori/).t0, tease: F(/^Behind the next door/).t0, door: F(/^After the evening/).t0, lone: PI[PI.length - 1].t0, dur: TL.dur };
function setT(t) {
  const L = TL.lines, at = (i) => L[i].t0;
  const loud = t >= K.intro && t < K.ch2, soft = (t >= K.ch2 && t < K.tryA) || (t >= K.again && t < K.tease), tease = t >= K.tease;
  const hard = t >= K.rattle && t < K.ch2 ? 1 : loud ? .6 : 0, asking = t >= K.ask && t < K.ch1;
  // flames: flicker, faster when loud
  for (let k = 0; k < 5; k++) { const f = S('fl' + k); if (f) f.setAttribute('transform', `translate(0 0) scale(1 ${1 + .1 * Math.sin(t * (loud ? 14 : 6) + k * 1.7)})`); f.style.transformOrigin = 'center bottom'; f.style.transformBox = 'fill-box'; }
  for (let k = 0; k < 2; k++) { const f = S('pf' + k); f.style.transformOrigin = 'center bottom'; f.style.transformBox = 'fill-box'; f.setAttribute('transform', `scale(1 ${1 + .12 * Math.sin(t * 8 + k)})`); }
  // the cups rattle on their saucers, the tray shakes
  for (let k = 0; k < 3; k++) { const c = S('cup' + k); c.style.transformBox = 'fill-box'; c.style.transformOrigin = 'center bottom';
    c.setAttribute('transform', hard ? `rotate(${(6 * hard) * Math.sin(t * 40 + k * 2)}) translate(0 ${-2.5 * hard * Math.abs(Math.sin(t * 33 + k))})` : ''); }
  // the piano trembles, Clara bobs with each loud note
  
  const bob = loud ? 2.5 * Math.abs(Math.sin(t * 5.2)) : soft ? .8 * Math.abs(Math.sin(t * 2)) : 0;
  const [cx, cy, cs] = CR.clara; S('clara').setAttribute('transform', `translate(${cx} ${cy - bob}) scale(${cs})`);
  // the audience: the Queen leans away, the King covers... his patience
  const lean = hard ? -8 * hard : (t >= K.again + 3 && t < K.tease) ? 7 + 1.2 * Math.sin(t * 1.3) : soft ? 2 * Math.sin(t * 1.3) : 0;
  S('queen').setAttribute('transform', `translate(${CR.queen[0]} ${CR.queen[1]}) rotate(${lean}) scale(${CR.queen[2]})`);
  S('king').setAttribute('transform', `translate(${CR.king[0]} ${CR.king[1]}) rotate(${lean * .8}) scale(${CR.king[2]})`);
  // the sign above the piano
  const d = S('dyn');
  if (asking) { d.textContent = 'p?'; d.setAttribute('fill', '#26296b'); d.setAttribute('opacity', Math.min(1, ph(t, K.ask, K.ask + .8))); d.setAttribute('font-size', 96); }
  else if (loud) { d.textContent = 'f'; d.setAttribute('fill', '#e4572e'); d.setAttribute('opacity', Math.min(1, ph(t, 3.4, 4.4))); d.setAttribute('font-size', 110 + 22 * hard * Math.abs(Math.sin(t * 5.2))); }
  else if (soft) { d.textContent = 'p'; d.setAttribute('fill', '#26296b'); d.setAttribute('opacity', .9); d.setAttribute('font-size', 86); }
  else if (asking) { d.textContent = 'p?'; d.setAttribute('fill', '#26296b'); d.setAttribute('opacity', Math.min(1, ph(t, K.ask, K.ask + .8))); d.setAttribute('font-size', 86); }
  else d.setAttribute('opacity', 0);
  const w = S('dynw'); w.textContent = asking ? 'PIANO?' : loud ? 'FORTE · LOUD' : soft ? 'PIANO · SOFT' : ''; w.setAttribute('fill', loud && !asking ? '#e4572e' : '#26296b'); w.setAttribute('opacity', d.getAttribute('opacity'));
  // notes rising from the piano: many and quick when loud, a few and slow when soft
  const n = loud ? 10 : soft ? 4 : 0, rate = loud ? .9 : .22;
  for (let k = 0; k < 10; k++) { const g = S('nt' + k);
    if (k >= n) { g.setAttribute('opacity', 0); continue; }
    const p = (t * rate + k / n) % 1, x = 740 + (k * 37) % 190 + 14 * Math.sin(t * 2 + k), y = 330 - p * (loud ? 230 : 150);
    g.setAttribute('transform', `translate(${x} ${y}) rotate(${loud ? 25 * Math.sin(t * 6 + k) : 8 * Math.sin(t + k)})`); g.setAttribute('opacity', (1 - p) * (loud ? 1 : .7)); }
  // the portrait becomes Cristofori's plate while his story is told
  const cr = t >= K.cristo && t < K.tease ? Math.min(1, ph(t, K.cristo, K.cristo + 1.1)) : 0;
  S('cristo').setAttribute('opacity', cr); S('clefp').setAttribute('opacity', 1 - cr);
  // behind the next door: the room dims, the door opens, a light, one note floats out
  S('dim').setAttribute('opacity', tease ? .5 * ph(t, K.tease, K.tease + 1.7) : 0);
  const op = tease ? ph(t, K.door, K.door + 3.5) : 0;
  S('leaf').setAttribute('transform', `translate(1204 0) scale(${1 - .72 * op} 1)`); S('glow').setAttribute('opacity', op * .95);
  const lo = S('lone'), q = ph(t, K.lone - 1.5, K.dur);
  lo.setAttribute('opacity', t >= K.lone - 1.5 ? Math.sin(Math.PI * q) : 0); lo.setAttribute('transform', `translate(${1236 - 290 * q} ${430 - 120 * q + 18 * Math.sin(q * 9)})`);
  // the line being spoken
  const sub = document.getElementById('sub'); if (sub) { const l = L.find(l => l.text && t >= l.t0 && t < l.t1 + .25); sub.textContent = l ? l.text.replace(/[⟨⟩]/g, '') : ''; sub.style.opacity = l ? 1 : 0; }
  const ttl = document.getElementById('ttl'); if (ttl) ttl.style.opacity = t < K.intro - .4 ? 1 : Math.max(0, 1 - (t - K.intro + .4) / .6);
}
window.setT = setT;
'''.replace('__TL__', json.dumps(TL))
open('/tmp/claude-0/anim/scene.js', 'w').write(JS)
# the film page: 1280 x 720, title card and subtitles
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,500&family=Atkinson+Hyperlegible:wght@400;700&display=swap">'
NM = open('/tmp/claude-0/lvl/levelstory.py').read()
film = f'''<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>
''' + open('/tmp/claude-0/anim/nm.css').read().replace('{','{{').replace('}','}}') + f'''
html,body{{margin:0;width:1280px;height:720px;overflow:hidden;background:#fff}} #scene{{width:1280px;height:720px;display:block}}
#sub{{position:absolute;left:50%;bottom:26px;transform:translateX(-50%);max-width:1040px;background:rgba(255,255,255,.94);border:2px solid {N};border-radius:16px;padding:12px 24px;font:500 27px/1.35 'Atkinson Hyperlegible',sans-serif;color:{N};text-align:center;transition:none}}
#ttl{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(255,255,255,.9);color:{N}}}
#ttl small{{font:700 18px 'Atkinson Hyperlegible',sans-serif;letter-spacing:.24em;text-transform:uppercase;color:{C}}} #ttl b{{font:900 72px 'Playfair Display',serif;margin-top:8px}} #ttl i{{font:italic 500 26px 'Playfair Display',serif;margin-top:10px;color:#6d6f9c}}
</style></head><body>{SVG}<div id="ttl"><small>The Piano Butler · Beginner · Room 8</small><b>Loud and soft</b><i>The music evening</i></div><div id="sub"></div>
<script>{JS}</script></body></html>'''
open('/tmp/claude-0/anim/film.html', 'w').write(film)
print('ok', len(SVG))
