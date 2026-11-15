# The seven Beginner rooms before Room 8 (her 14 Nov: "첫번째 비기너 방 다 만들어줘 먼저").
import sys, json
sys.path.insert(0, '/tmp/claude-0/anim'); from kit import *
R = {}
# 1 Sitting and hands: the Butler raises the stool, Clara sits, the key level appears; ending: Leipzig, 1828
import re as _re
SIT = json.load(open('/tmp/claude-0/pk/posture_svgs.json'))['1:Just right']
SIT = _re.sub(r'<text[^>]*>key level</text>', '', SIT); SIT = _re.sub(r'<line[^>]*stroke-dasharray="4 4"[^>]*>(</line>)?', '', SIT); SIT = inner(SIT).replace('cy="156.0"', 'cy="159.0"')
SIT = _re.sub(r'<line x1="6.0" y1="162.0"[^>]*>(</line>)?', '', SIT)
def _drop(svg, tag):
    i = svg.index(tag); d = 0; k = i
    for m in _re.finditer(r'<g\b|</g>', svg[i:]):
        d += 1 if m.group(0) == '<g' else -1
        if d == 0: return svg[:i] + svg[i + m.end():]
NOGIRL = _re.sub(r'<circle[^>]*>(</circle>)?', '', _drop(SIT, '<g data-who="girl">'))
# her 14 Nov: the first posture picture must be a side view: Clara comes in through the door and we see her at the piano from the side
R['hbr-B1'] = dict(n=1, title='Sitting and hands', sub='The chair comes first', at=('K.quote+3', 'K.endBody+4'),
  parts=[wall(chand=False, style='stripe', cat='B'), floor(), sign('B'), plate(1010, 200, bigtext(-2, 40, '𝄞', 88), '1828', 'Leipzig', 'Clara Wieck, aged nine'),
         f'<g id="side" opacity="0"><g transform="translate(470 178.8) scale(2.6)">{SIT}</g></g>',
         f'<g id="emptyp"><g transform="translate(470 178.8) scale(2.6)">' + NOGIRL + '</g></g>',
         clara_stand(1100, 'cst'),
         f'<g id="kl" opacity="0"><line x1="520" x2="800" y1="428" y2="428" stroke="{C}" stroke-width="4" stroke-dasharray="12 10"/><text x="520" y="416" font-family="Atkinson Hyperlegible,sans-serif" font-weight="700" font-size="24" fill="{C}">key level</text></g>',
         ''.join(f'<g id="tip{k}" opacity="0"><circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{C}" stroke-width="5"/><text x="{tx}" y="{ty}" text-anchor="middle" font-family="Atkinson Hyperlegible,sans-serif" font-weight="700" font-size="24" fill="{C}">{k + 1}. {lab}</text></g>' for k, (x, y, r, tx, ty, lab) in enumerate(((618, 478, 40, 560, 556, 'front half'), (752, 588, 30, 900, 586, 'feet flat'), (680, 356, 56, 760, 276, 'back tall'), (780, 426, 34, 900, 386, 'arms level')))),
         butler(240), door(), notes(), dim(), lone()],
  js=r'''
  const SH = F(/one thing at a time/) || {t0: 1e9, t1: 1e9}; const step = t >= SH.t0 + 2 && t < K.end ? Math.min(3, Math.floor((t - SH.t0 - 2) / ((SH.t1 - SH.t0 - 2) / 4))) : -1;
  for (let k = 0; k < 4; k++) S('tip' + k).setAttribute('opacity', step === k ? 1 : (step > k ? .35 : 0));
  // Clara comes in through the door and walks to the piano; once the Butler has spoken she is seen sitting, from the side
  const walk = ph(t, K.intro + .5, K.quote), sit = t >= K.quote + 1.2;
  const x = 1100 - 420 * walk; S('cst').setAttribute('transform', `translate(${x - 1100} ${-4 * Math.abs(Math.sin(t * 6)) * (walk > 0 && walk < 1 ? 1 : 0)})`);
  S('cst').setAttribute('opacity', sit ? 0 : 1); S('side').setAttribute('opacity', sit ? 1 : 0); S('emptyp').setAttribute('opacity', sit ? 0 : 1);
  const op0 = t >= K.intro && t < K.intro + 2 ? ph(t, K.intro, K.intro + 1.5) : (t >= K.intro + 2 && t < K.tease ? 1 - ph(t, K.intro + 2, K.intro + 3) : 0);
  const lf = S('leaf'); if (t < K.tease) { lf.setAttribute('transform', `translate(1176 0) scale(${1 - .72 * op0} 1)`); S('glow').setAttribute('opacity', op0 * .9); }
  S('kl').setAttribute('opacity', step === 3 || (t >= K.cue && t < K.end) ? 1 : 0);
  notesFX(t, (t >= K.cue && t < K.cue + 4) || (t >= K.endBody && t < K.tease) ? 6 : 0, 760, 200, 300, 180, .5);''')
# 2 The keyboard: counting the keys, losing count; then the twos and threes light up; ending: Mozart's smaller piano
def kb5(y=380, h=130):   # Mozart's keyboard: five octaves, F to F, 35 white keys at the same size as the 88
    n, kw = 36, 1188 / 52; x0 = 640 - n * kw / 2; o = ''
    for k in range(n): o += f'<rect x="{x0 + k * kw:.1f}" y="{y}" width="{kw:.1f}" height="{h}" fill="#fff" stroke="{N}" stroke-width="1.4"/>'
    for k in range(n - 1):
        L = (k + 3) % 7
        if L in (2, 6): continue
        o += f'<rect x="{x0 + (k + 1) * kw - 7:.1f}" y="{y}" width="14" height="{h * .62:.0f}" fill="{N}"/>'
    w = n * kw
    return f'<g id="kbd5" opacity="0"><rect x="{x0 - 14:.0f}" y="{y - 22}" width="{w + 28:.0f}" height="22" rx="4" fill="{N}"/>{o}<rect x="{x0 - 14:.0f}" y="{y + h}" width="{w + 28:.0f}" height="20" rx="4" fill="{N}"/><rect x="{x0 + 20:.0f}" y="{y + h + 20}" width="14" height="{600 - y - h - 20}" fill="{N}"/><rect x="{x0 + w - 34:.0f}" y="{y + h + 20}" width="14" height="{600 - y - h - 20}" fill="{N}"/><text x="640" y="350" text-anchor="middle" font-family="Atkinson Hyperlegible,sans-serif" font-weight="700" font-size="22" letter-spacing="3" fill="{C}">MOZART’S PIANO · ABOUT FIVE OCTAVES</text></g>'
def longkb(x0=46, y=380, h=130):   # all 88 keys: 52 white keys from A0 to C8, 36 black keys in twos and threes
    n, kw = 52, 1188 / 52; o = ''
    for k in range(n): o += f'<rect id="wk{k}" x="{x0 + k * kw:.1f}" y="{y}" width="{kw:.1f}" height="{h}" fill="#fff" stroke="{N}" stroke-width="1.4"/>'
    for k in range(n - 1):
        L = (k + 5) % 7   # 0 = C ... 6 = B; the first key is A
        if L in (2, 6): continue
        g = 2 if L in (0, 1) else 3
        o += f'<rect class="bk{g}" x="{x0 + (k + 1) * kw - 7:.1f}" y="{y}" width="14" height="{h * .62:.0f}" fill="{N}"/>'
    w = n * kw
    return f'<g id="kbd"><rect x="{x0 - 14}" y="{y - 22}" width="{w + 28:.0f}" height="22" rx="4" fill="{N}"/>{o}<rect x="{x0 - 14}" y="{y + h}" width="{w + 28:.0f}" height="20" rx="4" fill="{N}"/><rect x="{x0 + 20}" y="{y + h + 20}" width="14" height="{600 - y - h - 20}" fill="{N}"/><rect x="{x0 + w - 34:.0f}" y="{y + h + 20}" width="14" height="{600 - y - h - 20}" fill="{N}"/></g>'
R['hbr-P1'] = dict(n=2, title='The keyboard', sub='Eighty-eight keys', at=('K.quote+3', 'K.endBody+5'),
  parts=[wall(chand=False, win=False, style='dots', cat='P'), floor(), landing(), sign('P'), plate(640, 146, bigtext(0, 30, '88', 64, font='Playfair Display,serif', extra='font-weight="900"'), '1785', 'Vienna', 'about five octaves'), longkb(), kb5(),
         bigtext(330, 300, '', 64, 'cnt', 'Playfair Display,serif', C, 'font-weight="900"'), f'<g transform="translate(0 70)">{clara_stand(330, "clara")}</g>', butler(1090, 1.62), dim(), lone()],
  js=r'''
  // counting: the numbers climb, then lose their way
  const c = S('cnt'); if (t >= K.intro && t < K.quote) { const p = (t - K.intro) / (K.quote - K.intro); const v = Math.floor(p * 58); c.textContent = v < 44 ? String(v + 1) : v < 48 ? '…?' : String(v - 40);
  for (let k = 0; k < 52; k++) if (t >= K.intro && t < K.quote) S('wk' + k).setAttribute('stroke-width', k === Math.min(51, Math.floor(((t - K.intro) / (K.quote - K.intro)) * 58 * 52 / 88)) ? 4 : 1.4); c.setAttribute('opacity', 1); } else c.setAttribute('opacity', 0);
  // the pattern: twos and threes, again and again
  const pat = t >= K.quote + 2 && t < K.end, which = Math.floor(t / 1.2) % 2;
  document.querySelectorAll('.bk2').forEach(e => e.setAttribute('fill', pat && which === 0 ? '#e4572e' : '#26296b'));
  document.querySelectorAll('.bk3').forEach(e => e.setAttribute('fill', pat && which === 1 ? '#e4572e' : '#26296b'));
  // the low key and the high key ring in the cue
  for (let k = 0; k < 52; k++) S('wk' + k).setAttribute('fill', (t >= K.cue && t < K.cue + 1.3 && k === 2) || (t >= K.cue + 1.3 && t < K.cue + 2.6 && k === 51) ? '#ffd9a8' : '#fff');
  // Mozart's piano: the keyboard shrinks to about five octaves, then grows back
  const sh = t >= K.endBody && t < K.tease ? (t < K.endBody + 6 ? ph(t, K.endBody, K.endBody + 1.5) : 1 - ph(t, K.endBody + 6, K.endBody + 7.5)) : 0;
  S('kbd').setAttribute('opacity', 1 - sh); S('kbd5').setAttribute('opacity', sh);''')
# 3 Finger numbers: the bell board in the servants' hall; then the two hands
def bells():
    o = f'<g id="board"><rect x="400" y="120" width="480" height="210" rx="10" fill="#fff" stroke="{N}" stroke-width="5"/><text x="640" y="160" text-anchor="middle" font-family="Atkinson Hyperlegible,sans-serif" font-weight="700" font-size="18" letter-spacing="4" fill="#6d6f9c">THE BELL BOARD</text>'
    for k in range(5):
        x = 460 + k * 90
        o += f'<g id="bell{k}"><line x1="{x}" y1="180" x2="{x}" y2="200" stroke="{N}" stroke-width="3"/><path d="M{x - 22} 248 Q{x - 20} 202 {x} 200 Q{x + 20} 202 {x + 22} 248 Z" fill="{C}"/><circle cx="{x}" cy="254" r="6" fill="{N}"/></g><text id="bn{k}" x="{x}" y="304" text-anchor="middle" font-family="Playfair Display,serif" font-weight="900" font-size="32" fill="{N}">{k + 1}</text>'
    return o + '</g>'
R['hbr-L1'] = dict(n=3, title='Finger numbers', sub='The bell board', at=('K.intro+6', 'K.endBody+9'),
  parts=[wall(chand=False, style='stripe', cat='L'), floor(), sign('L'), plate(1010, 200, bigtext(0, 30, '1–5', 46, font='Playfair Display,serif', extra='font-weight="900"'), '1753', 'Berlin', 'C. P. E. Bach’s book'), bells(),
         f'<g id="hands" opacity="0"><g transform="translate(330 70) scale(2.3)">{inner(ART["hand-L"])}</g><g transform="translate(660 70) scale(2.3)">{inner(ART["hand-R"])}</g></g>',
         bigtext(640, 312, '', 64, 'bign', 'Playfair Display,serif', C, 'font-weight="900"'), clara_stand(640, 'clara', 'both'), butler(900), door(), dim(), lone()],
  js=r'''
  const cyc = t >= K.intro + 4 && t < K.tryA ? Math.floor((t - K.intro - 4) / .9) % 5 : -1;
  let ring = cyc; if (t >= K.cue && t < K.cue + 3.2) ring = Math.min(4, Math.floor((t - K.cue) / .62));
  const KH = (F(/^Your fingers have numbers/) || {}).t0 || 1e9; const e = t >= K.endBody && t < K.tease; const showHands = (t >= KH && t < K.end) || e; S('board').setAttribute('opacity', showHands ? 0 : 1); S('hands').setAttribute('opacity', showHands ? 1 : 0);
  for (let k = 0; k < 5; k++) { const b = S('bell' + k); b.style.transformBox = 'fill-box'; b.style.transformOrigin = 'center top'; b.setAttribute('transform', k === ring && !showHands ? `rotate(${18 * Math.sin(t * 22)})` : ''); S('bn' + k).setAttribute('fill', k === ring ? '#e4572e' : '#26296b'); }
  const bn = S('bign'); bn.textContent = ring >= 0 ? String(ring + 1) : ''; bn.setAttribute('opacity', showHands && ring >= 0 ? 1 : 0);
  // ending: the thumb that once hung idle becomes number 1
  const TB = (F(/proper working finger/) || {}).t0 || (K.endBody + 8); for (let k = 0; k < 5; k++) S('bn' + k).setAttribute('opacity', e ? 0 : 1); if (e) bn.setAttribute('opacity', 0); bn.setAttribute('font-size', 64);''')
# 4 The staff and the clefs: the Queen's floor and the King's floor
def grand():   # two horizontal staves, 16 between lines; clefs drawn to the staff (ink measured: treble 1.18 em tall, bass 0.58 em)
    T, B = 130, 280
    o = ''.join(f'<line x1="300" x2="820" y1="{T + i * 16}" y2="{T + i * 16}" stroke="{N}" stroke-width="3"/>' for i in range(5)) + ''.join(f'<line x1="300" x2="820" y1="{B + i * 16}" y2="{B + i * 16}" stroke="{N}" stroke-width="3"/>' for i in range(5))
    o += f'<line x1="300" x2="300" y1="{T}" y2="{B + 64}" stroke="{N}" stroke-width="4"/>' + bigtext(336, T + 59, '𝄞', 69, 'tclef') + bigtext(336, B + 59, '𝄢', 67, 'bclef')
    o += f'<ellipse id="hiN" cx="600" cy="{T}" rx="10" ry="7.5" transform="rotate(-20 600 {T})" fill="{C}" opacity="0"/><ellipse id="loN" cx="600" cy="{B + 64}" rx="10" ry="7.5" transform="rotate(-20 600 {B + 64})" fill="{C}" opacity="0"/>'
    o += f'<g id="letters" opacity="0">' + bigtext(470, T + 16 * 3 + 22, 'G', 64, 'lg', 'Playfair Display,serif', C, 'font-weight="900"') + bigtext(470, B + 16 + 22, 'F', 64, 'lf', 'Playfair Display,serif', C, 'font-weight="900"') + '</g>'
    lab = lambda y, t: f'<text x="820" y="{y}" text-anchor="end" font-family="Atkinson Hyperlegible,sans-serif" font-size="16" font-weight="700" letter-spacing="3" fill="#6d6f9c">{t}</text>'
    o += lab(T - 18, 'THE QUEEN’S FLOOR') + lab(B - 18, 'THE KING’S FLOOR')
    return f'<g id="gs">{o}</g>'
R['hbr-P2'] = dict(n=4, title='The staff and the clefs', sub='Two floors', at=('K.intro+4', 'K.endBody+6'),
  parts=[wall(chand=False, win=False, style='dots', cat='P'), floor(), sign('P'), ''.join(f'<rect x="{1000 + k * 30}" y="{600 - (k + 1) * 34}" width="{280 - k * 30}" height="34" fill="#fff" stroke="{N}" stroke-width="3"/>' for k in range(10)), plate(1080, 146, bigtext(0, 22, '𝄞𝄢', 48), 'c. 1025', 'Arezzo', 'Guido’s lines'), grand(), piece('VIC_QUEEN', 190, 1.3, 206, 'queen'), piece('VIC_KING', 190, 1.25, 344, 'king'),
         clara_stand(600, 'clara'), butler(905), dim(), lone()],
  js=r'''
  // the Queen and the King each claim a floor
  const mid = K.intro + (L0[0].t1 - K.intro) * .55, q = t >= K.intro && t < mid, k2 = t >= mid && t < L0[0].t1 + 1;
  S('queen').setAttribute('transform', `translate(190 ${206 - (q ? 8 * Math.abs(Math.sin(t * 6)) : 0)}) scale(1.3)`); S('king').setAttribute('transform', `translate(190 ${344 - (k2 ? 8 * Math.abs(Math.sin(t * 6)) : 0)}) scale(1.25)`);
  S('hiN').setAttribute('opacity', t >= K.cue && t < K.cue + 1.3 ? 1 : 0); S('loN').setAttribute('opacity', t >= K.cue + 1.3 && t < K.cue + 2.8 ? 1 : 0);
  // the signs at the start of each floor glow while their owner speaks
  S('tclef').setAttribute('fill', q ? '#e4572e' : '#26296b'); S('bclef').setAttribute('fill', k2 ? '#e4572e' : '#26296b');
  // ending: Guido's lines, and the clefs that began as letters
  const lt = t >= K.endBody + 4 && t < K.tease; S('letters').setAttribute('opacity', lt ? ph(t, K.endBody + 4, K.endBody + 5) : 0);''')
# 5 The beat: the hall clock's pendulum, a row of beats on the wall; ending: the metronome
def beatrow():   # her 14 Nov: the beat always sits underneath the music; music above, beats below
    X = lambda k: 850 + k * 32
    o = '<g id="row">' + ''.join(f'<circle id="bt{k}" cx="{X(k)}" cy="214" r="{14 if k % 4 == 0 else 10}" fill="#fff" stroke="{N}" stroke-width="3"/>' for k in range(8)) + f'<line x1="{X(3.5)}" x2="{X(3.5)}" y1="100" y2="232" stroke="{N}" stroke-width="3"/>'
    o += f'<text x="826" y="168" text-anchor="end" font-family="Atkinson Hyperlegible,sans-serif" font-weight="700" font-size="14" letter-spacing="2" fill="#6d6f9c">MUSIC</text><text x="826" y="219" text-anchor="end" font-family="Atkinson Hyperlegible,sans-serif" font-weight="700" font-size="14" letter-spacing="2" fill="#6d6f9c">BEAT</text>'
    o += '<g id="mus" opacity="0">' + ''.join(nshape(kd, X(k) - 4, 160, .9) for k, kd in ((0, 'crotchet'), (1, 'crotchet'), (2, 'minim'), (4, 'crotchet'), (5, 'crotchet'), (6, 'crotchet'), (7, 'crotchet'))) + '</g>'
    return o + '</g>'
def metronome(x=880): return f'<g id="metro" opacity="0"><path d="M{x - 50} 600 L{x - 22} 420 L{x + 22} 420 L{x + 50} 600 Z" fill="#fff" stroke="{N}" stroke-width="4"/><g id="marm"><line x1="{x}" y1="580" x2="{x}" y2="430" stroke="{N}" stroke-width="4"/><rect x="{x - 9}" y="470" width="18" height="16" fill="{C}"/></g></g>'
R['hbr-T1'] = dict(n=5, title='The beat', sub='The clock in the hall', at=('K.intro+5', 'K.endBody+3'),
  parts=[wall(chand=False, win=False, style='panel', cat='T'), floor(), sign('T'), plate(230, 330, ''.join(nshape('crotchet', -36 + k * 22, 30, .8) for k in range(4)), '1817', 'Vienna', 'metronome marks', 1.5), beatrow(), clock(700, 150), clara_stand(470, 'clara'), metronome(880), butler(930), fanlight_door(1150), dim(), lone()],
  js=r'''
  const per = (t >= K.cue && t < K.cue + 5) ? .62 : 1.0, ph0 = t / per, sw = Math.sin(Math.PI * ph0);
  const pd = S('clockpd'); pd.setAttribute('transform', `rotate(${6 * sw} 700 262)`);
  const beat = Math.floor(ph0) % 8; for (let k = 0; k < 8; k++) S('bt' + k).setAttribute('fill', k === beat && t >= K.intro ? (k % 4 === 0 ? '#e4572e' : '#26296b') : '#fff');
  const UN = (F(/^Underneath/) || {}).t0 || 1e9; S('mus').setAttribute('opacity', t >= UN && t < K.end ? ph(t, UN, UN + .8) : (t >= K.end ? .0 : 0));
  const mh = S('clockmh'); mh.setAttribute('transform', `rotate(${(t * 6) % 360} 700 204)`);
  S('clara').setAttribute('transform', `translate(0 ${-3 * Math.abs(Math.sin(Math.PI * ph0))})`);
  const me = t >= K.endBody && t < K.tease; S('metro').setAttribute('opacity', me ? ph(t, K.endBody, K.endBody + 1) : 0);
  S('marm').setAttribute('transform', `rotate(${me ? 22 * Math.sin(Math.PI * t / .75) : 0} 880 580)`); S('butler').setAttribute('opacity', me ? 0 : 1);''')
# 6 Crotchet and minim: one note gone in a tick, one that waits for two
R['hbr-T2'] = dict(n=6, title='Notes: crotchet and minim', sub='Two notes in the hall', at=('K.intro+5', 'K.endBody+4'),
  parts=[wall(win=False, chand=False, style='panel', cat='T'), floor(), sign('T'), fanlight_door(1150), plate(640, 160, '<g transform="translate(0 46) scale(1.6)"><path d="M0 -16 L12 0 L0 16 L-12 0 Z" fill="#26296b"/><rect x="-1.8" y="-62" width="3.6" height="48" fill="#26296b"/></g>', '1300s', 'Paris', 'minima: the smallest', 1.15), clock(330, 200, 'ck'),
         nshape('crotchet', 556, 430, 3, 'crn'), nshape('minim', 796, 430, 3, 'mnm'),
         '<g id="c1">' + f'<circle id="cc0" cx="560" cy="500" r="20" fill="{C}"/>' + '</g><g id="c2">' + ''.join(f'<circle id="mc{k}" cx="{776 + k * 50}" cy="500" r="20" fill="{C}"/>' for k in range(2)) + '</g>',
         clara_stand(930, 'clara'), dim(), lone()],
  js=r'''
  const per = 1.0, b = Math.floor(t / per), f = (t / per) % 1;
  S('ckpd').setAttribute('transform', `rotate(${6 * Math.sin(Math.PI * t / per)} 330 312)`);
  // the crotchet hops on every beat and is gone; the minim holds for two
  S('crn').setAttribute('transform', `translate(0 ${-8 * Math.max(0, 1 - f * 3)})`); S('crn').setAttribute('opacity', .35 + .65 * Math.max(0, 1 - f * 1.4));
  const m2 = (t / per) % 2; S('mnm').setAttribute('opacity', m2 < 1.9 ? 1 : .4);
  S('cc0').setAttribute('opacity', f < .7 ? 1 : .25); S('mc0').setAttribute('opacity', m2 < 1 ? 1 : .35); S('mc1').setAttribute('opacity', m2 >= 1 ? 1 : .35);
  // ending: the minim was once among the shortest notes; it shrinks, then grows back to today's size
  const e = t >= K.endBody && t < K.tease, sh = e ? (t < K.endBody + 6 ? ph(t, K.endBody, K.endBody + 1.2) : 1 - ph(t, K.endBody + 6, K.endBody + 8)) : 0;
  S('mnm').setAttribute('transform', `scale(${1 - .6 * sh})`);''')
# 7 Dotted minim and semibreve: the clock strikes four; Clara holds one note for the whole bar
def rings(): return ''.join(f'<circle id="rg{k}" cx="640" cy="330" r="60" fill="none" stroke="{C}" stroke-width="4" opacity="0"/>' for k in range(4))
R['hbr-T2-s2'] = dict(n=7, title='Notes: dotted minim and semibreve', sub='A note for the whole bar', at=('K.quote+1', 'K.endBody+5'),
  parts=[wall(win=False, chand=False, style='panel', cat='T'), floor(), sign('T'), plate(1010, 200, '<g transform="translate(0 22) scale(1.3)"><rect x="-34" y="-14" width="28" height="28" fill="#26296b"/><path d="M22 -16 L34 0 L22 16 L10 0 Z" fill="#26296b"/></g>', '1200s', 'Paris', 'breve · semibreve'), clock(300, 160, 'ck'), piano_front(640), stool(640), clara_sit(640, 'clara'), rings(),
         nshape('semibreve', 640, 214, 2.2, 'sbn'), '<g id="dotg" opacity="0">' + nshape('dminim', 626, 214, 2.0) + ''.join(f'<circle id="dc{k}" cx="{590 + k * 50}" cy="262" r="16" fill="#fff" stroke="{C if k == 2 else N}" stroke-width="3"/>' for k in range(3)) + '</g>', ''.join(f'<circle id="sc{k}" cx="{565 + k * 50}" cy="252" r="16" fill="#fff" stroke="{C}" stroke-width="3"/>' for k in range(4)),
         '<g id="brvg" opacity="0">' + nshape('breve', 520, 220, 1.6) + bigtext(592, 236, '=', 56, None, 'Playfair Display,serif', C, 'font-weight="900"') + nshape('semibreve', 660, 220, 1.6) + bigtext(724, 236, '+', 56, None, 'Playfair Display,serif', C, 'font-weight="900"') + nshape('semibreve', 790, 220, 1.6) + '</g>', butler(880), fanlight_door(1150), dim(), lone()],
  js=r'''
  const TS = (F(/^Then the clock strikes four/) || {}).t0 || K.intro, TC = (F(/^Clara holds the note/) || {}).t0 || 1e9;
  const per = 1.0, hold = (t >= TS && t < K.tryA), b = hold ? Math.floor((t - TS) / per) % 4 : -1;
  const dt = t >= K.intro && t < TS; S('dotg').setAttribute('opacity', dt ? 1 : 0); for (let k = 0; k < 3; k++) S('dc' + k).setAttribute('fill', dt && t >= TC + k * .9 ? (k === 2 ? '#e4572e' : '#26296b') : '#fff');
  S('ckpd').setAttribute('transform', `rotate(${6 * Math.sin(Math.PI * t / per)} 300 272)`);
  for (let k = 0; k < 4; k++) { S('sc' + k).setAttribute('fill', hold && k <= b ? '#e4572e' : '#fff');
    const p = ((t * .45) + k / 4) % 1, g = S('rg' + k); g.setAttribute('r', 60 + p * 260); g.setAttribute('opacity', hold ? (1 - p) * .8 : 0); }
  const ff = S('firef'); if (ff) { ff.style.transformBox = 'fill-box'; ff.style.transformOrigin = 'center bottom'; ff.setAttribute('transform', `scale(1 ${1 + .12 * Math.sin(t * 7)})`); }
  const e = t >= K.endBody && t < K.tease; S('brvg').setAttribute('opacity', e ? 1 : 0); S('sbn').setAttribute('opacity', e || dt ? 0 : 1);
  for (let k = 0; k < 4; k++) S('sc' + k).setAttribute('opacity', e || dt ? 0 : 1);''')
if __name__ == '__main__':
    for rid, r in R.items():
        try: TL = json.load(open(f'/tmp/claude-0/anim/rooms/{rid}.json'))
        except FileNotFoundError: continue
        svg = scene(r['parts'])
        js = 'const TL = ' + json.dumps(TL) + ';\n' + PRELUDE + 'function setT(t) {\n  common(t);\n' + r['js'] + '\n}\nwindow.setT = setT;\n'
        open(f'/tmp/claude-0/anim/rooms/{rid}.svg', 'w').write(svg); open(f'/tmp/claude-0/anim/rooms/{rid}.js', 'w').write(js)
        open(f'/tmp/claude-0/anim/rooms/{rid}.html', 'w').write(film(svg, js, r['n'], r['title'], r['sub']))
        json.dump({'at': r['at'], 'dur': TL['dur']}, open(f'/tmp/claude-0/anim/rooms/{rid}.meta.json', 'w'))
        print('built', rid)
