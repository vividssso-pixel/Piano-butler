// ─── Phase 470: chapter 14 (Rhythm Patterns): the Lesson Book, built in full under Book rules 14 and 15 (her 2026-10-14
// 09:17 '계속 가줘 최종검토는 한꺼번에하게'). The level plan's scope for room 14 (Level 3): quaver groupings, the single
// quaver and the quaver rest, the dotted crotchet, starting before beat 1 (AMEB Grade 1; rule 13 puts the anacrusis
// here). Semiquavers and syncopation are the drill's extra levels. It builds on chapter 5 (two quavers on one beat,
// walk and run-ning, the dot on a minim) and chapter 8 (bars, 2/4 3/4 4/4, the hearts under the beats, a tie).
// Counting with + for 'and' (rule 12): 1 + 2 +; quarters 1 e + a. Every note sits on G, as in chapter 8.

// items: ['ts', top] | ['|'] | ['||'] | ['sp', px] | ['box', beats] | [kind]; kinds and their beats:
const SRH_LEN = { q: 1, h: 2, hd: 3, w: 4, qd: 1.5, e: 0.5, er: 0.5, p: 1, p4: 2, s4: 1, r: 1, hr: 2 };
const SRH_HEADS = { p: 2, p4: 4, s4: 4 };   // notes joined by a beam
const srhRest = (k) => k === 'r' || k === 'hr' || k === 'er';
const srhIsNote = (it) => SRH_LEN[it[0]] !== undefined || it[0] === 'box';
const srhLen = (it) => it[0] === 'box' ? it[1] : SRH_LEN[it[0]];
// the sounds (and rests) of a row: b (beats from its start), d (length), j (the item), h (which note of a group), rest
function srhSounds(items) {
  const out = []; let b = 0;
  items.forEach((it, j) => { if (!srhIsNote(it)) return;
    const k = it[0], n = SRH_HEADS[k] || 1, d = srhLen(it) / n;
    if (k !== 'box') for (let h = 0; h < n; h++) out.push({ b: b + h * d, d, j, h, rest: srhRest(k) });
    b += srhLen(it); });
  return out;
}
const srhBeats = (items) => items.reduce((a, it) => a + (srhIsNote(it) ? srhLen(it) : 0), 0);
const srhTop = (items) => { const ts = items.find(it => it[0] === 'ts'); return ts ? ts[1] : 4; };
// the count of a place in the bar (0 = beat 1): 1 2 3 4, + for a half, e and a for the quarters
const srhCount = (pos) => { const w = Math.floor(pos + 1e-6), f = Math.round((pos - w) * 4) / 4; return f === 0 ? String(w + 1) : f === 0.5 ? '+' : f === 0.25 ? 'e' : 'a'; };
// the room an item takes: in time, but never so tight that heads, flags or counts touch
const srhW = (k, len, D, wide) => k === 'box' ? Math.max(len * D, 34) : k === 'e' || k === 'er' ? Math.max(len * D, wide ? 38 : 34) : k === 'p' ? Math.max(D, wide ? 66 : 52) : k === 'p4' ? Math.max(2 * D, wide ? 132 : 104) : k === 's4' ? Math.max(D, 92) : k === 'qd' && wide ? 2 * D : len * D;
// a quaver rest: the blob, then the stroke down to the left
const srhQuaverRest = (x, y, col, k = 1) => '<circle cx="' + pFix(x - 2.6 * k) + '" cy="' + pFix(y - 6.6 * k) + '" r="' + pFix(3 * k) + '" fill="' + col + '"/><path d="M' + pFix(x - 3.4 * k) + ' ' + pFix(y - 4.6 * k) + ' Q' + pFix(x + 1.6 * k) + ' ' + pFix(y - 3.4 * k) + ' ' + pFix(x + 4.6 * k) + ' ' + pFix(y - 9 * k) + ' L' + pFix(x - 1 * k) + ' ' + pFix(y + 9.5 * k) + '" fill="none" stroke="' + col + '" stroke-width="' + pFix(2.1 * k) + '" stroke-linecap="round" stroke-linejoin="round"/>';
// heads with stems up joined by one beam (quavers) or two (semiquavers); cols: each note's colour
function srhGroup(xs, y, cols, beams = 1, ink = PEN_N) {
  const top = y - 34; let s = '';
  xs.forEach((x, i) => { s += nvbHead(x, y, 'q', cols[i], 1) + '<line x1="' + pFix(x + 6.4) + '" y1="' + pFix(y - 1.5) + '" x2="' + pFix(x + 6.4) + '" y2="' + pFix(top) + '" stroke="' + cols[i] + '" stroke-width="1.9"/>'; });
  const x1 = xs[0] + 5.5, x2 = xs[xs.length - 1] + 7.3;
  for (let b = 0; b < beams; b++) s += '<rect x="' + pFix(x1) + '" y="' + pFix(top - 0.2 + b * 8) + '" width="' + pFix(x2 - x1) + '" height="5.2" fill="' + ink + '"/>';
  return s;
}
// one row on the treble staff, every note on G. Under it: a heart on every beat, and the count (every beat, lighter
// while a note holds; a +, e or a under every note between beats; a rest's counts in dashed circles).
// o: D (pixels a beat), from (where in the bar the row starts, in beats: an anacrusis), lit (a sound, or a list, in
// coral), hl (an item in coral), ties [[a, b]], counts (false | 'blank' boxes | 'ans' answers in the boxes), hearts,
// marks (under each sound)
function srhRaw(yOf, items, o = {}) {
  const D = o.D || 44, G = (d) => yOf(d, 'treble'), col = o.ink || PEN_N, cor = PEN_C, y = G(32);
  const snd = srhSounds(items), litSet = new Set([].concat(o.lit == null ? [] : o.lit));
  const out = [], under = [], noteX = {}, soundX = [], bars = [], cells = [], beats = [];
  let x = o.x0 || 46, b = 0, barB = -(o.from || 0), last = 0;   // barB: the beat (from the row's start) where this bar began
  const line = (xx, w = 1.5) => '<line x1="' + pFix(xx) + '" x2="' + pFix(xx) + '" y1="' + pFix(G(38)) + '" y2="' + pFix(G(30)) + '" stroke="' + col + '" stroke-width="' + w + '"/>';
  items.forEach((it, j) => {
    const k = it[0];
    if (k === 'ts') { [[it[1], G(36)], [4, G(32)]].forEach(([n, yy]) => out.push('<text x="' + pFix(x + 8) + '" y="' + pFix(yy + 7.6) + '" text-anchor="middle" font-family="Playfair Display, Georgia, serif" font-size="25" font-weight="900" fill="' + col + '">' + n + '</text>')); x += 26; return; }
    if (k === '|') { out.push(line(x + 2)); bars.push(x + 2); last = x + 2.8; x += 12; barB = b; return; }
    if (k === '||') { out.push(line(x + 1, 1.3), line(x + 6, 4)); bars.push(x + 1); last = x + 8; x += 10; return; }
    if (k === 'sp') { x += it[1]; last = x; return; }
    const len = srhLen(it), w = k === 'box' && it[2] ? it[2] : srhW(k, len, D, o.wide), nx = x + 12, n = SRH_HEADS[k] || 1, step = w / n;
    const mine = snd.map((s, i) => [s, i]).filter(([s]) => s.j === j);
    const c = (h) => { const m = mine.find(([s]) => s.h === h); return o.hl === j || (m && litSet.has(m[1])) ? cor : col; };
    mine.forEach(([s, i]) => { soundX[i] = nx + s.h * step; });
    if (k === 'box') out.push('<rect x="' + pFix(x + 4) + '" y="' + pFix(G(39.4)) + '" width="' + pFix(w - 10) + '" height="' + pFix(G(28.6) - G(39.4)) + '" rx="3" fill="#fff" fill-opacity="0.7" stroke="' + cor + '" stroke-width="1.6" stroke-dasharray="4 3"/>');
    else if (SRH_HEADS[k]) out.push(srhGroup(mine.map(([, i]) => soundX[i]), y, mine.map(([s]) => c(s.h)), k === 's4' ? 2 : 1, o.hl === j ? cor : col));
    else if (k === 'r') out.push(nvbRest(nx + 2, G(34), 'q', { k: 0.82, col: c(0) }).svg);
    else if (k === 'er') out.push(srhQuaverRest(nx + 2, G(34), c(0)));
    else if (k === 'hr') out.push('<rect x="' + pFix(nx - 5) + '" y="' + pFix(G(34) - 5) + '" width="16" height="5" fill="' + c(0) + '"/>');
    else out.push(nvbNote(nx, y, k === 'hd' ? 'h' : k === 'qd' ? 'q' : k, { col: c(0) }).svg + (k === 'hd' || k === 'qd' ? '<circle cx="' + pFix(nx + 14) + '" cy="' + pFix(G(33)) + '" r="2.6" fill="' + c(0) + '"/>' : ''));
    noteX[j] = nx;
    if (k !== 'box') {
      mine.forEach(([s, i]) => cells.push({ x: soundX[i], tx: srhCount(s.b - barB), si: i, rest: s.rest, light: false }));
      // the beats a note holds through (lighter), or a rest lasts through (circled)
      for (let P = Math.ceil(b - barB - 1e-6); P < b + len - barB - 1e-6; P++) { const B = P + barB, at = mine.find(([s]) => Math.abs(s.b - B) < 1e-6), bx = at ? soundX[at[1]] : nx + (B - b) / len * w;
        beats.push(bx); if (!at) cells.push({ x: bx, tx: srhCount(P), si: -1, rest: srhRest(k), light: !srhRest(k) }); }
    }
    b += len; x += w;
  });
  if (!last) last = x;
  (o.ties || []).forEach(([a, bb]) => { const x1 = noteX[a] + 4, x2 = noteX[bb] - 4, yy = y + 7.5;
    out.push('<path d="M' + pFix(x1) + ' ' + pFix(yy) + ' Q' + pFix((x1 + x2) / 2) + ' ' + pFix(yy + 14) + ' ' + pFix(x2) + ' ' + pFix(yy) + '" fill="none" stroke="' + cor + '" stroke-width="2.2" stroke-linecap="round"/>'); });
  // the sound lines (o.lines): each note's sound as a line, from the note to the next one; a rest leaves a gap
  if (o.lines) snd.forEach((s, i) => { if (s.rest) return; const want = soundX[i] - 4 + s.d * (D - 8), bl = bars.find(v => v > soundX[i]), x2 = bl ? Math.min(want, bl - 7) : want;
    out.push('<line x1="' + pFix(soundX[i] - 4) + '" x2="' + pFix(x2) + '" y1="' + pFix(G(43)) + '" y2="' + pFix(G(43)) + '" stroke="' + cor + '" stroke-width="5" stroke-linecap="round"/>'); });
  const yH = G(30) + (o.dyH || 28), yC = yH + (o.dyC || 26);
  if (o.hearts !== false) beats.forEach(bx => under.push('<path d="M0 5 Q-7.5 -0.5 -5 -4.2 Q-2.4 -6.8 0 -3 Q2.4 -6.8 5 -4.2 Q7.5 -0.5 0 5 Z" transform="translate(' + pFix(bx) + ' ' + pFix(yH) + ') scale(1.45)" fill="' + cor + '" stroke="' + cor + '" stroke-width="0.83"/>'));
  if (o.counts !== false) {
    const xs = cells.map(cl => cl.x).sort((a, z) => a - z), gap = Math.min(40, ...xs.slice(1).map((v, i) => v - xs[i]));
    const bw = Math.max(15, Math.min(o.bw || 24, gap - 5));
    cells.forEach(cl => {
      const on = cl.si >= 0 && litSet.has(cl.si), dim = 'rgba(38,41,107,0.38)';
      if (o.counts === 'blank' || o.counts === 'ans') {
        under.push('<rect x="' + pFix(cl.x - bw / 2) + '" y="' + pFix(yC - 19) + '" width="' + pFix(bw) + '" height="26" rx="3" fill="' + (cl.light ? 'rgba(38,41,107,0.2)' : '#fff') + '" stroke="' + (o.counts === 'ans' ? cor : 'rgba(38,41,107,0.62)') + '" stroke-width="1.4"' + (cl.rest ? ' stroke-dasharray="4 3"' : '') + '/>');
        if (o.counts === 'ans') under.push('<text x="' + pFix(cl.x) + '" y="' + pFix(yC) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="15" font-weight="900" font-style="italic" fill="' + cor + '">' + cl.tx + '</text>');
        return;
      }
      if (cl.rest) under.push('<circle cx="' + pFix(cl.x) + '" cy="' + pFix(yC - 5.5) + '" r="10" fill="#fff" stroke="' + col + '" stroke-width="1.3" stroke-dasharray="3.2 2.6"/>');
      under.push('<text x="' + pFix(cl.x) + '" y="' + pFix(yC) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="15" font-weight="900" fill="' + (on ? cor : cl.light ? dim : col) + '">' + cl.tx + '</text>');
    });
  }
  if (o.marks) snd.forEach((s, i) => { const m = o.marks[i]; if (m) under.push('<text x="' + pFix(soundX[i]) + '" y="' + pFix(yC + 22) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="15" font-weight="900" fill="' + (m === '✓' ? PEN_G : cor) + '">' + m + '</text>'); });
  return { raw: out.join('') + under.join(''), noteX, soundX, bars, beats, end: x, last, snd };
}
const srhPadBottom = (o = {}) => o.hearts === false && o.counts === false ? 22 : (o.dyH || 28) + (o.dyC || 26) + (o.counts === 'blank' || o.counts === 'ans' ? 9 : 12) + (o.marks ? 24 : 0);
// a staff with one row: SfStaff draws the lines and the clef, srhRaw the rest. width: the width that fills the picture,
// so every staff of a page has one scale
function SrhStaff({ items, width = 400, o = {}, label, pad, extra, full, k }) {   // k: a set scale (px a unit), never wider than the box
  const m = srhRaw((d) => dY(d), items, o), vbw = Math.ceil(m.last + 6);
  return <div style={k ? {width:Math.round(vbw * k),maxWidth:'100%'} : {width:full ? '100%' : Math.min(100, vbw / width * 100) + '%'}}><SfStaff clef="treble" width={vbw} span={[4, m.last]} pad={pad || [extra ? 34 : 16, srhPadBottom(o)]} label={label}
    extra={(yOf, layer, txt) => layer === 'over' && <g><g dangerouslySetInnerHTML={{ __html: srhRaw(yOf, items, o).raw }}/>{extra && extra(yOf, txt, srhRaw(yOf, items, o))}</g>}/></div>;
}

// the chapter's rhythms (none of them a song), shared with the screen and the Workbook
const SRH_ROWS = {
  pairs: [['ts', 4], ['p'], ['p'], ['q'], ['q'], ['||']],
  l2: [['ts', 4], ['p'], ['p'], ['q'], ['q'], ['|'], ['p4'], ['q'], ['q'], ['||']],
  four: [['ts', 4], ['p4'], ['q'], ['q'], ['||']],
  fourB: [['ts', 4], ['q'], ['q'], ['p4'], ['||']],
  wrong: [['ts', 4], ['q'], ['p4'], ['q'], ['||']],
  right: [['ts', 4], ['q'], ['p'], ['p'], ['q'], ['||']],
  three: [['ts', 3], ['p'], ['p'], ['q'], ['||']],
  alone: [['ts', 4], ['q'], ['er'], ['e'], ['q'], ['er'], ['e'], ['||']],
  aloneB: [['ts', 2], ['e'], ['er'], ['q'], ['||']],
  dot: [['ts', 4], ['qd'], ['e'], ['h'], ['||']],
  dotB: [['ts', 4], ['qd'], ['e'], ['qd'], ['e'], ['||']],
  dot3: [['ts', 3], ['qd'], ['e'], ['q'], ['||']],
  up4: [['ts', 4], ['q'], ['|'], ['q'], ['q'], ['q'], ['q'], ['|'], ['h'], ['q'], ['||']],
  up3: [['ts', 3], ['q'], ['|'], ['h'], ['q'], ['|'], ['h'], ['||']],
  upP: [['ts', 4], ['p'], ['|'], ['q'], ['q'], ['h'], ['|'], ['hd'], ['||']],
  mix4: [['ts', 4], ['qd'], ['e'], ['p'], ['q'], ['|'], ['p4'], ['h'], ['||']],
  mix3: [['ts', 3], ['q'], ['|'], ['qd'], ['e'], ['q'], ['|'], ['p'], ['er'], ['e'], ['q'], ['|'], ['h'], ['||']],
  mix2: [['ts', 2], ['q'], ['er'], ['e'], ['|'], ['qd'], ['e'], ['|'], ['p'], ['q'], ['||']],
};
const SRH_FROM = { up4: 3, up3: 2, upP: 3, mix3: 2 };   // where an anacrusis starts in its bar (beats)
// the middle of a 4/4 bar: halfway between the last sound before beat 3 and the sound on beat 3
const srhMid = (m) => { const z = m.snd.findIndex(s => Math.abs(s.b - 2) < 1e-6), a = z - 1; return (m.soundX[a] + m.soundX[z]) / 2 + 3.2; };

function srhLbPages(scr = false) {
  const ch = 'rhythm', fs = scr ? 1.3 : 1;
  const live = (still, comp) => <LbLive still={still} live={<>{still}{comp}</>}/>;
  const pic = (node, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{node}</div></LbPic>;
  const stack = (nodes, h, gap = 10) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap,width:'fit-content',maxWidth:'100%',margin:'0 auto'}}>{nodes}</div></LbPic>;
  const above = (yOf) => yOf(40, 'treble') - 6;
  const T = (x, s, yOf, txt, c = PEN_C, a = 'middle') => <text x={x} y={above(yOf)} textAnchor={a} fontSize={11.5 * fs} fontWeight="900" fill={c} style={txt}>{s}</text>;
  const tag = (x, s, c = PEN_C, a = 'start') => (yOf, txt) => T(x, s, yOf, txt, c, a);
  const tags = (...fs2) => (yOf, txt, m) => <g>{fs2.map((f, i) => <g key={i}>{f(yOf, txt, m)}</g>)}</g>;
  // a line the steps name: its number in a small square beside the staff
  const lineNo = (n) => <span style={{flex:'0 0 auto',width:20,height:20,display:'flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:12.5,fontWeight:800,lineHeight:1,...vicSquare(n - 1)}}>{n}</span>;
  const numbered = (n, node) => <div key={'n' + n} style={{display:'flex',alignItems:'center',gap:8,minWidth:0}}>{lineNo(n)}<div style={{flex:'0 1 auto',minWidth:0,display:'flex'}}>{node}</div></div>;
  const row = (key, k, D, extra, label, oo = {}) => <SrhStaff key={key} k={k} items={SRH_ROWS[key]} o={{ D, from: SRH_FROM[key] || 0, ...oo }} extra={extra} label={label}/>;
  const nb = (x) => x.replace(/ /g, ' ');
  const sp = (x) => x.replace(/ /g, ' ');   // a count in a picture: its marks well apart
  const KO_N = (x) => x.replace(/ 번\./g, ' 번.');   // '네 번.' never split
  // the middle of the bar, dashed; ok: the beams stop there (✓) or cross it (✗)
  const mid = (ok) => (yOf, txt, m) => { const xm = srhMid(m); return <g>
    <line x1={xm} x2={xm} y1={above(yOf) + 6} y2={yOf(29, 'treble')} stroke={ok ? PEN_G : PEN_C} strokeWidth="1.6" strokeDasharray="4 3"/>
    {T(xm, ok ? t('✓ beams stop at the middle', '✓ 빔이 한가운데에서 끝나요') : t('✗ a beam crosses the middle', '✗ 빔이 한가운데를 넘어요'), yOf, txt, ok ? PEN_G : PEN_C)}</g>; };

  // p1: two bars with every new sight; above them a line for each sound, as long as the sound, and a gap for the rest
  const w1 = (yOf, txt) => (x, str) => <text x={x} y={yOf(43, 'treble') - 12} textAnchor="middle" fontSize={12.5 * fs} fontWeight="900" fill={PEN_C} style={txt}>{str}</text>;
  const p1 = stack([
    <SrhStaff key="b1" k={1.15} items={[['ts', 4], ['p4'], ['er'], ['e'], ['q'], ['|']]} o={{ D: 46, lines: true }} pad={[56, 62]}
      extra={(yOf, txt, m) => { const w = w1(yOf, txt); return <g>{w((m.soundX[0] + m.soundX[3]) / 2, t('short', '짧게'))}{w(m.soundX[4] + 2, t('silence', '쉼'))}{w(m.soundX[6] + 16, t('long', '길게'))}</g>; }}
      label={t('A bar of 4/4 on G: four quavers joined by a beam, a quaver rest and a quaver, a crotchet. Above it, a line for each sound, as long as the sound, and a gap for the rest. The count under it: 1 + 2 + (3) + 4.', '4/4 한 마디, 모두 G: 빔으로 이어진 8분음표 넷, 8분쉼표와 8분음표, 4분음표. 위에는 소리마다 그 길이만큼의 줄, 쉼표에는 빈칸. 아래에 세는 법: 1 + 2 + (3) + 4.')}/>,
    <SrhStaff key="b2" k={1.15} items={[['qd'], ['e'], ['h'], ['||']]} o={{ D: 46, lines: true }} pad={[56, 62]}
      extra={(yOf, txt, m) => { const w = w1(yOf, txt); return <g>{w((m.soundX[0] + m.soundX[1]) / 2 + 6, t('long, short', '길게, 짧게'))}{w(m.soundX[2] + 32, t('longer', '더 길게'))}</g>; }}
      label={t('The next bar: a dotted crotchet and a quaver, then a minim, with their sound lines: long, short, longer. Counted 1 2 + 3 4.', '다음 마디: 점4분음표와 8분음표, 그다음 2분음표, 그리고 소리 줄: 길게, 짧게, 더 길게. 1 2 + 3 4로 세요.')}/>,
  ], 200, 4);

  // p2: line 1, quavers grouped by the beat and four over half a bar; then the middle of a 4/4 bar, crossed (✗) and kept (✓, line 2)
  const p2 = stack([
    numbered(1, row('l2', 1.25, 44, tags(tag(66, t('two quavers: one beat', '8분음표 둘: 한 박')), (yOf, txt, m) => T(m.bars[0] + 12, t('four quavers: half the bar', '8분음표 넷: 마디의 반'), yOf, txt, PEN_C, 'start')),
      t('Line 1, two bars of 4/4. Bar 1: two quavers, two quavers, two crotchets. Bar 2: four quavers under one beam, two crotchets. Counted 1 + 2 + 3 4, 1 + 2 + 3 4.', '1번 줄, 4/4 두 마디. 첫 마디: 8분음표 둘, 8분음표 둘, 4분음표 둘. 둘째 마디: 빔 하나에 8분음표 넷, 4분음표 둘. 1 + 2 + 3 4, 1 + 2 + 3 4로 세요.'))),
    <div key="wr" style={{display:'flex',gap:18,alignItems:'center',flexWrap:'wrap',justifyContent:'center'}}>
      <div style={{display:'flex',paddingLeft:28,maxWidth:'100%',boxSizing:'border-box',minWidth:0}}>{row('wrong', 1.2, 44, mid(false), t('A wrong bar of 4/4: a crotchet, four quavers under one beam across the middle of the bar, a crotchet.', '틀린 4/4 한 마디: 4분음표, 마디 한가운데를 넘어 빔으로 이은 8분음표 넷, 4분음표.'), { counts: false, hearts: false })}</div>
      {numbered(2, row('right', 1.2, 44, mid(true), t('Line 2, the same bar written right: a crotchet, two quavers, two quavers, a crotchet. No beam crosses the middle.', '2번 줄, 바르게 쓴 같은 마디: 4분음표, 8분음표 둘, 8분음표 둘, 4분음표. 한가운데를 넘는 빔이 없어요.'), { counts: false, hearts: false }))}
    </div>,
  ], 330, 18);

  // p3: a quaver alone has a flag; a quaver rest is half a beat of silence
  const p3 = stack([
    numbered(1, row('alone', 1.45, 48, tags((yOf, txt, m) => T(m.noteX[2] + 2, t('quaver rest', '8분쉼표'), yOf, txt), (yOf, txt, m) => T(m.noteX[6] + 12, t('flag', '꼬리'), yOf, txt)),
      t('Line 1, a bar of 4/4: a crotchet; a quaver rest and a quaver with a flag; a crotchet; a quaver rest and a quaver. Counted 1 (2) + 3 (4) +.', '1번 줄, 4/4 한 마디: 4분음표; 8분쉼표와 꼬리 달린 8분음표; 4분음표; 8분쉼표와 8분음표. 1 (2) + 3 (4) +로 세요.'))),
    numbered(2, row('aloneB', 1.45, 48, null, t('Line 2, a bar of 2/4: a quaver with a flag and a quaver rest, then a crotchet. Counted 1 (+) 2.', '2번 줄, 2/4 한 마디: 꼬리 달린 8분음표와 8분쉼표, 그다음 4분음표. 1 (+) 2로 세요.'))),
  ], 270, 8);

  // p4: the dotted crotchet: a crotchet tied to a quaver is one and a half beats; then long, short
  const p4a = <div key="tie" style={{display:'flex',paddingLeft:28,maxWidth:'100%',boxSizing:'border-box',minWidth:0}}><SrhStaff k={1.2} items={[['q'], ['e'], ['sp', 34], ['qd'], ['sp', 14]]} o={{ D: 56, counts: false, hearts: false, ties: [[0, 1]] }} pad={[34, 24]}
    label={t('A crotchet and a quaver tied together last as long as a dotted crotchet: one and a half beats.', '붙임줄로 이은 4분음표와 8분음표는 점4분음표와 길이가 같아요: 한 박 반.')}
    extra={(yOf, txt, m) => <g>
      <text x={(m.noteX[1] + m.noteX[3]) / 2 + 12} y={yOf(34, 'treble') + 7} textAnchor="middle" fontSize={24} fontWeight="900" fill={PEN_N} style={txt}>=</text>
      {T(m.noteX[0] + 2, t('1 beat', '한 박'), yOf, txt)}{T(m.noteX[1] + 10, t('½ beat', '반 박'), yOf, txt)}{T(m.noteX[3] + 6, t('1½ beats', '한 박 반'), yOf, txt)}</g>}/></div>;
  const p4 = stack([p4a,
    numbered(1, row('dot', 1.2, 48, tag(66, sp(t('long, short: 1 2 +', '길게, 짧게: 1 2 +'))), t('Line 1, a bar of 4/4: a dotted crotchet and a quaver, then a minim. Counted 1 2 + 3 4, the 2 lighter: the dotted crotchet holds through it.', '1번 줄, 4/4 한 마디: 점4분음표와 8분음표, 그다음 2분음표. 1 2 + 3 4로 세요. 2는 흐리게: 점4분음표가 그동안 이어져요.'))),
    numbered(2, row('dot3', 1.2, 48, null, t('Line 2, a bar of 3/4: a dotted crotchet and a quaver, then a crotchet. Counted 1 2 + 3.', '2번 줄, 3/4 한 마디: 점4분음표와 8분음표, 그다음 4분음표. 1 2 + 3으로 세요.'))),
  ], 330, 6);

  // p5: starting before beat 1: the short first bar and the short last bar make one full bar
  const ends = (first, lastN) => (yOf, txt, m) => <g>{T(m.noteX[1], first, yOf, txt)}{T((m.bars[1] + m.last) / 2, lastN, yOf, txt)}</g>;
  const p5 = stack([
    numbered(1, row('up4', 1.4, 40, ends(t('beat 4', '넷째 박'), t('3 beats', '세 박')), t('Line 1, a tune in 4/4 that starts on beat 4: one crotchet before the first bar line; a full bar of four crotchets; then a last bar of three beats, a minim and a crotchet. The short first bar and the short last bar make one full bar.', '1번 줄, 넷째 박에서 시작하는 4/4 선율: 첫 세로줄 앞에 4분음표 하나; 4분음표 넷의 갖춘마디; 마지막은 2분음표와 4분음표, 세 박의 짧은 마디. 짧은 첫 마디와 짧은 마지막 마디를 합치면 갖춘마디 하나가 돼요.'))),
    numbered(2, row('up3', 1.4, 40, ends(t('beat 3', '셋째 박'), t('2 beats', '두 박')), t('Line 2, a tune in 3/4 that starts on beat 3: one crotchet; a full bar, a minim and a crotchet; a last bar of two beats, a minim.', '2번 줄, 셋째 박에서 시작하는 3/4 선율: 4분음표 하나; 갖춘마디(2분음표와 4분음표); 마지막은 2분음표, 두 박의 짧은 마디.'))),
  ], 300, 10);

  // p6: lines to read: line 1 with its count, line 2 for the child to count
  const p6 = stack([
    numbered(1, row('mix4', 1.12, 42, null, t('Line 1, two bars of 4/4: a dotted crotchet and a quaver, two quavers, a crotchet; four quavers and a minim. Counted 1 2 + 3 + 4, then 1 + 2 + 3 4.', '1번 줄, 4/4 두 마디: 점4분음표와 8분음표, 8분음표 둘, 4분음표; 8분음표 넷과 2분음표. 1 2 + 3 + 4, 그다음 1 + 2 + 3 4로 세요.'))),
    numbered(2, row('mix3', 1.12, 42, null, t('Line 2, a tune in 3/4 that starts on beat 3, with no count written under it: a crotchet; a dotted crotchet, a quaver and a crotchet; two quavers, a quaver rest and a quaver, a crotchet; a last bar of a minim.', '2번 줄, 셋째 박에서 시작하는 3/4 선율, 아래에 세는 법은 없어요: 4분음표; 점4분음표, 8분음표, 4분음표; 8분음표 둘, 8분쉼표와 8분음표, 4분음표; 마지막은 2분음표.'), { counts: false })),
    numbered(3, row('mix2', 1.12, 42, null, t('Line 3, three bars of 2/4, with no count written under them: a crotchet, a quaver rest and a quaver; a dotted crotchet and a quaver; two quavers and a crotchet.', '3번 줄, 2/4 세 마디, 아래에 세는 법은 없어요: 4분음표, 8분쉼표와 8분음표; 점4분음표와 8분음표; 8분음표 둘과 4분음표.'), { counts: false })),
  ], 300, 10);

  // the check icons
  const ic = {
    beam: [{ k: 'raw', svg: srhGroup([14, 32, 50, 68], 37, [PEN_N, PEN_N, PEN_N, PEN_N]) }],
    rest: [{ k: 'raw', svg: srhQuaverRest(30, 22, PEN_N, 1.1) + nvbNote(52, 37, 'e', { col: PEN_C }).svg }],
    dot: [{ k: 'raw', svg: nvbNote(24, 37, 'q', { col: PEN_N }).svg + '<circle cx="38" cy="34" r="3" fill="' + PEN_C + '"/>' + nvbNote(58, 37, 'e', { col: PEN_N }).svg }],
    up: [{ k: 'raw', svg: nvbNote(14, 37, 'q', { col: PEN_C }).svg + '<line x1="34" x2="34" y1="4" y2="39" stroke="' + PEN_N + '" stroke-width="1.8"/>' + nvbNote(48, 37, 'q', { col: PEN_N }).svg + nvbNote(70, 37, 'q', { col: PEN_N }).svg }],
    read: [{ k: 'raw', svg: ['1', '2', '+', '3'].map((s, i) => '<text x="' + (16 + i * 20) + '" y="28" text-anchor="middle" font-family="Inter, sans-serif" font-size="18" font-weight="900" fill="' + (s === '+' ? PEN_C : PEN_N) + '">' + s + '</text>').join('') }],
  };
  const checksRows = [
    ['beam', t('I can count quavers in their beats, 1 + 2 +, and say how a beam groups them', '8분음표를 박에 맞춰 세고(1 + 2 +), 빔이 8분음표를 어떻게 묶는지 말할 수 있어요')],
    ['rest', t('I can play a quaver alone and count a quaver rest', '혼자 있는 8분음표를 치고 8분쉼표를 셀 수 있어요')],
    ['dot', t('I can play a dotted crotchet and a quaver: 1 2 +', '점4분음표와 8분음표를 칠 수 있어요: 1 2 +')],
    ['up', t('I can count in, count the missing beats, then start a tune before beat 1', '한 마디를 미리 세고 모자란 박도 센 다음, 첫 박보다 먼저 시작하는 선율을 칠 수 있어요')],
    ['read', t('I can count a new rhythm out loud, then clap it and play it', '새 리듬을 소리 내어 센 다음, 손뼉으로 치고 피아노로 칠 수 있어요')],
  ];

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <><b>리듬</b>은 길고 짧은 소리와 쉼의 무늬예요.</> : <><b>Rhythm</b> is the pattern of long and short sounds and silences.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Grouping quavers', '8분음표 묶기'), 2], [t('A quaver alone', '혼자 있는 8분음표'), 3], [t('The dotted crotchet', '점4분음표'), 4], [t('Before beat 1', '첫 박보다 먼저'), 5], [t('Count, clap, play', '세기, 손뼉 치기, 피아노 치기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I can /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Grouping quavers', '8분음표 묶기')}>
      {live(p2, <SrhPad page={2}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['8분음표', '반 박. 둘이면 한 박: 1 +.'],
        ['빔', '8분음표를 잇는 굵은 줄. 한 박의 8분음표끼리 이어요. 4/4에서는 첫째~둘째 박이나 셋째~넷째 박의 8분음표 넷을 이을 수도 있어요.'],
        ['마디 한가운데', '4/4에서 둘째 박과 셋째 박 사이. 빔은 이곳을 넘지 않아요.'],
      ] : [
        ['quaver', 'Half a beat. Two make one beat: 1 +. Its other name is an eighth note.'],
        ['beam', 'The thick line that joins quavers. It joins the quavers of one beat; in 4/4 it may join four, on beats 1 and 2 or on beats 3 and 4.'],
        ['the middle of the bar', 'In 4/4, between beats 2 and 3. A beam never crosses it.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        KO_N('오른손 3번 손가락, G: ' + nb('1 + 2 + 3 4') + '를 소리 내어 세면서 1번 줄을 쳐요. 네 번.'),
        KO_N('2번 줄: ' + nb('1 2 + 3 + 4') + '를 세면서 쳐요. 네 번.'),
      ] : [
        <>Right hand, finger 3 on G: play line 1, counting {nb('1 + 2 + 3 4')} out loud. Four times round.</>,
        <>Line 2: play it, counting {nb('1 2 + 3 + 4')}. Four times round.</>,
      ]}/>
      <LbRemember>{t('Beams group quavers by the beat: 1 +, 2 +.', '빔은 8분음표를 박마다 묶어요: 1 +, 2 +.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('A quaver alone', '혼자 있는 8분음표')}>
      {live(p3, <SrhPad page={3}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['꼬리', '혼자 있는 8분음표의 기둥에 달린 작은 깃. 묶인 8분음표에는 꼬리 대신 빔이 있어요.'],
        ['8분쉼표', '반 박 동안의 쉼. 쉬는 동안에도 세요.'],
      ] : [
        ['flag', 'The small tail on the stem of a quaver that stands alone. Grouped quavers have a beam instead.'],
        ['quaver rest', 'Half a beat of silence. Keep counting through it. Its other name is an eighth rest.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        KO_N('오른손 3번 손가락, G: 1번 줄을 쳐요. 쉼표에서는 손을 건반 바로 위로 들고, 이렇게 세요: ' + nb('1 (2) + 3 (4) +') + '. 네 번.'),
        KO_N('2번 줄: 1에서 짧게 치고, +에서 쉬어요. 이렇게 세요: ' + nb('1 (+) 2') + '. 네 번.'),
      ] : [
        <>Right hand, finger 3 on G: play line 1. On a rest, lift your hand just above the key and count {nb('1 (2) + 3 (4) +')}. Four times round.</>,
        <>Line 2: play short on 1, rest on the +. Count {nb('1 (+) 2')}, four times round.</>,
      ]}/>
      <LbRemember>{t('A flag: a quaver alone. A quaver rest: half a beat of silence.', '꼬리: 혼자 있는 8분음표. 8분쉼표: 반 박 쉬기.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The dotted crotchet', '점4분음표')}>
      {live(p4, <SrhPad page={4}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['점4분음표', '점이 붙은 4분음표: 한 박 반. 점은 음표 길이의 반을 더해요.'],
        ['점4분음표와 8분음표', '길게, 짧게. 1에서 치고 2까지 누르고 있다가, 2 다음 +에서 8분음표를 쳐요: 1 2 +.'],
      ] : [
        ['dotted crotchet', 'A crotchet with a dot: one and a half beats. The dot adds half the note’s length. Its other name is a dotted quarter note.'],
        ['dotted crotchet and quaver', 'Long, short. Play on 1, hold through 2, then the quaver on the + after 2: 1 2 +.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        KO_N('오른손 3번 손가락, G: ' + nb('1 2 + 3 4') + '로 세면서 1번 줄을 쳐요. 2에서도 떼지 말고 누르고 있어요. 네 번.'),
        KO_N('2번 줄(3/4): ' + nb('1 2 + 3') + '으로 세면서 쳐요. 네 번.'),
      ] : [
        <>Right hand, finger 3 on G: play line 1, counting {nb('1 2 + 3 4')}. Hold through 2. Four times round.</>,
        <>Line 2 (3/4): count {nb('1 2 + 3')}, four times round.</>,
      ]}/>
      <LbRemember>{t('A dotted crotchet: one and a half beats. Long, short: 1 2 +.', '점4분음표: 한 박 반. 길게, 짧게: 1 2 +.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Before beat 1', '첫 박보다 먼저')}>
      {live(p5, <SrhPad page={5}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['여린내기', '첫 박보다 먼저 시작하기.'],
        ['못갖춘마디', '박자표보다 박이 모자란 마디. 여린내기로 시작한 선율은 보통 마지막 마디도 못갖춘마디예요: 첫 마디와 합치면 갖춘마디 하나가 돼요.'],
        ['미리 세기', '치기 전에 소리 내어 세는 한 마디. 여린내기 앞에서는 모자란 박까지 세요. 다른 이름은 예비박이에요.'],
      ] : [
        ['anacrusis', 'Notes before the first full bar: the tune starts before beat 1. Its other names are upbeat and pick-up.'],
        ['incomplete bar', 'A bar with fewer beats than the time signature. A tune with an anacrusis usually ends with one too: with the first bar, it makes one full bar.'],
        ['count-in', 'One bar counted out loud before you play. Before an anacrusis, count the missing beats too.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        KO_N('1번 줄: 미리 ' + nb('1 2 3 4') + ', 그다음 ' + nb('1 2 3') + '을 소리 내어 세고, 4에서 G를 쳐요. 그다음 이어서 쳐요. 네 번.'),
        KO_N('2번 줄(3/4): 미리 ' + nb('1 2 3') + ', 그다음 ' + nb('1 2') + '를 세고 3에서 시작해요. 네 번.'),
      ] : [
        <>Line 1: count in {nb('1 2 3 4')}, then {nb('1 2 3')}, out loud. Play G on 4 and carry on. Four times round.</>,
        <>Line 2 (3/4): count in {nb('1 2 3')}, then {nb('1 2')}, and start on 3. Four times round.</>,
      ]}/>
      <LbRemember>{t('Before beat 1: count the missing beats, then start.', '첫 박보다 먼저: 모자란 박을 세고 시작해요.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Count, clap, play', '세기, 손뼉 치기, 피아노 치기')}>
      {live(p6, <SrhPad page={6}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['리듬 읽기', '치기 전에 세는 법을 찾아 소리 내어 말하기.'],
      ] : [
        ['reading a rhythm', 'Finding its count and saying it out loud before you play.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        KO_N('1번 줄: 소리 내어 세고, 손뼉으로 치고, G에서 피아노로 쳐요. 두 번.'),
        KO_N('2번 줄: 세는 법을 찾아요. 미리 ' + nb('1 2 3') + ', 그다음 ' + nb('1 2') + '를 세고 3에서 시작해요. 세고, 손뼉 치고, 피아노로 쳐요. 두 번.'),
        KO_N('3번 줄(2/4): 세는 법을 찾아 세고, 손뼉 치고, 피아노로 쳐요. 두 번.'),
      ] : [
        <>Line 1: count it out loud, clap it, then play it on G. Twice.</>,
        <>Line 2: find its count. Count in {nb('1 2 3')}, then {nb('1 2')}, and start on 3. Count it, clap it, play it. Twice.</>,
        <>Line 3 (2/4): find its count, then count it, clap it, play it. Twice.</>,
      ]}/>
      <LbRemember>{t('Count it, clap it, play it.', '세고, 손뼉 치고, 피아노로 쳐요.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_srh_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, x])}/>}/>
    </LbPage>,
  ];
}
function RhythmLessonBook() { return <>{srhLbPages(false)}</>; }
