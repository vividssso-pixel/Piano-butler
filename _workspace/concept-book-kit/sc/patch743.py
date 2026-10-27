import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BX (board call 26, the first Grade 8 room): Hear and Sing, Grade 8. The Grade 8 aural tests (Manual 2026, section 21):
# any major or minor triad, root position or an inversion, or a diminished triad in root position, within an octave: which
# triad, and (major or minor) its position; any of the four principal cadences in a major key in a short piece, the tonic chord
# first; about a minute and a half to memorise a three- or four-bar phrase from a printed copy, then play or sing it; the lower
# part of a two-part phrase with a few passing notes, hummed, sung or played from memory. The thing to make: chord colours.

# the triad pad names its notes by spelling, not by key (B♭ minor's first inversion is D♭ F B♭, not C♯ F B♭), and its Korean answer
# line takes the right ending after a closed syllable (기본형, 자리바꿈)
rep("""const name = l4Let(x.r) + ' ' + L6_QN[x.q][0], nameK = l4Let(x.r) + ' ' + L6_QN[x.q][1];""", """const rootN = TRI_ROOT[x.q][spPc(x.r)], name = rootN + ' ' + L6_QN[x.q][0], nameK = rootN + ' ' + L6_QN[x.q][1];""")
rep("""      <SpKb lo={-5} hi={16} W={24} H={74} lit={lit} names={res ? Object.fromEntries(n.map(k => [k, l4Let(k)])) : { 0: 'C' }} label={t('The triad', '3화음')}/>""", """      <SpKb lo={-5} hi={16} W={24} H={74} lit={lit} names={res ? Object.fromEntries(n.map(k => [k, triSpell(x.r, x.q, k)])) : { 0: 'C' }} label={t('The triad', '3화음')}/>""")
rep("""nameK + ', ' + L4_INVW[x.inv][1] + '였어요. ')""", """'정답은 ' + nameK + ', ' + L4_INVW[x.inv][1] + '. ')""")
rep("""function L6PosPad({""", """const TRI_ROOT = { maj: ['C', 'D♭', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B'], min: ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'B♭', 'B'], dim: ['C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'B♭', 'B'] };   // Build BX
const triRoot = (r, q) => (TRI_ROOT[q] || TRI_ROOT.maj)[spPc(r)];
const triSpell = (r, q, k) => { const sm = spPc(k - r); return l6Spell(triRoot(r, q), sm, sm === 0 ? 1 : sm <= 4 ? 3 : 5); };
function L6PosPad({""")
rep("""const LISTEN_7_DRILL = { id: 'listen-7', label: 'Hear and Sing, Grade 7', noPrint: true };   // Build BT""",
    """const LISTEN_7_DRILL = { id: 'listen-7', label: 'Hear and Sing, Grade 7', noPrint: true };   // Build BT
const LISTEN_8_DRILL = { id: 'listen-8', label: 'Hear and Sing, Grade 8', noPrint: true };   // Build BX""")
rep("""  { id: 'listen-7', label: 'Hear and Sing, Grade 7', concept: LISTEN_7_DRILL, track: 'start' },   // Build BT""",
    """  { id: 'listen-7', label: 'Hear and Sing, Grade 7', concept: LISTEN_7_DRILL, track: 'start' },   // Build BT
  { id: 'listen-8', label: 'Hear and Sing, Grade 8', concept: LISTEN_8_DRILL, track: 'start' },   // Build BX""")
rep("""'listen-7': '듣고 부르기, Grade 7'""", """'listen-7': '듣고 부르기, Grade 7', 'listen-8': '듣고 부르기, Grade 8'""")
rep("""'listen-7': ['listen-6']""", """'listen-7': ['listen-6'], 'listen-8': ['listen-7']""")
rep("""'listen-7': ['Hear & sing 7', '듣기 7']""", """'listen-7': ['Hear & sing 7', '듣기 7'], 'listen-8': ['Hear & sing 8', '듣기 8']""")
rep("""  'listen-7': 'aural ear grade 7""", """  'listen-8': 'aural ear grade 8 triad major minor diminished position inversion four cadences perfect plagal interrupted imperfect memory three four bars phrase lower part passing notes chord colours augmented',
  'listen-7': 'aural ear grade 7""")
rep("""id === 'listen-6' || id === 'listen-7') return 'aural';""", """id === 'listen-6' || id === 'listen-7' || id === 'listen-8') return 'aural';""")
# the house: the Grade 8 floor, the top floor under the attic
rep("""  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true,""",
    """  { ids: ['listen-8', 'scales-8', 'arps-8'], en: ['Grade 8', 'Your ears, scales, and arpeggios and chord walks: the top floor.'], ko: ['Grade 8', '귀, 스케일, 아르페지오와 화음 진행: 맨 위층.'] },   // Build BX: the Grade 8 floor (call 26)
  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true,""")
# the two-part pad can ask for one part only (Grade 8 asks for the lower part)
rep("""function PartsPad({ onResult, fixed, set, bpm = 60, rungs, title, note, tag = 'two' }) {""", """function PartsPad({ onResult, fixed, set, bpm = 60, rungs, title, note, tag = 'two', only = null }) {""")
rep("""  const [x, setX] = useState(fixed || { i: 0, ask: 'hi' }), [rung, setRung]""", """  const [x, setX] = useState(fixed || { i: 0, ask: only || 'hi' }), [rung, setRung]""")
rep("""do { y = { i: Math.floor(Math.random() * set.length), ask: Math.random() < 0.5 ? 'hi' : 'lo' }; } while (y.i === x.i && y.ask === x.ask && g++ < 10);""",
    """do { y = { i: Math.floor(Math.random() * set.length), ask: only || (Math.random() < 0.5 ? 'hi' : 'lo') }; } while (y.i === x.i && y.ask === x.ask && g++ < 10);""")
rep("""function L7MemPad({ onResult, fixed, set = L7_MEM, secs = 60, bars = 2, g = 7 }) {""", """function L7MemPad({ onResult, fixed, set = L7_MEM, secs = 60, bars = 2, g = 7, tag = 'mem' }) {""")
rep("""    <div className="try-box" style={actBox} data-l7="mem">""", """    <div className="try-box" style={actBox} data-l7={tag}>""")
rep("""        ? <div style={{width:'100%',maxWidth:360,background:'#fff',borderRadius:8}}><MelodyStaff notes={memNotes(P)} beats={P.beats} width={330} colors""",
    """        ? <div style={{width:'100%',maxWidth:Math.max(360, memW(P) + 20),background:'#fff',borderRadius:8}}><MelodyStaff notes={memNotes(P)} beats={P.beats} width={memW(P)} colors""")
rep("""const memNotes = (P) =>""", """const memLen = (P) => P.n.reduce((a, x) => a + x[1], 0);
const memNotes = (P) =>""")

CH = r'''
// ─── Chapter: Hear and Sing, Grade 8 (Build BX, 2026-10-28; board call 26, the first Grade 8 room) ───
const L8_MEM = [   // three- and four-bar phrases, written for this app ({ k: keynote, beats, n: [[staff step, beats, accidental]] })
  { k: 0, beats: 4, n: [[30, 1], [32, 1], [35, 1], [34, 1], [33, 1], [31, 1], [29, 1], [32, 1], [30, 1.5], [29, .5], [28, 2]] },
  { k: 7, beats: 3, n: [[32, 1], [34, 1], [36, 1], [35, 2], [33, 1], [34, 1], [32, 1], [31, 1, 1], [32, 3]] },
  { k: 5, beats: 4, n: [[31, 1], [32, 1], [33, 1], [35, 1], [34, 1, -1], [33, 1], [32, 1], [30, 1], [31, 4]] },
  { k: 2, beats: 4, n: [[29, 1], [31, 1, 1], [33, 1], [36, 1], [35, 2, 1], [33, 2], [34, 1], [33, 1], [32, 1], [31, 1, 1], [29, 4]] },
  { k: 9, beats: 4, n: [[33, 1], [35, 1], [37, 1], [35, 1], [34, 1], [32, 1, 1], [33, 1], [30, 1], [31, 1], [32, 1, 1], [33, 2]] },
  { k: 0, beats: 3, n: [[28, 1], [30, 1], [32, 1], [33, 2], [32, 1], [31, 1], [29, 1], [34, 1], [35, 3]] },
  { k: 7, beats: 4, n: [[36, 1], [35, 1], [34, 1], [33, 1], [32, 1], [33, .5], [34, .5], [35, 1], [31, 1, 1], [32, 4]] },
  { k: -2, beats: 4, n: [[27, 1, -1], [29, 1], [31, 1], [34, 1, -1], [33, 1], [31, 1], [32, 1], [30, 1, -1], [29, 1], [28, 1], [27, 2, -1]] },
];
function L8MemPad(p) { return <L7MemPad set={L8_MEM} secs={90} bars={t('3 or 4', '3~4')} g={8} tag="mem8" {...p}/>; }
const L8_TWO = [   // two parts, the lower one with a few passing notes (quavers between the beats)
  { hi: [[4, 1], [5, 1], [7, 1], [4, 1]], lo: [[0, 1], [2, 1], [4, .5], [2, .5], [0, 1]] },
  { hi: [[12, 1], [11, 1], [9, 1], [11, 1], [12, 2]], lo: [[0, 1], [2, .5], [4, .5], [5, 1], [7, 1], [0, 2]] },
  { hi: [[19, 1], [17, 1], [16, 1], [14, 1], [16, 2]], lo: [[12, 1], [14, .5], [12, .5], [9, 1], [11, 1], [12, 2]] },
  { hi: [[16, 1], [17, 1], [19, 1], [17, 1], [16, 2]], lo: [[12, 1], [14, 1], [16, .5], [14, .5], [9, 1], [12, 2]] },
  { hi: [[11, 1], [12, 1], [14, 1], [12, 1], [11, 2]], lo: [[7, 1], [9, .5], [7, .5], [6, 1], [4, 1], [7, 2]] },
  { hi: [[9, 1], [10, 1], [12, 1], [10, 1], [9, 2]], lo: [[5, 1], [7, .5], [5, .5], [4, 1], [7, 1], [5, 2]] },
];
function L8TwoPad(p) { return <PartsPad set={L8_TWO} bpm={60} only="lo" tag="two8" rungs={[[2, t('The first two beats', '처음 두 박')], [99, t('All of it, like the test', '전체, 시험처럼')]]} title={t('The lower part, passing notes and all', '아랫성부, 경과음까지')}
  note={LANG === 'ko' ? <>두 성부 프레이즈(전체를 두 번). 8급은 언제나 <b>아랫성부</b>(거북이)를 물어요. 아랫성부에는 <b>경과음</b>이 몇 개: 두 음 사이를 한 걸음씩 잇는 짧은 음. 외워서 흥얼거리거나 부르고, 건반에서 차례로 찾아요.</>
    : <>A two-part phrase (all of it played twice). Grade 8 always asks for <b>the lower part</b> (the turtle's). It has <b>a few passing notes</b>: short notes that join two notes step by step. From memory, hum or sing it, then find it on the keys in order.</>} {...p}/>; }
const L8CadPad = (p) => <CadPad cads={['perfect', 'plagal', 'interrupted', 'imperfect']} tag="cad8" {...p}/>;
const L8PosPad = (p) => <L6PosPad quals={['maj', 'min', 'dim']} {...p}/>;
// ── make: chord colours: one root, four triads ──
const CC_Q = { maj: [[0, 4, 7], 'Major', '장3화음', 'bright'], min: [[0, 3, 7], 'Minor', '단3화음', 'dark'], dim: [[0, 3, 6], 'Diminished', '감3화음', 'tight'], aug: [[0, 4, 8], 'Augmented', '증3화음', 'stretched'] };
function ChordColours() {
  const [r, setR] = useState(0), [q, setQ] = useState('maj');
  const N = CC_Q[q][0].map(x => r + x), lit = Object.fromEntries(N.map((x, j) => [x, j === 0 ? 'cor' : 'pale']));
  const play = (rr = r, qq = q) => { const M = CC_Q[qq][0].map(x => rr + x); spPlay(M.map((x, j) => ({ at: j * 0.45, keys: [x], len: 0.42, vol: 0.14 })).concat([{ at: 1.5, keys: M, len: 1.6, vol: 0.12 }]), 90); };
  const spin = () => { const order = ['maj', 'min', 'dim', 'aug']; spPlay(order.flatMap((qq, i) => [{ at: i * 2, keys: CC_Q[qq][0].map(x => r + x), len: 1.7, vol: 0.12 }]), 90); };
  return (
    <div className="try-box" style={actBox} data-mk="colour">
      <div style={actTitle}>{t('My chord colours', '나의 화음 색깔')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>근음 하나에 3화음 네 가지 색: <b>장</b>(밝음), <b>단</b>(어두움), <b>감</b>(조여듦: 3도 둘이 모두 작아요), <b>증</b>(늘어남: 3도 둘이 모두 커요). 건반을 눌러 근음을 고르고, 색을 바꿔 들어요.</> : <>One root, four triad colours: <b>major</b> (bright), <b>minor</b> (dark), <b>diminished</b> (tight: both 3rds small), <b>augmented</b> (stretched: both 3rds big). Tap a key for the root, then change the colour.</>}</div>
      {spChips(Object.keys(CC_Q).map(k => [k, t(CC_Q[k][1], CC_Q[k][2])]), q, (k) => { setQ(k); play(r, k); })}
      <SpKb lo={-5} hi={19} W={20} H={74} lit={lit} names={Object.fromEntries(N.map(x => [x, triSpell(r, q, x)]))} onTap={(x) => { setR(x); play(x, q); }} label={t('Choose the root', '근음 고르기')}/>
      {spMsg(triRoot(r, q) + ' ' + t(CC_Q[q][1].toLowerCase(), CC_Q[q][2]) + ': ' + N.map(x => triSpell(r, q, x)).join(' ') + t(' · ' + CC_Q[q][3], ''), BK.ink)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => play()}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={spin}>{t('▶ All four colours', '▶ 네 색 모두')}</button>
      </div>
    </div>
  );
}

const l8PicTri = () => lsRawPic('<ellipse cx="18" cy="34" rx="6.5" ry="4.6" transform="rotate(-20 18 34)" fill="#26296b"/><ellipse cx="18" cy="24" rx="6.5" ry="4.6" transform="rotate(-20 18 24)" fill="#26296b"/><ellipse cx="18" cy="14" rx="6.5" ry="4.6" transform="rotate(-20 18 14)" fill="#e4572e"/><text x="32" y="28" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#26296b">dim</text>', [0, 0, 56, 44]);
const l8PicCad = () => lsRawPic(['V–I', 'IV–I', 'V–vi', '…V'].map((x, i) => '<text x="' + (6 + (i % 2) * 38) + '" y="' + (18 + Math.floor(i / 2) * 18) + '" font-family="Georgia, serif" font-size="12" font-weight="900" fill="' + (i === 3 ? '#e4572e' : '#26296b') + '">' + x + '</text>').join(''), [0, 0, 80, 44]);
const l8PicTwo = () => lsRawPic('<path d="M4 12 L28 8 L52 12 L76 8" fill="none" stroke="#26296b" stroke-width="2.2" stroke-opacity="0.45"/><path d="M4 34 L16 30 L22 28 L28 30 L52 34 L64 30 L76 32" fill="none" stroke="#26296b" stroke-width="2.6"/><circle cx="22" cy="28" r="3" fill="#e4572e"/><circle cx="64" cy="30" r="3" fill="#e4572e"/>', [0, 0, 80, 44]);

function l8LbPages(scr = false) {
  const ch = 'listen-8', l7c = bkChapterNo('listen-7');
  const checks4 = [[l8PicTri(), t('I hear a major, minor or diminished triad, and its position', '장3화음, 단3화음, 감3화음과 그 자리를 들어요')], [l8PicCad(), t('I hear all four cadences in a short piece', '짧은 곡에서 네 종지를 모두 들어요')],
    [l7PicMem(), t('I memorise a three- or four-bar phrase in a minute and a half', '3~4마디 프레이즈를 1분 반 안에 외워요')], [l8PicTwo(), t('I sing the lower part of two parts, passing notes and all', '두 성부의 아랫성부를 경과음까지 불러요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('Major, minor or diminished?', '장, 단, 감3화음?'), 2], [t('All four cadences', '네 가지 종지'), 3], [t('Remember a longer phrase', '더 긴 프레이즈 외우기'), 4], [t('The lower part, passing notes and all', '아랫성부, 경과음까지'), 5], [t('My four checks', '나의 네 가지 확인'), 6]];
  const triStill = <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:12,width:'100%',maxWidth:720,margin:'0 auto'}}>{['maj', 'min', 'dim'].map(q => { const n = l6Tri(0, q, 0);
    return <div key={q}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{t('C ' + L6_QN[q][0], 'C ' + L6_QN[q][1])}: {n.map(k => triSpell(0, q, k)).join(' ')}</div>{l4Kb(Object.fromEntries(n.map((k, j) => [k, j === 0 ? 'pale' : 'cor'])), Object.fromEntries(n.map(k => [k, triSpell(0, q, k)])), scr, -2, 16)}</div>; })}</div></LbPic>;
  const cadStill = <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:12,width:'100%',maxWidth:680,margin:'0 auto'}}>{[['perfect', 0], ['plagal', 1], ['interrupted', 0], ['imperfect', 0]].map(([c, ti]) => <div key={c}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{cadCap(c)} · {CAD_N[c][2]}</div><CadChart x={{ key: 0, cad: c, ti }}/></div>)}</div></LbPic>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('The Grade 8 aural tests, one step each (Manual of Syllabuses, section 21): any major or minor triad, root position or an inversion, or any diminished triad in root position, within an octave: which triad, and (major or minor) its position (Grade 7, chapter ' + l7c + ', had major and minor only); any of the four principal cadences in a major key as they occur in a short piece, the tonic chord first; about a minute and a half to memorise a three- or four-bar phrase from a printed copy away from the instrument, then play or sing it; the lower part of a two-part phrase with a few passing notes, hummed, sung or played from memory. The tunes are written for this app.', '8급 청음 시험을 한 단계씩(실라버스 21절): 장3화음이나 단3화음을 기본형이나 자리바꿈으로, 또는 기본형의 감3화음을 한 옥타브 안에서: 어떤 3화음인지, 그리고(장·단이면) 그 자리(' + l7c + '장의 7급은 장·단만); 장조의 짧은 곡에서 나오는 네 가지 주요 종지 알기, 먼저 으뜸화음; 악보로 3~4마디 프레이즈를 악기 없이 약 1분 반 동안 외우고 치거나 부르기; 경과음이 몇 개 있는 두 성부 프레이즈의 아랫성부를 외워서 흥얼거리거나 부르거나 치기. 선율은 이 앱을 위해 지었어요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={150}><div style={{width:'100%',maxWidth:440,margin:'0 auto'}}><PartsLines P={L8_TWO[1]}/></div></LbPic>
      <LbSay size={18}>{t('Your ears for Grade 8, the top floor: the diminished triad too, all four endings, a longer phrase in your memory, and the lower part with its passing notes.', '맨 위층 8급의 귀: 감3화음까지, 네 가지 끝, 기억에 담는 더 긴 프레이즈, 그리고 경과음이 있는 아랫성부.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checks4.map(([, x], i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Major, minor or diminished?', '장, 단, 감3화음?')}
      teacher={<>{t('Grade 8: any major or minor triad, root position or an inversion, or any diminished triad in root position, within an octave. The child names the triad; for major or minor, its position too. The diminished triad has two minor 3rds: tight, unsettled.', '8급: 장3화음이나 단3화음(기본형이나 자리바꿈), 또는 기본형의 감3화음을 한 옥타브 안에서. 아이는 3화음을 말하고, 장·단이면 자리도 말해요. 감3화음은 단3도가 둘: 조여들고 불안해요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={triStill} live={<L8PosPad/>}/>
      <LbSay>{LANG === 'ko' ? <>밝으면 장, 어두우면 단, <b>조여들면 감</b>: 작은 3도가 둘. 장·단이면 4도를 찾아 자리를 말해요.</> : <>Bright, major; dark, minor; <b>tight, diminished</b>: two small 3rds. For major or minor, find the 4th and say the position.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 C장, C단, C감3화음을 쳐요. 차이를 들어요.</>, <>아무 3화음. 아래부터 흥얼거려요.</>, <>3화음 이름, 그리고 자리를 말해요.</>]
        : [<>Your teacher plays C major, C minor, then C diminished. Hear the difference.</>, <>Any triad. Hum it from the bottom.</>, <>Name the triad, then its position.</>]}/>
      <LbRemember>{t('Bright, dark, or tight.', '밝음, 어두움, 또는 조여듦.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('All four cadences', '네 가지 종지')}
      teacher={<>{t('Grade 8: any of the four principal cadences in a major key, as they occur in a short piece, the tonic chord first. New since Grade 7: the imperfect cadence, ending on V (a comma, not a full stop). The first rung plays only the last two chords.', '8급: 장조의 짧은 곡에서 나오는 네 가지 주요 종지 아무것이나, 먼저 으뜸화음. 7급에서 새로운 것: V로 끝나는 반종지(마침표가 아니라 쉼표). 첫 걸음은 마지막 두 화음만.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={cadStill} live={<L8CadPad/>}/>
      <LbSay>{LANG === 'ko' ? <>정격(V–I)과 변격(IV–I)은 <b>마침표</b>. 거짓(V–vi)은 <b>깜짝</b>. 반종지(…–V)는 <b>쉼표</b>: 아직 끝나지 않았어요.</> : <>Perfect (V–I) and plagal (IV–I) are <b>full stops</b>. Interrupted (V–vi) is <b>a surprise</b>. Imperfect (…–V) is <b>a comma</b>: not finished yet.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 네 가지를 차례로 쳐요.</>, <>짧은 곡 전체: 끝 두 화음만 기억해요.</>, <>마침표, 깜짝, 쉼표 중 무엇인가요? 이름을 말해요.</>]
        : [<>Your teacher plays all four, one after another.</>, <>A whole short piece: remember just the last two chords.</>, <>Full stop, surprise or comma? Name it.</>]}/>
      <LbRemember>{t('Full stop, surprise or comma.', '마침표, 깜짝, 또는 쉼표.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Remember a longer phrase', '더 긴 프레이즈 외우기')}
      teacher={<>{t('Grade 8: about one and a half minutes to memorise a three- or four-bar melodic phrase from a printed copy, away from the instrument; then the child plays or sings it from memory. You sound the keynote first. One bar more than Grade 7, half a minute longer: memorise it in pieces (bar by bar), then join them.', '8급: 악기에서 떨어져 악보로 3~4마디 선율 프레이즈를 약 1분 반 동안 외우고, 외운 대로 치거나 불러요. 먼저 선생님이 으뜸음을 울려요. 7급보다 한 마디 더, 30초 더: 조각으로(마디마다) 외우고, 그다음 이어요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:600,margin:'0 auto',background:'#fff',borderRadius:8}}><MelodyStaff notes={memNotes(L8_MEM[0])} beats={4} width={memW(L8_MEM[0], 440)}/></div></LbPic>} live={<L8MemPad/>}/>
      <LbSay>{LANG === 'ko' ? <>길면 <b>조각으로</b>: 마디마다 속으로 부르고, 이어 붙여요. 리듬을 세고, 마지막 음을 으뜸음에 견줘요.</> : <>Long ones go <b>in pieces</b>: sing each bar inside, then join them. Count the rhythm; check the last note against the keynote.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>으뜸음을 듣고 1분 반 동안 봐요: 1마디, 2마디, 이어서.</>, <>악보를 덮고 쳐요.</>, <>이번엔 불러요.</>]
        : [<>Hear the keynote, then look for a minute and a half: bar 1, bar 2, then together.</>, <>Close the copy and play it.</>, <>Now sing it.</>]}/>
      <LbRemember>{t('In pieces, then joined.', '조각으로, 그다음 이어서.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The lower part, passing notes and all', '아랫성부, 경과음까지')}
      teacher={<>{t('Grade 8: you play a two-part phrase with a few passing notes; the child hums, sings or plays the lower part from memory. The passing notes are quavers joining two notes a 3rd apart by step. The first rung is the first two beats.', '8급: 선생님이 경과음이 몇 개 있는 두 성부 프레이즈를 쳐요; 아이는 아랫성부를 외워서 흥얼거리거나 부르거나 쳐요. 경과음은 3도 떨어진 두 음을 한 걸음씩 잇는 8분음표. 첫 걸음은 처음 두 박.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:440,margin:'0 auto'}}><PartsLines P={L8_TWO[1]}/></div></LbPic>} live={<L8TwoPad/>}/>
      <LbSay>{LANG === 'ko' ? <>아랫줄, <b>거북이</b>를 따라가요. 경과음은 두 음 사이를 <b>한 걸음씩 잇는</b> 짧은 음.</> : <>Follow the lower line, <b>the turtle's</b>. Passing notes are short notes that <b>join two notes step by step</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 처음 두 박을 쳐요. 아랫성부를 불러요.</>, <>전체, 두 번. 아랫성부를 흥얼거려요.</>, <>그 아랫성부를 건반에서 쳐요.</>]
        : [<>Your teacher plays the first two beats. Sing the lower part.</>, <>All of it, twice. Hum the lower part.</>, <>Play that lower part on the keys.</>]}/>
      <LbRemember>{t('The turtle, passing notes and all.', '거북이, 경과음까지.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My four checks', '나의 네 가지 확인')}
      teacher={<>{t('Each one with you at the piano, away from the screen, as in the exam. Use material the child has not heard or seen this week; the teacher copy has phrases to show.', '하나씩 화면 없이 피아노 앞에서, 시험처럼. 이번 주에 듣거나 보지 않은 재료로; 선생님용에 보여 줄 프레이즈가 있어요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks4.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks4} storeKey="pb_l8_four"/>}/>
    </LbPage>,
  ];
}
function Listen8LessonBook() { return <>{l8LbPages(false)}</>; }
function L8Learn({ onStart }) {
  const pages = l8LbPages(true), opener = pages[0];
  return (
    <Lesson id="listen-8" title={bkChapterName('listen-8')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="listen-8"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
const L8_LEVELS = [
  { n: 1, label: 'Major, minor or diminished, and which position?', kind: 'pos', time: 30 },
  { n: 2, label: 'Which of the four cadences?', kind: 'cad', time: 40 },
  { n: 3, label: 'Remember a three- or four-bar phrase', kind: 'mem', time: 150 },
  { n: 4, label: 'The lower part, with passing notes', kind: 'two', time: 60 },
  { n: 5, label: 'All four, mixed, as in the Grade 8 exam', kind: 'mix', time: 150 },
];
Object.assign(LEVEL_KO, { 'Major, minor or diminished, and which position?': '장, 단, 감3화음? 그리고 어느 자리?', 'Which of the four cadences?': '네 종지 중 어느 것?', 'Remember a three- or four-bar phrase': '3~4마디 프레이즈 외우기', 'The lower part, with passing notes': '경과음이 있는 아랫성부', 'All four, mixed, as in the Grade 8 exam': '네 가지 섞어서, 8급 시험처럼' });
function genL8Question(lv, prev) {
  const uid = Math.random(); let kind = lv.kind;
  if (kind === 'mix') kind = pick(['pos', 'cad', 'mem', 'two'].filter(k => !prev || prev.kind !== k));
  let fx, key, g = 0;
  do {
    if (kind === 'pos') { const q = pick(['maj', 'min', 'dim']); fx = { r: Math.floor(Math.random() * 12), q, inv: q === 'dim' ? 0 : pick([0, 1, 2]) }; }
    else if (kind === 'cad') fx = { key: pick(CAD_KEYS), cad: pick(['perfect', 'plagal', 'interrupted', 'imperfect']), ti: Math.floor(Math.random() * 3) };
    else if (kind === 'mem') fx = { i: Math.floor(Math.random() * L8_MEM.length) };
    else fx = { i: Math.floor(Math.random() * L8_TWO.length), ask: 'lo' };
    key = kind + JSON.stringify(fx);
  } while (prev && prev.key === key && g++ < 10);
  return { kind, fx, answer: 'ok', choices: [], key, uid };
}
function L8Question({ q, given, locked, onAnswer, pixel }) {
  const pickIt = (c) => { if (locked || given) return; stopClicks(); onAnswer(c); };
  const res = (r) => pickIt(r.ok ? 'ok' : 'no');
  const title = { pos: t('Major, minor or diminished, and which position?', '장, 단, 감3화음? 그리고 어느 자리?'), cad: t('Home first, then the piece: which cadence?', '먼저 집, 그다음 곡: 어떤 종지?'), mem: t('Look, remember, then play it back.', '보고, 외우고, 다시 쳐요.'), two: t('Sing the lower part, then find it.', '아랫성부를 부르고, 찾아요.') }[q.kind];
  const body = q.kind === 'pos' ? <L8PosPad key={q.uid} fixed={q.fx} onResult={res}/> : q.kind === 'cad' ? <L8CadPad key={q.uid} fixed={q.fx} onResult={res}/> : q.kind === 'mem' ? <L8MemPad key={q.uid} fixed={q.fx} onResult={res}/> : <L8TwoPad key={q.uid} fixed={q.fx} onResult={res}/>;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {body}
  </div>);
}
Object.assign(LISTEN_8_DRILL, { levels: L8_LEVELS, generate: genL8Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: () => t('done', '완료'), Question: L8Question, Learn: L8Learn });
function L8Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="listen-8" teacher>{content}</WbPage>);
  const lt = (i) => { const nm = lwLet(i); return i < 0 ? nm + ',' : nm + (i >= 12 ? "'" : ''); };
  const ltS = (r, i) => { const sm = spPc(i - r), nm = l6Spell(lwLet(r), sm, sm === 0 ? 1 : sm <= 4 ? 3 : 5); return nm + (i < 0 ? ',' : i >= 12 ? "'" : ''); };
  const tri = ([r, q, inv]) => { const n = l6Tri(r, q, inv); return n.map(x => ltS(r, x)).join(' ') + ' (' + lwLet(r) + ' ' + L6_QN[q][0] + (q === 'dim' ? '' : ', ' + L4_INVW[inv][0]) + ')'; };
  const cad = ([key, c, ti]) => CAD_KN[key] + ': ' + CAD_TPL[c][ti].slice(0, 6).reduce((a, x, j) => a + (j % 2 === 0 && j ? ' | ' : ' ') + x, '').trim() + ' | ' + CAD_TPL[c][ti][6] + ' (' + c + ')';
  const lower = (P2) => P2.lo.map(([k, d]) => lt(k) + (d < 1 ? '(♪)' : '')).join(' ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('listen-8')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>No Workbook for this chapter: every step is by ear, as the Grade 8 aural tests ask. Play every test twice unless the Manual says otherwise. Middle C is C; the C above is C'; notes below middle C carry a comma.</div>
    <TcBlock page={2} title="Major, minor or diminished?" answers={<>{tcAns('PLAY', [[0, 'dim', 0], [7, 'min', 2], [2, 'maj', 1], [11, 'dim', 0], [9, 'min', 1], [5, 'maj', 2], [4, 'dim', 0], [10, 'min', 0]].map(tri))}</>}
      watch="The diminished triad heard as minor: both have a minor 3rd at the bottom. Listen to the top: the diminished 5th is tighter."
      say="“Bright, dark, or tight.”"/>
    <TcBlock page={3} title="All four cadences" answers={<>{tcAns('PLAY THE TONIC CHORD, THEN', [[0, 'imperfect', 0], [7, 'interrupted', 1], [2, 'plagal', 0], [5, 'perfect', 2], [-2, 'imperfect', 1], [9, 'interrupted', 2]].map(cad))}</>}
      watch="Imperfect heard as perfect: both have V. Ask which chord came last: a comma (V) or home (I)?"
      say="“Full stop, surprise or comma.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Remember a longer phrase" answers={<div style={{display:'grid',gap:'4px'}}>{L8_MEM.map((M, j) => <div key={j} style={{display:'flex',alignItems:'center',gap:4}}><span style={{fontSize:11,fontWeight:900,color:BK.muted,minWidth:14}}>{j + 1}.</span><div style={{flex:1,minWidth:0,maxWidth:520}}><MelodyStaff notes={memNotes(M)} beats={M.beats} width={memW(M, 480)}/></div></div>)}</div>}
      watch="Bar 3 lost while holding bars 1 and 2. Memorise in pieces and join them; sound the keynote first."
      say="“In pieces, then joined.”"/>
  </>);
  P(<>
    <TcBlock page={5} title="The lower part, passing notes and all" answers={<>{tcAns('PLAY; THE LOWER PART IS', L8_TWO.map(lower))}</>}
      watch="Passing notes left out (the child sings only the beats). Ask for the in-between notes: “what joined them?”"
      say="“The turtle, passing notes and all.”"/>
    <TcBlock page={6} title="My four checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one with you at the piano, away from the screen. The drill's level 5 mixes all four, as the exam does.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['listen-8'] = L8Teacher;
'''
rep("""TEACHER_COPIES['listen-7'] = L7Teacher;""", """TEACHER_COPIES['listen-7'] = L7Teacher;""" + CH)

HOME = r'''
// ══ Build BX: Hear and Sing, Grade 8 on the Home (the Aural door) ══
LBH_FN['listen-8'] = (s) => l8LbPages(s);
const l8Add = (id, i, en, ko, benEn, bko, make) => { const spec = lbhSpec('listen-8', i, { make });
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return t('Aural', '청음') + ' · ' + t('Hear and sing, Grade 8', '듣고 부르기, Grade 8'); }, C: () => <KqEngine spec={spec}/> });
  lbhRetitle(id, en, ko, benEn, bko); };
const l8CadQ = (n, prev) => { const C4 = ['perfect', 'plagal', 'interrupted', 'imperfect']; let x, g = 0; do { x = { key: pick(CAD_KEYS), cad: C4[n % 4], ti: Math.floor(Math.random() * 3) }; } while (prev && prev.key === JSON.stringify(x) && g++ < 10); const sq = CAD_TPL[x.cad][x.ti];
  return { kind: 'choice', cols: 2, prompt: ['Home first, then the piece: which cadence?', '먼저 집, 그다음 곡: 어떤 종지?'], opts: C4.map(c => ({ id: c, label: () => cadCap(c) })), ans: x.cad, ok: (a) => a === x.cad, key: JSON.stringify(x), play: () => cadPlay(x, false),
    fig: (c) => ({ mid: c.res ? <CadChart x={x}/> : null }), yes: ['Yes: ' + sq[5] + ' to ' + sq[6] + '.', '맞아요: ' + sq[5] + '에서 ' + sq[6] + '.'], no: ['It was ' + CAD_N[x.cad][0] + ': ' + sq[5] + ' to ' + sq[6] + '.', '정답은 ' + CAD_N[x.cad][1] + ': ' + sq[5] + '에서 ' + sq[6] + '.'] }; };
l8Add('l8-pos', 1, 'Major, minor or diminished?', '장, 단, 감3화음?', 'Bright, dark, or tight; then the position.', '밝음, 어두움, 조여듦; 그다음 자리.', lwTapQ(L8PosPad, (n) => ({ fixed: { r: (n * 5) % 12, q: ['maj', 'min', 'dim'][n % 3], inv: n % 3 === 2 ? 0 : n % 3 } }), ['Which triad, then the position.', '어떤 3화음, 그다음 자리.'], ['Heard ✓', '들었어요 ✓']));
l8Add('l8-cad', 2, 'All four cadences', '네 가지 종지', 'Full stop, surprise or comma?', '마침표, 깜짝, 쉼표?', l8CadQ);
l8Add('l8-mem', 3, 'Remember a longer phrase', '더 긴 프레이즈 외우기', 'Three or four bars in a minute and a half.', '3~4마디를 1분 반 안에.', lwTapQ(L8MemPad, (n) => ({ fixed: { i: (n * 3) % L8_MEM.length } }), ['The keynote, then look: play it back from memory.', '으뜸음, 그다음 보기: 외워서 다시 쳐요.'], ['From memory ✓', '외워서 ✓']));
l8Add('l8-two', 4, 'The lower part, passing notes and all', '아랫성부, 경과음까지', 'Follow the turtle, passing notes and all.', '거북이를 따라가요, 경과음까지.', lwTapQ(L8TwoPad, (n) => ({ fixed: { i: n % L8_TWO.length, ask: 'lo' } }), ['Hear the two parts, sing the lower one, then find it.', '두 성부를 듣고, 아랫성부를 부르고, 찾아요.'], ['Sung and found ✓', '부르고 찾았어요 ✓']));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""  { id: 'mk-cad', ch: 'listen-6',""", """  { id: 'mk-colour', ch: 'listen-8', title: 'My chord colours', blurb: 'One root, four colours: major, minor, diminished, augmented.', C: () => <ChordColours/> },   // Build BX
  { id: 'mk-cad', ch: 'listen-6',""")
rep("""  'mk-cad': ['나만의 끝 만들기',""", """  'mk-colour': ['나의 화음 색깔', '근음 하나, 색 넷: 장, 단, 감, 증3화음.'],
  'mk-cad': ['나만의 끝 만들기',""")
rep("""'mk-cad': ['chords', 3, 3, 'game ear'],""", """'mk-cad': ['chords', 3, 3, 'game ear'], 'mk-colour': ['chords', 3, 3, 'game ear'],""")
rep("""'mk-cad': 'p-chords',""", """'mk-cad': 'p-chords', 'mk-colour': 'p-chords',""")
rep("""  'mk-cad': () => (\n""", """  'mk-colour': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><circle cx="8" cy="15" r="3" fill="#fefbf3"/><circle cx="12" cy="10.5" r="3" fill="#e9a83a"/><circle cx="16" cy="6" r="3" fill="#fefbf3"/></svg>
  ),
  'mk-cad': () => (\n""")
rep("""    { id: 'au-7', en: 'Hear and sing, Grade 7', ko: '듣고 부르기, Grade 7', lessons: ['l7-pos', 'l7-cad', 'l7-mem', 'l7-two', 'mk-mem'], check: 'listen-7' },   // Build BT""",
    """    { id: 'au-7', en: 'Hear and sing, Grade 7', ko: '듣고 부르기, Grade 7', lessons: ['l7-pos', 'l7-cad', 'l7-mem', 'l7-two', 'mk-mem'], check: 'listen-7' },   // Build BT
    { id: 'au-8', en: 'Hear and sing, Grade 8', ko: '듣고 부르기, Grade 8', lessons: ['l8-pos', 'l8-cad', 'l8-mem', 'l8-two', 'mk-colour'], check: 'listen-8' },   // Build BX""")
rep("""  set('7', 'l7-pos l7-cad l7-mem l7-two mk-mem');   // Build BT: Hear and Sing, Grade 7""", """  set('7', 'l7-pos l7-cad l7-mem l7-two mk-mem');   // Build BT: Hear and Sing, Grade 7
  set('8', 'l8-pos l8-cad l8-mem l8-two mk-colour');   // Build BX: Hear and Sing, Grade 8""")
rep("""const LESSON_BOOKS = { 'pieces-78': Pieces78LessonBook,""", """const LESSON_BOOKS = { 'listen-8': Listen8LessonBook, 'pieces-78': Pieces78LessonBook,""")
rep("""const LB_PAGE_FNS = { 'pieces-78': p78LbPages,""", """const LB_PAGE_FNS = { 'listen-8': l8LbPages, 'pieces-78': p78LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"listen-8": "<path d=\\"M8 15C3 21 3 29 8 35M15 19C12 22 12 28 15 31\\"/><path d=\\"M22 34 L30 30 L34 32 L38 30 L44 33\\" stroke-width=\\"2.2\\"/><circle cx=\\"34\\" cy=\\"32\\" r=\\"2.6\\" fill=\\"#e4572e\\" stroke=\\"none\\"/><ellipse cx=\\"30\\" cy=\\"16\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 30 16)\\" fill=\\"#26296b\\"/><ellipse cx=\\"38\\" cy=\\"12\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 38 12)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
