import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# a right answer waits long enough to look at (and Next skips the wait)
rep("    else if (ok) later(() => advance(s), 700);\n    else setPendingNext(s);","    else if (ok) { later(() => advance(s), 2000); setPendingNext(s); }   // Phase 536: a right answer stays on screen for 2 s; Next goes on sooner\n    else setPendingNext(s);")
rep("  function goNext() { const s = pendingNext; setPendingNext(null); advance(s); }","  function goNext() { const s = pendingNext; timers.current.forEach(clearTimeout); timers.current = []; setPendingNext(null); advance(s); }")
# circle of fifths: the grand staff
rep("""        <div style={{maxWidth:200,margin:'2px auto 0'}}><KSStaff count={sg.count} type={sg.type} width={170}/></div>
        <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'4px 0 0'}}>{t('Clockwise: one more ♯.""","""        <div style={{display:'flex',alignItems:'stretch',justifyContent:'center',gap:4,margin:'4px auto 0',maxWidth:220}} role="img" aria-label={t('The key signature on the treble and bass staves', '높은음자리표와 낮은음자리표의 조표')}>
          <svg width="14" viewBox="0 0 10 100" preserveAspectRatio="none" aria-hidden="true" style={{flex:'none'}}><path d="M9 2 C2 16 2 36 4 50 C2 64 2 84 9 98" fill="none" stroke="#26296b" strokeWidth="1.8" vectorEffect="non-scaling-stroke"/></svg>
          <div style={{flex:'1 1 auto',minWidth:0}}><KSStaff count={sg.count} type={sg.type} width={170}/><KSStaff count={sg.count} type={sg.type} width={170} clef="bass"/></div>
        </div>
        <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'4px 0 0'}}>{t('Clockwise: one more ♯.""")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
