import sys
s=open(sys.argv[1],encoding='utf-8').read()
i=s.index("function KfMinor("); j=s.index("function KfCircle(")
new = r"""function KfMinor({ i, setI, go }) {   // Phase 522: learn (find the major, then 3 half steps down), then try (tap both)
  const kc = React.useContext(KfCtx);
  const [ph, setPh] = useState('rule');
  const [e, setE] = useState(0);
  const [r, setR] = useState(0);
  const [stage, setStage] = useState(0);
  const [bad, setBad] = useState(null);
  const [found, setFound] = useState(false);
  const timer = useRef(null);
  useEffect(() => () => clearTimeout(timer.current), []);
  const EXM = ['A', 'Bb', 'E'];
  const tryMode = ph === 'try';
  const ks = tryMode ? KEY_SIGS[i] : KEY_SIGS.find(q => q.major === EXM[e]);
  const pM = pcOfName(ks.major), pm = pcOfName(ks.minor), m12 = (x) => ((x % 12) + 12) % 12;
  const sym = ks.type === 'sharp' ? '♯' : '♭';
  const head = {textAlign:'center',fontFamily:"'Playfair Display', Georgia, serif",fontSize:22,fontWeight:900,color:'#26296b',lineHeight:1.2,margin:'0 0 8px',textWrap:'balance'};
  const marks = {}, names = {};
  if (!tryMode) {
    if (r === 0) marks[pM] = 'pick';
    else { marks[pM] = 'mate'; marks[pm] = 'pick'; names[m12(pM - 1)] = '1'; names[m12(pM - 2)] = '2'; names[pm] = '3'; }
  } else {
    if (stage === 1 || found) marks[pM] = 'mate';
    if (found) marks[pm] = 'pick';
  }
  if (bad != null) marks[bad] = 'miss';
  const pickKey = (x) => { clearTimeout(timer.current); setI(x); setStage(0); setFound(false); setBad(null); };
  const tapTry = (idx) => {
    if (found) return;
    const want = stage === 0 ? pM : pm;
    if (m12(idx) === want) { playKey(want, 0.5); if (stage === 0) setStage(1); else setFound(true); }
    else { setBad(idx); clearTimeout(timer.current); timer.current = setTimeout(() => setBad(null), 650); }
  };
  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};
  const stageLine = tryMode
    ? (found ? '' : stage === 0 ? t('Tap the major key.', '장조를 눌러요.') : t('Now 3 half steps down: tap the minor key.', '이제 반음 3칸 아래, 단조를 눌러요.'))
    : r === 0 ? t('1. Find the major key first.', '1. 먼저 장조를 찾아요.') : t('2. Count 3 half steps down. That is the minor.', '2. 반음 3칸 아래로 내려가요. 거기가 단조예요.');
  const resultLine = tryMode
    ? (found ? <>{majName(ks)} → <span style={{color:'#c0431f'}}>{minName(ks)}</span></> : '')
    : r === 0 ? <>{ks.count}{sym} → <span style={{color:'#c0431f'}}>{majName(ks)}</span></> : <>{majName(ks)} → <span style={{color:'#c0431f'}}>{minName(ks)}</span></>;
  const kb = <div style={{maxWidth:300,margin:'6px auto 0'}}><TapKeyboard octaves={1} marks={marks} names={Object.keys(names).length ? names : null} labels="all" bigLabels onTap={tryMode ? tapTry : undefined}/></div>;
  const staff = <div style={{maxWidth:200,margin:'0 auto'}}><KSStaff count={ks.count} type={ks.type} width={170}/></div>;
  return (<>
    <KfChain hi={[1]}/>
    <div style={head}>{t('Find the minor key', '단조 찾기')}</div>
    <div key={ph + r + e + stage + found} style={{textAlign:'center',fontSize:16,fontWeight:800,color:'#26296b',margin:'0 0 8px',textWrap:'balance',minHeight:40,animation:'fadeUp 0.3s both'}}>{stageLine}</div>
    {tryMode ? <KfNav i={i} setI={pickKey}>{staff}</KfNav> : staff}
    {kb}
    <div style={{...head,margin:'6px 0 2px',minHeight:27,visibility:resultLine === '' ? 'hidden' : 'visible'}}>{resultLine || ' '}</div>
    <div style={{textAlign:'center',marginTop:10,display:'flex',gap:8,justifyContent:'center',flexWrap:'wrap'}}>
      {tryMode
        ? <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { setPh('rule'); setR(0); setE(0); }}>{t('← The rule', '← 규칙')}</button>
        : (r === 1 ? <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => setR(0)}>{t('← Back', '← 이전')}</button>
          : e > 0 ? <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => { setE(e - 1); setR(1); }}>{t('← Back', '← 이전')}</button>
          : (kc && kc.step > 1) && <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={() => kc.setStep(kc.step - 1)}>{t('← Back', '← 이전')}</button>)}
      {!tryMode && <button className="ghost-btn" style={prim} onClick={r === 0 ? () => { setR(1); playKey(pm, 0.5); } : e < EXM.length - 1 ? () => { setE(e + 1); setR(0); } : () => { setPh('try'); setStage(0); setFound(false); setBad(null); }}>{r === 0 ? t('Next →', '다음 →') : e < EXM.length - 1 ? t('Another one →', '다른 예 →') : t('Your turn →', '내가 해보기 →')}</button>}
      {tryMode && found && go && <button className="ghost-btn" style={prim} onClick={go}>{t('Next →', '다음 →')}</button>}
    </div>
  </>);
}
"""
s=s[:i]+new+s[j:]
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
