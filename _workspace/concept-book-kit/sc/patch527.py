import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# remove the Try-it row in learn
a=s.index("      {!tryMode && <div style={{flexBasis:'100%'"); b=s.index("      {tryMode && found && go &&")
s=s[:a]+s[b:]
# compact group buttons
rep("style={{...KF_BTN,minWidth:110,...(grp === type ?","style={{...KF_BTN,minHeight:38,fontSize:14,minWidth:0,padding:'0 18px',...(grp === type ?")
rep("<div style={{display:'flex',gap:8,justifyContent:'center',margin:'0 0 6px'}}>{grpBtn","<div style={{display:'flex',gap:10,justifyContent:'center',margin:'0 0 10px'}}>{grpBtn")
# compact +/-
rep("style={{...KF_BTN,minWidth:84,fontSize:22,","style={{...KF_BTN,minHeight:38,minWidth:64,padding:0,fontSize:22,")
rep("display:'flex',gap:12,justifyContent:'center',alignItems:'center',margin:'4px 0 0'}}>","display:'flex',gap:14,justifyContent:'center',alignItems:'center',margin:'8px 0 4px'}}>")
# tighter prompt line in try
rep("minHeight:40,animation:'fadeUp 0.3s both'}}>{stageLine}","minHeight:tryMode ? 26 : 40,animation:'fadeUp 0.3s both'}}>{stageLine}")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
