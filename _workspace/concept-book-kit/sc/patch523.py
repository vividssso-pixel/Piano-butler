import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# ---- KfRule: the half step up arrives after a beat
rep("  const kx = (nm) => (sharp && pcOfName(nm) === 0 ? 12 : !sharp && pcOfName(nm) === 11 ? -1 : pcOfName(nm));",
"""  const kx = (nm) => (sharp && pcOfName(nm) === 0 ? 12 : !sharp && pcOfName(nm) === 11 ? -1 : pcOfName(nm));
  const [up, setUp] = useState(false);   // Phase 523: the move to the key plays as a short animation
  useEffect(() => { setUp(false); if (r === 1 && !one) { const id = setTimeout(() => { setUp(true); playKey(pcOfName(k.major), 0.5); }, 550); return () => clearTimeout(id); } }, [r, e]);""")
rep("if (r === 1) marks[kx(k.major)] = 'pick'; }","if (r === 1 && up) marks[kx(k.major)] = 'pick'; }")
rep("const tonicPos = r === 1 && !one ?","const tonicPos = r === 1 && up && !one ?")
rep("tonicFrom={sharp && r === 1 ? SHARP_POS[lastNm] : undefined}","tonicFrom={sharp && r === 1 && up ? SHARP_POS[lastNm] : undefined}")
rep("visibility:r === 1 || one ? 'visible' : 'hidden'}}>{n}","visibility:(r === 1 && up) || one ? 'visible' : 'hidden'}}>{n}")
rep("onClick={r === 0 && !one ? () => { setR(1); playKey(pcOfName(k.major), 0.5); } :","onClick={r === 0 && !one ? () => { setR(1); } :")
# ---- KfMinor: the three half steps down, one after another
rep("  const [found, setFound] = useState(false);\n  const timer = useRef(null);\n  useEffect(() => () => clearTimeout(timer.current), []);",
"""  const [found, setFound] = useState(false);
  const [sd, setSd] = useState(0);   // Phase 523: how many of the three half steps down have been shown
  const timer = useRef(null), walk = useRef([]);
  useEffect(() => () => { clearTimeout(timer.current); walk.current.forEach(clearTimeout); }, []);""")
rep("    if (r === 0) marks[pM] = 'pick';\n    else { marks[pM] = 'mate'; marks[pm] = 'pick'; names[m12(pM - 1)] = '1'; names[m12(pM - 2)] = '2'; names[pm] = '3'; }",
"""    if (r === 0) marks[pM] = 'pick';
    else {
      marks[pM] = 'mate';
      for (let q = 1; q <= sd; q++) { const kk = m12(pM - q); marks[kk] = q === sd ? 'pick' : 'mate'; names[kk] = String(q); }
    }""")
rep("const resultLine = tryMode\n    ? (found ?","const resultLine = tryMode\n    ? (found ?")
rep("    : r === 0 ? <>{ks.count}{sym} → <span style={{color:'#c0431f'}}>{majName(ks)}</span></> : <>{majName(ks)} → <span style={{color:'#c0431f'}}>{minName(ks)}</span></>;",
    "    : r === 0 ? <>{ks.count}{sym} → <span style={{color:'#c0431f'}}>{majName(ks)}</span></> : sd < 3 ? '' : <>{majName(ks)} → <span style={{color:'#c0431f'}}>{minName(ks)}</span></>;")
# start/stop the walk
rep("  const pickKey = (x) =>","""  const walkDown = () => {
    walk.current.forEach(clearTimeout); walk.current = []; setSd(0);
    [1, 2, 3].forEach((q) => walk.current.push(setTimeout(() => { setSd(q); playKey(m12(pM - q), 0.4); }, 450 + (q - 1) * 600)));
  };
  const stopWalk = () => { walk.current.forEach(clearTimeout); walk.current = []; setSd(0); };
  const pickKey = (x) =>""")
rep("onClick={r === 0 ? () => { setR(1); playKey(pm, 0.5); } : e < EXM.length - 1 ? () => { setE(e + 1); setR(0); } :","onClick={r === 0 ? () => { setR(1); walkDown(); } : e < EXM.length - 1 ? () => { stopWalk(); setE(e + 1); setR(0); } :")
rep("? <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => setR(0)}>{t('← Back', '← 이전')}</button>\n          : e > 0 ? <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => { setE(e - 1); setR(1); }}>",
    "? <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => { stopWalk(); setR(0); }}>{t('← Back', '← 이전')}</button>\n          : e > 0 ? <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => { setE(e - 1); setR(1); setSd(3); }}>")
rep("() => { setPh('try'); setStage(0); setFound(false); setBad(null); }}>","() => { stopWalk(); setPh('try'); setStage(0); setFound(false); setBad(null); }}>")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
