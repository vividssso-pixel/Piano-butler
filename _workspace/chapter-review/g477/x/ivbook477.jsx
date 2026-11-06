// ─── Phase 477: chapter 21, Intervals, built in full (Book rules 14 and 15; her 2026-10-17 02:05 macro-first plan: the
// whole first, then the parts, then the whole again). The third room of Level 4. Page 1 is the interval ladder: every
// interval from one note, a 2nd to an octave, on the staff and on the keys; the steps zoom in (counting, 2nd to 5th in the
// hand, 6th to the octave, melodic and harmonic, above the tonic with major and perfect); the screen lesson ends with the
// ladder again in the student's keys (Phase 476's [keys:...]), with the qualities.
// Placement (AMEB Music Craft 2026: Grade 1 all intervals by number, Grade 2 major and minor 2nd 3rd 6th 7th, perfect
// 1st 4th 5th 8th; ABRSM Theory: Grade 1 the number above the tonic in C G D F major, Grade 3 number and type).
// A note is { d, acc } (d: chapter 6's staff number, middle C 28; acc -1, 0 or 1); the old chapter's ivMidi, ivOrd, ivName,
// ivQuality, ivBuild and playIv are reused.

const IVX_N = (d, acc = 0) => ({ d, acc });
const ivxEn = (n) => n === 1 ? 'unison' : n === 8 ? 'octave' : n + (n === 2 ? 'nd' : n === 3 ? 'rd' : 'th');
const ivxShortEn = (n) => n === 8 ? '8ve' : ivxEn(n);
const ivxShort = (n) => LANG === 'ko' ? (n === 8 ? '8도' : n + '도') : ivxShortEn(n);
const ivxQ = (q) => LANG === 'ko' ? { M: '장', P: '완전', m: '단' }[q] : { M: 'major', P: 'perfect', m: 'minor' }[q];
const ivxQName = (q, n) => LANG === 'ko' ? ivxQ(q) + (n === 8 ? '8도' : n + '도') : ivxQ(q) + ' ' + ivxEn(n);
const ivxNoteTxt = (x) => dName(x.d) + (x.acc > 0 ? '♯' : x.acc < 0 ? '♭' : '');
// the key's notes from its tonic up an octave, as { d, acc }: the tonic near middle C (chapter 16's spelling)
const IVX_TONIC_D = { C: 28, Db: 29, D: 29, Eb: 30, E: 30, F: 31, Gb: 32, G: 32, Ab: 33, A: 33, Bb: 34, B: 34 };
function ivxScale(k) {
  const names = spellScale(k), d0 = IVX_TONIC_D[k] != null ? IVX_TONIC_D[k] : 28;
  const acc = (nm) => nm.length > 1 ? (nm[1] === '#' ? 1 : -1) : 0;
  return [...names, names[0]].map((nm, i) => IVX_N(d0 + i, acc(nm)));
}
// the quality above the tonic of a major key: M or P
const IVX_MP = { 2: 'M', 3: 'M', 4: 'P', 5: 'P', 6: 'M', 7: 'M', 8: 'P' };

// a staff with intervals. pairs: [{ a, b, harm, down (melodic, the higher note first), lab, lab2, hl ('a' | 'b' | 'both'),
// ladder (count up the lines and spaces from the lower note) }] laid out left to right (blank: an empty place; onlyA: the
// lower note alone, to write above). o.key: a key signature after the clef (a note the key already alters has no sign);
// o.bars: a bar line between the places; o.x0: where the first place starts; o.labSize. A harmonic 2nd: side by side, the
// lower note on the left; an accidental before its note (before the chord in a harmonic one)
function IvxStaff({ clef = 'treble', pairs, width = 320, o = {}, label }) {
  const ks = o.key ? skgKs(o.key, clef) : [], kmap = o.key ? skgMap(o.key) : {};
  const x0 = (o.x0 || 56) + (ks.length ? ks.length * 12 + 6 : 0), slot = (width - x0 - 6) / Math.max(1, pairs.length), notes = [], accs = [], labs = [], lads = [];
  const low = CLEFS[clef].low, signOf = (n) => { const k = kmap[dName(n.d)] || 0; return (n.acc || 0) === k ? null : (n.acc > 0 ? '#' : n.acc < 0 ? 'b' : 'n'); };
  pairs.forEach((p, i) => {
    if (p.blank) return;
    const cx = x0 + slot * (i + 0.5), second = p.harm && p.b.d - p.a.d === 1, gapM = p.ladder && !p.harm ? Math.min(48, slot * 0.4) : Math.min(o.gap || 30, slot * 0.3);
    let xa = p.harm ? (second ? cx - 7.4 : cx) : cx - gapM, xb = p.harm ? (second ? cx + 7.4 : cx) : cx + gapM;
    if (p.down && !p.harm) { const x = xa; xa = xb; xb = x; }
    const ca = p.hl === 'a' || p.hl === 'both' ? PEN_C : BK.ink, cb = p.hl === 'b' || p.hl === 'both' ? PEN_C : BK.ink;
    notes.push({ d: p.a.d, x: xa, color: ca }); if (!p.onlyA) notes.push({ d: p.b.d, x: xb, color: cb });
    const sa = signOf(p.a), sb = p.onlyA ? null : signOf(p.b), near = p.harm && sa && sb && p.b.d - p.a.d < 6;
    if (sb) accs.push([sb, (p.harm ? Math.min(xa, xb) : xb) - 17, p.b.d, cb]);
    if (sa) accs.push([sa, xa - 17 - (near ? 13 : 0), p.a.d, ca]);
    if (p.lab) labs.push([cx, p.lab, p.lab2, p.labCol]);
    if (p.ladder) lads.push([p, xa, xb, cx]);
  });
  const ysN = notes.map(n => dY(n.d)), yLab = Math.max(dY(low) + 30, ...ysN.map(y => y + 24)) + (o.labDy || 0);
  const bottomNeed = labs.length ? yLab + (labs.some(l => l[2]) ? 18 : 6) : Math.max(dY(low), ...ysN) + 14;
  const pad = [o.padTop != null ? o.padTop : 18, bottomNeed - Math.max(dY(low), ...ysN)];
  const ls = o.labSize || 13, hi = CLEFS[clef].high;
  return <SfStaff clef={clef} width={width} notes={notes} pad={pad} label={label} extra={(yOf, layer, txt) => layer !== 'over' ? null : <g>
    {ks.map(([sg, d], i) => <g key={'k' + i}>{tnAcc(sg, 48 + i * 12, yOf(d), BK.ink)}</g>)}
    {o.bars && pairs.slice(1).map((_, i) => <line key={'b' + i} x1={x0 + slot * (i + 1)} x2={x0 + slot * (i + 1)} y1={yOf(hi)} y2={yOf(low)} stroke={BK.ink} strokeWidth="1.2"/>)}
    {accs.map(([sg, x, d, c], i) => <g key={'a' + i}>{tnAcc(sg, x, yOf(d), c)}</g>)}
    {lads.map(([p, xa, xb, cx], i) => { const n = p.b.d - p.a.d + 1;
      return <g key={'l' + i}>{Array.from({ length: n }, (_, k) => { const x = p.harm ? cx + (p.b.d - p.a.d === 1 ? 24 : 16) + k * 10 : xa + (xb > xa ? 1 : -1) * (18 + (n > 1 ? k * (Math.abs(xb - xa) - 36) / (n - 1) : 0));
        return <text key={k} x={x} y={yOf(p.a.d + k) + 4.2} textAnchor="middle" fontSize={p.harm && n > 5 ? 10.5 : 11.5} fontWeight="900" fill={PEN_C} style={txt}>{k + 1}</text>; })}</g>; })}
    {labs.map(([x, a, b, c], i) => <text key={'t' + i} x={x} y={yLab} textAnchor="middle" fontSize={ls} fontWeight="900" fill={c || BK.ink} style={{fontFamily:'Inter, sans-serif'}}>{b ? <><tspan x={x} dy="0" fontSize={ls * 0.82} fontWeight="800" fill={BK.muted}>{a}</tspan><tspan x={x} dy={ls + 2}>{b}</tspan></> : a}</text>)}
  </g>}/>;
}
// a keyboard with a number over some white keys (counting, fingers): nums { d: '1' }; the rest as SacKeys
function IvxKeys({ d0 = 28, n = 8, nums = {}, numCol, o = {}, onTap, label }) {
  return <div role={label ? 'img' : undefined} aria-label={label}>
    <div aria-hidden="true" style={{display:'grid',gridTemplateColumns:'repeat(' + n + ',1fr)',padding:'0 ' + (3 / (n * 40 + 6) * 100) + '%',margin:'0 0 2px'}}>
      {Array.from({ length: n }, (_, i) => <div key={i} style={{textAlign:'center',fontSize:15,fontWeight:900,color:numCol || PEN_C,minHeight:20,fontFamily:'Inter, sans-serif'}}>{nums[d0 + i] == null ? '' : Array.isArray(nums[d0 + i]) ? <span style={{display:'inline-block',transform:'translateX(50%)'}}>{nums[d0 + i][0]}</span> : nums[d0 + i]}</div>)}
    </div>
    <SacKeys d0={d0} n={n} o={o} onTap={onTap}/>
  </div>;
}
// nums: a number over a white key, or [n, 'sharp'] over the black key to its right
// the ladder from a tonic: the 2nd to the octave as harmonic intervals; q: with major / perfect
const ivxLadder = (k, q, hlN) => { const sc = ivxScale(k); return sc.slice(1).map((b, i) => ({ a: sc[0], b, harm: true, lab: q ? ivxQ(IVX_MP[i + 2]) : ivxShort(i + 2), lab2: q ? ivxShort(i + 2) : null })); };
const ivxLadderLabel = (k, q) => { const sc = ivxScale(k);
  return t('From ' + ivxNoteTxt(sc[0]) + ', every interval up to the octave, both notes together: ' + sc.slice(1).map((b, i) => (q ? ivxQ(IVX_MP[i + 2]) + ' ' : '') + ivxEn(i + 2) + ' (' + ivxNoteTxt(b) + ')').join(', ') + '.',
    ivxNoteTxt(sc[0]) + '에서 옥타브까지 모든 음정, 두 음을 함께: ' + sc.slice(1).map((b, i) => (q ? ivxQ(IVX_MP[i + 2]) : '') + (i + 2 === 8 ? '8도' : (i + 2) + '도') + '(' + ivxNoteTxt(b) + ')').join(', ') + '.'); };

// the pictures' intervals (the pads play the same)
const IVX_P2 = [{ a: IVX_N(28), b: IVX_N(30), ladder: true }, { a: IVX_N(32), b: IVX_N(35), ladder: true }];
const IVX_P3 = [2, 3, 4, 5].map(n => ({ a: IVX_N(28), b: IVX_N(28 + n - 1), harm: true, n }));
const IVX_P4 = [6, 7, 8].map(n => ({ a: IVX_N(28), b: IVX_N(28 + n - 1), harm: true, n }));
const IVX_P5 = [{ a: IVX_N(28), b: IVX_N(30), harm: false, w: 'mel' }, { a: IVX_N(28), b: IVX_N(30), harm: true, w: 'harm' }, { a: IVX_N(32), b: IVX_N(33), harm: true, w: 'harm' }];
const IVX_P5B = [{ a: IVX_N(20), b: IVX_N(22), down: true, w: 'down' }, { a: IVX_N(18), b: IVX_N(22), harm: true, w: 'harm' }];
const ivxP5Lab = (w) => w === 'mel' ? t('melodic', '선율적') : w === 'down' ? t('going down', '내려가는') : t('harmonic', '화성적');
// Korean: words that belong together never part at a line end (아래 음, 두 음, 몇 도, 3번 손가락, a run of note names)
const ivxNbKo = (x) => typeof x !== 'string' ? x : x.replace(/(아래|위|두|그|한|여덟|같은) 음/g, '$1 음').replace(/둘 다/g, '둘 다').replace(/몇 도/g, '몇 도').replace(/(\d)번 손가락/g, '$1번 손가락').replace(/(?<![A-Za-z])([A-G][♯♭]?) (?=[A-G][♯♭]?(?![A-Za-z]))/g, '$1 ').replace(/([A-G][♯♭]?) 자리/g, '$1 자리').replace(/몇 번째/g, '몇 번째');
const ivxKoT = (x) => LANG === 'ko' ? ivxNbKo(x) : x;
const ivxTitle = (x) => <span style={{fontFamily:'inherit',fontVariantNumeric:'lining-nums'}}>{x}</span>;

function ivxLbPages(scr = false) {
  const ch = 'intervals';
  const live = (still, comp) => <LbLive still={still} live={comp}/>;
  const stack = (nodes, h, gap = 12, mw = 680) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap,width:'100%',maxWidth:mw,margin:'0 auto',alignItems:'stretch'}}>{nodes}</div></LbPic>;
  const X = (en, ko) => sscT(en, skgKo(ivxNbKo(ko)));
  const W = scr ? 320 : 380, M = scr ? 340 : 640;   // a staff's viewBox width, and its width on the page (print: about 1.7 times)
  const cap = (x, key = 'cap') => <div key={key} style={{textAlign:'center',fontSize:scr ? 14 : 13.5,fontWeight:800,color:BK.ink,margin:'2px auto 0',maxWidth:560,lineHeight:1.35,textWrap:'balance'}}>{sscSx(ivxKoT(x))}</div>;
  const nums8 = (d0) => Object.fromEntries(Array.from({ length: 8 }, (_, i) => [d0 + i, String(i + 1)]));
  const staff = (key, mw, node) => <div key={key} style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{node}</div>;

  // p1 (macro first): the interval ladder from C, a 2nd to an octave, and the keys counted 1 to 8; on screen the ladder pad
  const p1 = <LbLive still={stack([staff('lad', M, <IvxStaff pairs={ivxLadder('C')} width={W} o={{ labSize: scr ? 12 : 14 }} label={ivxLadderLabel('C')}/>),
    <div key="k" style={{maxWidth:420,margin:'10px auto 0',width:'100%',borderTop:'1px solid rgba(38,41,107,0.18)',paddingTop:8}}><IvxKeys d0={28} n={8} nums={nums8(28)} o={{ H: 100, lit: [60] }} label={t('The keys from middle C to the C above, counted 1 to 8: C is 1, the next C is 8.', '가운데 도부터 한 옥타브 위 C까지 건반을 1에서 8까지 세어요: C가 1, 다음 C가 8.')}/></div>,
    cap(t('Every interval from C, a 2nd to an octave. Its number: count the letters, both notes included.', 'C에서 옥타브까지 모든 음정. 음이름을 아래 음부터 위 음까지 세면 몇 도인지 알아요.'))], 400, 10)} live={<IvxMapPad/>}/>;
  // p2: counting: C to E, G to C, the lines and spaces counted from the lower note
  const p2 = stack([staff('s', scr ? 330 : 600, <IvxStaff pairs={IVX_P2.map(p => ({ ...p, lab: ivxShort(p.b.d - p.a.d + 1) }))} width={scr ? 320 : 300} o={{ labSize: 14 }} label={t('Two intervals on the treble staff, one note after the other, each counted up its lines and spaces: C to E, 1 2 3, a 3rd; G to C, 1 2 3 4, a 4th.', '높은음자리표 오선의 두 음정, 한 음씩: 줄과 칸을 세어요. C에서 E는 1 2 3, 3도; G에서 C는 1 2 3 4, 4도.')}/>),
    <div key="k" style={{maxWidth:420,margin:'0 auto',width:'100%'}}><IvxKeys d0={28} n={8} nums={{ 28: '1', 29: '2', 30: '3' }} o={{ H: 110, lit: [60], pale: [64] }} label={t('The keys C D E counted 1 2 3: C to E is a 3rd.', 'C D E 건반을 1 2 3으로 세어요: C에서 E는 3도.')}/></div>], 300, 16);
  // p3: the 2nd to the 5th in the hand: C position, thumb and each finger (the staff first, the keys under it)
  const p3 = stack([staff('s', M, <IvxStaff pairs={IVX_P3.map(p => ({ ...p, lab: t('1 and ' + p.n, '1번과 ' + p.n + '번'), lab2: ivxShort(p.n) }))} width={scr ? 320 : 340} o={{ labSize: 14 }} label={t('Four intervals from C, both notes together: C and D, a 2nd (fingers 1 and 2); C and E, a 3rd (1 and 3); C and F, a 4th (1 and 4); C and G, a 5th (1 and 5).', 'C에서 네 음정, 두 음을 함께: C와 D는 2도(1번과 2번), C와 E는 3도(1번과 3번), C와 F는 4도(1번과 4번), C와 G는 5도(1번과 5번).')}/>),
    <div key="k" style={{maxWidth:280,margin:'0 auto',width:'100%'}}><IvxKeys d0={28} n={5} nums={{ 28: '1', 29: '2', 30: '3', 31: '4', 32: '5' }} numCol={PEN_N} o={{ H: 96, lit: [60], pale: [62, 64, 65, 67] }} label={t('C position, the right hand: finger 1 on C, 2 on D, 3 on E, 4 on F, 5 on G.', 'C 자리의 오른손: 1번 손가락은 C, 2번은 D, 3번은 E, 4번은 F, 5번은 G.')}/></div>], 340, 8);
  // p4: the 6th, the 7th, the octave; the keys counted to 8
  const p4 = stack([staff('s', scr ? 330 : 500, <IvxStaff pairs={IVX_P4.map(p => ({ ...p, lab: ivxShort(p.n) }))} width={scr ? 320 : 290} o={{ labSize: 14 }} label={t('Three intervals from middle C, both notes together: C and A, a 6th; C and B, a 7th; C and the C above, an octave.', '가운데 도에서 세 음정, 두 음을 함께: C와 A는 6도, C와 B는 7도, C와 위의 C는 옥타브.')}/>),
    <div key="k" style={{maxWidth:440,margin:'0 auto',width:'100%'}}><IvxKeys d0={28} n={8} nums={nums8(28)} o={{ H: 110, lit: [60], pale: [69, 71, 72] }} label={t('The keys from C to C counted 1 to 8: A is 6, B is 7, C is 8.', 'C에서 C까지의 건반을 1에서 8까지 세어요: A가 6, B가 7, C가 8.')}/></div>], 320, 16);
  // p5: melodic and harmonic, on both staves; a melodic interval going down
  const p5 = stack([staff('t', scr ? 330 : 540, <IvxStaff pairs={IVX_P5.map(p => ({ ...p, lab: ivxP5Lab(p.w), lab2: ivxShort(p.b.d - p.a.d + 1) }))} width={320} o={{ labSize: 13.5, bars: true }} label={t('On the treble staff: C then E, a melodic 3rd; C and E together, a harmonic 3rd; G and A together, a harmonic 2nd, the two notes side by side.', '높은음자리표 오선: C 다음 E는 선율적 3도, C와 E를 함께 치면 화성적 3도, G와 A를 함께 치면 화성적 2도(두 음이 옆으로 붙어 있어요).')}/>),
    staff('b', scr ? 330 : 540, <IvxStaff clef="bass" pairs={IVX_P5B.map(p => ({ ...p, lab: ivxP5Lab(p.w), lab2: ivxShort(p.b.d - p.a.d + 1) }))} width={320} o={{ labSize: 13.5 }} label={t('On the bass staff: D then B below it, a 3rd going down; G and D together, a harmonic 5th.', '낮은음자리표 오선: D 다음 그 아래 B는 내려가는 3도, G와 D를 함께 치면 화성적 5도.')}/>)], 380, 10);
  // p6: above the tonic in G major, with its key signature: major and perfect; the keys of G major under it
  const g6 = ivxLadder('G', true);
  const gKeys = <div key="k" style={{maxWidth:440,margin:'0 auto',width:'100%'}}><IvxKeys d0={32} n={8} nums={{ 32: '1', 33: '2', 34: '3', 35: '4', 36: '5', 37: '6', 38: ['7', 'sharp'], 39: '8' }} o={{ H: 100, lit: [67], pale: [78] }} label={t('The keys from G to G: G is 1, F sharp (7) the black key before the top G.', 'G에서 G까지의 건반: G가 1, F♯(7)은 위 G 바로 앞의 검은 건반.')}/></div>;
  const p6 = stack(scr ? [g6.slice(0, 4), g6.slice(4)].map((row, r) => staff(r, 330, <IvxStaff pairs={row} width={320} o={{ labSize: 13, key: 'G' }} label={r ? '' : ivxLadderLabel('G', true)}/>))
    : [staff('s', 660, <IvxStaff pairs={g6} width={400} o={{ labSize: 13, key: 'G' }} label={ivxLadderLabel('G', true)}/>), gKeys], scr ? 330 : 360, 14);

  // the check icons
  const tx = (x, c, col, s = 18, y = 28) => '<text x="' + x + '" y="' + y + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + s + '" font-weight="900" fill="' + col + '">' + c + '</text>';
  const head = (x, y, col) => '<ellipse cx="' + x + '" cy="' + y + '" rx="6" ry="4.4" fill="' + col + '"/>';
  const st5 = '<g stroke="' + PEN_N + '" stroke-opacity="0.55" stroke-width="1.2">' + [8, 14, 20, 26, 32].map(y => '<line x1="6" x2="86" y1="' + y + '" y2="' + y + '"/>').join('') + '</g>';
  const ic = {
    count: [{ k: 'raw', svg: st5 + head(18, 32, PEN_N) + head(70, 26, PEN_N) + tx(34, '1', PEN_C, 11, 36) + tx(46, '2', PEN_C, 11, 33) + tx(58, '3', PEN_C, 11, 30) }],
    hand: [{ k: 'raw', svg: tx(22, '1', PEN_N, 20, 30) + '<line x1="34" x2="54" y1="22" y2="22" stroke="' + PEN_C + '" stroke-width="2.4"/>' + tx(68, '5', PEN_N, 20, 30) }],
    big: [{ k: 'raw', svg: st5 + head(24, 35, PEN_N) + head(66, 14, PEN_C) + tx(84, '8', PEN_C, 12, 10) }],
    harm: [{ k: 'raw', svg: st5 + head(20, 26, PEN_N) + head(36, 14, PEN_N) + head(64, 26, PEN_C) + head(64, 14, PEN_C) }],
    tonic: [{ k: 'raw', svg: tx(16, 'G', PEN_N, 18, 28) + (LANG === 'ko' ? tx(56, '장3도', PEN_C, 15, 28) : tx(58, 'major', PEN_C, 12, 19) + tx(58, '3rd', PEN_C, 14, 34)) }],
  };
  const checksRows = [
    ['count', t('I can count an interval on the staff, both notes included', '오선에서 두 음을 모두 세어 몇 도인지 말할 수 있어요')],
    ['hand', t('I can play a 2nd, 3rd, 4th and 5th in C position and name them', 'C 자리에서 2도, 3도, 4도, 5도를 치고 이름을 말할 수 있어요')],
    ['big', t('I can find a 6th, a 7th and an octave on the staff and on the keys', '오선과 건반에서 6도, 7도, 옥타브를 찾을 수 있어요')],
    ['harm', t('I can tell a melodic interval from a harmonic one, and write both', '선율적 음정과 화성적 음정을 구별하고, 둘 다 쓸 수 있어요')],
    ['tonic', t('I can name each interval above the tonic of C, G, D and F major', 'C, G, D, F장조에서 으뜸음 위의 음정을 말할 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? skgKo(sscNbKo(ivxNbKo(x))) : sscNbEn(x)]);
  const ch9 = bkChapterNo('reading-steps'), ch16 = bkChapterNo('scales');

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <>두 음 사이의 거리가 <b>음정</b>이에요. 아래&nbsp;음부터 위&nbsp;음까지 음이름을 세어 몇&nbsp;도인지 말해요.</> : <>An <b>interval</b> is the distance between two notes. Its number counts the letter names from the lower note to the higher.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Counting an interval', '음정 세기'), 2], [t('2nd to 5th, in the hand', '손 안의 2도~5도'), 3], [t('6th, 7th and octave', '6도, 7도, 옥타브'), 4], [t('Melodic and harmonic', '선율적 음정과 화성적 음정'), 5], [t('Above the tonic', '으뜸음 위의 음정'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}<span>{n}</span></span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)',textWrap:'pretty'}}>{bkGoal(15)}<span>{sscSx(x.replace(/^I can /, ''))}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Counting an interval', '음정 세기')}>
      {live(p2, <IvxCountPad set="p2"/>)}
      <LbDefs items={[
        [t('number', '몇 도(도수)'), X('Count the letter names from the lower note to the higher; both notes count. C to E: C D E, a 3rd.', '아래 음부터 위 음까지 음이름을 세어요. 두 음 모두 세요. C에서 E: C D E, 3도.')],
        [t('on the staff', '오선에서'), X('Count each line and space from the lower note up to the higher one. The lower note is 1.', '아래 음부터 위 음까지 줄과 칸을 하나씩 세어요. 아래 음이 1이에요.')],
        [t('unison', '1도'), X('Both notes on the same line or space: the same letter. Its number is 1.', '같은 줄이나 칸에 있는 두 음, 같은 음이름이에요. 세면 1이에요.')],
      ]}/>
      <LbPiano steps={[
        X('Play C, then E. Count aloud: C D E, a 3rd.', 'C를 치고 E를 쳐요. 소리 내어 세요: C D E, 3도.'),
        X('Play G, then the C above it. Count: G A B C, a 4th.', 'G를 치고 그 위의 C를 쳐요. 세어요: G A B C, 4도.'),
      ]}/>
      <LbRemember>{X('Count both notes: the lower note is 1.', '두 음을 모두 세요. 아래 음이 1이에요.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={ivxTitle(t('2nd to 5th, in the hand', '손 안의 2도~5도'))}>
      {live(p3, <IvxHandPad/>)}
      <LbDefs items={[
        [t('2nd', '2도'), X('The next letter: a step (chapter ' + ch9 + '). A line to the next space, or a space to the next line.', '바로 다음 음이름, 한 걸음이에요(' + ch9 + '챕터). 줄에서 옆 칸으로, 칸에서 옆 줄로.')],
        [t('3rd', '3도'), X('Skip one letter: a line to the next line, or a space to the next space.', '음이름 하나를 건너뛰어요. 줄에서 바로 위 줄로, 칸에서 바로 위 칸으로.')],
        [t('4th', '4도'), X('Skip two letters: a line to a space, or a space to a line.', '음이름 둘을 건너뛰어요. 줄에서 칸으로, 칸에서 줄로.')],
        [t('5th', '5도'), X('Skip three letters: line to line or space to space, with one line (or space) between.', '음이름 셋을 건너뛰어요. 줄에서 줄로, 칸에서 칸으로, 사이에 줄(칸) 하나.')],
        [t('in the hand', '손 안에서'), X('In a five-finger position, the thumb and finger 2 play a 2nd; with finger 3, a 3rd; 4, a 4th; 5, a 5th.', '다섯 손가락 자리에서 엄지와 2번 손가락은 2도, 3번은 3도, 4번은 4도, 5번은 5도를 쳐요.')],
      ]}/>
      <LbPiano steps={[
        X('Right hand in C position: play 1 and 2 together, then 1 and 3, 1 and 4, 1 and 5. Say: 2nd, 3rd, 4th, 5th.', '오른손 C 자리: 1번과 2번을 함께 친 다음, 1번과 3번, 1번과 4번, 1번과 5번을 쳐요. 말해요: 2도, 3도, 4도, 5도.'),
        X('Move to G position, thumb on G, and play them again.', '엄지를 G에 놓고 G 자리에서 다시 쳐요.'),
      ]}/>
      <LbRemember>{X('Thumb and finger 5: a 5th. With the thumb, the finger’s number is the interval’s.', '엄지와 5번 손가락은 5도. 엄지와 함께 치면 손가락 번호와 몇 도가 같아요.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={ivxTitle(t('6th, 7th and octave', '6도, 7도, 옥타브'))}>
      {live(p4, <IvxCountPad set="p4"/>)}
      <LbDefs items={[
        [t('6th', '6도'), X('Six letters: C to A.', '음이름 여섯 개: C에서 A까지.')],
        [t('7th', '7도'), X('Seven letters: C to B, one short of the octave.', '음이름 일곱 개: C에서 B까지. 옥타브보다 하나 적어요.')],
        [t('octave', '옥타브'), X('Eight letters, from a note to the next one of the same name: C to C. Also called an 8th; written 8ve for short.', '음이름 여덟 개, C에서 다음 C까지예요. 8도라고도 하고, 줄여서 8ve로 써요.')],
        [t('odd and even', '홀수와 짝수'), X('Odd (3rd, 5th, 7th): line to line, or space to space. Even (2nd, 4th, 6th, octave): line to space, or space to line.', '홀수(3·5·7도)는 줄에서 줄로, 칸에서 칸으로. 짝수(2·4·6·8도)는 줄에서 칸으로, 칸에서 줄로.')],
      ]}/>
      <LbPiano steps={[
        X('Play the picture’s intervals: C and A, C and B, C and C. Say: 6th, 7th, octave.', '그림의 음정을 쳐요: C와 A, C와 B, C와 C. 말해요: 6도, 7도, 옥타브.'),
        X('Play every C on the piano, one octave apart, from the lowest to the highest.', '피아노의 모든 C를 가장 낮은 C부터 가장 높은 C까지 한 옥타브씩 올라가며 쳐요.'),
      ]}/>
      <LbRemember>{X('An octave: the same letter, 8 counting both notes: C to C.', '옥타브: 두 음을 모두 세어 8, 같은 음이름이에요.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Melodic and harmonic', '선율적 음정과 화성적 음정')}>
      {live(p5, <IvxCountPad set="p5"/>)}
      <LbDefs items={[
        [t('melodic interval', '선율적 음정'), X('One note after the other. Written side by side.', '두 음을 차례로 쳐요. 옆으로 나란히 써요.')],
        [t('harmonic interval', '화성적 음정'), X('Both notes together. Written one above the other.', '두 음을 함께 쳐요. 위아래로 쌓아 써요.')],
        [t('a harmonic 2nd', '화성적 2도'), X('The two notes touch, side by side: the lower one on the left.', '두 음이 옆으로 붙어요. 아래 음이 왼쪽이에요.')],
        [t('going down', '내려가는 음정'), X('Count from the lower note just the same: D down to B is a 3rd.', '똑같이 아래 음부터 세어요. D에서 B로 내려가도 3도예요.')],
      ]}/>
      <LbPiano steps={[
        X('Play each interval of the picture, one note after the other, then together.', '그림의 음정마다 두 음을 차례로 친 다음, 함께 쳐요.'),
        X('Your teacher plays an interval. Say: melodic or harmonic.', '선생님이 음정을 쳐요. 선율적인지 화성적인지 말해요.'),
      ]}/>
      <LbRemember>{X('Melodic: one after the other. Harmonic: together.', '선율적은 차례로, 화성적은 함께.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Above the tonic', '으뜸음 위의 음정')}>
      {live(p6, <IvxTonicPad/>)}
      <LbDefs items={[
        [t('tonic', '으뜸음'), X('The key’s first note (chapter ' + ch16 + '): in G major, G.', '조의 첫 음이에요(' + ch16 + '챕터). G장조에서는 G.')],
        [t('above the tonic', '으뜸음 위'), X('Each note of the scale makes an interval with the tonic. Its number is the note’s degree: B in G major is a 3rd.', '음계의 각 음과 으뜸음 사이의 음정이에요. 몇 도인지는 그 음이 음계의 몇 번째 음인지와 같아요. G장조의 B는 3도.')],
        [t('major and perfect', '장음정과 완전음정'), X('From the tonic of a major key, the 2nd, 3rd, 6th and 7th are major; the 4th, 5th and octave are perfect.', '장조 으뜸음에서 2·3·6·7도는 장음정, 4·5·8도는 완전음정이에요.')],
      ]}/>
      <LbPiano steps={[
        X('Play G with each note of G major above it, together. Say: major 2nd, major 3rd, perfect 4th, perfect 5th, major 6th, major 7th, perfect octave.', 'G와 그 위의 G장조 음을 하나씩 함께 쳐요. 말해요: 장2도, 장3도, 완전4도, 완전5도, 장6도, 장7도, 완전8도.'),
        X('Do the same in C, D and F major.', 'C, D, F장조에서도 똑같이 해요.'),
      ]}/>
      <LbRemember>{X('From the tonic: 2nd, 3rd, 6th, 7th major; 4th, 5th, octave perfect.', '으뜸음에서 2·3·6·7도는 장음정, 4·5·8도는 완전음정.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, sscSx(x)])}/>} live={<FiveChecks376 storeKey="pb_five_ivx_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, sscSx(x)])}/>}/>
    </LbPage>,
  ];
}
function IntervalsLessonBook() { return <>{ivxLbPages(false)}</>; }
