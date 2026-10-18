#!/usr/bin/env python3
# Phase 501 (her 2026-10-19 09:25: 'there is no button back to Read it'): the Key finder gets a Back button beside Next on steps 2 to 5,
# and the three pills (Read it / Name the key / Play its scale) become buttons that jump to step 1 / 3 / 5.
import sys
s = open(sys.argv[1], encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, 'found %d (want %d): %s' % (s.count(a), n, a[:90])
    s = s.replace(a, b)

rep("function KfChain({ hi }) {\n  const items = [t('Read it', '읽기'), t('Name the key', '조 찾기'), t('Play its scale', '스케일 치기')];\n  return (",
    "const KfCtx = React.createContext(null);\nfunction KfChain({ hi }) {\n  const items = [t('Read it', '읽기'), t('Name the key', '조 찾기'), t('Play its scale', '스케일 치기')];\n  const kc = React.useContext(KfCtx), jump = [1, 3, 5];\n  return (")
rep("{items.map((l, i) => <React.Fragment key={i}>{i > 0 && <span style={{color:'#a3a5c2',fontWeight:800,fontSize:12}}>→</span>}<span style={{flex:'1 1 0',minWidth:0,textAlign:'center',lineHeight:1.2,padding:'5px 4px',borderRadius:14,fontSize:11.5,fontWeight:800,background:hi.includes(i) ? '#e4572e' : '#efe8d6',color:hi.includes(i) ? '#fff' : '#26296b'}}>{l}</span></React.Fragment>)}",
    "{items.map((l, i) => <React.Fragment key={i}>{i > 0 && <span style={{color:'#a3a5c2',fontWeight:800,fontSize:12}}>→</span>}{kc ? <button type=\"button\" aria-current={hi.includes(i) ? 'step' : undefined} onClick={() => kc.setStep(jump[i])} style={{flex:'1 1 0',minWidth:0,minHeight:44,cursor:'pointer',textAlign:'center',lineHeight:1.2,padding:'5px 4px',border:0,borderRadius:22,fontFamily:'inherit',fontSize:11.5,fontWeight:800,background:hi.includes(i) ? '#e4572e' : '#efe8d6',color:hi.includes(i) ? '#fff' : '#26296b'}}>{l}</button> : <span style={{flex:'1 1 0',minWidth:0,textAlign:'center',lineHeight:1.2,padding:'5px 4px',borderRadius:14,fontSize:11.5,fontWeight:800,background:hi.includes(i) ? '#e4572e' : '#efe8d6',color:hi.includes(i) ? '#fff' : '#26296b'}}>{l}</span>}</React.Fragment>)}")
rep("function KfNext({ go, label }) {\n  return <div style={{textAlign:'center',marginTop:14}}><button",
    "function KfNext({ go, label }) {\n  const kc = React.useContext(KfCtx);\n  return <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>{kc && kc.step > 1 && <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => kc.setStep(kc.step - 1)}>{t('← Back', '← 이전')}</button>}<button")
# KfPiece has no Next: give it a Back
rep("    <div style={{textAlign:'center',marginTop:14}}><a className=\"ghost-btn\" style={{...KF_BTN,display:'inline-flex'",
    "    <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}><button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => kc.setStep(4)}>{t('← Back', '← 이전')}</button><a className=\"ghost-btn\" style={{...KF_BTN,display:'inline-flex'")
rep("function KfPiece({ i, setI }) {\n  const ks = KEY_SIGS[i];", "function KfPiece({ i, setI }) {\n  const ks = KEY_SIGS[i], kc = React.useContext(KfCtx);")
rep("      {step === 1 && <KfFind key=\"sharp\"", "      <KfCtx.Provider value={{ step, setStep }}>\n      {step === 1 && <KfFind key=\"sharp\"")
rep("      {step === 5 && <KfPiece i={ki} setI={setKi}/>}", "      {step === 5 && <KfPiece i={ki} setI={setKi}/>}\n      </KfCtx.Provider>")
open(sys.argv[2], 'w', encoding='utf-8').write(s); print('ok')
