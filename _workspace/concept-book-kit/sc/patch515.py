import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
rep("function KSStaff({ count, type, width = 170, ink = '#26296b', accent = '#e4572e', upto, clef = 'treble', numbers, onPick, ghostPos }) {",
    "function KSStaff({ count, type, width = 170, ink = '#26296b', accent = '#e4572e', upto, clef = 'treble', numbers, onPick, ghostPos, ring }) {   // Phase 515: ring = circle the sign with this index")
rep("        return type === 'sharp' ? <SharpShape key={acc} x={x} y={y} color={col}/> : <FlatShape key={acc} x={x} y={y} color={col}/>;\n      })}\n    </svg>",
    "        return type === 'sharp' ? <SharpShape key={acc} x={x} y={y} color={col}/> : <FlatShape key={acc} x={x} y={y} color={col}/>;\n      })}\n      {ring != null && ring >= 0 && ring < accs.length && <circle cx={xs[ring]} cy={yPos(posMap[accs[ring]])} r=\"12\" fill=\"none\" stroke={ink} strokeWidth=\"2.2\" style={{animation:'fadeUp 0.3s both'}}/>}\n    </svg>")
i=s.index("function KfRule("); j=s.index("function KfMajor(")
new = r"""function KfRule({ type, go, back }) {
  const kc = React.useContext(KfCtx), sharp = type === 'sharp', n = 3, k = KEY_BY_COUNT(type, n), marks = {};
  const [r, setR] = useState(0);   // Phase 515: 0 = circle the sign, 1 = what the circle tells you
  const want = sharp ? n - 1 : n - 2;
  const lastNm = (sharp ? SHARP_ORDER : FLAT_ORDER)[want];
  marks[pcOfName(lastNm)] = r === 0 ? 'pick' : 'mate';
  if (r === 1) marks[pcOfName(k.major)] = 'pick';
  const head = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const say = r === 0
    ? (sharp ? t('1. Find the last ♯ and circle it.', '1. 마지막 샤프를 찾아 동그라미 쳐요.') : t('1. Find the second-to-last ♭ and circle it.', '1. 뒤에서 두 번째 플랫을 찾아 동그라미 쳐요.'))
    : (sharp ? t('2. Go up one half step. That is the key.', '2. 반음 위로 올라가요. 그게 바로 그 조예요.') : t('2. That ♭ is the key. (With one ♭ it is F.)', '2. 그 플랫이 바로 그 조예요. (플랫이 하나면 F예요.)'));
  return (<>
    <KfChain hi={[1]}/>
    <div style={head}>{sharp ? t('Sharps: find the key', '샤프로 조 찾기') : t('Flats: find the key', '플랫으로 조 찾기')}</div>
    <div key={r} style={{textAlign:'center',fontSize:16,fontWeight:800,color:'#26296b',margin:'0 0 8px',textWrap:'balance',minHeight:40,animation:'fadeUp 0.3s both'}}>{say}</div>
    <div style={{maxWidth:260,margin:'0 auto'}}><KSStaff count={n} type={type} width={200} ring={want}/></div>
    <div style={{maxWidth:300,margin:'4px auto 0'}}><TapKeyboard octaves={1} marks={marks} labels="all" bigLabels /></div>
    <div style={{...head,margin:'6px 0 2px',minHeight:27,visibility:r === 1 ? 'visible' : 'hidden'}}>{n}{sharp ? '♯' : '♭'} → <span style={{color:'#c0431f'}}>{majName(k)}</span></div>
    <div style={{textAlign:'center',marginTop:14,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>
      {r === 1 ? <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => setR(0)}>{t('← Back', '← 이전')}</button>
        : (back || (kc && kc.step > 1)) && <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={back || (() => kc && kc.setStep(1))}>{t('← Back', '← 이전')}</button>}
      <button className="ghost-btn" style={{...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'}} onClick={r === 0 ? () => { setR(1); playKey(pcOfName(k.major), 0.5); } : go}>{r === 0 ? t('Next →', '다음 →') : t('Try it →', '해 보기 →')}</button>
    </div>
  </>);
}
"""
s=s[:i]+new+s[j:]
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
