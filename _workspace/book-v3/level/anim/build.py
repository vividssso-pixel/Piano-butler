# her 14 Nov ("응", "영상", "둘 다 보여줘"): Beginner Room 8 as an illustrated, moving scene. One drawing serves the book page
# (a still at a chosen moment), the screen version (moves with the audio) and the video (filmed frame by frame).
import json, math, sys
sys.path.insert(0, '/tmp/claude-0/anim'); from kit import sign
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
o.append(f'<rect width="1280" height="600" fill="#f9e8e4"/>')
o.append('<g class="deco">' + ''.join(f'<path d="M{x} {y - 5} l5 5 -5 5 -5 -5 z" fill="#efcfc6"/>' for y in range(60, 470, 36) for x in range(18 + (y // 36 % 2) * 22, 1280, 44)) + '</g>')
o.append(f'<rect width="1280" height="16" fill="{N}"/><rect y="16" width="1280" height="2" fill="#fff"/>' + ''.join(f'<rect x="{6 + k * 16}" y="24" width="8" height="8" fill="{N}"/>' for k in range(80)) + f'<rect y="38" width="1280" height="2" fill="{N}"/>')
# window with night sky and curtains
o.append(f'<g id="win" class="deco" transform="translate(48 118) scale(.7)"><rect x="70" y="110" width="220" height="320" fill="{N}"/><circle cx="220" cy="180" r="26" fill="#fff"/><circle cx="232" cy="172" r="24" fill="{N}"/>'
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
o.append(chair(340) + chair(450))
o.append(f'<g id="queen" transform="translate(340 514) scale(2.1)">{P["VIC_QUEEN"]}</g><g id="king" transform="translate(450 514) scale(1.95)">{P["VIC_KING"]}</g>')
# the piano
keys = ''.join(f'<rect x="{606 + k * 18}" y="472" width="18" height="40" fill="#fff" stroke="{N}" stroke-width="1.5"/>' for k in range(14)) + ''.join(f'<rect x="{606 + k * 18 + 12}" y="472" width="11" height="24" fill="{N}"/>' for k in range(13) if k % 7 not in (2, 6))
o.append('<g transform="translate(-95 0)">')
o.append(f'<g id="piano"><rect x="590" y="300" width="290" height="176" rx="6" fill="{N}"/><rect x="580" y="290" width="310" height="16" rx="4" fill="{N}"/><rect x="616" y="320" width="238" height="120" rx="4" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2"/>'
         + f'<path d="M640 360 q40 -30 80 0 q40 30 80 0" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="2"/>{keys}<rect x="596" y="512" width="278" height="20" fill="{N}"/><rect x="606" y="532" width="16" height="68" fill="{N}"/><rect x="848" y="532" width="16" height="68" fill="{N}"/>'
         + ''.join(f'<rect x="{x - 3}" y="262" width="6" height="28" fill="#fff" stroke="{N}" stroke-width="2"/><rect x="{x - 10}" y="286" width="20" height="5" fill="{N}"/><path id="pf{k}" d="M{x} 246 q6 9 0 14 q-6 -5 0 -14 z" fill="{C}"/>' for k, x in enumerate((612, 858))) + '</g>')
# the stool
o.append(f'<rect x="680" y="552" width="110" height="14" rx="4" fill="{N}"/><rect x="690" y="566" width="10" height="34" fill="{N}"/><rect x="770" y="566" width="10" height="34" fill="{N}"/>')
# Clara from behind, in the app's pen style (her 14 Nov: "뒷모습으로 보여줘도 될 것 같아")
o.append(f'<defs><pattern id="hcl" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="7" height="7" fill="#fffdf7"/><line x1="0" y1="0" x2="0" y2="7" stroke="{N}" stroke-width="2.2"/></pattern></defs>'
         + '<g id="clara">'
         + '<g fill="none" stroke="#fff" stroke-width="10" stroke-linejoin="round">' + '<path d="M714 466 Q684 478 676 500 Q678 510 690 508 Q698 490 720 482 Z"/><path d="M756 466 Q786 478 794 500 Q792 510 780 508 Q772 490 750 482 Z"/><path d="M708 462 Q735 452 762 462 L782 552 Q735 562 688 552 Z"/><path d="M714 418 Q716 392 735 390 Q754 392 756 418 Q760 440 754 462 Q735 470 716 462 Q710 440 714 418 Z"/>' + '</g>'
         + f'<path d="M714 466 Q684 478 676 500 Q678 510 690 508 Q698 490 720 482 Z" fill="#fffdf7" stroke="{N}" stroke-width="4" stroke-linejoin="round"/>'
         + f'<path d="M756 466 Q786 478 794 500 Q792 510 780 508 Q772 490 750 482 Z" fill="#fffdf7" stroke="{N}" stroke-width="4" stroke-linejoin="round"/>'
         + f'<path d="M708 462 Q735 452 762 462 L782 552 Q735 562 688 552 Z" fill="url(#hcl)" stroke="{N}" stroke-width="4.5" stroke-linejoin="round"/>'
         + f'<path d="M714 418 Q716 392 735 390 Q754 392 756 418 Q760 440 754 462 Q735 470 716 462 Q710 440 714 418 Z" fill="{N}"/>'
         + f'<path d="M726 404 q9 -8 18 0" fill="none" stroke="#fff" stroke-width="2" stroke-opacity=".5" stroke-linecap="round"/>'
         + f'<path d="M722 398 l-12 -8 l2 16 z M748 398 l12 -8 l-2 16 z" fill="{PK}" stroke="{N}" stroke-width="2" stroke-linejoin="round"/><circle cx="735" cy="398" r="5" fill="{PK}" stroke="{N}" stroke-width="2"/>'
         + '</g>')
o.append('</g>')
# the Butler with the tea tray
o.append(f'<g id="butler" transform="translate(905 265) scale(1.62)">{RAB}</g>')
o.append(f'<g id="tray" transform="translate(-100 0)"><rect x="906" y="600" width="0" height="0"/><rect x="902" y="488" width="104" height="10" rx="3" fill="{N}"/><rect x="912" y="498" width="8" height="102" fill="{N}"/><rect x="988" y="498" width="8" height="102" fill="{N}"/><rect x="996" y="9999" width="120" height="8" rx="3" fill="{N}"/>' + ''.join(f'<g class="cup" id="cup{k}"><path d="M{912 + k * 32} 466 h24 v12 a12 12 0 0 1 -24 0 Z" fill="#fff" stroke="{N}" stroke-width="2.5"/><path d="M{936 + k * 32} 470 a5 5 0 0 1 0 10" fill="none" stroke="{N}" stroke-width="2.5"/><rect x="{908 + k * 32}" y="484" width="32" height="4" rx="2" fill="{N}"/></g>' for k in range(3)) + '</g>')
# sound: the dynamic sign and the notes
o.append(f'<text id="dyn" x="866" y="226" text-anchor="middle" font-family="Playfair Display,serif" font-style="italic" font-weight="900" font-size="120" fill="{C}" opacity="0">f</text><text id="dynw" x="866" y="262" text-anchor="middle" font-family="Atkinson Hyperlegible,sans-serif" font-weight="700" font-size="22" letter-spacing="3" fill="{C}" opacity="0"></text>')
o.append(''.join(f'<g id="nt{k}" opacity="0"><ellipse cx="0" cy="0" rx="11" ry="8" transform="rotate(-20)" fill="{N}"/><rect x="8" y="-44" width="3.5" height="44" fill="{N}"/></g>' for k in range(10)))
o.append(sign('E'))
o.append(f'<rect id="warm" width="1280" height="720" fill="#ffcf9e" opacity="0" pointer-events="none"/>')
o.append(f'<rect id="dim" width="1280" height="720" fill="{N}" opacity="0" pointer-events="none"/>')
# the door at the right, and its light
o.append(f'<g><rect x="1166" y="250" width="110" height="350" fill="{N}"/><rect id="glow" x="1176" y="260" width="90" height="340" fill="#ffd9a8" opacity="0"/>'
         + f'<g id="leaf" transform="translate(1176 0)"><rect x="0" y="260" width="90" height="340" fill="#fff" stroke="{N}" stroke-width="3"/><rect x="12" y="276" width="66" height="130" fill="none" stroke="{N}" stroke-width="2"/><rect x="12" y="424" width="66" height="156" fill="none" stroke="{N}" stroke-width="2"/><circle cx="74" cy="430" r="5" fill="{C}"/></g></g>')
# a single note that floats out of the door at the very end
o.append(f'<g id="lone" opacity="0"><ellipse cx="0" cy="0" rx="12" ry="9" transform="rotate(-20)" fill="#ffd9a8"/><rect x="9" y="-46" width="4" height="46" fill="#ffd9a8"/></g>')
from kit import NOTECARD, NOTEJS, WALLCOL, sign
SVG = '<svg id="scene" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">' + ''.join(o) + NOTECARD + '</svg>'
FILMSVG = SVG.replace('viewBox="0 0 1280 720"', 'viewBox="0 46 1280 610"', 1)
open('/tmp/claude-0/anim/scene.svg', 'w').write(SVG)
JS = NOTEJS + r'''
const TL = __TL__;
const ph = (t, a, b) => Math.max(0, Math.min(1, (t - a) / (b - a)));
const S = id => document.getElementById(id);
const CR = { clara: [560, 254.6, 2.2], queen: [340, 514, 2.1], king: [450, 514, 1.95] };
const L0 = TL.lines, F = (re) => L0.find(l => l.text && re.test(l.text)), PI = L0.filter(l => l.who === 'piano');
const K = { intro: L0[0].t0, rattle: F(/cups ring/).t0, ask: F(/Now the same piece/).t0, ch1: PI[0].t0, ch2: PI[0].t0 + 2.9, melody: PI[1].t0, 
  end: F(/^A true story from music history/).t0, again: F(/^So Clara plays it again/).t0, cristo: F(/Cristofori/).t0, tease: F(/^The Butler’s note/).t0, door: 1e9, lone: PI[PI.length - 1].t0, dur: TL.dur };
function setT(t) {
  K.tryA = K.end; const L = TL.lines, at = (i) => L[i].t0;
  const loud = t >= K.intro && t < K.ch2, soft = (t >= K.ch2 && t < K.tryA) || (t >= K.again && t < K.tease), tease = t >= K.tease;
  const hard = t >= K.rattle && t < K.ch2 ? 1 : loud ? .6 : 0, asking = t >= K.ask && t < K.ch1;
  // flames: flicker, faster when loud
  for (let k = 0; k < 5; k++) { const f = S('fl' + k); if (f) f.setAttribute('transform', `translate(0 0) scale(1 ${1 + .1 * Math.sin(t * (loud ? 14 : 6) + k * 1.7)})`); f.style.transformOrigin = 'center bottom'; f.style.transformBox = 'fill-box'; }
  for (let k = 0; k < 2; k++) { const f = S('pf' + k); f.style.transformOrigin = 'center bottom'; f.style.transformBox = 'fill-box'; f.setAttribute('transform', `scale(1 ${1 + .12 * Math.sin(t * 8 + k)})`); }
  // the cups rattle on their saucers, the tray shakes
  for (let k = 0; k < 3; k++) { const c = S('cup' + k); c.style.transformBox = 'fill-box'; c.style.transformOrigin = 'center bottom';
    c.setAttribute('transform', hard ? `rotate(${2.5 * Math.sin(t * 30 + k * 2)})` : ''); }
  // the piano trembles, Clara bobs with each loud note
  
  const bob = loud ? 2.5 * Math.abs(Math.sin(t * 5.2)) : soft ? .8 * Math.abs(Math.sin(t * 2)) : 0;
  S('clara').setAttribute('transform', `translate(0 ${-bob})`);
  // the audience: the Queen leans away, the King covers... his patience
  const lean = loud ? 0 : (t >= K.again + 2 && t < K.tease) ? 8 + 1.2 * Math.sin(t * 1.3) : soft ? 3 : 0;
  S('queen').setAttribute('transform', `translate(${CR.queen[0]} ${CR.queen[1] - (hard ? 6 : 0)}) rotate(${lean}) scale(${CR.queen[2] * (hard ? 1.04 : 1)})`);
  S('king').setAttribute('transform', `translate(${CR.king[0]} ${CR.king[1] - (hard ? 4 * Math.abs(Math.sin(t * 5.2)) : 0)}) rotate(${lean * .8}) scale(${CR.king[2]})`);
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
    const p = (t * rate + k / n) % 1, x = 515 + (k * 53) % 250 + 16 * Math.sin(t * 2 + k), y = 290 - p * (loud ? 220 : 150);
    g.setAttribute('transform', `translate(${x} ${y}) rotate(${loud ? 25 * Math.sin(t * 6 + k) : 8 * Math.sin(t + k)})`); g.setAttribute('opacity', (1 - p) * (loud ? 1 : .7)); }
  S('warm').setAttribute('opacity', (t >= K.again && t < K.tease) ? .16 * Math.min(1, ph(t, K.again, K.again + 2)) : (t >= K.ch2 && t < K.tryA) ? .1 : 0);
  // the portrait becomes Cristofori's plate while his story is told
  const cr = t >= K.cristo && t < K.tease ? Math.min(1, ph(t, K.cristo, K.cristo + 1.1)) : 0;
  S('cristo').setAttribute('opacity', cr); S('clefp').setAttribute('opacity', 1 - cr);
  // behind the next door: the room dims, the door opens, a light, one note floats out
  S('dim').setAttribute('opacity', tease ? .55 * ph(t, K.tease, K.tease + .6) : 0); noteCard(t);
  const op = tease ? ph(t, K.door, K.door + 3.5) : 0;
  S('leaf').setAttribute('transform', `translate(1176 0) scale(${1 - .72 * op} 1)`); S('glow').setAttribute('opacity', op * .95);
  const lo = S('lone'), q = ph(t, K.lone - 1.5, K.dur);
  lo.setAttribute('opacity', t >= K.lone - 1.5 ? Math.sin(Math.PI * q) : 0); lo.setAttribute('transform', `translate(${1221 - 300 * q} ${430 - 120 * q + 18 * Math.sin(q * 9)})`);
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
html,body{{margin:0;width:1280px;height:720px;overflow:hidden;background:#fff}} #scene{{width:1280px;height:610px;display:block}}
#sub{{position:absolute;left:0;right:0;top:610px;height:110px;box-sizing:border-box;display:flex;align-items:center;justify-content:center;padding:6px 60px;background:#fff;border-top:3px solid {N};font:500 24px/1.32 'Atkinson Hyperlegible',sans-serif;color:{N};text-align:center;transition:none}}
#ttl{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(255,255,255,.9);color:{N}}}
#ttl small{{font:700 18px 'Atkinson Hyperlegible',sans-serif;letter-spacing:.24em;text-transform:uppercase;color:{C}}} #ttl b{{font:900 72px 'Playfair Display',serif;margin-top:8px}} #ttl i{{font:italic 500 26px 'Playfair Display',serif;margin-top:10px;color:#6d6f9c}}
</style></head><body>{SVG.replace('viewBox="0 0 1280 720"', 'viewBox="0 46 1280 610"', 1)}<div id="ttl"><small>The Piano Butler · Beginner · Room 8</small><b>Loud and soft</b><i>The music evening</i></div><div id="sub"></div>
<script>{JS}</script></body></html>'''
open('/tmp/claude-0/anim/film.html', 'w').write(film)
print('ok', len(SVG))
