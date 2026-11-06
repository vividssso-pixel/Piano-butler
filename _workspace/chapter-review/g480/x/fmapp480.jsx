// ─── Phase 480: chapter 24's pads (pages 1 to 6), the screen lesson and the drill ───
const fmxMsg = (msg, bad) => <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:bad ? BK.coral : BK.ink,minHeight:22,margin:'8px 0 6px',textWrap:'balance',wordBreak:'keep-all'}}>{fmxKoT(msg)}</div>;
const fmxStopBtn = (playing, onPlay, label) => chxBtn('p', playing ? t('■ Stop', '■ 멈추기') : label || t('▶ Listen', '▶ 듣기'), playing ? () => onPlay(null) : () => onPlay(true), playing);
const fmxSecOf = (bar) => Math.floor(bar / 8), fmxPhOf = (bar) => Math.floor(bar / 4);

// page 1: the map: tap a row's part to hear it; the part sounding lit
function FmxMapPad() {
  const [sel, setSel] = useState({ kind: 'section', i: 2 }), [playing, setPlaying] = useState(false);
  useEffect(() => () => fmxStop(), []);
  const ids = fmxPieceIds();
  const go = (kind, i) => { fmxStop(); setSel({ kind, i }); setPlaying(true);
    const done = (p) => { if (p === -1) setPlaying(false); };
    if (kind === 'piece') fmxPlay(ids, (p) => { if (p === -1) { setPlaying(false); setSel({ kind: 'piece', i: 0 }); } else setSel({ kind: 'phrase', i: p, from: 'piece' }); });
    else if (kind === 'section') fmxPlay(ids.slice(i * 2, i * 2 + 2), done);
    else if (kind === 'phrase') fmxPlay([ids[i]], done);
    else if (kind === 'bar') fmxPlayNotes(FMX_PH[ids[fmxPhOf(i)]][i % 4].map(n => ({ d: n[2], dur: n[1] })), (k) => { if (k === -1) setPlaying(false); });
    else fmxPlayBeats(4, () => setPlaying(false)); };
  const stop = () => { fmxStop(); setPlaying(false); };
  const k = sel.kind, i = sel.i, sec = (j) => FMX_SEC[j];
  const secKo = (j) => (j === 2 ? '다시 나온 ' : '') + sec(j) + ' 부분';
  const msg = sel.from === 'piece' ? t('The piece: phrase ' + (i + 1) + ', in section ' + sec(fmxSecOf(i * 4)) + '.', '곡 전체: ' + fmxNth(i + 1) + ' 프레이즈, ' + secKo(fmxSecOf(i * 4)) + '.')
    : k === 'piece' ? t('The piece: 24 bars, A B A.', '곡 전체: 24마디, A B A.')
    : k === 'section' ? t('Section ' + sec(i) + (i === 2 ? ' again' : '') + ': bars ' + (i * 8 + 1) + ' to ' + (i * 8 + 8) + ', two phrases.', secKo(i) + ': ' + (i * 8 + 1) + '~' + (i * 8 + 8) + '마디, 프레이즈 두 개.')
    : k === 'phrase' ? t('Phrase ' + (i + 1) + ': bars ' + (i * 4 + 1) + ' to ' + (i * 4 + 4) + ', in section ' + sec(fmxSecOf(i * 4)) + '.', fmxNth(i + 1) + ' 프레이즈: ' + (i * 4 + 1) + '~' + (i * 4 + 4) + '마디, ' + secKo(fmxSecOf(i * 4)) + '.')
    : k === 'bar' ? t('Bar ' + (i + 1) + ': in phrase ' + (fmxPhOf(i) + 1) + ', section ' + sec(fmxSecOf(i)) + '.', (i + 1) + '마디: ' + fmxNth(fmxPhOf(i) + 1) + ' 프레이즈, ' + secKo(fmxSecOf(i)) + '.')
    : t('Bar 1: four beats.', '1마디: 네 박.');
  return (
    <div className="try-box" style={actBox} data-fmx="pad-map">
      <div style={actTitle}>{t('The map of a piece', '곡의 지도')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{fmxKoT(t('Tap any part: the piece, a section, a phrase, a bar or the beats. Hear it.', '아무 곳이나 눌러요: 곡 전체, 부분, 프레이즈, 마디, 박. 소리가 들려요.'))}</div>
      <div style={{maxWidth:420,margin:'0 auto'}}><FmxMapSvg scr sel={sel} onTap={go} label={t('The map of a piece: 24 bars; sections A, B, A; six phrases; the bars; bar 1’s four beats.', '곡의 지도: 24마디; A, B, A 부분; 프레이즈 여섯; 마디; 1마디의 네 박.')}/></div>
      <div style={{textAlign:'center',fontSize:13,color:BK.muted,margin:'4px 0 0',textWrap:'balance',wordBreak:'keep-all'}}>{fmxKoT(t('Beats make bars, bars make phrases, phrases make sections, sections make the piece.', '박이 모여 마디, 마디가 모여 프레이즈, 프레이즈가 모여 부분, 부분이 모여 곡이 돼요.'))}</div>
      {fmxMsg(msg)}
      {playing && <div style={{display:'flex',justifyContent:'center'}}>{chxBtn('s', t('■ Stop', '■ 멈추기'), stop, true)}</div>}
    </div>
  );
}
// page 2: two phrases; tap one to hear it to its resting note
function FmxPhrasePad() {
  const [on, setOn] = useState(-1);
  useEffect(() => () => fmxStop(), []);
  const ids = ['B', 'A'], w = fmxVbw(['B'], true, 18);
  const hear = (j) => { fmxStop(); setOn(j); fmxPlay([ids[j]], (p) => { if (p === -1) setOn(-1); }); };
  return (
    <div className="try-box" style={actBox} data-fmx="pad-phrase">
      <div style={actTitle}>{t('The phrase', '프레이즈')}</div>
      <div style={actNote}>{fmxKoT(t('Two phrases. Tap one: it plays to its resting note.', '프레이즈 두 개. 하나를 누르면 쉬는 음까지 들려요.'))}</div>
      <div style={{display:'flex',flexDirection:'column',gap:4}}>{ids.map((id, j) => <button key={id} type="button" data-fmx={'ph' + j} onClick={() => hear(j)} style={{border:'1.5px solid ' + (on === j ? PEN_C : 'rgba(38,41,107,0.18)'),borderRadius:10,background:'#fff',padding:'2px 4px',cursor:'pointer'}}>
        <FmxRow ids={[id]} ts={j === 0} tsRoom={j > 0} end={j === 1} marks rest width={w} D={18} n0={j * 4 + 1} label={t('Phrase ' + (j + 1) + ', bars ' + (j * 4 + 1) + ' to ' + (j * 4 + 4) + '.', fmxNth(j + 1) + ' 프레이즈, ' + (j * 4 + 1) + '~' + (j * 4 + 4) + '마디.')}/></button>)}</div>
      {fmxMsg(on === -1 ? t('Tap a phrase.', '프레이즈를 눌러요.') : t('Phrase ' + (on + 1) + ': bars ' + (on * 4 + 1) + ' to ' + (on * 4 + 4) + '. It rests on ' + fmxLast(ids[on]) + '.', fmxNth(on + 1) + ' 프레이즈: ' + (on * 4 + 1) + '~' + (on * 4 + 4) + '마디. ' + fmxLast(ids[on]) + '에서 쉬어요.'))}
    </div>
  );
}
// page 3: four phrases: give each a letter (the first is A); Check
const FMX_L3 = ['A', 'A', 'B', 'A'];
function FmxLetterPad() {
  const [ls, setLs] = useState(['A', '', '', '']), [on, setOn] = useState(-1), [checked, setChecked] = useState(false);
  useEffect(() => () => fmxStop(), []);
  const w = fmxVbw(['A'], true, 22);
  const hear = (j) => { fmxStop(); setOn(j); fmxPlay([FMX_L3[j]], (p) => { if (p === -1) setOn(-1); }); };
  const cyc = (j) => { if (j === 0) return; const nx = { '': 'A', A: 'B', B: 'C', C: 'A' }[ls[j]]; const c = ls.slice(); c[j] = nx; setLs(c); setChecked(false); };
  const ok = ls.every((l, j) => l === FMX_L3[j]);
  return (
    <div className="try-box" style={actBox} data-fmx="pad-letters">
      <div style={actTitle}>{t('Same or different', '같은 음악, 새 음악')}</div>
      <div style={actNote}>{fmxKoT(t('Tap ▶ to hear a phrase. Tap its box to give it a letter: same music, same letter.', '▶를 눌러 프레이즈를 들어요. 상자를 눌러 글자를 붙여요: 같은 음악은 같은 글자.'))}</div>
      <div style={{display:'flex',flexDirection:'column',gap:10}}>{FMX_L3.map((id, j) => <div key={j} style={{display:'flex',flexDirection:'column',gap:2}}>
        <div style={{display:'flex',gap:8,alignItems:'center'}}><span style={{fontSize:12,fontWeight:800,color:BK.muted,minWidth:60}}>{t('bars ' + (j * 4 + 1) + '–' + (j * 4 + 4), (j * 4 + 1) + '~' + (j * 4 + 4) + '마디')}</span>
          <button type="button" data-fmx={'let' + j} aria-label={t('Letter for phrase ' + (j + 1), fmxNth(j + 1) + ' 프레이즈의 글자')} onClick={() => cyc(j)} disabled={j === 0} style={{width:44,height:44,borderRadius:8,border:'1.8px ' + (ls[j] ? 'solid ' : 'dashed ') + (checked && ls[j] !== FMX_L3[j] ? PEN_C : PEN_N),background:'#fff',fontFamily:LB_SERIF,fontSize:22,fontWeight:900,color:PEN_N,cursor:j ? 'pointer' : 'default'}}>{ls[j] || '?'}</button>
          <button type="button" data-fmx={'play' + j} aria-label={t('Play phrase ' + (j + 1), fmxNth(j + 1) + ' 프레이즈 듣기')} onClick={() => hear(j)} style={{width:44,height:44,borderRadius:8,border:'1.5px solid ' + (on === j ? PEN_C : 'rgba(38,41,107,0.25)'),background:'#fff',color:on === j ? PEN_C : PEN_N,fontWeight:900,cursor:'pointer'}}>▶</button></div>
        <FmxRow ids={[id]} ts={j === 0} tsRoom={j > 0} end={j === 3} width={w} D={22} label={t('Phrase ' + (j + 1) + ', bars ' + (j * 4 + 1) + ' to ' + (j * 4 + 4) + '.', fmxNth(j + 1) + ' 프레이즈, ' + (j * 4 + 1) + '~' + (j * 4 + 4) + '마디.')}/></div>)}</div>
      {fmxMsg(!checked ? t('The first phrase is A.', '첫 프레이즈는 A예요.') : ok ? t('A A B A: phrase 3 is new music. ✓', 'A A B A: 3번째 프레이즈가 새 음악이에요. ✓') : t('Listen again: which phrases are the same?', '다시 들어요: 어느 프레이즈가 같나요?'), checked && !ok)}
      <div style={{display:'flex',justifyContent:'center'}}>{chxBtn('c', t('Check', '확인'), () => setChecked(true), false)}</div>
    </div>
  );
}
// pages 4 and 5: a road (binary or ternary); ▶ plays it in its order, the bar and the letter sounding lit
function FmxRoadPad({ kind }) {
  const [lit, setLit] = useState(-1), [cur, setCur] = useState(-1);
  useEffect(() => () => fmxStop(), []);
  const bars = kind === 'bin' ? FMX_BIN : FMX_TER, ord = FMX_ORDER[kind];
  const play = (go) => { fmxStop(); if (!go) { setLit(-1); setCur(-1); return; }
    const steps = []; ord.forEach((b, s) => bars[b].n.forEach(() => steps.push(s)));
    fmxPlayNotes(fmxRoadNotes(bars, ord), (k) => { if (k === -1) { setLit(-1); setCur(-1); return; } const s = steps[k]; setLit(ord[s]); setCur(Math.floor(s / 4)); }); };
  const playing = lit >= 0;
  return (
    <div className="try-box" style={actBox} data-fmx={'pad-' + kind}>
      <div style={actTitle}>{kind === 'bin' ? t('Binary form', '2부 형식') : t('Ternary form', '3부 형식')}</div>
      <div style={actNote}>{fmxKoT(kind === 'bin' ? t('▶ plays it with both repeats. Watch the letters.', '▶를 누르면 도돌이표대로 들려요. 글자를 봐요.') : t('▶ plays it: A, B, then D.C. back to A, to Fine.', '▶를 누르면 들려요: A, B, 그다음 D.C.에서 A로 돌아가 Fine까지.'))}</div>
      <SgnRoad bars={bars} rows={[[0, 1], [2, 3], [4, 5], [6, 7]]} rw={270} o={{ ts: 4, nums: true, lit: lit >= 0 ? lit : null, coral: kind === 'bin' ? ['start', 'end'] : ['fine', 'dc'] }} label={kind === 'bin' ? t('Binary form: two sections, each between repeat signs.', '2부 형식: 도돌이표 안의 두 부분.') : t('Ternary form: Fine after bar 4, D.C. al Fine after bar 8.', '3부 형식: 4마디 뒤 Fine, 8마디 뒤 D.C. al Fine.')}/>
      <div style={{margin:'10px 0 0'}}>{fmxGroups(kind, cur, 15, kind === 'ter')}</div>
      {fmxMsg(kind === 'bin' ? t('A A B B: two sections, each twice: binary form.', 'A A B B: 두 부분을 두 번씩: 2부 형식.') : t('A B A: A comes back, so ternary form.', 'A B A: A가 돌아오니까 3부 형식.'))}
      <div style={{display:'flex',justifyContent:'center'}}>{fmxStopBtn(playing, play)}</div>
    </div>
  );
}
// page 6: find the form: hear how each section starts, give it a letter, then name the form
function FmxFindPad() {
  const [ls, setLs] = useState(['A', '', '']), [name, setName] = useState(null), [on, setOn] = useState(-1);
  useEffect(() => () => fmxStop(), []);
  const hear = (j) => { fmxStop(); setOn(j); fmxPlay(FMX_PIECE[FMX_SEC[j]], (p) => { if (p === -1) setOn(-1); }); };
  const cyc = (j) => { if (j === 0) return; const c = ls.slice(); c[j] = { '': 'A', A: 'B', B: 'A' }[ls[j]]; setLs(c); setName(null); };
  const lettersOk = ls.join('') === 'ABA', ok = lettersOk && name === 'ternary';
  return (
    <div className="try-box" style={actBox} data-fmx="pad-find">
      <div style={actTitle}>{t('Find the form', '형식 찾기')}</div>
      <div style={actNote}>{fmxKoT(t('A piece in three sections. ▶ plays each section. Give each a letter, then name the form.', '세 부분으로 된 곡. ▶를 누르면 부분이 하나씩 들려요. 글자를 붙인 다음 형식 이름을 골라요.'))}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:8,maxWidth:330,margin:'0 auto'}}>{[0, 1, 2].map(j => <div key={j} style={{display:'flex',flexDirection:'column',gap:6,alignItems:'stretch'}}>
        <div style={{textAlign:'center',fontSize:12,fontWeight:800,color:BK.muted}}>{t('bars ' + (j * 8 + 1) + '–' + (j * 8 + 8), (j * 8 + 1) + '~' + (j * 8 + 8) + '마디')}</div>
        <button type="button" data-fmx={'flet' + j} onClick={() => cyc(j)} disabled={j === 0} style={{height:56,borderRadius:8,border:'1.8px ' + (ls[j] ? 'solid ' : 'dashed ') + PEN_N,background:'#fff',fontFamily:LB_SERIF,fontSize:26,fontWeight:900,color:j === 2 && ok ? PEN_C : PEN_N,cursor:j ? 'pointer' : 'default'}}>{ls[j] || '?'}</button>
        <button type="button" data-fmx={'fplay' + j} onClick={() => hear(j)} style={{minHeight:44,borderRadius:8,border:'1.5px solid ' + (on === j ? PEN_C : 'rgba(38,41,107,0.25)'),background:'#fff',color:on === j ? PEN_C : PEN_N,fontWeight:900,cursor:'pointer'}}>▶</button></div>)}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,maxWidth:300,margin:'12px auto 0'}}>{['binary', 'ternary'].map(n => <button key={n} className={'chip' + (name === n ? ' active' : '')} style={{minHeight:44,justifyContent:'center',fontWeight:900}} onClick={() => setName(n)}>{n === 'binary' ? t('binary', '2부 형식') : t('ternary', '3부 형식')}</button>)}</div>
      {fmxMsg(name == null ? t('Same music, same letter.', '같은 음악은 같은 글자.') : ok ? t('A B A: A comes back, so ternary form. ✓', 'A B A: A가 돌아오니까 3부 형식. ✓') : !lettersOk ? t('Listen to each section again: which two are the same?', '부분을 다시 들어요: 어느 둘이 같나요?') : t('A comes back after B: how many sections?', 'B 다음에 A가 돌아와요: 부분이 몇 개인가요?'), name != null && !ok)}
    </div>
  );
}
// the end: build a piece from A and B sections (the first always A); it names the form when it is binary or ternary.
// The phrases chosen so the piece ends on C: ending on B, A is phrase B (rests on G) and B is phrase E (rests on C);
// ending on A, A is phrase A (rests on C) and B is phrase C (rests on D)
const fmxBuildIds = (ls) => ls[ls.length - 1] === 'B' ? ls.map(l => l === 'A' ? 'B' : 'E') : ls.map(l => l === 'A' ? 'A' : 'C');
function FmxBuildPad() {
  const [ls, setLs] = useState(['A', 'B', 'A']), [cur, setCur] = useState(-1);
  useEffect(() => () => fmxStop(), []);
  const set = (x) => { fmxStop(); setCur(-1); setLs(x); };
  const tog = (j) => { if (j === 0) return; const c = ls.slice(); c[j] = c[j] === 'A' ? 'B' : 'A'; set(c); };
  const s = ls.join(' '), name = s === 'A B' || s === 'A A B B' ? 'bin' : s === 'A B A' ? 'ter' : null;
  const play = (go) => { fmxStop(); if (!go) { setCur(-1); return; } fmxPlay(fmxBuildIds(ls), (p) => setCur(p)); };
  return (
    <div className="try-box" style={actBox} data-fmx="pad-build">
      <div style={actTitle}>{t('Build a piece', '곡 만들기')}</div>
      <div style={actNote}>{fmxKoT(t('Each box is a section as you play it, in order. The first is A. Tap a box to change it; + adds one, − takes one off. ▶ plays your piece.', '상자 하나가 치는 차례대로 한 부분이에요. 첫 상자는 A. 상자를 누르면 바뀌고, +는 하나 더, −는 하나 빼요. ▶를 누르면 내 곡이 들려요.'))}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'0 0 8px'}}>{[['A', 'B'], ['A', 'B', 'A'], ['A', 'A', 'B', 'B']].map(x => <button key={x.join('')} className={'chip' + (s === x.join(' ') ? ' active' : '')} style={{minHeight:44,fontFamily:LB_SERIF,fontWeight:900}} onClick={() => set(x)}>{x.join(' ')}</button>)}</div>
      <div style={{display:'flex',gap:8,justifyContent:'center',alignItems:'center',flexWrap:'wrap'}}>
        {ls.map((l, j) => <button key={j} type="button" data-fmx={'blk' + j} onClick={() => tog(j)} disabled={j === 0} aria-label={t('Section ' + (j + 1) + ': ' + l, fmxNth(j + 1) + ' 부분: ' + l)} style={{width:56,height:56,borderRadius:8,border:'1.8px solid ' + (j === cur ? PEN_C : PEN_N),background:j === cur ? PEN_C : '#fff',color:j === cur ? '#fff' : PEN_N,fontFamily:LB_SERIF,fontSize:26,fontWeight:900,cursor:j ? 'pointer' : 'default'}}>{l}</button>)}
        <button type="button" aria-label={t('Add a section', '부분 더하기')} disabled={ls.length >= 5} onClick={() => set(ls.concat(['A']))} className="ghost-btn" style={{minWidth:44,minHeight:44}}>+</button>
        <button type="button" aria-label={t('Take a section off', '부분 빼기')} disabled={ls.length <= 2} onClick={() => set(ls.slice(0, -1))} className="ghost-btn" style={{minWidth:44,minHeight:44}}>−</button></div>
      {fmxMsg(s === 'A B' ? t('A B: two sections: binary form.', 'A B: 두 부분: 2부 형식.') : s === 'A A B B' ? t('A A B B: A twice, then B twice: binary form.', 'A A B B: A를 두 번, B를 두 번: 2부 형식.') : name === 'ter' ? t('A B A: A comes back, so ternary form.', 'A B A: A가 돌아오니까 3부 형식.') : t('Your piece: ' + s + '.', '내 곡: ' + s + '.'))}
      <div style={{display:'flex',justifyContent:'center'}}>{fmxStopBtn(cur >= 0, play)}</div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step; a piece of my own at the end ──
function FmxLearn({ onStart }) {
  const pages = fmxLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="form" title={bkChapterName('form')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="form"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
      <Step key="map" extra title={t('My piece', '나의 곡')} storeAs="k7"><FmxBuildPad/></Step>
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order ──
const FMX_LEVELS = [
  { n: 1, label: 'Same or different?', kind: 'sd', time: 10 },
  { n: 2, label: 'Which letter?', kind: 'letter', time: 14 },
  { n: 3, label: 'Listen: same or different?', kind: 'earSd', time: 22, noPrint: true },
  { n: 4, label: 'Bar, phrase, section or piece?', kind: 'part', time: 8 },
  { n: 5, label: 'Binary or ternary?', kind: 'bt', time: 8 },
  { n: 6, label: 'Listen: binary or ternary?', kind: 'earBt', time: 30, noPrint: true },
  { n: 7, label: 'Read the road', kind: 'road', time: 16 },
  { n: 8, label: 'The words', kind: 'word', time: 10 },
  { n: 9, label: 'Extra: four phrases, four letters', kind: 'pattern', time: 22 },
];
Object.assign(LEVEL_KO, { 'Same or different?': '같을까, 다를까?', 'Which letter?': '어떤 글자일까요?', 'Listen: same or different?': '듣기: 같을까, 다를까?', 'Bar, phrase, section or piece?': '마디? 프레이즈? 부분? 곡 전체?',
  'Binary or ternary?': '2부 형식? 3부 형식?', 'Listen: binary or ternary?': '듣기: 2부 형식? 3부 형식?', 'Read the road': '길 읽기', 'The words': '용어', 'Extra: four phrases, four letters': '더 해 보기: 네 프레이즈, 네 글자' });
const FMX_IDS = Object.keys(FMX_PH);
// letters for a row of phrases: the first A; the same phrase keeps its letter; a new one takes the next
const fmxLettersOf = (ids) => { const m = {}; let n = 0; return ids.map(id => m[id] || (m[id] = 'ABCD'[n++])); };
const FMX_PATTERNS = ['AABA', 'ABAB', 'AABB', 'ABBA', 'ABAC', 'ABCA', 'AAAB', 'ABCB'];
// one phrase per letter; the last letter's phrase ends on C (A or E), so the tune ends at home
const fmxIdsFor = (pat) => { const L = pat[pat.length - 1], h = pick(['A', 'E']), ids = shuffle(FMX_IDS.filter(x => x !== h)), m = { [L]: h }; let n = 0; return pat.split('').map(l => m[l] || (m[l] = ids[n++])); };
const FMX_WORDS = [
  ['form', 'how a piece is built: the order of its sections', '곡이 짜인 모양'],
  ['phrase', 'a musical sentence, often four bars', '음악의 한 문장, 보통 4마디'],
  ['phrase mark', 'a long curve over or under a phrase', '프레이즈 위나 아래의 긴 곡선'],
  ['section', 'a large part of a piece, one or more phrases long', '곡을 크게 나눈 덩어리, 프레이즈 하나 이상'],
  ['repetition', 'the same music again', '같은 음악이 다시 나오는 것'],
  ['contrast', 'new music, different from what came before', '앞과 다른 새 음악'],
  ['binary form', 'two sections: A B', '두 부분: A B'],
  ['ternary form', 'three sections: A B A', '세 부분: A B A'],
];
const FMX_WORD_KO2 = { form: '형식', phrase: '프레이즈', 'phrase mark': '프레이즈 표시', section: '부분', repetition: '반복', contrast: '대조', 'binary form': '2부 형식', 'ternary form': '3부 형식' };
const FMX_PART_KO = { bar: '마디', phrase: '프레이즈', section: '부분', piece: '곡 전체' };
const FMX_ROADS = {
  bin: { bars: FMX_BIN, ls: 'A A B B' },
  ter: { bars: FMX_TER, ls: 'A B A' },
  repA: { bars: (() => { const a = fmxBars('B'), b = fmxBars('E'); return [{ n: a[0] }, { n: a[1] }, { n: a[2] }, { n: a[3], end: true }, { n: b[0] }, { n: b[1] }, { n: b[2] }, { n: b[3] }]; })(), ls: 'A A B' },
  plain: { bars: (() => { const a = fmxBars('B'), b = fmxBars('E'); return [{ n: a[0] }, { n: a[1] }, { n: a[2] }, { n: a[3], dbl: true }, { n: b[0] }, { n: b[1] }, { n: b[2] }, { n: b[3] }]; })(), ls: 'A B' },
};
// listening, binary or ternary: phrases chosen so the piece ends on C (binary: A away, B home; ternary: A home, B away)
const FMX_EAR_PH = { bin: { A: ['B', 'C', 'D'], B: ['A', 'E'] }, ter: { A: ['A', 'E'], B: ['B', 'C', 'D'] } };
function genFmxQuestion(lv, prev) {
  const uid = Math.random(), same = (key) => prev && prev.key === key;
  for (let g = 0; g < 40; g++) {
    if (lv.kind === 'sd' || lv.kind === 'earSd') {
      const a = pick(FMX_IDS), sm = Math.random() < 0.5, b = sm ? a : pick(FMX_IDS.filter(x => x !== a)), key = lv.kind + a + b;
      if (same(key)) continue;
      return { kind: lv.kind, key, ids: [a, b], answer: sm ? 'same' : 'different', choices: ['same', 'different'], uid };
    }
    if (lv.kind === 'letter') {
      const pat = pick(FMX_PATTERNS), ids = fmxIdsFor(pat), ls = fmxLettersOf(ids), key = 'l' + ids.join('');
      if (same(key)) continue;
      const known = [...new Set(ls.slice(0, 3))], next = 'ABCD'[known.length], choices = known.concat([next]).sort();
      return { kind: 'letter', key, ids, ls, answer: ls[3], choices, uid };
    }
    if (lv.kind === 'part') {
      const kind = pick(['bar', 'phrase', 'section', 'piece']), i = kind === 'bar' ? Math.floor(Math.random() * 24) : kind === 'phrase' ? Math.floor(Math.random() * 6) : kind === 'section' ? Math.floor(Math.random() * 3) : 0, key = 'p' + kind + i;
      if (same(key)) continue;
      return { kind: 'part', key, sel: { kind, i }, answer: kind, choices: ['bar', 'phrase', 'section', 'piece'], uid };
    }
    if (lv.kind === 'bt' || lv.kind === 'earBt') {
      // binary or ternary half the time each; level 5's two binary pictures never come twice running (one ternary picture may)
      const ter = Math.random() < 0.5, bins = lv.kind === 'bt' ? [['A', 'B'], ['A', 'A', 'B', 'B']].filter(x => !prev || prev.ls == null || prev.ls.join('') !== x.join('')) : [['A', 'B']], ls = ter ? ['A', 'B', 'A'] : pick(bins);
      const ph = lv.kind === 'earBt' ? { A: pick(FMX_EAR_PH[ter ? 'ter' : 'bin'].A), B: pick(FMX_EAR_PH[ter ? 'ter' : 'bin'].B) } : null, key = lv.kind + ls.join('') + (ph ? ph.A + ph.B : '');
      if (lv.kind === 'earBt' && same(key)) continue;
      return { kind: lv.kind, key, ls, ph, answer: ter ? 'ternary' : 'binary', choices: ['binary', 'ternary'], uid };
    }
    if (lv.kind === 'road') {
      const r = pick(Object.keys(FMX_ROADS)), key = 'r' + r;
      if (same(key)) continue;
      return { kind: 'road', key, r, answer: FMX_ROADS[r].ls, choices: shuffle(Object.values(FMX_ROADS).map(x => x.ls)), uid };
    }
    if (lv.kind === 'word') {
      const wd = pick(FMX_WORDS), key = 'w' + wd[0];
      if (same(key)) continue;
      const wrong = shuffle(FMX_WORDS.filter(x => x[0] !== wd[0])).slice(0, 3).map(x => x[0]);
      return { kind: 'word', key, w: wd, answer: wd[0], choices: shuffle([wd[0], ...wrong]), uid };
    }
    if (lv.kind === 'pattern') {
      const pat = pick(FMX_PATTERNS), ids = fmxIdsFor(pat), key = 'x' + ids.join('');
      if (same(key)) continue;
      const wrong = shuffle(FMX_PATTERNS.filter(p => p !== pat)).slice(0, 3);
      return { kind: 'pattern', key, ids, answer: pat, choices: shuffle([pat, ...wrong]), uid };
    }
  }
  return { kind: 'sd', key: 'f', ids: ['A', 'A'], answer: 'same', choices: ['same', 'different'], uid };
}
const fmxCheck = (q, ans) => ans != null && String(ans) === String(q.answer);
const fmxChoiceTxt = (c, q) => q.kind === 'sd' || q.kind === 'earSd' ? (c === 'same' ? t('same', '같아요') : t('different', '달라요'))
  : q.kind === 'bt' || q.kind === 'earBt' ? (c === 'binary' ? t('binary', '2부 형식') : t('ternary', '3부 형식'))
  : q.kind === 'part' ? t(c === 'piece' ? 'the piece' : c, FMX_PART_KO[c])
  : q.kind === 'word' ? t(c, FMX_WORD_KO2[c])
  : q.kind === 'pattern' ? c.split('').join(' ') : c;
function fmxAnswerLabel(q) {
  if (q.kind === 'word') return t(q.w[0] + ' = ' + q.w[1], FMX_WORD_KO2[q.w[0]] + ' = ' + q.w[2]);
  if (q.kind === 'sd' || q.kind === 'earSd') return q.answer === 'same' ? t('the same music', '같은 음악') : t('different music', '다른 음악');
  if (q.kind === 'part') return { bar: t('a bar', '마디'), phrase: t('a phrase', '프레이즈'), section: t('a section', '부분'), piece: t('the whole piece', '곡 전체') }[q.answer];
  if (q.kind === 'letter') return t(q.answer + ' (' + q.ls.join(' ') + ')', q.answer + ' (' + q.ls.join(' ') + ')');
  if (q.kind === 'bt' || q.kind === 'earBt') return q.ls.join(' ') + ': ' + fmxChoiceTxt(q.answer, q);
  if (q.kind === 'road') return q.answer;
  if (q.kind === 'pattern') return q.answer.split('').join(' ');
  return fmxChoiceTxt(q.answer, q);
}
// blocks of letters (a map of sections); a '?' block dashed
const fmxBlocks = (ls, size = 36, pixel) => <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'2px 0 8px'}}>{ls.map((l, i) => <span key={i} style={{width:size * 1.3,height:size,display:'inline-flex',alignItems:'center',justifyContent:'center',borderRadius:6,border:'1.8px ' + (l === '?' ? 'dashed ' : 'solid ') + (pixel ? '#faf6ec' : PEN_N),fontFamily:LB_SERIF,fontSize:size * 0.6,fontWeight:900,color:pixel ? '#faf6ec' : PEN_N,background:pixel ? 'transparent' : '#fff'}}>{l}</span>)}</div>;
function FmxQuestion({ q, given, locked, onAnswer, pixel }) {
  const paper = locked && !given, isDone = !!given;
  const board = useBoard(q, given), btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const ink = pixel ? '#faf6ec' : 'var(--text)', box = { background: pixel ? '#fff' : 'transparent', borderRadius: pixel ? 0 : 8, padding: pixel ? '2px 0' : 0 };
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const hear = () => { if (q.kind === 'earSd') fmxPlay(q.ids); else if (q.kind === 'earBt') fmxPlay(q.ls.map(l => q.ph[l])); };
  useEffect(() => () => fmxStop(), [q.uid]);
  useEffect(() => { if ((q.kind === 'earSd' || q.kind === 'earBt') && !locked) { const tm = setTimeout(hear, 350); return () => clearTimeout(tm); } }, [q.uid]);
  const prompt = fmxKoT({ sd: t('Same music, or different?', '같은 음악일까요, 다른 음악일까요?'), earSd: t('Listen: same music, or different?', '듣고 골라요: 같은 음악? 다른 음악?'),
    letter: t('Which letter does phrase 4 get?', '4번째 프레이즈에는 어떤 글자를 붙일까요?'), part: t('What is the coral part?', '산호색으로 칠한 곳은 무엇일까요?'),
    bt: t('Binary or ternary?', '2부 형식일까요, 3부 형식일까요?'), earBt: t('Listen: binary or ternary?', '듣고 골라요: 2부 형식? 3부 형식?'),
    road: t('In what order are the sections played?', '부분을 어떤 차례로 칠까요?'), word: t('Which word means this?', '이 뜻의 용어는 무엇일까요?'),
    pattern: t('Which letters do the four phrases get?', '네 프레이즈에 어떤 글자가 붙을까요?') }[q.kind]);
  const n = q.ids ? q.ids.length : 0, w = fmxVbw(['A'], false, 20);
  const row = (id, j, lab) => <div key={j} style={{...box,margin:'0 0 4px'}}><FmxRow ids={[id]} end={q.kind !== 'sd' && j === n - 1} width={w} D={20} letters={lab ? [lab] : null} qmark={lab === '?' ? [0] : []}/></div>;
  let pic = null;
  if (q.kind === 'sd') pic = <>{q.ids.map((id, j) => row(id, j))}</>;
  else if (q.kind === 'letter') pic = <>{q.ids.map((id, j) => row(id, j, j < 3 ? q.ls[j] : isDone ? q.ls[3] : '?'))}</>;
  else if (q.kind === 'pattern') pic = <>{q.ids.map((id, j) => row(id, j, isDone ? fmxLettersOf(q.ids)[j] : String(j + 1)))}</>;
  else if (q.kind === 'part') pic = <div style={{...box,maxWidth:paper ? 600 : 420,margin:'0 auto'}}><FmxMapSvg scr={!paper} quiz sel={q.sel} label={t('A map of a piece with one part coral.', '한 곳을 산호색으로 칠한 곡의 지도.')}/></div>;
  else if (q.kind === 'bt') pic = <>{fmxBlocks(q.ls, pixel ? 30 : 40, pixel)}{q.ls.length === 4 && <div style={{textAlign:'center',fontSize:pixel ? 12 : 13,fontWeight:800,color:pixel ? '#faf6ec' : BK.muted,margin:'-4px 0 6px'}}>{t('each section played twice', '부분마다 두 번씩')}</div>}</>;
  else if (q.kind === 'road') pic = <div style={box}><SgnRoad bars={FMX_ROADS[q.r].bars} rows={[[0, 3], [4, 7]]} rw={330} o={{ ts: 4 }} label={t('An eight-bar road with its signs.', '기호가 있는 여덟 마디 길.')}/></div>;
  else if (q.kind === 'word') pic = <div style={{textAlign:'center',fontSize:pixel ? 13 : 20,fontWeight:900,color:ink,margin:'0 0 6px',textWrap:'balance',wordBreak:'keep-all'}}>“{t(q.w[1], q.w[2])}”</div>;
  else pic = <div style={{textAlign:'center',margin:'4px 0 6px'}}><button className="ghost-btn" style={{minHeight:44}} onClick={hear}>{t('▶ Listen again', '▶ 다시 듣기')}</button>{isDone && q.kind === 'earBt' && fmxBlocks(q.ls, 32)}</div>;
  const cols = q.kind === 'part' || q.kind === 'pattern' || q.kind === 'road' || q.kind === 'word' ? 2 : q.choices.length === 4 ? 4 : q.choices.length === 3 ? 3 : 2;
  return <div>{!paper && <BoardTrack b={board} pixel={pixel}/>}
    <p style={{fontSize:pixel ? 11.5 : 17,fontWeight:900,textAlign:'center',margin:'0 0 8px',color:ink,textWrap:'balance',wordBreak:'keep-all'}}>{prompt}</p>
    {pic && <div style={{margin:'0 auto 8px',maxWidth:q.kind === 'part' ? (paper ? 600 : 420) : paper ? 400 : 460}}>{pic}</div>}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} data-fmx-choice={c} onClick={() => { fmxStop(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:'10px 4px',minHeight:48}}><span style={{fontSize:pixel ? (q.kind === 'letter' ? 20 : q.kind === 'pattern' || q.kind === 'road' ? 15 : 11) : q.kind === 'letter' ? 22 : 16.5,fontWeight:900,fontFamily:q.kind === 'letter' || q.kind === 'pattern' || q.kind === 'road' ? LB_SERIF : undefined,wordBreak:'keep-all'}}>{fmxChoiceTxt(c, q)}</span></button>)}</div>
  </div>;
}
