import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
a=s.index("const CLK_LEVELS = ["); b=s.index("];\n",a)+3
NEWLV = """const CLK_LEVELS = [   // numbered like the ten Home lessons (1 half step, 2 whole step, 3 sharp, 4 flat, 5 natural, 6 rules, 7 play it, 8 two names, 9 double signs, 10 accidental or key signature)
  { n: 21, label: 'Half step or whole step?', short: ['Half or whole?', '반음? 온음?'], num: '1–2', kind: 'hw', time: 7, noPrint: true },
  { n: 22, label: 'Play a half step, up or down', short: ['Play a half step', '반음 치기'], num: '1', kind: 'find', size: 1, time: 9, noPrint: true },
  { n: 23, label: 'White neighbours: E F and B C', short: ['White neighbours', '흰건반 이웃'], num: '1', kind: 'wn', time: 7, noPrint: true },
  { n: 24, label: 'Play a whole step, up or down', short: ['Play a whole step', '온음 치기'], num: '2', kind: 'find', size: 2, time: 9, noPrint: true },
  { n: 25, label: 'Name the sign', short: ['Name the sign', '임시표 이름'], num: '3–5', kind: 'sign', time: 7, noPrint: true },
  { n: 26, label: 'Find the key', short: ['Find the key', '건반 찾기'], num: '3–4', kind: 'key', time: 9, noPrint: true },
  { n: 27, label: 'Sharps and flats on the staff', short: ['On the staff', '오선 위 음'], num: '3–4', kind: 'staff', time: 10, noPrint: true },
  { n: 28, label: 'The natural', short: ['The natural', '내추럴'], num: '5', kind: 'nat', time: 10, noPrint: true },
  { n: 29, label: 'Until the bar line', short: ['Until the bar line', '세로줄까지'], num: '6', kind: 'bar', time: 10, noPrint: true },
  { n: 30, label: 'Its own line or space', short: ['Its own line or space', '같은 줄이나 칸'], num: '6', kind: 'line', time: 10, noPrint: true },
  { n: 31, label: 'Which sign?', short: ['Which sign?', '어떤 임시표?'], num: '6', kind: 'write', time: 12, noPrint: true },
  { n: 32, label: 'Read the bar', short: ['Read the bar', '마디 읽기'], num: '7', kind: 'read', time: 15, noPrint: true },
  { n: 33, label: 'Name the black keys', short: ['Black key names', '검은건반 이름'], num: '8', kind: 'bname', time: 7, noPrint: true },
  { n: 34, label: 'One key, two names', short: ['Two names', '이름 둘'], num: '8', kind: 'enh', time: 8, noPrint: true },
  { n: 35, label: 'Double sharps and flats', short: ['Double signs', '겹샵, 겹플랫'], num: '9', kind: 'dbl', time: 9, noPrint: true },
  { n: 36, label: 'Coral note in a key signature', short: ['Coral note', '산호색 음'], num: '10', kind: 'note', time: 12, noPrint: true },
  { n: 37, label: 'Listen: which bar?', short: ['Listen', '듣기'], extra: true, extraStart: true, kind: 'ear', time: 14, noPrint: true },
  { n: 38, label: 'Extra: the bass clef', short: ['Bass clef', '낮은음자리표'], extra: true, kind: 'bass', time: 10, noPrint: true },
  { n: 39, label: 'Accidental in a key signature', short: ['Accidentals in a key', '조표 안의 임시표'], extra: true, kind: 'acc', time: 14, noPrint: true },
];
"""
s=s[:a]+NEWLV+s[b:]
rep("Object.assign(LEVEL_KO, { 'Coral note in a key signature': '조표 안의 산호색 음', 'Accidental in a key signature': '조표 안의 임시표' });",
    "Object.assign(LEVEL_KO, { 'Coral note in a key signature': '조표 안의 산호색 음', 'Accidental in a key signature': '조표 안의 임시표', 'Double sharps and flats': '겹샵과 겹플랫' });")
DBL = r"""// lesson 9's drill: a double-sharp or double-flat name, tap its key (her ALL_NAMES: C𝄪 = D, F𝄫 = E♭ ...)
const CLK_DBL = [[28, 2, 'C', '𝄪', 'D'], [30, 2, 'E', '𝄪', 'F♯'], [31, 2, 'F', '𝄪', 'G'], [32, 2, 'G', '𝄪', 'A'], [33, 2, 'A', '𝄪', 'B'],
  [29, -2, 'D', '𝄫', 'C'], [30, -2, 'E', '𝄫', 'D'], [31, -2, 'F', '𝄫', 'E♭'], [32, -2, 'G', '𝄫', 'F'], [33, -2, 'A', '𝄫', 'G'], [34, -2, 'B', '𝄫', 'A']];
function genDblQuestion(prev) {
  const pk = prev && prev.key; let r; for (let g = 0; g < 30; g++) { r = pick(CLK_DBL); if ('d' + r[2] + r[3] !== pk) break; }
  const [d, acc, L, sym, eq] = r;
  return { kind: 'dbl', d, L, sym, eq, key: 'd' + L + sym, answer: ivMidi({ d, acc }), up: acc > 0, uid: Math.random() };
}
function DblQuestion({ q, given, locked, onAnswer, pixel, fbAbove }) {
  const board = useBoard(q, given);
  const isDone = !!given;
  const prompt = <p style={pixel ? {fontSize:11.5,textAlign:'center',margin:'0 0 10px',lineHeight:1.7} : {fontSize:15,fontWeight:700,textAlign:'center',margin:'0 0 10px',color:'var(--muted)',textWrap:'balance',wordBreak:'keep-all'}}>{t('Tap the key of this note.', '이 음의 건반을 눌러요.')}</p>;
  return <div style={fbAbove ? {display:'contents'} : undefined}><BoardTrack b={board} pixel={pixel}/>{prompt}
    <div style={{textAlign:'center',fontSize:pixel ? 26 : 46,fontWeight:900,color:pixel ? '#faf6ec' : '#26296b',margin:'0 0 8px',order:2,lineHeight:1.1}}>{q.L}<span style={{fontFamily:MUSIC_FONT}}>{q.sym}</span></div>
    <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '4px 0',margin:'0 auto 10px',maxWidth:360,order:2}}><SacKeys d0={28} n={8} o={{ lit: isDone ? [q.answer] : [], miss: isDone && given.ans !== q.answer ? given.ans : null, H: 120 }} onTap={(m) => { if (locked || isDone) return; sacKey(m); onAnswer(m); }}/></div></div>;
}
"""
rep("const clkWho = (q) =>", DBL + "const clkWho = (q) => q.kind === 'dbl' ? 'dbl' : ")
# the one-liner clkWho continues with the old test; keep it as the fallback
rep("generate: (lv, prev) => CLK_TN.includes(lv.kind) ?", "generate: (lv, prev) => lv.kind === 'dbl' ? genDblQuestion(prev) : CLK_TN.includes(lv.kind) ?")
rep("check: (q, ans) => { const w = clkWho(q); return w === 'tn' ?", "check: (q, ans) => { const w = clkWho(q); if (w === 'dbl') return String(ans) === String(q.answer); return w === 'tn' ?")
rep("answerLabel: (q) => { const w = clkWho(q); return w === 'tn' ?", "answerLabel: (q) => { const w = clkWho(q); if (w === 'dbl') return q.L + q.sym + ' = ' + q.eq; return w === 'tn' ?")
rep("Question: (p) => { const w = p.q ? clkWho(p.q) : 'sac'; return w === 'tn' ?", "Question: (p) => { const w = p.q ? clkWho(p.q) : 'sac'; if (w === 'dbl') return <DblQuestion {...p}/>; return w === 'tn' ?")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
