import sys,re
s=open(sys.argv[1],encoding='utf-8').read()
a=s.index("function KfPiece({ i, setI }) {"); b=s.index("function KeyFinder({ only }) {")
old=s[a:b]
m=re.search(r"<div style=\{\{textAlign:'center',marginTop:14,display:'flex'.*?</div>\n", old, re.S)
btns=m.group(0)
new = r"""function KfPiece({ i, setI }) {   // Phase 531: one table of the key signatures, major and minor side by side, and how to tell which one the piece is in
  const ks = KEY_SIGS[i], kc = React.useContext(KfCtx);
  const [grp, setGrp] = useState(ks.type === 'flat' ? 'flat' : 'sharp');
  const rows = grp === 'flat' ? [0, 8, 9, 10, 11, 12, 13, 14] : [0, 1, 2, 3, 4, 5, 6, 7];
  const head = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const grpBtn = (type, label) => <button className="ghost-btn" aria-pressed={grp === type} style={{...KF_BTN,minHeight:38,fontSize:14,minWidth:0,padding:'0 18px',...(grp === type ? {background:'#26296b',color:'#fffefa',borderColor:'#26296b'} : {})}} onClick={() => { setGrp(type); if (KEY_SIGS[i].type !== type && i !== 0) setI(type === 'sharp' ? 1 : 8); }}>{label}</button>;
  const cell = {display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800,fontSize:16,color:'#26296b'};
  const colHead = {fontSize:12,fontWeight:800,letterSpacing:'0.06em',textTransform:'uppercase',color:'#6b6f9a',textAlign:'center'};
  return (<>
    <KfChain hi={[2]}/>
    <div style={head}>{t('Before you play the piece', '곡을 치기 전에')}</div>
    <div style={{display:'flex',gap:10,justifyContent:'center',margin:'4px 0 12px'}}>{grpBtn('sharp', t('♯ Sharp keys', '♯ 샵 조'))}{grpBtn('flat', t('♭ Flat keys', '♭ 플랫 조'))}</div>
    <div role="table" style={{maxWidth:320,margin:'0 auto'}}>
      <div style={{display:'grid',gridTemplateColumns:'64px 1fr 1fr',gap:6,padding:'0 4px 6px'}}>
        <div style={colHead}>{t('Signature', '조표')}</div><div style={colHead}>{t('Major', '장조')}</div><div style={colHead}>{t('Minor', '단조')}</div>
      </div>
      {rows.map(j => { const q = KEY_SIGS[j], on = j === i; return (
        <button key={j} type="button" role="row" aria-pressed={on} onClick={() => setI(j)} style={{display:'grid',gridTemplateColumns:'64px 1fr 1fr',gap:6,width:'100%',minHeight:36,padding:'0 4px',margin:'0 0 3px',border:'1px solid ' + (on ? '#e4572e' : 'rgba(38,41,107,0.12)'),borderRadius:8,background:on ? '#fbe3da' : '#fffefa',cursor:'pointer',font:'inherit'}}>
          <span style={cell}>{q.count === 0 ? '0' : q.count + (q.type === 'sharp' ? '♯' : '♭')}</span>
          <span style={{...cell,color:on ? '#c0431f' : '#26296b'}}>{prettyNote(q.major)}</span>
          <span style={{...cell,color:on ? '#c0431f' : '#26296b'}}>{prettyNote(q.minor)}m</span>
        </button>); })}
    </div>
    <div style={{maxWidth:320,margin:'12px auto 0',display:'flex',gap:12,alignItems:'center',padding:'10px 12px',border:'1px solid rgba(38,41,107,0.14)',borderRadius:10,background:'#fffefa'}}>
      <svg width="44" height="30" viewBox="0 0 44 30" aria-hidden="true" style={{flex:'none'}}>{[4, 11, 18, 25].map(y => <line key={y} x1="2" x2="42" y1={y} y2={y} stroke="#9a9cc0" strokeWidth="1.2"/>)}<line x1="33" x2="33" y1="4" y2="25" stroke="#26296b" strokeWidth="1.6"/><rect x="37" y="4" width="4" height="21" fill="#26296b"/></svg>
      <div style={{fontSize:15,fontWeight:700,color:'#26296b',lineHeight:1.45,minWidth:0}}>
        <div>{t('Same signature, two keys. Look at the last bar: the note it ends on (or its chord) is the key.', '조표는 같아도 조는 둘이에요. 마지막 마디를 보세요. 끝나는 음(이나 코드)이 그 곡의 조예요.')}</div>
        <div style={{marginTop:4}}>{t('Ends on ', '끝음 ')}<b style={{color:'#c0431f'}}>{prettyNote(ks.major)}</b> → {majName(ks)}</div>
        <div>{t('Ends on ', '끝음 ')}<b style={{color:'#c0431f'}}>{prettyNote(ks.minor)}</b> → {minName(ks)}</div>
      </div>
    </div>
    """ + btns.rstrip('\n') + r"""
  </>);
}
"""
s=s[:a]+new+s[b:]
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
