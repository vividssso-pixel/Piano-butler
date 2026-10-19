import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
old_start="      <Q q={q} level={lv} given={given} locked={phase !== 'ask'} onAnswer={answer} pixel={isGame} stats={{ correct, asked, streak }} />\n\n      <div style={{minHeight:isGame?34:44,marginTop:14,textAlign:'center'}}>"
a=s.index(old_start); b=s.index("      {!isGame && pendingNext && (",a)
new="""      {drill.feedbackAbove && !isGame
        ? <div style={{display:'flex',flexDirection:'column'}}>
            <Q q={q} level={lv} given={given} locked={phase !== 'ask'} onAnswer={answer} pixel={isGame} stats={{ correct, asked, streak }} fbAbove />
            <div style={{order:1,minHeight:44,margin:'10px 0 2px',textAlign:'center'}}>{feedback && <DrillFeedback given={given} isGame={isGame} drill={drill} q={q}/>}</div>
          </div>
        : <>
            <Q q={q} level={lv} given={given} locked={phase !== 'ask'} onAnswer={answer} pixel={isGame} stats={{ correct, asked, streak }} />
            <div style={{minHeight:isGame?34:44,marginTop:14,textAlign:'center'}}>{feedback && <DrillFeedback given={given} isGame={isGame} drill={drill} q={q}/>}</div>
          </>}
"""
s=s[:a]+new+s[b:]
# the feedback line as one piece
rep("// ─── Concept 1: Note names on the keyboard (Learn + Drill share PC_INFO) ─────────","""// Phase 540: the right / not quite line (shared; a drill with feedbackAbove shows it between the question and the buttons)
function DrillFeedback({ given, isGame, drill, q }) {
  return given.ok ? (
    <div style={{color:isGame?'#8fd3b9':'var(--good)',fontWeight:800,fontSize:isGame?11:17}}>{isGame ? 'NICE!' : t('Correct!', '정답!')}</div>
  ) : (
    <div style={{color:isGame?'#f08c70':'var(--bad)',fontWeight:800,fontSize:isGame?9:15,lineHeight:1.6}}>
      {given.timedOut ? (isGame ? 'TIME UP! ' : t('Time’s up: ', '시간이 다 됐어요. ')) : (isGame ? 'MISS! ' : t('Not quite: ', '아쉬워요. '))}
      {isGame ? 'IT WAS ' + drill.answerLabel(q).toUpperCase() : t('it was ' + drill.answerLabel(q), '정답: ' + drill.answerLabel(q))}
    </div>
  );
}
// ─── Concept 1: Note names on the keyboard (Learn + Drill share PC_INFO) ─────────""")
# the key signatures drill opts in
rep("Object.assign(KEYSIG_DRILL, { levels: SKG_LEVELS,","Object.assign(KEYSIG_DRILL, { feedbackAbove: true, levels: SKG_LEVELS,")
# the questions: root is display:contents so the feedback can sit between the staff and the choices
rep("function KnQuestion({ q, given, locked, onAnswer, pixel }) {","function KnQuestion({ q, given, locked, onAnswer, pixel, fbAbove }) {")
rep("  return <div><BoardTrack b={board} pixel={pixel}/>{top}\n    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8,marginTop:8}}>","  return <div style={fbAbove ? {display:'contents'} : undefined}><BoardTrack b={board} pixel={pixel}/>{top}\n    <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8,marginTop:8,order:2}}>")
rep("function SkgQuestion({ q, given, locked, onAnswer, pixel }) {","function SkgQuestion({ q, given, locked, onAnswer, pixel, fbAbove }) {")
a=s.index("function SkgQuestion({ q, given, locked, onAnswer, pixel, fbAbove }) {"); b=s.index("function skgCheck(")
seg=s[a:b]
g1="gap:8}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { stopClicks(); onAnswer(c); }}"
assert seg.count(g1)==1, seg.count(g1)
seg=seg.replace(g1,"gap:8,order:2}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { stopClicks(); onAnswer(c); }}")
w1="<div style={{display:'grid',gridTemplateColumns:'1fr',gap:8}}>{q.choices.map((c, i) =>"
assert seg.count(w1)==1, seg.count(w1)
seg=seg.replace(w1,"<div style={{display:'grid',gridTemplateColumns:'1fr',gap:8,order:2}}>{q.choices.map((c, i) =>")
r1="return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;"
assert seg.count(r1)==1
seg=seg.replace(r1,"return <div style={fbAbove ? {display:'contents'} : undefined}><BoardTrack b={board} pixel={pixel}/>{body}</div>;")
s=s[:a]+seg+s[b:]
rep("<button className=\"primary-btn\" onClick={goNext}>{t('Next →', '다음 →')}</button>","<button className=\"primary-btn\" style={drill.feedbackAbove ? {marginTop:16} : undefined} onClick={goNext}>{t('Next →', '다음 →')}</button>")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
