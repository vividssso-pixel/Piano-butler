
// ─── Chapter: The Piano’s Story, Grade 8 and Diplomas (Build DS, 2026-10-31; board call 33-2, the attic, beside The Piano’s Story) ───
// The diplomas' fifth area of general knowledge (Piano syllabus 2026, Level 3): "the construction and development of the
// instrument, with special consideration given to any implications this may have upon the repertoire that is performed".
// Every fact is in sc/research33-2-piano.md with its source; the pads' sounds are sketches of a difference, not recordings.
// Five steps, each with a thing to touch: two actions to press, a keyboard that grows, a slider through the pedals' years and
// their markings, a piano to build invention by invention (and a key to repeat), and the piano behind my own piece.

// ── step 1: Vienna and London, the two actions ──
const PS8_SW = { stroke: PEN_N, strokeWidth: 1.8, strokeLinejoin: 'round', strokeLinecap: 'round' };
// one key from the side, the player on the left; ph 0 at rest, 1 the hammer at the string, 2 fallen back while the key is held
function Ps8Action({ kind, ph = 0, w = 250, label = true }) {
  const key = ph ? -3.5 : 0, vi = kind === 'vienna';
  const strY = 34;
  // Vienna: the hammer rides on the back of the key in its fork; its head points to the player; the beak catches the rail
  // London: the hammer hangs from its own rail; the jack on the key pushes it up; its head points away from the player
  const ang = vi ? [0, 31, 12][ph] : [0, -27, -10][ph];
  const piv = vi ? [196, 80] : [128, 66];
  const head = vi ? [128, 74] : [196, 62];
  return <svg viewBox="0 0 250 132" style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={vi ? t('The Viennese action from the side: the hammer sits on the back of the key and points towards the player; when the key goes down its back end rises, the hammer’s tail catches under a rail and flicks the hammer up to the string.', '빈 액션을 옆에서: 해머가 건반 뒤쪽에 얹혀 연주자 쪽을 향해요. 건반을 누르면 뒤쪽이 올라가고, 해머 꼬리가 레일에 걸려 해머를 현으로 튕겨 올려요.') : t('The English action from the side: the hammer hangs from its own rail and points away from the player; a jack standing on the key pushes it up to the string, then slips away so the hammer falls back.', '영국 액션을 옆에서: 해머가 따로 레일에 매달려 연주자 반대쪽을 향해요. 건반 위의 잭이 해머를 현으로 밀어 올리고, 빠져나가서 해머가 되돌아와요.')}>
    <line x1="14" x2="240" y1={strY} y2={strY} stroke={PEN_N} strokeWidth="1.6"/>
    {label && <text x="236" y={strY - 6} textAnchor="end" fontSize="10.5" fontWeight="800" fill={BK.muted}>{t('string', '현')}</text>}
    <g style={{transform:'rotate(' + key + 'deg)',transformOrigin:'104px 104px',transition:'transform 0.12s ease'}}>
      <rect x="10" y="98" width="208" height="10" rx="2" fill="#fff" {...PS8_SW}/>
      {vi ? <g><rect x="188" y="84" width="16" height="14" rx="2" fill="#fff" {...PS8_SW}/></g>
        : <g><rect x="150" y="66" width="6" height="32" rx="1.5" fill={PEN_C} stroke={PEN_N} strokeWidth="1.2"/></g>}
    </g>
    <path d="M98 118 L104 108 L110 118 Z" fill={PEN_N}/>
    {vi ? <rect x="210" y="70" width="22" height="7" rx="1.5" fill={PEN_N}/> : <rect x="112" y="62" width="22" height="9" rx="2" fill={PEN_N}/>}
    <g style={{transform:'translateY(' + (vi && ph ? -3 : 0) + 'px) rotate(' + ang + 'deg)',transformOrigin:piv[0] + 'px ' + piv[1] + 'px',transition:'transform ' + (ph === 1 ? 0.09 : 0.22) + 's ease'}}>
      <line x1={piv[0]} y1={piv[1]} x2={head[0]} y2={head[1]} stroke={PEN_N} strokeWidth="2.6"/>
      {vi && <line x1={piv[0]} y1={piv[1]} x2={piv[0] + 16} y2={piv[1] - 4} stroke={PEN_N} strokeWidth="2.6"/>}
      <rect x={head[0] - 9} y={head[1] - 10} width="18" height="12" rx="5" fill={PEN_C} stroke={PEN_N} strokeWidth="1.4"/>
      <circle cx={piv[0]} cy={piv[1]} r="2.6" fill="#fff" stroke={PEN_N} strokeWidth="1.4"/>
    </g>
    {label && <><text x="14" y="128" fontSize="10.5" fontWeight="800" fill={BK.muted}>{t('← you sit here', '← 여기 앉아요')}</text>
      <text x={vi ? 221 : 123} y={vi ? 88 : 56} textAnchor="middle" fontSize="9.5" fontWeight="800" fill={BK.muted}>{t('rail', '레일')}</text>
      {!vi && <text x="166" y="92" fontSize="9.5" fontWeight="800" fill={PEN_C}>{t('jack', '잭')}</text>}</>}
  </svg>;
}
const PS8_ACT = {
  vienna: { name: ['Vienna', '빈'], who: ['Stein (Augsburg, from about 1769) and Walter (Vienna, from the early 1780s)', '슈타인(아우크스부르크, 1769년쯤부터)과 발터(빈, 1780년대 초부터)'],
    how: ['The hammer sits on the back of the key itself and points towards you. Its tail catches under a rail and the hammer flicks up.', '해머가 건반 뒤쪽에 바로 얹혀 나를 향해요. 꼬리가 레일에 걸려 해머가 튕겨 올라가요.'],
    feel: ['A light, elastic touch: the pianos of Haydn, Mozart and Beethoven. The dampers are lifted by knee levers.', '가볍고 탄력 있는 터치: 하이든, 모차르트, 베토벤의 피아노. 댐퍼는 무릎 레버로 들어요.'] },
  london: { name: ['London', '런던'], who: ['Backers (patent 1776), then Stodart and Broadwood', '배커스(1776년 특허), 그다음 스토다트와 브로드우드'],
    how: ['The hammer hangs from its own rail and points away from you. A jack on the key pushes it up, then slips away.', '해머가 따로 레일에 매달려 나와 반대쪽을 향해요. 건반 위의 잭이 밀어 올리고 빠져나가요.'],
    feel: ['Heavier and louder. Backers’ 1772 grand is probably the first piano with pedals. Your grand today comes from this family.', '더 무겁고 소리가 커요. 배커스의 1772년 그랜드가 아마 페달을 단 첫 피아노. 오늘의 그랜드는 이 집안이에요.'] },
};
// clue -> which action (the drill's level 1)
const PS8_CLUES = [
  ['vienna', 'The hammer sits on the key itself.', '해머가 건반 위에 바로 얹혀 있어요.'],
  ['london', 'The hammer hangs from its own rail; a jack pushes it up.', '해머가 따로 레일에 매달려 있고, 잭이 밀어 올려요.'],
  ['vienna', 'Stein in Augsburg, Walter in Vienna.', '아우크스부르크의 슈타인, 빈의 발터.'],
  ['london', 'Backers, Stodart and Broadwood.', '배커스, 스토다트, 브로드우드.'],
  ['vienna', 'Knee levers lift the dampers.', '무릎 레버가 댐퍼를 들어요.'],
  ['london', 'Probably the first piano with pedals (1772).', '아마 페달을 단 첫 피아노(1772년).'],
  ['vienna', '“A pleasant light elastic touch.”', '“기분 좋게 가볍고 탄력 있는 터치.”'],
  ['vienna', 'The kind of piano Mozart bought, about 1783.', '모차르트가 1783년쯤 산 바로 그 종류의 피아노.'],
  ['london', 'Chickering and Steinway perfected it, and it won the world.', '치커링과 스타인웨이가 완성해서 세계를 차지했어요.'],
  ['vienna', 'The hammer’s head points towards the player.', '해머 머리가 연주자 쪽을 향해요.'],
  ['london', 'The hammer’s head points away from the player.', '해머 머리가 연주자 반대쪽을 향해요.'],
];
// a sketch of the difference, not a recording: lighter and quicker, or fuller and louder
function ps8Hear(kind) { const ctx = getAudio(); if (!ctx) return; stopClicks(); const t0 = ctx.currentTime + 0.05;
  [60, 64, 67, 72].forEach((m, i) => blip(ctx, t0 + i * 0.28, mFreq(m), kind === 'vienna' ? 0.2 : 0.6, kind === 'vienna' ? 0.13 : 0.24, 'triangle')); }
function ActionsPad({ onResult, fixed }) {
  const [ph, setPh] = useState({ vienna: 0, london: 0 }), [quiz, setQuiz] = useState(!!fixed), [ci, setCi] = useState(fixed ? fixed.ci : 0), [ans, setAns] = useState(null);
  const press = (k) => { setPh(p => ({ ...p, [k]: 1 })); const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime + 0.03, mFreq(k === 'vienna' ? 67 : 60), k === 'vienna' ? 0.25 : 0.6, k === 'vienna' ? 0.13 : 0.24, 'triangle'); setTimeout(() => setPh(p => ({ ...p, [k]: 2 })), 160); };
  const lift = (k) => setPh(p => ({ ...p, [k]: 0 }));
  const ask = () => { let y, g = 0; do { y = Math.floor(Math.random() * PS8_CLUES.length); } while (y === ci && g++ < 10); setCi(y); setQuiz(true); setAns(null); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === PS8_CLUES[ci][0] }); };
  const col = (k) => { const A = PS8_ACT[k]; return <div key={k} style={{border:'1.5px solid ' + (quiz && ans && PS8_CLUES[ci][0] === k ? BK.green : 'rgba(38,41,107,0.3)'),borderRadius:10,padding:'8px 8px 10px',background:'#fff',minWidth:0}}>
    <div style={{fontFamily:LB_SERIF,fontSize:19,fontWeight:900,color:BK.ink,textAlign:'center'}}>{t(A.name[0], A.name[1])}</div>
    <Ps8Action kind={k} ph={ph[k]} w={230}/>
    {!quiz && <div style={{display:'flex',justifyContent:'center',marginTop:2}}><button className="ghost-btn" data-ps8-press={k} style={{...spBtn,minWidth:120}} onPointerDown={() => press(k)} onPointerUp={() => lift(k)} onPointerLeave={() => ph[k] && lift(k)} onClick={(e) => { if (e.detail === 0) { press(k); setTimeout(() => lift(k), 600); } }}>{t('Hold the key', '건반 누르기')}</button></div>}
    {(!quiz || ans) && <div style={{fontSize:13,color:BK.ink,lineHeight:1.45,marginTop:6}}><b>{t(A.who[0], A.who[1])}.</b> {t(A.how[0], A.how[1])} {t(A.feel[0], A.feel[1])}</div>}
    {quiz && !ans && <button className="choice-btn" data-ps8-act={k} onClick={() => say(k)} style={{width:'100%',marginTop:6,padding:'10px 4px',fontSize:15,fontWeight:900}}>{t(A.name[0], A.name[1])}</button>}
  </div>; };
  return (
    <div className="try-box" style={actBox} data-pm="actions">
      <div style={actTitle}>{t('Vienna and London: two ways to throw a hammer', '빈과 런던: 해머를 던지는 두 가지 방법')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>모차르트 시대에는 피아노 <b>액션</b>(건반이 해머를 움직이는 장치)이 두 집안이었어요. 건반을 꾹 눌러 보세요: 해머가 현을 치고 <b>바로 떨어져요</b>. 해머 머리가 어느 쪽을 보는지 비교해요.</> : <>In Mozart’s time the piano’s <b>action</b> (the machine between key and hammer) came in two families. Hold each key down: the hammer hits the string and <b>falls straight back</b>. Compare which way each hammer’s head points.</>}</div>
      {quiz && <div style={{textAlign:'center',margin:'4px auto 8px',maxWidth:420,padding:'12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff',fontSize:15,fontWeight:800,color:BK.ink,lineHeight:1.4}}>{t(PS8_CLUES[ci][1], PS8_CLUES[ci][2])}</div>}
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(220px,1fr))',gap:8}}>{col('vienna')}{col('london')}</div>
      {spMsg(ans ? (ans === PS8_CLUES[ci][0] ? t('Yes: ' + PS8_ACT[ans].name[0] + '.', '맞아요: ' + PS8_ACT[ans].name[1] + '.') : t('It is ' + PS8_ACT[PS8_CLUES[ci][0]].name[0] + '.', '정답은 ' + PS8_ACT[PS8_CLUES[ci][0]].name[1] + '.')) : quiz ? t('Vienna or London?', '빈일까요, 런던일까요?') : '', ans ? (ans === PS8_CLUES[ci][0] ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!quiz && <><button className="ghost-btn" style={spBtn} onClick={() => ps8Hear('vienna')}>{t('♪ Lighter, quicker', '♪ 더 가볍고 빠르게')}</button><button className="ghost-btn" style={spBtn} onClick={() => ps8Hear('london')}>{t('♪ Fuller, louder', '♪ 더 풍성하고 크게')}</button></>}
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Vienna or London?', '▶ 빈? 런던?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
      {!quiz && <div style={{fontSize:12,color:BK.muted,textAlign:'center',marginTop:6}}>{t('The two sounds are a sketch of the difference, not recordings of old pianos.', '두 소리는 차이를 보여 주는 스케치예요. 옛 피아노의 녹음이 아니에요.')}</div>}
    </div>
  );
}

// ── step 2: the keyboard grows ──
// [id, lowest MIDI, highest MIDI, name, the source's words: who played it]
const PS8_COMPASS = [
  ['five', 29, 89, ['Five octaves, to about 1790', '5옥타브, 1790년쯤까지'], ['Mozart all his life; Haydn; Beethoven until 1803', '모차르트는 평생; 하이든; 베토벤은 1803년까지']],
  ['erard', 29, 96, ['Érard’s grand, 1803', '에라르의 그랜드, 1803년'], ['Beethoven’s Érard: his Op. 53 to Op. 81a', '베토벤의 에라르: 작품 53부터 81a까지']],
  ['broadwood', 24, 96, ['English grands, 1808–1820', '영국 그랜드, 1808–1820년'], ['Broadwood: Beethoven’s English grand', '브로드우드: 베토벤의 영국 그랜드']],
  ['graf', 24, 101, ['Graf and others, about 1816–1840', '그라프 등, 1816–1840년쯤'], ['Beethoven from Op. 101 (1816)', '베토벤, 작품 101(1816년)부터']],
  ['mid', 21, 105, ['About 1850', '1850년쯤'], ['Seven octaves', '7옥타브']],
  ['today', 21, 108, ['Today', '오늘날'], ['88 keys: the piano you play', '88건반: 지금 여러분이 치는 피아노']],
];
const ps8Keys = (c) => c[2] - c[1] + 1;
const ps8NoteName = (m) => sprLetter(m).replace('#', '♯') + (Math.floor(m / 12) - 1);
const ps8Comp = (id) => PS8_COMPASS.find(c => c[0] === id);
// the first keyboard in the list (oldest first) that has this note
const ps8FirstWith = (m) => PS8_COMPASS.find(c => m >= c[1] && m <= c[2]);
function Ps8Ladder({ sel, mark, kw = 8.6, rows = true }) {
  const x0 = 24, W = 52 * kw + 30, top = mark != null ? kw * 2.6 : (sel ? 12 : 6), kh = 40, rowH = 15, H = top + kh + 10 + (rows ? PS8_COMPASS.length * rowH : 0) + 6;
  const c = sel ? ps8Comp(sel) : null, ca = c ? sprKeyX(c[1], x0, kw) - kw / 2 : 0, cb = c ? sprKeyX(c[2], x0, kw) + kw / 2 : 0;
  return <svg viewBox={'0 0 ' + W + ' ' + H} style={{width:'100%',display:'block'}} role="img" aria-label={t('An 88-key keyboard; under it a bar for each keyboard in history, from the five octaves of Mozart’s time to the 88 keys of today, each bar as wide as that keyboard.', '88건반. 그 아래 역사 속 건반마다 막대: 모차르트 시대의 5옥타브부터 오늘의 88건반까지, 막대마다 그 건반의 폭.')}>
    <SprKeys88 x0={x0} y0={top} kw={kw} h={kh} middleC={false} key1={mark != null ? mark : undefined} sw={0.6}/>
    {c && <><rect x={ca} y={top} width={cb - ca} height={kh} fill="rgba(228,87,46,0.2)" stroke={PEN_C} strokeWidth="1.6"/>{mark == null && <path d={'M' + ca + ' ' + (top - 2) + ' V' + (top - 7) + ' H' + cb + ' V' + (top - 2)} fill="none" stroke={PEN_C} strokeWidth="1.8"/>}</>}
    {rows && PS8_COMPASS.map((r, i) => { const y = top + kh + 10 + i * rowH, xa = sprKeyX(r[1], x0, kw) - kw / 2, xb = sprKeyX(r[2], x0, kw) + kw / 2, on = sel === r[0] || (mark != null && mark >= r[1] && mark <= r[2]);
      return <g key={r[0]}><rect x={xa} y={y} width={xb - xa} height={9} rx="4.5" fill={on ? PEN_C : '#fff'} stroke={on ? PEN_C : PEN_N} strokeWidth="1.2"/>
        <text x={xa - 3} y={y + 8} textAnchor="end" fontSize="8.5" fontWeight="900" fill={on ? PEN_C : BK.muted}>{ps8Keys(r)}</text></g>; })}
  </svg>;
}
function CompassPad({ onResult, fixed }) {
  const [sel, setSel] = useState('five'), [quiz, setQuiz] = useState(!!fixed), [m, setM] = useState(fixed ? fixed.m : 96), [ans, setAns] = useState(null);
  const c = ps8Comp(sel), right = ps8FirstWith(m);
  const ask = () => { const pool = []; for (let x = 21; x <= 108; x++) if (x < 29 || x > 89) pool.push(x); let y, g = 0; do { y = pick(pool); } while (y === m && g++ < 10); setM(y); setQuiz(true); setAns(null); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === right[0] }); };
  return (
    <div className="try-box" style={actBox} data-pm="compass">
      <div style={actTitle}>{t('The keyboard grows', '자라나는 건반')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>모차르트의 피아노는 <b>61건반</b>, 베토벤은 평생 동안 점점 넓어진 피아노를 받았고, 88건반은 훨씬 나중이에요. 건반을 눌러 그 피아노가 닿는 곳을 봐요: 내 곡의 가장 높은 음과 낮은 음은 어디에 있나요?</> : <>Mozart’s piano had <b>61 keys</b>; Beethoven got wider and wider pianos all his life; 88 keys came much later. Tap a keyboard and see how far it reaches: where do your piece’s highest and lowest notes sit?</>}</div>
      {!quiz && <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{PS8_COMPASS.map(r => <button key={r[0]} data-ps8-comp={r[0]} className={'chip' + (sel === r[0] ? ' active' : '')} aria-pressed={sel === r[0]} style={{minHeight:38,padding:'5px 10px'}} onClick={() => setSel(r[0])}>{t(r[3][0], r[3][1])}</button>)}</div>}
      <Ps8Ladder sel={quiz ? (ans ? right[0] : null) : sel} mark={quiz ? m : null}/>
      {!quiz && <div style={{margin:'8px auto 0',maxWidth:460,padding:'10px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff'}}>
        <div style={{fontSize:15,fontWeight:900,color:BK.ink}}>{t(c[3][0], c[3][1])}: {ps8NoteName(c[1])}–{ps8NoteName(c[2])}, {t(ps8Keys(c) + ' keys', ps8Keys(c) + '건반')}</div>
        <div style={{fontSize:13.5,color:BK.coral,fontWeight:800,marginTop:3}}>{t(c[4][0], c[4][1])}</div>
      </div>}
      {quiz && <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'8px 0 4px'}}>{t('Your piece has a ' + ps8NoteName(m) + '. Which is the first keyboard here that has it?', '내 곡에 ' + ps8NoteName(m) + '이 나와요. 이 음이 있는 가장 이른 건반은?')}</div>}
      {quiz && !ans && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6}}>{PS8_COMPASS.map(r => <button key={r[0]} data-ps8-first={r[0]} className="choice-btn" onClick={() => say(r[0])} style={{padding:'9px 4px',fontSize:13.5,fontWeight:900}}>{t(r[3][0], r[3][1])}</button>)}</div>}
      {spMsg(ans ? (ans === right[0] ? t('Yes: ' + right[3][0] + '. Before it, that key was not there.', '맞아요: ' + right[3][1] + '. 그 전에는 그 건반이 없었어요.') : t('It is ' + right[3][0] + ' (' + right[4][0] + ').', '정답은 ' + right[3][1] + '(' + right[4][1] + ').')) : '', ans ? (ans === right[0] ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Could it play this?', '▶ 이 음을 칠 수 있었을까?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}

// ── step 3: the pedals' story, and the markings ──
// [year, who, what, controls on the drawing]
const PS8_PSTOPS = [
  ['1720s', ['Cristofori', '크리스토포리'], ['A hand stop beside the keys shifts the whole action: the hammers strike one string instead of two. The first una corda.', '건반 옆의 손잡이가 액션 전체를 옮겨서 해머가 현 두 줄 대신 한 줄만 쳐요. 최초의 우나 코르다.'], { hand: 1 }],
  ['1765', ['Germany', '독일'], ['A knee lever takes the hand stop’s place for the dampers: your knee pushes up and every damper lifts.', '댐퍼를 드는 손잡이 대신 무릎 레버가 들어와요: 무릎으로 밀어 올리면 댐퍼가 모두 들려요.'], { knee: 1 }],
  ['1767', ['Zumpe, London', '춤페, 런던'], ['Two hand stops lift the dampers: one for the bass, one for the treble. You stop playing to pull them.', '손잡이 두 개가 댐퍼를 들어요: 하나는 저음, 하나는 고음. 당기려면 연주를 멈춰야 해요.'], { hand: 2 }],
  ['1772', ['Backers, London', '배커스, 런던'], ['Probably the first piano with pedals instead of knee levers.', '아마 무릎 레버 대신 페달을 단 첫 피아노.'], { ped: 2 }],
  ['1782–85', ['Mozart’s Walter, Vienna', '모차르트의 발터, 빈'], ['Two knee levers lift the dampers, and a moderator stop slides a strip of cloth between hammers and strings.', '무릎 레버 두 개가 댐퍼를 들고, 모데라토르 손잡이가 해머와 현 사이에 천 조각을 끼워요.'], { knee: 2, hand: 1 }],
  ['1814', ['Streicher, Vienna', '슈트라이허, 빈'], ['Knee levers and pedals both. After 1810 pedals take over from knee levers.', '무릎 레버와 페달이 둘 다. 1810년 뒤로는 페달이 무릎 레버를 대신해요.'], { knee: 2, ped: 2 }],
  ['1844', ['Boisselot, Paris', '부아슬로, 파리'], ['A pedal that keeps only the notes you hold: the first sostenuto shown.', '누르고 있는 음만 남기는 페달: 처음 선보인 소스테누토.'], { ped: 3 }],
  ['1874', ['Steinway', '스타인웨이'], ['Albert Steinway perfects and patents the sostenuto: the three pedals of today’s grand.', '알베르트 스타인웨이가 소스테누토를 완성하고 특허를 내요: 오늘 그랜드의 페달 세 개.'], { ped: 3 }],
];
// the piano's front: hand stops on the cheek, knee levers under the keys, pedals on the floor
function Ps8Front({ ctl = {}, w = 300 }) {
  const P = (x, on) => <path d={'M' + (x - 6) + ' 110 L' + (x - 11) + ' 128 Q' + x + ' 133 ' + (x + 11) + ' 128 L' + (x + 6) + ' 110 Z'} fill={on ? PEN_C : '#fff'} stroke={on ? PEN_C : PEN_N} strokeWidth="1.5"/>;
  return <svg viewBox="0 0 300 136" style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={t('The front of a piano: ', '피아노의 앞모습: ') + [ctl.hand ? t(ctl.hand + ' hand stop(s) beside the keys', '건반 옆 손잡이 ' + ctl.hand + '개') : '', ctl.knee ? t(ctl.knee + ' knee lever(s) under the keys', '건반 아래 무릎 레버 ' + ctl.knee + '개') : '', ctl.ped ? t(ctl.ped + ' pedal(s)', '페달 ' + ctl.ped + '개') : ''].filter(Boolean).join(', ')}>
    <rect x="20" y="20" width="260" height="30" rx="3" fill="#fff" {...PS8_SW}/>
    {Array.from({ length: 21 }, (_, i) => <line key={i} x1={32 + i * 11.8} x2={32 + i * 11.8} y1="34" y2="50" stroke={PEN_N} strokeWidth="1"/>)}
    <rect x="20" y="50" width="260" height="10" fill={PEN_N}/>
    <line x1="34" x2="34" y1="60" y2="104" {...PS8_SW}/><line x1="266" x2="266" y1="60" y2="104" {...PS8_SW}/>
    {ctl.hand >= 1 && <><circle cx="12" cy="30" r="5" fill={PEN_C}/><line x1="12" x2="20" y1="30" y2="30" stroke={PEN_C} strokeWidth="2"/></>}
    {ctl.hand >= 2 && <><circle cx="288" cy="30" r="5" fill={PEN_C}/><line x1="280" x2="288" y1="30" y2="30" stroke={PEN_C} strokeWidth="2"/></>}
    {ctl.knee >= 1 && <rect x="118" y="62" width="14" height="26" rx="4" fill={PEN_C} stroke={PEN_N} strokeWidth="1.2"/>}
    {ctl.knee >= 2 && <rect x="168" y="62" width="14" height="26" rx="4" fill={PEN_C} stroke={PEN_N} strokeWidth="1.2"/>}
    {ctl.ped && <><path d="M118 108 L150 94 L182 108" fill="none" {...PS8_SW}/>{ctl.ped === 2 ? <>{P(134, true)}{P(166, true)}</> : <>{P(124, true)}{P(150, true)}{P(176, true)}</>}</>}
  </svg>;
}
// the markings: [id, the marking, what it asks, then, today]
const PS8_MARKS = [
  ['ped', 'Ped. … ✱', ['Press the right pedal at “Ped.”, let it up at the star: every damper lifts off its string, then comes back.', '“Ped.”에서 오른쪽 페달을 밟고 별표에서 떼요: 댐퍼가 모두 현에서 들렸다가 돌아와요.'],
    ['Haydn first writes a pedal into a score in 1794, Beethoven in his first two piano concertos (1795): nearly 800 pedal marks in his music.', '하이든은 1794년 처음 악보에 페달을 적고, 베토벤은 피아노 협주곡 1·2번(1795년)부터: 그의 음악에 페달 표시가 800개 가까이.'],
    ['The same right pedal. Let your ear decide how deep and how long.', '같은 오른쪽 페달. 얼마나 깊이, 얼마나 오래는 귀가 정해요.']],
  ['knee', 'with the knee', ['Lift the dampers: in the 1770s to 1790s most pianos did it with a knee lever.', '댐퍼를 들어요: 1770–90년대 피아노는 대부분 무릎 레버로 했어요.'],
    ['In a sketch of 1790–92 Beethoven marks a row of chords “with the knee”.', '1790–92년 스케치에서 베토벤이 화음 한 줄에 “무릎으로”라고 적어요.'],
    ['Today it means the right pedal.', '오늘은 오른쪽 페달이에요.']],
  ['senza', 'senza sordino', ['“Without dampers”: the dampers stay up, so the strings go on ringing.', '“댐퍼 없이”: 댐퍼가 들린 채라 현이 계속 울려요.'],
    ['The “Moonlight” sonata opens with it.', '“월광” 소나타가 이 말로 시작해요.'],
    ['The right pedal. Careful: on the piano the sordini are the dampers, not a violinist’s mute.', '오른쪽 페달. 조심: 피아노에서 소르디니는 댐퍼예요. 바이올린의 약음기가 아니에요.']],
  ['una', 'una corda', ['“One string”: the left pedal shifts the hammers so they strike fewer strings, softer and veiled.', '“한 줄”: 왼쪽 페달이 해머를 옮겨 더 적은 줄을 치게 해요. 더 여리고 베일을 쓴 듯.'],
    ['On pianos of the late 1700s, with three strings a note, the player chose three, two or one by how far the pedal went down. Beethoven made it part of the music in his late sonatas.', '1700년대 후반 피아노는 음마다 현이 세 줄이라, 페달을 얼마나 밟느냐로 세 줄, 두 줄, 한 줄을 골랐어요. 베토벤은 후기 소나타에서 이것을 음악의 일부로 만들었어요.'],
    ['On a modern grand the treble hammers strike two strings, not one. An upright’s left pedal is not a true una corda: it moves the hammers closer.', '현대 그랜드에서 고음 해머는 한 줄이 아니라 두 줄을 쳐요. 업라이트의 왼쪽 페달은 진짜 우나 코르다가 아니에요: 해머를 현에 가까이 옮겨요.']],
  ['tre', 'tre corde', ['“Three strings” (or tutte le corde, “all the strings”): let the left pedal up.', '“세 줄”(또는 tutte le corde, “모든 줄”): 왼쪽 페달을 떼요.'],
    ['Beethoven sometimes asks for it so gently that the strings come back one by one.', '베토벤은 가끔 줄이 하나씩 돌아오도록 아주 천천히 떼라고 해요.'],
    ['Let the left pedal up, slowly if the music fades back in.', '왼쪽 페달을 떼요. 음악이 서서히 살아나면 천천히.']],
  ['sost', 'Sost. Ped.', ['The middle pedal of a grand: it keeps sounding only the notes you hold as you press it.', '그랜드의 가운데 페달: 밟는 순간 누르고 있던 음만 계속 울려요.'],
    ['First shown by Boisselot in Paris (1844); Albert Steinway perfected and patented it in 1874.', '파리의 부아슬로가 처음 선보이고(1844년), 알베르트 스타인웨이가 완성해 특허를 냈어요(1874년).'],
    ['Most uprights have a practice mute in the middle instead: check your own piano.', '업라이트 대부분은 가운데가 연습용 약음 페달이에요: 내 피아노를 확인해요.']],
];
const ps8Mark = (id) => PS8_MARKS.find(x => x[0] === id);
function PedalsPad({ onResult, fixed }) {
  const [yi, setYi] = useState(PS8_PSTOPS.length - 1), [mid, setMid] = useState('senza'), [quiz, setQuiz] = useState(!!fixed), [qm, setQm] = useState(fixed ? fixed.id : 'una'), [opts, setOpts] = useState(fixed ? fixed.opts : null), [ans, setAns] = useState(null);
  const st = PS8_PSTOPS[yi], mk = ps8Mark(mid);
  const ask = () => { let y, g = 0; do { y = pick(PS8_MARKS)[0]; } while (y === qm && g++ < 10); setQm(y); setOpts(shuffle(PS8_MARKS.filter(z => z[0] !== y)).slice(0, 3).map(z => z[0]).concat([y]).sort(() => Math.random() - 0.5)); setQuiz(true); setAns(null); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === qm }); };
  return (
    <div className="try-box" style={actBox} data-pm="pedals8">
      <div style={actTitle}>{t('Hand, knee, foot: the pedals’ story', '손, 무릎, 발: 페달 이야기')}</div>
      {!quiz && <>
        <div style={actNote}>{LANG === 'ko' ? <>모차르트는 발로 페달을 밟지 않았어요: <b>무릎</b>으로 레버를 밀어 올렸어요. 연도를 옮기며 피아노 앞이 어떻게 바뀌는지 봐요.</> : <>Mozart did not pedal with his foot: he pushed a lever up <b>with his knee</b>. Slide through the years and watch the front of the piano change.</>}</div>
        <Ps8Front ctl={st[3]}/>
        <input type="range" min="0" max={PS8_PSTOPS.length - 1} value={yi} data-ps8-year onChange={(e) => setYi(+e.target.value)} aria-label={t('Year', '연도')} style={{width:'100%',maxWidth:420,display:'block',margin:'6px auto 0',accentColor:PEN_C}}/>
        <div style={{display:'flex',justifyContent:'space-between',maxWidth:420,margin:'0 auto',fontSize:11.5,fontWeight:800,color:BK.muted}}><span>{PS8_PSTOPS[0][0]}</span><span>{t((yi + 1) + ' of ' + PS8_PSTOPS.length, PS8_PSTOPS.length + '개 중 ' + (yi + 1))}</span><span>{PS8_PSTOPS[PS8_PSTOPS.length - 1][0]}</span></div>
        <div style={{margin:'6px auto 10px',maxWidth:460,padding:'8px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff'}}><div style={{fontSize:15,fontWeight:900,color:BK.ink}}><span style={{color:BK.coral}}>{st[0]}</span> · {t(st[1][0], st[1][1])}</div><div style={{fontSize:13.5,color:BK.ink,lineHeight:1.45,marginTop:2}}>{t(st[2][0], st[2][1])}</div></div>
        <div style={{fontSize:13.5,fontWeight:900,color:BK.ink,textAlign:'center',margin:'4px 0'}}>{t('Read the marking', '표시 읽기')}</div>
        <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginBottom:6}}>{PS8_MARKS.map(x => <button key={x[0]} data-ps8-mark={x[0]} className={'chip' + (mid === x[0] ? ' active' : '')} aria-pressed={mid === x[0]} style={{minHeight:38,padding:'5px 10px',fontStyle:'italic'}} onClick={() => setMid(x[0])}>{x[1]}</button>)}</div>
        <div style={{maxWidth:460,margin:'0 auto',display:'grid',gap:6}}>
          <div style={{fontSize:14.5,fontWeight:800,color:BK.ink,lineHeight:1.45}}>{t(mk[2][0], mk[2][1])}</div>
          <div style={{fontSize:13,color:BK.ink,lineHeight:1.45}}><b style={{color:BK.coral}}>{t('Then', '그때')}</b>  {t(mk[3][0], mk[3][1])}</div>
          <div style={{fontSize:13,color:BK.ink,lineHeight:1.45}}><b style={{color:BK.coral}}>{t('Today', '오늘')}</b>  {t(mk[4][0], mk[4][1])}</div>
        </div>
      </>}
      {quiz && <>
        <div style={{textAlign:'center',margin:'6px auto',maxWidth:420,padding:'14px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff',fontFamily:LB_SERIF,fontSize:24,fontWeight:900,fontStyle:'italic',color:BK.ink}}>{ps8Mark(qm)[1]}</div>
        {!ans && <div style={{display:'grid',gap:6,marginTop:6}}>{opts.map(k => <button key={k} className="choice-btn" data-ps8-mean={k} onClick={() => say(k)} style={{padding:'10px 8px',fontSize:13.5,fontWeight:800,textAlign:'left',lineHeight:1.35}}>{t(ps8Mark(k)[2][0], ps8Mark(k)[2][1])}</button>)}</div>}
        {ans && <div style={{maxWidth:460,margin:'6px auto',fontSize:14,fontWeight:800,color:BK.ink,lineHeight:1.45}}>{t(ps8Mark(qm)[2][0], ps8Mark(qm)[2][1])}</div>}
      </>}
      {spMsg(ans ? (ans === qm ? t('Yes.', '맞아요.') : t('Not that one: read the marking again.', '그게 아니에요: 표시를 다시 읽어요.')) : quiz ? t('What does it ask for?', '무엇을 하라는 걸까요?') : '', ans ? (ans === qm ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ What does it mean?', '▶ 무슨 뜻일까?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}

// ── step 4: iron, felt and the singing tone: build the modern piano ──
// [id, year, name, who, what it gave]
const PS8_INV = [
  ['esc', '1821', ['Double escapement', '더블 이스케이프먼트'], ['Érard, Paris', '에라르, 파리'], ['A note can sound again before the key comes all the way up: quick repeated notes.', '건반이 끝까지 올라오기 전에 같은 음을 다시 칠 수 있어요: 빠른 반복음.']],
  ['iron', '1825–1843', ['The iron frame', '철 프레임'], ['Babcock (square piano, 1825), Broadwood (iron bars, 1827), Chickering (one-piece frame for the grand, 1843)', '배브콕(스퀘어 피아노, 1825년), 브로드우드(철 막대, 1827년), 치커링(그랜드용 통 프레임, 1843년)'], ['It holds much thicker, tighter strings: a bigger tone.', '훨씬 굵고 팽팽한 현을 버텨요: 더 큰 소리.']],
  ['felt', '1826', ['Felt hammers', '펠트 해머'], ['Henri Pape, Paris', '앙리 파프, 파리'], ['Felt instead of leather: a rounder tone. Careful Viennese makers still wrapped the felt in leather.', '가죽 대신 펠트: 더 둥근 소리. 신중한 빈의 제작자들은 펠트 위에 가죽을 한 겹 더 씌웠어요.']],
  ['cross', '1859', ['Crossed strings', '교차된 현'], ['Steinway, New York', '스타인웨이, 뉴욕'], ['The bass strings cross over the others.', '저음 현이 다른 현 위로 지나가요.']],
  ['k88', '1880s', ['88 keys', '88건반'], ['', ''], ['A0 to C8 becomes the standard: the keyboard you play.', 'A0부터 C8까지가 표준이 돼요: 지금 치는 건반.']],
];
const ps8Inv = (id) => PS8_INV.find(x => x[0] === id);
// a grand from above: the case, the strings (crossed or not), the frame, the hammers (leather squares or felt circles), the keys
function Ps8Grand({ on = {}, w = 320 }) {
  const n = on.k88 ? 22 : 17, top = (x) => x <= 60 ? 12 : 12 + 84 * Math.pow((x - 60) / 240, 1.5);   // the bentside: the strings end on it
  const bent = Array.from({ length: 25 }, (_, i) => { const x = 60 + i * 10; return x + ' ' + top(x).toFixed(1); }).join(' L');
  const xs = Array.from({ length: 13 }, (_, i) => 40 + i * 20);
  return <svg viewBox="0 0 320 150" style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={t('A grand piano from above: the keys at the front, the strings running back from them, the longest bass strings on the left. ', '위에서 본 그랜드 피아노: 앞에 건반, 거기서 뒤로 뻗는 현, 왼쪽에 가장 긴 저음 현. ') + PS8_INV.filter(x => on[x[0]]).map(x => t(x[2][0], x[2][1])).join(', ')}>
    <path d={'M20 118 L20 16 Q20 12 26 12 L' + bent + ' L300 118 Z'} fill="#fff" {...PS8_SW}/>
    {on.iron && <path d={'M28 112 L28 20 L' + Array.from({ length: 23 }, (_, i) => { const x = 62 + i * 10; return x + ' ' + (top(x) + 8).toFixed(1); }).join(' L') + ' L290 112 Z'} fill="rgba(38,41,107,0.08)" stroke={PEN_N} strokeWidth="3.2" strokeLinejoin="round"/>}
    {xs.map((x, i) => on.cross && i < 3 ? <line key={i} x1={x} y1="108" x2={x + 70 + i * 12} y2={top(x + 70 + i * 12) + 4} stroke={PEN_C} strokeWidth="1.8"/> : <line key={i} x1={x} y1="108" x2={x} y2={top(x) + 4} stroke={PEN_N} strokeWidth="1.1"/>)}
    {xs.map((x, i) => on.felt ? <circle key={'h' + i} cx={x} cy="104" r="3.4" fill={PEN_C}/> : <rect key={'h' + i} x={x - 3} y="101" width="6" height="6" fill="#fff" stroke={PEN_N} strokeWidth="1.4"/>)}
    <rect x="20" y="118" width="280" height="24" fill="#fff" {...PS8_SW}/>
    {Array.from({ length: n - 1 }, (_, i) => <line key={i} x1={20 + (i + 1) * 280 / n} x2={20 + (i + 1) * 280 / n} y1="118" y2="142" stroke={PEN_N} strokeWidth="0.9"/>)}
    {on.esc && <path d="M300 96 l6 -7 l6 7 M300 104 l6 -7 l6 7" fill="none" stroke={PEN_C} strokeWidth="2.2" strokeLinecap="round"/>}
  </svg>;
}
// the repeat toy: tap one key fast; with one escapement the key must come all the way up before it can sound again
const PS8_GAP = { single: 0.17, double: 0.07 };   // seconds: a toy's numbers, chosen to show the idea, not measured
function RepeatToy() {
  const [mode, setMode] = useState('single'), [n, setN] = useState({ taps: 0, notes: 0 }), last = React.useRef(-1), t0 = React.useRef(0);
  const tap = () => { const ctx = getAudio(); if (!ctx) return; const now = ctx.currentTime; if (!t0.current || now - t0.current > 3) { t0.current = now; last.current = -1; setN({ taps: 0, notes: 0 }); }
    const ok = last.current < 0 || now - last.current >= PS8_GAP[mode]; if (ok) { last.current = now; blip(ctx, now + 0.01, mFreq(72), 0.12, 0.15, 'triangle'); }
    setN(v => ({ taps: v.taps + 1, notes: v.notes + (ok ? 1 : 0) })); };
  return <div data-ps8-repeat style={{margin:'8px auto 0',maxWidth:420,textAlign:'center'}}>
    <div style={{fontSize:13.5,fontWeight:900,color:BK.ink,margin:'4px 0'}}>{t('Repeat one note as fast as you can for three seconds', '3초 동안 한 음을 최대한 빨리 반복해 봐요')}</div>
    {spChips([['single', t('One escapement', '이스케이프먼트 하나')], ['double', t('Double escapement', '더블 이스케이프먼트')]], mode, (v) => { setMode(v); t0.current = 0; setN({ taps: 0, notes: 0 }); })}
    <button className="primary-btn" style={{width:'auto',minWidth:160,minHeight:56,fontSize:18}} onPointerDown={tap} onClick={(e) => { if (e.detail === 0) tap(); }}>{t('Tap tap tap', '톡톡톡')}</button>
    <div style={{fontSize:14,fontWeight:900,color:BK.ink,marginTop:6}}>{t(n.taps + ' taps, ' + n.notes + ' notes sounded', n.taps + '번 눌러서 ' + n.notes + '번 소리 났어요')}</div>
    <div style={{fontSize:12,color:BK.muted,marginTop:2}}>{t('A toy: its timings are made up to show the idea, not measured from real pianos.', '장난감이에요: 시간은 생각을 보여 주려고 정한 것이지, 실제 피아노를 잰 값이 아니에요.')}</div>
  </div>;
}
function ModernPad({ onResult, fixed }) {
  const [on, setOn] = useState({}), [quiz, setQuiz] = useState(!!fixed), [qi, setQi] = useState(fixed ? fixed.id : 'felt'), [ans, setAns] = useState(null);
  const all = PS8_INV.every(x => on[x[0]]), last = PS8_INV.filter(x => on[x[0]]).slice(-1)[0];
  const ask = () => { let y, g = 0; do { y = pick(PS8_INV)[0]; } while (y === qi && g++ < 10); setQi(y); setQuiz(true); setAns(null); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === qi }); };
  return (
    <div className="try-box" style={actBox} data-pm="modern">
      <div style={actTitle}>{t('Build the modern piano', '현대 피아노 조립하기')}</div>
      {!quiz && <>
        <div style={actNote}>{LANG === 'ko' ? <>1820년의 피아노에서 시작해요: 가죽 해머, 나무 틀, 곧은 현. 발명을 하나씩 더해서 <b>오늘의 그랜드</b>를 만들어요.</> : <>Start with a piano of 1820: leather hammers, a wooden frame, straight strings. Add the inventions one by one and build <b>today’s grand</b>.</>}</div>
        <Ps8Grand on={on}/>
        <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'8px 0'}}>{PS8_INV.map(x => <button key={x[0]} data-ps8-inv={x[0]} className={'chip' + (on[x[0]] ? ' active' : '')} aria-pressed={!!on[x[0]]} style={{minHeight:38,padding:'5px 10px'}} onClick={() => setOn(o => ({ ...o, [x[0]]: !o[x[0]] }))}><b style={{color:on[x[0]] ? undefined : BK.coral}}>{x[1]}</b> {t(x[2][0], x[2][1])}</button>)}</div>
        {last && <div style={{margin:'0 auto 6px',maxWidth:460,padding:'8px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff'}}><div style={{fontSize:14.5,fontWeight:900,color:BK.ink}}>{t(last[2][0], last[2][1])}{last[3][0] ? ' · ' + t(last[3][0], last[3][1]) : ''}</div><div style={{fontSize:13.5,color:BK.ink,lineHeight:1.45,marginTop:2}}>{t(last[4][0], last[4][1])}</div></div>}
        {all && <div style={{fontSize:13.5,color:BK.coral,fontWeight:800,textAlign:'center',lineHeight:1.45,maxWidth:460,margin:'0 auto'}}>{t('Chopin played both Pleyel and Érard pianos and preferred the Pleyel’s more intimate sound; Liszt preferred the Érard’s more dramatic range of colours.', '쇼팽은 플레옐과 에라르를 다 쳤고 플레옐의 더 내밀한 소리를 좋아했어요; 리스트는 에라르의 더 극적인 색깔을 좋아했어요.')}</div>}
        <RepeatToy/>
      </>}
      {quiz && <>
        <div style={{textAlign:'center',margin:'6px auto',maxWidth:420,padding:'12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff',fontSize:15,fontWeight:800,color:BK.ink,lineHeight:1.4}}>{t(ps8Inv(qi)[4][0], ps8Inv(qi)[4][1])}</div>
        {!ans && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6}}>{PS8_INV.map(x => <button key={x[0]} className="choice-btn" data-ps8-which={x[0]} onClick={() => say(x[0])} style={{padding:'10px 4px',fontSize:13.5,fontWeight:900}}>{t(x[2][0], x[2][1])}</button>)}</div>}
      </>}
      {spMsg(ans ? (ans === qi ? t('Yes: ' + ps8Inv(qi)[2][0] + ', ' + ps8Inv(qi)[1] + '.', '맞아요: ' + ps8Inv(qi)[2][1] + ', ' + ps8Inv(qi)[1] + '.') : t('It is ' + ps8Inv(qi)[2][0] + ' (' + ps8Inv(qi)[1] + ').', '정답은 ' + ps8Inv(qi)[2][1] + '(' + ps8Inv(qi)[1] + ').')) : quiz ? t('Which invention gave this?', '어떤 발명이 이것을 주었을까요?') : '', ans ? (ans === qi ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Which invention?', '▶ 어떤 발명일까?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}

// ── step 5: their piano, my choices ──
// [id, who, the piano (from steps 1 to 4), the period (ERAS) for the line about today's piano]
const ps8Today = (e) => e ? e.today.replace(/^(On the piano|피아노로 칠 때): /, '') : '';
const PS8_MINE = [
  ['bach', ['Bach and the Baroque', '바흐와 바로크'], ['Harpsichord, clavichord and organ. Bach tried Silbermann’s early pianos; his keyboard music was not written for the piano.', '하프시코드, 클라비코드, 오르간. 바흐는 질버만의 초기 피아노를 쳐 봤지만, 그의 건반 음악은 피아노를 위해 쓰이지 않았어요.'], 'baroque'],
  ['mozart', ['Haydn and Mozart', '하이든과 모차르트'], ['The Viennese piano: hammer on the key, a light elastic touch, five octaves (61 keys), knee levers for the dampers, a moderator.', '빈의 피아노: 건반 위의 해머, 가볍고 탄력 있는 터치, 5옥타브(61건반), 댐퍼는 무릎 레버로, 모데라토르.'], 'classical'],
  ['beet1', ['Beethoven to 1803', '1803년까지의 베토벤'], ['Five octaves still. His first pedal marks are in his first two piano concertos (1795).', '여전히 5옥타브. 첫 페달 표시는 피아노 협주곡 1·2번(1795년)에.'], 'classical'],
  ['beet2', ['Beethoven, Op. 53 to 81a', '베토벤, 작품 53–81a'], ['His Érard of 1803: F1 to C7, 68 keys, with a moderator; then English grands to C7.', '1803년의 에라르: F1부터 C7까지 68건반, 모데라토르; 그다음 C7까지의 영국 그랜드.'], null],
  ['beet3', ['Beethoven from Op. 101', '작품 101부터의 베토벤'], ['Graf’s kind of grand: C1 to F7, 78 keys. Una corda and tre corde written into the music.', '그라프 같은 그랜드: C1부터 F7까지 78건반. 우나 코르다와 트레 코르데가 음악 안에.'], 'romantic'],
  ['chopin', ['Chopin', '쇼팽'], ['Paris grands of the 1830s and 40s, Pleyel and Érard; he preferred the Pleyel’s intimate sound. An Érard of 1836 reaches C1 to F7.', '1830–40년대 파리의 그랜드, 플레옐과 에라르; 그는 플레옐의 내밀한 소리를 좋아했어요. 1836년의 에라르는 C1부터 F7까지.'], 'romantic'],
  ['liszt', ['Liszt', '리스트'], ['The Érard, with its double escapement (1821) and, he felt, a more dramatic range of colours.', '에라르: 더블 이스케이프먼트(1821년), 그리고 그가 느끼기에 더 극적인 색깔.'], 'romantic'],
  ['late', ['The late 1800s', '1800년대 후반'], ['Iron frame, felt hammers, crossed strings (1859); seven octaves by about 1850, 88 keys by the 1880s.', '철 프레임, 펠트 해머, 교차된 현(1859년); 1850년쯤 7옥타브, 1880년대에 88건반.'], 'romantic'],
  ['modern', ['1900 to today', '1900년부터 오늘'], ['The piano you play: 88 keys, and on a grand the three pedals with the sostenuto (1874).', '지금 치는 피아노: 88건반, 그랜드라면 소스테누토(1874년)가 있는 페달 세 개.'], 'modern'],
];
const PS8_ASK = [
  ['range', ['Range: does the music climb to the top or bottom of that keyboard? On mine it is the middle.', '음역: 음악이 그 건반의 맨 위나 아래까지 가나요? 내 피아노에서는 가운데예요.']],
  ['pedal', ['Pedal: hand, knee or foot? How many marks, and what do they ask?', '페달: 손, 무릎, 발? 표시가 몇 개이고, 무엇을 하라고 하나요?']],
  ['touch', ['Touch: a light Viennese action or a heavier English one? Then feel your own.', '터치: 가벼운 빈 액션인가요, 무거운 영국 액션인가요? 그다음 내 피아노를 느껴 봐요.']],
  ['tone', ['Tone: leather or felt, wood or iron? Mine has felt and iron: listen to the balance of the hands.', '소리: 가죽인가요 펠트인가요, 나무인가요 철인가요? 내 피아노는 펠트와 철: 두 손의 균형을 들어 봐요.']],
];
const PS8_MINE_KEY = 'pb_ps8_mine';
function MyPianoPad() {
  const load = () => { try { return JSON.parse(localStorage.getItem(PS8_MINE_KEY)) || {}; } catch (e) { return {}; } };
  const [st, setSt] = useState(load), id = st.id || 'mozart', x = PS8_MINE.find(r => r[0] === id), era = x[3] ? ERAS.find(e => e.id === x[3]) : null, said = (st.said || {})[id] || {};
  const save = (v) => { setSt(v); try { localStorage.setItem(PS8_MINE_KEY, JSON.stringify(v)); } catch (e) {} };
  const tick = (k) => save({ ...st, id, said: { ...(st.said || {}), [id]: { ...said, [k]: !said[k] } } });
  return (
    <div className="try-box" style={actBox} data-pm="mine">
      <div style={actTitle}>{t('Their piano, my choices', '그들의 피아노, 나의 선택')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>디플로마 시험관은 묻습니다: <b>이 곡은 어떤 피아노를 위해 썼고, 그래서 오늘 당신은 어떻게 치나요?</b> 작곡가를 고르고, 네 가지를 소리 내어 답해 봐요.</> : <>A diploma examiner asks: <b>which piano was this written for, and so how do you play it today?</b> Choose your composer, then answer the four questions aloud.</>}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{PS8_MINE.map(r => <button key={r[0]} data-ps8-mine={r[0]} className={'chip' + (id === r[0] ? ' active' : '')} aria-pressed={id === r[0]} style={{minHeight:38,padding:'5px 10px'}} onClick={() => save({ ...st, id: r[0] })}>{t(r[1][0], r[1][1])}</button>)}</div>
      <div style={{margin:'0 auto 8px',maxWidth:460,padding:'10px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff'}}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.04em'}}>{t('THE PIANO', '그 피아노')}</div>
        <div style={{fontSize:14.5,fontWeight:800,color:BK.ink,lineHeight:1.45}}>{t(x[2][0], x[2][1])}</div>
        {era && <div style={{fontSize:13,color:BK.ink,lineHeight:1.45,marginTop:4}}><b style={{color:BK.coral}}>{t('On today’s piano', '오늘의 피아노로')}</b>  {ps8Today(era)}</div>}
      </div>
      <div style={{display:'grid',gap:6,maxWidth:460,margin:'0 auto'}}>{PS8_ASK.map(([k, q]) => <button key={k} data-ps8-ask={k} onClick={() => tick(k)} aria-pressed={!!said[k]} style={{display:'grid',gridTemplateColumns:'26px 1fr',gap:8,alignItems:'center',textAlign:'left',padding:'8px 10px',borderRadius:10,border:'1.5px solid ' + (said[k] ? BK.green : BK.line),background:said[k] ? BK.greenSoft : '#fff',fontFamily:'inherit',color:BK.ink,cursor:'pointer',fontSize:13.5,lineHeight:1.4}}>
        <span style={{width:22,height:22,borderRadius:11,border:'2px solid ' + (said[k] ? BK.green : BK.ink),background:said[k] ? BK.green : '#fff',color:'#fff',fontSize:13,fontWeight:900,display:'flex',alignItems:'center',justifyContent:'center'}}>{said[k] ? '✓' : ''}</span><span>{t(q[0], q[1])}</span></button>)}</div>
      <div style={{margin:'10px auto 0',maxWidth:460,fontSize:13.5,color:BK.ink,lineHeight:1.6,padding:'8px 12px',borderLeft:'3px solid ' + BK.coral,background:'#fff'}}>{LANG === 'ko' ? <>이렇게 말해 봐요: “이 곡은 <b>___</b>를 위해 쓰였어요. 그 피아노는 <b>___</b>는 할 수 있었지만 <b>___</b>는 못 했어요. 그래서 오늘 그랜드에서 저는 <b>___</b>.”</> : <>Say it like this: “It was written for <b>___</b>. That piano could <b>___</b> but not <b>___</b>. So on today’s grand I <b>___</b>.”</>}</div>
      {spMsg(Object.values(said).filter(Boolean).length === PS8_ASK.length ? t('All four said aloud for this composer.', '이 작곡가로 네 가지를 다 말했어요.') : '', BK.green)}
    </div>
  );
}

// ── easy to mix up: what a student might think, and what is so (each step) ──
const PS8_CAREFUL = {
  act: [[['“Viennese” means made in Vienna.', '“빈의”는 빈에서 만들었다는 뜻.'], ['It names the kind of action: Stein worked in Augsburg.', '액션의 종류 이름이에요: 슈타인은 아우크스부르크에서 일했어요.']],
    [['The English piano was the better one.', '영국 피아노가 더 좋았다.'], ['Heavier and louder, not better: Haydn, Mozart and Beethoven knew the Viennese touch.', '더 무겁고 컸을 뿐: 하이든, 모차르트, 베토벤이 안 터치는 빈의 것.']]],
  comp: [[['Mozart’s piano had 88 keys.', '모차르트의 피아노는 88건반.'], ['61 keys, F1 to F6.', '61건반, F1부터 F6까지.']],
    [['Beethoven ended up with a modern keyboard.', '베토벤은 결국 현대 건반을 가졌다.'], ['At most 78 keys, C1 to F7.', '많아야 78건반, C1부터 F7까지.']]],
  ped: [[['Mozart pressed a pedal with his foot.', '모차르트는 발로 페달을 밟았다.'], ['His Walter had knee levers.', '그의 발터에는 무릎 레버가 있었어요.']],
    [['senza sordino: without the mute.', '센차 소르디노: 약음기 없이.'], ['Without dampers: the right pedal down.', '댐퍼 없이: 오른쪽 페달을 밟아요.']],
    [['una corda: the hammer strikes one string.', '우나 코르다: 해머가 현 한 줄을 친다.'], ['On today’s grand, two of the three treble strings.', '오늘의 그랜드에서는 고음 세 줄 중 두 줄.']]],
  inv: [[['The iron frame came in 1859.', '철 프레임은 1859년에 나왔다.'], ['Step by step: 1825, 1827, 1843. 1859 is Steinway’s crossed strings.', '한 걸음씩: 1825, 1827, 1843년. 1859년은 스타인웨이의 교차현.']],
    [['Felt took over at once.', '펠트가 곧바로 자리 잡았다.'], ['Some Viennese makers still wrapped the felt in leather.', '어떤 빈 제작자는 펠트를 가죽으로 감쌌어요.']]],
  mine: [[['A fact is the answer.', '사실 하나가 답이다.'], ['A fact, then the choice it leads you to.', '사실 하나, 그리고 그것이 이끄는 나의 선택.']],
    [['There is one right way to play it today.', '오늘 치는 올바른 방법은 하나뿐이다.'], ['Many ways can be right: the examiner wants your reason.', '여러 방법이 맞을 수 있어요: 시험관은 나의 이유를 원해요.']]],
};
function Ps8Careful({ k }) {
  const scr = lbScreen();
  return <div data-ps8-careful={k} style={{border:'1px solid rgba(38,41,107,0.2)',borderRadius:10,padding:scr ? '8px 10px' : '7px 12px',background:'#fff'}}>
    <div style={{fontSize:12.5,fontWeight:900,color:BK.coral,marginBottom:4,letterSpacing:'0.04em'}}>{t('EASY TO MIX UP', '헷갈리기 쉬워요')}</div>
    {PS8_CAREFUL[k].map(([no, yes], i) => <div key={i} style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1.3fr',gap:scr ? 1 : 12,fontSize:scr ? 13.5 : 13,lineHeight:1.4,padding:'3px 0',borderTop:i ? '1px solid rgba(38,41,107,0.1)' : 'none'}}>
      <span style={{color:BK.muted}}><b style={{color:BK.coral}}>✗</b> {t(no[0], no[1])}</span><span style={{color:BK.ink,fontWeight:800}}><b style={{color:BK.green}}>✓</b> {t(yes[0], yes[1])}</span></div>)}
  </div>;
}
// ── the pictures on paper ──
const ps8PicAct = () => lsRawPic('<line x1="4" y1="8" x2="76" y2="8" stroke="#26296b" stroke-width="1.6"/><rect x="4" y="30" width="64" height="5" fill="#fff" stroke="#26296b" stroke-width="1.6"/><path d="M60 28 L30 22" stroke="#26296b" stroke-width="2"/><rect x="22" y="14" width="10" height="8" rx="3" fill="#e4572e"/>', [0, 0, 80, 40]);
const ps8PicComp = () => lsRawPic('<rect x="4" y="6" width="72" height="14" fill="#fff" stroke="#26296b" stroke-width="1.4"/>' + [0, 1, 2].map(i => '<rect x="' + (20 - i * 7) + '" y="' + (24 + i * 5) + '" width="' + (40 + i * 14) + '" height="3.6" rx="1.8" fill="' + (i === 2 ? '#e4572e' : '#26296b') + '"/>').join(''), [0, 0, 80, 40]);
const ps8PicPed = () => lsRawPic('<rect x="22" y="6" width="9" height="16" rx="3" fill="#e4572e"/><rect x="47" y="6" width="9" height="16" rx="3" fill="#e4572e"/>' + [28, 40, 52].map(x => '<path d="M' + (x - 3) + ' 26 L' + (x - 6) + ' 36 Q' + x + ' 39 ' + (x + 6) + ' 36 L' + (x + 3) + ' 26 Z" fill="#fff" stroke="#26296b" stroke-width="1.4"/>').join(''), [0, 0, 80, 40]);
const ps8PicIron = () => lsRawPic('<path d="M6 34 L6 8 L44 8 Q74 10 74 26 L74 34 Z" fill="none" stroke="#26296b" stroke-width="3"/><line x1="12" y1="28" x2="60" y2="14" stroke="#e4572e" stroke-width="1.6"/><line x1="12" y1="16" x2="56" y2="28" stroke="#26296b" stroke-width="1.2"/>', [0, 0, 80, 40]);
const ps8PicMine = () => lsRawPic('<rect x="6" y="8" width="40" height="26" rx="3" fill="#fff" stroke="#26296b" stroke-width="1.8"/><path d="M12 16 H40 M12 22 H34" stroke="#26296b" stroke-width="1.4"/><path d="M52 20 L70 20 M64 14 L70 20 L64 26" fill="none" stroke="#e4572e" stroke-width="2.2" stroke-linecap="round"/>', [0, 0, 80, 40]);

function ps8LbPages(scr = false) {
  const ch = 'piano-story-8', ps = bkChapterNo('piano-story'), p8 = bkChapterNo('pieces-8');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks = [[ps8PicAct(), t('I explain the Viennese and the English action, and who played each', '빈 액션과 영국 액션을 설명하고, 누가 무엇을 쳤는지 말해요')], [ps8PicComp(), t('I say how many keys my composer had, and where my piece meets the edge', '내 작곡가의 건반이 몇 개였는지, 내 곡이 어디서 끝에 닿는지 말해요')],
    [ps8PicPed(), t('I read every pedal marking in my score, then and today', '내 악보의 페달 표시를 그때와 오늘로 모두 읽어요')], [ps8PicIron(), t('I name the inventions that made the modern piano, with their dates', '현대 피아노를 만든 발명을 연도와 함께 말해요')], [ps8PicMine(), t('I explain my choices on today’s piano from the piano it was written for', '곡이 쓰인 피아노에서 출발해 오늘 피아노에서의 내 선택을 설명해요')]];
  const toc = [[t('Vienna and London', '빈과 런던'), 2], [t('The keyboard grows', '자라나는 건반'), 3], [t('Hand, knee, foot', '손, 무릎, 발'), 4], [t('Iron, felt and the singing tone', '철, 펠트, 노래하는 소리'), 5], [t('Their piano, my choices', '그들의 피아노, 나의 선택'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const actStill = <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:10,width:'100%',maxWidth:660,margin:'0 auto'}}>{['vienna', 'london'].map(k => <div key={k}><div style={{fontFamily:LB_SERIF,fontSize:scr ? 15 : 17,fontWeight:900,color:BK.ink,textAlign:'center'}}>{t(PS8_ACT[k].name[0], PS8_ACT[k].name[1])}</div><Ps8Action kind={k} ph={1} w={300}/><div style={{fontSize:scr ? 11.5 : 12.5,color:BK.ink,lineHeight:1.35,textAlign:'center'}}>{t(PS8_ACT[k].who[0], PS8_ACT[k].who[1])}</div></div>)}</div>;
  const compStill = <div style={{width:'100%',maxWidth:620,margin:'0 auto'}}><Ps8Ladder sel={null}/><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:'2px 14px',marginTop:4}}>{PS8_COMPASS.map(r => <div key={r[0]} style={{fontSize:scr ? 11.5 : 12.5,color:BK.ink,lineHeight:1.35}}><b style={{color:BK.coral}}>{ps8Keys(r)}</b> {t(r[3][0], r[3][1])} · {ps8NoteName(r[1])}–{ps8NoteName(r[2])}</div>)}</div></div>;
  const pedStill = <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:8,width:'100%',maxWidth:680,margin:'0 auto'}}>{[2, 4, 7].map(i => { const y = PS8_PSTOPS[i][0]; return <div key={i}><Ps8Front ctl={PS8_PSTOPS[i][3]} w={220}/><div style={{fontSize:scr ? 11.5 : 12.5,fontWeight:900,color:BK.ink,textAlign:'center'}}><span style={{color:BK.coral}}>{y}</span> · {t(PS8_PSTOPS[i][1][0], PS8_PSTOPS[i][1][1])}</div></div>; })}</div>;
  const ironStill = <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:10,width:'100%',maxWidth:660,margin:'0 auto',alignItems:'center'}}><div><div style={{fontSize:scr ? 12 : 13,fontWeight:900,color:BK.ink,textAlign:'center'}}>{t('About 1820', '1820년쯤')}</div><Ps8Grand on={{}} w={300}/></div><div><div style={{fontSize:scr ? 12 : 13,fontWeight:900,color:BK.ink,textAlign:'center'}}>{t('The 1880s', '1880년대')}</div><Ps8Grand on={{ esc: 1, iron: 1, felt: 1, cross: 1, k88: 1 }} w={300}/></div></div>;
  const mineStill = <div style={{display:'grid',gap:scr ? 4 : 6,width:'100%',maxWidth:640,margin:'0 auto'}}>{PS8_MINE.filter(r => ['bach', 'mozart', 'beet3', 'chopin', 'modern'].includes(r[0])).map(r => <div key={r[0]} style={{display:'grid',gridTemplateColumns:scr ? '110px 1fr' : '150px 1fr',gap:8,fontSize:scr ? 11.5 : 12.5,color:BK.ink,lineHeight:1.3}}><b style={{color:BK.coral}}>{t(r[1][0], r[1][1])}</b><span>{t(r[2][0], r[2][1])}</span></div>)}</div>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('For the diplomas (AMusA, LMusA): "For instrumentalists, the construction and development of the instrument, with special consideration given to any implications this may have upon the repertoire that is performed" (Piano syllabus, Section II, general knowledge), used "as a basis for discussing the interpretive choices". The Piano’s Story (chapter ' + ps + ') is the Grade 3–4 telling; this room goes from the two actions to the modern grand, and ends at the student’s own piece, with Knowing Your Pieces, Grade 8 and Diplomas (chapter ' + p8 + '). Every fact is listed with its source in the room’s research note; the sounds are sketches, not recordings.', '디플로마(AMusA, LMusA): "악기 연주자는 악기의 구조와 발달, 그리고 그것이 연주하는 레퍼토리에 미칠 수 있는 영향"(피아노 교재, Section II, 일반 지식), "해석의 선택을 논하는 바탕으로". 피아노 이야기(' + ps + '장)는 3–4급의 이야기; 이 방은 두 액션에서 현대 그랜드까지 가서, 학생 자신의 곡에서 끝나요. 내 곡 알기, Grade 8과 디플로마(' + p8 + '장)와 함께. 모든 사실은 방의 조사 노트에 출처와 함께 있어요; 소리는 스케치이지 녹음이 아니에요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:40,fontWeight:900,color:BK.ink,lineHeight:1.04,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={120}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}><Ps8Ladder sel="five" rows={false}/></div></LbPic>
      <LbSay size={18}>{t('Your piece was written for a piano that is not yours. It had fewer keys, a lighter touch, knee levers or one pedal, leather hammers and a wooden frame. Know that piano, and you know why the score looks the way it does.', '내 곡은 내 것이 아닌 피아노를 위해 쓰였어요. 건반은 더 적고, 터치는 더 가볍고, 무릎 레버나 페달 하나, 가죽 해머에 나무 틀. 그 피아노를 알면, 악보가 왜 그렇게 생겼는지 알아요.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h lb-can-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('After this chapter, I can', '이 챕터를 마치면')}</div>
          {checks.map(([, x], i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Vienna and London', '빈과 런던')}
      teacher={<>{t('Stein’s Viennese action (Augsburg, about 1769, refined through the 1770s; the Prellmechanik): the hammer sits on the key, its head towards the player, and a rail flicks it up. Walter built on Stein’s model in Vienna from the early 1780s; Mozart bought a Walter about 1783 (it is in the Mozart Museum, Salzburg). The English action (Backers, patented 1776; Stodart 1777; Broadwood 1780): the hammer hangs from its own rail, head away from the player, and a jack on the key pushes it. The drawings are simplified. Watch for “English pianos were better”: they were heavier and louder; the Viennese touch is the one Haydn, Mozart and Beethoven knew.', '슈타인의 빈 액션(아우크스부르크, 1769년쯤, 1770년대에 다듬음; 프렐메카닉): 해머가 건반 위에 얹혀 머리가 연주자를 향하고, 레일이 그것을 튕겨 올려요. 발터는 1780년대 초부터 빈에서 슈타인의 모델로 만들었고, 모차르트가 1783년쯤 발터를 샀어요(잘츠부르크 모차르트 박물관에 있어요). 영국 액션(배커스 1776년 특허; 스토다트 1777년; 브로드우드 1780년): 해머가 따로 레일에 매달려 머리가 연주자 반대쪽, 건반 위의 잭이 밀어요. 그림은 단순화했어요. “영국 피아노가 더 좋았다”에 주의: 더 무겁고 컸을 뿐; 하이든, 모차르트, 베토벤이 안 터치는 빈의 것이에요.')}</>}>
      <LbLive still={<LbPic h={190}>{actStill}</LbPic>} live={<ActionsPad/>}/>
      <LbSay>{LANG === 'ko' ? <>빈의 해머는 <b>건반 위에</b> 앉아 튕겨 올라가고, 런던의 해머는 <b>따로 매달려</b> 잭이 밀어 올려요. 그래서 빈의 터치는 가볍고, 런던은 묵직해요. 모차르트의 짧은 이음줄과 맑은 반주는 그 가벼운 건반에서 나왔어요.</> : <>The Viennese hammer <b>rides on the key</b> and is flicked up; the London hammer <b>hangs on its own</b> and a jack pushes it. So Vienna feels light and London weighty. Mozart’s short slurs and clear accompaniments come from that light keyboard.</>}</LbSay>
      <Ps8Careful k="act"/>
      <LbDefs items={[
        [t('action', '액션'), t('The machine between your key and the hammer.', '건반과 해머 사이의 장치.')],
        [t('Viennese action', '빈 액션'), t('The hammer sits on the key and is flicked up by a rail: light and quick.', '해머가 건반 위에 얹혀 레일에 튕겨 올라가요: 가볍고 빨라요.')],
        [t('English action', '영국 액션'), t('The hammer hangs from its own rail and a jack pushes it up: heavier and louder.', '해머가 따로 레일에 매달려 잭이 밀어 올려요: 더 무겁고 커요.')],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [<>모차르트의 한 프레이즈를 아주 가볍게, 손가락 끝으로만 쳐요: 빈의 터치를 상상해요.</>, <>같은 프레이즈를 팔 무게로 쳐요. 어느 쪽이 악보의 짧은 이음줄에 맞나요?</>]
        : [<>Play a Mozart phrase very lightly, from the fingertips: imagine the Viennese touch.</>, <>Play it again with arm weight. Which one fits the score’s short slurs?</>]}/>
      <LbRemember>{t('Vienna: light and quick. London: heavier and louder.', '빈: 가볍고 빠르게. 런던: 더 무겁고 크게.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('The keyboard grows', '자라나는 건반')}
      teacher={<>{t('Compasses from the Greifenberger Institut’s table: F1–F6 (61 keys) to about 1790, Mozart all his life and Beethoven until 1803; F1–C7 (68) for Beethoven’s Érard of 1803, his Op. 53 to Op. 81a; C1–C7 (73) English grands 1808–1820, Broadwood; C1–F7 (78) Graf and others about 1816–1840, Beethoven from Op. 101; A0–A7 (85) about 1850; A0–C8 (88) today. The quiz asks only notes outside the five octaves. Watch for “88 keys since Mozart”: Beethoven never had more than 78.', '음역은 그라이펜베르거 연구소의 표에서: F1–F6(61건반) 1790년쯤까지, 모차르트는 평생, 베토벤은 1803년까지; F1–C7(68) 1803년 베토벤의 에라르, 작품 53부터 81a; C1–C7(73) 1808–1820년 영국 그랜드, 브로드우드; C1–F7(78) 1816–1840년쯤 그라프 등, 베토벤 작품 101부터; A0–A7(85) 1850년쯤; A0–C8(88) 오늘. 퀴즈는 5옥타브 밖의 음만 물어요. “모차르트 때부터 88건반”에 주의: 베토벤도 78개를 넘지 못했어요.')}</>}>
      <LbLive still={<LbPic h={200}>{compStill}</LbPic>} live={<CompassPad/>}/>
      <Ps8Careful k="comp"/>
      <LbSay>{LANG === 'ko' ? <>건반은 <b>조금씩</b> 자랐어요: 61, 68, 73, 78, 85, 88. 작곡가는 자기 피아노의 끝까지 썼어요. 그 끝이 오늘 피아노에서는 <b>가운데</b>일 수도 있어요.</> : <>The keyboard grew <b>a few keys at a time</b>: 61, 68, 73, 78, 85, 88. Composers wrote to the edge of their piano; that edge may sit <b>in the middle</b> of yours.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>내 곡의 가장 높은 음과 가장 낮은 음을 쳐요.</>, <>작곡가의 피아노에 그 건반이 있었는지 찾아요.</>]
        : [<>Play the highest and the lowest note of your piece.</>, <>Find out whether your composer’s piano had those keys.</>]}/>
      <LbRemember>{t('Their edge may be my middle.', '그들의 끝이 나의 가운데일 수 있어요.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Hand, knee, foot', '손, 무릎, 발')}
      teacher={<>{t('From hand stops (Zumpe’s London square, 1767: two, bass and treble) to knee levers (Germany from about 1765; Mozart’s Walter, about 1782–85: two knee levers and a moderator stop) to pedals (Backers’ 1772 grand probably the first; Streicher, Vienna, 1814: both; pedals take over after 1810) to the sostenuto (Boisselot 1844; Albert Steinway’s patent 1874). Markings: Haydn’s first pedal in a score 1794; Beethoven’s first in his first two piano concertos (1795), “with the knee” in a sketch of 1790–92, nearly 800 pedal marks in all; senza sordino opens the “Moonlight” sonata (the dampers raised); una corda on a modern grand strikes two strings of three in the treble. Watch for “senza sordino = without mute”.', '손잡이(춤페의 런던 스퀘어, 1767년: 저음과 고음 두 개)에서 무릎 레버(독일 1765년쯤부터; 모차르트의 발터, 1782–85년쯤: 무릎 레버 둘과 모데라토르 손잡이), 페달(배커스의 1772년 그랜드가 아마 처음; 슈트라이허, 빈, 1814년: 둘 다; 1810년 뒤 페달이 대신함), 소스테누토(부아슬로 1844년; 알베르트 스타인웨이 특허 1874년)까지. 표시: 하이든의 첫 페달 1794년; 베토벤은 피아노 협주곡 1·2번(1795년), 1790–92년 스케치의 “무릎으로”, 모두 800개 가까이; 센차 소르디노로 “월광” 소나타가 시작(댐퍼를 든 채); 현대 그랜드의 우나 코르다는 고음에서 세 줄 중 두 줄. “센차 소르디노 = 약음기 없이”에 주의.')}</>}>
      <LbLive still={<LbPic h={170}>{pedStill}</LbPic>} live={<PedalsPad/>}/>
      <Ps8Careful k="ped"/>
      <LbSay>{LANG === 'ko' ? <>페달은 <b>손</b>에서 <b>무릎</b>으로, 그리고 <b>발</b>로 내려왔어요. 악보의 페달 표시는 그 시대 피아노에 대한 말이에요: <b>그때</b> 무엇을 했는지 읽고, <b>오늘</b> 무엇을 할지 정해요.</> : <>The pedals came down from the <b>hand</b> to the <b>knee</b> to the <b>foot</b>. A pedal marking speaks about its own piano: read what it did <b>then</b>, and decide what to do <b>today</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>내 곡의 페달 표시를 모두 짚어요: 누가 적었나요, 작곡가인가요 편집자인가요?</>, <>한 곳을 표시대로, 한 번은 귀로 정한 대로 쳐 보고, 고르는 이유를 말해요.</>]
        : [<>Point at every pedal marking in your piece: who wrote it, the composer or an editor?</>, <>Play one spot as marked, then as your ear decides, and say why you choose.</>]}/>
      <LbRemember>{t('Hand, knee, foot: read then, decide today.', '손, 무릎, 발: 그때를 읽고, 오늘을 정해요.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Iron, felt and the singing tone', '철, 펠트, 노래하는 소리')}
      teacher={<>{t('Érard’s double escapement (patented 1808 and 1821; still used, modified): quick repeated notes. The iron frame: Babcock’s for the square piano (1825), Broadwood’s iron bars and string plate (1827), Chickering’s one-piece frame for the grand (1843). Pape’s felt hammers (Paris, 1826); conservative Viennese makers covered felt with leather; felt won in the second half of the century. Steinway’s crossed strings (1859). 88 keys by the 1880s. Chopin played Pleyel and Érard and preferred the Pleyel’s more intimate sound; Liszt preferred the Érard’s more dramatic colours (Frederick Collection). The repeat toy’s timings are invented to show the idea.', '에라르의 더블 이스케이프먼트(1808년과 1821년 특허; 지금도 고쳐서 써요): 빠른 반복음. 철 프레임: 배브콕의 스퀘어 피아노용(1825년), 브로드우드의 철 막대와 현 판(1827년), 치커링의 그랜드용 통 프레임(1843년). 파프의 펠트 해머(파리, 1826년); 보수적인 빈 제작자는 펠트에 가죽을 씌웠고, 세기 후반에 펠트가 이겼어요. 스타인웨이의 교차현(1859년). 1880년대 88건반. 쇼팽은 플레옐과 에라르를 쳤고 플레옐의 내밀한 소리를 좋아했어요; 리스트는 에라르의 극적인 색깔을 좋아했어요(프레더릭 컬렉션). 반복 장난감의 시간은 생각을 보여 주려고 정한 것이에요.')}</>}>
      <LbLive still={<LbPic h={170}>{ironStill}</LbPic>} live={<ModernPad/>}/>
      <Ps8Careful k="inv"/>
      <LbDefs items={[
        [t('double escapement', '더블 이스케이프먼트'), t('An action that lets a note sound again before the key has come all the way up.', '건반이 끝까지 올라오기 전에 같은 음을 다시 칠 수 있게 하는 액션.')],
        [t('iron frame', '철 프레임'), t('A cast-iron plate that holds the strings’ huge pull.', '현의 엄청난 당김을 버티는 주철 판.')],
      ]}/>
      <LbPiano steps={LANG === 'ko' ? [<>같은 음을 아주 빠르게 반복해요: 건반이 반쯤만 올라와도 다시 소리 나요.</>, <>두 손으로 큰 화음을 치고 귀 기울여요: 철 프레임과 펠트가 만든 소리예요.</>]
        : [<>Repeat one note very fast: it sounds again with the key only half way up.</>, <>Play a big chord with both hands and listen: that sound is iron and felt.</>]}/>
      <LbRemember>{t('Escapement, iron, felt, crossed strings, 88 keys.', '이스케이프먼트, 철, 펠트, 교차현, 88건반.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Their piano, my choices', '그들의 피아노, 나의 선택')}
      teacher={<>{t('The examined skill: from the instrument to an interpretive choice. For each piece: which piano (action, compass, pedals, hammers, frame), what it could and could not do, and what that changes on a modern grand (range, pedal, touch, tone and balance). The lines “on today’s piano” are the app’s own period lines (the Piano’s Story’s eras). Ask the four questions; expect a reason for every choice.', '시험 보는 능력: 악기에서 해석의 선택으로. 곡마다: 어떤 피아노(액션, 음역, 페달, 해머, 틀), 무엇을 할 수 있었고 없었는지, 그래서 현대 그랜드에서 무엇이 달라지는지(음역, 페달, 터치, 소리와 균형). “오늘의 피아노로” 줄은 앱의 시대별 줄(피아노 이야기의 시대)이에요. 네 가지를 묻고, 선택마다 이유를 기대해요.')}</>}>
      <LbLive still={<LbPic h={170}>{mineStill}</LbPic>} live={<MyPianoPad/>}/>
      <Ps8Careful k="mine"/>
      <LbSay>{LANG === 'ko' ? <>정답은 하나가 아니에요. 시험관이 듣고 싶은 것은 <b>이유</b>예요: “그 피아노는 이랬어요. 그래서 저는 이렇게 쳐요.”</> : <>There is no single right answer. The examiner wants <b>your reason</b>: “That piano did this, so I play it like this.”</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>내 곡의 한 곳을 골라 그 피아노를 생각하며 쳐요.</>, <>“이 곡은 ___를 위해 쓰였어요…” 네 문장으로 소리 내어 말해요.</>]
        : [<>Choose one spot in your piece and play it thinking of that piano.</>, <>Say it aloud in four sentences: “It was written for ___…”</>]}/>
      <LbRemember>{t('Their piano, my reason, my choice.', '그들의 피아노, 나의 이유, 나의 선택.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('For each piece of the programme: the action of its time, the compass against the piece’s range, every pedal marking read then and today, the inventions with dates, and the interpretive choices with reasons.', '프로그램의 곡마다: 그 시대의 액션, 곡의 음역과 건반의 음역, 모든 페달 표시를 그때와 오늘로, 발명과 연도, 이유가 있는 해석의 선택.')}</>}>
      <LbSay>{t('For each piece, tick each one: not yet, nearly, or got it!', '곡마다 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey="pb_ps8_five"/>}/>
    </LbPage>,
  ];
}
function PianoStory8LessonBook() { return <>{ps8LbPages(false)}</>; }
function Ps8Learn({ onStart }) {
  const pages = ps8LbPages(true), opener = pages[0];
  return (
    <Lesson id="piano-story-8" title={bkChapterName('piano-story-8')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="piano-story-8"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
const PS8_LEVELS = [
  { n: 1, label: 'Vienna or London?', kind: 'act', time: 12 },
  { n: 2, label: 'Could it play this note?', kind: 'comp', time: 15 },
  { n: 3, label: 'Read the pedal marking', kind: 'mark', time: 15 },
  { n: 4, label: 'Which invention?', kind: 'inv', time: 12 },
];
Object.assign(LEVEL_KO, { 'Vienna or London?': '빈? 런던?', 'Could it play this note?': '이 음을 칠 수 있었을까?', 'Read the pedal marking': '페달 표시 읽기', 'Which invention?': '어떤 발명?' });
function genPs8Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'act') { let i, g = 0; do { i = Math.floor(Math.random() * PS8_CLUES.length); } while (prev && prev.key === 'a' + i && g++ < 10); return { kind, ci: i, answer: PS8_CLUES[i][0], choices: ['vienna', 'london'], key: 'a' + i, uid }; }
  if (kind === 'comp') { const pool = []; for (let x = 21; x <= 108; x++) if (x < 29 || x > 89) pool.push(x); let m, g = 0; do { m = pick(pool); } while (prev && prev.key === 'c' + m && g++ < 10);
    const a = ps8FirstWith(m)[0], others = shuffle(PS8_COMPASS.map(c => c[0]).filter(x => x !== a)).slice(0, 3); return { kind, m, answer: a, choices: PS8_COMPASS.map(c => c[0]).filter(x => x === a || others.includes(x)), key: 'c' + m, uid }; }
  if (kind === 'mark') { let x, g = 0; do { x = pick(PS8_MARKS); } while (prev && prev.key === x[0] && g++ < 10); return { kind, id: x[0], answer: x[0], choices: shuffle(PS8_MARKS.filter(z => z[0] !== x[0])).slice(0, 3).map(z => z[0]).concat([x[0]]).sort(() => Math.random() - 0.5), key: x[0], uid }; }
  let x, g = 0; do { x = pick(PS8_INV); } while (prev && prev.key === 'i' + x[0] && g++ < 10); return { kind: 'inv', id: x[0], answer: x[0], choices: PS8_INV.map(z => z[0]), key: 'i' + x[0], uid };
}
const ps8Label = (kind, c) => (kind === 'act' ? t(PS8_ACT[c].name[0], PS8_ACT[c].name[1]) : kind === 'comp' ? t(ps8Comp(c)[3][0], ps8Comp(c)[3][1]) : kind === 'mark' ? t(ps8Mark(c)[2][0], ps8Mark(c)[2][1]) : t(ps8Inv(c)[2][0], ps8Inv(c)[2][1]));
function Ps8Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  const grid = (cols, items, fs = 14, left) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 6px',fontSize:fs,fontWeight:900,lineHeight:1.25,textAlign:left ? 'left' : undefined}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  const card = (txt, o = {}) => <div style={{textAlign:'center',margin:'8px auto',maxWidth:420,padding:'12px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff',fontSize:o.fs || 15,fontWeight:800,fontStyle:o.it ? 'italic' : undefined,fontFamily:o.serif ? LB_SERIF : undefined,color:BK.ink,lineHeight:1.4}}>{txt}</div>;
  let title, body;
  if (q.kind === 'act') { title = t('Vienna or London?', '빈일까요, 런던일까요?'); body = <>{card(t(PS8_CLUES[q.ci][1], PS8_CLUES[q.ci][2]))}{grid(2, q.choices.map(c => [c, ps8Label('act', c)]), 16)}</>; }
  else if (q.kind === 'comp') { title = t('A ' + ps8NoteName(q.m) + ': which is the first keyboard here that has it?', ps8NoteName(q.m) + ': 이 음이 있는 가장 이른 건반은?'); body = <><Ps8Ladder sel={done ? q.answer : null} mark={q.m} rows={done}/>{grid(2, q.choices.map(c => [c, ps8Label('comp', c)]), 13)}</>; }
  else if (q.kind === 'mark') { title = t('What does it ask for?', '무엇을 하라는 걸까요?'); body = <>{card(ps8Mark(q.id)[1], { fs: 24, it: true, serif: true })}{grid(1, q.choices.map(c => [c, ps8Label('mark', c)]), 13, true)}</>; }
  else { title = t('Which invention gave this?', '어떤 발명이 이것을 주었을까요?'); body = <>{card(t(ps8Inv(q.id)[4][0], ps8Inv(q.id)[4][1]))}{grid(2, q.choices.map(c => [c, ps8Label('inv', c)]), 13.5)}</>; }
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {body}
  </div>);
}
const ps8AnswerLabel = (q) => ps8Label(q.kind, q.answer);
Object.assign(PIANO_STORY_8_DRILL, { levels: PS8_LEVELS, generate: genPs8Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: ps8AnswerLabel, Question: Ps8Question, Learn: Ps8Learn });
function Ps8Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="piano-story-8" teacher>{content}</WbPage>);
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('piano-story-8')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>The diplomas’ fifth area of general knowledge: the construction and development of the piano and what it means for the repertoire, as the ground for the candidate’s interpretive choices. Every fact here is listed with its source in the room’s research note (sc/research33-2-piano.md). The pads’ sounds are sketches of a difference, and the repeat toy’s timings are invented: neither is a recording or a measurement.</div>
    <TcBlock page={2} title="Vienna and London" answers={<>{tcAns('VIENNA', ['Stein (Augsburg, about 1769), Walter (Vienna, 1780s)', 'hammer on the key, head to the player', 'a rail flicks it up', 'light, elastic touch; knee levers', 'Mozart bought a Walter about 1783'], null)}{tcAns('LONDON', ['Backers (1776), Stodart (1777), Broadwood (1780)', 'hammer on its own rail, head away from the player', 'a jack pushes it', 'heavier, louder; Backers’ 1772 grand probably the first with pedals'], null)}</>}
      watch="“English pianos were better.” Heavier and louder, not better: the Viennese touch is the one Haydn, Mozart and Beethoven knew."
      say="“Vienna: light and quick. London: heavier and louder.”"/>
    <TcBlock page={3} title="The keyboard grows" answers={<>{tcAns('THE COMPASSES', PS8_COMPASS.map(r => ps8Keys(r) + ' keys, ' + ps8NoteName(r[1]) + '–' + ps8NoteName(r[2]) + ': ' + r[3][0] + ' (' + r[4][0] + ')'), null)}</>}
      watch="“88 keys since Mozart.” Mozart had 61; Beethoven at most 78; seven octaves about 1850, 88 by the 1880s."
      say="“Their edge may be my middle.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Hand, knee, foot" answers={<>{tcAns('THE YEARS', PS8_PSTOPS.map(s => s[0] + ' ' + s[1][0] + ': ' + s[2][0]), null)}{tcAns('THE MARKINGS', PS8_MARKS.map(m => m[1] + ': ' + m[2][0]), null)}</>}
      watch="“Senza sordino means without mute.” On the piano the sordini are the dampers: senza sordino is the right pedal. And una corda on a modern grand strikes two strings, not one."
      say="“Hand, knee, foot: read then, decide today.”"/>
    <TcBlock page={5} title="Iron, felt and the singing tone" answers={<>{tcAns('THE INVENTIONS', PS8_INV.map(x => x[1] + ' ' + x[2][0] + (x[3][0] ? ' (' + x[3][0] + ')' : '') + ': ' + x[4][0]), null)}</>}
      watch="“The iron frame was invented in 1859.” It came in steps (1825, 1827, 1843); 1859 is Steinway’s crossed strings."
      say="“Escapement, iron, felt, crossed strings, 88 keys.”"/>
    <TcBlock page={6} title="Their piano, my choices" answers={<>{tcAns('ASK', PS8_ASK.map(a => a[1][0]), null)}</>}
      watch="A fact with no choice after it. Every answer ends with “so I play it …”."
      say="“Their piano, my reason, my choice.”"/>
    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>For each piece of the programme, from the full score: the action, the compass against the piece’s range, every pedal marking then and today, the inventions with dates, and the choices with reasons.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['piano-story-8'] = Ps8Teacher;
// a small 88-key strip for paper: the whole keyboard, nothing shaded (the student shades)
const ps8Strip = (w = 300, sel, mark) => <div style={{width:w,maxWidth:'100%'}}><Ps8Ladder sel={sel} mark={mark} rows={false} kw={7}/></div>;
function Ps8Workbook({ startNo = 1 }) {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="piano-story-8">{content}</WbPage>);
  const line = (lab, w, h = 30) => <div style={{display:'grid',gridTemplateColumns:(w || 170) + 'px 1fr',gap:8,alignItems:'end',fontSize:12.5,fontWeight:800,color:BK.ink,margin:'4px 0'}}><span>{lab}</span><span style={{borderBottom:'1.5px solid rgba(38,41,107,0.45)',height:h}}/></div>;
  P(<>
    <WbTop step={1}/>
    <Part kind="home" title="Vienna and London" how="Fill in the table from the step, then label each drawing.">
      <div style={{display:'grid',gridTemplateColumns:'150px 1fr 1fr',border:'1.5px solid ' + BK.ink,borderRadius:6,overflow:'hidden',fontSize:12.5,fontWeight:800,color:BK.ink}}>
        {[['', 'Vienna', 'London'], ['Who built it, and when', '', ''], ['Where the hammer sits', '', ''], ['Which way its head points', '', ''], ['How the dampers are lifted', '', ''], ['Who played it', '', '']].map((r, i) => r.map((c, j) => <div key={i + '-' + j} style={{padding:'6px 8px',minHeight:i ? 34 : 0,borderTop:i ? '1px solid ' + BK.line : 'none',borderLeft:j ? '1px solid ' + BK.line : 'none',background:i === 0 ? 'rgba(38,41,107,0.06)' : '#fff',fontFamily:i === 0 ? LB_SERIF : undefined,fontSize:i === 0 ? 15 : 12}}>{c}</div>))}
      </div>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,marginTop:10}}>{['vienna', 'london'].map(k => <div key={k}><Ps8Action kind={k} ph={0} w={260} label={false}/>{line('This is the', 80, 22)}</div>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="home" title="The keyboard grows" how="Shade each keyboard’s compass on its strip, and write how many keys it had.">
      {PS8_COMPASS.filter(r => ['five', 'erard', 'graf', 'today'].includes(r[0])).map(r => <div key={r[0]} style={{display:'grid',gridTemplateColumns:'170px 1fr 70px',gap:8,alignItems:'center',margin:'6px 0'}}><span style={{fontSize:12.5,fontWeight:800,color:BK.ink}}>{r[3][0]}<br/><span style={{color:BK.muted,fontWeight:700}}>{ps8NoteName(r[1])}–{ps8NoteName(r[2])}</span></span>{ps8Strip(330)}{bkBox(60, 24)}</div>)}
    </Part>
    <Part kind="home" title="My piece" how="With your score open.">
      {line('Highest note, lowest note')}{line('My composer’s piano had (keys)')}{line('Where my piece meets that piano’s edge')}
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="home" title="Read the markings" how="What does each one ask for, then and today?">
      {PS8_MARKS.map(m => <div key={m[0]} style={{display:'grid',gridTemplateColumns:'130px 1fr',gap:8,alignItems:'end',margin:'5px 0'}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:15,fontWeight:900,color:BK.ink}}>{m[1]}</span><span style={{borderBottom:'1.5px solid rgba(38,41,107,0.45)',height:28}}/></div>)}
    </Part>
    <Part kind="home" title="The inventions" how="Write the year under each invention, then number them in order.">
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,1fr)',gap:8}}>{[2, 0, 4, 1, 3].map(k => PS8_INV[k]).concat([['', '', ['Pedals instead of knee levers (the first)', ''], ['', ''], ['', '']]]).map((x, i) => <div key={i} style={{border:'1px solid ' + BK.line,borderRadius:6,padding:'6px 8px',fontSize:12,fontWeight:800,color:BK.ink,display:'grid',gap:4}}>{x[2][0]}{bkBox(90, 22)}</div>)}</div>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={5}/>
    <Part kind="together" title="My piece’s piano" how="One for each piece of the programme. Then say it aloud in four sentences.">
      {[1, 2].map(n => <div key={n} style={{margin:'4px 0 10px'}}>{line('Piece ' + n + ', composer, year')}{line('The piano it was written for')}{line('It could … but not …', 0, 36)}{line('So on today’s grand I …', 0, 36)}</div>)}
    </Part>
    <Faces/>
  </>);
  P(<Ps8PaperCheck/>);
  return <>{pages}</>;
}
function Ps8PaperCheck() {
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Vienna or London? Write V or L')}
    <BkGrid cols={2} gap="6px 8px">{[0, 1, 4, 5].map((k, i) => <BkCell key={k} n={i + 1}><div style={{display:'grid',gridTemplateColumns:'1fr auto',gap:8,alignItems:'center',padding:'14px 2px 2px',fontSize:12,fontWeight:800,color:BK.ink}}>{PS8_CLUES[k][1]}{bkBox(30, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('B', 'Which is the first keyboard that has this note? Write its number of keys (61, 68, 73, 78, 85, 88)')}
    <BkGrid cols={3} gap="6px 8px">{[96, 24, 108].map((m, i) => <BkCell key={m} n={i + 5}><div style={{display:'grid',gap:4,padding:'14px 2px 2px',fontSize:12,fontWeight:800,color:BK.ink}}>{ps8NoteName(m)}{ps8Strip(190, null, m)}{bkBox(60, 22)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'What does it ask for?')}
    <BkGrid cols={2} gap="6px 8px">{['senza', 'una', 'tre', 'sost'].map((id, i) => <BkCell key={id} n={i + 8}><div style={{display:'grid',gap:6,padding:'14px 2px 2px'}}><span style={{fontFamily:LB_SERIF,fontStyle:'italic',fontSize:15,fontWeight:900,color:BK.ink}}>{ps8Mark(id)[1]}</span><span style={{borderBottom:'1.5px solid rgba(38,41,107,0.45)',height:24}}/></div></BkCell>)}</BkGrid>
    {bkSec('D', 'Which invention? Write its year')}
    <BkGrid cols={2} gap="6px 8px">{['esc', 'felt', 'cross', 'k88'].map((id, i) => <BkCell key={id} n={i + 12}><div style={{display:'grid',gridTemplateColumns:'1fr auto',gap:8,alignItems:'center',padding:'14px 2px 2px',fontSize:12,fontWeight:800,color:BK.ink}}>{ps8Inv(id)[4][0]}{bkBox(70, 22)}</div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['piano-story-8'] = Ps8Workbook;
