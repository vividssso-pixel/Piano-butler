// ─── Phase 482: chapter 26's pads (pages 1 to 6, and "in order" at the end), the screen lesson and the drill ───
const cpxMsg = (msg, bad) => <div role="status" aria-live="polite" style={{textAlign:'center',fontSize:15,fontWeight:900,color:bad ? BK.coral : BK.ink,minHeight:22,margin:'8px 0 6px',textWrap:'balance',wordBreak:'keep-all'}}>{cpxKoT(msg)}</div>;
// one sound at a time. A pad (its owner) hears when its sound stops, whoever stops it; a pad that leaves stops only its own.
let _cpxTm = null, _cpxEnd = null, _cpxOwner = null;
function cpxStop(owner) {
  if (owner !== undefined && owner !== _cpxOwner) return;
  if (_cpxTm) clearTimeout(_cpxTm); _cpxTm = null; _cpxOwner = null; stopClicks();
  const e = _cpxEnd; _cpxEnd = null; if (e) e();
}
// a composer's sound: the piece the chapter names where the app has it, else their first (a real opening, or bars in their style)
const CPX_CLIP = { beethoven: 'Für Elise', chopin: '“Minute” Waltz, Op. 64 No. 1' };
const cpxSound = (id) => { const l = (CMP_HEAR[id] || []).filter(cmpHasSound), h = (CPX_CLIP[id] && l.find(x => x.title && x.title[0] === CPX_CLIP[id])) || cmpFirstSound(cmpById(id)); return cmpHasSound(h) ? h : null; };
function cpxHear(id, onEnd, owner) {
  cpxStop(); const h = cpxSound(id); if (!h) return 0;
  const s = cmpPlay(h); if (!s) return 0;
  _cpxEnd = onEnd || null; _cpxOwner = owner;
  _cpxTm = setTimeout(() => { _cpxTm = null; _cpxOwner = null; const e = _cpxEnd; _cpxEnd = null; if (e) e(); }, s * 1000 + 250); return s;
}
const cpxIsTune = (id) => { const h = cpxSound(id); return !!(h && h.kind === 'tune' && h.title); };
const cpxSoundName = (id) => { const h = cpxSound(id), c = cmpById(id); if (!h) return ''; return cpxIsTune(id) ? cmpT(h.title).replace(/: [^:]*!$/, '') : t('a few bars in the style of ' + mtlSur(c), mtlSur(c) + '풍의 짧은 음악'); };
// Korean particles after a word: a if it ends on a closed syllable, else b. Quotes and a last (bracket) are skipped; a
// number is read in Korean (0 영/십, 1 일, 3 삼, 6 육, 7 칠, 8 팔 are closed).
const cpxJ = (w, a, b) => { const base = String(w).replace(/\s*\([^)]*\)\s*$/, ''), s = base.replace(/[”’"')\]\s.]+$/, ''), ch = s.slice(-1), c = ch.charCodeAt(0);
  const closed = c >= 0xAC00 && c <= 0xD7A3 ? (c - 0xAC00) % 28 > 0 : /[013678]/.test(ch); return base + (closed ? a : b); };
// the width a drawing really has (one SVG unit a CSS pixel), up to max
function useCpxW(max = 680) {
  const ref = React.useRef(null), [w, setW] = useState(() => { try { return Math.min(max, Math.max(200, window.innerWidth - 70)); } catch (e) { return max; } });
  useEffect(() => { const el = ref.current; if (!el) return;
    const set = () => { const r = Math.round(el.getBoundingClientRect().width); if (r > 0) setW(Math.min(max, Math.max(200, r))); }; set();
    if (typeof ResizeObserver === 'undefined') { window.addEventListener('resize', set); return () => window.removeEventListener('resize', set); }
    const ro = new ResizeObserver(set); ro.observe(el); return () => ro.disconnect(); }, []);
  return [ref, w];
}
// a Stop that stays in the tab order when there is nothing to stop
const cpxStopBtn = (playing, stop) => <button type="button" className="ghost-btn" aria-disabled={!playing} onClick={playing ? stop : undefined} style={{minHeight:44,...(playing ? {} : { opacity: 0.3, cursor: 'default' })}}>{t('■ Stop', '■ 멈추기')}</button>;
// the composer heard when a period is tapped
const CPX_ERA_SOUND = { baroque: 'bach', classical: 'mozart', romantic: 'chopin', modern: 'joplin', contemporary: 'hisaishi' };
const cpxList = (ids) => { const n = ids.map(id => mtlSur(cmpById(id))); return LANG === 'ko' || n.length < 2 ? n.join(', ') : n.slice(0, -1).join(', ') + ' and ' + n[n.length - 1]; };
const cpxNowKo = (id) => (cpxIsTune(id) ? mtlSur(cmpById(id)) + '의 ' : '') + cpxSoundName(id);
const cpxChip = (on, label, onClick, key) => <button key={key} type="button" className={'chip' + (on ? ' active' : '')} aria-pressed={!!on} onClick={onClick} style={{minHeight:44,padding:'4px 12px',fontSize:14,fontWeight:800}}>{label}</button>;

// page 1: the timeline. A period (its chip or its band) lights its composers, shows them as buttons and plays one of
// them; a composer plays. It fits the width: on phones only the periods, keyboards and composers.
function MtlMapPad() {
  const me = React.useRef({}).current, [box, w] = useCpxW();
  const [sel, setSel] = useState(null), [era, setEra] = useState(null), [playing, setPlaying] = useState(false);
  useEffect(() => () => cpxStop(me), []);
  const go = (kind, id) => { setEra(kind === 'era' ? id : cmpById(id).era); setSel({ kind, id });
    setPlaying(cpxHear(kind === 'cmp' ? id : CPX_ERA_SOUND[id], () => setPlaying(false), me) > 0); };
  const eraIds = (id) => CPX_IDS.filter(x => cmpById(x).era === id), wide = w >= 480;
  let msg = t('Tap a period or a composer. Hear them.', '시대나 작곡가를 눌러요. 소리가 들려요.');
  if (sel && sel.kind === 'era') { const s = CPX_ERA_SOUND[sel.id];
    msg = t(cmpEraTag(sel.id) + ', ' + cpxYrs(sel.id) + '.' + (playing ? ' Playing: ' + (cpxIsTune(s) ? mtlSur(cmpById(s)) + '’s ' : '') + cpxSoundName(s) + '.' : ''),
      cmpEraTag(sel.id) + ', ' + cpxYrs(sel.id) + '.' + (playing ? ' 듣는 곡: ' + cpxNowKo(s) + '.' : '')); }
  if (sel && sel.kind === 'cmp') { const c = cmpById(sel.id);
    msg = t(cmpT(c.name) + ', ' + mtlLife(c) + ', ' + cmpEraLabel(c) + '.' + (playing ? ' Playing: ' + cpxSoundName(sel.id) + '.' : ''), cmpT(c.name) + ', ' + mtlLife(c) + ', ' + cmpEraLabel(c) + '.' + (playing ? ' 듣는 곡: ' + cpxSoundName(sel.id) + '.' : '')); }
  return (
    <div className="try-box" style={actBox} data-cpx="pad-map">
      <div style={actTitle}>{t('The timeline of music', '음악의 타임라인')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{cpxKoT(t('Tap a period or a composer’s line. Hear them.', '시대나 작곡가의 선을 눌러요. 소리가 들려요.'))}</div>
      <div role="group" aria-label={t('Periods', '시대')} style={{display:'flex',flexWrap:'wrap',justifyContent:'center',gap:6,margin:'0 0 8px'}}>{MTL_ERAS.map(id => cpxChip(sel && sel.kind === 'era' && sel.id === id, cmpEraTag(id), () => go('era', id), id))}</div>
      <div ref={box}><MusTimeline W={w} stack fs={11} laneH={15} barH={8} guides firstPiano={wide} rowLabels={wide} rows={['era', 'keys', 'cmp']}
        sel={sel} lit={sel && sel.kind === 'era' ? eraIds(sel.id) : []} onTap={go} label={t('The timeline of music, 1600 to today: periods, keyboards and composers. Each period and each composer can be tapped.', '음악의 타임라인, 1600년부터 오늘날까지: 시대, 건반 악기, 작곡가. 시대와 작곡가를 하나씩 누를 수 있어요.')}/></div>
      {era && <div role="group" aria-label={t('Composers', '작곡가')} style={{display:'flex',flexWrap:'wrap',justifyContent:'center',gap:6,margin:'8px 0 0'}}>{eraIds(era).map(id => cpxChip(sel && sel.kind === 'cmp' && sel.id === id, mtlSur(cmpById(id)), () => go('cmp', id), id))}</div>}
      {cpxMsg(msg)}
      <div style={{display:'flex',justifyContent:'center'}}>{cpxStopBtn(playing, () => cpxStop())}</div>
    </div>
  );
}

// pages 2 to 5: one period: its stretch of the timeline and its who's who; a composer tapped plays, with one fact
function CpxPeriodPad({ k }) {
  const me = React.useRef({}).current, [box, w] = useCpxW();
  const P = CPX_PAGES[k], [sel, setSel] = useState(null), [playing, setPlaying] = useState(false);
  useEffect(() => () => cpxStop(me), []);
  const go = (id) => { setSel(id); setPlaying(cpxHear(id, () => setPlaying(false), me) > 0); };
  const c = sel && cmpById(sel), nm = sel && cpxSoundName(sel), lab = k === 3 ? t('Modern and Contemporary', '근대와 현대') : cmpEraTag(P.era);
  return (
    <div className="try-box" style={actBox} data-cpx={'pad-era' + k}>
      <div style={actTitle}>{lab}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{cpxKoT(t('Tap a composer: hear their music and read one fact.', '작곡가를 눌러요: 음악을 듣고 이야기 하나를 읽어요.'))}</div>
      <div ref={box} style={{margin:'0 0 6px'}}><MusTimeline big W={w} rowLabels={w >= 480} from={P.from} to={P.to} rows={['era', 'keys', 'cmp']} ids={P.ids} sel={sel ? { kind: 'cmp', id: sel } : null} onTap={(kind, id) => go(id)} tapKinds={['cmp']} firstPiano={k === 0 && w >= 340} label={t(lab + ': the composers on the timeline; each can be tapped.', lab + ': 타임라인 위의 작곡가들. 하나씩 누를 수 있어요.')}/></div>
      <CpxWho ids={P.ids} onTap={go} sel={sel} cols={w < 480 ? 1 : 2} scr/>
      {c ? <div role="status" aria-live="polite" style={{margin:'10px 0 6px',padding:'8px 12px',border:'1px solid rgba(38,41,107,0.18)',borderRadius:8,background:'#fff',fontSize:14.5,lineHeight:1.5,color:BK.ink,wordBreak:'keep-all'}}>
          <b style={{color:BK.coral}}>{cmpT(c.name)}</b> · {mtlLife(c)}<span style={{color:BK.muted}}> · {nm ? (playing ? t('Playing: ', '듣는 곡: ') : '') + nm : t('no music to hear for this one', '이 작곡가는 들어 볼 곡이 없어요')}</span>
          <span style={{display:'block',marginTop:4}}>{cpxKoT(cmpT(c.fun))}</span></div>
        : cpxMsg(t('Tap a name.', '이름을 눌러요.'))}
      <div style={{display:'flex',justifyContent:'center'}}>{cpxStopBtn(playing, () => cpxStop())}</div>
    </div>
  );
}

// page 6: a line down from one year: who was alive then (and who was born, or died, that year)
const CPX_P6 = CPX_PAGES.slice(0, 3).flatMap(p => p.ids);
function CpxAlivePad() {
  const [box, w] = useCpxW(), [y, setY] = useState(1785);
  const alive = CPX_P6.filter(id => mtlAlive(cmpById(id), y)), born = CPX_P6.filter(id => cmpById(id).born === y), died = CPX_P6.filter(id => cmpById(id).died === y);
  const msg = t('In ' + y + ': ' + (alive.length ? cpxList(alive) + (alive.length > 1 ? ' were' : ' was') + ' alive.' : 'none of them was alive.') + (born.length ? ' Born that year: ' + cpxList(born) + '.' : '') + (died.length ? ' Died that year: ' + cpxList(died) + '.' : ''),
    y + '년: ' + (alive.length ? cpxJ(cpxList(alive), '이', '가') + ' 살아 있었어요.' : '이 중 아무도 살아 있지 않았어요.') + (born.length ? ' 그해에 태어난 사람: ' + cpxList(born) + '.' : '') + (died.length ? ' 그해에 세상을 떠난 사람: ' + cpxList(died) + '.' : ''));
  return (
    <div className="try-box" style={actBox} data-cpx="pad-alive">
      <div style={actTitle}>{t('Who was alive?', '누가 살아 있었을까?')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{cpxKoT(t('Slide to a year. The composers the line crosses light up.', '해를 골라요. 선이 지나는 작곡가가 밝게 표시돼요.'))}</div>
      <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(52px,1fr))',gap:4,maxWidth:420,margin:'0 auto 6px'}}>{[1685, 1745, 1785, 1815, 1845].map(v => <button key={v} type="button" className={'chip' + (y === v ? ' active' : '')} aria-pressed={y === v} onClick={() => setY(v)} style={{minHeight:44,padding:'4px 0',fontSize:14,fontWeight:800}}>{v}</button>)}</div>
      <div style={{display:'flex',alignItems:'center',gap:8,margin:'0 0 6px'}}>
        <button type="button" className="ghost-btn" aria-label={t('One year earlier', '한 해 전')} onClick={() => setY(v => Math.max(1670, v - 1))} style={{minHeight:44,minWidth:44}}>−</button>
        <input type="range" min={1670} max={1910} value={y} onChange={(e) => setY(+e.target.value)} aria-label={t('Year', '연도')} aria-valuetext={String(y)} style={{flex:1,minWidth:0,height:44,margin:0,accentColor:BK.coral}}/>
        <button type="button" className="ghost-btn" aria-label={t('One year later', '한 해 뒤')} onClick={() => setY(v => Math.min(1910, v + 1))} style={{minHeight:44,minWidth:44}}>+</button></div>
      <div ref={box}><MusTimeline stack W={w} rowLabels={w >= 480} fs={12} laneH={18} barH={10} from={1670} to={1910} rows={['era', 'cmp']} ids={CPX_P6} year={y} label={t('Fifteen lives, Baroque to Romantic, with a line down from ' + y + '.', '바로크부터 낭만주의까지 열다섯 명의 생애와 ' + y + '년에서 내려온 선.')}/></div>
      {cpxMsg(msg)}
    </div>
  );
}

// the end: four composers born at least 12 years apart (two may share a period): tap them in the order they were born
function cpxFour(prev) { const k = (a) => [...a].sort().join();
  for (let g = 0; g < 200; g++) { const ids = sampleN(CPX_IDS, 4), b = ids.map(id => cmpById(id).born).sort((x, y) => x - y);
    if (b.slice(1).some((v, i) => v - b[i] < 12) || (prev && k(ids) === k(prev))) continue; return ids; }
  return shuffle(CPX_PAGES.map(p => pick(p.ids))); }
function CpxOrderPad() {
  const [box, w] = useCpxW(), [four, setFour] = useState(() => cpxFour()), [done, setDone] = useState([]), [bad, setBad] = useState(null);
  const order = [...four].sort((a, b) => cmpById(a).born - cmpById(b).born), all = done.length === 4;
  const tap = (id) => { if (done.includes(id) || all) return; if (id === order[done.length]) { setDone(d => [...d, id]); setBad(null); } else setBad(id); };
  const again = () => { setFour(f => cpxFour(f)); setDone([]); setBad(null); };
  const last = done.length ? mtlSur(cmpById(done[done.length - 1])) : '';
  const msg = all ? t('All four in order: ' + done.map(id => mtlSur(cmpById(id)) + ' ' + cmpById(id).born).join(', ') + '.', '네 명 모두 차례대로: ' + done.map(id => mtlSur(cmpById(id)) + ' ' + cmpById(id).born).join(', ') + '.')
    : bad ? t('Not yet: someone else was born earlier.', '아직 아니에요: 더 일찍 태어난 사람이 있어요.') : t(done.length ? 'Next: who was born after ' + last + '?' : 'Who was born first?', done.length ? last + ' 다음에는 누가 태어났을까요?' : '누가 제일 먼저 태어났을까요?');
  return (
    <div className="try-box" style={actBox} data-cpx="pad-order">
      <div style={actTitle}>{t('In order', '차례대로')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{cpxKoT(t('Tap the four in the order they were born. Each one joins the timeline.', '네 명을 태어난 차례대로 눌러요. 누를 때마다 타임라인에 나타나요.'))}</div>
      <div role="group" aria-label={t('Composers', '작곡가')} style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:420,margin:'0 auto 8px'}}>{four.map(id => { const k = done.indexOf(id);
        return <button key={id} type="button" aria-disabled={k >= 0 || all} onClick={() => tap(id)} className={'choice-btn' + (k >= 0 ? ' good' : bad === id ? ' bad' : '')} style={{minHeight:48,fontSize:15.5,fontWeight:900,wordBreak:'keep-all'}}>{k >= 0 ? (k + 1) + '. ' : ''}{cmpT(cmpById(id).name)}</button>; })}</div>
      <div ref={box}><MusTimeline W={w} rowLabels={w >= 480} fs={12} laneH={18} barH={10} rows={['era', 'cmp']} ids={done} lit={all ? [] : done.slice(-1)} label={t('The timeline with the composers placed so far: ' + (done.length ? cpxList(done) : 'none yet') + '.', '지금까지 놓은 작곡가가 있는 타임라인: ' + (done.length ? cpxList(done) : '아직 없음') + '.')}/></div>
      {cpxMsg(msg, !!bad && !all)}
      <div style={{display:'flex',justifyContent:'center'}}>{(all || done.length > 0) && chxBtn('n', all ? t('Four more', '다른 네 명') : t('Start again', '처음부터'), again, false)}</div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step; "in order" at the end ──
function CpxLearn({ onStart }) {
  const pages = cpxLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="composers" title={bkChapterName('composers')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="composers"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
      <Step key="order" extra title={t('In order', '차례대로')} storeAs="k7"><CpxOrderPad/></Step>
    </Lesson>
  );
}

// ── the drill, after page 6: the map first (a year), then the composers ──
const CPX_LEVELS = [
  { n: 1, label: 'Which period is this year in?', kind: 'year', time: 10 },
  { n: 2, label: 'Which period?', kind: 'era', time: 10 },
  { n: 3, label: 'Who was born first?', kind: 'first', time: 10 },
  { n: 4, label: 'Alive at the same time?', kind: 'same', time: 12 },
  { n: 5, label: 'Who wrote it?', kind: 'wrote', time: 12 },
  { n: 6, label: 'Listen: Baroque, Classical or Romantic?', kind: 'earEra', time: 18, noPrint: true },
  { n: 7, label: 'Listen: who wrote it?', kind: 'earWho', time: 18, noPrint: true },
  { n: 8, label: 'The words', kind: 'word', time: 10 },
  { n: 9, label: 'Extra: in order of birth', kind: 'order', time: 18 },
];
Object.assign(LEVEL_KO, { 'Which period?': '어느 시대일까요?', 'Which period is this year in?': '이 해는 어느 시대일까요?', 'Who was born first?': '누가 먼저 태어났을까요?', 'Alive at the same time?': '같은 시기에 살았을까요?',
  'Who wrote it?': '누가 썼을까요?', 'Listen: Baroque, Classical or Romantic?': '듣기: 어느 시대의 음악일까요?', 'Listen: who wrote it?': '듣기: 누가 썼을까요?', 'The words': '용어', 'Extra: in order of birth': '더 해 보기: 태어난 차례' });
const CPX_WORDS = [
  ['composer', 'a person who writes music', '곡을 쓰는 사람'],
  ['period', 'a stretch of years whose music shares a style', '음악 양식이 비슷한 기간'],
  ['counterpoint', 'two or more tunes at once, each as important as the other', '두 개 이상의 선율을 똑같이 중요하게 동시에 엮는 것'],
  ['harpsichord', 'a keyboard whose strings are plucked', '현을 뜯어 소리 내는 건반 악기'],
  ['fortepiano', 'the early piano of Mozart’s time', '모차르트 시대의 초기 피아노'],
  ['Alberti bass', 'a left hand that breaks a chord: lowest, highest, middle, highest', '화음을 맨 아래 음, 맨 위 음, 가운데 음, 맨 위 음으로 펼쳐 치는 왼손 반주'],
  ['rubato', 'time bent for feeling', '표현을 위해 빠르기를 당겼다가 늦추는 것'],
  ['virtuoso', 'a performer with dazzling skill', '놀라운 기교를 가진 연주자'],
  ['Impressionism', 'music of soft colours and moods, about 1890 to 1920', '부드러운 색채와 분위기의 음악(1890~1920년쯤)'],
  ['contemporaries', 'people who lived at the same time', '같은 시기에 살았던 사람들'],
];
const CPX_WORD_KO = { composer: '작곡가', period: '시대', counterpoint: '대위법', harpsichord: '하프시코드', fortepiano: '포르테피아노', 'Alberti bass': '알베르티 베이스', rubato: '루바토', virtuoso: '비르투오소', Impressionism: '인상주의', contemporaries: '동시대인' };
// who can be asked a period: not those across two (Beethoven, Debussy, and Kabalevsky, whose later pieces are Contemporary).
// Listening for the period: real openings only, of the three periods whose sound is taught (marches and lullabies left out).
const CPX_ONE = CPX_IDS.filter(id => !cmpById(id).span && id !== 'kabalevsky');
const CPX_EAR_ERAS = ['baroque', 'classical', 'romantic'];
const CPX_EAR = CPX_ONE.filter(id => cpxIsTune(id) && CPX_EAR_ERAS.includes(cmpById(id).era) && !['schubert', 'rschumann', 'brahms'].includes(id));
const CPX_TUNE = CPX_IDS.filter(cpxIsTune);
const CPX_BOUND = [1750, 1820, 1900, 1950];
const CPX_FILM = /\(film music\)$/;
// a title in Korean text is quoted (unless it already is, or it is a count of pieces); a (bracket) after it is dropped
const cpxKoTitle = (k) => { const s = k.replace(/\s*\(.*\)$/, ''); return /^“/.test(s) || /\d+곡$/.test(s) ? s : '“' + s + '”'; };
const cpxOverlap = (a, b) => Math.min(mtlEnd(a), mtlEnd(b)) - Math.max(a.born, b.born);
// each level remembers its last few questions, so a printed sheet does not ask the same thing twice in a row of them
const _cpxRecent = {};
function genCpxQuestion(lv, prev) {
  const r = _cpxRecent[lv.n] || (_cpxRecent[lv.n] = []), keep = { year: 12, era: 10, earEra: 3, wrote: 11, earWho: 7, word: 8 }[lv.kind] || 12;
  let q = null; for (let g = 0; g < 12; g++) { const x = genCpxQuestion0(lv, prev); if (!x) continue; q = x; if (!r.includes(x.key)) break; }
  if (q) { r.push(q.key); while (r.length > keep) r.shift(); }
  return q;
}
function genCpxQuestion0(lv, prev) {
  const uid = Math.random(), same = (key) => prev && prev.key === key;
  // each period (and yes and no) equally often, whatever the number of composers in it
  const want = { era: pick(lv.kind === 'earEra' ? CPX_EAR_ERAS : MTL_ERAS), yes: Math.random() < 0.5 };
  for (let g = 0; g < 80; g++) {
    if (g === 60) prev = null;   // never stuck on the no-repeat rule
    const kind = lv.kind;
    if (kind === 'era' || kind === 'earEra') {
      const pool = (kind === 'era' ? CPX_ONE : CPX_EAR).filter(x => cmpById(x).era === want.era), id = pick(pool.length ? pool : CPX_ONE); if (same(id)) continue;
      return { kind, key: id, id, answer: cmpById(id).era, choices: kind === 'earEra' ? [...CPX_EAR_ERAS] : [...MTL_ERAS], ids: [id], uid };
    }
    if (kind === 'year') {
      const [a0, b0] = mtlYears(want.era), y = a0 + Math.floor(Math.random() * (Math.min(b0, 2020) - a0)); if (CPX_BOUND.some(b => Math.abs(b - y) < 4) || same(String(y))) continue;
      return { kind, key: String(y), year: y, answer: mtlEraOf(y), choices: [...MTL_ERAS], uid };
    }
    if (kind === 'first') {
      const [a, b] = sampleN(CPX_IDS, 2).map(cmpById); if (Math.abs(a.born - b.born) < 15) continue;
      const key = [a.id, b.id].sort().join('-'); if (same(key)) continue;
      return { kind, key, answer: (a.born < b.born ? a : b).id, choices: [a.id, b.id], ids: [a.id, b.id], uid };
    }
    if (kind === 'same') {
      const yes = want.yes, [a, b] = sampleN(CPX_IDS, 2).map(cmpById), ov = cpxOverlap(a, b);
      if (yes ? ov < 10 : ov > -5) continue;
      const key = [a.id, b.id].sort().join('-'); if (same(key)) continue;
      return { kind, key, answer: yes ? 'yes' : 'no', choices: ['yes', 'no'], ids: [a.id, b.id], uid };
    }
    if (kind === 'wrote' || kind === 'earWho') {
      const id = pick(kind === 'wrote' ? CPX_IDS : CPX_TUNE); if (same(id)) continue;
      const era = cmpById(id).era, others = shuffle(CPX_IDS.filter(x => x !== id && cmpById(x).era !== era)).slice(0, 3);
      return { kind, key: id, id, answer: id, choices: shuffle([id, ...others]), ids: [id], uid };
    }
    if (kind === 'word') {
      const w = pick(CPX_WORDS); if (same(w[0])) continue;
      return { kind, key: w[0], w, answer: w[0], choices: shuffle([w[0], ...shuffle(CPX_WORDS.filter(x => x !== w).map(x => x[0])).slice(0, 3)]), uid };
    }
    // order: three composers born at least 15 years apart; four orders to choose from
    const three = sampleN(CPX_IDS, 3).map(cmpById).sort((a, b) => a.born - b.born);
    if (three[1].born - three[0].born < 15 || three[2].born - three[1].born < 15) continue;
    const ids = three.map(c => c.id), key = ids.join('-'); if (same(key)) continue;
    const perms = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]].map(p => p.map(i => ids[i]).join('-'));
    // the names shown in an order that is not the answer
    let shown = shuffle(ids); if (shown.join('-') === key) shown = [shown[1], shown[2], shown[0]];
    return { kind: 'order', key, answer: key, choices: shuffle([key, ...shuffle(perms.slice(1)).slice(0, 3)]), ids, shown, uid };
  }
  return null;
}
const cpxCheck = (q, ans) => ans != null && String(ans) === String(q.answer);
const cpxNm = (id) => mtlSur(cmpById(id));
// the orders break only before an arrow
const cpxChoiceTxt = (c, q) => q.kind === 'era' || q.kind === 'earEra' || q.kind === 'year' ? cmpEraTag(c)
  : q.kind === 'same' ? (c === 'yes' ? t('yes', '네') : t('no', '아니요'))
  : q.kind === 'word' ? t(c, CPX_WORD_KO[c])
  : q.kind === 'order' ? c.split('-').map(cpxNm).join(' → ')
  : cmpT(cmpById(c).name);
function cpxAnswerLabel(q) { return cpxKoT(cpxAnswerLabel0(q)); }
function cpxAnswerLabel0(q) {
  const life = (id) => cpxNm(id) + ' ' + mtlLife(cmpById(id)), lives = (q.ids || []).map(life).join(', ');
  if (q.kind === 'word') return t(q.w[0] + ' = ' + q.w[1], CPX_WORD_KO[q.w[0]] + ' = ' + q.w[2]);
  if (q.kind === 'year') return t(cmpEraTag(q.answer) + ' (' + cpxYrs(q.answer) + ')', cmpEraTag(q.answer) + '(' + cpxYrs(q.answer) + ')');
  if (q.kind === 'era' || q.kind === 'earEra') return t(cmpEraTag(q.answer) + ': ' + life(q.id), cmpEraTag(q.answer) + '(' + life(q.id) + ')') + (q.kind === 'earEra' ? ' · ' + cpxSoundName(q.id) : '');
  if (q.kind === 'same') return t(cpxChoiceTxt(q.answer, q) + ': ' + lives, cpxChoiceTxt(q.answer, q) + '(' + lives + ')');
  if (q.kind === 'first') return t(cmpT(cmpById(q.answer).name) + ': ' + lives, cmpT(cmpById(q.answer).name) + '(' + lives + ')');
  if (q.kind === 'order') return lives;
  if (q.kind === 'earWho') return t(cmpT(cmpById(q.id).name) + ': ' + cpxSoundName(q.id), cmpT(cmpById(q.id).name) + '의 ' + cpxSoundName(q.id));
  if (q.kind === 'wrote') return t(cmpT(cmpById(q.id).name) + ': ' + CPX_PIECE[q.id][0], cmpT(cmpById(q.id).name) + '의 ' + cpxKoTitle(CPX_PIECE[q.id][1]));
  return cpxChoiceTxt(q.answer, q);
}
function CpxQuestion({ q, given, locked, onAnswer, pixel }) {
  const me = React.useRef({}).current, [box, w] = useCpxW(520), givenRef = React.useRef(given); givenRef.current = given;
  const paper = locked && !given, isDone = !!given;
  const board = useBoard(q, given), btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const ink = pixel ? '#faf6ec' : 'var(--text)';
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const ear = q.kind === 'earEra' || q.kind === 'earWho';
  const hear = () => cpxHear(q.id, null, me);
  useEffect(() => () => cpxStop(me), [q.uid]);
  useEffect(() => { if (ear && !locked) { const tm = setTimeout(() => { if (!givenRef.current) hear(); }, 350); return () => clearTimeout(tm); } }, [q.uid]);
  const nm = (id) => cmpT(cmpById(id).name);
  const prompt = cpxKoT(({ era: () => t('In which period did ' + nm(q.id) + ' compose?', cpxJ(nm(q.id), '은', '는') + ' 어느 시대의 작곡가일까요?'), earEra: () => t('Listen: is this music Baroque, Classical or Romantic?', '듣고 골라요: 바로크, 고전주의, 낭만주의 중 어느 시대의 음악일까요?'),
    year: () => t('Which period is this year in?', '이 해는 어느 시대일까요?'), first: () => t('Who was born first?', '누가 먼저 태어났을까요?'),
    same: () => t('Were ' + nm(q.ids[0]) + ' and ' + nm(q.ids[1]) + ' alive at the same time?', cpxJ(nm(q.ids[0]), '과', '와') + ' ' + cpxJ(nm(q.ids[1]), '은', '는') + ' 같은 시기에 살았을까요?'),
    wrote: () => { const [e, k] = CPX_PIECE[q.id]; return CPX_FILM.test(e) ? t('Who wrote the music for ' + e.replace(CPX_FILM, '').trim() + '?', cpxKoTitle(k) + '의 음악을 누가 썼을까요?') : t('Who wrote ' + e + '?', cpxJ(cpxKoTitle(k), '을', '를') + ' 누가 썼을까요?'); },
    earWho: () => t('Listen: who wrote this?', '듣고 골라요: 누가 썼을까요?'),
    word: () => t('Which word means this?', '이 뜻의 용어는 무엇일까요?'), order: () => t('In what order were they born?', '어떤 차례로 태어났을까요?') })[q.kind]());
  let pic = null;
  if (q.kind === 'year') pic = <div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:pixel ? 22 : paper ? 30 : 44,fontWeight:900,color:pixel ? ink : BK.ink,margin:'0 0 4px',fontVariantNumeric:'lining-nums'}}>{q.year}</div>;
  else if (q.kind === 'word') pic = <div style={{textAlign:'center',fontSize:pixel ? 13 : 20,fontWeight:900,color:ink,margin:'0 0 6px',textWrap:'balance',wordBreak:'keep-all'}}>“{cpxKoT(t(q.w[1], q.w[2]))}”</div>;
  else if (q.kind === 'order') pic = <div style={{textAlign:'center',fontSize:pixel ? 13 : 18,fontWeight:900,color:ink,margin:'0 0 6px',wordBreak:'keep-all'}}>{(q.shown || q.ids).map((id, i) => <React.Fragment key={id}>{i > 0 && ' · '}<span style={{whiteSpace:'nowrap'}}>{nm(id)}</span></React.Fragment>)}</div>;
  else if (ear) pic = <div style={{textAlign:'center',margin:'4px 0 6px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={hear}>{t('▶ Listen again', '▶ 다시 듣기')}</button></div>;
  // after an answer: the lives on the timeline (or the year's line on the periods), drawn at the width it has
  const reveal = isDone && !pixel && q.kind !== 'word' ? <div style={{margin:'10px auto 0',maxWidth:520,background:'#fff',borderRadius:8,padding:'6px 0'}}>{q.kind === 'year'
    ? <MusTimeline W={w} fs={12} rows={['era']} year={q.year} hiEra={q.answer} ids={[]} rowLabels={false} label={t(q.year + ' on the timeline of periods.', '시대 타임라인 위의 ' + q.year + '년.')}/>
    : <MusTimeline W={w} fs={12} laneH={18} barH={10} rows={['era', 'cmp']} ids={q.ids} lit={q.ids} hiEra={q.kind === 'era' || q.kind === 'earEra' ? q.answer : null} rowLabels={false} label={t('Their lives on the timeline: ', '타임라인 위의 생애: ') + q.ids.map(id => nm(id) + ' ' + mtlLife(cmpById(id))).join(', ')}/>}</div> : null;
  // the periods: one row of five on paper, sized to their words; two columns on phones (Contemporary across both)
  const eraQ = q.kind === 'era' || q.kind === 'earEra' || q.kind === 'year', narrow = !paper && (pixel || (typeof window !== 'undefined' && window.innerWidth < 520));
  const five = eraQ && paper && q.choices.length === 5;
  const tight = pixel || (typeof window !== 'undefined' && window.innerWidth < 400);
  const cols = q.choices.length === 2 && q.kind === 'same' ? 2 : eraQ ? (paper ? q.choices.length : narrow ? 2 : 3) : tight ? 1 : 2;
  const grid = 'repeat(' + cols + ',minmax(0,1fr))';
  return <div ref={box}>{!paper && <BoardTrack b={board} pixel={pixel}/>}
    <p style={{fontSize:pixel ? 11.5 : 17,fontWeight:900,textAlign:'center',margin:'0 0 8px',color:ink,textWrap:'balance',wordBreak:'keep-all'}}>{prompt}</p>
    {pic}
    <div style={five ? {display:'flex',flexWrap:'wrap',justifyContent:'center',gap:8,maxWidth:680,margin:'0 auto'} : {display:'grid',gridTemplateColumns:grid,justifyContent:'center',gap:8,maxWidth:q.kind === 'order' ? 560 : 520,margin:'0 auto'}}>{q.choices.map((c, j) => <button key={c} disabled={locked} data-cpx-choice={c} onClick={() => { cpxStop(); onAnswer(c); }} className={btnCls + st(c)}
      style={{minHeight:pixel ? undefined : 48,padding:five ? '6px 14px' : '6px 8px',gridColumn:eraQ && !paper && cols === 2 && q.choices.length % 2 && j === q.choices.length - 1 ? 'span 2' : undefined}}>
      <span style={{fontSize:pixel ? 11 : q.kind === 'order' ? 15 : five ? 15 : 16.5,fontWeight:900,wordBreak:'keep-all'}}>{cpxKoT(cpxChoiceTxt(c, q))}</span></button>)}</div>
    {reveal}
  </div>;
}
