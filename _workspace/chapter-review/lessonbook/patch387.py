# Phase 387: chapter 2 applied -- the book registered, the app lesson is the book on screen,
# the drill gets a naming level, the chapter is renamed everywhere, and the printed Lesson Book
# loses its teacher strips (Sohyun 2026-10-09: teacher content lives in the Teacher copy; the
# app's teacher view keeps it). Run from the repo root: python3 _workspace/chapter-review/lessonbook/patch387.py
import os, sys
p = 'drills.src.html'
s = open(p, encoding='utf-8').read()
done = []
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    assert c == n, f"{what}: expected {n}, got {c}"
    s = s.replace(a, b)
    done.append(what)

# ── 1. the printed Lesson Book loses the TEACHER strip (the app's teacher view keeps page.props.teacher)
rep("""      {teacher && <div data-lb-teacher style={{display:'flex',gap:12,alignItems:'center',borderTop:'1.3px dashed ' + BK.line,marginTop:12,paddingTop:9}}>
        <span style={{flex:'0 0 auto',fontSize:9.5,fontWeight:900,letterSpacing:'0.06em',color:'#fff',background:BK.ink,borderRadius:4,padding:'3px 7px'}}>TEACHER</span>
        <div style={{flex:1,fontSize:11.8,color:BK.ink,lineHeight:1.45}}>{teacher}</div>
        {qr && <div style={{flex:'0 0 auto',display:'flex',alignItems:'center',gap:6}}><span style={{fontSize:9,color:BK.muted,textAlign:'right',lineHeight:1.2,width:48}}>Try it in the app</span><QR url={qr} size={46}/></div>}
      </div>}
""",
"""      {/* Sohyun 2026-10-09: teacher content prints in the Teacher copy, not in the Lesson Book;
          on screen it still shows in the teacher view (LbScreenPage). */}
""", 'LbPage: no printed teacher strip')

# ── 2. chapter 1 Teacher copy absorbs what its lesson-book strips said and the copy did not
rep("<div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Each workbook page faces its Lesson Book page. Every answer here should also be tried at the piano -- the paper is only the reminder.</div>",
    "<div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>Each workbook page faces its Lesson Book page. Every answer here should also be tried at the piano -- the paper is only the reminder. This chapter is the base for every other one: its five checks come before every time at the piano, at every level.</div>",
    'ch1 teacher intro: base-chapter line')
rep('watch="Right hand first, then left hand. Move on to the next tune only when the hand stays round. Relaxed, never squeezed tight."',
    'watch="Right hand first, then left hand, then together if it is easy. Any five white keys near the middle will do; the letter names come with the Note Names chapter. Move on to the next tune only when the hand stays round. Relaxed, never squeezed tight."',
    'ch1 teacher p6: strip content')
rep("<div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>Score each concept on its own (4 marks each, pass 3+). Then check the posture at the piano, not just on paper.</div>",
    "<div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>At the start of each lesson the student says the five checks out loud while doing them; you only correct. Score each concept on its own (4 marks each, pass 3+). Then check the posture at the piano, not just on paper.</div>",
    'ch1 teacher p7: five-checks-aloud line')

# ── 3. the key tints follow the book (pale coral under the small roof, pale navy under the big)
rep("const GROUP_TINT = { two: '#fbe3da', three: '#e4eeea' };",
    "const GROUP_TINT = { two: '#fbe9e2', three: '#e9eaf4' };   // the book's membership tints (Phase 387)",
    'GROUP_TINT pastel coral/navy')

# ── 4. KeyHouses: optional mode chips + brand colours (coral/navy, pastel fills)
rep("function KeyHouses() {\n  const OCT = 2;", "function KeyHouses({ modes }) {\n  const OCT = 2;", 'KeyHouses modes param')
rep("{[['houses', t('houses', '집')], ['small', 'C D E'], ['big', 'F G A B']].map(([k, l]) =>",
    "{[['houses', t('houses', '집')], ['small', 'C D E'], ['big', 'F G A B']].filter(([k]) => !modes || modes.includes(k)).map(([k, l]) =>",
    'KeyHouses mode filter')
rep("const mid = (h.x1 + h.x2) / 2, on = lit === i, col = h.kind === 'small' ? '#b8801f' : '#2e8a6e';",
    "const mid = (h.x1 + h.x2) / 2, on = lit === i, col = h.kind === 'small' ? '#e4572e' : '#26296b';",
    'KeyHouses house colours')
rep("""        <span style={{color:'#b8801f'}}>{t('▲ small house = 2', '▲ 작은 집 = 2')}</span><span style={{color:'#2e8a6e'}}>{t('▲ big house = 3', '▲ 큰 집 = 3')}</span>""",
    """        <span style={{color:'#e4572e'}}>{t('▲ small house = 2', '▲ 작은 집 = 2')}</span><span style={{color:'#26296b'}}>{t('▲ big house = 3', '▲ 큰 집 = 3')}</span>""",
    'KeyHouses legend colours')

# ── 5. HighLowGame: a pitch-only mode for the chapter step (loud/soft left the chapter)
rep("function HighLowGame() {\n  const [kind, setKind] = useState('pitch'); // pitch | volume",
    "function HighLowGame({ pitchOnly }) {\n  const [kind, setKind] = useState('pitch'); // pitch | volume",
    'HighLowGame pitchOnly param')
rep("""        <div style={{display:'flex',gap:4}}>{[['pitch', t('high/low', '높게/낮게')], ['volume', t('loud/soft', '크게/작게')]].map(([k, l]) => <button key={k} className={'chip' + (kind === k ? ' active' : '')} style={{padding:'3px 9px',fontSize:12}} onClick={() => { setKind(k); setQ(null); setAns(null); }}>{l}</button>)}</div>""",
    """        {!pitchOnly && <div style={{display:'flex',gap:4}}>{[['pitch', t('high/low', '높게/낮게')], ['volume', t('loud/soft', '크게/작게')]].map(([k, l]) => <button key={k} className={'chip' + (kind === k ? ' active' : '')} style={{padding:'3px 9px',fontSize:12}} onClick={() => { setKind(k); setQ(null); setAns(null); }}>{l}</button>)}</div>}""",
    'HighLowGame hide volume chip')

# ── 6. WholePiano in the brand colours
rep("const col = { small: '#b8801f', big: '#2e8a6e' };", "const col = { small: '#e4572e', big: '#26296b' };", 'WholePiano colours')

# ── 7. FiveChecks376: per-chapter storage + live-drawn icons
rep("function FiveChecks376({ rows }) {\n  const [st, setSt] = useState(() => { try { return JSON.parse(localStorage.getItem(FIVE_KEY)) || {}; } catch (e) { return {}; } });",
    "function FiveChecks376({ rows, storeKey }) {\n  const SK = storeKey || FIVE_KEY;\n  const [st, setSt] = useState(() => { try { return JSON.parse(localStorage.getItem(SK)) || {}; } catch (e) { return {}; } });",
    'FiveChecks376 storeKey')
rep("try { localStorage.setItem(FIVE_KEY, JSON.stringify(nx)); } catch (e) {}", "try { localStorage.setItem(SK, JSON.stringify(nx)); } catch (e) {}", 'FiveChecks376 set SK')
rep("try { localStorage.removeItem(FIVE_KEY); } catch (e) {}", "try { localStorage.removeItem(SK); } catch (e) {}", 'FiveChecks376 remove SK')
rep("<div style={{flex:'0 0 64px',display:'flex',justifyContent:'center'}}><PbArt name={a} h={a === 'chk-hand' ? 38 : 52}/></div>",
    "<div style={{flex:'0 0 64px',display:'flex',justifyContent:'center'}}>{typeof a === 'string' ? <PbArt name={a} h={a === 'chk-hand' ? 38 : 52}/> : <PenArt shapes={a.shapes} vb={a.vb} style={{width:64}}/>}</div>",
    'FiveChecks376 live icons')

# ── 8. the black-key songs: finger rows (a2), both hands (a4), two new famous tunes (q3)
rep("""const BLACK_SONGS = {
  hotcross: { get title() { return t('Hot Cross Buns', '핫 크로스 번'); }, get chip() { return t('Hot Cross', '핫 크로스 번'); }, keys: [10, 8, 6, 10, 8, 6, 6, 6, 6, 6, 8, 8, 8, 8, 10, 8, 6], durs: [1, 1, 2, 1, 1, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1, 2] },
  mary: { get title() { return t('Mary Had a Little Lamb', '떴다 떴다 비행기'); }, get chip() { return t('Mary Had', '떴다 떴다 비행기'); }, keys: [10, 8, 6, 8, 10, 10, 10, 8, 8, 8, 10, 13, 13, 10, 8, 6, 8, 10, 10, 10, 10, 8, 8, 10, 8, 6], durs: [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4] },
};""",
"""// Fingers on the black keys (Sohyun 2026-10-09): both hands, 2 3 4 first -- left hand 3-2 on the
// small roof below, right hand 2-3-4 on the big roof; Mary's two high notes take R5 (her note:
// 1 and 5 properly arrive with C position). Finger rows replace the old note-name row (A2).
const BLACK_SONGS = {
  hotcross: { get title() { return t('Hot Cross Buns', '핫 크로스 번'); }, get chip() { return t('Hot Cross', '핫 크로스 번'); },
    keys: [10, 8, 6, 10, 8, 6, 6, 6, 6, 6, 8, 8, 8, 8, 10, 8, 6], durs: [1, 1, 2, 1, 1, 2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1, 2],
    f: ['R4', 'R3', 'R2', 'R4', 'R3', 'R2', 'R2', 'R2', 'R2', 'R2', 'R3', 'R3', 'R3', 'R3', 'R4', 'R3', 'R2'] },
  mary: { get title() { return t('Mary Had a Little Lamb', '떴다 떴다 비행기'); }, get chip() { return t('Mary Had', '떴다 떴다 비행기'); },
    keys: [10, 8, 6, 8, 10, 10, 10, 8, 8, 8, 10, 13, 13, 10, 8, 6, 8, 10, 10, 10, 10, 8, 8, 10, 8, 6], durs: [1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4],
    f: ['R4', 'R3', 'R2', 'R3', 'R4', 'R4', 'R4', 'R3', 'R3', 'R3', 'R4', 'R5', 'R5', 'R4', 'R3', 'R2', 'R3', 'R4', 'R4', 'R4', 'R4', 'R3', 'R3', 'R4', 'R3', 'R2'] },
  oldmac: { get title() { return t('Old MacDonald', '올드 맥도날드'); }, get chip() { return t('Old MacDonald', '올드 맥도날드'); },
    keys: [6, 6, 6, 1, 3, 3, 1, 10, 10, 8, 8, 6], durs: [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3],
    f: ['R2', 'R2', 'R2', 'L3', 'L2', 'L2', 'L3', 'R4', 'R4', 'R3', 'R3', 'R2'] },
  rain: { get title() { return t('Rain Rain Go Away', '레인 레인 고 어웨이'); }, get chip() { return t('Rain Rain', '레인 레인'); },
    keys: [13, 13, 10, 13, 10, 13, 13, 10, 15, 13, 13, 10], durs: [1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 2],
    f: ['R3', 'R3', 'R2', 'R3', 'R2', 'R3', 'R3', 'R2', 'R4', 'R3', 'R3', 'R2'] },
};""",
    'BLACK_SONGS: fingers + Old MacDonald + Rain Rain')
rep("""      <div style={actNote}>{LANG === 'ko' ? <>아직 악보는 읽지 않아요 -- 큰 집만 써요. 오른손 2, 3, 4번 손가락을 큰 집의 검은건반 세 개에 올려요. 먼저 <b>보기</b>, 그다음 <b>내 차례</b>: 주황색 건반이 다음 차례예요.</> : <>No reading yet -- just the big house. Use right-hand fingers 2, 3 and 4 on its three black keys. <b>Watch</b> first, then <b>your turn</b>: the orange key is the next one.</>}</div>""",
    """      <div style={actNote}>{LANG === 'ko' ? <>아직 악보는 없어요 -- 손가락 번호만 봐요. 오른손 <b>2, 3, 4</b>는 큰 지붕에, 왼손 <b>3, 2</b>는 아래 작은 지붕에. 먼저 <b>보기</b>, 그다음 <b>내 차례</b>: 주황색 건반이 다음 차례예요. 바통 터치하듯 레가토로!</> : <>No written notes -- just finger numbers. Right-hand <b>2, 3, 4</b> on the big roof; left-hand <b>3, 2</b> on the small roof below. <b>Watch</b> first, then <b>your turn</b>: the orange key is the next one. Legato, like a relay baton!</>}</div>""",
    'BlackKeySong note: both hands, fingers')
rep("""  const label = (k) => ({ 6: '1', 8: '2', 10: '3', 13: '5' }[k]);""",
    """""",
    'BlackKeySong drop unused label map')
rep("""        {song.keys.map((k, j) => <span key={j} style={{minWidth:14,textAlign:'center',color:(mode === 'watch' ? j === i : j <= i) ? '#e4572e' : '#c9c0aa'}}>{({ 6: 'G♭', 8: 'A♭', 10: 'B♭', 13: 'D♭' })[k]}</span>)}""",
    """        {song.keys.map((k, j) => { const on = mode === 'watch' ? j === i : j <= i; const L = song.f[j][0] === 'L'; return <span key={j} title={L ? t('left hand', '왼손') : t('right hand', '오른손')} style={{minWidth:17,textAlign:'center',color:on ? '#e4572e' : L ? '#26296b' : '#8a8dc0',fontWeight:900}}><span style={{fontSize:9,opacity:0.75}}>{song.f[j][0]}</span>{song.f[j].slice(1)}</span>; })}""",
    'BlackKeySong finger row')

# ── 9. the drill: loud/soft out, a naming level in
rep("""const FS_LEVELS = [
  { n: 1, label: 'High or low?',    kind: 'high', time: 6 },
  { n: 2, label: 'Loud or soft?',   kind: 'loud', time: 6 },
  { n: 3, label: 'Small house or big house?', kind: 'house', time: 6 },
];""",
"""const FS_LEVELS = [
  { n: 1, label: 'High or low?',    kind: 'high', time: 6 },
  { n: 2, label: 'Small house or big house?', kind: 'house', time: 6 },
  { n: 3, label: "What's this key's name?", kind: 'name', time: 7 },
];""",
    'FS_LEVELS: naming level replaces loud/soft')
rep("""  if (lv.kind === 'loud') { const loud = Math.random() < 0.5; return { kind: 'loud', key: uid, loud, answer: loud ? 'Loud (f)' : 'Soft (p)', choices: ['Soft (p)', 'Loud (f)'], uid }; }""",
"""  if (lv.kind === 'loud') { const loud = Math.random() < 0.5; return { kind: 'loud', key: uid, loud, answer: loud ? 'Loud (f)' : 'Soft (p)', choices: ['Soft (p)', 'Loud (f)'], uid }; }
  if (lv.kind === 'name') {
    const L7 = ['C', 'D', 'E', 'F', 'G', 'A', 'B'], PCS = [0, 2, 4, 5, 7, 9, 11];
    let wi, g = 0;
    do { wi = Math.floor(Math.random() * 7); } while (prev && prev.key === 'n' + wi && g++ < 10);
    const o = Math.floor(Math.random() * 3);
    const others = shuffle(L7.filter(x => x !== L7[wi])).slice(0, 3);
    return { kind: 'name', key: 'n' + wi, k: o * 12 + PCS[wi], answer: L7[wi], choices: shuffle([L7[wi], ...others]), uid };
  }""",
    'genFsQuestion: name kind')
rep("""  const title = (LANG === 'ko' ? { finger: '몇 번 손가락에 불이 켜졌나요?', high: '들어 봐요: 높을까, 낮을까?', loud: '들어 봐요: 클까, 작을까?', house: '어떤 집일까요?' } : { finger: 'Which finger number is lit?', high: 'L""",
"""  const title = (LANG === 'ko' ? { finger: '몇 번 손가락에 불이 켜졌나요?', name: '이 건반의 이름은 무엇일까요?', high: '들어 봐요: 높을까, 낮을까?', loud: '들어 봐요: 클까, 작을까?', house: '어떤 집일까요?' } : { finger: 'Which finger number is lit?', name: "What is this key's name?", high: 'L""",
    'FsQuestion title map')
rep("""    {q.kind === 'house' && <div style={{marginBottom:12}}><TapKeyboard octaves={3} marks={marks} pixel={pixel}/></div>}""",
"""    {q.kind === 'house' && <div style={{marginBottom:12}}><TapKeyboard octaves={3} marks={marks} pixel={pixel}/></div>}
    {q.kind === 'name' && <div style={{marginBottom:12}}><TapKeyboard octaves={3} marks={{ [q.k]: 'target' }} tint pixel={pixel}/></div>}""",
    'FsQuestion name keyboard')
rep("""'repeat(' + (q.choices.length === 5 ? 5 : 2) + ',1fr)'""",
    """'repeat(' + (q.choices.length === 5 ? 5 : q.choices.length === 4 ? 4 : 2) + ',1fr)'""",
    'FsQuestion 4-wide choices')

# ── 10. the old app lesson goes; the new one (the book on screen) lives in the chapter code below
i = s.index('function FirstStepsLearn({ onStart }) {')
j = s.index('const FINGER_LEVELS', i)
s = s[:i] + '// Phase 387: FirstStepsLearn is the Lesson Book opened on screen -- defined with the chapter pages (fsLbPages).\n' + s[j:]
done.append('old FirstStepsLearn removed')

# ── 11. the chapter pages + tools, inserted before the book registry
jsx = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fs387.jsx'), encoding='utf-8').read()
rep("const LESSON_BOOKS = { 'posture-hands': PostureLessonBook };",
    jsx + "\nconst LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook };",
    'chapter 2 book + tools registered')

# ── 12. one name everywhere
rep("{ id: 'first-steps', label: 'Black Keys & Your First Song', concept: FIRST_STEPS_DRILL, track: 'start' }",
    "{ id: 'first-steps', label: 'Keyboard Patterns & Note Names', concept: FIRST_STEPS_DRILL, track: 'start' }",
    'chapter label')
rep("  id: 'first-steps', label: 'Keyboard Patterns', levels: FS_LEVELS, generate: genFsQuestion,",
    "  id: 'first-steps', label: 'Keyboard Patterns & Note Names', levels: FS_LEVELS, generate: genFsQuestion,",
    'drill label')
rep("'first-steps': '검은건반과 첫 노래',", "'first-steps': '건반 패턴과 음이름',", 'Korean chapter name')
rep("'first-steps': ['Black keys', '검은건반'],", "'first-steps': ['Patterns', '패턴'],", 'short room name')
rep("'first-steps': 'black key small house big house first song white neighbour keyboard pattern whole piano 88 keys middle c pentatonic jam improvise band',",
    "'first-steps': 'black key small house big house roof first song white neighbour keyboard pattern whole piano 88 keys middle c pentatonic jam improvise band note names letter name c d e f g a b',",
    'search keywords')

open(p, 'w', encoding='utf-8').write(s)
print('\n'.join('ok: ' + d for d in done))
print('PATCH 387 DONE,', len(done), 'edits')
