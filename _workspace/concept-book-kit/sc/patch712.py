import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AS (board call 18, the second Grade 4 room): Scales and Arpeggios, Grade 4. As Scales Further did (board call 14: the
# room teaches the skill each group is for; the key lists and the speeds live in the teacher's copy). Every key, speed and
# fingering below was read off the technical work book (Level 1, Grade 4 pp58-64; page images read 26 Oct): scales four octaves,
# mf, clear even legato, four notes a beat at crotchet 63, hands separately and together in similar motion (E major; C sharp
# natural, harmonic and melodic minor; A flat major; F natural, harmonic and melodic minor); staccato A flat major and F melodic
# minor at 52; contrary motion two octaves at 52 (A major, F sharp harmonic minor, E flat major, C harmonic minor); chromatic from
# E and from G sharp/A flat, four octaves, 63, hands separately and together; arpeggios E and A flat major and minor, four
# octaves, hands separately, two notes a beat at 76. The book prints two octaves to show the fingering: in the exam the scales
# and arpeggios go four, "in most cases ... commencing one octave lower than written".

rep("""const LISTEN_4_DRILL = { id: 'listen-4', label: 'Hear and Sing, Grade 4', noPrint: true };   // Build AR""",
    """const LISTEN_4_DRILL = { id: 'listen-4', label: 'Hear and Sing, Grade 4', noPrint: true };   // Build AR
const SCALES_4_DRILL = { id: 'scales-4', label: 'Scales and Arpeggios, Grade 4' };   // Build AS""")
rep("""  { id: 'listen-4', label: 'Hear and Sing, Grade 4', concept: LISTEN_4_DRILL, track: 'start' },   // Build AR""",
    """  { id: 'listen-4', label: 'Hear and Sing, Grade 4', concept: LISTEN_4_DRILL, track: 'start' },   // Build AR
  { id: 'scales-4', label: 'Scales and Arpeggios, Grade 4', concept: SCALES_4_DRILL, track: 'start' },   // Build AS""")
rep("""'listen-4': '듣고 부르기, Grade 4'""", """'listen-4': '듣고 부르기, Grade 4', 'scales-4': '스케일과 아르페지오, Grade 4'""")
rep("""'listen-4': ['listen-23', 'intervals'],""", """'listen-4': ['listen-23', 'intervals'], 'scales-4': ['scales-23'],""")
rep("""'listen-4': ['Hear, Grade 4', '듣기 4'],""", """'listen-4': ['Hear, Grade 4', '듣기 4'], 'scales-4': ['Scales, Grade 4', '스케일 4'],""")
rep("""  'listen-4': 'aural ear grade 4""", """  'scales-4': 'scales arpeggios grade 4 four octaves finger 4 four notes a beat semiquavers staccato legato contrary motion mirror twins chromatic hands together arpeggio thumb technique',
  'listen-4': 'aural ear grade 4""")
rep("""'scales-23': 'k-play', 'harmony-23'""", """'scales-23': 'k-play', 'scales-4': 'k-play', 'harmony-23'""")
rep("""    { id: 'kpl-23', en: 'Scales further', ko: '스케일 한 걸음 더', lessons: ['scf-thumb', 'scf-meet', 'scf-mel', 'scf-mirror', 'scf-chrom'], check: 'scales-23' },   // Build AK""",
    """    { id: 'kpl-23', en: 'Scales further', ko: '스케일 한 걸음 더', lessons: ['scf-thumb', 'scf-meet', 'scf-mel', 'scf-mirror', 'scf-chrom'], check: 'scales-23' },   // Build AK
    { id: 'kpl-4', en: 'Scales and arpeggios, Grade 4', ko: '스케일과 아르페지오, Grade 4', lessons: ['s4-four', 's4-touch', 's4-mirror', 's4-chrom', 's4-arp'], check: 'scales-4' },   // Build AS""")
rep("""  set('4', 'l4-iv l4-two l4-mid l4-clap');   // Build AR: Hear and Sing, Grade 4""", """  set('4', 'l4-iv l4-two l4-mid l4-clap');   // Build AR: Hear and Sing, Grade 4
  set('4', 's4-four s4-touch s4-mirror s4-chrom s4-arp');   // Build AS: Scales and Arpeggios, Grade 4""")

CH = r'''
// ─── Chapter: Scales and Arpeggios, Grade 4 (Build AS, 2026-10-26; board call 18, the second Grade 4 room) ───
// What Grade 4 adds to Scales Further: four octaves (the pattern repeats; finger 4 plays one note, the same note, in every
// octave: the landmark that tells the hand where it is while the arm carries it up the keyboard); four notes a beat, legato and
// staccato; contrary motion in four new keys; the chromatic scale hands together over four octaves (the hands' fingers differ
// only around E-F and B-C); arpeggios over four octaves (the thumb's notes). The keys, speeds and fingerings are the book's.
const s4Run = (first, pat, top) => first.concat(pat, pat, pat, [top]);   // four octaves going up: 29 fingers
const S4_MEL = [0, 2, 3, 5, 7, 9, 11];
const S4_SC = {   // r: the keynote of the one-octave keyboard (semitones from middle C); R and L: four octaves going up
  E: { en: 'E major', ko: 'E장조', st: SP_MAJ, r: 4, nm: ['E', 'F♯', 'G♯', 'A', 'B', 'C♯', 'D♯'], R: s4Run([1, 2, 3, 1, 2, 3, 4], [1, 2, 3, 1, 2, 3, 4], 5), L: s4Run([5, 4, 3, 2, 1, 3, 2], [1, 4, 3, 2, 1, 3, 2], 1) },
  Csm: { en: 'C♯ minor', ko: 'C♯단조', st: SP_NAT, r: 1, nm: ['C♯', 'D♯', 'E', 'F♯', 'G♯', 'A', 'B'], R: s4Run([2, 3, 1, 2, 3, 1, 2], [3, 4, 1, 2, 3, 1, 2], 3), L: s4Run([3, 2, 1, 4, 3, 2, 1], [3, 2, 1, 4, 3, 2, 1], 2) },
  Csmel: { en: 'C♯ melodic minor', ko: 'C♯ 가락 단음계', st: S4_MEL, r: 1, nm: ['C♯', 'D♯', 'E', 'F♯', 'G♯', 'A♯', 'B♯'], R: s4Run([2, 3, 1, 2, 3, 4, 1], [2, 3, 1, 2, 3, 4, 1], 3), L: s4Run([3, 2, 1, 4, 3, 2, 1], [3, 2, 1, 4, 3, 2, 1], 2) },
  Ab: { en: 'A♭ major', ko: 'A♭장조', st: SP_MAJ, r: -4, nm: ['A♭', 'B♭', 'C', 'D♭', 'E♭', 'F', 'G'], R: s4Run([2, 3, 1, 2, 3, 1, 2], [3, 4, 1, 2, 3, 1, 2], 3), L: s4Run([3, 2, 1, 4, 3, 2, 1], [3, 2, 1, 4, 3, 2, 1], 2) },
  Fm: { en: 'F minor', ko: 'F단조', st: SP_NAT, r: 5, nm: ['F', 'G', 'A♭', 'B♭', 'C', 'D♭', 'E♭'], R: s4Run([1, 2, 3, 4, 1, 2, 3], [1, 2, 3, 4, 1, 2, 3], 4), L: s4Run([5, 4, 3, 2, 1, 3, 2], [1, 4, 3, 2, 1, 3, 2], 1) },
};
const S4_KEYS = ['E', 'Csm', 'Csmel', 'Ab', 'Fm'];
const s4Name = (k) => t(S4_SC[k].en, S4_SC[k].ko);
const s4Chip = (k) => (k === 'Csmel' ? t('C♯m melodic', 'C♯m 가락') : k === 'Csm' ? 'C♯m' : k === 'Fm' ? 'Fm' : S4_SC[k].nm[0]);
const s4Oct = (k) => { const c = S4_SC[k]; return c.st.map(x => c.r + x).concat([c.r + 12]); };   // one octave, keynote to keynote
const s4Mid = (k, h) => S4_SC[k][h].slice(7, 15);   // a middle octave's fingers
const s4F4 = (k, h) => s4Mid(k, h).slice(0, 7).indexOf(4);   // the degree finger 4 plays
const s4F4Note = (k, h) => S4_SC[k].nm[s4F4(k, h)];
// a scale's notes over n octaves, up then down (the melodic minor comes down as the natural minor)
const s4Seq = (k, start, n = 4) => { const c = S4_SC[k], dn = k === 'Csmel' ? SP_NAT : c.st, out = [];
  for (let x = 0; x <= 7 * n; x++) out.push(start + 12 * Math.floor(x / 7) + c.st[x % 7]);
  for (let x = 7 * n - 1; x >= 0; x--) out.push(start + 12 * Math.floor(x / 7) + dn[x % 7]); return out; };

// ── step 1: four octaves: where does finger 4 go? ──
function S4Map({ k, h, mw = 520 }) {   // four octaves in miniature: finger 4's note in every octave
  const c = S4_SC[k], lo = c.r - 12, lit = {}, j4 = s4F4(k, h);
  for (let o = 0; o < 4; o++) { lit[lo + 12 * o] = 'pale'; lit[lo + 12 * o + c.st[j4]] = 'cor'; } lit[lo + 48] = 'pale';
  const m = spMiniKeys(lo, lo + 48, lit, 8, 30, 2, 4);
  return <div style={{maxWidth:mw,margin:'4px auto 0'}}><svg viewBox={'0 0 ' + m.w + ' 38'} style={{width:'100%',display:'block'}} role="img" aria-label={t('Four octaves', '네 옥타브')} dangerouslySetInnerHTML={{ __html: m.svg }}/>
    <div style={{display:'flex',justifyContent:'space-between',fontSize:11.5,fontWeight:800,color:BK.muted,margin:'2px 2px 0'}}><span>{t('octave 1', '1옥타브')}</span><span>2</span><span>3</span><span>4</span></div></div>;
}
function S4FourPad({ fixed, onResult }) {
  const T = useSpTimers();
  const [k, setK] = useState(fixed ? fixed.k : 'E'), [h, setH] = useState(fixed ? fixed.h : 'R'), [res, setRes] = useState(null), [bad, setBad] = useState(null), [miss, setMiss] = useState(0), [at, setAt] = useState(-1);
  const c = S4_SC[k], K = s4Oct(k), F = s4Mid(k, h), j4 = s4F4(k, h), done = !!res;
  const reset = (fn) => { T.clear(); setRes(null); setBad(null); setMiss(0); setAt(-1); if (fn) fn(); };
  const play = () => { T.clear(); const sq = s4Seq(k, c.r - (h === 'L' ? 24 : 12)), run = spPlay(sq.map((x, n) => ({ at: n / 4, keys: [x], len: n === sq.length - 1 ? 1.5 : 0.25, vol: 0.13 })), 63, 4); if (!run) return;
    sq.forEach((x, n) => T.at(run.ms(n / 4), () => setAt(spPc(x)))); T.at(run.ms(sq.length / 4 + 1), () => setAt(-1)); };
  const tap = (i) => { playKey(i - (h === 'L' ? 12 : 0), 0.5); if (done) return; if (i === K[j4]) { const r = { ok: miss === 0 }; setRes(r); setBad(null); if (onResult) onResult(r); } else { setBad(i); setMiss(m => m + 1); } };
  const lit = {}, nums = {}; K.forEach((x, j) => { if (F[j] === 1 || done) nums[x] = F[j]; lit[x] = done && j === j4 ? 'good' : 'pale'; }); if (bad != null && !done) lit[bad] = 'bad'; if (at >= 0) K.forEach(x => { if (spPc(x) === at) lit[x] = 'cor'; });
  const extra = done ? (k === 'Csmel' && h === 'R' ? t(' Coming down (the natural minor) it goes back to D♯.', ' 내려올 때(자연 단음계)는 다시 D♯.') : (k === 'Csm' || k === 'Ab') && h === 'R' ? t(' The very first octave starts on 2 3, so 4 joins from the second octave.', ' 맨 처음 옥타브는 2 3으로 시작해서, 4는 둘째 옥타브부터.') : '') : '';
  return (
    <div className="try-box" style={actBox} data-s4="four">
      <div style={actTitle}>{t('One 4 in every octave', '옥타브마다 4번 하나')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>네 옥타브. 팔이 손을 데려가는 동안 손가락 무늬는 옥타브마다 똑같아요. <b>4번은 옥타브마다 한 번, 언제나 같은 음</b>을 쳐요: 그 음을 알면 어느 옥타브에서든 길을 잃지 않아요. 엄지 자리는 보여 줄게요. 4번이 치는 건반을 눌러요.</>
        : <>Four octaves. The arm carries the hand up the keyboard, and the fingers keep the same pattern in every octave. <b>Finger 4 plays once an octave, always the same note</b>: know it, and you know where you are in any octave. The thumbs are shown. Tap the key finger 4 plays.</>}</div>
      {!fixed && spChips(S4_KEYS.map(x => [x, s4Chip(x)]), k, (x) => reset(() => setK(x)))}
      {!fixed && spChips([['R', spHand('R')], ['L', spHand('L')]], h, (x) => reset(() => setH(x)))}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 4px'}}>{s4Name(k)}{k === 'Csmel' ? t(', going up', ', 올라갈 때') : ''} · {spHand(h)}</div>
      <SpKb lo={c.r} hi={c.r + 12} W={30} H={84} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, c.nm[j % 7]]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}} onTap={tap} label={s4Name(k)}/>
      {done && <S4Map k={k} h={h}/>}
      {spMsg(done ? t('Finger 4 plays ' + c.nm[j4] + ' in every octave.' + extra, '4번은 옥타브마다 ' + c.nm[j4] + '.' + extra)
        : bad != null ? t(h === 'R' ? 'Not there: after the thumb comes a group of three (1 2 3) and a group of four (1 2 3 4). The group of four ends on 4.' : 'Not there: going up, the left hand crosses 4 over the thumb.', h === 'R' ? '거기가 아니에요: 엄지 다음에 셋 묶음(1 2 3)과 넷 묶음(1 2 3 4). 넷 묶음의 끝이 4번.' : '거기가 아니에요: 올라갈 때 왼손은 엄지 위로 4번이 넘어가요.')
        : t('Where does finger 4 go?', '4번은 어디에?'), done ? BK.green : bad != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Four octaves', '▶ 네 옥타브')}</button>
        {done && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}

// ── step 2: four notes a beat, legato and staccato ──
const S4_ST = {   // the two staccato scales: two octaves up and down, as the book prints them
  Ab: { en: 'A♭ major', ko: 'A♭장조', r: -4, up: SP_MAJ, dn: SP_MAJ, nmU: ['A♭', 'B♭', 'C', 'D♭', 'E♭', 'F', 'G'], nmD: ['A♭', 'B♭', 'C', 'D♭', 'E♭', 'F', 'G'] },
  Fmel: { en: 'F melodic minor', ko: 'F 가락 단음계', r: 5, up: S4_MEL, dn: SP_NAT, nmU: ['F', 'G', 'A♭', 'B♭', 'C', 'D', 'E'], nmD: ['F', 'G', 'A♭', 'B♭', 'C', 'D♭', 'E♭'] },
};
const s4Two = (k) => { const c = S4_ST[k], out = [];
  for (let x = 0; x <= 14; x++) out.push({ i: c.r + 12 * Math.floor(x / 7) + c.up[x % 7], nm: c.nmU[x % 7] });
  for (let x = 13; x >= 0; x--) out.push({ i: c.r + 12 * Math.floor(x / 7) + c.dn[x % 7], nm: c.nmD[x % 7] }); return out; };   // 29 notes: 7 beats of four and the last
const S4_BPM = 52;
// four lead-in clicks, then the scale four notes a beat with no clicks: legato (each note held to the next) or staccato (short)
const s4PlayTouch = (k, stacc, bpm = S4_BPM) => { const sq = s4Two(k);
  return plRun(4 + 8, { bpm, vol: 0.28, silentFrom: 4, extra: (ctx, tm, i, spb) => { if (i < 4) return; const b = i - 4;
    for (let q = 0; q < 4; q++) { const n = b * 4 + q; if (n >= sq.length) break; blip(ctx, tm + q * spb / 4, spHz(sq[n].i), n === sq.length - 1 ? spb * (stacc ? 0.2 : 1) : stacc ? spb * 0.07 : spb / 4 * 0.98, 0.15, 'triangle'); } } }); };
function S4Groups({ k, cur = -1, marks = null }) {
  const sq = s4Two(k), groups = []; for (let b = 0; b * 4 < sq.length; b++) groups.push(sq.slice(b * 4, b * 4 + 4).map((x, q) => [x, b * 4 + q]));
  return <div style={{display:'flex',flexWrap:'wrap',gap:5,justifyContent:'center',margin:'4px 0 8px'}}>{groups.map((g, b) => <div key={b} style={{display:'flex',gap:2,alignItems:'center',padding:'3px 4px',borderRadius:8,background:b % 2 ? '#fff' : 'rgba(38,41,107,0.07)',border:'1px solid rgba(38,41,107,0.14)',position:'relative'}}>
    {marks && <span style={{position:'absolute',top:-9,left:4,fontSize:11,fontWeight:900,color:marks[b] === '✓' ? BK.green : BK.coral,background:'#fff',borderRadius:6,padding:'0 2px',lineHeight:'14px'}}>{marks[b]}</span>}
    {g.map(([x, n], q) => <span key={n} style={{minWidth:22,height:24,padding:'0 2px',boxSizing:'border-box',display:'inline-flex',alignItems:'center',justifyContent:'center',borderRadius:12,fontSize:12,fontWeight:900,
      background:n === cur ? BK.coral : 'transparent',color:n === cur ? '#fff' : q === 0 ? BK.coral : BK.ink,textDecoration:q === 0 ? 'underline' : 'none',textUnderlineOffset:3}}>{x.nm}</span>)}</div>)}</div>;
}
function S4TouchPad({ fixed, onResult }) {
  const T = usePlTimers();
  const [k, setK] = useState(fixed ? fixed.k : 'Ab'), [stacc, setStacc] = useState(fixed ? fixed.stacc : false), [phase, setPhase] = useState('ready'), [cur, setCur] = useState(-1), [res, setRes] = useState(null);
  const run = useRef(null), taps = useRef([]);
  const reset = (fn) => { T.clear(); stopClicks(); setPhase('ready'); setCur(-1); setRes(null); if (fn) fn(); };
  const go = (mode, st) => { T.clear(); setRes(null); taps.current = []; const r = s4PlayTouch(k, st); if (!r) return; run.current = r; setPhase(mode === 'tap' ? 'count' : 'listen');
    const spb = r.spb, n = s4Two(k).length;
    for (let x = 0; x < n; x++) T.at(r, r.at[4 + Math.floor(x / 4)] + (x % 4) * spb / 4, () => setCur(x));
    if (mode === 'tap') T.at(r, r.at[4] - 0.05, () => setPhase('tap'));
    T.at(r, r.at[11] + spb + 0.15, () => { setCur(-1);
      if (mode !== 'tap') { setPhase('ready'); return; }
      const tol = Math.min(PL_TOL, spb * 0.2), exp = Array.from({ length: 8 }, (_, b) => r.at[4 + b]), mt = plMatch(exp, taps.current.filter(tp => tp > r.at[4] - tol), tol);
      const out = { hits: mt.hits, total: 8, extra: mt.extra, marks: mt.offs.map(o => (o === null ? '?' : '✓')), ok: mt.hits >= 7 && mt.extra <= 1 };
      setRes(out); setPhase('done'); if (onResult) onResult({ ok: out.ok }); }); };
  const tap = React.useCallback(() => { const r = run.current; if (r && (phase === 'count' || phase === 'tap')) { taps.current.push(r.now()); const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime, SRH_HZ, 0.08, 0.14, 'triangle'); } }, [phase]);
  const c = S4_ST[k];
  return (
    <div className="try-box" style={actBox} data-s4="touch">
      <div style={actTitle}>{t('Four notes a beat', '한 박에 네 음')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>4급 스케일은 <b>한 박에 네 음</b>: 1-e-+-a. 네 음씩 묶음, 묶음의 첫 음이 박(밑줄)이에요. 클릭 네 번 다음에는 클릭이 없어요: <b>박마다 패드를 눌러요</b>. 스타카토는 <b>같은 손가락, 같은 박</b>, 음만 짧게.</>
        : <>Grade 4 scales go <b>four notes a beat</b>: 1-e-and-a. Each group of four starts on the beat (underlined). After four clicks there are none: <b>tap the pad on every beat</b>. Staccato: <b>the same fingers, the same beat</b>, only the notes short.</>}</div>
      {!fixed && spChips([['Ab', t(S4_ST.Ab.en, S4_ST.Ab.ko)], ['Fmel', t(S4_ST.Fmel.en, S4_ST.Fmel.ko)]], k, (x) => reset(() => setK(x)))}
      {!fixed && spChips([[false, t('Legato', '레가토')], [true, t('Staccato', '스타카토')]], stacc, (x) => reset(() => setStacc(x)))}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>{t(c.en, c.ko)} · {stacc ? t('staccato', '스타카토') : t('legato', '레가토')} · {spMM(S4_BPM)}</div>
      <S4Groups k={k} cur={cur} marks={res ? res.marks : null}/>
      {spMsg(phase === 'listen' ? t('Listen: four to a beat…', '들어요: 한 박에 넷…') : phase === 'count' ? t('Four clicks, then tap every beat…', '클릭 넷, 그다음 박마다 눌러요…') : phase === 'tap' ? t('Tap on every beat!', '박마다 눌러요!')
        : res ? t('Beats on time: ' + res.hits + ' of 8.' + (res.ok ? ' Steady ✓' : ' Count 1-e-and-a inside, and tap on the 1.'), '제때 누른 박: 8개 중 ' + res.hits + '개.' + (res.ok ? ' 고르게 ✓' : ' 속으로 1-e-+-a를 세고, 1에 눌러요.')) : '', res ? (res.ok ? BK.green : BK.coral) : undefined)}
      <PlPad on={phase === 'count' || phase === 'tap'} onTap={tap} label={t('TAP THE BEAT', '박 누르기')}/>
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={() => go('listen', stacc)}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={() => go('tap', stacc)}>{res ? t('▶ Again', '▶ 다시') : t('▶ Tap the beat', '▶ 박 누르기')}</button>
      </div>
      {plHint()}
    </div>
  );
}

// ── step 3: contrary motion in the Grade 4 keys (two octaves, four notes a beat) ──
Object.assign(SCF_CM, {   // the book's fingerings, the first octave of two (Grade 4 p61)
  A4: { g: 4, en: 'A major', ko: 'A장조', st: SP_MAJ, s: -3, nm: ['A', 'B', 'C♯', 'D', 'E', 'F♯', 'G♯'], R: [1, 2, 3, 1, 2, 3, 4, 1], L: [1, 2, 3, 1, 2, 3, 4, 1] },
  Fsmh: { g: 4, en: 'F♯ harmonic minor', ko: 'F♯ 화성 단음계', st: SP_HAR, s: 6, nm: ['F♯', 'G♯', 'A', 'B', 'C♯', 'D', 'E♯'], R: [2, 3, 1, 2, 3, 1, 2, 3], L: [2, 1, 2, 3, 1, 2, 3, 4] },
  Eb4: { g: 4, en: 'E♭ major', ko: 'E♭장조', st: SP_MAJ, s: 3, nm: ['E♭', 'F', 'G', 'A♭', 'B♭', 'C', 'D'], R: [2, 1, 2, 3, 4, 1, 2, 3], L: [2, 1, 2, 3, 4, 1, 2, 3] },
  Cmh: { g: 4, en: 'C harmonic minor', ko: 'C 화성 단음계', st: SP_HAR, s: 0, nm: ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B'], R: [1, 2, 3, 1, 2, 3, 4, 1], L: [1, 2, 3, 1, 2, 3, 4, 1] },
});
const S4_CM_KEYS = ['A4', 'Fsmh', 'Eb4', 'Cmh'];
const s4CmChip = (k) => ({ A4: 'A', Fsmh: 'F♯m', Eb4: 'E♭', Cmh: 'Cm' })[k];
function S4MirrorPad({ fixed, onResult }) {
  const T = useSpTimers();
  const [k, setK] = useState(fixed || 'A4'), [ans, setAns] = useState(null);
  const yes = scfMirror(k), d = scfFirstDiff(k), c = scfCm(k), ok = ans != null && ans === yes;
  const reset = (fn) => { T.clear(); setAns(null); if (fn) fn(); };
  const play = () => { T.clear(); const ix = spUpDown(8); spPlay(ix.map((j, n) => ({ at: n / 4, keys: [c.R[j], c.L[j]], len: n === ix.length - 1 ? 1.5 : 0.25, vol: 0.12 })), 52, 4); };
  const say = (v) => { if (ans != null) return; setAns(v); if (onResult) onResult({ ok: v === yes }); };
  return (
    <div className="try-box" style={actBox} data-s4="mirror">
      <div style={actTitle}>{t('Contrary motion: mirror twins?', '반대 방향: 거울 쌍둥이?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>4급의 반대 방향: 두 옥타브, <b>한 박에 네 음</b>. 두 손이 한 음에서 시작해 멀어졌다 돌아와요. <b>손마다 자기 스케일 번호</b>. 번호가 끝까지 같으면 거울 쌍둥이예요.</>
        : <>Grade 4 contrary motion: two octaves, <b>four notes a beat</b>. Both hands start on one note, move apart and come back, <b>each with its own scale fingering</b>. If the numbers match all the way, they are mirror twins.</>}</div>
      {!fixed && scfKeyChips(S4_CM_KEYS, k, (x) => reset(() => setK(x)), s4CmChip)}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 4px'}}>{scfCmName(k)}</div>
      <ScfCmKb k={k} mark={ans != null && !yes ? d : -1}/>
      {ans == null ? <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:10}}>
        <button className="choice-btn" style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => say(true)}>{t('Mirror twins', '거울 쌍둥이')}</button>
        <button className="choice-btn" style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => say(false)}>{t('Not mirror twins', '거울 쌍둥이 아님')}</button></div>
        : spMsg((ok ? t('Yes. ', '맞아요. ') : t('Look again. ', '다시 봐요. ')) + (yes ? t('The same numbers all the way: mirror twins.', '끝까지 같은 번호: 거울 쌍둥이.') : t('Note ' + (d + 1) + ': the right hand plays ' + c.nmR[d] + ' with ' + c.fR[d] + ', the left hand ' + c.nmL[d] + ' with ' + c.fL[d] + '. Each hand keeps its own fingering.', (d + 1) + '번째 음: 오른손은 ' + c.nmR[d] + '에 ' + c.fR[d] + '번, 왼손은 ' + c.nmL[d] + '에 ' + c.fL[d] + '번. 손마다 자기 번호를 지켜요.')), ok ? BK.green : BK.coral)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hear it', '▶ 들어 보기')}</button>
        {ans != null && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}

// ── step 4: the chromatic scale hands together: where do the fingers differ? ──
const S4_CH = [['E', 4], ['G♯/A♭', 8]];
const s4ChR = (x) => chromFinger(spPc(x), 'RH', false), s4ChL = (x) => chromFinger(spPc(x), 'LH', false);
const s4ChLet = (i) => ['C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B'][spPc(i)];
function S4ChromPad({ fixed, onResult }) {
  const T = useSpTimers();
  const [st, setSt] = useState(fixed != null ? fixed : 0), [found, setFound] = useState([]), [bad, setBad] = useState(null), [miss, setMiss] = useState(0), [pl, setPl] = useState(-1);
  const s0 = S4_CH[st][1], K = Array.from({ length: 13 }, (_, j) => s0 + j), targets = [...new Set(K.filter(x => s4ChR(x) !== s4ChL(x)).map(spPc))], done = found.length === targets.length;
  const reset = (fn) => { T.clear(); setFound([]); setBad(null); setMiss(0); setPl(-1); if (fn) fn(); };
  const play = () => { T.clear(); const ix = Array.from({ length: 13 }, (_, j) => j).concat(Array.from({ length: 12 }, (_, j) => 11 - j)); const run = spPlay(ix.map((j, n) => ({ at: n / 4, keys: [K[j], K[j] - 12], len: n === ix.length - 1 ? 1.5 : 0.25, vol: 0.11 })), 63, 4); if (!run) return;
    ix.forEach((j, n) => T.at(run.ms(n / 4), () => setPl(j))); T.at(run.ms(ix.length / 4 + 1), () => setPl(-1)); };
  const tap = (i) => { playKey(i, 0.4); if (done) return; const pc = spPc(i); if (targets.includes(pc)) { if (found.includes(pc)) return; const nf = found.concat([pc]); setFound(nf); setBad(null); if (nf.length === targets.length) { if (onResult) onResult({ ok: miss === 0 }); T.at(300, play); } }
    else { setBad(i); setMiss(m => m + 1); } };
  const up = {}, dn = {}, lit = {}, act = {}; K.forEach(x => { up[x] = s4ChR(x); dn[x] = s4ChL(x); if (found.includes(spPc(x))) lit[x] = 'good'; }); if (bad != null) lit[bad] = 'bad'; if (pl >= 0) { lit[K[pl]] = 'cor'; act[K[pl]] = true; act['d' + K[pl]] = true; }
  return (
    <div className="try-box" style={actBox} data-s4="chrom">
      <div style={actTitle}>{t('Chromatic, hands together', '반음계, 양손 함께')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>4급 반음계: 네 옥타브, 양손 함께. 오른손 번호는 위, 왼손은 아래. <b>3번은 언제나 함께</b> 떨어져요. 두 손의 번호가 <b>다른 건반</b>을 모두 눌러요.</>
        : <>Grade 4 chromatic: four octaves, hands together. The right hand's fingers above, the left hand's below. <b>The 3s always land together</b>. Tap every key where the two hands use <b>different fingers</b>.</>}</div>
      {!fixed && spChips(S4_CH.map(([n], j) => [j, t('From ' + n, n + '에서')]), st, (x) => reset(() => setSt(x)))}
      <SpKb lo={s0} hi={s0 + 12} W={30} H={84} lit={lit} names={Object.fromEntries(K.filter(spIsW).map(x => [x, s4ChLet(x)]))} up={up} dn={dn} act={act} onTap={tap} label={t('Chromatic scale', '반음계')}/>
      {spMsg(done ? t('Only around E–F and B–C: the right hand puts 2 on F and C, the left hand on E and B. Everywhere else the hands match.', 'E–F와 B–C 둘레에서만: 오른손은 F와 C에 2번, 왼손은 E와 B에 2번. 나머지는 두 손이 같아요.')
        : bad != null ? t('Those numbers match: look for a 1 against a 2.', '거기는 번호가 같아요: 1과 2가 마주한 곳을 찾아요.') : t('Where do the hands differ? ' + found.length + ' of ' + targets.length, '두 손이 다른 곳은? ' + targets.length + '개 중 ' + found.length + '개'), done ? BK.green : bad != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Hands together', '▶ 양손 함께 듣기')}</button>
        {done && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}

// ── step 5: arpeggios over four octaves: which finger? ──
const S4_AR = {   // two octaves going up, as the book prints them (Grade 4 pp63-64); four octaves repeat the middle
  E: { en: 'E major', ko: 'E장조', r: 4, q: [0, 4, 7], nm: ['E', 'G♯', 'B'], R: [1, 2, 3, 1, 2, 3, 5], L: [5, 3, 2, 1, 3, 2, 1] },
  Em: { en: 'E minor', ko: 'E단조', r: 4, q: [0, 3, 7], nm: ['E', 'G', 'B'], R: [1, 2, 3, 1, 2, 3, 5], L: [5, 4, 2, 1, 4, 2, 1] },
  Ab: { en: 'A♭ major', ko: 'A♭장조', r: -4, q: [0, 4, 7], nm: ['A♭', 'C', 'E♭'], R: [2, 1, 2, 4, 1, 2, 4], L: [2, 1, 4, 2, 1, 4, 2] },
  Abm: { en: 'A♭ minor', ko: 'A♭단조', r: -4, q: [0, 3, 7], nm: ['A♭', 'C♭', 'E♭'], R: [2, 1, 2, 4, 1, 2, 4], L: [2, 1, 4, 2, 1, 4, 2] },
};
const S4_AR_KEYS = ['E', 'Em', 'Ab', 'Abm'];
const s4ArName = (k) => t(S4_AR[k].en, S4_AR[k].ko);
const s4ArKeys = (k, start = S4_AR[k].r, n = 2) => { const c = S4_AR[k], out = []; for (let j = 0; j <= 3 * n; j++) out.push(start + 12 * Math.floor(j / 3) + c.q[j % 3]); return out; };
const s4ArSeq = (k, start) => { const up = s4ArKeys(k, start, 4); return up.concat(up.slice(0, -1).reverse()); };
function S4ArpPad({ fixed, onResult }) {
  const T = useSpTimers();
  const [k, setK] = useState(fixed ? fixed.k : 'E'), [h, setH] = useState(fixed ? fixed.h : 'R'), [at, setAt] = useState(0), [wrong, setWrong] = useState(null), [miss, setMiss] = useState(0), [pl, setPl] = useState(null);
  const c = S4_AR[k], K = s4ArKeys(k), F = c[h], done = at >= 7, sh = h === 'L' ? 12 : 0;
  const reset = (fn) => { T.clear(); setAt(0); setWrong(null); setMiss(0); setPl(null); if (fn) fn(); };
  const play = () => { T.clear(); const sq = s4ArSeq(k, c.r - 12 - sh), run = spPlay(sq.map((x, n) => ({ at: n / 2, keys: [x], len: n === sq.length - 1 ? 1.5 : 0.5, vol: 0.13 })), 76, 2); if (!run) return;
    sq.forEach((x, n) => T.at(run.ms(n / 2), () => setPl(spPc(x)))); T.at(run.ms(sq.length / 2 + 1), () => setPl(null)); };
  const say = (f) => { if (done) return; if (f === F[at]) { const n = at + 1; setAt(n); setWrong(null); playKey(K[at] - sh, 0.4); if (n >= 7) { if (onResult) onResult({ ok: miss === 0 }); T.at(300, play); } } else { setWrong(f); setMiss(x => x + 1); } };
  const lit = {}, nums = {}; K.forEach((x, j) => { if (j < at) { nums[x] = F[j]; lit[x] = 'pale'; } }); if (!done) lit[K[at]] = wrong != null ? 'bad' : 'cor'; if (pl != null) K.forEach(x => { if (spPc(x) === pl) lit[x] = 'cor'; });
  const white = [...new Set(K.map((x, j) => (F[j] === 1 ? c.nm[j % 3] : null)).filter(Boolean))];   // the notes the thumb plays
  return (
    <div className="try-box" style={actBox} data-s4="arp">
      <div style={actTitle}>{t('Arpeggios: which finger?', '아르페지오: 몇 번 손가락?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>4급 아르페지오: 네 옥타브, 한 손씩, <b>한 박에 두 음</b>. 책은 두 옥타브를 보여 줘요: 가운데가 옥타브마다 되풀이돼요. <b>엄지는 흰건반</b>에: A♭ 아르페지오에서는 하나뿐인 흰건반에. 빨간 건반의 손가락을 골라요.</>
        : <>Grade 4 arpeggios: four octaves, hands separately, <b>two notes a beat</b>. The book shows two octaves: the middle repeats in every octave. <b>The thumb takes a white key</b>: in the A♭ arpeggios, the only white key. Choose the finger for the coral key.</>}</div>
      {!fixed && spChips(S4_AR_KEYS.map(x => [x, x === 'Em' ? 'Em' : x === 'Abm' ? 'A♭m' : S4_AR[x].nm[0]]), k, (x) => reset(() => setK(x)))}
      {!fixed && spChips([['R', spHand('R')], ['L', spHand('L')]], h, (x) => reset(() => setH(x)))}
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:BK.ink,margin:'2px 0 4px'}}>{s4ArName(k)} · {spHand(h)}</div>
      <SpKb lo={c.r} hi={c.r + 24} W={21} H={74} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, c.nm[j % 3]]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}} label={s4ArName(k)}/>
      {!done && <div style={{display:'grid',gridTemplateColumns:'repeat(5,minmax(0,1fr))',gap:6,marginTop:10}}>{[1, 2, 3, 4, 5].map(f => <button key={f} className={'choice-btn' + (wrong === f ? ' bad' : '')} onClick={() => say(f)} style={{padding:'12px 2px',fontSize:18,fontWeight:900}}>{f}</button>)}</div>}
      {spMsg(done ? t(spHand(h) + ': ' + F.join(' ') + '. The thumb on ' + white.join(' and ') + (miss ? '.' : '. First time!'), spHand(h) + ': ' + F.join(' ') + '. 엄지는 ' + white.join(', ') + (miss ? '.' : '. 한 번에!'))
        : wrong != null ? (F[at] === 1 ? t('A white key in this chord: the thumb.', '이 화음의 흰건반: 엄지.') : t('Not that one: count from the last thumb.', '그 번호가 아니에요: 마지막 엄지부터 세어 봐요.')) : t('Note ' + (at + 1) + ' of 7', '7개 중 ' + (at + 1) + '번째'), done ? BK.green : wrong != null ? BK.coral : undefined)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={play}>{t('▶ Four octaves', '▶ 네 옥타브')}</button>
        {done && !fixed && <button className="ghost-btn" style={spBtn} onClick={() => reset()}>{t('▶ Again', '▶ 다시')}</button>}
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const s4PicFour = () => { const m = spMiniKeys(4, 40, { 4: 'pale', 15: 'cor', 16: 'pale', 27: 'cor', 28: 'pale', 39: 'cor', 40: 'pale' }, 4, 30, 2, 7); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };
const s4PicTouch = () => ({ shapes: [{ k: 'raw', svg: [0, 1].map(b => '<rect x="' + (3 + b * 38) + '" y="11" width="35" height="22" rx="6" fill="' + (b % 2 ? '#fff' : 'rgba(38,41,107,0.10)') + '"/>' + [0, 1, 2, 3].map(q => lsCircleSvg(9 + b * 38 + q * 8, 22, 3.4, 'play', '')).join('')).join('') }], vb: [0, 0, 80, 44] });
const s4PicMirror = () => spPicMirror();
const s4PicChrom = () => { const m = spMiniKeys(4, 12, { 4: 'cor', 5: 'cor', 11: 'cor', 12: 'cor' }); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };
const s4PicArp = () => { const m = spMiniKeys(-4, 20, { [-4]: 'pale', 0: 'cor', 3: 'pale', 8: 'pale', 12: 'cor', 15: 'pale', 20: 'pale' }, 7); return { shapes: [{ k: 'raw', svg: m.svg }], vb: [0, 0, m.w, 44] }; };

function s4LbPages(scr = false) {
  const ch = 'scales-4', sp = bkChapterNo('scales-23');
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const checks5 = [[s4PicFour(), t('I play four octaves and know where finger 4 goes in every octave', '네 옥타브를 치고, 옥타브마다 4번 자리를 알아요')], [s4PicTouch(), t('I play four notes a beat, even, legato and staccato', '한 박에 네 음을 고르게, 레가토와 스타카토로')],
    [s4PicMirror(), t('I play contrary motion in the Grade 4 keys, each hand with its own fingers', '4급 조의 반대 방향을 손마다 자기 번호로')], [s4PicChrom(), t('I play the chromatic scale hands together: the hands differ only at E–F and B–C', '반음계 양손 함께: 두 손은 E–F와 B–C에서만 달라요')],
    [s4PicArp(), t('I play arpeggios over four octaves, the thumb on the right notes, two notes a beat', '네 옥타브 아르페지오, 엄지는 제자리에, 한 박에 두 음')]];
  const toc = [[t('One 4 in every octave', '옥타브마다 4번 하나'), 2], [t('Four notes a beat', '한 박에 네 음'), 3], [t('Contrary motion: mirror twins?', '반대 방향: 거울 쌍둥이?'), 4], [t('Chromatic, hands together', '반음계, 양손 함께'), 5], [t('Arpeggios: which finger?', '아르페지오: 몇 번 손가락?'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]];
  const kbW = scr ? 30 : 40, kbH = scr ? 80 : 104;
  const fourStill = (k, h) => { const c = S4_SC[k], K = s4Oct(k), F = s4Mid(k, h), j4 = s4F4(k, h), lit = {}, nums = {}; K.forEach((x, j) => { lit[x] = j === j4 ? 'cor' : 'pale'; nums[x] = F[j]; });
    return <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{s4Name(k)} · {spHand(h)}</div><SpKb lo={c.r} hi={c.r + 12} W={kbW} H={kbH} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, c.nm[j % 7]]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}}/></div>; };
  const chromStill = () => { const s0 = 4, K = Array.from({ length: 13 }, (_, j) => s0 + j), up = {}, dn = {}, lit = {}; K.forEach(x => { up[x] = s4ChR(x); dn[x] = s4ChL(x); if (s4ChR(x) !== s4ChL(x)) lit[x] = 'cor'; });
    return <SpKb lo={s0} hi={s0 + 12} W={kbW} H={kbH} lit={lit} names={Object.fromEntries(K.filter(spIsW).map(x => [x, s4ChLet(x)]))} up={up} dn={dn}/>; };
  const arpStill = (k, h) => { const c = S4_AR[k], K = s4ArKeys(k), lit = {}, nums = {}; K.forEach((x, j) => { lit[x] = c[h][j] === 1 ? 'cor' : 'pale'; nums[x] = c[h][j]; });
    return <div><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{s4ArName(k)} · {spHand(h)}</div><SpKb lo={c.r} hi={c.r + 24} W={scr ? 19 : 24} H={scr ? 66 : 84} lit={lit} names={Object.fromEntries(K.map((x, j) => [x, c.nm[j % 3]]))} up={h === 'R' ? nums : {}} dn={h === 'L' ? nums : {}}/></div>; };
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('The Grade 4 technical work as skills (chapter ' + sp + ' has Grades 2 and 3). From the technical work book, Grade 4: scales four octaves, mf, clear even legato, four notes a beat at ♩ = 63, hands separately and together; staccato scales at ♩ = 52; contrary motion two octaves at ♩ = 52; chromatic scales four octaves at ♩ = 63, hands separately and together; arpeggios four octaves, hands separately, two notes a beat at ♩ = 76. The book prints two octaves to show the fingering: play four, in most cases starting an octave lower than written. Another fingering is fine if it is logical and systematic. The keys are in the teacher\'s copy.', '4급 테크니컬 워크를 기술로(' + sp + '장은 2·3급). 테크니컬 워크 책 4급: 스케일은 네 옥타브, mf, 고르고 또렷한 레가토, 한 박에 네 음 ♩ = 63, 한 손씩 그리고 양손 함께; 스타카토 스케일 ♩ = 52; 반대 방향은 두 옥타브 ♩ = 52; 반음계는 네 옥타브 ♩ = 63, 한 손씩 그리고 양손 함께; 아르페지오는 네 옥타브, 한 손씩, 한 박에 두 음 ♩ = 76. 책은 운지를 보여 주려고 두 옥타브만 적어요: 시험에서는 네 옥타브, 대개 적힌 것보다 한 옥타브 아래에서 시작해요. 논리적이고 일관되면 다른 운지도 괜찮아요. 조 목록은 선생님용에 있어요.'))}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:46,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={170}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}>{fourStill('E', 'R')}<S4Map k="E" h="R" mw={560}/></div></LbPic>
      <LbSay size={18}>{t('Grade 4 technique: four octaves with one 4 in every octave, four notes a beat, legato and staccato, contrary motion in new keys, the chromatic scale hands together, and arpeggios over four octaves.', '4급 테크닉: 옥타브마다 4번 하나로 네 옥타브, 한 박에 네 음, 레가토와 스타카토, 새 조의 반대 방향, 양손 반음계, 네 옥타브 아르페지오.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:700}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {[t('find finger 4 in every octave of a four-octave scale', '네 옥타브 스케일에서 옥타브마다 4번 자리를 찾을 수 있어요'), t('play four notes a beat, legato and staccato', '한 박에 네 음을 레가토와 스타카토로 칠 수 있어요'), t('play the chromatic scale hands together', '반음계를 양손으로 칠 수 있어요'), t('finger an arpeggio over four octaves', '네 옥타브 아르페지오의 손가락을 알아요')].map((x, i) => <div key={i} style={{display:'flex',alignItems:'flex-start',gap:9,fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('One 4 in every octave', '옥타브마다 4번 하나')}
      teacher={<>{spTx(t('Four octaves, hands separately and together, ♩ = 63 four notes a beat: E major; C♯ minor natural, harmonic and melodic; A♭ major; F minor natural, harmonic and melodic. In each scale finger 4 plays one note per octave: RH D♯ in E major and C♯ minor, A♯ going up in C♯ melodic minor (D♯ coming down), B♭ in A♭ major and F minor; LH F♯ in E major and C♯ minor, D♭ in A♭ major, G in F minor. In C♯ minor and A♭ major the RH starts on 2 3, so the first octave has no 4. Find the 4s before playing four octaves: they keep the hand oriented while the arm travels.', '네 옥타브, 한 손씩 그리고 양손 함께, ♩ = 63 한 박에 네 음: E장조; C♯단조 자연·화성·가락; A♭장조; F단조 자연·화성·가락. 스케일마다 4번은 옥타브에 한 음: 오른손은 E장조와 C♯단조에서 D♯, C♯ 가락 단음계는 올라갈 때 A♯(내려올 때 D♯), A♭장조와 F단조에서 B♭; 왼손은 E장조와 C♯단조에서 F♯, A♭장조에서 D♭, F단조에서 G. C♯단조와 A♭장조는 오른손이 2 3으로 시작해서 첫 옥타브에는 4가 없어요. 네 옥타브를 치기 전에 4번 자리를 먼저 찾아요: 팔이 이동하는 동안 손이 길을 잃지 않게 해 줘요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{fourStill('E', 'R')}{fourStill('E', 'L')}</div></LbPic>} live={<S4FourPad/>}/>
      <LbSay>{LANG === 'ko' ? <>네 옥타브에서는 <b>팔이 손을 데려가요</b>. 손가락 무늬는 옥타브마다 똑같고, <b>4번은 옥타브마다 한 번, 같은 음</b>. E장조 오른손은 D♯, 왼손은 F♯.</> : <>In four octaves <b>the arm carries the hand</b>. The finger pattern is the same in every octave, and <b>finger 4 plays once an octave, always the same note</b>. E major: right hand D♯, left hand F♯.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>E장조 오른손: 옥타브마다 D♯에 4번을 놓아 봐요. 네 옥타브 위로.</>, <>왼손: F♯에 4번. 네 옥타브 위로.</>, <>네 옥타브 스케일: 4번이 올 때마다 속으로 "4!". ♩ = 63, 한 박에 네 음까지.</>]
        : [<>E major, right hand: put finger 4 on D♯ in each octave, four octaves up.</>, <>Left hand: finger 4 on F♯, four octaves up.</>, <>The four-octave scale: say "4!" inside each time it comes. Up to ♩ = 63, four notes a beat.</>]}/>
      <LbRemember>{t('One 4 in every octave, always the same note.', '옥타브마다 4번 하나, 언제나 같은 음.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Four notes a beat', '한 박에 네 음')}
      teacher={<>{spTx(t('Every Grade 4 scale goes four notes a beat (semiquavers): similar motion and chromatic at ♩ = 63, contrary motion and staccato at ♩ = 52. Staccato: A♭ major and F melodic minor, four octaves, hands separately and together, mf, the same fingering as legato. The beat note of each group of four is where unevenness shows first: tap or count the beats while the scale runs.', '4급 스케일은 모두 한 박에 네 음(16분음표): 같은 방향과 반음계 ♩ = 63, 반대 방향과 스타카토 ♩ = 52. 스타카토: A♭장조와 F 가락 단음계, 네 옥타브, 한 손씩 그리고 양손 함께, mf, 레가토와 같은 운지. 네 음 묶음의 박 음에서 고르지 않음이 먼저 드러나요: 스케일이 흐르는 동안 박을 치거나 세어 보세요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:620,margin:'0 auto'}}><S4Groups k="Ab"/></div></LbPic>} live={<S4TouchPad/>}/>
      <LbSay>{LANG === 'ko' ? <><b>한 박에 네 음</b>: 1-e-+-a. 묶음의 첫 음이 박. <b>스타카토</b>는 같은 손가락, 같은 박에 음만 짧게.</> : <><b>Four notes a beat</b>: 1-e-and-a. The first of each group is the beat. <b>Staccato</b>: the same fingers, the same beat, only the notes short.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>A♭장조 한 옥타브를 한 박에 두 음으로, 그다음 네 음으로.</>, <>박 음(밑줄)만 살짝 강하게. 그다음 고르게.</>, <>스타카토로: 같은 손가락, 짧게. ♩ = 52까지.</>]
        : [<>A♭ major, one octave, two notes a beat, then four.</>, <>Lean a little on each beat note (underlined). Then play it even.</>, <>Staccato: the same fingers, short. Up to ♩ = 52.</>]}/>
      <LbRemember>{t('Four to a beat: 1-e-and-a.', '한 박에 넷: 1-e-+-a.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Contrary motion: mirror twins?', '반대 방향: 거울 쌍둥이?')}
      teacher={<>{spTx(t('Contrary motion, two octaves, hands together from one note, ♩ = 52 four notes a beat: A major, F♯ harmonic minor, E♭ major, C harmonic minor. Each hand keeps its own scale fingering: in A, E♭ and C minor the numbers mirror all the way; in F♯ minor they don\'t (RH 2 3 1 2 3 1 2 3, LH 2 1 2 3 1 2 3 4), so the hands turn at different times.', '반대 방향, 두 옥타브, 두 손이 한 음에서, ♩ = 52 한 박에 네 음: A장조, F♯ 화성 단음계, E♭장조, C 화성 단음계. 손마다 자기 스케일 번호: A, E♭, C단조는 끝까지 같은 번호; F♯단조는 달라요(오른손 2 3 1 2 3 1 2 3, 왼손 2 1 2 3 1 2 3 4). 그래서 두 손이 다른 때에 넘어가요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={160}><div style={{display:'grid',gridTemplateColumns:'1fr',gap:16,width:'100%',maxWidth:scr ? 440 : 560,margin:'0 auto'}}><div><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{scfCmName('A4')} · {t('mirror twins', '거울 쌍둥이')}</div><ScfCmKb k="A4" W={scr ? 20 : 30} H={scr ? 66 : 84}/></div><div><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{scfCmName('Fsmh')} · {t('not mirror twins', '거울 쌍둥이 아님')}</div><ScfCmKb k="Fsmh" W={scr ? 20 : 30} H={scr ? 66 : 84} mark={scfFirstDiff('Fsmh')}/></div></div></LbPic>} live={<S4MirrorPad/>}/>
      <LbSay>{LANG === 'ko' ? <>4급 반대 방향 네 조 중 셋은 <b>거울 쌍둥이</b>: A장조, E♭장조, C단조. <b>F♯단조</b>만 두 손의 번호가 둘째 음부터 달라요.</> : <>Three of the four Grade 4 keys are <b>mirror twins</b>: A major, E♭ major, C minor. Only in <b>F♯ minor</b> do the numbers part, from the second note.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>두 손을 같은 음에. F♯단조: 오른손 2 3 1, 왼손 2 1 2.</>, <>번호가 달라지는 곳에서 멈춰서 확인해요.</>, <>한 박에 두 음, 그다음 네 음. ♩ = 52까지.</>]
        : [<>Both hands on the same note. F♯ minor: right hand 2 3 1, left hand 2 1 2.</>, <>Stop where the numbers part, and check.</>, <>Two notes a beat, then four. Up to ♩ = 52.</>]}/>
      <LbRemember>{t('Each hand keeps its own numbers.', '손마다 자기 번호를 지켜요.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Chromatic, hands together', '반음계, 양손 함께')}
      teacher={<>{spTx(t('Chromatic scales from E and from G♯/A♭, four octaves, hands separately and together, ♩ = 63 four notes a beat. The book\'s fingering keeps the Grades 2–3 rule: 3 on every black key, 1 on white keys, 2 on the right hand\'s F and C and the left hand\'s E and B. Hands together, the 3s always land together; the fingers differ only on E, F, B and C. From E the left hand starts on 2.', 'E와 G♯/A♭에서 반음계, 네 옥타브, 한 손씩 그리고 양손 함께, ♩ = 63 한 박에 네 음. 책의 운지는 2·3급 규칙 그대로: 검은건반 3, 흰건반 1, 오른손 F와 C, 왼손 E와 B는 2. 양손 함께면 3번은 언제나 같이 떨어지고, 번호가 다른 곳은 E, F, B, C뿐이에요. E에서 시작하면 왼손은 2번으로 시작해요.'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={<LbPic h={160}><div style={{width:'100%',maxWidth:600,margin:'0 auto'}}>{chromStill()}</div></LbPic>} live={<S4ChromPad/>}/>
      <LbSay>{LANG === 'ko' ? <>양손 함께면 <b>3번은 언제나 함께</b>. 두 손이 다른 곳은 <b>E–F와 B–C</b> 둘레뿐: 오른손은 F와 C에 2, 왼손은 E와 B에 2.</> : <>Hands together, <b>the 3s always land together</b>. The hands differ only around <b>E–F and B–C</b>: the right hand's 2 on F and C, the left hand's on E and B.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>E에서 한 손씩, 한 옥타브. E–F와 B–C에서 번호를 확인해요.</>, <>양손 함께, 아주 천천히: 3번이 같이 떨어지는지 들어 봐요.</>, <>네 옥타브, 한 박에 네 음. ♩ = 63까지.</>]
        : [<>From E, each hand, one octave. Check the numbers at E–F and B–C.</>, <>Hands together, very slowly: hear the 3s land together.</>, <>Four octaves, four notes a beat. Up to ♩ = 63.</>]}/>
      <LbRemember>{t('The 3s together; the 2s apart.', '3번은 함께, 2번은 따로.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Arpeggios: which finger?', '아르페지오: 몇 번 손가락?')}
      teacher={<>{spTx(t('Arpeggios E major and minor, A♭ major and minor, four octaves, hands separately, ♩ = 76 two notes a beat, as continuous even quavers. The book\'s fingerings: E major and minor RH 1 2 3 1 2 3 5; LH 5 3 2 1 3 2 1 (major), 5 4 2 1 4 2 1 (minor). A♭ major and minor RH 2 1 2 4 1 2 4, LH 2 1 4 2 1 4 2: the thumb on C (C♭ in the minor), the only white key. The book also suggests practising them first in two long-short rhythms (optional, not for the exam).', '아르페지오 E장조와 단조, A♭장조와 단조, 네 옥타브, 한 손씩, ♩ = 76 한 박에 두 음, 끊김 없이 고른 8분음표로. 책의 운지: E장조·단조 오른손 1 2 3 1 2 3 5; 왼손 5 3 2 1 3 2 1(장조), 5 4 2 1 4 2 1(단조). A♭장조·단조 오른손 2 1 2 4 1 2 4, 왼손 2 1 4 2 1 4 2: 엄지는 C(단조는 C♭), 하나뿐인 흰건반. 책은 먼저 긴-짧은 두 가지 리듬으로 연습해 보라고도 해요(선택, 시험에는 없음).'))}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=5')}>
      <LbLive still={<LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{arpStill('E', 'L')}{arpStill('Ab', 'R')}</div></LbPic>} live={<S4ArpPad/>}/>
      <LbSay>{LANG === 'ko' ? <>아르페지오는 <b>한 박에 두 음</b>, 네 옥타브. <b>엄지는 흰건반</b>: E에서는 E, A♭에서는 하나뿐인 흰건반 C(단조는 C♭). 왼손 E장조는 5 3 2 1, E단조는 5 4 2 1.</> : <>Arpeggios: <b>two notes a beat</b>, four octaves. <b>The thumb takes a white key</b>: E in E, and in A♭ the only white key, C (C♭ in the minor). The left hand: 5 3 2 1 in E major, 5 4 2 1 in E minor.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>E장조 오른손 두 옥타브: 1 2 3 1 2 3 5. 엄지가 E에 올 때 팔이 손을 데려가요.</>, <>A♭장조 오른손: 엄지 자리 C를 먼저 찾고, 2 1 2 4.</>, <>네 옥타브, 고른 8분음표. ♩ = 76까지.</>]
        : [<>E major, right hand, two octaves: 1 2 3 1 2 3 5. As the thumb comes to E, the arm carries the hand on.</>, <>A♭ major, right hand: find the thumb's C first, then 2 1 2 4.</>, <>Four octaves, even quavers. Up to ♩ = 76.</>]}/>
      <LbRemember>{t('The thumb on the white key; the arm carries the hand.', '엄지는 흰건반에, 팔이 손을 데려가요.')}</LbRemember>
    </LbPage>,
    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Each one played to you from memory, in the Grade 4 keys (the teacher\'s copy lists them), four octaves where the book asks for four. Listen for the beat notes: even groups of four, and the same evenness staccato.', '하나씩 외워서, 4급 조로(선생님용에 목록), 책이 네 옥타브를 요구하는 것은 네 옥타브로 들려줘요. 박 음을 들어 주세요: 고른 네 음 묶음, 스타카토도 똑같이 고르게.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks5.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks5} storeKey="pb_s4_five"/>}/>
    </LbPage>,
  ];
}
function Scales4LessonBook() { return <>{s4LbPages(false)}</>; }
function S4Learn({ onStart }) {
  const pages = s4LbPages(true), opener = pages[0];
  return (
    <Lesson id="scales-4" title={bkChapterName('scales-4')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="scales-4"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill ──
const S4_LEVELS = [
  { n: 1, label: 'Four octaves: where does finger 4 go?', kind: 'four', time: 15 },
  { n: 2, label: 'Legato or staccato?', kind: 'touch', time: 20 },
  { n: 3, label: 'Grade 4 contrary motion: mirror twins?', kind: 'mirror', time: 15 },
  { n: 4, label: 'Chromatic hands together: the same finger?', kind: 'chrom', time: 12 },
  { n: 5, label: 'Arpeggios: which finger?', kind: 'arp', time: 15 },
];
Object.assign(LEVEL_KO, { 'Four octaves: where does finger 4 go?': '네 옥타브: 4번은 어디에?', 'Legato or staccato?': '레가토? 스타카토?', 'Grade 4 contrary motion: mirror twins?': '4급 반대 방향: 거울 쌍둥이?', 'Chromatic hands together: the same finger?': '양손 반음계: 같은 손가락?', 'Arpeggios: which finger?': '아르페지오: 몇 번 손가락?' });
const s4ChAns = (i) => (s4ChR(i) !== s4ChL(i) ? 'diff' : s4ChR(i) === 3 ? '3' : '1');
const S4_CH_LAB = { '3': ['Both 3', '둘 다 3번'], '1': ['Both 1', '둘 다 1번'], diff: ['Different fingers', '다른 손가락'] };
function genS4Question(lv, prev) {
  const uid = Math.random(), kind = lv.kind;
  if (kind === 'four') { let k, h, g = 0; do { k = pick(S4_KEYS); h = Math.random() < 0.5 ? 'R' : 'L'; } while (prev && prev.key === k + h && g++ < 10); const nm = S4_SC[k].nm;
    return { kind, k, h, answer: s4F4Note(k, h), choices: nm.slice(), key: k + h, uid }; }
  if (kind === 'touch') { let k, st, g = 0; do { k = Math.random() < 0.5 ? 'Ab' : 'Fmel'; st = Math.random() < 0.5; } while (prev && prev.key === k + st && g++ < 10); return { kind, k, st, answer: st ? 'stac' : 'leg', choices: ['leg', 'stac'], key: k + st, uid }; }
  if (kind === 'mirror') { let k, g = 0; do { k = pick(S4_CM_KEYS); } while (prev && prev.key === 'c' + k && g++ < 10); return { kind, k, answer: scfMirror(k) ? 'yes' : 'no', choices: ['yes', 'no'], key: 'c' + k, uid }; }
  if (kind === 'chrom') { let st, j, g = 0; do { st = Math.floor(Math.random() * 2); j = Math.floor(Math.random() * 12); } while (prev && prev.key === 'h' + st + j && g++ < 10); const i = S4_CH[st][1] + j;
    return { kind, st, j, i, answer: s4ChAns(i), choices: ['3', '1', 'diff'], key: 'h' + st + j, uid }; }
  let k, h, j, g = 0; do { k = pick(S4_AR_KEYS); h = Math.random() < 0.5 ? 'R' : 'L'; j = Math.floor(Math.random() * 7); } while (prev && prev.key === 'a' + k + h + j && g++ < 10);
  return { kind: 'arp', k, h, j, answer: S4_AR[k][h][j], choices: [1, 2, 3, 4, 5], key: 'a' + k + h + j, uid };
}
function s4AnswerLabel(q) {
  if (q.kind === 'four') return q.answer;
  if (q.kind === 'touch') return q.answer === 'stac' ? t('staccato', '스타카토') : t('legato', '레가토');
  if (q.kind === 'mirror') return q.answer === 'yes' ? t('mirror twins', '거울 쌍둥이') : t('not mirror twins', '거울 쌍둥이 아님');
  if (q.kind === 'chrom') return t(S4_CH_LAB[q.answer][0], S4_CH_LAB[q.answer][1]);
  return t('finger ' + q.answer, q.answer + '번');
}
function S4Question({ q, given, locked, onAnswer, pixel }) {
  const done = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn', cls = (c) => btnCls + (!done ? '' : c === q.answer ? ' good' : given.ans === c ? ' bad' : '');
  const pickIt = (c) => { if (locked || done) return; stopClicks(); onAnswer(c); };
  const grid = (cols, items) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{items.map(([c, lab]) => <button key={String(c)} disabled={locked} className={cls(c)} style={{padding:'12px 4px',fontSize:15,fontWeight:900}} onClick={() => pickIt(c)}>{lab}</button>)}</div>;
  const playTouch = () => { stopClicks(); s4PlayTouch(q.k, q.st); };
  useEffect(() => { if (q.kind !== 'touch') return; const id = setTimeout(playTouch, 350); return () => { clearTimeout(id); stopClicks(); }; }, [q.uid]);
  let title, body;
  if (q.kind === 'four') { const c = S4_SC[q.k], K = s4Oct(q.k), F = s4Mid(q.k, q.h), j4 = s4F4(q.k, q.h), nums = {}, lit = {}; K.forEach((x, j) => { if (F[j] === 1 || (done && j === j4)) nums[x] = F[j]; lit[x] = 'pale'; }); if (done) lit[K[j4]] = 'good';
    title = t(s4Name(q.k) + (q.k === 'Csmel' ? ' going up' : '') + ', ' + spHand(q.h).toLowerCase() + ': which note does finger 4 play in every octave?', s4Name(q.k) + (q.k === 'Csmel' ? '(올라갈 때)' : '') + ', ' + spHand(q.h) + ': 옥타브마다 4번이 치는 음은?');
    body = <><SpKb lo={c.r} hi={c.r + 12} W={28} H={78} lit={lit} names={{ [K[0]]: c.nm[0] }} up={q.h === 'R' ? nums : {}} dn={q.h === 'L' ? nums : {}}/>{grid(4, q.choices.map(x => [x, x]))}</>; }
  else if (q.kind === 'touch') { title = t('Listen: legato or staccato?', '들어 봐요: 레가토? 스타카토?');
    body = <><div style={{textAlign:'center'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:44}} onClick={playTouch}>{t('▶ Play it again', '▶ 다시 듣기')}</button></div>{grid(2, [['leg', t('Legato', '레가토')], ['stac', t('Staccato', '스타카토')]])}</>; }
  else if (q.kind === 'mirror') { title = t('Contrary motion, ' + scfCmName(q.k) + ': mirror twins?', '반대 방향, ' + scfCmName(q.k) + ': 거울 쌍둥이일까?');
    body = <><ScfCmKb k={q.k} mark={done && q.answer === 'no' ? scfFirstDiff(q.k) : -1}/>{grid(2, [['yes', t('Mirror twins', '거울 쌍둥이')], ['no', t('Not mirror twins', '거울 쌍둥이 아님')]])}</>; }
  else if (q.kind === 'chrom') { const s0 = S4_CH[q.st][1], lit = { [q.i]: done ? (given.ans === q.answer ? 'good' : 'bad') : 'cor' }, up = {}, dn = {}; if (done) { up[q.i] = s4ChR(q.i); dn[q.i] = s4ChL(q.i); }
    title = t('Chromatic scale hands together: on ' + s4ChLet(q.i) + ', which fingers?', '양손 반음계: ' + s4ChLet(q.i) + '에서 두 손의 손가락은?');
    body = <><SpKb lo={s0} hi={s0 + 12} W={28} H={78} lit={lit} names={{ [q.i]: s4ChLet(q.i) }} up={up} dn={dn}/>{grid(3, q.choices.map(c => [c, t(S4_CH_LAB[c][0], S4_CH_LAB[c][1])]))}</>; }
  else { const c = S4_AR[q.k], K = s4ArKeys(q.k), F = c[q.h], nums = {}, lit = {}; K.forEach((x, j) => { if (j < q.j) nums[x] = F[j]; lit[x] = 'pale'; }); lit[K[q.j]] = done ? (given.ans === q.answer ? 'good' : 'bad') : 'cor'; if (done) nums[K[q.j]] = F[q.j];
    title = t(s4ArName(q.k) + ' arpeggio, ' + spHand(q.h).toLowerCase() + ': which finger plays the coral ' + c.nm[q.j % 3] + '?', s4ArName(q.k) + ' 아르페지오, ' + spHand(q.h) + ': 빨간 ' + c.nm[q.j % 3] + '은 몇 번?');
    body = <><SpKb lo={c.r} hi={c.r + 24} W={19} H={70} lit={lit} names={{ [K[q.j]]: c.nm[q.j % 3] }} up={q.h === 'R' ? nums : {}} dn={q.h === 'L' ? nums : {}}/>{grid(5, [1, 2, 3, 4, 5].map(f => [f, String(f)]))}</>; }
  const why = !done || pixel ? null : q.kind === 'four' ? t(spHand(q.h) + ', a middle octave: ' + s4Mid(q.k, q.h).join(' ') + '.', spHand(q.h) + ', 가운데 옥타브: ' + s4Mid(q.k, q.h).join(' ') + '.')
    : q.kind === 'chrom' ? t(q.answer === 'diff' ? 'Around E–F and B–C the hands differ: RH 2 on F and C, LH 2 on E and B.' : q.answer === '3' ? 'A black key: both hands 3.' : 'A white key away from E–F and B–C: both hands 1.', q.answer === 'diff' ? 'E–F와 B–C 둘레에서는 달라요: 오른손 F와 C에 2, 왼손 E와 B에 2.' : q.answer === '3' ? '검은건반: 두 손 모두 3번.' : 'E–F와 B–C에서 떨어진 흰건반: 두 손 모두 1번.')
    : q.kind === 'arp' ? t(spHand(q.h) + ': ' + S4_AR[q.k][q.h].join(' ') + '.', spHand(q.h) + ': ' + S4_AR[q.k][q.h].join(' ') + '.') : null;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {body}
    {why && <div style={{marginTop:10,fontSize:13.5,color:'#4a4d86',background:'#fff',borderRadius:8,padding:'7px 10px',lineHeight:1.45}}>{why}</div>}
  </div>);
}
Object.assign(SCALES_4_DRILL, { levels: S4_LEVELS, generate: genS4Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: s4AnswerLabel, Question: S4Question, Learn: S4Learn });
// the teacher's copy: the keys and speeds, and what to listen for (the Workbook comes with the floor's Workbooks)
function S4Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="scales-4" teacher>{content}</WbPage>);
  const mid = (k) => S4_SC[k].en + ': RH ' + s4Mid(k, 'R').join(' ') + ' · LH ' + s4Mid(k, 'L').join(' ') + ' (4: RH ' + s4F4Note(k, 'R') + ', LH ' + s4F4Note(k, 'L') + ')';
  const arp = (k) => S4_AR[k].en + ': RH ' + S4_AR[k].R.join(' ') + ' · LH ' + S4_AR[k].L.join(' ');
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('scales-4')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>{spTx('The keys, speeds and fingerings are the technical work book\'s (Grade 4 pp58–64). Scales and arpeggios four octaves (the book prints two: in most cases start an octave lower than written), mf, from memory. Another fingering is fine if it is logical and systematic.')}</div>
    <TcBlock page={2} title="One 4 in every octave" answers={<>{tcAns(spTx('SIMILAR MOTION, FOUR OCTAVES, HANDS SEPARATELY AND TOGETHER, ♩ = 63 FOUR NOTES A BEAT · A MIDDLE OCTAVE'), [mid('E'), mid('Csm'), mid('Csmel') + '; coming down as the natural minor', mid('Ab'), mid('Fm')])}</>}
      watch="Losing the place in the third and fourth octaves. Find the 4s first; the RH in C♯ minor and A♭ starts on 2 3, so its first 4 is in the second octave. C♯ melodic minor moves the RH 4 to A♯ going up."
      say="“One 4 in every octave, always the same note.”"/>
    <TcBlock page={3} title="Four notes a beat" answers={<>{tcAns(spTx('STACCATO, FOUR OCTAVES, HANDS SEPARATELY AND TOGETHER, ♩ = 52'), ['A♭ major', 'F melodic minor'])}{tcAns('ALL SCALES', ['four notes a beat: similar motion and chromatic ♩ = 63; contrary motion and staccato ♩ = 52'], null)}</>}
      watch="Rushing the groups of four, or staccato that drags because the fingers press instead of lifting. Same fingering as legato."
      say="“Four to a beat: 1-e-and-a.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Contrary motion: mirror twins?" answers={<>{tcAns(spTx('TWO OCTAVES FROM ONE NOTE, ♩ = 52 FOUR NOTES A BEAT'), ['A major (mirror)', 'F♯ harmonic minor (not: RH 2 3 1 2 3 1 2 3, LH 2 1 2 3 1 2 3 4)', 'E♭ major (mirror: 2 1 2 3 4 1 2 3)', 'C harmonic minor (mirror)'])}</>}
      watch="The LH copying the RH in F♯ minor. Each hand keeps its own fingering."
      say="“Each hand keeps its own numbers.”"/>
    <TcBlock page={5} title="Chromatic, hands together" answers={<>{tcAns(spTx('FROM E AND FROM G♯/A♭, FOUR OCTAVES, ♩ = 63'), ['RH 3 on black, 1 on white, 2 on F and C', 'LH 3 on black, 1 on white, 2 on E and B (from E the LH starts on 2)', 'Hands together the fingers differ only on E, F, B and C'])}</>}
      watch="The hands drifting apart at E–F and B–C. The 3s land together: listen for one sound."
      say="“The 3s together; the 2s apart.”"/>
    <TcBlock page={6} title="Arpeggios: which finger?" answers={<>{tcAns(spTx('FOUR OCTAVES, HANDS SEPARATELY, ♩ = 76 TWO NOTES A BEAT'), [arp('E'), arp('Em'), arp('Ab'), arp('Abm')])}</>}
      watch="A bump each time the thumb passes: the arm carries the hand smoothly. E minor LH uses 4 on G, E major LH 3 on G♯."
      say="“The thumb on the white key; the arm carries the hand.”"/>
    <TcBlock page={7} title="My five checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one played to you from memory, in the Grade 4 keys, at the book's speeds. Listen for even groups of four, the same staccato, and the turns.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['scales-4'] = S4Teacher;
'''
rep("""TEACHER_COPIES['scales-23'] = ScfTeacher;""", """TEACHER_COPIES['scales-23'] = ScfTeacher;""" + CH)   # after the Grades 2-3 scales code: it borrows SCF_CM and its keyboard

HOME = r'''
// ══ Build AS: Scales and Arpeggios, Grade 4 on the Home (Technique, after Scales further) ══
LBH_FN['scales-4'] = (s) => s4LbPages(s);
const s4HomeAdd = (id, i, en, ko, benEn, bko, make) => lbhAdd(id, 'k-play', 'tech', en, ko, benEn, bko, lbhSpec('scales-4', i, { make }));
const s4TouchQ = (n, prev) => { let k, st, g = 0; do { k = Math.random() < 0.5 ? 'Ab' : 'Fmel'; st = Math.random() < 0.5; } while (prev && prev.key === k + st && g++ < 10); const a = st ? 'stac' : 'leg';
  return { kind: 'choice', cols: 2, key: k + st, prompt: ['Listen: legato or staccato?', '들어 봐요: 레가토? 스타카토?'], opts: [{ id: 'leg', label: () => t('Legato', '레가토') }, { id: 'stac', label: () => t('Staccato', '스타카토') }], ans: a, ok: (v) => v === a,
    play: () => s4PlayTouch(k, st), fig: () => ({ mid: <S4Groups k={k}/> }), yes: st ? ['Yes: staccato, short and even.', '맞아요: 스타카토, 짧고 고르게.'] : ['Yes: legato, each note joined to the next.', '맞아요: 레가토, 음마다 이어져요.'], no: st ? ['It was staccato: short notes, the same beat.', '스타카토였어요: 짧은 음, 같은 박.'] : ['It was legato: each note held to the next.', '레가토였어요: 다음 음까지 이어서.'] }; };
const s4MirrorQ = (n, prev) => { let k, g = 0; do { k = pick(S4_CM_KEYS); } while (prev && prev.key === k && g++ < 10); const a = scfMirror(k) ? 'yes' : 'no';
  return { kind: 'choice', cols: 2, key: k, prompt: ['Contrary motion, ' + SCF_CM[k].en + ': mirror twins?', '반대 방향, ' + SCF_CM[k].ko + ': 거울 쌍둥이일까?'], opts: [{ id: 'yes', label: () => t('Mirror twins', '거울 쌍둥이') }, { id: 'no', label: () => t('Not mirror twins', '거울 쌍둥이 아님') }], ans: a, ok: (v) => v === a,
    fig: (c) => ({ mid: <ScfCmKb k={k} mark={c.res && a === 'no' ? scfFirstDiff(k) : -1}/> }), yes: a === 'yes' ? ['Yes: the same numbers all the way.', '맞아요: 끝까지 같은 번호.'] : ['Yes: each hand keeps its own numbers.', '맞아요: 손마다 자기 번호.'], no: a === 'yes' ? ['Look again: the numbers match all the way.', '다시 봐요: 끝까지 같은 번호예요.'] : ['Look again: the coral keys have different numbers.', '다시 봐요: 빨간 건반의 번호가 달라요.'] }; };
s4HomeAdd('s4-four', 1, 'One 4 in every octave', '옥타브마다 4번 하나', 'Four octaves: finger 4 plays the same note in every octave.', '네 옥타브: 4번은 옥타브마다 같은 음.', lwTapQ(S4FourPad, (n) => ({ fixed: { k: S4_KEYS[(n * 2) % S4_KEYS.length], h: n % 2 ? 'L' : 'R' } }), ['Tap the key finger 4 plays.', '4번이 치는 건반을 눌러요.'], ['Finger 4 found ✓', '4번 자리 찾았어요 ✓']));
s4HomeAdd('s4-touch', 2, 'Four notes a beat', '한 박에 네 음', 'Legato or staccato, four notes to every beat.', '레가토든 스타카토든, 박마다 네 음.', s4TouchQ);
s4HomeAdd('s4-mirror', 3, 'Contrary motion: mirror twins?', '반대 방향: 거울 쌍둥이?', 'The Grade 4 keys: three twins and one not.', '4급 조: 쌍둥이 셋, 아닌 것 하나.', s4MirrorQ);
s4HomeAdd('s4-chrom', 4, 'Chromatic, hands together', '반음계, 양손 함께', 'The 3s together; the hands differ only at E–F and B–C.', '3번은 함께, E–F와 B–C에서만 달라요.', lwTapQ(S4ChromPad, (n) => ({ fixed: n % 2 }), ['Tap every key where the hands use different fingers.', '두 손의 번호가 다른 건반을 모두 눌러요.'], ['Found them ✓', '찾았어요 ✓']));
s4HomeAdd('s4-arp', 5, 'Arpeggios: which finger?', '아르페지오: 몇 번 손가락?', 'Four octaves; the thumb on the white key.', '네 옥타브, 엄지는 흰건반에.', lwTapQ(S4ArpPad, (n) => ({ fixed: { k: S4_AR_KEYS[n % S4_AR_KEYS.length], h: n % 2 ? 'L' : 'R' } }), ['Choose the finger for each coral key.', '빨간 건반마다 손가락을 골라요.'], ['All seven ✓', '일곱 개 모두 ✓']));
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
rep("""const LESSON_BOOKS = { 'listen-4': Listen4LessonBook,""", """const LESSON_BOOKS = { 'scales-4': Scales4LessonBook, 'listen-4': Listen4LessonBook,""")
rep("""const LB_PAGE_FNS = { 'listen-4': l4LbPages,""", """const LB_PAGE_FNS = { 'scales-4': s4LbPages, 'listen-4': l4LbPages,""")
rep("""const HOUSE_ICONS = {"listen-4": """, """const HOUSE_ICONS = {"scales-4": "<path d=\\"M4 31 H12 V25 H20 V19 H28 V13 H36 V7 H44\\"/><rect x=\\"9\\" y=\\"30\\" width=\\"7\\" height=\\"11\\" rx=\\"1.5\\" fill=\\"#26296b\\"/><text x=\\"30\\" y=\\"41\\" font-size=\\"12\\" font-weight=\\"900\\" fill=\\"#e4572e\\" stroke=\\"none\\" font-family=\\"Inter, sans-serif\\">4</text>", "listen-4": """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
