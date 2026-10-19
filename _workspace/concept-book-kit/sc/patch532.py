import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("gridTemplateColumns:'64px 1fr 1fr',gap:6,padding:'0 4px 6px'","gridTemplateColumns:'124px 1fr 1fr',gap:6,padding:'0 4px 6px'")
rep("gridTemplateColumns:'64px 1fr 1fr',gap:6,width:'100%',minHeight:36,","gridTemplateColumns:'124px 1fr 1fr',gap:6,width:'100%',minHeight:54,")
rep("<span style={cell}>{q.count === 0 ? '0' : q.count + (q.type === 'sharp' ? '♯' : '♭')}</span>","<span style={{...cell,padding:'2px 0'}} aria-label={sigLabel(q)}><span style={{width:120,display:'block'}}><KSStaff count={q.count} type={q.type} width={170}/></span></span>")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
