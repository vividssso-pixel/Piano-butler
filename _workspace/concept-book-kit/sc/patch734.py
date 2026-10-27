import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build BO (board call 26, the first Grade 6 room): Hear and Sing, Grade 6. The Grade 6 practical aural tests (Manual of
# Syllabuses 2026, section 21, read 28 Oct): the keynote, then any interval of the major OR HARMONIC MINOR scale straight after
# it, sung and named; any major triad, root position or inverted, within an octave: its position recognised; the higher or the
# lower part of a two-part progression of FOUR successive intervals within an octave from middle C, sung from memory; perfect
# and plagal cadences in a major key as they occur in a short piece, the tonic chord first sounded. Tests are played twice.
# The house gains the Grade 6 floor (floor 7; its rooms appear as they are built), two more floor styles for floors 8 and 9,
# and the Home's floor marks for Grades 6 to 8.

rep("""const LISTEN_5_DRILL = { id: 'listen-5', label: 'Hear and Sing, Grade 5', noPrint: true };   // Build AZ""",
    """const LISTEN_5_DRILL = { id: 'listen-5', label: 'Hear and Sing, Grade 5', noPrint: true };   // Build AZ
const LISTEN_6_DRILL = { id: 'listen-6', label: 'Hear and Sing, Grade 6', noPrint: true };   // Build BO""")
rep("""  { id: 'listen-5', label: 'Hear and Sing, Grade 5', concept: LISTEN_5_DRILL, track: 'start' },   // Build AZ""",
    """  { id: 'listen-5', label: 'Hear and Sing, Grade 5', concept: LISTEN_5_DRILL, track: 'start' },   // Build AZ
  { id: 'listen-6', label: 'Hear and Sing, Grade 6', concept: LISTEN_6_DRILL, track: 'start' },   // Build BO""")
rep("""'listen-5': '듣고 부르기, Grade 5'""", """'listen-5': '듣고 부르기, Grade 5', 'listen-6': '듣고 부르기, Grade 6'""")
rep("""'listen-5': ['listen-4']""", """'listen-5': ['listen-4'], 'listen-6': ['listen-5']""")
rep("""'listen-5': ['Hear & sing 5', '듣기 5']""", """'listen-5': ['Hear & sing 5', '듣기 5'], 'listen-6': ['Hear & sing 6', '듣기 6']""")
rep("""  'listen-5': 'aural ear grade 5""", """  'listen-6': 'aural ear grade 6 interval harmonic minor major scale keynote minor third minor sixth triad position root first second inversion two-part four intervals upper lower part cadence perfect plagal phrase ending',
  'listen-5': 'aural ear grade 5""")
rep("""id === 'listen-4' || id === 'listen-5') return 'aural';""", """id === 'listen-4' || id === 'listen-5' || id === 'listen-6') return 'aural';""")
# the house: the Grade 6 floor under the attic; floors 8 and 9 get their own wallpaper, floor and lamp
rep("""  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true,""",
    """  { ids: ['listen-6', 'scales-6', 'arps-6', 'harmony-6'], en: ['Grade 6', 'Your ears, scales, arpeggios and chord walks, and chords and cadences.'], ko: ['Grade 6', '귀, 스케일, 아르페지오와 화음 진행, 그리고 화음과 종지.'] },   // Build BO: the Grade 6 floor (call 26); its rooms appear as they are built
  { ids: ['piano-story', 'pitch-range', 'composers', 'styles'], stories: true,""")
rep("""  { wp: 'regency', fl: 'chequer', lamp: 'chandelier' }  // 7 Know the music
];""", """  { wp: 'regency', fl: 'chequer', lamp: 'chandelier' },  // 7 Know the music
  { wp: 'sprig', fl: 'herring', lamp: 'lantern' },      // 8 (Build BO: Grades 6 to 8 add three floors)
  { wp: 'trellis', fl: 'tiles', lamp: 'pendant' }       // 9
];""")
rep("""const HOME_FLOOR_NAME = { G: 'Beginner', P1: 'Prelim – Grade 1', '23': 'Grades 2–3', '4': 'Grade 4', '5': 'Grade 5' };""",
    """const HOME_FLOOR_NAME = { G: 'Beginner', P1: 'Prelim – Grade 1', '23': 'Grades 2–3', '4': 'Grade 4', '5': 'Grade 5', '6': 'Grade 6', '7': 'Grade 7', '8': 'Grade 8' };   // Build BO: Grades 6 to 8""")

CH = r'''
// ─── Chapter: Hear and Sing, Grade 6 (Build BO, 2026-10-28; board call 26, the first Grade 6 room) ───
// The Grade 6 aural tests (Manual 2026, section 21), one step each, every step with an easier rung first (call 25: the aural
// ladder): the keynote, then any interval of the major or harmonic minor scale (one scale first, then either); a major triad's
// position (one note at a time first); four intervals in two parts, one part sung (the first two intervals first); perfect or
// plagal at the end of a short piece, the tonic chord first (the last two chords first). Every test is heard twice.
const L6_SC = { maj: [0, 2, 4, 5, 7, 9, 11, 12], hm: [0, 2, 3, 5, 7, 8, 11, 12] };
const L6_IVS = [['M2', 2, 2], ['m3', 3, 3], ['M3', 3, 4], ['P4', 4, 5], ['P5', 5, 7], ['m6', 6, 8], ['M6', 6, 9], ['M7', 7, 11], ['P8', 8, 12]];   // [id, number, semitones]
const L6_IVN = { M2: ['major 2nd', '장2도'], m3: ['minor 3rd', '단3도'], M3: ['major 3rd', '장3도'], P4: ['perfect 4th', '완전4도'], P5: ['perfect 5th', '완전5도'], m6: ['minor 6th', '단6도'], M6: ['major 6th', '장6도'], M7: ['major 7th', '장7도'], P8: ['perfect octave', '완전8도'] };
const l6IvName = (id) => t(L6_IVN[id][0], L6_IVN[id][1]);
const l6Iv = (mode, n) => L6_IVS.find(x => x[1] === n && x[2] === L6_SC[mode][n - 1]);   // from the keynote to degree n
const l6Mode = (m) => (m === 'maj' ? t('major', '장음계') : t('harmonic minor', '화성 단음계'));
// spelling: the keynote's name by pitch class (minor keys as they are written: C♯, F♯, G♯ minor), then each degree's letter
const L6_KN = { maj: ['C', 'D♭', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'A♭', 'A', 'B♭', 'B'], hm: ['C', 'C♯', 'D', 'E♭', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'B♭', 'B'] };
const L6_NAT = { C: 0, D: 2, E: 4, F: 5, G: 7, A: 9, B: 11 };
const l6Spell = (kName, semis, n) => { const L = 'CDEFGAB', l0 = L.indexOf(kName[0]), k0 = (L6_NAT[kName[0]] + (kName.includes('♯') ? 1 : kName.includes('♭') ? -1 : 0) + 12) % 12;
  const letter = L[(l0 + n - 1) % 7], d = ((k0 + semis - L6_NAT[letter]) % 12 + 18) % 12 - 6; return letter + ({ '-2': '𝄫', '-1': '♭', 0: '', 1: '♯', 2: '𝄪' })[d]; };
const l6Deg = (k, mode, n) => l6Spell(L6_KN[mode][spPc(k)], L6_SC[mode][n - 1], n);

// ── step 1: the keynote, then any interval of the major or harmonic minor scale: sing it, then name it ──
function L6IvPad({ onResult, fixed, keys = L5_KEYS }) {
  const [set, setSet] = useState('hm'), [x, setX] = useState(fixed || { k: 0, mode: 'hm', n: 6 }), [heard, setHeard] = useState(false), [ans, setAns] = useState(null), [run, setRun] = useState(0);
  const iv = l6Iv(x.mode, x.n), d = iv[2];
  const play = () => { setHeard(true); l4PlayIv(x.k, d); };
  const make = (st) => { let y, g = 0; do { y = { k: pick(keys), mode: st === 'both' ? pick(['maj', 'hm']) : st, n: pick([2, 3, 4, 5, 6, 7, 8]) }; } while (y.k === x.k && y.n === x.n && y.mode === x.mode && g++ < 10); return y; };
  const fresh = () => { const y = make(set); setX(y); setAns(null); setHeard(true); l4PlayIv(y.k, l6Iv(y.mode, y.n)[2]); };
  const rung = (st) => { setSet(st); setX(make(st)); setAns(null); setHeard(false); };
  const say = (id) => { if (!heard || ans) return; setAns(id); const ok = id === iv[0]; setRun(r => (ok ? r + 1 : 0)); if (onResult) onResult({ ok }); };
  const sc = L6_SC[x.mode].map(s => x.k + s), lit = {}; if (ans) { lit[x.k] = 'pale'; lit[x.k + d] = ans === iv[0] ? 'good' : 'cor'; }
  const minorNote = x.mode === 'hm' ? t(' In the harmonic minor the 3rd and the 6th are minor; the rest are as in the major.', ' 화성 단음계에서는 3도와 6도가 단음정, 나머지는 장음계와 같아요.') : '';
  return (
    <div className="try-box" style={actBox} data-l6="iv">
      <div style={actTitle}>{t('Major or minor: any interval', '장조든 단조든: 어떤 음정이든')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>먼저 <b>으뜸음</b>, 그다음 그 음계의 다른 음(두 번). 이제 음계는 <b>장음계</b>일 수도, <b>화성 단음계</b>일 수도 있어요. 부르고 <b>온전한 이름</b>을 말해요. 단음계에서는 <b>3도와 6도가 반음 낮아요</b>: 단3도, 단6도.</>
        : <>First <b>the keynote</b>, then another note of its scale (twice). Now the scale can be <b>major</b> or <b>harmonic minor</b>. Sing it, then give its <b>full name</b>. In the minor, <b>the 3rd and the 6th are a semitone lower</b>: a minor 3rd, a minor 6th.</>}</div>
      {!fixed && spChips([['maj', t('Major only', '장음계만')], ['hm', t('Minor only', '단음계만')], ['both', t('Either, like the test', '둘 다, 시험처럼')]], set, rung)}
      <SpKb lo={Math.min(0, x.k)} hi={Math.max(14, x.k + 12)} W={24} H={74} lit={lit} names={ans ? Object.fromEntries(sc.map((s, j) => [s, String(j + 1)])) : { [x.k]: '1' }} label={t('The keynote and the scale', '으뜸음과 음계')}/>
      {heard && <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,marginTop:10}}>{L6_IVS.map(([id]) => <button key={id} className={'choice-btn' + (!ans ? '' : id === iv[0] ? ' good' : id === ans ? ' bad' : '')} onClick={() => say(id)} style={{padding:'10px 2px',fontSize:13.5,fontWeight:900,lineHeight:1.15}}>{l6IvName(id)}</button>)}</div>}
      {lwMsg(!heard ? t('Tap ▶ to hear the keynote and the note.', '▶를 누르면 으뜸음과 음이 나와요.') : ans ? (ans === iv[0] ? t('Yes: a ' + L6_IVN[iv[0]][0] + ', degree ' + x.n + ' of the ' + (x.mode === 'maj' ? 'major' : 'harmonic minor') + '. ' + (run > 1 ? run + ' in a row.' : ''), '맞아요: ' + L6_IVN[iv[0]][1] + ', ' + l6Mode(x.mode) + '의 ' + x.n + '번 음. ' + (run > 1 ? run + '번 연속.' : ''))
        : t('It was a ' + L6_IVN[iv[0]][0] + ', degree ' + x.n + ' of the ' + (x.mode === 'maj' ? 'major.' : 'harmonic minor.') + minorNote, L6_IVN[iv[0]][1] + '였어요. ' + l6Mode(x.mode) + '의 ' + x.n + '번 음.' + minorNote)) : t('Sing it, then name it.', '부르고, 이름을 말해요.'), ans ? (ans === iv[0] ? BK.green : BK.coral) : undefined)}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={heard && !fixed ? fresh : play}>{!heard ? t('▶ Keynote, then the note', '▶ 으뜸음, 그다음 음') : fixed ? t('♪ Again', '♪ 다시') : t('▶ Another', '▶ 다른 것')}</button>
        {heard && !fixed && <button className="ghost-btn" style={lwBtn} onClick={play}>{t('♪ Again', '♪ 다시')}</button>}
        {ans && <button className="ghost-btn" style={lwBtn} onClick={() => spPlay(sc.map((s, j) => ({ at: j * 0.55, keys: [s], len: 0.5 })), 100)}>{t('♪ Its scale', '♪ 그 음계')}</button>}
      </>)}
    </div>
  );
}

// ── step 2: a triad, root position or inverted: which position? The 4th tells: none, on top, or at the bottom ──
const L6_TQ = { maj: [0, 4, 7], min: [0, 3, 7], dim: [0, 3, 6] };
const L6_QN = { maj: ['major', '장3화음'], min: ['minor', '단3화음'], dim: ['diminished', '감3화음'] };
const l6Tri = (r, q, inv) => { const n = L6_TQ[q].map(x => r + x); for (let j = 0; j < inv; j++) n.push(n.shift() + 12); while (n[0] > 7) n.forEach((_, i) => { n[i] -= 12; }); while (n[0] < -4) n.forEach((_, i) => { n[i] += 12; }); return n; };
const l6Gap = (a, b) => (b - a === 5 ? 4 : 3);   // the gap between neighbouring notes: a 3rd, or (5 semitones) a 4th
function L6Gaps({ n, w = 260 }) {   // the three notes with the gaps between them; the 4th in coral
  const g = [l6Gap(n[0], n[1]), l6Gap(n[1], n[2])], box = (x) => <span style={{display:'inline-flex',alignItems:'center',justifyContent:'center',minWidth:30,height:30,borderRadius:15,border:'2px solid #26296b',fontWeight:900,fontSize:14,color:BK.ink,background:'#fff'}}>{l4Let(x)}</span>;
  const gap = (v) => <span style={{fontSize:13,fontWeight:900,color:v === 4 ? BK.coral : BK.muted,padding:'0 4px',whiteSpace:'nowrap'}}>{v === 4 ? t('— 4th —', '— 4도 —') : t('— 3rd —', '— 3도 —')}</span>;
  return <div style={{display:'flex',alignItems:'center',justifyContent:'center',flexWrap:'wrap',gap:2,maxWidth:w,margin:'6px auto 0'}}>{box(n[0])}{gap(g[0])}{box(n[1])}{gap(g[1])}{box(n[2])}</div>;
}
const l6PosWord = (inv) => t(L4_INVW[inv][0], L4_INVW[inv][1]);
const l6PosWhy = (inv) => [t('No 4th: root position.', '4도가 없어요: 기본형.'), t('The 4th on top: first inversion.', '4도가 위에: 첫째 자리바꿈.'), t('The 4th at the bottom: second inversion.', '4도가 아래에: 둘째 자리바꿈.')][inv];
function L6PosPad({ onResult, fixed, quals = ['maj'] }) {
  const [x, setX] = useState(fixed || { r: 0, q: quals[0], inv: 1 }), [heard, setHeard] = useState(false), [pq, setPq] = useState(null), [pi, setPi] = useState(null), [res, setRes] = useState(null);
  const n = l6Tri(x.r, x.q, x.inv), many = quals.length > 1;
  const play = () => { setHeard(true); l4PlayTri(n); };
  const fresh = () => { let y, g = 0; do { const q = pick(quals); y = { r: Math.floor(Math.random() * 12), q, inv: q === 'dim' ? 0 : pick([0, 1, 2]) }; } while (y.r === x.r && y.inv === x.inv && g++ < 10);
    setX(y); setPq(null); setPi(null); setRes(null); setHeard(true); l4PlayTri(l6Tri(y.r, y.q, y.inv)); };
  const finish = (q, inv) => { const ok = (!many || q === x.q) && (x.q === 'dim' || inv === x.inv); const r = { ok }; setRes(r); if (onResult) onResult(r); };
  const pickQ = (q) => { if (!heard || res) return; setPq(q); if (q === 'dim') finish(q, 0); else if (pi != null) finish(q, pi); };
  const pickI = (inv) => { if (!heard || res || pq === 'dim') return; setPi(inv); if (!many || pq) finish(pq || x.q, inv); };
  const lit = {}; if (res) n.forEach(k => { lit[k] = res.ok ? 'good' : 'cor'; });
  const name = l4Let(x.r) + ' ' + L6_QN[x.q][0], nameK = l4Let(x.r) + ' ' + L6_QN[x.q][1];
  const cls = (on, right) => 'choice-btn' + (!res ? (on ? ' active' : '') : right ? ' good' : on ? ' bad' : '');
  return (
    <div className="try-box" style={actBox} data-l6="pos">
      <div style={actTitle}>{many ? t('Which triad, and which position?', '어떤 3화음, 어느 자리?') : t('Which position is the triad?', '3화음은 어느 자리?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>{many ? <>장3화음이나 단3화음{quals.includes('dim') ? <>, 또는 기본형의 감3화음</> : null}이 울려요(두 번). 먼저 어떤 3화음인지, 그다음 <b>자리</b>를 말해요.</> : <>장3화음이 울려요(두 번). <b>기본형</b>일까요, <b>첫째 자리바꿈</b>일까요, <b>둘째 자리바꿈</b>일까요?</>} 열쇠는 <b>4도</b>: 없으면 기본형, <b>위에</b> 있으면 첫째 자리바꿈, <b>아래에</b> 있으면 둘째 자리바꿈. 둘째 자리바꿈은 아래가 비어 있어 움직이고 싶은 소리예요.</>
        : <>{many ? <>A major or minor triad{quals.includes('dim') ? <>, or a diminished triad in root position,</> : null} sounds (twice). Say which triad, then its <b>position</b>.</> : <>A major triad sounds (twice). Is it in <b>root position</b>, <b>first inversion</b> or <b>second inversion</b>?</>} The key is <b>the 4th</b>: none, root position; <b>on top</b>, first inversion; <b>at the bottom</b>, second inversion. Second inversion sounds open underneath, as if it wants to move.</>}</div>
      <SpKb lo={-5} hi={16} W={24} H={74} lit={lit} names={res ? Object.fromEntries(n.map(k => [k, l4Let(k)])) : { 0: 'C' }} label={t('The triad', '3화음')}/>
      {res && <L6Gaps n={n}/>}
      {heard && many && <div style={{display:'grid',gridTemplateColumns:'repeat(' + quals.length + ',minmax(0,1fr))',gap:6,marginTop:10}}>{quals.map(q => <button key={q} className={cls(pq === q, q === x.q)} onClick={() => pickQ(q)} style={{padding:'10px 2px',fontSize:14,fontWeight:900}}>{t(L6_QN[q][0][0].toUpperCase() + L6_QN[q][0].slice(1), L6_QN[q][1])}</button>)}</div>}
      {heard && <div style={{display:'grid',gridTemplateColumns:'repeat(3,minmax(0,1fr))',gap:6,marginTop:8,opacity:pq === 'dim' ? 0.4 : 1}}>{[0, 1, 2].map(inv => <button key={inv} disabled={pq === 'dim'} className={cls(pi === inv, x.q !== 'dim' && inv === x.inv)} onClick={() => pickI(inv)} style={{padding:'10px 2px',fontSize:13.5,fontWeight:900,lineHeight:1.15}}>{t(L4_INVW[inv][0][0].toUpperCase() + L4_INVW[inv][0].slice(1), L4_INVW[inv][1])}</button>)}</div>}
      {lwMsg(!heard ? t('Tap ▶ to hear the triad.', '▶를 누르면 3화음이 나와요.') : res ? (res.ok ? t('Yes: ' + name + ', ' + L4_INVW[x.inv][0] + '. ', '맞아요: ' + nameK + ', ' + L4_INVW[x.inv][1] + '. ') : t('It was ' + name + ', ' + L4_INVW[x.inv][0] + '. ', nameK + ', ' + L4_INVW[x.inv][1] + '였어요. ')) + (x.q === 'dim' ? t('Two 3rds, no 4th.', '3도 둘, 4도 없음.') : l6PosWhy(x.inv))
        : many && !pq ? t('Which triad first?', '먼저 어떤 3화음?') : t('Listen for the 4th: which position?', '4도를 들어 봐요: 어느 자리?'), res ? (res.ok ? BK.green : BK.coral) : undefined)}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={heard && !fixed ? fresh : play}>{!heard ? t('▶ Play a triad', '▶ 3화음 듣기') : fixed ? t('♪ Again', '♪ 다시') : t('▶ Another', '▶ 다른 것')}</button>
        {heard && !fixed && <button className="ghost-btn" style={lwBtn} onClick={play}>{t('♪ Again', '♪ 다시')}</button>}
        {heard && <button className="ghost-btn" style={lwBtn} onClick={() => spPlay(n.map((k, j) => ({ at: j * 0.8, keys: [k], len: 0.75 })).concat([{ at: 2.6, keys: n, len: 1.6 }]), 90)}>{t('♪ One at a time, from the bottom', '♪ 아래부터 하나씩')}</button>}
      </>)}
    </div>
  );
}

// ── step 3: a two-part phrase, sung one part at a time: the higher (the bird's) or the lower (the turtle's) ──
// a phrase is { hi, lo }: [[key, beats], ...] each; note against note when every note is one beat. rungs: [[beats, [en, ko]], ...]
const l6Pairs = (prs) => ({ hi: prs.map(p => [p[1], 1]), lo: prs.map(p => [p[0], 1]) });
const ptsAt = (part) => { let b = 0; return part.map(([k, d]) => { const o = { k, at: b, d }; b += d; return o; }); };
const ptsLen = (P) => ptsAt(P.hi).reduce((m, o) => Math.max(m, o.at + o.d), 0);
const ptsPart = (P, ask, beats) => ptsAt(ask === 'hi' ? P.hi : P.lo).filter(o => o.at < beats - 1e-6);
const ptsPlay = (P, beats, bpm) => { const L = Math.min(beats, ptsLen(P)), ev = [];
  for (let r = 0; r < 2; r++) ['hi', 'lo'].forEach(h => ptsAt(P[h]).filter(o => o.at < L - 1e-6).forEach(o => ev.push({ at: r * (L + 1.5) + o.at, keys: [o.k], len: o.d * 0.95, vol: 0.13 })));
  return spPlay(ev, bpm); };
const L6_TWO = [   // four intervals in two parts, within an octave from middle C: [[low, high] x4]
  [[0, 4], [2, 5], [4, 7], [0, 4]], [[0, 7], [2, 5], [4, 7], [5, 9]], [[4, 12], [2, 11], [5, 9], [4, 7]], [[0, 12], [2, 11], [4, 9], [5, 9]],
  [[7, 11], [5, 12], [4, 12], [2, 11]], [[0, 4], [0, 5], [0, 7], [0, 4]], [[7, 12], [5, 9], [4, 7], [0, 4]], [[2, 5], [4, 7], [5, 9], [7, 11]],
  [[0, 9], [2, 7], [4, 7], [2, 11]], [[7, 11], [6, 9], [4, 11], [7, 11]], [[5, 9], [7, 10], [9, 12], [5, 12]], [[4, 7], [2, 7], [0, 9], [0, 12]],
].map(l6Pairs);
function PartsPad({ onResult, fixed, set, bpm = 60, rungs, title, note, tag = 'two' }) {
  const full = ptsLen(set[fixed ? fixed.i : 0]), R = rungs || [[full, t('All of it', '전체')]];
  const [x, setX] = useState(fixed || { i: 0, ask: 'hi' }), [rung, setRung] = useState(fixed ? R[R.length - 1][0] : R[0][0]), [heard, setHeard] = useState(false), [got, setGot] = useState(0), [miss, setMiss] = useState(0), [wrong, setWrong] = useState(null);
  const P = set[x.i], part = ptsPart(P, x.ask, rung).map(o => o.k), N = part.length, done = got >= N;
  const allK = P.hi.concat(P.lo).map(p => p[0]), lo = Math.min(0, ...allK), hi = Math.max(12, ...allK);
  const clear = () => { setGot(0); setMiss(0); setWrong(null); };
  const play = () => { setHeard(true); ptsPlay(P, rung, bpm); };
  const fresh = () => { let y, g = 0; do { y = { i: Math.floor(Math.random() * set.length), ask: Math.random() < 0.5 ? 'hi' : 'lo' }; } while (y.i === x.i && y.ask === x.ask && g++ < 10); setX(y); clear(); setHeard(true); ptsPlay(set[y.i], rung, bpm); };
  const step = (b) => { setRung(b); clear(); setHeard(false); };
  const tap = (k) => { playKey(k, 0.5); if (!heard || done) return; if (k === part[got]) { const g = got + 1; setGot(g); setWrong(null); if (g >= N && onResult) onResult({ ok: miss === 0 }); } else { setMiss(m => m + 1); setWrong(k); } };
  const lit = {}; if (done) { ptsPart(P, 'hi', rung).concat(ptsPart(P, 'lo', rung)).forEach(o => { lit[o.k] = 'pale'; }); part.forEach(k => { lit[k] = 'good'; }); } else { part.slice(0, got).forEach(k => { lit[k] = 'cor'; }); if (wrong != null) lit[wrong] = 'bad'; }
  const askW = x.ask === 'hi' ? t('the higher part', '윗성부') : t('the lower part', '아랫성부');
  return (
    <div className="try-box" style={actBox} data-l6={tag}>
      <div style={actTitle}>{title}</div>
      <div style={actNote}>{note}</div>
      {!fixed && R.length > 1 && spChips(R.map(([b, lab]) => [b, lab]), rung, step)}
      {heard && <div style={{textAlign:'center',fontSize:16,fontWeight:900,color:BK.coral,margin:'0 0 6px'}}>{x.ask === 'hi' ? t('Sing the higher part ↑', '윗성부를 불러요 ↑') : t('Sing the lower part ↓', '아랫성부를 불러요 ↓')}</div>}
      <SpKb lo={lo} hi={hi} W={hi - lo > 14 ? 26 : 32} H={84} lit={lit} names={done ? Object.fromEntries(part.map(k => [k, l4Let(k)])) : { 0: 'C' }} onTap={tap} label={t('Find the part you sang', '부른 성부 찾기')}/>
      {lwMsg(!heard ? t('Tap ▶ to hear the two parts.', '▶를 누르면 두 성부가 나와요.') : done ? t(askW.charAt(0).toUpperCase() + askW.slice(1) + ': ' + part.map(l4Let).join(', ') + '. ' + (miss ? 'Found it.' : 'First time!'), askW + ': ' + part.map(l4Let).join(', ') + '. ' + (miss ? '찾았어요.' : '한 번에!'))
        : wrong != null ? t('Not that one: sing the part again, then try.', '그 음이 아니에요: 다시 불러 보고 찾아요.') : t('Sing it, then find note ' + (got + 1) + ' of ' + N + '.', '부르고, ' + N + '음 중 ' + (got + 1) + '번째를 찾아요.'), done ? BK.green : wrong != null ? BK.coral : undefined)}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={heard && !fixed ? fresh : play}>{!heard ? t('▶ Play the two parts', '▶ 두 성부 듣기') : fixed ? t('♪ Again', '♪ 다시') : t('▶ Another', '▶ 다른 것')}</button>
        {heard && !fixed && <button className="ghost-btn" style={lwBtn} onClick={play}>{t('♪ Again', '♪ 다시')}</button>}
        {heard && !done && <button className="ghost-btn" style={lwBtn} onClick={() => spPlay(ptsPart(P, x.ask, rung).map(o => ({ at: o.at * 1.2, keys: [o.k], len: o.d * 1.1 })), 72)}>{t('♪ Just that part', '♪ 그 성부만')}</button>}
      </>)}
    </div>
  );
}
function L6TwoPad(p) { return <PartsPad set={L6_TWO} bpm={60} rungs={[[2, t('First two', '처음 둘')], [4, t('All four, like the test', '넷 모두, 시험처럼')]]} title={t('Four intervals: sing one part', '네 음정: 한 성부를 불러요')}
  note={LANG === 'ko' ? <>두 음씩 <b>네 번</b>, 두 성부로(전체를 두 번). 외워서 묻는 성부의 네 음을 부르고, 건반에서 차례로 찾아요. 윗성부는 새, 아랫성부는 거북이. 처음엔 <b>둘만</b>, 그다음 넷.</>
    : <>Two notes together, <b>four times</b>, in two parts (all of it played twice). From memory, sing the four notes of the part asked for, then find them on the keys in order. The higher part is the bird's, the lower the turtle's. First <b>just two</b>, then all four.</>} {...p}/>; }

// ── step 4: a short piece in a major key, the tonic chord first: does it end perfect (V–I) or plagal (IV–I)? ──
const CAD_N = { perfect: ['perfect', '정격종지', 'V → I'], plagal: ['plagal', '변격종지', 'IV → I'], interrupted: ['interrupted', '거짓종지', 'V → vi'], imperfect: ['imperfect', '반종지', '… → V'] };
const cadName = (c) => t(CAD_N[c][0], CAD_N[c][1]);
const cadCap = (c) => t(CAD_N[c][0][0].toUpperCase() + CAD_N[c][0].slice(1), CAD_N[c][1]);
const CAD_PC = { I: [0, 4, 7], ii: [2, 5, 9], iii: [4, 7, 11], IV: [5, 9, 0], V: [7, 11, 2], vi: [9, 0, 4] };
const CAD_TPL = {   // four bars: two chords a bar, then the last chord held; the last two chords make the cadence
  perfect: [['I', 'IV', 'V', 'I', 'ii', 'V', 'I'], ['I', 'vi', 'IV', 'V', 'I', 'V', 'I'], ['I', 'V', 'vi', 'IV', 'ii', 'V', 'I']],
  plagal: [['I', 'V', 'vi', 'V', 'I', 'IV', 'I'], ['I', 'IV', 'V', 'vi', 'I', 'IV', 'I'], ['I', 'vi', 'ii', 'V', 'I', 'IV', 'I']],
  interrupted: [['I', 'IV', 'I', 'V', 'ii', 'V', 'vi'], ['I', 'vi', 'IV', 'I', 'IV', 'V', 'vi'], ['I', 'V', 'vi', 'IV', 'I', 'V', 'vi']],
  imperfect: [['I', 'IV', 'V', 'I', 'vi', 'ii', 'V'], ['I', 'V', 'vi', 'IV', 'I', 'IV', 'V'], ['I', 'vi', 'ii', 'V', 'vi', 'I', 'V']],
};
const CAD_KEYS = [0, 7, 2, 5, -2, 9];   // C, G, D, F, B♭ and A major
const CAD_KN = { 0: 'C', 7: 'G', 2: 'D', 5: 'F', '-2': 'B♭', 9: 'A' };
// close-position chords in the right hand, each moving as little as it can from the one before; the root in the bass
const cadVoice = (key, seq) => { let prev = null;
  return seq.map((rn) => { const pcs = CAD_PC[rn].map(x => (x + key + 120) % 12), cands = [];
    for (let lo = -3; lo <= 9; lo++) { if (!pcs.includes(spPc(lo))) continue; const v = [lo], used = [spPc(lo)];
      for (let c = lo + 1; v.length < 3 && c < lo + 12; c++) if (pcs.includes(spPc(c)) && !used.includes(spPc(c))) { v.push(c); used.push(spPc(c)); } cands.push(v); }
    let v; if (!prev) v = cands.find(w => spPc(w[2]) === spPc(key) && w[2] >= 7) || cands[0];
    else v = cands.reduce((b, w) => { const m = w.reduce((a, y, i) => a + Math.abs(y - prev[i]), 0), mb = b.reduce((a, y, i) => a + Math.abs(y - prev[i]), 0); return m < mb ? w : b; });
    prev = v; let b = spPc(pcs[0]) - 24; while (b < -20) b += 12; return { up: v, bass: b }; }); };
// the tonic chord first, then the phrase (or, the easier rung, just its last two chords)
const cadPlay = (x, end, bpm = 72) => { const seq = CAD_TPL[x.cad][x.ti], V = cadVoice(x.key, seq), ton = cadVoice(x.key, ['I'])[0], ev = [{ at: 0, keys: [ton.bass].concat(ton.up), len: 3, vol: 0.1 }];
  const from = end ? 5 : 0; let at = 4.5; for (let j = from; j < 7; j++) { const L = j === 6 ? 4 : 2; ev.push({ at, keys: [V[j].bass].concat(V[j].up), len: L, vol: 0.1 }); at += L; }
  return spPlay(ev, bpm); };
function CadChart({ x, end, show = true }) {   // the phrase's chords, bar by bar; the cadence (the last two) in coral
  const seq = CAD_TPL[x.cad][x.ti], bars = [[0, 1], [2, 3], [4, 5], [6]].filter(b => !end || b.some(j => j >= 5));
  return <div style={{display:'flex',justifyContent:'center',alignItems:'stretch',flexWrap:'wrap',margin:'8px auto 0',border:'1.5px solid #26296b',borderRadius:4,maxWidth:360,background:'#fff'}}>
    {bars.map((b, bi) => <div key={bi} style={{flex:'1 1 0',display:'flex',justifyContent:'space-around',alignItems:'center',minWidth:62,padding:'8px 4px',borderLeft:bi ? '1.5px solid #26296b' : 'none'}}>
      {b.filter(j => !end || j >= 5).map(j => <span key={j} style={{fontFamily:LB_SERIF,fontSize:17,fontWeight:900,color:j >= 5 && show ? BK.coral : BK.ink}}>{show || j < 5 ? seq[j] : '?'}</span>)}</div>)}
  </div>;
}
function CadPad({ onResult, fixed, cads = ['perfect', 'plagal'], tag = 'cad' }) {
  const [x, setX] = useState(fixed || { key: 0, cad: cads[0], ti: 0 }), [end, setEnd] = useState(!fixed), [heard, setHeard] = useState(false), [ans, setAns] = useState(null), [run, setRun] = useState(0);
  const play = () => { setHeard(true); cadPlay(x, end); };
  const make = () => { let y, g = 0; do { y = { key: pick(CAD_KEYS), cad: pick(cads), ti: Math.floor(Math.random() * 3) }; } while (y.cad === x.cad && y.ti === x.ti && g++ < 10); return y; };
  const fresh = () => { const y = make(); setX(y); setAns(null); setHeard(true); cadPlay(y, end); };
  const rung = (e) => { setEnd(e); setX(make()); setAns(null); setHeard(false); };
  const say = (c) => { if (!heard || ans) return; setAns(c); const ok = c === x.cad; setRun(r => (ok ? r + 1 : 0)); if (onResult) onResult({ ok }); };
  const seq = CAD_TPL[x.cad][x.ti];
  return (
    <div className="try-box" style={actBox} data-l6={tag}>
      <div style={actTitle}>{cads.length === 2 ? t('Perfect or plagal?', '정격종지? 변격종지?') : t('Which cadence?', '어떤 종지?')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>먼저 <b>으뜸화음</b>(집), 그다음 장조의 짧은 곡. 끝의 두 화음이 <b>종지</b>예요. <b>정격종지</b>는 V에서 I로: 문이 닫히듯 단단히 끝나요. <b>변격종지</b>는 IV에서 I로: 더 부드럽게 끝나요.{cads.includes('interrupted') ? <> <b>거짓종지</b>는 V에서 vi로: 집에 올 줄 알았는데 깜짝!</> : null}{cads.includes('imperfect') ? <> <b>반종지</b>는 V에서 멈춰요: 아직 안 끝난 쉼표.</> : null}</>
        : <>First <b>the tonic chord</b> (home), then a short piece in a major key. The last two chords are the <b>cadence</b>. <b>Perfect</b> is V to I: a firm, closed ending. <b>Plagal</b> is IV to I: a softer ending.{cads.includes('interrupted') ? <> <b>Interrupted</b> is V to vi: you expect home, and get a surprise.</> : null}{cads.includes('imperfect') ? <> <b>Imperfect</b> stops on V: a comma, not finished.</> : null}</>}</div>
      {!fixed && spChips([[true, t('Just the ending', '끝만')], [false, t('The whole piece, like the test', '곡 전체, 시험처럼')]], end, rung)}
      {ans ? <CadChart x={x} end={end}/> : <div style={{textAlign:'center',fontSize:13.5,fontWeight:800,color:BK.muted,margin:'6px 0'}}>{CAD_KN[x.key]}{t(' major', '장조')} · {end ? t('the tonic chord, then the last two chords', '으뜸화음, 그다음 마지막 두 화음') : t('the tonic chord, then four bars', '으뜸화음, 그다음 네 마디')}</div>}
      {heard && <div style={{display:'grid',gridTemplateColumns:'repeat(' + (cads.length > 2 ? 2 : cads.length) + ',minmax(0,1fr))',gap:8,marginTop:10}}>{cads.map(c => <button key={c} className={'choice-btn' + (!ans ? '' : c === x.cad ? ' good' : c === ans ? ' bad' : '')} onClick={() => say(c)} style={{padding:'9px 4px',fontSize:15,fontWeight:900,lineHeight:1.2}}>{cadCap(c)}<div style={{fontSize:12,fontWeight:800,opacity:0.8}}>{CAD_N[c][2]}</div></button>)}</div>}
      {lwMsg(!heard ? t('Tap ▶: home first, then the piece.', '▶를 눌러요: 먼저 집, 그다음 곡.') : ans ? (ans === x.cad ? t('Yes: ' + CAD_N[x.cad][0] + ', ' + seq[5] + ' to ' + seq[6] + '. ' + (run > 1 ? run + ' in a row.' : ''), '맞아요: ' + CAD_N[x.cad][1] + ', ' + seq[5] + '에서 ' + seq[6] + '. ' + (run > 1 ? run + '번 연속.' : ''))
        : t('It was ' + CAD_N[x.cad][0] + ': ' + seq[5] + ' to ' + seq[6] + '.', CAD_N[x.cad][1] + '였어요: ' + seq[5] + '에서 ' + seq[6] + '.')) : t('Listen to the last two chords: which ending?', '마지막 두 화음을 들어 봐요: 어떤 끝?'), ans ? (ans === x.cad ? BK.green : BK.coral) : undefined)}
      {lwRow(<>
        <button className="ghost-btn" style={lwBtn} onClick={heard && !fixed ? fresh : play}>{!heard ? t('▶ Home, then the piece', '▶ 집, 그다음 곡') : fixed ? t('♪ Again', '♪ 다시') : t('▶ Another', '▶ 다른 것')}</button>
        {heard && !fixed && <button className="ghost-btn" style={lwBtn} onClick={play}>{t('♪ Again', '♪ 다시')}</button>}
        {heard && !ans && <button className="ghost-btn" style={lwBtn} onClick={() => { const ton = cadVoice(x.key, ['I'])[0]; spPlay([{ at: 0, keys: [ton.bass].concat(ton.up), len: 2, vol: 0.1 }], 72); }}>{t('♪ Home chord', '♪ 집 화음')}</button>}
      </>)}
    </div>
  );
}
const L6CadPad = (p) => <CadPad cads={['perfect', 'plagal']} {...p}/>;

// ── make: my own four bars, and the ending they make (call 25: one thing to make in every room) ──
const CM_CH = ['I', 'ii', 'IV', 'V', 'vi'];
const cmEnding = (a, b) => (a === 'V' && b === 'I' ? 'perfect' : a === 'IV' && b === 'I' ? 'plagal' : a === 'V' && b === 'vi' ? 'interrupted' : b === 'V' ? 'imperfect' : null);
function CadMaker() {
  const T = useSpTimers();
  const [key, setKey] = useState(0), [seq, setSeq] = useState(['I', 'IV', 'V', 'I', 'ii', 'V', 'I']), [sel, setSel] = useState(6), [at, setAt] = useState(-1);
  const end = cmEnding(seq[5], seq[6]);
  const playChord = (rn) => { const v = cadVoice(key, [rn])[0]; spPlay([{ at: 0, keys: [v.bass].concat(v.up), len: 1.6, vol: 0.1 }], 72); };
  const put = (rn) => { setSeq(q => q.map((y, j) => (j === sel ? rn : y))); playChord(rn); if (sel < 6) setSel(sel + 1); };
  const playAll = () => { T.clear(); const V = cadVoice(key, seq), ev = []; let b = 0; V.forEach((v, j) => { const L = j === 6 ? 4 : 2; ev.push({ at: b, keys: [v.bass].concat(v.up), len: L, vol: 0.1 }); b += L; });
    const r = spPlay(ev, 80); if (!r) return; let bb = 0; seq.forEach((_, j) => { const at0 = bb; T.at(r.ms(at0), () => setAt(j)); bb += j === 6 ? 4 : 2; }); T.at(r.ms(bb + 0.5), () => setAt(-1)); };
  const surprise = () => { const q = ['I'].concat(Array.from({ length: 4 }, () => pick(CM_CH))).concat([seq[5], seq[6]]); setSeq(q); };
  const slot = (j) => <button key={j} onClick={() => setSel(j)} aria-pressed={sel === j} style={{minWidth:36,minHeight:44,padding:'4px 2px',borderRadius:8,border:sel === j ? '2.5px solid ' + BK.coral : '1.5px solid rgba(38,41,107,0.35)',background:at === j ? BK.coral : '#fff',color:at === j ? '#fff' : j >= 5 && end ? BK.coral : BK.ink,fontFamily:LB_SERIF,fontSize:18,fontWeight:900,cursor:'pointer'}}>{seq[j]}</button>;
  return (
    <div className="try-box" style={actBox} data-mk="cad">
      <div style={actTitle}>{t('Make your own ending', '나만의 끝 만들기')}</div>
      <div style={actNote}>{LANG === 'ko' ? <>네 마디를 내 화음으로 채워요. 칸을 누르고 아래 화음을 골라요. 마지막 두 칸이 <b>종지</b>: 어떤 끝이 되는지 바로 이름이 나와요. ▶로 들어 봐요.</>
        : <>Fill four bars with your own chords. Tap a box, then a chord below. The last two boxes are the <b>cadence</b>: its name shows as soon as you make one. Tap ▶ to hear it.</>}</div>
      {spChips(CAD_KEYS.slice(0, 4).map(k => [k, CAD_KN[k] + t(' major', '장조')]), key, (k) => { T.clear(); setAt(-1); setKey(k); })}
      <div style={{display:'flex',justifyContent:'center',flexWrap:'nowrap',gap:0,margin:'4px auto 8px',border:'1.5px solid #26296b',borderRadius:6,background:'#fffefa',width:'fit-content',maxWidth:'100%'}}>
        {[[0, 1], [2, 3], [4, 5], [6]].map((b, bi) => <div key={bi} style={{display:'flex',gap:4,padding:'8px 4px',borderLeft:bi ? '1.5px solid #26296b' : 'none'}}>{b.map(slot)}</div>)}
      </div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap'}}>{CM_CH.map(rn => <button key={rn} className="chip" onClick={() => put(rn)} style={{minWidth:48,minHeight:44,fontFamily:LB_SERIF,fontSize:17,fontWeight:900}}>{rn}</button>)}</div>
      {spMsg(end ? t(seq[5] + ' → ' + seq[6] + ': ' + (/^[aeiou]/.test(CAD_N[end][0]) ? 'an ' : 'a ') + CAD_N[end][0] + ' cadence.', seq[5] + ' → ' + seq[6] + ': ' + CAD_N[end][1] + '.') : t('The last two chords make no named cadence yet: try V then I.', '마지막 두 화음은 아직 이름 있는 종지가 아니에요: V 다음 I을 해 봐요.'), end ? BK.coral : BK.muted)}
      <div style={{display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap',marginTop:8}}>
        <button className="ghost-btn" style={spBtn} onClick={playAll}>{t('▶ Play my four bars', '▶ 내 네 마디 듣기')}</button>
        <button className="ghost-btn" style={spBtn} onClick={surprise}>{t('Mix up bars 1 to 3', '1~3마디 섞기')}</button>
      </div>
    </div>
  );
}

// ── the pictures on paper ──
const l6PicIv = () => lsRawPic([0, 1, 2, 3, 4, 5, 6, 7].map(i => lsCircleSvg(6 + i * 9.5, 38 - i * 4.4, 4.6, i === 2 || i === 5 ? 'play' : 'beat', String(i + 1))).join(''), [0, 0, 84, 44]);
const l6PicPos = () => lsRawPic('<ellipse cx="20" cy="34" rx="6.5" ry="4.6" transform="rotate(-20 20 34)" fill="#26296b"/><ellipse cx="20" cy="22" rx="6.5" ry="4.6" transform="rotate(-20 20 22)" fill="#26296b"/><ellipse cx="20" cy="6" rx="6.5" ry="4.6" transform="rotate(-20 20 6)" fill="#e4572e"/><path d="M32 8 L40 8 M36 8 L36 20 M32 20 L40 20" stroke="#e4572e" stroke-width="2"/><text x="44" y="18" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="#e4572e">4</text>', [0, 0, 64, 44]);
const l6PicTwo = () => lsRawPic('<path d="M6 12 L22 8 L38 12 L54 6 L70 10" fill="none" stroke="#e4572e" stroke-width="2.4"/><path d="M6 34 L22 30 L38 34 L54 26 L70 32" fill="none" stroke="#26296b" stroke-width="2.4"/>' + [6, 22, 38, 54, 70].map((x, i) => '<circle cx="' + x + '" cy="' + [12, 8, 12, 6, 10][i] + '" r="3.4" fill="#e4572e"/><circle cx="' + x + '" cy="' + [34, 30, 34, 26, 32][i] + '" r="3.4" fill="#26296b"/>').join(''), [0, 0, 76, 44]);
const l6PicCad = () => lsRawPic('<rect x="3" y="9" width="70" height="26" rx="3" fill="#fff" stroke="#26296b" stroke-width="2"/><path d="M38 9 V35" stroke="#26296b" stroke-width="2"/><text x="20" y="28" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="900" fill="#e4572e">V</text><text x="56" y="28" text-anchor="middle" font-family="Georgia, serif" font-size="14" font-weight="900" fill="#e4572e">I</text>', [0, 0, 76, 44]);
const l6ScaleRow = (mode, scr) => { const sc = L6_SC[mode]; return <div style={{width:'100%',maxWidth:520,margin:'0 auto'}}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink,marginBottom:2}}>{mode === 'maj' ? t('C major', 'C장음계') : t('C harmonic minor: 3 and 6 a semitone lower', 'C 화성 단음계: 3과 6이 반음 낮아요')}</div>
  <SpKb maxW={520} lo={0} hi={14} W={scr ? 26 : 34} H={scr ? 64 : 80} lit={Object.fromEntries(sc.map((s, j) => [s, j === 0 ? 'pale' : mode === 'hm' && (j === 2 || j === 5) ? 'cor' : null]).filter(e => e[1]))} names={Object.fromEntries(sc.map((s, j) => [s, String(j + 1)]))}/></div>; };
const l6PosStill = (scr) => <LbPic h={170}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr 1fr',gap:12,width:'100%',maxWidth:700,margin:'0 auto'}}>{[0, 1, 2].map(inv => { const n = l6Tri(0, 'maj', inv);
  return <div key={inv}><div style={{textAlign:'center',fontSize:13,fontWeight:900,color:BK.ink}}>{t('C major, ' + L4_INVW[inv][0], 'C장3화음, ' + L4_INVW[inv][1])}</div>{l4Kb(Object.fromEntries(n.map(k => [k, 'cor'])), Object.fromEntries(n.map(k => [k, l4Let(k)])), scr, -2, 16)}<L6Gaps n={n} w={230}/></div>; })}</div></LbPic>;
function PartsLines({ P, w = 420 }) {   // a two-part phrase drawn as two lines of notes: the bird's line on top, the turtle's below
  const H = ptsAt(P.hi), L = ptsAt(P.lo), len = ptsLen(P), ks = P.hi.concat(P.lo).map(p => p[0]), lo = Math.min(...ks), hi = Math.max(...ks), X = (b) => 16 + b / len * 368, Y = (k) => 96 - (k - lo) / Math.max(1, hi - lo) * 80;
  const line = (pts, c) => '<path d="' + pts.map((o, j) => (j ? 'L' : 'M') + X(o.at).toFixed(1) + ' ' + Y(o.k).toFixed(1) + ' H' + X(o.at + o.d * 0.85).toFixed(1)).join(' ') + '" fill="none" stroke="' + c + '" stroke-width="2.4"/>' + pts.map(o => '<ellipse cx="' + X(o.at).toFixed(1) + '" cy="' + Y(o.k).toFixed(1) + '" rx="6" ry="4.4" transform="rotate(-20 ' + X(o.at).toFixed(1) + ' ' + Y(o.k).toFixed(1) + ')" fill="' + c + '"/><text x="' + X(o.at).toFixed(1) + '" y="' + (Y(o.k) + (c === '#e4572e' ? -9 : 17)).toFixed(1) + '" text-anchor="middle" font-family="Inter, sans-serif" font-size="11" font-weight="900" fill="' + c + '">' + l4Let(o.k) + '</text>').join('');
  return <svg viewBox="0 0 400 112" style={{width:'100%',maxWidth:w,display:'block',margin:'0 auto'}} role="img" aria-label={t('Two parts', '두 성부')} dangerouslySetInnerHTML={{ __html: line(H, '#e4572e') + line(L, '#26296b') }}/>;
}

function l6LbPages(scr = false) {
  const ch = 'listen-6', l5c = bkChapterNo('listen-5');
  const checks4 = [[l6PicIv(), t('I sing and name any interval of the major or harmonic minor scale', '장음계나 화성 단음계의 어떤 음정이든 부르고 이름을 말해요')], [l6PicPos(), t('I hear which position a major triad is in', '장3화음이 어느 자리인지 들어요')],
    [l6PicTwo(), t('I sing the higher or the lower part of four intervals', '네 음정에서 윗성부나 아랫성부를 불러요')], [l6PicCad(), t('I hear a perfect or a plagal cadence at the end of a piece', '곡 끝의 정격종지와 변격종지를 들어요')]];
  const pen = (x) => <PenArt shapes={x.shapes} vb={x.vb} style={{width:90}}/>;
  const toc = [[t('Major or minor: any interval', '장조든 단조든: 어떤 음정이든'), 2], [t('Which position is the triad?', '3화음은 어느 자리?'), 3], [t('Four intervals: sing one part', '네 음정: 한 성부를 불러요'), 4], [t('Perfect or plagal?', '정격종지? 변격종지?'), 5], [t('My four checks', '나의 네 가지 확인'), 6]];
  const cadStill = <LbPic h={150}><div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:14,width:'100%',maxWidth:680,margin:'0 auto'}}>{[['perfect', 0], ['plagal', 1]].map(([c, ti]) => <div key={c}><div style={{textAlign:'center',fontSize:13.5,fontWeight:900,color:BK.ink}}>{cadCap(c)} · {CAD_N[c][2]}</div><CadChart x={{ key: 0, cad: c, ti }}/></div>)}</div></LbPic>;
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{t('The Grade 6 aural tests, one step each (Manual of Syllabuses, section 21): the keynote, then any interval of the major or harmonic minor scale straight after it, sung and named (Grade 5, chapter ' + l5c + ', had the major only); any major triad, root position or an inversion, within an octave: the candidate recognises its position; the higher or the lower part of a two-part progression of four successive intervals, within an octave from middle C, sung from memory; perfect and plagal cadences in a major key as they occur in a short piece, the tonic chord first sounded. Each step here starts with an easier rung, then the test as the examiner gives it. The app plays and scores the answers; whether a child sang in tune is your ear.', '6급 청음 시험을 한 단계씩(실라버스 21절): 으뜸음 다음에 바로 장음계나 화성 단음계의 어떤 음정이든 부르고 이름 말하기(5급, ' + l5c + '장은 장음계만); 기본형이나 자리바꿈의 장3화음을 한 옥타브 안에서 듣고 자리 알기; 연속된 네 음정의 두 성부 진행에서 윗성부나 아랫성부를 외워서 부르기(가운데 도부터 한 옥타브 안); 장조의 짧은 곡에서 나오는 정격종지와 변격종지 알기, 먼저 으뜸화음을 울려요. 단계마다 쉬운 한 걸음부터, 그다음 시험처럼. 앱은 듣기와 답을 맡고, 음정이 맞았는지는 선생님의 귀예요.')}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      <LbPic h={150}><div style={{width:'100%',maxWidth:420,margin:'0 auto'}}><PartsLines P={L6_TWO[2]}/></div></LbPic>
      <LbSay size={18}>{t('Your ears for Grade 6: the minor scale’s intervals too, where a triad stands, four moves in two parts, and how a piece ends.', '6급의 귀: 단음계의 음정까지, 3화음의 자리, 두 성부로 네 걸음, 그리고 곡이 끝나는 모양.')}</LbSay>
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
    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Major or minor: any interval', '장조든 단조든: 어떤 음정이든')}
      teacher={<>{t('Grade 6: you sound the keynote, then any note of its major OR harmonic minor scale straight after it (up to the octave); the child sings it, then names it in full. Played twice. New from Grade 5: the minor 3rd and the minor 6th (the major 7th is the raised leading note, the same as in the major). The first rung keeps to one scale; then either, as in the exam.', '6급: 으뜸음을 울린 다음 바로 그 장음계나 화성 단음계의 어떤 음이든(옥타브까지) 쳐요. 아이는 부르고 온전한 이름을 말해요. 두 번 들려줘요. 5급에서 새로운 것: 단3도와 단6도(장7도는 올린 이끔음이라 장음계와 같아요). 첫 걸음은 한 음계만, 그다음 시험처럼 둘 중 아무거나.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=1')}>
      <LbLive still={<LbPic h={190}><div style={{display:'grid',gap:10,width:'100%'}}>{l6ScaleRow('maj', scr)}{l6ScaleRow('hm', scr)}</div></LbPic>} live={<L6IvPad/>}/>
      <LbSay>{LANG === 'ko' ? <>음계는 같은 번호로 올라가요. 단음계에서는 <b>3과 6이 반음 낮아서</b> 단3도, 단6도. 4, 5, 8은 언제나 완전, 2와 7은 둘 다 장음정.</> : <>Both scales climb by the same numbers. In the minor, <b>3 and 6 are a semitone lower</b>: a minor 3rd, a minor 6th. 4, 5 and 8 are always perfect; 2 and 7 are major in both.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 C장음계와 C 화성 단음계를 쳐요. 같이 불러요.</>, <>선생님이 으뜸음과 다른 음을 두 번 쳐요. 그 음을 불러요.</>, <>장조였나요, 단조였나요? 번호와 온전한 이름을 말해요.</>]
        : [<>Your teacher plays C major, then C harmonic minor. Sing along.</>, <>Your teacher plays the keynote and another note, twice. Sing the note.</>, <>Major or minor? Say its number and its full name.</>]}/>
      <LbRemember>{t('Minor: 3 and 6 a semitone lower.', '단조: 3과 6이 반음 낮아요.')}</LbRemember>
    </LbPage>,
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Which position is the triad?', '3화음은 어느 자리?')}
      teacher={<>{t('Grade 6: any major triad, root position or an inversion, within an octave; the child says its position. Played twice. Listening for the 4th: root position has two 3rds; first inversion has the 4th on top; second inversion has the 4th at the bottom (open underneath, unsettled). The first rung plays the notes one at a time from the bottom.', '6급: 장3화음을 기본형이나 자리바꿈으로 한 옥타브 안에서 쳐요. 아이는 자리를 말해요. 두 번 들려줘요. 4도를 들어요: 기본형은 3도 둘; 첫째 자리바꿈은 4도가 위에; 둘째 자리바꿈은 4도가 아래에(아래가 비어 불안정해요). 첫 걸음은 아래부터 한 음씩.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=2')}>
      <LbLive still={l6PosStill(scr)} live={<L6PosPad/>}/>
      <LbSay>{LANG === 'ko' ? <>3화음의 세 음 사이에는 틈이 둘. 둘 다 3도면 <b>기본형</b>. <b>4도가 위에</b> 있으면 첫째 자리바꿈, <b>아래에</b> 있으면 둘째 자리바꿈.</> : <>A triad has two gaps between its three notes. Two 3rds: <b>root position</b>. <b>The 4th on top</b>: first inversion. <b>At the bottom</b>: second inversion.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 C장3화음을 세 자리로 쳐요. 4도가 어디 있는지 들어요.</>, <>이번엔 아무 장3화음. 아래부터 한 음씩 흥얼거려요.</>, <>어느 자리인지 말해요.</>]
        : [<>Your teacher plays C major in all three positions. Listen for where the 4th is.</>, <>Now any major triad. Hum it one note at a time from the bottom.</>, <>Say its position.</>]}/>
      <LbRemember>{t('No 4th: root. 4th on top: first. 4th at the bottom: second.', '4도 없음: 기본형. 위에: 첫째. 아래에: 둘째.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Four intervals: sing one part', '네 음정: 한 성부를 불러요')}
      teacher={<>{t('Grade 6: four intervals played one after the other in two parts, within an octave from middle C; the child sings the higher or the lower part (four notes) from memory, as asked. Played twice. One more interval than Grade 5. The first rung is the first two intervals only.', '6급: 네 음정을 차례로 두 성부로 쳐요(가운데 도부터 한 옥타브 안). 아이는 묻는 대로 윗성부나 아랫성부(네 음)를 외워서 불러요. 두 번 들려줘요. 5급보다 음정이 하나 더. 첫 걸음은 처음 두 음정만.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=3')}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:440,margin:'0 auto'}}><PartsLines P={L6_TWO[3]}/></div></LbPic>} live={<L6TwoPad/>}/>
      <LbSay>{LANG === 'ko' ? <>두 줄이 함께 가요. 위의 줄은 <b>새</b>, 아래 줄은 <b>거북이</b>. 한 줄만 눈으로 따라가듯 귀로 따라가요.</> : <>Two lines move together. The top line is <b>the bird's</b>, the bottom line <b>the turtle's</b>. Follow one line with your ear, as your eye would.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 처음 두 음정을 쳐요. 윗성부를 불러요.</>, <>이제 네 음정 모두, 두 번. 아랫성부를 불러요.</>, <>부른 네 음을 건반에서 찾아요.</>]
        : [<>Your teacher plays the first two intervals. Sing the higher part.</>, <>Now all four, twice. Sing the lower part.</>, <>Find the four notes you sang on the keys.</>]}/>
      <LbRemember>{t('Two parts, four moves: follow one line.', '두 성부, 네 걸음: 한 줄만 따라가요.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Perfect or plagal?', '정격종지? 변격종지?')}
      teacher={<>{t('Grade 6: perfect and plagal cadences in a major key as they occur in a short piece played by you, the tonic chord being first sounded. Perfect: V–I; plagal: IV–I. The app’s pieces are four bars of chords (two a bar) in C, G, D, F, B♭ or A major, with the cadence at the end; the first rung plays the tonic chord, then just the last two chords. Below the pad: Make your own ending, where the child writes four bars and the cadence is named as it is made.', '6급: 선생님이 치는 장조의 짧은 곡에서 나오는 정격종지와 변격종지 알기, 먼저 으뜸화음을 울려요. 정격: V–I, 변격: IV–I. 앱의 곡은 C, G, D, F, B♭, A장조의 네 마디(마디마다 화음 둘), 끝에 종지. 첫 걸음은 으뜸화음 다음 마지막 두 화음만. 아래에는 \'나만의 끝 만들기\': 아이가 네 마디를 쓰면 종지 이름이 바로 나와요.')}</>} qr={bkLink('drill=' + ch + '&tab=drill&level=4')}>
      <LbLive still={cadStill} live={<><L6CadPad/><div style={{height:12}}/><CadMaker/></>}/>
      <LbSay>{LANG === 'ko' ? <>곡의 끝 두 화음이 <b>종지</b>. <b>V에서 I</b>은 정격종지: 단단히 닫혀요. <b>IV에서 I</b>은 변격종지: 부드럽게 닫혀요.</> : <>The last two chords of a piece are its <b>cadence</b>. <b>V to I</b> is perfect: firmly closed. <b>IV to I</b> is plagal: softly closed.</>}</LbSay>
      <LbPiano steps={LANG === 'ko' ? [<>선생님이 으뜸화음, 그다음 V–I, IV–I을 쳐요. 차이를 들어요.</>, <>이번엔 짧은 곡 전체. 끝 두 화음만 기억해요.</>, <>정격종지일까요, 변격종지일까요?</>]
        : [<>Your teacher plays the tonic chord, then V–I and IV–I. Hear the difference.</>, <>Now a whole short piece. Remember just the last two chords.</>, <>Perfect or plagal?</>]}/>
      <LbRemember>{t('V to I: perfect. IV to I: plagal.', 'V에서 I: 정격. IV에서 I: 변격.')}</LbRemember>
    </LbPage>,
    <LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My four checks', '나의 네 가지 확인')}
      teacher={<>{t('Each one with you at the piano, away from the screen, played twice as in the exam: you play, the child sings or names. You only correct.', '하나씩 화면 없이 피아노 앞에서, 시험처럼 두 번씩: 선생님이 치고, 아이는 부르거나 이름을 말해요. 선생님은 고쳐 주기만 해요.')}</>}>
      <LbSay>{t('Tick each one: not yet, nearly, or got it!', '하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={checks4.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={checks4} storeKey="pb_l6_four"/>}/>
    </LbPage>,
  ];
}
function Listen6LessonBook() { return <>{l6LbPages(false)}</>; }
function L6Learn({ onStart }) {
  const pages = l6LbPages(true), opener = pages[0];
  return (
    <Lesson id="listen-6" title={bkChapterName('listen-6')} onStart={onStart} noArt
      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value="listen-6"><div className="lb-screen lb-open" style={{display:'flex',flexDirection:'column',gap:12,margin:'0 0 8px'}}>{lbWordsFirst(opener.props.children)}</div></BkChapterCtx.Provider></LbScreenCtx.Provider>}>
      {pages.slice(1).map((pg, i) => <Step key={i} title={pg.props.title}><LbScreenPage page={pg}/></Step>)}
    </Lesson>
  );
}
// ── the drill: every question is heard, through the pads (each one reports right or wrong) ──
const L6_LEVELS = [
  { n: 1, label: 'Major or minor: name the interval', kind: 'iv', time: 25 },
  { n: 2, label: 'A major triad: which position?', kind: 'pos', time: 25 },
  { n: 3, label: 'Four intervals: sing the higher or the lower part', kind: 'two', time: 60 },
  { n: 4, label: 'Perfect or plagal?', kind: 'cad', time: 40 },
  { n: 5, label: 'All four, mixed, as in the Grade 6 exam', kind: 'mix', time: 60 },
];
Object.assign(LEVEL_KO, { 'Major or minor: name the interval': '장조든 단조든: 음정 이름', 'A major triad: which position?': '장3화음: 어느 자리?', 'Four intervals: sing the higher or the lower part': '네 음정: 윗성부나 아랫성부 부르기', 'Perfect or plagal?': '정격종지? 변격종지?', 'All four, mixed, as in the Grade 6 exam': '네 가지 섞어서, 6급 시험처럼' });
function genL6Question(lv, prev) {
  const uid = Math.random(); let kind = lv.kind;
  if (kind === 'mix') kind = pick(['iv', 'pos', 'two', 'cad'].filter(k => !prev || prev.kind !== k));
  let fx, key, g = 0;
  do {
    if (kind === 'iv') fx = { k: pick(L5_KEYS), mode: pick(['maj', 'hm']), n: pick([2, 3, 4, 5, 6, 7, 8]) };
    else if (kind === 'pos') fx = { r: Math.floor(Math.random() * 12), q: 'maj', inv: pick([0, 1, 2]) };
    else if (kind === 'two') fx = { i: Math.floor(Math.random() * L6_TWO.length), ask: Math.random() < 0.5 ? 'hi' : 'lo' };
    else fx = { key: pick(CAD_KEYS), cad: pick(['perfect', 'plagal']), ti: Math.floor(Math.random() * 3) };
    key = kind + JSON.stringify(fx);
  } while (prev && prev.key === key && g++ < 10);
  return { kind, fx, answer: 'ok', choices: [], key, uid };
}
function L6Question({ q, given, locked, onAnswer, pixel }) {
  const pickIt = (c) => { if (locked || given) return; stopClicks(); onAnswer(c); };
  const res = (r) => pickIt(r.ok ? 'ok' : 'no');
  const title = { iv: t('The keynote, then a note of its scale: name the interval.', '으뜸음, 그다음 그 음계의 음: 음정 이름은?'), pos: t('A major triad: which position?', '장3화음: 어느 자리?'),
    two: q.fx.ask === 'hi' ? t('Sing the higher part, then find its four notes.', '윗성부를 부르고, 네 음을 찾아요.') : t('Sing the lower part, then find its four notes.', '아랫성부를 부르고, 네 음을 찾아요.'), cad: t('Home first, then the piece: perfect or plagal?', '먼저 집, 그다음 곡: 정격? 변격?') }[q.kind];
  const body = q.kind === 'iv' ? <L6IvPad key={q.uid} fixed={q.fx} onResult={res}/> : q.kind === 'pos' ? <L6PosPad key={q.uid} fixed={q.fx} onResult={res}/> : q.kind === 'two' ? <L6TwoPad key={q.uid} fixed={q.fx} onResult={res}/> : <L6CadPad key={q.uid} fixed={q.fx} onResult={res}/>;
  return (<div>
    <p style={pixel ? {fontSize:11.5,textAlign:'center'} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 8px',color:'var(--muted)',textWrap:'balance'}}>{title}</p>
    {body}
  </div>);
}
Object.assign(LISTEN_6_DRILL, { levels: L6_LEVELS, generate: genL6Question, check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer, answerLabel: () => t('done', '완료'), Question: L6Question, Learn: L6Learn });
// the teacher's copy (no Workbook: every step is by ear)
function L6Teacher() {
  const pages = [];
  const P = (content) => pages.push(<WbPage key={pages.length} no={pages.length + 1} chId="listen-6" teacher>{content}</WbPage>);
  const lt = (i) => { const nm = lwLet(i); return i < 0 ? nm + ',' : nm + (i >= 12 ? "'" : ''); };
  const iv = ([k, mode, n]) => { const v = l6Iv(mode, n); return L6_KN[mode][spPc(k)] + (mode === 'maj' ? ' major' : ' minor') + ', then ' + l6Deg(k, mode, n) + ': ' + L6_IVN[v[0]][0]; };
  const two = (P2) => P2.lo.map((p, j) => lt(p[0]) + '+' + lt(P2.hi[j][0])).join(' → ');
  const tri = ([r, inv]) => { const n = l6Tri(r, 'maj', inv); return n.map(lt).join(' ') + ' (' + lwLet(r) + ', ' + L4_INVW[inv][0] + ')'; };
  const cad = ([key, c, ti]) => CAD_KN[key] + ': ' + CAD_TPL[c][ti].slice(0, 6).reduce((a, x, j) => a + (j % 2 === 0 && j ? ' | ' : ' ') + x, '').trim() + ' | ' + CAD_TPL[c][ti][6] + ' (' + c + ')';
  P(<>
    <div style={{fontFamily:LB_SERIF,fontSize:28,fontWeight:900,color:BK.ink,margin:'2px 0 2px'}}>Teacher copy · {bkChapterName('listen-6')}</div>
    <div style={{fontSize:12.5,color:BK.muted,margin:'0 0 12px',lineHeight:1.5}}>No Workbook for this chapter: every step is by ear, as the Grade 6 aural tests ask. Each block faces its Lesson Book page and gives you material to play, the same as the app uses. Play every test twice. Middle C is C here; the C above is C'; notes below middle C carry a comma (B♭,).</div>
    <TcBlock page={2} title="Major or minor: any interval" answers={<>{tcAns('PLAY', [[0, 'hm', 6], [2, 'maj', 6], [-3, 'hm', 3], [5, 'maj', 7], [4, 'hm', 7], [7, 'hm', 6], [-2, 'maj', 3], [2, 'hm', 3]].map(iv))}</>}
      watch="The minor 6th heard as a perfect 5th, or the minor 3rd as major. Sing up the scale from 1 aloud the first time: the 3rd and 6th give the minor away."
      say="“Minor: 3 and 6 a semitone lower.”"/>
    <TcBlock page={3} title="Which position is the triad?" answers={<>{tcAns('PLAY', [[0, 2], [7, 1], [2, 0], [5, 2], [9, 1], [4, 0], [10, 2], [3, 1]].map(tri))}</>}
      watch="Second inversion called root position because the top note is the root. Ask for the bottom note first, then where the 4th is."
      say="“No 4th: root. 4th on top: first. 4th at the bottom: second.”"/>
  </>);
  P(<>
    <TcBlock page={4} title="Four intervals: sing one part" answers={<>{tcAns('PLAY (LOWER+HIGHER)', L6_TWO.slice(0, 8).map(two))}</>}
      watch="Jumping to the other part where one part stays still (phrase 6) or where the parts cross a 6th. Ask for the lower part as often as the higher."
      say="“Two parts, four moves: follow one line.”"/>
    <TcBlock page={5} title="Perfect or plagal?" answers={<>{tcAns('PLAY THE TONIC CHORD, THEN', [[0, 'perfect', 0], [7, 'plagal', 1], [2, 'perfect', 2], [5, 'plagal', 0], [-2, 'perfect', 1], [9, 'plagal', 2]].map(cad))}</>}
      watch="Plagal heard as perfect: both end on I. Play V–I and IV–I side by side, then ask which chord came before the last."
      say="“V to I: perfect. IV to I: plagal.”"/>
    <TcBlock page={6} title="My four checks" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>Each one with you at the piano, away from the screen, played twice: you play, the child sings or names. Use material the child has not heard this week. The drill's level 5 mixes all four, as the exam does.</div>}/>
  </>);
  return <>{pages}</>;
}
TEACHER_COPIES['listen-6'] = L6Teacher;
'''
rep("""TEACHER_COPIES['listen-5'] = L5Teacher;""", """TEACHER_COPIES['listen-5'] = L5Teacher;""" + CH)

HOME = r'''
// ══ Build BO: Hear and Sing, Grade 6 on the Home (the Aural door) ══
LBH_FN['listen-6'] = (s) => l6LbPages(s);
const l6Add = (id, i, en, ko, benEn, bko, make) => { const spec = lbhSpec('listen-6', i, { make });
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return t('Aural', '청음') + ' · ' + t('Hear and sing, Grade 6', '듣고 부르기, Grade 6'); }, C: () => <KqEngine spec={spec}/> });
  lbhRetitle(id, en, ko, benEn, bko); };
const l6IvQ = (n, prev) => { let k, mode, dg, g = 0; do { k = pick(L5_KEYS); mode = n % 2 ? 'maj' : 'hm'; dg = pick([2, 3, 4, 5, 6, 7, 8]); } while (prev && prev.key === k + mode + dg && g++ < 10); const v = l6Iv(mode, dg);
  return { kind: 'choice', cols: 3, prompt: ['The keynote, then a note: sing it, then name it.', '으뜸음, 그다음 음: 부르고, 이름을 말해요.'], opts: L6_IVS.map(x => ({ id: x[0], label: () => l6IvName(x[0]) })), ans: v[0], ok: (a) => a === v[0],
    key: k + mode + dg, play: () => l4PlayIv(k, v[2]),
    fig: (c) => ({ mid: c.res ? <SpKb lo={Math.min(0, k)} hi={Math.max(14, k + 12)} W={24} H={72} lit={{ [k]: 'pale', [k + v[2]]: c.res === 'ok' ? 'good' : 'cor' }} names={Object.fromEntries(L6_SC[mode].map((s, j) => [k + s, String(j + 1)]))}/> : null }),
    yes: ['Yes: a ' + L6_IVN[v[0]][0] + '.', '맞아요: ' + L6_IVN[v[0]][1] + '.'], no: ['It was a ' + L6_IVN[v[0]][0] + ' (' + (mode === 'maj' ? 'major' : 'harmonic minor') + ', degree ' + dg + ').', L6_IVN[v[0]][1] + '였어요(' + l6Mode(mode) + ', ' + dg + '번 음).'] }; };
const l6PosQ = (n, prev) => { let r, inv, g = 0; do { r = Math.floor(Math.random() * 12); inv = n % 3; } while (prev && prev.key === r + '-' + inv && g++ < 10); const nn = l6Tri(r, 'maj', inv);
  return { kind: 'choice', cols: 3, prompt: ['A major triad: which position?', '장3화음: 어느 자리?'], opts: [0, 1, 2].map(x => ({ id: x, label: () => t(L4_INVW[x][0], L4_INVW[x][1]) })), ans: inv, ok: (a) => a === inv, key: r + '-' + inv, play: () => l4PlayTri(nn),
    fig: (c) => ({ mid: c.res ? <><SpKb lo={-5} hi={16} W={22} H={66} lit={Object.fromEntries(nn.map(k => [k, 'cor']))} names={Object.fromEntries(nn.map(k => [k, l4Let(k)]))}/><L6Gaps n={nn}/></> : null }),
    yes: ['Yes: ' + L4_INVW[inv][0] + '.', '맞아요: ' + L4_INVW[inv][1] + '.'], no: ['It was ' + L4_INVW[inv][0] + '. Listen for the 4th: none, on top, or at the bottom.', L4_INVW[inv][1] + '였어요. 4도를 들어 봐요: 없음, 위, 아래.'] }; };
const l6CadQ = (n, prev) => { let x, g = 0; do { x = { key: pick(CAD_KEYS), cad: n % 2 ? 'plagal' : 'perfect', ti: Math.floor(Math.random() * 3) }; } while (prev && prev.key === JSON.stringify(x) && g++ < 10); const sq = CAD_TPL[x.cad][x.ti];
  return { kind: 'choice', cols: 2, prompt: ['Home first, then the piece: perfect or plagal?', '먼저 집, 그다음 곡: 정격? 변격?'], opts: ['perfect', 'plagal'].map(c => ({ id: c, label: () => cadCap(c) + ' · ' + CAD_N[c][2] })), ans: x.cad, ok: (a) => a === x.cad, key: JSON.stringify(x), play: () => cadPlay(x, false),
    fig: (c) => ({ mid: c.res ? <CadChart x={x}/> : null }), yes: ['Yes: ' + sq[5] + ' to ' + sq[6] + '.', '맞아요: ' + sq[5] + '에서 ' + sq[6] + '.'], no: ['It was ' + CAD_N[x.cad][0] + ': ' + sq[5] + ' to ' + sq[6] + '.', CAD_N[x.cad][1] + '였어요: ' + sq[5] + '에서 ' + sq[6] + '.'] }; };
l6Add('l6-iv', 1, 'Major or minor: any interval', '장조든 단조든: 어떤 음정이든', 'The minor 3rd and 6th join the major scale’s intervals.', '장음계의 음정에 단3도와 단6도가 더해져요.', l6IvQ);
l6Add('l6-pos', 2, 'Which position is the triad?', '3화음은 어느 자리?', 'Listen for the 4th: none, on top, or at the bottom.', '4도를 들어요: 없음, 위, 아래.', l6PosQ);
l6Add('l6-two', 3, 'Four intervals: sing one part', '네 음정: 한 성부를 불러요', 'Four intervals in two parts: sing the higher or the lower.', '두 성부의 네 음정: 윗성부나 아랫성부 부르기.', lwTapQ(L6TwoPad, (n) => ({ fixed: { i: (n * 5) % L6_TWO.length, ask: n % 2 ? 'lo' : 'hi' } }), ['Hear the two parts, sing the one asked, then find its notes.', '두 성부를 듣고, 묻는 성부를 부르고, 음을 찾아요.'], ['Sung and found ✓', '부르고 찾았어요 ✓']));
l6Add('l6-cad', 4, 'Perfect or plagal?', '정격종지? 변격종지?', 'Home first, then a short piece: how does it end?', '먼저 집, 그다음 짧은 곡: 어떻게 끝날까요?', l6CadQ);
'''
rep("""
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""", HOME + """
lbhAdd('rb-finger', 'r-beat', 'rhythm', 'The beat in your fingers'""")
# the make-toy: in the room's toolbox and on the Home
rep("""  { id: 'mk-iv', ch: 'intervals', title: 'A tune from one interval',""",
    """  { id: 'mk-cad', ch: 'listen-6', title: 'Make your own ending', blurb: 'Write four bars of chords; the cadence is named as you make it.', C: () => <CadMaker/> },   // Build BO
  { id: 'mk-iv', ch: 'intervals', title: 'A tune from one interval',""")
rep("""  'mk-iv': ['음정 하나로 선율 만들기',""", """  'mk-cad': ['나만의 끝 만들기', '네 마디를 화음으로 쓰면, 만드는 대로 종지 이름이 나와요.'],
  'mk-iv': ['음정 하나로 선율 만들기',""")
rep("""'mk-iv': ['intervals', 1, 2, 'game ear'],""", """'mk-iv': ['intervals', 1, 2, 'game ear'], 'mk-cad': ['chords', 3, 3, 'game ear'],""")
rep("""'mk-iv': 'p-intervals',""", """'mk-iv': 'p-intervals', 'mk-cad': 'p-chords',""")
rep("""  'mk-iv': () => (\n""", """  'mk-cad': () => (
    <svg width="34" height="34" viewBox="0 0 24 24"><rect width="24" height="24" rx="6" fill="#3b4fa8"/><rect x="3" y="7" width="18" height="10" rx="1.5" fill="#fefbf3"/><path d="M12 7 V17" stroke="#3b4fa8" strokeWidth="1.4"/><text x="7.5" y="15.2" textAnchor="middle" fontSize="7.5" fontWeight="900" fill="#e9a83a">V</text><text x="16.5" y="15.2" textAnchor="middle" fontSize="7.5" fontWeight="900" fill="#3b4fa8">I</text></svg>
  ),
  'mk-iv': () => (\n""")
rep("""    { id: 'au-5', en: 'Hear and sing, Grade 5', ko: '듣고 부르기, Grade 5', lessons: ['l5-iv', 'l5-two', 'l5-tri', 'l5-clap'], check: 'listen-5' },""",
    """    { id: 'au-5', en: 'Hear and sing, Grade 5', ko: '듣고 부르기, Grade 5', lessons: ['l5-iv', 'l5-two', 'l5-tri', 'l5-clap'], check: 'listen-5' },
    { id: 'au-6', en: 'Hear and sing, Grade 6', ko: '듣고 부르기, Grade 6', lessons: ['l6-iv', 'l6-pos', 'l6-two', 'l6-cad', 'mk-cad'], check: 'listen-6' },   // Build BO""")
rep("""  set('5', 'l5-iv l5-two l5-tri l5-clap');   // Build AZ: Hear and Sing, Grade 5""", """  set('5', 'l5-iv l5-two l5-tri l5-clap');   // Build AZ: Hear and Sing, Grade 5
  set('6', 'l6-iv l6-pos l6-two l6-cad mk-cad');   // Build BO: Hear and Sing, Grade 6""")
# the books and the house
rep("""const LESSON_BOOKS = { 'harmony-5': Harmony5LessonBook,""", """const LESSON_BOOKS = { 'listen-6': Listen6LessonBook, 'harmony-5': Harmony5LessonBook,""")
rep("""const LB_PAGE_FNS = { 'harmony-5': h5LbPages,""", """const LB_PAGE_FNS = { 'listen-6': l6LbPages, 'harmony-5': h5LbPages,""")
rep("""const HOUSE_ICONS = {""", """const HOUSE_ICONS = {"listen-6": "<path d=\\"M8 15C3 21 3 29 8 35M15 19C12 22 12 28 15 31\\"/><ellipse cx=\\"26\\" cy=\\"35\\" rx=\\"4.6\\" ry=\\"3.4\\" transform=\\"rotate(-20 26 35)\\" fill=\\"#26296b\\"/><ellipse cx=\\"26\\" cy=\\"28\\" rx=\\"4.6\\" ry=\\"3.4\\" transform=\\"rotate(-20 26 28)\\" fill=\\"#26296b\\"/><ellipse cx=\\"26\\" cy=\\"21\\" rx=\\"4.6\\" ry=\\"3.4\\" transform=\\"rotate(-20 26 21)\\" fill=\\"#26296b\\"/><ellipse cx=\\"39\\" cy=\\"32\\" rx=\\"4.6\\" ry=\\"3.4\\" transform=\\"rotate(-20 39 32)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><ellipse cx=\\"39\\" cy=\\"25\\" rx=\\"4.6\\" ry=\\"3.4\\" transform=\\"rotate(-20 39 25)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/><ellipse cx=\\"39\\" cy=\\"18\\" rx=\\"4.6\\" ry=\\"3.4\\" transform=\\"rotate(-20 39 18)\\" fill=\\"#e4572e\\" stroke=\\"#e4572e\\"/>", """)
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
