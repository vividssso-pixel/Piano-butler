
// ─── Chapter: Knowing Your Pieces, Grade 8 and Diplomas (Build DQ, 2026-10-31; board call 33-1, the fourth Grade 8 room) ───
// The general knowledge of the Certificate of Performance and the diplomas (Piano syllabus 2026, Section II): the significance of
// titles and every marking; the composer's life, influences, impact and output; the period, its style and its performance
// conventions; the structure, keys, melodic and harmonic language and climax points; the piano of the time and what it did to the
// repertoire; and all of it as the ground for the candidate's own interpretive choices. The room reuses the app's own data: the map
// from the Grade 7 room, the eras' conventions from the piano's story (ERAS), the piano's own timeline (PIANO_TIMELINE).
// ── step 1: the arc of my piece: the climax, the keys on the way, the language ──
const PA_LANG = [['dia', 'Diatonic', '온음계적'], ['chr', 'Chromatic', '반음계적'], ['mod', 'Modal', '선법적'], ['wt', 'Whole tone', '온음 음계'], ['ato', 'Atonal', '무조'], ['ext', 'Added-note and jazz chords', '부가음·재즈 화음']];
const paLoad = () => { try { return JSON.parse(localStorage.getItem('pb_piece_arc') || 'null') || null; } catch (e) { return null; } };
const paSave = (v) => { try { localStorage.setItem('pb_piece_arc', JSON.stringify(v)); } catch (e) {} };
// the arc: one column per section, the line through their tensions; the highest point is the climax (hidden in a quiz)
function PaArc({ secs, ten, w = 460, h = 120, quiz, sel, mark }) {
  const n = secs.length, top = Math.max(...ten), ci = ten.indexOf(top), cw = w / n;
  const pts = ten.map((v, i) => [cw * i + cw / 2, h - 22 - (v - 1) * ((h - 46) / 4)]);
  const d = pts.map((p, i) => (i ? 'L' : 'M') + p[0].toFixed(1) + ' ' + p[1].toFixed(1)).join(' ');
  const hot = (i) => (quiz ? mark === i : i === ci);
  return <svg viewBox={'0 0 ' + w + ' ' + h} style={{width:'100%',maxWidth:w,display:'block',margin:'4px auto'}} role="img" aria-label={t('The arc of the piece', '곡의 곡선')} data-pa-arc>
    {secs.map((x, i) => <g key={i}><rect x={cw * i + 1} y={2} width={cw - 2} height={h - 4} rx={4} fill={sel === i ? '#fbe3da' : '#fff'} stroke={sel === i ? BK.coral : BK.line} strokeWidth={sel === i ? 1.6 : 1}/><text x={cw * i + cw / 2} y={h - 6} textAnchor="middle" fontSize="12" fontWeight="900" fill={BK.ink} fontFamily="Georgia, serif">{x[0]}</text></g>)}
    <path d={d} fill="none" stroke={BK.ink} strokeWidth="2.2" strokeLinejoin="round"/>
    {pts.map((p, i) => <circle key={i} cx={p[0]} cy={p[1]} r={hot(i) ? 6 : 3.5} fill={hot(i) ? BK.coral : BK.ink}/>)}
  </svg>;
}
function PieceArcMaker() {
  const secs = pmLoad() || PM_PRESETS.ternary.map(x => x.slice());
  const [st, setSt] = useState(() => paLoad() || { ten: [], lang: [], path: '' });
  const ten = secs.map((_, i) => st.ten[i] || (i === Math.floor(secs.length / 2) ? 4 : 2));
  const upd = (v) => { const n = { ...st, ...v }; setSt(n); paSave(n); };
  const top = Math.max(...ten), ci = ten.indexOf(top), cx = secs[ci];
  const inp = { width:'100%', minWidth:0, padding:'8px 8px', fontSize:14.5, fontWeight:700, border:'1.5px solid rgba(38,41,107,0.3)', borderRadius:8, color:BK.ink, background:'#fff', boxSizing:'border-box' };
  return (
    <div className="try-box" style={actBox} data-pm="arc">
      <div style={actTitle}>{t('The arc of my piece', '내 곡의 곡선')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>부분마다 <b>긴장</b>을 1에서 5까지 눌러요. 가장 높은 곳이 <b>클라이맥스</b>예요. 그다음 그리로 가는 조와, 화성의 말투를 적어요. 부분은 내 곡의 지도(7급 방)에서 가져와요; 이 기기에 저장돼요.</> : <>Tap each section's <b>tension</b>, 1 to 5. The highest point is <b>the climax</b>. Then write the keys that lead there, and the language of its harmony. The sections come from your map (the Grade 7 room); saved on this device.</>}</div>
      <PaArc secs={secs} ten={ten}/>
      <div style={{display:'grid',gridTemplateColumns:'repeat(' + secs.length + ',minmax(0,1fr))',gap:4,margin:'2px 0 6px'}}>{secs.map((x, i) => <div key={i} style={{display:'grid',gap:3,justifyItems:'center'}}>{[5, 4, 3, 2, 1].map(v => <button key={v} data-pa-ten={i + ':' + v} onClick={() => upd({ ten: secs.map((_, k) => (k === i ? v : ten[k])) })} aria-label={x[0] + ': ' + v} aria-pressed={ten[i] === v} style={{width:28,height:20,borderRadius:5,border:'1.5px solid ' + (ten[i] >= v ? BK.ink : BK.line),background:ten[i] >= v ? (v === top && i === ci ? BK.coral : BK.ink) : '#fff',cursor:'pointer',padding:0}}/>)}</div>)}</div>
      {spMsg(t('The climax: ' + cx[0] + ' (bars ' + cx[1] + '–' + cx[2] + ')', '클라이맥스: ' + cx[0] + ' (' + cx[1] + '–' + cx[2] + '마디)'), BK.coral)}
      <label style={{display:'grid',gap:2,fontSize:11.5,fontWeight:900,color:BK.muted,marginTop:6}}>{t('The keys on the way (home → … → home)', '가는 길의 조 (집 → … → 집)')}<input value={st.path} onChange={(e) => upd({ path: e.target.value })} placeholder={t('e.g. D → A → B minor → D', '예: D → A → B단조 → D')} style={inp}/></label>
      <div style={{fontSize:11.5,fontWeight:900,color:BK.muted,margin:'8px 0 4px'}}>{t('Its language (as many as fit)', '그 말투 (맞는 만큼)')}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>{PA_LANG.map(([id, en, ko]) => { const on = st.lang.includes(id); return <button key={id} className={'chip' + (on ? ' active' : '')} aria-pressed={on} style={{minHeight:40,padding:'6px 12px'}} onClick={() => upd({ lang: on ? st.lang.filter(x => x !== id) : st.lang.concat([id]) })}>{t(en, ko)}</button>; })}</div>
    </div>
  );
}
// an arc for the drill: four to six sections, one clear top
const paQuizArc = (prev) => { let secs, ten, g = 0;
  do { const n = 4 + Math.floor(Math.random() * 3), names = n === 4 ? ['A', 'B', 'A', 'Coda'] : n === 5 ? ['A', 'B', 'A', 'C', 'A'] : ['Intro', 'A', 'B', 'A', 'C', 'A']; const ci = 1 + Math.floor(Math.random() * (n - 2));
    ten = names.map((_, i) => (i === ci ? 5 : 1 + Math.floor(Math.random() * 3))); secs = names.map((x, i) => [x, i * 8 + 1, i * 8 + 8, '']);
  } while (prev && prev.key === ten.join('') && g++ < 10);
  return { secs, ten, answer: ten.indexOf(5), key: ten.join('') }; };
// ── step 2: what the title promises ──
// the words on the title page and what each one promises (dictionary meanings; the board lists them for her check)
const P8_TITLES = [
  ['nocturne', 'Nocturne', '녹턴', 'A night piece: a singing melody over a quiet, flowing left hand.', '밤의 곡: 조용히 흐르는 왼손 위에서 노래하는 선율.'],
  ['etude', 'Étude', '연습곡', 'A study: one technical problem, made into music.', '연습곡: 기술 문제 하나를 음악으로 만든 것.'],
  ['prelude', 'Prelude', '전주곡', 'An opening piece, or a short free piece on its own; it once came before a fugue or a suite.', '여는 곡, 또는 그 자체로 짧고 자유로운 곡; 원래는 푸가나 모음곡 앞에 왔어요.'],
  ['impromptu', 'Impromptu', '즉흥곡', 'As if made up on the spot: free in shape, but written out in full.', '그 자리에서 지어낸 듯: 모양은 자유롭지만 다 적혀 있어요.'],
  ['toccata', 'Toccata', '토카타', 'A "touch" piece: fast and brilliant, showing the fingers.', '"만지는" 곡: 빠르고 화려하게, 손가락을 보여 줘요.'],
  ['scherzo', 'Scherzo', '스케르초', 'A "joke": fast, in 3, often with a sudden change of mood.', '"농담": 빠르고 3박자, 흔히 기분이 갑자기 바뀌어요.'],
  ['barcarolle', 'Barcarolle', '뱃노래', 'A boat song: a rocking 6/8, like a gondola on the water.', '뱃노래: 물 위의 곤돌라처럼 흔들리는 6/8.'],
  ['intermezzo', 'Intermezzo', '간주곡', 'An "in-between" piece: short, lyrical, often reflective.', '"사이의" 곡: 짧고 서정적이며, 흔히 사색적.'],
  ['ballade', 'Ballade', '발라드', 'A story told in music: contrasting episodes that build to a dramatic end.', '음악으로 들려주는 이야기: 대비되는 장면들이 극적인 끝으로 쌓여요.'],
  ['mazurka', 'Mazurka', '마주르카', 'A Polish dance in 3, its accent often on the second or third beat.', '폴란드 춤곡, 3박자, 악센트가 흔히 둘째나 셋째 박에.'],
  ['polonaise', 'Polonaise', '폴로네즈', 'A stately Polish dance in 3, with its own repeated rhythm.', '당당한 폴란드 춤곡, 3박자, 특유의 리듬이 되풀이돼요.'],
  ['sonata', 'Sonata', '소나타', '"Sounded", played rather than sung: a large work in several movements.', '"울리는", 노래가 아니라 연주하는 것: 여러 악장의 큰 작품.'],
  ['fantasia', 'Fantasia', '환상곡', 'Free in form, as if improvised: the imagination leads.', '형식이 자유롭고 즉흥 같은 곡: 상상이 이끌어요.'],
  ['rhapsody', 'Rhapsody', '광시곡', 'One movement, free and in episodes, often from folk tunes.', '한 악장, 자유롭고 장면장면으로, 흔히 민요에서.'],
  ['bagatelle', 'Bagatelle', '바가텔', 'A "trifle": a short, light piece.', '"하찮은 것": 짧고 가벼운 곡.'],
  ['invention', 'Invention', '인벤션', 'A short piece grown from one idea, passed between the hands.', '한 가지 생각에서 자라난 짧은 곡, 두 손이 주고받아요.'],
  ['variations', 'Variations', '변주곡', 'One theme, then the same theme in new clothes, again and again.', '주제 하나, 그다음 같은 주제가 새 옷을 입고 또 또.'],
  ['berceuse', 'Berceuse', '자장가', 'A lullaby: soft and rocking, over one repeated bass.', '자장가: 부드럽게 흔들리며, 되풀이되는 베이스 위에서.'],
];
const p8Title = (id) => P8_TITLES.find(x => x[0] === id);
function TitlePad({ onResult, fixed }) {
  const [id, setId] = useState(fixed ? fixed.id : 'nocturne'), [quiz, setQuiz] = useState(!!fixed), [opts, setOpts] = useState(fixed ? fixed.opts : null), [ans, setAns] = useState(null);
  const x = p8Title(id);
  const ask = () => { let y, g = 0; do { y = pick(P8_TITLES)[0]; } while (y === id && g++ < 10); setId(y); setOpts(shuffle(P8_TITLES.filter(z => z[0] !== y)).slice(0, 3).map(z => z[0]).concat([y]).sort(() => Math.random() - 0.5)); setQuiz(true); setAns(null); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === id }); };
  return (
    <div className="try-box" style={actBox} data-pm="title">
      <div style={actTitle}>{t('What the title promises', '제목이 약속하는 것')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>시험관은 <b>제목의 뜻</b>을 물어요: 녹턴, 발라드, 간주곡은 각각 무엇을 약속할까요? 단어를 눌러 보고, 내 곡의 제목부터 말해 봐요.</> : <>The examiner asks what <b>the title means</b>: what does a nocturne, a ballade, an intermezzo promise? Tap a word; then say your own piece's title first.</>}</div>
      {!quiz && <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginBottom:8}}>{P8_TITLES.map(([k, en, ko]) => <button key={k} className={'chip' + (k === id ? ' active' : '')} aria-pressed={k === id} style={{minHeight:38,padding:'5px 11px'}} onClick={() => setId(k)}>{t(en, ko)}</button>)}</div>}
      <div style={{textAlign:'center',margin:'6px auto',maxWidth:420,padding:'14px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff'}}>
        {(!quiz || ans) && <div style={{fontFamily:LB_SERIF,fontSize:22,fontWeight:900,color:BK.ink}}>{t(x[1], x[2])}</div>}
        <div style={{fontSize:14.5,color:BK.ink,lineHeight:1.45,marginTop:4}}>{t(x[3], x[4])}</div>
      </div>
      {quiz && !ans && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,marginTop:6}}>{opts.map(k => <button key={k} className="choice-btn" onClick={() => say(k)} style={{padding:'10px 4px',fontSize:14,fontWeight:900}}>{t(p8Title(k)[1], p8Title(k)[2])}</button>)}</div>}
      {spMsg(ans ? (ans === id ? t('Yes: a ' + x[1].toLowerCase() + '.', '맞아요: ' + x[2] + '.') : t('It is a ' + x[1].toLowerCase() + '.', '정답은 ' + x[2] + '.')) : quiz ? t('Which title promises this?', '이것을 약속하는 제목은?') : '', ans ? (ans === id ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Which title?', '▶ 어떤 제목일까?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── step 3: how they played it then: the performance conventions of each period (from the piano's story) ──
const P8_ERAS = ['baroque', 'classical', 'romantic', 'modern'];
const p8Era = (id) => ERAS.find(e => e.id === id);
function ConventionsPad({ onResult, fixed }) {
  const [id, setId] = useState(fixed ? fixed.id : 'baroque'), [quiz, setQuiz] = useState(!!fixed), [ti, setTi] = useState(fixed ? fixed.ti : 0), [ans, setAns] = useState(null);
  const e = p8Era(id);
  const ask = () => { let y, g = 0; do { y = pick(P8_ERAS); } while (y === id && g++ < 10); setId(y); setTi(Math.floor(Math.random() * p8Era(y).traits.length)); setQuiz(true); setAns(null); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === id }); };
  return (
    <div className="try-box" style={actBox} data-pm="conv">
      <div style={actTitle}>{t('How they played it then', '그때는 어떻게 쳤을까')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>디플로마는 그 시대의 <b>연주 관습</b>을 물어요: 꾸밈음, 페달, 루바토, 터치. 시대를 눌러 그 특징과, 오늘 피아노로 칠 때의 길을 읽어요.</> : <>The diplomas ask about the <b>performance conventions</b> of the time: ornaments, pedal, rubato, touch. Tap a period for its features and the way to play it on today's piano.</>}</div>
      {!quiz && spChips(P8_ERAS.map(k => [k, p8Era(k).short + ' ' + p8Era(k).years]), id, setId)}
      {quiz && !ans ? <div style={{textAlign:'center',margin:'6px auto',maxWidth:420,padding:'14px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff',fontSize:16,fontWeight:800,color:BK.ink,lineHeight:1.4}}>{e.traits[ti]}</div>
        : <div style={{margin:'6px auto',maxWidth:460,padding:'10px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff'}}>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:900,color:BK.ink}}>{e.name} <span style={{fontSize:13,color:BK.muted,fontWeight:800}}>{e.years}</span></div>
          <div style={{fontSize:12.5,fontWeight:800,color:BK.muted,margin:'2px 0 4px'}}>{e.inst}</div>
          <ul style={{margin:'0 0 6px',paddingLeft:18,fontSize:14,color:BK.ink,lineHeight:1.45}}>{e.traits.map((x, i) => <li key={i} style={{fontWeight:quiz && ans && i === ti ? 900 : 600}}>{x}</li>)}</ul>
          <div style={{fontSize:13.5,color:BK.coral,fontWeight:800,lineHeight:1.4}}>{e.today}</div>
        </div>}
      {quiz && !ans && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,marginTop:6}}>{P8_ERAS.map(k => <button key={k} className="choice-btn" onClick={() => say(k)} style={{padding:'10px 4px',fontSize:14,fontWeight:900}}>{p8Era(k).short}</button>)}</div>}
      {spMsg(ans ? (ans === id ? t('Yes: ' + e.short + '.', '맞아요: ' + e.short + '.') : t('That is ' + e.short + '.', '정답은 ' + e.short + '.')) : quiz ? t('Which period plays like this?', '어느 시대의 연주일까요?') : '', ans ? (ans === id ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Which period?', '▶ 어느 시대일까?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── step 4: the piano of the time: six stops on the piano's own timeline, and what each one let composers do ──
// [timeline index, the clue (what this piano could do), the period whose composers wrote for it]
const P8_PIANOS = [
  [0, 'Strings plucked by quills: pressing harder does not make it louder, so loud and soft come in blocks.', '깃촉이 현을 뜯어요: 세게 눌러도 커지지 않아서, 셈여림이 덩어리로 바뀌어요.', 'baroque'],
  [1, 'Hammers that fall back after striking: soft and loud from the same key, for the first time.', '치고 나서 되돌아오는 해머: 같은 건반에서 처음으로 여리게도 세게도.', null],
  [4, 'Light, quick and clear, about five octaves: a tune with a quiet accompaniment sits well on it.', '가볍고 빠르고 또렷하며 약 5옥타브: 조용한 반주 위의 선율이 잘 어울려요.', 'classical'],
  [5, 'Six octaves and more; a note can be repeated before the key comes all the way up.', '6옥타브 이상; 건반이 다 올라오기 전에 같은 음을 다시 칠 수 있어요.', null],
  [6, 'A cast-iron frame and crossed strings: thick, tight strings and a big singing tone that carries the pedal.', '주철 프레임과 교차된 현: 굵고 팽팽한 현, 페달을 받쳐 주는 크게 노래하는 소리.', 'romantic'],
  [7, 'Seven and a quarter octaves, A0 to C8: the keyboard you play today, from the lowest growl to the highest sparkle.', '7과 1/4옥타브, A0부터 C8까지: 오늘 치는 바로 그 건반, 가장 낮은 울림부터 가장 높은 반짝임까지.', 'modern'],
];
const p8PianoName = (k) => { const e = PIANO_TIMELINE[P8_PIANOS[k][0]]; return e.y + ' · ' + e.t; };
function PianoOfTimePad({ onResult, fixed }) {
  const [k, setK] = useState(fixed ? fixed.k : 0), [quiz, setQuiz] = useState(!!fixed), [ans, setAns] = useState(null);
  const e = PIANO_TIMELINE[P8_PIANOS[k][0]], era = P8_PIANOS[k][3] ? p8Era(P8_PIANOS[k][3]) : null;
  const ask = () => { let y, g = 0; do { y = Math.floor(Math.random() * P8_PIANOS.length); } while (y === k && g++ < 10); setK(y); setQuiz(true); setAns(null); };
  const say = (v) => { if (!quiz || ans != null) return; setAns(v); if (onResult) onResult({ ok: v === k }); };
  return (
    <div className="try-box" style={actBox} data-pm="piano">
      <div style={actTitle}>{t('The piano of the time', '그 시대의 피아노')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>곡은 <b>그때의 피아노</b>를 위해 쓰였어요: 몇 옥타브였는지, 소리가 얼마나 오래 울렸는지, 페달이 있었는지. 정거장을 눌러 보고, 내 곡의 작곡가가 어느 피아노 앞에 앉았는지 찾아요. 긴 이야기는 다락방의 피아노 이야기 방에.</> : <>A piece was written for <b>the piano of its time</b>: how many octaves it had, how long its sound lasted, whether it had pedals. Tap a stop, and find which piano your composer sat at. The long story is in the attic, in the piano's story room.</>}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(6,minmax(0,1fr))',gap:4,margin:'4px 0 8px'}}>{P8_PIANOS.map((p, i) => { const on = !quiz || ans != null ? i === k : false, badOne = quiz && ans != null && ans === i && i !== k;
        return <button key={i} data-p8-stop={i} onClick={() => (quiz ? say(i) : setK(i))} aria-pressed={on} style={{padding:'8px 2px',borderRadius:8,cursor:'pointer',textAlign:'center',border:'1.5px solid ' + (on ? (quiz ? BK.green : BK.coral) : badOne ? BK.coral : BK.line),background:on ? (quiz ? BK.greenSoft : '#fbe3da') : '#fff',fontFamily:'inherit',color:BK.ink,minWidth:0}}>
          <div style={{fontSize:11,fontWeight:900,color:BK.coral}}>{PIANO_TIMELINE[p[0]].y}</div><div style={{fontSize:11.5,fontWeight:900,lineHeight:1.15}}>{quiz && ans == null ? '?' : PIANO_TIMELINE[p[0]].t}</div></button>; })}</div>
      <div style={{margin:'6px auto',maxWidth:460,padding:'10px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff'}}>
        <div style={{fontSize:14.5,fontWeight:800,color:BK.ink,lineHeight:1.45}}>{t(P8_PIANOS[k][1], P8_PIANOS[k][2])}</div>
        {(!quiz || ans != null) && <div style={{fontSize:13,color:BK.muted,lineHeight:1.45,marginTop:4}}>{e.d}</div>}
        {(!quiz || ans != null) && era && <div style={{fontSize:13.5,color:BK.coral,fontWeight:800,marginTop:4}}>{t('Written for it: ', '이 피아노를 위해 쓴 사람: ') + era.composers.join(', ')}</div>}
      </div>
      {spMsg(ans != null ? (ans === k ? t('Yes: ' + p8PianoName(k) + '.', '맞아요: ' + p8PianoName(k) + '.') : t('It is ' + p8PianoName(k) + '.', '정답은 ' + p8PianoName(k) + '.')) : quiz ? t('Which piano is this? Tap the stop.', '어떤 피아노일까요? 정거장을 눌러요.') : '', ans != null ? (ans === k ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Which piano?', '▶ 어떤 피아노일까?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── step 5: viva cards: the examiner's questions, asked by yourself, answered aloud ──
// [id, area, the question, what a full answer covers] -- the five areas of the diploma general knowledge, and the interpretive choice
const P8_VIVA = [
  ['v-title', 'terms', ['What does the title mean, and what does it promise?', '제목은 무슨 뜻이고, 무엇을 약속하나요?'], ['the word, its origin, what the listener expects', '단어, 그 유래, 듣는 이가 기대하는 것']],
  ['v-mark', 'terms', ['Pick any marking on the first page: what does it ask for, and how do you do it?', '첫 쪽의 표시 하나를 골라요: 무엇을 요구하고, 어떻게 하나요?'], ['the term, the sound it wants, the way your hand makes it', '용어, 원하는 소리, 손이 그걸 만드는 방법']],
  ['v-map', 'structure', ['Draw the map: sections, bars and keys.', '지도를 그려요: 부분, 마디, 조.'], ['letters, bar numbers, the key of each section, the form’s name', '글자, 마디 번호, 부분마다 조, 형식의 이름']],
  ['v-climax', 'structure', ['Where is the climax, and how does the music get there?', '클라이맥스는 어디이고, 음악은 어떻게 거기에 이르나요?'], ['the bar, the keys on the way, texture and register, the harmony’s language', '마디, 가는 길의 조, 짜임새와 음역, 화성의 말투']],
  ['v-period', 'context', ['Which period, and which features of the music place it there?', '어느 시대이고, 음악의 어떤 특징이 그렇게 말해 주나요?'], ['the dates, two or three features in the score, other music of the time', '연도, 악보 속 특징 두세 가지, 그 시대의 다른 음악']],
  ['v-conv', 'context', ['Which performance conventions of the time shape how you play it?', '그 시대의 어떤 연주 관습이 내 연주를 결정하나요?'], ['ornaments, pedal, rubato, touch, repeats', '꾸밈음, 페달, 루바토, 터치, 반복']],
  ['v-from', 'composer', ['Who influenced this composer, and whom did they influence?', '이 작곡가는 누구에게 영향을 받았고, 누구에게 영향을 주었나요?'], ['teachers and models, what was passed on, the later composers who took it up', '스승과 본보기, 물려준 것, 그것을 이어받은 뒤의 작곡가']],
  ['v-output', 'composer', ['What else did they write, and where does this piece sit in their output?', '그 밖에 무엇을 썼고, 이 곡은 작품 전체에서 어디에 있나요?'], ['for piano and beyond, early or late, typical or unusual', '피아노곡과 그 너머, 초기인지 후기인지, 전형적인지 특이한지']],
  ['v-piano', 'piano', ['What piano was this written for, and what could it do, or not do?', '어떤 피아노를 위해 썼고, 그 피아노는 무엇을 할 수 있었나요, 없었나요?'], ['octaves, sustain, pedals, the weight of the touch', '옥타브, 울림의 길이, 페달, 터치의 무게']],
  ['v-today', 'piano', ['What does that change in how you play it on a modern piano?', '그것이 현대 피아노로 칠 때 무엇을 바꾸나요?'], ['pedal, balance, tempo, ornaments', '페달, 균형, 빠르기, 꾸밈음']],
  ['v-choice', 'choice', ['Name one interpretive choice you make, and its reason from the score or its history.', '내가 하는 해석의 선택 하나와, 악보나 역사에서 온 그 이유를 말해요.'], ['the choice, the evidence, what it does for the listener', '선택, 근거, 듣는 이에게 주는 것']],
];
const P8_AREAS = { terms: ['Titles and terms', '제목과 용어'], structure: ['Structure and climax', '구조와 클라이맥스'], context: ['Period and conventions', '시대와 관습'], composer: ['The composer', '작곡가'], piano: ['The piano of the time', '그 시대의 피아노'], choice: ['My choices', '나의 선택'] };
const VIVA_KEY = 'pb_p8_viva';
function VivaCards() {
  const [all, setAll] = useState(() => { try { return JSON.parse(localStorage.getItem(VIVA_KEY) || '{}') || {}; } catch (e) { return {}; } });
  const [piece, setPiece] = useState(() => { try { return localStorage.getItem('pb_piece_title') || ''; } catch (e) { return ''; } });
  const [order, setOrder] = useState(() => shuffle(P8_VIVA.map(x => x[0]))), [i, setI] = useState(0), [open, setOpen] = useState(false);
  const key = piece.trim() || '_', st = all[key] || {};
  const mark = (v) => { const n = { ...all, [key]: { ...st, [order[i]]: v } }; setAll(n); try { localStorage.setItem(VIVA_KEY, JSON.stringify(n)); } catch (e) {} setOpen(false); setI(Math.min(i + 1, order.length)); };
  const done = i >= order.length, q = done ? null : P8_VIVA.find(x => x[0] === order[i]), said = P8_VIVA.filter(x => st[x[0]] === 1).length;
  const inp = { width:'100%', minWidth:0, padding:'8px 8px', fontSize:14.5, fontWeight:700, border:'1.5px solid rgba(38,41,107,0.3)', borderRadius:8, color:BK.ink, background:'#fff', boxSizing:'border-box', textAlign:'center' };
  return (
    <div className="try-box" style={actBox} data-pm="viva">
      <div style={actTitle}>{t('Viva cards', '비바 카드')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>시험관의 질문 열한 장. 카드를 읽고 <b>소리 내어</b> 답한 다음, 말했는지 아직인지 표시해요. 곡마다 따로 세어요; 이 기기에 저장돼요.</> : <>Eleven of the examiner's questions. Read the card, answer <b>aloud</b>, then mark it said or not yet. Counted for each piece; saved on this device.</>}</div>
      <input value={piece} placeholder={t('Which piece? (title, composer)', '어떤 곡? (제목, 작곡가)')} onChange={(e) => { setPiece(e.target.value); try { localStorage.setItem('pb_piece_title', e.target.value); } catch (er) {} }} style={inp}/>
      <div style={{display:'flex',gap:4,justifyContent:'center',margin:'8px 0 6px'}} aria-label={t('Progress', '진행')}>{P8_VIVA.map(x => <span key={x[0]} data-viva-dot={st[x[0]] == null ? '' : st[x[0]]} style={{width:14,height:14,borderRadius:7,border:'1.5px solid ' + (st[x[0]] === 1 ? BK.green : st[x[0]] === 0 ? BK.coral : BK.line),background:st[x[0]] === 1 ? BK.green : st[x[0]] === 0 ? '#fbe3da' : '#fff'}}/>)}</div>
      {q ? <div data-viva-card style={{margin:'6px auto',maxWidth:460,padding:'14px 14px 12px',borderRadius:12,border:'1.5px solid ' + BK.ink,background:'#fff',textAlign:'center'}}>
          <div style={{fontSize:11,fontWeight:900,color:BK.coral,letterSpacing:'0.1em',textTransform:'uppercase'}}>{t(P8_AREAS[q[1]][0], P8_AREAS[q[1]][1])}</div>
          <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:900,color:BK.ink,lineHeight:1.3,margin:'6px 0',textWrap:'balance'}}>{t(q[2][0], q[2][1])}</div>
          {open ? <div style={{fontSize:13.5,color:BK.muted,fontWeight:700,lineHeight:1.4}}>{t('A full answer covers: ', '다 말하려면: ') + t(q[3][0], q[3][1])}</div>
            : <button className="ghost-btn" style={{...spBtn, minHeight:36, padding:'6px 12px', fontSize:13}} onClick={() => setOpen(true)}>{t('What to cover', '무엇을 말할지')}</button>}
        </div>
        : spMsg(t(said + ' of ' + P8_VIVA.length + ' said well' + (piece.trim() ? ' for ' + piece.trim() : '') + '.', (piece.trim() ? piece.trim() + ': ' : '') + P8_VIVA.length + '장 중 ' + said + '장을 잘 말했어요.'), said === P8_VIVA.length ? BK.green : BK.coral)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {q && <button className="ghost-btn" data-viva-no style={{...spBtn, color:BK.coral, borderColor:BK.coral}} onClick={() => mark(0)}>{t('Not yet', '아직')}</button>}
        {q && <button className="ghost-btn" data-viva-yes style={{...spBtn, color:BK.green, borderColor:BK.green}} onClick={() => mark(1)}>{t('Said it ✓', '말했어요 ✓')}</button>}
        {done && <button className="ghost-btn" style={spBtn} onClick={() => { setOrder(shuffle(P8_VIVA.map(x => x[0]))); setI(0); }}>{t('▶ Again, shuffled', '▶ 다시, 섞어서')}</button>}
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const p8PicArc = () => lsRawPic('<rect x="4" y="6" width="72" height="32" rx="3" fill="#fff" stroke="#26296b" stroke-width="2"/><path d="M10 32 L24 26 L38 12 L52 22 L68 30" fill="none" stroke="#26296b" stroke-width="2.2" stroke-linejoin="round"/><circle cx="38" cy="12" r="4.5" fill="#e4572e"/>', [0, 0, 80, 44]);
const p8PicTitle = () => lsRawPic('<rect x="8" y="4" width="64" height="36" rx="3" fill="#fff" stroke="#26296b" stroke-width="2"/><path d="M18 14 H62 M24 22 H56" stroke="#e4572e" stroke-width="2.4"/><path d="M18 31 H62" stroke="#26296b" stroke-width="1.6"/>', [0, 0, 80, 44]);
const p8PicConv = () => lsRawPic('<path d="M6 16 H74 M6 22 H74 M6 28 H74" stroke="#26296b" stroke-width="1.4"/><path d="M20 10 q6 -8 12 0 q6 8 12 0" fill="none" stroke="#e4572e" stroke-width="2.4"/><ellipse cx="48" cy="25" rx="5" ry="3.6" fill="#26296b" transform="rotate(-20 48 25)"/><path d="M53 24 V8" stroke="#26296b" stroke-width="2"/><path d="M58 36 H70" stroke="#e4572e" stroke-width="3" stroke-linecap="round"/>', [0, 0, 80, 44]);
const p8PicPiano = () => lsRawPic('<path d="M6 36 H74" stroke="#26296b" stroke-width="2"/>' + [12, 24, 36, 48, 60, 72].map((x, i) => '<circle cx="' + x + '" cy="36" r="' + (i === 4 ? 5 : 3) + '" fill="' + (i === 4 ? '#e4572e' : '#26296b') + '"/>').join('') + '<rect x="30" y="8" width="24" height="16" rx="2" fill="#fff" stroke="#26296b" stroke-width="2"/><path d="M34 24 V12 M38 24 V12 M42 24 V12 M46 24 V12 M50 24 V12" stroke="#26296b" stroke-width="1.2"/>', [0, 0, 80, 44]);
const p8PicViva = () => lsRawPic('<rect x="22" y="4" width="36" height="36" rx="4" fill="#fff" stroke="#26296b" stroke-width="2"/><rect x="14" y="8" width="36" height="36" rx="4" fill="#fff" stroke="#e4572e" stroke-width="2"/><text x="32" y="33" text-anchor="middle" font-size="18" font-weight="900" fill="#26296b" font-family="Georgia, serif">?</text>', [0, 0, 80, 48]);

function p8LbPages(scr = false) {
  const ch = 'pieces-8', p7 = bkChapterNo('pieces-78'), ps = bkChapterNo('piano-story');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks = [[p8PicArc(), t('I show the climax of each piece and the keys that lead there', '곡마다 클라이맥스와 거기로 가는 조를 보여요')], [p8PicTitle(), t('I explain the title and every marking in the score', '제목과 악보의 모든 표시를 설명해요')],
    [p8PicConv(), t('I name the performance conventions of its time, and follow or bend them on purpose', '그 시대의 연주 관습을 말하고, 일부러 따르거나 비껴요')], [p8PicPiano(), t('I say which piano it was written for, and what that changes today', '어떤 피아노를 위해 썼는지, 오늘 무엇이 달라지는지 말해요')], [p8PicViva(), t('I answer the viva cards aloud, with my reasons', '비바 카드에 소리 내어, 이유와 함께 답해요')]];
  const toc = [[t('The arc of my piece', '내 곡의 곡선'), 2], [t('What the title promises', '제목이 약속하는 것'), 3], [t('How they played it then', '그때는 어떻게 쳤을까'), 4], [t('The piano of the time', '그 시대의 피아노'), 5], [t('Viva cards', '비바 카드'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const arcStill = <PaArc secs={[['A', 1, 16, 'I'], ['B', 17, 32, 'V'], ['C', 33, 48, 'vi'], ['A', 49, 64, 'I'], ['Coda', 65, 72, 'I']]} ten={[2, 3, 5, 2, 1]} w={scr ? 400 : 560} h={scr ? 110 : 130}/>;
  const titleStill = <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:scr ? 4 : 8,width:'100%',maxWidth:640,margin:'0 auto'}}>{['nocturne', 'scherzo', 'barcarolle', 'intermezzo', 'ballade', 'mazurka'].map(id => { const x = p8Title(id); return <div key={id} style={{display:'grid',gridTemplateColumns:'90px 1fr',gap:8,alignItems:'baseline',fontSize:scr ? 12.5 : 13.5,color:BK.ink,lineHeight:1.3}}><b style={{fontFamily:LB_SERIF,fontSize:scr ? 14 : 16}}>{t(x[1], x[2])}</b><span>{t(x[3], x[4])}</span></div>; })}</div>;
  const convStill = <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : 'repeat(2,1fr)',gap:8,width:'100%',maxWidth:720,margin:'0 auto'}}>{P8_ERAS.map(k => { const e = p8Era(k); return <div key={k} style={{border:'1.5px solid rgba(38,41,107,0.3)',borderRadius:8,padding:'6px 8px',background:'#fff'}}><div style={{fontWeight:900,fontSize:scr ? 13 : 14.5,color:BK.ink}}>{e.short} <span style={{fontSize:11,color:BK.muted,fontWeight:800}}>{e.years}</span></div><div style={{fontSize:scr ? 11.5 : 12.5,color:BK.coral,fontWeight:800,lineHeight:1.35}}>{e.today}</div></div>; })}</div>;
  const pianoStill = <div style={{display:'grid',gridTemplateColumns:scr ? '1fr 1fr' : 'repeat(3,1fr)',gap:6,width:'100%',maxWidth:720,margin:'0 auto'}}>{P8_PIANOS.map((p, i) => <div key={i} style={{border:'1.5px solid rgba(38,41,107,0.3)',borderRadius:8,padding:'6px 8px',background:'#fff'}}><div style={{fontSize:11,fontWeight:900,color:BK.coral}}>{PIANO_TIMELINE[p[0]].y}</div><div style={{fontWeight:900,fontSize:scr ? 12.5 : 13.5,color:BK.ink,lineHeight:1.2}}>{PIANO_TIMELINE[p[0]].t}</div><div style={{fontSize:scr ? 11 : 12,color:BK.ink,lineHeight:1.35,marginTop:2}}>{t(p[1], p[2])}</div></div>)}</div>;
  const vivaStill = <div style={{display:'grid',gap:scr ? 4 : 6,width:'100%',maxWidth:600,margin:'0 auto'}}>{P8_VIVA.map(q => <div key={q[0]} style={{display:'grid',gridTemplateColumns:scr ? '110px 1fr' : '150px 1fr',gap:8,fontSize:scr ? 12 : 13,color:BK.ink,lineHeight:1.3}}><span style={{fontSize:10.5,fontWeight:900,color:BK.coral,letterSpacing:'0.06em',textTransform:'uppercase'}}>{t(P8_AREAS[q[1]][0], P8_AREAS[q[1]][1])}</span><span style={{fontWeight:700}}>{t(q[2][0], q[2][1])}</span></div>)}</div>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('The general knowledge of the Certificate of Performance and the diplomas (Piano syllabus, Section II): questions from the full score on the significance of titles and the meaning of every marking; the composer (biography, influences, impact on later composers, output); the historical and stylistic context, including the performance conventions of the time; the structure (layout, keys, melodic and harmonic language, climax points); and the construction and development of the piano and its effect on the repertoire. The candidate uses all of it to explain their interpretive choices. For the Certificate, a movement must also be placed among the other movements of its work, with a description of them. This room adds the diploma depth to the Grade 7 room (chapter ' + p7 + '); the piano’s story (chapter ' + ps + ', in the attic) has the long version.', 'Certificate of Performance와 디플로마의 일반 지식(피아노 교재, Section II): 전체 악보에서, 제목의 의미와 모든 표시의 뜻; 작곡가(생애, 영향, 뒤의 작곡가에게 준 영향, 작품); 역사적·양식적 맥락과 그 시대의 연주 관습; 구조(배치, 조, 선율·화성의 말투, 클라이맥스); 피아노의 구조와 발달이 레퍼토리에 미친 영향. 수험생은 이 모두로 자기 해석의 선택을 설명해요. Certificate는 악장이 작품의 다른 악장들 사이 어디에 있는지도, 다른 악장의 설명과 함께. 이 방은 7급 방(' + p7 + '장)에 디플로마 깊이를 더해요; 긴 이야기는 다락방의 피아노 이야기(' + ps + '장)에.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={120}><PaArc secs={[['A', 1, 16, 'I'], ['B', 17, 32, 'V'], ['C', 33, 48, 'vi'], ['A', 49, 64, 'I'], ['Coda', 65, 72, 'I']]} ten={[2, 3, 5, 2, 1]} w={520} h={110}/></LbPic>
      <LbSay size={18}>{t('The diplomas ask you to know each piece like its composer: what the title promises, where it climbs to its climax, how its time played it, which piano it was written for, and why you play it the way you do.', '디플로마는 곡을 작곡가처럼 알기를 바라요: 제목이 약속하는 것, 어디서 클라이맥스로 오르는지, 그 시대는 어떻게 쳤는지, 어떤 피아노를 위해 썼는지, 그리고 나는 왜 이렇게 치는지.')}</LbSay>
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
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The arc of my piece', '내 곡의 곡선')}
      teacher={<>{t('"Structure: formal layout, keys, melodic/harmonic language and climax points." On the Grade 7 map, add the arc: a tension for each section, the climax at the top, the keys that lead there, the language of the harmony. The pad keeps one arc per device, over the map saved in the Grade 7 room; the Workbook has a sheet for each piece.', '"구조: 형식의 배치, 조, 선율·화성의 말투, 클라이맥스." 7급의 지도 위에 곡선을 더해요: 부분마다 긴장, 꼭대기의 클라이맥스, 거기로 가는 조, 화성의 말투. 패드는 7급 방에 저장된 지도 위에 기기마다 곡선 하나를 저장해요; 워크북에 곡마다 한 장.')}</>}>
      <LbLive still={<LbPic h={150}>{arcStill}</LbPic>} live={<PieceArcMaker/>}/>
      <LbSay>{LANG === 'ko' ? <>부분마다 <b>긴장</b>을 재요: 음역, 셈여림, 짜임새, 화성. 가장 높은 곳이 <b>클라이맥스</b>; 거기로 가는 <b>조</b>를 말하고, 화성의 <b>말투</b>를 이름 붙여요.</> : <>Measure each section's <b>tension</b>: register, dynamics, texture, harmony. The highest point is <b>the climax</b>; say which <b>keys</b> lead there, and name the harmony's <b>language</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>내 곡에서 가장 센 마디를 쳐요. 그 앞 여덟 마디는 어떻게 거기에 이르나요?</>, <>부분마다 마지막 화음을 쳐요: 집에서 얼마나 먼 조인가요?</>, <>클라이맥스에서 끝까지 쳐요: 음악은 어떻게 내려오나요?</>]
        : [<>Play the strongest bar of your piece. How do the eight bars before it get there?</>, <>Play the last chord of each section: how far from home is its key?</>, <>Play from the climax to the end: how does the music come down?</>]}/>
      <LbRemember>{t('Tension up, climax, the way home.', '긴장이 오르고, 클라이맥스, 집으로 가는 길.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('What the title promises', '제목이 약속하는 것')}
      teacher={<>{t('"Terminology, including the significance of titles and the meaning of all markings contained in the score." The cards give the dictionary meaning of eighteen title words; the markings themselves are the Terms room’s. Ask for the title first, then any marking on the page, then how the hand makes it.', '"용어, 제목의 의미와 악보의 모든 표시의 뜻을 포함." 카드는 제목 단어 열여덟 개의 사전 뜻; 표시 자체는 음악 용어 방의 것. 먼저 제목을, 그다음 그 쪽의 아무 표시를, 그다음 손이 그걸 어떻게 만드는지 물어요.')}</>}>
      <LbLive still={<LbPic h={150}>{titleStill}</LbPic>} live={<TitlePad/>}/>
      <LbSay>{LANG === 'ko' ? <>제목은 <b>약속</b>이에요: 녹턴은 밤을, 뱃노래는 물을, 스케르초는 농담을. 그 약속을 알면 첫 마디부터 어떻게 칠지 보여요.</> : <>A title is <b>a promise</b>: a nocturne promises night, a barcarolle water, a scherzo a joke. Know the promise and the first bar tells you how to play it.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>내 곡의 제목을 한 문장으로 설명해요.</>, <>첫 쪽의 표시를 모두 짚으며 뜻을 말해요.</>, <>표시 하나를 골라 두 가지로 쳐 보고, 악보가 원하는 쪽을 골라요.</>]
        : [<>Explain your piece's title in one sentence.</>, <>Point at every marking on the first page and say what it means.</>, <>Pick one marking, play it two ways, and choose the one the score wants.</>]}/>
      <LbRemember>{t('The title is a promise.', '제목은 약속이에요.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('How they played it then', '그때는 어떻게 쳤을까')}
      teacher={<>{t('"Historical and stylistic context: how each work relates to the period from which it arises, considering both its compositional style and the performance conventions of the time." The periods, their features and the lines for today’s piano are the app’s own, from the piano’s story room; they are generalisations, so check them against each piece (a late Beethoven sonata is not played like a Mozart one).', '"역사적·양식적 맥락: 작품이 그 시대와 어떻게 이어지는지, 작곡 양식과 그 시대의 연주 관습 둘 다." 시대와 특징, 오늘 피아노를 위한 줄은 피아노 이야기 방의 앱 자료예요; 일반화이니 곡마다 대조해요(후기 베토벤 소나타는 모차르트처럼 치지 않아요).')}</>}>
      <LbLive still={<LbPic h={150}>{convStill}</LbPic>} live={<ConventionsPad/>}/>
      <LbSay>{LANG === 'ko' ? <>시대마다 <b>관습</b>이 있어요: 꾸밈음을 박 위에서 시작할지, 페달을 얼마나, 루바토를 어디까지, 반복을 칠지. 따르든 비껴가든, <b>알고</b> 하는 거예요.</> : <>Each period has its <b>conventions</b>: whether an ornament starts on the beat, how much pedal, how far the rubato goes, whether to play the repeats. Follow them or bend them, but <b>know</b> them.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>내 곡의 시대를 말하고, 악보에서 그 시대의 특징 둘을 짚어요.</>, <>한 프레이즈를 그 시대의 관습대로 쳐요: 페달, 터치, 꾸밈음.</>, <>같은 프레이즈를 다르게 쳐 보고, 왜 하나를 고르는지 말해요.</>]
        : [<>Say your piece's period, and point at two of its features in the score.</>, <>Play one phrase the way its time did: pedal, touch, ornaments.</>, <>Play the same phrase another way, and say why you choose one.</>]}/>
      <LbRemember>{t('Know the convention, then choose.', '관습을 알고, 그다음 골라요.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The piano of the time', '그 시대의 피아노')}
      teacher={<>{t('"Knowledge of the construction and development of the piano and its effect on the repertoire." Six stops from the piano’s story (chapter ' + ps + '): the harpsichord, Cristofori’s hammers (1700), the Viennese fortepiano, the six-octave pianos and the double escapement (1821), the iron frame and crossed strings (1825 to 1859), 88 keys (1880s). For each piece: which piano, what it could do, what that changes on today’s instrument (pedal, balance, tempo, ornaments).', '"피아노의 구조와 발달, 그리고 레퍼토리에 미친 영향." 피아노 이야기(' + ps + '장)의 정거장 여섯: 하프시코드, 크리스토포리의 해머(1700), 빈의 포르테피아노, 6옥타브 피아노와 더블 이스케이프먼트(1821), 철 프레임과 교차현(1825–1859), 88건반(1880년대). 곡마다: 어떤 피아노, 무엇을 할 수 있었는지, 오늘 악기에서 무엇이 달라지는지(페달, 균형, 빠르기, 꾸밈음).')}</>}>
      <LbLive still={<LbPic h={170}>{pianoStill}</LbPic>} live={<PianoOfTimePad/>}/>
      <LbSay>{LANG === 'ko' ? <>바흐의 건반은 <b>세게 쳐도 커지지 않았고</b>, 모차르트의 피아노는 <b>5옥타브</b>였고, 쇼팽의 피아노는 <b>페달을 받쳐 줄 울림</b>이 있었어요. 그래서 악보가 그렇게 생겼어요.</> : <>Bach's keyboard <b>could not play louder by touch</b>, Mozart's piano had <b>five octaves</b>, Chopin's had <b>a sustain that carried the pedal</b>. That is why the scores look the way they do.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>내 곡의 작곡가가 앉았던 피아노를 말해요.</>, <>그 피아노에서 할 수 없었던 것 하나를 찾아 악보에서 짚어요(음역, 페달, 울림).</>, <>오늘의 피아노에서 그 자리를 어떻게 칠지 정하고, 이유를 말해요.</>]
        : [<>Name the piano your composer sat at.</>, <>Find one thing that piano could not do, and point at its trace in the score (range, pedal, sustain).</>, <>Decide how you play that spot on today's piano, and say why.</>]}/>
      <LbRemember>{t('Their piano, then mine.', '그들의 피아노, 그다음 나의 피아노.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Viva cards', '비바 카드')}
      teacher={<>{t('The diplomas examine the general knowledge as a conversation from the full score ("a mature understanding of the structure, style and historical background ... as a basis for discussing the interpretive choices"). Eleven cards cover the five areas and the interpretive choice; the composer cards (influences, output, impact on later composers) go deeper than the Grade 7 card. Ask them in any order; the student answers in sentences, pointing at the score.', '디플로마는 일반 지식을 전체 악보로 나누는 대화로 봐요("구조, 양식, 역사적 배경의 성숙한 이해... 해석의 선택을 논하는 바탕으로"). 카드 열한 장이 다섯 영역과 해석의 선택을 덮어요; 작곡가 카드(영향, 작품, 뒤의 작곡가에게 준 영향)는 7급 카드보다 깊이. 아무 순서로 물어요; 학생은 악보를 짚으며 문장으로 답해요.')}</>}>
      <LbLive still={<LbPic h={170}>{vivaStill}</LbPic>} live={<VivaCards/>}/>
      <LbSay>{LANG === 'ko' ? <>시험관은 <b>대화</b>를 원해요: 사실 하나, 악보의 근거 하나, 그래서 내가 고른 것 하나. 카드를 소리 내어 답하면 시험장에서 말이 먼저 나와요.</> : <>The examiner wants <b>a conversation</b>: one fact, one piece of evidence in the score, one thing you chose because of it. Answer the cards aloud and the words come first in the exam room.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>카드 세 장을 뽑아 소리 내어 답해요.</>, <>답마다 악보에서 근거 한 곳을 치거나 짚어요.</>, <>곡마다 카드 열한 장을 다 '말했어요'로.</>]
        : [<>Draw three cards and answer aloud.</>, <>For each answer, play or point at one piece of evidence in the score.</>, <>All eleven cards 'said' for every piece.</>]}/>
      <LbRemember>{t('A fact, the evidence, my choice.', '사실, 근거, 나의 선택.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('For each piece of the programme, from the full score: the arc and its climax, the title and the markings, the conventions of its time, the piano it was written for, and the viva cards with reasons. The student answers in sentences and plays the evidence.', '프로그램의 곡마다, 전체 악보로: 곡선과 클라이맥스, 제목과 표시, 그 시대의 관습, 쓰인 피아노, 이유가 있는 비바 카드. 학생은 문장으로 답하고 근거를 쳐요.')}</>}>
      <LbSay>{t('For each piece, tick each one: not yet, nearly, or got it!', '곡마다 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey="pb_p8_five"/>}/>
    </LbPage>,
  ];
}
function Pieces8LessonBook() { return <>{p8LbPages(false)}</>; }
function P8Learn({ onStart }) {
  const pages = p8LbPages(true), opener = pages[0];
  return (
    <Lesson id="pieces-8" title={bkChapterName('pieces-8')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="pieces-8"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
const P8_LEVELS = [
  { n: 1, label: 'What the title promises', kind: 'title', time: 15 },
  { n: 2, label: 'Where is the climax?', kind: 'arc', time: 12 },
  { n: 3, label: 'Which period plays like this?', kind: 'conv', time: 15 },
  { n: 4, label: 'Which piano?', kind: 'piano', time: 15 },
];
Object.assign(LEVEL_KO, { 'What the title promises': '제목이 약속하는 것', 'Where is the climax?': '클라이맥스는 어디?', 'Which period plays like this?': '어느 시대의 연주?', 'Which piano?': '어떤 피아노?' });
function genP8Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'title') { let x, g = 0; do { x = pick(P8_TITLES); } while (prev && prev.key === x[0] && g++ < 10); return { kind, id: x[0], answer: x[0], choices: shuffle(P8_TITLES.filter(z => z[0] !== x[0])).slice(0, 3).map(z => z[0]).concat([x[0]]).sort(() => Math.random() - 0.5), key: x[0], uid }; }
  if (kind === 'arc') { const a = paQuizArc(prev); return { kind, secs: a.secs, ten: a.ten, answer: a.answer, choices: a.secs.map((_, i) => i), key: a.key, uid }; }
  if (kind === 'conv') { let id, ti, g = 0; do { id = pick(P8_ERAS); ti = Math.floor(Math.random() * p8Era(id).traits.length); } while (prev && prev.key === id + ti && g++ < 10); return { kind, id, ti, answer: id, choices: P8_ERAS.slice(), key: id + ti, uid }; }
  let k, g = 0; do { k = Math.floor(Math.random() * P8_PIANOS.length); } while (prev && prev.key === 'p' + k && g++ < 10); return { kind: 'piano', k, answer: k, choices: P8_PIANOS.map((_, i) => i), key: 'p' + k, uid };
}
function P8Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  const grid = (cols, items, fs = 14) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:fs,fontWeight:900,lineHeight:1.2}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  const card = (txt, fs = 15) => <div style={{textAlign:'center',margin:'8px auto',maxWidth:420,padding:'12px 12px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff',fontSize:fs,fontWeight:800,color:BK.ink,lineHeight:1.4}}>{txt}</div>;
  let title, body;
  if (q.kind === 'title') { const x = p8Title(q.id); title = t('Which title promises this?', '이것을 약속하는 제목은?'); body = <>{card(t(x[3], x[4]))}{grid(2, q.choices.map(c => [c, t(p8Title(c)[1], p8Title(c)[2])]))}</>; }
  else if (q.kind === 'arc') { title = t('Where is the climax?', '클라이맥스는 어디일까요?'); body = <><PaArc secs={q.secs} ten={q.ten} quiz mark={done ? q.answer : -1} sel={done && given.ans !== q.answer ? given.ans : -1} w={420} h={120}/>{grid(q.choices.length, q.choices.map(c => [c, q.secs[c][0]]), q.choices.length > 5 ? 12 : 14)}</>; }
  else if (q.kind === 'conv') { const e = p8Era(q.id); title = t('Which period plays like this?', '어느 시대의 연주일까요?'); body = <>{card(e.traits[q.ti])}{grid(2, q.choices.map(c => [c, p8Era(c).short]))}</>; }
  else { title = t('Which piano is this?', '어떤 피아노일까요?'); body = <>{card(t(P8_PIANOS[q.k][1], P8_PIANOS[q.k][2]))}{grid(2, q.choices.map(c => [c, p8PianoName(c)]), 12.5)}</>; }
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {body}
  </div>);
}
const p8AnswerLabel = (q) => (q.kind === 'title' ? t(p8Title(q.answer)[1], p8Title(q.answer)[2]) : q.kind === 'arc' ? q.secs[q.answer][0] : q.kind === 'conv' ? p8Era(q.answer).short : p8PianoName(q.answer));
Object.assign(PIECES_8_DRILL, { levels: P8_LEVELS, generate: genP8Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: p8AnswerLabel, Question: P8Question, Learn: P8Learn });
function P8Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="pieces-8" teacher>{content}</WbPage>);
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('pieces-8')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>The general knowledge of the Certificate of Performance and the diplomas, from the Piano syllabus (Section II). The Workbook has a diploma sheet for each piece of the programme: the arc, the title, the conventions, the piano, the composer, the choices. The title meanings, the periods' conventions and the piano's stops are the app's own (the piano's story room): please check them against the works your students play.</div>
    <TcBlock page={2} title="The arc of my piece" answers={<>{tcAns('LOOK FOR', ['the loudest, highest or most chromatic bars', 'the keys on the way, and how far from home', 'texture and register thickening before the top', 'the way down after it'], null)}</>}
      watch="A climax named without the road to it. Ask “which keys lead there, and what thickens?”"
      say="“Tension up, climax, the way home.”"/>
    <TcBlock page={3} title="What the title promises" answers={<>{tcAns('THE WORDS', P8_TITLES.slice(0, 9).map(x => x[1] + ': ' + x[3]), null)}{tcAns('', P8_TITLES.slice(9).map(x => x[1] + ': ' + x[3]), null)}</>}
      watch="A title translated but not applied. Ask “so how do you play the first bar?”"
      say="“The title is a promise.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="How they played it then" answers={<>{tcAns('THE PERIODS', P8_ERAS.map(k => { const e = p8Era(k); return e.short + ' (' + e.years + '): ' + e.today; }), null)}</>}
      watch="Conventions recited, then ignored at the piano. Ask for one phrase both ways, and the reason for the choice."
      say="“Know the convention, then choose.”"/>
    <TcBlock page={5} title="The piano of the time" answers={<>{tcAns('THE STOPS', P8_PIANOS.map(p => PIANO_TIMELINE[p[0]].y + ' ' + PIANO_TIMELINE[p[0]].t + ': ' + p[1]), null)}</>}
      watch="“Bach wrote for the piano.” Bach’s keyboard music was written for the harpsichord, clavichord and organ; he tried early pianos."
      say="“Their piano, then mine.”"/>
    <TcBlock page={6} title="Viva cards" answers={<>{tcAns('THE CARDS', P8_VIVA.map(q => q[2][0]), null)}</>}
      watch="Facts without evidence. Every answer: one fact, one place in the score, one choice."
      say="“A fact, the evidence, my choice.”"/>
    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>For each piece of the programme, ask from the full score as the examiners would; two examiners sit the diplomas. The student answers in sentences and plays the evidence.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['pieces-8'] = P8Teacher;
function P8Workbook({ startNo = 1 }) {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="pieces-8">{content}</WbPage>);
  const line = (lab, w, h = 30) => <div style={{display:'grid',gridTemplateColumns:(w || 170) + 'px 1fr',gap:8,alignItems:'end',fontSize:12.5,fontWeight:800,color:BK.ink,margin:'4px 0'}}><span>{lab}</span><span style={{borderBottom:'1.5px solid rgba(38,41,107,0.45)',height:h}}/></div>;
  const sheet = (n) => <>
    <WbTop step={1}/>
    <Part kind="together" title={'My piece ' + n + ': the diploma sheet'} how="One sheet for each piece of the programme. Fill it in with the full score open, then say it aloud.">
      {line('Title, and what it promises')}{line('Composer, dates, where they worked')}
      <div style={{fontSize:12,fontWeight:900,color:BK.ink,margin:'8px 0 4px'}}>The arc: a letter and the bars of each section; draw the tension line; circle the climax</div>
      <div style={{display:'flex',border:'1.5px solid ' + BK.ink,borderRadius:6,height:96,background:'#fff'}}>{[0, 1, 2, 3, 4, 5].map(i => <div key={i} style={{flex:1,borderLeft:i ? '1.5px dashed rgba(38,41,107,0.35)' : 'none'}}/>)}</div>
      {line('The keys on the way, and the harmony’s language', 0, 40)}{line('Period, and two features that place it there', 0, 40)}{line('The conventions of its time I follow, or bend', 0, 40)}{line('The piano it was written for, and what that changes today', 0, 40)}{line('Influences: from whom, to whom; its place in the output', 0, 40)}{line('One interpretive choice, and its reason', 0, 40)}
    </Part>
    <Faces/>
  </>;
  P(sheet(1)); P(sheet(2)); P(sheet(3));
  P(<P8PaperCheck/>);
  return <>{pages}</>;
}
function P8PaperCheck() {
  const arcs = [[['A', 'B', 'A', 'Coda'], [2, 4, 1, 1]], [['A', 'B', 'A', 'C', 'A'], [1, 2, 2, 5, 1]], [['Intro', 'A', 'B', 'A'], [1, 2, 5, 2]]];
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'What the title promises: write the title word')}
    <BkGrid cols={2} gap="6px 8px">{['nocturne', 'barcarolle', 'scherzo', 'etude'].map((id, i) => <BkCell key={id} n={i + 1}><div style={{display:'grid',gap:4,padding:'14px 2px 2px',fontSize:12,fontWeight:800,color:BK.ink}}>{p8Title(id)[3]}{bkBox(150, 22)}</div></BkCell>)}</BkGrid>
    {bkSec('B', 'Where is the climax? Circle the section')}
    <BkGrid cols={3} gap="6px 8px">{arcs.map(([names, ten], i) => <BkCell key={i} n={i + 5}><div style={{padding:'12px 2px 2px'}}><PaArc secs={names.map((x, k) => [x, k * 8 + 1, k * 8 + 8, ''])} ten={ten} quiz mark={-1} sel={-1} w={200} h={86}/></div></BkCell>)}</BkGrid>
    {bkSec('C', 'Which period plays like this? (Baroque, Classical, Romantic, 20th century)')}
    <BkGrid cols={2} gap="6px 8px">{[['baroque', 1], ['classical', 0], ['romantic', 3], ['modern', 0]].map(([k, ti], i) => <BkCell key={k} n={i + 8}><div style={{display:'grid',gap:4,padding:'14px 2px 2px',fontSize:11.5,fontWeight:800,color:BK.ink}}>{p8Era(k).traits[ti]}{bkBox(130, 22)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'Which piano? Write its date from the stops: before 1700 · 1700 · 1770s–90s · 1800–1820s · 1825–1859 · 1880s')}
    <BkGrid cols={2} gap="6px 8px">{[0, 2, 4, 5].map((k, i) => <BkCell key={k} n={i + 12}><div style={{display:'grid',gap:4,padding:'14px 2px 2px',fontSize:11.5,fontWeight:800,color:BK.ink}}>{P8_PIANOS[k][1]}{bkBox(110, 22)}</div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['pieces-8'] = P8Workbook;
