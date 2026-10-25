
// ─── Chapter 5: Hand Positions (Build T, 2026-10-25; her pick: the Beginner floor's new technique room) ───
// Five fingers on five keys, one finger on each: C position, then the same shape on G; moving between them with the arm
// (chapter 1's 'the arm carries the hand'); both hands together on the same finger numbers (chapter 1's mirror twins);
// the tune passing from hand to hand. On the keys only: the staff comes in chapter 8, and Steps & skips (chapter 9) puts
// these same positions on the staff. Five-finger positions in every key wait for Tones & semitones (tone, tone, semitone,
// tone). The tunes are new and our own; one circle is one steady beat, a dashed circle holds one more (as in chapter 1).
const HP_POS = { C: { lh: [21, 22, 23, 24, 25], rh: [28, 29, 30, 31, 32] }, G: { lh: [18, 19, 20, 21, 22], rh: [32, 33, 34, 35, 36] } };   // d: white keys, 28 = middle C
const HP_LET = ['C', 'D', 'E', 'F', 'G', 'A', 'B'];
const hpLet = (d) => HP_LET[((d % 7) + 7) % 7];
const hpSemi = (d) => { const o = Math.floor((d - 28) / 7), r = ((d - 28) % 7 + 7) % 7; return 12 * o + [0, 2, 4, 5, 7, 9, 11][r]; };   // semitones from middle C
const hpKeysOf = (pos, hand) => (hand === 'L' ? HP_POS[pos].lh : HP_POS[pos].rh);
const hpFingerD = (pos, hand, f) => { const ks = hpKeysOf(pos, hand); return hand === 'L' ? ks[5 - f] : ks[f - 1]; };
const hpFingerOf = (pos, hand, d) => { const i = hpKeysOf(pos, hand).indexOf(d); return i < 0 ? null : hand === 'L' ? 5 - i : i + 1; };
// the keyboard in pen: o.hands 'LR' | 'L' | 'R'; o.lit = { d: 'cor' | 'ink' }; o.fingers false hides the circles; o.letters
// false hides the letters; o.span = [d0, d1] the keys drawn; the hands named under their keys, middle C under its key
function hpKeysRaw(pos, o = {}) {
  const hands = o.hands || 'LR', W = o.W || 24, H = o.H || 62, showF = o.fingers !== false;
  const ks = [].concat(hands.includes('L') ? HP_POS[pos].lh : [], hands.includes('R') ? HP_POS[pos].rh : []);
  const [d0, d1] = o.span || [Math.min(...ks, 28) - 1, Math.max(...ks, 28) + 1], nw = d1 - d0 + 1;
  const top = showF ? 26 : 8, x0 = 6, on = {}, fingers = {};
  ks.forEach(d => { on[d] = o.pale === false ? undefined : 'pale'; });
  Object.entries(o.lit || {}).forEach(([d, m]) => { on[d] = m; });
  if (showF) { if (hands.includes('L')) HP_POS[pos].lh.forEach((d, i) => { fingers[d] = 5 - i; }); if (hands.includes('R')) HP_POS[pos].rh.forEach((d, i) => { fingers[d] = i + 1; }); }
  let s = sskKeysRaw(x0, top, d0, nw, W, H, { on, fingers, letters: o.letters !== false });
  const kx = (d) => x0 + (d - d0 + 0.5) * W, ly = top + H + 15, txt = (x, y, str, col, fs = 11) => '<text x="' + pFix(x) + '" y="' + pFix(y) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="' + fs + '" font-weight="900" fill="' + col + '">' + penEsc(str) + '</text>';
  if (o.names !== false) {
    if (hands.includes('L')) s += txt((kx(HP_POS[pos].lh[0]) + kx(HP_POS[pos].lh[4])) / 2, ly, t('left hand', '왼손'), PEN_N);
    if (hands.includes('R')) s += txt((kx(HP_POS[pos].rh[0]) + kx(HP_POS[pos].rh[4])) / 2, ly, t('right hand', '오른손'), PEN_N);
  }
  if (o.mc !== false && 28 >= d0 && 28 <= d1) s += txt(kx(28), ly + (o.names !== false && ks.includes(28) ? 14 : 0), t('middle C', '가운데 도'), PEN_C, 10);
  return { svg: s, vb: [0, 0, x0 * 2 + nw * W, ly + (o.names !== false && ks.includes(28) ? 20 : 8)], d0, nw, W, H, top, x0 };
}
function HpKeys({ pos, label, ...o }) {
  const r = hpKeysRaw(pos, o);
  return <svg viewBox={r.vb.join(' ')} style={{width:'100%',maxWidth:o.maxW || r.vb[2] * (o.k || 1.25),display:'block',margin:'0 auto'}} role="img" aria-label={label || t(pos + ' position', pos + ' 자리')}><g dangerouslySetInnerHTML={{__html: r.svg}}/></svg>;
}
const hpMini = (pos, hands) => { const r = hpKeysRaw(pos, { hands, W: 9, H: 30, names: false, mc: false, letters: false, fingers: false }); return { shapes: [{ k: 'raw', svg: r.svg }], vb: r.vb }; };
// play a run of keys with each one lit as it sounds; returns a stop function
function hpRun(seq, setLit, gap = 430) {
  const ts = []; seq.forEach((x, i) => ts.push(setTimeout(() => { const ds = [].concat(x); setLit(ds); ds.forEach(d => playKey(hpSemi(d), 0.5)); }, i * gap)));
  ts.push(setTimeout(() => setLit([]), seq.length * gap)); return () => ts.forEach(clearTimeout);
}
const hpBtn = { padding:'10px 14px', fontSize:14, minHeight:44 };
// step 1 and 2: one position, each hand up and back, the finger lit as its key sounds
function HpPosPad({ pos }) {
  const [lit, setLit] = useState([]), stop = useRef(null);
  useEffect(() => () => stop.current && stop.current(), []);
  const go = (hand) => { stop.current && stop.current(); const ks = hpKeysOf(pos, hand); stop.current = hpRun(hand === 'R' ? ks.concat(ks.slice(0, 4).reverse()) : ks.slice().reverse().concat(ks.slice(1)), setLit); };
  const cur = lit[0], f = cur != null ? hpFingerOf(pos, HP_POS[pos].rh.includes(cur) ? 'R' : 'L', cur) : null;
  return <div className="try-box" style={{display:'flex',flexDirection:'column',gap:10}}>
    <HpKeys pos={pos} lit={Object.fromEntries(lit.map(d => [d, 'cor']))}/>
    <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:'var(--navy)',minHeight:22}}>{cur != null ? hpLet(cur) + ' · ' + t('finger ', '손가락 ') + f : t('Tap a hand to hear it go up and back.', '손을 누르면 올라갔다 내려오는 소리를 들어요.')}</div>
    <div style={{display:'flex',justifyContent:'center',gap:8,flexWrap:'wrap'}}>
      <button className="ghost-btn" style={hpBtn} onClick={() => go('L')}>▶ {t('Left hand', '왼손')} 5 4 3 2 1</button>
      <button className="ghost-btn" style={hpBtn} onClick={() => go('R')}>▶ {t('Right hand', '오른손')} 1 2 3 4 5</button>
    </div>
  </div>;
}
// step 3: C to G and back, the arm carrying the hand (lift, travel, land)
function HpMovePad() {
  const [hand, setHand] = useState('R'), [pos, setPos] = useState('C'), [lit, setLit] = useState([]), [ph, setPh] = useState(''), stop = useRef([]);
  const clear = () => { stop.current.forEach(f => f()); stop.current = []; setLit([]); setPh(''); };
  useEffect(() => clear, []);
  const span = hand === 'R' ? [27, 37] : [17, 26];
  const run = (from) => { clear(); const to = from === 'C' ? 'G' : 'C', a = hpKeysOf(from, hand), b = hpKeysOf(to, hand), up = (ks) => hand === 'R' ? ks : ks.slice().reverse();
    setPos(from); stop.current.push(hpRun(up(a), setLit, 400));
    const t1 = setTimeout(() => setPh('lift'), 2000), t2 = setTimeout(() => { setPh('travel'); setPos(to); }, 2400), t3 = setTimeout(() => setPh('land'), 2800), t4 = setTimeout(() => { setPh(''); stop.current.push(hpRun(up(b), setLit, 400)); }, 3200);
    stop.current.push(() => [t1, t2, t3, t4].forEach(clearTimeout)); };
  const W = ['lift', 'travel', 'land'], WK = { lift: '들고', travel: '옮기고', land: '내려놓기' };
  return <div className="try-box" style={{display:'flex',flexDirection:'column',gap:10}}>
    <div style={{display:'flex',justifyContent:'center',gap:6}}>{['R', 'L'].map(h => <button key={h} className={'chip' + (hand === h ? ' active' : '')} style={{minHeight:44,padding:'8px 14px'}} onClick={() => { clear(); setHand(h); }}>{h === 'R' ? t('Right hand', '오른손') : t('Left hand', '왼손')}</button>)}</div>
    <div style={{transition:'opacity .2s',opacity:ph === 'travel' ? 0.35 : 1}}><HpKeys pos={pos} hands={hand} span={span} lit={Object.fromEntries(lit.map(d => [d, 'cor']))} names={false}/></div>
    <div style={{display:'flex',justifyContent:'center',gap:14,fontSize:15,fontWeight:900}}>{W.map(w => <span key={w} style={{color:ph === w ? '#e4572e' : 'rgba(38,41,107,0.35)'}}>{t(w, WK[w])}</span>)}</div>
    <div style={{display:'flex',justifyContent:'center',gap:8,flexWrap:'wrap'}}>
      <button className="ghost-btn" style={hpBtn} onClick={() => run('C')}>▶ C → G</button>
      <button className="ghost-btn" style={hpBtn} onClick={() => run('G')}>▶ G → C</button>
    </div>
  </div>;
}
// step 4: both hands in C position, the same finger numbers together -- mirror twins, moving apart and back
function HpTogetherPad() {
  const [lit, setLit] = useState([]), stop = useRef(null);
  useEffect(() => () => stop.current && stop.current(), []);
  const pairs = [1, 2, 3, 4, 5, 4, 3, 2, 1].map(f => [hpFingerD('C', 'L', f), hpFingerD('C', 'R', f)]);
  const cur = lit.length ? hpFingerOf('C', 'R', lit[1]) : null;
  return <div className="try-box" style={{display:'flex',flexDirection:'column',gap:10}}>
    <HpKeys pos="C" lit={Object.fromEntries(lit.map(d => [d, 'cor']))}/>
    <div style={{textAlign:'center',fontSize:22,fontWeight:900,color:'var(--navy)',minHeight:30,fontFamily:"'Playfair Display', Georgia, serif"}}>{cur ? cur + ' + ' + cur : ''}</div>
    <div style={{textAlign:'center'}}><button className="ghost-btn" style={hpBtn} onClick={() => { stop.current && stop.current(); stop.current = hpRun(pairs, setLit, 600); }}>▶ 1+1 2+2 3+3 4+4 5+5</button></div>
  </div>;
}
// the tunes: one row per hand, one circle a steady beat ('-' holds one more beat, '' the other hand's turn, '|' a bar line)
function HpRows({ rows, name, how, play }) {
  // her 2026-10-25 23:04: rows were cut off on a phone, and the beat should be seen passing through the rests while it plays.
  // So: lines of two bars (the hands' rows stacked in each), and every beat lights as it passes -- a note, a held note's dashed
  // circle (it keeps sounding), or the other hand's turn (a small dot).
  const [at, setAt] = useState(-1), stop = useRef(null), scr = lbScreen();
  useEffect(() => () => stop.current && stop.current(), []);
  const seq0 = rows[0].seq, B = 520, Z = 26, multi = rows.length > 1;
  const bars = []; let cur = []; seq0.forEach((x, i) => { if (x === '|') { bars.push(cur); cur = []; } else cur.push(i); }); if (cur.length) bars.push(cur);
  const beats = bars.flat(), posAt = (r, i) => (Array.isArray(r.pos) ? r.pos[i] : r.pos);
  const go = () => { stop.current && stop.current(); const ts = [];
    beats.forEach((i, j) => ts.push(setTimeout(() => { setAt(i);
      rows.forEach(r => { const x = r.seq[i]; if (!/^[1-5]$/.test(x)) return; let hold = 1; for (let k = j + 1; k < beats.length && r.seq[beats[k]] === '-'; k++) hold++;
        playKey(hpSemi(hpFingerD(posAt(r, i), r.hand, +x)), hold * B / 1000 - 0.06); }); }, j * B)));
    ts.push(setTimeout(() => setAt(-1), beats.length * B)); stop.current = () => ts.forEach(clearTimeout); };
  const cell = (x, i) => { const on = at === i, box = { width:Z, height:Z, flex:'0 0 auto', boxSizing:'border-box', transition:'background .1s, border-color .1s' };
    if (x === '') return <span key={i} style={{...box,display:'inline-flex',alignItems:'center',justifyContent:'center'}}><span style={{width:7,height:7,borderRadius:4,background:on ? BK.coral : 'transparent'}}/></span>;
    if (x === '-') return <span key={i} style={{...box,borderRadius:Z / 2,border:'1.8px dashed ' + (on ? BK.coral : BK.line),background:on ? '#fbe3da' : 'transparent'}}/>;
    return <span key={i} style={{...box,borderRadius:Z / 2,background:on ? BK.coral : '#fff',border:'2px solid ' + (on ? BK.coral : BK.ink),display:'inline-flex',alignItems:'center',justifyContent:'center',fontSize:14,fontWeight:900,color:on ? '#fff' : BK.ink}}>{x}</span>; };
  const moves = Array.isArray(rows[0].pos), hRows = rows.length * Z + (rows.length - 1) * 6;
  const bar = (k) => <span key={'b' + k} style={{width:1.6,height:hRows,background:BK.ink,opacity:0.5,flex:'0 0 auto',alignSelf:'flex-end'}}/>;
  const lines = []; for (let k = 0; k < bars.length; k += 2) lines.push([k, bars.slice(k, k + 2)]);
  return <div style={{...VIC_PANEL,padding:'8px 14px 10px'}}>
    <div style={{display:'flex',alignItems:'baseline',gap:'2px 10px',flexWrap:'wrap'}}>
      <span style={{fontFamily:LB_SERIF,fontSize:19,fontWeight:800,color:BK.ink}}>{name}</span>
      <span style={{fontSize:12.5,color:BK.muted}}>{how}</span>
      {scr && play !== false && <button className="ghost-btn" style={{marginLeft:'auto',padding:'4px 12px',fontSize:13,minHeight:36}} onClick={go}>▶ {t('Listen', '듣기')}</button>}
    </div>
    {lines.map(([k0, ln]) => <div key={k0} style={{display:'flex',alignItems:'flex-end',gap:6,marginTop:8,flexWrap:'nowrap'}}>
      {multi && <div style={{display:'flex',flexDirection:'column',gap:6,flex:'0 0 auto'}}>{rows.map(r => <span key={r.label} style={{height:Z,display:'flex',alignItems:'center',fontSize:11,fontWeight:900,color:BK.muted,width:40}}>{r.hand === 'R' ? t('right', '오른손') : t('left', '왼손')}</span>)}</div>}
      {ln.map((b, bi) => { const k = k0 + bi, prev = k ? posAt(rows[0], bars[k - 1][0]) : null, p = posAt(rows[0], b[0]);
        return [bi > 0 ? bar(k) : null, <div key={k} style={{display:'flex',flexDirection:'column',gap:6,flex:'0 0 auto'}}>
          {moves && <span style={{height:14,fontSize:11,fontWeight:900,color:BK.coral,whiteSpace:'nowrap'}}>{k === 0 || p !== prev ? t(p + ' position', p + ' 자리') : ''}</span>}
          {rows.map(r => <div key={r.label} style={{display:'flex',gap:4}}>{b.map(i => cell(r.seq[i], i))}</div>)}
        </div>]; })}
      {bar('end' + k0)}
    </div>)}
  </div>;
}
const HP_TUNES = () => [
  { name: t('Up and down the street', '길을 따라 올라갔다 내려오기'), how: t('right hand, C position', '오른손, C 자리'),
    rows: [{ hand: 'R', pos: 'C', label: t('right C', '오른손 C'), seq: ['1', '2', '3', '4', '|', '5', '-', '-', '-', '|', '5', '4', '3', '2', '|', '1', '-', '-', '-'] }] },
  { name: t('The left hand climbs too', '왼손도 올라가요'), how: t('left hand, C position', '왼손, C 자리'),
    rows: [{ hand: 'L', pos: 'C', label: t('left C', '왼손 C'), seq: ['5', '4', '3', '2', '|', '1', '-', '-', '-', '|', '1', '2', '3', '4', '|', '5', '-', '-', '-'] }] },
  { name: t('Over to G', 'G로 건너가요'), how: t('right hand: C position, then lift, travel, land in G position', '오른손: C 자리, 들고 옮기고 내려놓아 G 자리'),
    rows: [{ hand: 'R', pos: ['C', 'C', 'C', 'C', '', 'C', 'C', 'C', 'C', '', 'G', 'G', 'G', 'G', '', 'G', 'G', 'G', 'G'], label: t('right C → G', '오른손 C → G'), seq: ['1', '3', '5', '-', '|', '5', '3', '1', '-', '|', '1', '3', '5', '-', '|', '5', '3', '1', '-'] }] },
  { name: t('Mirror twins', '거울 쌍둥이'), how: t('both hands together, C position: the same numbers', '양손 함께, C 자리: 같은 번호'),
    rows: [{ hand: 'R', pos: 'C', label: t('right C', '오른손 C'), seq: ['1', '2', '3', '2', '|', '1', '-', '-', '-'] }, { hand: 'L', pos: 'C', label: t('left C', '왼손 C'), seq: ['1', '2', '3', '2', '|', '1', '-', '-', '-'] }] },
  { name: t('Echo', '메아리'), how: t('the right hand calls, the left hand answers with the same letters, lower', '오른손이 부르고, 왼손이 같은 글자로 낮게 대답해요'),
    rows: [{ hand: 'R', pos: 'C', label: t('right C', '오른손 C'), seq: ['1', '2', '3', '-', '|', '', '', '', '', '|', '3', '4', '5', '-', '|', '', '', '', ''] },
      { hand: 'L', pos: 'C', label: t('left C', '왼손 C'), seq: ['', '', '', '', '|', '5', '4', '3', '-', '|', '', '', '', '', '|', '3', '2', '1', '-'] }] },
];
function hpLbPages(scr = false) {
  const ch = 'hand-positions';
  const checks5 = [[hpMini('C', 'R'), t('Right hand in C position, first time: thumb on middle C', '오른손 C 자리, 한 번에: 엄지는 가운데 도')], [hpMini('C', 'L'), t('Left hand in C position: little finger on the C below', '왼손 C 자리: 새끼손가락은 아래 C')],
    [hpMini('G', 'LR'), t('Each hand in G position: the same shape', '양손 각각 G 자리: 같은 모양')], [hpMini('G', 'R'), t('From C to G and back: lift, travel, land', 'C에서 G로, 다시 C로: 들고, 옮기고, 내려놓기')], [hpMini('C', 'LR'), t('Both hands together, the same numbers: mirror twins', '양손 함께, 같은 번호: 거울 쌍둥이')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  return [
    // 1. opener
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('Chapter 1 gave the hand its shape; this chapter gives it a place. Two positions, C and G, on the keys only: the staff comes in chapter ' + bkChapterNo('staff') + ', and Steps & skips (chapter ' + bkChapterNo('reading-steps') + ') reads these same positions on it. Five-finger positions in every key come with Tones & semitones.', '1장은 손에 모양을 주었고, 이 챕터는 손에 자리를 줘요. C 자리와 G 자리 두 가지를 건반에서만 익혀요. 오선은 ' + bkChapterNo('staff') + '장에서 배우고, 걸음·건너뛰기(' + bkChapterNo('reading-steps') + '장)에서 같은 자리를 오선 위에서 읽어요. 모든 조의 다섯 손가락 자리는 온음과 반음에서 해요.')}</>} qr={bkLink('drill=' + ch + '&lock=1')}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Hand Positions', '손 자리')}</div>
      </div></LbOnly>
      <LbPic h={200}><HpKeys pos="C" k={1.5} label={t('C position: both hands on the keyboard, one finger on each key, the left hand 5 4 3 2 1 on C D E F G below middle C, the right hand 1 2 3 4 5 on C D E F G from middle C', 'C 자리: 양손을 건반에, 건반 하나에 손가락 하나. 왼손 5 4 3 2 1은 가운데 도 아래 C D E F G, 오른손 1 2 3 4 5는 가운데 도부터 C D E F G')}/></LbPic>
      <LbSay size={18}>{t('Five fingers, five keys, one finger on each: that is a hand position. Learn two, C and G, and move between them.', '다섯 손가락, 건반 다섯 개, 건반 하나에 손가락 하나: 이게 손 자리예요. C 자리와 G 자리를 익히고, 그 사이를 옮겨 다녀요.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[['C position', 2], ['G position', 3], ['Move between them', 4], ['Hands together', 5], ['Taking turns', 6], ['Play: tunes in C and G', 7], ['My five checks', 8]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('put each hand in C position, first time', '양손을 각각 한 번에 C 자리에 놓을 수 있어요'), t('move the same shape to G', '같은 모양을 G로 옮길 수 있어요'), t('go from C to G and back, the arm carrying the hand', '팔이 손을 데려가서, C에서 G로 갔다 돌아올 수 있어요'), t('play both hands together on the same finger numbers', '양손이 같은 번호로 함께 칠 수 있어요'), t('pass a tune from one hand to the other', '선율을 한 손에서 다른 손으로 넘길 수 있어요')].map(x => <div key={x} style={{display:'flex',gap:9,alignItems:'flex-start',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{flex:'0 0 auto',marginTop:3}}>{bkGoal(15)}</span><span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    // 2. C position
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('C position', 'C 자리')}
      teacher={<>{t('Find middle C by its small house first, then put the thumb on it. The left hand\'s little finger lands on the next C down. Watch for two fingers squeezed onto one key, or a finger left with no key. Say: "One finger, one key."', '가운데 도를 작은 집으로 먼저 찾고, 그다음 엄지를 올려요. 왼손 새끼손가락은 그 아래 C에 내려놓아요. 손가락 둘이 한 건반에 몰리거나, 건반 없이 남는 손가락이 있는지 봐 주세요. 이렇게 말해 주세요: "손가락 하나, 건반 하나."')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={190}><HpKeys pos="C" k={1.5}/></LbPic>} live={<HpPosPad pos="C"/>}/>
      <LbSay>{LANG === 'ko' ? <>먼저 <b>가운데 도</b>를 찾아요: 피아노 한가운데 작은 집 바로 왼쪽의 C예요. <b>오른손</b>: 엄지 1번은 가운데 도, 2 3 4 5번은 D E F G. <b>왼손</b>: 새끼손가락 5번은 그 아래 C, 4 3 2 1번은 D E F G.</>
        : <>Find <b>middle C</b> first: the C just left of the small house in the middle of the piano. <b>Right hand</b>: thumb 1 on middle C, fingers 2 3 4 5 on D E F G. <b>Left hand</b>: little finger 5 on the C below, fingers 4 3 2 1 on D E F G.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 C 자리: C D E F G를 올라갔다 내려오며 손가락 번호를 말해요. <b>1 2 3 4 5 4 3 2 1</b>.</>,
        <>왼손 C 자리: C D E F G를 올라갔다 내려오며 말해요. <b>5 4 3 2 1 2 3 4 5</b>.</>,
        <>두 손을 무릎에 내렸다가, 보지 않고 한 번에 C 자리로 돌아와요. 다섯 번.</>,
      ] : [
        <>Right hand in C position: play C D E F G and back, saying the finger numbers: <b>1 2 3 4 5 4 3 2 1</b>.</>,
        <>Left hand in C position: play C D E F G and back, saying <b>5 4 3 2 1 2 3 4 5</b>.</>,
        <>Hands on your knees, then back to C position in one go, without looking twice. Five times.</>,
      ]}/>
      <LbRemember>{t('One finger, one key. Right thumb on middle C; left little finger on the C below.', '손가락 하나, 건반 하나. 오른손 엄지는 가운데 도, 왼손 새끼손가락은 아래 C.')}</LbRemember>
    </LbPage>,
    // 3. G position
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('G position', 'G 자리')}
      teacher={<>{t('The shape does not change, only the place. G is the second white key of a big house. Ask: "In G position, which finger plays C?" (right hand 4, left hand 2). The left hand sits low, a little below where it sat for C.', '모양은 그대로, 자리만 바뀌어요. G는 큰 집의 두 번째 흰 건반이에요. 물어봐 주세요: "G 자리에서 C는 몇 번 손가락?" (오른손 4번, 왼손 2번). 왼손은 C 자리보다 조금 아래, 낮은 곳에 앉아요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={190}><HpKeys pos="G" W={17} k={1.6}/></LbPic>} live={<HpPosPad pos="G"/>}/>
      <LbSay>{LANG === 'ko' ? <><b>같은 모양</b>을 <b>G</b>로 옮겨요: G A B C D. G는 큰 집의 두 번째 흰 건반이에요. <b>오른손</b>: 엄지 1번은 가운데 도 위의 G. <b>왼손</b>: 새끼손가락 5번은 낮은 G, C 자리 때보다 조금 아래예요.</>
        : <>The <b>same shape</b>, moved to <b>G</b>: G A B C D. G is the second white key of a big house. <b>Right hand</b>: thumb 1 on the G above middle C. <b>Left hand</b>: little finger 5 on a low G, a little below where it sat for C.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손 G 자리: G A B C D를 올라갔다 내려오며 음이름을 말해요.</>,
        <>왼손 G 자리: G A B C D를 올라갔다 내려오며 음이름을 말해요.</>,
        <>수수께끼: G 자리에서 C는 몇 번 손가락일까요? 오른손으로, 그다음 왼손으로 쳐 봐요.</>,
      ] : [
        <>Right hand in G position: play G A B C D and back, saying the note names.</>,
        <>Left hand in G position: play G A B C D and back, saying the note names.</>,
        <>A puzzle: in G position, which finger plays C? Play it with the right hand, then the left.</>,
      ]}/>
      <LbRemember>{t('The same shape on G: G A B C D, one finger on each.', 'G 위의 같은 모양: G A B C D, 건반 하나에 손가락 하나.')}</LbRemember>
    </LbPage>,
    // 4. move
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Move between them', '자리 옮기기')}
      teacher={<>{t('The arm carries the hand (chapter 1): the shape stays round in the air. Watch for fingers crawling along the keys to the new place, or a hand that flattens on the way. Keep the beat: one silent beat to move.', '팔이 손을 데려가요(1장): 손은 공중에서도 둥근 모양 그대로예요. 손가락이 건반을 기어서 새 자리로 가거나, 가는 길에 손이 납작해지는지 봐 주세요. 박을 지켜요: 옮기는 데 조용한 박 하나.')}</>}>
      <LbLive still={<LbPic h={190}><div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4,width:'100%'}}>
        <div style={{fontSize:13,fontWeight:900,color:BK.ink}}>{t('right hand, C position', '오른손, C 자리')}</div>
        <HpKeys pos="C" hands="R" span={[27, 37]} names={false} k={1.4}/>
        <div style={{fontFamily:LB_SERIF,fontSize:18,fontWeight:800,fontStyle:'italic',color:BK.coral}}><span style={{fontFamily:'Inter, sans-serif',fontStyle:'normal'}}>↓</span> {t('lift, travel, land', '들고, 옮기고, 내려놓기')}</div>
        <div style={{fontSize:13,fontWeight:900,color:BK.ink}}>{t('right hand, G position', '오른손, G 자리')}</div>
        <HpKeys pos="G" hands="R" span={[27, 37]} names={false} k={1.4}/>
      </div></LbPic>} live={<HpMovePad/>}/>
      <LbSay>{LANG === 'ko' ? <>자리를 옮길 때는 <b>팔이 손을 데려가요</b>: <b>들고, 옮기고, 내려놓기</b>. 손은 공중에서도 둥근 모양 그대로, 움직이는 다리처럼.</>
        : <>To move, the <b>arm carries the hand</b>: <b>lift, travel, land</b>. In the air the hand keeps its round shape, like a bridge on the move.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>오른손: C 자리에서 C D E F G, 들고 옮겨서 G 자리에 내려놓고 G A B C D.</>,
        <>다시 돌아와요: G 자리에서 C 자리로.</>,
        <>일정한 박으로: 다섯 음, 옮기는 조용한 박 하나, 다섯 음.</>,
        <>왼손도 똑같이 해요.</>,
      ] : [
        <>Right hand: C D E F G in C position, then lift, travel and land in G position: G A B C D.</>,
        <>And back again, from G to C.</>,
        <>On a steady beat: five notes, one silent beat to move, five notes.</>,
        <>The left hand the same.</>,
      ]}/>
      <LbRemember>{t('Lift, travel, land: the arm carries the hand. The shape stays the same.', '들고, 옮기고, 내려놓기: 팔이 손을 데려가요. 모양은 그대로.')}</LbRemember>
    </LbPage>,
    // 5. together
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Hands together', '양손 함께')}
      teacher={<>{t('Same numbers together moves the hands in opposite directions, so the shapes mirror each other: the easiest way to start hands together. Slow, one steady beat each, both keys exactly together.', '같은 번호를 함께 치면 두 손이 반대 방향으로 움직여서 모양이 서로 거울처럼 돼요. 양손을 시작하기에 가장 쉬운 방법이에요. 천천히, 한 박에 하나씩, 두 건반을 정확히 함께.')}</>}>
      <LbLive still={<LbPic h={190}><HpKeys pos="C" k={1.5} lit={{ 24: 'cor', 29: 'cor' }}/></LbPic>} live={<HpTogetherPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 손 모두 C 자리. <b>같은 번호를 함께</b> 쳐요: 두 엄지, 그다음 두 2번... 두 손은 <b>거울 쌍둥이</b>예요: 한 손이 올라가면 다른 손은 내려가요.</>
        : <>Both hands in C position. Play the <b>same numbers together</b>: both thumbs, then both 2s... Your hands are <b>mirror twins</b>: as one goes up, the other goes down.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>두 엄지를 함께: 왼손은 G, 오른손은 가운데 도.</>,
        <>1+1, 2+2, 3+3, 4+4, 5+5, 그리고 다시 1+1까지. 번호를 말하면서.</>,
        <>한 박에 하나씩 천천히. 두 손이 멀어졌다가 다시 가까워져요.</>,
      ] : [
        <>Both thumbs together: left hand on G, right hand on middle C.</>,
        <>1+1, 2+2, 3+3, 4+4, 5+5, and back to 1+1, saying the numbers.</>,
        <>Slowly, one steady beat each. The hands move apart, then back together.</>,
      ]}/>
      <LbRemember>{t('Same numbers together: mirror twins.', '같은 번호를 함께: 거울 쌍둥이.')}</LbRemember>
    </LbPage>,
    // 6. turns
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Taking turns', '번갈아 치기')}
      teacher={<>{t('The waiting hand stays on its keys, ready and quiet, never off in the lap. This is the first step to reading a tune that moves between the staves.', '기다리는 손은 무릎이 아니라 자기 건반 위에서 조용히 준비해요. 오선 사이를 오가는 선율을 읽는 첫걸음이에요.')}</>}>
      <HpRows {...HP_TUNES()[4]} name={t('Echo', '메아리')}/>
      <LbPic h={150}><HpKeys pos="C" k={1.4}/></LbPic>
      <LbSay>{LANG === 'ko' ? <>선율이 한 손에서 다른 손으로 넘어가요. 오른손이 부르고, 왼손이 <b>같은 글자로, 낮게</b> 대답해요. 기다리는 손은 자기 건반 위에서 준비해요.</>
        : <>The tune passes from one hand to the other. The right hand calls; the left hand answers with <b>the same letters, lower</b>. The waiting hand stays ready on its keys.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [
        <>둘 다 C 자리. 오른손 C D E, 왼손이 C D E로 대답해요.</>,
        <>오른손 E F G, 왼손 E F G. 그다음 G F E D C를 번갈아.</>,
        <>바꿔요: 왼손이 먼저 부르고, 오른손이 대답해요.</>,
      ] : [
        <>Both hands in C position. Right hand C D E; the left hand answers C D E.</>,
        <>Right hand E F G, left hand E F G. Then G F E D C, in turn.</>,
        <>Swap: the left hand calls first, the right hand answers.</>,
      ]}/>
      <LbRemember>{t('The waiting hand stays ready on its keys.', '기다리는 손은 자기 건반 위에서 준비해요.')}</LbRemember>
    </LbPage>,
    // 7. play
    <LbPage key="7" no={7} chId={ch} kicker={t('Play', '연주')} title={t('Tunes in C and G', 'C 자리·G 자리 곡')}
      teacher={<>{t('Our own tunes, by finger numbers: no staff yet. One circle is one steady beat; a dashed circle holds one more. The row says which hand and which position.', '우리가 만든 곡이에요. 손가락 번호로 쳐요: 오선은 아직이에요. 동그라미 하나가 일정한 박 하나, 점선 동그라미는 한 박 더. 줄 이름이 어느 손, 어느 자리인지 알려 줘요.')}</>}>
      <LbSay>{LANG === 'ko' ? <>손가락 번호로 쳐요. <b>동그라미 하나가 일정한 박 하나</b>, 점선 동그라미는 한 박 더 눌러요.</> : <>Play by finger numbers. <b>One circle is one steady beat</b>; a dashed circle holds one more.</>}</LbSay>
      {HP_TUNES().slice(0, 4).map(x => <HpRows key={x.name} {...x}/>)}
      <LbRemember>{t('Round hand, one finger on each key, a steady beat.', '둥근 손, 건반 하나에 손가락 하나, 일정한 박.')}</LbRemember>
    </LbPage>,
    // 8. five checks
    <LbPage key="8" no={8} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Chapter 1\'s five checks still come first at the piano. These five are this chapter\'s own: the student shows each one on the keys; you only correct.', '1장의 다섯 가지 확인이 피아노 앞에서 언제나 먼저예요. 이 다섯 가지는 이 챕터의 것이에요: 학생이 건반에서 하나씩 보여 주고, 선생님은 고쳐 주기만 해요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_hp_five"/>}/>
    </LbPage>,
  ];
}
function HandPositionsLessonBook() { return <>{hpLbPages(false)}</>; }
function HpLearn({ onStart }) {
  const pages = hpLbPages(true), opener = pages[0];
  return (
    <Lesson id="hand-positions" title={t('Hand positions', '손 자리')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="hand-positions"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={pg.props.kicker === t('Play', '연주') ? t('Play: ' + pg.props.title.charAt(0).toLowerCase() + pg.props.title.slice(1), '연주: ' + pg.props.title) : pg.props.title}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}
// ── the drill, in the book's order ──
const HP_LEVELS = [
  { n: 1, label: 'Which finger? C position', kind: 'fingerC', time: 8 },
  { n: 2, label: 'Find the key: C position', kind: 'keyC', time: 10, noPrint: true },
  { n: 3, label: 'Which finger? G position', kind: 'fingerG', time: 8 },
  { n: 4, label: 'Which hand, which position?', kind: 'which', time: 10 },
  { n: 5, label: 'Mirror twins', kind: 'mirror', time: 12 },
];
Object.assign(LEVEL_KO, { 'Which finger? C position': '몇 번 손가락? C 자리', 'Find the key: C position': '건반 찾기: C 자리', 'Which finger? G position': '몇 번 손가락? G 자리', 'Which hand, which position?': '어느 손, 어느 자리?', 'Mirror twins': '거울 쌍둥이' });
const HP_WHICH = ['C-R', 'C-L', 'G-R', 'G-L'];
function genHpQuestion(lv, prev) {
  const uid = Math.random(), hand = Math.random() < 0.5 ? 'R' : 'L';
  let f, g = 0; do { f = 1 + Math.floor(Math.random() * 5); } while (prev && prev.f === f && prev.hand === hand && g++ < 8);
  if (lv.kind === 'fingerC' || lv.kind === 'fingerG') { const pos = lv.kind === 'fingerC' ? 'C' : 'G'; return { kind: lv.kind, pos, hand, f, d: hpFingerD(pos, hand, f), answer: f, choices: [1, 2, 3, 4, 5], key: pos + hand + f, uid }; }
  if (lv.kind === 'keyC') return { kind: 'keyC', pos: 'C', hand, f, answer: hpFingerD('C', hand, f), key: 'C' + hand + f, uid };
  if (lv.kind === 'which') { let a, h = 0; do { a = pick(HP_WHICH); } while (prev && prev.answer === a && h++ < 8); const [pos, hd] = a.split('-'); return { kind: 'which', pos, hand: hd, answer: a, choices: HP_WHICH, key: a, uid }; }
  const pos = Math.random() < 0.6 ? 'C' : 'G', other = hand === 'R' ? 'L' : 'R';
  return { kind: 'mirror', pos, hand, f, given: hpFingerD(pos, hand, f), answer: hpLet(hpFingerD(pos, other, f)), choices: hpKeysOf(pos, 'R').map(hpLet), key: pos + hand + f, uid };
}
const hpWhichLabel = (a) => { const [pos, h] = a.split('-'); return (h === 'R' ? t('Right hand', '오른손') : t('Left hand', '왼손')) + ' · ' + t(pos + ' position', pos + ' 자리'); };
function hpAnswerLabel(q) {
  if (q.kind === 'fingerC' || q.kind === 'fingerG') return t('finger ' + q.answer, q.answer + '번 손가락');
  if (q.kind === 'keyC') return hpLet(q.answer) + ' (' + t('finger ', '손가락 ') + q.f + ')';
  if (q.kind === 'which') return hpWhichLabel(q.answer);
  return q.answer;
}
function HpQuestion({ q, given, locked, onAnswer, pixel }) {
  const done = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn', other = q.hand === 'R' ? 'L' : 'R';
  const cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const handW = q.hand === 'R' ? t('Right hand', '오른손') : t('Left hand', '왼손');
  const title = q.kind === 'fingerC' || q.kind === 'fingerG' ? t(handW + ', ' + q.pos + ' position: which finger plays the coral key?', handW + ' ' + q.pos + ' 자리: 산호색 건반은 몇 번 손가락일까요?')
    : q.kind === 'keyC' ? t(handW + ', C position: tap the key for finger ' + q.f + '.', handW + ' C 자리: ' + q.f + '번 손가락의 건반을 눌러요.')
    : q.kind === 'which' ? t('Which hand, and which position?', '어느 손, 어느 자리일까요?')
    : t('Both hands in ' + q.pos + ' position. The ' + (q.hand === 'R' ? 'right' : 'left') + ' hand plays finger ' + q.f + ', ' + hpLet(q.given) + '. Which key does the ' + (q.hand === 'R' ? 'left' : 'right') + ' hand\'s finger ' + q.f + ' play?', '양손 모두 ' + q.pos + ' 자리. ' + (q.hand === 'R' ? '오른손' : '왼손') + ' ' + q.f + '번이 ' + hpLet(q.given) + '를 쳐요. ' + (q.hand === 'R' ? '왼손' : '오른손') + ' ' + q.f + '번은 어느 건반일까요?');
  const ks = hpKeysOf(q.pos, q.hand), span = q.kind === 'which' ? [17, 37] : null;
  const lit = {}; if (q.kind === 'fingerC' || q.kind === 'fingerG') lit[q.d] = 'cor';
  if (q.kind === 'keyC' && done) { lit[q.answer] = 'cor'; }
  if (q.kind === 'mirror') { lit[q.given] = 'cor'; if (done) lit[hpFingerD(q.pos, other, q.f)] = 'ink'; }
  const tap = (d) => { if (locked || done) return; playKey(hpSemi(d), 0.5); onAnswer(d); };
  const kb = q.kind === 'keyC'
    ? (() => { const r = hpKeysRaw('C', { hands: q.hand, fingers: false, letters: false, names: false, lit }), d0 = r.d0, W = r.W;
        return <svg viewBox={r.vb.join(' ')} style={{width:'100%',maxWidth:r.vb[2] * 1.5,display:'block',margin:'0 auto'}} role="group" aria-label={title}>
          <g dangerouslySetInnerHTML={{__html: r.svg}}/>
          {Array.from({ length: r.nw }, (_, i) => d0 + i).map(d => <rect key={d} data-key={d} x={r.x0 + (d - d0) * W} y={r.top} width={W} height={r.H} fill="transparent" style={{cursor:'pointer'}} role="button" aria-label={hpLet(d)} onClick={() => tap(d)}/>)}
        </svg>; })()
    : q.kind === 'mirror' ? <div style={{display:'flex',flexDirection:'column',gap:4}}>{['R', 'L'].map(h => <HpKeys key={h} pos={q.pos} hands={h} letters names lit={lit} label={title}/>)}</div>
    : <HpKeys pos={q.pos} hands={q.hand} span={span} W={q.kind === 'which' ? 15 : 24} k={q.kind === 'which' ? 1.7 : 1.5} fingers={q.kind === 'which' || q.kind === 'mirror'} letters={q.kind === 'mirror'} names={q.kind === 'mirror'} lit={lit} label={title}/>;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    <div style={{marginBottom:12}}>{kb}</div>
    {q.kind !== 'keyC' && <div style={{display:'grid',gridTemplateColumns:'repeat(' + (q.kind === 'which' ? 2 : 5) + ',1fr)',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} className={cls(c)} style={{padding:pixel ? '14px 4px' : '12px 4px',fontSize:pixel ? 9 : 15}} onClick={() => onAnswer(c)}>{q.kind === 'which' ? hpWhichLabel(c) : c}</button>)}</div>}
    {done && !pixel && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{q.kind === 'which' ? t('Count the fingers: the right hand goes 1 to 5 from its thumb, the left hand 5 to 1. C position starts on a C, G position on a G.', '손가락 번호를 봐요: 오른손은 엄지부터 1에서 5, 왼손은 5에서 1. C 자리는 C에서, G 자리는 G에서 시작해요.')
      : q.kind === 'mirror' ? t('Same numbers, mirror twins: the ' + (q.hand === 'R' ? 'left' : 'right') + ' hand\'s finger ' + q.f + ' plays ' + q.answer + '.', '같은 번호, 거울 쌍둥이: ' + (q.hand === 'R' ? '왼손' : '오른손') + ' ' + q.f + '번은 ' + q.answer + '예요.')
      : t(handW + ' ' + q.pos + ' position: ' + (q.hand === 'R' ? '1 2 3 4 5 on ' : '5 4 3 2 1 on ') + hpKeysOf(q.pos, 'R').map(hpLet).join(' ') + '.', handW + ' ' + q.pos + ' 자리: ' + hpKeysOf(q.pos, 'R').map(hpLet).join(' ') + ' 위에 ' + (q.hand === 'R' ? '1 2 3 4 5' : '5 4 3 2 1') + '.')}</div>}
  </div>);
}
Object.assign(HAND_POS_DRILL, { levels: HP_LEVELS, generate: genHpQuestion, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: hpAnswerLabel, Question: HpQuestion, Learn: HpLearn });
