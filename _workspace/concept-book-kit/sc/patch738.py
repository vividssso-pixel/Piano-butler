import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BS (board call 26, the Grade 6 floor's room lessons): Theory of Music Grade 6 general knowledge and creative work, and the
# Grades 5-6 practical general knowledge (form: First Movement (Sonata), Fugue), as lessons in rooms that already exist:
# Form: sonata form, the fugue · Melody: a melody that changes key (the four-line stanza "with modulation") · Instruments: the brass
# of the orchestra (horn in F, trumpet in B♭, tenor trombone, tuba in F: ranges and clefs) · Styles: sonata, symphony, concerto,
# overture. The tunes are our own, written for these lessons. Ranges, examples and definitions are from my own knowledge, so they
# go on the board's list of things for Sohyun to check.

rep("""  'form': ['fmx-map', 'fmx-phrase', 'fmx-letters', 'fmx-binary', 'fmx-ternary', 'fmx-find', 'fmx-build', 'fmx-forms5',""",
    """  'form': ['fmx-map', 'fmx-phrase', 'fmx-letters', 'fmx-binary', 'fmx-ternary', 'fmx-find', 'fmx-build', 'fmx-forms5', 'fmx-sonata', 'fmx-fugue',""")
rep("""'mlx-couplet', 'mlx-stanza', 'mlx-build', 'tune-anatomy',""", """'mlx-couplet', 'mlx-stanza', 'mlx-modulate', 'mlx-build', 'tune-anatomy',""")
rep("""  'pitch-range': ['spr-zone', 'spr-big', 'spr-fam', 'spr-ladder', 'spr-tune', 'spr-wind',""", """  'pitch-range': ['spr-zone', 'spr-big', 'spr-fam', 'spr-ladder', 'spr-tune', 'spr-wind', 'spr-brass',""")
rep("""  'styles': ['csx-map', 'csx-texture', 'csx-era', 'csx-penta', 'csx-blues', 'csx-jam', 'csx-pop', 'mk-sty', 'csx-ear'],""",
    """  'styles': ['csx-map', 'csx-texture', 'csx-era', 'csx-penta', 'csx-blues', 'csx-jam', 'csx-pop', 'mk-sty', 'csx-ear', 'csx-genres'],""")
rep("""'fmx-build', 'fmx-forms5', 'same-or-new', 'binary-ternary-spot',""", """'fmx-build', 'fmx-forms5', 'fmx-sonata', 'fmx-fugue', 'same-or-new', 'binary-ternary-spot',""")
rep("""'mlx-couplet', 'mlx-stanza', 'mlx-build', 'phrase-marks',""", """'mlx-couplet', 'mlx-stanza', 'mlx-modulate', 'mlx-build', 'phrase-marks',""")
rep("""  set('5', 'mlx-stanza fmx-forms5 spr-wind');   // Build BE: Grade 5 creative work and general knowledge""",
    """  set('5', 'mlx-stanza fmx-forms5 spr-wind');   // Build BE: Grade 5 creative work and general knowledge
  set('6', 'fmx-sonata fmx-fugue mlx-modulate spr-brass csx-genres');   // Build BS: Grade 6 general knowledge and creative work""")

CODE = r'''
// ══ Build BS: the Grade 6 floor's room lessons (Theory of Music Grade 6 general knowledge and creative work) ══
// ── Form: sonata form, heard in a tiny movement of our own: [note, beats] tunes over [note, beats] basses, in semitones from middle C ──
const SON_TUNE = {
  s1: [[12, .5], [16, .5], [19, 1], [19, 1], [17, .5], [16, .5], [14, 1], [11, 1], [12, 2], [16, .5], [19, .5], [24, 1], [23, .5], [21, .5], [19, 1], [17, 1], [16, 1], [14, 2]],
  br: [[19, .5], [18, .5], [19, .5], [21, .5], [23, 1], [19, 1], [21, .5], [19, .5], [18, .5], [16, .5], [18, 1], [14, 1]],
  s2: [[11, 2], [12, 1], [14, 1], [16, 1.5], [14, .5], [12, 1], [11, 1], [9, 1], [11, 1], [12, 1], [6, 1], [7, 4]],
  cd: [[19, .5], [14, .5], [11, .5], [14, .5], [19, .5], [14, .5], [11, .5], [14, .5], [7, 1], [14, 1], [7, 2]],
  dv: [[9, .5], [12, .5], [16, 1], [16, 1], [14, .5], [12, .5], [11, 1], [8, 1], [9, 2], [14, .5], [17, .5], [21, 1], [21, 1], [19, .5], [17, .5], [16, 1], [13, 1], [14, 2], [19, 1], [17, 1], [16, 1], [14, 1], [17, 1], [16, 1], [14, 1], [11, 1]],
  rbr: [[19, .5], [17, .5], [19, .5], [21, .5], [23, 1], [19, 1], [21, .5], [19, .5], [17, .5], [16, .5], [17, 1], [14, 1]],
  coda: [[24, 1], [19, 1], [16, 1], [19, 1], [12, 1], [7, 1], [12, 2]],
};
const SON_BASS = { s1: [[-12, 4], [-17, 2], [-12, 2], [-12, 4], [-17, 4]], br: [[-17, 4], [-10, 4]], s2: [[-17, 4], [-12, 4], [-15, 2], [-10, 2], [-17, 4]], cd: [[-17, 4], [-10, 2], [-17, 2]],
  dv: [[-15, 4], [-20, 2], [-15, 2], [-10, 4], [-15, 2], [-10, 2], [-17, 8]], rbr: [[-12, 4], [-17, 4]], coda: [[-12, 4], [-17, 2], [-12, 2]] };
const sonUp = (P, k) => P.map(([x, d]) => [x + k, d]);
const SON = [
  { id: 'exp', en: 'Exposition', ko: '제시부', parts: [
    { id: 's1', en: 'First subject', ko: '제1주제', key: ['C major, the tonic', 'C장조, 으뜸조'], m: SON_TUNE.s1, b: SON_BASS.s1 },
    { id: 'br', en: 'Bridge', ko: '경과부', key: ['on the move: F♯ appears', '이동 중: F♯이 나타나요'], m: SON_TUNE.br, b: SON_BASS.br },
    { id: 's2', en: 'Second subject', ko: '제2주제', key: ['G major, the dominant', 'G장조, 딸림조'], m: SON_TUNE.s2, b: SON_BASS.s2, away: true },
    { id: 'cd', en: 'Codetta', ko: '코데타', key: ['G major', 'G장조'], m: SON_TUNE.cd, b: SON_BASS.cd, away: true }] },
  { id: 'dev', en: 'Development', ko: '발전부', parts: [
    { id: 'dv', en: 'Development', ko: '발전부', key: ['new keys: A minor, D minor, then V', '새 조들: A단조, D단조, 그다음 V'], m: SON_TUNE.dv, b: SON_BASS.dv, away: true }] },
  { id: 'rec', en: 'Recapitulation', ko: '재현부', parts: [
    { id: 'r1', en: 'First subject', ko: '제1주제', key: ['C major', 'C장조'], m: SON_TUNE.s1, b: SON_BASS.s1 },
    { id: 'rb', en: 'Bridge', ko: '경과부', key: ['stays home', '집에 머물러요'], m: SON_TUNE.rbr, b: SON_BASS.rbr },
    { id: 'r2', en: 'Second subject', ko: '제2주제', key: ['C major, now the tonic', 'C장조, 이제 으뜸조'], m: sonUp(SON_TUNE.s2, 5), b: sonUp(SON_BASS.s2, 5), home: true },
    { id: 'rc', en: 'Codetta', ko: '코데타', key: ['C major', 'C장조'], m: sonUp(SON_TUNE.cd, 5), b: sonUp(SON_BASS.cd, 5) }] },
  { id: 'coda', en: 'Coda', ko: '코다', parts: [{ id: 'co', en: 'Coda', ko: '코다', key: ['C major', 'C장조'], m: SON_TUNE.coda, b: SON_BASS.coda }] },
];
const SON_PARTS = SON.flatMap(sec => sec.parts.map(p => ({ ...p, sec: sec.id })));
const sonLen = (P) => P.reduce((a, x) => a + x[1], 0);
const sonEvents = (parts) => { const ev = [], at0 = []; let at = 0; parts.forEach(p => { at0.push(at); let a = at; p.m.forEach(([x, d]) => { ev.push({ at: a, keys: [x], len: d * 0.92, vol: 0.15 }); a += d; }); a = at; p.b.forEach(([x, d]) => { ev.push({ at: a, keys: [x], len: d * 0.95, vol: 0.1 }); a += d; }); at += sonLen(p.m); }); return { ev, at0, end: at }; };
const SON_CLUE = [['s1', ['The first main tune, in the home key.', '첫째 주요 선율, 집 조에서.']], ['br', ['The passage that leads from the first key to the second.', '첫째 조에서 둘째 조로 이끄는 부분.']],
  ['s2', ['A second main tune, often more singing: in the dominant (in a minor key, the relative major).', '둘째 주요 선율, 흔히 더 노래하듯: 딸림조에서(단조 곡이면 나란한 장조).']], ['dev', ['The tunes broken into pieces and taken through new keys.', '선율을 조각내어 새 조들로 데려가요.']],
  ['rec', ['Both main tunes again, now both in the home key.', '두 주요 선율이 다시, 이제 둘 다 집 조에서.']], ['coda', ['A last word added at the very end, in the home key.', '맨 끝에 덧붙인 마지막 말, 집 조에서.']]];
const SON_ANS = [['s1', 'First subject', '제1주제'], ['br', 'Bridge', '경과부'], ['s2', 'Second subject', '제2주제'], ['dev', 'Development', '발전부'], ['rec', 'Recapitulation', '재현부'], ['coda', 'Coda', '코다']];
function FmxSonataPad() {
  const [sel, setSel] = useState('s1'), [now, setNow] = useState(null), [quiz, setQuiz] = useState(null), [pickd, setPick] = useState(null);
  const T = useSpTimers(), P = SON_PARTS.find(p => p.id === sel);
  const play = (parts) => { T.clear(); const E = sonEvents(parts), r = spPlay(E.ev, 132); if (!r) return; parts.forEach((p, j) => T.at(r.ms(E.at0[j]), () => setNow(p.id))); T.at(r.ms(E.end) + 200, () => setNow(null)); };
  const tapPart = (p) => { setSel(p.id); play([p]); };
  const ask = () => { T.clear(); setNow(null); let c, g = 0; do { c = pick(SON_CLUE); } while (quiz && quiz.id === c[0] && g++ < 8); setQuiz({ id: c[0], clue: c[1] }); setPick(null); };
  const box = (p, sec) => { const on = now === p.id || (!now && sel === p.id); return <button key={p.id} onClick={() => tapPart(p)} style={{flex:'1 1 0',minWidth:0,padding:'6px 3px',borderRadius:8,cursor:'pointer',border:'1.5px solid ' + (on ? BK.coral : 'rgba(38,41,107,0.3)'),background:on ? '#fbe3da' : '#fff',color:BK.ink,textAlign:'center'}}>
    <div style={{fontSize:12,fontWeight:900,lineHeight:1.15,wordBreak:'keep-all'}}>{sec.parts.length > 1 ? t(p.en, p.ko) : '▶'}</div>
    <div style={{fontSize:10.5,fontWeight:800,color:p.away ? BK.coral : p.home ? BK.green : BK.muted,marginTop:2}}>{p.id === 'br' ? '→' : p.id === 'dv' ? '?' : p.away ? 'G' : 'C'}</div></button>; };
  return (
    <div className="try-box" style={actBox} data-fmx="sonata">
      <div style={actTitle}>{t('Sonata form', '소나타 형식')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>소나타, 교향곡, 협주곡의 첫 악장에 흔한 형식(“첫 악장 형식”). 세 부분: <b>제시부</b>(두 주제, 둘째는 딸림조로), <b>발전부</b>(주제를 조각내어 새 조들로), <b>재현부</b>(두 주제 다시, 이제 <b>둘 다 집 조에서</b>), 그리고 흔히 <b>코다</b>. 아래는 이 앱이 지은 작은 악장: 상자를 눌러 들어요.</>
        : <>The usual form of a first movement in a sonata, symphony or concerto ("first movement form"). Three parts: <b>the exposition</b> (two subjects, the second in the dominant), <b>the development</b> (the tunes broken up and taken through new keys) and <b>the recapitulation</b> (both subjects again, now <b>both in the home key</b>), often with <b>a coda</b>. Below is a tiny movement written for this app: tap a box to hear it.</>}</div>
      <div style={{display:'grid',gap:6,margin:'6px 0'}}>{SON.map(sec => <div key={sec.id}>
        <div style={{fontFamily:LB_SERIF,fontSize:14.5,fontWeight:900,color:BK.ink,margin:'0 0 2px'}}>{t(sec.en, sec.ko)}</div>
        <div style={{display:'flex',gap:4}}>{sec.parts.map(p => box(p, sec))}</div></div>)}</div>
      {quiz ? <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:BK.ink,margin:'6px 0',textWrap:'balance'}}>{t(quiz.clue[0], quiz.clue[1])}</div>
        : <div style={{fontSize:14,color:BK.ink,lineHeight:1.45,textAlign:'center',margin:'4px 0'}}><b>{t(SON.find(x => x.id === P.sec).en, SON.find(x => x.id === P.sec).ko)}{SON.find(x => x.id === P.sec).parts.length > 1 ? ' · ' + t(P.en, P.ko) : ''}</b>: {t(P.key[0], P.key[1])}</div>}
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:6}}>{SON_ANS.map(([id, en, ko]) => <button key={id} className={'choice-btn' + (pickd == null ? '' : id === quiz.id ? ' good' : id === pickd ? ' bad' : '')} onClick={() => { if (pickd == null) setPick(id); }} style={{padding:'10px 4px',fontSize:14,fontWeight:900}}>{t(en, ko)}</button>)}</div>}
      {quiz && pickd != null && spMsg(pickd === quiz.id ? t('Yes.', '맞아요.') : t('It was the ' + SON_ANS.find(x => x[0] === quiz.id)[1].toLowerCase() + '.', '정답은 ' + SON_ANS.find(x => x[0] === quiz.id)[2] + '.'), pickd === quiz.id ? BK.green : BK.coral)}
      {!quiz && <div style={{fontSize:13,fontWeight:800,color:BK.coral,textAlign:'center',marginTop:4}}>{t('Listen to: Mozart, Sonata in C major K. 545, first movement · Beethoven, Sonata in F minor Op. 2 No. 1, first movement', '들어 볼 곡: 모차르트, 소나타 C장조 K. 545, 첫 악장 · 베토벤, 소나타 F단조 Op. 2 No. 1, 첫 악장')}</div>}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => play(SON_PARTS)}>{t('▶ The whole movement', '▶ 악장 전체')}</button>
        <button className="ghost-btn" style={spBtn} onClick={ask}>{quiz && pickd == null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(null); setPick(null); }}>{t('← Back', '← 돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── Form: the fugue: an exposition in three voices (our own subject, in C minor), drawn as three lanes ──
const FUG_S = [[0, 1], [-5, 1], [-4, 1], [-5, .5], [-7, .5], [-9, .5], [-10, .5], [-9, .5], [-7, .5], [-5, 2]];   // C G A♭ G F E♭ D E♭ F G
const FUG_V = [   // [voice, start beat, kind, [note, beats]]
  ['alto', 0, 'subject', FUG_S], ['sop', 8, 'answer', sonUp(FUG_S, 19)], ['alto', 8, 'counter', [[3, 1], [-2, 1], [0, 1], [-2, 1], [-5, 2], [-6, 2]]],
  ['bass', 16, 'subject', sonUp(FUG_S, -12)], ['alto', 16, 'counter', [[8, 1], [3, 1], [5, 1], [3, 1], [0, 2], [-1, 2]]], ['sop', 16, 'free', [[15, 4], [19, 2], [14, 2]]],
  ['sop', 24, 'episode', [[15, .5], [14, .5], [12, .5], [14, .5], [12, .5], [10, .5], [8, .5], [10, .5], [8, .5], [7, .5], [5, .5], [7, .5], [5, .5], [3, .5], [2, 1]]], ['alto', 24, 'episode', [[3, 2], [2, 2], [0, 2], [-1, 2]]], ['bass', 24, 'episode', [[-16, 2], [-17, 2], [-19, 2], [-17, 2]]],
  ['alto', 32, 'subject', FUG_S], ['sop', 32, 'free', [[15, 2], [14, 2], [12, 2], [11, 2]]], ['bass', 32, 'free', [[-12, 2], [-16, 2], [-19, 2], [-17, 2]]],
  ['sop', 40, 'free', [[16, 3]]], ['alto', 40, 'free', [[0, 3]]], ['bass', 40, 'free', [[-24, 3]]],   // the last chord: C major, a Picardy third
];
const FUG_KIND = { subject: ['Subject', '주제', BK.coral], answer: ['Answer', '응답', BK.ink], counter: ['Countersubject', '대주제', '#8a8cb8'], free: ['Free part', '자유 성부', 'rgba(38,41,107,0.25)'], episode: ['Episode', '에피소드', 'rgba(38,41,107,0.12)'] };
const FUG_TERMS = [
  ['subject', ['The tune the whole fugue is made from, first heard alone in one voice.', '푸가 전체를 만드는 선율. 처음엔 한 성부 혼자.']],
  ['answer', ['The subject again in the next voice, a 5th higher (in the dominant), while the first voice goes on.', '다음 성부의 주제, 5도 위(딸림조)에서. 첫 성부는 계속 가요.']],
  ['counter', ['The countersubject: the tune the first voice plays against the answer, heard again with later entries.', '대주제: 첫 성부가 응답에 맞서 연주하는 선율. 뒤의 등장에서도 다시 들려요.']],
  ['exposition', ['The opening: every voice enters in turn with the subject or the answer.', '시작 부분: 모든 성부가 차례로 주제나 응답으로 들어와요.']],
  ['episode', ['A passage between entries, made from bits of the subject, often in sequence, that moves to new keys.', '등장 사이의 부분. 주제의 조각으로, 흔히 동형 진행하며 새 조로 가요.']],
  ['entry', ['Middle and final entries: the subject comes back in related keys, and at the end in the home key.', '중간 등장과 마지막 등장: 주제가 근친조들에서, 끝에는 집 조에서 다시 와요.']],
];
const FUG_TN = { subject: ['Subject', '주제'], answer: ['Answer', '응답'], counter: ['Countersubject', '대주제'], exposition: ['Exposition', '제시부'], episode: ['Episode', '에피소드'], entry: ['Final entry', '마지막 등장'] };
function FmxFuguePad() {
  const [term, setTerm] = useState('subject'), [beat, setBeat] = useState(-1), [quiz, setQuiz] = useState(null), [pickd, setPick] = useState(null);
  const T = useSpTimers(), END = 43;
  const play = () => { T.clear(); const ev = []; FUG_V.forEach(([, st, , P]) => { let a = st; P.forEach(([x, d]) => { ev.push({ at: a, keys: [x], len: d * 0.92, vol: 0.12 }); a += d; }); });
    const r = spPlay(ev, 96); if (!r) return; for (let b = 0; b <= END; b++) T.at(r.ms(b), () => setBeat(b)); T.at(r.ms(END) + 300, () => setBeat(-1)); };
  const ask = () => { T.clear(); setBeat(-1); let c, g = 0; do { c = pick(FUG_TERMS); } while (quiz && quiz.id === c[0] && g++ < 8); setQuiz({ id: c[0], clue: c[1] }); setPick(null); };
  const X = (b) => 52 + b / END * 336, lanes = [['sop', t('Top', '위')], ['alto', t('Middle', '가운데')], ['bass', t('Bass', '베이스')]];
  const svg = lanes.map(([v, lab], i) => '<text x="0" y="' + (22 + i * 30) + '" font-family="Inter, sans-serif" font-size="11" font-weight="800" fill="#6b6e9c">' + lab + '</text>' + FUG_V.filter(e => e[0] === v).map(([, st, kd, P]) => { const w = sonLen(P) / END * 336, c = FUG_KIND[kd][2], on = (kd === 'counter' && term === 'counter') || (kd === term) || (term === 'exposition' && st < 24) || (term === 'entry' && st === 32 && kd === 'subject');
    return '<rect x="' + (X(st) + 1).toFixed(1) + '" y="' + (10 + i * 30) + '" width="' + (w - 2).toFixed(1) + '" height="18" rx="4" fill="' + c + '" stroke="' + (on ? '#e4572e' : 'none') + '" stroke-width="2.4"' + (kd === 'free' || kd === 'episode' ? ' stroke-dasharray="' + (on ? '' : '3 3') + '"' : '') + '/>'; }).join('')).join('')
    + '<path d="M' + X(24) + ' 4 V96" stroke="#26296b" stroke-width="1" stroke-dasharray="2 3"/><text x="' + X(12) + '" y="104" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="900" fill="#26296b">' + t('EXPOSITION', '제시부') + '</text><text x="' + X(28) + '" y="104" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="900" fill="#26296b">' + t('EPISODE', '에피소드') + '</text><text x="' + X(36) + '" y="104" text-anchor="middle" font-family="Inter, sans-serif" font-size="10.5" font-weight="900" fill="#26296b">' + t('ENTRY', '등장') + '</text>'
    + (beat >= 0 ? '<path d="M' + X(beat).toFixed(1) + ' 4 V96" stroke="#e4572e" stroke-width="2"/>' : '');
  const def = FUG_TERMS.find(x => x[0] === term)[1];
  return (
    <div className="try-box" style={actBox} data-fmx="fugue">
      <div style={actTitle}>{t('The fugue', '푸가')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>한 선율(<b>주제</b>)로 짓는 곡. 성부(보통 셋이나 넷)가 차례로 같은 주제로 들어와 서로 얽혀요. 아래는 이 앱이 지은 세 성부 푸가의 시작: 가운데 → 위 → 베이스 순서로 들어와요.</> : <>A piece built from one tune, <b>the subject</b>. The voices (usually three or four) come in one after another with it and weave together. Below, the opening of a three-voice fugue written for this app: middle, then top, then bass.</>}</div>
      <svg viewBox="0 0 400 110" style={{width:'100%',maxWidth:440,display:'block',margin:'6px auto'}} role="img" aria-label={t('Three voices of a fugue', '푸가의 세 성부')} dangerouslySetInnerHTML={{ __html: svg }}/>
      {!quiz && spChips(Object.keys(FUG_TN).map(x => [x, t(FUG_TN[x][0], FUG_TN[x][1])]), term, setTerm)}
      {quiz ? <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:BK.ink,margin:'6px 0',textWrap:'balance'}}>{t(quiz.clue[0], quiz.clue[1])}</div>
        : <div style={{fontSize:14,color:BK.ink,lineHeight:1.45,margin:'2px 0 4px',textWrap:'pretty'}}><b>{t(FUG_TN[term][0], FUG_TN[term][1])}</b>: {t(def[0], def[1])}</div>}
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:6}}>{Object.keys(FUG_TN).map(id => <button key={id} className={'choice-btn' + (pickd == null ? '' : id === quiz.id ? ' good' : id === pickd ? ' bad' : '')} onClick={() => { if (pickd == null) setPick(id); }} style={{padding:'10px 4px',fontSize:14,fontWeight:900}}>{t(FUG_TN[id][0], FUG_TN[id][1])}</button>)}</div>}
      {quiz && pickd != null && spMsg(pickd === quiz.id ? t('Yes.', '맞아요.') : t('It was the ' + FUG_TN[quiz.id][0].toLowerCase() + '.', '정답은 ' + FUG_TN[quiz.id][1] + '.'), pickd === quiz.id ? BK.green : BK.coral)}
      {!quiz && <div style={{fontSize:13,fontWeight:800,color:BK.coral,textAlign:'center',marginTop:4}}>{t('Listen to: Bach, The Well-Tempered Clavier, Book 1, Fugue No. 2 in C minor (three voices)', '들어 볼 곡: 바흐, 평균율 클라비어 곡집 1권, 푸가 2번 C단조(세 성부)')}</div>}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hear the voices enter', '▶ 성부가 들어오는 소리')}</button>
        <button className="ghost-btn" style={spBtn} onClick={ask}>{quiz && pickd == null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(null); setPick(null); }}>{t('← Back', '← 돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── Melody: a melody that changes key. Four lines; lines 2 and 3 may travel to a related key; the new note shows the new key ──
const MOD_SC = { M: [0, 2, 4, 5, 7, 9, 11], m: [0, 2, 3, 5, 7, 8, 11] };   // the minor is the harmonic minor
const MOD_T = { open: [1, 3, 5, 8, 6, 4, 5], move: [3, 4, 5, 4, 2, 7, 1], home: [5, 6, 5, 4, 3, 2, 1] };   // 7 = the leading note below the tonic
const MOD_BASS = { open: [1, 1, 4, 5], move: [1, 4, 5, 1], home: [1, 4, 5, 1] };
const MOD_TO = [['home', 0, 'M', 'Stay home', '집에 머물기'], ['dom', 7, 'M', 'The dominant', '딸림조'], ['rel', 9, 'm', 'The relative minor', '나란한 단조'], ['sub', 5, 'M', 'The subdominant', '버금딸림조']];   // [id, semitones above home, mode]
const MOD_HOMES = { C: [0, 'C'], G: [7, 'G'], F: [5, 'F'], D: [2, 'D'] };
const modKeyName = (pc, mode) => (mode === 'M' ? H6_MAJ[spPc(pc)] + t(' major', '장조') : H6_MIN[spPc(pc)] + t(' minor', '단조'));
const modNote = (base, mode, dg) => base + (dg === 8 ? 12 : dg === 7 ? MOD_SC[mode][6] - 12 : MOD_SC[mode][dg - 1]);
const modLine = (kind, base, mode) => MOD_T[kind].map(dg => modNote(base, mode, dg));
const modHomeBase = (hk) => { const pc = MOD_HOMES[hk][0]; return pc > 4 ? pc - 12 : pc; };
const modRoute = (hk, r2, r3) => { const hb = modHomeBase(hk), hpc = MOD_HOMES[hk][0], H = { pc: hpc, mode: 'M', base: hb };
  const to = (id) => { const x = MOD_TO.find(y => y[0] === id); return { pc: hpc + x[1], mode: x[2], base: hb + x[1], id }; };
  return [{ ...H, kind: 'open', id: 'home' }, { ...to(r2), kind: 'move' }, { ...to(r3), kind: 'move' }, { ...H, kind: 'home', id: 'home' }].map(L => ({ ...L, notes: modLine(L.kind, L.base, L.mode), bass: MOD_BASS[L.kind].map(dg => spPc(L.pc + MOD_SC[L.mode][dg - 1]) - 24) })); };
const modInHome = (hk, x) => MOD_SC.M.includes(spPc(x - MOD_HOMES[hk][0]));
const modPlay = (lines, upto = 4) => { const ev = []; lines.slice(0, upto).forEach((L, i) => { L.notes.forEach((x, j) => ev.push({ at: i * 8 + j, keys: [x], len: j === 6 ? 1.9 : 0.92, vol: 0.15 })); L.bass.forEach((x, j) => ev.push({ at: i * 8 + j * 2, keys: [x], len: 1.9, vol: 0.1 })); }); return spPlay(ev, 100); };
const MOD_LET = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B'];
const modLetter = (L, x) => { const s = spPc(x - L.pc), dg = MOD_SC[L.mode].indexOf(s) + 1; return l6Spell(L.mode === 'M' ? H6_MAJ[spPc(L.pc)] : H6_MIN[spPc(L.pc)], s, dg || 1); };
function MlxModulatePad() {
  const [hk, setHk] = useState('C'), [r2, setR2] = useState('dom'), [r3, setR3] = useState('rel'), [now, setNow] = useState(-1), [quiz, setQuiz] = useState(null), [pickd, setPick] = useState(null);
  const T = useSpTimers(), lines = modRoute(hk, quiz ? quiz.r : r2, r3);
  const play = (upto = 4) => { T.clear(); const r = modPlay(lines, upto); if (!r) return; for (let i = 0; i < upto; i++) T.at(r.ms(i * 8), () => setNow(i)); T.at(r.ms(upto * 8) + 200, () => setNow(-1)); };
  const ask = () => { T.clear(); setNow(-1); let r, g = 0; do { r = pick(MOD_TO)[0]; } while (quiz && quiz.r === r && g++ < 8); setQuiz({ r }); setPick(null); const L = modRoute(hk, r, r3); setTimeout(() => { const rr = modPlay(L, 2); if (rr) { T.at(rr.ms(0), () => setNow(0)); T.at(rr.ms(8), () => setNow(1)); T.at(rr.ms(16) + 200, () => setNow(-1)); } }, 50); };
  const hide = quiz && pickd == null;
  const cycle = (i) => { if (quiz || (i !== 1 && i !== 2)) return; T.clear(); setNow(-1); const ids = MOD_TO.map(x => x[0]), nx = (v) => ids[(ids.indexOf(v) + 1) % ids.length]; if (i === 1) setR2(nx(r2)); else setR3(nx(r3)); };
  const row = (L, i) => { const hideRow = hide && i === 1, on = now === i, can = !quiz && (i === 1 || i === 2);
    return <div key={i} onClick={() => cycle(i)} role={can ? 'button' : undefined} data-mod-line={i + 1} style={{display:'flex',alignItems:'center',gap:6,padding:'5px 6px',borderRadius:8,cursor:can ? 'pointer' : 'default',border:'1.5px ' + (can ? 'dashed ' : 'solid ') + (on ? BK.coral : can ? 'rgba(38,41,107,0.35)' : 'rgba(38,41,107,0.14)'),background:on ? '#fbe3da' : '#fff'}}>
      <div style={{width:74,flex:'0 0 74px',lineHeight:1.15}}><div style={{fontSize:11,fontWeight:900,color:BK.muted}}>{t('Line ' + (i + 1), (i + 1) + '줄')}</div><div style={{fontSize:12.5,fontWeight:900,color:L.id === 'home' ? BK.ink : BK.coral}}>{hideRow ? '?' : modKeyName(L.pc, L.mode)}{can && <span style={{color:BK.muted,fontWeight:800}}> ↻</span>}</div></div>
      <div style={{display:'flex',gap:3,flexWrap:'wrap',flex:1,minWidth:0}}>{L.notes.map((x, j) => { const nw = !modInHome(hk, x); return <span key={j} style={{minWidth:24,padding:'2px 3px',borderRadius:5,textAlign:'center',fontSize:13,fontWeight:900,color:nw && !hideRow ? '#fff' : BK.ink,background:nw && !hideRow ? BK.coral : 'rgba(38,41,107,0.06)'}}>{hideRow ? '·' : modLetter(L, x)}</span>; })}</div></div>; };
  const newNote = (id) => { if (id === 'home') return null; const L = modRoute(hk, id, 'home')[1]; const nn = L.notes.find(x => !modInHome(hk, x)); return nn == null ? null : modLetter(L, nn); };
  return (
    <div className="try-box" style={actBox} data-mlx="modulate">
      <div style={actTitle}>{t('A melody that changes key', '조가 바뀌는 선율')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>6급: 네 줄 시에 <b>전조가 있는</b> 균형 잡힌 선율. 1줄은 집에서 시작해 쉼표처럼, 2·3줄은 <b>근친조로 여행</b>, 4줄은 집으로. 새 조는 <b>새 음 하나</b>로 알 수 있어요: 딸림조는 4음을 올리고(C장조 → G장조: F♯), 나란한 단조는 그 이끔음(G♯), 버금딸림조는 7음을 내려요(B♭). 산호색이 새 음.</>
        : <>Grade 6: a balanced melody for a four-line stanza, <b>with a modulation</b>. Line 1 starts at home and pauses like a comma; lines 2 and 3 <b>travel to related keys</b>; line 4 comes home. You can tell the new key by <b>one new note</b>: the dominant raises the 4th (C major → G major: F♯), the relative minor brings its leading note (G♯), the subdominant lowers the 7th (B♭). New notes are coral.</>}</div>
      {!quiz && spChips(Object.keys(MOD_HOMES).map(x => [x, MOD_HOMES[x][1] + t(' major', '장조')]), hk, (v) => { T.clear(); setHk(v); setNow(-1); })}
      {!quiz && <div style={{fontSize:12.5,fontWeight:800,color:BK.muted,textAlign:'center'}}>{t('Tap line 2 or 3 to send it to another key: home, the dominant, the relative minor, the subdominant.', '2줄이나 3줄을 누르면 다른 조로 가요: 집, 딸림조, 나란한 단조, 버금딸림조.')}</div>}
      <div style={{display:'grid',gap:4,margin:'6px 0'}}>{(quiz ? lines.slice(0, 2) : lines).map(row)}</div>
      {quiz && <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:BK.ink,margin:'4px 0'}}>{t('Where did line 2 go?', '2줄은 어디로 갔을까요?')}</div>}
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8}}>{MOD_TO.map(x => <button key={x[0]} className={'choice-btn' + (pickd == null ? '' : x[0] === quiz.r ? ' good' : x[0] === pickd ? ' bad' : '')} onClick={() => { if (pickd == null) setPick(x[0]); }} style={{padding:'10px 4px',fontSize:14,fontWeight:900}}>{t(x[3], x[4])}</button>)}</div>}
      {spMsg(quiz && pickd != null ? (pickd === quiz.r ? t('Yes', '맞아요') : t('It was ' + MOD_TO.find(x => x[0] === quiz.r)[3].toLowerCase(), '정답은 ' + MOD_TO.find(x => x[0] === quiz.r)[4])) + (newNote(quiz.r) ? t(': listen for ' + newNote(quiz.r) + '.', ': ' + newNote(quiz.r) + '을 들어 봐요.') : t(': no new note.', ': 새 음이 없어요.')) : !quiz ? (r2 === 'home' && r3 === 'home' ? t('No journey yet: send line 2 or 3 to a related key.', '아직 여행이 없어요: 2줄이나 3줄을 근친조로 보내요.') : t('Home, away' + (r3 !== 'home' && r2 !== 'home' ? ', further' : '') + ', and home: a melody with a modulation.', '집, 밖으로' + (r3 !== 'home' && r2 !== 'home' ? ', 더 멀리' : '') + ', 그리고 집: 전조가 있는 선율.')) : '', quiz && pickd != null ? (pickd === quiz.r ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => play(quiz ? 2 : 4)}>{quiz ? t('▶ Lines 1 and 2 again', '▶ 1, 2줄 다시') : t('▶ Play the four lines', '▶ 네 줄 듣기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={ask}>{quiz && pickd == null ? t('▶ Another', '▶ 다른 것') : t('▶ Where did it go?', '▶ 어디로 갔을까?')}</button>
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => { T.clear(); setQuiz(null); setPick(null); setNow(-1); }}>{t('← Back', '← 돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── Instruments: the brass of the orchestra (sounding ranges, approximate: semitones from middle C) ──
const SPR_BRASS = [
  { n: ['Horn in F', 'F 호른'], clef: ['treble clef, bass clef for low notes', '높은음자리표, 낮은 음은 낮은음자리표'], lo: -25, hi: 17, w: 5, tr: ['A transposing instrument: it sounds a perfect 5th lower than written. Its long tube is coiled round; the player\'s hand sits in the bell.', '이조 악기: 적힌 것보다 완전5도 낮게 소리 나요. 긴 관이 둥글게 감겨 있고, 연주자의 손이 벨 안에 있어요.'] },
  { n: ['Trumpet in B♭', 'B♭ 트럼펫'], clef: ['treble clef', '높은음자리표'], lo: -8, hi: 22, w: 2, tr: ['A transposing instrument: it sounds a tone (a major 2nd) lower than written. The highest of the brass.', '이조 악기: 적힌 것보다 온음(장2도) 낮게 소리 나요. 금관에서 가장 높아요.'] },
  { n: ['Tenor trombone', '테너 트롬본'], clef: ['bass clef, tenor clef for high notes', '낮은음자리표, 높은 음은 테너음자리표'], lo: -20, hi: 17, w: 0, tr: ['It sounds as written. A slide makes the tube longer or shorter: seven positions.', '적힌 대로 소리 나요. 슬라이드로 관을 늘이고 줄여요: 일곱 포지션.'] },
  { n: ['Tuba in F', 'F 튜바'], clef: ['bass clef', '낮은음자리표'], lo: -31, hi: 5, w: 0, tr: ['Written at the pitch it sounds, in bass clef. The bass of the brass.', '소리 나는 음 그대로, 낮은음자리표로 적어요. 금관의 베이스.'] },
];
function SprBrassPad() {
  const [i, setI] = useState(0), [quiz, setQuiz] = useState(null), [pickd, setPick] = useState(null);
  const v = SPR_BRASS[quiz ? quiz.i : i], hide = quiz && pickd == null;
  const ask = () => { let j, g = 0; do { j = Math.floor(Math.random() * SPR_BRASS.length); } while (quiz && quiz.i === j && g++ < 8); setQuiz({ i: j }); setPick(null); sprWindPlay(SPR_BRASS[j]); };
  const wr = () => spPlay([{ at: 0, keys: [12 - v.w], len: 1.4, vol: 0.16 }], 72);
  return (
    <div className="try-box" style={actBox} data-spr="brass">
      <div style={actTitle}>{t('The brass', '금관 악기')}</div>
      <div style={actNote}>{t('The brass of the orchestra: horn in F, trumpet in B♭, tenor trombone and tuba. You buzz your lips into a cup-shaped mouthpiece; valves, or the trombone\'s slide, change the length of the tube. Each one\'s range (the notes it sounds) is lit on the whole keyboard, with the clef it reads.', '오케스트라의 금관 악기: F 호른, B♭ 트럼펫, 테너 트롬본, 튜바. 컵 모양 마우스피스에 입술을 떨어 소리 내고; 밸브나 트롬본의 슬라이드로 관의 길이를 바꿔요. 악기마다 음역(소리 나는 음)을 건반 전체 위에 밝히고, 읽는 음자리표도 함께.')}</div>
      {!quiz && spChips(SPR_BRASS.map((x, j) => [j, t(x.n[0], x.n[1])]), i, (j) => { setI(j); sprWindPlay(SPR_BRASS[j]); })}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 0'}}>{hide ? t('Which instrument?', '어느 악기일까요?') : t(v.n[0], v.n[1]) + ' · ' + t(v.clef[0], v.clef[1])}</div>
      <SprWindRange v={v}/>
      <div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.coral,marginTop:4}}>{t('About ', '약 ') + sprWNote(v.lo) + ' – ' + sprWNote(v.hi) + t(' (sounding)', '(소리 나는 음)')}</div>
      {quiz ? <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{SPR_BRASS.map((x, j) => <button key={j} className={'choice-btn' + (pickd == null ? '' : j === quiz.i ? ' good' : j === pickd ? ' bad' : '')} onClick={() => { if (pickd == null) setPick(j); }} style={{padding:'11px 4px',fontSize:14.5,fontWeight:900}}>{t(x.n[0], x.n[1])}</button>)}</div> : null}
      {spMsg(hide ? t(v.clef[0][0].toUpperCase() + v.clef[0].slice(1) + '. ' + v.tr[0].split('. ')[0].replace(/\.?$/, '.'), v.clef[1] + '. ' + v.tr[1].split('. ')[0].replace(/\.?$/, '.')) : t(v.tr[0], v.tr[1]), quiz && !hide ? (pickd === quiz.i ? BK.green : BK.coral) : undefined)}
      {!hide && v.w > 0 && <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted,marginTop:4}}>{t('Written C5 sounds ' + sprWNote(12 - v.w) + '.', '적힌 C5는 ' + sprWNote(12 - v.w) + '로 소리 나요.')}</div>}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => sprWindPlay(v)}>{t('▶ Low, middle, high', '▶ 낮은, 가운데, 높은 음')}</button>
        {!hide && v.w > 0 && <button className="ghost-btn" style={spBtn} onClick={wr}>{t('▶ What written C5 sounds', '▶ 적힌 C5의 소리')}</button>}
        <button className="ghost-btn" style={spBtn} onClick={ask}>{quiz && pickd == null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(null); setPick(null); }}>{t('← Back', '← 돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── Styles: sonata, symphony, concerto, overture: who plays, the plan of the movements, and examples ──
const CSX6 = [
  { id: 'sonata', en: 'Sonata', ko: '소나타', who: ['A solo instrument, or an instrument and piano', '독주 악기 하나, 또는 악기와 피아노'], mv: [['f', 'Fast', '빠르게', 'sonata form'], ['s', 'Slow', '느리게'], ['f', 'Fast', '빠르게', 'often a rondo']],
    say: ['A piece in several movements, usually three (fast, slow, fast), for one player or two. Its first movement is usually in sonata form.', '여러 악장으로 된 곡, 보통 셋(빠르게, 느리게, 빠르게). 한두 명이 연주해요. 첫 악장은 보통 소나타 형식.'],
    ex: ['Mozart: Piano Sonata in C major, K. 545 · Beethoven: Sonata in C minor, Op. 13 ("Pathétique")', '모차르트: 피아노 소나타 C장조 K. 545 · 베토벤: 소나타 C단조 Op. 13("비창")'] },
  { id: 'symphony', en: 'Symphony', ko: '교향곡', who: ['The orchestra', '오케스트라'], mv: [['f', 'Fast', '빠르게', 'sonata form'], ['s', 'Slow', '느리게'], ['m', 'Minuet or scherzo', '미뉴에트나 스케르초'], ['f', 'Fast', '빠르게']],
    say: ['A sonata for orchestra, usually in four movements: the third a minuet and trio (Haydn, Mozart) or a scherzo (Beethoven).', '오케스트라를 위한 소나타. 보통 네 악장: 셋째는 미뉴에트와 트리오(하이든, 모차르트)나 스케르초(베토벤).'],
    ex: ['Haydn: Symphony No. 94 ("Surprise") · Beethoven: Symphony No. 5 in C minor', '하이든: 교향곡 94번("놀람") · 베토벤: 교향곡 5번 C단조'] },
  { id: 'concerto', en: 'Concerto', ko: '협주곡', who: ['A soloist with the orchestra', '독주자와 오케스트라'], mv: [['f', 'Fast', '빠르게', 'with a cadenza'], ['s', 'Slow', '느리게'], ['f', 'Fast', '빠르게']],
    say: ['A soloist with (and against) the orchestra, usually in three movements. Near the end of the first movement the orchestra stops and the soloist plays a cadenza alone.', '독주자가 오케스트라와 함께(또 맞서) 연주해요. 보통 세 악장. 첫 악장 끝 무렵 오케스트라가 멈추고 독주자가 혼자 카덴차를 연주해요.'],
    ex: ['Mozart: Piano Concerto No. 23 in A major, K. 488 · Beethoven: Piano Concerto No. 5 ("Emperor")', '모차르트: 피아노 협주곡 23번 A장조 K. 488 · 베토벤: 피아노 협주곡 5번("황제")'] },
  { id: 'overture', en: 'Overture', ko: '서곡', who: ['The orchestra', '오케스트라'], mv: [['s', 'Slow, dotted', '느리게, 점음표'], ['f', 'Fast, voices entering in turn', '빠르게, 성부가 차례로']],
    say: ['The orchestral piece that opens an opera, oratorio or play. Handel\'s are French overtures: slow and grand with dotted rhythms, then fast, the voices coming in one after another. Later there were concert overtures, single pieces for the concert hall.', '오페라, 오라토리오, 연극을 여는 관현악곡. 헨델의 서곡은 프랑스풍 서곡: 점음표 리듬으로 느리고 웅장하게, 그다음 성부가 차례로 들어오며 빠르게. 뒤에는 연주회장을 위한 한 곡짜리 연주회용 서곡도 나왔어요.'],
    ex: ['Handel: Overture to Messiah · Mozart: Overture to The Marriage of Figaro · Mendelssohn: The Hebrides (a concert overture)', '헨델: 메시아 서곡 · 모차르트: 피가로의 결혼 서곡 · 멘델스존: 헤브리디스(연주회용 서곡)'] },
];
const CSX6_CLUE = [['sonata', ['Three movements for a pianist, or a violinist and a pianist.', '피아니스트 한 명, 또는 바이올리니스트와 피아니스트를 위한 세 악장.']], ['symphony', ['Four movements for the whole orchestra; the third is a minuet or a scherzo.', '오케스트라 전체를 위한 네 악장; 셋째는 미뉴에트나 스케르초.']],
  ['concerto', ['A soloist and the orchestra; a cadenza near the end of the first movement.', '독주자와 오케스트라; 첫 악장 끝 무렵의 카덴차.']], ['overture', ['It opens an opera or an oratorio.', '오페라나 오라토리오의 막을 열어요.']]];
const CSX6_MOT = [0, 4, 7, 4, 5, 2, -1, 0];
const csx6Play = (g) => { const ev = []; let at = 0; const bpmOf = { f: 150, s: 60, m: 120 };
  g.mv.forEach(([k]) => { const sc = bpmOf[k] / 150, step = k === 's' ? 1.6 : k === 'm' ? 0.8 : 0.5, dot = g.id === 'overture' && k === 's';
    CSX6_MOT.forEach((x, j) => { const d = dot ? (j % 2 ? 0.4 : 1.2) : step; ev.push({ at, keys: [x + (k === 's' ? 0 : 12), x - 12], len: d * 0.9, vol: 0.13 }); at += d; }); at += 1; });
  return spPlay(ev, 150); };
function CsxGenresPad() {
  const [i, setI] = useState(0), [quiz, setQuiz] = useState(null), [pickd, setPick] = useState(null);
  const g = CSX6[quiz ? CSX6.findIndex(x => x.id === quiz.id) : i], hide = quiz && pickd == null;
  const ask = () => { let c, gg = 0; do { c = pick(CSX6_CLUE); } while (quiz && quiz.id === c[0] && gg++ < 8); setQuiz({ id: c[0], clue: c[1] }); setPick(null); };
  return (
    <div className="try-box" style={actBox} data-csx="genres">
      <div style={actTitle}>{t('Sonata, symphony, concerto, overture', '소나타, 교향곡, 협주곡, 서곡')}</div>
      <div style={actNote}>{t('Four kinds of piece from the great composers: who plays, and the plan of the movements (fast, slow, dance).', '위대한 작곡가들의 네 가지 곡: 누가 연주하는지, 그리고 악장의 설계(빠르게, 느리게, 춤곡).')}</div>
      {!quiz && spChips(CSX6.map((x, j) => [j, t(x.en, x.ko)]), i, setI)}
      {quiz && <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:BK.ink,margin:'4px 0',textWrap:'balance'}}>{t(quiz.clue[0], quiz.clue[1])}</div>}
      {!hide && <><div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:24,fontWeight:900,color:BK.ink,margin:'4px 0 0'}}>{t(g.en, g.ko)}</div>
        <div style={{textAlign:'center',fontSize:13,fontWeight:800,color:BK.muted}}>{t(g.who[0], g.who[1])}</div>
        <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap',margin:'6px 0'}}>{g.mv.map(([k, en, ko, note], j) => <div key={j} style={{minWidth:64,padding:'5px 7px',borderRadius:8,textAlign:'center',border:'1.5px solid ' + (k === 'f' ? BK.ink : 'rgba(38,41,107,0.35)'),background:k === 'f' ? 'rgba(38,41,107,0.07)' : '#fff'}}>
          <div style={{fontSize:10.5,fontWeight:900,color:BK.muted}}>{['I', 'II', 'III', 'IV'][j]}</div><div style={{fontSize:12.5,fontWeight:900,color:k === 's' ? BK.coral : BK.ink,lineHeight:1.15}}>{t(en, ko)}</div>{note && <div style={{fontSize:10.5,fontWeight:700,color:BK.muted}}>{t(note, note === 'sonata form' ? '소나타 형식' : note === 'often a rondo' ? '흔히 론도' : '카덴차와 함께')}</div>}</div>)}</div>
        <div style={{fontSize:14,color:BK.ink,lineHeight:1.45,margin:'2px 0 6px',textWrap:'pretty'}}>{t(g.say[0], g.say[1])}</div>
        <div style={{fontSize:13,fontWeight:800,color:BK.coral,textAlign:'center'}}>{t('Listen to: ', '들어 볼 곡: ') + t(g.ex[0], g.ex[1])}</div></>}
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{CSX6.map(x => <button key={x.id} className={'choice-btn' + (pickd == null ? '' : x.id === quiz.id ? ' good' : x.id === pickd ? ' bad' : '')} onClick={() => { if (pickd == null) setPick(x.id); }} style={{padding:'11px 4px',fontSize:14.5,fontWeight:900}}>{t(x.en, x.ko)}</button>)}</div>}
      {quiz && pickd != null && spMsg(pickd === quiz.id ? t('Yes.', '맞아요.') : t('It was the ' + g.en.toLowerCase() + '.', '정답은 ' + g.ko + '.'), pickd === quiz.id ? BK.green : BK.coral)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!hide && <button className="ghost-btn" style={spBtn} onClick={() => csx6Play(g)}>{t('▶ Hear the plan', '▶ 설계 듣기')}</button>}
        <button className="ghost-btn" style={spBtn} onClick={ask}>{quiz && pickd == null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(null); setPick(null); }}>{t('← All four', '← 네 가지 모두')}</button>}
      </div>
    </div>
  );
}
TOOLS.push({ id: 'fmx-sonata', ch: 'form', title: 'Sonata form', blurb: 'Exposition, development, recapitulation: a tiny movement to hear, part by part.', C: () => <FmxSonataPad/> },
  { id: 'fmx-fugue', ch: 'form', title: 'The fugue', blurb: 'Subject, answer, countersubject: three voices come in one after another.', C: () => <FmxFuguePad/> },
  { id: 'mlx-modulate', ch: 'melody', title: 'A melody that changes key', blurb: 'Four lines: send lines 2 and 3 to related keys; one new note shows the new key.', C: () => <MlxModulatePad/> },
  { id: 'spr-brass', ch: 'pitch-range', title: 'The brass', blurb: 'Horn in F, trumpet in B♭, tenor trombone, tuba: their ranges and clefs.', C: () => <SprBrassPad/> },
  { id: 'csx-genres', ch: 'styles', title: 'Sonata, symphony, concerto, overture', blurb: 'Who plays, the plan of the movements, and pieces to hear.', C: () => <CsxGenresPad/> });
lbhRetitle('fmx-sonata', 'Sonata form', '소나타 형식', 'Exposition, development, recapitulation: a tiny movement to hear, part by part.', '제시부, 발전부, 재현부: 작은 악장을 부분마다 들어요.');
lbhRetitle('fmx-fugue', 'The fugue', '푸가', 'Subject, answer, countersubject: three voices come in one after another.', '주제, 응답, 대주제: 세 성부가 차례로 들어와요.');
lbhRetitle('mlx-modulate', 'A melody that changes key', '조가 바뀌는 선율', 'Four lines: send lines 2 and 3 to related keys; one new note shows the new key.', '네 줄: 2줄과 3줄을 근친조로 보내요; 새 음 하나가 새 조를 알려 줘요.');
lbhRetitle('spr-brass', 'The brass', '금관 악기', 'Horn in F, trumpet in B♭, tenor trombone, tuba: their ranges and clefs.', 'F 호른, B♭ 트럼펫, 테너 트롬본, 튜바: 음역과 음자리표.');
lbhRetitle('csx-genres', 'Sonata, symphony, concerto, overture', '소나타, 교향곡, 협주곡, 서곡', 'Who plays, the plan of the movements, and pieces to hear.', '누가 연주하는지, 악장의 설계, 그리고 들어 볼 곡.');
Object.assign(TOOL_META, { 'fmx-sonata': ['melody', 3, 3, 'show ear'], 'fmx-fugue': ['melody', 3, 3, 'show ear'], 'mlx-modulate': ['melody', 3, 3, 'make ear'], 'spr-brass': ['about', 0, 3, 'show ear'], 'csx-genres': ['about', 0, 3, 'show ear'] });
Object.assign(TOOL_CONCEPT, { 'fmx-sonata': 'c-map', 'fmx-fugue': 'c-map', 'mlx-modulate': 'c-map', 'spr-brass': 'about', 'csx-genres': 'about' });
'''
rep("""Object.assign(TOOL_CONCEPT, { 'mlx-stanza': 'c-map', 'fmx-forms5': 'c-map', 'spr-wind': 'about' });""",
    """Object.assign(TOOL_CONCEPT, { 'mlx-stanza': 'c-map', 'fmx-forms5': 'c-map', 'spr-wind': 'about' });""" + CODE)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
