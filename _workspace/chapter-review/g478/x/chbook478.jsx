// ─── Phase 478: chapter 22, Chords, built in full (Book rules 14 and 15; her 2026-10-17 02:05 macro-first plan: the
// whole first, then the parts, then the whole again). The fourth room of Level 4. Page 1 is the chord clock: every major
// triad is one shape, 4 half steps then 3, turned to start on any of the twelve keys (chapter 16's keyboard clock); the
// steps zoom in (stack a triad, major and minor, the tonic triad, I IV V, both hands); the screen lesson ends with I, IV
// and V in the student's keys (Phase 476's [keys:...]).
// Placement (AMEB Music Craft 2022: Preliminary the root-position tonic triad of C, G and F major, treble; Grade 1 I and
// V in root position, treble and bass, keys C G D F B♭ major; Grade 2 I ii IV V, root and 1st inversion, aural major and
// minor triads. ABRSM Theory: Grade 1 tonic triads of C, G, D and F major; Grade 4 IV and V). Not here: inversions,
// cadences, minor keys' chords, 7ths (the toolbox).
// A note is { d, acc } (chapter 6's staff number, middle C 28); chapter 21's IVX_N, ivxScale, IVX_TONIC_D, ivxNoteTxt are
// reused, and the old chapter's playChord sound.

const CHX_L = 'CDEFGAB', CHX_PC = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };
const chxAcc = (nm) => nm.length > 1 ? (nm[1] === '#' ? 1 : -1) : 0;
// a triad's letter names from its root ('C', 'F#', 'Bb'): major 4 + 3 half steps, minor 3 + 4. For the roots of KEY12 (major) and
// CHX_MIN12 (minor) only: it writes no double sharps or flats
function chxSpell(root, q = 'major') {
  const L = CHX_L.indexOf(root[0]), pc0 = (CHX_PC[root[0]] + chxAcc(root) + 12) % 12;
  return [0, 2, 4].map((st, j) => { const l = CHX_L[(L + st) % 7], want = (pc0 + [0, q === 'minor' ? 3 : 4, 7][j]) % 12, a = ((want - CHX_PC[l] + 18) % 12) - 6;
    return l + (a > 0 ? '#' : a < 0 ? 'b' : ''); });
}
// the root's place on the staff: treble from middle C up to B; bass an octave lower
const CHX_D = { C: 28, D: 29, E: 30, F: 31, G: 32, A: 33, B: 34 };
// (bass: C to F an octave lower, G to B two, so the triad sits on the staff)
const chxNotes = (root, q = 'major', clef = 'treble') => { const d0 = CHX_D[root[0]] - (clef === 'bass' ? (CHX_D[root[0]] >= 32 ? 14 : 7) : 0); return chxSpell(root, q).map((nm, j) => IVX_N(d0 + j * 2, chxAcc(nm))); };
const chxTxt = (names) => names.map(prettyNote).join(' ');
const chxNotesTxt = (notes) => notes.map(ivxNoteTxt).join(' ');
const chxQ = (q) => LANG === 'ko' ? (q === 'minor' ? '단3화음' : '장3화음') : q;
const chxName = (root, q = 'major') => LANG === 'ko' ? prettyNote(root) + ' ' + chxQ(q) : prettyNote(root) + ' ' + q;
// a key's scale over an octave and a half (I, IV and V fit): chapter 21's tonic places
function chxScale(k) {
  const names = spellScale(k), d0 = IVX_TONIC_D[k] != null ? IVX_TONIC_D[k] : 28;
  return Array.from({ length: 12 }, (_, i) => IVX_N(d0 + i, chxAcc(names[i % 7])));
}
// (a triad whose top note would sit above the first ledger line, B♭ and B major's V say, goes down an octave)
const chxDeg = (k, deg) => { const sc = chxScale(k), tr = [sc[deg - 1], sc[deg + 1], sc[deg + 3]]; return tr[2].d >= 41 ? tr.map(n => IVX_N(n.d - 7, n.acc)) : tr; };
const CHX_ROM = { 1: 'I', 4: 'IV', 5: 'V' };
const chxRomKo = (deg) => ({ 1: '으뜸화음', 4: '버금딸림화음', 5: '딸림화음' })[deg];
// the twelve roots: major as the keys are named (chapter 16), minor with the usual sharps
const CHX_MIN12 = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'G#', 'A', 'Bb', 'B'];
const chxRoot12 = (i, q) => (q === 'minor' ? CHX_MIN12 : KEY12)[((i % 12) + 12) % 12];
// Korean: words that belong together never part at a line end
const chxNbKo = (x) => typeof x !== 'string' ? x : ivxNbKo(x).replace(/반 걸음 (\d+)개/g, '반 걸음 $1개').replace(/반 걸음/g, '반 걸음').replace(/(근음|3음|5음)과 /g, '$1과 ')
  .replace(/([A-G][♯♭]?) (장3화음|단3화음|3화음|장조)/g, '$1 $2').replace(/하나 건너/g, '하나 건너').replace(/(\d)번 음/g, '$1번 음').replace(/음 위의/g, '음 위의')
  .replace(/(\d), (?=\d)/g, '$1, ').replace(/(\d번), (?=\d번)/g, '$1, ').replace(/I, IV, V(?![A-Za-z])/g, 'I, IV, V').replace(/([A-G][♯♭]?), (?=[A-G])/g, '$1, ').replace(/(\d) \+ (\d)/g, '$1 + $2');
const chxKoT = (x) => LANG === 'ko' ? chxNbKo(x) : x;

// a staff with chords. places: [{ notes: [{ d, acc }] low to high, broken (one after the other, left to right), lab, lab2,
// hl: [note indices in coral], side: [a word right of each note, e.g. root 3rd 5th], blank }]. o.key: a key signature (a
// note the key already alters has no sign); o.bars; o.x0; o.labSize; o.padTop; o.gap (broken: the space between notes).
// A block chord's signs: the top one nearest, a lower one a column further left when they would touch
function ChxStaff({ clef = 'treble', places, width = 320, o = {}, label }) {
  const ks = o.key ? skgKs(o.key, clef) : [], kmap = o.key ? skgMap(o.key) : {};
  const ksx = clef === 'bass' ? 56 : 48, x0 = (o.x0 || 56) + (ks.length ? ks.length * 12 + 6 + (clef === 'bass' ? 8 : 0) : 0), slot = (width - x0 - 6) / Math.max(1, places.length);
  const notes = [], accs = [], labs = [], sides = [];
  const low = CLEFS[clef].low, hi = CLEFS[clef].high;
  const signOf = (n) => { const k = kmap[dName(n.d)] || 0; return (n.acc || 0) === k ? null : (n.acc > 0 ? '#' : n.acc < 0 ? 'b' : 'n'); };
  places.forEach((p, i) => {
    if (!p) return;
    if (p.blank) { if (p.lab) labs.push([x0 + slot * (i + 0.5), p.lab, p.lab2, p.labCol]); return; }
    const cx = x0 + slot * (i + 0.5), n = p.notes.length, hl = p.hl || [], g = Math.max(Math.min(o.gap || 30, slot * 0.3), p.broken && p.notes.some(nt => signOf(nt)) ? 30 : 0);
    const xs = p.notes.map((_, j) => p.broken ? cx + (j - (n - 1) / 2) * g : cx), col = (j) => hl.includes(j) ? PEN_C : BK.ink;
    p.notes.forEach((nt, j) => notes.push({ d: nt.d, x: xs[j], color: col(j) }));
    if (p.broken) p.notes.forEach((nt, j) => { const s = signOf(nt); if (s) accs.push([s, xs[j] - 17, nt.d, col(j)]); });
    else { const used = []; p.notes.map((nt, j) => [nt, j]).sort((a, b) => b[0].d - a[0].d).forEach(([nt, j]) => { const s = signOf(nt); if (!s) return;
      let c = 0; while (used.some(([cc, dd]) => cc === c && Math.abs(dd - nt.d) < 6)) c++; used.push([c, nt.d]); accs.push([s, cx - 17 - c * 11, nt.d, col(j)]); }); }
    if (p.side) p.notes.forEach((nt, j) => { if (p.side[j]) sides.push([xs[j] + 14, nt.d, p.side[j], hl.includes(j), p.broken || p.side.every(w => String(w).length < 2) ? 0 : j - (n - 1) / 2]); });   // a block chord's words fan out, 16 apart (single figures stay on their notes)
    if (p.lab) labs.push([cx, p.lab, p.lab2, p.labCol]);
  });
  const ysN = notes.map(n => dY(n.d)), yLab = o.labY != null ? o.labY : Math.max(dY(low) + 30, ...ysN.map(y => y + 24), ...sides.map(([, d, , , off]) => dY(d) + 4 - off * 6 + 18)) + (o.labDy || 0);
  const bottomNeed = labs.length ? yLab + (labs.some(l => l[2]) ? ((o.labSize || 13) > 13 ? (o.labSize || 13) + 8 : 18) : 6) : Math.max(dY(low), ...ysN) + 14;
  const pad = [o.padTop != null ? o.padTop : 18, bottomNeed - Math.max(dY(low), ...ysN)];
  const ls = o.labSize || 13;
  return <SfStaff clef={clef} width={width} notes={notes} pad={pad} label={label} extra={(yOf, layer, txt) => layer !== 'over' ? null : <g>
    {ks.map(([sg, d], i) => <g key={'k' + i}>{tnAcc(sg, ksx + i * 12, yOf(d), BK.ink)}</g>)}
    {o.arrow && <text x={x0 + slot} y={yOf(clef === 'bass' ? 22 : 34) + 6} textAnchor="middle" fontSize="18" fontWeight="900" fill={BK.muted} style={txt}>→</text>}
    {o.bars && places.slice(1).map((_, i) => <line key={'b' + i} x1={x0 + slot * (i + 1)} x2={x0 + slot * (i + 1)} y1={yOf(hi)} y2={yOf(low)} stroke={BK.ink} strokeWidth="1.2"/>)}
    {accs.map(([sg, x, d, c], i) => <g key={'a' + i}>{tnAcc(sg, x, yOf(d), c)}</g>)}
    {sides.map(([x, d, w, on, off], i) => <text key={'s' + i} x={x} y={yOf(d) + 4 - off * 6} fontSize={o.sideSize || 11.5} fontWeight="900" fill={on ? PEN_C : BK.muted} style={txt}>{w}</text>)}
    {labs.map(([x, a, b, c], i) => <text key={'t' + i} x={x} y={yLab} textAnchor="middle" fontSize={ls} fontWeight="900" fill={c || BK.ink} style={{fontFamily:'Inter, sans-serif'}}>{b ? <><tspan x={x} dy="0" fontSize={ls * 0.82} fontWeight="800" fill={BK.muted}>{a}</tspan><tspan x={x} dy={ls + 2}>{b}</tspan></> : a}</text>)}
  </g>}/>;
}

// a keyboard (chapter 17's SacKeys, drawn again) with a small number in a key: o.nums { midi: '1' } (the half steps
// counted); o.lit (coral), o.pale, o.H; onTap(midi)
function ChxKeys({ d0 = 28, n = 8, o = {}, onTap, label }) {
  const W = 40, H = o.H || 120, BW = 25, BH = Math.round(H * 0.6), x0 = 3, keys = [];
  for (let i = 0; i < n; i++) { const d = d0 + i, m = ivMidi({ d }); keys.push({ i, d, m, white: true, L: dName(d) }); if ('CDFGA'.includes(dName(d)) && i < n - 1) keys.push({ i, d, m: m + 1, white: false }); }
  const lit = new Set(o.lit || []), pale = new Set(o.pale || []), nums = o.nums || {};
  const cx = (k) => k.white ? x0 + (k.i + 0.5) * W : x0 + (k.i + 1) * W;
  const tap = (k) => onTap ? () => onTap(k.m) : undefined;
  const num = (k, y, fill) => nums[k.m] != null && <text x={cx(k)} y={y} textAnchor="middle" fontSize="13" fontWeight="900" fill={fill} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{nums[k.m]}</text>;
  return (
    <svg viewBox={`0 0 ${x0 * 2 + n * W} ${H + 6}`} role="img" aria-label={label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>
      {keys.filter(k => k.white).map(k => <g key={'w' + k.i} onClick={tap(k)} style={{cursor:onTap ? 'pointer' : 'default'}} data-chx={k.m}>
        <rect x={x0 + k.i * W} y={3} width={W} height={H} rx="3" fill={lit.has(k.m) ? PEN_C : pale.has(k.m) ? '#fbd9cc' : '#fff'} stroke={PEN_N} strokeWidth="1.6"/>
        {num(k, Math.min(BH + 15, H - 27), lit.has(k.m) ? '#fff' : pale.has(k.m) ? PEN_N : PEN_C)}
        <text x={cx(k)} y={H - 8} textAnchor="middle" fontSize="15" fontWeight="900" fill={lit.has(k.m) ? '#fff' : PEN_N} style={{pointerEvents:'none'}}>{k.L}</text>
      </g>)}
      {keys.filter(k => !k.white).map(k => <g key={'b' + k.i} onClick={tap(k)} style={{cursor:onTap ? 'pointer' : 'default'}} data-chx={k.m}>
        <rect x={cx(k) - BW / 2} y={3} width={BW} height={BH} rx="2" fill={lit.has(k.m) ? PEN_C : pale.has(k.m) ? '#f08c70' : PEN_N} stroke={lit.has(k.m) ? '#fff' : PEN_N} strokeWidth={lit.has(k.m) ? 2.2 : 1.4}/>
        {num(k, BH - 9, pale.has(k.m) && !lit.has(k.m) ? PEN_N : '#fff')}
      </g>)}
    </svg>
  );
}
// the keys under a chord: from the root's white key, wide enough for the 5th
const chxKeyRange = (notes) => { const a = notes[0], b = notes[notes.length - 1], d0 = a.d - (a.acc < 0 ? 1 : 0), d1 = b.d + (b.acc > 0 ? 1 : 0); return [d0, Math.max(5, d1 - d0 + 1)]; };
// the half steps counted, root to 3rd (1 to 4 or 3), then 3rd to 5th
const chxCount = (notes) => { const m = notes.map(ivMidi), out = {}; for (let x = m[0] + 1; x <= m[1]; x++) out[x] = String(x - m[0]); for (let x = m[1] + 1; x <= m[2]; x++) out[x] = String(x - m[1]); return out; };

// the chord clock: chapter 16's twelve keys round a circle, C at the top, a half step a step; the triad one shape (a
// triangle: root, 3rd, 5th; the root coral) on any key; minor moves the 3rd in a half step. at: the root (0 to 11);
// the half steps written on two sides (4 and 3, or 3 and 4). o.ghost: the same triangle turned two keys on, dashed, with an
// arrow (print: the shape turns)
function ChxRing({ at = 0, q = 'major', onPick, o = {}, label }) {
  const C = 180, R1 = 160, R0 = 106, RP = 86, black = [1, 3, 6, 8, 10], idx = ((at % 12) + 12) % 12;
  const pt = (a, r) => [C + r * Math.cos(a * Math.PI / 180), C + r * Math.sin(a * Math.PI / 180)];
  const arcPath = (i, ra, rb) => { const a0 = -105 + i * 30, a1 = a0 + 30, [x0, y0] = pt(a0, ra), [x1, y1] = pt(a0, rb), [x2, y2] = pt(a1, rb), [x3, y3] = pt(a1, ra);
    return `M${x0} ${y0} L${x1} ${y1} A${rb} ${rb} 0 0 1 ${x2} ${y2} L${x3} ${y3} A${ra} ${ra} 0 0 0 ${x0} ${y0} Z`; };
  const set = [0, q === 'minor' ? 3 : 4, 7], on = set.map(s => (idx + s) % 12), shape = set.map(s => pt(-90 + (idx + s) * 30, RP));
  const names = chxSpell(chxRoot12(idx, q), q);
  const two = (x, y, a, b, fill) => <text x={x} y={y} textAnchor="middle" fontSize="16" fontWeight="900" fill={fill} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}><tspan x={x} dy="-3">{a}</tspan><tspan x={x} dy="16.5">{b}</tspan></text>;
  const one = (x, y, a, fill) => <text x={x} y={y + 6} textAnchor="middle" fontSize="18" fontWeight="900" fill={fill} style={{fontFamily:"'Playfair Display', Georgia, serif",pointerEvents:'none'}}>{pbAccT(a)}</text>;
  const mid = (a, b, f = 0.78) => [C + ((a[0] + b[0]) / 2 - C) * f, C + ((a[1] + b[1]) / 2 - C) * f];
  const halo = { fontFamily: 'Inter, sans-serif', paintOrder: 'stroke', stroke: '#fff', strokeWidth: 4, strokeLinejoin: 'round' };
  return (
    <svg viewBox="0 0 360 360" role="img" aria-label={label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>
      {KEY12.map((k, i) => { const b = black.includes(i), j = on.indexOf(i), lit = j >= 0;
        const fill = lit ? (j === 0 ? PEN_C : '#fbd9cc') : b ? PEN_N : '#fff', ink = lit ? (j === 0 ? '#fff' : PEN_N) : b ? '#fff' : PEN_N;
        const [lx, ly] = pt(-90 + i * 30, 133);
        const lab = lit ? one(lx, ly, prettyNote(names[j]), ink) : b ? two(lx, ly, prettyNote(KEY_ALIAS_BACK[k]), prettyNote(k), ink) : one(lx, ly, k, ink);
        return <g key={k} data-key={k} onClick={onPick ? () => onPick(i) : undefined} style={{cursor:onPick ? 'pointer' : 'default'}}>
          {onPick && <path d={arcPath(i, 96, 176)} fill="transparent"/>}
          <path d={arcPath(i, R0, R1)} fill={fill} stroke={PEN_N} strokeWidth="1.4" strokeLinejoin="round"/>
          {lab}
        </g>; })}
      {o.ghost && (() => { const gs = set.map(sv => pt(-90 + (idx + 2 + sv) * 30, RP)), a0 = -90 + idx * 30 + 6, a1 = a0 + 54, [ax, ay] = pt(a0, 171), [bx, by] = pt(a1, 171);
        const r = a1 * Math.PI / 180, dx = -Math.sin(r), dy = Math.cos(r), nx = Math.cos(r), ny = Math.sin(r);   // the arc's way at its end, and across it
        const head = [[bx + dx * 2, by + dy * 2], [bx - dx * 8 + nx * 5, by - dy * 8 + ny * 5], [bx - dx * 8 - nx * 5, by - dy * 8 - ny * 5]];
        return <g style={{pointerEvents:'none'}}><polygon points={gs.map(q2 => q2.join(',')).join(' ')} fill="none" stroke={PEN_N} strokeWidth="1.6" strokeDasharray="5 4" opacity="0.6" strokeLinejoin="round"/>
          <circle cx={gs[0][0]} cy={gs[0][1]} r="6" fill="#fff" stroke={PEN_N} strokeWidth="1.6"/>
          <path d={`M${ax} ${ay} A171 171 0 0 1 ${bx} ${by}`} fill="none" stroke={PEN_N} strokeWidth="1.8" strokeLinecap="round"/>
          <polygon points={head.map(q2 => q2.join(',')).join(' ')} fill={PEN_N}/></g>; })()}
      <g style={{pointerEvents:'none'}}>
        <polygon points={shape.map(p => p.join(',')).join(' ')} fill="rgba(38,41,107,0.05)" stroke={PEN_N} strokeWidth="2.4" strokeLinejoin="round"/>
        {[[0, 1, set[1]], [1, 2, 7 - set[1]]].map(([a, b, n]) => { const [x, y] = mid(shape[a], shape[b]); return <text key={a} x={x} y={y + 7} textAnchor="middle" fontSize="20" fontWeight="900" fill={PEN_C} style={halo}>{n}</text>; })}
        {shape.map((p, j) => <circle key={j} cx={p[0]} cy={p[1]} r={j === 0 ? 8 : 5} fill={j === 0 ? PEN_C : PEN_N} stroke="#fff" strokeWidth="2.5"/>)}
      </g>
    </svg>
  );
}

// the pictures' chords (the pads play the same)
const CHX_P2 = ['C', 'F', 'G'].map(r => ({ notes: chxNotes(r), r }));
const chxSide = () => [t('root', '근음'), t('3rd', '3음'), t('5th', '5음')];
const chxOnLines = (notes, clef = 'treble') => (notes[0].d - CLEFS[clef].low) % 2 === 0;
const chxLinesWord = (notes, clef) => chxOnLines(notes, clef) ? t('all lines', '모두 줄') : t('all spaces', '모두 칸');
const CHX_TONIC_KEYS = ['C', 'G', 'D', 'F'];

function chxLbPages(scr = false) {
  const ch = 'chords';
  const live = (still, comp) => <LbLive still={still} live={comp}/>;
  const stack = (nodes, h, gap = 12, mw = 680) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap,width:'100%',maxWidth:mw,margin:'0 auto',alignItems:'stretch'}}>{nodes}</div></LbPic>;
  const X = (en, ko) => sscT(en, skgKo(chxNbKo(ko)));
  const cap = (x, key = 'cap') => <div key={key} style={{textAlign:'center',fontSize:scr ? 14 : 13.5,fontWeight:800,color:BK.ink,margin:'2px auto 0',maxWidth:560,lineHeight:1.35,textWrap:'balance'}}>{sscSx(chxKoT(x))}</div>;
  const staff = (key, mw, node) => <div key={key} style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{node}</div>;
  const row = (key, kids, gap = 18) => <div key={key} style={{display:'flex',gap,justifyContent:'center',alignItems:'center',flexWrap:'wrap'}}>{kids}</div>;
  const C3 = chxNotes('C');

  // p1 (macro first): the chord clock, C major's triangle; beside it the same triad on the staff, root 3rd 5th
  const p1 = <LbLive still={stack([row('r', [
      <div key="ring" style={{width:'100%',maxWidth:scr ? 300 : 290}}><ChxRing at={0} o={{ ghost: !scr }} label={t('The chord clock: the twelve keys round a circle, a half step a step. A triangle joins C, E and G: the C major triad, 4 half steps then 3. A dashed copy of the triangle, turned two keys on, joins D, F sharp and A: the same shape makes the major triad on any key.', '화음 시계: 열두 건반이 원을 따라 반 걸음씩 놓여 있어요. 삼각형이 C, E, G를 이어요: C 장3화음, 반 걸음 4개 다음 3개. 두 건반 돌린 점선 삼각형은 D, F♯, A를 이어요: 같은 모양이 어느 건반에서나 장3화음을 만들어요.')}/></div>,
      <div key="st" style={{width:'100%',maxWidth:scr ? 240 : 300}}><ChxStaff places={[{ notes: C3, side: chxSide(), lab: chxName('C') }]} width={170} o={{ x0: 50, labSize: 14, sideSize: 12.5 }} label={t('The C major triad on the treble staff: C, E and G stacked, the root at the bottom, then the 3rd, then the 5th.', '높은음자리표 오선의 C 장3화음: C, E, G를 쌓아요. 맨 아래가 근음, 그 위에 3음과 5음.')}/></div>], 26),
    cap(t('Every major triad is one shape: 4 half steps, then 3. Turn it to start on any of the twelve keys.', '장3화음은 모두 같은 모양이에요: 반 걸음 4개, 그다음 3개. 돌리면 열두 건반 어디에서나 시작할 수 있어요.'))], 400, 10)} live={<ChxClockPad/>}/>;
  // p2: stack a triad: C E G and G B D on lines, F A C in spaces; the keys of C E G under them
  const p2 = stack([staff('s', scr ? 330 : 440, <ChxStaff places={CHX_P2.map(p => ({ notes: p.notes, lab: chxLinesWord(p.notes), lab2: chxNotesTxt(p.notes) }))} width={scr ? 320 : 300} o={{ labSize: 14, bars: true }} label={t('Three triads on the treble staff: C E G, all on lines; F A C, all in spaces; G B D, all on lines.', '높은음자리표 오선의 3화음 셋: C E G는 모두 줄, F A C는 모두 칸, G B D는 모두 줄.')}/>),
    staff('b', scr ? 330 : 440, <ChxStaff clef="bass" places={['C', 'F', 'G'].map(r => { const nt = chxNotes(r, 'major', 'bass'); return { notes: nt, lab: chxLinesWord(nt, 'bass'), lab2: chxNotesTxt(nt) }; })} width={scr ? 320 : 300} o={{ labSize: 14, bars: true, padTop: 8 }} label={t('The same three on the bass staff: C E G, all in spaces; F A C, all on lines; G B D, all on lines.', '낮은음자리표 오선의 같은 3화음 셋: C E G는 모두 칸, F A C는 모두 줄, G B D는 모두 줄.')}/>),
    <div key="k" style={{maxWidth:340,margin:'0 auto',width:'100%'}}><ChxKeys d0={28} n={8} o={{ H: 96, lit: [60], pale: [64, 67] }} label={t('The keys from C: C, E and G marked. Play one, skip one, play one, skip one, play one.', 'C부터의 건반: C, E, G에 표시. 하나 치고, 하나 건너뛰고, 하나 치고, 하나 건너뛰고, 하나 쳐요.')}/></div>], 380, 10);
  // p3: major and minor: C E G and C E♭ G, the 3rd coral; the half steps counted on two keyboards
  const Cm = chxNotes('C', 'minor');
  const p3 = stack([staff('s', scr ? 330 : 420, <ChxStaff places={[{ notes: C3, hl: [1], lab: t('major', '장3화음'), lab2: 'C E G' }, { notes: Cm, hl: [1], lab: t('minor', '단3화음'), lab2: 'C E♭ G' }]} width={scr ? 300 : 260} o={{ labSize: 14, bars: true }} label={t('C major, C E G, and C minor, C E flat G: only the 3rd moves, down a half step.', 'C 장3화음 C E G와 C 단3화음 C E♭ G: 3음만 반 걸음 내려가요.')}/>),
    row('k', [[C3, t('C major: 4 + 3', 'C 장3화음: 4 + 3')], [Cm, t('C minor: 3 + 4', 'C 단3화음: 3 + 4')]].map(([nt, w], i) => <div key={i} style={{width:'100%',maxWidth:scr ? 200 : 230,display:'flex',flexDirection:'column',gap:4}}>
      <ChxKeys d0={28} n={5} o={{ H: 104, lit: [ivMidi(nt[1])], pale: [ivMidi(nt[0]), ivMidi(nt[2])], nums: chxCount(nt) }} label={t(i ? 'C to E flat: 3 half steps; E flat to G: 4.' : 'C to E: 4 half steps; E to G: 3.', i ? 'C에서 E♭까지 반 걸음 3개, E♭에서 G까지 반 걸음 4개.' : 'C에서 E까지 반 걸음 4개, E에서 G까지 반 걸음 3개.')}/>
      <div style={{textAlign:'center',fontSize:14,fontWeight:900,color:BK.ink}}>{sscSx(chxKoT(w))}</div></div>), 22)], 360, 12);
  // p4: the tonic triad of C, G, D and F major, each with its key signature
  const p4 = stack([<div key="g" style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:scr ? '4px 10px' : '6px 40px',width:'100%',maxWidth:scr ? 340 : 560,margin:'0 auto'}}>{CHX_TONIC_KEYS.map(k => { const nt = chxDeg(k, 1);
    return <div key={k}><ChxStaff places={[{ notes: nt, lab: skgKeyName(k), lab2: chxNotesTxt(nt) }]} width={150} o={{ x0: 46, labSize: 14, key: k, labY: dY(28) + 24 }} label={t(skgKeyName(k) + ', its key signature, and the tonic triad: ' + chxNotesTxt(nt) + '.', skgKeyName(k) + ' 조표와 으뜸화음: ' + chxNotesTxt(nt) + '.')}/></div>; })}</div>,
    cap(t('The 1st, 3rd and 5th notes of the scale. The key signature gives them their sharps and flats.', '음계의 1번, 3번, 5번 음. 샤프와 플랫은 조표가 정해요.'))], scr ? 330 : 360, 8);
  // p5: I, IV and V in C major and in G major (with its key signature): the numerals and the letters
  const p5row = (k, w) => { const pl = [1, 4, 5].map(dg => { const nt = chxDeg(k, dg); return { notes: nt, lab: CHX_ROM[dg], lab2: prettyNote(spellScale(k)[dg - 1]) }; });
    return <ChxStaff places={pl} width={w} o={{ labSize: 15, bars: true, key: k === 'C' ? null : k, x0: k === 'C' ? 74 : 56 }} label={t(skgKeyName(k) + ': I is ' + chxNotesTxt(chxDeg(k, 1)) + ', IV is ' + chxNotesTxt(chxDeg(k, 4)) + ', V is ' + chxNotesTxt(chxDeg(k, 5)) + '.', skgKeyName(k) + ': I은 ' + chxNotesTxt(chxDeg(k, 1)) + ', IV는 ' + chxNotesTxt(chxDeg(k, 4)) + ', V는 ' + chxNotesTxt(chxDeg(k, 5)) + '.')}/>; };
  const p5 = stack([staff('c', scr ? 330 : 470, <>{!scr && <div style={{fontSize:13,fontWeight:900,color:BK.muted,textAlign:'center'}}>{skgKeyName('C')}</div>}{p5row('C', 300)}</>),
    staff('g', scr ? 330 : 470, <>{!scr && <div style={{fontSize:13,fontWeight:900,color:BK.muted,textAlign:'center'}}>{skgKeyName('G')}</div>}{p5row('G', 300)}</>)], 400, 8);
  // p6: both hands: C E G blocked and broken, the right hand on the treble staff (fingers 1 3 5), the left on the bass (5 3 1)
  const CB = chxNotes('C', 'major', 'bass');
  const hand = (w) => <div style={{fontSize:13,fontWeight:900,color:BK.muted,margin:'0 0 -4px'}}>{w}</div>;
  const p6 = stack([staff('t', scr ? 330 : 540, <>{hand(t('Right hand', '오른손'))}<ChxStaff places={[{ notes: C3, side: ['1', '3', '5'] }, { notes: C3, broken: true }]} width={300} o={{ bars: true, padTop: 10 }} label={t('The right hand on the treble staff: C E G together, fingers 1 3 5; then broken, one note after the other.', '높은음자리표 오선의 오른손: C E G를 함께, 1 3 5번 손가락. 그다음 펼쳐서 한 음씩.')}/></>),
    staff('b', scr ? 330 : 540, <>{hand(t('Left hand', '왼손'))}<ChxStaff clef="bass" places={[{ notes: CB, side: ['5', '3', '1'], lab: t('blocked', '함께') }, { notes: CB, broken: true, lab: t('broken', '펼쳐서') }]} width={300} o={{ bars: true, labSize: 14, padTop: 6 }} label={t('The left hand on the bass staff: C E G together, fingers 5 3 1; then broken.', '낮은음자리표 오선의 왼손: C E G를 함께, 5 3 1번 손가락. 그다음 펼쳐서.')}/></>),
    <div key="k" style={{maxWidth:260,margin:'6px auto 0',width:'100%'}}><ChxKeys d0={28} n={5} o={{ H: 100, lit: [60], pale: [64, 67] }} label={t('C, E and G on the keys.', '건반의 C, E, G.')}/></div>,
    cap(t('Right hand 1 3 5 · left hand 5 3 1', '오른손 1 3 5 · 왼손 5 3 1'), 'cap6')], 360, 10);

  // the check icons
  const tx = (x, c, col, s = 18, y = 28) => '<text x="' + x + '" y="' + y + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + s + '" font-weight="900" fill="' + col + '">' + c + '</text>';
  const head = (x, y, col) => '<ellipse cx="' + x + '" cy="' + y + '" rx="4.4" ry="3.1" fill="' + col + '"/>';
  const st5 = '<g stroke="' + PEN_N + '" stroke-opacity="0.55" stroke-width="1.2">' + [8, 14, 20, 26, 32].map(y => '<line x1="6" x2="86" y1="' + y + '" y2="' + y + '"/>').join('') + '</g>';
  const ic = {
    stack: [{ k: 'raw', svg: st5 + head(46, 32, PEN_C) + head(46, 26, PEN_N) + head(46, 20, PEN_N) }],
    mm: [{ k: 'raw', svg: tx(24, '4+3', PEN_N, 15, 27) + tx(68, '3+4', PEN_C, 15, 27) }],
    tonic: [{ k: 'raw', svg: tx(20, 'G', PEN_N, 20, 29) + tx(64, 'G B D', PEN_C, 13, 27) }],
    prim: [{ k: 'raw', svg: tx(16, 'I', PEN_N, 17, 28) + tx(44, 'IV', PEN_C, 17, 28) + tx(74, 'V', PEN_N, 17, 28) }],
    hands: [{ k: 'raw', svg: st5 + head(22, 32, PEN_N) + head(22, 26, PEN_N) + head(22, 20, PEN_N) + head(52, 32, PEN_C) + head(66, 26, PEN_C) + head(80, 20, PEN_C) }],
  };
  const checksRows = [
    ['stack', t('I can stack a triad on any white key and name its notes', '흰건반 어디에서나 3화음을 쌓고 음이름을 말할 수 있어요')],
    ['mm', t('I can tell a major triad from a minor one, by counting and by ear', '반 걸음을 세거나 소리를 듣고 장3화음과 단3화음을 구별할 수 있어요')],
    ['tonic', t('I can write and play the tonic triad of C, G, D and F major', 'C, G, D, F장조의 으뜸화음을 쓰고 칠 수 있어요')],
    ['prim', t('I can play I, IV and V in C and G major and name their letters', 'C장조와 G장조에서 I, IV, V를 치고 음이름을 말할 수 있어요')],
    ['hands', t('I can play a triad blocked and broken, in each hand', '오른손과 왼손 모두 3화음을 함께, 또 펼쳐서 칠 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? skgKo(sscNbKo(chxNbKo(x))) : sscNbEn(x)]);
  const ch11 = bkChapterNo('tones'), ch16 = bkChapterNo('scales'), ch21 = bkChapterNo('intervals');

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <>세 음 이상이 함께 울리는 소리를 <b>화음</b>이라고 해요. <b>3화음</b>은 근음, 3음, 5음, 세 음을 3도씩 쌓은 화음이에요.</> : <>A <b>chord</b> is three or more notes sounding together. A <b>triad</b> has three: the root, the 3rd and the 5th, stacked in 3rds.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Stack a triad', '3화음 쌓기'), 2], [t('Major and minor', '장3화음과 단3화음'), 3], [t('The tonic triad', '으뜸화음'), 4], [t('I, IV and V', 'I, IV, V'), 5], [t('Both hands', '양손으로'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}<span>{n}</span></span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)',textWrap:'pretty'}}>{bkGoal(15)}<span>{sscSx(x.replace(/^I can /, ''))}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={ivxTitle(t('Stack a triad', '3화음 쌓기'))}>
      {live(p2, <ChxStackPad/>)}
      <LbDefs items={[
        [t('triad', '3화음'), X('Three notes stacked in 3rds: skip a letter, skip a letter. C E G.', '3도씩 쌓은 세 음이에요. 음이름을 하나씩 건너뛰어요. C E G.')],
        [t('root', '근음'), X('The note the triad is built on. It names the triad: C E G is a C triad.', '3화음을 쌓는 음이에요. 3화음의 이름이 돼요. C E G는 C 3화음.')],
        [t('root position', '기본 위치'), X('The root at the bottom, as in every triad in this chapter.', '근음이 맨 아래에 있어요. 이 챕터의 3화음은 모두 기본 위치예요.')],
        [t('3rd and 5th', '3음과 5음'), X('A 3rd and a 5th above the root (chapter ' + ch21 + ').', '근음에서 3도 위, 5도 위의 음이에요(' + ch21 + '챕터).')],
        [t('on the staff', '오선에서'), X('All three on lines, or all three in spaces, on either staff.', '높은음자리표 오선에서도 낮은음자리표 오선에서도 세 음이 모두 줄에, 또는 모두 칸에 있어요.')],
      ]}/>
      <LbPiano steps={[
        X('Right hand: play C, E and G together with fingers 1, 3 and 5.', '오른손: C, E, G를 1, 3, 5번 손가락으로 함께 쳐요.'),
        X('Play the triad on each white key from C up to B. Say its letters: D F A, E G B …', 'C부터 B까지 흰건반마다 3화음을 쳐요. 음이름을 말해요: D F A, E G B …'),
      ]}/>
      <LbRemember>{X('Skip a letter, skip a letter: root, 3rd, 5th.', '하나 건너, 하나 건너: 근음, 3음, 5음.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={ivxTitle(t('Major and minor', '장3화음과 단3화음'))}>
      {live(p3, <ChxMinorPad/>)}
      <LbDefs items={[
        [t('major triad', '장3화음'), X('Root to 3rd: a major 3rd, 4 half steps (chapter ' + ch11 + '). 3rd to 5th: 3. C E G.', '근음에서 3음까지 장3도, 반 걸음 4개(' + ch11 + '챕터). 3음에서 5음까지 반 걸음 3개. C E G.')],
        [t('minor triad', '단3화음'), X('Root to 3rd: a minor 3rd, 3 half steps. 3rd to 5th: 4. C E♭ G.', '근음에서 3음까지 단3도, 반 걸음 3개. 3음에서 5음까지 반 걸음 4개. C E♭ G.')],
        [t('the 3rd moves', '3음이 움직여요'), X('Major to minor: the 3rd goes down a half step. The root and the 5th stay.', '장3화음에서 단3화음으로: 3음이 반 걸음 내려가요. 근음과 5음은 그대로예요.')],
        [t('on the white keys', '흰건반에서'), X('C, F and G make major triads; D, E and A make minor ones.', 'C, F, G 위에는 장3화음, D, E, A 위에는 단3화음이 생겨요.')],
      ]}/>
      <LbPiano steps={[
        X('Play C E G, then C E♭ G. Count the half steps of each: 4 + 3, then 3 + 4.', 'C E G를 치고 C E♭ G를 쳐요. 반 걸음을 세어요: 4 + 3, 그다음 3 + 4.'),
        X('Your teacher plays a triad. Say: major or minor.', '선생님이 3화음을 쳐요. 장3화음인지 단3화음인지 말해요.'),
      ]}/>
      <LbRemember>{X('Major: 4 + 3. Minor: 3 + 4.', '장3화음은 4 + 3, 단3화음은 3 + 4.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The tonic triad', '으뜸화음')}>
      {live(p4, <ChxTonicPad/>)}
      <LbDefs items={[
        [t('tonic triad', '으뜸화음'), X('The triad on the tonic, the key’s first note (chapter ' + ch16 + '). In G major: G B D.', '조의 첫 음인 으뜸음 위에 쌓은 3화음이에요(' + ch16 + '챕터). G장조에서는 G B D.')],
        [t('Roman numeral', '로마 숫자'), X('A triad’s number: its root’s place in the scale. The tonic triad is I.', '3화음에는 근음의 번호를 로마 숫자로 붙여요. 으뜸화음은 I이에요.')],
        [t('with the key signature', '조표와 함께'), X('The key signature gives the triad its sharp or flat: D major’s is D F♯ A.', '샤프나 플랫은 조표대로예요. D장조의 으뜸화음은 D F♯ A.')],
      ]}/>
      <LbPiano steps={[
        X('Play the tonic triad of C, G, D and F major, together and then one note at a time.', 'C, G, D, F장조의 으뜸화음을 함께 친 다음 한 음씩 쳐요.'),
        X('Play the scale of G major, then its tonic triad. Say: G B D.', 'G장조 음계를 치고 으뜸화음을 쳐요. 말해요: G B D.'),
      ]}/>
      <LbRemember>{X('The tonic triad: the scale’s 1st, 3rd and 5th notes.', '으뜸화음: 음계의 1번, 3번, 5번 음.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('I, IV and V', 'I, IV, V')}>
      {live(p5, <ChxPrimaryPad/>)}
      <LbDefs items={[
        [t('I, IV and V', 'I, IV, V'), X('The primary triads: the triads on the 1st, 4th and 5th notes of the scale. In C major: C, F and G.', '주요 3화음: 음계의 1번, 4번, 5번 음 위의 3화음이에요. C장조에서는 C, F, G.')],
        [t('their names', '이름'), X('I is the tonic triad, IV the subdominant, V the dominant.', 'I은 으뜸화음, IV는 버금딸림화음, V는 딸림화음이에요.')],
        [t('in a major key', '장조에서'), X('I, IV and V are all major triads.', 'I, IV, V는 모두 장3화음이에요.')],
        [t('numeral and letter', '로마 숫자와 음이름'), X('The numeral is its root’s place in the key; the letter, its root. In G major, IV is C.', '로마 숫자는 근음의 번호, 음이름은 근음의 이름이에요. G장조에서 IV는 C예요.')],
      ]}/>
      <LbPiano steps={[
        X('Right hand: play I, IV, V and I again in C major, saying the numerals.', '오른손: C장조에서 I, IV, V, 다시 I을 치며 로마 숫자를 말해요.'),
        X('Do the same in G major and in F major, saying the letters: G, C, D, G; F, B♭, C, F.', 'G장조와 F장조에서도 똑같이, 음이름을 말하며 쳐요: G, C, D, G; F, B♭, C, F.'),
      ]}/>
      <LbRemember>{X('I, IV, V: the triads on the 1st, 4th and 5th notes.', 'I, IV, V: 1번, 4번, 5번 음 위의 3화음.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Both hands', '양손으로')}>
      {live(p6, <ChxHandsPad/>)}
      <LbDefs items={[
        [t('blocked chord', '함께 치는 화음'), X('All the notes together. Its other name is a solid chord.', '세 음을 한꺼번에 치는 화음이에요.')],
        [t('broken chord', '펼친 화음'), X('The notes one after the other. Here, from the root up.', '한 음씩 차례로 쳐요. 다른 이름은 분산화음이에요.')],
        [t('fingers', '손가락 번호'), X('Right hand 1 3 5, from the root up; left hand 5 3 1.', '오른손은 근음부터 1 3 5, 왼손은 5 3 1.')],
        [t('on the bass staff', '낮은음자리표 오선에서'), X('The same shape: C E G here is in three spaces.', '모양은 같아요. 여기서 C E G는 세 칸에 있어요.')],
      ]}/>
      <LbPiano steps={[
        X('Play C E G blocked, then broken, in the right hand, then in the left.', 'C E G를 오른손으로 함께, 그다음 펼쳐서 쳐요. 왼손도 똑같이.'),
        X('Left hand blocked, right hand broken: C, then F, then G.', '왼손은 함께, 오른손은 펼쳐서 C, F, G 순서로 쳐요.'),
      ]}/>
      <LbRemember>{X('Blocked: together. Broken: one after the other.', '함께 치는 화음은 한꺼번에, 펼친 화음은 한 음씩 차례로.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, sscSx(x)])}/>} live={<FiveChecks376 storeKey="pb_five_chx_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, sscSx(x)])}/>}/>
    </LbPage>,
  ];
}
function ChordsLessonBook() { return <>{chxLbPages(false)}</>; }
