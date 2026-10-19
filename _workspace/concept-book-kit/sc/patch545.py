import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("<div style={{fontSize:11.5,color:'var(--brass)',marginBottom:6}}>LEVEL {lv.n}</div>","{!lv.short && <div style={{fontSize:11.5,color:'var(--brass)',marginBottom:6}}>LEVEL {lv.n}</div>}")
rep("<span>LV {lv.n}</span><span>{streak","<span>{lv.short ? (lv.num ? lv.num + ' ' : '') + t(lv.short[0], lv.short[1]).toUpperCase() : 'LV ' + lv.n}</span><span>{streak")
rep("<div style={{fontSize:12,color:'#6d6f9c',marginBottom:18}}>Level {lv.n}: {lv.label}</div>","<div style={{fontSize:12,color:'#6d6f9c',marginBottom:18}}>{lv.short ? '' : 'Level ' + lv.n + ': '}{lv.label}</div>")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
