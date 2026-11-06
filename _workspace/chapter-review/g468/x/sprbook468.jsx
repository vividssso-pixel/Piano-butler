// ─── Phase 468: chapter 12 (Pitch, Hz & Range): the Lesson Book, built in full under Book rules 14 and 15 (her
// 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'). The level plan's scope for room 12 (Level 2): high, middle and low;
// the instrument families; why big is low and small is high (AMEB Preliminary general knowledge: high, middle, low, the
// families). It builds on chapter 2 (low on the left, the turtle under the sea; high on the right, the bird in the sky;
// middle C the ground) and on the two clefs (the Queen's high treble, the King's low bass). Low, middle and high are
// the drill's own notes: middle is middle C and the keys near it (G below to F above). Hertz is one entry on the 'why'
// page; octaves doubling in hertz is the drill's extra level.

// the instruments, drawn in navy lines with a coral touch, each in a 60 x 60 box (x, y its top left; s its scale)
const SPR_INST = [
  { id: 'violin', fam: 'strings', en: 'violin', ko: '바이올린' }, { id: 'cello', fam: 'strings', en: 'cello', ko: '첼로' },
  { id: 'guitar', fam: 'strings', en: 'guitar', ko: '기타' }, { id: 'harp', fam: 'strings', en: 'harp', ko: '하프' },
  { id: 'flute', fam: 'woodwind', en: 'flute', ko: '플루트' }, { id: 'clarinet', fam: 'woodwind', en: 'clarinet', ko: '클라리넷' },
  { id: 'recorder', fam: 'woodwind', en: 'recorder', ko: '리코더' },
  { id: 'trumpet', fam: 'brass', en: 'trumpet', ko: '트럼펫' }, { id: 'trombone', fam: 'brass', en: 'trombone', ko: '트롬본' },
  { id: 'tuba', fam: 'brass', en: 'tuba', ko: '튜바' },
  { id: 'drum', fam: 'percussion', en: 'drum', ko: '북' }, { id: 'xylophone', fam: 'percussion', en: 'xylophone', ko: '실로폰' },
  { id: 'triangle', fam: 'percussion', en: 'triangle', ko: '트라이앵글' },
];
const SPR_FAMS = ['strings', 'woodwind', 'brass', 'percussion'];
const SPR_FAM = {
  strings: { en: 'strings', ko: '현악기', how: () => t('bow or pluck its strings', '현을 활로 긋거나 손가락으로 뜯어요'), howLong: () => t('The strings vibrate: you bow or pluck them.', '현(줄)이 떨려요: 활로 긋거나 손가락으로 뜯어요.') },
  woodwind: { en: 'woodwind', ko: '목관 악기', how: () => t('blow across a hole or through a reed', '구멍이나 리드에 바람을 불어 넣어요'), howLong: () => t('You blow across a hole (the flute) or through a reed (the clarinet).', '구멍(플루트)이나 리드(클라리넷)에 바람을 불어 넣어요.') },
  brass: { en: 'brass', ko: '금관 악기', how: () => t('buzz your lips into it', '입술을 떨며 불어요'), howLong: () => t('You buzz your lips into it.', '입술을 떨며 불어요.') },
  percussion: { en: 'percussion', ko: '타악기', how: () => t('hit, shake or scrape it', '치거나 흔들거나 긁어요'), howLong: () => t('You hit, shake or scrape it.', '치거나, 흔들거나, 긁어요.') },
};
const sprName = (id) => { const i = SPR_INST.find(x => x.id === id); return i ? t(i.en, i.ko) : id; };
const sprFamName = (f) => t(SPR_FAM[f].en, SPR_FAM[f].ko);
const SPR_SW = { stroke: PEN_N, strokeWidth: 1.7, strokeLinecap: 'round', strokeLinejoin: 'round', fill: 'none' };
const SPR_SWF = { ...SPR_SW, fill: '#fff' };
// a violin-family body: its lowest point (the endpin's tip, or the body) at (cx, base), h tall; peg: the endpin of a
// cello or double bass; bass: the double bass's sloping shoulders. The right side as cubic segments, mirrored.
const SPR_BODY = { fiddle: [[0, 38], [12, 38, 18, 42, 17, 52], [16, 58, 10, 60, 11, 64], [12, 68, 21, 70, 20, 84], [19, 96, 8, 99, 0, 99]],
  bass: [[0, 34], [4, 34, 9, 39, 13, 47], [17, 54, 12, 58, 11, 63], [12, 68, 22, 70, 21, 84], [20, 96, 8, 99, 0, 99]] };
function SprFiddle({ cx, base, h, peg, hl, bass }) {
  const s = h / (peg ? 108 : 100), X = (v) => cx + v * s, Y = (v) => base - h + v * s, B = SPR_BODY[bass ? 'bass' : 'fiddle'];
  let d = 'M' + X(B[0][0]) + ' ' + Y(B[0][1]);
  for (let i = 1; i < B.length; i++) d += ' C' + X(B[i][0]) + ' ' + Y(B[i][1]) + ' ' + X(B[i][2]) + ' ' + Y(B[i][3]) + ' ' + X(B[i][4]) + ' ' + Y(B[i][5]);
  for (let i = B.length - 1; i >= 1; i--) { const p = i > 1 ? [B[i - 1][B[i - 1].length - 2], B[i - 1][B[i - 1].length - 1]] : B[0]; d += ' C' + X(-B[i][2]) + ' ' + Y(B[i][3]) + ' ' + X(-B[i][0]) + ' ' + Y(B[i][1]) + ' ' + X(-p[0]) + ' ' + Y(p[1]); }
  d += ' Z';
  const sw = Math.max(1.2, Math.min(1.8, 0.9 + s * 0.6));
  return <g>
    {peg && <line x1={X(0)} x2={X(0)} y1={Y(99)} y2={Y(108)} {...SPR_SW} strokeWidth={sw}/>}
    <rect x={X(-2.6)} y={Y(8)} width={5.2 * s} height={(bass ? 28 : 32) * s} rx={1.2 * s} fill={PEN_N}/>
    <circle cx={X(0)} cy={Y(5)} r={3.6 * s} {...SPR_SWF} strokeWidth={sw}/>
    <path d={d} {...SPR_SWF} fill={hl ? '#fbe3da' : '#fff'} strokeWidth={sw}/>
    <path d={'M' + X(-7) + ' ' + Y(68) + ' q' + (-2 * s) + ' ' + (5 * s) + ' 0 ' + (10 * s) + ' M' + X(7) + ' ' + Y(68) + ' q' + (2 * s) + ' ' + (5 * s) + ' 0 ' + (10 * s)} fill="none" stroke={PEN_C} strokeWidth={sw * 0.8} strokeLinecap="round"/>
    <line x1={X(-6)} x2={X(6)} y1={Y(76)} y2={Y(76)} stroke={PEN_C} strokeWidth={sw}/>
    <line x1={X(-1.3)} x2={X(-1.3)} y1={Y(10)} y2={Y(90)} stroke={PEN_N} strokeWidth="0.7"/><line x1={X(1.3)} x2={X(1.3)} y1={Y(10)} y2={Y(90)} stroke={PEN_N} strokeWidth="0.7"/>
  </g>;
}
function SprInst({ id, x = 0, y = 0, s = 1 }) {
  const g = (kids) => <g transform={'translate(' + x + ' ' + y + ') scale(' + s + ')'}>{kids}</g>;
  if (id === 'violin') return g(<SprFiddle cx={30} base={50} h={36}/>);
  if (id === 'cello') return g(<SprFiddle cx={30} base={59} h={58} peg/>);
  if (id === 'guitar') return g(<>
    <rect x="27.6" y="4" width="4.8" height="26" rx="1" fill={PEN_N}/><rect x="25.5" y="1" width="9" height="7" rx="1.5" {...SPR_SWF}/>
    <path d="M30 26 C38 26 41 30 39 36 C46 38 48 46 44 52 C40 58 20 58 16 52 C12 46 14 38 21 36 C19 30 22 26 30 26 Z" {...SPR_SWF}/>
    <circle cx="30" cy="40" r="4.2" fill="none" stroke={PEN_C} strokeWidth="1.6"/><line x1="25" x2="35" y1="50" y2="50" stroke={PEN_C} strokeWidth="1.8"/></>);
  if (id === 'harp') return g(<>
    <path d="M14 56 L14 6 Q30 2 50 18 L18 54" {...SPR_SW}/><path d="M14 56 L22 56 L50 20" {...SPR_SW}/>
    {[0, 1, 2, 3, 4, 5].map(i => { const xx = 19 + i * 5, top = 8 + i * 2.6 + (i > 2 ? (i - 2) * 1.5 : 0), bot = 51 - i * 5.3; return <line key={i} x1={xx} x2={xx} y1={top} y2={bot} stroke={i === 2 ? PEN_C : PEN_N} strokeWidth="1.1"/>; })}</>);
  if (id === 'flute') return g(<>
    <rect x="3" y="27" width="54" height="6" rx="2" transform="rotate(-18 30 30)" {...SPR_SWF}/>
    <g transform="rotate(-18 30 30)">{[22, 28, 34, 40, 46].map(xx => <circle key={xx} cx={xx} cy="30" r="1.5" fill={PEN_N}/>)}<ellipse cx="11" cy="30" rx="2" ry="1.4" fill={PEN_C}/></g></>);
  if (id === 'clarinet') return g(<>
    <path d="M27.8 2 L32.2 2 L33 10 L27 10 Z" fill={PEN_N}/><rect x="26.5" y="10" width="7" height="38" rx="1" fill={PEN_N}/>
    <path d="M26.5 47 L21 58 L39 58 L33.5 47 Z" fill={PEN_N}/>{[17, 23, 29, 35, 41].map(yy => <circle key={yy} cx="30" cy={yy} r="1.4" fill="#fff"/>)}
    <line x1="33.5" x2="36" y1="20" y2="20" stroke={PEN_N} strokeWidth="1.2"/><line x1="33.5" x2="36" y1="32" y2="32" stroke={PEN_N} strokeWidth="1.2"/><circle cx="30" cy="10" r="1.6" fill={PEN_C}/></>);
  if (id === 'recorder') return g(<>
    <path d="M26.5 3 Q30 1 33.5 3 L33.5 13 L26.5 13 Z" {...SPR_SWF}/><rect x="28" y="9" width="4" height="3" fill={PEN_C}/>
    <path d="M27 13 L33 13 L33.6 50 L36 57 L24 57 L26.4 50 Z" {...SPR_SWF}/>{[20, 26, 32, 38, 44].map(yy => <circle key={yy} cx="30" cy={yy} r="1.6" fill={PEN_N}/>)}</>);
  if (id === 'trumpet') return g(<>
    <path d="M6 28 L40 28 M6 33 L40 33" {...SPR_SW}/><path d="M40 26 L54 18 L54 43 L40 35 Z" {...SPR_SWF}/>
    <path d="M14 33 Q14 44 24 44 L36 44 Q40 44 40 38" {...SPR_SW}/>{[20, 26, 32].map(xx => <rect key={xx} x={xx - 2} y="19" width="4" height="9" rx="1" fill={PEN_N}/>)}
    <circle cx="4" cy="30.5" r="2" fill={PEN_C}/></>);
  if (id === 'trombone') return g(<>
    <path d="M48 36 L12 36 Q6 39 12 42 L48 42" {...SPR_SW}/><path d="M26 22 L50 22 Q55 22 55 29 Q55 36 50 36" {...SPR_SW}/>
    <path d="M26 20 L26 24 L6 31 L6 13 Z" {...SPR_SWF}/><line x1="36" x2="36" y1="22" y2="36" stroke={PEN_N} strokeWidth="1.4"/>
    <line x1="22" x2="22" y1="36" y2="42" stroke={PEN_C} strokeWidth="2.2"/><circle cx="50" cy="42" r="1.8" fill={PEN_C}/></>);
  if (id === 'tuba') return g(<>
    <path d="M14 3 L46 3 L38 15 L22 15 Z" {...SPR_SWF}/>
    <ellipse cx="30" cy="38" rx="15" ry="17" {...SPR_SWF}/><ellipse cx="30" cy="38" rx="7" ry="9" {...SPR_SW}/><line x1="30" x2="30" y1="15" y2="21" {...SPR_SW}/>
    {[38, 42, 46].map(xx => <rect key={xx} x={xx - 1.5} y="26" width="3" height="11" rx="1" fill={PEN_N}/>)}
    <path d="M16 36 L5 30" {...SPR_SW}/><circle cx="4.5" cy="29.5" r="2" fill={PEN_C}/></>);
  if (id === 'drum') return g(<>
    <ellipse cx="30" cy="24" rx="20" ry="7" {...SPR_SWF}/><path d="M10 24 V44 Q30 54 50 44 V24" {...SPR_SWF}/><path d="M10 24 Q30 34 50 24" {...SPR_SW}/>
    <path d="M14 28 L22 46 L30 30 L38 47 L46 28" fill="none" stroke={PEN_C} strokeWidth="1.4" strokeLinejoin="round"/><path d="M16 4 L28 20 M44 4 L34 20" {...SPR_SW}/></>);
  if (id === 'xylophone') return g(<>
    <line x1="6" x2="54" y1="18" y2="24" {...SPR_SW}/><line x1="6" x2="54" y1="46" y2="40" {...SPR_SW}/>
    {[0, 1, 2, 3, 4, 5].map(i => { const xx = 8 + i * 8, h = 30 - i * 3.2, yy = 32 - h / 2 + i * 0.2; return <rect key={i} x={xx} y={yy} width="6" height={h} rx="1.4" fill={PEN_N}/>; })}
    <path d="M10 46 L6 58 M50 41 L54 58" {...SPR_SW}/><path d="M24 4 L34 14 M38 4 L28 14" stroke={PEN_N} strokeWidth="1.4"/><circle cx="23" cy="3.5" r="2.6" fill={PEN_C}/><circle cx="39" cy="3.5" r="2.6" fill={PEN_C}/></>);
  if (id === 'triangle') return g(<>
    <path d="M30 14 L48 48 L12 48 L26.5 20.5" {...SPR_SW} strokeWidth="2.2"/><line x1="30" x2="30" y1="4" y2="14" stroke={PEN_N} strokeWidth="1"/>
    <line x1="40" x2="56" y1="34" y2="22" stroke={PEN_C} strokeWidth="2" strokeLinecap="round"/></>);
  return null;
}
// the 88 keys, small: 52 white keys from A0 to C8 (x0, y0 the top left; kw a white key's width; h its height).
// marks: { midi: 'cor' | 'ink' } dots on keys; range: [lo, hi] shaded; key1: one key filled coral, an arrow over it
const sprWhites = (() => { const w = []; for (let m = 21; m <= 108; m++) if ([0, 2, 4, 5, 7, 9, 11].includes(m % 12)) w.push(m); return w; })();
const sprIsWhite = (m) => [0, 2, 4, 5, 7, 9, 11].includes(((m % 12) + 12) % 12);
const sprKeyX = (m, x0 = 0, kw = 10) => { const wi = sprWhites.filter(w => w <= m).length - 1; return sprIsWhite(m) ? x0 + wi * kw + kw / 2 : x0 + (wi + 1) * kw; };
function SprKeys88({ x0 = 0, y0 = 0, kw = 10, h = 46, marks = {}, range, rangeCol = '#fbe3da', middleC = true, cLabel, cfs = 10.5, key1, sw = 0.7 }) {
  const bw = kw * 0.62, bh = h * 0.6;
  return <g>
    {sprWhites.map((m, i) => <rect key={m} x={x0 + i * kw} y={y0} width={kw} height={h} fill={key1 === m ? PEN_C : range && m >= range[0] && m <= range[1] ? rangeCol : '#fff'} stroke={PEN_N} strokeWidth={sw}/>)}
    {Array.from({ length: 88 }, (_, i) => 21 + i).filter(m => !sprIsWhite(m)).map(m => <rect key={m} x={sprKeyX(m, x0, kw) - bw / 2} y={y0} width={bw} height={bh} fill={key1 === m || (range && m >= range[0] && m <= range[1]) ? PEN_C : PEN_N}/>)}
    {key1 != null && <path d={'M' + (sprKeyX(key1, x0, kw) - kw * 1.3) + ' ' + (y0 - kw * 2.2) + ' L' + (sprKeyX(key1, x0, kw) + kw * 1.3) + ' ' + (y0 - kw * 2.2) + ' L' + sprKeyX(key1, x0, kw) + ' ' + (y0 - kw * 0.4) + ' Z'} fill={PEN_C}/>}
    {middleC && <><circle cx={sprKeyX(60, x0, kw)} cy={y0 + h - kw * 0.55} r={kw * 0.28} fill={PEN_C}/>{cLabel !== false && <text x={sprKeyX(60, x0, kw)} y={y0 + h + cfs + 2} textAnchor="middle" fontSize={cfs} fontWeight="900" fill={PEN_C}>{cLabel || t('middle C', '가운데 도')}</text>}</>}
    {Object.entries(marks).map(([m, c]) => <circle key={m} cx={sprKeyX(+m, x0, kw)} cy={y0 + (sprIsWhite(+m) ? h - kw * 0.55 : bh - kw * 0.45)} r={kw * 0.3} fill={c === 'ink' ? PEN_N : PEN_C} stroke="#fff" strokeWidth="0.8"/>)}
  </g>;
}
// ranges (sounding), from RANGES; the trumpet here is the B-flat trumpet as it sounds (RANGES gives its written range)
const SPR_RANGE = (name) => name === 'Trumpet' ? { name, lo: 52, hi: 84 } : ALL_RANGES.find(r => r.name === name);
const SPR_RNAME = { Alto: ['alto', '알토'], Tenor: ['tenor', '테너'], 'Double bass': ['double bass', '더블베이스'], Cello: ['cello', '첼로'], Viola: ['viola', '비올라'], Violin: ['violin', '바이올린'], Flute: ['flute', '플루트'], Piccolo: ['piccolo', '피콜로'], Tuba: ['tuba', '튜바'], Trumpet: ['trumpet', '트럼펫'], Soprano: ['soprano', '소프라노'], Bass: ['bass voice', '베이스 가수'] };
const sprRName = (n) => SPR_RNAME[n] ? t(SPR_RNAME[n][0], SPR_RNAME[n][1]) : n;
const sprLetter = (m) => SHARP_NAMES[((m % 12) + 12) % 12];
// the violin family to scale, biggest (lowest) on the left
const SPR_VFAM = [{ n: 'Double bass', h: 156, peg: true, bass: true }, { n: 'Cello', h: 110, peg: true }, { n: 'Viola', h: 62 }, { n: 'Violin', h: 54 }];
const SPR_VLOWS = [28, 36, 48, 55];   // E1, C2, C3, G3

function sprLbPages(scr = false) {
  const ch = 'pitch-range', fs = scr ? 1.4 : 1;
  const live = (still, comp) => <LbLive still={still} live={<>{still}{comp}</>}/>;
  const pic = (node, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{node}</div></LbPic>;
  const svg = (vb, kids, label) => <svg viewBox={vb} style={{width:'100%',display:'block'}} role="img" aria-label={label}>{kids}</svg>;
  const tx = (x, y, s, o = {}) => <text x={x} y={y} textAnchor={o.a || 'middle'} fontSize={(o.size || 12) * fs} fontWeight={o.w || 900} fill={o.c || PEN_N} paintOrder="stroke" stroke="#fff" strokeWidth={o.halo ? 4 : 0} strokeLinejoin="round">{s}</text>;
  const arrowLH = (x1, x2, y) => <g><line x1={x1 + 6} x2={x2 - 6} y1={y} y2={y} stroke={PEN_C} strokeWidth="1.8"/><path d={'M' + (x1 + 12) + ' ' + (y - 5) + ' L' + x1 + ' ' + y + ' L' + (x1 + 12) + ' ' + (y + 5) + ' M' + (x2 - 12) + ' ' + (y - 5) + ' L' + x2 + ' ' + y + ' L' + (x2 - 12) + ' ' + (y + 5)} fill="none" stroke={PEN_C} strokeWidth="1.8" strokeLinejoin="round"/>
    {tx(x1, y + 16 * fs, t('lower', '더 낮게'), { a: 'start', size: 11.5, c: PEN_C })}{tx(x2, y + 16 * fs, t('higher', '더 높게'), { a: 'end', size: 11.5, c: PEN_C })}</g>;

  // 1. four instruments in a row, from the biggest (low, left) to the smallest (high, right), over the keys
  const p1 = svg('0 0 540 262', <>
    <SprFiddle cx={70} base={156} h={150} peg bass/><SprFiddle cx={190} base={156} h={104} peg/><SprFiddle cx={310} base={156} h={54}/><SprInst id="flute" x={418} y={120} s={0.72}/>
    {[['Double bass', 70], ['Cello', 190], ['Violin', 310], ['Piccolo', 440]].map(([n, x]) => <g key={n}>{tx(x, 174, sprRName(n), { size: 12.5 })}</g>)}
    <SprKeys88 x0={10} y0={186} kw={10} h={40} cLabel={false}/>
    {arrowLH(30, 510, 240)}
  </>, t('A double bass, a cello, a violin and a piccolo in a row, from the biggest on the left to the smallest on the right; under them the 88 keys, low on the left, high on the right.', '더블베이스, 첼로, 바이올린, 피콜로가 한 줄로: 가장 큰 것이 왼쪽, 가장 작은 것이 오른쪽. 그 아래 88건반: 왼쪽은 낮은 음, 오른쪽은 높은 음.'));

  // 2. low, middle, high on the keys (the turtle's sea to the bird's sky), then on the grand staff
  const p2keys = svg('0 0 560 136', <>
    <TurtleG x={28} y={36} s={1.15}/><BirdG x={528} y={28} s={1.15}/>
    <SprKeys88 x0={20} y0={56} kw={10} cfs={11}/>
    <rect x={sprKeyX(55, 20, 10) - 5} y={56} width={sprKeyX(65, 20, 10) - sprKeyX(55, 20, 10) + 10} height={46} fill={PEN_C} fillOpacity="0.2"/>
    {tx(24, 126, t('low', '낮은 음'), { a: 'start', size: 13.5 })}{tx(546, 126, t('high', '높은 음'), { a: 'end', size: 13.5 })}
    {tx(sprKeyX(60, 20, 10), 46, t('middle', '가운데 음'), { size: 13.5 })}
  </>);
  const p2staff = <SfStaff clef="grand" width={380} pad={[24, 26]} label={t('The grand staff: a low G on line 1 of the bass staff, middle C between the staves, a high G above the treble staff.', '큰보표: 낮은음자리표 오선 1번 줄의 낮은 G, 두 오선 사이의 가운데 도, 높은음자리표 오선 위의 높은 G.')}
    extra={(yOf, layer, txt) => { if (layer !== 'over') return null;
      const notes = [[18, 'bass', 130, t('low', '낮은 음'), 0, 21, 'middle'], [28, 'treble', 210, t('middle C', '가운데 도'), 18, 4.5, 'start'], [39, 'treble', 290, t('high', '높은 음'), 0, -11, 'middle']];
      return <g>{notes.map(([d, st, x, w, lx, ly, la]) => { const y = yOf(d, st), cl = CLEFS[st];
        return <g key={d}><g dangerouslySetInnerHTML={{ __html: ledgersFor(d, cl.low, cl.high).map(p => '<line x1="' + (x - 12) + '" x2="' + (x + 12) + '" y1="' + yOf(p, st) + '" y2="' + yOf(p, st) + '" stroke="' + PEN_N + '" stroke-width="1.4"/>').join('') + nvbHead(x, y, 'w', d === 28 ? PEN_C : PEN_N, 0.9) }}/>
          <text x={x + lx} y={y + ly} textAnchor={la} fontSize={12 * fs} fontWeight="900" fill={d === 28 ? PEN_C : PEN_N} paintOrder="stroke" stroke="#fff" strokeWidth="4" strokeLinejoin="round" style={txt}>{w}</text></g>; })}</g>; }}/>;
  const p2 = <div style={{display:'flex',flexDirection:'column',gap:12,width:'100%'}}><div role="img" aria-label={t('The 88 keys: low on the left, where the turtle swims; middle C and the keys near it shaded in the middle; high on the right, where the bird flies.', '88건반: 왼쪽은 낮은 음, 거북이가 헤엄쳐요; 가운데 도와 그 근처는 가운데에 칠해져 있어요; 오른쪽은 높은 음, 새가 날아요.')}>{p2keys}</div><div style={{maxWidth:600,margin:'0 auto',width:'100%'}}>{p2staff}</div></div>;

  // 3. why: the xylophone's bars and the piano's strings, long and low on the left, short and high on the right
  const p3 = svg('0 0 520 426', <>
    {tx(260, 16, t('A xylophone', '실로폰'), { size: 12.5 })}
    <line x1="60" x2="460" y1="34" y2="50" {...SPR_SW}/><line x1="60" x2="460" y1="126" y2="110" {...SPR_SW}/>
    {[0, 1, 2, 3, 4, 5, 6, 7].map(i => { const x = 72 + i * 48, h = 96 - i * 7.4, y = 80 - h / 2 + i * 0.6; return <g key={i}><rect x={x} y={y} width="30" height={h} rx="4" fill={PEN_N}/><text x={x + 15} y={y + h - 8} textAnchor="middle" fontSize={11 * fs} fontWeight="900" fill="#fff">{'CDEFGABC'[i]}</text></g>; })}
    {tx(70, 146, t('long bar: low', '긴 막대: 낮은 음'), { a: 'start', size: 11.5, c: PEN_C })}{tx(458, 146, t('short bar: high', '짧은 막대: 높은 음'), { a: 'end', size: 11.5, c: PEN_C })}
    {tx(260, 172, t('Inside the piano', '피아노 안'), { size: 12.5 })}
    <path d="M40 182 L480 182 L480 204 Q470 236 380 240 L40 240 Z" {...SPR_SW}/>
    {Array.from({ length: 22 }, (_, i) => { const x = 50 + i * 20, len = 54 - i * 1.9; return <line key={i} x1={x} x2={x} y1={186} y2={186 + len} stroke={PEN_N} strokeWidth={Math.max(1, 2.8 - i * 0.09)}/>; })}
    {tx(40, 260, t('long, thick strings: low', '길고 굵은 현: 낮은 음'), { a: 'start', size: 11.5, c: PEN_C })}{tx(480, 260, t('short, thin strings: high', '짧고 가는 현: 높은 음'), { a: 'end', size: 11.5, c: PEN_C })}
    {tx(260, 290, t('Two drums', '북 두 개'), { size: 12.5 })}
    <SprInst id="drum" x={90} y={296} s={1.7}/><SprInst id="drum" x={340} y={330} s={0.9}/>
    {tx(141, 416, t('big drum: low', '큰 북: 낮은 음'), { size: 11.5, c: PEN_C })}{tx(367, 416, t('small drum: high', '작은 북: 높은 음'), { size: 11.5, c: PEN_C })}
  </>, t('A xylophone: eight bars from a long C on the left to a short C on the right. Long bar: low; short bar: high. Inside the piano: long, thick strings on the left, short, thin ones on the right. Two drums: the big one low, the small one high.', '실로폰: 왼쪽의 긴 C부터 오른쪽의 짧은 C까지 막대 여덟 개. 긴 막대는 낮은 음, 짧은 막대는 높은 음. 피아노 안: 왼쪽은 길고 굵은 현, 오른쪽은 짧고 가는 현. 북 두 개: 큰 북은 낮은 음, 작은 북은 높은 음.'));

  // 4. the four families, three of each
  const famCols = [['strings', ['violin', 'guitar', 'harp']], ['woodwind', ['flute', 'clarinet', 'recorder']], ['brass', ['trumpet', 'trombone', 'tuba']], ['percussion', ['drum', 'xylophone', 'triangle']]];
  const p4 = svg('0 0 560 344', <>{famCols.map(([f, list], c) => { const cx = 70 + c * 140;
    return <g key={f}><rect x={cx - 64} y="4" width="128" height="336" rx="8" fill="none" stroke="rgba(38,41,107,0.28)" strokeWidth="1"/>
      {tx(cx, 26, sprFamName(f).toUpperCase(), { size: 12.5, c: PEN_C })}
      {list.map((id, k) => <g key={id}><SprInst id={id} x={cx - 36} y={36 + k * 100} s={1.2}/>{tx(cx, 120 + k * 100, sprName(id), { size: 12, w: 800 })}</g>)}</g>; })}</>,
    t('The four families. Strings: violin, guitar, harp. Woodwind: flute, clarinet, recorder. Brass: trumpet, trombone, tuba. Percussion: drum, xylophone, triangle.', '네 가족. 현악기: 바이올린, 기타, 하프. 목관 악기: 플루트, 클라리넷, 리코더. 금관 악기: 트럼펫, 트롬본, 튜바. 타악기: 북, 실로폰, 트라이앵글.'));

  // 5. the violin family to scale, each one's lowest note on the keys under it
  const vx = [80, 210, 320, 420];
  const p5 = svg('0 0 520 432', <>
    {SPR_VFAM.map((v, i) => <g key={v.n}><SprFiddle cx={vx[i]} base={312} h={v.h * 1.8} peg={v.peg} bass={v.bass}/>{tx(vx[i], 330, sprRName(v.n), { size: 12.5 })}</g>)}
    <SprKeys88 x0={0} y0={350} kw={10} h={40} middleC={false} marks={{ 28: 'cor', 36: 'cor', 48: 'cor', 55: 'cor' }}/>
    {SPR_VFAM.map((v, i) => { const kx = sprKeyX(SPR_VLOWS[i], 0, 10); return <line key={v.n} x1={vx[i]} x2={kx} y1={336} y2={380} stroke={PEN_C} strokeWidth="1.2" strokeDasharray="3 3"/>; })}
    {arrowLH(20, 500, 406)}
  </>, t('The violin family drawn to scale: the double bass, the biggest, on the left; then the cello, the viola and the violin, the smallest, on the right. Under them, each one’s lowest note on the keys: E, C, C and G, each a little higher.', '크기대로 그린 바이올린 가족: 가장 큰 더블베이스가 왼쪽, 그다음 첼로, 비올라, 가장 작은 바이올린이 오른쪽. 그 아래 건반에 각자의 가장 낮은 음: E, C, C, G, 하나씩 조금 더 높아요.'));

  // 6. ranges over the 88 keys
  const rows = ['Double bass', 'Cello', 'Viola', 'Violin', 'Flute', 'Piccolo', 'Bass', 'Soprano'];
  const p6 = svg('0 0 540 382', <>
    {rows.map((n, i) => { const r = SPR_RANGE(n), x1 = sprKeyX(r.lo, 10, 10), x2 = sprKeyX(r.hi, 10, 10), y = 8 + i * 36 + (i > 5 ? 10 : 0), left = x1 > 120;
      return <g key={n}><rect x={x1} y={y} width={x2 - x1} height="16" rx="8" fill={PEN_N}/>{left ? tx(x1 - 7, y + 13, sprRName(n), { a: 'end', size: 13 }) : tx(x2 + 7, y + 13, sprRName(n), { a: 'start', size: 13 })}</g>; })}
    <rect x={10} y={306} width={520} height="16" rx="8" fill={PEN_C}/>{tx(270, 319, t('the piano: all 88 keys', '피아노: 88건반 전부'), { size: 12, c: '#fff' })}
    <SprKeys88 x0={10} y0={326} kw={10} h={40} cfs={11}/>
  </>, t('Ranges over the 88 keys. The double bass plays low, the cello a little higher, then the viola; the violin from the G below middle C, the flute from middle C, the piccolo highest of all. A bass voice sings low, a soprano from middle C up. Under them, the piano’s range: all 88 keys.', '88건반 위의 음역. 더블베이스는 낮게, 첼로는 조금 더 높게, 그다음 비올라; 바이올린은 가운데 도 아래 G부터, 플루트는 가운데 도부터, 피콜로가 가장 높아요. 베이스 가수는 낮게, 소프라노는 가운데 도부터 위로. 그 아래 피아노의 음역: 88건반 전부.'));

  // the check icons
  const ic = {
    zones: [{ k: 'raw', svg: '<rect x="4" y="12" width="84" height="18" rx="2" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.2"/>' + [14, 46, 78].map((x, i) => '<circle cx="' + x + '" cy="21" r="4" fill="' + (i === 1 ? PEN_C : PEN_N) + '"/>').join('') }],
    why: [{ k: 'raw', svg: [0, 1, 2, 3, 4].map(i => '<rect x="' + (10 + i * 15) + '" y="' + (6 + i * 3) + '" width="10" height="' + (30 - i * 6) + '" rx="2" fill="' + (i === 0 ? PEN_C : PEN_N) + '"/>').join('') }],
    fam: [{ k: 'raw', svg: '<circle cx="12" cy="20" r="8" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.5"/><path d="M28 13 L42 13 L42 27 L28 27 Z" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.5"/><path d="M50 27 L58 12 L66 27 Z" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.5"/><path d="M74 13 L88 20 L74 27 Z" fill="#fff" stroke="' + PEN_C + '" stroke-width="1.6"/>' }],
    order: [{ k: 'raw', svg: [[16, 32], [38, 24], [58, 18], [76, 14]].map(([x, h]) => '<ellipse cx="' + x + '" cy="' + (36 - h / 2) + '" rx="' + (h / 4) + '" ry="' + (h / 2) + '" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.5"/>').join('') + '<line x1="8" x2="86" y1="38" y2="38" stroke="' + PEN_C + '" stroke-width="1.6"/>' }],
    range: [{ k: 'raw', svg: '<rect x="4" y="22" width="84" height="14" rx="2" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.2"/><rect x="30" y="8" width="40" height="8" rx="4" fill="' + PEN_C + '"/>' }],
  };
  const nbKo = (s) => s.replace(/수 있어요/g, '수 있어요');
  const checksRows = [
    ['zones', t('I can play low, middle and high, and find them on the staff', nbKo('낮은 음, 가운데 음, 높은 음을 치고 오선에서 찾을 수 있어요'))],
    ['why', t('I can say why a big instrument sounds low', nbKo('큰 악기가 왜 낮은 소리를 내는지 말할 수 있어요'))],
    ['fam', t('I can name the four families and how each makes its sound', nbKo('네 악기 가족과 각자 소리 내는 방법을 말할 수 있어요'))],
    ['order', t('I can put the violin family in order, from low to high', nbKo('바이올린 가족을 낮은 것부터 높은 것까지 차례대로 말할 수 있어요'))],
    ['range', t('I can show an instrument’s range on the piano keys', nbKo('악기의 음역을 피아노 건반에서 보여 줄 수 있어요'))],
  ];

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Pitch, Hz & Range', '음높이, 헤르츠와 음역')}</div>
      </div></LbOnly>
      {pic(p1, 220, 660)}
      <LbSay size={17.5}>{LANG === 'ko' ? <><b>음높이</b>는 소리의 높고 낮음이에요. <b>음역</b>은 악기가 낼 수{' '}있는 가장 낮은 음부터 가장 높은{' '}음까지예요.</>
        : <><b>Pitch</b> is how high or low a sound is. Every instrument has a <b>range</b>: the notes from its lowest to its highest.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Low, middle and high', '낮은 음, 가운데 음, 높은 음'), 2], [t('Big is low, small is high', '크면 낮고, 작으면 높아요'), 3], [t('The instrument families', '악기 가족'), 4], [t('Low to high', '낮은 것부터 높은 것까지'), 5], [t('The piano’s range', '피아노의 음역'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I can /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Low, middle and high', '낮은 음, 가운데 음, 높은 음')}>
      {live(pic(p2, 280, 660), <SprPad page={2}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['낮은 음', '건반의 왼쪽 멀리: 낮은음자리표 오선의 아래쪽과 그 아래.'],
        ['높은 음', '건반의 오른쪽 멀리: 높은음자리표 오선의 위쪽과 그 위.'],
        ['가운데 음', '가운데 도와 그 근처: 아래의 G부터 위의 F까지.'],
      ] : [
        ['low', 'Far to the left on the keys: the bottom of the bass staff and below.'],
        ['high', 'Far to the right on the keys: the top of the treble staff and above.'],
        ['middle', 'Middle C and the keys near it: from the G below to the F above.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>가운데 도를 쳐요. 그다음 왼쪽 맨 끝 가까이의 C(낮은 음)와 오른쪽 맨 끝 가까이의 C(높은 음)를 쳐요.</>,
        <>오른손으로 가운데 도에서 C{' '}D{' '}E{' '}D{' '}C를 쳐요. 그다음 한 C 아래에서, 한 C 위에서 쳐요: 같은 선율이 더 낮게, 더 높게.</>,
      ] : [
        <>Play middle C. Then a C near the left end (low) and a C near the right end (high).</>,
        <>Right hand: play C D E D C from middle C. Then from the next C down, and from the next C up: the same tune, lower and higher.</>,
      ]}/>
      <LbRemember>{t('Left: low. Right: high. Middle C: the middle.', '왼쪽은 낮은 음, 오른쪽은 높은 음, 가운데 도는 가운데.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Big is low, small is high', '크면 낮고, 작으면 높아요')}>
      {live(pic(p3, 260, 600), <SprPad page={3}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['떨림', '아주 빠르게 앞뒤로 움직이는 것. 크고 긴 것은 천천히 떨려서 낮은 소리, 작고 짧은 것은 빨리 떨려서 높은 소리가 나요.'],
        ['헤르츠(Hz)', '1초에 떨리는 횟수. 가운데 도 위의 A는 1초에 440번 떨려요: 440 Hz.'],
      ] : [
        ['vibrate', 'To move back and forth very fast. Big, long things vibrate slowly and sound low; small, short things vibrate fast and sound high.'],
        ['hertz (Hz)', 'How many times something vibrates in one second. The A above middle C vibrates 440 times a second: 440 Hz.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>손을 피아노 옆판에 대고, 가장 낮은 건반과 가장 높은 건반을 쳐요. 어느 쪽이 손을 더 떨게 하나요?</>,
        <>자를 책상 끝에 대고 길게 내밀어 튕겨요. 그다음 짧게 내밀어 튕겨요. 어느 쪽이 더 높은 소리를 낼까요?</>,
      ] : [
        <>Lay a hand flat on the side of the piano. Play the lowest key, then the highest. Which one buzzes your hand more?</>,
        <>Hold a ruler on a table edge with a long end out and twang it. Then with a short end out. Which sounds higher?</>,
      ]}/>
      <LbRemember>{t('Big and long: low. Small and short: high.', '크고 길면 낮은 소리, 작고 짧으면 높은 소리.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The instrument families', '악기 가족')}>
      {live(pic(p4, 250, 640), <SprPad page={4}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['악기 가족', '같은 방법으로 소리를 내는 악기들.'],
        ['현악기', SPR_FAM.strings.howLong()],
        ['목관 악기', SPR_FAM.woodwind.howLong()],
        ['금관 악기', SPR_FAM.brass.howLong()],
        ['타악기', SPR_FAM.percussion.howLong()],
      ] : [
        ['instrument family', 'Instruments that make their sound the same way.'],
        ['strings', SPR_FAM.strings.howLong()],
        ['woodwind', SPR_FAM.woodwind.howLong()],
        ['brass', SPR_FAM.brass.howLong()],
        ['percussion', SPR_FAM.percussion.howLong()],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>건반 하나를 누르면 피아노 안에서 해머가 현을 쳐요. 피아노는 북처럼 치는 현악기예요.</>,
        <>북처럼: 가장 낮은 C를 네 번, 짧고 힘 있게. 플루트처럼: 가운데 도보다 두 C 위의 C에서 C{' '}D{' '}E{' '}D{' '}C를 부드럽게.</>,
      ] : [
        <>Press a key: inside the piano, a hammer hits a string. The piano is a string instrument played like a drum.</>,
        <>Like a drum: the lowest C four times, short and strong. Like a flute: C D E D C two Cs above middle C, smooth.</>,
      ]}/>
      <LbRemember>{LANG === 'ko' ? <>현악기는 긋거나 뜯기, 목관 악기는 불기,<br/>금관 악기는 입술 떨기, 타악기는 치기.</> : <>Strings: bow or pluck. Woodwind: blow.<br/>Brass: buzz. Percussion: hit.</>}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Low to high', '낮은 것부터 높은 것까지')}>
      {live(pic(p5, 280, 650), <SprPad page={5}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['바이올린 가족', '바이올린, 비올라, 첼로, 더블베이스. 한 가족 안에서는 클수록 낮아요.'],
        ['목소리', '소프라노, 알토, 테너, 베이스. 가장 높은 목소리부터 가장 낮은 목소리까지.'],
      ] : [
        ['the violin family', 'Violin, viola, cello and double bass. In one family, the bigger, the lower.'],
        ['voices', 'Soprano, alto, tenor and bass: from the highest voice to the lowest.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>그림의 주황색 점을 찾아 쳐요: 더블베이스의 가장 낮은 E, 첼로의 C, 비올라의 C, 바이올린의 G. 하나씩 높아져요.</>,
        <>가운데 도 아래의 C를 베이스 가수처럼 낮게 불러 봐요. 그다음 가운데 도 위의 C를 소프라노처럼 높게.</>,
      ] : [
        <>Find the orange dots and play them: the double bass’s lowest E, the cello’s C, the viola’s C, the violin’s G. Each is higher.</>,
        <>Sing the C below middle C low, like a bass singer. Then the C above middle C high, like a soprano.</>,
      ]}/>
      <LbRemember>{t('In one family: the bigger, the lower.', '한 가족 안에서는 클수록 낮아요.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('The piano’s range', '피아노의 음역')}>
      {live(pic(p6, 260, 650), <SprPad page={6}/>)}
      <LbDefs items={LANG === 'ko' ? [
        ['음역', '악기가 낼 수 있는 음, 가장 낮은 음부터 가장 높은 음까지.'],
        ['피콜로', '작은 플루트. 오케스트라에서 가장 높은 악기예요.'],
        ['피아노의 음역', '88건반, 가장 낮은 A부터 가장 높은 C까지. 오케스트라의 어느 악기보다 넓어요.'],
      ] : [
        ['range', 'The notes an instrument can play, from its lowest to its highest.'],
        ['piccolo', 'A small flute: the highest instrument in the orchestra.'],
        ['the piano’s range', '88 keys, from the lowest A to the highest C: wider than any instrument in the orchestra.'],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [
        <>88건반 피아노에서 가장 낮은 A와 가장 높은 C를 쳐요: 더블베이스보다 낮고, 피콜로만큼 높아요.</>,
        <>가운데 도를 쳐요: 첼로, 바이올린, 플루트, 소프라노 모두 낼 수 있는 음이에요.</>,
      ] : [
        <>On an 88-key piano, play the lowest A and the highest C: lower than a double bass, as high as a piccolo.</>,
        <>Play middle C: the cello, the violin, the flute and a soprano can all play it.</>,
      ]}/>
      <LbRemember>{t('88 keys: lower than a double bass, as high as a piccolo.', '88건반: 더블베이스보다 낮고, 피콜로만큼 높아요.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_spr_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, x])}/>}/>
    </LbPage>,
  ];
}
function PitchRangeLessonBook() { return <>{sprLbPages(false)}</>; }
