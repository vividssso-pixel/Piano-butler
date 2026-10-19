import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("alignItems:'center',margin:'8px 0 4px'}}>","alignItems:'center',margin:'12px 0 18px'}}>")
rep("justifyContent:'center',margin:'0 0 10px'}}>{grpBtn","justifyContent:'center',margin:'4px 0 14px'}}>{grpBtn")
rep("const kb = <div style={{maxWidth:300,margin:'6px auto 0'}}>","const kb = <div style={{maxWidth:300,margin:tryMode ? '0 auto' : '10px auto 0'}}>")
rep("<div style={{textAlign:'center',marginTop:10,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>\n      {tryMode\n        ? <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => { setPh('rule')",
"<div style={{textAlign:'center',marginTop:tryMode ? 22 : 14,display:'flex',gap:10,justifyContent:'center',flexWrap:'wrap'}}>\n      {tryMode\n        ? <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => { setPh('rule')")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
