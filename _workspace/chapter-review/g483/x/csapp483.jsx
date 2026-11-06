// ─── Phase 483: chapter 27's sounds, pads (pages 1 to 6), the screen lesson and the drill ───
// the sounds: events [beat, MIDI, beats, velocity] played through chapter 26's one-at-a-time owner (cpxStop)
function csxPlay(ev, bpm, onEnd, owner, inst = 'piano') {
  cpxStop(); if (!ev.length) return 0;
  const s = playEvents(inst, ev, bpm); if (!s) return 0;
  _cpxEnd = onEnd || null; _cpxOwner = owner;
  _cpxTm = setTimeout(() => { _cpxTm = null; _cpxOwner = null; const e = _cpxEnd; _cpxEnd = null; if (e) e(); }, s * 1000 + 250); return s;
}
const csxTexEv = (tex, tune = 'a') => {
  const ev = CSX_TUNES[tune].map(([b, d, l]) => [b, csxD(d), l, 0.62]);
  if (tex === 'homophony') CSX_CHORDS[tune].forEach(([b, ds, l]) => ds.forEach(d => ev.push([b, csxD(d), l, 0.3])));
  if (tex === 'polyphony') CSX_VOICE2[tune].forEach(([b, d, l]) => ev.push([b, csxD(d), l, 0.5]));
  return ev;
};
// a tune made up for this page on the five notes (C D E G A), or the same tune on the five black keys
const CSX_FOLK = [0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 2, 1, 0];
const CSX_FOLK_L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2];
const csxFolkEv = (black) => { let b = 0; const set = black ? [66, 68, 70, 73, 75] : [60, 62, 64, 67, 69]; return CSX_FOLK.map((k, i) => { const e = [b, set[k], CSX_FOLK_L[i], 0.6]; b += CSX_FOLK_L[i]; return e; }); };
// swing: a pattern of quavers, played even or long-short (two parts of three, then one)
const CSX_SWING_N = [64, 67, 69, 67, 64, 67, 69, 67];
const csxSwingEv = (swing) => { const long = swing ? 2 / 3 : 1 / 2, ev = [];
  for (let r = 0; r < 2; r++) CSX_SWING_N.forEach((m, i) => { const k = Math.floor(i / 2), off = i % 2; ev.push([(r * 4 + k) + (off ? long : 0), m, (off ? 1 - long : long) * 0.95, off ? 0.4 : 0.6]); });
  ev.push([8, 60, 1.5, 0.6]); return ev; };
// the 12-bar blues in C: a left-hand boogie (root with the fifth, sixth, flat seventh, sixth), swung, and the chord on beat 1
const CSX_ROOT = { I: 48, IV: 53, V: 55 };
const csxChordNm = (c) => t(c + ' (' + { I: 'C', IV: 'F', V: 'G' }[c] + ')', c + '(' + { I: 'C', IV: 'F', V: 'G' }[c] + ')');   // I (C), IV (F), V (G)
const csxBluesEv = (bars = 12) => { const ev = [];
  BLUES_12.slice(0, bars).forEach((c, i) => { const r = CSX_ROOT[c];
    [7, 9, 10, 9].forEach((up, k) => { const b = i * 4 + k; [0, 2 / 3].forEach((o, j) => { ev.push([b + o, r, (j ? 1 / 3 : 2 / 3) * 0.95, j ? 0.35 : 0.5]); ev.push([b + o, r + up, (j ? 1 / 3 : 2 / 3) * 0.95, j ? 0.3 : 0.45]); }); });
    [12, 16, 19].forEach(u => ev.push([i * 4, r + u, 1.6, 0.3])); });
  ev.push([bars * 4, 48, 2, 0.5]); ev.push([bars * 4, 60, 2, 0.4]); ev.push([bars * 4, 64, 2, 0.35]); ev.push([bars * 4, 67, 2, 0.35]); return ev; };
// pop: C G Am F, four beats each, twice: the bass on 1 and 3, the chord on every beat
const csxPopEv = (loops = 2) => { const ev = [];
  for (let r = 0; r < loops; r++) CSX_POP.forEach(([, [bass, ...ch]], i) => { const b0 = (r * 4 + i) * 4;
    [0, 2].forEach(k => ev.push([b0 + k, bass, 1.8, 0.5])); [0, 1, 2, 3].forEach(k => ch.forEach(m => ev.push([b0 + k, m, 0.9, k % 2 ? 0.25 : 0.35]))); });
  ev.push([loops * 16, 48, 2, 0.5]); [60, 64, 67].forEach(m => ev.push([loops * 16, m, 2, 0.35])); return ev; };
// the sound of each period (r1): Bach's Invention No. 1 (two tunes, the second an octave lower), Mozart's Sonata K. 545
// (a clear tune over an Alberti bass), Liszt's Liebestraum No. 3 (a long singing tune over a held bass), bars in the style of
// Debussy (whole-tone chords: new scales and chords) and of Hisaishi (a film tune). The first two are their openings, as in
// the score (Mutopia: BWV 772 with its two mordents; K. 545, the Alberti bass from middle C), checked in the r2 review.
const CSX_ERA_CLIP = {
  baroque: { name: ['Bach’s Invention No. 1 in C', '바흐의 인벤션 1번 C장조'], h: { kind: 'tune', inst: 'harpsichord', bpm: 72,
    v: ['r:0.25 C4:0.25 D4:0.25 E4:0.25 F4:0.25 D4:0.25 E4:0.25 C4:0.25 G4:0.5 C5:0.5 B4:0.125 C5:0.125 B4:0.25 C5:0.5 | D5:0.25 G4:0.25 A4:0.25 B4:0.25 C5:0.25 A4:0.25 B4:0.25 G4:0.25 D5:0.5 G5:0.5 F5:0.125 G5:0.125 F5:0.25 G5:0.5 | E5:1.5',
        'r:2 r:0.25 C3:0.25 D3:0.25 E3:0.25 F3:0.25 D3:0.25 E3:0.25 C3:0.25 | G3:0.5 G2:0.5 r:1 r:0.25 G3:0.25 A3:0.25 B3:0.25 C4:0.25 A3:0.25 B3:0.25 G3:0.25 | C4:1.5'] } },
  classical: { name: ['Mozart’s Sonata in C, K. 545', '모차르트의 소나타 C장조 K. 545'], h: { kind: 'tune', inst: 'piano', bpm: 112,
    v: ['C5:2 E5:1 G5:1 | B4:1.5 C5:0.25 D5:0.25 C5:1 r:1', 'C4:0.5@0.35 G4:0.5@0.3 E4:0.5@0.3 G4:0.5@0.3 C4:0.5@0.35 G4:0.5@0.3 E4:0.5@0.3 G4:0.5@0.3 | D4:0.5@0.35 G4:0.5@0.3 F4:0.5@0.3 G4:0.5@0.3 C4:0.5@0.35 G4:0.5@0.3 E4:0.5@0.3 G4:0.5@0.3'] } },
  romantic: { name: ['Liszt’s Liebestraum No. 3', '리스트의 “사랑의 꿈” 3번'], id: 'liszt' },
  modern: { name: ['a few bars in the style of Debussy', '드뷔시풍의 짧은 음악'], style: 'debussy' },
  contemporary: { name: ['a few bars in the style of Hisaishi', '히사이시풍의 짧은 음악'], id: 'hisaishi' },
};
const csxEraClip = (era) => { const c = CSX_ERA_CLIP[era]; return c.h || (c.style ? (CMP_HEAR[c.style] || []).find(h => h.kind === 'style') : cpxSound(c.id)); };
function csxEraHear(era, onEnd, owner) {
  cpxStop(); const h = csxEraClip(era); if (!h || !cmpHasSound(h)) return 0;
  const s = cmpPlay(h); if (!s) return 0;
  _cpxEnd = onEnd || null; _cpxOwner = owner;
  _cpxTm = setTimeout(() => { _cpxTm = null; _cpxOwner = null; const e = _cpxEnd; _cpxEnd = null; if (e) e(); }, s * 1000 + 250); return s;
}
const csxEraNow = (era) => t(CSX_ERA_CLIP[era].name[0], CSX_ERA_CLIP[era].name[1]);
// the styles row: what each one plays
const CSX_STYLE_SOUND = { 'folk songs: always, everywhere': (cb, me) => csxPlay(csxFolkEv(false), 104, cb, me), blues: (cb, me) => csxPlay(csxBluesEv(4), 112, cb, me),
  ragtime: (cb, me) => cpxHear('joplin', cb, me), jazz: (cb, me) => csxPlay(csxSwingEv(true), 120, cb, me), 'rock and pop': (cb, me) => csxPlay(csxPopEv(1), 100, cb, me) };
const CSX_STYLE_W = { 'folk songs: always, everywhere': ['Folk songs: passed on by ear, everywhere and always. Playing: a tune on five notes.', '민요: 언제나 어디서나 귀로 전해져요. 듣는 곡: 다섯 음으로 된 선율.'],
  blues: ['Blues, from the 1890s: three chords over twelve bars. Playing: its first four bars, swung.', '블루스, 1890년대부터: 열두 마디에 세 화음. 듣는 곡: 처음 네 마디, 스윙으로.'],
  ragtime: ['Ragtime, 1895 to 1920: a jumpy right hand over a steady left. Playing: Joplin’s “The Entertainer”.', '래그타임, 1895~1920: 꾸준한 왼손 위에 통통 튀는 오른손. 듣는 곡: 조플린의 “엔터테이너”.'],
  jazz: ['Jazz, from about 1900: swing and improvisation. Playing: quavers swung.', '재즈, 1900년쯤부터: 스윙과 즉흥 연주. 듣는 곡: 스윙으로 친 8분음표.'],
  'rock and pop': ['Rock and pop, from the 1950s: songs with a strong drum beat, a verse and a chorus. Playing: four chords, C G Am F.', '록과 팝, 1950년대부터: 드럼 비트가 강한 노래, 벌스와 후렴. 듣는 곡: 네 화음 C G Am F.'] };
const CSX_STYLE_IDS = Object.keys(CSX_STYLE_SOUND);
const csxStyleNm = (id) => { const s = (id === MTL_FOLK[2] ? [MTL_FOLK] : MTL_STYLES).find(x => x[2] === id); return t(s[2], s[3]); };

// page 1: the timeline: a period (its sound) or a style, tapped, plays
function CsxMapPad() {
  const me = React.useRef({}).current, [box, w] = useCpxW();
  const [sel, setSel] = useState(null), [playing, setPlaying] = useState(false);
  useEffect(() => () => cpxStop(me), []);
  const go = (kind, id) => { setSel({ kind, id }); const end = () => setPlaying(false);
    setPlaying((kind === 'style' ? CSX_STYLE_SOUND[id](end, me) : csxEraHear(id, end, me)) > 0); };
  let msg = w >= 480 ? t('The sound row: how each period sounds. The styles row: the genres beside the concert hall.', '소리 줄: 시대마다 다른 소리. 스타일 줄: 연주회장 밖의 장르.') : t('The periods above; the styles beside them, below.', '위에는 시대, 아래에는 그 곁의 스타일.');
  if (sel && sel.kind === 'sound') { const E = CSX_ERA[sel.id];
    msg = t(cmpEraTag(sel.id) + ': ' + E.listen.map(x => x[0]).join(' · ') + '.' + (playing ? ' Playing: ' + csxEraNow(sel.id) + '.' : ''),
      cmpEraTag(sel.id) + ': ' + E.listen.map(x => x[1]).join(' · ') + '.' + (playing ? ' 듣는 곡: ' + csxEraNow(sel.id) + '.' : '')); }
  if (sel && sel.kind === 'style') msg = t(CSX_STYLE_W[sel.id][0], CSX_STYLE_W[sel.id][1]);
  const chips = (kind, ids, nm) => <div role="group" aria-label={kind === 'sound' ? t('Periods', '시대') : t('Styles', '스타일')} style={{display:'flex',flexWrap:'wrap',justifyContent:'center',gap:6,margin:'0 0 6px'}}>{ids.map(id => cpxChip(sel && sel.kind === kind && sel.id === id, nm(id), () => go(kind, id), id))}</div>;
  return (
    <div className="try-box" style={actBox} data-csx="pad-map">
      <div style={actTitle}>{t('The timeline of music', '음악의 타임라인')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{csxKoT(t('Tap a period’s sound or a style. Hear it.', '시대의 소리나 스타일을 눌러요. 소리가 들려요.'))}</div>
      {chips('sound', MTL_ERAS, cmpEraTag)}
      {chips('style', CSX_STYLE_IDS, (id) => id === MTL_FOLK[2] ? t('folk', '민요') : csxStyleNm(id))}
      <div ref={box} style={{marginTop:4}}><MusTimeline W={w} focus={['sound', 'style']} cmpNames={false} rowLabels={w >= 480} fs={w >= 480 ? 10.5 : 11} rows={w >= 480 ? ['era', 'keys', 'sound', 'style'] : ['era', 'style']} sel={sel} hiEra={sel && sel.kind === 'sound' ? sel.id : null}
        onTap={(kind, id) => go(kind === 'era' ? 'sound' : kind, id)} tapKinds={['era', 'sound', 'style']} label={t('The timeline of music with the sound of each period and the styles. Each can be tapped.', '시대별 소리와 스타일을 담은 음악의 타임라인. 하나씩 누를 수 있어요.')}/></div>
      {cpxMsg(csxKoT(msg))}
      <div style={{display:'flex',justifyContent:'center'}}>{cpxStopBtn(playing, () => cpxStop())}</div>
    </div>
  );
}

// page 2: one tune three ways; then the ear: which texture?
function CsxTexturePad() {
  const me = React.useRef({}).current, [tex, setTex] = useState('monophony'), [playing, setPlaying] = useState(false), [quiz, setQuiz] = useState(null), [score, setScore] = useState({ right: 0, tries: 0 });
  useEffect(() => () => cpxStop(me), []);
  const play = (x, tune = 'a') => setPlaying(csxPlay(csxTexEv(x, tune), 120, () => setPlaying(false), me) > 0);
  const ask = () => { const x = pick(CSX_TEX), tune = pick(['a', 'b', 'c']); setQuiz({ x, tune, ans: null }); play(x, tune); };
  const answer = (a) => { if (!quiz || quiz.ans) return; setQuiz(q => ({ ...q, ans: a })); setTex(quiz.x); setScore(s => ({ right: s.right + (a === quiz.x ? 1 : 0), tries: s.tries + 1 })); };
  const hidden = quiz && !quiz.ans;
  return (
    <div className="try-box" style={actBox} data-csx="pad-texture">
      <div style={actTitle}>{t('Texture', '텍스처')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{csxKoT(t('Choose a texture and hear the same tune that way.', '텍스처를 고르면 같은 선율을 그 텍스처로 들려줘요.'))}</div>
      <div role="group" aria-label={t('Textures', '텍스처')} style={{display:'flex',flexWrap:'wrap',justifyContent:'center',gap:6,margin:'0 0 8px'}}>{CSX_TEX.map(x => cpxChip(!hidden && tex === x, csxTexW(x), () => { setQuiz(null); setTex(x); play(x); }, x))}</div>
      <div aria-hidden={hidden || undefined} style={{maxWidth:440,margin:'0 auto',visibility:hidden ? 'hidden' : 'visible'}}><CsxRoll tex={quiz && quiz.ans ? quiz.x : tex} tune={quiz ? quiz.tune : 'a'} label={t('The tune as ', '선율: ') + csxTexW(quiz && quiz.ans ? quiz.x : tex)}/></div>
      {cpxMsg(csxKoT(hidden ? t('Which texture did you hear?', '어떤 텍스처였나요?') : quiz && quiz.ans ? (quiz.ans === quiz.x ? t('Yes: ' + CSX_TEX_W[quiz.x][0] + '.', '맞아요: ' + CSX_TEX_W[quiz.x][1] + '.') : t('It was ' + CSX_TEX_W[quiz.x][0] + '. Look at the picture.', CSX_TEX_W[quiz.x][1] + '였어요. 그림을 봐요.')) : { monophony: t('Monophony: one line alone.', '모노포니: 선율 한 줄만.'), homophony: t('Homophony: the tune, with chords underneath.', '호모포니: 선율 아래에 화음.'), polyphony: t('Polyphony: a second tune joins on beat 3.', '폴리포니: 셋째 박에 두 번째 선율이 들어와요.') }[tex]), quiz && quiz.ans && quiz.ans !== quiz.x)}
      {hidden && <div role="group" aria-label={t('Your answer', '답')} style={{display:'flex',flexWrap:'wrap',justifyContent:'center',gap:6,margin:'0 0 6px'}}>{CSX_TEX.map(x => chxBtn(x, csxTexW(x), () => answer(x), false))}</div>}
      <div style={{display:'flex',justifyContent:'center',gap:8,alignItems:'center',flexWrap:'wrap'}}>{chxBtn('q', t('Ear test', '귀 테스트'), ask, false)}{cpxStopBtn(playing, () => cpxStop())}{score.tries > 0 && <span style={{fontSize:13,fontWeight:800,color:BK.muted}}>{t(score.right + ' of ' + score.tries, score.tries + '번 중 ' + score.right + '번')}</span>}</div>
    </div>
  );
}

// page 3: the periods: tap one to hear it and see what to listen for
function CsxEraPad() {
  const me = React.useRef({}).current, [sel, setSel] = useState(null), [playing, setPlaying] = useState(false);
  useEffect(() => () => cpxStop(me), []);
  const go = (id) => { setSel(id); setPlaying(csxEraHear(id, () => setPlaying(false), me) > 0); };
  return (
    <div className="try-box" style={actBox} data-csx="pad-era">
      <div style={actTitle}>{t('The sound of each period', '시대마다 다른 소리')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{csxKoT(t('Tap a period: hear a piece from it and listen for its sounds.', '시대를 눌러요: 그 시대의 곡을 듣고 그 소리를 찾아 들어요.'))}</div>
      <CsxEraChart sel={sel} onTap={go} scr/>
      {cpxMsg(csxKoT(!sel ? t('Tap a period.', '시대를 눌러요.') : t(playing ? 'Playing: ' + csxEraNow(sel) + '.' : cmpEraTag(sel) + '.', playing ? '듣는 곡: ' + csxEraNow(sel) + '.' : cmpEraTag(sel) + '.')))}
      <div style={{display:'flex',justifyContent:'center'}}>{cpxStopBtn(playing, () => cpxStop())}</div>
    </div>
  );
}

// page 4: the five notes: tap keys; hear a tune made up on them (white or black)
function CsxPentaPad() {
  const me = React.useRef({}).current, [black, setBlack] = useState(false), [lit, setLit] = useState(-1), [playing, setPlaying] = useState(false), [box, w] = useCpxW(420);
  useEffect(() => () => cpxStop(me), []);
  const set = black ? CSX_BLACK : CSX_PENTA;
  const key = (pc) => { csxPlay([[0, 60 + pc, 0.9, 0.6]], 100, () => setLit(-1), me); setLit(pc); };   // play first: its stop ends the last key's light
  const tune = () => setPlaying(csxPlay(csxFolkEv(black), 104, () => setPlaying(false), me) > 0);
  return (
    <div className="try-box" style={actBox} data-csx="pad-penta">
      <div style={actTitle}>{t('Five notes', '다섯 음')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{csxKoT(t('Tap the filled keys to make up a tune. Any order works.', '칠한 건반을 눌러 선율을 지어 봐요. 어떤 차례로 쳐도 어울려요.'))}</div>
      <div role="group" aria-label={t('Which five', '어느 다섯 음')} style={{display:'flex',justifyContent:'center',gap:6,margin:'0 0 8px'}}>{cpxChip(!black, csxNotes('C D E G A'), () => { setBlack(false); setLit(-1); }, 'w')}{cpxChip(black, t('black keys', '검은건반'), () => { setBlack(true); setLit(-1); }, 'b')}</div>
      {!black && <div style={{maxWidth:380,margin:'0 auto 10px'}}><CsxMinus47 label={t('C D E F G A B C numbered 1 to 8; F (4) and B (7) crossed out: C D E G A are left.', 'C D E F G A B C에 1부터 8까지 번호를 붙였어요. F(4)와 B(7)를 지워서 C D E G A가 남아요.')}/></div>}
      <div ref={box} style={{maxWidth:420,margin:'0 auto'}}><style>{'.csx-key:focus{outline:none}.csx-key:focus-visible>rect{stroke:#e4572e;stroke-width:3}'}</style><CsxKeys on={set} letters={!black} onKey={key} lit={lit} W={w} kh={Math.round(w * 0.3)} fs={13} label={t('One octave of keys, middle C to B, the five notes filled. Each key plays.', '가운데 도(C)부터 B까지 한 옥타브. 다섯 음을 칠했어요. 건반마다 소리가 나요.')}/></div>
      {w < 400 && <div role="group" aria-label={t('The five notes', '다섯 음')} style={{display:'flex',justifyContent:'center',gap:6,margin:'8px 0 0',flexWrap:'wrap'}}>{set.map(pc => <span key={'n' + pc} style={{display:'inline-flex',minWidth:44}}>{cpxChip(lit === pc, CSX_PC_W[pc], () => key(pc), 'c' + pc)}</span>)}</div>}
      {cpxMsg(csxKoT(lit >= 0 ? CSX_PC_W[lit] + (set.includes(lit) ? '' : t(': not one of the five', ': 다섯 음에 들지 않아요')) : t('A folk-style tune made up on these five notes:', '이 다섯 음으로 지은 민요풍 선율:')), lit >= 0 && !set.includes(lit))}
      <div style={{display:'flex',justifyContent:'center',gap:8}}>{chxBtn('t', t('▶ Hear it', '▶ 듣기'), tune, false)}{cpxStopBtn(playing, () => cpxStop())}</div>
    </div>
  );
}

// page 5: the 12-bar blues (play it, then find the chord of a bar), and straight or swing
function csxBluesGap(prev) { for (let g = 0; g < 20; g++) { const i = Math.floor(Math.random() * 12); if (i !== prev) return i; } return 9; }
function CsxBluesPad() {
  const me = React.useRef({}).current, tm = React.useRef([]), [hl, setHl] = useState(-1), [playing, setPlaying] = useState(null), [gap, setGap] = useState(null), [ans, setAns] = useState(null), [box, w] = useCpxW(420);
  const clear = () => { tm.current.forEach(clearTimeout); tm.current = []; setHl(-1); };
  useEffect(() => () => { clear(); cpxStop(me); }, []);
  const end = () => { clear(); setPlaying(null); };
  const blues = () => { clear(); const bpm = 112, s = csxPlay(csxBluesEv(12), bpm, end, me); if (!s) return; setPlaying('blues'); setHl(0);
    for (let i = 1; i < 12; i++) tm.current.push(setTimeout(() => setHl(i), (0.1 + i * 4 * 60 / bpm) * 1000)); };
  const swing = (sw) => { clear(); setPlaying(csxPlay(csxSwingEv(sw), 112, end, me) ? (sw ? 'swing' : 'straight') : null); };
  const ask = () => { setGap(g => csxBluesGap(g)); setAns(null); };
  return (
    <div className="try-box" style={actBox} data-csx="pad-blues">
      <div style={actTitle}>{t('Blues and swing', '블루스와 스윙')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{csxKoT(t('Hear the 12 bars swung, then find a missing chord.', '열두 마디를 스윙으로 듣고, 빠진 화음을 찾아요.'))}</div>
      <div ref={box} style={{maxWidth:420,margin:'0 auto'}}><CsxBlues W={w} ch={Math.max(46, Math.round(w / 7.5))} hl={hl} gaps={gap != null && !ans ? [gap] : []} fill={gap != null && ans ? gap : -1} label={t('The 12-bar blues in C' + (gap != null && !ans ? ', bar ' + (gap + 1) + ' empty.' : '.'), 'C장조 12마디 블루스' + (gap != null && !ans ? ', ' + (gap + 1) + '마디가 비었어요.' : '.'))}/></div>
      {gap != null && !ans && <div role="group" aria-label={t('Bar ' + (gap + 1), (gap + 1) + '마디')} style={{display:'flex',justifyContent:'center',gap:6,margin:'8px 0 0'}}>{['I', 'IV', 'V'].map(c => chxBtn(c, csxChordNm(c), () => setAns(c), false))}</div>}
      {cpxMsg(csxKoT(gap == null ? (playing === 'blues' ? t('Bar ' + (Math.max(0, hl) + 1) + ': ' + BLUES_12[Math.max(0, hl)] + '.', (Math.max(0, hl) + 1) + '마디: ' + BLUES_12[Math.max(0, hl)] + '.') : t('Three chords: I (C), IV (F), V (G).', '세 화음: I(C), IV(F), V(G).')) : !ans ? t('Which chord goes in bar ' + (gap + 1) + '?', (gap + 1) + '마디에는 어떤 화음이 올까요?') : ans === BLUES_12[gap] ? t('Yes: bar ' + (gap + 1) + ' is ' + ans + '.', '맞아요: ' + (gap + 1) + '마디는 ' + ans + ' 화음이에요.') : t('Bar ' + (gap + 1) + ' is ' + BLUES_12[gap] + '.', (gap + 1) + '마디는 ' + BLUES_12[gap] + ' 화음이에요.')), ans && ans !== BLUES_12[gap])}
      <div style={{display:'flex',justifyContent:'center',gap:8,flexWrap:'wrap'}}>{chxBtn('p', t('▶ 12 bars', '▶ 열두 마디'), blues, false)}{chxBtn('g', gap == null || ans ? t('A missing chord', '빠진 화음') : t('Another bar', '다른 마디'), ask, false)}</div>
      <div style={{borderTop:'1px dashed rgba(38,41,107,0.25)',margin:'12px 0 0',paddingTop:10}}>
        <div style={{display:'grid',gridTemplateColumns:w < 380 ? '1fr' : 'repeat(2,minmax(0,1fr))',gap:14,maxWidth:420,margin:'0 auto'}}>
          {[false, true].map(sw => <div key={String(sw)}><div style={{fontSize:12,fontWeight:900,letterSpacing:'0.08em',color:playing === (sw ? 'swing' : 'straight') ? BK.coral : BK.muted,textAlign:'center',textTransform:'uppercase'}}>{sw ? t('swing', '스윙') : t('straight', '스트레이트')}</div><CsxSwing swing={sw} W={w < 380 ? w : Math.round(w / 2 - 7)} H={36} label={sw ? t('Swing: long-short.', '스윙: 길게-짧게.') : t('Straight: even.', '스트레이트: 고르게.')}/></div>)}</div>
        <div style={{display:'flex',justifyContent:'center',gap:8,marginTop:6,flexWrap:'wrap',whiteSpace:'nowrap',wordBreak:'keep-all'}}>{chxBtn('s1', t('▶ Straight', '▶ 스트레이트'), () => swing(false), playing === 'straight')}{chxBtn('s2', t('▶ Swing', '▶ 스윙'), () => swing(true), playing === 'swing')}{cpxStopBtn(!!playing, () => cpxStop())}</div>
      </div>
    </div>
  );
}

// page 6: a song's map (tap verse or chorus) and the four chords
function CsxPopPad() {
  const me = React.useRef({}).current, tm = React.useRef([]), [hl, setHl] = useState('chorus'), [on, setOn] = useState(-1), [playing, setPlaying] = useState(false), [box, w] = useCpxW(480);
  const clear = () => { tm.current.forEach(clearTimeout); tm.current = []; setOn(-1); };
  useEffect(() => () => { clear(); cpxStop(me); }, []);
  const loop = () => { clear(); const bpm = 100, s = csxPlay(csxPopEv(2), bpm, () => { clear(); setPlaying(false); }, me); if (!s) return; setPlaying(true);
    for (let i = 0; i < 8; i++) tm.current.push(setTimeout(() => setOn(i % 4), (0.1 + i * 4 * 60 / bpm) * 1000)); };
  return (
    <div className="try-box" style={actBox} data-csx="pad-pop">
      <div style={actTitle}>{t('A song', '노래 한 곡')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{csxKoT(t('Tap verse, chorus or bridge. Then hear the four chords.', '벌스, 후렴, 브리지를 눌러요. 그다음 네 화음을 들어요.'))}</div>
      <div role="group" aria-label={t('The parts of a song', '노래의 부분')} style={{display:'flex',justifyContent:'center',gap:6,margin:'0 0 8px'}}>{['verse', 'chorus', 'bridge'].map(k => cpxChip(hl === k, t(CSX_SONG_W[k][0], CSX_SONG_W[k][1]), () => setHl(k), k))}</div>
      <div ref={box} style={{maxWidth:480,margin:'0 auto'}}><CsxSong hl={hl} W={w} fs={w < 400 ? 13 : 12} label={t('A song’s map, the ' + CSX_SONG_W[hl][0] + ' lit.', '노래의 지도. ' + cpxJ(CSX_SONG_W[hl][1], '을', '를') + ' 표시했어요.')}/></div>
      {cpxMsg(csxKoT({ verse: t('Verse: the same tune, new words each time (twice here).', '벌스: 같은 선율, 매번 새 가사(여기서는 두 번).'), chorus: t('Chorus: the same tune and the same words, three times.', '후렴: 같은 선율, 같은 가사로 세 번.'), bridge: t('Bridge: something new, once, before the last chorus.', '브리지: 마지막 후렴 전에 한 번 나오는 새로운 부분.') }[hl]))}
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:8,maxWidth:340,margin:'4px auto 8px'}}>{CSX_POP.map(([n], i) => <div key={n} style={{border:'1.4px solid ' + (on === i ? BK.coral : BK.ink),borderRadius:6,padding:'6px 0',textAlign:'center',background:on === i ? 'rgba(228,87,46,0.10)' : '#fff'}}><div style={{fontSize:18,fontWeight:900,color:on === i ? BK.coral : BK.ink}}>{n}</div><div style={{fontSize:11,fontWeight:800,color:BK.muted}}>{['I', 'V', 'vi', 'IV'][i]}</div></div>)}</div>
      <div style={{display:'flex',justifyContent:'center',gap:8}}>{chxBtn('p', t('▶ Four chords', '▶ 네 화음'), loop, false)}{cpxStopBtn(playing, () => cpxStop())}</div>
    </div>
  );
}

// ── the book on screen: the opener is the lesson's head, every other page a step; a texture ear test at the end ──
function CsxLearn({ onStart }) {
  const pages = csxLbPages(true);
  const opener = pages[0];
  return (
    <Lesson id="styles" title={bkChapterName('styles')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="styles"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => (
        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
      <Step key="ear" extra title={t('Which style?', '어떤 스타일일까요?')} storeAs="k7"><CsxGenreEarPad/></Step>
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order ──
const CSX_LEVELS = [
  { n: 1, label: 'Which texture?', kind: 'tex', time: 10 },
  { n: 2, label: 'Listen: which texture?', kind: 'texEar', time: 16, noPrint: true },
  { n: 3, label: 'Which period sounds like this?', kind: 'sound', time: 12 },
  { n: 4, label: 'Which style is it?', kind: 'genre', time: 12 },
  { n: 5, label: 'The 12-bar blues', kind: 'blues', time: 10 },
  { n: 6, label: 'Listen: straight or swing?', kind: 'swing', time: 12, noPrint: true },
  { n: 7, label: 'Which five notes?', kind: 'penta', time: 12 },
  { n: 8, label: 'The words', kind: 'word', time: 10 },
  { n: 9, label: 'Extra: listen: which style?', kind: 'earGenre', time: 20, noPrint: true },
];
Object.assign(LEVEL_KO, { 'Which texture?': '어떤 텍스처일까요?', 'Listen: which texture?': '듣기: 어떤 텍스처일까요?', 'Which period sounds like this?': '어느 시대의 소리일까요?', 'Which style is it?': '어떤 스타일일까요?',
  'The 12-bar blues': '12마디 블루스', 'Listen: straight or swing?': '듣기: 스트레이트일까, 스윙일까?', 'Which five notes?': '어떤 다섯 음일까요?', 'The words': '용어', 'Extra: listen: which style?': '더 해 보기: 듣고 어떤 스타일인지 맞혀요' });
// the four style families and what marks each (from Phase 282's GENRE_TRAITS, one fact a line)
const CSX_GENRES = ['folk', 'classical', 'jazz', 'pop'];
const CSX_GENRE_W = { folk: ['folk', '민속 음악'], classical: ['classical', '클래식'], jazz: ['jazz and blues', '재즈와 블루스'], pop: ['pop', '대중음악'] };
const CSX_TRAITS = [
  ['folk', 'Passed on by ear, often with no known composer.', '귀로 전해지고, 작곡가를 모르는 경우가 많아요.'],
  ['folk', 'Songs and dances of one people or place, such as “Arirang”.', '“아리랑”처럼 한 민족이나 한 지역의 노래와 춤곡.'],
  ['folk', 'Often on five notes: a pentatonic scale.', '다섯 음으로 된 5음음계를 쓸 때가 많아요.'],
  ['classical', 'Written down note by note and played as written.', '음 하나하나 악보에 적고, 적힌 대로 연주해요.'],
  ['classical', 'Sonatas and symphonies, for the concert hall.', '연주회장을 위한 소나타와 교향곡.'],
  ['classical', 'Composed by the likes of Bach, Mozart and Chopin.', '바흐, 모차르트, 쇼팽 같은 작곡가들이 썼어요.'],
  ['jazz', 'Players make the music up as they play: improvisation.', '연주하면서 음악을 지어내요: 즉흥 연주.'],
  ['jazz', 'Quavers played long-short: swing.', '8분음표를 길게-짧게 쳐요: 스윙.'],
  ['jazz', 'Three chords over twelve bars.', '열두 마디에 세 화음.'],
  ['pop', 'Songs with a strong drum beat, sung over a band.', '밴드 반주에 맞춰 부르는, 드럼 비트가 강한 노래.'],
  ['pop', 'Songs of about three minutes, on records, radio and online.', '음반, 라디오, 인터넷으로 듣는 3분쯤 되는 노래.'],
  ['pop', 'Four chords looped again and again, such as C G Am F.', 'C G Am F처럼 네 화음을 되풀이해요.'],
];
// pentatonic: a major scale without its 4th and 7th (the shape of C D E G A, on other notes); and sets that are not: a half
// step between neighbours as written, or not five notes. None is five notes without half steps in another shape (r1: no
// C D E F♯ G♯), and every half step sits between two notes written side by side (r1: not C E G B D).
const CSX_SETS = [['C D E G A', 'penta'], ['F♯ G♯ A♯ C♯ D♯', 'penta'], ['G A B D E', 'penta'], ['F G A C D', 'penta'], ['D E F♯ A B', 'penta'],
  ['C D E F G', 'half'], ['C E F G A', 'half'], ['D E F A B', 'half'], ['G A B C D', 'half'], ['A B C D E', 'half'], ['D E F G A', 'half'], ['C D E F G A B', 'seven'], ['C D E G', 'four']];
const CSX_WORDS = [
  ['texture', 'how the lines of music are layered', '음악에서 선율과 화음이 짜인 모양'],
  ['monophony', 'one line alone', '선율 한 줄만 있는 것'],
  ['homophony', 'a tune with chords underneath', '아래에서 화음이 받쳐 주는 선율'],
  ['polyphony', 'two or more tunes at once, each as important as the other', '두 개 이상의 선율이 똑같이 중요하게 동시에 흐르는 것'],
  ['style', 'the way music sounds', '음악 소리의 특징'],
  ['ornament', 'a quick decoration of a note, such as a trill', '트릴처럼 음을 빠르게 꾸미는 것'],
  ['minimalism', 'short patterns repeated many times, changing slowly', '짧은 패턴을 되풀이하며 조금씩 바꾸는 음악'],
  ['folk music', 'the songs and dances of a people, passed on by ear', '한 민족이 귀로 전해 온 노래와 춤곡'],
  ['pentatonic scale', 'a major scale without its 4th and 7th notes', '장음계에서 4번째와 7번째 음을 뺀 다섯 음의 음계'],
  ['12-bar blues', 'three chords over twelve bars', '열두 마디에 세 화음'],
  ['swing', 'pairs of quavers played long-short', '8분음표 두 개를 길게-짧게 치는 것'],
  ['improvisation', 'making music up as you play', '연주하면서 음악을 지어내는 것'],
  ['verse', 'the same tune with new words each time', '같은 선율에 매번 새 가사가 붙는 부분'],
  ['chorus', 'the part that comes back with the same words', '같은 가사로 다시 나오는 부분'],
];
const CSX_WORD_KO = { texture: '텍스처', monophony: '모노포니', homophony: '호모포니', polyphony: '폴리포니', style: '스타일', ornament: '꾸밈음', minimalism: '미니멀리즘', 'folk music': '민속 음악', 'pentatonic scale': '5음음계', '12-bar blues': '12마디 블루스', swing: '스윙', improvisation: '즉흥 연주', verse: '벌스', chorus: '후렴' };
// the four styles to hear: folk (a tune on five notes, alone), classical (a real opening with its accompaniment: Vivaldi,
// Bach, Beethoven, Liszt), jazz and blues (the boogie, swung), pop (four chords)
const CSX_EAR_CLASSICAL = ['vivaldi', 'bach', 'beethoven', 'liszt'];
// a composer's clip, at most four bars (r2: within the game's 20 seconds)
function csxHearBars(id, bars, onEnd, owner) {
  cpxStop(); const h = cpxSound(id); if (!h) return 0;
  const s = cmpPlay(h, bars); if (!s) return 0;
  _cpxEnd = onEnd || null; _cpxOwner = owner;
  _cpxTm = setTimeout(() => { _cpxTm = null; _cpxOwner = null; const e = _cpxEnd; _cpxEnd = null; if (e) e(); }, s * 1000 + 250); return s;
}
const csxGenrePlay = (g, k, cb, me) => g === 'folk' ? csxPlay(csxFolkEv(k % 2 === 1), 104, cb, me) : g === 'classical' ? csxHearBars(CSX_EAR_CLASSICAL[k % CSX_EAR_CLASSICAL.length], 4, cb, me) : g === 'jazz' ? csxPlay(csxBluesEv(4), 112, cb, me) : csxPlay(csxPopEv(1), 100, cb, me);
const csxGenreClip = (g, k) => g === 'folk' ? 'folk' + (k % 2) : g === 'classical' ? CSX_EAR_CLASSICAL[k % CSX_EAR_CLASSICAL.length] : g;   // what is heard
// each level remembers its last questions (not again soon) and its last two answers (never three the same in a row)
const _csxRecent = {}, _csxAns = {};
function genCsxQuestion(lv, prev) {
  const r = _csxRecent[lv.n] || (_csxRecent[lv.n] = []), a = _csxAns[lv.n] || (_csxAns[lv.n] = []);
  const keep = ({ tex: 4, texEar: 3, sound: 8, genre: 6, blues: 1, swing: 0, penta: 3, word: 8, earGenre: 1 })[lv.kind] ?? 4;
  const third = (x) => a.length > 1 && a[a.length - 1] === x.answer && a[a.length - 2] === x.answer;
  let q = null; for (let g = 0; g < 40; g++) { const x = genCsxQuestion0(lv, prev); if (!x) continue; q = x; if (!r.includes(x.key) && !third(x)) break; }
  if (q) { r.push(q.key); while (r.length > keep) r.shift(); a.push(q.answer); while (a.length > 2) a.shift(); }
  return q;
}
function genCsxQuestion0(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'tex' || kind === 'texEar') { const x = pick(CSX_TEX), tune = pick(['a', 'b', 'c']); return { kind, key: x + tune, x, tune, answer: x, choices: [...CSX_TEX], uid }; }
  if (kind === 'sound') { const era = pick(MTL_ERAS), k = Math.floor(Math.random() * 3); return { kind, key: era + k, era, w: CSX_ERA[era].listen[k], answer: era, choices: [...MTL_ERAS], uid }; }
  if (kind === 'genre') { const g = pick(CSX_GENRES), tr = pick(CSX_TRAITS.filter(x => x[0] === g)); return { kind, key: tr[1], tr, answer: g, choices: [...CSX_GENRES], uid }; }
  if (kind === 'blues') { const want = pick(['I', 'I', 'IV', 'IV', 'V']), i = pick(BLUES_12.map((c, j) => c === want ? j : -1).filter(j => j >= 0)); return { kind, key: 'b' + i, bar: i, answer: BLUES_12[i], choices: ['I', 'IV', 'V'], uid }; }
  if (kind === 'swing') { const sw = Math.random() < 0.5; return { kind, key: 'sw' + sw, sw, answer: sw ? 'swing' : 'straight', choices: ['straight', 'swing'], uid }; }
  if (kind === 'penta') { const right = pick(CSX_SETS.filter(s => s[1] === 'penta')), wrong = shuffle(CSX_SETS.filter(s => s[1] !== 'penta')).slice(0, 3); return { kind, key: right[0], answer: right[0], choices: shuffle([right, ...wrong].map(s => s[0])), uid }; }
  if (kind === 'word') { const w = pick(CSX_WORDS); return { kind, key: w[0], w, answer: w[0], choices: shuffle([w[0], ...shuffle(CSX_WORDS.filter(x => x !== w).map(x => x[0])).slice(0, 3)]), uid }; }
  const g = pick(CSX_GENRES), k = Math.floor(Math.random() * 4); return { kind: 'earGenre', key: csxGenreClip(g, k), g, k, answer: g, choices: [...CSX_GENRES], uid };
}
const csxCheck = (q, ans) => ans != null && String(ans) === String(q.answer);
const csxChoiceTxt = (c, q) => q.kind === 'tex' || q.kind === 'texEar' ? csxTexW(c) : q.kind === 'sound' ? cmpEraTag(c) : q.kind === 'genre' || q.kind === 'earGenre' ? t(CSX_GENRE_W[c][0], CSX_GENRE_W[c][1])
  : q.kind === 'blues' ? csxChordNm(c) : q.kind === 'swing' ? (c === 'swing' ? t('swing', '스윙') : t('straight', '스트레이트')) : q.kind === 'word' ? t(c, CSX_WORD_KO[c]) : c;
function csxAnswerLabel(q) { return csxKoT(csxAnswerLabel0(q)); }
function csxAnswerLabel0(q) {
  const ch = csxChoiceTxt(q.answer, q);
  if (q.kind === 'word') return t(q.w[0] + ' = ' + q.w[1], CSX_WORD_KO[q.w[0]] + ' = ' + q.w[2]);
  if (q.kind === 'sound') return t(ch + ': ' + q.w[0], ch + '(' + q.w[1] + ')');
  if (q.kind === 'blues') return t('bar ' + (q.bar + 1) + ': ' + ch, (q.bar + 1) + '마디는 ' + ch);
  if (q.kind === 'penta') return t(ch + ': a major scale without its 4th and 7th notes', ch + '​(장음계에서 4번째와 7번째 음을 뺀 다섯 음)');
  if (q.kind === 'swing') return t(ch + (q.sw ? ': long-short' : ': even'), ch + (q.sw ? '(길게-짧게)' : '(고르게)'));
  return ch;
}
function CsxQuestion({ q, given, locked, onAnswer, pixel }) {
  const me = React.useRef({}).current, givenRef = React.useRef(given), heardRef = React.useRef(null); givenRef.current = given;
  const paper = locked && !given, isDone = !!given;
  const board = useBoard(q, given), btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const ink = pixel ? '#faf6ec' : 'var(--text)';
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const ear = q.kind === 'texEar' || q.kind === 'swing' || q.kind === 'earGenre';
  const hear = () => { heardRef.current = q.uid; return hear0(); };
  const hear0 = () => q.kind === 'texEar' ? csxPlay(csxTexEv(q.x, q.tune), 120, null, me) : q.kind === 'swing' ? csxPlay(csxSwingEv(q.sw), 112, null, me) : csxGenrePlay(q.g, q.k, null, me);
  useEffect(() => () => cpxStop(me), [q.uid]);
  useEffect(() => { if (ear && !locked) { const tm = setTimeout(() => { if (!givenRef.current && heardRef.current !== q.uid) hear(); }, 350); return () => clearTimeout(tm); } }, [q.uid]);
  const prompt = csxKoT(({ tex: () => t('Which texture is this?', '이 그림은 어떤 텍스처일까요?'), texEar: () => t('Listen: which texture is this?', '듣고 골라요: 어떤 텍스처일까요?'), sound: () => t('Which period sounds like this?', '이런 소리는 어느 시대일까요?'),
    genre: () => t('Which style is this?', '어떤 스타일의 특징일까요?'), blues: () => t('Which chord goes in bar ' + (q.bar + 1) + ' of the 12-bar blues?', '12마디 블루스의 ' + (q.bar + 1) + '마디에는 어떤 화음이 올까요?'),
    swing: () => t('Listen: straight or swing?', '듣고 골라요: 스트레이트일까, 스윙일까?'), penta: () => t('Which five notes make a pentatonic scale?', '어느 다섯 음이 5음음계일까요?'), word: () => t('Which word means this?', '이 뜻의 용어는 무엇일까요?'),
    earGenre: () => t('Listen: which style is this?', '듣고 골라요: 어떤 스타일일까요?') })[q.kind]());
  let pic = null;
  if (q.kind === 'tex') pic = <div style={{maxWidth:360,margin:'0 auto 8px',background:'#fff',borderRadius:8,padding:4}}><CsxRoll tex={q.x} tune={q.tune} even label={t('A tune drawn as blocks; the texture to name.', '막대로 그린 선율. 텍스처를 맞혀요.')}/></div>;
  else if (q.kind === 'sound' || q.kind === 'genre' || q.kind === 'word') { const w = q.kind === 'sound' ? q.w : q.kind === 'genre' ? [q.tr[1], q.tr[2]] : [q.w[1], q.w[2]];
    pic = <div style={{textAlign:'center',fontSize:pixel ? 13 : 19,fontWeight:900,color:ink,margin:'0 0 8px',textWrap:'balance',wordBreak:'keep-all'}}>“{csxKoT(t(w[0], w[1]))}”</div>; }
  else if (q.kind === 'blues') pic = <div style={{maxWidth:360,margin:'0 auto 8px',background:'#fff',borderRadius:8,padding:4}}><CsxBlues gaps={isDone ? [] : [q.bar]} hl={isDone ? q.bar : -1} letters={false} label={t('The 12-bar blues with bar ' + (q.bar + 1) + ' empty.', (q.bar + 1) + '마디가 빈 12마디 블루스.')}/></div>;
  else if (ear) pic = <div style={{textAlign:'center',margin:'4px 0 6px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={hear}>{t('▶ Listen again', '▶ 다시 듣기')}</button>
    {isDone && !pixel && (q.kind === 'texEar' ? <div style={{maxWidth:360,margin:'8px auto 0',background:'#fff',borderRadius:8,padding:4}}><CsxRoll tex={q.x} tune={q.tune} label={csxTexW(q.x)}/></div> : q.kind === 'swing' ? <div style={{maxWidth:300,margin:'8px auto 0'}}><CsxSwing swing={q.sw} label={q.sw ? t('Swing: long-short.', '스윙: 길게-짧게.') : t('Straight: even.', '스트레이트: 고르게.')}/></div> : null)}</div>;
  const tight = pixel || (typeof window !== 'undefined' && window.innerWidth < 400);
  const cols = q.choices.length === 2 || (q.choices.length === 3 && !tight) ? q.choices.length : (q.kind === 'word' || q.kind === 'penta') && tight ? 1 : 2;
  return <div>{!paper && <BoardTrack b={board} pixel={pixel}/>}
    <p style={{fontSize:pixel ? 11.5 : 17,fontWeight:900,textAlign:'center',margin:'0 0 8px',color:ink,textWrap:'balance',wordBreak:'keep-all'}}>{prompt}</p>
    {pic}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,maxWidth:520,margin:'0 auto'}}>{q.choices.map((c, j) => <button key={c} disabled={locked} data-csx-choice={c} onClick={() => { cpxStop(); onAnswer(c); }} className={btnCls + st(c)}
      style={{minHeight:pixel ? undefined : 48,padding:'6px 8px',gridColumn:cols === 2 && q.choices.length % 2 && j === q.choices.length - 1 ? 'span 2' : undefined}}>
      <span style={{fontSize:pixel ? 11 : 16,fontWeight:900,wordBreak:'keep-all'}}>{q.kind === 'penta' ? csxNotes(c) : csxKoT(csxChoiceTxt(c, q))}</span></button>)}</div>
  </div>;
}
// the lesson's last step: hear a style, name it
function CsxGenreEarPad() {
  const me = React.useRef({}).current, [q, setQ] = useState(null), [ans, setAns] = useState(null), [playing, setPlaying] = useState(false), [score, setScore] = useState({ right: 0, tries: 0 });
  useEffect(() => () => cpxStop(me), []);
  const play = (x) => setPlaying(csxGenrePlay(x.g, x.k, () => setPlaying(false), me) > 0);
  const next = () => { const x = genCsxQuestion(CSX_LEVELS[8], null); setQ(x); setAns(null); play(x); };   // the drill's own pick: no clip twice running
  const choose = (g) => { if (!q || ans) return; setAns(g); setScore(s => ({ right: s.right + (g === q.g ? 1 : 0), tries: s.tries + 1 })); };
  return (
    <div className="try-box" style={actBox} data-csx="pad-ear">
      <div style={actTitle}>{t('Which style?', '어떤 스타일일까요?')}</div>
      <div style={{...actNote,textWrap:'pretty'}}>{csxKoT(t('Hear a few bars. Folk, classical, jazz and blues, or pop?', '몇 마디를 들어요. 민속 음악, 클래식, 재즈와 블루스, 대중음악 중 무엇일까요?'))}</div>
      <div role="group" aria-label={t('Styles', '스타일')} style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,maxWidth:360,margin:'0 auto 8px'}}>{CSX_GENRES.map(g => <button key={g} type="button" aria-disabled={!q || !!ans} onClick={() => choose(g)} className={'choice-btn' + (ans && g === q.g ? ' good' : ans === g ? ' bad' : '')} style={{minHeight:48,fontSize:15,fontWeight:900,wordBreak:'keep-all',opacity:q ? 1 : 0.5}}>{t(CSX_GENRE_W[g][0], CSX_GENRE_W[g][1])}</button>)}</div>
      {cpxMsg(csxKoT(!q ? t('Press ▶ Hear one.', '▶ 듣기를 눌러요.') : !ans ? t('Which style is it?', '어떤 스타일일까요?') : ans === q.g ? t('Yes.', '맞아요.') : t('It was ' + CSX_GENRE_W[q.g][0] + '.', cpxJ(CSX_GENRE_W[q.g][1], '이었어요', '였어요') + '.')), ans && ans !== q.g)}
      <div style={{display:'flex',justifyContent:'center',gap:8,alignItems:'center',flexWrap:'wrap'}}>{chxBtn('n', q ? t('▶ Next', '▶ 다음') : t('▶ Hear one', '▶ 듣기'), next, false)}{q && chxBtn('a', t('Again', '다시'), () => play(q), false)}{cpxStopBtn(playing, () => cpxStop())}{score.tries > 0 && <span style={{fontSize:13,fontWeight:800,color:BK.muted}}>{t(score.right + ' of ' + score.tries, score.tries + '번 중 ' + score.right + '번')}</span>}</div>
    </div>
  );
}
