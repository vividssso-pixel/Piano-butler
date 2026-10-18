#!/usr/bin/env python3
# Phase 498: (1) scale keyboard: note name and finger number sit balanced inside the key (her 09:15: the letters were too high);
# (2) the Key finder gets a fifth step, the circle of fifths (her 'yes' to my recommendation), and the concept book a page for it.
import sys
s = open(sys.argv[1], encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, 'found %d (want %d): %s' % (s.count(a), n, a[:90])
    s = s.replace(a, b)

# 1. keyboard labels
rep('y={whiteH-36} textAnchor="middle" fontSize="13"', 'y={whiteH-24} textAnchor="middle" fontSize="13"')
rep('y={whiteH-14} textAnchor="middle" fontSize="14"', 'y={whiteH-7} textAnchor="middle" fontSize="14"')
rep('y={blackH-33} textAnchor="middle" fontSize="11"', 'y={blackH-36} textAnchor="middle" fontSize="11"')
rep('y={blackH-15} textAnchor="middle" fontSize="13" fontWeight="900" fill="#fff"', 'y={blackH-18} textAnchor="middle" fontSize="13" fontWeight="900" fill="#fff"')

# 2. Key finder: five steps
CIRCLE = r'''function KfCircle({ i, setI, go }) {
  const ks = KEY_SIGS[i];
  const [sel, setSel] = useState(FIFTHS.includes(ks.major) ? ks.major : 'C');
  const sg = KEY_SIGS.find(x => x.major === sel) || KEY_SIGS[0];
  const pick = (k) => { setSel(k); playKey(pcOfName(k), 0.5); const j = KEY_SIGS.findIndex(q => q.major === k); if (j >= 0) setI(j); };
  return (<>
    <KfChain hi={[1]}/>
    <div style={{textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 6px',textWrap:'balance'}}>{t('Every key, in one circle', '모든 조를 한 바퀴에')}</div>
    <div style={{maxWidth:290,margin:'0 auto'}}><FifthsRing sel={sel} onPick={pick} o={{ filled: [], twins: true, minors: true }} label={t('The circle of fifths, ' + skgKeyName(sel) + ' ringed; inside each key, its relative minor.', '5도권: ' + skgKeyName(sel) + '에 동그라미. 조마다 안쪽에 그 나란한조.')}/></div>
    <div style={{maxWidth:200,margin:'2px auto 0'}}><KSStaff count={sg.count} type={sg.type} width={170}/></div>
    <div style={{textAlign:'center',fontSize:14,fontWeight:800,color:'#26296b',margin:'2px 0 4px',textWrap:'balance'}}>{cbKeyLines(sel)[0]}</div>
    <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'6px 0 0'}}>{t('Clockwise: one more ♯. Anticlockwise: one more ♭.', '시계 방향은 샤프 하나 더, 반시계 방향은 플랫 하나 더.')}</div>
    <KfNext go={go}/>
  </>);
}
function KfPiece({ i, setI }) {'''
rep("function KfPiece({ i, setI }) {", CIRCLE)
rep("t('Major and minor', '장조와 단조'), t('Before a piece', '곡 치기 전에')];\n  const go = () => setStep(s => Math.min(4, s + 1));",
    "t('Major and minor', '장조와 단조'), t('Circle of fifths', '5도권'), t('Before a piece', '곡 치기 전에')];\n  const go = () => setStep(s => Math.min(5, s + 1));")
rep("{t('← The four steps', '← 네 단계')}", "{t('← The five steps', '← 다섯 단계')}")
rep("aria-label={t('Four steps', '네 단계')}", "aria-label={t('Five steps', '다섯 단계')}")
rep("const nv = ((step - 1 + d + 4) % 4) + 1; setStep(nv); const el = document.getElementById('kf-tab-'", "const nv = ((step - 1 + d + 5) % 5) + 1; setStep(nv); const el = document.getElementById('kf-tab-'")
rep("{[1, 2, 3, 4].map(i => <button key={i} id={'kf-tab-' + i}", "{[1, 2, 3, 4, 5].map(i => <button key={i} id={'kf-tab-' + i}")
rep("      {step === 4 && <KfPiece i={ki} setI={setKi}/>}", "      {step === 4 && <KfCircle key=\"circle\" i={ki} setI={setKi} go={go}/>}\n      {step === 5 && <KfPiece i={ki} setI={setKi}/>}")
# words
rep("blurb: 'Four short steps: sharps, flats, major and minor, before a piece.'", "blurb: 'Five short steps: sharps, flats, major and minor, the circle of fifths, before a piece.'")
rep("'네 단계: 샤프, 플랫, 장조와 단조, 곡 치기 전에.'", "'다섯 단계: 샤프, 플랫, 장조와 단조, 5도권, 곡 치기 전에.'")
rep("'key-finder': ['Four short steps to find any key.', '조를 찾는 네 단계예요.'],", "'key-finder': ['Five short steps to find any key.', '조를 찾는 다섯 단계예요.'],")
rep("['Four steps: find the key from its signature', '네 단계: 조표로 조 찾기']", "['Five steps: find the key from its signature', '다섯 단계: 조표로 조 찾기']")
rep("blurb: 'Four steps to find the key, three to play the scales.'", "blurb: 'Five steps to find the key, three to play the scales.'")
rep("'조 찾기 네 단계, 스케일 치기 세 단계.'", "'조 찾기 다섯 단계, 스케일 치기 세 단계.'", 2)
rep("Find the key in four steps, play the scales in three.", "Find the key in five steps, play the scales in three.")

# 3. the concept book: one more page
rep("' of 4', '조 찾기 · 4단계 중 ' + n + '단계'", "' of 5', '조 찾기 · 5단계 중 ' + n + '단계'")
rep("[t('Before a piece', '곡 치기 전에'), 5],\n    [t('White keys', '흰건반'), 6], [t('Black keys', '검은건반'), 7], [t('All twelve', '열두 조'), 8],",
    "[t('Circle of fifths', '5도권'), 5], [t('Before a piece', '곡 치기 전에'), 6],\n    [t('White keys', '흰건반'), 7], [t('Black keys', '검은건반'), 8], [t('All twelve', '열두 조'), 9],")
rep("{i < 4 ? t('Key: '", "{i < 5 ? t('Key: '")
rep("fontWeight:800}}>9</span></div>", "fontWeight:800}}>10</span></div>")
rep("    P(5, kk(4), t('Before you play the piece'", "    P(5, kk(4), t('Every key, in one circle', '모든 조를 한 바퀴에'), <CbCirclePic/>,\n      X('Clockwise: one more ♯. Anticlockwise: one more ♭.', '시계 방향은 샤프 하나 더, 반시계 방향은 플랫 하나 더.'),\n      X('Inside each key is its relative minor.', '조마다 안쪽에 그 나란한조가 있어요.')),\n    P(6, kk(5), t('Before you play the piece'")
rep("P(6, sk(1)", "P(7, sk(1)"); rep("P(7, sk(2)", "P(8, sk(2)"); rep("P(8, sk(3)", "P(9, sk(3)")
rep("kk(4), t('Before you play the piece'", "kk(5), t('Before you play the piece'") if False else None
rep('<LbPage key="9" no={9} chId={ch}', '<LbPage key="10" no={10} chId={ch}')
rep("function CbPiecePic() {", """function CbCirclePic() {
  return <div role="img" aria-label={t('The circle of fifths: the twelve major keys in a ring, C at the top, each with its relative minor inside. Clockwise one more sharp, anticlockwise one more flat.', '5도권: 열두 장조가 원을 이루고 맨 위에 C, 조마다 안쪽에 나란한조. 시계 방향은 샤프 하나 더, 반시계 방향은 플랫 하나 더.')} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:14,width:'100%',maxWidth:560}}>
    <div aria-hidden="true" style={{width:'100%',maxWidth:430}}><FifthsRing o={{ filled: [], paper: true, twins: true, minors: true }}/></div>
    <div aria-hidden="true" style={{display:'flex',gap:28,fontSize:19,fontWeight:900,color:'#26296b'}}><span>{t('↻ one more ♯', '↻ 샤프 하나 더')}</span><span>{t('↺ one more ♭', '↺ 플랫 하나 더')}</span></div>
  </div>;
}
function CbPiecePic() {""")
rep("'I can name the major key from its key signature', '조표를 보고 장조 이름을 말할 수 있어요'", "'I can name the major key from its key signature and find it on the circle of fifths', '조표를 보고 장조 이름을 말하고, 5도권에서 찾을 수 있어요'")
open(sys.argv[2], 'w', encoding='utf-8').write(s); print('ok')
