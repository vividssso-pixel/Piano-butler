import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BW (board call 26, the fourth Grade 7 room): Knowing Your Pieces, Grades 7 and 8. The practical exams' general knowledge
# for Grades 7 and 8 (Manual 2026, the general knowledge table): notes, signs, terms, title and key; any key changes, or other
# tonal organisation (atonal, pentatonic, whole tone); form, through a detailed structural analysis, and, for a movement, a brief
# knowledge of its place among the other movements; the period and its style; other genres typical of the period; the composer,
# their works and musical influences. Theory stops at Grade 6, so this room carries the knowing for the top two floors. The thing
# to make: a map of your own piece. Genre lists and the movement plans are textbook knowledge (on the board's list to check).

rep("""const ARPS_7_DRILL = { id: 'arps-7', label: 'Arpeggios and Progressions, Grade 7' };   // Build BV""",
    """const ARPS_7_DRILL = { id: 'arps-7', label: 'Arpeggios and Progressions, Grade 7' };   // Build BV
const PIECES_78_DRILL = { id: 'pieces-78', label: 'Knowing Your Pieces, Grades 7 and 8' };   // Build BW""")
rep("""  { id: 'arps-7', label: 'Arpeggios and Progressions, Grade 7', concept: ARPS_7_DRILL, track: 'start' },   // Build BV""",
    """  { id: 'arps-7', label: 'Arpeggios and Progressions, Grade 7', concept: ARPS_7_DRILL, track: 'start' },   // Build BV
  { id: 'pieces-78', label: 'Knowing Your Pieces, Grades 7 and 8', concept: PIECES_78_DRILL, track: 'start' },   // Build BW""")
rep("""'arps-7': '아르페지오와 화음 진행, Grade 7'""", """'arps-7': '아르페지오와 화음 진행, Grade 7', 'pieces-78': '내 곡 알기, Grade 7과 8'""")
rep("""'arps-7': 'k-play'""", """'arps-7': 'k-play', 'pieces-78': 'c-map'""")
rep("""  'arps-7': 'arpeggios grade 7""", """  'pieces-78': 'general knowledge grade 7 grade 8 piece form structure analysis map sections key changes tonal organisation atonal pentatonic whole tone movement larger work period style genres composer works influences',
  'arps-7': 'arpeggios grade 7""")
rep("""'arps-7': ['arps-6']""", """'arps-7': ['arps-6'], 'pieces-78': ['form', 'composers']""")
rep("""'arps-7': ['Arpeggios 7', '아르페지오 7']""", """'arps-7': ['Arpeggios 7', '아르페지오 7'], 'pieces-78': ['My pieces', '내 곡']""")

CH = r'''
// ─── Chapter: Knowing Your Pieces, Grades 7 and 8 (Build BW, 2026-10-28; board call 26, the fourth Grade 7 room) ───
// ── step 1 (and the thing to make): a map of my piece: its sections, bars and keys ──
const PM_PRESETS = {
  binary: [['A', 1, 8, 'I'], ['B', 9, 16, 'V → I']],
  ternary: [['A', 1, 16, 'I'], ['B', 17, 32, 'vi'], ['A', 33, 48, 'I']],
  rondo: [['A', 1, 8, 'I'], ['B', 9, 16, 'V'], ['A', 17, 24, 'I'], ['C', 25, 32, 'IV'], ['A', 33, 40, 'I']],
  sonata: [['Exposition', 1, 40, 'I → V'], ['Development', 41, 70, '…'], ['Recapitulation', 71, 110, 'I'], ['Coda', 111, 120, 'I']],
};
const PM_NAMES = { binary: ['Binary', '2부 형식'], ternary: ['Ternary', '3부 형식'], rondo: ['Rondo', '론도'], sonata: ['Sonata form', '소나타 형식'] };
const pmLoad = () => { try { const v = JSON.parse(localStorage.getItem('pb_piece_map') || 'null'); return Array.isArray(v) && v.length ? v : null; } catch (e) { return null; } };
const pmSave = (v) => { try { localStorage.setItem('pb_piece_map', JSON.stringify(v)); } catch (e) {} };
function PmBar({ secs, sel = -1, w = 420 }) {
  const total = Math.max(1, ...secs.map(x => +x[2] || 0)), first = Math.min(...secs.map(x => +x[1] || 1));
  return <div style={{display:'flex',width:'100%',maxWidth:w,margin:'6px auto',border:'1.5px solid ' + BK.ink,borderRadius:6,overflow:'hidden',background:'#fff'}}>{secs.map((x, i) => { const len = Math.max(1, (+x[2] || 0) - (+x[1] || 0) + 1);
    return <div key={i} style={{flex:Math.max(len, (total - first + 1) * 0.2) + ' 1 0',minWidth:0,borderLeft:i ? '1.5px solid ' + BK.ink : 'none',padding:'6px 3px',textAlign:'center',background:sel === i ? '#fbe3da' : String(x[0]).startsWith('A') ? 'rgba(38,41,107,0.07)' : '#fff'}}>
      <div style={{fontFamily:LB_SERIF,fontSize:x[0].length > 9 ? 11 : x[0].length > 2 ? 12.5 : 18,fontWeight:900,color:BK.ink,lineHeight:1.1,overflow:'hidden',textOverflow:'ellipsis',whiteSpace:'nowrap'}}>{x[0]}</div>
      <div style={{fontSize:10.5,fontWeight:800,color:BK.muted,whiteSpace:'nowrap'}}>{x[1]}–{x[2]}</div>
      <div style={{fontSize:11,fontWeight:900,color:BK.coral,whiteSpace:'nowrap',overflow:'hidden',textOverflow:'ellipsis'}}>{x[3]}</div></div>; })}</div>;
}
function PieceMapMaker() {
  const [secs, setSecs] = useState(() => pmLoad() || PM_PRESETS.ternary.map(x => x.slice())), [sel, setSel] = useState(0), [title, setTitle] = useState(() => { try { return localStorage.getItem('pb_piece_title') || ''; } catch (e) { return ''; } });
  const upd = (v) => { setSecs(v); pmSave(v); };
  const field = (i, j, v) => upd(secs.map((x, k) => (k === i ? x.map((y, m) => (m === j ? v : y)) : x)));
  const add = () => { const last = secs[secs.length - 1], s0 = (+last[2] || 0) + 1; upd(secs.concat([[String.fromCharCode(65 + Math.min(secs.length, 6)), s0, s0 + 7, '']])); setSel(secs.length); };
  const del = () => { if (secs.length < 2) return; const v = secs.filter((_, k) => k !== sel); upd(v); setSel(Math.max(0, sel - 1)); };
  const inp = { width:'100%', minWidth:0, padding:'8px 6px', fontSize:15, fontWeight:800, border:'1.5px solid rgba(38,41,107,0.3)', borderRadius:8, color:BK.ink, background:'#fff', boxSizing:'border-box' };
  const x = secs[Math.min(sel, secs.length - 1)];
  return (
    <div className="try-box" style={actBox} data-pm="map">
      <div style={actTitle}>{t('The map of my piece', '내 곡의 지도')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>내가 치는 곡의 <b>지도</b>를 그려요: 부분(글자나 이름), 마디, 그리고 조. 형식 하나로 시작해서 내 곡에 맞게 고쳐요. 이 기기에 저장돼요.</> : <>Draw <b>the map</b> of a piece you play: its sections (a letter or a name), their bars, and their keys. Start from a form, then change it to fit your piece. It is saved on this device.</>}</div>
      <input value={title} placeholder={t('My piece (title, composer)', '내 곡(제목, 작곡가)')} onChange={(e) => { setTitle(e.target.value); try { localStorage.setItem('pb_piece_title', e.target.value); } catch (er) {} }} style={{...inp, textAlign:'center', marginBottom:6}} aria-label={t('The piece', '곡')}/>
      {spChips(Object.keys(PM_PRESETS).map(k => [k, t(PM_NAMES[k][0], PM_NAMES[k][1])]), null, (k) => { upd(PM_PRESETS[k].map(y => y.slice())); setSel(0); })}
      <PmBar secs={secs} sel={sel}/>
      <div style={{display:'flex',gap:4,flexWrap:'wrap',justifyContent:'center',margin:'4px 0'}}>{secs.map((y, i) => <button key={i} className={'chip' + (i === sel ? ' active' : '')} onClick={() => setSel(i)} style={{minHeight:36,padding:'4px 10px'}}>{y[0] || '?'}</button>)}</div>
      {x && <div style={{display:'grid',gridTemplateColumns:'1.4fr 0.7fr 0.7fr 1.2fr',gap:6,alignItems:'end'}}>
        {[[0, t('Section', '부분')], [1, t('From bar', '시작 마디')], [2, t('To bar', '끝 마디')], [3, t('Key', '조')]].map(([j, lab]) => <label key={j} style={{display:'grid',gap:2,fontSize:11,fontWeight:900,color:BK.muted,minWidth:0}}>{lab}<input value={x[j]} inputMode={j === 1 || j === 2 ? 'numeric' : 'text'} onChange={(e) => field(sel, j, j === 1 || j === 2 ? e.target.value.replace(/[^0-9]/g, '') : e.target.value)} style={inp}/></label>)}
      </div>}
      {spMsg(t(secs.length + ' sections · bars ' + (secs[0] ? secs[0][1] : 1) + '–' + (secs[secs.length - 1] ? secs[secs.length - 1][2] : '') + ' · the same letter means the same music.', '부분 ' + secs.length + '개 · 마디 ' + (secs[0] ? secs[0][1] : 1) + '–' + (secs[secs.length - 1] ? secs[secs.length - 1][2] : '') + ' · 같은 글자는 같은 음악.'))}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={add}>{t('+ A section', '+ 부분 더하기')}</button>
        <button className="ghost-btn" style={spBtn} disabled={secs.length < 2} onClick={del}>{t('Remove this one', '이 부분 지우기')}</button>
      </div>
    </div>
  );
}
// ── step 2: keys, and other tonal worlds: major, minor, pentatonic, whole tone, atonal ──
const TW = {
  maj: { en: 'Major', ko: '장조', notes: [0, 2, 4, 5, 7, 9, 11], tune: [0, 4, 7, 5, 4, 2, 4, 0], clue: ['A home note (the tonic) and bright 3rds: C D E F G A B.', '집(으뜸음)이 있고 밝은 3도: C D E F G A B.'] },
  min: { en: 'Minor', ko: '단조', notes: [9, 11, 0, 2, 4, 5, 8], tune: [9, 12, 16, 14, 12, 11, 8, 9], clue: ['A home note and a darker 3rd; often a raised 7th (G♯ in A minor).', '집이 있고 어두운 3도; 흔히 올린 7음(A단조의 G♯).'] },
  pen: { en: 'Pentatonic', ko: '5음 음계', notes: [6, 8, 10, 13, 15], tune: [6, 8, 10, 13, 10, 8, 6, 3], clue: ['Five notes, no semitones: the black keys.', '반음 없는 다섯 음: 검은건반.'] },
  wt: { en: 'Whole tone', ko: '온음 음계', notes: [0, 2, 4, 6, 8, 10], tune: [0, 2, 4, 6, 8, 10, 8, 4], clue: ['Six notes, every step a tone: dreamy, no pull to a home note.', '여섯 음, 모두 온음: 꿈결 같고, 집으로 끌리지 않아요.'] },
  ato: { en: 'Atonal', ko: '무조', notes: [0, 3, 11, 2, 6, 5, 9, 8, 1, 7, 10, 4], tune: [0, 3, 11, 14, 6, 5, 9, 8], clue: ['No home key at all; all twelve notes are equal (sometimes in a fixed order, a tone row).', '집 조가 아예 없어요; 열두 음이 모두 같아요(때로 정해진 순서, 음렬).'] },
};
const TW_IDS = ['maj', 'min', 'pen', 'wt', 'ato'];
const twPlay = (id) => spPlay(TW[id].tune.map((x, j) => ({ at: j * 0.5, keys: [x], len: j === 7 ? 1.2 : 0.46, vol: 0.15 })), 84);
function TonalPad({ onResult, fixed }) {
  const [id, setId] = useState(fixed ? fixed.id : 'pen'), [quiz, setQuiz] = useState(!!fixed), [ans, setAns] = useState(null);
  const x = TW[id], show = !quiz || ans, lit = {}; if (show) x.notes.forEach(n => { lit[n] = 'cor'; lit[n + 12] = 'cor'; });
  const ask = () => { let y, g = 0; do { y = pick(TW_IDS); } while (y === id && g++ < 10); setId(y); setQuiz(true); setAns(null); twPlay(y); };
  const say = (v) => { if (!quiz || ans) return; setAns(v); if (onResult) onResult({ ok: v === id }); };
  return (
    <div className="try-box" style={actBox} data-pm="tonal">
      <div style={actTitle}>{t('Keys, and other tonal worlds', '조, 그리고 다른 음의 세계')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>7·8급은 곡의 <b>조가 바뀌는 곳</b>을 짚어요: 새 임시표가 계속 나오고, 새 조의 종지로 닫혀요. 조가 아예 없는 곡도 있어요: <b>5음 음계</b>, <b>온음 음계</b>, <b>무조</b>. 들어 보고 알아맞혀요.</> : <>Grades 7 and 8 point out <b>where the key changes</b>: new accidentals that keep coming, and a cadence in the new key. Some pieces have another kind of home, or none: <b>pentatonic</b>, <b>whole tone</b>, <b>atonal</b>. Listen and tell them apart.</>}</div>
      {!quiz && spChips(TW_IDS.map(y => [y, t(TW[y].en, TW[y].ko)]), id, (y) => { setId(y); twPlay(y); })}
      <SpKb lo={0} hi={23} W={14} H={62} lit={lit} names={{ 0: 'C', 12: 'C' }} label={t('Its notes', '그 음들')}/>
      {show && <div style={{fontSize:14,color:BK.ink,lineHeight:1.45,textAlign:'center',margin:'4px 0'}}><b>{t(x.en, x.ko)}</b>: {t(x.clue[0], x.clue[1])}</div>}
      {quiz && !ans && <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,marginTop:6}}>{TW_IDS.map(y => <button key={y} className="choice-btn" onClick={() => say(y)} style={{padding:'10px 2px',fontSize:13.5,fontWeight:900}}>{t(TW[y].en, TW[y].ko)}</button>)}</div>}
      {spMsg(ans ? (ans === id ? t('Yes: ' + x.en.toLowerCase() + '.', '맞아요: ' + x.ko + '.') : t('It was ' + x.en.toLowerCase() + '.', '정답은 ' + x.ko + '.')) : quiz ? t('Which tonal world?', '어떤 음의 세계일까요?') : '', ans ? (ans === id ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => twPlay(id)}>{quiz && !ans ? t('♪ Again', '♪ 다시') : t('▶ Hear it', '▶ 들어 보기')}</button>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Which world?', '▶ 어떤 세계일까?')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── step 3: one movement of a larger work: where my piece sits ──
const MV = {
  sonata: { en: 'Classical sonata', ko: '고전 소나타', mv: [['Fast', '빠르게', 'often sonata form', '흔히 소나타 형식'], ['Slow', '느리게', 'often in a related key', '흔히 근친조에서'], ['Fast', '빠르게', 'often a rondo', '흔히 론도']] },
  symphony: { en: 'Classical symphony', ko: '고전 교향곡', mv: [['Fast', '빠르게', 'sonata form', '소나타 형식'], ['Slow', '느리게', '', ''], ['Minuet and trio (or scherzo)', '미뉴에트와 트리오(또는 스케르초)', 'in 3', '3박자'], ['Fast', '빠르게', 'the finale', '피날레']] },
  suite: { en: 'Baroque suite', ko: '바로크 모음곡', mv: [['Allemande', '알망드', 'moderate, in 4', '보통 빠르기, 4박자'], ['Courante', '쿠랑트', 'running, in 3', '달리듯, 3박자'], ['Sarabande', '사라방드', 'slow, in 3', '느리게, 3박자'], ['Gigue', '지그', 'lively, compound time', '활기차게, 겹박자']] },
  set: { en: 'A set of pieces', ko: '모음곡집', mv: [['No. 1', '1번', 'each piece', '곡마다'], ['No. 2', '2번', 'its own', '자기만의'], ['No. 3', '3번', 'character', '성격']] },
};
function MovementPad({ onResult, fixed }) {
  const [w, setW] = useState(fixed ? fixed.w : 'sonata'), [mine, setMine] = useState(fixed ? fixed.m : 1), [quiz, setQuiz] = useState(!!fixed), [ans, setAns] = useState(null);
  const W = MV[w];
  const ask = () => { const ww = pick(['sonata', 'symphony', 'suite']), m = Math.floor(Math.random() * MV[ww].mv.length); setW(ww); setMine(m); setQuiz(true); setAns(null); };
  const say = (j) => { if (!quiz || ans != null) return; setAns(j); if (onResult) onResult({ ok: j === mine }); };
  const qText = quiz ? (w === 'suite' ? t('In a Baroque suite, which dance is ' + W.mv[mine][2] + '?', '바로크 모음곡에서 ' + W.mv[mine][3] + '인 춤곡은?') : w === 'symphony' && mine === 2 ? t('In a Classical symphony, where does the minuet usually come?', '고전 교향곡에서 미뉴에트는 대개 어디에?') : t('In a ' + W.en.toLowerCase() + ', which movement is usually ' + (W.mv[mine][0].toLowerCase()) + (W.mv[mine][2] ? ', ' + W.mv[mine][2] : '') + '?', W.ko + '에서 대개 ' + W.mv[mine][1] + (W.mv[mine][3] ? ', ' + W.mv[mine][3] : '') + '인 악장은?')) : null;
  return (
    <div className="try-box" style={actBox} data-pm="mvt">
      <div style={actTitle}>{t('One movement of a larger work', '큰 작품의 한 악장')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>내 곡이 소나타나 모음곡의 <b>한 악장</b>이라면, 다른 악장들과의 관계를 짧게 말할 수 있어야 해요: 몇 번째 악장인지, 빠른지 느린지, 어떤 조인지. 작품을 고르고, 내 악장을 눌러요.</> : <>If your piece is <b>one movement</b> of a sonata or a suite, say briefly how it fits with the others: which movement it is, fast or slow, in which key. Choose the work, then tap your movement.</>}</div>
      {!quiz && spChips(Object.keys(MV).map(k => [k, t(MV[k].en, MV[k].ko)]), w, (k) => { setW(k); setMine(0); })}
      {quiz && <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:BK.ink,margin:'4px 0',textWrap:'balance'}}>{qText}</div>}
      <div style={{display:'flex',gap:5,justifyContent:'center',flexWrap:'wrap',margin:'6px 0'}}>{W.mv.map(([en, ko, n1, n2], j) => { const on = (!quiz && j === mine) || (quiz && ans != null && j === mine), badOne = quiz && ans === j && j !== mine;
        return <button key={j} onClick={() => (quiz ? say(j) : setMine(j))} style={{minWidth:70,flex:'1 1 0',maxWidth:130,padding:'8px 6px',borderRadius:8,cursor:'pointer',textAlign:'center',border:'1.5px solid ' + (on ? (quiz ? BK.green : BK.coral) : badOne ? BK.coral : 'rgba(38,41,107,0.3)'),background:on ? (quiz ? '#e3f1ec' : '#fbe3da') : '#fff',color:BK.ink}}>
          <div style={{fontSize:10.5,fontWeight:900,color:BK.muted}}>{['I', 'II', 'III', 'IV'][j]}</div><div style={{fontSize:13,fontWeight:900,lineHeight:1.15}}>{quiz && ans == null ? '?' : t(en, ko)}</div>{!quiz && n1 && <div style={{fontSize:10.5,fontWeight:700,color:BK.muted}}>{t(n1, n2)}</div>}</button>; })}</div>
      {spMsg(quiz ? (ans == null ? t('Tap the movement.', '악장을 눌러요.') : ans === mine ? t('Yes: movement ' + ['I', 'II', 'III', 'IV'][mine] + '.', '맞아요: ' + ['I', 'II', 'III', 'IV'][mine] + '악장.') : t('It is usually movement ' + ['I', 'II', 'III', 'IV'][mine] + ': ' + W.mv[mine][0] + '.', '대개 ' + ['I', 'II', 'III', 'IV'][mine] + '악장: ' + W.mv[mine][1] + '.')) : t('My piece: movement ' + ['I', 'II', 'III', 'IV'][mine] + ' of ' + W.mv.length + (W.mv[mine][0] ? ', ' + W.mv[mine][0].toLowerCase() : '') + '.', '내 곡: ' + W.mv.length + '개 중 ' + ['I', 'II', 'III', 'IV'][mine] + '악장' + (W.mv[mine][1] ? ', ' + W.mv[mine][1] : '') + '.'), quiz && ans != null ? (ans === mine ? BK.green : BK.coral) : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {!fixed && <button className="ghost-btn" style={spBtn} onClick={ask}>{t('▶ Your turn', '▶ 내가 해보기')}</button>}
        {quiz && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => { setQuiz(false); setAns(null); }}>{t('Back', '돌아가기')}</button>}
      </div>
    </div>
  );
}
// ── step 4: other music of its time: genres typical of each period ──
const GEN = [
  ['suite', 'baroque', 'Dance suite', '춤곡 모음곡'], ['grosso', 'baroque', 'Concerto grosso', '콘체르토 그로소'], ['oratorio', 'baroque', 'Oratorio', '오라토리오'], ['fugue', 'baroque', 'Prelude and fugue', '전주곡과 푸가'],
  ['symph', 'classical', 'Symphony', '교향곡'], ['quartet', 'classical', 'String quartet', '현악 4중주'], ['csonata', 'classical', 'Sonata in sonata form', '소나타 형식의 소나타'],
  ['nocturne', 'romantic', 'Nocturne and other character pieces', '녹턴과 성격 소품'], ['lied', 'romantic', 'Art song (Lied)', '예술 가곡(리트)'], ['poem', 'romantic', 'Symphonic poem', '교향시'], ['etude', 'romantic', 'Concert étude', '연주회용 연습곡'],
  ['ballet', 'modern', 'Ballet for the Ballets Russes', '발레 뤼스를 위한 발레'], ['serial', 'modern', 'Twelve-note (serial) music', '12음(음렬) 음악'], ['minimal', 'contemporary', 'Minimalism', '미니멀리즘'], ['film', 'contemporary', 'Video game music', '비디오 게임 음악'],
];
const GEN_ERAS = ['baroque', 'classical', 'romantic', 'modern', 'contemporary'];
function GenresPad({ onResult, fixed }) {
  const [deck, setDeck] = useState(() => (fixed ? [GEN.find(x => x[0] === fixed.id)] : shuffle(GEN).slice(0, 6))), [i, setI] = useState(0), [ans, setAns] = useState(null), [score, setScore] = useState(0);
  const g = deck[i], done = i >= deck.length;
  const say = (era) => { if (ans || done) return; setAns(era); const ok = era === g[1]; if (ok) setScore(s0 => s0 + 1); if (fixed && onResult) onResult({ ok }); };
  const next = () => { setAns(null); setI(i + 1); if (!fixed && i + 1 >= deck.length && onResult) onResult({ ok: score >= deck.length - 1 }); };
  const again = () => { setDeck(shuffle(GEN).slice(0, 6)); setI(0); setAns(null); setScore(0); };
  return (
    <div className="try-box" style={actBox} data-pm="genres">
      <div style={actTitle}>{t('Other music of its time', '그 시대의 다른 음악')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>7·8급은 내 곡의 시대에 흔했던 <b>다른 갈래</b>(관현악, 합창, 오페라…)도 알아야 해요. 카드의 갈래는 어느 시대의 것일까요?</> : <>Grades 7 and 8 also ask about <b>other genres typical of your piece's period</b> (orchestral, choral, opera…). Which period does each card belong to?</>}</div>
      {!done ? <><div style={{textAlign:'center',margin:'6px auto',maxWidth:300,padding:'16px 10px',borderRadius:10,border:'1.5px solid ' + BK.ink,background:'#fff',fontFamily:LB_SERIF,fontSize:20,fontWeight:900,color:BK.ink}}>{t(g[2], g[3])}</div>
        <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:6,marginTop:6}}>{GEN_ERAS.map(e => { const p = CMP_PERIODS[e]; return <button key={e} className={'choice-btn' + (!ans ? '' : e === g[1] ? ' good' : e === ans ? ' bad' : '')} onClick={() => say(e)} style={{padding:'9px 2px',fontSize:13.5,fontWeight:900,lineHeight:1.2}}>{t(p.short[0], p.short[1])}<div style={{fontSize:11,fontWeight:800,opacity:0.75}}>{p.years[0]}–{p.years[1] > 2025 ? '' : p.years[1]}</div></button>; })}</div></>
        : spMsg(t(score + ' of ' + deck.length + ' in the right period.', deck.length + '개 중 ' + score + '개를 맞는 시대에.'), score >= deck.length - 1 ? BK.green : BK.coral)}
      {ans && spMsg(ans === g[1] ? t('Yes: ' + CMP_PERIODS[g[1]].short[0] + '.', '맞아요: ' + CMP_PERIODS[g[1]].short[1] + '.') : t('It is ' + CMP_PERIODS[g[1]].short[0] + '.', '정답은 ' + CMP_PERIODS[g[1]].short[1] + '.'), ans === g[1] ? BK.green : BK.coral)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        {ans && !fixed && !done && <button className="ghost-btn" style={spBtn} onClick={next}>{i + 1 < deck.length ? t('Next card →', '다음 카드 →') : t('Finish', '끝내기')}</button>}
        {done && !fixed && <button className="ghost-btn" style={spBtn} onClick={again}>{t('▶ Six new cards', '▶ 새 카드 여섯')}</button>}
      </div>
    </div>
  );
}
// ── step 5: know the composer: a card to fill in ──
const CC_FIELDS = [['name', 'Composer', '작곡가'], ['dates', 'Born – died', '생몰년'], ['where', 'Where they lived and worked', '살고 일한 곳'], ['period', 'Period', '시대'], ['works', 'Three other works', '다른 작품 셋'], ['from', 'Influenced by', '영향을 받은 사람'], ['to', 'Influenced', '영향을 준 사람']];
function MyComposerCard() {
  const [v, setV] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_composer_card') || '{}') || {}; } catch (e) { return {}; } });
  const set = (k, x) => { const n = { ...v, [k]: x }; setV(n); try { localStorage.setItem('pb_composer_card', JSON.stringify(n)); } catch (e) {} };
  const filled = CC_FIELDS.filter(([k]) => (v[k] || '').trim()).length;
  const inp = { width:'100%', minWidth:0, padding:'8px 8px', fontSize:14.5, fontWeight:700, border:'1.5px solid rgba(38,41,107,0.3)', borderRadius:8, color:BK.ink, background:'#fff', boxSizing:'border-box' };
  return (
    <div className="try-box" style={actBox} data-pm="composer">
      <div style={actTitle}>{t('My composer card', '나의 작곡가 카드')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>시험관은 작곡가의 <b>다른 작품</b>과 <b>음악적 영향</b>을 물을 수 있어요. 곡마다 카드 한 장. 작곡가 방(이야기 층)에서 찾아 채워요. 이 기기에 저장돼요.</> : <>The examiner may ask about the composer's <b>other works</b> and <b>musical influences</b>. One card for each piece. Find what you need in the Composers room (on the Stories floor), and fill it in. It is saved on this device.</>}</div>
      <div style={{display:'grid',gap:6}}>{CC_FIELDS.map(([k, en, ko]) => <label key={k} style={{display:'grid',gap:2,fontSize:11.5,fontWeight:900,color:BK.muted}}>{t(en, ko)}<input value={v[k] || ''} onChange={(e) => set(k, e.target.value)} style={inp}/></label>)}</div>
      {spMsg(filled === CC_FIELDS.length ? t('A full card: say it aloud without looking ✓', '다 채운 카드: 보지 않고 말해 봐요 ✓') : t(filled + ' of ' + CC_FIELDS.length + ' filled in', CC_FIELDS.length + '칸 중 ' + filled + '칸'), filled === CC_FIELDS.length ? BK.green : undefined)}
    </div>
  );
}
// the drill's form question: letters to a name
const FORM_Q = [['A B', 'binary'], ['A B A', 'ternary'], ['A B A C A', 'rondo'], ['Exposition, development, recapitulation', 'sonata'], ['Theme, var. 1, var. 2, var. 3', 'variations'], ['Minuet, trio, minuet', 'minuet']];
const FORM_N = { binary: ['Binary', '2부 형식'], ternary: ['Ternary', '3부 형식'], rondo: ['Rondo', '론도'], sonata: ['Sonata form', '소나타 형식'], variations: ['Theme and variations', '주제와 변주'], minuet: ['Minuet and trio', '미뉴에트와 트리오'] };

// ── the pictures on paper ──
const p78PicMap = () => lsRawPic('<rect x="4" y="12" width="72" height="20" rx="3" fill="#fff" stroke="#26296b" stroke-width="2"/><path d="M28 12 V32 M52 12 V32" stroke="#26296b" stroke-width="2"/><text x="16" y="27" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="900" fill="#26296b">A</text><text x="40" y="27" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="900" fill="#e4572e">B</text><text x="64" y="27" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="900" fill="#26296b">A</text>', [0, 0, 80, 44]);
const p78PicTonal = () => { const m = spMiniKeys(0, 12, { 1: 'cor', 3: 'cor', 6: 'cor', 8: 'cor', 10: 'cor' }); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };
const p78PicMvt = () => lsRawPic(['I', 'II', 'III'].map((x, i) => '<rect x="' + (4 + i * 25) + '" y="12" width="22" height="20" rx="3" fill="' + (i === 1 ? '#fbe3da' : '#fff') + '" stroke="' + (i === 1 ? '#e4572e' : '#26296b') + '" stroke-width="2"/><text x="' + (15 + i * 25) + '" y="26" text-anchor="middle" font-family="Georgia, serif" font-size="10" font-weight="900" fill="#26296b">' + x + '</text>').join(''), [0, 0, 80, 44]);
const p78PicGen = () => lsRawPic('<rect x="8" y="6" width="30" height="34" rx="3" fill="#fff" stroke="#26296b" stroke-width="2"/><rect x="42" y="6" width="30" height="34" rx="3" fill="#fff" stroke="#e4572e" stroke-width="2"/><path d="M14 16 H32 M14 22 H28 M48 16 H66 M48 22 H62" stroke="#26296b" stroke-width="1.6"/>', [0, 0, 80, 44]);
const p78PicComp = () => lsRawPic('<rect x="18" y="4" width="44" height="36" rx="3" fill="#fff" stroke="#26296b" stroke-width="2"/><circle cx="32" cy="17" r="6" fill="#26296b"/><path d="M42 14 H56 M42 20 H54 M24 30 H56" stroke="#e4572e" stroke-width="1.8"/>', [0, 0, 80, 44]);

function p78LbPages(scr = false) {
  const ch = 'pieces-78', fc = bkChapterNo('form'), cc = bkChapterNo('composers');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks = [[p78PicMap(), t('I draw the map of each piece: its sections, bars and keys', '곡마다 지도를 그려요: 부분, 마디, 조')], [p78PicTonal(), t('I point out where the key changes, or name its other tonal world', '조가 바뀌는 곳을 짚거나, 다른 음의 세계를 말해요')],
    [p78PicMvt(), t('I say how a movement fits the whole work', '한 악장이 작품 전체에 어떻게 들어맞는지 말해요')], [p78PicGen(), t('I name other genres of my piece\'s period', '내 곡의 시대의 다른 갈래를 말해요')], [p78PicComp(), t('I talk about the composer: other works and influences', '작곡가에 대해 말해요: 다른 작품과 영향')]];
  const toc = [[t('The map of my piece', '내 곡의 지도'), 2], [t('Keys, and other tonal worlds', '조, 그리고 다른 음의 세계'), 3], [t('One movement of a larger work', '큰 작품의 한 악장'), 4], [t('Other music of its time', '그 시대의 다른 음악'), 5], [t('My composer card', '나의 작곡가 카드'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const genStill = <div style={{display:'grid',gridTemplateColumns:scr ? '1fr 1fr' : 'repeat(5,1fr)',gap:8,width:'100%',maxWidth:780,margin:'0 auto'}}>{GEN_ERAS.map(e => <div key={e} style={{border:'1.5px solid rgba(38,41,107,0.3)',borderRadius:8,padding:'6px 6px',background:'#fff'}}><div style={{fontWeight:900,fontSize:scr ? 13 : 15,color:BK.ink}}>{t(CMP_PERIODS[e].short[0], CMP_PERIODS[e].short[1])}</div><div style={{fontSize:11,fontWeight:800,color:BK.muted,marginBottom:3}}>{CMP_PERIODS[e].years[0]}–{CMP_PERIODS[e].years[1] > 2025 ? '' : CMP_PERIODS[e].years[1]}</div>{GEN.filter(g => g[1] === e).map(g => <div key={g[0]} style={{fontSize:scr ? 11.5 : 13,color:BK.ink,lineHeight:1.35,marginTop:scr ? 0 : 3}}>{t(g[2], g[3])}</div>)}</div>)}</div>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('The general knowledge for Grades 7 and 8 (Manual of Syllabuses, the general knowledge table): by referring to the score of each List piece, the candidate names and explains notes, rests, signs, terms, its title and key; identifies key changes, or explains other tonal organisation (atonal, pentatonic, whole tone); explains form through a detailed structural analysis, and, for a movement from a larger work, shows a brief knowledge of its relationship to the other movements. From the score or from general knowledge: the period and its style; other genres typical of the period, not necessarily for the instrument (orchestral, choral); and the composer, their works and musical influences. Theory exams stop at Grade 6, so this chapter carries the knowing for Grades 7 and 8. Forms are in chapter ' + fc + ', composers and periods in chapter ' + cc + '.', '7·8급 일반 지식(실라버스 일반 지식 표): 리스트 곡마다 악보를 보며 음표, 쉼표, 기호, 용어, 제목, 조를 말하고 설명; 조가 바뀌는 곳을 짚거나 다른 음 조직(무조, 5음 음계, 온음 음계)을 설명; 자세한 구조 분석으로 형식을 설명하고, 큰 작품의 한 악장이면 다른 악장과의 관계를 짧게. 악보나 일반 지식으로: 시대와 양식; 그 시대에 흔한 다른 갈래(악기와 상관없이: 관현악, 합창); 작곡가, 그 작품과 음악적 영향. 이론 시험은 6급에서 끝나므로 이 챕터가 7·8급의 앎을 맡아요. 형식은 ' + fc + '장, 작곡가와 시대는 ' + cc + '장.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={120}><PmBar secs={PM_PRESETS.rondo} w={520}/></LbPic>
      <LbSay size={18}>{t('Grades 7 and 8 ask you to know your pieces inside out: their map, their keys, their place in a bigger work, their time, and their composer.', '7·8급은 내 곡을 속속들이 알기를 바라요: 지도, 조, 큰 작품 속 자리, 시대, 그리고 작곡가.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checks.map(([, x], i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The map of my piece', '내 곡의 지도')}
      teacher={<>{t('"Explain form, through a detailed structural analysis." With the score: mark the sections and their bar numbers, the return of themes, the cadences that close sections, and the key of each section; then talk through the map. The pad keeps one map per device; the Workbook has a blank map for each List piece.', '"자세한 구조 분석으로 형식을 설명." 악보로: 부분과 마디 번호, 주제가 돌아오는 곳, 부분을 닫는 종지, 부분마다 조를 표시하고, 그 지도로 설명해요. 패드는 기기마다 지도 하나를 저장해요; 워크북에 리스트 곡마다 빈 지도가 있어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={150}><div style={{display:'grid',gap:10,width:'100%',maxWidth:560,margin:'0 auto'}}>{['ternary', 'rondo'].map(k => <div key={k}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{t(PM_NAMES[k][0], PM_NAMES[k][1])}</div><PmBar secs={PM_PRESETS[k]} w={540}/></div>)}</div></LbPic>} live={<PieceMapMaker/>}/>
      <LbSay>{LANG === 'ko' ? <>부분마다 <b>글자</b>(같은 음악은 같은 글자), <b>마디</b>, <b>조</b>. 부분을 닫는 종지를 찾으면 경계가 보여요.</> : <>Each section gets <b>a letter</b> (the same music, the same letter), <b>its bars</b> and <b>its key</b>. Find the cadences that close the sections and the borders appear.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>내 곡의 처음 주제를 쳐요. 그 주제가 다시 오는 마디를 찾아요.</>, <>부분마다 마지막 종지를 쳐요. 무슨 조로 닫히나요?</>, <>지도를 보며 곡 전체를 선생님께 설명해요.</>]
        : [<>Play your piece's opening theme. Find the bars where it comes back.</>, <>Play the last cadence of each section. Which key does it close in?</>, <>Explain the whole piece to your teacher from the map.</>]}/>
      <LbRemember>{t('Letters, bars, keys.', '글자, 마디, 조.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Keys, and other tonal worlds', '조, 그리고 다른 음의 세계')}
      teacher={<>{t('"Identify any key changes that occur, or explain other type(s) of tonal organisation, e.g. atonal, pentatonic, whole tone." A key change shows as accidentals that keep coming and a cadence in the new key. The app plays a short tune in each world (written for the app); a 20th-century piece may be modal, pentatonic, whole tone or atonal.', '"일어나는 조바꿈을 짚거나, 다른 음 조직(예: 무조, 5음 음계, 온음 음계)을 설명." 조바꿈은 계속 나오는 임시표와 새 조의 종지로 보여요. 앱은 세계마다 짧은 선율을 들려줘요(앱을 위해 지은 것); 20세기 곡은 선법, 5음 음계, 온음 음계, 무조일 수 있어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={150}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:12,width:'100%',maxWidth:720,margin:'0 auto'}}>{['pen', 'wt', 'ato'].map(y => <div key={y}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{t(TW[y].en, TW[y].ko)}</div><SpKb lo={0} hi={11} W={scr ? 16 : 26} H={scr ? 52 : 84} lit={Object.fromEntries(TW[y].notes.map(n => [spPc(n), 'cor']))} names={{}} k={1}/></div>)}</div></LbPic>} live={<TonalPad/>}/>
      <LbSay>{LANG === 'ko' ? <>조바꿈은 <b>계속 나오는 새 임시표</b>와 <b>새 조의 종지</b>. 조가 아예 다른 세계도: 검은건반 다섯 음, 온음만 여섯 음, 집 없는 열두 음.</> : <>A key change shows as <b>new accidentals that keep coming</b> and <b>a cadence in the new key</b>. Some music lives in another world: five black-key notes, six notes a tone apart, twelve notes with no home.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>내 곡에서 새 임시표가 계속 나오는 곳에 동그라미.</>, <>그 부분의 종지를 쳐요: 어느 조?</>, <>검은건반만으로, 온음만으로 짧게 지어 봐요.</>]
        : [<>Circle the places in your piece where new accidentals keep coming.</>, <>Play the cadence there: which key?</>, <>Make up a few bars on the black keys only, then with whole tones only.</>]}/>
      <LbRemember>{t('New accidentals, then a cadence: a new key.', '새 임시표, 그다음 종지: 새 조.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('One movement of a larger work', '큰 작품의 한 악장')}
      teacher={<>{t('"Where the piece is a movement from a larger work: brief knowledge of its relationship to the other movements in the work is expected" (Grades 7 and 8). Which movement it is, how many there are, their speeds and characters, the key relationships. The plans in the app are the usual ones (a Classical sonata fast–slow–fast; a symphony with a minuet or scherzo third; a Baroque suite allemande, courante, sarabande, gigue); individual works differ, so check each piece.', '"곡이 큰 작품의 한 악장이면: 다른 악장들과의 관계를 짧게 알아야 해요"(7·8급). 몇 번째 악장인지, 모두 몇 개인지, 빠르기와 성격, 조의 관계. 앱의 설계는 흔한 것(고전 소나타 빠르게–느리게–빠르게; 셋째가 미뉴에트나 스케르초인 교향곡; 알망드, 쿠랑트, 사라방드, 지그의 바로크 모음곡); 작품마다 다르니 곡마다 확인해요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={130}><div style={{display:'grid',gap:8,width:'100%',maxWidth:560,margin:'0 auto'}}>{['sonata', 'suite'].map(k => <div key={k} style={{display:'flex',gap:6,alignItems:'center'}}><span style={{width:scr ? 120 : 150,fontSize:scr ? 12.5 : 15,fontWeight:900,color:BK.ink}}>{t(MV[k].en, MV[k].ko)}</span>{MV[k].mv.map(([en, ko], j) => <span key={j} style={{flex:1,padding:scr ? '6px 3px' : '12px 4px',borderRadius:6,border:'1.5px solid rgba(38,41,107,0.3)',textAlign:'center',fontSize:scr ? 12 : 14.5,fontWeight:900,color:BK.ink,background:'#fff'}}>{t(en, ko)}</span>)}</div>)}</div></LbPic>} live={<MovementPad/>}/>
      <LbSay>{LANG === 'ko' ? <>내 악장은 <b>몇 번째</b>? 다른 악장은 <b>빠른가, 느린가</b>? <b>어떤 조</b>? 세 문장이면 충분해요.</> : <>Which movement is mine? Are the others <b>fast or slow</b>? <b>In which keys</b>? Three sentences are enough.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>내 곡이 들어 있는 작품의 다른 악장을 들어요(녹음).</>, <>악장마다 빠르기와 조를 적어요.</>, <>내 악장이 어디에, 왜 그런 성격인지 말해요.</>]
        : [<>Listen to the other movements of the work your piece comes from (a recording).</>, <>Write each movement's speed and key.</>, <>Say where yours sits, and why it has its character.</>]}/>
      <LbRemember>{t('Which one, how many, fast or slow.', '몇 번째, 몇 개, 빠른가 느린가.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Other music of its time', '그 시대의 다른 음악')}
      teacher={<>{t('"Knowledge of other genres typical of the period but not necessarily instrument-specific is also expected, e.g. orchestral music, choral music." The cards are examples of genres typical of each period (the period dates are the app\'s, as in the Composers room); please check them and add the genres your students meet.', '"악기와 상관없이 그 시대에 흔한 다른 갈래(예: 관현악, 합창)도 알아야 해요." 카드는 시대마다 흔한 갈래의 예(시대 연도는 작곡가 방처럼 앱의 것); 확인해 주시고, 학생이 만나는 갈래를 더해 주세요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={170}>{genStill}</LbPic>} live={<GenresPad/>}/>
      <LbSay>{LANG === 'ko' ? <>내 곡이 쓰일 때 다른 사람들은 무엇을 들었을까요? 교회의 오라토리오, 궁전의 교향곡, 거실의 녹턴, 극장의 발레.</> : <>When your piece was new, what else were people hearing? Oratorios in church, symphonies in palaces, nocturnes in the living room, ballets in the theatre.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>내 곡의 시대를 말해요.</>, <>그 시대의 다른 갈래 둘을 말하고, 한 곡씩 들어요.</>, <>내 곡과 닮은 점 하나를 말해요.</>]
        : [<>Say your piece's period.</>, <>Name two other genres of that time, and listen to one piece of each.</>, <>Say one thing they share with your piece.</>]}/>
      <LbRemember>{t('My piece, and the music around it.', '내 곡, 그리고 그 둘레의 음악.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('My composer card', '나의 작곡가 카드')}
      teacher={<>{t('"Knowledge of the composers of each of the pieces being presented, in particular relating to their works and musical influences, is expected." One card per piece: dates, where they worked, period, three other works, who influenced them and whom they influenced. The Composers room (chapter ' + cc + ') has the period worlds.', '"연주하는 곡마다 작곡가를, 특히 그 작품과 음악적 영향에 관해 알아야 해요." 곡마다 카드 한 장: 생몰년, 일한 곳, 시대, 다른 작품 셋, 영향을 받은 사람과 준 사람. 작곡가 방(' + cc + '장)에 시대의 세계가 있어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gap:scr ? 4 : 10,width:'100%',maxWidth:scr ? 460 : 580,margin:'0 auto'}}>{CC_FIELDS.map(([k, en, ko]) => <div key={k} style={{display:'grid',gridTemplateColumns:scr ? '160px 1fr' : '210px 1fr',gap:6,alignItems:'end',fontSize:scr ? 12.5 : 15,fontWeight:800,color:BK.ink}}><span>{t(en, ko)}</span><span style={{borderBottom:'1.5px solid rgba(38,41,107,0.4)',height:scr ? 16 : 24}}/></div>)}</div></LbPic>} live={<MyComposerCard/>}/>
      <LbSay>{LANG === 'ko' ? <>작곡가도 누군가에게서 배웠고, 누군가를 가르쳤어요. <b>누구에게서, 누구에게로</b>: 그 줄을 알면 곡이 더 잘 들려요.</> : <>Composers learned from someone and passed it on to someone. <b>From whom, to whom</b>: know that line and the piece speaks more clearly.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>카드를 채워요.</>, <>그 작곡가의 다른 곡 하나를 들어요.</>, <>보지 않고 카드를 말해요.</>]
        : [<>Fill in the card.</>, <>Listen to another piece by the same composer.</>, <>Say the card without looking.</>]}/>
      <LbRemember>{t('From whom, to whom.', '누구에게서, 누구에게로.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('For each List piece, as the examiner would ask: the map, the keys or tonal world, its place in the work, the period and its other genres, the composer. Ask from the score; the child answers in sentences.', '리스트 곡마다 시험관처럼: 지도, 조나 음의 세계, 작품 속 자리, 시대와 다른 갈래, 작곡가. 악보를 보며 묻고, 아이는 문장으로 대답해요.')}</>}>
      <LbSay>{t('For each piece, tick each one: not yet, nearly, or got it!', '곡마다 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey="pb_p78_five"/>}/>
    </LbPage>,
  ];
}
function Pieces78LessonBook() { return <>{p78LbPages(false)}</>; }
function P78Learn({ onStart }) {
  const pages = p78LbPages(true), opener = pages[0];
  return (
    <Lesson id="pieces-78" title={bkChapterName('pieces-78')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="pieces-78"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
const P78_LEVELS = [
  { n: 1, label: 'Name the form', kind: 'form', time: 15 },
  { n: 2, label: 'Which tonal world?', kind: 'tonal', time: 20 },
  { n: 3, label: 'Which movement?', kind: 'mvt', time: 15 },
  { n: 4, label: 'Which period?', kind: 'genre', time: 12 },
];
Object.assign(LEVEL_KO, { 'Name the form': '형식 이름', 'Which tonal world?': '어떤 음의 세계?', 'Which movement?': '어느 악장?', 'Which period?': '어느 시대?' });
function genP78Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'form') { let f, g = 0; do { f = pick(FORM_Q); } while (prev && prev.key === f[1] && g++ < 10); return { kind, f, answer: f[1], choices: shuffle(Object.keys(FORM_N)).slice(0, 4).concat([f[1]]).filter((x, i, a) => a.indexOf(x) === i).slice(-4), key: f[1], uid }; }
  if (kind === 'tonal') { let id, g = 0; do { id = pick(TW_IDS); } while (prev && prev.key === id && g++ < 10); return { kind, id, answer: id, choices: TW_IDS.slice(), key: id, uid }; }
  if (kind === 'mvt') { let w, m, g = 0; do { w = pick(['sonata', 'symphony', 'suite']); m = Math.floor(Math.random() * MV[w].mv.length); } while (prev && prev.key === w + m && g++ < 10); return { kind, w, m, answer: m, choices: MV[w].mv.map((_, j) => j), key: w + m, uid }; }
  let gg, g = 0; do { gg = pick(GEN); } while (prev && prev.key === gg[0] && g++ < 10); return { kind: 'genre', gg, answer: gg[1], choices: GEN_ERAS.slice(), key: gg[0], uid };
}
function P78Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  useEffect(() => { if (q.kind !== 'tonal') return; const id = setTimeout(() => twPlay(q.id), 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  const grid = (cols, items) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:14,fontWeight:900,lineHeight:1.2}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  let title, body;
  if (q.kind === 'form') { title = t('Which form is this?', '어떤 형식일까요?'); body = <><div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:20,fontWeight:900,color:BK.ink,margin:'8px 0'}}>{q.f[0]}</div>{grid(2, q.choices.map(c => [c, t(FORM_N[c][0], FORM_N[c][1])]))}</>; }
  else if (q.kind === 'tonal') { title = t('Listen: which tonal world?', '들어요: 어떤 음의 세계?'); body = <><div style={{textAlign:'center'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={() => twPlay(q.id)}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>{grid(3, q.choices.map(c => [c, t(TW[c].en, TW[c].ko)]))}</>; }
  else if (q.kind === 'mvt') { const W = MV[q.w]; title = q.w === 'suite' ? t('In a Baroque suite, which dance is ' + W.mv[q.m][2] + '?', '바로크 모음곡에서 ' + W.mv[q.m][3] + '인 춤곡은?') : t('In a ' + W.en.toLowerCase() + ', which movement is usually ' + W.mv[q.m][0].toLowerCase() + (W.mv[q.m][2] ? ' (' + W.mv[q.m][2] + ')' : '') + '?', W.ko + '에서 대개 ' + W.mv[q.m][1] + (W.mv[q.m][3] ? '(' + W.mv[q.m][3] + ')' : '') + '인 악장은?');
    body = grid(W.mv.length, q.choices.map(c => [c, q.w === 'suite' ? t(W.mv[c][0], W.mv[c][1]) : ['I', 'II', 'III', 'IV'][c]])); }
  else { title = t('Which period does this genre belong to?', '이 갈래는 어느 시대의 것일까요?'); body = <><div style={{textAlign:'center',fontFamily:LB_SERIF,fontSize:20,fontWeight:900,color:BK.ink,margin:'8px 0'}}>{t(q.gg[2], q.gg[3])}</div>{grid(2, q.choices.map(e => [e, t(CMP_PERIODS[e].short[0], CMP_PERIODS[e].short[1])]))}</>; }
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {body}
  </div>);
}
const p78AnswerLabel = (q) => (q.kind === 'form' ? t(FORM_N[q.answer][0], FORM_N[q.answer][1]) : q.kind === 'tonal' ? t(TW[q.answer].en, TW[q.answer].ko) : q.kind === 'mvt' ? (q.w === 'suite' ? t(MV.suite.mv[q.answer][0], MV.suite.mv[q.answer][1]) : ['I', 'II', 'III', 'IV'][q.answer]) : t(CMP_PERIODS[q.answer].short[0], CMP_PERIODS[q.answer].short[1]));
Object.assign(PIECES_78_DRILL, { levels: P78_LEVELS, generate: genP78Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: p78AnswerLabel, Question: P78Question, Learn: P78Learn });
function P78Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="pieces-78" teacher>{content}</WbPage>);
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('pieces-78')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>The general knowledge for Grades 7 and 8, from the Manual's table. The Workbook has a "My piece" sheet for each List piece: a map, the keys, the period, the composer. The genre lists and movement plans are textbook knowledge: please check them against the works your students play.</div>
    <TcBlock page={2} title="The map of my piece" answers={<>{tcAns('LOOK FOR', ['returning themes', 'cadences that close sections', 'the key of each section', 'bar numbers'], null)}</>}
      watch="A map with letters but no bars or keys. Ask “in which bar does B start, and in which key?”"
      say="“Letters, bars, keys.”"/>
    <TcBlock page={3} title="Keys, and other tonal worlds" answers={<>{tcAns('THE WORLDS', ['pentatonic: five notes, no semitones', 'whole tone: six notes a tone apart', 'atonal: no home key'], null)}</>}
      watch="Every accidental called a key change. A key change keeps its new accidentals and closes with a cadence in the new key."
      say="“New accidentals, then a cadence: a new key.”"/>
    <TcBlock page={4} title="One movement of a larger work" answers={<>{tcAns('SAY', ['which movement, of how many', 'the others: fast or slow, and their keys', 'what this movement brings to the whole'], null)}</>}
      watch="Knowing the movement but not the others. Listen to the whole work together once."
      say="“Which one, how many, fast or slow.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="Other music of its time" answers={<>{tcAns('THE CARDS', GEN_ERAS.map(e => CMP_PERIODS[e].short[0] + ': ' + GEN.filter(g => g[1] === e).map(g => g[2]).join(', ')), null)}</>}
      watch="Genres named without an example. Ask for one piece and its composer."
      say="“My piece, and the music around it.”"/>
    <TcBlock page={6} title="My composer card" answers={<>{tcAns('THE CARD', CC_FIELDS.map(f => f[1]), null)}</>}
      watch="Influences as a list of names. Ask what was passed on: a form, a sound, a way of writing for the piano."
      say="“From whom, to whom.”"/>
    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>For each List piece, ask from the score as the examiner would. The child answers in sentences, pointing at the score.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['pieces-78'] = P78Teacher;
function P78Workbook({ startNo = 1 }) {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="pieces-78">{content}</WbPage>);
  const line = (lab, w, h = 30) => <div style={{display:'grid',gridTemplateColumns:(w || 170) + 'px 1fr',gap:8,alignItems:'end',fontSize:12.5,fontWeight:800,color:BK.ink,margin:'4px 0'}}><span>{lab}</span><span style={{borderBottom:'1.5px solid rgba(38,41,107,0.45)',height:h}}/></div>;
  const sheet = (n) => <>
    <WbTop step={1}/>
    <Part kind="together" title={'My piece ' + n} how="One sheet for each List piece. Fill it in with the score open, then say it aloud.">
      {line('Title')}{line('Composer')}{line('Key(s)')}
      <div style={{fontSize:12,fontWeight:900,color:BK.ink,margin:'8px 0 4px'}}>The map: a letter, the bars and the key of each section</div>
      <div style={{display:'flex',border:'1.5px solid ' + BK.ink,borderRadius:6,height:110,background:'#fff'}}>{[0, 1, 2, 3, 4, 5].map(i => <div key={i} style={{flex:1,borderLeft:i ? '1.5px dashed rgba(38,41,107,0.35)' : 'none'}}/>)}</div>
      {line('Key changes or tonal world', 0, 44)}{line('A movement of (work, which movement)', 0, 44)}{line('Period and its style', 0, 44)}{line('Other genres of the period', 0, 44)}{line('Other works by the composer', 0, 44)}{line('Influences (from whom, to whom)', 0, 44)}
    </Part>
    <Faces/>
  </>;
  P(sheet(1)); P(sheet(2)); P(sheet(3));
  P(<P78PaperCheck/>);
  return <>{pages}</>;
}
function P78PaperCheck() {
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'Name the form')}
    <BkGrid cols={2} gap="6px 8px">{[FORM_Q[1], FORM_Q[2], FORM_Q[3], FORM_Q[5]].map((f, i) => <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:4,padding:'14px 2px 2px',fontSize:12,fontWeight:800,color:BK.ink}}>{f[0]}{bkBox(170, 22)}</div></BkCell>)}</BkGrid>
    {bkSec('B', 'Which tonal world? (major, minor, pentatonic, whole tone, atonal)')}
    <BkGrid cols={2} gap="6px 8px">{[['Five notes, no semitones'], ['Six notes, each a tone apart'], ['No home key; all twelve notes equal'], ['A home note and a raised 7th']].map(([d], i) => <BkCell key={i} n={i + 5}><div style={{display:'grid',gap:4,padding:'14px 2px 2px',fontSize:12,fontWeight:800,color:BK.ink}}>{d}{bkBox(150, 22)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'Which period? (Baroque, Classical, Romantic, Modern, Contemporary)')}
    <BkGrid cols={4} gap="6px 8px">{['oratorio', 'quartet', 'lied', 'minimal'].map((id, i) => <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:4,padding:'14px 0 0',justifyItems:'center',fontSize:11.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>{GEN.find(g => g[0] === id)[2]}{bkBox(90, 22)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'My piece in one sentence each: its form, its key, its period')}
    {[13, 14, 15].map(n => <div key={n} style={{display:'flex',gap:8,alignItems:'end',fontSize:12,fontWeight:800,color:BK.ink,margin:'6px 0'}}><span>{n}.</span><span style={{flex:1,borderBottom:'1.5px solid rgba(38,41,107,0.45)',height:18}}/></div>)}
  </div>;
}
WORKBOOKS['pieces-78'] = P78Workbook;
'''
rep("""WORKBOOKS['arps-7'] = A7Workbook;""", """WORKBOOKS['arps-7'] = A7Workbook;""" + CH)

HOME = r'''
// ══ Build BW: Knowing Your Pieces, Grades 7 and 8 on the Home (Pieces, Melody and form) ══
LBH_FN['pieces-78'] = (s) => p78LbPages(s);
const p78HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'c-map', 'piece', en, ko, benEn, bko, lbhSpec('pieces-78', i, { make }));
const p78Q = (kind) => (n, prev) => { const L = P78_LEVELS.find(x => x.kind === kind), q = genP78Question(L, prev);
  const lab = (c) => (kind === 'form' ? t(FORM_N[c][0], FORM_N[c][1]) : kind === 'tonal' ? t(TW[c].en, TW[c].ko) : kind === 'genre' ? t(CMP_PERIODS[c].short[0], CMP_PERIODS[c].short[1]) : q.w === 'suite' ? t(MV.suite.mv[c][0], MV.suite.mv[c][1]) : ['I', 'II', 'III', 'IV'][c]);
  const prompt = kind === 'form' ? ['Which form: ' + q.f[0] + '?', '어떤 형식: ' + q.f[0] + '?'] : kind === 'tonal' ? ['Listen: which tonal world?', '들어요: 어떤 음의 세계?'] : kind === 'genre' ? ['Which period: ' + q.gg[2] + '?', '어느 시대: ' + q.gg[3] + '?'] : [MV[q.w].en + ': which movement is ' + MV[q.w].mv[q.m][0].toLowerCase() + '?', MV[q.w].ko + ': ' + MV[q.w].mv[q.m][1] + '인 악장은?'];
  return { kind: 'choice', cols: kind === 'tonal' ? 3 : 2, key: q.key, prompt, opts: q.choices.map(c => ({ id: c, label: () => lab(c) })), ans: q.answer, ok: (v) => v === q.answer, play: kind === 'tonal' ? () => twPlay(q.id) : undefined, fig: () => ({ mid: null }),
    yes: ['Yes: ' + lab(q.answer) + '.', '맞아요: ' + lab(q.answer) + '.'], no: ['It is ' + lab(q.answer) + '.', '정답은 ' + lab(q.answer) + '.'] }; };
p78HomeAdd('p78-form', 1, 'Name the form', '형식 이름', 'Binary, ternary, rondo, sonata form, variations, minuet and trio.', '2부, 3부, 론도, 소나타 형식, 변주, 미뉴에트와 트리오.', p78Q('form'));
p78HomeAdd('p78-tonal', 2, 'Keys, and other tonal worlds', '조, 그리고 다른 음의 세계', 'Major, minor, pentatonic, whole tone or atonal?', '장조, 단조, 5음, 온음, 무조?', p78Q('tonal'));
p78HomeAdd('p78-mvt', 3, 'One movement of a larger work', '큰 작품의 한 악장', 'Where does the slow movement go? And the minuet?', '느린 악장은 어디에? 미뉴에트는?', p78Q('mvt'));
p78HomeAdd('p78-genre', 4, 'Other music of its time', '그 시대의 다른 음악', 'Which period does each genre belong to?', '갈래마다 어느 시대의 것일까?', p78Q('genre'));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""'fmx-build', 'fmx-forms5', 'fmx-sonata', 'fmx-fugue', 'same-or-new', 'binary-ternary-spot', 'form-shapes', 'rondo-refrain', 'form-builder'], check: 'form' },""",
    """'fmx-build', 'fmx-forms5', 'fmx-sonata', 'fmx-fugue', 'same-or-new', 'binary-ternary-spot', 'form-shapes', 'rondo-refrain', 'form-builder'], check: 'form' },
    { id: 'c-pieces', en: 'Knowing your pieces, Grades 7 and 8', ko: '내 곡 알기, Grade 7과 8', lessons: ['p78-form', 'p78-tonal', 'p78-mvt', 'p78-genre', 'mk-map'], check: 'pieces-78' },   // Build BW""")
rep("""  set('7', 'a7-walk a7-arp a7-inv a7-dim mk-accomp');   // Build BV: Arpeggios and Progressions, Grade 7""", """  set('7', 'a7-walk a7-arp a7-inv a7-dim mk-accomp');   // Build BV: Arpeggios and Progressions, Grade 7
  set('7', 'p78-form p78-tonal p78-mvt p78-genre mk-map');   // Build BW: Knowing Your Pieces, Grades 7 and 8""")
rep("""  { id: 'mk-cad', ch: 'listen-6',""", """  { id: 'mk-map', ch: 'pieces-78', title: 'The map of my piece', blurb: 'Sections, bars and keys of a piece you play, drawn as a map.', C: () => <PieceMapMaker/> },   // Build BW
  { id: 'mk-cad', ch: 'listen-6',""")
rep("""  'mk-cad': ['나만의 끝 만들기',""", """  'mk-map': ['내 곡의 지도', '내가 치는 곡의 부분, 마디, 조를 지도로 그려요.'],
  'mk-cad': ['나만의 끝 만들기',""")
rep("""'mk-cad': ['chords', 3, 3, 'game ear'],""", """'mk-cad': ['chords', 3, 3, 'game ear'], 'mk-map': ['melody', 3, 3, 'write show'],""")
rep("""'mk-cad': 'p-chords',""", """'mk-cad': 'p-chords', 'mk-map': 'c-map',""")
rep("""  'mk-cad': () => (\n""", """  'mk-map': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><rect x="3" y="8" width="18" height="9" rx="1.5" fill="#fefbf3"/><path d="M9 8 V17 M15 8 V17" stroke="#3b4fa8" strokeWidth="1.2"/><rect x="9.6" y="8.6" width="4.8" height="7.8" fill="#e9a83a"/></svg>
  ),
  'mk-cad': () => (\n""")
rep("""const LESSON_BOOKS = { 'arps-7': Arps7LessonBook,""", """const LESSON_BOOKS = { 'pieces-78': Pieces78LessonBook, 'arps-7': Arps7LessonBook,""")
rep("""const LB_PAGE_FNS = { 'arps-7': a7LbPages,""", """const LB_PAGE_FNS = { 'pieces-78': p78LbPages, 'arps-7': a7LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"pieces-78": "<rect x=\\"4\\" y=\\"12\\" width=\\"40\\" height=\\"18\\" rx=\\"2\\"/><path d=\\"M17 12 V30 M31 12 V30\\"/><rect x=\\"17.6\\" y=\\"12.6\\" width=\\"12.8\\" height=\\"16.8\\" fill=\\"#fbe3da\\" stroke=\\"none\\"/><text x=\\"10.5\\" y=\\"25\\" text-anchor=\\"middle\\" font-size=\\"11\\" font-weight=\\"900\\" fill=\\"#26296b\\" stroke=\\"none\\" font-family=\\"Georgia, serif\\">A</text><text x=\\"24\\" y=\\"25\\" text-anchor=\\"middle\\" font-size=\\"11\\" font-weight=\\"900\\" fill=\\"#e4572e\\" stroke=\\"none\\" font-family=\\"Georgia, serif\\">B</text><text x=\\"37.5\\" y=\\"25\\" text-anchor=\\"middle\\" font-size=\\"11\\" font-weight=\\"900\\" fill=\\"#26296b\\" stroke=\\"none\\" font-family=\\"Georgia, serif\\">A</text>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
