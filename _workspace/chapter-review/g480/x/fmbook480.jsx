// ─── Phase 480: chapter 24, Musical Form, built in full (Book rules 14 and 15; her 2026-10-17 macro-first plan and her
// 09:42 order: terms, then form, then melody). The last room of Level 4. Page 1 is the map of a piece: the whole piece,
// its sections (A B A), their phrases, the bars, one bar's beats, each row a zoom into the one above; the steps zoom in
// (the phrase, same or different and the letters, binary, ternary, finding the form); the screen lesson ends with a piece
// the student builds from A and B. Placement (AMEB Music Craft 2022): Grade 1 repetition and contrast in an eight-bar
// melody, repeat signs; Grade 2 the definition of phrase, binary and ternary form marked with A and B; Grade 3 (aural)
// A and B in a sixteen-bar four-phrase melody. Rondo comes at Grade 5 (the older tools keep it). Chapter 20's roads
// (SgnRoad: repeat signs, Fine, D.C. al Fine) draw the binary and ternary pieces; chapter 10's SdyStaff the phrases.

// the book's phrases: four bars each, 4/4, right hand from middle C; the book's own. Each ends on a resting note.
const FMX_PH = {
  A: [[['q', 1, 28], ['q', 1, 29], ['q', 1, 30], ['q', 1, 31]], [['q', 1, 32], ['q', 1, 30], ['h', 2, 28]], [['q', 1, 29], ['q', 1, 30], ['q', 1, 31], ['q', 1, 29]], [['w', 4, 28]]],   // C D E F | G E C | D E F D | C (home)
  B: [[['q', 1, 30], ['q', 1, 32], ['q', 1, 31], ['q', 1, 32]], [['q', 1, 33], ['q', 1, 32], ['q', 1, 31], ['q', 1, 30]], [['q', 1, 29], ['q', 1, 30], ['q', 1, 31], ['q', 1, 29]], [['w', 4, 32]]],   // E G F G | A G F E | D E F D | G (away)
  C: [[['q', 1, 32], ['q', 1, 33], ['q', 1, 32], ['q', 1, 31]], [['q', 1, 30], ['q', 1, 31], ['h', 2, 30]], [['q', 1, 29], ['q', 1, 30], ['q', 1, 31], ['q', 1, 30]], [['w', 4, 29]]],   // G A G F | E F E | D E F E | D (away)
  D: [[['q', 1, 30], ['q', 1, 32], ['q', 1, 31], ['q', 1, 30]], [['h', 2, 29], ['h', 2, 31]], [['q', 1, 30], ['q', 1, 29], ['q', 1, 28], ['q', 1, 29]], [['w', 4, 30]]],   // E G F E | D F | E D C D | E
  E: [[['q', 1, 32], ['q', 1, 31], ['q', 1, 30], ['q', 1, 29]], [['q', 1, 31], ['q', 1, 33], ['h', 2, 32]], [['q', 1, 33], ['q', 1, 32], ['q', 1, 31], ['q', 1, 29]], [['w', 4, 28]]],   // G F E D | F A G | A G F D | C (home)
};
const FMX_NOTE = ['C', 'D', 'E', 'F', 'G', 'A', 'B'];
const fmxCount = (id) => FMX_PH[id].reduce((a, b) => a + b.length, 0);
// a row of phrases as staff items (one system): bar lines between bars, the final bar line at the very end (end: false,
// a single one). tsRoom: the time signature's room kept on rows without it, so rows stack bar under bar; gap: room
// before each bar line (small staves: the line clear of the last note's stem)
const fmxItems = (ids, o = {}) => { const items = o.ts ? [['ts', 4]] : o.tsRoom ? [['sp', 26]] : [];
  ids.forEach((id, p) => FMX_PH[id].forEach((bar, b) => { bar.forEach(n => items.push(n)); if (o.gap) items.push(['sp', o.gap]);
    const last = p === ids.length - 1 && b === 3; items.push(last && o.end !== false ? ['||'] : ['|']); }));
  return items; };
const fmxGap = (D) => D < 22 ? 7 : 0;
// note index ranges of each phrase in a row; its last note (the resting note)
const fmxRanges = (ids) => { let k = 0; return ids.map(id => { const a = k; k += fmxCount(id); return [a, k - 1]; }); };
const fmxNotes = (ids) => ids.flatMap(id => FMX_PH[id].flat().map(n => ({ d: n[2], dur: n[1] })));
const fmxLast = (id) => { const bar = FMX_PH[id][3]; return FMX_NOTE[(bar[bar.length - 1][2] - 28) % 7]; };
// the sound: one at a time. A sound started while another plays (or a pad that closes) ends the other one properly:
// its pad's end callback runs, so no pad stays lit with nothing sounding.
let _fmxT = [], _fmxEnd = null;
const fmxStop = () => { _fmxT.forEach(clearTimeout); _fmxT = []; chxStop(); const e = _fmxEnd; _fmxEnd = null; if (e) e(); };
const FMX_BPM = 150;
function fmxRun(notes, cb, bpm = FMX_BPM) {
  fmxStop();
  if (!cb) { _fmxT = playMelody(notes, bpm, null); return; }
  const end = () => { if (_fmxEnd === end) _fmxEnd = null; cb(-1); };
  _fmxEnd = end; _fmxT = playMelody(notes, bpm, (i) => i === -1 ? end() : cb(i));
}
// a run of phrases; onPhrase(i) as each starts, -1 at the end (or when stopped)
function fmxPlay(ids, onPhrase, bpm = FMX_BPM) {
  const starts = []; let k = 0; ids.forEach(id => { starts.push(k); k += fmxCount(id); });
  fmxRun(fmxNotes(ids), onPhrase ? (i) => { if (i === -1) onPhrase(-1); else if (starts.includes(i)) onPhrase(starts.indexOf(i)); } : null, bpm);
}
// notes (d, dur) with onStep per note, for the roads
const fmxPlayNotes = (notes, onStep, bpm = FMX_BPM) => fmxRun(notes, onStep, bpm);
// clicks (the beats), stoppable like the rest
function fmxPlayBeats(n, onEnd) { fmxStop(); playClicks(FMX_BPM, n); const end = () => { if (_fmxEnd === end) _fmxEnd = null; onEnd(); }; _fmxEnd = end; _fmxT = [setTimeout(end, n * 60000 / FMX_BPM)]; }

// one system of phrases on the treble staff: phrase marks (marks), letters over the phrases (letters; coral: the indexes
// drawn coral; qmark: boxes to fill), the resting notes coral (rest), the first bar's number (n0)
function FmxRow({ ids, ts, tsRoom, marks, letters, coral = [], rest, n0, width, label, D = 26, end, qmark = [], secEnd }) {
  const gap = fmxGap(D), items = fmxItems(ids, { ts, tsRoom, end, gap }), rg = fmxRanges(ids);
  const k = marks ? { slurs: rg.map(([a, b]) => [a, b]) } : {};
  const o = { D, hl: rest ? rg.map(([, b]) => b) : [] }, small = D < 22, [bw0, bh0] = small ? [46, 42] : [30, 28];
  const extra = (yOf, txt, mm) => <g>
    {letters && rg.map(([a, b], j) => { const x = (mm.notes[a].x + mm.notes[b].x) / 2, y = yOf(38) - (small ? 22 : 20), c = coral.includes(j) ? PEN_C : PEN_N, q = qmark.includes(j);
      return <g key={j}><rect x={x - bw0 / 2} y={y - bh0 + 7} width={bw0} height={bh0} rx={4} fill="#fff" stroke={c} strokeWidth={q ? 1.4 : 1.8} strokeDasharray={q ? '4 3' : undefined}/>
        <text x={x} y={small ? y - 4 : y} textAnchor="middle" fontSize={small ? 28 : 20} fontWeight="900" fill={c} style={{fontFamily:LB_SERIF}}>{letters[j] || ''}</text></g>; })}
    {secEnd && mm.bars.length > 0 && <line x1={mm.bars[mm.bars.length - 1] - 4} x2={mm.bars[mm.bars.length - 1] - 4} y1={yOf(38)} y2={yOf(30)} stroke={PEN_N} strokeWidth="1.5"/>}
    {n0 != null && <text x={mm.notes[0].x - 8} y={yOf(38) - 6} fontSize="11" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{n0}</text>}
  </g>;
  return <SdyStaff full={!width} width={width || 400} items={items} o={o} k={k} label={label} extra={extra} room={letters ? (small ? 46 : 30) : n0 != null ? 6 : 0}/>;
}
const fmxVbw = (ids, ts, D = 26, tsRoom) => sdyVbw(fmxItems(ids, { ts, tsRoom, gap: fmxGap(D) }), { D });

// ── the map of a piece (page 1): rows zooming in: the piece, its sections, the phrases, the bars, one bar's beats ──
// the piece: A B A, eight bars a section, four a phrase. sel: { kind, i } lit coral; onTap(kind, i). Nothing selected
// (the printed page): the A that comes back is coral. quiz: no row names (the drill asks them)
const FMX_SEC = ['A', 'B', 'A'];
const FMX_LEVELS6 = ['piece', 'section', 'phrase', 'bar', 'beat'];
const FMX_LEVEL_W = { piece: ['the piece', '곡 전체'], section: ['sections', '부분'], phrase: ['phrases', '프레이즈'], bar: ['bars', '마디'], beat: ['beats', '박'] };
function FmxMapSvg({ sel, onTap, label, scr, quiz }) {
  // print: 640 wide, the row names in a column on the left; screen: 340 wide, each row's name above it, rows tall enough to tap
  const W = scr ? 340 : 640, L = scr ? 6 : 108, R = W - (scr ? 6 : 10), w = R - L;
  const extra = (i) => Math.floor(i / 4) * 2 + Math.floor(i / 8) * 3, bw = (w - extra(23)) / 24, bx = (i) => L + i * bw + extra(i);
  const rowY = scr ? { piece: 24, section: 100, phrase: 180, bar: 236, beat: 336 } : { piece: 14, section: 70, phrase: 124, bar: 176, beat: 252 };
  const H = scr ? 392 : 300, ph = scr ? 44 : 30, sh = scr ? 50 : 38, barH = scr ? 30 : 26, bt = scr ? 44 : 46, fs = scr ? 15 : 11;
  const on = (kind, i) => sel && sel.kind === kind && (sel.i == null || sel.i === i);
  const nm = (kind) => t(FMX_LEVEL_W[kind][0], FMX_LEVEL_W[kind][1]);
  const tap = (kind, i, lab) => onTap ? { onClick: () => onTap(kind, i), onKeyDown: (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onTap(kind, i); } }, role: 'button', tabIndex: 0, 'aria-label': lab, style: { cursor: 'pointer' } } : {};
  const col = (kind, i, base = PEN_N) => on(kind, i) ? PEN_C : base;
  const lab = (kind) => quiz ? null : scr ? (kind === 'beat' ? null : <text x={L} y={rowY[kind] - 8} fontSize={fs} fontWeight="900" fill={BK.muted} letterSpacing="0.06em" style={{fontFamily:'Inter, sans-serif'}}>{nm(kind).toUpperCase()}</text>)
    : <text x={0} y={rowY[kind] + (kind === 'beat' ? 26 : kind === 'bar' ? 17 : 20)} fontSize="11" fontWeight="900" fill={BK.muted} letterSpacing="0.08em" style={{fontFamily:'Inter, sans-serif'}}>{nm(kind).toUpperCase()}</text>;
  const ret = !sel && !quiz;   // the printed page: the A that comes back, coral
  const secX = (i) => bx(i * 8), secW = () => 8 * bw + extra(7) - extra(0);
  return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>
    {FMX_LEVELS6.map(k => <React.Fragment key={k}>{lab(k)}</React.Fragment>)}
    <g {...tap('piece', 0, nm('piece'))} data-fmx="piece"><rect x={L} y={rowY.piece} width={w} height={ph} rx={6} fill={on('piece', 0) ? '#fbe3da' : 'rgba(38,41,107,0.08)'} stroke={col('piece', 0)} strokeWidth="1.6"/>
      <text x={L + w / 2} y={rowY.piece + ph / 2 + fs * 0.36} textAnchor="middle" fontSize={scr ? 15 : 13} fontWeight="800" fill={col('piece', 0)} style={{fontFamily:'Inter, sans-serif'}}>{t('24 bars', '24마디')}</text></g>
    {FMX_SEC.map((s, i) => { const c = col('section', i, i === 2 && ret ? PEN_C : PEN_N);
      return <g key={'s' + i} {...tap('section', i, t('section ' + (i + 1) + ', ' + s, fmxNth(i + 1) + ' 부분, ' + s))} data-fmx={'section' + i}><rect x={secX(i) + 1} y={rowY.section} width={secW() - 2} height={sh} rx={6} fill={on('section', i) ? '#fbe3da' : '#fff'} stroke={c} strokeWidth={on('section', i) ? 2.6 : 1.8}/>
        <text x={secX(i) + secW() / 2} y={rowY.section + sh / 2 + 9} textAnchor="middle" fontSize="26" fontWeight="900" fill={c} style={{fontFamily:LB_SERIF}}>{s}</text>
        {i === 2 && ret && <text x={secX(i) + secW() / 2 + 16} y={rowY.section + sh / 2 + 9} fontSize="11.5" fontWeight="800" fill={PEN_C} style={{fontFamily:'Inter, sans-serif'}}>{t('again', '다시')}</text>}</g>; })}
    {[0, 1, 2, 3, 4, 5].map(i => { const x1 = bx(i * 4) + 4, x2 = bx(i * 4 + 3) + bw - 4, y = rowY.phrase, c = col('phrase', i);
      return <g key={'p' + i} {...tap('phrase', i, t('phrase ' + (i + 1), fmxNth(i + 1) + ' 프레이즈'))} data-fmx={'phrase' + i}>{onTap && <rect x={x1 - 3} y={y - (scr ? 14 : 4)} width={x2 - x1 + 6} height={scr ? 50 : 36} fill="transparent"/>}
        <path d={`M${x1} ${y} Q${(x1 + x2) / 2} ${y + 34} ${x2} ${y}`} fill="none" stroke={c} strokeWidth={on('phrase', i) ? 3 : 2} strokeLinecap="round"/></g>; })}
    {Array.from({ length: 24 }, (_, i) => <g key={'b' + i} {...tap('bar', i, t('bar ' + (i + 1), (i + 1) + '마디'))} data-fmx={'bar' + i}>{onTap && <rect x={bx(i) - 1} y={rowY.bar - 12} width={bw + 2} height={56} fill="transparent"/>}
      <rect x={bx(i) + 0.5} y={rowY.bar} width={bw - 1} height={barH} rx={3} fill={on('bar', i) ? '#fbe3da' : '#fff'} stroke={col('bar', i)} strokeWidth="1.2"/>
      {!scr && <text x={bx(i) + bw / 2} y={rowY.bar + 17} textAnchor="middle" fontSize="9.5" fontWeight="800" fill={col('bar', i)} style={{fontFamily:'Inter, sans-serif'}}>{i + 1}</text>}
      {scr && [0, 8, 16, 23].includes(i) && <text x={bx(i) + bw / 2} y={rowY.bar + barH + 18} textAnchor="middle" fontSize="14" fontWeight="800" fill={col('bar', i, BK.muted)} style={{fontFamily:'Inter, sans-serif'}}>{i + 1}</text>}</g>)}
    <path d={`M${bx(0) + 1} ${rowY.bar + barH + 1} L${L + 1} ${rowY.beat} M${bx(0) + bw - 1} ${rowY.bar + barH + 1} L${L + 4 * bt} ${rowY.beat}`} fill="none" stroke={BK.muted} strokeWidth="1" strokeDasharray="3 3"/>
    <g {...tap('beat', 0, t('bar 1: four beats', '1마디: 네 박'))} data-fmx="beat"><rect x={L} y={rowY.beat} width={4 * bt} height={scr ? 48 : 40} rx={5} fill={on('beat', 0) ? '#fbe3da' : '#fff'} stroke={col('beat', 0)} strokeWidth="1.4"/>
      {[0, 1, 2, 3].map(j => <g key={j}><circle cx={L + bt / 2 + j * bt} cy={rowY.beat + 15} r={6} fill={col('beat', 0)}/><text x={L + bt / 2 + j * bt} y={rowY.beat + (scr ? 40 : 35)} textAnchor="middle" fontSize={scr ? 14 : 11} fontWeight="900" fill={col('beat', 0)} style={{fontFamily:'Inter, sans-serif'}}>{j + 1}</text></g>)}</g>
    {scr && !quiz && <text x={L + 4 * bt + 12} y={rowY.beat + 16} fontSize={fs} fontWeight="900" fill={BK.muted} letterSpacing="0.06em" style={{fontFamily:'Inter, sans-serif'}}>{nm('beat').toUpperCase()}</text>}
    {!quiz && <text x={L + 4 * bt + 12} y={rowY.beat + (scr ? 36 : 25)} fontSize={scr ? 14 : 12} fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{t('bar 1: four beats', '1마디: 네 박')}</text>}
  </svg>;
}
// the piece the map shows: A = phrases B then A (ends at home), B = phrases D then C (ends on D, leading back), then A
const FMX_PIECE = { A: ['B', 'A'], B: ['D', 'C'] };
const fmxPieceIds = (secs = FMX_SEC) => secs.flatMap(s => FMX_PIECE[s]);

// ── page 4 and 5: binary and ternary on chapter 20's roads ──
const fmxBars = (id) => FMX_PH[id].map(bar => bar.map(n => sgnQ(n[2], n[0] === 'w' ? 'w' : n[0] === 'h' ? 'h' : 'q')));
// binary: ‖: B :‖: E :‖  (A ends away on G, B comes home to C); ternary: A Fine, C D.C. al Fine
const FMX_BIN = (() => { const a = fmxBars('B'), b = fmxBars('E'); return [{ n: a[0] }, { n: a[1] }, { n: a[2] }, { n: a[3], end: true }, { start: true, n: b[0] }, { n: b[1] }, { n: b[2] }, { n: b[3], end: true }]; })();
const FMX_TER = (() => { const a = fmxBars('A'), b = fmxBars('C'); return [{ n: a[0] }, { n: a[1] }, { n: a[2] }, { n: a[3], fine: true }, { n: b[0] }, { n: b[1] }, { n: b[2] }, { n: b[3], dc: true }]; })();
const FMX_ORDER = { bin: [0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 4, 5, 6, 7], ter: [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3] };
const fmxRoadNotes = (bars, ord) => ord.flatMap(i => bars[i].n.map(n => ({ d: n[2], dur: n[1] })));
// the playing order in groups, one per section played: its bar numbers, its letter under them; cur: the group sounding
const FMX_GROUPS = { bin: [[[1, 2, 3, 4], 'A'], [[1, 2, 3, 4], 'A'], [[5, 6, 7, 8], 'B'], [[5, 6, 7, 8], 'B']], ter: [[[1, 2, 3, 4], 'A'], [[5, 6, 7, 8], 'B'], [[1, 2, 3, 4], 'A']] };
const fmxGroups = (kind, cur = -1, sz = 15, coralLast) => <div style={{display:'flex',justifyContent:'center',flexWrap:'wrap',gap:'8px 16px'}}>{FMX_GROUPS[kind].map(([ns, l], g) => { const now = g === cur, c = coralLast && g === FMX_GROUPS[kind].length - 1 ? PEN_C : PEN_N;
  return <div key={g} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6}}>
    <div style={{display:'flex',gap:3}}>{ns.map(n => <span key={n} style={{minWidth:sz * 1.5,textAlign:'center',fontSize:sz,fontWeight:900,padding:'1px 2px',borderRadius:5,border:'1.4px solid rgba(38,41,107,0.35)',color:now ? '#fff' : BK.ink,background:now ? PEN_N : 'transparent'}}>{n}</span>)}</div>
    <span style={{width:sz * 2.4,height:sz * 2.4,display:'inline-flex',alignItems:'center',justifyContent:'center',borderRadius:6,border:'1.8px solid ' + c,fontFamily:LB_SERIF,fontSize:sz * 1.55,fontWeight:900,color:now ? '#fff' : c,background:now ? c : '#fff'}}>{l}</span></div>; })}</div>;
// Korean: words that belong together never part at a line end
const fmxNbKo = (x) => typeof x !== 'string' ? x : chxNbKo(x).replace(/(2부|3부) 형식/g, '$1 형식').replace(/([AB]) (다음|부분)/g, '$1 $2').replace(/D\.C\. al Fine/g, 'D.C. al Fine')
  .replace(/(\d)마디 (\d)/g, '$1마디 $2').replace(/맨 (처음|끝)/g, '맨 $1').replace(/쉬는 음/g, '쉬는 음').replace(/프레이즈 표시/g, '프레이즈 표시')
  .replace(/(같은|다른|다음|새) (음악|글자)/g, '$1 $2').replace(/곡 전체/g, '곡 전체').replace(/글자 붙이기/g, '글자 붙이기').replace(/형식 이름 말하기/g, '형식 이름 말하기').replace(/첫 (번째|상자|프레이즈)/g, '첫 $1');
const fmxNth = (n) => n === 1 ? '첫 번째' : n + '번째';
const fmxKoT = (x) => LANG === 'ko' ? fmxNbKo(x) : x;

function fmxLbPages(scr = false) {
  const ch = 'form';
  const live = (still, comp) => <LbLive still={still} live={comp}/>;
  const stack = (nodes, h, gap = 12, mw = 680) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap,width:'100%',maxWidth:mw,margin:'0 auto',alignItems:'stretch'}}>{nodes}</div></LbPic>;
  const X = (en, ko) => sscT(en, skgKo(fmxNbKo(ko)));
  const cap = (x, key = 'cap') => <div key={key} style={{textAlign:'center',fontSize:scr ? 14 : 13.5,fontWeight:800,color:BK.ink,margin:'2px auto 0',maxWidth:560,lineHeight:1.35,textWrap:'balance'}}>{fmxKoT(x)}</div>;
  const B = (s) => <b>{s}</b>;
  const ch20 = bkChapterNo('signs'), ch8 = bkChapterNo('time-signatures');

  // p1 (macro first): the map of a piece
  const p1 = <LbLive still={stack([<FmxMapSvg key="m" label={t('The map of a piece. The piece: 24 bars. Its sections: A, B, then A again (coral), eight bars each. The phrases: a curve over each four bars, six in all. The bars: 1 to 24. Bar 1 opened up: four beats.', '곡의 지도. 곡 전체: 24마디. 부분: A, B, 그리고 다시 A(산호색), 8마디씩. 프레이즈: 4마디마다 곡선 하나, 모두 여섯. 마디: 1부터 24. 1마디를 펼치면: 네 박.')}/>,
    cap(t('Beats make bars, bars make phrases, phrases make sections, sections make the piece.', '박이 모여 마디, 마디가 모여 프레이즈, 프레이즈가 모여 부분, 부분이 모여 곡이 돼요.'))], 360, 10)} live={<FmxMapPad/>}/>;
  // p2: two phrases: phrase marks, resting notes coral
  const w2 = fmxVbw(['B'], true);
  const p2 = stack([<FmxRow key="a" ids={['B']} ts marks rest width={w2} n0={1} end={false} label={t('Bars 1 to 4: E G F G, A G F E, D E F D, G, all in one phrase mark; the last G coral.', '1~4마디: E G F G, A G F E, D E F D, G. 프레이즈 표시 하나로 묶여 있고, 마지막 G는 산호색이에요.')}/>,
    <FmxRow key="b" ids={['A']} tsRoom marks rest width={w2} n0={5} label={t('Bars 5 to 8: C D E F, G E C, D E F D, C, all in one phrase mark; the last C coral.', '5~8마디: C D E F, G E C, D E F D, C. 프레이즈 표시 하나로 묶여 있고, 마지막 C는 산호색이에요.')}/>,
    cap(t('Two phrases, four bars each. The first rests on G, the second on C.', '4마디씩 두 프레이즈. 첫 프레이즈는 G에서, 둘째 프레이즈는 C에서 쉬어요.'), 'c2')], 300, 30, 640);
  // p3: sixteen bars, four phrases: A A B A
  const w3 = fmxVbw(['A'], true), L3 = ['A', 'A', 'B', 'A'];
  const p3 = stack(L3.map((id, i) => <FmxRow key={i} ids={[id]} ts={i === 0} tsRoom={i > 0} end={i === 3} letters={[L3[i]]} coral={L3[i] === 'B' ? [0] : []} width={w3} n0={i * 4 + 1} label={t('Bars ' + (i * 4 + 1) + ' to ' + (i * 4 + 4) + ': phrase ' + L3[i] + '.', (i * 4 + 1) + '~' + (i * 4 + 4) + '마디: 프레이즈 ' + L3[i] + '.')}/>)
    .concat([cap(t('Same music, same letter: A A B A.', '같은 음악은 같은 글자: A A B A.'), 'c3')]), 420, 4, 640);
  // p4: binary
  const p4 = stack([<SgnRoad key="r" bars={FMX_BIN} rows={[[0, 3], [4, 7]]} rw={560} o={{ ts: 4, nums: true, coral: ['start', 'end'] }} label={t('Eight bars in two sections. Bars 1 to 4 end with an end-repeat sign; bars 5 to 8 start with a start-repeat sign and end with an end-repeat sign.', '두 부분, 여덟 마디. 1~4마디 끝에 끝 도돌이표, 5~8마디 앞에 시작 도돌이표, 끝에 끝 도돌이표.')}/>,
    <React.Fragment key="g">{fmxGroups('bin', -1, 16)}</React.Fragment>, cap(t('Played: A A B B. Two sections, each twice: binary form.', '치는 차례: A A B B. 두 부분을 두 번씩: 2부 형식.'), 'c4')], 330, 22, 640);
  // p5: ternary
  const p5 = stack([<SgnRoad key="r" bars={FMX_TER} rows={[[0, 3], [4, 7]]} rw={560} o={{ ts: 4, nums: true, coral: ['fine', 'dc'] }} label={t('Eight bars. Fine over the end of bar 4; D.C. al Fine over the end of bar 8.', '여덟 마디. 4마디 끝 위에 Fine, 8마디 끝 위에 D.C. al Fine.')}/>,
    <React.Fragment key="g">{fmxGroups('ter', -1, 16, true)}</React.Fragment>, cap(t('Played: A B A. A comes back: ternary form.', '치는 차례: A B A. A가 돌아오니까 3부 형식.'), 'c5')], 330, 22, 640);
  // p6: find the form: four steps on a map of blocks
  const step = (n, en, ko, node) => <div key={n} style={{display:'grid',gridTemplateColumns:'34px minmax(0,1fr) 270px',alignItems:'center',gap:14}}>
    <span style={{width:30,height:30,borderRadius:15,background:PEN_N,color:'#fff',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:900,fontSize:16}}>{n}</span>
    <span style={{fontSize:16.5,fontWeight:800,color:BK.ink,lineHeight:1.3}}>{fmxKoT(t(en, ko))}</span><span>{node}</span></div>;
  const blocks = (ls, opts = {}) => <svg viewBox="0 0 230 50" style={{width:'100%',display:'block'}} aria-hidden="true">{ls.map((l, i) => { const w = 230 / ls.length, c = opts.coral === i ? PEN_C : PEN_N;
    return <g key={i}><rect x={i * w + 7} y={5} width={w - 14} height={40} rx={5} fill="#fff" stroke={c} strokeWidth="1.6" strokeDasharray={l === '?' ? '4 3' : undefined}/>{opts.dbl && i < ls.length - 1 && <g><line x1={(i + 1) * w - 2} x2={(i + 1) * w - 2} y1={2} y2={48} stroke={PEN_N} strokeWidth="1.4"/><line x1={(i + 1) * w + 2} x2={(i + 1) * w + 2} y1={2} y2={48} stroke={PEN_N} strokeWidth="1.4"/></g>}
      {Array.isArray(l) ? <g fill={c} textAnchor="middle" fontWeight="900" style={{fontFamily:'Inter, sans-serif'}}><text x={i * w + w / 2} y={24} fontSize="14">{l[0]}</text><text x={i * w + w / 2} y={38} fontSize="10.5" fill={BK.muted}>{l[1]}</text></g>
        : <text x={i * w + w / 2} y={32} textAnchor="middle" fontSize={22} fontWeight="900" fill={c} style={{fontFamily:LB_SERIF}}>{l}</text>}</g>; })}</svg>;
  const p6 = stack([step(1, 'Find the sections: double bar lines, repeat signs, Fine.', '부분 찾기: 겹세로줄, 도돌이표, Fine.', blocks(['?', '?', '?'], { dbl: true })),
    step(2, 'Listen to each section: the same music as A, or new?', '부분마다 들어요: A와 같은 음악인가요, 새 음악인가요?', blocks([['1–8', t('bars', '마디')], ['9–16', t('bars', '마디')], ['17–24', t('bars', '마디')]])),
    step(3, 'Same music, same letter; new music, the next letter.', '같은 음악은 같은 글자, 새 음악은 다음 글자.', blocks(['A', 'B', 'A'], { coral: 2 })),
    step(4, 'Name the form: A B is binary, A B A is ternary.', '형식 이름 말하기: A B는 2부 형식, A B A는 3부 형식.', <div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:24,fontWeight:900,color:PEN_C}}>{t('ternary', '3부 형식')}</div>)], 330, 40, 680);

  // the check icons
  const tx = (x, c, col, s = 18, y = 28) => '<text x="' + x + '" y="' + y + '" text-anchor="middle" style="font-family:Georgia, serif" font-size="' + s + '" font-weight="900" fill="' + col + '">' + c + '</text>';
  const box = (x, l, col) => '<rect x="' + (x - 11) + '" y="10" width="22" height="22" rx="3" fill="#fff" stroke="' + col + '" stroke-width="1.6"/>' + tx(x, l, col, 15, 27);
  const ic = {
    map: [{ k: 'raw', svg: '<rect x="6" y="6" width="80" height="9" rx="2" fill="none" stroke="' + PEN_N + '" stroke-width="1.4"/>' + [6, 33, 60].map((x, i) => '<rect x="' + (x + 1) + '" y="20" width="24" height="14" rx="2" fill="none" stroke="' + (i === 2 ? PEN_C : PEN_N) + '" stroke-width="1.4"/>').join('') }],
    phrase: [{ k: 'raw', svg: [18, 34, 50].map(x => '<ellipse cx="' + x + '" cy="14" rx="4.4" ry="3.1" fill="' + PEN_N + '"/>').join('') + '<ellipse cx="72" cy="14" rx="5.4" ry="3.8" fill="none" stroke="' + PEN_C + '" stroke-width="2"/><path d="M10 22 Q46 42 82 22" fill="none" stroke="' + PEN_N + '" stroke-width="2"/>' }],
    letters: [{ k: 'raw', svg: box(14, 'A', PEN_N) + box(36, 'A', PEN_N) + box(58, 'B', PEN_C) + box(80, 'A', PEN_N) }],
    binary: [{ k: 'raw', svg: box(26, 'A', PEN_N) + box(64, 'B', PEN_N) + '<circle cx="42" cy="17" r="1.8" fill="' + PEN_N + '"/><circle cx="42" cy="25" r="1.8" fill="' + PEN_N + '"/><line x1="45.5" x2="45.5" y1="8" y2="34" stroke="' + PEN_N + '" stroke-width="2.6"/>' }],
    ternary: [{ k: 'raw', svg: box(18, 'A', PEN_N) + box(46, 'B', PEN_N) + box(74, 'A', PEN_C) }],
  };
  const checksRows = [
    ['map', t('I can show a piece’s sections, phrases, bars and beats on its map', '곡의 지도에서 부분, 프레이즈, 마디, 박을 보여 줄 수 있어요')],
    ['phrase', t('I can find the phrases of a tune and play each to its resting note', '선율의 프레이즈를 찾고, 쉬는 음까지 하나씩 칠 수 있어요')],
    ['letters', t('I can give each phrase a letter: same music, same letter', '프레이즈마다 글자를 붙일 수 있어요: 같은 음악은 같은 글자')],
    ['binary', t('I can play a piece in binary form and say A A B B', '2부 형식 곡을 치고 A A B B라고 말할 수 있어요')],
    ['ternary', t('I can play a piece in ternary form and say A B A', '3부 형식 곡을 치고 A B A라고 말할 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? skgKo(sscNbKo(fmxNbKo(x))) : sscNbEn(x)]);

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <>곡이 짜인 모양이 <b>형식</b>이에요. 같은 음악은 같은 글자로, 새 음악은 다음 글자로 나타내요.</> : <><b>Form</b> is how a piece is built. Same music gets the same letter; new music gets the next letter.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('The phrase', '프레이즈'), 2], [t('Same or different', '같은 음악, 새 음악'), 3], [t('Binary form', '2부 형식'), 4], [t('Ternary form', '3부 형식'), 5], [t('Finding the form', '형식 찾기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}<span>{n}</span></span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)',textWrap:'pretty'}}>{bkGoal(15)}<span>{x.replace(/^I can /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The phrase', '프레이즈')}>
      {live(p2, <FmxPhrasePad/>)}
      <LbDefs items={[
        [t('phrase', '프레이즈'), X('A musical sentence: often four bars, ending on a resting note.', '음악의 한 문장. 보통 4마디이고, 쉬는 음에서 끝나요.')],
        [t('phrase mark', '프레이즈 표시'), X('A long curve over or under a phrase. Its notes are played smoothly, as one idea.', '프레이즈 위나 아래의 긴 곡선. 그 음들을 한 덩어리로 매끄럽게 쳐요.')],
        [t('resting note', '쉬는 음'), X('The note a phrase comes to rest on, at its end. It is often long.', '프레이즈가 끝에서 머무는 음. 보통 길어요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the picture’s two phrases. Lift your hand a little after each resting note.', '그림의 두 프레이즈를 쳐요. 쉬는 음이 끝날 때마다 손을 살짝 들어요.'),
        X('In a piece you know, find the phrases. Count the bars in each.', '아는 곡에서 프레이즈를 찾아요. 프레이즈마다 마디를 세어요.'),
      ]}/>
      <LbRemember>{X('A phrase ends on a resting note.', '프레이즈는 쉬는 음에서 끝나요.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Same or different', '같은 음악, 새 음악')}>
      {live(p3, <FmxLetterPad/>)}
      <LbDefs items={[
        [t('repetition', '반복'), X('The same music again.', '같은 음악이 다시 나오는 것.')],
        [t('contrast', '대조'), X('New music, different from what came before.', '앞과 다른 새 음악.')],
        [t('letters', '글자'), X('The first music is A. Same music, same letter; new music, the next letter: B, then C.', '처음 음악은 A. 같은 음악은 같은 글자, 새 음악은 다음 글자: B, 그다음 C.')],
      ]}/>
      <LbPiano steps={[
        X('Play the four phrases. Say each one’s letter as you start it.', '네 프레이즈를 쳐요. 프레이즈를 시작할 때마다 글자를 말해요.'),
        X('Your teacher plays two phrases. Say: same or different?', '선생님이 프레이즈 두 개를 쳐요. 같은지 다른지 말해요.'),
      ]}/>
      <LbRemember>{X('Same music, same letter.', '같은 음악은 같은 글자.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Binary form', '2부 형식')}>
      {live(p4, <FmxRoadPad kind="bin"/>)}
      <LbDefs items={[
        [t('section', '부분'), X('A large part of a piece, one or more phrases long. It often ends with a double bar line or a repeat sign.', '곡을 크게 나눈 한 덩어리. 프레이즈 하나 이상으로 되어 있고, 끝에 보통 겹세로줄이나 도돌이표가 있어요.')],
        [t('binary form', '2부 형식'), X('Two sections, A and B, often each played twice (chapter ' + ch20 + '’s repeat signs).', '두 부분 A와 B. 보통 부분마다 두 번씩 쳐요(' + ch20 + '챕터의 도돌이표).')],
      ]}/>
      <LbPiano steps={[
        X('Play the picture, with both repeats. Say A A B B as you go.', '도돌이표를 지켜 그림을 쳐요. 치면서 A A B B라고 말해요.'),
        X('Point to where A ends and where B starts.', 'A가 끝나는 곳과 B가 시작하는 곳을 짚어요.'),
      ]}/>
      <LbRemember>{X('Binary: A B.', '2부 형식: A B.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Ternary form', '3부 형식')}>
      {live(p5, <FmxRoadPad kind="ter"/>)}
      <LbDefs items={[
        [t('ternary form', '3부 형식'), X('Three sections: A, then B, then A again.', '세 부분: A, 그다음 B, 그리고 다시 A.')],
        [t('the return', '돌아오기'), X('A coming back after B. It is often written with D.C. al Fine (chapter ' + ch20 + ').', 'B 다음에 A가 다시 나오는 것. 보통 D.C. al Fine(' + ch20 + '챕터)으로 적어요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the picture: A, B, then D.C. back to A, and stop at Fine.', '그림을 쳐요: A, B, 그다음 D.C.에서 A로 돌아가 Fine에서 멈춰요.'),
        X('Play A, then make up your own B, then play A again.', 'A를 치고, 나만의 B를 지어 친 다음, 다시 A를 쳐요.'),
      ]}/>
      <LbRemember>{X('Ternary: A B A.', '3부 형식: A B A.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Finding the form', '형식 찾기')}>
      {live(p6, <FmxFindPad/>)}
      <LbDefs items={[
        [t('form', '형식'), X('How a piece is built: the order of its sections, shown with letters.', '곡이 짜인 모양. 부분을 찾아 글자로 나타내요.')],
        [t('double bar line', '겹세로줄'), X('Two bar lines close together. Two thin lines end a section; a thin and a thick line end the piece (chapter ' + ch8 + ').', '가는 세로줄 두 개. 부분의 끝에 써요(곡의 끝에는 끝세로줄, ' + ch8 + '챕터).')],
      ]}/>
      <LbPiano steps={[
        X('Take a piece you are learning. Find its sections and give them letters.', '배우고 있는 곡을 펴요. 부분을 찾아 글자를 붙여요.'),
        X('Play it and say each letter as it starts. Then name the form.', '치면서 부분이 시작될 때마다 글자를 말해요. 그다음 형식 이름을 말해요.'),
      ]}/>
      <LbRemember>{X('Find the sections, give the letters, name the form.', '부분 찾기, 글자 붙이기, 형식 이름 말하기.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (1 to 5). The check-up on paper is in the Workbook.', '1~5쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_fmx_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, x])}/>}/>
    </LbPage>,
  ];
}
function FormLessonBook() { return <>{fmxLbPages(false)}</>; }
