# The seven Beginner rooms before Room 8 (her 14 Nov: "첫번째 비기너 방 다 만들어줘 먼저").
import sys, json
sys.path.insert(0, '/tmp/claude-0/anim'); from kit import *
R = {}
# 1 Sitting and hands: the Butler raises the stool, Clara sits, the key level appears; ending: Leipzig, 1828
R['hbr-B1'] = dict(n=1, title='Sitting and hands', sub='The chair comes first', at=('K.quote+3', 'K.endBody+4'),
  parts=[wall(), floor(), plate(1010, 200, bigtext(-2, 44, '𝄞', 132), '1828', 'Leipzig', 'Clara Wieck, aged nine'), chair(230), chair(340),
         piece('VIC_QUEEN', 230, 2.0, 514, 'queen'), piece('VIC_KING', 340, 1.9, 514, 'king'), piano_front(640), stool(640), clara_sit(640, 'csit'), clara_stand(470, 'cst'),
         f'<g id="kl" opacity="0"><line x1="540" x2="860" y1="482" y2="482" stroke="{C}" stroke-width="4" stroke-dasharray="12 10"/><text x="440" y="490" font-family="Atkinson Hyperlegible,sans-serif" font-weight="700" font-size="22" fill="{C}">key level</text></g>',
         butler(880), door(), notes(), dim(), lone()],
  js=r'''
  const up = ph(t, K.quote, K.quote + 1.6), sit = t >= K.quote + 1.8 && !(t >= K.tease && false);
  S('stool').setAttribute('transform', `translate(0 ${18 * (1 - up)})`);
  S('cst').setAttribute('opacity', sit ? 0 : 1); S('csit').setAttribute('opacity', sit ? 1 : 0);
  S('kl').setAttribute('opacity', t >= K.quote + 2.4 && t < K.end ? ph(t, K.quote + 2.4, K.quote + 3.2) : 0);
  const clap = t >= K.endBody && t < K.tease; S('queen').setAttribute('transform', `translate(230 ${514 - (clap ? 5 * Math.abs(Math.sin(t * 7)) : 0)}) scale(2.0)`); S('king').setAttribute('transform', `translate(340 ${514 - (clap ? 5 * Math.abs(Math.sin(t * 7 + 1)) : 0)}) scale(1.9)`);
  notesFX(t, (t >= K.cue && t < K.cue + 4) || clap ? 6 : 0, 560, 200, 290, 180, .5);''')
# 2 The keyboard: counting the keys, losing count; then the twos and threes light up; ending: Mozart's smaller piano
def longkb(x0=150, n=25, kw=34, y=390, h=120):
    o = ''.join(f'<rect id="wk{k}" x="{x0 + k * kw}" y="{y}" width="{kw}" height="{h}" fill="#fff" stroke="{N}" stroke-width="2"/>' for k in range(n))
    for k in range(n - 1):
        if k % 7 in (2, 6): continue
        g = 2 if k % 7 in (0, 1) else 3
        o += f'<rect class="bk{g}" x="{x0 + (k + 1) * kw - 10}" y="{y}" width="20" height="{h * .62:.0f}" fill="{N}"/>'
    return f'<g id="kbd"><rect x="{x0 - 16}" y="{y - 20}" width="{n * kw + 32}" height="20" rx="4" fill="{N}"/>{o}<rect x="{x0 - 16}" y="{y + h}" width="{n * kw + 32}" height="22" rx="4" fill="{N}"/><rect x="{x0}" y="{y + h + 22}" width="14" height="{600 - y - h - 22}" fill="{N}"/><rect x="{x0 + n * kw - 14}" y="{y + h + 22}" width="14" height="{600 - y - h - 22}" fill="{N}"/></g>'
R['hbr-P1'] = dict(n=2, title='The keyboard', sub='Eighty-eight keys', at=('K.quote+3', 'K.endBody+5'),
  parts=[wall(), floor(), plate(1010, 200, bigtext(0, 30, '88', 64, font='Playfair Display,serif', extra='font-weight="900"'), '1785', 'Vienna', 'about five octaves'), longkb(),
         bigtext(560, 330, '', 54, 'cnt', 'Playfair Display,serif', C, 'font-weight="900"'), clara_stand(560, 'clara'), butler(1000, 1.1), door(), dim(), lone()],
  js=r'''
  // counting: the numbers climb, then lose their way
  const c = S('cnt'); if (t >= K.intro && t < K.quote) { const p = (t - K.intro) / (K.quote - K.intro); const v = Math.floor(p * 58); c.textContent = v < 44 ? String(v + 1) : v < 48 ? '…?' : String(v - 40); c.setAttribute('opacity', 1); } else c.setAttribute('opacity', 0);
  // the pattern: twos and threes, again and again
  const pat = t >= K.quote + 2 && t < K.end, which = Math.floor(t / 1.2) % 2;
  document.querySelectorAll('.bk2').forEach(e => e.setAttribute('fill', pat && which === 0 ? '#e4572e' : '#26296b'));
  document.querySelectorAll('.bk3').forEach(e => e.setAttribute('fill', pat && which === 1 ? '#e4572e' : '#26296b'));
  // the low key and the high key ring in the cue
  for (let k = 0; k < 25; k++) S('wk' + k).setAttribute('fill', (t >= K.cue && t < K.cue + 1.3 && k === 0) || (t >= K.cue + 1.3 && t < K.cue + 2.6 && k === 24) ? '#ffd9a8' : '#fff');
  // Mozart's piano: the keyboard shrinks to about five octaves, then grows back
  const sh = t >= K.endBody && t < K.tease ? (t < K.endBody + 6 ? ph(t, K.endBody, K.endBody + 1.5) : 1 - ph(t, K.endBody + 6, K.endBody + 7.5)) : 0;
  S('kbd').setAttribute('transform', `translate(${150 * sh * .31} 0) scale(${1 - .31 * sh} 1)`);''')
# 3 Finger numbers: the bell board in the servants' hall; then the two hands
def bells():
    o = f'<g id="board"><rect x="400" y="120" width="480" height="210" rx="10" fill="#fff" stroke="{N}" stroke-width="5"/><text x="640" y="160" text-anchor="middle" font-family="Atkinson Hyperlegible,sans-serif" font-weight="700" font-size="18" letter-spacing="4" fill="#6d6f9c">THE BELL BOARD</text>'
    for k in range(5):
        x = 460 + k * 90
        o += f'<g id="bell{k}"><line x1="{x}" y1="180" x2="{x}" y2="200" stroke="{N}" stroke-width="3"/><path d="M{x - 22} 248 Q{x - 20} 202 {x} 200 Q{x + 20} 202 {x + 22} 248 Z" fill="{C}"/><circle cx="{x}" cy="254" r="6" fill="{N}"/></g><text id="bn{k}" x="{x}" y="304" text-anchor="middle" font-family="Playfair Display,serif" font-weight="900" font-size="32" fill="{N}">{k + 1}</text>'
    return o + '</g>'
R['hbr-L1'] = dict(n=3, title='Finger numbers', sub='The bell board', at=('K.intro+6', 'K.endBody+9'),
  parts=[wall(chand=False), floor(), plate(1010, 200, bigtext(0, 30, '1–5', 46, font='Playfair Display,serif', extra='font-weight="900"'), '1800s', 'London', '+ 1 2 3 4'), bells(),
         f'<g id="hands" opacity="0"><g transform="translate(330 70) scale(2.3)">{inner(ART["hand-L"])}</g><g transform="translate(660 70) scale(2.3)">{inner(ART["hand-R"])}</g></g>',
         bigtext(640, 312, '', 64, 'bign', 'Playfair Display,serif', C, 'font-weight="900"'), clara_stand(640, 'clara', 'both'), butler(900), door(), dim(), lone()],
  js=r'''
  const cyc = t >= K.intro + 4 && t < K.tryA ? Math.floor((t - K.intro - 4) / .9) % 5 : -1;
  let ring = cyc; if (t >= K.cue && t < K.cue + 3.2) ring = Math.min(4, Math.floor((t - K.cue) / .62));
  const KH = (F(/fingers, the Butler explains/) || {}).t0 || 1e9; const showHands = t >= KH && t < K.end; S('board').setAttribute('opacity', showHands ? 0 : 1); S('hands').setAttribute('opacity', showHands ? 1 : 0);
  for (let k = 0; k < 5; k++) { const b = S('bell' + k); b.style.transformBox = 'fill-box'; b.style.transformOrigin = 'center top'; b.setAttribute('transform', k === ring && !showHands ? `rotate(${18 * Math.sin(t * 22)})` : ''); S('bn' + k).setAttribute('fill', k === ring ? '#e4572e' : '#26296b'); }
  const bn = S('bign'); bn.textContent = ring >= 0 ? String(ring + 1) : ''; bn.setAttribute('opacity', showHands && ring >= 0 ? 1 : 0);
  // ending: the English way, a cross for the thumb, turns into 1 to 5
  const e = t >= K.endBody && t < K.tease; for (let k = 0; k < 5; k++) S('bn' + k).setAttribute('opacity', e ? 0 : 1); if (e) { bn.setAttribute('opacity', 1); bn.textContent = t < K.endBody + 7 ? '+ 1 2 3 4' : '1 2 3 4 5'; bn.setAttribute('font-size', 54); } else bn.setAttribute('font-size', 64);''')
# 4 The staff and the clefs: the Queen's floor and the King's floor
def grand():
    o = ''.join(f'<line x1="300" x2="940" y1="{130 + i * 16}" y2="{130 + i * 16}" stroke="{N}" stroke-width="3"/>' for i in range(5)) + ''.join(f'<line x1="300" x2="940" y1="{300 + i * 16}" y2="{300 + i * 16}" stroke="{N}" stroke-width="3"/>' for i in range(5))
    o += f'<line x1="300" x2="300" y1="130" y2="364" stroke="{N}" stroke-width="4"/>' + bigtext(336, 206, '𝄞', 104, 'tclef') + bigtext(336, 352, '𝄢', 66, 'bclef')
    o += f'<ellipse id="hiN" cx="640" cy="146" rx="16" ry="12" transform="rotate(-20 640 146)" fill="{C}" opacity="0"/><ellipse id="loN" cx="640" cy="348" rx="16" ry="12" transform="rotate(-20 640 348)" fill="{C}" opacity="0"/>'
    o += f'<g id="letters" opacity="0">' + bigtext(262, 210, 'G', 64, 'lg', 'Playfair Display,serif', C, 'font-weight="900"') + bigtext(262, 356, 'F', 64, 'lf', 'Playfair Display,serif', C, 'font-weight="900"') + '</g>'
    return f'<g id="gs">{o}</g>'
R['hbr-P2'] = dict(n=4, title='The staff and the clefs', sub='Two floors', at=('K.intro+4', 'K.endBody+6'),
  parts=[wall(chand=False, win=False), floor(), plate(1060, 200, bigtext(0, 26, '𝄞𝄢', 70), 'c. 1025', 'Arezzo', 'Guido’s lines'), grand(), piece('VIC_QUEEN', 190, 1.3, 240, 'queen'), piece('VIC_KING', 190, 1.25, 410, 'king'),
         clara_stand(640, 'clara'), butler(900), door(), dim(), lone()],
  js=r'''
  // the Queen and the King each claim a floor
  const mid = K.intro + (L0[0].t1 - K.intro) * .55, q = t >= K.intro && t < mid, k2 = t >= mid && t < L0[0].t1 + 1;
  S('queen').setAttribute('transform', `translate(190 ${240 - (q ? 8 * Math.abs(Math.sin(t * 6)) : 0)}) scale(1.3)`); S('king').setAttribute('transform', `translate(190 ${410 - (k2 ? 8 * Math.abs(Math.sin(t * 6)) : 0)}) scale(1.25)`);
  S('hiN').setAttribute('opacity', t >= K.cue && t < K.cue + 1.3 ? 1 : 0); S('loN').setAttribute('opacity', t >= K.cue + 1.3 && t < K.cue + 2.8 ? 1 : 0);
  // the signs at the start of each floor glow while their owner speaks
  S('tclef').setAttribute('fill', q ? '#e4572e' : '#26296b'); S('bclef').setAttribute('fill', k2 ? '#e4572e' : '#26296b');
  // ending: Guido's lines, and the clefs that began as letters
  const lt = t >= K.endBody + 4 && t < K.tease; S('letters').setAttribute('opacity', lt ? ph(t, K.endBody + 4, K.endBody + 5) : 0);''')
# 5 The beat: the hall clock's pendulum, a row of beats on the wall; ending: the metronome
def beatrow(): return '<g id="row">' + ''.join(f'<circle id="bt{k}" cx="{250 + k * 50}" cy="96" r="{20 if k % 4 == 0 else 14}" fill="#fff" stroke="{N}" stroke-width="3"/>' for k in range(8)) + f'<line x1="{250 + 3.5 * 50}" x2="{250 + 3.5 * 50}" y1="70" y2="122" stroke="{N}" stroke-width="4"/></g>'
def metronome(x=880): return f'<g id="metro" opacity="0"><path d="M{x - 50} 600 L{x - 22} 420 L{x + 22} 420 L{x + 50} 600 Z" fill="#fff" stroke="{N}" stroke-width="4"/><g id="marm"><line x1="{x}" y1="580" x2="{x}" y2="430" stroke="{N}" stroke-width="4"/><rect x="{x - 9}" y="470" width="18" height="16" fill="{C}"/></g></g>'
R['hbr-T1'] = dict(n=5, title='The beat', sub='The clock in the hall', at=('K.intro+5', 'K.endBody+3'),
  parts=[wall(chand=False), floor(), plate(1050, 210, bigtext(0, 26, '♩♩♩♩', 40), '1817', 'Vienna', 'the first metronome marks'), beatrow(), clock(700, 150), clara_stand(470, 'clara'), metronome(880), butler(930), door(), dim(), lone()],
  js=r'''
  const per = (t >= K.cue && t < K.cue + 5) ? .62 : 1.0, ph0 = t / per, sw = Math.sin(Math.PI * ph0);
  const pd = S('clockpd'); pd.setAttribute('transform', `rotate(${6 * sw} 700 262)`);
  const beat = Math.floor(ph0) % 8; for (let k = 0; k < 8; k++) S('bt' + k).setAttribute('fill', k === beat && t >= K.intro ? (k % 4 === 0 ? '#e4572e' : '#26296b') : '#fff');
  const mh = S('clockmh'); mh.setAttribute('transform', `rotate(${(t * 6) % 360} 700 204)`);
  S('clara').setAttribute('transform', `translate(0 ${-3 * Math.abs(Math.sin(Math.PI * ph0))})`);
  const me = t >= K.endBody && t < K.tease; S('metro').setAttribute('opacity', me ? ph(t, K.endBody, K.endBody + 1) : 0);
  S('marm').setAttribute('transform', `rotate(${me ? 22 * Math.sin(Math.PI * t / .75) : 0} 880 580)`); S('butler').setAttribute('opacity', me ? 0 : 1);''')
# 6 Crotchet and minim: one note gone in a tick, one that waits for two
R['hbr-T2'] = dict(n=6, title='Notes: crotchet and minim', sub='Two notes in the hall', at=('K.intro+5', 'K.endBody+4'),
  parts=[wall(win=False), floor(), plate(1010, 200, bigtext(-2, 40, MI, 110), '1300s', 'Paris', 'minima: the smallest'), clock(160, 200, 'ck'),
         bigtext(470, 440, CR, 300, 'crn'), bigtext(780, 440, MI, 300, 'mnm'),
         '<g id="c1">' + f'<circle id="cc0" cx="470" cy="500" r="20" fill="{C}"/>' + '</g><g id="c2">' + ''.join(f'<circle id="mc{k}" cx="{756 + k * 50}" cy="500" r="20" fill="{C}"/>' for k in range(2)) + '</g>',
         clara_stand(1040, 'clara'), door(), dim(), lone()],
  js=r'''
  const per = 1.0, b = Math.floor(t / per), f = (t / per) % 1;
  S('ckpd').setAttribute('transform', `rotate(${6 * Math.sin(Math.PI * t / per)} 160 312)`);
  // the crotchet hops on every beat and is gone; the minim holds for two
  S('crn').setAttribute('transform', `translate(0 ${-24 * Math.max(0, 1 - f * 3)})`); S('crn').setAttribute('opacity', .35 + .65 * Math.max(0, 1 - f * 1.4));
  const m2 = (t / per) % 2; S('mnm').setAttribute('opacity', m2 < 1.9 ? 1 : .4);
  S('cc0').setAttribute('opacity', f < .7 ? 1 : .25); S('mc0').setAttribute('opacity', m2 < 1 ? 1 : .35); S('mc1').setAttribute('opacity', m2 >= 1 ? 1 : .35);
  // ending: the minim was once among the shortest notes; it shrinks, then grows back to today's size
  const e = t >= K.endBody && t < K.tease, sh = e ? (t < K.endBody + 6 ? ph(t, K.endBody, K.endBody + 1.2) : 1 - ph(t, K.endBody + 6, K.endBody + 8)) : 0;
  S('mnm').setAttribute('font-size', 300 - 180 * sh);''')
# 7 Dotted minim and semibreve: the clock strikes four; Clara holds one note for the whole bar
def rings(): return ''.join(f'<circle id="rg{k}" cx="640" cy="330" r="60" fill="none" stroke="{C}" stroke-width="4" opacity="0"/>' for k in range(4))
R['hbr-T2-s2'] = dict(n=7, title='Notes: dotted minim and semibreve', sub='A note for the whole bar', at=('K.quote+1', 'K.endBody+5'),
  parts=[wall(win=False), floor(), plate(1010, 200, bigtext(0, 30, SB, 100), '1200s', 'Paris', 'breve · semibreve'), clock(300, 160, 'ck'), piano_front(640), stool(640), clara_sit(640, 'clara'), rings(),
         bigtext(640, 220, SB, 120, 'sbn'), ''.join(f'<circle id="sc{k}" cx="{565 + k * 50}" cy="252" r="16" fill="#fff" stroke="{C}" stroke-width="3"/>' for k in range(4)),
         bigtext(640, 250, '', 110, 'brv', 'NM', N), butler(900), door(), dim(), lone()],
  js=r'''
  const per = 1.0, hold = (t >= K.intro && t < K.tryA), b = hold ? Math.floor((t - K.intro) / per) % 4 : -1;
  S('ckpd').setAttribute('transform', `rotate(${6 * Math.sin(Math.PI * t / per)} 300 272)`);
  for (let k = 0; k < 4; k++) { S('sc' + k).setAttribute('fill', hold && k <= b ? '#e4572e' : '#fff');
    const p = ((t * .45) + k / 4) % 1, g = S('rg' + k); g.setAttribute('r', 60 + p * 260); g.setAttribute('opacity', hold ? (1 - p) * .8 : 0); }
  const e = t >= K.endBody && t < K.tease; S('brv').textContent = e ? '𝅜 = 𝅝 + 𝅝' : ''; S('sbn').setAttribute('opacity', e ? 0 : 1);
  for (let k = 0; k < 4; k++) S('sc' + k).setAttribute('opacity', e ? 0 : 1);''')
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
