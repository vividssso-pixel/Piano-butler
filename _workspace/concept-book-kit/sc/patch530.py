import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
rep("  const [sd, setSd] = useState(0);   // Phase 523","  const [intro, setIntro] = useState(true);   // Phase 530: first, every key signature is a pair: a major and its relative minor\n  const [sd, setSd] = useState(0);   // Phase 523")
rep("  if (!tryMode) {\n    if (r === 0) marks[pM] = 'pick';","  if (!tryMode) {\n    if (intro) { marks[pM] = 'pick'; marks[pm] = 'pick'; }\n    else if (r === 0) marks[pM] = 'pick';")
rep("    : r === 0 ? t('1. Find the major key first.'","    : intro ? t('Every key signature has two keys: a major and its relative minor.', '조표 하나에는 두 조가 한 세트예요. 장조와 그 나란한 단조.')\n    : r === 0 ? t('1. Find the major key first.'")
rep("    : r === 0 ? <>{ks.count}{sym} → <span style={{color:'#c0431f'}}>{majName(ks)}</span></>","    : intro ? <>{majName(ks)} <span style={{fontWeight:700}}>+</span> <span style={{color:'#c0431f'}}>{minName(ks)}</span></>\n    : r === 0 ? <>{ks.count}{sym} → <span style={{color:'#c0431f'}}>{majName(ks)}</span></>")
rep("{t('Find the minor key', '단조 찾기')}","{t('Find the relative minor key', '나란한 단조 찾기')}")
rep("<div key={ph + r + e + stage + found}","<div key={ph + r + e + stage + found + intro}")
rep("onClick={r === 0 ? () => { setR(1); walkDown(); } :","onClick={intro ? () => setIntro(false) : r === 0 ? () => { setR(1); walkDown(); } :")
rep("}>{r === 0 ? t('Next →', '다음 →') : e < EXM.length - 1","}>{intro || r === 0 ? t('Next →', '다음 →') : e < EXM.length - 1")
rep("          : (kc && kc.step > 1) && <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => kc.setStep(kc.step - 1)}>{t('← Back', '← 이전')}</button>)}",
"          : !intro ? <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => setIntro(true)}>{t('← Back', '← 이전')}</button>\n          : (kc && kc.step > 1) && <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => kc.setStep(kc.step - 1)}>{t('← Back', '← 이전')}</button>)}")
# going back to the rule from Try returns to the first example, not the intro
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
