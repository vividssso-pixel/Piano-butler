import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BV (board call 26, the third Grade 7 room): Arpeggios and Progressions, Grade 7, from the technical work book (Grade 7
# pp54-59, read 28 Oct): I–IV–V–I chord progressions in G, F and E major; arpeggios, root position and inversions, D and A♭ major
# and minor, four octaves, (i) all p (ii) all f, ♩ = 72; the dominant 7th of D and of A♭, root position and inversions; the
# diminished 7th of D and of A♭. Fingerings are the book's (D major, first inversion: the right hand's thumb on A, the left
# hand's on D). The thing to make: an accompaniment, Alberti, waltz or broken chords, under a tune of your own.

rep("""const ARPS_6_DRILL = { id: 'arps-6', label: 'Arpeggios and Progressions, Grade 6' };   // Build BQ""",
    """const ARPS_6_DRILL = { id: 'arps-6', label: 'Arpeggios and Progressions, Grade 6' };   // Build BQ
const ARPS_7_DRILL = { id: 'arps-7', label: 'Arpeggios and Progressions, Grade 7' };   // Build BV""")
rep("""  { id: 'arps-6', label: 'Arpeggios and Progressions, Grade 6', concept: ARPS_6_DRILL, track: 'start' },   // Build BQ""",
    """  { id: 'arps-6', label: 'Arpeggios and Progressions, Grade 6', concept: ARPS_6_DRILL, track: 'start' },   // Build BQ
  { id: 'arps-7', label: 'Arpeggios and Progressions, Grade 7', concept: ARPS_7_DRILL, track: 'start' },   // Build BV""")
rep("""'arps-6': '아르페지오와 화음 진행, Grade 6'""", """'arps-6': '아르페지오와 화음 진행, Grade 6', 'arps-7': '아르페지오와 화음 진행, Grade 7'""")
rep("""'arps-6': 'k-play'""", """'arps-6': 'k-play', 'arps-7': 'k-play'""")
rep("""  'arps-6': 'arpeggios grade 6""", """  'arps-7': 'arpeggios grade 7 d major d minor a flat major minor inversions chord progression I IV V I g f e dominant seventh inversions diminished seventh accompaniment alberti waltz broken chords',
  'arps-6': 'arpeggios grade 6""")
rep("""'arps-6': ['scales-5', 'chords']""", """'arps-6': ['scales-5', 'chords'], 'arps-7': ['arps-6']""")
rep("""'arps-6': ['Arpeggios 6', '아르페지오 6']""", """'arps-6': ['Arpeggios 6', '아르페지오 6'], 'arps-7': ['Arpeggios 7', '아르페지오 7']""")
# the chord walk: where no note stays (IV to V), say so
rep("""        : bad ? t('Not quite: keep ' + stays.map(x => cwName(k, x)).join(' and ') + ', and move the others one step.', '아니에요: 그대로 둘 음 ' + stays.map(x => cwName(k, x)).join(', ') + '. 나머지는 한 걸음.')""",
    """        : bad ? (stays.length ? t('Not quite: keep ' + stays.map(x => cwName(k, x)).join(' and ') + ', and move the others one step.', '아니에요: 그대로 둘 음 ' + stays.map(x => cwName(k, x)).join(', ') + '. 나머지는 한 걸음.') : t('Not quite: no note stays here; move each note to the nearest note of ' + cwRn(G.prog[at]) + '.', '아니에요: 여기는 그대로인 음이 없어요; 음마다 ' + cwRn(G.prog[at]) + '의 가장 가까운 음으로.'))""")
# the arpeggio pad: a Grade 7 note (two white keys in D) and messages that do not assume one white key
rep("""function ArpPosPad({ keys = ['Eb', 'Fsm', 'Fs', 'Ebm'], onResult, fixed }) {""", """function ArpPosPad({ keys = ['Eb', 'Fsm', 'Fs', 'Ebm'], onResult, fixed, note, g = 6 }) {""")
rep("""      <div style={actNote}>{LANG === 'ko' ? <>같은 세 음, 시작만 달라요: <b>기본형</b>은 으뜸음에서""", """      <div style={actNote}>{note || (LANG === 'ko' ? <>같은 세 음, 시작만 달라요: <b>기본형</b>은 으뜸음에서""")
rep("""All black keys? Use the C-major shape: the thumb on the first note. Tap every key the thumb plays.</>}</div>""", """All black keys? Use the C-major shape: the thumb on the first note. Tap every key the thumb plays.</>)}</div>""")
rep("""      {spMsg(done ? t(spHand(h) + ': ' + F.join(' ') + '. ' + (W.length ? 'The thumb on ' + W[0] + ', the white key.' : 'All black: the C-major shape.'), spHand(h) + ': ' + F.join(' ') + '. ' + (W.length ? '엄지는 흰건반 ' + W[0] + '에.' : '모두 검은건반: C장조 모양.'))""",
    """      {spMsg(done ? (g >= 7 && W.length !== 1 ? t(spHand(h) + ': ' + F.join(' ') + '. The thumb on ' + [...new Set(thumbs.map(x => apNames(k, pos)[K.indexOf(x)]))].join(' and ') + '.', spHand(h) + ': ' + F.join(' ') + '. 엄지는 ' + [...new Set(thumbs.map(x => apNames(k, pos)[K.indexOf(x)]))].join(', ') + '에.') : t(spHand(h) + ': ' + F.join(' ') + '. ' + (W.length ? 'The thumb on ' + W[0] + ', the white key.' : 'All black: the C-major shape.'), spHand(h) + ': ' + F.join(' ') + '. ' + (W.length ? '엄지는 흰건반 ' + W[0] + '에.' : '모두 검은건반: C장조 모양.')))""")
rep("""        : bad != null ? t(W.length ? 'Not there: find the white key, ' + W[0] + '.'""", """        : bad != null ? (g >= 7 && W.length > 1 ? t('Not there: the thumb takes a white key, but which one? Try another.', '거기가 아니에요: 엄지는 흰건반에, 그런데 어느 것? 다른 것을 눌러 봐요.') : t(W.length ? 'Not there: find the white key, ' + W[0] + '.'""")
rep("""'거기가 아니에요: 모두 검은건반이라 엄지가 묶음마다 시작해요.') : t('Where does the thumb go?""", """'거기가 아니에요: 모두 검은건반이라 엄지가 묶음마다 시작해요.')) : t('Where does the thumb go?""")
# the diminished 7th pad: a note for another grade
rep("""function Sev7Pad({ kind = 'dom', keys = ['Fs', 'Eb', 'C', 'G', 'F'], onResult, fixed, g = 6 }) {""", """function Sev7Pad({ kind = 'dom', keys = ['Fs', 'Eb', 'C', 'G', 'F'], onResult, fixed, g = 6, note }) {""")
rep("""      <div style={actNote}>{kind === 'dom' ? (LANG === 'ko' ? <>책의 '<b>F♯의 딸림7</b>'""", """      <div style={actNote}>{note || (kind === 'dom' ? (LANG === 'ko' ? <>책의 '<b>F♯의 딸림7</b>'""")
rep("""It looks the same from any of its notes.</>)}</div>""", """It looks the same from any of its notes.</>))}</div>""")

CH = r'''
// ─── Chapter: Arpeggios and Progressions, Grade 7 (Build BV, 2026-10-28; board call 26, the third Grade 7 room) ───
// ── step 2: the book's arpeggio fingerings, two octaves up, by position (Grade 7 pp55-57) ──
Object.assign(AP_DATA, {
  D: { en: 'D major', ko: 'D장조', r: 2, q: [0, 4, 7], nm: ['D', 'F♯', 'A'], R: [[1, 2, 3, 1, 2, 3, 5], [2, 1, 2, 4, 1, 2, 4], [1, 2, 4, 1, 2, 4, 5]], L: [[5, 3, 2, 1, 3, 2, 1], [3, 2, 1, 3, 2, 1, 2], [5, 3, 2, 1, 3, 2, 1]] },
  Dm: { en: 'D minor', ko: 'D단조', r: 2, q: [0, 3, 7], nm: ['D', 'F', 'A'], R: [[1, 2, 3, 1, 2, 3, 5], [1, 2, 4, 1, 2, 4, 5], [1, 2, 3, 1, 2, 3, 5]], L: [[5, 4, 2, 1, 4, 2, 1], [5, 4, 2, 1, 4, 2, 1], [5, 3, 2, 1, 3, 2, 1]] },
  Ab: { en: 'A♭ major', ko: 'A♭장조', r: -4, q: [0, 4, 7], nm: ['A♭', 'C', 'E♭'], R: [[2, 1, 2, 4, 1, 2, 4], [1, 2, 4, 1, 2, 4, 5], [2, 4, 1, 2, 4, 1, 2]], L: [[2, 1, 4, 2, 1, 4, 2], [5, 4, 2, 1, 4, 2, 1], [4, 2, 1, 4, 2, 1, 2]] },
  Abm: { en: 'A♭ minor', ko: 'A♭단조', r: -4, q: [0, 3, 7], nm: ['A♭', 'C♭', 'E♭'], R: [[2, 1, 2, 4, 1, 2, 4], [1, 2, 4, 1, 2, 4, 5], [2, 4, 1, 2, 4, 1, 2]], L: [[2, 1, 4, 2, 1, 4, 2], [5, 4, 2, 1, 4, 2, 1], [4, 2, 1, 4, 2, 1, 2]] },
});
const A7_KEYS = ['D', 'Dm', 'Ab', 'Abm'];
const A7ArpNote = () => (LANG === 'ko' ? <>7급 아르페지오: D와 A♭의 장3화음, 단3화음을 기본형과 자리바꿈으로, 네 옥타브, (i) 모두 p (ii) 모두 f, {spMM(72)}. <b>A♭</b>은 흰건반이 하나(C, 단조는 C♭): 엄지가 거기 살아요. <b>D</b>는 흰건반이 둘 이상(D와 A, 단조는 F까지): 엄지가 그중 어디로 가는지 책의 운지에서 찾아요. 엄지가 치는 건반을 모두 눌러요.</>
  : <>Grade 7 arpeggios: D and A♭, major and minor, root position and inversions, four octaves, (i) all p (ii) all f, {spMM(72)}. <b>A♭</b> has one white key (C, or C♭ in the minor): the thumb lives there. <b>D</b> has two or more (D and A, and F in the minor): find which one the thumb takes in the book's fingering. Tap every key the thumb plays.</>);
function A7ArpPad(p) { return <ArpPosPad keys={A7_KEYS} g={7} note={<A7ArpNote/>} {...p}/>; }
// ── step 3: the dominant 7th from every note: root position and three inversions (each starts on the next note up) ──
const D7_POS = [['Root position', '기본형'], ['First inversion', '첫째 자리바꿈'], ['Second inversion', '둘째 자리바꿈'], ['Third inversion', '셋째 자리바꿈']];
function Dom7InvPad({ keys = ['D', 'Ab'], onResult, fixed }) {
  const T = useSpTimers();
  const [k, setK] = useState(fixed ? fixed.k : keys[0]), [inv, setInv] = useState(fixed ? fixed.inv : 1), [hit, setHit] = useState(false), [bad, setBad] = useState(null), [miss, setMiss] = useState(0), [pl, setPl] = useState(null);
  const N = s7Notes(k, 'dom'), nm = s7Names(k, 'dom'), want = spPc(N[inv]);
  const reset = (fn) => { T.clear(); setHit(false); setBad(null); setMiss(0); setPl(null); if (fn) fn(); };
  const run = () => { T.clear(); const r = s7Play(k, 'dom', inv, 72, false); if (!r) return; const up = []; for (let j = 0; j <= 8; j++) { const d = inv + j; up.push(N[d % 4] + 12 * Math.floor(d / 4)); } const sq = up.concat(up.slice(0, -1).reverse());
    sq.forEach((x, n) => T.at(r.ms(n / 4), () => setPl(x))); T.at(r.ms(sq.length / 4 + 0.3), () => setPl(null)); };
  const tap = (i) => { playKey(i, 0.4); if (hit) return; if (spPc(i) === want) { setHit(true); setBad(null); if (onResult) onResult({ ok: miss === 0 }); setTimeout(run, 300); } else { setBad(i); setMiss(m => m + 1); } };
  const lit = {}; N.forEach(x => { lit[x] = 'pale'; lit[x + 12] = 'pale'; }); if (hit) { lit[N[inv]] = 'good'; } if (bad != null) lit[bad] = 'bad'; if (pl != null && pl >= -12 && pl <= 19) lit[pl] = 'cor';
  return (
    <div className="try-box" style={actBox} data-a7="inv">
      <div style={actTitle}>{t('The dominant 7th from every note', '모든 음에서 딸림7화음')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>7급은 딸림7화음을 <b>네 자리</b>로: 기본형은 첫 음에서, 첫째 자리바꿈은 둘째 음에서, 둘째는 셋째 음에서, <b>셋째 자리바꿈</b>은 넷째 음(7음)에서. D의 딸림7: A C♯ E G. 그 자리가 시작하는 건반을 눌러요.</> : <>Grade 7 plays the dominant 7th in <b>four positions</b>: root position starts on its first note, first inversion on the second, second inversion on the third, and <b>third inversion</b> on the fourth (the 7th). The dominant 7th of D: A C♯ E G. Tap the key the position starts on.</>}</div>
      {!fixed && spChips(keys.map(x => [x, t('of ' + S7_KEYS[x], S7_KEYS[x] + '의')]), k, (x) => reset(() => setK(x)))}
      {!fixed && spChips([0, 1, 2, 3].map(p => [p, t(D7_POS[p][0], D7_POS[p][1])]), inv, (x) => reset(() => setInv(x)))}
      <div style={{display:'flex',justifyContent:'center',gap:6,margin:'2px 0 6px'}}>{nm.map((x, j) => <span key={j} style={{minWidth:40,padding:'5px 6px',borderRadius:8,border:'1.5px solid ' + (j === inv ? BK.coral : 'rgba(38,41,107,0.25)'),background:j === inv ? '#fbe3da' : '#fff',textAlign:'center',fontWeight:900,fontSize:15,color:BK.ink}}>{x}<div style={{fontSize:10,fontWeight:800,color:BK.muted}}>{['1', '3', '5', '7'][j]}</div></span>)}</div>
      <SpKb lo={-12} hi={19} W={14} H={70} lit={lit} names={Object.fromEntries(N.map((x, j) => [x, nm[j]]))} onTap={tap} label={t('Find the first note', '첫 음 찾기')}/>
      {spMsg(hit ? t(D7_POS[inv][0] + ': it starts on ' + nm[inv] + ': ' + [0, 1, 2, 3, 4].map(j => nm[(inv + j) % 4]).join(' ') + '…', D7_POS[inv][1] + ': ' + nm[inv] + '에서 시작: ' + [0, 1, 2, 3, 4].map(j => nm[(inv + j) % 4]).join(' ') + '…') : bad != null ? t('Not that one: count along the chord, A C♯ E G.', '그 건반이 아니에요: 화음을 따라 세어요.') : t(D7_POS[inv][0] + ': where does it start?', D7_POS[inv][1] + ': 어디서 시작할까요?'), hit ? BK.green : bad != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={run}>{t('▶ Hear it, two octaves', '▶ 두 옥타브 듣기')}</button>
        {hit && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset(() => setInv((inv + 1) % 4))}>{t('▶ Next position', '▶ 다음 자리')}</button>}
      </div>
    </div>
  );
}
// ── step 4: the diminished 7th of D and of A♭ ──
const A7DimNote = () => (LANG === 'ko' ? <>'<b>D의 감7</b>'은 D의 <b>이끔음 C♯</b>에서 시작해요: C♯ E G B♭, 반음 셋씩. 'A♭의 감7'은 이끔음 G에서: G B♭ D♭ F♭(E와 같은 건반). 네 옥타브, 모두 p와 모두 f, {spMM(72)}.</>
  : <>The "<b>diminished 7th of D</b>" starts on D's <b>leading note, C♯</b>: C♯ E G B♭, three semitones each. The diminished 7th of A♭ starts on its leading note, G: G B♭ D♭ F♭ (the same key as E). Four octaves, all p and all f, {spMM(72)}.</>);
function A7DimPad(p) { return <Sev7Pad kind="dim" keys={['D', 'Ab']} g={7} note={<A7DimNote/>} {...p}/>; }
// ── make: an accompaniment under a tune of your own: Alberti, waltz or broken chords, under I–IV–V–I or I–vi–IV–V ──
const AC_PAT = { alberti: ['Alberti bass', '알베르티 베이스'], waltz: ['Waltz', '왈츠'], broken: ['Broken chords', '분산 화음'] };
const AC_PROG = { a: ['I', 'IV', 'V', 'I'], b: ['I', 'vi', 'IV', 'V'] };
const acEvents = (key, prog, pat) => { const V = cadVoice(key, prog), ev = []; const bar = pat === 'waltz' ? 3 : 4;
  V.forEach((v, b) => { const c = v.up.map(x => x - 12).sort((a, b2) => a - b2), at = b * bar;
    if (pat === 'alberti') [0, 2, 1, 2, 0, 2, 1, 2].forEach((j, q) => ev.push({ at: at + q / 2, keys: [c[j]], len: 0.48, vol: 0.1 }));
    else if (pat === 'waltz') { ev.push({ at, keys: [v.bass], len: 0.95, vol: 0.12 }); ev.push({ at: at + 1, keys: c, len: 0.6, vol: 0.08 }); ev.push({ at: at + 2, keys: c, len: 0.6, vol: 0.08 }); }
    else [v.bass, c[0], c[1], c[2], c[0] + 12, c[2], c[1], c[0]].forEach((x, q) => ev.push({ at: at + q / 2, keys: [x], len: 0.48, vol: 0.1 })); });
  return { ev, len: V.length * bar }; };
function AccompMaker() {
  const T = useSpTimers();
  const [key, setKey] = useState(0), [prog, setProg] = useState('a'), [pat, setPat] = useState('alberti'), [bar, setBar] = useState(-1), [loop, setLoop] = useState(false), lp = useRef(false);
  const play = () => { T.clear(); const E = acEvents(key, AC_PROG[prog], pat), bpm = pat === 'waltz' ? 132 : 96, r = spPlay(E.ev, bpm); if (!r) return; const bl = pat === 'waltz' ? 3 : 4;
    for (let b = 0; b < 4; b++) T.at(r.ms(b * bl), () => setBar(b)); T.at(r.ms(E.len), () => { setBar(-1); if (lp.current) play(); }); };
  const toggle = () => { const v = !loop; setLoop(v); lp.current = v; if (v) play(); else { T.clear(); setBar(-1); } };
  useEffect(() => () => { lp.current = false; }, []);
  const names = {}; for (let x = 0; x <= 19; x++) if (MOD_SC.M.includes(spPc(x - key))) names[x] = lwLet(x).replace('G♭', 'F♯');
  const lit = {}; Object.keys(names).forEach(x => { lit[x] = 'pale'; }); lit[spPc(key) + (spPc(key) > 7 ? 0 : 12)] = 'cor';
  return (
    <div className="try-box" style={actBox} data-mk="accomp">
      <div style={actTitle}>{t('My accompaniment', '나의 반주')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>아르페지오는 반주가 돼요. 무늬(<b>알베르티 베이스</b>, <b>왈츠</b>, <b>분산 화음</b>)와 화음 진행을 골라 반주를 틀고, 위의 건반으로 내 선율을 얹어요. 흐린 건반은 그 조의 음, 빨간 건반이 으뜸음.</> : <>Arpeggios become accompaniments. Choose a pattern (<b>Alberti bass</b>, <b>waltz</b> or <b>broken chords</b>) and a progression, start it, and play a tune of your own on the keys above. The pale keys are the key's notes; the coral one is the tonic.</>}</div>
      {spChips([[0, t('C major', 'C장조')], [7, t('G major', 'G장조')], [5, t('F major', 'F장조')]], key, (v) => { setKey(v); })}
      {spChips(Object.keys(AC_PAT).map(x => [x, t(AC_PAT[x][0], AC_PAT[x][1])]), pat, setPat)}
      {spChips(Object.keys(AC_PROG).map(x => [x, AC_PROG[x].join(' – ')]), prog, setProg)}
      <div style={{display:'flex',justifyContent:'center',gap:6,margin:'4px 0 8px'}}>{AC_PROG[prog].map((rn, j) => <span key={j} style={{minWidth:44,padding:'6px 8px',borderRadius:8,textAlign:'center',fontFamily:LB_SERIF,fontSize:18,fontWeight:900,border:'1.5px solid ' + (bar === j ? BK.coral : 'rgba(38,41,107,0.25)'),background:bar === j ? '#fbe3da' : '#fff',color:BK.ink}}>{rn}</span>)}</div>
      <SpKb lo={0} hi={19} W={22} H={76} lit={lit} names={names} onTap={(x) => playKey(x, 0.6)} label={t('Your tune', '내 선율')}/>
      {spMsg(loop ? t('Round and round: make up a tune on top.', '빙글빙글: 위에 선율을 지어요.') : t('Start the accompaniment, then play.', '반주를 틀고 연주해요.'), loop ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Four bars', '▶ 네 마디')}</button>
        <button className="ghost-btn" style={spBtn} onClick={toggle}>{loop ? t('■ Stop the loop', '■ 반복 멈추기') : t('↻ Loop it', '↻ 반복하기')}</button>
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const a7PicWalk = () => lsRawPic(['I', 'IV', 'V', 'I'].map((x, i) => '<text x="' + (10 + i * 19) + '" y="28" text-anchor="middle" font-family="Georgia, serif" font-size="13" font-weight="900" fill="' + (i === 2 ? '#e4572e' : '#26296b') + '">' + x + '</text>').join(''), [0, 0, 80, 44]);
const a7PicInv = () => lsRawPic([0, 1, 2, 3].map(i => '<ellipse cx="' + (14 + i * 14) + '" cy="' + (36 - i * 9) + '" rx="5" ry="3.7" transform="rotate(-20 ' + (14 + i * 14) + ' ' + (36 - i * 9) + ')" fill="' + (i === 3 ? '#e4572e' : '#26296b') + '"/>').join('') + '<path d="M60 8 L72 8" stroke="#e4572e" stroke-width="2"/>', [0, 0, 80, 44]);

function a7LbPages(scr = false) {
  const ch = 'arps-7', s7n = bkChapterNo('scales-7');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks = [[a7PicWalk(), t('I play I–IV–V–I in G, F and E from three positions', 'G, F, E장조에서 세 자리로 I–IV–V–I을 쳐요')], [a6PicArp(), t('I play D and A♭ arpeggios, major and minor, from every note', 'D와 A♭의 장·단 아르페지오를 모든 음에서 쳐요')],
    [a7PicInv(), t('I play the dominant 7th of D and of A♭ in all four positions', 'D와 A♭의 딸림7화음을 네 자리 모두 쳐요')], [a6PicDim(), t('I find and play the diminished 7th of D and of A♭', 'D와 A♭의 감7화음을 찾아서 쳐요')]];
  const toc = [[t('I–IV–V–I from three positions', '세 자리에서 I–IV–V–I'), 2], [t('Arpeggios from every note', '모든 음에서 아르페지오'), 3], [t('The dominant 7th from every note', '모든 음에서 딸림7화음'), 4], [t('The diminished 7th of a key', '어느 조의 감7화음'), 5], [t('My four checks', '나의 네 가지 확인'), 6]];
  const walkStill = (k) => <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:10,width:'100%',maxWidth:720,margin:'0 auto'}}>{[1, 2, 3].map(p => <div key={p}><div style={{textAlign:'center',fontSize:12.5,fontWeight:900,color:BK.ink}}>{t('Position ' + p, '자리 ' + p)}: {CW_GR[7].prog.map(rn => cwChord(k, p, rn).map(i => cwName(k, i)).join(' ')).join(' · ')}</div>
    <SpKb lo={-12} hi={19} W={scr ? 9 : 14} H={scr ? 44 : 78} lit={Object.fromEntries(cwChord(k, p, 'I').map(x => [x, 'cor']).concat(cwChord(k, p, 'IV').filter(x => !cwChord(k, p, 'I').includes(x)).map(x => [x, 'pale'])))} names={{}} k={1}/></div>)}</div>;
  const invStill = <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:scr ? 10 : 22,width:'100%',maxWidth:scr ? 760 : 640,margin:'0 auto'}}>{[0, 1, 2, 3].map(p => { const N = s7Notes('D', 'dom'), nm = s7Names('D', 'dom'), K = [0, 1, 2, 3, 4].map(j => N[(p + j) % 4] + 12 * Math.floor((p + j) / 4));
    return <div key={p}><div style={{textAlign:'center',fontSize:12.5,fontWeight:900,color:BK.ink}}>{t(D7_POS[p][0], D7_POS[p][1])}: {[0, 1, 2, 3].map(j => nm[(p + j) % 4]).join(' ')}</div><SpKb lo={-10} hi={22} W={scr ? 6 : 14} H={scr ? 40 : 72} lit={Object.fromEntries(K.map((x, j) => [x, j === 0 ? 'cor' : 'pale']))} names={{}} k={1}/></div>; })}</div>;
  const dimStill = <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{['D', 'Ab'].map(k => { const N = s7Notes(k, 'dim'), nm = s7Names(k, 'dim');
    return <div key={k}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{t('Diminished 7th of ' + S7_KEYS[k], S7_KEYS[k] + '의 감7')}: {nm.join(' ')}</div><SpKb lo={-12} hi={19} W={scr ? 9 : 16} H={scr ? 48 : 86} lit={Object.fromEntries(N.map(x => [x, 'cor']))} names={Object.fromEntries(N.map((x, j) => [x, nm[j]]))} k={1}/></div>; })}</div>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('The rest of the Grade 7 technical work (chapter ' + s7n + ' has the scales). From the technical work book, Grade 7: I–IV–V–I chord progressions in G, F and E major, from memory, mf, clear even legato, ♩ = ca 72 (alternative fingerings are acceptable); arpeggios root position and inversions, D and A♭ major and minor, four octaves, hands separately and together, (i) all p (ii) all f, clear even legato, ♩ = 72 four notes a beat; dominant 7th arpeggios of D and of A♭, root position and inversions, the same qualities; diminished 7th arpeggios of D and of A♭, the same qualities. The book prints two octaves: in most cases start an octave lower than written.', '7급 테크닉의 나머지(' + s7n + '장은 스케일). 테크닉 책의 7급: G, F, E장조 I–IV–V–I 진행, 외워서, mf, 고르고 또렷한 레가토, ♩ = 약 72(다른 운지도 괜찮아요); D와 A♭ 장·단 아르페지오, 기본형과 자리바꿈, 네 옥타브, 한 손씩 그리고 양손, (i) 모두 p (ii) 모두 f, 고르고 또렷한 레가토, ♩ = 72 한 박에 네 음; D와 A♭의 딸림7 아르페지오, 기본형과 자리바꿈, 같은 조건; D와 A♭의 감7 아르페지오, 같은 조건. 책은 두 옥타브만 인쇄해요: 대개 한 옥타브 아래에서 시작해요.'))}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={140}><div style={{width:'100%'}}>{invStill}</div></LbPic>
      <LbSay size={18}>{t('Grade 7 chords and arpeggios: a four-chord walk, D and A♭ arpeggios from every note, the dominant 7th in all four positions, and the diminished 7th.', '7급 화음과 아르페지오: 네 화음 진행, D와 A♭ 아르페지오를 모든 음에서, 네 자리의 딸림7, 그리고 감7.')}</LbSay>
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
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('I–IV–V–I from three positions', '세 자리에서 I–IV–V–I')}
      teacher={<>{spTx(t('I–IV–V–I chord progressions in G, F and E major, from memory, mf, clear even legato, ♩ = ca 72; alternative fingerings are acceptable. The right hand plays the chords from three positions (the key note, the 3rd or the 5th on top); the left hand the roots. From I to IV the key note stays; from IV to V no note stays; from V to I the 5th stays.', 'G, F, E장조 I–IV–V–I 진행, 외워서, mf, 고르고 또렷한 레가토, ♩ = 약 72; 다른 운지도 괜찮아요. 오른손은 세 자리(맨 위가 으뜸음, 3음, 5음)의 화음, 왼손은 근음. I에서 IV로는 으뜸음이 그대로; IV에서 V로는 그대로인 음이 없어요; V에서 I로는 5음이 그대로.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={140}>{walkStill('G')}</LbPic>} live={<ChordWalkPad g={7}/>}/>
      <LbSay>{LANG === 'ko' ? <>I–V–I에 <b>IV</b>가 더해졌어요. I에서 IV는 으뜸음을 붙잡고, IV에서 V는 <b>붙잡을 음이 없어</b> 모두 가까운 음으로, V에서 I은 5음을 붙잡아요.</> : <>I–V–I gains <b>IV</b>. I to IV keeps the key note; IV to V has <b>no note to keep</b>, so every note moves to the nearest; V to I keeps the 5th.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>G장조, 자리 1: 오른손 화음 넷을 천천히.</>, <>왼손 베이스를 더해서. 자리 2, 자리 3도.</>, <>F장조와 E장조. {spMM(72)} 정도로, 외워서.</>]
        : [<>G major, position 1: the right hand's four chords, slowly.</>, <>Add the left hand's bass. Then positions 2 and 3.</>, <>F major and E major. About {spMM(72)}, from memory.</>]}/>
      <LbRemember>{t('IV to V: nothing stays, so move the least.', 'IV에서 V: 붙잡을 음이 없으니 가장 적게 움직여요.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Arpeggios from every note', '모든 음에서 아르페지오')}
      teacher={<>{spTx(t('D and A♭ major and minor, root position and inversions, four octaves, hands separately and together, (i) all p (ii) all f, clear even legato, ♩ = 72. The book\'s fingerings (pp55-57), two octaves up: D major RH root 1 2 3 1 2 3 5, first inversion 2 1 2 4 1 2 4, second 1 2 4 1 2 4 5; LH root 5 3 2 1 3 2 1, first 3 2 1 3 2 1 2, second 5 3 2 1 3 2 1. D minor RH 1 2 3…, 1 2 4…, 1 2 3…; LH 5 4 2 1…, 5 4 2 1…, 5 3 2 1…. A♭ major and minor as E♭ in Grade 6: RH 2 1 2 4…, 1 2 4…, 2 4 1 2…; LH 2 1 4 2…, 5 4 2 1…, 4 2 1 4….', 'D와 A♭ 장·단, 기본형과 자리바꿈, 네 옥타브, 한 손씩 그리고 양손, (i) 모두 p (ii) 모두 f, 고르고 또렷한 레가토, ♩ = 72. 책의 운지(55-57쪽), 두 옥타브 올라가며: D장조 오른손 기본형 1 2 3 1 2 3 5, 첫째 자리바꿈 2 1 2 4 1 2 4, 둘째 1 2 4 1 2 4 5; 왼손 기본형 5 3 2 1 3 2 1, 첫째 3 2 1 3 2 1 2, 둘째 5 3 2 1 3 2 1. D단조 오른손 1 2 3…, 1 2 4…, 1 2 3…; 왼손 5 4 2 1…, 5 4 2 1…, 5 3 2 1…. A♭ 장·단은 6급의 E♭처럼: 오른손 2 1 2 4…, 1 2 4…, 2 4 1 2…; 왼손 2 1 4 2…, 5 4 2 1…, 4 2 1 4….'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={150}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{[['D', 1], ['Ab', 0]].map(([k, p]) => { const K = apKeys(k, p), F = AP_DATA[k].R[p];
        return <div key={k}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{t(AP_DATA[k].en + ', ' + AP_POS[p][0].toLowerCase(), AP_DATA[k].ko + ', ' + AP_POS[p][1])}</div><SpKb lo={K[0] - 1} hi={K[6] + 1} W={scr ? 14 : 18} H={scr ? 56 : 70} lit={Object.fromEntries(K.map((x, j) => [x, F[j] === 1 ? 'cor' : 'pale']))} names={Object.fromEntries(K.map((x, j) => [x, apNames(k, p)[j]]))} up={Object.fromEntries(K.map((x, j) => [x, F[j]]))}/></div>; })}</div></LbPic>} live={<A7ArpPad/>}/>
      <LbSay>{LANG === 'ko' ? <>A♭은 6급의 E♭처럼, <b>하나뿐인 흰건반 C</b>에 엄지. D는 흰건반이 여럿: D장조 첫째 자리바꿈은 오른손 엄지가 <b>A</b>, 왼손 엄지가 <b>D</b>.</> : <>A♭ works like Grade 6's E♭: the thumb on <b>the one white key, C</b>. D has more than one white key: in D major's first inversion the right thumb takes <b>A</b>, the left thumb <b>D</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>D장조 세 자리, 오른손만, 모두 p.</>, <>왼손, 그다음 양손. 모두 f로도.</>, <>D단조, A♭장조, A♭단조. 네 옥타브, {spMM(72)}까지.</>]
        : [<>D major in all three positions, right hand alone, all p.</>, <>Left hand, then hands together. Then all f.</>, <>D minor, A♭ major, A♭ minor. Four octaves, up to {spMM(72)}.</>]}/>
      <LbRemember>{t('A♭: the thumb on C. D: check the book.', 'A♭: 엄지는 C. D: 책을 확인해요.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The dominant 7th from every note', '모든 음에서 딸림7화음')}
      teacher={<>{spTx(t('Dominant 7th arpeggios of D (A C♯ E G) and of A♭ (E♭ G B♭ D♭), root position and inversions, four octaves, hands separately and together, (i) all p (ii) all f, clear even legato, ♩ = 72. Grade 6 had root position only; Grade 7 adds the first (from the 3rd), second (from the 5th) and third (from the 7th) inversions. Fingerings: the book\'s, pp58-59.', 'D(A C♯ E G)와 A♭(E♭ G B♭ D♭)의 딸림7 아르페지오, 기본형과 자리바꿈, 네 옥타브, 한 손씩 그리고 양손, (i) 모두 p (ii) 모두 f, 고르고 또렷한 레가토, ♩ = 72. 6급은 기본형만; 7급은 첫째(3음에서), 둘째(5음에서), 셋째(7음에서) 자리바꿈을 더해요. 운지: 책 58-59쪽.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={140}>{invStill}</LbPic>} live={<Dom7InvPad/>}/>
      <LbSay>{LANG === 'ko' ? <>네 음 화음이라 자리도 넷. 다음 음에서 시작할 때마다 하나씩: 기본형, 첫째, 둘째, 그리고 <b>7음에서 시작하는 셋째 자리바꿈</b>.</> : <>A four-note chord, so four positions. Start on the next note each time: root, first, second, and <b>the third inversion, starting on the 7th</b>.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>D의 딸림7: A C♯ E G. 기본형 두 옥타브, 오른손.</>, <>C♯에서(첫째), E에서(둘째), G에서(셋째).</>, <>A♭의 딸림7(E♭ G B♭ D♭)도. 네 옥타브, {spMM(72)}까지.</>]
        : [<>The dominant 7th of D: A C♯ E G. Root position, two octaves, right hand.</>, <>From C♯ (first), from E (second), from G (third).</>, <>Then the dominant 7th of A♭ (E♭ G B♭ D♭). Four octaves, up to {spMM(72)}.</>]}/>
      <LbRemember>{t('Four notes, four starting places.', '네 음, 네 시작점.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The diminished 7th of a key', '어느 조의 감7화음')}
      teacher={<>{spTx(t('Diminished 7th arpeggios of D (C♯ E G B♭) and of A♭ (G B♭ D♭ F♭), four octaves, hands separately and together, (i) all p (ii) all f, clear even legato, ♩ = 72. Each starts on the key\'s leading note; every gap is three semitones. Fingerings: the book\'s.', 'D(C♯ E G B♭)와 A♭(G B♭ D♭ F♭)의 감7 아르페지오, 네 옥타브, 한 손씩 그리고 양손, (i) 모두 p (ii) 모두 f, 고르고 또렷한 레가토, ♩ = 72. 저마다 그 조의 이끔음에서 시작하고, 사이는 모두 반음 셋. 운지: 책.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={140}>{dimStill}</LbPic>} live={<A7DimPad/>}/>
      <LbSay>{LANG === 'ko' ? <>이끔음에서 시작해 <b>반음 셋씩</b> 네 번. A♭의 감7에는 <b>F♭</b>: 건반은 E와 같지만, 화음 안에서는 F♭이라고 써요.</> : <>Start on the leading note and climb <b>three semitones</b> at a time. The diminished 7th of A♭ has <b>F♭</b>: the same key as E, but written F♭ in this chord.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>D의 감7: C♯ E G B♭. 오른손 두 옥타브.</>, <>A♭의 감7: G B♭ D♭ F♭. 왼손.</>, <>양손 네 옥타브, 모두 p와 모두 f. {spMM(72)}까지.</>]
        : [<>The diminished 7th of D: C♯ E G B♭. Right hand, two octaves.</>, <>The diminished 7th of A♭: G B♭ D♭ F♭. Left hand.</>, <>Hands together, four octaves, all p and all f. Up to {spMM(72)}.</>]}/>
      <LbRemember>{t('From the leading note, three semitones each.', '이끔음에서, 반음 셋씩.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My four checks', '나의 네 가지 확인')}
      teacher={<>{t('Each one played to you from memory at the book\'s speeds. Listen for chords that move the least, a thumb that passes without a bump, all four positions of the dominant 7th, and even dynamics, all p and all f.', '하나씩 외워서 책의 빠르기로 들려줘요. 가장 적게 움직이는 화음, 덜컹거림 없이 넘어가는 엄지, 딸림7의 네 자리 모두, 그리고 고른 셈여림(모두 p, 모두 f)을 들어 주세요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks} storeKey="pb_a7_four"/>}/>
    </LbPage>,
  ];
}
function Arps7LessonBook() { return <>{a7LbPages(false)}</>; }
function A7Learn({ onStart }) {
  const pages = a7LbPages(true), opener = pages[0];
  return (
    <Lesson id="arps-7" title={bkChapterName('arps-7')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="arps-7"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
const A7_LEVELS = [
  { n: 1, label: 'I, IV or V: which chord is this?', kind: 'walk', time: 15 },
  { n: 2, label: 'D and A♭ arpeggios: which note does the thumb play?', kind: 'thumb', time: 15 },
  { n: 3, label: 'The dominant 7th: where does this position start?', kind: 'inv', time: 15 },
  { n: 4, label: 'The diminished 7th of D or A♭: its notes', kind: 'dim', time: 20 },
];
Object.assign(LEVEL_KO, { 'I, IV or V: which chord is this?': 'I, IV, V: 어떤 화음일까?', 'D and A♭ arpeggios: which note does the thumb play?': 'D와 A♭ 아르페지오: 엄지가 치는 음은?', 'The dominant 7th: where does this position start?': '딸림7: 이 자리는 어디서 시작할까?', 'The diminished 7th of D or A♭: its notes': 'D나 A♭의 감7: 그 음들' });
function genA7Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'walk') { let k, pos, rn, g = 0; do { k = pick(CW_GR[7].keys); pos = pick([1, 2, 3]); rn = pick(['I', 'IV', 'V']); } while (prev && prev.key === k + pos + rn && g++ < 10); return { kind, k, pos, rn, answer: rn, choices: ['I', 'IV', 'V'], key: k + pos + rn, uid }; }
  if (kind === 'thumb') { let k, pos, h, g = 0; do { k = pick(A7_KEYS); pos = pick([0, 1, 2]); h = Math.random() < 0.5 ? 'R' : 'L'; } while (prev && prev.key === k + pos + h && g++ < 10); const F = AP_DATA[k][h][pos], j = F.indexOf(1);
    return { kind, k, pos, h, answer: apNames(k, pos)[j], choices: AP_DATA[k].nm.slice(), key: k + pos + h, uid }; }
  if (kind === 'inv') { let k, inv, g = 0; do { k = pick(['D', 'Ab']); inv = pick([0, 1, 2, 3]); } while (prev && prev.key === k + inv && g++ < 10); return { kind, k, inv, answer: s7Names(k, 'dom')[inv], choices: s7Names(k, 'dom'), key: k + inv, uid }; }
  let k, g = 0; do { k = pick(['D', 'Ab']); } while (prev && prev.key === 'dim' + k && g++ < 10); const right = s7Names(k, 'dim').join(' ');
  return { kind: 'dim', k, answer: right, choices: shuffle([right].concat(s7Wrong(k, 'dim'))), key: 'dim' + k, uid };
}
function A7Question(props) {
  const { q, given, locked, onAnswer, pixel } = props;
  if (q.kind === 'dim') return <A6Question {...props}/>;
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  const grid = (cols, items) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  let title, body, why = null;
  if (q.kind === 'walk') { const C = cwChord(q.k, q.pos, q.rn); title = t(CW_KEY[q.k][1] + ' major: which chord is this?', CW_KEY[q.k][1] + '장조: 어떤 화음일까요?');
    body = <><SpKb lo={-12} hi={19} W={12} H={60} lit={Object.fromEntries(C.map(x => [x, done ? 'good' : 'cor']))} names={Object.fromEntries(C.map(x => [x, cwName(q.k, x)]))}/>{grid(3, q.choices.map(c => [c, c]))}</>;
    why = t('Its notes: ' + C.map(x => cwName(q.k, x)).join(' ') + ', built on degree ' + ({ I: 1, IV: 4, V: 5 })[q.rn] + '.', '이 음들: ' + C.map(x => cwName(q.k, x)).join(' ') + ', ' + ({ I: 1, IV: 4, V: 5 })[q.rn] + '번 음 위의 화음.'); }
  else if (q.kind === 'thumb') { const K = apKeys(q.k, q.pos), nm = apNames(q.k, q.pos), F = AP_DATA[q.k][q.h][q.pos];
    title = t(AP_DATA[q.k].en + ', ' + AP_POS[q.pos][0].toLowerCase() + ', ' + spHand(q.h).toLowerCase() + ': which note does the thumb play?', AP_DATA[q.k].ko + ', ' + AP_POS[q.pos][1] + ', ' + spHand(q.h) + ': 엄지가 치는 음은?');
    body = <><SpKb lo={K[0] - 1} hi={K[6] + 1} W={15} H={62} lit={Object.fromEntries(K.map((x, j) => [x, done && F[j] === 1 ? 'good' : 'pale']))} names={Object.fromEntries(K.map((x, j) => [x, nm[j]]))} up={done && q.h === 'R' ? Object.fromEntries(K.map((x, j) => [x, F[j]])) : {}} dn={done && q.h === 'L' ? Object.fromEntries(K.map((x, j) => [x, F[j]])) : {}}/>{grid(3, q.choices.map(c => [c, c]))}</>;
    why = t('The book: ' + F.join(' ') + '.', '책: ' + F.join(' ') + '.'); }
  else { title = t('The dominant 7th of ' + S7_KEYS[q.k] + ', ' + D7_POS[q.inv][0].toLowerCase() + ': which note does it start on?', S7_KEYS[q.k] + '의 딸림7, ' + D7_POS[q.inv][1] + ': 어느 음에서 시작할까요?'); body = grid(4, q.choices.map(c => [c, c]));
    why = t('The chord: ' + s7Names(q.k, 'dom').join(' ') + '. Each inversion starts one note further up.', '화음: ' + s7Names(q.k, 'dom').join(' ') + '. 자리바꿈마다 한 음 위에서 시작해요.'); }
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {body}
    {done && !pixel && why && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(ARPS_7_DRILL, { levels: A7_LEVELS, generate: genA7Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: (q) => String(q.answer), Question: A7Question, Learn: A7Learn });
const A7_WB = {
  walk: [['G', 1, 'IV'], ['F', 2, 'V'], ['E', 3, 'IV'], ['G', 2, 'V']],
  thumb: [['Ab', 0, 'R'], ['D', 1, 'R'], ['D', 1, 'L'], ['Abm', 2, 'R']],
  inv: [['D', 1], ['D', 3], ['Ab', 2], ['Ab', 3]],
  chk: { walk: [['F', 1, 'I'], ['E', 2, 'V'], ['G', 3, 'IV'], ['E', 1, 'IV']], thumb: [['Ab', 1, 'R'], ['Dm', 0, 'L'], ['D', 2, 'R'], ['Abm', 0, 'L']], inv: [['D', 2], ['Ab', 1], ['D', 0], ['Ab', 3]], dim: ['D', 'Ab'] },
};
function A7Teacher() {
  const pages = [], W = A7_WB;
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="arps-7" teacher>{content}</WbPage>);
  const thumbOf = ([k, p, h]) => { const F = AP_DATA[k][h][p]; return AP_DATA[k].en + ' ' + AP_POS[p][0].toLowerCase() + ' ' + h + 'H: ' + apNames(k, p)[F.indexOf(1)] + ' (' + F.join(' ') + ')'; };
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('arps-7')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>{spTx('The keys, speeds and fingerings are the technical work book\'s (Grade 7 pp54-59). Arpeggios four octaves (the book prints two), from memory. Another fingering is fine if it is logical and systematic.')}</div>
    <TcBlock page={2} title="I–IV–V–I from three positions" answers={<>{tcAns('TRY IT', W.walk.map(([k, p, rn]) => CW_KEY[k][1] + ' major, position ' + p + ': ' + rn + ' = ' + cwChord(k, p, rn).map(x => cwName(k, x)).join(' ')))}{tcAns(spTx('G, F AND E MAJOR, mf, ♩ = ca 72'), ['I to IV: the key note stays', 'IV to V: nothing stays', 'V to I: the 5th stays'], null)}</>}
      watch="A big jump from IV to V. Every note goes to the nearest note of V."
      say="“IV to V: nothing stays, so move the least.”"/>
    <TcBlock page={3} title="Arpeggios from every note" answers={<>{tcAns('TRY IT', W.thumb.map(thumbOf))}</>}
      watch="In D, the thumb reaching for D in the first inversion (the book puts the RH thumb on A). In A♭ minor, C♭ is the white key B."
      say="“A♭: the thumb on C. D: check the book.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="The dominant 7th from every note" answers={<>{tcAns('TRY IT', W.inv.map(([k, i]) => 'of ' + S7_KEYS[k] + ', ' + D7_POS[i][0].toLowerCase() + ': from ' + s7Names(k, 'dom')[i]))}{tcAns('THE CHORDS', ['of D: ' + s7Names('D', 'dom').join(' '), 'of A♭: ' + s7Names('Ab', 'dom').join(' ')], null)}</>}
      watch="The third inversion started on the root. It starts on the 7th: G in D's, D♭ in A♭'s."
      say="“Four notes, four starting places.”"/>
    <TcBlock page={5} title="The diminished 7th of a key" answers={<>{tcAns('THE CHORDS', ['of D: ' + s7Names('D', 'dim').join(' '), 'of A♭: ' + s7Names('Ab', 'dim').join(' ')], null)}</>}
      watch="F♭ written E. In the chord it is F♭: G B♭ D♭ F♭, each a minor 3rd apart."
      say="“From the leading note, three semitones each.”"/>
    <TcBlock page={6} title="The check-up on paper (the Workbook's last page)" answers={<>{tcAns('A', W.chk.walk.map(([, , rn]) => rn))}{tcAns('B', W.chk.thumb.map(([k, p, h]) => apNames(k, p)[AP_DATA[k][h][p].indexOf(1)]), 5)}{tcAns('C', W.chk.inv.map(([k, i]) => s7Names(k, 'dom')[i]), 9)}{tcAns('D', W.chk.dim.map(k => s7Names(k, 'dim').join(' ')), 13)}
      <div style={{fontSize:12,color:BK.ink,marginTop:6,lineHeight:1.5}}>One mark for each answer. Score each part on its own (A, B, C: 4 marks each, pass 3+; D: 2 marks, pass 2). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.5.</div></>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['arps-7'] = A7Teacher;
function A7Workbook({ startNo = 1 }) {
  const W = A7_WB, pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={startNo + 1 + pages.length} chId="arps-7">{content}</WbPage>);
  P(<>
    <WbTop step={1}/>
    <Part kind="together" title="Name the chord" how="Each picture is one chord of I–IV–V–I in the key shown. Write I, IV or V.">
      <BkGrid cols={2} gap="6px 10px">{W.walk.map(([k, p, rn], i) => { const C = cwChord(k, p, rn); return <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 4px'}}>{s4wLabel(CW_KEY[k][1] + ' major')}
        <SpKb lo={-12} hi={19} W={11} H={46} lit={Object.fromEntries(C.map(x => [x, 'cor']))} names={Object.fromEntries(C.map(x => [x, cwName(k, x)]))} k={1}/>
        <div style={{display:'flex',justifyContent:'center'}}>{nvBox(i === 0, rn, 50, 26)}</div></div></ExCell>; })}</BkGrid>
    </Part>
    <Part kind="home" title="Chord walks this week" how="Tick a box each day.">
      <PhLog rows={spTxRows(['G major, position 1: I IV V I, the right hand alone', 'Add the bass; then positions 2 and 3', 'F and E major, from memory, about ♩ = 72'])} label={300}/>
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
      <PhLog rows={spTxRows(['D major, three positions, each hand, all p then all f', 'D minor and A♭ major and minor', 'Hands together, four octaves, up to ♩ = 72'])} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<>
    <WbTop step={3}/>
    <Part kind="together" title="Where does it start?" how="The dominant 7th in four positions: root, first, second, third inversion. Write the note each one starts on.">
      <BkGrid cols={2} gap="6px 10px">{W.inv.map(([k, inv], i) => <ExCell key={i} n={i + 1} ex={i === 0}><div style={{display:'grid',gap:4,padding:'16px 4px 6px',justifyItems:'center',fontSize:12,fontWeight:800,color:BK.ink,textAlign:'center'}}>{'Dominant 7th of ' + S7_KEYS[k] + ' (' + s7Names(k, 'dom').join(' ') + ')'}<span>{D7_POS[inv][0]}: {nvBox(i === 0, s7Names(k, 'dom')[inv], 44, 26)}</span></div></ExCell>)}</BkGrid>
    </Part>
    <Part kind="home" title="Sevenths this week" how="Tick a box each day.">
      <PhLog rows={['The dominant 7th of D, all four positions, right hand', 'The dominant 7th of A♭ the same; then the left hand', 'The diminished 7ths of D and A♭, hands together']} label={300}/>
    </Part>
    <Faces/>
  </>);
  P(<A7PaperCheck/>);
  return <>{pages}</>;
}
const spTxRows = (rows) => rows.map(r => spTx(r));
function A7PaperCheck() {
  const C = A7_WB.chk;
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
WORKBOOKS['arps-7'] = A7Workbook;
'''
rep("""WORKBOOKS['arps-6'] = A6Workbook;""", """WORKBOOKS['arps-6'] = A6Workbook;""" + CH)

HOME = r'''
// ══ Build BV: Arpeggios and Progressions, Grade 7 on the Home (Technique, Playing scales and chords) ══
LBH_FN['arps-7'] = (s) => a7LbPages(s);
const a7HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'k-play', 'tech', en, ko, benEn, bko, lbhSpec('arps-7', i, { make }));
const a7InvQ = (n, prev) => { const q = genA7Question(A7_LEVELS[2], prev);
  return { kind: 'choice', cols: 4, key: q.key, prompt: ['The dominant 7th of ' + S7_KEYS[q.k] + ', ' + D7_POS[q.inv][0].toLowerCase() + ': which note does it start on?', S7_KEYS[q.k] + '의 딸림7, ' + D7_POS[q.inv][1] + ': 어느 음에서 시작할까요?'], opts: q.choices.map(x => ({ id: x, label: () => x })), ans: q.answer, ok: (v) => v === q.answer,
    play: () => s7Play(q.k, 'dom', q.inv, 72, false), fig: () => ({ mid: null }), yes: ['Yes: from ' + q.answer + '.', '맞아요: ' + q.answer + '에서.'], no: ['It starts on ' + q.answer + ': ' + s7Names(q.k, 'dom').join(' ') + ', one note further up each time.', q.answer + '에서 시작해요: ' + s7Names(q.k, 'dom').join(' ') + ', 자리마다 한 음 위로.'] }; };
const a7DimQ = (n, prev) => { const k = n % 2 ? 'Ab' : 'D', right = s7Names(k, 'dim').join(' '), opts = shuffle([right].concat(s7Wrong(k, 'dim')));
  return { kind: 'choice', cols: 1, key: k + n, prompt: ['The diminished 7th of ' + S7_KEYS[k] + ': which notes?', S7_KEYS[k] + '의 감7화음: 어떤 음들?'], opts: opts.map(x => ({ id: x, label: () => x })), ans: right, ok: (v) => v === right,
    play: () => s7Play(k, 'dim'), fig: (c) => ({ mid: c.res ? <SpKb lo={-12} hi={19} W={12} H={60} lit={Object.fromEntries(s7Notes(k, 'dim').map(x => [x, 'cor']))} names={Object.fromEntries(s7Notes(k, 'dim').map((x, j) => [x, s7Names(k, 'dim')[j]]))}/> : null }),
    yes: ['Yes: ' + right + '.', '맞아요: ' + right + '.'], no: ['It was ' + right + ': from the leading note, three semitones each.', '정답은 ' + right + ': 이끔음에서 반음 셋씩.'] }; };
a7HomeAdd('a7-walk', 1, 'I–IV–V–I from three positions', '세 자리에서 I–IV–V–I', 'From IV to V nothing stays: move the least.', 'IV에서 V는 그대로인 음이 없어요: 가장 적게.', lwTapQ(ChordWalkPad, (n) => ({ g: 7, fixed: { k: CW_GR[7].keys[n % 3], pos: 1 + (n % 3) } }), ['Tap the three notes of the next chord.', '다음 화음의 세 음을 눌러요.'], ['Walked ✓', '진행했어요 ✓']));
a7HomeAdd('a7-arp', 2, 'D and A♭ arpeggios from every note', 'D와 A♭ 아르페지오, 모든 음에서', 'Where does the thumb go?', '엄지는 어디에?', lwTapQ(A7ArpPad, (n) => ({ fixed: { k: A7_KEYS[n % 4], pos: n % 3, h: n % 2 ? 'L' : 'R' } }), ['Tap every key the thumb plays.', '엄지가 치는 건반을 모두 눌러요.'], ['Found them ✓', '찾았어요 ✓']));
a7HomeAdd('a7-inv', 3, 'The dominant 7th from every note', '모든 음에서 딸림7화음', 'Root, first, second, third: one note further up each time.', '기본형, 첫째, 둘째, 셋째: 자리마다 한 음 위.', a7InvQ);
a7HomeAdd('a7-dim', 4, 'The diminished 7th of D and A♭', 'D와 A♭의 감7화음', 'From the leading note, three semitones each.', '이끔음에서 반음 셋씩.', a7DimQ);
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""check: 'scales-7' },   // Build BU""", """check: 'scales-7' },   // Build BU
    { id: 'kpl-a7', en: 'Arpeggios and progressions, Grade 7', ko: '아르페지오와 화음 진행, Grade 7', lessons: ['a7-walk', 'a7-arp', 'a7-inv', 'a7-dim', 'mk-accomp'], check: 'arps-7' },   // Build BV""")
rep("""  set('7', 's7-grand s7-poly s7-mirror s7-chrom s7-345 s7-voices s7-lyd mk-mode');   // Build BU: Scales, Grade 7""", """  set('7', 's7-grand s7-poly s7-mirror s7-chrom s7-345 s7-voices s7-lyd mk-mode');   // Build BU: Scales, Grade 7
  set('7', 'a7-walk a7-arp a7-inv a7-dim mk-accomp');   // Build BV: Arpeggios and Progressions, Grade 7""")
rep("""  { id: 'mk-cad', ch: 'listen-6',""", """  { id: 'mk-accomp', ch: 'arps-7', title: 'My accompaniment', blurb: 'Alberti bass, waltz or broken chords under I–IV–V–I; play your own tune on top.', C: () => <AccompMaker/> },   // Build BV
  { id: 'mk-cad', ch: 'listen-6',""")
rep("""  'mk-cad': ['나만의 끝 만들기',""", """  'mk-accomp': ['나의 반주', '알베르티 베이스, 왈츠, 분산 화음으로 I–IV–V–I 반주; 위에 내 선율을 얹어요.'],
  'mk-cad': ['나만의 끝 만들기',""")
rep("""'mk-cad': ['chords', 3, 3, 'game ear'],""", """'mk-cad': ['chords', 3, 3, 'game ear'], 'mk-accomp': ['chords', 3, 3, 'game ear'],""")
rep("""'mk-cad': 'p-chords',""", """'mk-cad': 'p-chords', 'mk-accomp': 'p-chords',""")
rep("""  'mk-cad': () => (\n""", """  'mk-accomp': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><path d="M3 17 L7 12 L11 15 L15 12 L19 15" fill="none" stroke="#fefbf3" strokeWidth="1.8"/><path d="M3 8 Q8 4 12 7 T21 6" fill="none" stroke="#e9a83a" strokeWidth="1.8"/></svg>
  ),
  'mk-cad': () => (\n""")
rep("""const LESSON_BOOKS = { 'scales-7': Scales7LessonBook,""", """const LESSON_BOOKS = { 'arps-7': Arps7LessonBook, 'scales-7': Scales7LessonBook,""")
rep("""const LB_PAGE_FNS = { 'scales-7': s7LbPages,""", """const LB_PAGE_FNS = { 'arps-7': a7LbPages, 'scales-7': s7LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"arps-7": "<ellipse cx=\\"10\\" cy=\\"38\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 10 38)\\" fill=\\"#26296b\\"/><ellipse cx=\\"19\\" cy=\\"30\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 19 30)\\" fill=\\"#26296b\\"/><ellipse cx=\\"28\\" cy=\\"22\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 28 22)\\" fill=\\"#26296b\\"/><ellipse cx=\\"37\\" cy=\\"14\\" rx=\\"4.4\\" ry=\\"3.3\\" transform=\\"rotate(-20 37 14)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><text x=\\"38\\" y=\\"40\\" font-size=\\"11\\" font-weight=\\"900\\" fill=\\"#26296b\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">7</text>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
