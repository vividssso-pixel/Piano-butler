#!/usr/bin/env python3
# Phase 503 (her 2026-10-19 09:34): the Key finder follows her order of teaching.
#  1. The orders: learn the sharp order, then the flat order (seven of each) -- nothing else.
#  2. The major key: sharps first (rule screen = a beat to breathe, then 1..7 unfold), then flats the same way (their own rule is different).
#  3. The minor, 4. the circle, 5. before a piece.  The concept book follows (11 pages).
import sys
s = open(sys.argv[1], encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, 'found %d (want %d): %s' % (s.count(a), n, a[:90])
    s = s.replace(a, b)

# ---- KfFind: modes ----
rep("function KfFind({ type, go, setKi }) {", "function KfFind({ type, go, setKi, mode, goLabel, onBack }) {   // mode 'order' = only the order; mode 'find' = only the unfolding count")
rep("  const [n, setN] = useState(7);\n  const [lit, setLit] = useState(7);", "  const [n, setN] = useState(mode === 'find' ? 1 : 7);\n  const [lit, setLit] = useState(mode === 'find' ? 1 : 7);")
rep("useState('order');   // Phase 502", "useState(mode === 'find' ? 'find' : 'order');   // Phase 502")
rep("{sharp ? t('Sharps always come in this order.', '샤프는 언제나 이 순서로 붙어요.') : t('Flats come in the same order, backwards.', '플랫은 같은 순서를 거꾸로 붙어요.')}",
    "{sharp ? t('Seven sharps, always in this order.', '샤프는 일곱 개, 언제나 이 순서로 붙어요.') : t('Seven flats, the same order backwards.', '플랫도 일곱 개, 같은 순서를 거꾸로 붙어요.')}")
rep("    <KfNext go={startFind}/>\n  </>);\n  const prim", "    <KfNext go={mode === 'order' ? go : startFind} label={goLabel}/>\n  </>);\n  const prim")
rep("    <KfChain hi={[0, 1]}/>\n    <div style={titleStyle}>\n      {done ?", "    <KfChain hi={mode === 'find' ? [1] : [0, 1]}/>\n    <div style={titleStyle}>\n      {done ?")
rep("onClick={toOrder}>{t('← The order', '← 순서')}</button>", "onClick={mode === 'find' ? onBack : toOrder}>{mode === 'find' ? t('← The rule', '← 규칙') : t('← The order', '← 순서')}</button>")
rep("<button className=\"ghost-btn\" style={prim} onClick={go}>{t('Next →', '다음 →')}</button>)}", "<button className=\"ghost-btn\" style={prim} onClick={go}>{goLabel || t('Next →', '다음 →')}</button>)}")

# ---- new screens ----
NEW = r'''function KfOrders({ go, setKi }) {
  const [ty, setTy] = useState('sharp');
  const seg = (v, l) => <button key={v} className={'chip' + (ty === v ? ' active' : '')} aria-pressed={ty === v} style={{...KF_BTN,flex:'1 1 0',minWidth:0}} onClick={() => setTy(v)}>{l}</button>;
  return (<>
    <div style={{display:'flex',gap:6,marginBottom:6}}>{seg('sharp', t('Sharps ♯', '샤프 ♯'))}{seg('flat', t('Flats ♭', '플랫 ♭'))}</div>
    <KfFind key={ty} type={ty} mode="order" setKi={setKi} go={ty === 'sharp' ? () => setTy('flat') : go} goLabel={ty === 'sharp' ? t('Flat order →', '플랫 순서 →') : t('Next →', '다음 →')}/>
  </>);
}
function KfRule({ type, go, back }) {
  const kc = React.useContext(KfCtx), sharp = type === 'sharp', n = 3, k = KEY_BY_COUNT(type, n), marks = {};
  if (sharp) marks[pcOfName(SHARP_ORDER[2])] = 'mate';
  marks[pcOfName(k.major)] = 'pick';
  return (<>
    <KfChain hi={[1]}/>
    <div style={{textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'}}>{sharp ? t('Sharps: find the key', '샤프로 조 찾기') : t('Flats: find the key', '플랫으로 조 찾기')}</div>
    <div style={{maxWidth:260,margin:'0 auto'}}><KSStaff count={n} type={type} width={200} upto={sharp ? n - 1 : n - 2}/></div>
    <div style={{maxWidth:300,margin:'4px auto 0'}}><TapKeyboard octaves={1} marks={marks} labels="all" bigLabels/></div>
    <div style={{textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',margin:'6px 0 2px'}}>{n}{sharp ? '♯' : '♭'} → <span style={{color:'#c0431f'}}>{majName(k)}</span></div>
    <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'6px 0 0',textWrap:'balance'}}>{sharp ? t('The key is a half step above the last ♯.', '장조는 마지막 샤프의 반음 위예요.') : t('The key is the second-to-last ♭. One flat is F.', '장조는 뒤에서 두 번째 플랫이에요. 플랫이 하나면 F.')}</div>
    <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>
      <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={back || (() => kc && kc.setStep(1))}>{t('← Back', '← 이전')}</button>
      <button className="ghost-btn" style={{...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'}} onClick={go}>{t('Try it →', '해 보기 →')}</button>
    </div>
  </>);
}
function KfMajor({ go, setKi }) {
  const [st, setSt] = useState('sharp-rule');
  if (st === 'sharp-rule') return <KfRule type="sharp" go={() => setSt('sharp')}/>;
  if (st === 'sharp') return <KfFind key="fs" type="sharp" mode="find" setKi={setKi} go={() => setSt('flat-rule')} goLabel={t('Now flats →', '이제 플랫 →')} onBack={() => setSt('sharp-rule')}/>;
  if (st === 'flat-rule') return <KfRule type="flat" go={() => setSt('flat')} back={() => setSt('sharp')}/>;
  return <KfFind key="ff" type="flat" mode="find" setKi={setKi} go={go} onBack={() => setSt('flat-rule')}/>;
}
function KfNav('''
rep("function KfNav(", NEW)
rep("const kc = React.useContext(KfCtx), jump = [1, 3, 5];", "const kc = React.useContext(KfCtx), jump = [1, 2, 5];")
rep("const names = [null, t('Sharps', '샤프'), t('Flats', '플랫'), t('Major and minor', '장조와 단조'), t('Circle of fifths', '5도권'), t('Before a piece', '곡 치기 전에')];",
    "const names = [null, t('The orders', '순서'), t('Find the major key', '장조 찾기'), t('Find the minor key', '단조 찾기'), t('Circle of fifths', '5도권'), t('Before a piece', '곡 치기 전에')];")
rep("      {step === 1 && <KfFind key=\"sharp\" type=\"sharp\" go={go} setKi={setKi}/>}\n      {step === 2 && <KfFind key=\"flat\" type=\"flat\" go={go} setKi={setKi}/>}",
    "      {step === 1 && <KfOrders go={go} setKi={setKi}/>}\n      {step === 2 && <KfMajor go={go} setKi={setKi}/>}")

# words
rep("blurb: 'Five short steps: sharps, flats, major and minor, the circle of fifths, before a piece.'", "blurb: 'Five short steps: the orders, the major key, the minor key, the circle of fifths, before a piece.'")
rep("'다섯 단계: 샤프, 플랫, 장조와 단조, 5도권, 곡 치기 전에.'", "'다섯 단계: 순서, 장조 찾기, 단조 찾기, 5도권, 곡 치기 전에.'")

# ---- the concept book: 11 pages ----
rep("function CbPiecePic() {", r'''function CbOrdersPic() {
  const row = (type) => <div style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4}}>
    <div style={{width:'100%',maxWidth:380}}><KSStaff count={7} type={type} width={300}/></div>
    <div style={{display:'flex',flexWrap:'wrap',gap:'0 9px',justifyContent:'center',fontSize:19,fontWeight:800,color:'#26296b'}}>{KF_WORDS[type].map((w, i) => <span key={i}>{w}</span>)}</div>
  </div>;
  return <div role="img" aria-label={t('The seven sharps in order, F C G D A E B, and the seven flats in order, B E A D G C F, on the staff, with the sentence for each.', '샤프 일곱 개의 순서 F C G D A E B와 플랫 일곱 개의 순서 B E A D G C F를 오선에 그리고, 각각 문장을 붙였어요.')} style={{display:'flex',flexDirection:'column',gap:30,width:'100%',maxWidth:560}}>
    <div aria-hidden="true">{row('sharp')}</div><div aria-hidden="true">{row('flat')}</div>
  </div>;
}
function CbPiecePic() {''')
rep("    P(2, kk(1), t('What key has 3♯?'", "    P(2, kk(1), t('The orders', '샤프와 플랫의 순서'), <CbOrdersPic/>,\n      X('Seven sharps, seven flats: learn each order first.', '샤프 일곱 개, 플랫 일곱 개: 순서부터 익혀요.'),\n      X('Sharps F C G D A E B. Flats B E A D G C F.', '샤프 F C G D A E B. 플랫 B E A D G C F.')),\n    P(3, kk(2), t('What key has 3♯?'")
rep("X('Say the sharps in order. The key is a half step above the last ♯.', '샤프를 순서대로 말해요. 마지막 샤프의 반음 위가 그 조예요.')", "X('Sharps: the key is a half step above the last ♯.', '샤프: 장조는 마지막 샤프의 반음 위예요.')")
rep("      X('Sharps F C G D A E B. The key is a half step above the last ♯.', '샤프 F C G D A E B. 마지막 샤프의 반음 위가 장조.')),", "      X('Count the sharps in the order, then go a half step up.', '순서대로 샤프를 세고, 반음 위로 가요.')),")
rep("    P(3, kk(2), t('What key has 3♭?'", "    P(4, kk(2), t('What key has 3♭?'")
rep("X('Say the flats in order. The key is the second-to-last ♭. One flat is F.', '플랫을 말해요. 뒤에서 두 번째 플랫이 그 조예요. 하나면 F.')", "X('Flats: the key is the second-to-last ♭. One flat is F.', '플랫: 장조는 뒤에서 두 번째 플랫이에요. 하나면 F.')")
rep("      X('Flats B E A D G C F. The key is the second-to-last ♭.', '플랫 B E A D G C F. 뒤에서 두 번째 플랫이 장조.')),", "      X('Sharps and flats find the key in different ways.', '샤프와 플랫은 장조를 찾는 방법이 달라요.')),")
rep("    P(4, kk(3), t('Is it major or minor?'", "    P(5, kk(3), t('Is it major or minor?'")
rep("    P(5, kk(4), t('Every key, in one circle'", "    P(6, kk(4), t('Every key, in one circle'")
rep("    P(6, kk(5), t('Before you play the piece'", "    P(7, kk(5), t('Before you play the piece'")
rep("P(7, sk(1)", "P(8, sk(1)"); rep("P(8, sk(2)", "P(9, sk(2)"); rep("P(9, sk(3)", "P(10, sk(3)")
rep('<LbPage key="10" no={10} chId={ch}', '<LbPage key="11" no={11} chId={ch}')
rep("""    [t('Sharps', '샤프'), 2], [t('Flats', '플랫'), 3], [t('Major and minor', '장조와 단조'), 4], [t('Circle of fifths', '5도권'), 5], [t('Before a piece', '곡 치기 전에'), 6],
    [t('White keys', '흰건반'), 7], [t('Black keys', '검은건반'), 8], [t('All twelve', '열두 조'), 9],""",
"""    [t('The orders', '순서'), 2], [t('Sharps: the key', '샤프: 장조'), 3], [t('Flats: the key', '플랫: 장조'), 4], [t('Minor', '단조'), 5], [t('Circle of fifths', '5도권'), 6], [t('Before a piece', '곡 치기 전에'), 7],
    [t('White keys', '흰건반'), 8], [t('Black keys', '검은건반'), 9], [t('All twelve', '열두 조'), 10],""")
rep("{i < 5 ? t('Key: '", "{i < 6 ? t('Key: '")
rep("fontWeight:800}}>10</span></div>", "fontWeight:800}}>11</span></div>")
open(sys.argv[2], 'w', encoding='utf-8').write(s); print('ok')
