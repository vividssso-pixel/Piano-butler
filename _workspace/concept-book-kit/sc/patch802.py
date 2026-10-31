"""Build DZ (the audit's gaps, her 11:33; her 13:42 'only what is needed, useful and fun'): Rhythm, Grade 2 had no
make-it toy: Split the beat with the Grade 2 ways only (crotchet, two quavers, four semiquavers, quaver and two
semiquavers, two semiquavers and a quaver, the triplet: what the room teaches; the dotted ones are Grade 3), in step 2.
(Intervals, Grade 2 gets none: its own pad already sounds every interval above the tonic.)"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

# 1. Split the beat takes its ways, its stars and its store
R("""function BeatSplit() {
  const [c, setC] = useState(['q', 'p', 's4', 'q', 'ds', 'ds', 't3', 'q']), [bpm, setBpm] = useState(66);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem('pb_mk_split')) || {}; } catch (e) { return {}; } });""",
  """function BeatSplit({ kinds, sk = 'pb_mk_split', starsDef = BS_STARS, start = ['q', 'p', 's4', 'q', 'ds', 'ds', 't3', 'q'] } = {}) {   // Build DZ: kinds, stars and store for Rhythm, Grade 2
  const KS = kinds ? BS_KINDS.filter(x => kinds.includes(x[0])) : BS_KINDS, dot = KS.some(x => x[0] === 'ds');
  const [c, setC] = useState(start), [bpm, setBpm] = useState(66);
  const [stars, setStars] = useState(() => { try { return JSON.parse(localStorage.getItem(sk)) || {}; } catch (e) { return {}; } });""")
R("""  const flip = (j) => { const n = c.slice(); n[j] = BS_KINDS[(BS_KINDS.findIndex(x => x[0] === n[j]) + 1) % BS_KINDS.length][0]; setC(n);
    const s2 = { ...stars }; if (n.includes('t3')) s2.trip = 1; if (n.includes('ds')) s2.dot = 1; if (BS_KINDS.every(x => n.includes(x[0]))) s2.all = 1;
    if (Object.keys(s2).length !== Object.keys(stars).length) { setStars(s2); try { localStorage.setItem('pb_mk_split', JSON.stringify(s2)); } catch (e) {} } };""",
  """  const flip = (j) => { const n = c.slice(); n[j] = KS[(KS.findIndex(x => x[0] === n[j]) + 1) % KS.length][0]; setC(n);
    const s2 = { ...stars }; if (n.includes('t3')) s2.trip = 1; if (n.includes('ds')) s2.dot = 1; if (n.includes('s4')) s2.semi = 1; if (KS.every(x => n.includes(x[0]))) s2.all = 1;
    if (Object.keys(s2).length !== Object.keys(stars).length) { setStars(s2); try { localStorage.setItem(sk, JSON.stringify(s2)); } catch (e) {} } };""")
R("""      <div style={actNote}>{LANG === 'ko' ? <>4/4 두 마디. 박을 누를 때마다 <b>쪼개는 방법</b>이 바뀌어요: 하나 그대로, 둘, 넷, 길게 짧게, 셋잇단까지 일곱 가지. 듣고, 쳐 보고, 빠르게도!</> : <>Two bars of 4/4. Tap a beat to <b>split it a new way</b>: whole, in two, in four, long-short, in three… seven ways. Listen, tap it back, then speed up!</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{BS_STARS.map(""",
  """      <div style={actNote}>{LANG === 'ko' ? <>4/4 두 마디. 박을 누를 때마다 <b>쪼개는 방법</b>이 바뀌어요: 하나 그대로, 둘, 넷, {dot ? '길게 짧게, ' : ''}셋잇단까지 {dot ? '일곱' : '여섯'} 가지. 듣고, 쳐 보고, 빠르게도!</> : <>Two bars of 4/4. Tap a beat to <b>split it a new way</b>: whole, in two, in four, {dot ? 'long-short, ' : ''}in three… {dot ? 'seven' : 'six'} ways. Listen, tap it back, then speed up!</>}</div>
      <div style={{display:'flex',gap:'4px 12px',justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>{starsDef.map(""")

# 2. the two new toys
R("""// ══ Build CI: batch 7, the Grade 4 rooms' things to make (call 25; her 09:56: fun first) ══""",
  """// Build DZ: Rhythm, Grade 2's Split the beat: the room's six ways (no dotted rhythm: that is Grade 3)
const BS2_STARS = [['trip', 'Use a triplet', '셋잇단음표 쓰기'], ['semi', 'Use four semiquavers', '16분음표 넷 쓰기'], ['all', 'All six in two bars', '두 마디에 여섯 가지 모두']];
function BeatSplit2() { return <BeatSplit kinds={['q', 'p', 's4', 'es', 'se', 't3']} sk="pb_mk_split2" starsDef={BS2_STARS} start={['q', 'p', 's4', 'q', 'es', 'se', 't3', 'q']}/>; }
// ══ Build CI: batch 7, the Grade 4 rooms' things to make (call 25; her 09:56: fun first) ══""")
# 3. their tool entries and where they go
R("""  { id: 'mk-split', ch: 'rhythm-3',""", """  { id: 'mk-split2', ch: 'rhythm-2', title: 'Split the beat', blurb: 'Two bars of 4/4, each beat split one of six ways: semiquavers, a triplet and more. Then tap it.', C: () => <BeatSplit2/> },
  { id: 'mk-split', ch: 'rhythm-3',""")
R("""  'mk-split': ['박 쪼개기',""", """  'mk-split2': ['박 쪼개기', '4/4 두 마디, 박마다 여섯 가지로 쪼개요: 16분음표, 셋잇단음표까지. 그리고 쳐 봐요.'],
  'mk-split': ['박 쪼개기',""")
R("""  'harmony-3': { 2: ['mk-choir'] }, 'rhythm-3': { 0: ['mk-split'] },""", """  'harmony-3': { 2: ['mk-choir'] }, 'rhythm-3': { 0: ['mk-split'] }, 'rhythm-2': { 1: ['mk-split2'] },""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok two toys', len(s))
