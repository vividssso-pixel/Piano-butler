// ─── Phase 472: chapter 17, Accidentals: a new room on Level 3, after Scales (the level plan of Phase 435: 'the word
// accidental; the natural; a sign lasts until the bar line, on the same line or space; reading tunes with them'; AMEB
// Preliminary reads sharps and flats, Grade 1 adds the natural). It builds on chapter 11 (the half step; sharp and flat;
// F♯ = G♭), chapter 8 (bar lines; the tie) and chapter 9 (reading a tune; C position). Built in full under Book rules 14
// and 15 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게').
// Words: accidental, sharp, flat, natural, bar line; Korean 임시표, 샤프 (its other name 올림표), 플랫 (내림표), 내추럴
// (제자리표), 세로줄 (chapter 8's word for the bar line); a sign 'has effect' to the bar line (효과가 있어요).
// A tune is written as chapter 9's items ['q', beats, d] with a fourth item for its sign: '#', 'b' or 'n' (the natural).

const SAC_ACC = { '#': 1, b: -1, n: 0 };
const sacIsNote = (it) => !['|', '||', 'ts', 'sp', 'p'].includes(it[0]) && !sskIsRest(it[0]);
// how each note of a tune sounds: a sign holds to its bar line, for its own line or space (its d) only; a natural cancels
// (carried: no sign of its own, the sign held; natHeld: a natural earlier in the bar holds; reset: plain again after a bar line; other: plain, its letter signed on
// another line or space in the bar). A beamed pair ('p') is two plain-or-held notes.
function sacRead(items) {
  const out = []; let held = {}, prev = {};
  const note = (d, dur, s) => {
    if (s) held[d] = SAC_ACC[s];
    const acc = held[d] || 0;
    out.push({ d, dur, acc, sign: s || null, carried: !s && !!held[d], natHeld: !s && held[d] === 0, reset: !s && held[d] === undefined && !!prev[d],
      other: !s && !acc && Object.keys(held).some(k => +k !== d && (+k - d) % 7 === 0 && held[k]) });
  };
  items.forEach(it => {
    if (it[0] === '|' || it[0] === '||') { prev = held; held = {}; return; }
    if (it[0] === 'p') { note(it[2][0], 0.5); note(it[2][1], 0.5); return; }
    if (sacIsNote(it)) note(it[2], it[1], it[3]);
  });
  return out;
}
const sacMidi = (n) => ivMidi({ d: n.d, acc: n.acc });
const sacNameTxt = (n) => dName(n.d) + (n.acc === 1 ? '♯' : n.acc === -1 ? '♭' : '');
const SAC_MF = "'Noto Music','Apple Symbols','Segoe UI Symbol','DejaVu Sans',serif";   // MUSIC_FONT with a Latin fallback before serif (a CJK serif sets ♭ full width)
const sacSignRaw = (c, sz) => '<tspan style="font-family:' + SAC_MF + ';font-weight:400" font-size="' + Math.round(sz * 1.35) + '">' + c + '</tspan>';
const sacNameRaw = (n, sz = 14) => dName(n.d) + (n.acc ? sacSignRaw(n.acc === 1 ? '♯' : '♭', sz) : '');

// room before a signed note, and each note's sign, for sskRaw (which draws notes, bars and the words under them)
function sacPrep(items, room) {
  const out = [], signs = [];
  items.forEach(it => {
    if (it[0] === 'p') { signs.push(null, null); out.push(it); return; }
    if (sacIsNote(it)) { if (it[3]) out.push(['sp', room]); signs.push(it[3] || null); out.push(it.slice(0, 3)); } else out.push(it);
  });
  return { items: out, signs };
}
// a tune on one staff with its signs. o: sskRaw's options (hl: coral notes; under: words or boxes under the notes;
// underCoral; boxS; D; x0) and room (before a signed note), noSign (notes whose sign is left to draw: the room stays),
// signHl (signs in coral), ring (notes circled in coral: a worked example), bracket ({ from: a note, bar: a bar line,
// label }: a coral bracket from a sign to its bar line; bracketRoom: the same room above, no bracket). width: the reference
// width (not full: one size on every page); left: drawn from the left (a row of a set, inside sacSet's box)
function SacStaff({ items, clef = 'treble', width = 400, o = {}, label, full, pad, left }) {
  const P = sacPrep(items, o.room || 16), oo = { ...o, clef }, m = sskRaw((d) => dY(d), P.items, oo), vbw = Math.ceil(m.last + 6);
  const hi = dY(CLEFS[clef].high), lo = dY(CLEFS[clef].low);
  const sTop = Math.min(m.top, ...m.notes.map((n, j) => P.signs[j] ? n.y - 21 : Infinity)), sBot = Math.max(m.bottom, ...m.notes.map((n, j) => P.signs[j] ? n.y + 17 : -Infinity));
  const top = o.bracket || o.bracketRoom ? Math.min(sTop, hi) - 30 : sTop;
  const p = pad || [Math.max(12, hi - top + 6), Math.max(12, sBot - lo + 6)];
  return <div style={{width:full ? '100%' : Math.min(100, vbw / width * 100) + '%',margin:full || left ? undefined : '0 auto'}}><SfStaff clef={clef} width={vbw} span={[4, m.last]} pad={p} label={label}
    extra={(yOf, layer) => { if (layer !== 'over') return null; const mm = sskRaw((d) => yOf(d, clef), P.items, oo);
      return <g><g dangerouslySetInnerHTML={{ __html: mm.raw }}/>
        {mm.notes.map((n, j) => P.signs[j] && !(o.noSign || []).includes(j) && <g key={'s' + j}>{tnAcc(P.signs[j], n.x - 21, n.y, (o.signHl || []).includes(j) ? PEN_C : (o.ink || PEN_N))}</g>)}
        {(o.ring || []).map(j => mm.notes[j] && <ellipse key={'r' + j} cx={mm.notes[j].x} cy={mm.notes[j].y} rx="15" ry="11" fill="none" stroke={PEN_C} strokeWidth="1.8"/>)}
        {o.bracket && (() => { const a = mm.notes[o.bracket.from], x1 = a.x - 27, x2 = mm.bars[o.bracket.bar], y = Math.min(sTop, hi) - 12, yt = yOf(CLEFS[clef].high) - 4;
          return <g><path d={`M${x1} ${y + 6} L${x1} ${y} L${x2} ${y} L${x2} ${yt}`} fill="none" stroke={PEN_C} strokeWidth="1.8" strokeLinejoin="round"/>
            {o.bracket.label && <text x={(x1 + x2) / 2} y={y - 6} textAnchor="middle" fontSize="13" fontWeight="900" fill={PEN_C} style={{paintOrder:'stroke',stroke:'#fff',strokeWidth:3}}>{o.bracket.label}</text>}</g>; })()}
      </g>; }}/></div>;
}
// a staff's drawn width (its viewBox), for a set of rows drawn at one size from one left edge
const sacVbw = (items, o = {}, clef = 'treble') => Math.ceil(sskRaw((d) => dY(d), sacPrep(items, o.room || 16).items, { ...o, clef }).last + 6);
// a set of staves at one size (ref), their clefs in line: a box as wide as the widest, centred; each row drawn from its left
const sacSetBox = (list, ref, oOf = () => ({})) => Math.min(ref, Math.max(...list.map((it, i) => sacVbw(it, oOf(it, i)))));
const sacInSet = (box, ref, node, key) => <div key={key} style={{width:box / ref * 100 + '%',margin:'0 auto'}}>{node}</div>;
// a tune split at every bar line, one bar a row (the phone screen's drills)
const sacBars = (items) => { const rows = [[]]; items.forEach(it => { rows[rows.length - 1].push(it); if (it[0] === '|') rows.push([]); }); return rows.filter(r => r.some(sacIsNote)); };
// names under each note (the held ones in coral when asked; only those when 'heldOnly')
const sacUnder = (items, coralHeld, heldOnly) => { const r = sacRead(items);
  return { under: r.map(n => heldOnly && !n.carried ? undefined : sacNameRaw(n)), underCoral: coralHeld ? r.map((n, j) => n.carried ? j : -1).filter(j => j >= 0) : [] }; };

// a keyboard from a white key d0, n white keys: tappable; lit (solid coral), pale, dots and miss, by MIDI number
function SacKeys({ d0 = 28, n = 8, o = {}, onTap, label }) {
  const W = 40, H = o.H || 130, BW = 25, BH = Math.round(H * 0.6), x0 = 3, keys = [];
  for (let i = 0; i < n; i++) { const d = d0 + i, m = ivMidi({ d }); keys.push({ i, d, m, white: true, L: dName(d) }); if ('CDFGA'.includes(dName(d)) && i < n - 1) keys.push({ i, d, m: m + 1, white: false }); }
  const lit = new Set([].concat(o.lit == null ? [] : o.lit)), pale = new Set(o.pale || []), dots = new Set(o.dots || []);
  const cx = (k) => k.white ? x0 + (k.i + 0.5) * W : x0 + (k.i + 1) * W;
  const tap = (k) => onTap ? () => onTap(k.m) : undefined;
  return (
    <svg viewBox={`0 0 ${x0 * 2 + n * W} ${H + 6}`} role="img" aria-label={label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>
      {keys.filter(k => k.white).map(k => <g key={'w' + k.i} onClick={tap(k)} style={{cursor:onTap ? 'pointer' : 'default'}} data-sac={k.m}>
        <rect x={x0 + k.i * W} y={3} width={W} height={H} rx="3" fill={lit.has(k.m) ? PEN_C : pale.has(k.m) ? '#fbd9cc' : '#fff'} stroke={o.miss === k.m ? PEN_C : PEN_N} strokeWidth={o.miss === k.m ? 3.2 : 1.6}/>
        {!o.noNames && <text x={cx(k)} y={H - 8} textAnchor="middle" fontSize="15" fontWeight="900" fill={lit.has(k.m) ? '#fff' : PEN_N} style={{pointerEvents:'none'}}>{k.L}</text>}
        {dots.has(k.m) && <circle cx={cx(k)} cy={H - 34} r="6" fill={PEN_C}/>}
      </g>)}
      {keys.filter(k => !k.white).map(k => <g key={'b' + k.i} onClick={tap(k)} style={{cursor:onTap ? 'pointer' : 'default'}} data-sac={k.m}>
        <rect x={cx(k) - BW / 2} y={3} width={BW} height={BH} rx="2" fill={lit.has(k.m) ? PEN_C : pale.has(k.m) ? '#f08c70' : PEN_N} stroke={o.miss === k.m ? PEN_C : lit.has(k.m) ? '#fff' : PEN_N} strokeWidth={o.miss === k.m ? 3.2 : lit.has(k.m) ? 2.2 : 1}/>
        {dots.has(k.m) && <circle cx={cx(k)} cy={BH - 10} r="5.5" fill={PEN_C} stroke="#fff" strokeWidth="1.5"/>}
      </g>)}
    </svg>
  );
}

// the tunes of the book's pictures (the pads on pages 2 to 6 play them)
const SAC_TUNES = {
  1: [['ts', 4], ['q', 1, 31, '#'], ['q', 1, 34, 'b'], ['q', 1, 34, 'n'], ['q', 1, 35], ['||']],
  2: [['w', 4, 31, '#'], ['w', 4, 34, 'b'], ['w', 4, 35, '#'], ['||']],
  3: [['q', 1, 34, 'b'], ['q', 1, 33], ['q', 1, 34, 'n'], ['q', 1, 35], ['||']],
  4: [['ts', 4], ['q', 1, 35, '#'], ['q', 1, 36], ['q', 1, 35], ['q', 1, 34], ['|'], ['q', 1, 35], ['q', 1, 36], ['h', 2, 37], ['||']],
  5: [['q', 1, 38, '#'], ['q', 1, 37], ['q', 1, 31], ['q', 1, 38], ['||']],
  6: [['ts', 4], ['q', 1, 30], ['q', 1, 31, '#'], ['q', 1, 32], ['q', 1, 31], ['|'], ['q', 1, 30], ['q', 1, 31], ['h', 2, 32], ['|'],
      ['q', 1, 32], ['q', 1, 30, 'b'], ['q', 1, 29], ['q', 1, 30], ['|'], ['q', 1, 29], ['q', 1, 30], ['h', 2, 28], ['||']],
};
const SAC_TUNE_O = { 2: { D: 18 } };                                                  // the semibreves closer together
const SAC_KEYS = { 1: [28, 9], 2: [28, 9], 3: [31, 6], 4: [33, 6], 5: [31, 9], 6: [28, 6] };   // each page's keyboard: from d, n white keys
// a tune split at a bar line into two rows (chapter 9's way for four bars)
const sacRows = (items) => { const k = items.findIndex((it, i) => it[0] === '|' && items.slice(0, i).filter(x => x[0] === '|').length === 1); return k < 0 ? [items] : [items.slice(0, k + 1), items.slice(k + 1)]; };

function sacLbPages(scr = false) {
  const ch = 'accidentals';
  const live = (still, comp) => <LbLive still={still} live={comp}/>;
  const stack = (nodes, h, gap = 12, mw = 680) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap,width:'100%',maxWidth:mw,margin:'0 auto',alignItems:'stretch'}}>{nodes}</div></LbPic>;
  const X = sscT, T = SAC_TUNES, REF = scr ? 270 : 330;   // one staff size on every page: the staff drawn at (its width / REF) of the picture
  const tune = (items, o = {}, key = 's', label) => <div key={key} style={{width:'100%'}}><SacStaff items={items} width={REF} o={{ boxS: 26, ...o }} label={label}/></div>;
  const keys = (k, o, label, mw = 470) => <div key="k" style={{maxWidth:mw,margin:'0 auto',width:'100%'}}><SacKeys d0={SAC_KEYS[k][0]} n={SAC_KEYS[k][1]} o={{ H: 150, ...o }} label={label}/></div>;

  // p1: the three signs in one bar, and their keys
  const p1 = stack([tune(T[1], { ...sacUnder(T[1]) }, 's', t('One bar on the treble staff: F sharp, B flat, B natural, C, each name under its note.', '높은음자리표 오선의 한 마디: F♯, B♭, B♮, C, 음표마다 아래에 이름.')),
    keys(1, { lit: [66, 70, 71] }, t('The keys from C to D: F sharp, B flat and B in coral.', 'C에서 D까지의 건반: F♯, B♭, B는 산호색.'))], 220, 16);
  // p2: three signs on the staff, and their keys
  const p2 = stack([tune(T[2], { D: 18, ...sacUnder(T[2]) }, 's', t('Three notes on the treble staff, each with its sign just before it: F sharp, B flat, C sharp; their names under them.', '높은음자리표 오선의 세 음, 음표 바로 앞에 임시표: F♯, B♭, C♯; 아래에 이름.')),
    keys(2, { lit: [66, 70, 73] }, t('The keys from C to D: F sharp, B flat and C sharp in coral.', 'C에서 D까지의 건반: F♯, B♭, C♯는 산호색.'))], 300, 16);
  // p3: a natural cancels the flat
  const p3 = stack([tune(T[3], { signHl: [2], hl: [2], under: sacUnder(T[3]).under, underCoral: [2] }, 's', t('One bar: B flat, A, B natural (in coral), C. Under the notes: B flat, A, B, C.', '한 마디: B♭, A, B♮(산호색), C. 음표 아래: B♭, A, B, C.')),
    keys(3, { lit: [71] }, t('The keys from F to D: B in coral.', 'F에서 D까지의 건반: B는 산호색.'), 340)], 300, 16);
  // p4: until the bar line
  const p4 = stack([tune(T[4], { ...sacUnder(T[4], true), bracket: { from: 0, bar: 0, label: t('C♯ until the bar line', 'C♯: 세로줄까지') } }, 's', t('Two bars: C sharp, D, C, B, then C, D, E. A coral bracket runs from the sharp to the bar line. Under the notes: C sharp, D, C sharp (in coral: still C sharp), B; then C, D, E.', '두 마디: C♯, D, C, B, 그다음 C, D, E. 샤프에서 세로줄까지 산호색 괄호. 음표 아래: C♯, D, C♯(산호색: 아직 C♯), B; 그다음 C, D, E.')),
    keys(4, { lit: [73] }, t('The keys from A to F: C sharp in coral.', 'A에서 F까지의 건반: C♯는 산호색.'), 340)], 240, 16);
  // p5: only its own line or space
  const p5 = stack([tune(T[5], { ...sacUnder(T[5], true) }, 's', t('One bar: F sharp on the top line, E, F in the bottom space, F on the top line. Under the notes: F sharp, E, F (another space: plain), F sharp (in coral: the same line, still F sharp).', '한 마디: 맨 윗줄의 F♯, E, 맨 아래 칸의 F, 맨 윗줄의 F. 음표 아래: F♯, E, F(다른 칸: 그대로 F), F♯(산호색: 같은 줄이라 아직 F♯).')),
    keys(5, { lit: [78], pale: [65] }, t('The keys from F to G: the high F sharp in coral, the low F pale coral.', 'F에서 G까지의 건반: 높은 F♯는 산호색, 낮은 F는 옅은 산호색.'), 480)], 300, 16);
  // p6: a tune with its signs, in two rows; only the held notes named (in coral)
  const r6 = sacRows(T[6]), box6 = sacSetBox(r6, REF);
  const p6 = stack(r6.map((row, i) => sacInSet(box6, REF, <SacStaff items={row} width={box6} left o={{ boxS: 26, ...sacUnder(row, true, true) }} label={ i ? t('Bars 3 and 4: G, E flat, D, E (in coral under it: still E flat), then D, E, C.', '3, 4마디: G, E♭, D, E(아래에 산호색: 아직 E♭), 그다음 D, E, C.') : t('A tune in four bars. Bars 1 and 2: E, F sharp, G, F (in coral under it: still F sharp), then E, F, G.', '네 마디 선율. 1, 2마디: E, F♯, G, F(아래에 산호색: 아직 F♯), 그다음 E, F, G.')}/>, 'r' + i)), 280, 14);

  // the check icons
  const g = (x, c, s, col) => '<text x="' + x + '" y="30" text-anchor="middle" style="font-family:' + SAC_MF + '" font-size="' + s + '" fill="' + col + '">' + c + '</text>';
  const tx = (x, c, col, s = 18) => '<text x="' + x + '" y="28" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + s + '" font-weight="900" fill="' + col + '">' + c + '</text>';
  const ic = {
    signs: [{ k: 'raw', svg: g(22, '♯', 28, PEN_N) + g(46, '♭', 28, PEN_N) + g(70, '♮', 28, PEN_C) }],
    natural: [{ k: 'raw', svg: tx(24, 'B', PEN_N) + g(36, '♭', 22, PEN_N) + tx(56, '→', PEN_N, 14) + tx(76, 'B', PEN_C) }],
    bar: [{ k: 'raw', svg: g(20, '♯', 24, PEN_C) + '<line x1="30" x2="62" y1="22" y2="22" stroke="' + PEN_C + '" stroke-width="2"/><line x1="66" x2="66" y1="8" y2="34" stroke="' + PEN_N + '" stroke-width="2.4"/>' + tx(80, 'F', PEN_N, 14) }],
    line: [{ k: 'raw', svg: '<text x="30" y="18" text-anchor="middle" font-family="Inter, sans-serif" font-size="16" font-weight="900" fill="' + PEN_C + '">F</text>' + '<text x="41" y="20" text-anchor="middle" style="font-family:' + SAC_MF + '" font-size="20" fill="' + PEN_C + '">♯</text>' + '<text x="62" y="37" text-anchor="middle" font-family="Inter, sans-serif" font-size="16" font-weight="900" fill="' + PEN_N + '">F</text>' }],
    tune: [{ k: 'raw', svg: [0, 1, 2, 3].map(i => '<ellipse cx="' + (16 + i * 20) + '" cy="' + (28 - i * 4) + '" rx="6" ry="4.6" fill="' + (i === 1 ? PEN_C : PEN_N) + '" transform="rotate(-20 ' + (16 + i * 20) + ' ' + (28 - i * 4) + ')"/><line x1="' + (21.5 + i * 20) + '" x2="' + (21.5 + i * 20) + '" y1="' + (27 - i * 4) + '" y2="' + (6 - i * 4 + 4) + '" stroke="' + PEN_N + '" stroke-width="1.6"/>').join('') }],
  };
  const checksRows = [
    ['signs', t('I can name the three accidentals and say what each one does', '세 가지 임시표의 이름과 하는 일을 말할 수 있어요')],
    ['natural', t('I can play a natural: the plain note again', '내추럴이 붙은 음을 원래 음으로 칠 수 있어요')],
    ['bar', t('I can keep a sign until the bar line', '임시표를 세로줄까지 지킬 수 있어요')],
    ['line', t('I can keep a sign to its own line or space', '같은 줄이나 칸의 음표에만 임시표를 지킬 수 있어요')],
    ['tune', t('I can read and play a tune with accidentals', '임시표가 있는 선율을 읽고 칠 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? sscNbKo(x).replace(/(\S) 수 있어요/g, '$1 수 있어요') : sscNbEn(x)]);

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <>곡 중간에 음표 바로 앞에 붙는 샤프, 플랫, 내추럴을 <b>임시표</b>라고 해요. 임시표는 세로줄까지 효과가 있어요.</> : <>An <b>accidental</b> is a sharp, flat or natural written just before a note. It lasts until the bar line.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Sharp and flat', '샤프와 플랫'), 2], [t('The natural', '내추럴'), 3], [t('Until the bar line', '세로줄까지'), 4], [t('Its own line or space', '같은 줄이나 칸만'), 5], [t('Reading a tune', '선율 읽기'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{sscSx(x.replace(/^I can /, ''))}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Sharp and flat', '샤프와 플랫')}>
      {live(p2, <SacPad page={2}/>)}
      <LbDefs items={[
        [sscSx(t('sharp ♯', '샤프 ♯')), X('Play the next key up: a half step higher.', '바로 위의 건반을 쳐요: 위로 반 걸음. 다른 이름은 올림표예요.')],
        [sscSx(t('flat ♭', '플랫 ♭')), X('Play the next key down: a half step lower.', '바로 아래의 건반을 쳐요: 아래로 반 걸음. 다른 이름은 내림표예요.')],
        [t('where it sits', '자리'), X('Just before the note, on its line or space.', '음표 바로 앞, 그 음표의 줄이나 칸.')],
      ]}/>
      <LbPiano steps={[
        X('Play the three notes of the picture, saying each name: F sharp, B flat, C sharp. The sign is said after the letter.', '그림의 세 음을 이름을 말하며 쳐요: F 샤프, B 플랫, C 샤프. 임시표는 음이름 뒤에 붙여 읽어요.'),
        X('Play F, then F♯; B, then B♭. Say “up” for the sharp, “down” for the flat.', 'F 다음 F♯, B 다음 B♭을 쳐요. 샤프는 “위로”, 플랫은 “아래로”라고 말해요.'),
      ]}/>
      <LbRemember>{X('A sign sits just before its note, on the same line or space.', '임시표는 음표 바로 앞, 같은 줄이나 칸에 붙어요.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('The natural', '내추럴')}>
      {live(p3, <SacPad page={3}/>)}
      <LbDefs items={[
        [sscSx(t('natural ♮', '내추럴 ♮')), X('Cancels a sharp or flat: play the plain note again.', '샤프나 플랫을 없애요: 원래 음으로 쳐요. 다른 이름은 제자리표예요.')],
        [sscSx(t('B♭, then B♮', 'B♭ 다음 B♮')), X('After B♭, a natural brings back B, the white key: a half step up.', '내추럴이 붙으면 원래의 B, 흰건반으로 돌아가요: 위로 반 걸음.')],
        [sscSx(t('F♯, then F♮', 'F♯ 다음 F♮')), X('After F♯, a natural brings back F: a half step down.', '내추럴이 붙으면 원래의 F로 돌아가요: 아래로 반 걸음.')],
      ]}/>
      <LbPiano steps={[
        X('Play the notes of the picture: B♭, A, B♮, C. Say “flat” and “natural”.', '그림의 음을 쳐요: B♭, A, B♮, C. “플랫”, “내추럴”이라고 말해요.'),
        X('Play F♯, then F♮; C♯, then C♮. Say each name.', 'F♯ 다음 F♮, C♯ 다음 C♮을 쳐요. 이름을 하나씩 말해요.'),
      ]}/>
      <LbRemember>{X('A natural cancels a sharp or flat.', '내추럴은 샤프나 플랫을 없애요.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Until the bar line', '세로줄까지')}>
      {live(p4, <SacPad page={4}/>)}
      <LbDefs items={[
        [t('until the bar line', '세로줄까지'), X('A sign lasts to the end of its bar. Every later note on its line or space in that bar takes it too.', '임시표는 그 마디 끝까지 효과가 있어요. 같은 마디 안에서 같은 줄이나 칸에 다시 나오는 음표도 모두 바뀌어요.')],
        [t('after the bar line', '세로줄 다음'), X('The note is plain again. A note tied over the bar line keeps its sign.', '음표는 다시 원래 음이에요. 붙임줄로 세로줄을 넘어 이어진 음표는 임시표가 그대로예요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the notes of the picture, saying the names: C♯ D C♯ B, then C D E.', '이름을 말하며 그림의 음을 쳐요: C♯ D C♯ B, 그다음 C D E.'),
        X('Point to the sign, then to the bar line where it stops. Play it again.', '임시표를 가리키고, 효과가 끝나는 세로줄을 가리켜요. 다시 쳐요.'),
      ]}/>
      <LbRemember>{X('A sign lasts until the bar line.', '임시표는 세로줄까지 효과가 있어요.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Its own line or space', '같은 줄이나 칸만')}>
      {live(p5, <SacPad page={5}/>)}
      <LbDefs items={[
        [t('its own line or space', '같은 줄이나 칸만'), X('A sign changes only the notes on its own line or space. An F an octave away stays F.', '임시표는 같은 줄이나 칸의 음표만 바꿔요. 한 옥타브 떨어진 F는 그대로 F예요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the notes of the picture: F♯, E, F, F♯. The low F is plain; the high F is still F♯.', '그림의 음을 쳐요: F♯, E, F, F♯. 낮은 F는 그대로 F, 높은 F는 아직 F♯예요.'),
        X('Play high F♯, then low F, then high F♯ again. Say each name.', '높은 F♯, 낮은 F, 다시 높은 F♯를 쳐요. 이름을 하나씩 말해요.'),
      ]}/>
      <LbRemember>{X('A sign changes only its own line or space.', '임시표는 같은 줄이나 칸만 바꿔요.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Reading a tune', '선율 읽기')}>
      {live(p6, <SacPad page={6}/>)}
      <LbDefs items={[
        [t('before you play', '치기 전에'), X('Find every sign. Find the bar line where it stops. Then play.', '임시표를 모두 찾아요. 효과가 끝나는 세로줄을 찾아요. 그다음 쳐요.')],
      ]}/>
      <LbPiano steps={[
        X('Point to each sign and to the bar line where it stops. Say the names of all the notes.', '임시표를 하나씩 가리키고, 효과가 끝나는 세로줄도 가리켜요. 모든 음의 이름을 말해요.'),
        X('Put the right hand in C position and play the tune. Finger 4 plays F and F♯; finger 3 plays E and E♭.', '오른손을 C 자리에 놓고 선율을 쳐요. 4번 손가락으로 F와 F♯, 3번 손가락으로 E와 E♭을 쳐요.'),
      ]}/>
      <LbRemember>{X('Find the signs, find the bar lines, then play.', '임시표를 찾고, 세로줄을 찾고, 그다음 쳐요.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, sscSx(x)])}/>} live={<FiveChecks376 storeKey="pb_five_sac_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, sscSx(x)])}/>}/>
    </LbPage>,
  ];
}
function AccidentalsLessonBook() { return <>{sacLbPages(false)}</>; }
