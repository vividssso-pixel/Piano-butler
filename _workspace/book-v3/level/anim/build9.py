# Beginner Room 9, Ear training (her 14 Nov: "다음 이야기도 부탁해"): the door from Room 8. Clara listens at a closed door;
# high notes show at the top of the door, low ones at the bottom; at the end the door opens on the Butler at the practice piano.
import json, math
N, C, PK, T = '#26296b', '#e4572e', '#f4a9bb', '#f6f6fb'
P = json.load(open('/tmp/claude-0/lvl/pieces.json')); ART = json.load(open('/tmp/claude-0/lvl/pb-art.json'))
TL = json.load(open('/tmp/claude-0/anim/e9.json'))
def inner(svg): return svg[svg.index('>') + 1:svg.rindex('</svg>')]
RAB = inner(ART['rabbit'])
o = []
o.append(f'<rect width="1280" height="600" fill="{T}"/>')
o.append('<g class="deco">' + ''.join(f'<path d="M{x} {y - 5} l5 5 -5 5 -5 -5 z" fill="#e2e2ef"/>' for y in range(60, 470, 36) for x in range(18 + (y // 36 % 2) * 22, 1280, 44)) + '</g>')
o.append(f'<rect width="1280" height="16" fill="{N}"/><rect y="16" width="1280" height="2" fill="#fff"/>' + ''.join(f'<rect x="{6 + k * 16}" y="24" width="8" height="8" fill="{N}"/>' for k in range(80)) + f'<rect y="38" width="1280" height="2" fill="{N}"/>')
# a wall lamp on each side of the door
o.append('<g class="deco">' + ''.join(f'<path d="M{x} 250 q0 -30 -20 -40" fill="none" stroke="{N}" stroke-width="4"/><rect x="{x - 32}" y="196" width="24" height="18" rx="4" fill="#fff" stroke="{N}" stroke-width="3"/><path id="lf{k}" d="M{x - 20} 178 q7 10 0 16 q-7 -6 0 -16 z" fill="{C}"/>' for k, x in enumerate((90, 520))) + '</g>')
# portraits of the Queen and the King on the wall, in oval frames
o.append('<g class="deco">' + ''.join(f'<g transform="translate({x} 200)"><ellipse rx="54" ry="68" fill="#fff" stroke="{N}" stroke-width="5"/><ellipse rx="45" ry="59" fill="none" stroke="{N}" stroke-width="1.6"/><g transform="translate(0 46) scale(1.05)">{P[k]}</g></g>' for x, k in ((850, 'VIC_QUEEN'), (980, 'VIC_KING'))) + '</g>')
# wainscot
o.append(f'<rect y="470" width="1280" height="130" fill="#fff"/><rect y="466" width="1280" height="6" fill="{N}"/><g class="deco">' + ''.join(f'<rect x="{20 + k * 160}" y="490" width="130" height="92" fill="none" stroke="{N}" stroke-width="2" stroke-opacity=".55"/>' for k in range(8)) + '</g>')
# the doorway: frame, then the room behind it (clipped to the opening), then the door leaf
o.append('<g transform="translate(-180 0)">')
o.append(f'<rect x="288" y="184" width="214" height="416" fill="{N}"/><path d="M288 184 L395 140 L502 184 Z" fill="{N}"/>')
o.append(f'<clipPath id="cp9"><rect x="300" y="196" width="190" height="404"/></clipPath><g id="inside" clip-path="url(#cp9)"><rect x="300" y="196" width="190" height="404" fill="#ffe2bf"/><rect x="306" y="440" width="96" height="104" rx="4" fill="{N}"/><rect x="314" y="450" width="80" height="46" fill="none" stroke="#fff" stroke-opacity=".5"/>'
         + ''.join(f'<rect x="{308 + k * 13}" y="496" width="13" height="20" fill="#fff" stroke="{N}" stroke-width="1"/>' for k in range(7)) + f'<rect x="306" y="544" width="9" height="56" fill="{N}"/><rect x="393" y="544" width="9" height="56" fill="{N}"/>'
         + f'<g transform="translate(372 400) scale(.95)">{RAB}</g></g>')
o.append(f'<g id="leaf" transform="translate(300 0)"><rect x="0" y="196" width="190" height="404" fill="#fff" stroke="{N}" stroke-width="3"/>'
         + f'<rect x="18" y="214" width="154" height="150" fill="none" stroke="{N}" stroke-width="2"/><rect x="18" y="384" width="154" height="196" fill="none" stroke="{N}" stroke-width="2"/>'
         + f'<circle cx="168" cy="392" r="8" fill="{C}"/><path d="M164 410 h8 l-2 14 h-4 z" fill="{N}"/></g>')
o.append(f'<rect id="crack" x="300" y="594" width="190" height="6" fill="#ffd9a8" opacity=".9"/>')
o.append('</g>')
# floor
o.append(f'<rect y="600" width="1280" height="120" fill="#fff"/>' + ''.join(f'<rect x="{c * 40}" y="{600 + r * 40}" width="40" height="40" fill="{N}"/>' for r in range(3) for c in range(32) if (r + c) % 2 == 0) + f'<rect y="598" width="1280" height="4" fill="{N}"/>')
# Clara, standing, seen from behind, her ear turned to the door
o.append(f'<defs><pattern id="hcl" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="7" height="7" fill="#fffdf7"/><line x1="0" y1="0" x2="0" y2="7" stroke="{N}" stroke-width="2.2"/></pattern></defs>')
legs = f'<rect x="572" y="520" width="14" height="70" rx="6" fill="#fffdf7" stroke="{N}" stroke-width="4"/><rect x="598" y="520" width="14" height="70" rx="6" fill="#fffdf7" stroke="{N}" stroke-width="4"/><ellipse cx="576" cy="594" rx="14" ry="7" fill="{N}"/><ellipse cx="608" cy="594" rx="14" ry="7" fill="{N}"/>'
arm = f'<path d="M566 436 Q536 420 512 394 Q506 386 514 382 Q540 404 574 420 Z" fill="#fffdf7" stroke="{N}" stroke-width="4" stroke-linejoin="round"/><path d="M618 436 Q632 470 630 500 Q624 506 618 500 Q618 472 606 444 Z" fill="#fffdf7" stroke="{N}" stroke-width="4" stroke-linejoin="round"/>'
dress = f'<path d="M566 426 Q592 416 618 426 L640 530 Q592 542 544 530 Z" fill="url(#hcl)" stroke="{N}" stroke-width="4.5" stroke-linejoin="round"/>'
head = (f'<g id="chead"><path d="M572 384 Q574 358 592 356 Q610 358 612 384 Q616 404 610 424 Q592 432 574 424 Q568 404 572 384 Z" fill="{N}" stroke="#fff" stroke-width="6" paint-order="stroke"/>'
        + f'<path d="M580 364 l-12 -8 l2 16 z M604 364 l12 -8 l-2 16 z" fill="{PK}" stroke="{N}" stroke-width="2" stroke-linejoin="round"/><circle cx="592" cy="364" r="5" fill="{PK}" stroke="{N}" stroke-width="2"/></g>')
o.append(f'<g id="clara" transform="translate(-160 0)">{legs}{dress}{arm}{head}</g>')
# what she hears: notes at the top of the door for high, at the bottom for low; two ladders for the same tune
def note(i, col=N): return f'<g id="hn{i}" opacity="0"><ellipse cx="0" cy="0" rx="12" ry="9" transform="rotate(-20)" fill="{col}"/><rect x="9" y="-46" width="4" height="46" fill="{col}"/></g>'
o.append(''.join(note(i) for i in range(6)))
o.append(f'<text id="ans" x="520" y="300" font-family="Playfair Display,serif" font-weight="900" font-size="64" fill="{C}" opacity="0"></text>')
o.append(f'<g id="same" opacity="0">' + ''.join(f'<g transform="translate({x} 0)">' + ''.join(f'<circle cx="{k * 22}" cy="{200 - k * 18}" r="9" fill="{N}"/>' for k in range(3)) + '</g>' for x in (500, 600)) + f'<text x="575" y="196" text-anchor="middle" font-family="Playfair Display,serif" font-weight="900" font-size="48" fill="{C}">=</text></g>')
# the Butler's word in his book
o.append(f'<g id="book" opacity="0" transform="translate(-170 0)"><rect x="700" y="210" width="190" height="96" rx="6" fill="#fff" stroke="{N}" stroke-width="3"/><line x1="795" y1="214" x2="795" y2="302" stroke="{N}" stroke-width="2"/><text x="795" y="272" text-anchor="middle" font-family="Playfair Display,serif" font-style="italic" font-weight="700" font-size="34" fill="{C}">Correct.</text></g>')
o.append(f'<rect id="dim" width="1280" height="720" fill="{N}" opacity="0" pointer-events="none"/>')
# the stairs to the next floor, at the right, with a small door at the top
o.append(f'<g id="stairs">' + ''.join(f'<rect x="{1080 + k * 0}" y="{600 - (k + 1) * 34}" width="{200 - k * 22}" height="34" fill="#fff" stroke="{N}" stroke-width="3" transform="translate({k * 22} 0)"/>' for k in range(7))
         + f'<line x1="1080" y1="600" x2="1240" y2="362" stroke="{N}" stroke-width="5"/>' + ''.join(f'<line x1="{1080 + k * 26}" y1="{600 - k * 38.6}" x2="{1080 + k * 26}" y2="{560 - k * 38.6}" stroke="{N}" stroke-width="3"/>' for k in range(7))
         + f'<rect x="1214" y="250" width="56" height="112" fill="{N}"/><rect id="pglow" x="1220" y="256" width="44" height="106" fill="#ffd9a8" opacity="0"/><rect x="1220" y="256" width="44" height="106" fill="#fff" stroke="{N}" stroke-width="2" id="pdoor"/>'
         + f'<text id="plbl" x="1170" y="300" text-anchor="middle" font-family="Playfair Display,serif" font-weight="900" font-size="22" letter-spacing="2" fill="#b8892f" opacity="0">PRELIM</text></g>')
SVG = '<svg id="scene" viewBox="0 0 1280 720" xmlns="http://www.w3.org/2000/svg">' + ''.join(o) + '</svg>'
open('/tmp/claude-0/anim/scene9.svg', 'w').write(SVG)
JS = r'''
const TL = __TL__;
const ph = (t, a, b) => Math.max(0, Math.min(1, (t - a) / (b - a)));
const S = id => document.getElementById(id);
const L0 = TL.lines, F = (re) => L0.find(l => l.text && re.test(l.text)), PI = L0.filter(l => l.who === 'piano');
const K = { intro: L0[0].t0, tune: PI[0].t0, high: PI[1].t0, highA: F(/^High\./).t0, low: PI[2].t0, lowA: F(/^Low\./).t0, same1: PI[3].t0, same2: PI[4].t0, sameA: F(/same tune, twice/).t0,
  end: F(/^And here is how it ended/).t0, open: F(/^When the playing stops/).t0, word: F(/writes one word/).t0, tease: F(/^Behind the next door/).t0, pre: F(/^At the top of the stairs/).t0, dur: TL.dur };
function setT(t) {
  // the light under the door breathes while someone plays
  const playing = (t >= K.tune && t < K.tune + 4) || (t >= K.high && t < K.high + 1.6) || (t >= K.low && t < K.low + 1.6) || (t >= K.same1 && t < K.same2 + 2.2);
  S('crack').setAttribute('opacity', playing ? .6 + .4 * Math.abs(Math.sin(t * 7)) : .5);
  for (let k = 0; k < 2; k++) { const f = S('lf' + k); if (f) { f.style.transformBox = 'fill-box'; f.style.transformOrigin = 'center bottom'; f.setAttribute('transform', `scale(1 ${1 + .1 * Math.sin(t * 6 + k)})`); } }
  // Clara's head: pressed to the door, tilting up for a high note and down for a low one
  let tilt = -14, dy = 0;
  if (t >= K.high && t < K.low) { tilt = -22; dy = -4; } else if (t >= K.low && t < K.same1) { tilt = -6; dy = 4; }
  S('chead').setAttribute('transform', `rotate(${tilt} 592 424) translate(0 ${dy})`);
  // notes coming through the door
  for (let i = 0; i < 6; i++) { const g = S('hn' + i); let on = 0, x = 0, y = 0;
    const hi = t >= K.high && t < K.highA + 2.5, lo = t >= K.low && t < K.lowA + 2.5, tune = t >= K.tune && t < K.tune + 6;
    if (hi || lo || tune) { const t0 = hi ? K.high : lo ? K.low : K.tune, p = ((t - t0) * .45 + i / 6) % 1;
      x = 320 + p * 120; y = hi ? 230 + 18 * Math.sin(p * 6 + i) : lo ? 560 + 10 * Math.sin(p * 6 + i) : 420 - p * 60; on = Math.sin(Math.PI * p); }
    g.setAttribute('opacity', on); g.setAttribute('transform', `translate(${x} ${y})`); }
  // the answers
  const a = S('ans'); let txt = '', op = 0, ay = 300;
  if (t >= K.highA && t < K.low) { txt = 'HIGH ↑'; op = ph(t, K.highA, K.highA + .4); ay = 300; }
  else if (t >= K.lowA && t < K.same1) { txt = 'LOW ↓'; op = ph(t, K.lowA, K.lowA + .4); ay = 440; }
  a.textContent = txt; a.setAttribute('opacity', op); a.setAttribute('y', ay);
  S('same').setAttribute('opacity', t >= K.same1 && t < K.end ? (t < K.same2 ? .5 : 1) : 0);
  // the door opens on the Butler
  const od = t >= K.open ? ph(t, K.open, K.open + 2.5) : 0;
  S('leaf').setAttribute('transform', `translate(${300 + 190 * od} 0) scale(${1 - .82 * od} 1)`);
  S('crack').setAttribute('opacity', od > 0 ? 0 : S('crack').getAttribute('opacity'));
  S('book').setAttribute('opacity', t >= K.word && t < K.tease ? ph(t, K.word, K.word + .6) : 0);
  // behind the next door: the room dims, the little door at the top of the stairs lights up
  S('dim').setAttribute('opacity', t >= K.tease ? .45 * ph(t, K.tease, K.tease + 1.5) : 0);
  const pg = t >= K.pre ? ph(t, K.pre, K.pre + 3) : 0;
  S('pglow').setAttribute('opacity', pg); S('pdoor').setAttribute('transform', `translate(${1220 * .0} 0) scale(${1 - .6 * pg} 1)`); S('pdoor').style.transformBox = 'fill-box'; S('pdoor').style.transformOrigin = 'left center';
  S('plbl').setAttribute('opacity', pg);
  const sub = document.getElementById('sub'); if (sub) { const l = L0.find(l => l.text && t >= l.t0 && t < l.t1 + .25); sub.textContent = l ? l.text.replace(/[⟨⟩]/g, '') : ''; sub.style.opacity = l ? 1 : 0; }
  const ttl = document.getElementById('ttl'); if (ttl) ttl.style.opacity = t < K.intro - .4 ? 1 : Math.max(0, 1 - (t - K.intro + .4) / .6);
}
window.setT = setT;
'''.replace('__TL__', json.dumps(TL))
open('/tmp/claude-0/anim/scene9.js', 'w').write(JS)
film = open('/tmp/claude-0/anim/film.html').read()
i = film.index('<svg id="scene"'); j = film.index('</svg>', i) + 6
film = film[:i] + SVG + film[j:]
film = film.replace('Room 8</small><b>Loud and soft</b><i>The music evening</i>', 'Room 9</small><b>Ear training</b><i>The door</i>')
i = film.index('<script>') + 8; j = film.index('</script>', i)
film = film[:i] + JS + film[j:]
# the dim layer sits above the stairs, but the little door and its name must shine through: move the stairs above the dim layer
open('/tmp/claude-0/anim/film9.html', 'w').write(film)
print('ok', len(SVG))
