// ─── Phase 481: chapter 25, Melody & Phrasing: the tune, its staves, the map (page 1) and the Lesson Book ───
// Notes are [kind, beats, d] (d: 28 = middle C, a step a number), the same as chapters 10 and 24.
const mlxName = dName;
const mlxQ = (ds) => ds.map(d => ['q', 1, d]);
// the tune of page 1: a question (bars 1 to 4: the motif, then two sequences a step higher each, resting on G) and an
// answer (bars 5 to 8: the motif repeated and its sequence, then down to C, the tonic). The high point: the A in bar 3.
const MLX_TUNE = [mlxQ([28, 30, 29, 31]), mlxQ([29, 31, 30, 32]), mlxQ([30, 32, 31, 33]), [['w', 4, 32]], mlxQ([28, 30, 29, 31]), mlxQ([29, 31, 30, 32]), mlxQ([31, 29, 30, 29]), [['w', 4, 28]]];
const MLX_Q = MLX_TUNE.slice(0, 4), MLX_A = MLX_TUNE.slice(4);
// what each bar of the tune is: the motif, a repetition, a sequence (a step up), or something else
const MLX_ROLE = ['motif', 'up', 'up', 'rest', 'rep', 'up', 'end', 'rest'];
const mlxFlat = (bars) => bars.flat();
const mlxCount = (bars) => bars.reduce((a, b) => a + b.length, 0);
const mlxHigh = (bars) => { const ns = mlxFlat(bars); let hi = 0; ns.forEach((n, i) => { if (n[2] > ns[hi][2]) hi = i; }); return hi; };
// note index ranges of each bar
const mlxBarRanges = (bars) => { let k = 0; return bars.map(b => { const a = k; k += b.length; return [a, k - 1]; }); };
// staff items for a row of bars: bar lines between bars, the final bar line at the end (end: false, a single one);
// tsRoom: the time signature's room on rows without it; gap: room before each bar line on small staves
const mlxGap = fmxGap;
// the width of a bar of four crotchets (an empty bar is drawn this wide)
const mlxBarW = (D) => sdyVbw([['ts', 4]].concat(mlxQ([28, 30, 29, 31]), [['|']]), { D }) - sdyVbw([['ts', 4], ['|']], { D });
const mlxItems = (bars, o = {}) => { const items = o.ts ? [['ts', 4]] : o.tsRoom ? [['sp', 26]] : [], n = bars.length + (o.empty || 0);
  bars.forEach((bar, b) => { bar.forEach(x => items.push(x)); if (o.gap) items.push(['sp', o.gap]); items.push(b === n - 1 && o.end !== false ? ['||'] : ['|']); });
  for (let j = bars.length; j < n; j++) items.push(['sp', mlxBarW(o.D || 26) - 12], ['sp', o.gap || 0], j === n - 1 && o.end !== false ? ['||'] : ['|']);
  return items; };
const mlxVbw = (bars, ts, D = 26, tsRoom, empty = 0) => sdyVbw(mlxItems(bars, { ts, tsRoom, gap: mlxGap(D), empty, D }), { D });

// ── the sound: one at a time; a sound started while another plays (or a pad that closes) ends the other properly ──
let _mlxT = [], _mlxEnd = null;
const MLX_BPM = 112;
const mlxStop = () => { _mlxT.forEach(clearTimeout); _mlxT = []; stopClicks(); const e = _mlxEnd; _mlxEnd = null; if (e) e(); };
// notes [{ d, dur, vol, lift }]: lift shortens a note (a breath after it); onStep(i) as each sounds, -1 at the end
function mlxRun(notes, onStep, bpm = MLX_BPM) {
  mlxStop(); const ctx = getAudio(); if (!ctx) { if (onStep) onStep(-1); return; }
  const spb = 60 / bpm, t0 = ctx.currentTime + 0.1; let tt = 0;
  const end = () => { if (_mlxEnd === end) _mlxEnd = null; if (onStep) onStep(-1); };
  _mlxEnd = end;
  notes.forEach((n, i) => {
    blip(ctx, t0 + tt * spb, sskHz(n.d), n.dur * spb * (n.lift ? 0.55 : 0.94), n.vol || 0.17, 'triangle');
    if (onStep) _mlxT.push(setTimeout(() => onStep(i), (0.1 + tt * spb) * 1000));
    tt += n.dur;
  });
  _mlxT.push(setTimeout(end, (0.1 + tt * spb) * 1000 + 150));
}
const mlxNotes = (bars) => mlxFlat(bars).map(n => ({ d: n[2], dur: n[1] }));
// a phrase played shaped: growing to its high point, softer to its end, a lift after the last note
const mlxShaped = (bars) => { const ns = mlxNotes(bars), hi = mlxHigh(bars), n = ns.length;
  return ns.map((x, i) => ({ ...x, vol: i <= hi ? 0.1 + 0.13 * (i / Math.max(1, hi)) : 0.23 - 0.13 * ((i - hi) / Math.max(1, n - 1 - hi)), lift: i === n - 1 })); };
const mlxFlatPlay = (bars) => mlxNotes(bars).map(x => ({ ...x, vol: 0.17 }));

// ── one system of bars on the treble staff. line: the tune's line drawn above it (its high point coral when hiCoral);
// marks: phrase marks (bar ranges); hair: hairpins [[note a, note b, 'cresc' | 'dim']]; hl: notes drawn coral;
// motifs: brackets over bars [[bar, label, coral]]; breath: a breath mark after the last note; n0: the first bar's number;
// tag: '?' or '.' names the phrase (question, answer) in a word over its last note; ring: notes circled; empty: bars to come
function MlxRow({ bars, ts, tsRoom, end, D = 26, width, label, line, hiCoral, marks, hair, hl = [], motifs, breath, n0, lit = -1, tag, ring = [], empty = 0 }) {
  const gap = mlxGap(D), items = mlxItems(bars, { ts, tsRoom, end, gap, empty, D }), rg = mlxBarRanges(bars), ns = mlxFlat(bars), hi = mlxHigh(bars);
  const k = {};
  if (marks) k.slurs = marks.map(([a, b]) => [rg[a][0], rg[b][1]]);
  if (hair) k.hair = hair;
  const o = { D, hl: hl.concat(lit >= 0 ? [lit] : []) };
  const room = (line ? 34 : 0) + (motifs ? 24 : 0) + (tag ? 16 : 0) + (n0 != null && !line && !motifs && !tag ? 8 : 0) + (breath ? 6 : 0);
  const extra = (yOf, txt, mm) => { const pts = mm.notes.map((n, i) => [n.x, yOf(ns[i][2] + 12)]);
    const top = line ? yOf(ns[hi][2] + 12) - 10 : yOf(40);
    return <g>
      {line && <g><polyline points={pts.map(p => p.join(',')).join(' ')} fill="none" stroke={PEN_N} strokeWidth="2" strokeLinejoin="round" strokeLinecap="round"/>
        {pts.map((p, i) => <circle key={i} cx={p[0]} cy={p[1]} r={i === hi && hiCoral ? 4.4 : 2.6} fill={i === hi && hiCoral ? PEN_C : i === lit ? PEN_C : PEN_N}/>)}</g>}
      {motifs && motifs.map(([b, lab, cor], j) => { const [a, z] = rg[b], x1 = mm.notes[a].x - 7, x2 = mm.notes[z].x + 7, y = top - 8, c = cor ? PEN_C : PEN_N;
        return <g key={'m' + j}><path d={`M${x1} ${y + 6} L${x1} ${y} L${x2} ${y} L${x2} ${y + 6}`} fill="none" stroke={c} strokeWidth="1.6"/>
          {lab && <text x={(x1 + x2) / 2} y={y - 5} textAnchor="middle" fontSize="12" fontWeight="900" fill={c} style={{fontFamily:'Inter, sans-serif'}}>{lab}</text>}</g>; })}
      {ring.map(j => { const n = mm.notes[j]; return n ? <ellipse key={'r' + j} cx={n.x} cy={n.y} rx={11} ry={8.5} fill="none" stroke={PEN_C} strokeWidth="1.6"/> : null; })}
      {breath && (() => { const n = mm.notes[mm.notes.length - 1], x = n.x + 17, y = yOf(39); return <text x={x} y={y} fontSize="30" fontWeight="900" fill={PEN_N} style={{fontFamily:LB_SERIF}}>,</text>; })()}
      {tag && (() => { const n = mm.notes[mm.notes.length - 1], y = line ? yOf(ns[hi][2] + 12) - 12 : yOf(41);
        return <text x={n.x} y={y} textAnchor="middle" fontSize="13" fontWeight="900" fill={PEN_C} style={{fontFamily:'Inter, sans-serif'}}>{tag === '?' ? t('question', '질문') : tag === '.' ? t('answer', '대답') : tag}</text>; })()}
      {n0 != null && <text x={mm.notes[0].x - (line || motifs ? 24 : 8)} y={yOf(38) - 6} fontSize="13" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{n0}</text>}
    </g>; };
  return <SdyStaff full={!width} width={width || 400} items={items} o={o} k={k} label={label} extra={extra} room={room}/>;
}

// ── the map of a tune (page 1): rows zooming in: the tune and its line, its two phrases, the bars and their motif, bar 1's
// notes. sel: { kind, i } lit coral; onTap(kind, i). Nothing selected (the printed page): the motif, bar 1, is coral.
const MLX_LEVELS4 = ['tune', 'phrase', 'bar', 'notes'];
const MLX_LEVEL_W = { tune: ['the tune', '선율 전체'], phrase: ['phrases', '프레이즈'], bar: ['bars', '마디'], notes: ['the notes', '음'] };
const MLX_ROLE_W = { motif: ['motif', '동기'], up: ['↑ sequence', '↑ 동형 진행'], rep: ['= repetition', '= 반복'] };
const mlxNarrow = () => { try { return window.innerWidth < 420; } catch (e) { return false; } };
function MlxMapSvg({ sel, onTap, label, scr }) {
  // print: 640 wide, the row names in a column on the left; screen: 340 wide, each row's name above it, rows tall enough
  // to tap; on a narrow phone the bars sit two by two under their phrase (taps of 44 px or more)
  const narrow = scr && mlxNarrow(), W = scr ? 340 : 640, L = scr ? 2 : 108, R = W - (scr ? 2 : 10), w = R - L;
  const ph = scr ? (narrow ? 66 : 56) : 34, bh = scr ? (narrow ? 66 : 58) : 50, th = scr ? 98 : 80, fs = scr ? 15 : 11, bgap = 6;
  const barRows = narrow ? 2 : 1, rowY = scr ? { tune: 24, phrase: 150, bar: narrow ? 242 : 232 } : { tune: 10, phrase: 104, bar: 152 };
  rowY.notes = rowY.bar + barRows * (bh + bgap) + (scr ? 40 : 28);
  const zw = scr ? 200 : 260, zh = scr ? 90 : 82, sp = scr ? 10 : 9, H = rowY.notes + zh + 6;
  const on = (kind, i) => !!sel && sel.kind === kind && (sel.i == null || sel.i === i);
  const nm = (kind) => t(MLX_LEVEL_W[kind][0], MLX_LEVEL_W[kind][1]);
  const tap = (kind, i, lab) => onTap ? { onClick: () => onTap(kind, i), onKeyDown: (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onTap(kind, i); } }, role: 'button', tabIndex: 0, 'aria-label': lab, 'aria-pressed': on(kind, i), className: 'mlx-part', style: { cursor: 'pointer' } } : {};
  const col = (kind, i, base = PEN_N) => on(kind, i) ? PEN_C : base;
  const lab = (kind) => scr ? <text x={L + 4} y={rowY[kind] - 8} fontSize={fs} fontWeight="900" fill={BK.muted} letterSpacing="0.06em" style={{fontFamily:'Inter, sans-serif'}}>{nm(kind).toUpperCase()}</text>
    : <text x={0} y={rowY[kind] + (kind === 'tune' ? 44 : kind === 'notes' ? 36 : 22)} fontSize="11" fontWeight="900" fill={BK.muted} letterSpacing="0.08em" style={{fontFamily:'Inter, sans-serif'}}>{nm(kind).toUpperCase()}</text>;
  const ret = !sel;
  const bw = narrow ? w / 4 : w / 8, bx = (i) => narrow ? L + (i >= 4 ? w / 2 : 0) + (i % 2) * bw : L + i * bw, by = (i) => narrow ? rowY.bar + Math.floor((i % 4) / 2) * (bh + bgap) : rowY.bar;
  // the tune's line: a dot where each note starts, its height its pitch (C to A); a long note holds the line level
  const ns = mlxFlat(MLX_TUNE), hi = mlxHigh(MLX_TUNE), beatX = (b) => L + 8 + (b / 32) * (w - 16), yAt = (d) => rowY.tune + th - 14 - (d - 28) * ((th - 34) / 5);
  let bt = 0; const pts = ns.map(n => { const p = [beatX(bt + 0.5), yAt(n[2])]; bt += n[1]; return p; });
  bt = 0; const path = ns.flatMap(n => { const a = [[beatX(bt + 0.5), yAt(n[2])]]; if (n[1] > 1) a.push([beatX(bt + n[1] - 0.5), yAt(n[2])]); bt += n[1]; return a; });
  const tuneCol = col('tune', 0);
  // a bar's notes as a small shape (dots joined); a held note a dot and a level line
  const shape = (b, x0, y0, ww, hh, c) => { const bar = MLX_TUNE[b], y = (d) => y0 + hh - (d - 28) * (hh / 6);
    if (bar.length < 2) return <g><circle cx={x0 + 4} cy={y(bar[0][2])} r={2.4} fill={c}/><line x1={x0 + 4} x2={x0 + ww - 4} y1={y(bar[0][2])} y2={y(bar[0][2])} stroke={c} strokeWidth="1.6"/></g>;
    const p = bar.map((n, j) => [x0 + ww * (j + 0.5) / bar.length, y(n[2])]);
    return <g><polyline points={p.map(q => q.join(',')).join(' ')} fill="none" stroke={c} strokeWidth="1.6"/>{p.map((q, j) => <circle key={j} cx={q[0]} cy={q[1]} r={2.4} fill={c}/>)}</g>; };
  // bar 1 on a little staff with its clef (the zoom)
  const zx = L, zy = rowY.notes, zTop = zy + 22, zBot = zTop + 4 * sp, zNoteY = (d) => zBot - (d - 30) * (sp / 2), zc = col('notes', 0, ret ? PEN_C : PEN_N);
  return <svg viewBox={`0 0 ${W} ${H}`} role={onTap ? 'group' : 'img'} aria-label={label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none',overflow:'visible'}}>
    {onTap && <style>{'.mlx-part:focus{outline:none}.mlx-part:focus-visible>rect:first-of-type{stroke:#e4572e;stroke-width:3;stroke-dasharray:5 3}'}</style>}
    {MLX_LEVELS4.map(k => <React.Fragment key={k}>{lab(k)}</React.Fragment>)}
    <g {...tap('tune', 0, nm('tune'))} data-mlx="tune"><rect x={L} y={rowY.tune} width={w} height={th} rx={6} fill={on('tune', 0) ? '#fbe3da' : 'rgba(38,41,107,0.06)'} stroke={tuneCol} strokeWidth="1.6"/>
      <polyline points={path.map(p => p.join(',')).join(' ')} fill="none" stroke={tuneCol} strokeWidth="1.8" strokeLinejoin="round"/>
      {pts.map((p, i) => <circle key={i} cx={p[0]} cy={p[1]} r={i === hi ? 3.8 : 2.3} fill={tuneCol}/>)}
      <text x={pts[hi][0]} y={pts[hi][1] - 8} textAnchor="middle" fontSize={scr ? 13 : 11} fontWeight="800" fill={tuneCol} style={{fontFamily:'Inter, sans-serif'}}>{t('high point', '가장 높은 음')}</text>
      <text x={L + 8} y={rowY.tune + 16} fontSize={scr ? 13 : 11.5} fontWeight="900" fill={tuneCol} style={{fontFamily:'Inter, sans-serif'}}>{t('8 bars', '모두 8마디')}</text></g>
    {[0, 1].map(i => { const c = col('phrase', i), x = L + i * w / 2;
      return <g key={'p' + i} {...tap('phrase', i, i ? t('the answer', '대답') : t('the question', '질문'))} data-mlx={'phrase' + i}><rect x={x + 1} y={rowY.phrase} width={w / 2 - 2} height={ph} rx={6} fill={on('phrase', i) ? '#fbe3da' : '#fff'} stroke={c} strokeWidth={on('phrase', i) ? 2.6 : 1.8}/>
        <text x={x + w / 4} y={rowY.phrase + ph / 2 + 6} textAnchor="middle" fontSize={scr ? 17 : 16} fontWeight="900" fill={c} style={{fontFamily:LB_SERIF}}>{i ? t('answer.', '대답.') : t('question?', '질문?')}</text></g>; })}
    {Array.from({ length: 8 }, (_, i) => { const role = MLX_ROLE[i], mot = role === 'motif' || role === 'up' || role === 'rep', c = col('bar', i, i === 0 && ret ? PEN_C : mot ? PEN_N : BK.muted), y0 = by(i);
      return <g key={'b' + i} {...tap('bar', i, t('bar ' + (i + 1), (i + 1) + '마디'))} data-mlx={'bar' + i}>
        <rect x={bx(i) + 1.5} y={y0} width={bw - 3} height={bh} rx={4} fill={on('bar', i) ? '#fbe3da' : '#fff'} stroke={c} strokeWidth={mot ? 1.6 : 1}/>
        {shape(i, bx(i) + 6, y0 + 13, bw - 12, scr ? 20 : 17, c)}
        {MLX_ROLE_W[role] && <text x={bx(i) + bw / 2} y={y0 + bh - 7} textAnchor="middle" fontSize={scr ? 11 : 9.5} fontWeight="900" fill={c} style={{fontFamily:'Inter, sans-serif'}}>{scr && !narrow && role !== 'motif' ? MLX_ROLE_W[role][0][0] : t(MLX_ROLE_W[role][0], MLX_ROLE_W[role][1])}</text>}
        <text x={bx(i) + 5} y={y0 + 12} fontSize={scr ? (narrow ? 12 : 10.5) : 8.5} fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{i + 1}</text></g>; })}
    {!narrow && <path d={`M${bx(0) + 2} ${rowY.bar + bh + 1} L${zx + 1} ${zy} M${bx(0) + bw - 2} ${rowY.bar + bh + 1} L${zx + zw} ${zy}`} fill="none" stroke={BK.muted} strokeWidth="1" strokeDasharray="3 3"/>}
    <g {...tap('notes', 0, t('bar 1: the motif, four notes', '1마디: 동기, 네 음'))} data-mlx="notes"><rect x={zx} y={zy} width={zw} height={zh} rx={5} fill={on('notes', 0) ? '#fbe3da' : '#fff'} stroke={col('notes', 0)} strokeWidth="1.4"/>
      {[0, 1, 2, 3, 4].map(j => <line key={j} x1={zx + 8} x2={zx + zw - 8} y1={zTop + j * sp} y2={zTop + j * sp} stroke={PEN_N} strokeWidth="0.9"/>)}
      <text x={zx + 12} y={zBot + sp * 0.75} fontSize={sp * 5.2} fill={PEN_N} style={{fontFamily:"'Noto Music', serif"}}>𝄞</text>
      {MLX_TUNE[0].map((n, j) => { const x = zx + 62 + j * ((zw - 84) / 3), y = zNoteY(n[2]);
        return <g key={j}>{n[2] === 28 && <line x1={x - sp} x2={x + sp} y1={y} y2={y} stroke={PEN_N} strokeWidth="1"/>}<ellipse cx={x} cy={y} rx={sp * 0.68} ry={sp * 0.48} transform={`rotate(-20 ${x} ${y})`} fill={zc}/><line x1={x + sp * 0.63} x2={x + sp * 0.63} y1={y - 1} y2={y - 3.4 * sp} stroke={zc} strokeWidth="1.3"/></g>; })}</g>
    <text x={zx + zw + 12} y={zy + 26} fontSize={scr ? 14 : 12} fontWeight="900" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{t('bar 1: the motif', '1마디: 동기')}</text>
    <text x={zx + zw + 12} y={zy + (scr ? 46 : 44)} fontSize={scr ? 13 : 11.5} fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>C E D F</text>
  </svg>;
}

// ── the Lesson Book: page 1 the map; steps 1 to 5; page 7 the five checks ──
const mlxNbKo = (x) => typeof x !== 'string' ? x : chxNbKo(x).replace(/(질문|대답) 프레이즈/g, '$1 프레이즈').replace(/동형 진행/g, '동형 진행').replace(/가장 높은 음/g, '가장 높은 음')
  .replace(/쉬는 음/g, '쉬는 음').replace(/프레이즈 표시/g, '프레이즈 표시').replace(/(한|두|세|네) (걸음|음|마디|번)/g, '$1 $2').replace(/(\d)마디 (\d)/g, '$1마디 $2')
  .replace(/첫 (번째|마디|프레이즈|음)/g, '첫 $1').replace(/(같은|다른|새) (음|모양|동기)/g, '$1 $2')
  .replace(/점점 (세게|여리게|세지고|여려져요)/g, '점점 $1').replace(/내 (선율|곡)/g, '내 $1').replace(/마지막 음/g, '마지막 음').replace(/그린 것/g, '그린 것').replace(/(올라가는|내려가는) 동형/g, '$1 동형').replace(/한 걸음/g, '한 걸음').replace(/▶ /g, '▶ ');
const mlxKoT = (x) => LANG === 'ko' ? mlxNbKo(x) : x;

function mlxLbPages(scr = false) {
  const ch = 'melody';
  const live = (still, comp) => <LbLive still={still} live={comp}/>;
  const stack = (nodes, h, gap = 12, mw = 680) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap,width:'100%',maxWidth:mw,margin:'0 auto',alignItems:'stretch'}}>{nodes}</div></LbPic>;
  const X = (en, ko) => sscT(en, skgKo(mlxNbKo(ko)));
  const cap = (x, key = 'cap') => <div key={key} style={{textAlign:'center',fontSize:scr ? 14 : 13.5,fontWeight:800,color:BK.ink,margin:'2px auto 0',maxWidth:560,lineHeight:1.35,textWrap:'balance'}}>{mlxKoT(x)}</div>;
  const ch24 = bkChapterNo('form'), ch16 = bkChapterNo('scales');

  // p1 (macro first): the map of a tune
  const p1 = <LbLive still={stack([<MlxMapSvg key="m" label={t('The map of a tune. The tune: 8 bars; its line rises to a high point, the A in bar 3, and comes down to C. Its phrases: a question, bars 1 to 4, and an answer, bars 5 to 8. Its bars: bar 1 is the motif (coral); bars 2 and 3 are the motif a step higher each time (sequence); bar 5 is the motif again (repetition); bar 6 a step higher. Bar 1 opened up: C E D F on the staff.', '선율의 지도. 선율 전체: 8마디. 선율선이 3마디의 A까지 올라갔다가 C로 내려와요. 프레이즈: 질문(1~4마디)과 대답(5~8마디). 마디: 1마디가 동기(산호색), 2·3마디는 동기를 한 걸음씩 높여서(동형 진행), 5마디는 동기 그대로(반복), 6마디는 한 걸음 높여서. 1마디를 펼치면: 오선 위의 C E D F.')}/>,
    cap(t('Here: notes make the motif, the motif makes the phrases, a question and an answer make the tune.', '여기서는 음이 모여 동기, 동기가 모여 프레이즈, 질문과 대답이 모여 선율이 돼요.'))], 380, 10)} live={<MlxMapPad/>}/>;
  // p2: the line of a tune
  const w8 = mlxVbw(MLX_Q, true);
  const p2 = stack([<MlxRow key="q" bars={MLX_Q} ts end={false} line hiCoral hl={[mlxHigh(MLX_Q)]} width={w8} n0={1} label={t('Bars 1 to 4 with their line drawn above: up and down in small waves to the A in bar 3, the high point (coral), then down to G.', '1~4마디와 그 위에 그린 선율선: 작은 물결로 오르내리며 3마디의 A(가장 높은 음, 산호색)까지 올라간 뒤 G로 내려와요.')}/>,
    <MlxRow key="a" bars={MLX_A} tsRoom line width={w8} n0={5} label={t('Bars 5 to 8 with their line: up to G in bar 6, then down to C.', '5~8마디와 선율선: 6마디의 G까지 올라갔다가 C로 내려와요.')}/>,
    cap(t('The line follows the notes: up, down, and up to one high point.', '선율선은 음을 따라가요: 올라가고, 내려가고, 가장 높은 음 하나까지 올라가요.'), 'c2')], 330, 26, 640);
  // p3: phrasing: one phrase, its phrase mark, growing to the high point and softer to the resting note, a breath
  const nQ = mlxCount(MLX_Q), hQ = mlxHigh(MLX_Q);
  const lab3 = (en, ko, key) => <div key={key} style={{fontSize:12,fontWeight:900,letterSpacing:'0.08em',color:BK.muted,textAlign:'left',maxWidth:600,margin:'0 auto -6px',width:'100%'}}>{mlxKoT(t(en, ko)).toUpperCase()}</div>;
  const p3 = stack([lab3('One loudness', '같은 세기', 'l1'), <div key="f" style={{maxWidth:600,margin:'0 auto',width:'100%'}}><MlxRow bars={MLX_Q} ts end={false} marks={[[0, 3]]} width={mlxVbw(MLX_Q, true)} label={t('Bars 1 to 4 under one phrase mark, with no other marks.', '1~4마디, 프레이즈 표시 하나만 있어요.')}/></div>,
    lab3('Shaped', '모양 살려서', 'l2'), <div key="r" style={{maxWidth:600,margin:'0 auto',width:'100%'}}><MlxRow bars={MLX_Q} ts end={false} marks={[[0, 3]]} hair={[[0, hQ - 1, 'cresc'], [hQ, nQ - 1, 'dim']]} hl={[hQ]} breath width={mlxVbw(MLX_Q, true)} label={t('Bars 1 to 4 under one phrase mark. Under the notes: a crescendo up to the A in bar 3 (coral), a diminuendo down to the G; a breath mark after the G.', '1~4마디가 프레이즈 표시 하나로 묶여 있어요. 음 아래: 3마디의 A(산호색)까지 크레셴도, G까지 디미누엔도. G 뒤에 숨표.')}/></div>,
    cap(t('A common shape: louder to the high point, softer to the resting note, then a breath before the next phrase.', '자주 쓰는 모양: 가장 높은 음까지 점점 세게, 쉬는 음까지 점점 여리게, 그다음 숨을 쉬고 다음 프레이즈로.'), 'c3')], 300, 18, 640);
  // p4: question and answer, one over the other, their last notes coral
  const p4 = stack([<MlxRow key="q" bars={MLX_Q} ts end={false} hl={[nQ - 1]} tag="?" width={w8} n0={1} label={t('The question, bars 1 to 4: it ends on G (coral), not the tonic.', '질문(1~4마디): G(산호색)에서 끝나요. 으뜸음이 아니에요.')}/>,
    <MlxRow key="a" bars={MLX_A} tsRoom hl={[mlxCount(MLX_A) - 1]} tag="." width={w8} n0={5} label={t('The answer, bars 5 to 8: it starts like the question and ends on C (coral), the tonic.', '대답(5~8마디): 질문처럼 시작해서 C(산호색), 으뜸음에서 끝나요.')}/>,
    cap(t('The same start. The question rests on G; the answer comes home to C.', '시작은 같아요. 질문은 G에서 쉬고, 대답은 C로 돌아와요.'), 'c4')], 330, 30, 640);
  // p5: the motif and where it comes back
  const mot = (bars, off) => bars.map((_, b) => b + off).filter(b => MLX_ROLE[b] !== 'rest' && MLX_ROLE[b] !== 'end').map(b => [b - off, b === 0 ? t('motif', '동기') : '', b === 0]);
  const p5 = stack([<MlxRow key="q" bars={MLX_Q} ts end={false} motifs={mot(MLX_Q, 0)} hl={[0, 1, 2, 3]} width={w8} n0={1} label={t('Bars 1 to 4: bar 1, the motif (coral, bracketed); bars 2 and 3 bracketed: the same four-note shape, each a step higher.', '1~4마디: 1마디가 동기(산호색, 괄호), 2·3마디도 괄호: 같은 네 음 모양이 한 걸음씩 높아져요.')}/>,
    <MlxRow key="a" bars={MLX_A} tsRoom motifs={mot(MLX_A, 4)} width={w8} n0={5} label={t('Bars 5 to 8: bars 5 and 6 bracketed: the motif again, then a step higher.', '5~8마디: 5·6마디 괄호: 동기가 다시, 그다음 한 걸음 높게.')}/>,
    cap(t('Bar 1 is the motif. It comes back in bars 2, 3, 5 and 6.', '1마디가 동기예요. 2, 3, 5, 6마디에 다시 나와요.'), 'c5')], 330, 26, 640);
  // p6: what a motif can do: the motif, a repetition, a sequence up, a sequence down
  const box = (en, ko, bars, cor) => <div key={en} style={{display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'space-between',gap:4,minWidth:0}}>
    <div style={{width:'100%',maxWidth:192,margin:'0 auto'}}><MlxRow bars={bars} end={false} hl={cor ? [0, 1, 2, 3] : []} width={mlxVbw([MLX_Q[0]], false)} label={t(en + ': ' + bars[0].map(n => mlxName(n[2])).join(' ') + '.', ko + ': ' + bars[0].map(n => mlxName(n[2])).join(' ') + '.')}/></div>
    <span style={{fontSize:14,fontWeight:900,color:cor ? PEN_C : BK.ink,textAlign:'center'}}>{mlxKoT(t(en, ko))}</span></div>;
  const p6 = stack([<div key="g" style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:'22px 40px',alignItems:'stretch',maxWidth:520,margin:'0 auto',width:'100%'}}>
      {box('the motif, from D', 'D에서 시작한 동기', [mlxQ([29, 31, 30, 32])], true)}{box('repetition', '반복', [mlxQ([29, 31, 30, 32])])}{box('sequence up', '올라가는 동형 진행', [mlxQ([30, 32, 31, 33])])}{box('sequence down', '내려가는 동형 진행', [mlxQ([28, 30, 29, 31])])}</div>,
    cap(t('The same notes: repetition. The same shape a step higher or lower: sequence.', '같은 음으로 다시: 반복. 같은 모양으로 한 걸음 높거나 낮게: 동형 진행.'), 'c6')], 260, 26, 680);

  // the check icons
  const dots = (pts, col, hiI) => '<polyline points="' + pts.map(p => p.join(',')).join(' ') + '" fill="none" stroke="' + col + '" stroke-width="1.8"/>' + pts.map((p, i) => '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + (i === hiI ? 4 : 2.4) + '" fill="' + (i === hiI ? PEN_C : col) + '"/>').join('');
  const ic = {
    map: [{ k: 'raw', svg: '<rect x="6" y="4" width="80" height="15" rx="2" fill="none" stroke="' + PEN_N + '" stroke-width="1.4"/><polyline points="12,15 22,11 30,13 40,8 48,6 58,12 68,10 80,15" fill="none" stroke="' + PEN_N + '" stroke-width="1.4"/><circle cx="48" cy="6" r="3" fill="' + PEN_C + '"/>' + [6, 47].map(x => '<rect x="' + x + '" y="23" width="39" height="13" rx="2" fill="none" stroke="' + PEN_N + '" stroke-width="1.4"/>').join('') }],
    line: [{ k: 'raw', svg: dots([[10, 30], [24, 22], [36, 26], [50, 14], [62, 8], [76, 20], [86, 30]], PEN_N, 4) }],
    phrasing: [{ k: 'raw', svg: '<polyline points="46,14 8,20 46,26" fill="none" stroke="' + PEN_N + '" stroke-width="1.8"/><polyline points="50,14 80,20 50,26" fill="none" stroke="' + PEN_N + '" stroke-width="1.8"/><text x="84" y="14" style="font-family:Georgia, serif" font-size="22" font-weight="900" fill="' + PEN_C + '">,</text>' }],
    qa: [{ k: 'raw', svg: '<text x="28" y="30" text-anchor="middle" style="font-family:Georgia, serif" font-size="26" font-weight="900" fill="' + PEN_N + '">?</text><circle cx="64" cy="25" r="3.6" fill="' + PEN_C + '"/>' }],
    seq: [{ k: 'raw', svg: dots([[8, 30], [16, 24], [24, 28], [32, 22]], PEN_N) + dots([[38, 24], [46, 18], [54, 22], [62, 16]], PEN_N) + dots([[68, 18], [76, 12], [84, 16], [90, 10]], PEN_C) }],
  };
  const checksRows = [
    ['map', t('I can show a tune’s phrases, its motif and its high point on its map', '선율의 지도에서 프레이즈, 동기, 가장 높은 음을 보여 줄 수 있어요')],
    ['line', t('I can draw the line of a tune I hear', '들은 선율의 선율선을 그릴 수 있어요')],
    ['phrasing', t('I can play a phrase louder to its high point, softer to its end, and breathe', '프레이즈를 가장 높은 음까지 점점 세게, 끝까지 점점 여리게 치고 숨을 쉴 수 있어요')],
    ['qa', t('I can play a question and an answer and say which is which', '질문과 대답을 치고, 각각 질문인지 대답인지 말할 수 있어요')],
    ['seq', t('I can play a motif in sequence, a step higher each time', '동기를 한 걸음씩 높여 동형 진행으로 칠 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? skgKo(sscNbKo(mlxNbKo(x))) : sscNbEn(x)]);

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <>음이 리듬과 함께 하나씩 이어져 만드는 음악이 <b>선율</b>이에요. 이 선율은 한 동기로 만든 질문과 대답이에요.</> : <><b>Melody</b> is notes one after another, with their rhythm, that make a tune. This tune is a question and an answer, built from one motif.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('The line of a tune', '선율선'), 2], [t('Phrasing', '프레이징'), 3], [t('Question and answer', '질문과 대답'), 4], [t('The motif', '동기'), 5], [t('Repetition and sequence', '반복과 동형 진행'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}<span>{n}</span></span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)',textWrap:'pretty'}}>{bkGoal(15)}<span>{x.replace(/^I can /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The line of a tune', '선율선')}>
      {live(p2, <MlxLinePad/>)}
      <LbDefs items={[
        [t('melody', '선율'), X('Notes one after another, with their rhythm, that make a tune.', '음이 리듬과 함께 하나씩 이어져 만드는 음악. 다른 이름은 가락이에요.')],
        [t('contour', '선율선'), X('The up-and-down shape of a melody. Drawn, it is the line of the tune.', '선율이 올라가고 내려가는 모양. 선으로 그려서 나타내요.')],
        [t('high point', '가장 높은 음'), X('The highest note of a phrase or a tune.', '프레이즈나 선율에서 제일 높이 올라간 음. 선율선의 꼭대기예요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the picture’s tune. Draw its line in the air with your other hand.', '그림의 선율을 쳐요. 다른 손으로 공중에 선율선을 그려요.'),
        X('Your teacher plays a tune. Draw its line, and mark its high point.', '선생님이 선율을 쳐요. 선율선을 그리고 가장 높은 음에 표시해요.'),
      ]}/>
      <LbRemember>{X('The line goes where the notes go.', '선율선은 음이 가는 대로 가요.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Phrasing', '프레이징')}>
      {live(p3, <MlxPhrasingPad/>)}
      <LbDefs items={[
        [t('phrasing', '프레이징'), X('How a phrase is shaped as it is played: where it gets louder and softer, and where it breathes.', '프레이즈를 모양 있게 치는 방법: 어디서 세지고 여려지는지, 어디서 숨을 쉬는지.')],
        [t('breath mark', '숨표'), X('A comma above the staff between two phrases. Lift briefly: the time comes from the note before.', '두 프레이즈 사이, 오선 위쪽에 쓰는 콤마(,) 모양의 표. 손을 잠깐 들어요: 그 시간은 앞 음에서 빼요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the phrase: louder to the high point, softer to the resting note, then lift at the breath mark.', '프레이즈를 쳐요: 가장 높은 음까지 점점 세게, 쉬는 음까지 점점 여리게, 숨표에서 손을 들어요.'),
        X('Play it once at one loudness, then shaped. Say which you like.', '한 번은 같은 세기로, 한 번은 모양을 살려 쳐요. 어느 쪽이 좋은지 말해요.'),
      ]}/>
      <LbRemember>{X('A phrase often gets louder to its high point and softer to its end.', '프레이즈는 보통 가장 높은 음까지 점점 세지고, 끝으로 갈수록 여려져요.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Question and answer', '질문과 대답')}>
      {live(p4, <MlxQaPad/>)}
      <LbDefs items={[
        [t('question phrase', '질문 프레이즈'), X('The first phrase of a pair, ending away from the tonic. It sounds unfinished.', '짝을 이루는 두 프레이즈 중 첫째. 으뜸음이 아닌 음에서 끝나서 아직 안 끝난 느낌이에요.')],
        [t('answer phrase', '대답 프레이즈'), X('The phrase after a question, ending on the tonic (chapter ' + ch16 + '). It sounds finished.', '질문 뒤에 와서 으뜸음(' + ch16 + '챕터)에서 끝나는 프레이즈. 끝난 느낌이에요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the question, then the answer. Listen to how each one ends.', '질문을 치고 대답을 쳐요. 둘이 어떻게 끝나는지 잘 들어요.'),
        X('Play the answer. Then end it on G instead of C: it turns into a question.', '대답을 쳐요. 그다음 C 대신 G로 끝내요: 질문으로 바뀌어요.'),
      ]}/>
      <LbRemember>{X('A question ends away from the tonic; its answer ends on the tonic.', '질문은 으뜸음이 아닌 음에서, 대답은 으뜸음에서 끝나요.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The motif', '동기')}>
      {live(p5, <MlxMotifPad/>)}
      <LbDefs items={[
        [t('motif', '동기'), X('A short musical idea, a few notes long, that comes back in the music.', '몇 개의 음으로 된 짧은 음악 조각. 곡 안에서 다시 나와요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the motif, bar 1. Then play the tune and say “motif” each time it comes back.', '1마디의 동기를 쳐요. 그다음 선율을 치면서 동기가 다시 나올 때마다 “동기”라고 말해요.'),
        X('In a piece you are learning, find a motif. Count how many times it comes.', '배우고 있는 곡에서 동기를 찾아요. 몇 번 나오는지 세어요.'),
      ]}/>
      <LbRemember>{X('A motif is a short idea that comes back.', '동기는 다시 나오는 짧은 음악 조각이에요.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Repetition and sequence', '반복과 동형 진행')}>
      {live(p6, <MlxSeqPad/>)}
      <LbDefs items={[
        [t('repetition', '반복'), X('The same music again, on the same notes (chapter ' + ch24 + ').', '같은 음악이 같은 음으로 다시 나오는 것(' + ch24 + '챕터).')],
        [t('sequence', '동형 진행'), X('The same shape again straight after, starting on a higher or lower note.', '같은 모양이 바로 이어서, 더 높거나 낮은 음에서 시작해 다시 나오는 것.')],
      ]}/>
      <LbPiano steps={[
        X('Play the motif from D twice (repetition). Then from D and from E (sequence up), and from D and from C (sequence down).', 'D에서 동기를 두 번 쳐요(반복). 그다음 D와 E에서(올라가는 동형 진행), D와 C에서(내려가는 동형 진행) 쳐요.'),
        X('Make a motif of four notes. Play it, then play it a step higher, and a step higher again.', '네 음으로 동기를 만들어요. 그 동기를 치고, 한 걸음 높여서 치고, 또 한 걸음 높여서 쳐요.'),
      ]}/>
      <LbRemember>{X('Same notes: repetition. Same shape, new start: sequence.', '같은 음이면 반복, 같은 모양으로 새 음에서 시작하면 동형 진행.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (1 to 4, and 6). The check-up on paper is in the Workbook.', '1~4쪽과 6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_mlx_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, x])}/>}/>
    </LbPage>,
  ];
}
function MelodyLessonBook() { return <>{mlxLbPages(false)}</>; }
