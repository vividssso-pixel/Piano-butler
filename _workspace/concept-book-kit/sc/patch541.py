import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
def seg_replace(start, end, pairs):
    global s
    a=s.index(start); b=s.index(end,a); seg=s[a:b]
    for x,y in pairs:
        assert seg.count(x)==1,(x[:80],seg.count(x)); seg=seg.replace(x,y)
    s=s[:a]+seg+s[b:]
# feedback goes straight under the question; the picture and the buttons follow
rep("<div style={{order:1,minHeight:44,margin:'10px 0 2px',textAlign:'center'}}>","<div style={{order:1,minHeight:40,margin:'4px 0 6px',textAlign:'center'}}>")
# KnQuestion
seg_replace("function KnQuestion(","const SkgQuestionAll",[
 ("const paper = (node, mw = 240) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '4px 0',margin:'0 auto 10px',maxWidth:mw}}>","const paper = (node, mw = 240) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '4px 0',margin:'0 auto 10px',maxWidth:mw,order:2}}>"),
 ("{done ? paper(<KSStaff count={q.idx + 1} type={q.type} ink={ink} upto={q.idx} width={170}/>) : <div style={{height:8}}/>}","{done ? paper(<KSStaff count={q.idx + 1} type={q.type} ink={ink} upto={q.idx} width={170}/>) : <div style={{height:8,order:2}}/>}"),
 ("margin:'-4px 0 10px'}}>{t('Last note: '","margin:'-4px 0 10px',order:2}}>{t('Last note: '"),
 ("gap:8,marginTop:8,order:2}}>","gap:8,marginTop:8,order:3}}>"),
])
# SkgQuestion
seg_replace("function SkgQuestion(","function skgCheck(",[
 ("const paper = (node, mw = 400) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '4px 0',margin:'0 auto 10px',maxWidth:mw}}>","const paper = (node, mw = 400) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '4px 0',margin:'0 auto 10px',maxWidth:mw,order:2}}>"),
 ("gap:8,order:2}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { stopClicks(); onAnswer(c); }}","gap:8,order:3}}>{q.choices.map(c => <button key={c} disabled={locked} onClick={() => { stopClicks(); onAnswer(c); }}"),
 ("gridTemplateColumns:'1fr',gap:8,order:2}}>{q.choices.map((c, i) =>","gridTemplateColumns:'1fr',gap:8,order:3}}>{q.choices.map((c, i) =>"),
 ("<div style={{textAlign:'center',margin:'0 0 10px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={() => skgPlay(q)}","<div style={{textAlign:'center',margin:'0 0 10px',order:2}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={() => skgPlay(q)}"),
])
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
