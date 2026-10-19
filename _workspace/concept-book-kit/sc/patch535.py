import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("  const [grp, setGrp] = useState(ks.type === 'flat' ? 'flat' : 'sharp');\n  const rows =","  const [grp, setGrp] = useState(ks.type === 'flat' ? 'flat' : 'sharp');\n  const [view, setView] = useState('list');   // Phase 535: the table, or the circle of fifths (the same keys)\n  const rows =")
rep("""    <div style={{display:'flex',gap:10,justifyContent:'center',margin:'4px 0 12px'}}>{grpBtn('sharp', t('♯ Sharp keys', '♯ 샵 조'))}{grpBtn('flat', t('♭ Flat keys', '♭ 플랫 조'))}</div>
    <div role="table\"""","""    <div role="group" aria-label={t('How to see the keys', '조를 보는 방법')} style={{display:'flex',gap:0,justifyContent:'center',margin:'0 auto 12px',maxWidth:240,border:'1.5px solid #26296b',borderRadius:999,overflow:'hidden'}}>
      {[['list', t('List', '목록')], ['circle', t('Circle', '원')]].map(([v, lab]) => <button key={v} type="button" aria-pressed={view === v} onClick={() => setView(v)} style={{flex:1,minHeight:38,border:'none',cursor:'pointer',font:'inherit',fontSize:14,fontWeight:800,background:view === v ? '#26296b' : '#fffefa',color:view === v ? '#fffefa' : '#26296b'}}>{lab}</button>)}
    </div>
    {view === 'circle' && (() => { const sel = FIFTHS.includes(ks.major) ? ks.major : 'C', sg = KEY_SIGS.find(x => x.major === sel) || KEY_SIGS[0];
      const pick = (k) => { playKey(pcOfName(k), 0.5); const j = KEY_SIGS.findIndex(q => q.major === k); if (j >= 0) setI(j); };
      return <>
        <div style={{maxWidth:290,margin:'0 auto'}}><FifthsRing sel={sel} onPick={pick} o={{ filled: [], twins: true, minors: true }} label={t('The circle of fifths, ' + skgKeyName(sel) + ' ringed; inside each key, its relative minor.', '5도권: ' + skgKeyName(sel) + '에 동그라미. 조마다 안쪽에 그 나란한조.')}/></div>
        <div style={{maxWidth:200,margin:'2px auto 0'}}><KSStaff count={sg.count} type={sg.type} width={170}/></div>
        <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'4px 0 0'}}>{t('Clockwise: one more ♯. Anticlockwise: one more ♭.', '시계 방향은 샵 하나 더, 반시계 방향은 플랫 하나 더.')}</div>
      </>; })()}
    {view === 'list' && <div style={{display:'flex',gap:10,justifyContent:'center',margin:'4px 0 14px'}}>{grpBtn('sharp', t('♯ Sharp keys', '♯ 샵 조'))}{grpBtn('flat', t('♭ Flat keys', '♭ 플랫 조'))}</div>}
    {view === 'list' && <div role="table\"""")
# close the conditional after the table's closing div (just before the guide card)
rep("""        </button>); })}
    </div>
    <div style={{maxWidth:320,margin:'12px auto 0',display:'flex'""","""        </button>); })}
    </div>}
    <div style={{maxWidth:320,margin:'12px auto 0',display:'flex'""")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
