import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BE (board call 23): the three Grade 5 lessons in rooms that already exist. Theory of Music Grade 5 (Manual of Syllabuses
# 2026): Creative Work, a melody in a major or minor key up to three sharps or flats to a four-line stanza, the words under the
# notes, phrase marks, modulation optional (Melody); General Knowledge (a), Minuet and Trio, Scherzo, Air with variations,
# Recitative and Aria (Form); (b) the woodwinds of the symphony orchestra, their ranges and clefs (Stories of music, Pitch and
# range). The stanzas are new, written for the room by the rule the couplets keep (important words strong, small words weak).

rep("""  Dm: { t: 29, n: 1, s: 'flat', en: 'D minor', ko: 'D단조', minor: true }, Gm: { t: 32, n: 2, s: 'flat', en: 'G minor', ko: 'G단조', minor: true },   // Build AY: harmonic minor
};""", """  Dm: { t: 29, n: 1, s: 'flat', en: 'D minor', ko: 'D단조', minor: true }, Gm: { t: 32, n: 2, s: 'flat', en: 'G minor', ko: 'G단조', minor: true },   // Build AY: harmonic minor
  A: { t: 33, n: 3, s: 'sharp', en: 'A major', ko: 'A장조' }, Eb: { t: 30, n: 3, s: 'flat', en: 'E♭ major', ko: 'E♭장조' },   // Build BE: three sharps or flats (Grade 5)
  Fsm: { t: 31, n: 3, s: 'sharp', en: 'F♯ minor', ko: 'F♯단조', minor: true }, Cm: { t: 28, n: 3, s: 'flat', en: 'C minor', ko: 'C단조', minor: true },
};""")

CODE = r'''
// ─── Build BE: a melody for a four-line stanza (Grade 5) ───
const MW_STZ = [
  { id: 'garden', m: 2, l: ['^Sun-light ^warms the ^gar-den ^wall,', '^Ro-ses ^climb and ^ros-es ^fall,', '^Swal-lows ^dart a-^cross the ^sky,', '^Sum-mer ^clouds go ^float-ing ^high.'],
    model: [1, 2, 3, 1, 5, 4, 3, 4, 5, 6, 5, 4, 3, 2, 5, 6, 5, 4, 3, 4, 5, 6, 5, 4, 3, 2, 2, 1] },
  { id: 'river', m: 3, l: ['^Down by the ^riv-er the ^wil-lows are ^green,', '^Ducks in a ^row on the ^wa-ter are ^seen,', '^Sun-set is ^paint-ing the ^sky in the ^west,', '^Swal-lows fly ^home to their ^nests for a ^rest.'],
    model: [1, 2, 3, 4, 3, 2, 3, 4, 5, 3, 4, 5, 6, 5, 4, 3, 2, 3, 4, 5, 6, 5, 4, 3, 4, 5, 6, 5, 4, 2, 3, 4, 5, 4, 3, 2, 3, 2, 2, 1] },
  { id: 'fox', m: 2, l: ['A ^fox is ^run-ning ^home to ^bed,', 'His ^tail is ^bright, his ^coat is ^red,', 'The ^moon looks ^down on ^field and ^hill,', 'The ^wood is ^dark, the ^night is ^still.'],
    model: [1, 3, 2, 3, 4, 5, 4, 3, 3, 4, 5, 4, 3, 2, 3, 2, 3, 5, 4, 5, 6, 5, 4, 5, 5, 6, 5, 4, 3, 2, 2, 1] },
];
const MW_STZ_R = {};
MW_STZ.forEach(P => { const L = P.l.map(mwSyl), syls = L.flat(), set = mwSet(syls, P.m, mwStarts(syls), { per: 99 }); if (!set) return;
  const ends = []; let acc = 0; L.forEach(x => { acc += x.length; ends.push(acc - 1); });   // the last syllable of each line
  const barOf = []; let si = 0; set.rhy.forEach((bar, b) => bar.forEach(kk => { for (let u = 0; u < (kk === 'p' ? 2 : 1); u++) barOf[si++] = b; }));
  const nB = set.rhy.length, lb = ends.map(e => barOf[e]), lines = lb.map((b, i) => [i === 0 ? 0 : lb[i - 1] + 1, i === 3 ? nB - 1 : b]);
  MW_STZ_R[P.id] = { id: 's-' + P.id, m: P.m, bars: set.rhy, ana: set.a || 0, lines, ends, phr: ends.map((e, i) => [i === 0 ? 0 : ends[i - 1] + 1, e]), words: syls.map(mwTx), model: P.model }; });
const MW_STZ_IDS = MW_STZ.map(p => p.id).filter(id => MW_STZ_R[id] && MW_STZ_R[id].model.length === MW_STZ_R[id].words.length);
const MW_KEY_MAJ5 = ['C', 'G', 'D', 'A', 'F', 'Bb', 'Eb'], MW_KEY_MIN5 = ['Am', 'Em', 'Bm', 'Fsm', 'Dm', 'Gm', 'Cm'];
function mwRulesS(notes, R, k, phr) {
  const n = notes.length, deg = (d) => mwDeg(d, k), filled = notes.filter(d => d != null).length, moves = [];
  for (let i = 1; i < n; i++) if (notes[i] != null && notes[i - 1] != null) moves.push(Math.abs(notes[i] - notes[i - 1]));
  const steps = moves.filter(m => m <= 1).length, mids = R.ends.slice(0, 3).map(e => notes[e]);
  return [
    ['start', notes[0] == null ? null : [1, 3, 5].includes(deg(notes[0]))],
    ['steps', filled < n ? (moves.length >= 10 && steps * 2 < moves.length ? false : null) : steps * 2 >= moves.length],
    ['mid', mids.some(d => d == null) ? (mids.some(d => d != null && deg(d) === 1) ? false : null) : mids.every(d => deg(d) !== 1)],
    ['end', notes[n - 1] == null ? null : deg(notes[n - 1]) === 1],
    ['phr', phr === 'lines' ? true : null],
  ];
}
const MW_RULE_S = { start: MW_RULE_W.start, steps: MW_RULE_W.steps, mid: ['Lines 1, 2 and 3 end away from the tonic', '1, 2, 3줄은 으뜸음이 아닌 음에서 끝나요'], end: ['Line 4 ends on the tonic', '4줄은 으뜸음에서 끝나요'], phr: ['A phrase mark over each line', '줄마다 프레이즈 표시'] };
const mwStzChip = (id) => mwPlain(MW_STZ.find(p => p.id === id).l[0]).split(' ').slice(0, 3).join(' ').replace(/[,.]/g, '') + '…';
function MwStanzaPad() {
  const [pid, setPid] = useState(MW_STZ_IDS[0]), [k, setK] = useState('D'), R = MW_STZ_R[pid], slots = mwSlots(R), last = slots.length - 1;
  const [notes, setNotes] = useState(() => Array(mwSlots(MW_STZ_R[MW_STZ_IDS[0]]).length).fill(null)), [cur, setCur] = useState(0), [phr, setPhr] = useState(null), [lit, setLit] = useState(-1), [msg, setMsg] = useState(null);
  const T = useSpTimers(), K = MW_KEYS[k];
  const chooseP = (id) => { T.clear(); setPid(id); setNotes(Array(mwSlots(MW_STZ_R[id]).length).fill(null)); setCur(0); setPhr(null); setLit(-1); setMsg(null); };
  const chooseK = (x) => { T.clear(); const sh = MW_KEYS[x].t - K.t; setK(x); setNotes(notes.map(d => d == null || d + sh < MW_LO || d + sh > MW_HI ? null : d + sh)); setLit(-1); setMsg(null); };
  const tap = (semi) => { T.clear(); setLit(-1); spPlay([{ keys: [semi], at: 0, len: 0.8 }], 120);
    const d = mwDOf(semi, k); if (d == null) { const nm = MW_SEMI_NM[((semi % 12) + 12) % 12]; setMsg(K.minor ? t(nm + ' is not in ' + K.en + ' (the harmonic minor: its 7th is raised). Use the named keys.', nm + '은(는) ' + K.ko + '(화성 단음계: 7음을 올려요)의 음이 아니에요. 이름이 적힌 건반을 써요.') : t(nm + ' is not in ' + K.en + '. Use the named keys.', nm + '은(는) ' + K.ko + '의 음이 아니에요. 이름이 적힌 건반을 써요.')); return; }
    const nx = notes.slice(); nx[cur] = d; setNotes(nx); setMsg(null);
    let j = cur + 1; while (j <= last && nx[j] != null) j++; setCur(j <= last ? j : Math.min(cur + 1, last)); };
  const back = () => { T.clear(); const j = notes[cur] != null ? cur : Math.max(0, cur - 1), nx = notes.slice(); nx[j] = null; setNotes(nx); setCur(j); setMsg(null); };
  const play = () => { T.clear(); const ev = slots.map((s, i) => notes[i] == null ? null : { keys: [mwSemi(notes[i], k)], at: mwBarAt(R, s.b) + s.at, len: s.len }).filter(Boolean); if (!ev.length) return;
    const r = spPlay(ev, 96, R.m); if (!r) return; const endB = Math.max(...slots.map(s => mwBarAt(R, s.b) + s.at + s.len));
    slots.forEach((s, i) => { if (notes[i] != null) T.at(r.ms(mwBarAt(R, s.b) + s.at), () => setLit(i)); }); T.at(r.ms(endB) + 150, () => setLit(-1)); };
  const rules = mwRulesS(notes, R, k, phr), allOk = notes.every(d => d != null) && rules.every(([, v]) => v === true);
  const names = {}, litK = {}; for (let d = MW_LO; d <= MW_HI; d++) { const sm = mwSemi(d, k); names[sm] = mwName(d, k); if (mwDeg(d, k) === 1) litK[sm] = 'pale'; }
  if (lit >= 0 && notes[lit] != null) litK[mwSemi(notes[lit], k)] = 'cor';
  return (
    <div className="try-box" style={actBox} data-mw="stanza">
      <div style={actTitle}>{t('A melody for a four-line stanza', '네 줄 시에 선율 붙이기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>5급: 네 줄의 시. 가사가 리듬을 정해요(센 음절마다 마디줄). <b>음절마다 음 하나</b>, 샵이나 플랫 세 개까지의 장조나 단조로. 가사는 음표 아래. <b>1, 2, 3줄은 으뜸음이 아닌 음에서 쉬고, 4줄이 집으로</b> 돌아와요. 줄마다 프레이즈 표시. 전조는 해도 되고 안 해도 돼요.</>
        : <>Grade 5: a stanza of four lines. The words set the rhythm (a bar line before each strong syllable). Write <b>a note for every syllable</b>, in a major or minor key up to three sharps or flats; the words sit under the notes. <b>Lines 1 to 3 rest away from the tonic; line 4 comes home.</b> A phrase mark over each line. A modulation is allowed, not needed.</>}</div>
      {spChips(MW_STZ_IDS.map(id => [id, mwStzChip(id)]), pid, chooseP)}
      {spChips(MW_KEY_MAJ5.map(x => [x, t(MW_KEYS[x].en, MW_KEYS[x].ko)]), k, chooseK)}
      {spChips(MW_KEY_MIN5.map(x => [x, t(MW_KEYS[x].en, MW_KEYS[x].ko)]), k, chooseK)}
      <MwStaff k={k} rh={R} notes={notes} cur={cur} lit={lit} phr={phr} words={R.words} sp={1.3} onSlot={(i) => { setCur(i); setMsg(null); }} per={mlxPer() === 2 ? 2 : 4} label={t('A sixteen-bar melody with the words under the notes.', '음표 아래에 가사가 있는 16마디 선율.')}/>
      <div style={{margin:'6px 0 4px'}}><SpKb lo={0} hi={19} names={names} lit={litK} onTap={tap} label={t('Piano keys: the notes of ' + K.en + ' are named; the tonic is coral.', '피아노 건반: ' + K.ko + '의 음에 이름이 있고, 으뜸음은 산호색이에요.')}/></div>
      {msg ? spMsg(msg, BK.coral) : allOk ? spMsg(t('Four lines, one journey home: a melody for the stanza. ▶ Play it, then sing it.', '네 줄, 집으로 가는 한 길: 시에 붙인 선율이에요. ▶ 치고, 노래해 봐요.'), BK.green) : null}
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'6px 0'}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Play', '▶ 듣기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={back}>{t('⌫ Back', '⌫ 지우기')}</button>
        <button className="ghost-btn" style={spBtn} data-mw-phr onClick={() => setPhr(phr === null ? 'lines' : null)}>{t('Phrase marks: ', '프레이즈 표시: ') + (phr ? t('one a line', '줄마다') : t('none', '없음'))}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => { T.clear(); setNotes(R.model.map(dg => K.t + dg - 1)); setPhr('lines'); setCur(last); setMsg(null); }}>{t('An example', '보기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => chooseP(pid)}>{t('Clear', '모두 지우기')}</button>
      </div>
      <div style={{display:'grid',gap:3,maxWidth:440,margin:'4px auto 0'}} data-mw-rules>
        {rules.map(([id, v]) => <div key={id} data-mw-rule={id + ':' + v} style={{display:'flex',gap:8,alignItems:'baseline',fontSize:14,fontWeight:800,color:v === true ? BK.green : v === false ? BK.coral : BK.muted}}>
          <span style={{width:16,flex:'0 0 16px',textAlign:'center',fontWeight:900}}>{v === true ? '✓' : v === false ? '✗' : '○'}</span><span>{t(MW_RULE_S[id][0], MW_RULE_S[id][1])}</span></div>)}
      </div>
    </div>
  );
}
'''
rep("""// ── the drill: the strong syllables (the online exam's way: pick the right marks)""", CODE + """
// ── the drill: the strong syllables (the online exam's way: pick the right marks)""")

STORIES = r'''
// ══ Build BE: Grade 5 general knowledge: four forms (Form); the woodwinds, their ranges and clefs (Stories of music) ══
const FMX5 = [
  { id: 'minuet', en: 'Minuet and trio', ko: '미뉴에트와 트리오', boxes: [['Minuet', '미뉴에트', 'A'], ['Trio', '트리오', 'B'], ['Minuet', '미뉴에트', 'A']],
    say: ['A dance in 3/4 at a moderate speed. The minuet (A) is in binary form, each half repeated; the trio (B) is a second minuet, often lighter and quieter (it was once played by three instruments); then the minuet again, da capo, usually without its repeats. Often the third movement of a Classical symphony, sonata or string quartet.', '3/4박자의 보통 빠르기 춤곡. 미뉴에트(A)는 2부 형식, 반씩 되풀이; 트리오(B)는 또 하나의 미뉴에트, 흔히 더 가볍고 조용해요(예전에는 악기 셋이 연주했어요); 그다음 미뉴에트를 다시, 다 카포로, 대개 되풀이 없이. 고전 교향곡, 소나타, 현악 4중주의 셋째 악장인 경우가 많아요.'],
    ex: ['Mozart: Eine kleine Nachtmusik, K. 525, third movement', '모차르트: 아이네 클라이네 나흐트무지크 K. 525, 셋째 악장'] },
  { id: 'scherzo', en: 'Scherzo', ko: '스케르초', boxes: [['Scherzo', '스케르초', 'A'], ['Trio', '트리오', 'B'], ['Scherzo', '스케르초', 'A']],
    say: ['Italian for "joke": quick and lively, in 3/4 but often felt one in a bar. Beethoven put it in the minuet\'s place in his symphonies, with a trio in the middle: scherzo, trio, scherzo.', '이탈리아어로 "농담": 빠르고 활기차게, 3/4박자지만 흔히 한 마디를 한 박으로 느껴요. 베토벤은 교향곡에서 미뉴에트 자리에 두었고, 가운데에 트리오: 스케르초, 트리오, 스케르초.'],
    ex: ['Beethoven: Symphony No. 3 ("Eroica"), third movement', '베토벤: 교향곡 3번("영웅"), 셋째 악장'] },
  { id: 'air', en: 'Air with variations', ko: '주제와 변주', boxes: [['Air', '주제', 'A'], ['Var. 1', '변주 1', 'A¹'], ['Var. 2', '변주 2', 'A²'], ['Var. 3', '변주 3', 'A³']],
    say: ['An air (the theme), then variations: each keeps the theme you can still recognise, and changes something: its rhythm, its decoration, its harmony, its key (major to minor) or its texture.', '주제(에어) 다음에 변주들: 변주마다 알아볼 수 있는 주제를 지키면서 무언가를 바꿔요: 리듬, 꾸밈, 화성, 조(장조에서 단조로), 또는 짜임새.'],
    ex: ['Handel: "The Harmonious Blacksmith" (Air and variations, Suite No. 5 in E major) · Mozart: Variations on "Ah vous dirai-je, maman", K. 265', '헨델: "유쾌한 대장장이"(주제와 변주, 모음곡 5번 E장조) · 모차르트: "아, 어머니께 말씀드리죠" 변주곡 K. 265'] },
  { id: 'recit', en: 'Recitative and aria', ko: '레치타티보와 아리아', boxes: [['Recitative', '레치타티보', 'R'], ['Aria', '아리아', 'A'], ['', '', 'B'], ['', '', 'A']],
    say: ['From opera, oratorio and cantata. The recitative tells the story: sung speech in the rhythm of the words, few repeats, a light accompaniment (often just harpsichord and cello). The aria shows a character\'s feelings: a shaped melody, words repeated, a fuller accompaniment; in Handel often da capo, A B A.', '오페라, 오라토리오, 칸타타에서. 레치타티보는 이야기를 들려줘요: 낱말의 리듬으로 노래하는 말, 되풀이가 적고, 가벼운 반주(흔히 하프시코드와 첼로만). 아리아는 인물의 마음을 보여 줘요: 모양 있는 선율, 되풀이되는 가사, 더 풍성한 반주; 헨델에서는 흔히 다 카포, A B A.'],
    ex: ['Handel: Messiah, "Comfort ye" (recitative) and "Ev\'ry valley" (aria) · Mozart: The Marriage of Figaro', '헨델: 메시아, "위로하라"(레치타티보)와 "골짜기마다"(아리아) · 모차르트: 피가로의 결혼'] },
];
const FMX5_CLUE = [['minuet', ['A stately dance in 3/4; a second dance in the middle; then the first again, da capo.', '3/4박자의 우아한 춤곡; 가운데에 둘째 춤곡; 그다음 첫째를 다시, 다 카포.']],
  ['scherzo', ['Italian for "joke": quick, felt one in a bar; Beethoven put it in the minuet\'s place.', '이탈리아어로 "농담": 빠르고, 한 마디를 한 박으로; 베토벤이 미뉴에트 자리에 두었어요.']],
  ['air', ['A theme, then the same theme changed again and again: rhythm, decoration, key.', '주제, 그다음 같은 주제를 거듭 바꿔요: 리듬, 꾸밈, 조.']],
  ['recit', ['Sung speech tells the story; then a song shows the feelings.', '노래하는 말이 이야기를 들려주고; 그다음 노래가 마음을 보여 줘요.']]];
// the air and two variations (the tune of "Ah vous dirai-je, maman", a folk song): the theme; running quavers; the minor
const FMX5_AIR = { theme: [0, 0, 7, 7, 9, 9, 7, 5, 5, 4, 4, 2, 2, 0], v1: 'quavers', v2: [0, 0, 7, 7, 8, 8, 7, 5, 5, 3, 3, 2, 2, 0] };
const fmx5Play = (which) => { const th = FMX5_AIR.theme, ev = [];
  if (which === 'v1') { th.forEach((x, j) => { const at = j + (j > 6 ? 1 : 0); if (j === 6 || j === 13) ev.push({ at, keys: [x], len: 2 }); else ev.push({ at, keys: [x], len: 0.5 }, { at: at + 0.5, keys: [x + (x === th[j + 1] ? 2 : 0)], len: 0.5 }); }); }
  else { const m = which === 'v2' ? FMX5_AIR.v2 : th; m.forEach((x, j) => ev.push({ at: j + (j > 6 ? 1 : 0), keys: [x], len: j === 6 || j === 13 ? 2 : 1 })); }
  return spPlay(ev.map(e => ({ ...e, vol: 0.15 })), 104); };
function Fmx5Boxes({ f }) {
  return <div style={{display:'flex',gap:4,justifyContent:'center',flexWrap:'wrap',margin:'6px 0'}}>{f.boxes.map(([en, ko, L], j) => <div key={j} style={{minWidth:58,padding:'6px 8px',borderRadius:8,border:'1.5px solid ' + (L === 'A' || L === 'R' ? BK.ink : 'rgba(38,41,107,0.35)'),background:L.startsWith('A') ? 'rgba(38,41,107,0.07)' : '#fff',textAlign:'center'}}>
    <div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:900,color:L === 'B' ? BK.coral : BK.ink,lineHeight:1.1}}>{L}</div>{en && <div style={{fontSize:11.5,fontWeight:800,color:BK.muted}}>{t(en, ko)}</div>}</div>)}</div>;
}
function FmxForms5Pad() {
  const [i, setI] = useState(0), [quiz, setQuiz] = useState(null), [pickd, setPick] = useState(null);
  const f = FMX5[quiz ? FMX5.findIndex(x => x.id === quiz.id) : i], hide = quiz && pickd == null;
  const ask = () => { let c, g = 0; do { c = pick(FMX5_CLUE); } while (quiz && quiz.id === c[0] && g++ < 8); setQuiz({ id: c[0], clue: c[1] }); setPick(null); };
  return (
    <div className="try-box" style={actBox} data-fmx="forms5">
      <div style={actTitle}>{t('Four forms from the great composers', '위대한 작곡가들의 네 가지 형식')}</div>
      <div style={actNote}>{t('Grade 5 general knowledge: four forms, and an example of each by a great composer. Each shape is drawn as letters: the same letter, the same music.', '5급 일반 지식: 네 가지 형식, 그리고 위대한 작곡가의 예를 하나씩. 모양은 글자로: 같은 글자는 같은 음악.')}</div>
      {!quiz && spChips(FMX5.map((x, j) => [j, t(x.en, x.ko)]), i, setI)}
      {quiz && <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:BK.ink,margin:'4px 0',textWrap:'balance'}}>{t(quiz.clue[0], quiz.clue[1])}</div>}
      {!hide && <><div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:24,fontWeight:900,color:BK.ink,margin:'4px 0 0'}}>{t(f.en, f.ko)}</div>
        <Fmx5Boxes f={f}/>
        <div style={{fontSize:14,color:BK.ink,lineHeight:1.45,margin:'2px 0 6px',textWrap:'pretty'}}>{t(f.say[0], f.say[1])}</div>
        <div style={{fontSize:13,fontWeight:800,color:BK.coral,textAlign:'center'}}>{t('Listen to: ', '들어 볼 곡: ') + t(f.ex[0], f.ex[1])}</div>
        {f.id === 'air' && <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>{[['theme', t('▶ The air', '▶ 주제')], ['v1', t('▶ Var. 1: running', '▶ 변주 1: 잘게')], ['v2', t('▶ Var. 2: minor', '▶ 변주 2: 단조')]].map(([w, lab]) => <button key={w} className="ghost-btn" style={spBtn} onClick={() => fmx5Play(w)}>{lab}</button>)}</div>}</>}
      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{FMX5.map(x => <button key={x.id} className={'choice-btn' + (pickd == null ? '' : x.id === quiz.id ? ' good' : x.id === pickd ? ' bad' : '')} onClick={() => { if (pickd == null) setPick(x.id); }} style={{padding:'11px 4px',fontSize:14.5,fontWeight:900}}>{t(x.en, x.ko)}</button>)}</div>}
      {quiz && pickd != null && spMsg(pickd === quiz.id ? t('Yes.', '맞아요.') : t('It was the ' + f.en.toLowerCase() + '.', f.ko + '였어요.'), pickd === quiz.id ? BK.green : BK.coral)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={ask}>{quiz && pickd == null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(null); setPick(null); }}>{t('← All four', '← 네 가지 모두')}</button>}
      </div>
    </div>
  );
}
// the woodwinds: the sounding range (semitones from middle C), the clef, and how a transposing instrument is written
const SPR_WIND = [
  { n: ['Flute', '플루트'], clef: ['treble clef', '높은음자리표'], lo: 0, hi: 36, tr: ['It sounds as written. Held sideways; the highest of these five.', '적힌 대로 소리 나요. 옆으로 들고 불어요; 이 다섯 중 가장 높아요.'] },
  { n: ['Oboe', '오보에'], clef: ['treble clef', '높은음자리표'], lo: -2, hi: 33, tr: ['It sounds as written. A double reed; the orchestra tunes to its A.', '적힌 대로 소리 나요. 겹리드; 오케스트라는 오보에의 A에 맞춰 조율해요.'] },
  { n: ['Clarinet in B♭', 'B♭ 클라리넷'], clef: ['treble clef', '높은음자리표'], lo: -10, hi: 34, tr: ['A transposing instrument: it sounds a tone (a major 2nd) lower than written.', '이조 악기: 적힌 것보다 온음(장2도) 낮게 소리 나요.'] },
  { n: ['Clarinet in A', 'A 클라리넷'], clef: ['treble clef', '높은음자리표'], lo: -11, hi: 33, tr: ['A transposing instrument: it sounds a minor 3rd lower than written.', '이조 악기: 적힌 것보다 단3도 낮게 소리 나요.'] },
  { n: ['Bassoon', '바순'], clef: ['bass clef, and tenor clef for high notes', '낮은음자리표, 높은 음은 테너음자리표'], lo: -26, hi: 16, tr: ['It sounds as written. A double reed; the bass of the woodwinds.', '적힌 대로 소리 나요. 겹리드; 목관의 베이스.'] },
];
const SPR_NM = ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B'];
const sprWNote = (x) => SPR_NM[((x % 12) + 12) % 12] + (4 + Math.floor(x / 12));
const sprWindPlay = (v) => spPlay([v.lo, Math.round((v.lo + v.hi) / 2), v.hi].map((x, j) => ({ at: j * 1.1, keys: [x], len: 1, vol: 0.15 })), 72);
function SprWindRange({ v }) {   // the whole keyboard, the instrument's range lit, middle C marked
  const lit = {}; for (let x = v.lo; x <= v.hi; x++) lit[x] = 'pale'; lit[v.lo] = 'cor'; lit[v.hi] = 'cor';
  const m = spMiniKeys(-39, 48, lit, 6, 28, 2, 4);
  return <div style={{maxWidth:520,margin:'4px auto 0'}}><svg viewBox={'0 0 ' + m.w + ' 34'} style={{width:'100%',display:'block'}} role="img" aria-label={t('The range on the keyboard', '건반 위의 음역')} dangerouslySetInnerHTML={{ __html: m.svg }}/>
    <div style={{display:'flex',justifyContent:'space-between',fontSize:12,fontWeight:800,color:BK.muted,margin:'2px 0 0'}}><span>A0</span><span>{t('middle C', '가운데 도')} C4</span><span>C8</span></div></div>;
}
function SprWindPad() {
  const [i, setI] = useState(0), [quiz, setQuiz] = useState(null), [pickd, setPick] = useState(null);
  const v = SPR_WIND[quiz ? quiz.i : i], hide = quiz && pickd == null;
  const ask = () => { let j, g = 0; do { j = Math.floor(Math.random() * SPR_WIND.length); } while (quiz && quiz.i === j && g++ < 8); setQuiz({ i: j }); setPick(null); };
  return (
    <div className="try-box" style={actBox} data-spr="wind">
      <div style={actTitle}>{t('The woodwinds', '목관 악기')}</div>
      <div style={actNote}>{t('The woodwinds of the orchestra: flute, oboe, two clarinets and bassoon. Each one\'s range is lit on the whole keyboard (the notes it sounds), with the clef it reads.', '오케스트라의 목관 악기: 플루트, 오보에, 클라리넷 둘, 바순. 악기마다 음역(소리 나는 음)을 건반 전체 위에 밝히고, 읽는 음자리표도 함께.')}</div>
      {!quiz && spChips(SPR_WIND.map((x, j) => [j, t(x.n[0], x.n[1])]), i, (j) => { setI(j); sprWindPlay(SPR_WIND[j]); })}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 0'}}>{hide ? t('Which instrument?', '어느 악기일까요?') : t(v.n[0], v.n[1]) + ' · ' + t(v.clef[0], v.clef[1])}</div>
      <SprWindRange v={v}/>
      <div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.coral,marginTop:4}}>{t('About ', '약 ') + sprWNote(v.lo) + ' – ' + sprWNote(v.hi) + t(' (sounding)', '(소리 나는 음)')}</div>
      {quiz ? <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>{SPR_WIND.map((x, j) => <button key={j} className={'choice-btn' + (pickd == null ? '' : j === quiz.i ? ' good' : j === pickd ? ' bad' : '')} onClick={() => { if (pickd == null) setPick(j); }} style={{padding:'11px 4px',fontSize:14.5,fontWeight:900}}>{t(x.n[0], x.n[1])}</button>)}</div> : null}
      {spMsg(hide ? t(v.clef[0][0].toUpperCase() + v.clef[0].slice(1) + '. ' + v.tr[0].split('. ')[0].replace(/\.?$/, '.'), v.clef[1] + '. ' + v.tr[1].split('. ')[0].replace(/\.?$/, '.')) : t(v.tr[0], v.tr[1]), quiz && !hide ? (pickd === quiz.i ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => sprWindPlay(v)}>{t('▶ Low, middle, high', '▶ 낮은, 가운데, 높은 음')}</button>
        <button className="ghost-btn" style={spBtn} onClick={ask}>{quiz && pickd == null ? t('▶ Another', '▶ 다른 것') : t('▶ Your turn', '▶ 내가 해보기')}</button>
        {quiz && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(null); setPick(null); }}>{t('← Back', '← 돌아가기')}</button>}
      </div>
    </div>
  );
}
TOOLS.push({ id: 'mlx-stanza', ch: 'melody', title: 'A melody for a four-line stanza', blurb: 'Four lines of words, sixteen bars, lines 1 to 3 away from home and line 4 home.', C: () => <MwStanzaPad/> },
  { id: 'fmx-forms5', ch: 'form', title: 'Minuet and trio, scherzo, variations, recitative and aria', blurb: 'Four forms from the great composers, drawn as letters.', C: () => <FmxForms5Pad/> },
  { id: 'spr-wind', ch: 'pitch-range', title: 'The woodwinds', blurb: 'Flute, oboe, clarinets in B♭ and A, bassoon: their ranges and clefs.', C: () => <SprWindPad/> });
lbhRetitle('mlx-stanza', 'A melody for a four-line stanza', '네 줄 시에 선율 붙이기', 'Four lines of words, sixteen bars, lines 1 to 3 away from home and line 4 home.', '네 줄의 가사, 16마디, 1-3줄은 집 밖에서, 4줄은 집으로.');
lbhRetitle('fmx-forms5', 'Minuet and trio, scherzo, variations, recitative and aria', '미뉴에트와 트리오, 스케르초, 변주, 레치타티보와 아리아', 'Four forms from the great composers, drawn as letters.', '위대한 작곡가들의 네 가지 형식, 글자로 그려요.');
lbhRetitle('spr-wind', 'The woodwinds', '목관 악기', 'Flute, oboe, clarinets in B♭ and A, bassoon: their ranges and clefs.', '플루트, 오보에, B♭과 A 클라리넷, 바순: 음역과 음자리표.');
Object.assign(TOOL_META, { 'mlx-stanza': ['melody', 3, 3, 'show ear'], 'fmx-forms5': ['melody', 3, 3, 'show ear'], 'spr-wind': ['about', 0, 3, 'show ear'] });
Object.assign(TOOL_CONCEPT, { 'mlx-stanza': 'c-map', 'fmx-forms5': 'c-map', 'spr-wind': 'about' });
'''
rep("""Object.assign(TOOL_CONCEPT, { 'spr-tune': 'about', 'cpx-dances': 'about' });""", """Object.assign(TOOL_CONCEPT, { 'spr-tune': 'about', 'cpx-dances': 'about' });""" + STORIES)
rep("""'mlx-write', 'mlx-couplet', 'mlx-build', 'tune-anatomy',""", """'mlx-write', 'mlx-couplet', 'mlx-stanza', 'mlx-build', 'tune-anatomy',""")
rep("""  'form': ['fmx-map', 'fmx-phrase', 'fmx-letters', 'fmx-binary', 'fmx-ternary', 'fmx-find', 'fmx-build', 'form-shapes',""", """  'form': ['fmx-map', 'fmx-phrase', 'fmx-letters', 'fmx-binary', 'fmx-ternary', 'fmx-find', 'fmx-build', 'fmx-forms5', 'form-shapes',""")
rep("""  'pitch-range': ['spr-zone', 'spr-big', 'spr-fam', 'spr-ladder', 'spr-tune', 'spr-range',""", """  'pitch-range': ['spr-zone', 'spr-big', 'spr-fam', 'spr-ladder', 'spr-tune', 'spr-wind', 'spr-range',""")
rep("""lessons: ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-words', 'mlx-write', 'mlx-couplet', 'mlx-build',""", """lessons: ['mlx-map', 'mlx-line', 'mlx-phrasing', 'mlx-qa', 'mlx-motif', 'mlx-seq', 'mlx-words', 'mlx-write', 'mlx-couplet', 'mlx-stanza', 'mlx-build',""")
rep("""lessons: ['fmx-map', 'fmx-phrase', 'fmx-letters', 'fmx-binary', 'fmx-ternary', 'fmx-find', 'fmx-build', 'same-or-new',""", """lessons: ['fmx-map', 'fmx-phrase', 'fmx-letters', 'fmx-binary', 'fmx-ternary', 'fmx-find', 'fmx-build', 'fmx-forms5', 'same-or-new',""")
rep("""  set('4', 'spr-tune cpx-dances');   // Build AW""", """  set('5', 'mlx-stanza fmx-forms5 spr-wind');   // Build BE: Grade 5 creative work and general knowledge
  set('4', 'spr-tune cpx-dances');   // Build AW""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
