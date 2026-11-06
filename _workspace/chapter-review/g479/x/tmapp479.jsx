// ─── Phase 479: chapter 23's pads (pages 1 to 6), the screen lesson and the drill ───
// a word's reading card: the word as printed, its Korean reading, its meaning; hear it, say it
const tmxPron = (e) => { if (!e) return null; const k = e.name || (e.w.charAt(0).toUpperCase() + e.w.slice(1)); return PRON[k] ? k : null; };
const tmxSay = (e) => { const k = tmxPron(e); if (k) { chxStop(); speakTerm({ term: k }); } };
// the parts of a little-word term that are not words of their own in this chapter
const TMX_PART = { mosso: ['movement', '움직임', '모소'], moto: ['movement', '움직임', '모토'], 'poco a poco': ['little by little', '조금씩', '포코 아 포코'] };
const tmxPartMean = (w) => { const e = TMX.find(x => x.w === w); return e ? tmxMean(e) : TMX_PART[w] ? t(TMX_PART[w][0], TMX_PART[w][1]) : ''; };
function TmxCard({ e, extra }) {
  if (!e) return null;
  const k = tmxPron(e), snd = tmxSound(e);
  return <div data-tmx-card={e.w} style={{border:'1.5px solid rgba(38,41,107,0.18)',borderRadius:12,background:'#fff',padding:'10px 12px',margin:'10px auto 0',maxWidth:360,textAlign:'center'}}>
    <div style={{fontSize:11.5,fontWeight:900,letterSpacing:'0.08em',textTransform:'uppercase',color:BK.muted}}>{e.fam ? tmxFam(e.fam) : t('A little word with a term', '꾸며 주는 말 + 용어')}</div>
    <div style={{margin:'4px 0 0'}}>{tmxWord(e.w, 30)}</div>
    {LANG === 'ko' && e.rd && <div style={{fontSize:14,fontWeight:800,color:BK.muted,marginTop:2}}>{tmxNbKo(e.rd)}</div>}
    <div style={{fontSize:16.5,fontWeight:800,color:BK.ink,margin:'6px 0 8px',textWrap:'balance',wordBreak:'keep-all'}}>{tmxKoT(tmxMean(e))}</div>
    <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>
      {snd && chxBtn('h', t('▶ Hear it', '▶ 들어 보기'), () => tmxPlay(e))}
      {k && chxBtn('s', LANG === 'ko' ? '이탈리아어 발음 듣기' : 'Say it: ' + PRON[k], () => tmxSay(e))}
      {extra}
    </div>
  </div>;
}
const tmxFamHead = (f, note) => <div style={{fontSize:11.5,fontWeight:900,letterSpacing:'0.08em',textTransform:'uppercase',color:BK.muted,margin:'0 0 4px'}}>{tmxFam(f)}{note && <span style={{textTransform:'none',letterSpacing:0,fontWeight:700}}> · {note}</span>}</div>;

// page 1 and the end: the whole ladder, family by family, in its order (an arrow under the speeds, a wedge over the
// dynamics, beats in the changes); tap a word: hear it, and its card opens under its family. end: tick the words you know
const TMX_KNOWN = 'pb_terms_known_v1';
const tmxKnownLoad = () => { try { const v = JSON.parse(localStorage.getItem(TMX_KNOWN)); return v && typeof v === 'object' ? v : {}; } catch (err) { return {}; } };
const tmxWedge = () => <svg viewBox="0 0 300 18" style={{width:'100%',display:'block',margin:'0 0 5px'}} aria-hidden="true"><polygon points="6,9 294,2 294,16" fill="rgba(38,41,107,0.10)" stroke={PEN_N} strokeWidth="1.2" strokeLinejoin="round"/></svg>;
const tmxArrow = () => <svg viewBox="0 0 300 10" style={{width:'100%',display:'block',margin:'5px 0 0'}} aria-hidden="true"><line x1="4" x2="290" y1="5" y2="5" stroke={BK.muted} strokeWidth="1.4"/><polygon points="298,5 290,1 290,9" fill={BK.muted}/></svg>;
function TmxMapPad({ end }) {
  const [sel, setSel] = useState(null), [known, setKnown] = useState(tmxKnownLoad);
  useEffect(() => () => chxStop(), []);
  const e = sel ? tmxOf(sel) : null;
  const tap = (x) => { setSel(x.w); tmxPlay(x); };
  const mark = (w) => { const nk = { ...known }; if (nk[w]) delete nk[w]; else nk[w] = 1; setKnown(nk); try { localStorage.setItem(TMX_KNOWN, JSON.stringify(nk)); } catch (err) {} };
  const n = TMX.filter(x => known[x.w]).length;
  const notes = { speed: t('slow → fast', '느리게 → 빠르게'), vol: t('soft → loud', '여리게 → 세게') };
  const chg = (x) => { const on = sel === x.w; return <button key={x.w} type="button" data-tmx={x.w} aria-pressed={on} onClick={() => tap(x)} style={{border:'1.5px solid ' + (on ? PEN_C : 'rgba(38,41,107,0.28)'),background:'#fff',borderRadius:14,padding:'4px 10px 2px',minHeight:44,minWidth:64,display:'inline-flex',flexDirection:'column',alignItems:'center',gap:1,cursor:'pointer'}}>
    <span style={{display:'inline-flex',alignItems:'center',gap:4}}>{end && known[x.w] && <span style={{color:PEN_G,fontWeight:900,fontSize:13}}>✓</span>}{tmxWord(x.w, 15, on ? PEN_C : PEN_N)}</span><span aria-hidden="true" style={{width:58,display:'block'}}><TmxBeatsSvg gaps={TMX_GAPS[x.w]} w0={174} w={x.w} sel={sel} word={false}/></span></button>; };
  const card = e && <TmxCard e={e} extra={end ? chxBtn('k', known[e.w] ? t('✓ I know it', '✓ 알아요') : t('I know it', '알아요'), () => mark(e.w), known[e.w]) : null}/>;
  return (
    <div className="try-box" style={actBox} data-tmx={end ? 'pad-mine' : 'pad-map'}>
      {!end && <div style={actTitle}>{t('The expression ladder', '표현의 사다리')}</div>}
      <div style={{...actNote,textWrap:'pretty'}}>{tmxKoT(end ? t('Tap a word, then tick it when you can say what it means and play it.', '용어를 누르고, 뜻을 말하고 칠 수 있으면 ✓ 표시해요.')
        : t('Tap any word: hear it and read what it means.', '아무 용어나 눌러요. 소리를 듣고 뜻을 읽어요.'))}</div>
      <div style={{display:'flex',flexDirection:'column',gap:8}}>
        {['speed', 'change', 'vol', 'touch', 'little'].map(f => <div key={f} data-tmx-fam={f}>{tmxFamHead(f, notes[f])}
          {f === 'vol' && tmxWedge()}
          {f === 'vol' ? <>
            <div style={{display:'grid',gridTemplateColumns:'repeat(6,minmax(0,1fr))',gap:3}}>{TMX_VOL6.map(w => tmxChip(w, sel === w, tap, w, end && known[w], 16, true))}</div>
            <div style={{display:'flex',flexWrap:'wrap',gap:4,marginTop:4}}>{['cresc.', 'decresc.', 'sf'].map(w => tmxChip(w, sel === w, tap, w, end && known[w]))}</div></>
            : <div style={{display:'flex',flexWrap:'wrap',gap:4}}>{TMX.filter(x => x.fam === f).map(x => f === 'change' ? chg(x) : tmxChip(x.w, sel === x.w, tap, x.w, end && known[x.w]))}</div>}
          {f === 'speed' && tmxArrow()}
          {e && e.fam === f && card}</div>)}
      </div>
      {!e && <div style={{textAlign:'center',fontSize:14.5,fontWeight:800,color:BK.muted,margin:'10px 0 0'}}>{t('Tap a word to start.', '용어를 하나 눌러 시작해요.')}</div>}
      {end && <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'10px 0 0'}} data-tmx="known-count">{t('I know ' + n + ' of ' + TMX.length + ' words.', TMX.length + '개 중 ' + n + '개를 알아요.')}</div>}
    </div>
  );
}
// page 2: the speed ladder, fast at the top; tap a rung: its clicks
function TmxSpeedPad() {
  const [sel, setSel] = useState('Moderato');
  useEffect(() => () => chxStop(), []);
  const e = tmxOf(sel);
  return (
    <div className="try-box" style={actBox} data-tmx="pad-speed">
      <div style={actTitle}>{t('The speed ladder', '빠르기 사다리')}</div>
      <div style={actNote}>{tmxKoT(t('Fast at the top, slow at the bottom. Tap a word: hear its speed.', '위로 갈수록 빠르고, 아래로 갈수록 느려요. 빠르기말을 누르면 그 빠르기가 들려요.'))}</div>
      <div style={{display:'flex',flexDirection:'column',gap:4,maxWidth:320,margin:'0 auto'}}>{TMX_SPEED.slice().reverse().map(x => { const on = sel === x.w;
        return <button key={x.w} type="button" data-tmx={x.w} aria-pressed={on} onClick={() => { setSel(x.w); tmxPlay(x); }} style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) 66px',alignItems:'center',gap:8,minHeight:44,padding:'2px 12px',border:'1.5px solid ' + (on ? PEN_C : 'rgba(38,41,107,0.2)'),borderRadius:10,background:'#fff',cursor:'pointer',textAlign:'left'}}>
          {tmxWord(x.w, 19, on ? PEN_C : PEN_N)}<svg viewBox="0 0 66 22" width="66" height="22" aria-hidden="true"><StmMark x={2} y={18} n={x.bpm} size={13} c={on ? PEN_C : BK.muted}/></svg></button>; })}</div>
      {chxMsg(t(e.w + ': ' + e.en + '.', e.rd + ': ' + e.ko + '.'))}
    </div>
  );
}
// page 3: changing speed: the beats as dots; tap a row: hear it
const TMX_CHG = ['accel.', 'rall.', 'rit.', 'riten.', 'a tempo'];
function TmxChangePad() {
  const [sel, setSel] = useState('accel.');
  useEffect(() => () => chxStop(), []);
  const e = tmxOf(sel), same = sel === 'rall.' || sel === 'rit.';
  return (
    <div className="try-box" style={actBox} data-tmx="pad-change">
      <div style={actTitle}>{t('Changing speed', '빠르기 변화')}</div>
      <div style={actNote}>{tmxKoT(t('The dots are beats: closer is faster. Tap a row to hear it.', '점은 박이에요. 가까울수록 빨라요. 줄을 누르면 들려요.'))}</div>
      <div style={{display:'flex',flexDirection:'column',gap:4,maxWidth:340,margin:'0 auto'}}>{TMX_CHG.map(w => { const on = sel === w, x = tmxOf(w);
        return <button key={w} type="button" data-tmx={w} aria-pressed={on} onClick={() => { setSel(w); tmxPlay(x); }} style={{display:'grid',gridTemplateColumns:'84px minmax(0,1fr)',alignItems:'center',gap:8,minHeight:48,padding:'2px 10px',border:'1.5px solid ' + (on ? PEN_C : 'rgba(38,41,107,0.2)'),borderRadius:10,background:'#fff',cursor:'pointer',textAlign:'left'}}>
          {tmxWord(w, 18, on ? PEN_C : PEN_N)}<TmxBeatsSvg gaps={TMX_GAPS[w]} x0={12} w0={174} w={w} sel={sel} word={false} label={w}/></button>; })}</div>
      {chxMsg(t(e.w + ': ' + e.en + '.' + (same ? ' rall. and rit.: two names, one meaning.' : ''), e.rd + ': ' + e.ko + '.' + (same ? ' 랄렌탄도와 리타르단도는 이름은 둘, 뜻은 하나.' : '')))}
    </div>
  );
}
// page 4: loud and soft: the six rungs under a wedge, the hairpins and an accent
function TmxVolPad() {
  const [sel, setSel] = useState('mf');
  useEffect(() => () => chxStop(), []);
  const e = tmxOf(sel), tap = (w) => { setSel(w); tmxPlay(tmxOf(w)); };
  const pin = (w, c) => <svg viewBox="0 0 60 16" width="52" height="14" aria-hidden="true">{w === 'cresc.' ? <path d="M58 2 L2 8 L58 14" fill="none" stroke={c} strokeWidth="1.8" strokeLinejoin="round"/> : <path d="M2 2 L58 8 L2 14" fill="none" stroke={c} strokeWidth="1.8" strokeLinejoin="round"/>}</svg>;
  const btn = (w, h = 50) => { const on = sel === w, c = on ? PEN_C : PEN_N; return <button key={w} type="button" data-tmx={w} aria-pressed={on} onClick={() => tap(w)} style={{minHeight:h,border:'1.5px solid ' + (on ? PEN_C : 'rgba(38,41,107,0.2)'),borderRadius:10,background:'#fff',cursor:'pointer',display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',gap:2,padding:'2px 2px'}}>{/^(de)?cresc\.$/.test(w) && pin(w, c)}{tmxWord(w, w.length < 3 ? 20 : 15, c)}</button>; };
  return (
    <div className="try-box" style={actBox} data-tmx="pad-vol">
      <div style={actTitle}>{t('Loud and soft', '셈여림')}</div>
      <div style={actNote}>{tmxKoT(t('One rung louder each time. Tap a sign to hear it.', '한 칸씩 더 세게. 기호를 누르면 들려요.'))}</div>
      <div style={{maxWidth:340,margin:'0 auto'}}>
        <svg viewBox="0 0 300 26" style={{width:'100%',display:'block'}} aria-hidden="true"><polygon points="8,13 292,3 292,23" fill="rgba(38,41,107,0.10)" stroke={PEN_N} strokeWidth="1.4" strokeLinejoin="round"/></svg>
        <div style={{display:'grid',gridTemplateColumns:'repeat(6,minmax(0,1fr))',gap:3,marginTop:4}}>{TMX_VOL6.map(w => btn(w))}</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,marginTop:8}}>{['cresc.', 'decresc.', 'sf'].map(w => btn(w, 54))}</div>
      </div>
      {chxMsg(t(e.w + ': ' + e.en + '.', e.rd + ': ' + e.ko + '.'))}
    </div>
  );
}
// page 5: one tune, three touches; then the character words
function TmxTouchPad() {
  const [sel, setSel] = useState('legato'), [touch, setTouch] = useState('legato');
  useEffect(() => () => chxStop(), []);
  const e = tmxOf(sel), tap = (x) => { setSel(x.w); if (TMX_T3B[x.w]) setTouch(x.w); tmxPlay(x); };
  return (
    <div className="try-box" style={actBox} data-tmx="pad-touch">
      <div style={actTitle}>{t('Touch and character', '터치와 느낌')}</div>
      <div style={actNote}>{tmxKoT(t('Dots: short. A slur: smooth. Both: in between. Tap a word to hear it.', '점은 짧게, 이음줄은 부드럽게, 둘 다 있으면 그 사이. 용어를 누르면 들려요.'))}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>{Object.keys(TMX_T3B).map(w => tmxChip(w, sel === w, tap))}</div>
      <div style={{maxWidth:300,margin:'4px auto 0'}}><SdyStaff full items={tmxBar(TMX_T3B[touch][1])} o={{ D: 40 }} k={TMX_T3B[touch][0]} label={t('C D E F, ' + touch + '.', 'C D E F, ' + tmxOf(touch).rd + '.')}/></div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginTop:4}}>{['sostenuto', 'cantabile', 'leggiero', 'maestoso', 'espressivo'].map(w => tmxChip(w, sel === w, tap))}</div>
      {chxMsg(t(e.w + ': ' + e.en + '.', e.rd + ': ' + e.ko + '.'))}
    </div>
  );
}
// page 6: a little word and a big one: pick a term; its two halves and what they make
function TmxBuildPad() {
  const [sel, setSel] = useState('poco rit.');
  useEffect(() => () => chxStop(), []);
  const c = tmxOf(sel), b = tmxOf(c.b), tap = (x) => { setSel(x.w); tmxPlay(x); };
  const half = (w, on) => <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:2,minWidth:0}}>
    <span style={{border:'1.5px solid ' + (on ? PEN_C : 'rgba(38,41,107,0.3)'),borderRadius:8,padding:'4px 10px',background:'#fff'}}>{tmxWord(w, 19, on ? PEN_C : PEN_N)}</span>
    <span style={{fontSize:12.5,fontWeight:800,color:BK.muted,textAlign:'center',textWrap:'balance',wordBreak:'keep-all'}}>{tmxKoT(tmxPartMean(w))}</span></div>;
  return (
    <div className="try-box" style={actBox} data-tmx="pad-build">
      <div style={actTitle}>{t('Little words', '꾸며 주는 말')}</div>
      <div style={actNote}>{tmxKoT(t('A little word changes the term beside it. Pick one.', '꾸며 주는 말이 옆의 용어를 바꿔요. 하나를 골라요.'))}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>{TMX_COMBO.map(x => tmxChip(x.w, sel === x.w, tap))}</div>
      <div style={{display:'grid',gridTemplateColumns:'minmax(0,1fr) 18px minmax(0,1fr)',alignItems:'start',gap:6,maxWidth:300,margin:'12px auto 0'}}>
        {half(c.a, true)}<span style={{fontWeight:900,color:BK.muted,textAlign:'center',paddingTop:8}}>+</span>{half(c.b)}</div>
      {chxMsg('= ' + t(c.w + ': ' + c.en + '.', (c.rd ? c.rd + ': ' : c.w + ': ') + c.ko + '.'))}
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>
        {b && tmxSound(b) && chxBtn('b', '▶ ' + b.w, () => tmxPlay(b))}
        {tmxSound(c) && chxBtn('c', '▶ ' + c.w, () => tmxPlay(c), true)}
      </div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step; the whole ladder again at the end ──
function TmxLearn({ onStart }) {
  const pages = tmxLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="terms" title={bkChapterName('terms')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="terms"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
      <Step key="map" extra title={t('My terms', '나의 용어')} storeAs="k7"><TmxMapPad end/></Step>
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order: speed (1, 2), changing speed (3), loud and soft (4), listening (5),
// touch and character (6), little words (7), build a term (8); 9 extra: meaning → term, every family ──
const TMX_LEVELS = [
  { n: 1, label: 'Speed words: what they mean', kind: 'tm', fam: 'speed', time: 9 },
  { n: 2, label: 'Which is faster?', kind: 'faster', time: 7 },
  { n: 3, label: 'Changing speed', kind: 'tm', fam: 'change', time: 9 },
  { n: 4, label: 'Loud and soft: the signs', kind: 'tm', fam: 'vol', time: 9 },
  { n: 5, label: 'Listen: which one?', kind: 'ear', time: 12, noPrint: true },
  { n: 6, label: 'Touch and character', kind: 'tm', fam: 'touch', time: 9 },
  { n: 7, label: 'Little words', kind: 'tm', fam: 'little', time: 9 },
  { n: 8, label: 'Build the term', kind: 'combo', time: 11 },
  { n: 9, label: 'Extra: meaning → term', kind: 'mt', time: 10 },
];
Object.assign(LEVEL_KO, { 'Speed words: what they mean': '빠르기말의 뜻', 'Which is faster?': '어느 쪽이 더 빠를까요?', 'Changing speed': '빠르기 변화', 'Loud and soft: the signs': '셈여림 기호',
  'Listen: which one?': '듣기: 어느 쪽?', 'Touch and character': '터치와 느낌', 'Little words': '꾸며 주는 말', 'Build the term': '용어 만들기', 'Extra: meaning → term': '더 해 보기: 뜻 → 용어' });
// words a child cannot tell apart by meaning alone never stand as each other's wrong answer
const TMX_GRP = { Largo: 'slow', Lento: 'slow', Adagio: 'slow', Allegro: 'lively', Vivace: 'lively', Presto: 'vfast', Prestissimo: 'vfast', 'rall.': 'rit', 'rit.': 'rit' };
const tmxClash = (a, b) => a.w === b.w || (TMX_GRP[a.w] && TMX_GRP[a.w] === TMX_GRP[b.w]) || a.en === b.en || a.ko === b.ko;
const TMX_EAR = [['accel.', 'rit.'], ['legato', 'staccato'], ['cresc.', 'decresc.'], ['Adagio', 'Presto'], ['sf', 'cresc.'], ['a tempo', 'riten.']];
// level 8: each term with three that a child might build instead
const TMX_BUILD_WRONG = { 'poco rit.': ['molto rit.', 'poco accel.', 'senza rit.'], 'molto cresc.': ['poco cresc.', 'molto decresc.', 'sempre staccato'], 'sempre staccato': ['sempre legato', 'senza staccato', 'poco rit.'],
  'più mosso': ['meno mosso', 'senza rit.', 'molto cresc.'], 'meno mosso': ['più mosso', 'con moto', 'sempre staccato'], 'con moto': ['meno mosso', 'sempre legato', 'molto cresc.'],
  'senza rit.': ['poco rit.', 'molto rit.', 'meno mosso'], 'poco a poco cresc.': ['molto cresc.', 'poco a poco decresc.', 'sempre staccato'] };
const _tmxBag = {};
const TMX_FPAIRS = []; TMX_SPEED.forEach((x, i) => TMX_SPEED.forEach((y, j) => { if (j - i >= 2 && !tmxClash(x, y)) TMX_FPAIRS.push([i, j]); }));
const tmxFromBag = (kind, list) => { let b = _tmxBag[kind]; if (!b || !b.length) b = _tmxBag[kind] = shuffle(list.slice()); return b.pop(); };
function genTmxQuestion(lv, prev) {
  const uid = Math.random(), same = (key) => prev && prev.key === key;
  for (let g = 0; g < 40; g++) {
    if (lv.kind === 'tm' || lv.kind === 'mt') {
      const pool = lv.fam ? TMX.filter(x => x.fam === lv.fam) : TMX, e = tmxFromBag(lv.kind + (lv.fam || ''), pool), key = lv.kind + e.w;
      if (same(key)) continue;
      const wrong = [];
      for (const x of shuffle(TMX.filter(x => x.fam === e.fam && !tmxClash(x, e)))) if (wrong.length < 3 && !wrong.some(y => tmxClash(x, y))) wrong.push(x);
      if (wrong.length < 3) continue;
      if (lv.kind === 'tm') return { kind: 'tm', key, w: e.w, answer: e.en, choices: shuffle([e.en, ...wrong.map(x => x.en)]), uid };
      return { kind: 'mt', key, w: e.w, answer: e.w, choices: shuffle([e.w, ...wrong.map(x => x.w)]), uid };
    }
    if (lv.kind === 'faster') {
      const [i, j] = tmxFromBag('faster', TMX_FPAIRS).slice().sort(() => Math.random() - 0.5);
      const a = TMX_SPEED[i], b = TMX_SPEED[j], key = 'f' + [a.w, b.w].sort().join();
      if (same(key)) continue;
      return { kind: 'faster', key, answer: (i > j ? a : b).w, choices: shuffle([a.w, b.w]), uid };
    }
    if (lv.kind === 'ear') {
      const pair = pick(TMX_EAR), w = pick(pair), key = 'e' + w;
      if (same(key)) continue;
      return { kind: 'ear', key, w, answer: w, choices: pair.slice(), uid };
    }
    if (lv.kind === 'combo') {
      const c = tmxFromBag('combo', TMX_COMBO), key = 'c' + c.w;
      if (same(key)) continue;
      return { kind: 'combo', key, w: c.w, answer: c.w, choices: shuffle([c.w, ...TMX_BUILD_WRONG[c.w]]), uid };
    }
  }
  return { kind: 'tm', key: 'x', w: 'Andante', answer: 'at a walking pace', choices: ['at a walking pace', 'very fast', 'slowly', 'moderately fast'], uid };
}
const tmxCheck = (q, ans) => ans != null && String(ans) === String(q.answer);
// a meaning in the student's language (the answer is kept in English, the key the check compares)
const tmxEnToKo = (en) => { const e = TMX.find(x => x.en === en) || TMX_COMBO.find(x => x.en === en); return e ? t(e.en, e.ko) : en; };
function tmxAnswerLabel(q) {
  if (q.kind === 'faster') { const [a, b] = q.answer === q.choices[0] ? q.choices : [q.choices[1], q.choices[0]]; return t(a + ' (faster than ' + b + ')', tmxOf(a).rd + '(' + a + ')가 ' + tmxOf(b).rd + '(' + b + ')보다 빨라요'); }
  const e = tmxOf(q.w); return t(e.w + ': ' + e.en, e.w + ' = ' + e.ko);
}
function TmxQuestion({ q, given, locked, onAnswer, pixel }) {
  const paper = locked && !given;
  const board = useBoard(q, given), isDone = !!given, btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const ink = pixel ? '#faf6ec' : 'var(--text)', e = q.w ? tmxOf(q.w) : null;
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  useEffect(() => () => chxStop(), [q.uid]);
  useEffect(() => { if (q.kind === 'ear' && !locked) { const tm = setTimeout(() => tmxPlay(tmxOf(q.w)), 350); return () => { clearTimeout(tm); chxStop(); }; } }, [q.uid]);
  const prompt = { tm: t('What does it mean?', '무슨 뜻일까요?'), mt: t('Which term means this?', '이 뜻의 용어는 무엇일까요?'), combo: t('Which term means this?', '이 뜻의 용어는 무엇일까요?'),
    faster: t('Which is faster?', '어느 쪽이 더 빠를까요?'), ear: t('Listen: which one?', '듣고 골라요: 어느 쪽일까요?') }[q.kind];
  const wordCol = pixel ? '#faf6ec' : PEN_N;
  let head = null;
  if (q.kind === 'tm') head = <div style={{textAlign:'center',margin:'0 0 4px'}}>{tmxWord(q.w, pixel ? 20 : 34, wordCol)}{LANG === 'ko' && e.rd && <div style={{fontSize:pixel ? 10 : 14,fontWeight:800,color:pixel ? '#faf6ec' : BK.muted,marginTop:2}}>{e.rd}</div>}</div>;
  if (q.kind === 'mt' || q.kind === 'combo') head = <div style={{textAlign:'center',fontSize:pixel ? 13 : 21,fontWeight:900,color:ink,margin:'0 0 6px',textWrap:'balance',wordBreak:'keep-all'}}>“{tmxKoT(tmxMean(e))}”</div>;
  if (q.kind === 'ear') head = <div style={{textAlign:'center',margin:'4px 0 6px'}}><button className="ghost-btn" style={{minHeight:44}} onClick={() => tmxPlay(tmxOf(q.w))}>{t('▶ Listen again', '▶ 다시 듣기')}</button></div>;
  const after = isDone && !pixel && e && q.kind !== 'ear' && <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'0 0 8px'}}>
    {tmxSound(e) && chxBtn('h', t('▶ Hear it', '▶ 들어 보기'), () => tmxPlay(e))}{tmxPron(e) && chxBtn('s', LANG === 'ko' ? '이탈리아어 발음 듣기' : 'Say it: ' + PRON[tmxPron(e)], () => tmxSay(e))}</div>;
  const words = q.kind !== 'tm', long = words && (q.kind === 'combo' || q.choices.some(c => c.length > 10)), cols = paper ? 2 : words && !long && !pixel ? 2 : 1;
  const lab = (c) => words ? tmxWord(c, pixel ? 11 : 21, pixel ? '#26296b' : undefined) : <span style={{fontSize:pixel ? 11 : 16.5,fontWeight:800,wordBreak:'keep-all'}}>{tmxKoT(tmxEnToKo(c))}</span>;
  return <div>{!paper && <BoardTrack b={board} pixel={pixel}/>}
    <p style={{fontSize:pixel ? 11.5 : 17,fontWeight:900,textAlign:'center',margin:'0 0 8px',color:ink,textWrap:'balance',wordBreak:'keep-all'}}>{prompt}</p>
    {head}
    {after}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:6}}>{q.choices.map(c => <button key={c} disabled={locked} data-tmx-choice={c} onClick={() => { if (q.kind === 'ear') chxStop(); onAnswer(c); }} className={btnCls + st(c)} style={{padding:'10px 6px',minHeight:48}}>{lab(c)}</button>)}</div>
  </div>;
}
