// ─── Phase 474: chapter 19, Key Signatures: the first room of Level 4 (the level plan of Phase 435: 'C, G and F major
// (then D, B flat); a key signature lasts the whole piece, an accidental one bar. (All 15 keys, the circle: later.)'; AMEB
// 2026 Music Craft: Preliminary keys C, G, F major; Grade 1 adds D and B♭ major). It builds on chapter 16 (the major scale;
// G major's F♯, F major's B♭) and chapter 17 (accidentals: until the bar line, on their own line or space). Built in full
// under Book rules 14 and 15 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게').
// Words: key signature, accidental, natural; Korean 조표, 임시표, 내추럴, G장조 (the app's way of naming keys).
// A tune is chapter 17's items (['q', beats, d, sign?]) read with a key: every note of a letter in the key signature
// takes its sharp or flat, in every octave and every bar, unless an accidental in its bar says otherwise.

const SKG_ORDER = { '#': ['F', 'C', 'G', 'D', 'A', 'E', 'B'], b: ['B', 'E', 'A', 'D', 'G', 'C', 'F'] };
const SKG_KEY = { C: ['#', 0], G: ['#', 1], D: ['#', 2], A: ['#', 3], F: ['b', 1], Bb: ['b', 2], Eb: ['b', 3] };
// each sign's place from the treble staff's bottom line (E4 = d 30); on the bass staff two places lower (G2 = d 18)
const SKG_POS = { '#': { F: 8, C: 5, G: 9, D: 6, A: 3, E: 7, B: 4 }, b: { B: 4, E: 7, A: 3, D: 6, G: 2, C: 5, F: 1 } };
const skgSigns = (key) => { const [s, n] = SKG_KEY[key]; return SKG_ORDER[s].slice(0, n).map(l => [s, l]); };
const skgSignD = (s, l, clef) => (clef === 'bass' ? 16 : 30) + SKG_POS[s][l];
const skgKs = (key, clef = 'treble') => skgSigns(key).map(([s, l]) => [s, skgSignD(s, l, clef)]);
const skgMap = (key) => Object.fromEntries(skgSigns(key).map(([s, l]) => [l, SAC_ACC[s]]));
const skgKeyName = (key) => t(prettyNote(key) + ' major', prettyNote(key) + '장조');
const skgSignNames = (key) => skgSigns(key).map(([s, l]) => l + (s === '#' ? '♯' : '♭'));
const skgCountWords = (key) => { const [s, n] = SKG_KEY[key];
  return n === 0 ? t('no sharps or flats', '샤프도 플랫도 없음') : t(['', 'one', 'two', 'three'][n] + (s === '#' ? ' sharp' : ' flat') + (n > 1 ? 's' : ''), (s === '#' ? '샤프 ' : '플랫 ') + ['', '하나', '둘', '셋'][n]); };
// a line or space by name (the drill's answers, the Teacher copy): 1st line at the bottom
const skgWhere = (d, clef = 'treble', en) => { const k = d - CLEFS[clef].low, ord = ['first', 'second', 'third', 'fourth', 'fifth'], ko = ['맨 아랫', '둘째 ', '셋째 ', '넷째 ', '다섯째 '], T = en ? (a) => a : t;
  if (k < 0 || k > 9) return k > 9 ? T('above the staff', '오선 위') : T('below the staff', '오선 아래');
  if (k === 9) return T('the space above the staff', '오선 위의 칸');
  if (k % 2 === 0) return k === 8 ? T('the top line', '맨 윗줄') : k === 4 ? T('the middle line', '가운데 줄') : T('the ' + ord[k / 2] + ' line', ko[k / 2] + '줄');
  if (k === 1) return T('the first space', '맨 아래 칸');
  return k === 7 ? T('the top space', '맨 위 칸') : T('the ' + ord[(k - 1) / 2] + ' space', ko[(k - 1) / 2].trim() + ' 칸'); };
// Korean: a sign never parts from the syllable after it (a word joiner); 'ㄹ 수 있어요', '맨 윗줄', '맨 위 칸' on one line
const skgKo = (x) => x.replace(/([♯♭♮])(?=[가-힣(])/g, '$1\u2060').replace(/(\S) 수 있어요/g, '$1\u00a0수\u00a0있어요').replace(/맨 (윗줄|위 칸|아랫줄)/g, '맨\u00a0$1');
// the Phase 299 lesson's ticks (0 to 6, under the same id): not this lesson's steps (they are synced by union, so ignored, not deleted)
function skgOldStep(id, k) { return id === 'key-signatures' && /^\d+$/.test(String(k)); }

// how each note of a tune sounds in a key: the key signature, unless an accidental earlier in its bar (on its own line or
// space) says otherwise. byKey: changed by the key signature; held / natHeld: an accidental earlier in the bar still holds;
// back: an accidental in the bar before, so the key signature again
function skgRead(items, key = 'C') {
  const ks = skgMap(key), out = []; let held = {}, prev = {};
  const note = (d, dur, s) => {
    if (s) held[d] = SAC_ACC[s];
    const kAcc = ks[dName(d)] || 0, h = held[d], acc = h !== undefined ? h : kAcc;
    out.push({ d, dur, acc, sign: s || null, byKey: !s && h === undefined && kAcc !== 0, held: !s && h !== undefined && h !== 0, natHeld: !s && h === 0,
      back: !s && h === undefined && prev[d] !== undefined && prev[d] !== kAcc });
  };
  items.forEach(it => {
    if (it[0] === '|' || it[0] === '||') { prev = held; held = {}; return; }
    if (it[0] === 'p') { note(it[2][0], 0.5); note(it[2][1], 0.5); return; }
    if (sacIsNote(it)) note(it[2], it[1], it[3]);
  });
  return out;
}
const skgNames = (items, key) => skgRead(items, key).map(sacNameTxt);
// names under the notes (only some: 'only' a list of note indexes); coral: the indexes named in coral
const skgUnder = (items, key, only, coral = []) => ({ under: skgRead(items, key).map((n, j) => only && !only.includes(j) ? undefined : sacNameRaw(n)), underCoral: coral });
const skgOf = (items, key, f) => skgRead(items, key).map((n, j) => f(n) ? j : -1).filter(j => j >= 0);

// a staff with its clef, its key signature (k: the key; o.ks: signs drawn as given, [[sign, d]]; o.ksRoom: the room of
// that many signs, none drawn, to write in; o.ksCol: their colour) and a tune (SacStaff's options: hl, under, ring, bracket ...)
function SkgStaff({ items, k = 'C', clef = 'treble', width = 400, o = {}, label, full, pad, left }) {
  const ks = o.ks || skgKs(k, clef), base = o.base || (clef === 'bass' ? 54 : 46), room = o.ksRoom != null ? o.ksRoom : ks.length;
  const ksx = (i) => base + 6 + i * 15, x0 = skgX0(items, base, room);
  const P = sacPrep(items, o.room || 16), oo = { ...o, clef, x0 }, m = sskRaw((d) => dY(d), P.items, oo);
  const vbw = Math.ceil(Math.max(m.last, x0 + 8) + 6), hi = dY(CLEFS[clef].high), lo = dY(CLEFS[clef].low);
  const kTop = Math.min(Infinity, ...ks.map(([s, d]) => dY(d) - (s === 'b' ? 20 : 16))), kBot = Math.max(-Infinity, ...ks.map(([s, d]) => dY(d) + (s === 'b' ? 6 : 16)));
  const sTop = Math.min(m.top, kTop, ...m.notes.map((n, j) => P.signs[j] ? n.y - 21 : Infinity)), sBot = Math.max(m.bottom, kBot, ...m.notes.map((n, j) => P.signs[j] ? n.y + 17 : -Infinity));
  const top = o.bracket || o.bracketRoom ? Math.min(sTop, hi) - 30 : sTop;
  const p = pad || [Math.max(12, hi - top + 6), Math.max(12, sBot - lo + 6)];
  return <div style={{width:full ? '100%' : Math.min(100, vbw / width * 100) + '%',margin:full || left ? undefined : '0 auto'}}><SfStaff clef={clef} width={vbw} span={[4, m.last || vbw - 6]} pad={p} label={label}
    extra={(yOf, layer) => { if (layer !== 'over') return null; const mm = sskRaw((d) => yOf(d, clef), P.items, oo);
      return <g>{ks.map(([s, d], i) => <g key={'k' + i}>{tnAcc(s, ksx(i), yOf(d, clef), o.ksCol || PEN_N)}</g>)}
        <g dangerouslySetInnerHTML={{ __html: mm.raw }}/>
        {mm.notes.map((n, j) => P.signs[j] && !(o.noSign || []).includes(j) && <g key={'s' + j}>{tnAcc(P.signs[j], n.x - 21, n.y, (o.signHl || []).includes(j) ? PEN_C : (o.ink || PEN_N))}</g>)}
        {(o.ring || []).map(j => mm.notes[j] && <ellipse key={'r' + j} cx={mm.notes[j].x} cy={mm.notes[j].y} rx="15" ry="11" fill="none" stroke={PEN_C} strokeWidth="1.8"/>)}
        {o.bracket && (() => { const a = mm.notes[o.bracket.from], x1 = a.x - 27, x2 = mm.bars[o.bracket.bar], y = Math.min(sTop, hi) - 12, yt = yOf(CLEFS[clef].high, clef) - 4;
          return <g><path d={`M${x1} ${y + 6} L${x1} ${y} L${x2} ${y} L${x2} ${yt}`} fill="none" stroke={PEN_C} strokeWidth="1.8" strokeLinejoin="round"/>
            {o.bracket.label && <text x={(x1 + x2) / 2} y={y - 6} textAnchor="middle" fontSize="13" fontWeight="900" fill={PEN_C} style={{paintOrder:'stroke',stroke:'#fff',strokeWidth:3}}>{String(o.bracket.label).split(/([♯♭♮])/).map((x, i) => /[♯♭♮]/.test(x) ? <tspan key={i} style={{fontFamily:SAC_MF,fontWeight:400}} fontSize="17">{x}</tspan> : x)}</text>}</g>; })()}
        {o.ksRing && ks.length > 0 && <rect x={ksx(0) - 11} y={kTop - 4} width={(ks.length - 1) * 15 + 22} height={kBot - kTop + 8} rx="8" fill="none" stroke={PEN_C} strokeWidth="1.8"/>}
      </g>; }}/></div>;
}
const skgX0 = (items, base, room) => base + (room ? room * 15 + 4 + (items[0] && items[0][0] === 'ts' ? 4 : items[0] && items[0][0] !== 'sp' ? 14 : 0) : 0);
const skgVbw = (items, k, o = {}, clef = 'treble') => { const ks = o.ks || skgKs(k, clef), room = o.ksRoom != null ? o.ksRoom : ks.length, x0 = skgX0(items, o.base || (clef === 'bass' ? 54 : 46), room);
  return Math.ceil(Math.max(sskRaw((d) => dY(d), sacPrep(items, o.room || 16).items, { ...o, clef, x0 }).last, x0 + 8) + 6); };
// a set of staves at one size, their clefs in line (chapter 17's way)
const skgSetBox = (list, k, ref, oOf = () => ({}), clef = 'treble') => Math.min(ref, Math.max(...list.map((it, i) => skgVbw(it, k, oOf(it, i), clef))));
// a key signature alone (a short staff), with room after it; both clefs from one origin and with one pad, so a set of
// them (treble and bass mixed) is drawn at one size with its staff lines in line
const SKG_ALONE = [['sp', 26]];
const SKG_AL = { base: 54, ksRoom: 2 }, SKG_AL_PAD = [34, 24];
// a key signature to draw or name in the Workbook: one size everywhere (about 5 mm between the lines in print)
const skgAloneW = (items, room = 2, k = 1.95) => Math.round(skgVbw(items, 'C', { base: 54, ksRoom: room, ks: [] }) * k);

// the tunes of the book's pictures (the pads on pages 2 to 5 play them)
const SKG_TUNES = {
  1: [[['ts', 4], ['q', 1, 34], ['q', 1, 33], ['q', 1, 32], ['q', 1, 31], ['|'], ['q', 1, 32], ['q', 1, 33], ['h', 2, 34], ['|']],
      [['q', 1, 36], ['q', 1, 37], ['q', 1, 38], ['q', 1, 37], ['|'], ['h', 2, 36], ['h', 2, 32], ['||']]],          // B A G F♯ | G A B; D E F♯ E | D G
  2: [['ts', 4], ['q', 1, 33], ['q', 1, 32], ['q', 1, 31], ['q', 1, 32], ['|'], ['q', 1, 38], ['q', 1, 37], ['h', 2, 36], ['||']],   // A G F♯ G | F♯ E D
  3: [32, 33, 34, 35, 36, 37, 38, 39].map(d => ['q', 1, d]).concat([['||']]),                                                 // G major
  4: [31, 32, 33, 34, 35, 36, 37, 38].map(d => ['q', 1, d]).concat([['||']]),                                                 // F major
  5: [['ts', 4], ['q', 1, 33], ['q', 1, 31, 'n'], ['q', 1, 32], ['q', 1, 31], ['|'], ['q', 1, 31], ['q', 1, 30], ['h', 2, 29], ['||']],   // A F♮ G F | F♯ E D
};
const SKG_TUNE_KEY = { 1: 'G', 2: 'G', 3: 'G', 4: 'F', 5: 'G' };
const SKG_KEYS = { 2: [31, 9], 3: [32, 8], 4: [31, 8], 5: [29, 6] };   // each page's keyboard: from d, n white keys
// page 6 and its pad: the five keys, each with its scale (from d), its keyboard
const SKG_FIVE = ['C', 'G', 'D', 'F', 'Bb'];
const SKG_SCALE_D = { C: 28, G: 32, D: 29, F: 31, Bb: 34, A: 33, Eb: 30 };
const skgScale = (key) => [0, 1, 2, 3, 4, 5, 6, 7].map(i => ['q', 1, SKG_SCALE_D[key] + i]).concat([['||']]);
const skgScaleKeys = (key) => key === 'Bb' ? [33, 9] : [SKG_SCALE_D[key], 8];

function skgLbPages(scr = false) {
  const ch = 'key-signatures';
  const live = (still, comp) => <LbLive still={still} live={comp}/>;
  const stack = (nodes, h, gap = 12, mw = 680) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap,width:'100%',maxWidth:mw,margin:'0 auto',alignItems:'stretch'}}>{nodes}</div></LbPic>;
  const X = (en, ko) => sscT(en, skgKo(ko)), T = SKG_TUNES, REF = scr ? 270 : 330;   // one staff size on every page (chapter 17's)
  const tune = (items, k, o = {}, key = 's', label) => <div key={key} style={{width:'100%'}}><SkgStaff items={items} k={k} width={REF} o={{ boxS: 26, ...o }} label={label}/></div>;
  const keys = (pg, o, label, mw = 470) => <div key="k" style={{maxWidth:mw,margin:'0 auto',width:'100%'}}><SacKeys d0={SKG_KEYS[pg][0]} n={SKG_KEYS[pg][1]} o={{ H: 150, ...o }} label={label}/></div>;
  const cap = (x) => <div style={{textAlign:'center',fontSize:scr ? 14 : 13.5,fontWeight:800,color:BK.ink,marginTop:2,lineHeight:1.35}}>{sscSx(x)}</div>;
  // a key signature alone on a short staff, a caption under it (both clefs from one origin, one pad: one size, lines in line)
  const alone = (k, clef, c, w = 150, key) => <div key={key} style={{display:'flex',flexDirection:'column',alignItems:'center'}}><div style={{width:'100%',maxWidth:w}}><SkgStaff items={SKG_ALONE} k={k} clef={clef} width={w} full pad={SKG_AL_PAD} o={{ ...SKG_AL, ksCol: PEN_C }}/></div>{c && cap(c)}</div>;
  const pair = (k, a, b, label) => <div key="pair" role="img" aria-label={label} style={{display:'grid',gridTemplateColumns:'1fr 1fr',alignItems:'start',gap:scr ? 10 : 30,maxWidth:scr ? 330 : 490,margin:'0 auto',width:'100%'}}>{alone(k, 'treble', a, scr ? 150 : 225, 't')}{alone(k, 'bass', b, scr ? 150 : 225, 'b')}</div>;
  const F = (row, k) => skgOf(row, k, n => n.byKey);

  // p1: a tune in G major on two lines of music, the key signature at the start of each; every F (in coral) is F♯.
  // On a phone one bar a line.
  const r1 = scr ? T[1].flatMap(sacBars) : T[1], o1 = { D: 27 };
  const vb1 = r1.map(row => skgVbw(row, 'G', o1)), box1 = Math.max(...vb1), ref1 = Math.max(REF, box1);
  const p1 = stack(r1.map((row, i) => sacInSet(box1 * (REF / ref1), REF, <SkgStaff items={row} k="G" width={box1} left o={{ ...o1, ksCol: PEN_C, hl: F(row, 'G') }}
    label={skgP1Label(row, i, scr)}/>, i)), scr ? undefined : 262, scr ? 6 : 10);
  // p2: one sharp on the F line: both Fs sharp
  const p2 = stack([tune(T[2], 'G', { D: 26, ksCol: PEN_C, hl: F(T[2], 'G'), ...skgUnder(T[2], 'G', null, F(T[2], 'G')) }, 's', t('Two bars on the treble staff with one sharp, on the top line, after the clef: A, G, F sharp (in the bottom space), G, then F sharp (on the top line), E, D. Both F sharps in coral.', '높은음자리표 오선의 두 마디, 음자리표 다음 맨 윗줄에 샤프 하나: A, G, F♯(맨 아래 칸), G, 그다음 F♯(맨 윗줄), E, D. 두 F♯는 산호색.')),
    keys(2, { lit: [66, 78] }, t('The keys from F to G: both F sharps in coral, an octave apart.', 'F에서 G까지의 건반: 한 옥타브 떨어진 두 F♯는 산호색.'))], 300, 16);
  // p3: G major's key signature on both staves; the scale written with it
  const pairG = pair('G', t('treble: the top line', '높은음자리표: 맨 윗줄'), t('bass: the fourth line', '낮은음자리표: 넷째 줄'), t('G major’s key signature: one sharp, on the top line of the treble staff and on the fourth line of the bass staff.', 'G장조의 조표: 샤프 하나, 높은음자리표 오선의 맨 윗줄과 낮은음자리표 오선의 넷째 줄.'));
  const p3 = stack([pairG,
    tune(T[3], 'G', { D: scr ? 27 : 30, hl: [6], ...skgUnder(T[3], 'G', null, [6]) }, 's', t('G major written with its key signature: G A B C D E F sharp G, no sign before the F; F sharp in coral.', '조표로 쓴 G장조: G A B C D E F♯ G, F 앞에는 샤프가 없어요; F♯는 산호색.'))], 380, 22);
  // p4: F major
  const pairF = pair('F', t('treble: the middle line', '높은음자리표: 가운데 줄'), t('bass: the second line', '낮은음자리표: 둘째 줄'), t('F major’s key signature: one flat, on the middle line of the treble staff and on the second line of the bass staff.', 'F장조의 조표: 플랫 하나, 높은음자리표 오선의 가운데 줄과 낮은음자리표 오선의 둘째 줄.'));
  const p4 = stack([pairF,
    tune(T[4], 'F', { D: scr ? 27 : 30, hl: [3], ...skgUnder(T[4], 'F', null, [3]) }, 's', t('F major written with its key signature: F G A B flat C D E F, no sign before the B; B flat in coral.', '조표로 쓴 F장조: F G A B♭ C D E F, B 앞에는 플랫이 없어요; B♭은 산호색.'))], 380, 22);
  // p5: a natural in G major: until the bar line, then the key signature again
  const p5 = stack([tune(T[5], 'G', { D: 25, ...SKG_P5O() }, 's', t('Two bars in G major. A coral bracket runs from a natural before F to the bar line. Under the notes: A, F, G, F (still F: the natural holds), then F sharp (in coral: the key signature again), E, D.', 'G장조의 두 마디. F 앞의 내추럴에서 세로줄까지 산호색 괄호. 음표 아래: A, F, G, F(아직 F: 내추럴이 그대로), 그다음 F♯(산호색: 다시 조표대로), E, D.')),
    keys(5, { lit: [65], pale: [66] }, t('The keys from D to B: F in coral, F sharp pale coral.', 'D에서 B까지의 건반: F는 산호색, F♯는 옅은 산호색.'), 300)], 250, 16);
  // p6: the five keys by their signs, on both staves (one size, one origin)
  const p6 = <LbPic h={380}><SkgFiveTable/></LbPic>;

  // the check icons
  const g = (x, c, s, col, y = 30) => '<text x="' + x + '" y="' + y + '" text-anchor="middle" style="font-family:' + SAC_MF + '" font-size="' + s + '" fill="' + col + '">' + c + '</text>';
  const tx = (x, c, col, s = 18, y = 28) => '<text x="' + x + '" y="' + y + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + s + '" font-weight="900" fill="' + col + '">' + c + '</text>';
  const st5 = '<g stroke="' + PEN_N + '" stroke-opacity="0.55" stroke-width="1.2">' + [8, 14, 20, 26, 32].map(y => '<line x1="6" x2="86" y1="' + y + '" y2="' + y + '"/>').join('') + '</g>';
  const ic = {
    find: [{ k: 'raw', svg: st5 + g(18, '♯', 22, PEN_C, 11.5) + '<ellipse cx="46" cy="29" rx="5.4" ry="4" fill="' + PEN_C + '"/><ellipse cx="72" cy="8" rx="5.4" ry="4" fill="' + PEN_C + '"/>' }],
    g: [{ k: 'raw', svg: tx(34, 'G', PEN_N, 22, 30) + g(60, '♯', 26, PEN_C, 30) + tx(76, 'F', PEN_C, 13, 34) }],
    f: [{ k: 'raw', svg: tx(34, 'F', PEN_N, 22, 30) + g(58, '♭', 26, PEN_C, 30) + tx(74, 'B', PEN_C, 13, 34) }],
    acc: [{ k: 'raw', svg: g(18, '♮', 24, PEN_C) + '<line x1="28" x2="58" y1="22" y2="22" stroke="' + PEN_C + '" stroke-width="2"/><line x1="62" x2="62" y1="8" y2="34" stroke="' + PEN_N + '" stroke-width="2.4"/>' + g(78, '♯', 22, PEN_N) }],
    name: [{ k: 'raw', svg: g(22, '♯♯', 22, PEN_C) + tx(52, '=', PEN_N, 16) + tx(72, 'D', PEN_N, 20) }],
  };
  const checksRows = [
    ['find', t('I can find the key signature and say which notes it changes', '조표를 찾고, 어떤 음이 바뀌는지 말할 수 있어요')],
    ['g', t('I can play G major from its key signature, every F as F♯', '조표를 보고 G장조 음계를 칠 수 있어요: F는 모두 F♯')],
    ['f', t('I can play F major from its key signature, every B as B♭', '조표를 보고 F장조 음계를 칠 수 있어요: B는 모두 B♭')],
    ['acc', t('I can say how long a key signature lasts and how long an accidental lasts', '조표와 임시표가 언제까지 효과가 있는지 말할 수 있어요')],
    ['name', t('I can name C, G, D, F and B♭ major from their key signatures', '조표를 보고 C, G, D, F, B♭장조를 말할 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? skgKo(sscNbKo(x)) : sscNbEn(x)]);
  const ch16 = bkChapterNo('scales'), ch17 = bkChapterNo('accidentals');

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <><b>조표</b>는 오선마다 맨 앞, 음자리표 바로 뒤에 적는 샤프나 플랫이에요. 곡 끝까지 그&nbsp;음을 바꿔요.</> : <>A <b>key signature</b> is the sharps or flats written just after the clef at the start of every line of music. It changes those notes for the whole piece.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('The key signature', '조표'), 2], [t('G major', 'G장조'), 3], [t('F major', 'F장조'), 4], [t('Key signature and accidental', '조표와 임시표'), 5], [sscSx(t('D major and B♭ major', 'D장조와 B♭장조')), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}<span>{n}</span></span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{sscSx(x.replace(/^I can /, ''))}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The key signature', '조표')}>
      {live(p2, <SkgPad page={2}/>)}
      <LbDefs items={[
        [t('where it sits', '자리'), X('After the clef and before the time signature, at the start of every line of music.', '오선마다 맨 앞, 음자리표 다음, 박자표 앞.')],
        [t('its line or space', '줄이나 칸'), X('Each sharp or flat sits on the line or space of the note it changes. The sharp on the top line changes F.', '샤프나 플랫은 저마다 자기가 바꾸는 음의 줄이나 칸에 있어요. 맨 윗줄의 샤프는 F를 바꿔요.')],
        [t('every octave', '모든 옥타브'), X('It changes every note of that letter: high or low, in every bar.', '이름이 같은 음을 모두 바꿔요: 높은 음도 낮은 음도, 어느 마디에서나.')],
      ]}/>
      <LbPiano steps={[
        X('Play the notes of the picture, saying the names: A G F♯ G, then F♯ E D. Both Fs are\u00a0F♯.', '이름을 말하며 그림의 음을 쳐요: A G F♯ G, 그다음 F♯ E D. F는 둘 다 F♯예요.'),
        X('Play every F♯ on the piano, from the lowest to the highest.', '피아노의 F♯를 가장 낮은 것부터 가장 높은 것까지 모두 쳐요.'),
      ]}/>
      <LbRemember>{X('A key signature changes every note of its letter, for the whole piece.', '조표는 이름이 같은 음을 곡 끝까지 모두 바꿔요.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('G major', 'G장조')}>
      {live(p3, <>{pairG}<SkgPad page={3}/></>)}
      <LbDefs items={[
        [t('G major', 'G장조'), X('Its key signature is one sharp: F♯.', '조표는 샤프 하나, F♯예요.')],
        [t('on the staff', '오선에서'), X('On the treble staff the sharp sits on the top line; on the bass staff, on the fourth line. Both are F: the F line.', '높은음자리표 오선에서는 맨 윗줄, 낮은음자리표 오선에서는 넷째 줄에 있어요. 둘 다 F 자리, F 줄이에요.')],
        [t('no sign before F', 'F 앞에 샤프 없음'), X('The scale’s F♯ (chapter ' + ch16 + ') is in the key signature, so no F needs a sharp of its own.', '음계의 F♯(' + ch16 + '챕터)가 조표에 있어서, F마다 따로 샤프를 붙이지 않아요.')],
      ]}/>
      <LbPiano steps={[
        X('Play G major with the right hand from the picture: 1 2 3, thumb under, 1 2 3 4 5. Finger 4 plays F♯.', '그림을 보며 오른손으로 G장조 음계를 쳐요: 1 2 3, 엄지 밑으로 넣기, 1 2 3 4 5. 4번 손가락으로 F♯를 쳐요.'),
        X('Left hand, an octave lower: 5 4 3 2 1, 3 over, 3 2 1. Finger 2 plays F♯.', '왼손으로 한 옥타브 아래에서 쳐요: 5 4 3 2 1, 3번 넘기기, 3 2 1. 2번 손가락으로 F♯를 쳐요.'),
      ]}/>
      <LbRemember>{X('G major’s key signature: one sharp, F♯.', 'G장조의 조표: 샤프 하나, F♯.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('F major', 'F장조')}>
      {live(p4, <>{pairF}<SkgPad page={4}/></>)}
      <LbDefs items={[
        [t('F major', 'F장조'), X('Its key signature is one flat: B♭.', '조표는 플랫 하나, B♭이에요.')],
        [t('on the staff', '오선에서'), X('On the treble staff the flat sits on the middle line; on the bass staff, on the second line. Both are B: the B line.', '높은음자리표 오선에서는 가운데 줄, 낮은음자리표 오선에서는 둘째 줄에 있어요. 둘 다 B 자리, B 줄이에요.')],
        [t('no sign before B', 'B 앞에 플랫 없음'), X('The scale’s B♭ (chapter ' + ch16 + ') is in the key signature, so no B needs a flat of its own.', '음계의 B♭(' + ch16 + '챕터)이 조표에 있어서, B마다 따로 플랫을 붙이지 않아요.')],
      ]}/>
      <LbPiano steps={[
        X('Play F major with the right hand from the picture: 1 2 3 4, thumb under, 1 2 3 4. Finger 4 plays B♭.', '그림을 보며 오른손으로 F장조 음계를 쳐요: 1 2 3 4, 엄지 밑으로 넣기, 1 2 3 4. 4번 손가락으로 B♭을 쳐요.'),
        X('Left hand, an octave lower: 5 4 3 2 1, 3 over, 3 2 1. Finger 2 plays B♭.', '왼손으로 한 옥타브 아래에서 쳐요: 5 4 3 2 1, 3번 넘기기, 3 2 1. 2번 손가락으로 B♭을 쳐요.'),
      ]}/>
      <LbRemember>{X('F major’s key signature: one flat, B♭.', 'F장조의 조표: 플랫 하나, B♭.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Key signature and accidental', '조표와 임시표')}>
      {live(p5, <SkgPad page={5}/>)}
      <LbDefs items={[
        [t('key signature', '조표'), X('Lasts the whole piece, in every octave.', '곡 끝까지, 모든 옥타브에서 효과가 있어요.')],
        [t('accidental', '임시표'), X('Lasts until the bar line, on its own line or space (chapter ' + ch17 + ').', '세로줄까지, 같은 줄이나 칸에만 효과가 있어요(' + ch17 + '챕터).')],
        [sscSx(t('natural ♮', '내추럴 ♮')), X('Cancels the key signature’s sharp or flat on its own line or space, until the bar line. After the bar line, the key signature holds again.', '같은 줄이나 칸에서 조표의 샤프나 플랫을 세로줄까지 없애요. 세로줄 다음에는 다시 조표대로예요.')],
      ]}/>
      <LbPiano steps={[
        X('Play the notes of the picture, saying the names: A F G F, then F♯ E D.', '이름을 말하며 그림의 음을 쳐요: A F G F, 그다음 F♯ E D.'),
        X('Point to the natural, then to the bar line where it stops. Play it again.', '내추럴을 가리키고, 효과가 끝나는 세로줄을 가리켜요. 다시 쳐요.'),
      ]}/>
      <LbRemember>{X('Key signature: the whole piece. Accidental: until the bar line.', '조표는 곡 끝까지, 임시표는 세로줄까지.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={<span>{sscSx(t('D major and B♭ major', 'D장조와 B♭장조'))}</span>}>
      {live(p6, <><LbPic><SkgFiveTable/></LbPic><SkgFivePad/></>)}
      <LbDefs items={[
        [t('D major', 'D장조'), X('Two sharps: F♯ and C♯, F♯ first.', '샤프 둘: F♯와 C♯, F♯가 먼저예요.')],
        [sscSx(t('B♭ major', 'B♭장조')), X('Two flats: B♭ and E♭, B♭ first.', '플랫 둘: B♭과 E♭, B♭이 먼저예요.')],
        [t('naming the key', '조 이름'), X('Count the signs. None: C major. One sharp: G. Two sharps: D. One flat: F. Two flats: B♭.', '조표를 세어요. 없으면 C장조, 샤프 하나면 G장조, 둘이면 D장조, 플랫 하나면 F장조, 둘이면 B♭장조.')],
      ]}/>
      <LbPiano steps={[
        X('Play D major with the right hand, with C major’s fingers: 1 2 3, thumb under, 1 2 3 4 5. Finger 3 plays F♯, finger 4 plays C♯.', '오른손으로 D장조 음계를 C장조와 같은 손가락으로 쳐요: 1 2 3, 엄지 밑으로 넣기, 1 2 3 4 5. 3번 손가락으로 F♯, 4번 손가락으로 C♯를 쳐요.'),
        X('Cover the names in the picture. Point to each key signature, count its signs and say its key.', '그림의 이름을 가려요. 조표를 하나씩 가리키며 개수를 세고 조 이름을 말해요.'),
      ]}/>
      <LbRemember>{X('Count the signs: none C; one sharp G, two D; one flat F, two B♭.', '조표를 세어요: 없으면 C, 샤프 하나면 G, 둘이면 D, 플랫 하나면 F, 둘이면 B♭.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, sscSx(x)])}/>} live={<FiveChecks376 storeKey="pb_five_skg_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, sscSx(x)])}/>}/>
    </LbPage>,
  ];
}
// page 1's rows described for a screen reader: each row by its own notes (on a phone a row is a bar)
const skgP1Label = (row, i, scr) => { const nm = skgRead(row, 'G').map(n => sacNameTxt(n).replace('♯', ' sharp')).join(', '), nmk = skgRead(row, 'G').map(sacNameTxt).join(', ');
  return i === 0 ? t('A tune in G major. ' + (scr ? 'Bar 1' : 'The first line of music') + ': the treble clef, the key signature (one sharp, on the top line), 4/4, then ' + nm + '; every F sharp in coral.', 'G장조 선율. ' + (scr ? '1마디' : '첫째 오선') + ': 높은음자리표, 조표(맨 윗줄의 샤프 하나), 4/4, 그다음 ' + nmk + '; F♯는 모두 산호색.')
    : t((scr ? 'Bar ' + (i + 1) : 'The next line of music') + ': the treble clef and the sharp on the top line again, then ' + nm + '.', (scr ? (i + 1) + '마디' : '다음 오선') + ': 다시 높은음자리표와 맨 윗줄의 샤프, 그다음 ' + nmk + '.'); };
// page 5's picture and pad: the natural's bracket, the names, the coral notes
const SKG_P5O = () => { const T5 = SKG_TUNES[5]; return { signHl: [1], hl: [1, 4], ...skgUnder(T5, 'G', null, [1, 3, 4]), bracket: { from: 1, bar: 0, label: t('F♮ until the bar line', 'F♮: 세로줄까지') } }; };
// page 6's picture: the five key signatures on both staves, a column a key, its name and count under it (print);
// on a phone the same in two columns of keys
function SkgFiveTable() {
  const scr = lbScreen(), W = scr ? 170 : 136, cell = (k, clef) => <div key={k + clef} style={{maxWidth:W,width:'100%',margin:'0 auto'}}><SkgStaff items={[['sp', 8]]} k={k} clef={clef} width={W} full pad={[22, 16]} o={{ ...SKG_AL, ksCol: PEN_C }}/></div>;
  const name = (k) => <div key={'n' + k} style={{textAlign:'center',fontSize:scr ? 14 : 16,fontWeight:900,color:BK.ink,lineHeight:1.3}}>{sscSx(skgKeyName(k))}<br/><span style={{fontWeight:700,color:BK.muted,fontSize:scr ? 12.5 : 13}}>{skgCountWords(k)}</span></div>;
  const label = t('Five key signatures on the treble staff (top row) and the bass staff (second row), a column a key: C major, no sharps or flats; G major, one sharp; D major, two sharps, F sharp then C sharp (the bass staff’s C sharp in the second space); F major, one flat; B flat major, two flats, B flat then E flat (the bass staff’s E flat in the third space).', '조표 다섯, 위는 높은음자리표 오선, 아래는 낮은음자리표 오선, 한 줄에 한 조: C장조, 샤프도 플랫도 없음; G장조, 샤프 하나; D장조, 샤프 둘, F♯ 다음 C♯(낮은음자리표 오선의 C♯는 둘째 칸); F장조, 플랫 하나; B♭장조, 플랫 둘, B♭ 다음 E♭(낮은음자리표 오선의 E♭은 셋째 칸).');
  if (scr) return <div role="img" aria-label={label} style={{display:'grid',gridTemplateColumns:'1fr 1fr',alignItems:'center',gap:'2px 10px',width:'100%',maxWidth:380,margin:'0 auto'}}>
    {SKG_FIVE.map(k => <React.Fragment key={k}><div style={{gridColumn:'1 / -1',textAlign:'center',fontSize:14.5,fontWeight:900,color:BK.ink,marginTop:6}}>{sscSx(skgKeyName(k))} <span style={{fontWeight:700,color:BK.muted,fontSize:13}}>· {skgCountWords(k)}</span></div>{cell(k, 'treble')}{cell(k, 'bass')}</React.Fragment>)}</div>;
  return <div role="img" aria-label={label} style={{display:'grid',gridTemplateColumns:'repeat(5,1fr)',gap:'44px 6px',width:'100%',maxWidth:700,margin:'0 auto',alignItems:'start'}}>
    {SKG_FIVE.map(k => cell(k, 'treble'))}{SKG_FIVE.map(k => cell(k, 'bass'))}{SKG_FIVE.map(name)}</div>;
}
function KeySigLessonBook() { return <>{skgLbPages(false)}</>; }
