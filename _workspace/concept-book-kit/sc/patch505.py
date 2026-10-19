#!/usr/bin/env python3
# Phase 505 (her 2026-10-19 11:07):
#  - The order screen: '−' and '+' take the last sharp (flat) away or bring it back, one at a time, with the staff, the numbers,
#    the sentence and the zigzag on the keyboard following; '+' sounds the note it adds. The Sharps/Flats chips go: Next moves from the sharp order
#    to the flat order (with a Back); fewer buttons.
#  - 'Explore' goes from the Key finder and the Scale finder (the learning screens teach only what is being learned), and the circle of fifths
#    leaves the Key finder (it is its own tool): four steps again: the orders, the major key, the minor key, before a piece. Concept book: ten pages.
import sys
s = open(sys.argv[1], encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, 'found %d (want %d): %s' % (s.count(a), n, a[:90])
    s = s.replace(a, b)

# ---- the order screen: stepper ----
rep("  else if (ran) order.slice(0, lit).forEach((nm, i) => { marks[kidx(nm)] = i === lit - 1 ? 'pick' : 'mate'; });",
    "  else if (ran || phase === 'order') order.slice(0, lit).forEach((nm, i) => { marks[kidx(nm)] = i === lit - 1 ? 'pick' : 'mate'; });")
rep("  const trail = ran && !done && lit > 0 ?", "  const trail = (ran || phase === 'order') && !done && lit > 0 ?")
rep("numbers={ran} upto={ran && lit > 0 ? lit - 1 : undefined}/>", "numbers={ran || phase === 'order'} upto={(ran || phase === 'order') && lit > 0 ? lit - 1 : undefined}/>")
rep("  const say = () => { clear(); setLit(0); setRan(true);",
    "  const less = () => { clear(); if (n > 1) { setN(n - 1); setLit(n - 1); } };\n  const add = () => { clear(); if (n < 7) { setN(n + 1); setLit(n + 1); playKey(pcOfName(order[n]), 0.45); } };\n  const say = () => { clear(); setLit(0); setRan(true);")
# order phase body: stepper instead of nothing; the Say button smaller
rep("    <div style={{textAlign:'center',margin:'4px 0 10px'}}><button className=\"ghost-btn\" style={{...KF_BTN,minWidth:120}} onClick={say}>{t('▶ Say the order', '▶ 순서 듣기')}</button></div>\n    {board}\n    <KfNext go={mode === 'order' ? go : startFind} label={goLabel}/>",
    "    <div style={{display:'flex',gap:8,alignItems:'center',justifyContent:'center',margin:'4px 0 8px'}}>\n      <button className=\"ghost-btn\" aria-label={t('One less', '하나 빼기')} disabled={n <= 1} style={{...KF_BTN,minWidth:52,padding:0,fontSize:22,opacity:n <= 1 ? 0.35 : 1}} onClick={less}>−</button>\n      <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:120}} onClick={say}>{t('▶ Say the order', '▶ 순서 듣기')}</button>\n      <button className=\"ghost-btn\" aria-label={t('One more', '하나 더하기')} disabled={n >= 7} style={{...KF_BTN,minWidth:52,padding:0,fontSize:22,opacity:n >= 7 ? 0.35 : 1}} onClick={add}>+</button>\n    </div>\n    {board}\n    <KfNext go={mode === 'order' ? go : startFind} label={goLabel} back={backFn}/>")
rep("function KfFind({ type, go, setKi, mode, goLabel, onBack }) {", "function KfFind({ type, go, setKi, mode, goLabel, onBack, backFn }) {")
rep("function KfNext({ go, label }) {\n  const kc = React.useContext(KfCtx);\n  return <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{kc && kc.step > 1 && <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => kc.setStep(kc.step - 1)}>",
    "function KfNext({ go, label, back }) {\n  const kc = React.useContext(KfCtx);\n  return <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{((kc && kc.step > 1) || back) && <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={back || (() => kc.setStep(kc.step - 1))}>")
# the orders: no Sharps/Flats chips; Next goes sharp -> flat, Back flat -> sharp
a = s.index("function KfOrders({ go, setKi }) {")
b = s.index("function KfRule(")
s = s[:a] + """function KfOrders({ go, setKi }) {
  const [ty, setTy] = useState('sharp');
  return <KfFind key={ty} type={ty} mode="order" setKi={setKi} go={ty === 'sharp' ? () => setTy('flat') : go} goLabel={ty === 'sharp' ? t('Flat order →', '플랫 순서 →') : t('Next →', '다음 →')} backFn={ty === 'flat' ? () => setTy('sharp') : undefined}/>;
}
""" + s[b:]

# ---- no Explore buttons ----
for _ in range(2):
    i = s.index("      <div style={{textAlign:'center',marginTop:12}}><button className=\"ghost-btn\" style={{minHeight:44,fontSize:13,fontWeight:700,color:'#5a5d8f'}} onClick={() => setStep(0)}>{t('Explore', '더 둘러보기')}</button></div>\n")
    j = s.index("\n", i) + 1
    s = s[:i] + s[j:]

# ---- Key finder: four steps again ----
rep("{t('← The five steps', '← 다섯 단계')}", "{t('← The four steps', '← 네 단계')}")
rep("aria-label={t('Five steps', '다섯 단계')}", "aria-label={t('Four steps', '네 단계')}")
rep("const nv = ((step - 1 + d + 5) % 5) + 1; setStep(nv); const el = document.getElementById('kf-tab-'", "const nv = ((step - 1 + d + 4) % 4) + 1; setStep(nv); const el = document.getElementById('kf-tab-'")
rep("{[1, 2, 3, 4, 5].map(i => <button key={i} id={'kf-tab-' + i}", "{[1, 2, 3, 4].map(i => <button key={i} id={'kf-tab-' + i}")
rep("const go = () => setStep(s => Math.min(5, s + 1));", "const go = () => setStep(s => Math.min(4, s + 1));")
rep("      {step === 4 && <KfCircle key=\"circle\" i={ki} setI={setKi} go={go}/>}\n      {step === 5 && <KfPiece i={ki} setI={setKi}/>}", "      {step === 4 && <KfPiece i={ki} setI={setKi}/>}")
rep("t('Find the minor key', '단조 찾기'), t('Circle of fifths', '5도권'), t('Before a piece', '곡 치기 전에')];", "t('Find the minor key', '단조 찾기'), t('Before a piece', '곡 치기 전에')];")
rep("jump = [1, 2, 5];", "jump = [1, 2, 4];")
rep("onClick={() => kc.setStep(4)}>{t('← Back', '← 이전')}</button><a className", "onClick={() => kc.setStep(3)}>{t('← Back', '← 이전')}</button><a className")
rep("blurb: 'Five short steps: the orders, the major key, the minor key, the circle of fifths, before a piece.'", "blurb: 'Four short steps: the orders, the major key, the minor key, before a piece.'")
rep("'다섯 단계: 순서, 장조 찾기, 단조 찾기, 5도권, 곡 치기 전에.'", "'네 단계: 순서, 장조 찾기, 단조 찾기, 곡 치기 전에.'")
rep("['Five steps: find the key from its signature', '다섯 단계: 조표로 조 찾기']", "['Four steps: find the key from its signature', '네 단계: 조표로 조 찾기']")
rep("['Five short steps to find any key.', '조를 찾는 다섯 단계예요.']", "['Four short steps to find any key.', '조를 찾는 네 단계예요.']")
rep("blurb: 'Five steps to find the key, three to play the scales.'", "blurb: 'Four steps to find the key, three to play the scales.'")
rep("'조 찾기 다섯 단계, 스케일 치기 세 단계.'", "'조 찾기 네 단계, 스케일 치기 세 단계.'", 2)
rep("Find the key in five steps, play the scales in three.", "Find the key in four steps, play the scales in three.")
rep(" Right hand, left hand, both. Explore any scale, major or minor.", " Right hand, left hand, both.")
rep(" 맨 아래 “더 둘러보기”에서는 장조·단조 어떤 스케일이든 찾아요.", "")

# ---- the concept book: ten pages, no circle page ----
rep("' of 5', '조 찾기 · 5단계 중 ' + n + '단계'", "' of 4', '조 찾기 · 4단계 중 ' + n + '단계'")
a = s.index("    P(6, kk(4), t('Every key, in one circle'")
b = s.index("    P(7, kk(5), t('Before you play the piece'")
s = s[:a] + s[b:]
rep("    P(7, kk(5), t('Before you play the piece'", "    P(6, kk(4), t('Before you play the piece'")
rep("P(8, sk(1)", "P(7, sk(1)"); rep("P(9, sk(2)", "P(8, sk(2)"); rep("P(10, sk(3)", "P(9, sk(3)")
rep('<LbPage key="11" no={11} chId={ch}', '<LbPage key="10" no={10} chId={ch}')
rep("[t('Minor', '단조'), 5], [t('Circle of fifths', '5도권'), 6], [t('Before a piece', '곡 치기 전에'), 7],\n    [t('White keys', '흰건반'), 8], [t('Black keys', '검은건반'), 9], [t('All twelve', '열두 조'), 10],",
    "[t('Minor', '단조'), 5], [t('Before a piece', '곡 치기 전에'), 6],\n    [t('White keys', '흰건반'), 7], [t('Black keys', '검은건반'), 8], [t('All twelve', '열두 조'), 9],")
rep("{i < 6 ? t('Key: '", "{i < 5 ? t('Key: '")
rep("fontWeight:800}}>11</span></div>", "fontWeight:800}}>10</span></div>")
rep("'I can name the major key from its key signature and find it on the circle of fifths', '조표를 보고 장조 이름을 말하고, 5도권에서 찾을 수 있어요'", "'I can name the major key from its key signature', '조표를 보고 장조 이름을 말할 수 있어요'")
open(sys.argv[2], 'w', encoding='utf-8').write(s); print('ok')
