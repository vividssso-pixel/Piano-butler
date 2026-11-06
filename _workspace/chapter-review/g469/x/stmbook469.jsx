// ─── Phase 469: chapter 13 (Tempo Race): the Lesson Book, built in full under Book rules 14 and 15 (her 2026-10-14
// 09:17 '계속 가줘 최종검토는 한꺼번에하게'). The level plan's scope for room 13 (Level 3): slow to fast, Adagio, Andante,
// Moderato, Allegro; the metronome (AMEB Preliminary). rit., a tempo and the other words are the drill's extra level.
// It builds on chapter 3 (a steady beat, counting 1 2 3 4) and chapter 5 (the crotchet, ♩, one beat).
// The four words sound at one speed each everywhere (Adagio 70, Andante 90, Moderato 110, Allegro 140): six seconds
// hold exactly 7, 9, 11 and 14 beats. Real music gives each word a span of speeds (the Teacher copy gives them).

const STM_WORDS = [
  { w: 'Adagio', bpm: 70, en: 'Slow. Italian for ‘at ease’.', ko: '느리게. 이탈리아어로 ‘편안하게’.', short: () => t('slow', '느리게') },
  { w: 'Andante', bpm: 90, en: 'At a walking pace. Italian for ‘walking’.', ko: '걷는 빠르기로. 이탈리아어로 ‘걸어가는’.', short: () => t('at a walking pace', '걷는 빠르기로') },
  { w: 'Moderato', bpm: 110, en: 'At a medium speed.', ko: '보통 빠르기로.', short: () => t('at a medium speed', '보통 빠르기로') },
  { w: 'Allegro', bpm: 140, en: 'Fast and lively. Italian for ‘cheerful’.', ko: '빠르고 경쾌하게. 이탈리아어로 ‘즐거운’.', short: () => t('fast and lively', '빠르고 경쾌하게') },
];
const STM_W = (w) => STM_WORDS.find(x => x.w === w);
const STM_KO = { Adagio: '아다지오', Andante: '안단테', Moderato: '모데라토', Allegro: '알레그로' };
const STM_FONT = "'Playfair Display', Georgia, serif";
const STM_SW = { stroke: PEN_N, strokeWidth: 1.7, strokeLinecap: 'round', strokeLinejoin: 'round', fill: 'none' };
// a tempo word as printed music shows it: bold and upright
const stmWordSvg = (x, y, w, o = {}) => <text x={x} y={y} textAnchor={o.a || 'start'} fontWeight="900" fontSize={o.size || 15} fill={o.c || PEN_N} style={{fontFamily:STM_FONT}}>{w}</text>;
// a crotchet and '= n' (a metronome mark), its baseline at y
function StmMark({ x, y, n, size = 14, c = PEN_N, anchor = 'start' }) {
  const k = size / 14, w = (n === undefined ? 0 : String(n).length * 8.4 + 18) * k, x0 = anchor === 'middle' ? x - (w + 10 * k) / 2 : x;
  return <g><ellipse cx={x0 + 4.6 * k} cy={y - 3.2 * k} rx={4.6 * k} ry={3.4 * k} transform={'rotate(-22 ' + (x0 + 4.6 * k) + ' ' + (y - 3.2 * k) + ')'} fill={c}/>
    <line x1={x0 + 8.8 * k} x2={x0 + 8.8 * k} y1={y - 4 * k} y2={y - 19 * k} stroke={c} strokeWidth={1.4 * k}/>
    {n !== undefined && <text x={x0 + 14 * k} y={y} fontSize={size} fontWeight="900" fill={c}>= {n}</text>}</g>;
}
// a metronome: (x, y) the middle of its foot, h tall; swing the rod's angle; wt the weight, 0 at the top (slow) to 1 low
// (fast); nums: the scale's numbers; words: the tempo words beside the scale
function StmMetronome({ x, y, h = 160, swing = 0, wt = 0.35, nums, words, fs = 1, ww = 0.06 }) {
  const X = (v) => x + v * h, Y = (v) => y - v * h, pv = [x, Y(0.2)], len = 0.86 * h, wy = 0.8 - wt * 0.42;
  const scaleY = (n) => Y(0.84) + (Math.log(n / 40) / Math.log(208 / 40)) * (Y(0.34) - Y(0.84));
  return <g>
    <path d={'M' + X(-0.36) + ' ' + y + ' L' + X(-0.11) + ' ' + Y(1) + ' L' + X(0.11) + ' ' + Y(1) + ' L' + X(0.36) + ' ' + y + ' Z'} {...STM_SW} fill="#fff" strokeWidth={2}/>
    <rect x={X(-0.42)} y={y} width={0.84 * h} height={0.05 * h} rx="2" fill={PEN_N}/>
    <rect x={X(-0.13)} y={Y(0.88)} width={0.26 * h} height={0.57 * h} rx="2" fill="#fff" stroke={PEN_N} strokeWidth="1"/>
    {nums && nums.map(n => <g key={n}><line x1={X(-0.13)} x2={X(-0.11)} y1={scaleY(n)} y2={scaleY(n)} stroke={PEN_N} strokeWidth="0.8"/><text x={X(-0.105)} y={scaleY(n) + 3.2} textAnchor="start" fontSize={9 * fs} fontWeight="800" fill={PEN_N}>{n}</text></g>)}
    {words && words.map(([w, n]) => <g key={w}><line x1={X(0.13)} x2={X(0.34)} y1={scaleY(n)} y2={scaleY(n)} stroke={PEN_C} strokeWidth="1" strokeDasharray="2 2"/>{stmWordSvg(X(0.36), scaleY(n) + 4.5, w, { size: 13 * fs, c: PEN_C })}</g>)}
    <g transform={'rotate(' + swing + ' ' + pv[0] + ' ' + pv[1] + ')'}>
      <line x1={pv[0]} x2={pv[0]} y1={pv[1]} y2={pv[1] - len} stroke={PEN_N} strokeWidth="2.4" strokeLinecap="round"/>
      <path d={'M' + (x - ww * h) + ' ' + Y(wy) + ' L' + (x + ww * h) + ' ' + Y(wy) + ' L' + (x + ww * 0.6 * h) + ' ' + Y(wy - 0.075) + ' L' + (x - ww * 0.6 * h) + ' ' + Y(wy - 0.075) + ' Z'} fill={PEN_C}/>
    </g>
    <circle cx={pv[0]} cy={pv[1]} r={0.025 * h} fill={PEN_N}/>
  </g>;
}
// beat dots: one at each beat of bpm from 0 to secs seconds, s pixels a second
// the drawn crotchet mark inside running text (kept clear of a hanging indent)
const stmMm = (n) => <span style={{display:'inline-flex',alignItems:'baseline',gap:3,textIndent:0,whiteSpace:'nowrap',fontWeight:900,color:'inherit'}}><svg viewBox="8 16 26 54" style={{height:'1.3em',width:'0.62em',display:'inline-block',alignSelf:'baseline',transform:'translateY(0.2em)'}} aria-hidden="true"><NoteShape base={1} cx={16} ink={BK.ink}/></svg>= {n}</span>;
const stmWt = (n) => Math.log(n / 40) / Math.log(208 / 40);
const stmBeats = (bpm, secs) => { const out = []; for (let tt = 0; tt < secs - 1e-6; tt += 60 / bpm) out.push(tt); return out; };
const stmDotsRow = (x0, y, times, s, o = {}) => <g>{times.map((tt, i) => <circle key={i} cx={x0 + tt * s} cy={y} r={o.r || 6} fill={i === 0 && o.first ? PEN_C : o.fill || PEN_N}/>)}</g>;
// the chapter's tunes (right hand, C position, none of them a song), shared with the screen and the Workbook
const STM_ROWS = {
  walk: [['ts', 4], ['q', 1, 28], ['q', 1, 29], ['q', 1, 30], ['q', 1, 31], ['|'], ['w', 4, 32], ['||']],
  hill: [['ts', 4], ['q', 1, 28], ['q', 1, 30], ['q', 1, 32], ['q', 1, 30], ['|'], ['q', 1, 29], ['q', 1, 31], ['h', 2, 28], ['||']],
  waltz: [['ts', 3], ['q', 1, 32], ['q', 1, 31], ['q', 1, 30], ['|'], ['q', 1, 29], ['q', 1, 30], ['q', 1, 31], ['|'], ['hd', 3, 32], ['||']],
  steps: [['ts', 4], ['q', 1, 32], ['q', 1, 31], ['q', 1, 30], ['q', 1, 29], ['|'], ['q', 1, 28], ['q', 1, 29], ['h', 2, 30], ['||']],
};
const STM_LETTER = { 28: 'C', 29: 'D', 30: 'E', 31: 'F', 32: 'G' };
// a tune with its tempo word over the first bar (and the metronome mark beside it when mark is set)
function StmTune({ items, word, mark, width, k = {}, o = {}, wordCol, full = true, label }) {
  return <SdyStaff full={full} width={width} items={items} o={{ D: 24, ...o }} k={k} room={word ? 30 : 0} label={label}
    extra={(yOf) => word ? <g>{stmWordSvg(6, yOf(38, 'treble') - 24, word, { size: 15, c: wordCol || PEN_N })}{mark && <StmMark x={6 + word.length * 9.6 + 12} y={yOf(38, 'treble') - 24} n={mark} size={13}/>}</g> : null}/>;
}

function stmLbPages(scr = false) {
  const ch = 'tempo', fs = scr ? 1.35 : 1;
  const live = (still, comp) => <LbLive still={still} live={<>{still}{comp}</>}/>;
  const pic = (node, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{node}</div></LbPic>;
  const svg = (vb, kids, label) => <svg viewBox={vb} style={{width:'100%',display:'block'}} role="img" aria-label={label}>{kids}</svg>;
  const tx = (x, y, s, o = {}) => <text x={x} y={y} textAnchor={o.a || 'middle'} fontSize={(o.size || 12) * fs} fontWeight={o.w || 900} fill={o.c || PEN_N} paintOrder="stroke" stroke="#fff" strokeWidth={o.halo ? 4 : 0} strokeLinejoin="round">{s}</text>;

  // 1. the tempo dial: the four words round an arc, slow on the left, fast on the right; a metronome beside it
  const dial = (cx, cy, r) => { const ang = (i) => Math.PI * (1 - (i + 0.5) / 4), at = (i, rr) => [cx + rr * Math.cos(ang(i)), cy - rr * Math.sin(ang(i))];
    return <g>
      <path d={'M' + (cx - r) + ' ' + cy + ' A' + r + ' ' + r + ' 0 0 1 ' + (cx + r) + ' ' + cy} fill="none" stroke={PEN_N} strokeWidth="2.2"/>
      {[0, 1, 2, 3, 4].map(i => { const a = Math.PI * (1 - i / 4); return <line key={i} x1={cx + (r - 9) * Math.cos(a)} x2={cx + (r + 3) * Math.cos(a)} y1={cy - (r - 9) * Math.sin(a)} y2={cy - (r + 3) * Math.sin(a)} stroke={PEN_N} strokeWidth="1.6"/>; })}
      {STM_WORDS.map((x, i) => { const [px, py] = at(i, r + 20); return <g key={x.w}>{stmWordSvg(px, py + 5, x.w, { a: i < 2 ? 'end' : 'start', size: 15 * fs })}</g>; })}
      <line x1={cx} y1={cy} x2={at(1, r - 18)[0]} y2={at(1, r - 18)[1]} stroke={PEN_C} strokeWidth="3.4" strokeLinecap="round"/><circle cx={cx} cy={cy} r="7" fill={PEN_C}/>
      {tx(cx - r, cy + 22, t('slower', '더 느리게'), { size: 11.5, c: PEN_C })}{tx(cx + r, cy + 22, t('faster', '더 빠르게'), { size: 11.5, c: PEN_C })}
    </g>; };
  const p1 = svg('0 0 620 322', <>
    <StmMetronome x={104} y={292} h={252} swing={-14} wt={0.45}/>
    {dial(394, 254, 140)}
  </>, t('A metronome with its rod swinging, and a dial like a car’s speedometer: Adagio and Andante on the slow side, Moderato and Allegro on the fast side; the needle points to Andante.', '막대가 흔들리는 메트로놈, 그리고 자동차 속도계 같은 다이얼: 느린 쪽에 아다지오와 안단테, 빠른 쪽에 모데라토와 알레그로. 바늘은 안단테를 가리켜요.'));

  // 2. the same tune slow and fast, on a ruler of seconds
  const s2 = 48, x2 = 70, sec = (n) => x2 + n * s2;
  const beatRow = (y, spb, lab) => { const notes = [['C', 0], ['D', 1], ['E', 2], ['F', 3], ['G', 4]];
    return <g>{tx(x2 - 14, y + 4, lab, { a: 'end', size: 12.5 })}
      {[0, 1, 2, 3, 4, 5, 6, 7].map(b => <circle key={b} cx={sec(b * spb)} cy={y} r={b < 5 ? 7 : 4.5} fill={b < 5 ? PEN_N : '#fff'} stroke={PEN_N} strokeWidth={b < 5 ? 0 : 1.4}/>)}
      <line x1={sec(4 * spb) + 8} x2={sec(7 * spb)} y1={y} y2={y} stroke={PEN_N} strokeWidth="1.2" strokeDasharray="3 3"/>
      {notes.map(([L, b]) => <g key={L}>{tx(sec(b * spb), y - 13, L, { size: 12 })}</g>)}
      {tx(sec(8 * spb) + 10, y + 4, spb === 1 ? t('8 seconds', '8초') : t('4 seconds', '4초'), { a: 'start', size: 11.5, c: PEN_C })}</g>; };
  const p2 = svg('0 0 540 270', <>
    <line x1={x2} x2={sec(8)} y1={34} y2={34} stroke={PEN_N} strokeWidth="1.2"/>
    {[0, 1, 2, 3, 4, 5, 6, 7, 8].map(n => <g key={n}><line x1={sec(n)} x2={sec(n)} y1={28} y2={40} stroke={PEN_N} strokeWidth="1.2"/>{tx(sec(n), 22, String(n), { size: 10.5, w: 800 })}</g>)}
    {tx(x2 - 14, 38, t('seconds', '초'), { a: 'end', size: 11, w: 800 })}
    {beatRow(118, 1, t('slow', '느리게'))}
    {beatRow(222, 0.5, t('fast', '빠르게'))}
  </>, t('A ruler of seconds from 0 to 8. The tune C D E F G, one dot for each beat (the long G holds for four). Slow: one beat each second, 8 seconds. Fast: two beats each second, 4 seconds.', '0초부터 8초까지 초 눈금자. 선율 C D E F G, 박마다 점 하나 (긴 G는 네 박). 느리게: 1초에 한 박, 8초. 빠르게: 1초에 두 박, 4초.'));
  const p2tune = <div style={{maxWidth:500,margin:'0 auto 14px',width:'100%'}}><StmTune items={STM_ROWS.walk} label={t('The tune: C D E F, then a long G.', '선율: C D E F, 그리고 긴 G.')}/></div>;

  // 3. four lanes, six seconds each: 7, 9, 11 and 14 beats
  const s3 = 58, x3 = 118;
  const p3 = svg('0 0 540 396', <>
    <line x1={x3} x2={x3 + 6 * s3} y1={26} y2={26} stroke={PEN_N} strokeWidth="1.2"/>
    {[0, 1, 2, 3, 4, 5, 6].map(n => <g key={n}><line x1={x3 + n * s3} x2={x3 + n * s3} y1={20} y2={32} stroke={PEN_N} strokeWidth="1.2"/></g>)}
    {tx(x3 + 3 * s3, 13, t('6 seconds', '6초'), { size: 11.5, w: 800 })}
    {STM_WORDS.map((x, i) => { const y = 92 + i * 86, beats = stmBeats(x.bpm, 6);
      return <g key={x.w}><line x1={x3 - 6} x2={x3 + 6 * s3 + 6} y1={y + 40} y2={y + 40} stroke="rgba(38,41,107,0.18)" strokeWidth="1"/>
        {stmWordSvg(x3 - 14, y + 5, x.w, { a: 'end', size: 15 * fs })}{stmDotsRow(x3, y, beats, s3, { r: 8 })}
        {tx(x3 + 6 * s3 + 14, y + 4, t(beats.length + ' beats', beats.length + '박'), { a: 'start', size: 11.5, c: PEN_C })}</g>; })}
  </>, t('Four lanes, six seconds each. Adagio: 7 beats. Andante: 9 beats. Moderato: 11 beats. Allegro: 14 beats. The faster the tempo, the more beats in the same time.', '네 줄, 각각 6초. 아다지오: 7박. 안단테: 9박. 모데라토: 11박. 알레그로: 14박. 빠를수록 같은 시간에 박이 더 많아요.'));

  // 4. where the word goes: two pieces' first bars
  const piece = (title, word, items) => <div style={{display:'flex',flexDirection:'column',gap:2,width:'100%'}}>
    <div style={{textAlign:'center',fontFamily:STM_FONT,fontWeight:800,fontSize:15 * fs,color:BK.ink}}>{title}</div>
    <StmTune items={items} word={word} wordCol={PEN_C} label={t(title + ': the word ' + word + ' over the first bar, above the staff.', title + ': 첫 마디 위, 오선 위에 ' + word + '.')}/></div>;
  const p4 = <div style={{display:'flex',flexDirection:'column',gap:30,width:'100%',maxWidth:560,margin:'0 auto'}}>
    {piece(t('Morning Walk', '아침 산책'), 'Andante', STM_ROWS.hill)}{piece(t('Spinning Top', '팽이'), 'Allegro', STM_ROWS.waltz)}
    <div style={{textAlign:'center',fontSize:13 * fs,fontWeight:900,color:BK.coral}}>{t('The tempo word: at the start, above the staff, in bold.', '빠르기말: 맨 앞, 오선 위, 굵은 글씨.')}</div>
  </div>;

  // 5. the metronome and two metronome marks
  const p5 = svg('0 0 560 380', <>
    <StmMetronome x={146} y={356} h={336} swing={0} wt={stmWt(90)} ww={0.03} nums={[40, 60, 80, 100, 120, 144, 176, 208]} words={STM_WORDS.map(x => [x.w, x.bpm])} fs={fs}/>
    {[[60, 110, t('one beat a second', '1초에 한 박')], [120, 246, t('two beats a second', '1초에 두 박')]].map(([n, y, lab]) => { const x0 = 350, s = 180;
      return <g key={n}><StmMark x={x0} y={y} n={n} size={17 * fs}/>{tx(x0 + 80 * fs, y, lab, { a: 'start', size: 12, c: PEN_C })}
        <line x1={x0} x2={x0 + s} y1={y + 34} y2={y + 34} stroke={PEN_N} strokeWidth="1"/><line x1={x0} x2={x0} y1={y + 29} y2={y + 39} stroke={PEN_N} strokeWidth="1"/><line x1={x0 + s} x2={x0 + s} y1={y + 29} y2={y + 39} stroke={PEN_N} strokeWidth="1"/>
        {stmDotsRow(x0 + 8, y + 22, stmBeats(n, 2), s / 2, { r: 6 })}
        {tx(x0 + s / 2, y + 52, t('2 seconds', '2초'), { size: 10.5, w: 800 })}</g>; })}
  </>, t('A metronome. Its scale runs from 40 at the top to 208 at the bottom, with Adagio, Andante, Moderato and Allegro beside their numbers; the weight slides on the rod. Beside it: crotchet = 60, one beat a second, 2 beats in 2 seconds; crotchet = 120, two beats a second, 4 beats in 2 seconds.', '메트로놈. 눈금은 위의 40부터 아래의 208까지, 숫자 옆에 아다지오, 안단테, 모데라토, 알레그로. 추는 막대 위를 미끄러져요. 옆에: 4분음표 = 60, 1초에 한 박, 2초에 2박; 4분음표 = 120, 1초에 두 박, 2초에 4박.'));

  // 6. steady, rushing, dragging
  const rows6 = [['steady', [0, 1, 2, 3, 4, 5, 6, 7].map(i => i * 54)], ['rush', [0, 54, 104, 150, 192, 230, 264, 294]], ['drag', [0, 54, 110, 170, 234, 302, 374, 450].map(v => v * 0.86)]];
  const lab6 = { steady: t('steady', '꾸준하게'), rush: t('rushing', '서두르기'), drag: t('dragging', '처지기') };
  const sub6 = { steady: t('the same gap every time', '매번 똑같은 간격'), rush: t('the beats get closer and closer', '박이 점점 가까이'), drag: t('the beats get further and further apart', '박이 점점 멀리') };
  const p6 = svg('0 0 540 414', <>
    {tx(100, 20, t('the ticks', '똑딱 소리'), { a: 'end', size: 11, w: 800, c: BK.muted })}
    {rows6.map(([k, xs], i) => { const y = 56 + i * 136;
      return <g key={k}>{tx(100, y + 5, lab6[k], { a: 'end', size: 13.5, c: k === 'steady' ? PEN_N : PEN_C })}
        {[0, 1, 2, 3, 4, 5, 6, 7].map(j => <line key={'t' + j} x1={122 + j * 54} x2={122 + j * 54} y1={y - 34} y2={y - 18} stroke="rgba(38,41,107,0.45)" strokeWidth="2"/>)}
        {xs.map((x, j) => <circle key={j} cx={122 + x} cy={y} r="9.5" fill={k === 'steady' || j < 3 ? PEN_N : PEN_C}/>)}
        {tx(122, y + 38, sub6[k], { a: 'start', size: 11.5, w: 800, c: k === 'steady' ? PEN_N : PEN_C })}</g>; })}
  </>, t('Three rows of eight beats, with the metronome’s ticks above each row. Steady: the same gap every time, each beat on its tick. Rushing: the gaps get smaller, the beats closer and closer. Dragging: the gaps get bigger, the beats further and further apart.', '여덟 박이 세 줄, 줄마다 위에 메트로놈 똑딱 소리. 꾸준하게: 매번 똑같은 간격, 박마다 똑딱 소리에 맞아요. 서두르기: 간격이 줄어 박이 점점 가까이. 처지기: 간격이 늘어 박이 점점 멀리.'));

  // the check icons
  const ic = {
    speed: [{ k: 'raw', svg: [0, 1, 2, 3].map(i => '<circle cx="' + (10 + i * 22) + '" cy="12" r="4" fill="' + PEN_N + '"/>').join('') + [0, 1, 2, 3, 4, 5, 6, 7].map(i => '<circle cx="' + (10 + i * 10) + '" cy="30" r="3.4" fill="' + PEN_C + '"/>').join('') }],
    words: [{ k: 'raw', svg: '<path d="M16 38 A30 30 0 0 1 76 38" fill="none" stroke="' + PEN_N + '" stroke-width="2"/><line x1="46" y1="38" x2="60" y2="18" stroke="' + PEN_C + '" stroke-width="3" stroke-linecap="round"/><circle cx="46" cy="38" r="3.5" fill="' + PEN_C + '"/>' }],
    read: [{ k: 'raw', svg: [16, 22, 28, 34, 40].map(y => '<line x1="6" x2="86" y1="' + y + '" y2="' + y + '" stroke="' + PEN_N + '" stroke-width="1"/>').join('') + '<rect x="6" y="2" width="34" height="9" rx="2" fill="' + PEN_C + '"/>' }],
    metro: [{ k: 'raw', svg: '<path d="M30 38 L40 3 L52 3 L62 38 Z" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.6"/><line x1="46" y1="32" x2="56" y2="6" stroke="' + PEN_N + '" stroke-width="2"/><rect x="49" y="15" width="7" height="5" fill="' + PEN_C + '"/>' }],
    steady: [{ k: 'raw', svg: [0, 1, 2, 3, 4, 5].map(i => '<circle cx="' + (10 + i * 14.5) + '" cy="20" r="4.5" fill="' + (i === 0 ? PEN_C : PEN_N) + '"/>').join('') }],
  };
  const checksRows = [
    ['speed', t('I can say what tempo is, and play a tune slow and fast', '빠르기가 무엇인지 말하고, 선율을 느리게 또 빠르게 칠 수 있어요')],
    ['words', t('I can put Adagio, Andante, Moderato and Allegro in order and say what each means', '아다지오, 안단테, 모데라토, 알레그로를 느린 것부터 차례대로 말하고 뜻을 말할 수 있어요')],
    ['read', t('I can find the tempo word in the music and count in at that tempo', '악보에서 빠르기말을 찾아 그 빠르기로 미리 셀 수 있어요')],
    ['metro', t('I can say what a metronome mark means and play with a metronome', '메트로놈 표시가 무슨 뜻인지 말하고 메트로놈에 맞춰 칠 수 있어요')],
    ['steady', t('I can keep a steady tempo when the metronome goes quiet', '메트로놈 소리가 꺼져도 꾸준한 빠르기를 지킬 수 있어요')],
  ];

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {pic(p1, 220, 660)}
      <LbSay size={17.5}>{LANG === 'ko' ? <><b>빠르기(템포)</b>는 박이 얼마나 빠르게 가는지를 말해요. 이탈리아어 빠르기말과 메트로놈이 빠르기를 알려 줘요.</>
        : <><b>Tempo</b> is how fast the beat goes. Italian tempo words and the metronome tell you the tempo.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Slow and fast', '느리게와 빠르게'), 2], [t('Four tempo words', '빠르기말 네 개'), 3], [t('Reading the tempo', '빠르기 읽기'), 4], [t('The metronome', '메트로놈'), 5], [t('A steady tempo', '꾸준한 빠르기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I can /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Slow and fast', '느리게와 빠르게')}>
      {live(pic(<div style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>{p2tune}{p2}</div>, 280, 640), <StmPad page={2}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['빠르기(템포)', '박이 얼마나 빠르게 가는지. 이탈리아어로 ‘시간’.'],
        ['느리게', '박과 박 사이가 멀어요.'],
        ['빠르게', '박과 박 사이가 가까워요.'],
      ] : [
        ['tempo', 'How fast the beat goes. Italian for ‘time’.'],
        ['slow', 'The beats come far apart.'],
        ['fast', 'The beats come close together.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손으로 가운데 도부터 C{' '}D{' '}E{' '}F{' '}G를 1{' '}2{' '}3{' '}4 느리게 세며 쳐요. 그다음 빠르게 세며 쳐요.</>,
        <>선율을 여리고 느리게, 여리고 빠르게, 그다음 세고 느리게 쳐요. 세게는 빠르게가 아니에요.</>,
      ] : [
        <>Right hand: play C{' '}D{' '}E{' '}F{' '}G from middle C, counting 1{' '}2{' '}3{' '}4 slowly. Then the same notes, counting fast.</>,
        <>Play the tune soft and slow, then soft and fast, then loud and slow. Loud is not the same as fast.</>,
      ]}/>
      <LbRemember>{t('Tempo: how fast the beat goes. Same notes, new tempo.', '빠르기: 박이 얼마나 빠른지. 음은 그대로, 빠르기만 바꿔요.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Four tempo words', '빠르기말 네 개')}>
      {live(pic(p3, 250, 600), <StmPad page={3}/>)}
      <LbDefs items={STM_WORDS.map(x => [LANG === 'ko' ? x.w + ' ' + STM_KO[x.w] : x.w, t(x.en, x.ko)])}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>2쪽의 선율을 아다지오, 안단테, 모데라토, 알레그로 순서로 쳐요: 한 번 칠 때마다 조금 더 빠르게.</>,
        <>방을 걸으며 걸음마다 ‘하나’라고 말해요: 그게 안단테예요. 그 빠르기로 C를 여덟 번 쳐요.</>,
      ] : [
        <>Play the tune from page 2 at each tempo: Adagio, Andante, Moderato, Allegro, a little faster each time.</>,
        <>Walk across the room saying ‘one’ on every step: that is Andante. Play C eight times at that tempo.</>,
      ]}/>
      <LbRemember>{t('Adagio, Andante, Moderato, Allegro: slow to fast.', '아다지오, 안단테, 모데라토, 알레그로: 느린 것부터 빠른 것까지.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Reading the tempo', '빠르기 읽기')}>
      {live(pic(p4, 230, 640), <StmPad page={4}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['빠르기말', '빠르기를 알려 주는 말.'],
        ['미리 세기', '치기 전에 곡의 빠르기로 한 마디를 세는 것: 1 2 3 4. 다른 이름은 예비박.'],
      ] : [
        ['tempo word', 'The word that tells you the tempo.'],
        ['count-in', 'One bar counted at the tempo before you play: 1 2 3 4.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>‘아침 산책’: 빠르기말을 읽고, 그 빠르기로 1{' '}2{' '}3{' '}4를 미리 센 다음 쳐요.</>,
        <>‘팽이’: 3박자예요. 알레그로로 1{' '}2{' '}3을 미리 센 다음 쳐요.</>,
      ] : [
        <>‘Morning Walk’: read the tempo word, count in 1{' '}2{' '}3{' '}4 at that tempo, then play.</>,
        <>‘Spinning Top’ has three beats in a bar. Count in 1{' '}2{' '}3 at Allegro, then play.</>,
      ]}/>
      <LbRemember>{t('Read the tempo word first. Count in, then play.', '빠르기말 먼저 읽기. 미리 세고, 그다음 치기.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The metronome', '메트로놈')}>
      {live(pic(p5, 270, 640), <StmPad page={5}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['메트로놈', '정한 빠르기로 꾸준히 똑딱이는 기계. 추를 내리면 빨라지고, 올리면 느려져요.'],
        ['메트로놈 표시', <>{stmMm(60)}처럼 쓴 것: 1분에 4분음표 60박.</>],
      ] : [
        ['metronome', 'A machine that ticks a steady beat at the tempo you set. Slide the weight down to go faster, up to go slower.'],
        ['metronome mark', <>A mark like {stmMm(60)}: 60 crotchet beats in a minute.</>],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>메트로놈을 60에 맞추고 2쪽의 선율을 쳐요: 똑딱 하나에 한 박, 긴 G는 네 박.</>,
        <>120에 맞추고 다시 쳐요: 두 배 빨라요.</>,
      ] : [
        <>Set a metronome to 60 and play the tune from page 2: one beat on each tick, four for the long G.</>,
        <>Set it to 120 and play it again: twice as fast.</>,
      ]}/>
      <LbRemember>{stmMm(60)}{t(': 60 beats a minute, one every second.', ': 1분에 60박, 1초에 한 박.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('A steady tempo', '꾸준한 빠르기')}>
      {live(pic(p6, 230, 640), <StmPad page={6}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['꾸준한 빠르기', '처음부터 끝까지 같은 빠르기.'],
        ['서두르기', '모르는 사이에 점점 빨라지는 것.'],
        ['처지기', '모르는 사이에 점점 느려지는 것.'],
      ] : [
        ['steady tempo', 'The same tempo from the start to the end.'],
        ['rushing', 'Getting faster without meaning to.'],
        ['dragging', 'Getting slower without meaning to.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>메트로놈을 90에 맞추고 ‘아침 산책’을 쉬지 않고 네 번 쳐요.</>,
        <>다시 쳐요. 세 번째에는 메트로놈 소리를 끄고, 네 번째에 다시 켜요. 아직 똑딱 소리에 맞나요? 앞서면 서두른 것, 뒤처지면 처진 거예요.</>,
      ] : [
        <>Set a metronome to 90. Play ‘Morning Walk’ four times without stopping.</>,
        <>Again, but turn the metronome’s sound off for the third time and on for the fourth. Still on the ticks? Ahead: you rushed. Behind: you dragged.</>,
      ]}/>
      <LbRemember>{t('Keep the tempo steady: no rushing, no dragging.', '빠르기는 꾸준하게: 서두르지도, 처지지도 않게.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_stm_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, x])}/>}/>
    </LbPage>,
  ];
}
function TempoLessonBook() { return <>{stmLbPages(false)}</>; }
