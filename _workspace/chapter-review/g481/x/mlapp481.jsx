// ─── Phase 481: chapter 25's pads (pages 1 to 6), the screen lesson and the drill ───
const mlxMsg = (msg, bad) => <div role="status" aria-live="polite" style={{textAlign:'center',fontSize:15,fontWeight:900,color:bad ? BK.coral : BK.ink,minHeight:22,margin:'8px 0 6px',textWrap:'balance',wordBreak:'keep-all'}}>{mlxKoT(msg)}</div>;
const mlxStopBtn = (playing, onPlay, label) => chxBtn('p', playing ? t('■ Stop', '■ 멈추기') : label || t('▶ Listen', '▶ 듣기'), playing ? () => onPlay(false) : () => onPlay(true), playing);
// a chip that is off looks off
const mlxOff = (ok) => ok ? {} : { opacity: 0.3, cursor: 'default' };

// ── phrases made from a motif (the pads and the drill). A motif is a four-note shape (steps from its lowest place);
// a bar after it is a repetition, a sequence a step up or down, or a different shape. Every note stays from C to A, so
// every stem goes up and the phrase sits in one hand.
const MLX_MOTIFS = [[0, 2, 1, 3], [0, 1, 2, 0], [2, 1, 0, 1], [0, 2, 0, 1], [3, 2, 1, 0], [1, 0, 1, 2], [0, 1, 0, 2], [2, 0, 1, 0]];
const mlxBar = (shape, s) => shape.map(x => ['q', 1, s + x]);
const mlxIn = (bars) => mlxFlat(bars).every(n => n[2] >= 28 && n[2] <= 33);
const mlxShapeOf = (bar) => bar.map(n => n[2] - Math.min(...bar.map(m => m[2])));
const mlxSameShape = (a, b) => a.length === b.length && mlxShapeOf(a).join() === mlxShapeOf(b).join();
// the same ups and downs (a motif with one interval stretched still counts as the motif, so it is never a "different" bar)
const mlxSameUpDown = (a, b) => a.length === b.length && a.every((n, i) => !i || Math.sign(n[2] - a[i - 1][2]) === Math.sign(b[i][2] - b[i - 1][2]));
// the bar after `prev`: 'rep' | 'up' | 'down', or 'new' (another shape)
const mlxNext = (prev, how) => how === 'rep' ? prev.map(n => n.slice()) : how === 'up' ? prev.map(n => ['q', 1, n[2] + 1]) : how === 'down' ? prev.map(n => ['q', 1, n[2] - 1]) : null;
function mlxNewBar(notLike, near) { for (let g = 0; g < 80; g++) { const sh = pick(MLX_MOTIFS), s = near + pick([-1, 0, 1]), b = mlxBar(sh, s); if (mlxIn([b]) && !notLike.some(x => mlxSameShape(x, b) || mlxSameUpDown(x, b))) return b; } return null; }
// a four-bar phrase: the motif, two bars made from it (hows), a long last note (endD)
function mlxPhrase(hows, endD, mi, s) {
  for (let g = 0; g < 80; g++) {
    const sh = mi != null ? MLX_MOTIFS[mi] : pick(MLX_MOTIFS), st = s != null ? s : 28 + Math.floor(Math.random() * 3), b1 = mlxBar(sh, st), bars = [b1];
    hows.forEach(h => { const p = bars[bars.length - 1]; bars.push(!p ? null : h === 'new' ? mlxNewBar([b1], p[0][2]) : mlxNext(p, h)); });
    if (endD != null) bars.push([['w', 4, endD]]);
    if (bars.every(Boolean) && mlxIn(bars)) return bars;
  }
  return [mlxBar([0, 2, 1, 3], 28), mlxBar([0, 2, 1, 3], 29), mlxBar([0, 2, 1, 3], 30), [['w', 4, endD || 32]]];
}
// the line of a run of bars, drawn small: a dot where each note starts, its height its pitch; a long note holds the line
// level; mirror: upside down
function MlxLine({ bars, w = 150, h = 54, col = PEN_N, mirror, pad = 8 }) {
  const ns = mlxFlat(bars), tot = ns.reduce((a, n) => a + n[1], 0), lo = 28, hiD = 33;
  const X = (b) => pad + (b + 0.5) / tot * (w - 2 * pad), Y = (d) => { const y = (d - lo) / (hiD - lo); return mirror ? pad + y * (h - 2 * pad) : h - pad - y * (h - 2 * pad); };
  let bt = 0; const pts = ns.map(n => { const p = [X(bt), Y(n[2])]; bt += n[1]; return p; });
  bt = 0; const path = ns.flatMap(n => { const a = [[X(bt), Y(n[2])]]; if (n[1] > 1) a.push([X(bt + n[1] - 1), Y(n[2])]); bt += n[1]; return a; });
  return <svg viewBox={`0 0 ${w} ${h}`} style={{width:'100%',display:'block'}} aria-hidden="true"><polyline points={path.map(p => p.join(',')).join(' ')} fill="none" stroke={col} strokeWidth="2.2" strokeLinejoin="round" strokeLinecap="round"/>
    {pts.map((p, i) => <circle key={i} cx={p[0]} cy={p[1]} r={2.6} fill={col}/>)}</svg>;
}
// a run of bars in rows of `per` (two on a narrow screen), all at one scale; total: bar places, the ones after `bars` empty
const mlxPer = () => { try { return window.innerWidth < 480 ? 2 : 4; } catch (e) { return 4; } };
function MlxRows({ bars, total, per = 4, ts = true, tsRoom, n0, end, hl = [], lit = -1, tag, line, motifs, D = 21, label }) {
  const T = Math.max(total || 0, bars.length), out = [], tmpl = Array.from({ length: Math.min(per, T) }, () => mlxQ([28, 30, 29, 31]));
  for (let lo = 0; lo < T; lo += per) {
    const part = bars.slice(lo, lo + per), k0 = mlxCount(bars.slice(0, lo)), kn = mlxCount(part), last = lo + per >= T, empty = Math.min(per, T - lo) - part.length;
    out.push(<MlxRow key={lo} bars={part} empty={empty} ts={ts && lo === 0} tsRoom={(ts && lo > 0) || (!ts && tsRoom)} end={last ? end : false} tag={last ? tag : undefined} line={line && part.length > 0} D={D}
      n0={n0 != null ? n0 + lo : undefined} hl={hl.map(i => i - k0).filter(i => i >= 0 && i < kn)} lit={lit >= k0 && lit < k0 + kn ? lit - k0 : -1}
      motifs={motifs ? motifs.filter(([b]) => b >= lo && b < lo + per).map(([b, x, c]) => [b - lo, x, c]) : undefined} width={mlxVbw(tmpl, ts || tsRoom, D)} label={label}/>);
  }
  return <div style={{display:'flex',flexDirection:'column',gap:4}}>{out}</div>;
}

// page 1: the map: tap any part to hear it; the part sounding lit
function MlxMapPad() {
  const [sel, setSel] = useState({ kind: 'bar', i: 0 }), [playing, setPlaying] = useState(false);
  useEffect(() => () => mlxStop(), []);
  const rgQ = mlxBarRanges(MLX_TUNE);
  const barOf = (k) => rgQ.findIndex(([a, z]) => k >= a && k <= z);
  const go = (kind, i) => { mlxStop(); setSel({ kind, i }); setPlaying(true);
    const done = (k) => { if (k === -1) setPlaying(false); };
    if (kind === 'tune') mlxRun(mlxNotes(MLX_TUNE), (k) => { if (k === -1) { setPlaying(false); setSel({ kind: 'tune', i: 0 }); } else setSel({ kind: 'bar', i: barOf(k), from: 'tune' }); });
    else if (kind === 'phrase') mlxRun(mlxNotes(i ? MLX_A : MLX_Q), done);
    else if (kind === 'bar') mlxRun(mlxNotes([MLX_TUNE[i]]), done);
    else mlxRun(mlxNotes([MLX_TUNE[0]]), done, 72); };
  const stop = () => { mlxStop(); setPlaying(false); };
  const k = sel.kind, i = sel.i;
  const barTxt = (b) => ({ motif: t('the motif', '동기'), up: t('a sequence (the bar before, a step higher)', '동형 진행(앞 마디를 한 걸음 높여서)'), rep: t('a repetition (the motif again)', '반복(동기 그대로)'), rest: t('a long note; the phrase rests', '긴 음, 프레이즈가 쉬어요'), end: t('down towards the end', '끝으로 내려가요') })[MLX_ROLE[b]];
  const msg = sel.from === 'tune' ? t('Playing the tune: bar ' + (i + 1) + ', in the ' + (i < 4 ? 'question' : 'answer') + '.', '선율 전체를 듣는 중: ' + (i + 1) + '마디(' + (i < 4 ? '질문' : '대답') + ').')
    : k === 'tune' ? t('The tune: 8 bars in all, a question and an answer.', '선율 전체: 모두 8마디, 질문과 대답.')
    : k === 'phrase' ? (i ? t('The answer, bars 5 to 8: it ends on C, the tonic.', '대답(5~8마디): 으뜸음 C에서 끝나요.') : t('The question, bars 1 to 4: it rests on G.', '질문(1~4마디): G에서 쉬어요.'))
    : k === 'bar' ? t('Bar ' + (i + 1) + ': ' + barTxt(i) + '.', (i + 1) + '마디: ' + barTxt(i) + '.')
    : t('Bar 1, slowly: C E D F, the motif.', '1마디를 천천히: C E D F, 동기.');
  return (
    <div className="try-box" style={actBox} data-mlx="pad-map">
      <div style={actTitle}>{t('The map of a tune', '선율의 지도')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{mlxKoT(t('Tap any part: the tune, a phrase, a bar or the notes. Hear it.', '아무 곳이나 눌러요: 선율 전체, 프레이즈, 마디, 음. 소리가 들려요.'))}</div>
      <div style={{maxWidth:440,margin:'0 -6px'}}><MlxMapSvg scr sel={sel} onTap={go} label={t('The map of a tune: the tune and its line; the question and the answer; eight bars, the motif and its copies; bar 1’s notes.', '선율의 지도: 선율 전체와 선율선; 질문과 대답; 여덟 마디, 동기와 그 반복·동형 진행; 1마디의 음.')}/></div>
      <div style={{textAlign:'center',fontSize:13,color:BK.muted,margin:'4px 0 0',textWrap:'balance',wordBreak:'keep-all'}}>{mlxKoT(t('Here: notes make the motif, the motif makes the phrases, a question and an answer make the tune.', '여기서는 음이 모여 동기, 동기가 모여 프레이즈, 질문과 대답이 모여 선율이 돼요.'))}</div>
      {mlxMsg(msg)}
      <div style={{display:'flex',justifyContent:'center'}}><button type="button" className="ghost-btn" disabled={!playing} onClick={stop} style={{minHeight:44,...mlxOff(playing)}}>{t('■ Stop', '■ 멈추기')}</button></div>
    </div>
  );
}

// page 2: hear a tune; pick its line from three; then see the notes under the line
const mlxUd = (b) => { const ns = mlxFlat(b).map(n => n[2]); return ns.slice(1).map((d, i) => Math.sign(d - ns[i])); };
function mlxLineQuiz(prevKey) {
  for (let g = 0; g < 60; g++) {
    const bars = mlxPhrase([pick(['rep', 'up', 'down', 'new']), pick(['up', 'down', 'new'])], pick([28, 29, 30, 32])), other = mlxPhrase([pick(['up', 'down', 'new']), pick(['rep', 'up', 'down', 'new'])], pick([28, 30, 32]));
    const key = mlxKey(bars), ua = mlxUd(bars), ub = mlxUd(other);
    // the other tune's line differs from this one in at least five of its moves
    if (key === prevKey || ua.filter((x, i) => x !== ub[i]).length < 5) continue;
    const opts = shuffle([{ id: 'a', bars }, { id: 'b', bars, mirror: true }, { id: 'c', bars: other }]);
    return { bars, opts, answer: 'a', key };
  }
  return null;
}
function MlxLinePad() {
  const playRef = React.useRef(null), [q, setQ] = useState(() => mlxLineQuiz() || mlxLineQuiz()), [ans, setAns] = useState(null), [lit, setLit] = useState(-1), [playing, setPlaying] = useState(false), [score, setScore] = useState({ right: 0, tries: 0 });
  useEffect(() => () => mlxStop(), []);
  const hear = (go) => { if (!go) { mlxStop(); return; } setPlaying(true); mlxRun(mlxNotes(q.bars), (k) => { setLit(k); if (k === -1) setPlaying(false); }); };
  const choose = (id) => { if (ans) return; setAns(id); setScore(s => ({ right: s.right + (id === q.answer ? 1 : 0), tries: s.tries + 1 })); };
  const next = () => { mlxStop(); setLit(-1); setAns(null); setQ(mlxLineQuiz(q.key) || mlxLineQuiz()); setTimeout(() => { const b = playRef.current && playRef.current.querySelector('button'); if (b) b.focus(); }, 0); };
  const ok = ans === q.answer, one = mlxPer() === 2;
  return (
    <div className="try-box" style={actBox} data-mlx="pad-line">
      <div style={actTitle}>{t('Which line?', '어느 선율선일까요?')}</div>
      <div style={actNote}>{mlxKoT(t('▶ Listen plays a tune. Tap the line it makes. Then see its notes.', '▶ 듣기를 누르면 선율이 들려요. 그 선율의 선율선을 눌러요. 그다음 음을 봐요.'))}</div>
      <div ref={playRef} style={{display:'flex',justifyContent:'center',margin:'0 0 8px'}}>{mlxStopBtn(playing, hear)}</div>
      <div style={{display:'grid',gridTemplateColumns:one ? '1fr' : 'repeat(3,minmax(0,1fr))',gap:8,maxWidth:one ? 300 : undefined,margin:'0 auto'}}>{q.opts.map((o, j) => { const good = ans && o.id === q.answer, bad = ans === o.id && !ok;
        return <button key={o.id} type="button" data-mlx={'line' + j} disabled={!!ans} aria-label={t('Line ' + (j + 1), (j + 1) + '번 선율선')} onClick={() => choose(o.id)} style={{border:'1.8px solid ' + (good ? BK.green : bad ? PEN_C : 'rgba(38,41,107,0.25)'),borderRadius:10,background:'#fff',padding:'6px 4px',cursor:ans ? 'default' : 'pointer',minHeight:64}}>
          <MlxLine bars={o.bars} mirror={o.mirror} col={good ? BK.green : PEN_N}/></button>; })}</div>
      {ans && <div style={{margin:'10px auto 0',maxWidth:460}}><MlxRows bars={q.bars} per={mlxPer()} line lit={lit} label={t('The tune with its line drawn above.', '선율과 그 위의 선율선.')}/></div>}
      {mlxMsg(!ans ? t('Listen, then choose.', '듣고 골라요.') : ok ? t('Yes: the line goes where the notes go.', '맞아요: 선율선은 음이 가는 대로 가요.') : t('Not this one. Look at the notes under the line.', '이 선이 아니에요. 선 아래의 음을 봐요.'), ans && !ok)}
      <div style={{display:'flex',justifyContent:'center',gap:8,alignItems:'center'}}>{ans && chxBtn('n', t('Next tune', '다음 선율'), next, false)}{score.tries > 0 && <span style={{fontSize:13,fontWeight:800,color:BK.muted}}>{t(score.right + ' of ' + score.tries, score.tries + '개 중 ' + score.right + '개')}</span>}</div>
    </div>
  );
}

// page 3: the phrase played two ways: at one loudness, or shaped (louder to the high point, softer, a breath)
function MlxPhrasingPad() {
  const [way, setWay] = useState(null), [lit, setLit] = useState(-1);
  useEffect(() => () => mlxStop(), []);
  const n = mlxCount(MLX_Q), hi = mlxHigh(MLX_Q);
  const play = (w) => { if (way === w) { mlxStop(); return; } mlxStop(); setWay(w); mlxRun(w === 'shaped' ? mlxShaped(MLX_Q) : mlxFlatPlay(MLX_Q), (k) => { setLit(k); if (k === -1) setWay(null); }, 100); };
  const btn = (w, en, ko) => <button type="button" data-mlx={w} aria-pressed={way === w} className={'chip' + (way === w ? ' active' : '')} style={{minHeight:48,display:'flex',justifyContent:'center',alignItems:'center',fontWeight:900}} onClick={() => play(w)}>{way === w ? t('■ Stop', '■ 멈추기') : t(en, ko)}</button>;
  return (
    <div className="try-box" style={actBox} data-mlx="pad-phrasing">
      <div style={actTitle}>{t('Phrasing', '프레이징')}</div>
      <div style={actNote}>{mlxKoT(t('Hear the phrase two ways: at one loudness, and shaped.', '프레이즈를 두 가지로 들어요: 같은 세기로, 그리고 모양을 살려서.'))}</div>
      <div style={{maxWidth:520,margin:'0 auto'}}><MlxRow bars={MLX_Q} ts end={false} marks={[[0, 3]]} hair={way === 'flat' ? null : [[0, hi - 1, 'cresc'], [hi, n - 1, 'dim']]} breath={way !== 'flat'} hl={way === 'flat' ? [] : [hi]} lit={lit} width={mlxVbw(MLX_Q, true, 17)} D={17} label={t('Bars 1 to 4 under one phrase mark, with a crescendo to the high point and a diminuendo to the end, and a breath mark.', '1~4마디, 프레이즈 표시 하나, 가장 높은 음까지 크레셴도, 끝까지 디미누엔도, 숨표.')}/></div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:360,margin:'10px auto 0'}}>{btn('flat', '▶ One loudness', '▶ 같은 세기')}{btn('shaped', '▶ Shaped', '▶ 모양 살려서')}</div>
      {mlxMsg(way === 'shaped' ? t('Louder to the high point, softer to the end, then a breath.', '가장 높은 음까지 점점 세게, 끝까지 점점 여리게, 그다음 숨.') : way === 'flat' ? t('Every note the same: no shape.', '모든 음이 같은 세기: 모양이 없어요.') : t('Tap one way, then the other.', '한 가지를 듣고, 다른 것도 들어요.'))}
    </div>
  );
}

// page 4: the question, then a second phrase whose last note the student chooses (G: a question again; C: an answer)
const MLX_ENDS = [32, 28];
function MlxQaPad() {
  const [endD, setEndD] = useState(32), [lit, setLit] = useState([-1, -1]);
  useEffect(() => () => mlxStop(), []);
  const ansOf = (d) => MLX_A.slice(0, 3).concat([[['w', 4, d]]]), ans = ansOf(endD), per = mlxPer();
  const play = (j, bars) => { if (lit[j] >= 0 && !bars) { mlxStop(); return; } mlxStop(); mlxRun(mlxNotes(bars || (j ? ans : MLX_Q)), (k) => setLit(j ? [-1, k] : [k, -1])); };
  const home = endD === 28;
  const staff = (j) => <button type="button" data-mlx={j ? 'a' : 'q'} aria-label={j ? t('Play the second phrase', '둘째 프레이즈 듣기') : t('Play the question', '질문 듣기')} onClick={() => play(j)} style={{position:'relative',border:'1.5px solid ' + (lit[j] >= 0 ? PEN_C : 'rgba(38,41,107,0.18)'),borderRadius:10,background:'#fff',padding:'2px 4px 2px 22px',cursor:'pointer'}}>
    <span aria-hidden="true" style={{position:'absolute',left:7,top:8,fontSize:13,fontWeight:900,color:lit[j] >= 0 ? PEN_C : PEN_N}}>{lit[j] >= 0 ? '■' : '▶'}</span>
    <MlxRows bars={j ? ans : MLX_Q} per={per} ts={j === 0} tsRoom end={j ? undefined : false} n0={j ? 5 : 1} hl={[mlxCount(MLX_Q) - 1]} tag={j ? (home ? '.' : '?') : '?'} lit={lit[j]} label={j ? t('The second phrase, bars 5 to 8, ending on ' + mlxName(endD) + '.', '둘째 프레이즈(5~8마디), ' + mlxName(endD) + '에서 끝나요.') : t('The question, bars 1 to 4, ending on G.', '질문(1~4마디), G에서 끝나요.')}/></button>;
  return (
    <div className="try-box" style={actBox} data-mlx="pad-qa">
      <div style={actTitle}>{t('Question and answer', '질문과 대답')}</div>
      <div style={actNote}>{mlxKoT(t('Tap the question to hear it. Then choose the second phrase’s last note: which note makes it an answer?', '질문을 눌러 들어요. 그다음 둘째 프레이즈의 마지막 음을 골라요: 어느 음이 대답을 만들까요?'))}</div>
      <div style={{display:'flex',flexDirection:'column',gap:6,maxWidth:520,margin:'0 auto'}}>{staff(0)}{staff(1)}</div>
      <div role="group" aria-label={t('Last note', '마지막 음')} style={{display:'flex',gap:8,justifyContent:'center',margin:'10px 0 0'}}>{MLX_ENDS.map(d => <button key={d} type="button" data-mlx={'end' + mlxName(d)} aria-pressed={endD === d} className={'chip' + (endD === d ? ' active' : '')} style={{minWidth:56,minHeight:44,display:'flex',justifyContent:'center',alignItems:'center',fontFamily:LB_SERIF,fontWeight:900,fontSize:18}} onClick={() => { setEndD(d); play(1, ansOf(d)); }}>{mlxName(d)}</button>)}</div>
      {mlxMsg(home ? t('It ends on C, the tonic: an answer. It sounds finished.', '으뜸음 C에서 끝나요: 대답. 끝난 느낌이에요.') : t('It ends on ' + mlxName(endD) + ': another question. It sounds unfinished.', mlxName(endD) + '에서 끝나요: 또 질문. 아직 안 끝난 느낌이에요.'), false)}
    </div>
  );
}

// page 5: mark every bar where the motif comes back (as it is, or a step higher); Check. Two bars a row; each bar's
// button placed over its bar from the same layout the row is drawn with
const MLX_MOTIF_BARS = [0, 1, 2, 4, 5];
function MlxMotifPad() {
  const [on, setOn] = useState([0]), [checked, setChecked] = useState(false), [lit, setLit] = useState(-1), [playing, setPlaying] = useState(false);
  useEffect(() => () => mlxStop(), []);
  const rg = mlxBarRanges(MLX_TUNE), D = 20;
  const tog = (b) => { if (b === 0) return; setChecked(false); setOn(o => o.includes(b) ? o.filter(x => x !== b) : o.concat([b]).sort()); };
  const ok = on.slice().sort().join() === MLX_MOTIF_BARS.join();
  const hear = (go) => { if (!go) { mlxStop(); return; } setPlaying(true); mlxRun(mlxNotes(MLX_TUNE), (k) => { setLit(k); if (k === -1) setPlaying(false); }); };
  const row = (lo) => { const bars = MLX_TUNE.slice(lo, lo + 2), o = { ts: lo === 0, tsRoom: lo > 0, end: lo === 6 ? undefined : false, gap: mlxGap(D) }, its = mlxItems(bars, o), m = sskRaw((d) => dY(d), its, { D, clef: 'treble' }), w = sdyVbw(its, { D }), rgB = mlxBarRanges(bars), k0 = rg[lo][0];
    const span = (b) => { const x1 = b === 0 ? m.notes[rgB[0][0]].x - 14 : m.bars[0] + 3, x2 = b === 0 ? m.bars[0] - 3 : (m.bars[1] != null ? m.bars[1] - 3 : w - 6); return { left: (x1 / w * 100) + '%', width: ((x2 - x1) / w * 100) + '%' }; };
    return <div key={lo}>
      <div style={{position:'relative',height:46,margin:'0 0 2px'}}>{[0, 1].map(b => { const bar = b + lo, sel = on.includes(bar), wrong = checked && sel !== MLX_MOTIF_BARS.includes(bar);
        return <button key={b} type="button" data-mlx={'mb' + bar} onClick={() => tog(bar)} disabled={bar === 0} aria-pressed={sel} aria-label={t('Bar ' + (bar + 1), (bar + 1) + '마디')} style={{position:'absolute',top:0,...span(b),height:44,padding:0,borderRadius:8,border:'1.8px ' + (sel ? 'solid ' : 'dashed ') + (wrong ? PEN_C : bar === 0 ? PEN_C : PEN_N),background:sel ? (bar === 0 ? '#fbe3da' : '#fff') : 'transparent',color:wrong ? PEN_C : PEN_N,fontWeight:900,fontSize:13,cursor:bar ? 'pointer' : 'default'}}>{sel ? (bar === 0 ? t('motif', '동기') : '✓') : bar + 1}</button>; })}</div>
      <MlxRow bars={bars} ts={o.ts} tsRoom={o.tsRoom} end={o.end} hl={lo === 0 ? [0, 1, 2, 3] : []} lit={lit >= k0 && lit < k0 + mlxCount(bars) ? lit - k0 : -1} width={w} D={D} label={t('Bars ' + (lo + 1) + ' and ' + (lo + 2) + '.', (lo + 1) + '·' + (lo + 2) + '마디.')}/></div>; };
  return (
    <div className="try-box" style={actBox} data-mlx="pad-motif">
      <div style={actTitle}>{t('Find the motif', '동기 찾기')}</div>
      <div style={actNote}>{mlxKoT(t('Bar 1 is the motif. Tap every bar where it comes back, the same or a step higher. Then Check.', '1마디가 동기예요. 동기가 그대로 또는 한 걸음 높게 다시 나오는 마디를 모두 누르고, 확인을 눌러요.'))}</div>
      <div style={{display:'flex',flexDirection:'column',gap:8,maxWidth:420,margin:'0 auto'}}>{[0, 2, 4, 6].map(row)}</div>
      {mlxMsg(!checked ? t('Look for the shape: a skip up, a step down, a skip up.', '모양을 찾아요: 위로 건너뛰고, 한 걸음 아래로, 다시 위로 건너뛰어요.') : ok ? t('Bars 1, 2, 3, 5 and 6: the motif five times. ✓', '1, 2, 3, 5, 6마디: 동기가 다섯 번. ✓') : t('Look again: the same shape, the same or a step higher?', '다시 봐요: 같은 모양인가요? 그대로인가요, 한 걸음 높은가요?'), checked && !ok)}
      <div style={{display:'flex',justifyContent:'center',gap:8}}>{chxBtn('c', t('Check', '확인'), () => setChecked(true), false)}{mlxStopBtn(playing, hear)}</div>
    </div>
  );
}

// page 6: start from the motif (from D); each tap adds a bar: the same again, a step up or a step down
const MLX_SEQ0 = mlxBar([0, 2, 1, 3], 29);
const MLX_HOW_W = { rep: ['repetition', '반복'], up: ['sequence up', '올라가는 동형 진행'], down: ['sequence down', '내려가는 동형 진행'] };
function MlxSeqPad() {
  const [bars, setBars] = useState([MLX_SEQ0]), [hows, setHows] = useState([]), [lit, setLit] = useState(-1), [playing, setPlaying] = useState(false);
  useEffect(() => () => mlxStop(), []);
  const last = bars[bars.length - 1];
  const can = (h) => bars.length < 4 && mlxIn([mlxNext(last, h)]);
  const add = (h) => { if (!can(h)) return; mlxStop(); setLit(-1); const nb = mlxNext(last, h); setBars(bars.concat([nb])); setHows(hows.concat([h])); mlxRun(mlxNotes([nb]), null); };
  const reset = () => { mlxStop(); setLit(-1); setBars([MLX_SEQ0]); setHows([]); };
  const hear = (go) => { if (!go) { mlxStop(); return; } setPlaying(true); mlxRun(mlxNotes(bars), (k) => { setLit(k); if (k === -1) setPlaying(false); }); };
  const W = (h) => t(MLX_HOW_W[h][0], MLX_HOW_W[h][1]), nm = (b) => b.map(n => mlxName(n[2])).join(' ');
  return (
    <div className="try-box" style={actBox} data-mlx="pad-seq">
      <div style={actTitle}>{t('Repetition and sequence', '반복과 동형 진행')}</div>
      <div style={actNote}>{mlxKoT(t('The motif starts on D. Each button adds a bar: the same again, or the same shape a step up or down.', '동기는 D에서 시작해요. 버튼을 누를 때마다 한 마디가 더해져요: 그대로 다시, 또는 같은 모양을 한 걸음 위나 아래로.'))}</div>
      <div style={{maxWidth:520,margin:'0 auto'}}><MlxRows bars={bars} total={4} per={mlxPer()} end={false} motifs={bars.map((_, b) => [b, b === 0 ? t('motif', '동기') : { rep: '=', up: '↑', down: '↓' }[hows[b - 1]], b === 0])} lit={lit} label={t('The motif and the bars added after it; empty bars to come.', '동기와 그 뒤에 더한 마디; 남은 빈 마디.')}/></div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,maxWidth:420,margin:'8px auto 0'}}>{['rep', 'up', 'down'].map(h => <button key={h} type="button" data-mlx={'add-' + h} className="chip" disabled={!can(h)} aria-label={W(h)} style={{minHeight:56,display:'flex',justifyContent:'center',alignItems:'center',fontWeight:900,flexDirection:'column',gap:0,whiteSpace:'normal',padding:'4px 6px',lineHeight:1.15,...mlxOff(can(h))}} onClick={() => add(h)}><span style={{fontSize:17,lineHeight:1}}>{{ rep: '=', up: '↑', down: '↓' }[h]}</span><span style={{fontSize:12,textAlign:'center',wordBreak:'keep-all'}}>{mlxKoT(W(h))}</span></button>)}</div>
      {mlxMsg(bars.length === 1 ? t('The motif: ' + nm(MLX_SEQ0) + '.', '동기: ' + nm(MLX_SEQ0) + '.') : t('Bar ' + bars.length + ': ' + nm(last) + ', ' + W(hows[hows.length - 1]) + '.', bars.length + '마디: ' + nm(last) + ', ' + W(hows[hows.length - 1]) + '.'))}
      <div style={{display:'flex',justifyContent:'center',gap:8}}>{mlxStopBtn(playing, hear)}{bars.length > 1 && chxBtn('r', t('Start again', '처음부터'), reset, bars.length === 4)}</div>
    </div>
  );
}

// the end: my tune: a motif, two bars made from it, a last note; it says which way it ends
function MlxBuildPad() {
  const [mi, setMi] = useState(0), [h2, setH2] = useState('up'), [h3, setH3] = useState('up'), [endD, setEndD] = useState(28), [lit, setLit] = useState(-1), [playing, setPlaying] = useState(false);
  useEffect(() => () => mlxStop(), []);
  const s = 28, b1 = mlxBar(MLX_MOTIFS[mi], s), b2 = mlxNext(b1, h2), b3 = b2 && mlxNext(b2, h3), bars = [b1, b2, b3, [['w', 4, endD]]];
  const fits = (b) => !!b && mlxIn([b]);
  const set = (f) => { mlxStop(); setLit(-1); f(); };
  // bar 3 stays possible when bar 2 changes
  const keep3 = (nb2, cur) => fits(mlxNext(nb2, cur)) ? cur : ['up', 'rep', 'down'].find(h => fits(mlxNext(nb2, h)));
  const hear = (go) => { if (!go) { mlxStop(); return; } setPlaying(true); mlxRun(mlxShaped(bars), (k) => { setLit(k); if (k === -1) setPlaying(false); }); };
  const H = { rep: '=', up: '↑', down: '↓' };
  const chips = (name, cur, setF, okF) => <div role="group" aria-label={name} style={{display:'flex',gap:6,justifyContent:'flex-start'}}>{['rep', 'up', 'down'].map(h => <button key={h} type="button" aria-pressed={cur === h} aria-label={t(MLX_HOW_W[h][0], MLX_HOW_W[h][1])} className={'chip' + (cur === h ? ' active' : '')} disabled={!okF(h)} style={{minWidth:48,minHeight:44,display:'flex',justifyContent:'center',alignItems:'center',fontWeight:900,fontSize:17,...mlxOff(okF(h))}} onClick={() => set(() => setF(h))}>{H[h]}</button>)}</div>;
  const label = (en, ko) => <div style={{fontSize:12.5,fontWeight:900,color:BK.muted,letterSpacing:'0.04em',whiteSpace:'nowrap'}}>{mlxKoT(t(en, ko))}</div>;
  return (
    <div className="try-box" style={actBox} data-mlx="pad-build">
      <div style={actTitle}>{t('My tune', '나의 선율')}</div>
      <div style={actNote}>{mlxKoT(t('Choose a motif, what bars 2 and 3 do with it (=, ↑, ↓) and the last note. ▶ Listen plays your tune.', '동기, 2·3마디의 모양(=, ↑, ↓), 마지막 음을 차례로 골라요. ▶ 듣기를 누르면 내 선율이 들려요.'))}</div>
      <div style={{textAlign:'center',margin:'4px 0 4px'}}>{label('Motif', '동기')}</div>
      <div role="group" aria-label={t('Motif', '동기')} style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,maxWidth:300,margin:'0 auto'}}>{MLX_MOTIFS.slice(0, 4).map((sh, j) => <button key={j} type="button" aria-pressed={mi === j} className={'chip' + (mi === j ? ' active' : '')} style={{width:'100%',minHeight:44,padding:'2px 4px'}} aria-label={t('Motif ' + (j + 1), (j + 1) + '번 동기')} onClick={() => set(() => { setMi(j); setH2('up'); setH3('up'); })}><MlxLine bars={[mlxBar(sh, 28)]} w={60} h={26} pad={5} col={mi === j ? '#fff' : PEN_N}/></button>)}</div>
      <div style={{display:'grid',gridTemplateColumns:'auto auto',gap:'6px 12px',justifyContent:'center',alignItems:'center',margin:'8px auto 0'}}>
        {label('Bar 2', '2마디')}{chips(t('Bar 2', '2마디'), h2, (h) => { setH2(h); setH3(x => keep3(mlxNext(b1, h), x)); }, (h) => fits(mlxNext(b1, h)))}
        {label('Bar 3', '3마디')}{chips(t('Bar 3', '3마디'), h3, setH3, (h) => fits(b2 && mlxNext(b2, h)))}
        {label('Last note', '마지막 음')}<div role="group" aria-label={t('Last note', '마지막 음')} style={{display:'flex',gap:6,justifyContent:'flex-start'}}>{[32, 28].map(d => <button key={d} type="button" aria-pressed={endD === d} className={'chip' + (endD === d ? ' active' : '')} style={{minWidth:48,minHeight:44,display:'flex',justifyContent:'center',alignItems:'center',fontFamily:LB_SERIF,fontWeight:900,fontSize:17}} onClick={() => set(() => setEndD(d))}>{mlxName(d)}</button>)}</div></div>
      <div style={{maxWidth:520,margin:'10px auto 0'}}><MlxRows bars={bars} per={mlxPer()} line lit={lit} hl={[mlxCount(bars) - 1]} tag={endD === 28 ? '.' : '?'} label={t('My tune with its line.', '내 선율과 선율선.')}/></div>
      {mlxMsg(endD === 28 ? t('It ends on C, the tonic: it ends like an answer.', '으뜸음 C에서 끝나요: 대답처럼 끝나요.') : t('It ends on G: it ends like a question.', 'G에서 끝나요: 질문처럼 끝나요.'))}
      <div style={{display:'flex',justifyContent:'center'}}>{mlxStopBtn(playing, hear)}</div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step; my tune at the end ──
function MlxLearn({ onStart }) {
  const pages = mlxLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="melody" title={bkChapterName('melody')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="melody"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
      <Step key="mine" extra title={t('My tune', '나의 선율')} storeAs="k7"><MlxBuildPad/></Step>
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order ──
const MLX_LEVELS = [
  { n: 1, label: 'Which line?', kind: 'line', time: 14 },
  { n: 2, label: 'Where is the high point?', kind: 'high', time: 10 },
  { n: 3, label: 'Listen: which line?', kind: 'earLine', time: 22, noPrint: true },
  { n: 4, label: 'Question or answer?', kind: 'qa', time: 8 },
  { n: 5, label: 'Listen: question or answer?', kind: 'earQa', time: 18, noPrint: true },
  { n: 6, label: 'Where does the motif come back?', kind: 'back', time: 14 },
  { n: 7, label: 'Repetition or sequence?', kind: 'rs', time: 10 },
  { n: 8, label: 'The words', kind: 'word', time: 10 },
  { n: 9, label: 'Extra: what comes next?', kind: 'next', time: 16 },
];
Object.assign(LEVEL_KO, { 'Which line?': '어느 선율선일까요?', 'Where is the high point?': '가장 높은 음은 몇 마디에?', 'Listen: which line?': '듣기: 어느 선율선일까요?', 'Question or answer?': '질문일까, 대답일까?',
  'Listen: question or answer?': '듣기: 질문일까, 대답일까?', 'Where does the motif come back?': '동기는 어디서 다시 나올까요?', 'Repetition or sequence?': '반복일까, 동형 진행일까?', 'The words': '용어', 'Extra: what comes next?': '더 해 보기: 다음은 무엇일까요?' });
const MLX_WORDS = [
  ['melody', 'notes one after another, with their rhythm, that make a tune', '음이 리듬과 함께 하나씩 이어져 만드는 음악'],
  ['contour', 'the up-and-down shape of a melody', '선율이 올라가고 내려가는 모양'],
  ['high point', 'the highest note of a phrase or a tune', '선율선의 꼭대기에 있는 음'],
  ['phrasing', 'how a phrase is shaped as it is played: louder, softer, a breath', '프레이즈를 모양 있게 치는 방법: 세게, 여리게, 숨'],
  ['breath mark', 'a comma above the staff between phrases: a short lift', '프레이즈 사이 오선 위쪽의 콤마(,): 손을 잠깐 들어요'],
  ['question phrase', 'the first phrase of a pair, ending away from the tonic', '짝의 첫 프레이즈, 으뜸음이 아닌 음에서 끝나요'],
  ['answer phrase', 'the phrase after a question, ending on the tonic', '질문 뒤에 와서 으뜸음에서 끝나는 프레이즈'],
  ['motif', 'a short idea of a few notes that comes back', '다시 나오는, 몇 개의 음으로 된 짧은 조각'],
  ['sequence', 'the same shape again straight after, starting higher or lower', '같은 모양이 바로 이어서 더 높거나 낮은 음에서 다시'],
  ['repetition', 'the same music again, on the same notes', '같은 음악이 같은 음으로 다시'],
];
const MLX_WORD_KO = { melody: '선율', contour: '선율선', 'high point': '가장 높은 음', phrasing: '프레이징', 'breath mark': '숨표', 'question phrase': '질문 프레이즈', 'answer phrase': '대답 프레이즈', motif: '동기', sequence: '동형 진행', repetition: '반복' };
const MLX_RS_W = { rep: ['repetition', '반복'], up: ['sequence up', '올라가는 동형 진행'], down: ['sequence down', '내려가는 동형 진행'], new: ['a different shape', '다른 모양'] };
const mlxKey = (bars) => mlxFlat(bars).map(n => n[2]).join('');
function genMlxQuestion(lv, prev) {
  const uid = Math.random(), same = (key) => prev && prev.key === key;
  for (let g = 0; g < 80; g++) {
    if (g === 60) prev = null;   // never stuck on the no-repeat rule
    if (lv.kind === 'line' || lv.kind === 'earLine') {
      const z = mlxLineQuiz(prev && prev.key); if (!z || same(z.key)) continue;
      const opts = z.opts.map((o, j) => ({ ...o, id: 'abc'[j], ok: o.id === 'a' })), answer = opts.find(o => o.ok).id;
      return { kind: lv.kind, key: z.key, bars: z.bars, opts, answer, choices: opts.map(o => o.id), uid };
    }
    if (lv.kind === 'high') {
      const bars = mlxPhrase([pick(['up', 'down', 'new']), pick(['up', 'down', 'new', 'rep'])], pick([28, 29, 30, 32])), ns = mlxFlat(bars), top = Math.max(...ns.map(n => n[2]));
      if (ns.filter(n => n[2] === top).length !== 1) continue;
      const bar = mlxBarRanges(bars).findIndex(([a, z]) => mlxHigh(bars) >= a && mlxHigh(bars) <= z), key = 'h' + mlxKey(bars);
      if (same(key)) continue;
      return { kind: 'high', key, bars, answer: String(bar + 1), choices: ['1', '2', '3', '4'], uid };
    }
    if (lv.kind === 'qa' || lv.kind === 'earQa') {
      // bar 1 starts on C (a motif starting on its lowest note, from C), so C is heard as home; a question ends on D or G,
      // not on the note before it; an answer comes to C from D, E or G
      const ans = Math.random() < 0.5; let bars = null;
      for (let h = 0; h < 40 && !bars; h++) {
        const b = mlxPhrase([pick(['rep', 'up', 'new']), pick(['up', 'down', 'new'])], ans ? 28 : pick([29, 32]), pick([0, 1, 3, 6]), 28), ns = mlxFlat(b), pen = ns[ns.length - 2][2], end = ns[ns.length - 1][2];
        if (ns[0][2] === 28 && (ans ? [29, 30, 32].includes(pen) : pen !== end)) bars = b;
      }
      if (!bars) continue;
      const key = lv.kind + mlxKey(bars); if (same(key)) continue;
      return { kind: lv.kind, key, bars, answer: ans ? 'answer' : 'question', choices: ['question', 'answer'], uid };
    }
    if (lv.kind === 'back') {
      const at = pick([1, 2, 3]), how = pick(['rep', 'up', 'down']), b1 = mlxBar(pick(MLX_MOTIFS), 28 + Math.floor(Math.random() * 3));
      const copy = how === 'rep' ? b1.map(n => n.slice()) : mlxNext(b1, how), bars = [b1];
      for (let b = 1; b < 4; b++) bars.push(b === at ? copy : mlxNewBar([b1].concat(bars.slice(1).filter(Boolean)), (bars[b - 1] || b1)[0][2]));
      if (!bars.every(Boolean) || !mlxIn(bars) || bars.some((x, b) => b && b !== at && (mlxSameShape(x, b1) || mlxSameUpDown(x, b1)))) continue;
      const key = 'b' + mlxKey(bars); if (same(key)) continue;
      return { kind: 'back', key, bars, how, answer: String(at + 1), choices: ['2', '3', '4'], uid };
    }
    if (lv.kind === 'rs') {
      const how = pick(['rep', 'up', 'down', 'new']), b1 = mlxBar(pick(MLX_MOTIFS), 28 + Math.floor(Math.random() * 3));
      const b2 = how === 'new' ? mlxNewBar([b1], b1[0][2]) : mlxNext(b1, how), bars = [b1, b2];
      if (!b2 || !mlxIn(bars)) continue;
      const key = 'r' + mlxKey(bars); if (same(key)) continue;
      return { kind: 'rs', key, bars, answer: how, choices: ['rep', 'up', 'down', 'new'], uid };
    }
    if (lv.kind === 'word') {
      const wd = pick(MLX_WORDS), key = 'w' + wd[0]; if (same(key)) continue;
      const wrong = shuffle(MLX_WORDS.filter(x => x[0] !== wd[0])).slice(0, 3).map(x => x[0]);
      return { kind: 'word', key, w: wd, answer: wd[0], choices: shuffle([wd[0], ...wrong]), uid };
    }
    if (lv.kind === 'next') {
      const dir = pick(['up', 'down']), sh = pick(MLX_MOTIFS), mx = Math.max(...sh), st = dir === 'up' ? 28 + Math.floor(Math.random() * Math.max(1, 4 - mx)) : 30 + Math.floor(Math.random() * Math.max(1, 4 - mx)), b1 = mlxBar(sh, st), b2 = mlxNext(b1, dir), b3 = mlxNext(b2, dir);
      if (!mlxIn([b1, b2, b3])) continue;
      const other = mlxNewBar([b1], b3[0][2]), back = mlxNext(b2, dir === 'up' ? 'down' : 'up');
      if (!other) continue;
      const opts = shuffle([{ ok: true, bar: b3 }, { bar: b2.map(n => n.slice()) }, { bar: back }, { bar: other }].filter(o => mlxIn([o.bar]))).map((o, j) => ({ ...o, id: 'abcd'[j] }));
      if (opts.length < 3 || new Set(opts.map(o => mlxKey([o.bar]))).size !== opts.length) continue;
      const key = 'n' + mlxKey([b1, b2]); if (same(key)) continue;
      return { kind: 'next', key, bars: [b1, b2], dir, opts, answer: opts.find(o => o.ok).id, choices: opts.map(o => o.id), uid };
    }
  }
  // never reached (the loop drops the no-repeat rule after 60 tries)
  return { kind: 'qa', key: 'f', bars: MLX_Q, answer: 'question', choices: ['question', 'answer'], uid };
}
const mlxCheck = (q, ans) => ans != null && String(ans) === String(q.answer);
const mlxChoiceTxt = (c, q) => q.kind === 'qa' || q.kind === 'earQa' ? (c === 'question' ? t('question', '질문') : t('answer', '대답'))
  : q.kind === 'high' || q.kind === 'back' ? t('bar ' + c, c + '마디')
  : q.kind === 'rs' ? t(MLX_RS_W[c][0], MLX_RS_W[c][1])
  : q.kind === 'word' ? t(c, MLX_WORD_KO[c]) : c;
function mlxAnswerLabel(q) { return mlxKoT(mlxAnswerLabel0(q)); }
function mlxAnswerLabel0(q) {
  const nmBar = (bar) => bar.map(n => mlxName(n[2])).join(' ');
  if (q.kind === 'word') return t(q.w[0] + ' = ' + q.w[1], MLX_WORD_KO[q.w[0]] + ' = ' + q.w[2]);
  if (q.kind === 'qa' || q.kind === 'earQa') { const e = mlxName(mlxFlat(q.bars).slice(-1)[0][2]); return q.answer === 'answer' ? t('an answer (it ends on C, the tonic)', '대답(으뜸음 C에서 끝나요)') : t('a question (it ends on ' + e + ')', '질문(' + e + '에서 끝나요)'); }
  if (q.kind === 'line' || q.kind === 'earLine') return t('line ' + ('abc'.indexOf(q.answer) + 1), ('abc'.indexOf(q.answer) + 1) + '번 선율선');
  if (q.kind === 'next') return t('picture ' + ('abcd'.indexOf(q.answer) + 1) + ': ' + nmBar(q.opts.find(o => o.ok).bar), ('abcd'.indexOf(q.answer) + 1) + '번: ' + nmBar(q.opts.find(o => o.ok).bar));
  if (q.kind === 'back') { const w = q.answer === '2' ? MLX_RS_W[q.how] : { rep: ['the motif again', '동기 그대로'], up: ['the motif a step higher', '동기를 한 걸음 높여서'], down: ['the motif a step lower', '동기를 한 걸음 낮춰서'] }[q.how];
    return t('bar ' + q.answer + ' (' + w[0] + ')', q.answer + '마디(' + w[1] + ')'); }
  if (q.kind === 'high') return t('bar ' + q.answer + ' (' + mlxName(mlxFlat(q.bars)[mlxHigh(q.bars)][2]) + ')', q.answer + '마디(' + mlxName(mlxFlat(q.bars)[mlxHigh(q.bars)][2]) + ')');
  return mlxChoiceTxt(q.answer, q);
}
function MlxQuestion({ q, given, locked, onAnswer, pixel }) {
  const paper = locked && !given, isDone = !!given;
  const board = useBoard(q, given), btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const ink = pixel ? '#faf6ec' : 'var(--text)', box = { background: pixel ? '#fff' : 'transparent', borderRadius: pixel ? 0 : 8, padding: pixel ? '2px 0' : 0 };
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const ear = q.kind === 'earLine' || q.kind === 'earQa';
  const hear = () => mlxRun(mlxNotes(q.bars), null);
  useEffect(() => () => mlxStop(), [q.uid]);
  useEffect(() => { if (ear && !locked) { const tm = setTimeout(hear, 350); return () => clearTimeout(tm); } }, [q.uid]);
  const prompt = mlxKoT({ line: t('Which line is this tune?', '이 선율의 선율선은 어느 것일까요?'), earLine: t('Listen: which line is this tune?', '듣고 골라요: 이 선율의 선율선은?'),
    high: t('Which bar has the high point?', '가장 높은 음은 몇 마디에 있을까요?'), qa: t('Does this phrase end like a question or like an answer?', '이 프레이즈는 질문처럼 끝날까요, 대답처럼 끝날까요?'), earQa: t('Listen: does it end like a question or like an answer?', '듣고 골라요: 질문처럼 끝날까요, 대답처럼 끝날까요?'),
    back: t('Bar 1 is the motif. Where does it come back?', '1마디가 동기예요. 어디서 다시 나올까요?'), rs: t('What is bar 2, compared with bar 1?', '1마디와 비교하면 2마디는?'),
    word: t('Which word means this?', '이 뜻의 용어는 무엇일까요?'), next: q.dir === 'down' ? t('The motif goes down a step each bar. Which bar comes next?', '동기가 마디마다 한 걸음씩 내려가요. 다음 마디는?') : t('The motif goes up a step each bar. Which bar comes next?', '동기가 마디마다 한 걸음씩 올라가요. 다음 마디는?') }[q.kind]);
  // staves: on paper one row at one size per bar count; on screen two bars a row (the four-bar tunes)
  const D = 20, nb = q.bars ? q.bars.length : 0;
  const rows = (bars, o = {}) => <div style={box}><MlxRows bars={bars} per={paper ? 4 : 2} end={false} line={o.line} hl={o.hl || []} motifs={o.motifs} n0={paper || q.kind === 'rs' ? undefined : 1} D={D} label={o.label || t('A tune.', '선율.')}/></div>;
  let pic = null;
  if (q.kind === 'line' || q.kind === 'high' || q.kind === 'qa') pic = rows(q.bars, { hl: isDone && q.kind === 'high' ? [mlxHigh(q.bars)] : [] });
  else if (q.kind === 'back') pic = rows(q.bars, { motifs: [[0, t('motif', '동기'), true]].concat(isDone ? [[+q.answer - 1, { rep: '=', up: '↑', down: '↓' }[q.how], false]] : []) });
  else if (q.kind === 'rs') pic = rows(q.bars, { motifs: [[0, '1', false], [1, '2', false]] });
  else if (q.kind === 'next') pic = rows(q.bars, { motifs: [[0, t('motif', '동기'), true], [1, { up: '↑', down: '↓' }[q.dir], false]] });
  else if (q.kind === 'word') pic = <div style={{textAlign:'center',fontSize:pixel ? 13 : 20,fontWeight:900,color:ink,margin:'0 0 6px',textWrap:'balance',wordBreak:'keep-all'}}>“{t(q.w[1], q.w[2])}”</div>;
  else pic = <div style={{textAlign:'center',margin:'4px 0 6px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={hear}>{t('▶ Listen again', '▶ 다시 듣기')}</button>{isDone && <div style={{marginTop:8}}>{q.kind === 'earLine' ? rows(q.bars, { line: true }) : rows(q.bars, { hl: [mlxCount(q.bars) - 1] })}</div>}</div>;
  const picChoice = q.kind === 'line' || q.kind === 'earLine' || q.kind === 'next', lineQ = q.kind === 'line' || q.kind === 'earLine';
  const cols = paper && (q.kind === 'word' || q.kind === 'rs' || q.kind === 'next') ? 4 : lineQ ? (mlxPer() === 2 && !paper ? 1 : 3) : picChoice ? 2 : q.kind === 'word' || q.kind === 'rs' ? 2 : q.choices.length;
  const choiceBody = (c) => { if (lineQ) { const o = q.opts.find(x => x.id === c); return <div style={{width:'100%',maxWidth:260,background:'#fff',borderRadius:6}}><MlxLine bars={o.bars} mirror={o.mirror}/></div>; }
    if (q.kind === 'next') { const o = q.opts.find(x => x.id === c); return <div style={{width:'100%',background:'#fff',borderRadius:6}}><MlxRow bars={[o.bar]} end={false} width={mlxVbw([o.bar], false, 21)} D={21} label={o.bar.map(n => mlxName(n[2])).join(' ')}/></div>; }
    return <span style={{fontSize:pixel ? (q.kind === 'high' || q.kind === 'back' ? 15 : 11) : 16.5,fontWeight:900,wordBreak:'keep-all'}}>{mlxKoT(mlxChoiceTxt(c, q))}</span>; };
  return <div>{!paper && <BoardTrack b={board} pixel={pixel}/>}
    <p style={{fontSize:pixel ? 11.5 : 17,fontWeight:900,textAlign:'center',margin:'0 0 8px',color:ink,textWrap:'balance',wordBreak:'keep-all'}}>{prompt}</p>
    {pic && <div style={{margin:'0 auto 8px',maxWidth:paper ? (nb <= 2 ? 320 : 520) : 460}}>{pic}</div>}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,maxWidth:picChoice ? (paper && q.kind === 'next' ? 700 : 460) : undefined,margin:'0 auto'}}>{q.choices.map((c, j) => <button key={c} disabled={locked} data-mlx-choice={c} aria-label={picChoice ? t('Picture ' + (j + 1), (j + 1) + '번 그림') : undefined} onClick={() => { mlxStop(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:picChoice ? '6px' : '10px 4px',minHeight:48,display:'flex',flexDirection:'column',alignItems:'center',gap:2}}>
      {picChoice && <span style={{fontSize:pixel ? 10 : 12,fontWeight:900}}>{j + 1}</span>}{choiceBody(c)}</button>)}</div>
  </div>;
}
