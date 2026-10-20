import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# 1. levels, numbered like the eleven Home lessons (her order 2026-10-20): 1 pattern, 2 same pattern, 3 degrees, 4-7 fingering, 8 both hands, 9 twelve keys, 10 chromatic, 11 minors
a = s.index("const SSC_LEVELS = ["); b = s.index("];\n", a) + 3
NEWLV = """const SSC_LEVELS = [   // numbered like the eleven Home lessons (1 pattern, 2 same pattern, 3 degrees, 4-7 fingering, 8 both hands, 9 twelve keys, 10 chromatic, 11 minors)
  { n: 1, label: 'Whole or half?', short: ['Whole or half?', '온음? 반음?'], num: '1', kind: 'step', time: 8 },
  { n: 2, label: 'Where is the half step?', short: ['Where is the half step?', '반음은 어디?'], num: '1', kind: 'half', time: 8 },
  { n: 3, label: 'Build the scale', short: ['Build the scale', '음계 만들기'], num: '1–2', kind: 'build', time: 20 },
  { n: 5, label: 'Which degree?', short: ['Which degree?', '몇 번 음?'], num: '3', kind: 'degree', time: 8 },
  { n: 6, label: 'Name the scale note', short: ['Name the note', '음 이름 맞히기'], num: '3', kind: 'name', time: 9 },
  { n: 61, label: 'Which finger, any key?', short: ['Which finger?', '몇 번 손가락?'], num: '4–8', kind: 'finger12', time: 10 },
  { n: 62, label: 'Build any of the twelve major scales', short: ['Build any key', '어느 조든 만들기'], num: '9', kind: 'build12', time: 22 },
  { n: 63, label: 'Chromatic scale: which finger?', short: ['Chromatic fingers', '반음계 손가락'], num: '10', kind: 'chrom', time: 9 },
  { n: 64, label: 'Which kind of minor?', short: ['Which minor?', '어떤 단음계?'], num: '11', kind: 'minform', time: 12 },
  { n: 9, label: 'Harmonic minor, the raised 7th', short: ['The raised 7th', '올린 7번 음'], num: '11', kind: 'minor7', time: 9 },
  { n: 7, label: 'Listen: a major scale?', short: ['Listen', '듣기'], extra: true, extraStart: true, kind: 'ear', time: 14, noPrint: true },
  { n: 8, label: 'Extra: D and B♭ major', short: ['D and B♭ signs', 'D와 B♭의 조표'], extra: true, kind: 'acc2', time: 9 },
  { n: 10, label: 'My keys: the scale notes', short: ['My keys', '나의 조'], extra: true, kind: 'mykeys', time: 10 },
];
"""
s = s[:a] + NEWLV + s[b:]
rep("Object.assign(LEVEL_KO, {\n  'Whole or half?'", "Object.assign(LEVEL_KO, {\n  'Build any of the twelve major scales': '열두 장음계 중 아무거나 만들기', 'Chromatic scale: which finger?': '반음계: 몇 번 손가락?', 'Which kind of minor?': '어떤 단음계일까요?', 'Which finger, any key?': '어느 조든 몇 번 손가락?', 'Harmonic minor, the raised 7th': '화성단음계의 올린 7번 음',\n  'Whole or half?'")
# 2. generator
rep("function genSscQuestion(lv, prev) {\n  if (lv.kind === 'mykeys') return genMyScaleQ(prev);\n",
    "function genSscQuestion(lv, prev) {\n  if (lv.kind === 'mykeys') return genMyScaleQ(prev);\n  if (['finger12', 'build12', 'chrom', 'minform'].includes(lv.kind)) return genScNew(lv, prev);\n")
NEWGEN = r"""
// ─── Phase 587 (her order, 2026-10-20): Scales drill rebuilt to match the eleven lessons. New kinds on the lessons' own keyboard (ScKeys): any key and hand (finger12), build any of the twelve (build12), chromatic fingering (chrom), which minor (minform).
const SC_MINQ = [
  { ans: 'harmonic', en: 'Raise only the 7th note, going up and coming down. Which minor is that?', ko: '7번째 음만 올려요, 올라갈 때도 내려올 때도. 어떤 단음계일까요?' },
  { ans: 'melodic', en: 'Going up it raises the 6th and 7th; coming down it plays the natural minor. Which minor is that?', ko: '올라갈 때는 6음과 7음을 올리고, 내려올 때는 자연 단음계를 쳐요. 어떤 단음계일까요?' },
  { ans: 'natural', en: 'The very same notes as its relative major: A minor uses C major’s white keys. Which minor is that?', ko: '나란한조인 장조와 음이 똑같아요: A 단조는 C 장조의 흰건반을 써요. 어떤 단음계일까요?' },
  { ans: 'melodic', en: 'Which minor comes down differently from the way it went up?', ko: '올라간 길과 내려오는 길이 다른 단음계는 어느 것일까요?' },
  { ans: 'harmonic', en: 'Which minor has the wide T+S step, with a G♯ in it?', ko: 'G♯이 있고, 넓은 T+S 간격이 생기는 단음계는 어느 것일까요?' },
];
function genScNew(lv, prev) {
  const uid = Math.random(), pk = prev && prev.key;
  const again = (f) => { for (let g = 0; g < 30; g++) { const q = f(); if (q.key !== pk) return { ...q, uid }; } return { ...f(), uid }; };
  if (lv.kind === 'finger12') return again(() => { const k = pick(SC_12), hand = pick(['RH', 'LH']), d = Math.floor(Math.random() * 8);
    return { kind: 'finger12', start: k, hand, d, key: k + hand + d, answer: String(SCALES[k].octaves[1][hand][d]), choices: ['1', '2', '3', '4', '5'] }; });
  if (lv.kind === 'build12') return again(() => { const k = pick(SC_12); return { kind: 'build12', start: k, key: 'b12' + k }; });
  if (lv.kind === 'chrom') return again(() => { const hand = pick(['RH', 'LH']), j = Math.floor(Math.random() * 13);
    return { kind: 'chrom', hand, j, key: 'c' + hand + j, answer: String(chromFinger(j % 12, hand, j === 0)), choices: ['1', '2', '3'] }; });
  return again(() => { const m = pick(SC_MINQ), i = SC_MINQ.indexOf(m); return { kind: 'minform', i, key: 'mf' + i, answer: m.ans, choices: ['natural', 'harmonic', 'melodic'] }; });
}
function ScDrillQ({ q, given, locked, onAnswer, pixel }) {
  const board = useBoard(q, given);
  const [bs, setBs] = useState({ uid: q.uid, done: 1, miss: null });
  const cur = bs.uid === q.uid ? bs : { uid: q.uid, done: 1, miss: null };
  const isDone = !!given;
  const btnCls = pixel ? 'pixel-choice' : 'choice-btn';
  const prompt = (txt) => <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)',textWrap:'balance',wordBreak:'keep-all'}}>{txt}</p>;
  const big = (txt) => <div style={{textAlign:'center',fontSize:pixel ? 14 : 22,fontWeight:900,margin:'0 0 8px',color:pixel ? 'var(--brass)' : BK.ink}}>{txt}</div>;
  const st = (c) => !isDone ? '' : (String(c) === String(q.answer) ? ' good' : (String(given.ans) === String(c) ? ' bad' : ''));
  const grid = (cols, render) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,marginTop:10}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => onAnswer(c)} className={btnCls + st(c)} style={{padding:'14px 2px'}}><span style={{fontSize:pixel ? 11 : 18,fontWeight:900}}>{render(c)}</span></button>)}</div>;
  const paper = (node) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:'4px 4px 8px',margin:'0 auto 6px',maxWidth:440}}>{node}</div>;
  let body;
  if (q.kind === 'finger12') {
    const K = scIdx(q.start), F = SCALES[q.start].octaves[1][q.hand], N = scNames(q.start), marks = {}, names = {};
    K.forEach(k => { marks[k] = 'pass'; }); marks[K[q.d]] = 'target';
    if (isDone) K.forEach((k, j) => { names[k] = String(F[j]); });
    body = <>{big(sscScaleName(q.start) + ' · ' + (q.hand === 'RH' ? t('right hand', '오른손') : t('left hand', '왼손')))}{prompt(t('Going up, which finger plays the coral key?', '올라갈 때 산호색 건반은 몇 번 손가락으로 칠까요?'))}
      {paper(<ScKeys ring ks={K} marks={marks} names={names} arcs={[]} nonce={q.uid}/>)}{grid(5, c => c)}</>;
  } else if (q.kind === 'build12') {
    const K = scIdx(q.start), N = scNames(q.start), marks = {}, names = {};
    K.forEach(k => { marks[k] = 'pass'; });
    for (let j = 0; j < cur.done; j++) { marks[K[j]] = j === cur.done - 1 && !isDone ? 'pick' : 'good'; names[K[j]] = N[j]; }
    if (isDone) K.forEach((k, j) => { names[k] = N[j]; });
    if (cur.miss != null) marks[cur.miss] = 'bad';
    const tap = (k) => { if (locked || isDone) return; const next = cur.done;
      if (k === K[next]) { setBs({ uid: q.uid, done: next + 1, miss: null }); playKey(k, 0.4); if (next + 1 === 8) onAnswer({ ok: true }); }
      else if (!K.slice(0, next).includes(k)) { setBs({ uid: q.uid, done: next, miss: k }); onAnswer({ ok: false, miss: k }); } };
    body = <>{big(sscScaleName(q.start))}{prompt(t('Play the scale up: tap each key from the coral one, whole and half steps in the pattern T T S T T T S.', '음계를 올라가요: 산호색 건반부터 T T S T T T S 패턴으로 눌러요.'))}
      {paper(<ScKeys ks={K} marks={cur.done === 1 && !isDone ? { ...marks, [K[0]]: 'pick' } : marks} names={names} arcs={[]} nonce={q.uid + ':' + cur.done} onTap={tap}/>)}</>;
  } else if (q.kind === 'chrom') {
    const K0 = Array.from({ length: 13 }, (_, j) => j), marks = {}, names = {};
    K0.forEach(k => { marks[k] = 'pass'; }); marks[q.j] = 'target';
    if (isDone) K0.forEach((k, j) => { names[k] = String(chromFinger(k % 12, q.hand, j === 0)); });
    body = <>{big(t('Chromatic scale from C · ', 'C에서 시작하는 반음계 · ') + (q.hand === 'RH' ? t('right hand', '오른손') : t('left hand', '왼손')))}{prompt(t('Going up, which finger plays the coral key?', '올라갈 때 산호색 건반은 몇 번 손가락으로 칠까요?'))}
      {paper(<ScKeys ring ks={K0} marks={marks} names={names} arcs={[]} nonce={q.uid}/>)}{grid(3, c => c)}</>;
  } else {
    const M = SC_MINQ[q.i], K = isDone ? MINOR_FORMS[q.answer].steps.map(x => 9 + x).concat([21]) : null, marks = {}, names = {};
    if (K) { const N = spellMinor('A', q.answer).map(prettyAny).concat(['A']); K.forEach((k, j) => { marks[k] = 'pass'; names[k] = N[j]; }); }
    body = <>{big(t('Three kinds of minor', '세 가지 단음계'))}{prompt(t(M.en, M.ko))}
      {K && paper(<ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={q.uid}/>)}{grid(3, c => MINOR_FORMS[c].label)}</>;
  }
  return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;
}
"""
rep("function sscPlayScale(q) {", NEWGEN + "function sscPlayScale(q) {")
rep("const SscQuestionAll = (p) => p.q && p.q.kind === 'mykeys' ? <MyScaleQuestion {...p}/> : <SscQuestion {...p}/>;",
    "const SscQuestionAll = (p) => p.q && p.q.kind === 'mykeys' ? <MyScaleQuestion {...p}/> : p.q && ['finger12', 'build12', 'chrom', 'minform'].includes(p.q.kind) ? <ScDrillQ {...p}/> : <SscQuestion {...p}/>;")
rep("  if (q.kind === 'build') return !!(ans && ans.ok);", "  if (q.kind === 'build' || q.kind === 'build12') return !!(ans && ans.ok);")
rep("function sscAnswerLabel(q) {\n  if (q.kind === 'mykeys') return myScaleLabel(q);\n",
    "function sscAnswerLabel(q) {\n  if (q.kind === 'mykeys') return myScaleLabel(q);\n  if (q.kind === 'finger12' || q.kind === 'chrom') return t('finger ' + q.answer, q.answer + '번 손가락');\n  if (q.kind === 'build12') return scNames(q.start).join(' ');\n  if (q.kind === 'minform') return MINOR_FORMS[q.answer].label;\n")
open(sys.argv[2],'w',encoding='utf-8').write(s)
