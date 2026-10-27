import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BZ (board call 26, the third Grade 8 room, the last room of the house): Arpeggios and Progressions, Grade 8, from the
# technical work book (Grade 8 pp76-82, read 28 Oct): I–IV–I⁶₄–V–I chord progressions in C, D and E♭ major; arpeggios, root
# position and inversions, E and B♭ major and minor, four octaves, (i) all p (ii) all f, ♩ = 84; the dominant 7th of E and of B♭,
# root position and inversions; the diminished 7th of E and of B♭. Fingerings are the book's. The thing to make: one diminished 7th, four keys.

rep("""function Dom7InvPad({ keys = ['D', 'Ab'], onResult, fixed }) {""", """function Dom7InvPad({ keys = ['D', 'Ab'], onResult, fixed, note, bpm = 72 }) {""")
rep("""const r = s7Play(k, 'dom', inv, 72, false); if (!r) return; const up = []""", """const r = s7Play(k, 'dom', inv, bpm, false); if (!r) return; const up = []""")
rep("""      <div style={actNote}>{LANG === 'ko' ? <>7급은 딸림7화음을 <b>네 자리</b>로""", """      <div style={actNote}>{note || (LANG === 'ko' ? <>7급은 딸림7화음을 <b>네 자리</b>로""")
rep("""The dominant 7th of D: A C♯ E G. Tap the key the position starts on.</>}</div>""", """The dominant 7th of D: A C♯ E G. Tap the key the position starts on.</>)}</div>""")
rep("""body = <><SpKb lo={-12} hi={19} W={12} H={60} lit={Object.fromEntries(C.map(x => [x, done ? 'good' : 'cor']))} names={Object.fromEntries(C.map(x => [x, cwName(q.k, x)]))}/>""", """body = <><SpKb lo={cwRange(q.k)[0]} hi={cwRange(q.k)[1]} W={14} H={60} lit={Object.fromEntries(C.map(x => [x, done ? 'good' : 'cor']))} names={Object.fromEntries(C.map(x => [x, cwName(q.k, x)]))}/>""")   # Grade 8's keys (D, E♭) sit higher
rep("""if (pl != null && pl >= -12 && pl <= 19) lit[pl] = 'cor';
  return (
    <div className="try-box" style={actBox} data-a7="inv">""", """const hiK = Math.max(19, N[3] + 13); if (pl != null && pl >= -12 && pl <= hiK) lit[pl] = 'cor';
  return (
    <div className="try-box" style={actBox} data-a7="inv">""")
rep("""      <SpKb lo={-12} hi={19} W={14} H={70} lit={lit} names={Object.fromEntries(N.map((x, j) => [x, nm[j]]))} onTap={tap} label={t('Find the first note', '첫 음 찾기')}/>""", """      <SpKb lo={-12} hi={hiK} W={hiK > 19 ? 12 : 14} H={70} lit={lit} names={Object.fromEntries(N.map((x, j) => [x, nm[j]]))} onTap={tap} label={t('Find the first note', '첫 음 찾기')}/>""")   # the dominant 7th of E reaches A above the second octave
rep("""const ARPS_7_DRILL = { id: 'arps-7', label: 'Arpeggios and Progressions, Grade 7' };   // Build BV""",
    """const ARPS_7_DRILL = { id: 'arps-7', label: 'Arpeggios and Progressions, Grade 7' };   // Build BV
const ARPS_8_DRILL = { id: 'arps-8', label: 'Arpeggios and Progressions, Grade 8' };   // Build BZ""")
rep("""  { id: 'arps-7', label: 'Arpeggios and Progressions, Grade 7', concept: ARPS_7_DRILL, track: 'start' },   // Build BV""",
    """  { id: 'arps-7', label: 'Arpeggios and Progressions, Grade 7', concept: ARPS_7_DRILL, track: 'start' },   // Build BV
  { id: 'arps-8', label: 'Arpeggios and Progressions, Grade 8', concept: ARPS_8_DRILL, track: 'start' },   // Build BZ""")
rep("""'arps-7': '아르페지오와 화음 진행, Grade 7'""", """'arps-7': '아르페지오와 화음 진행, Grade 7', 'arps-8': '아르페지오와 화음 진행, Grade 8'""")
rep("""'arps-7': 'k-play'""", """'arps-7': 'k-play', 'arps-8': 'k-play'""")
rep("""  'arps-7': 'arpeggios grade 7""", """  'arps-8': 'arpeggios grade 8 e major e minor b flat major minor inversions chord progression I IV I64 V I cadential six four c d e flat dominant seventh diminished seventh cadenza',
  'arps-7': 'arpeggios grade 7""")
rep("""'arps-7': ['arps-6']""", """'arps-7': ['arps-6'], 'arps-8': ['arps-7']""")
rep("""'arps-7': ['Arpeggios 7', '아르페지오 7']""", """'arps-7': ['Arpeggios 7', '아르페지오 7'], 'arps-8': ['Arpeggios 8', '아르페지오 8']""")

CH = r'''
// ─── Chapter: Arpeggios and Progressions, Grade 8 (Build BZ, 2026-10-28; board call 26, the last room of the house) ───
Object.assign(AP_DATA, {   // the book's fingerings, Grade 8 pp77-79
  E: { en: 'E major', ko: 'E장조', r: 4, q: [0, 4, 7], nm: ['E', 'G♯', 'B'], R: [[1, 2, 3, 1, 2, 3, 5], [2, 1, 2, 4, 1, 2, 4], [1, 2, 4, 1, 2, 4, 5]], L: [[5, 3, 2, 1, 3, 2, 1], [3, 2, 1, 3, 2, 1, 2], [5, 3, 2, 1, 3, 2, 1]] },
  Em: { en: 'E minor', ko: 'E단조', r: 4, q: [0, 3, 7], nm: ['E', 'G', 'B'], R: [[1, 2, 3, 1, 2, 3, 5], [1, 2, 4, 1, 2, 4, 5], [1, 2, 3, 1, 2, 3, 5]], L: [[5, 4, 2, 1, 4, 2, 1], [5, 4, 2, 1, 4, 2, 1], [5, 3, 2, 1, 3, 2, 1]] },
  Bb: { en: 'B♭ major', ko: 'B♭장조', r: -2, q: [0, 4, 7], nm: ['B♭', 'D', 'F'], R: [[2, 1, 2, 4, 1, 2, 4], [1, 2, 4, 1, 2, 4, 5], [1, 2, 4, 1, 2, 4, 5]], L: [[3, 2, 1, 3, 2, 1, 2], [5, 4, 2, 1, 4, 2, 1], [5, 3, 2, 1, 3, 2, 1]] },
  Bbm: { en: 'B♭ minor', ko: 'B♭단조', r: -2, q: [0, 3, 7], nm: ['B♭', 'D♭', 'F'], R: [[2, 3, 1, 2, 3, 1, 2], [2, 1, 2, 3, 1, 2, 3], [1, 2, 3, 1, 2, 3, 5]], L: [[3, 2, 1, 3, 2, 1, 2], [2, 1, 3, 2, 1, 3, 2], [5, 3, 2, 1, 3, 2, 1]] },
});
const A8_KEYS = ['E', 'Em', 'Bb', 'Bbm'];
const A8ArpNote = () => (LANG === 'ko' ? <>8급 아르페지오: E와 B♭의 장·단, 기본형과 자리바꿈, 네 옥타브, (i) 모두 p (ii) 모두 f, {spMM(84)}. E장조는 7급의 D장조와 같은 운지, E단조는 D단조와 같아요. B♭단조는 흰건반이 F 하나: 엄지가 F에 살아요. 엄지가 치는 건반을 모두 눌러요.</>
  : <>Grade 8 arpeggios: E and B♭, major and minor, root position and inversions, four octaves, (i) all p (ii) all f, {spMM(84)}. E major fingers like Grade 7's D major, E minor like D minor. B♭ minor has one white key, F: the thumb lives there. Tap every key the thumb plays.</>);
function A8ArpPad(p) { return <ArpPosPad keys={A8_KEYS} g={8} note={<A8ArpNote/>} {...p}/>; }
const A8DimNote = () => (LANG === 'ko' ? <>'<b>E의 감7</b>'은 E의 이끔음 <b>D♯</b>에서: D♯ F♯ A C. '<b>B♭의 감7</b>'은 이끔음 <b>A</b>에서: A C E♭ G♭. 반음 셋씩. 네 옥타브, 모두 p와 모두 f, {spMM(84)}.</>
  : <>The "<b>diminished 7th of E</b>" starts on E's leading note, <b>D♯</b>: D♯ F♯ A C. The diminished 7th of B♭ starts on <b>A</b>: A C E♭ G♭. Three semitones each. Four octaves, all p and all f, {spMM(84)}.</>);
function A8DimPad(p) { return <Sev7Pad kind="dim" keys={['E', 'Bb']} g={8} note={<A8DimNote/>} {...p}/>; }
const A8InvNote = () => (LANG === 'ko' ? <>8급도 딸림7화음을 <b>네 자리</b>로, 새 두 조. E의 딸림7: <b>B D♯ F♯ A</b>. B♭의 딸림7: <b>F A C E♭</b>. 그 자리가 시작하는 건반을 눌러요. 네 옥타브, 모두 p와 모두 f, {spMM(84)}.</>
  : <>Grade 8 plays the dominant 7th in <b>four positions</b> too, in two new keys. The dominant 7th of E: <b>B D♯ F♯ A</b>. Of B♭: <b>F A C E♭</b>. Tap the key the position starts on. Four octaves, all p and all f, {spMM(84)}.</>);
function A8InvPad(p) { return <Dom7InvPad keys={['E', 'Bb']} bpm={84} note={<A8InvNote/>} {...p}/>; }
// ── make: one diminished 7th, four keys: any of its four notes can act as a leading note and rise a semitone to a new tonic ──
const FK_HOME = [[0, 'C'], [2, 'D'], [3, 'Eb']];
const FK_NAME = { maj: ['C', 'D♭', 'D', 'E♭', 'E', 'F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'B'], min: ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'B♭', 'B'] };
const fkKey = (pc, m) => (LANG === 'ko' ? FK_NAME[m][pc] + (m === 'maj' ? '장조' : '단조') : FK_NAME[m][pc] + (m === 'maj' ? ' major' : ' minor'));
const fkNear = (x, pcs) => { let best = null; for (let y = x - 6; y <= x + 6; y++) if (pcs.includes(spPc(y)) && (best == null || Math.abs(y - x) < Math.abs(best - x))) best = y; return best; };
const fkTri = (T, m) => [0, m === 'maj' ? 4 : 3, 7].map(x => spPc(T + x));
const fkDim = (home) => { const L = spPc(home - 1), v = [0, 3, 6, 9].map(x => spPc(L + x)).sort((a, b) => a - b); return v.map(x => (x < 3 ? x + 12 : x)).sort((a, b) => a - b); };   // close, from E♭ above middle C up
function FourKeysMaker() {
  const T = useSpTimers();
  const [hi, setHi] = useState(0), [m, setM] = useState('maj'), [door, setDoor] = useState(null), [tried, setTried] = useState([]), [now, setNow] = useState(-1);
  const home = FK_HOME[hi][0], D = fkDim(home), names = s7Names(FK_HOME[hi][1], 'dim'), dimPc = s7Notes(FK_HOME[hi][1], 'dim').map(spPc);
  const nameOf = (x) => names[dimPc.indexOf(spPc(x))];
  const go = (lead) => { T.clear(); const nT = spPc(lead + 1), hT = fkTri(home, 'maj'), nt = fkTri(nT, m);
    const homeV = [home - 12].concat(D.map(x => fkNear(x, hT))), dimV = [spPc(lead) - 12 - (spPc(lead) > 6 ? 12 : 0)].concat(D), resV = [nT - 12 - (nT > 7 ? 12 : 0)].concat(D.map(x => (spPc(x) === spPc(lead) ? x + 1 : fkNear(x, nt))));
    const v7 = [7, 11, 2, 5].map(x => spPc(nT + x)), v7V = [spPc(nT + 7) - 24].concat(resV.slice(1).map(x => fkNear(x, v7))), endV = [resV[0]].concat(v7V.slice(1).map(x => fkNear(x, nt)));
    const ch = [homeV, dimV, resV, v7V, endV], ev = ch.map((k, n) => ({ at: n * 1.2, keys: k, len: n === 4 ? 2.4 : 1.1, vol: 0.12 }));
    const r = spPlay(ev, 80); setDoor(lead); if (!tried.includes(spPc(lead))) setTried(tried.concat([spPc(lead)])); if (!r) return; ch.forEach((_, n) => T.at(r.ms(n * 1.2), () => setNow(n))); T.at(r.ms(6.4), () => setNow(-1)); };
  const lit = {}; D.forEach(x => { lit[x] = 'pale'; }); if (door != null) { lit[D.find(x => spPc(x) === spPc(door))] = 'cor'; lit[D.find(x => spPc(x) === spPc(door)) + 1] = 'good'; }
  const steps = [t('home', '집'), t('dim. 7th', '감7'), t('new key', '새 조'), 'V7', 'I'];
  return (
    <div className="try-box" style={actBox} data-mk="fourkeys">
      <div style={actTitle}>{t('One chord, four keys', '한 화음, 네 개의 조')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>감7화음의 네 음은 <b>어느 것이든 이끔음</b>이 될 수 있어요: 반음 올라가면 새 으뜸음. 그래서 감7 하나가 <b>네 조</b>로 이어져요. 집 조를 고르고, 네 음 중 하나를 골라 들어 봐요: 집 → 감7 → 새 조 → V7 → I.</> : <>Any of a diminished 7th's four notes can act as <b>a leading note</b>: up a semitone, and it is a new tonic. So one diminished 7th leads to <b>four keys</b>. Choose a home key, then one of the four notes, and listen: home → diminished 7th → new key → V7 → I.</>}</div>
      {spChips(FK_HOME.map(([x, k], j) => [j, fkKey(x, 'maj')]), hi, (j) => { T.clear(); setHi(j); setDoor(null); setTried([]); })}
      {spChips([['maj', t('to a major key', '장조로')], ['min', t('to a minor key', '단조로')]], m, (x) => { T.clear(); setM(x); setDoor(null); setTried([]); })}
      <SpKb lo={-2} hi={16} W={20} H={74} lit={lit} names={Object.fromEntries(D.map(x => [x, nameOf(x)]).concat(door != null ? [[D.find(x => spPc(x) === spPc(door)) + 1, FK_NAME[m][spPc(door + 1)]]] : []))} label={t('The diminished 7th of ' + fkKey(home, 'maj'), fkKey(home, 'maj') + '의 감7')}/>
      <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:6,marginTop:8}}>{D.map(x => <button key={x} className="choice-btn" onClick={() => go(x)} style={{padding:'8px 2px',fontSize:13.5,fontWeight:900,lineHeight:1.25,borderColor:door != null && spPc(door) === spPc(x) ? BK.coral : undefined}}>{nameOf(x)} ↗<br/><span style={{fontSize:12.5}}>{fkKey(spPc(x + 1), m)}</span>{tried.includes(spPc(x)) && <span style={{color:BK.green}}> ✓</span>}</button>)}</div>
      <div style={{display:'flex',justifyContent:'center',gap:4,flexWrap:'wrap',margin:'8px 0 2px'}}>{steps.map((x, n) => <span key={n} style={{padding:'4px 8px',borderRadius:6,fontSize:12,fontWeight:900,border:'1.5px solid ' + (now === n ? BK.coral : 'rgba(38,41,107,0.25)'),background:now === n ? '#fbe3da' : '#fff',color:BK.ink}}>{x}</span>)}</div>
      {spMsg(tried.length >= 4 ? t('All four keys from one chord!', '한 화음에서 네 조 모두!') : door != null ? t(nameOf(door) + ' rose a semitone to ' + FK_NAME[m][spPc(door + 1)] + ': ' + fkKey(spPc(door + 1), m) + '. ' + tried.length + ' of 4 keys.', nameOf(door) + '에서 반음 올라 ' + FK_NAME[m][spPc(door + 1)] + ': ' + fkKey(spPc(door + 1), m) + '. 네 조 중 ' + tried.length + '개.') : t('Tap one of the four notes.', '네 음 중 하나를 눌러요.'), tried.length >= 4 ? BK.green : undefined)}
    </div>
  );
}
const a8PicWalk = () => lsRawPic(['I', 'IV', 'I⁶₄', 'V', 'I'].map((x, i) => '<text x="' + (6 + i * 15) + '" y="28" font-family="Georgia, serif" font-size="11" font-weight="900" fill="' + (i === 2 ? '#e4572e' : '#26296b') + '">' + x + '</text>').join(''), [0, 0, 80, 44]);

function a8LbPages(scr = false) {
  const ch = 'arps-8', s8n = bkChapterNo('scales-8');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks = [[a8PicWalk(), t('I play I–IV–I⁶₄–V–I in C, D and E♭ from three positions', 'C, D, E♭장조에서 세 자리로 I–IV–I⁶₄–V–I을 쳐요')], [a6PicArp(), t('I play E and B♭ arpeggios, major and minor, from every note', 'E와 B♭의 장·단 아르페지오를 모든 음에서 쳐요')],
    [a7PicInv(), t('I play the dominant 7th of E and of B♭ in all four positions', 'E와 B♭의 딸림7화음을 네 자리 모두 쳐요')], [a6PicDim(), t('I find and play the diminished 7th of E and of B♭', 'E와 B♭의 감7화음을 찾아서 쳐요')]];
  const toc = [[t('I–IV–I⁶₄–V–I from three positions', '세 자리에서 I–IV–I⁶₄–V–I'), 2], [t('Arpeggios from every note', '모든 음에서 아르페지오'), 3], [t('The dominant 7th from every note', '모든 음에서 딸림7화음'), 4], [t('The diminished 7th of a key', '어느 조의 감7화음'), 5], [t('My four checks', '나의 네 가지 확인'), 6]];
  const walkStill = (k) => <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:10,width:'100%',maxWidth:720,margin:'0 auto'}}>{[1, 2, 3].map(p => <div key={p}><div style={{textAlign:'center',fontSize:12,fontWeight:900,color:BK.ink}}>{t('Position ' + p, '자리 ' + p)}: {cwChord(k, p, 'I').map(i => cwName(k, i)).join(' ')}</div>
    <SpKb lo={cwRange(k)[0]} hi={cwRange(k)[1]} W={scr ? 12 : 15} H={scr ? 44 : 80} lit={Object.fromEntries(cwChord(k, p, 'I').map(x => [x, 'cor']).concat(cwChord(k, p, 'IV').filter(x => !cwChord(k, p, 'I').includes(x)).map(x => [x, 'pale'])))} names={{}} k={1}/></div>)}</div>;
  const invStill = <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:scr ? 10 : 22,width:'100%',maxWidth:scr ? 760 : 640,margin:'0 auto'}}>{[0, 1, 2, 3].map(p => { const N = s7Notes('E', 'dom'), nm = s7Names('E', 'dom'), K = [0, 1, 2, 3, 4].map(j => N[(p + j) % 4] + 12 * Math.floor((p + j) / 4));
    return <div key={p}><div style={{textAlign:'center',fontSize:12.5,fontWeight:900,color:BK.ink}}>{t(D7_POS[p][0], D7_POS[p][1])}: {[0, 1, 2, 3].map(j => nm[(p + j) % 4]).join(' ')}</div><SpKb lo={-10} hi={26} W={scr ? 6 : 13} H={scr ? 40 : 72} lit={Object.fromEntries(K.map((x, j) => [x, j === 0 ? 'cor' : 'pale']))} names={{}} k={1}/></div>; })}</div>;
  const dimStill = <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{['E', 'Bb'].map(k => { const N = s7Notes(k, 'dim'), nm = s7Names(k, 'dim');
    return <div key={k}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{t('Diminished 7th of ' + S7_KEYS[k], S7_KEYS[k] + '의 감7')}: {nm.join(' ')}</div><SpKb lo={-12} hi={19} W={scr ? 9 : 16} H={scr ? 48 : 86} lit={Object.fromEntries(N.map(x => [x, 'cor']))} names={Object.fromEntries(N.map((x, j) => [x, nm[j]]))} k={1}/></div>; })}</div>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('The rest of the Grade 8 technical work (chapter ' + s8n + ' has the scales). From the technical work book, Grade 8: I–IV–I⁶₄–V–I chord progressions in C, D and E♭ major, from memory, mf, legato, ♩ = ca 72 (alternative fingerings are acceptable); arpeggios root position and inversions, E and B♭ major and minor, four octaves, hands separately and together, (i) all p (ii) all f, clear even legato, ♩ = 84 four notes a beat; dominant 7th arpeggios of E and of B♭, root position and inversions, the same qualities; diminished 7th arpeggios of E and of B♭, the same qualities. The book prints two octaves.', '8급 테크닉의 나머지(' + s8n + '장은 스케일). 테크닉 책의 8급: C, D, E♭장조 I–IV–I⁶₄–V–I 진행, 외워서, mf, 레가토, ♩ = 약 72(다른 운지도 괜찮아요); E와 B♭ 장·단 아르페지오, 기본형과 자리바꿈, 네 옥타브, 한 손씩 그리고 양손, (i) 모두 p (ii) 모두 f, 고르고 또렷한 레가토, ♩ = 84 한 박에 네 음; E와 B♭의 딸림7, 기본형과 자리바꿈, 같은 조건; E와 B♭의 감7, 같은 조건. 책은 두 옥타브만 인쇄해요.'))}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={140}><div style={{width:'100%'}}>{invStill}</div></LbPic>
      <LbSay size={18}>{t('The last room of the house: a five-chord walk with the cadential six-four, E and B♭ arpeggios, and the sevenths in every position.', '집의 마지막 방: 종지 6-4가 있는 다섯 화음 진행, E와 B♭ 아르페지오, 그리고 모든 자리의 7화음.')}</LbSay>
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
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('I–IV–I⁶₄–V–I from three positions', '세 자리에서 I–IV–I⁶₄–V–I')}
      teacher={<>{spTx(t('I–IV–I⁶₄–V–I chord progressions in C, D and E♭ major, from memory, mf, legato, ♩ = ca 72; alternative fingerings are acceptable. I⁶₄ is the cadential six-four: the right hand plays the notes of I while the bass moves to the 5th (the dominant); V keeps that bass note, an octave lower in the book (LH 5 2 1 5 2).', 'C, D, E♭장조 I–IV–I⁶₄–V–I 진행, 외워서, mf, 레가토, ♩ = 약 72; 다른 운지도 괜찮아요. I⁶₄는 종지 6-4: 오른손은 I의 음을 치고, 베이스는 5음(딸림음)으로 가요; V도 같은 베이스 음, 책에서는 한 옥타브 아래(왼손 5 2 1 5 2).'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={140}>{walkStill('C')}</LbPic>} live={<ChordWalkPad g={8}/>}/>
      <LbSay>{LANG === 'ko' ? <>V 앞에 <b>I⁶₄</b>(종지 6-4)가 끼었어요: 오른손은 I 그대로, 베이스만 <b>5음으로</b>. V도 같은 음을 베이스로 써요.</> : <><b>I⁶₄</b> (the cadential six-four) slips in before V: the right hand keeps I, only the bass moves <b>to the 5th</b>, and V keeps that same note in the bass.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>C장조, 자리 1: 오른손 다섯 화음.</>, <>왼손 베이스: C, F, G, 한 옥타브 아래 G, C. 손가락 5 2 1 5 2.</>, <>D와 E♭장조, 세 자리 모두. {spMM(72)} 정도로.</>]
        : [<>C major, position 1: the right hand's five chords.</>, <>The left hand's bass: C, F, G, then G an octave lower, C. Fingers 5 2 1 5 2.</>, <>D and E♭ major, all three positions. About {spMM(72)}.</>]}/>
      <LbRemember>{t('I⁶₄: I on top, the 5th below.', 'I⁶₄: 위는 I, 아래는 5음.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Arpeggios from every note', '모든 음에서 아르페지오')}
      teacher={<>{spTx(t('E and B♭ major and minor, root position and inversions, four octaves, hands separately and together, (i) all p (ii) all f, clear even legato, ♩ = 84. The book\'s fingerings (pp77-79): E major as D major in Grade 7 (RH 1 2 3…, 2 1 2 4…, 1 2 4…; LH 5 3 2 1…, 3 2 1 3…, 5 3 2 1…); E minor as D minor; B♭ major RH 2 1 2 4…, 1 2 4…, 1 2 4…, LH 3 2 1 3…, 5 4 2 1…, 5 3 2 1…; B♭ minor RH 2 3 1 2…, 2 1 2 3…, 1 2 3…, LH 3 2 1 3…, 2 1 3 2…, 5 3 2 1….', 'E와 B♭ 장·단, 기본형과 자리바꿈, 네 옥타브, 한 손씩 그리고 양손, (i) 모두 p (ii) 모두 f, 고르고 또렷한 레가토, ♩ = 84. 책의 운지(77-79쪽): E장조는 7급 D장조처럼(오른손 1 2 3…, 2 1 2 4…, 1 2 4…; 왼손 5 3 2 1…, 3 2 1 3…, 5 3 2 1…); E단조는 D단조처럼; B♭장조 오른손 2 1 2 4…, 1 2 4…, 1 2 4…, 왼손 3 2 1 3…, 5 4 2 1…, 5 3 2 1…; B♭단조 오른손 2 3 1 2…, 2 1 2 3…, 1 2 3…, 왼손 3 2 1 3…, 2 1 3 2…, 5 3 2 1….'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={150}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{[['E', 1], ['Bbm', 0]].map(([k, p]) => { const K = apKeys(k, p), F = AP_DATA[k].R[p];
        return <div key={k}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{t(AP_DATA[k].en + ', ' + AP_POS[p][0].toLowerCase(), AP_DATA[k].ko + ', ' + AP_POS[p][1])}</div><SpKb lo={K[0] - 1} hi={K[6] + 1} W={scr ? 14 : 18} H={scr ? 56 : 70} lit={Object.fromEntries(K.map((x, j) => [x, F[j] === 1 ? 'cor' : 'pale']))} names={Object.fromEntries(K.map((x, j) => [x, apNames(k, p)[j]]))} up={Object.fromEntries(K.map((x, j) => [x, F[j]]))}/></div>; })}</div></LbPic>} live={<A8ArpPad/>}/>
      <LbSay>{LANG === 'ko' ? <>E장·단조는 7급 D장·단조와 <b>같은 운지</b>. B♭단조는 흰건반 <b>F 하나</b>: 엄지가 거기.</> : <>E major and minor finger <b>just like</b> Grade 7's D major and minor. B♭ minor has <b>one white key, F</b>: the thumb's home.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>E장조 세 자리, 한 손씩, 모두 p.</>, <>E단조, 그다음 B♭장조와 B♭단조.</>, <>양손 네 옥타브, 모두 f도. {spMM(84)}까지.</>]
        : [<>E major in three positions, hands separately, all p.</>, <>E minor, then B♭ major and B♭ minor.</>, <>Hands together, four octaves, all f too. Up to {spMM(84)}.</>]}/>
      <LbRemember>{t('E like D; B♭ minor: the thumb on F.', 'E는 D처럼; B♭단조: 엄지는 F.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The dominant 7th from every note', '모든 음에서 딸림7화음')}
      teacher={<>{spTx(t('Dominant 7th arpeggios of E (B D♯ F♯ A) and of B♭ (F A C E♭), root position and inversions, four octaves, hands separately and together, (i) all p (ii) all f, clear even legato, ♩ = 84. Fingerings: the book\'s, pp80-81.', 'E(B D♯ F♯ A)와 B♭(F A C E♭)의 딸림7 아르페지오, 기본형과 자리바꿈, 네 옥타브, 한 손씩 그리고 양손, (i) 모두 p (ii) 모두 f, 고르고 또렷한 레가토, ♩ = 84. 운지: 책 80-81쪽.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={140}>{invStill}</LbPic>} live={<A8InvPad/>}/>
      <LbSay>{LANG === 'ko' ? <>7급과 같은 네 자리, 새 두 조. E의 딸림7은 <b>B D♯ F♯ A</b>, B♭의 딸림7은 <b>F A C E♭</b>.</> : <>The same four positions as Grade 7, two new keys. The dominant 7th of E is <b>B D♯ F♯ A</b>; of B♭, <b>F A C E♭</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>E의 딸림7, 기본형 두 옥타브.</>, <>D♯에서, F♯에서, A에서.</>, <>B♭의 딸림7도. 네 옥타브, {spMM(84)}까지.</>]
        : [<>The dominant 7th of E, root position, two octaves.</>, <>From D♯, from F♯, from A.</>, <>Then the dominant 7th of B♭. Four octaves, up to {spMM(84)}.</>]}/>
      <LbRemember>{t('Four notes, four starting places.', '네 음, 네 시작점.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The diminished 7th of a key', '어느 조의 감7화음')}
      teacher={<>{spTx(t('Diminished 7th arpeggios of E (D♯ F♯ A C) and of B♭ (A C E♭ G♭), four octaves, hands separately and together, (i) all p (ii) all f, clear even legato, ♩ = 84. In the toolbox, One chord, four keys: each of the four notes taken as a leading note, resolving to a new key (vii°7–I), then V7–I there.', 'E(D♯ F♯ A C)와 B♭(A C E♭ G♭)의 감7 아르페지오, 네 옥타브, 한 손씩 그리고 양손, (i) 모두 p (ii) 모두 f, 고르고 또렷한 레가토, ♩ = 84. 도구함의 \'한 화음, 네 개의 조\': 네 음을 하나씩 이끔음으로 삼아 새 조로 해결(vii°7–I), 그다음 그 조의 V7–I.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={140}>{dimStill}</LbPic>} live={<A8DimPad/>}/>
      <LbSay>{LANG === 'ko' ? <>이끔음에서 반음 셋씩. 네 음 모두 같은 거리라서, <b>어느 음이든 이끔음</b>이 될 수 있어요.</> : <>From the leading note, three semitones each. All four notes are the same distance apart, so <b>any of them</b> can act as the leading note.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>E의 감7: D♯ F♯ A C.</>, <>B♭의 감7: A C E♭ G♭.</>, <>양손 네 옥타브, 모두 p와 모두 f. {spMM(84)}까지.</>]
        : [<>The diminished 7th of E: D♯ F♯ A C.</>, <>The diminished 7th of B♭: A C E♭ G♭.</>, <>Hands together, four octaves, all p and all f. Up to {spMM(84)}.</>]}/>
      <LbRemember>{t('From the leading note, three semitones each.', '이끔음에서, 반음 셋씩.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My four checks', '나의 네 가지 확인')}
      teacher={<>{t('Each one played to you from memory at the book\'s speeds. Listen for the bass that stays from I⁶₄ to V, smooth thumbs, all four positions of each dominant 7th, and even dynamics.', '하나씩 외워서 책의 빠르기로 들려줘요. I⁶₄에서 V까지 머무는 베이스, 매끄러운 엄지, 딸림7마다 네 자리 모두, 고른 셈여림을 들어 주세요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey="pb_a8_four"/>}/>
    </LbPage>,
  ];
}
function Arps8LessonBook() { return <>{a8LbPages(false)}</>; }
function A8Learn({ onStart }) {
  const pages = a8LbPages(true), opener = pages[0];
  return (
    <Lesson id="arps-8" title={bkChapterName('arps-8')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="arps-8"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
const A8_LEVELS = [
  { n: 1, label: 'Grade 8 walk: I, IV or V?', kind: 'walk', time: 15 },
  { n: 2, label: 'E and B♭ arpeggios: which note does the thumb play?', kind: 'thumb', time: 15 },
  { n: 3, label: 'The dominant 7th of E or B♭: where does it start?', kind: 'inv', time: 15 },
  { n: 4, label: 'The diminished 7th of E or B♭: its notes', kind: 'dim', time: 20 },
];
Object.assign(LEVEL_KO, { 'Grade 8 walk: I, IV or V?': '8급 진행: I, IV, V?', 'E and B♭ arpeggios: which note does the thumb play?': 'E와 B♭ 아르페지오: 엄지가 치는 음은?', 'The dominant 7th of E or B♭: where does it start?': 'E나 B♭의 딸림7: 어디서 시작할까?', 'The diminished 7th of E or B♭: its notes': 'E나 B♭의 감7: 그 음들' });
function genA8Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'walk') { let k, pos, rn, g = 0; do { k = pick(CW_GR[8].keys); pos = pick([1, 2, 3]); rn = pick(['I', 'IV', 'V']); } while (prev && prev.key === k + pos + rn && g++ < 10); return { kind, k, pos, rn, answer: rn, choices: ['I', 'IV', 'V'], key: k + pos + rn, uid }; }
  if (kind === 'thumb') { let k, pos, h, g = 0; do { k = pick(A8_KEYS); pos = pick([0, 1, 2]); h = Math.random() < 0.5 ? 'R' : 'L'; } while (prev && prev.key === k + pos + h && g++ < 10); const F = AP_DATA[k][h][pos], j = F.indexOf(1);
    return { kind, k, pos, h, answer: apNames(k, pos)[j], choices: AP_DATA[k].nm.slice(), key: k + pos + h, uid }; }
  if (kind === 'inv') { let k, inv, g = 0; do { k = pick(['E', 'Bb']); inv = pick([0, 1, 2, 3]); } while (prev && prev.key === k + inv && g++ < 10); return { kind, k, inv, answer: s7Names(k, 'dom')[inv], choices: s7Names(k, 'dom'), key: k + inv, uid }; }
  let k, g = 0; do { k = pick(['E', 'Bb']); } while (prev && prev.key === 'dim' + k && g++ < 10); const right = s7Names(k, 'dim').join(' ');
  return { kind: 'dim', k, answer: right, choices: shuffle([right].concat(s7Wrong(k, 'dim'))), key: 'dim' + k, uid };
}
Object.assign(ARPS_8_DRILL, { levels: A8_LEVELS, generate: genA8Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: (q) => String(q.answer), Question: A7Question, Learn: A8Learn });
const A8_WB = {
  walk: [['C', 1, 'IV'], ['D', 2, 'V'], ['Eb', 3, 'IV'], ['C', 2, 'V']],
  thumb: [['E', 1, 'R'], ['E', 1, 'L'], ['Bbm', 0, 'R'], ['Bb', 0, 'L']],
  inv: [['E', 1], ['E', 3], ['Bb', 2], ['Bb', 3]],
  chk: { walk: [['D', 1, 'I'], ['Eb', 2, 'V'], ['C', 3, 'IV'], ['D', 2, 'IV']], thumb: [['Em', 1, 'R'], ['Bbm', 1, 'L'], ['E', 2, 'R'], ['Bb', 0, 'R']], inv: [['E', 2], ['Bb', 1], ['E', 0], ['Bb', 3]], dim: ['E', 'Bb'] },
};
function A8Teacher() {
  const pages = [], W = A8_WB;
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="arps-8" teacher>{content}</WbPage>);
  const thumbOf = ([k, p, h]) => { const F = AP_DATA[k][h][p]; return AP_DATA[k].en + ' ' + AP_POS[p][0].toLowerCase() + ' ' + h + 'H: ' + apNames(k, p)[F.indexOf(1)] + ' (' + F.join(' ') + ')'; };
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('arps-8')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>{spTx('The keys, speeds and fingerings are the technical work book\'s (Grade 8 pp76-82). Arpeggios four octaves (the book prints two), from memory. Another fingering is fine if it is logical and systematic.')}</div>
    <TcBlock page={2} title="I–IV–I⁶₄–V–I from three positions" answers={<>{tcAns('TRY IT', W.walk.map(([k, p, rn]) => CW_KEY[k][1] + ' major, position ' + p + ': ' + rn + ' = ' + cwChord(k, p, rn).map(x => cwName(k, x)).join(' ')))}{tcAns(spTx('C, D AND E♭ MAJOR, mf, ♩ = ca 72'), ['I⁶₄: I over the 5th in the bass', 'V: the same bass note, an octave lower (LH 5 2 1 5 2)'], null)}</>}
      watch="The bass from I⁶₄ to V: the same note, the dominant, dropped an octave (LH 1 then 5), while the right hand moves from I to V."
      say="“I⁶₄: I on top, the 5th below.”"/>
    <TcBlock page={3} title="Arpeggios from every note" answers={<>{tcAns('TRY IT', W.thumb.map(thumbOf))}</>}
      watch="B♭ minor's root position started with the thumb. The book starts RH on 2 (2 3 1 2…), the thumb on F."
      say="“E like D; B♭ minor: the thumb on F.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="The dominant 7th from every note" answers={<>{tcAns('TRY IT', W.inv.map(([k, i]) => 'of ' + S7_KEYS[k] + ', ' + D7_POS[i][0].toLowerCase() + ': from ' + s7Names(k, 'dom')[i]))}{tcAns('THE CHORDS', ['of E: ' + s7Names('E', 'dom').join(' '), 'of B♭: ' + s7Names('Bb', 'dom').join(' ')], null)}</>}
      watch="D♯ dropped in the dominant 7th of E (it is the leading note of E)."
      say="“Four notes, four starting places.”"/>
    <TcBlock page={5} title="The diminished 7th of a key" answers={<>{tcAns('THE CHORDS', ['of E: ' + s7Names('E', 'dim').join(' '), 'of B♭: ' + s7Names('Bb', 'dim').join(' ')], null)}</>}
      watch="G♭ written F♯ in the diminished 7th of B♭: A C E♭ G♭, each a minor 3rd."
      say="“From the leading note, three semitones each.”"/>
    <TcBlock page={6} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', W.chk.walk.map(([, , rn]) => rn))}{tcAns('B', W.chk.thumb.map(([k, p, h]) => apNames(k, p)[AP_DATA[k][h][p].indexOf(1)]), 5)}{tcAns('C', W.chk.inv.map(([k, i]) => s7Names(k, 'dom')[i]), 9)}{tcAns('D', W.chk.dim.map(k => s7Names(k, 'dim').join(' ')), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (A, B, C: 4 marks each, pass 3+; D: 2 marks, pass 2). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.5.</div></>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['arps-8'] = A8Teacher;
function A8Workbook({ startNo = 1 }) {
  const W = A8_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="arps-8">{content}</WbPage>);
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Name the chord" how="Each picture is one chord of the walk in the key shown. Write I, IV or V.">
      <BkGrid cols={2} gap="6px 10px">{W.walk.map(([k, p, rn], i) => { const C = cwChord(k, p, rn); return <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}>{s4wLabel(CW_KEY[k][1] + ' major')}
        <SpKb lo={cwRange(k)[0]} hi={cwRange(k)[1]} W={13} H={50} lit={Object.fromEntries(C.map(x => [x, 'cor']))} names={Object.fromEntries(C.map(x => [x, cwName(k, x)]))} k={1}/>
        <div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, rn, 50, 26)}</div></div></ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="Chord walks this week" how="Tick a box each day.">
      <PhLog rows={spTxRows(['C major, position 1: I IV I⁶₄ V I, the right hand alone', 'Add the bass: C F G, low G, C; then positions 2 and 3', 'D and E♭ major, from memory, about ♩ = 72'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={2}/>
    <Part kind="together" title="Where is the thumb?" how="Two octaves of each arpeggio. Write the note the thumb plays.">
      <BkGrid cols={2} gap="6px 10px">{W.thumb.map(([k, p, h], i) => { const K = apKeys(k, p), F = AP_DATA[k][h][p]; return <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}>{s4wLabel(AP_DATA[k].en + ', ' + AP_POS[p][0].toLowerCase() + ', ' + (h === 'R' ? 'right hand' : 'left hand'))}
        <SpKb lo={K[0] - 1} hi={K[6] + 1} W={12} H={48} lit={Object.fromEntries(K.map(x => [x, 'pale']))} names={Object.fromEntries(K.map((x, j) => [x, apNames(k, p)[j]]))} k={1}/>
        <div style={{display:'flex',alignItems:'center',justifyContent:'center',gap:8,fontSize:11.5,fontWeight:800,color:BK.ink}}>thumb: {nvBox(i === 0, apNames(k, p)[F.indexOf(1)], 44, 26)}</div></div></ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="Arpeggios this week" how="Tick a box each day.">
      <PhLog rows={spTxRows(['E major, three positions, each hand, all p then all f', 'E minor, B♭ major and B♭ minor', 'Hands together, four octaves, up to ♩ = 84'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Where does it start?" how="The dominant 7th in four positions. Write the note each one starts on.">
      <BkGrid cols={2} gap="6px 10px">{W.inv.map(([k, inv], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 6px',justifyItems:'center',fontSize:12,fontWeight:800,color:BK.ink,textAlign:'center'}}>{'Dominant 7th of ' + S7_KEYS[k] + ' (' + s7Names(k, 'dom').join(' ') + ')'}<span>{D7_POS[inv][0]}: {nvBox(i === 0, s7Names(k, 'dom')[inv], 44, 26)}</span></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Sevenths this week" how="Tick a box each day.">
      <PhLog rows={['The dominant 7th of E, all four positions, right hand', 'The dominant 7th of B♭ the same; then the left hand', 'The diminished 7ths of E and B♭, hands together']} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<A8PaperCheck/>);
  return <>{pages}</>;
}
function A8PaperCheck() {
  const C = A8_WB.chk;
  return <div className="lb-paper" style={{display:'flex',flexDirection:'column',gap:4}}>
    <LbPaperHead/>
    {bkSec('A', 'I, IV or V?')}
    <BkGrid cols={4} gap="6px 8px">{C.walk.map(([k, p, rn], i) => { const Cc = cwChord(k, p, rn); return <BkCell key={i} n={i + 1}><div style={{display:'grid',gap:3,padding:'14px 0 0',justifyItems:'center',fontSize:11,fontWeight:800,color:BK.ink,textAlign:'center'}}>{CW_KEY[k][1] + ' major: ' + Cc.map(x => cwName(k, x)).join(' ')}{bkBox(40, 24)}</div></BkCell>; })}</BkGrid>
    {bkSec('B', 'Which note does the thumb play?')}
    <BkGrid cols={4} gap="6px 8px">{C.thumb.map(([k, p, h], i) => <BkCell key={i} n={i + 5}><div style={{display:'grid',gap:3,padding:'14px 0 0',justifyItems:'center',fontSize:11,fontWeight:800,color:BK.ink,textAlign:'center'}}>{AP_DATA[k].en + ', ' + ['root', '1st inv.', '2nd inv.'][p] + ', ' + h + 'H'}{bkBox(40, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('C', 'The dominant 7th: which note does it start on?')}
    <BkGrid cols={4} gap="6px 8px">{C.inv.map(([k, inv], i) => <BkCell key={i} n={i + 9}><div style={{display:'grid',gap:3,padding:'14px 0 0',justifyItems:'center',fontSize:11,fontWeight:800,color:BK.ink,textAlign:'center'}}>{'of ' + S7_KEYS[k] + ', ' + ['root', '1st inv.', '2nd inv.', '3rd inv.'][inv]}{bkBox(40, 24)}</div></BkCell>)}</BkGrid>
    {bkSec('D', 'Write the diminished 7th')}
    <BkGrid cols={2} gap="6px 8px">{C.dim.map((k, i) => <BkCell key={i} n={i + 13}><div style={{display:'grid',gap:3,padding:'14px 0 0',justifyItems:'center',fontSize:11.5,fontWeight:800,color:BK.ink,textAlign:'center'}}>{'of ' + S7_KEYS[k]}{bkBox(170, 24)}</div></BkCell>)}</BkGrid>
  </div>;
}
WORKBOOKS['arps-8'] = A8Workbook;
'''
rep("""WORKBOOKS['arps-7'] = A7Workbook;""", """WORKBOOKS['arps-7'] = A7Workbook;""" + CH)

HOME = r'''
// ══ Build BZ: Arpeggios and Progressions, Grade 8 on the Home (Technique, Playing scales and chords) ══
LBH_FN['arps-8'] = (s) => a8LbPages(s);
const a8HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'k-play', 'tech', en, ko, benEn, bko, lbhSpec('arps-8', i, { make }));
const a8InvQ = (n, prev) => { const q = genA8Question(A8_LEVELS[2], prev);
  return { kind: 'choice', cols: 4, key: q.key, prompt: ['The dominant 7th of ' + S7_KEYS[q.k] + ', ' + D7_POS[q.inv][0].toLowerCase() + ': which note does it start on?', S7_KEYS[q.k] + '의 딸림7, ' + D7_POS[q.inv][1] + ': 어느 음에서 시작할까요?'], opts: q.choices.map(x => ({ id: x, label: () => x })), ans: q.answer, ok: (v) => v === q.answer,
    play: () => s7Play(q.k, 'dom', q.inv, 84, false), fig: () => ({ mid: null }), yes: ['Yes: from ' + q.answer + '.', '맞아요: ' + q.answer + '에서.'], no: ['It starts on ' + q.answer + ': ' + s7Names(q.k, 'dom').join(' ') + '.', q.answer + '에서 시작해요: ' + s7Names(q.k, 'dom').join(' ') + '.'] }; };
const a8DimQ = (n, prev) => { const k = n % 2 ? 'Bb' : 'E', right = s7Names(k, 'dim').join(' '), opts = shuffle([right].concat(s7Wrong(k, 'dim')));
  return { kind: 'choice', cols: 1, key: k + n, prompt: ['The diminished 7th of ' + S7_KEYS[k] + ': which notes?', S7_KEYS[k] + '의 감7화음: 어떤 음들?'], opts: opts.map(x => ({ id: x, label: () => x })), ans: right, ok: (v) => v === right,
    play: () => s7Play(k, 'dim'), fig: (c) => ({ mid: c.res ? <SpKb lo={-12} hi={19} W={12} H={60} lit={Object.fromEntries(s7Notes(k, 'dim').map(x => [x, 'cor']))} names={Object.fromEntries(s7Notes(k, 'dim').map((x, j) => [x, s7Names(k, 'dim')[j]]))}/> : null }),
    yes: ['Yes: ' + right + '.', '맞아요: ' + right + '.'], no: ['It was ' + right + ': from the leading note, three semitones each.', '정답은 ' + right + ': 이끔음에서 반음 셋씩.'] }; };
a8HomeAdd('a8-walk', 1, 'I–IV–I⁶₄–V–I from three positions', '세 자리에서 I–IV–I⁶₄–V–I', 'The cadential six-four: I on top, the 5th below.', '종지 6-4: 위는 I, 아래는 5음.', lwTapQ(ChordWalkPad, (n) => ({ g: 8, fixed: { k: CW_GR[8].keys[n % 3], pos: 1 + (n % 3) } }), ['Tap the three notes of the next chord.', '다음 화음의 세 음을 눌러요.'], ['Walked ✓', '진행했어요 ✓']));
a8HomeAdd('a8-arp', 2, 'E and B♭ arpeggios from every note', 'E와 B♭ 아르페지오, 모든 음에서', 'Where does the thumb go?', '엄지는 어디에?', lwTapQ(A8ArpPad, (n) => ({ fixed: { k: A8_KEYS[n % 4], pos: n % 3, h: n % 2 ? 'L' : 'R' } }), ['Tap every key the thumb plays.', '엄지가 치는 건반을 모두 눌러요.'], ['Found them ✓', '찾았어요 ✓']));
a8HomeAdd('a8-inv', 3, 'The dominant 7th of E and B♭, every position', 'E와 B♭의 딸림7, 모든 자리', 'One note further up each time.', '자리마다 한 음 위.', a8InvQ);
a8HomeAdd('a8-dim', 4, 'The diminished 7th of E and B♭', 'E와 B♭의 감7화음', 'From the leading note, three semitones each.', '이끔음에서 반음 셋씩.', a8DimQ);
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""check: 'scales-8' },   // Build BY""", """check: 'scales-8' },   // Build BY
    { id: 'kpl-a8', en: 'Arpeggios and progressions, Grade 8', ko: '아르페지오와 화음 진행, Grade 8', lessons: ['a8-walk', 'a8-arp', 'a8-inv', 'a8-dim', 'mk-fourkeys'], check: 'arps-8' },   // Build BZ""")
rep("""  set('8', 's8-grand s8-poly s8-apart s8-sixes s8-dt mk-thirds');   // Build BY: Scales, Grade 8""", """  set('8', 's8-grand s8-poly s8-apart s8-sixes s8-dt mk-thirds');   // Build BY: Scales, Grade 8
  set('8', 'a8-walk a8-arp a8-inv a8-dim mk-fourkeys');   // Build BZ: Arpeggios and Progressions, Grade 8""")
rep("""  { id: 'mk-cad', ch: 'listen-6',""", """  { id: 'mk-fourkeys', ch: 'arps-8', title: 'One chord, four keys', blurb: 'One diminished 7th, four leading notes: each one rises a semitone into a new key.', C: () => <FourKeysMaker/> },   // Build BZ
  { id: 'mk-cad', ch: 'listen-6',""")
rep("""  'mk-cad': ['나만의 끝 만들기',""", """  'mk-fourkeys': ['한 화음, 네 개의 조', '감7 하나, 이끔음 넷: 하나하나 반음 올라 새 조로.'],
  'mk-cad': ['나만의 끝 만들기',""")
rep("""'mk-cad': ['chords', 3, 3, 'game ear'],""", """'mk-cad': ['chords', 3, 3, 'game ear'], 'mk-fourkeys': ['chords', 3, 3, 'game ear'],""")
rep("""'mk-cad': 'p-chords',""", """'mk-cad': 'p-chords', 'mk-fourkeys': 'p-chords',""")
rep("""  'mk-cad': () => (\n""", """  'mk-fourkeys': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/>{[19, 14.5, 10, 5.5].map((y, i) => <ellipse key={i} cx="8" cy={y} rx="3" ry="2.1" fill="#fefbf3"/>)}<path d="M13 15 L20 8 M16 8 H20 V12" fill="none" stroke="#e9a83a" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/></svg>
  ),
  'mk-cad': () => (\n""")
rep("""const LESSON_BOOKS = { 'scales-8': Scales8LessonBook,""", """const LESSON_BOOKS = { 'arps-8': Arps8LessonBook, 'scales-8': Scales8LessonBook,""")
rep("""const LB_PAGE_FNS = { 'scales-8': s8LbPages,""", """const LB_PAGE_FNS = { 'arps-8': a8LbPages, 'scales-8': s8LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"arps-8": "<ellipse cx=\\"10\\" cy=\\"38\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 10 38)\\" fill=\\"#26296b\\"/><ellipse cx=\\"19\\" cy=\\"30\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 19 30)\\" fill=\\"#26296b\\"/><ellipse cx=\\"28\\" cy=\\"22\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 28 22)\\" fill=\\"#26296b\\"/><ellipse cx=\\"37\\" cy=\\"14\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 37 14)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><text x=\\"38\\" y=\\"40\\" font-size=\\"11\\" font-weight=\\"900\\" fill=\\"#26296b\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">8</text>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
