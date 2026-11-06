// ─── Phase 471: chapter 16 (Scales): the Lesson Book, built in full under Book rules 14 and 15 (her 2026-10-14 09:17
// '계속 가줘 최종검토는 한꺼번에하게'). The level plan's scope for this room (Level 3): C, G and F major: whole, whole,
// half, whole, whole, whole, half; the scale degrees; the fingering (AMEB Preliminary). D and B flat major and the
// harmonic minors (Grade 1) are the drill's extra levels; rule 13 keeps major and minor here (the pentatonic, blues,
// whole-tone scales and the modes wait for More Scales). It builds on chapter 11 (a half step is a semitone, a whole
// step a tone; sharps and flats; 'whole, whole, half, whole, whole, whole, half' as the major scale's recipe). Every
// fingering comes from SCALES (Sohyun's checked fingerings): C and G standard, F's right hand 1 2 3 4, 1 2 3 4.

const SSC_L = ['C', 'D', 'E', 'F', 'G', 'A', 'B'], SSC_PCS = [0, 2, 4, 5, 7, 9, 11];
const SSC_MAJOR = [0, 2, 4, 5, 7, 9, 11, 12];
const SSC_STEPS = ['whole', 'whole', 'half', 'whole', 'whole', 'whole', 'half'];
const SSC_BASE = { C: 0, G: 7, F: 5, D: 2, Bb: 10 };   // the tonic as a key from middle C (playKey)
// the keys of a keyboard that starts on a white key: each white key, and the black key after it
function sscKeyList(start, n) {
  const s0 = SSC_L.indexOf(start), out = [];
  for (let i = 0; i < n; i++) { const j = s0 + i, L = SSC_L[j % 7], semi = SSC_PCS[j % 7] + 12 * Math.floor(j / 7) - SSC_PCS[s0];
    out.push({ id: 'w' + i, white: true, i, L, semi });
    if ('CDFGA'.includes(L) && i < n - 1) out.push({ id: 'b' + i, white: false, i, L, semi: semi + 1 }); }
  return out;
}
// the major scale's eight keys on a keyboard from its tonic, with their names (G major's 7th is F♯, F major's 4th B♭)
function sscScale(start) {
  const ks = sscKeyList(start, 8), names = spellScale(start);
  return SSC_MAJOR.map((o, d) => ({ ...ks.find(k => k.semi === o), d, name: names[d % 7] }));
}
// a name with its sign in the music font (inside SVG text)
const sscNameSvg = (nm, sz) => <>{nm[0]}{nm.length > 1 && <tspan style={{fontFamily:MUSIC_FONT,fontWeight:400}} fontSize={sz * 1.35} dy={nm[1] === 'b' ? 1 : 0}>{nm[1] === 'b' ? '♭' : '♯'}</tspan>}</>;
const sscName = (nm) => nm.length > 1 ? <>{nm[0]}{tnSign(nm[1] === 'b' ? 'b' : '#')}</> : nm;
const sscNameTxt = (nm) => nm.length > 1 ? nm[0] + (nm[1] === 'b' ? '♭' : '♯') : nm;

// One octave of keys from a tonic, the book's way (navy outlines, the scale's keys named), and tappable on screen.
// o: nums (degree numbers on the scale's keys), steps (whole and half under the keys, each on a straight bracket),
// fingers ([8] over the keys, with a hand label), boxes ([8]: undefined no box, '' an empty box, else filled; a black
// note's box sits over the white key of its letter, every box named), lit (a degree lit coral), done (degrees played),
// miss (a key id outlined), coral (degrees whose key is tinted: the sharp or flat), arrow ({ from, to, label, over }:
// a straight arrow), hideNames (every white key named alike, no black key named: nothing gives the scale away), onTap
function SscKeys({ start = 'C', o = {}, label, onTap }) {
  const W = 44, H = o.H || 150, BW = 28, BH = Math.round(H * 0.61), n = 8;
  const keys = sscKeyList(start, n), sc = sscScale(start), byId = {}; sc.forEach(k => { byId[k.id] = k; });
  const blackF = o.fingers && sc.some(s => !s.white), arrowOver = o.arrow && o.arrow.over;
  const blackX = o.boxes && !o.hideNames && sc.some((s, d) => !s.white && o.boxes[d] !== undefined);
  // the step words: a second row where two would touch (F major's G A, A B♭)
  const ko = LANG === 'ko', sw = (w) => ko ? 16 : w === 'half' ? 23 : 36;   // the words' widths at 12 (Korean 14)
  const x0 = 4, cx = (k) => k.white ? x0 + (k.i + 0.5) * W : x0 + (k.i + 1) * W;
  const stepRow = []; if (o.steps) { let last = null; sc.slice(0, 7).forEach((s, d) => { const m = (cx(s) + cx(sc[d + 1])) / 2, w = sw(SSC_STEPS[d]);
    const r = last && last.r === 0 && m - last.m < (w + last.w) / 2 + 5 ? 1 : 0; stepRow.push(r); last = { m, w, r }; }); }
  const rows2 = stepRow.includes(1);
  const T = (o.boxes ? (blackX ? 70 : 50) + (o.hand ? 14 : 0) : o.fingers ? (blackF ? 70 : 48) : 8) + (arrowOver ? 30 : 0);
  const B = o.steps ? (rows2 ? 58 : 40) : o.arrow && !o.arrow.over ? 36 : 8;
  const VW = x0 * 2 + n * W, VH = T + H + B;
  const done = new Set(o.done || []), coral = new Set(o.coral || []), lit = new Set([].concat(o.lit == null ? [] : o.lit));
  const st = (k) => { const s = byId[k.id]; if (!s) return 'off'; if (lit.has(s.d)) return 'lit'; if (done.has(s.d)) return 'done'; if (coral.has(s.d)) return 'coral'; return 'on'; };
  const fillW = { lit: '#f6c4b2', done: '#e4e5f3', coral: '#fbe3da', on: '#fff', off: '#fff' }, fillB = { lit: '#f08c70', done: '#6d6f9c', coral: PEN_C, on: PEN_N, off: PEN_N };
  const tap = (k) => onTap ? () => onTap(k) : undefined;
  const nm = (s, y, size, fill) => <text x={cx(s)} y={y} textAnchor="middle" fontSize={size} fontWeight="900" fill={fill} style={{pointerEvents:'none'}}>{sscNameSvg(s.name, size)}</text>;
  const bx = (s) => s.white ? cx(s) : cx(keys.find(k => k.white && k.L === s.name[0]));   // a black note's box: over its letter's white key
  return (
    <svg viewBox={`0 0 ${VW} ${VH}`} role="img" aria-label={label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>
      {keys.filter(k => k.white).map(k => { const s = byId[k.id], state = st(k), miss = o.miss === k.id, y = T + H - (o.nums ? 46 : 16);
        return <g key={k.id} onClick={tap(k)} style={{cursor:onTap ? 'pointer' : 'default'}} data-ssc={k.id}>
          <rect x={x0 + k.i * W} y={T} width={W} height={H} rx="3" fill={fillW[state]} stroke={miss ? PEN_C : PEN_N} strokeWidth={miss ? 3.2 : 1.6}/>
          {o.hideNames ? <text x={cx(k)} y={y} textAnchor="middle" fontSize="15" fontWeight="800" fill={PEN_N} style={{pointerEvents:'none'}}>{k.L}</text>
            : s ? nm(s, y, 16, PEN_N) : <text x={cx(k)} y={y} textAnchor="middle" fontSize="14" fontWeight="800" fill="rgba(38,41,107,0.4)" style={{pointerEvents:'none'}}>{k.L}</text>}
          {s && o.nums && <g style={{pointerEvents:'none'}}><circle cx={cx(k)} cy={T + H - 22} r="13" fill={s.d === 0 || s.d === 7 ? PEN_C : '#fff'} stroke={s.d === 0 || s.d === 7 ? PEN_C : PEN_N} strokeWidth="1.6"/>
            <text x={cx(k)} y={T + H - 16.5} textAnchor="middle" fontSize="15" fontWeight="900" fill={s.d === 0 || s.d === 7 ? '#fff' : PEN_N}>{s.d + 1}</text></g>}
        </g>; })}
      {keys.filter(k => !k.white).map(k => { const s = byId[k.id], state = st(k), miss = o.miss === k.id;
        return <g key={k.id} onClick={tap(k)} style={{cursor:onTap ? 'pointer' : 'default'}} data-ssc={k.id}>
          <rect x={cx(k) - BW / 2} y={T} width={BW} height={BH} rx="2" fill={fillB[state]} stroke={miss ? PEN_C : PEN_N} strokeWidth={miss ? 3.2 : 1}/>
          {s && !o.hideNames && nm(s, T + 27, 13.5, '#fff')}
          {s && o.nums && <g style={{pointerEvents:'none'}}><circle cx={cx(k)} cy={T + BH - 18} r="11" fill="#fff" stroke={PEN_C} strokeWidth="1.6"/><text x={cx(k)} y={T + BH - 13} textAnchor="middle" fontSize="13.5" fontWeight="900" fill={PEN_N}>{s.d + 1}</text></g>}
        </g>; })}
      {o.fingers && <g>{o.hand && <text x={x0} y={(arrowOver ? 14 : T - (blackF ? 56 : 34))} fontSize="12" fontWeight="900" fill={PEN_C}>{o.hand}</text>}
        {sc.map((s, d) => { const fy = T - (s.white ? 14 : 38); return <g key={d}>{!s.white && <line x1={cx(s)} x2={cx(s)} y1={fy + 11} y2={T} stroke={PEN_N} strokeWidth="1" strokeDasharray="2 2"/>}<circle cx={cx(s)} cy={fy} r="11" fill={lit.has(d) ? PEN_C : '#fff'} stroke={PEN_N} strokeWidth="1.4"/>
          <text x={cx(s)} y={fy + 5} textAnchor="middle" fontSize="15" fontWeight="900" fill={lit.has(d) ? '#fff' : PEN_N}>{o.fingers[d]}</text></g>; })}</g>}
      {o.boxes && <g>{o.hand && <text x={x0} y={14} fontSize="12" fontWeight="900" fill={PEN_C}>{o.hand}</text>}
        {sc.map((s, d) => o.boxes[d] !== undefined && <g key={'x' + d}>
          {blackX && <text x={bx(s)} y={T - 44} textAnchor="middle" fontSize="13" fontWeight="900" fill={PEN_N}>{sscNameSvg(s.name, 13)}</text>}
          {!s.white && !o.hideNames && <line x1={bx(s)} y1={T - 6} x2={cx(s)} y2={T} stroke={PEN_N} strokeWidth="1.6" strokeDasharray="3 2"/>}
          <rect x={bx(s) - 16} y={T - 38} width="32" height="32" rx="3" fill={o.boxes[d] !== '' ? '#fdf3ef' : '#fff'} stroke={o.boxes[d] !== '' ? PEN_C : PEN_N} strokeWidth="1.5"/>
          {o.boxes[d] !== '' && <text x={bx(s)} y={T - 15} textAnchor="middle" fontSize="18" fontWeight="900" fontStyle="italic" fill={PEN_C}>{o.boxes[d]}</text>}</g>)}</g>}
      {o.steps && sc.slice(0, 7).map((s, d) => { const a = cx(s) + 5, b = cx(sc[d + 1]) - 5, half = SSC_STEPS[d] === 'half', c = half ? PEN_C : PEN_N, y = T + H + 9;
        return <g key={'s' + d}><path d={`M${a} ${y - 5} L${a} ${y} L${b} ${y} L${b} ${y - 5}`} fill="none" stroke={c} strokeWidth={half ? 2.4 : 1.6} strokeLinejoin="round"/>
          {stepRow[d] === 1 && <line x1={(a + b) / 2} x2={(a + b) / 2} y1={y + 2} y2={y + 22} stroke={c} strokeWidth="1" strokeDasharray="2 2"/>}
          <text x={(a + b) / 2} y={y + (stepRow[d] === 1 ? 40 : 21)} textAnchor="middle" fontSize={ko ? 14 : 12} fontWeight="900" fill={c}>{half ? t('half', '반') : t('whole', '온')}</text></g>; })}
      {o.arrow && (() => { const a = cx(sc[o.arrow.from]), b = cx(sc[o.arrow.to]), over = o.arrow.over, y = over ? T - (o.fingers ? (blackF ? 62 : 34) : 8) : T + H + 10, dir = b > a ? 1 : -1;
        return <g><path d={`M${a} ${y + (over ? 4 : -4)} L${a} ${y} L${b} ${y}`} fill="none" stroke={PEN_C} strokeWidth="2.4" strokeLinejoin="round"/>
          <path d={`M${b - 7 * dir} ${y - 5} L${b} ${y} L${b - 7 * dir} ${y + 5}`} fill="none" stroke={PEN_C} strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round"/>
          <text x={b + 10 * dir} y={y + 4.5} textAnchor={dir > 0 ? 'start' : 'end'} fontSize="13" fontWeight="900" fill={PEN_C}>{o.arrow.label}</text></g>; })()}
    </svg>
  );
}
// the scale on the treble staff, as semibreves: its sign before the note, the numbers (or names) under, the tonic coral
const SSC_D0 = { C: 28, G: 32, F: 31, D: 29, Bb: 34 };   // the tonic's place (dY: C4 = 28)
// o: gap, lit, tonic (both tonics coral), tonicLabel (the word under them), under ('nums' | 'names'), noAcc (room left
// for the sign, the sign not drawn), accInk, fingers ({ RH, LH }: over and under the notes), padTop, extra
function SscStaff({ start = 'C', o = {}, label }) {
  const sc = sscScale(start), d0 = SSC_D0[start] - (o.octDown ? 7 : 0), gap = o.gap || 42, x0 = 74, AW = 12;   // AW: room before a note with a sign
  const ids = o.range ? Array.from({ length: o.range[1] - o.range[0] + 1 }, (_, j) => o.range[0] + j) : [0, 1, 2, 3, 4, 5, 6, 7];   // o.range: a part of the scale
  let shift = 0;
  const notes = ids.map((i, j) => { if (o.noAcc || sc[i].name.length > 1) shift += AW; return { i, d: d0 + i, x: x0 + j * gap + shift, color: o.lit === i || ((o.tonic) && (i === 0 || i === 7)) ? PEN_C : PEN_N }; });
  const w = x0 + (ids.length - 1) * gap + shift + 26, coral = (i) => (o.tonic && (i === 0 || i === 7)) || o.lit === i;
  return <div style={{width:'100%'}}><SfStaff clef="treble" width={w} span={[4, w - 4]} pad={[o.padTop || (o.fingers ? 30 : 16), o.tonicLabel ? 62 : o.under ? 46 : o.fingers ? 36 : 18]} label={label} notes={notes}
    extra={(yOf, layer, txt) => layer === 'over' && <g>
      {!o.noAcc && notes.map(n => sc[n.i].name.length > 1 && <g key={'a' + n.i}>{tnAcc(sc[n.i].name[1] === 'b' ? 'b' : '#', n.x - 19, yOf(n.d), o.accInk || PEN_C)}</g>)}
      {o.under && notes.map(n => <text key={'u' + n.i} x={n.x} y={yOf(Math.min(26, d0 - 2)) + 16} textAnchor="middle" fontSize="15" fontWeight="900" fill={coral(n.i) ? PEN_C : PEN_N} style={txt}>{o.under === 'names' ? sscNameSvg(sc[n.i].name, 15) : n.i + 1}</text>)}
      {o.tonicLabel && notes.filter(n => n.i === 0 || n.i === 7).map(n => <text key={'t' + n.i} x={n.x} y={yOf(Math.min(26, d0 - 2)) + 34} textAnchor="middle" fontSize="13" fontWeight="900" fill={PEN_C} style={txt}>{o.tonicLabel}</text>)}
      {o.fingers && ['RH', 'LH'].map(h => o.fingers[h] && <g key={h}>{notes.map(n => <text key={n.i} x={n.x} y={h === 'RH' ? Math.min(yOf(42), yOf(n.d) - 14) : Math.max(yOf(26) + 4, yOf(n.d) + 24)} textAnchor="middle" fontSize="15" fontWeight="900" fill={PEN_N} style={txt}>{o.fingers[h][n.i]}</text>)}</g>)}
      {o.extra && o.extra(yOf, txt, notes)}
    </g>}/></div>;
}

// ♯ and ♭ in running text, in the music font (the text fonts' own signs are thin, or full width in Korean)
const sscSx = (x) => typeof x !== 'string' || !/[♯♭]/.test(x) ? x : x.split(/([♯♭])/).map((p, i) => p === '♯' ? <React.Fragment key={i}>{tnSign('#')}</React.Fragment> : p === '♭' ? <React.Fragment key={i}>{tnSign('b')}</React.Fragment> : p);
// the places a line must not break: a number and its word, a pair of note names, a two-word term
const sscNbKo = (x) => x.replace(/ 번\./g, ' 번.').replace(/칠 수 있어요/g, '칠 수 있어요').replace(/(온|반) 걸음/g, '$1 걸음').replace(/손가락 번호/g, '손가락 번호')
  .replace(/([34])번 넘기기/g, '$1번 넘기기').replace(/엄지 밑으로 넣기/g, '엄지 밑으로 넣기').replace(/밑으로 넣/g, '밑으로 넣').replace(/(?<![A-Za-z])([A-G][♯♭]?) ([A-G][♯♭]?)(?![A-Za-z])/g, '$1 $2').replace(/(\d) (\d)/g, '$1 $2').replace(/(\d) (\d)/g, '$1 $2');
const sscNbEn = (x) => x.replace(/([TS]) (?=[TS](?![A-Za-z]))/g, '$1 ').replace(/(F sharp|B flat|[34] over|1 to 8|thumb under)/g, (m) => m.replace(/ /g, ' ')).replace(/(?<![A-Za-z])([A-G][♯♭]?) ([A-G][♯♭]?)(?![A-Za-z])/g, '$1 $2').replace(/(\d) (\d)/g, '$1 $2').replace(/(\d) (\d)/g, '$1 $2');
const sscT = (en, ko) => sscSx(LANG === 'ko' ? sscNbKo(ko) : sscNbEn(en));

function sscLbPages(scr = false) {
  const ch = 'scales';
  const live = (still, comp) => <LbLive still={still} live={<>{still}{comp}</>}/>;
  const stack = (nodes, h, gap = 12, mw = 600) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap,width:'100%',maxWidth:mw,margin:'0 auto'}}>{nodes}</div></LbPic>;
  const X = sscT;
  const F = SCALES.C.octaves[1], FF = SCALES.F.octaves[1];   // the one-octave fingerings (G is C's)
  // a staff (gap 44) with the keys under it, each note over its own key (staff 408 units wide, keys 360 from unit 48)
  const staffKeys = (staff, keys, mw) => <div style={{maxWidth:mw,margin:'0 auto',width:'100%',display:'flex',flexDirection:'column',gap:8}}>{staff}<div style={{marginLeft:(48 / 408 * 100) + '%',width:(360 / 408 * 100) + '%'}}>{keys}</div></div>;

  // p1: C major on the staff and on the keys, numbered 1 to 8, each note over its key
  const p1 = stack([staffKeys(
    <SscStaff key="s" start="C" o={{ under: 'nums', tonic: true, gap: 44 }} label={t('C major on the treble staff: C D E F G A B C, one note on each line and space going up, numbered 1 to 8; the two Cs, 1 and 8, in coral.', '높은음자리표 오선의 C장조 음계: C D E F G A B C, 줄과 칸을 하나씩 올라가며 1에서 8까지 번호; 두 C, 1과 8은 산호색.')}/>,
    <SscKeys key="k" start="C" o={{ nums: true }} label={t('The same eight notes on the keys, C to C, numbered 1 to 8, each under its note.', '같은 여덟 음을 건반에서: C에서 C까지, 1에서 8까지 번호, 음마다 그 아래에.')}/>, 470)], 230, 10);
  // p2: the steps of C major
  const p2 = stack([<div key="k" style={{maxWidth:600,margin:'0 auto',width:'100%'}}><SscKeys start="C" o={{ nums: true, steps: true, H: 185 }} label={t('C major on the keys, numbered 1 to 8. Under the keys, every step from one note to the next: whole, whole, half, whole, whole, whole, half. The two half steps, E F (3 to 4) and B C (7 to 8), in coral.', 'C장조 음계를 건반에서, 1에서 8까지 번호. 건반 아래에 한 음에서 다음 음까지의 걸음: 온, 온, 반, 온, 온, 온, 반. 반 걸음 둘, E F(3과 4 사이)와 B C(7과 8 사이)는 산호색.')}/></div>], 300);
  // p3: the fingering of C major, each hand going up
  const p3 = <LbPic h={300}><div style={{display:'flex',flexDirection:'column',gap:14,width:'100%',maxWidth:380,margin:'0 auto'}}>
    <div key="r" style={{width:'100%'}}><SscKeys start="C" o={{ H: 112, fingers: F.RH, hand: t('RIGHT HAND', '오른손'), arrow: { from: 2, to: 3, label: t('thumb under', '엄지 밑으로 넣기'), over: false } }} label={t('Right hand, C major going up: fingers 1 2 3 1 2 3 4 5 over the keys; under the keys an arrow from E to F: after finger 3 on E, the thumb goes under to F.', '오른손, C장조 음계 올라가기: 건반 위에 손가락 1 2 3 1 2 3 4 5; 건반 아래 E에서 F로 화살표: E를 3번으로 친 다음, 엄지를 밑으로 넣어 F를 쳐요.')}/></div>
    <div key="l" style={{width:'100%'}}><SscKeys start="C" o={{ H: 112, fingers: F.LH, hand: t('LEFT HAND', '왼손'), arrow: { from: 4, to: 5, label: t('3 over', '3번 넘기기'), over: true } }} label={t('Left hand, C major going up: fingers 5 4 3 2 1 3 2 1 over the keys; over them an arrow from G to A: after the thumb on G, finger 3 crosses over to A.', '왼손, C장조 음계 올라가기: 건반 위에 손가락 5 4 3 2 1 3 2 1; 그 위에 G에서 A로 화살표: G를 엄지로 친 다음, 3번이 넘어가 A를 쳐요.')}/></div>
  </div></LbPic>;
  // p4: the degrees: C major numbered, the tonic named under both ends; in print, the keys under it too (on screen the pad has them)
  const p4staff = <SscStaff key="s" start="C" o={{ under: 'nums', tonic: true, tonicLabel: t('tonic', '으뜸음'), gap: 44 }}
    label={t('C major on the staff, each note numbered under it, 1 to 8. Under the two Cs, 1 and 8, the word tonic.', '오선의 C장조 음계, 음마다 아래에 번호 1에서 8. 두 C, 1과 8 아래에 으뜸음.')}/>;
  const p4 = stack([scr ? <div key="s" style={{maxWidth:520,margin:'0 auto',width:'100%'}}>{p4staff}</div>
    : <React.Fragment key="s">{staffKeys(p4staff, <SscKeys start="C" o={{ nums: true }} label={t('The same notes on the keys, numbered 1 to 8.', '같은 음을 건반에서, 1에서 8까지 번호.')}/>, 560)}</React.Fragment>], 260, 6);
  // p5: G major: F sharp makes 6 to 7 whole and 7 to 8 half
  const p5 = stack([
    <div key="k" style={{maxWidth:520,margin:'0 auto',width:'100%'}}><SscKeys start="G" o={{ nums: true, steps: true, coral: [6] }} label={t('G major on the keys, G to G, numbered 1 to 8, with the steps under them: whole, whole, half, whole, whole, whole, half. Degree 7 is the black key F sharp, in coral: E to F sharp a whole step, F sharp to G a half step.', 'G장조 음계를 건반에서, G에서 G까지, 1에서 8까지 번호, 아래에 걸음: 온, 온, 반, 온, 온, 온, 반. 7번 음은 검은건반 F♯, 산호색: E에서 F♯는 온 걸음, F♯에서 G는 반 걸음.')}/></div>,
    <div key="s" style={{maxWidth:470,margin:'0 auto',width:'100%'}}><SscStaff start="G" o={{ under: 'names', tonic: true }} label={t('G major on the treble staff: G A B C D E F sharp G, the sharp sign before F on the top line.', '높은음자리표 오선의 G장조 음계: G A B C D E F♯ G, 맨 윗줄의 F 앞에 샤프.')}/></div>,
  ], 340, 6);
  // p6: F major: B flat makes 3 to 4 half; the right hand's own fingering (fingers only: no degree numbers to mix them up)
  const p6 = stack([
    <div key="k" style={{maxWidth:470,margin:'0 auto',width:'100%'}}><SscKeys start="F" o={{ steps: true, coral: [3], fingers: FF.RH, hand: t('RIGHT HAND', '오른손') }} label={t('F major on the keys, F to F, the right hand fingers over them, 1 2 3 4 1 2 3 4, and the steps under them. The black key B flat, in coral: A to B flat a half step.', 'F장조 음계를 건반에서, F에서 F까지, 위에 오른손 손가락 1 2 3 4 1 2 3 4, 아래에 걸음. 검은건반 B♭은 산호색: A에서 B♭은 반 걸음.')}/></div>,
    <div key="s" style={{maxWidth:430,margin:'0 auto',width:'100%'}}><SscStaff start="F" o={{ under: 'names', tonic: true }} label={t('F major on the treble staff: F G A B flat C D E F, the flat sign before B on the middle line.', '높은음자리표 오선의 F장조 음계: F G A B♭ C D E F, 가운데 줄의 B 앞에 플랫.')}/></div>,
  ], 360, 6);

  // the check icons
  const ic = {
    steps: [{ k: 'raw', svg: [0, 1, 2, 3].map(i => { const x = 6 + i * 21, c = i === 2 ? PEN_C : PEN_N; return '<path d="M' + x + ' 18 L' + x + ' 24 L' + (x + 17) + ' 24 L' + (x + 17) + ' 18" fill="none" stroke="' + c + '" stroke-width="' + (i === 2 ? 2.8 : 2) + '" stroke-linejoin="round"/>'; }).join('') }],
    finger: [{ k: 'raw', svg: [1, 2, 3, 1].map((f, i) => '<circle cx="' + (13 + i * 22) + '" cy="20" r="8.5" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.5"/><text x="' + (13 + i * 22) + '" y="24.5" text-anchor="middle" font-family="Inter, sans-serif" font-size="12.5" font-weight="900" fill="' + (i === 3 ? PEN_C : PEN_N) + '">' + f + '</text>').join('') }],
    deg: [{ k: 'raw', svg: [1, 2, 3, 8].map((f, i) => '<text x="' + (14 + i * 21) + '" y="27" text-anchor="middle" font-family="Inter, sans-serif" font-size="17" font-weight="900" fill="' + (f === 1 || f === 8 ? PEN_C : PEN_N) + '">' + (i === 3 ? '…8' : f) + '</text>').join('') }],
    g: [{ k: 'raw', svg: '<text x="46" y="29" text-anchor="middle" font-family="Inter, sans-serif" font-size="20" font-weight="900" fill="' + PEN_N + '">G <tspan fill="' + PEN_C + '">F<tspan font-family="' + MUSIC_FONT.replace(/"/g, "'") + '" font-weight="400" font-size="26">♯</tspan></tspan></text>' }],
    f: [{ k: 'raw', svg: '<text x="46" y="29" text-anchor="middle" font-family="Inter, sans-serif" font-size="20" font-weight="900" fill="' + PEN_N + '">F <tspan fill="' + PEN_C + '">B<tspan font-family="' + MUSIC_FONT.replace(/"/g, "'") + '" font-weight="400" font-size="24" dx="-2">♭</tspan></tspan></text>' }],
  };
  const checksRows = [
    ['steps', t('I can say the major scale’s steps: whole, whole, half, whole, whole, whole, half', '장음계의 걸음을 말할 수 있어요: 온, 온, 반, 온, 온, 온, 반')],
    ['finger', t('I can play C major with each hand, with its fingering', 'C장조 음계를 한 손씩 정해진 손가락 번호로 칠 수 있어요')],
    ['deg', t('I can number a scale’s notes 1 to 8 and find the tonic', '음계의 음에 1에서 8까지 번호를 붙이고 으뜸음을 찾을 수 있어요')],
    ['g', t('I can play G major with its F sharp', 'G장조 음계를 F♯를 넣어 칠 수 있어요')],
    ['f', t('I can play F major with its B flat and its right-hand fingering', 'F장조 음계를 B♭을 넣어 오른손 손가락 번호대로 칠 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? sscNbKo(x) : sscNbEn(x)]);

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <>한 음에서 한 옥타브 위나 아래의 같은 글자 음까지, 한 걸음씩 차례로 가는 음들을 <b>음계</b>라고 해요. 다른 이름은 스케일이에요.</> : <>A <b>scale</b> is notes in order, step by step, up or down, from one note to the same letter an octave away.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('The major scale', '장음계'), 2], [t('C major fingering', 'C장조 손가락 번호'), 3], [t('Scale degrees', '음의 번호'), 4], [t('G major', 'G장조 음계'), 5], [t('F major', 'F장조 음계'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{sscSx(x.replace(/^I can /, ''))}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The major scale', '장음계')}>
      {live(p2, <SscPad page={2}/>)}
      <LbDefs items={[
        [t('major scale', '장음계'), X('Eight notes: seven letters in order, then the first again. They go up whole, whole, half, whole, whole, whole, half. In tones and semitones: T T S T T T S.', '여덟 음: 일곱 글자를 차례로, 그리고 첫 글자를 한 번 더. 온, 온, 반, 온, 온, 온, 반 걸음으로 올라가요. 온음과 반음으로는 온 온 반 온 온 온 반.')],
        [t('C major', 'C장조 음계'), X('The major scale from C: all white keys. Its half steps are E F (3 to 4) and B C (7 to 8).', 'C에서 시작하는 장음계: 모두 흰건반. 반 걸음은 E F(3과 4 사이)와 B C(7과 8 사이)예요.')],
      ]}/>
      <LbPiano steps={[
        X('Play each pair of white keys from C to C and say "whole" or "half": C D, D E, E F, F G, G A, A B, B C.', 'C에서 C까지 흰건반 짝을 하나씩 치며 "온" 또는 "반"이라고 말해요: C D, D E, E F, F G, G A, A B, B C.'),
        X('Find the two half steps of C major, E F and B C, in every octave of the piano, and play them.', '피아노의 모든 옥타브에서 C장조 음계의 반 걸음 둘, E F와 B C를 찾아 쳐요.'),
      ]}/>
      <LbRemember>{X('A major scale: whole, whole, half, whole, whole, whole, half.', '장음계: 온, 온, 반, 온, 온, 온, 반.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('C major fingering', 'C장조 손가락 번호')}>
      {live(p3, <SscPad page={3}/>)}
      <LbDefs items={[
        [t('fingering', '음계의 손가락 번호'), X('The finger for each note of a scale.', '음계의 음마다 정해진 손가락. 다른 이름은 운지예요.')],
        [t('thumb under', '엄지 밑으로 넣기'), X('Right hand going up: after finger 3 on E, the thumb passes under the hand to F. Coming down, finger 3 crosses over the thumb.', '오른손으로 올라갈 때: E를 3번으로 친 다음, 엄지를 손 밑으로 넣어 F를 쳐요. 내려올 때는 3번이 엄지 위로 넘어가요.')],
        [t('3 over', '3번 넘기기'), X('Left hand going up: after the thumb on G, finger 3 crosses over the thumb to A. Coming down, the thumb passes under.', '왼손으로 올라갈 때: G를 엄지로 친 다음, 3번이 엄지 위로 넘어가 A를 쳐요. 내려올 때는 엄지가 손 밑으로 들어가요.')],
      ]}/>
      <LbPiano steps={[
        X('Right hand: C major up and down. Up: 1 2 3, thumb under, 1 2 3 4 5. Down: 5 4 3 2 1, 3 over, 3 2 1. Slowly, four times.', '오른손: C장조 음계를 올라갔다 내려와요. 올라갈 때 1 2 3, 엄지 밑으로 넣기, 1 2 3 4 5. 내려올 때 5 4 3 2 1, 3번 넘기기, 3 2 1. 천천히 네 번.'),
        X('Left hand: C major up and down. Up: 5 4 3 2 1, 3 over, 3 2 1. Down: 1 2 3, thumb under, 1 2 3 4 5. Slowly, four times.', '왼손: C장조 음계를 올라갔다 내려와요. 올라갈 때 5 4 3 2 1, 3번 넘기기, 3 2 1. 내려올 때 1 2 3, 엄지 밑으로 넣기, 1 2 3 4 5. 천천히 네 번.'),
      ]}/>
      <LbRemember>{X('Going up: the right hand’s thumb under after 3; the left hand’s 3 over after the thumb.', '올라갈 때: 오른손은 3번 다음 엄지 밑으로 넣기, 왼손은 엄지 다음 3번 넘기기.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Scale degrees', '음의 번호')}>
      {live(p4, <SscPad page={4}/>)}
      <LbDefs items={[
        [t('degree', '음의 번호'), X('A note’s number in its scale: 1 to 8, from the bottom. 8 is 1 again, an octave higher.', '음계의 음마다 붙는 번호: 아래에서부터 1에서 8까지. 8은 한 옥타브 위의 1이에요. 다른 이름은 음도예요.')],
        [t('tonic', '으뜸음'), X('Degree 1: the scale’s home note. The tonic of C major is C.', '1번 음: 음계의 집 같은 음. C장조의 으뜸음은 C예요.')],
      ]}/>
      <LbPiano steps={[
        X('Right hand: play C major, saying the numbers: 1 to 8 going up, 8 to 1 coming down.', '오른손: C장조 음계를 치며 번호를 말해요: 올라갈 때 1에서 8, 내려올 때 8에서 1.'),
        X('Right hand: play 1 3 5 8, then 8 5 3 1, saying the numbers. It ends on the tonic.', '오른손: 번호를 말하며 1 3 5 8, 그다음 8 5 3 1을 쳐요. 으뜸음에서 끝나요.'),
      ]}/>
      <LbRemember>{X('Degrees 1 to 8. Degree 1, the tonic, is home.', '음의 번호는 1부터 8까지. 1번 음인 으뜸음이 집이에요.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('G major', 'G장조 음계')}>
      {live(p5, <SscPad page={5}/>)}
      <LbDefs items={[
        [t('G major', 'G장조 음계'), X('The major scale from G: G A B C D E F♯ G. One sharp: F♯.', 'G에서 시작하는 장음계: G A B C D E F♯ G. 샤프 하나, F♯.')],
        [sscSx(t('F♯ in G major', 'G장조의 F♯')), X('From E, a whole step up is F♯; from F♯, a half step up is G. So 6 to 7 is whole and 7 to 8 is half, as the major scale asks.', 'E에서 위로 온 걸음은 F♯. F♯에서 위로 반 걸음은 G. 그래서 6과 7 사이는 온, 7과 8 사이는 반이에요.')],
        [t('each letter once', '글자는 한 번씩'), X('A major scale uses every letter once, in order. So G major has F♯, never G♭.', '장음계는 모든 글자를 차례로 한 번씩 써요. 그래서 G장조에는 G♭이 아니라 F♯가 있어요.')],
      ]}/>
      <LbPiano steps={[
        X('Right hand, with C major’s fingers: up 1 2 3, thumb under, 1 2 3 4 5; down 5 4 3 2 1, 3 over, 3 2 1. Finger 4 plays F♯. Slowly, four times.', '오른손, C장조와 같은 손가락으로: 올라갈 때 1 2 3, 엄지 밑으로 넣기, 1 2 3 4 5. 내려올 때 5 4 3 2 1, 3번 넘기기, 3 2 1. 4번이 F♯를 쳐요. 천천히 네 번.'),
        X('Left hand: up 5 4 3 2 1, 3 over, 3 2 1; down 1 2 3, thumb under, 1 2 3 4 5. Finger 2 plays F♯. Slowly, four times.', '왼손: 올라갈 때 5 4 3 2 1, 3번 넘기기, 3 2 1. 내려올 때 1 2 3, 엄지 밑으로 넣기, 1 2 3 4 5. 2번이 F♯를 쳐요. 천천히 네 번.'),
      ]}/>
      <LbRemember>{X('G major: one sharp, F♯.', 'G장조 음계: 샤프 하나, F♯.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('F major', 'F장조 음계')}>
      {live(p6, <SscPad page={6}/>)}
      <LbDefs items={[
        [t('F major', 'F장조 음계'), X('The major scale from F: F G A B♭ C D E F. One flat: B♭, never A♯. From A, a half step up is B♭: 3 to 4 is half.', 'F에서 시작하는 장음계: F G A B♭ C D E F. 플랫 하나, B♭(A♯가 아니에요). A에서 위로 반 걸음은 B♭: 3과 4 사이는 반.')],
        [t('F major’s right hand', 'F장조 오른손'), X('Up: 1 2 3 4, thumb under to C, 1 2 3 4. Down: 4 crosses over the thumb to B♭ (4 over).', '올라갈 때: 1 2 3 4, 엄지 밑으로 넣어 C, 1 2 3 4. 내려올 때: 4번이 엄지 위로 넘어가 B♭을 쳐요(4번 넘기기).')],
      ]}/>
      <LbPiano steps={[
        X('Right hand: F major up and down. Up: 1 2 3 4, thumb under, 1 2 3 4. Down: 4 3 2 1, 4 over, 3 2 1. Slowly, four times.', '오른손: F장조 음계를 올라갔다 내려와요. 올라갈 때 1 2 3 4, 엄지 밑으로 넣기, 1 2 3 4. 내려올 때 4 3 2 1, 4번 넘기기, 3 2 1. 천천히 네 번.'),
        X('Left hand, with C major’s fingers: up 5 4 3 2 1, 3 over, 3 2 1; down 1 2 3, thumb under, 1 2 3 4 5. Slowly, four times.', '왼손, C장조와 같은 손가락으로: 올라갈 때 5 4 3 2 1, 3번 넘기기, 3 2 1. 내려올 때 1 2 3, 엄지 밑으로 넣기, 1 2 3 4 5. 천천히 네 번.'),
      ]}/>
      <LbRemember>{X('F major: one flat, B♭. Right hand 1 2 3 4, 1 2 3 4.', 'F장조 음계: 플랫 하나, B♭. 오른손 1 2 3 4, 1 2 3 4.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, sscSx(x)])}/>} live={<FiveChecks376 storeKey="pb_five_ssc_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, sscSx(x)])}/>}/>
    </LbPage>,
  ];
}
function ScalesLessonBook() { return <>{sscLbPages(false)}</>; }
