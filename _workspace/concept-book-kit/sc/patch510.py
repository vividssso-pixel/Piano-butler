import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:80],s.count(a)); s=s.replace(a,b)
# --- lesson mode helpers
rep("const KfCtx = React.createContext(null);\nfunction KfChain({ hi }) {\n",
    "const KfCtx = React.createContext(null);\nconst KfOnlyCtx = React.createContext(false);   // Phase 510: one lesson on its own, no tabs and no three-pill chain\nfunction KfChain({ hi }) {\n  if (React.useContext(KfOnlyCtx)) return null;\n")
rep("<button className=\"ghost-btn\" style={{...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'}} onClick={go}>{label || t('Next →', '다음 →')}</button></div>;\n}",
    "{go && <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'}} onClick={go}>{label || t('Next →', '다음 →')}</button>}</div>;\n}")
# last screen of the order tap lesson: no Next when there is nowhere to go
rep("    {got >= 7 ? <KfNext go={mode === 'order' ? go : startFind} label={goLabel}",
    "    {got >= 7 && !(mode === 'order' && !go) ? <KfNext go={mode === 'order' ? go : startFind} label={goLabel}")
# find mode final button
rep("<button className=\"ghost-btn\" style={prim} onClick={go}>{goLabel || t('Next →', '다음 →')}</button>)}",
    "go && <button className=\"ghost-btn\" style={prim} onClick={go}>{goLabel || t('Next →', '다음 →')}</button>)}")
# piece: back only inside the four-step walk
rep("<button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => kc.setStep(3)}>{t('← Back', '← 이전')}</button><a clas",
    "{kc && kc.step > 1 && <button className=\"ghost-btn\" style={{...KF_BTN,minWidth:110}} onClick={() => kc.setStep(3)}>{t('← Back', '← 이전')}</button>}<a clas")
# --- KeyFinder only
rep("function KeyFinder() {\n  const [step, setStep] = useState(1);\n  const [ki, setKi] = useState(1);",
"""function KeyFinder({ only }) {
  const [step, setStep] = useState(1);
  const [ki, setKi] = useState(1);
  if (only) return (
    <div className="try-box" data-kf-lesson={only} style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>
      <KfOnlyCtx.Provider value={true}>
      <KfCtx.Provider value={{ step: 1, setStep: () => {} }}>
        {only === 'sharps' && <KfFind key="os" type="sharp" mode="order" setKi={setKi}/>}
        {only === 'flats' && <KfFind key="of" type="flat" mode="order" setKi={setKi}/>}
        {only === 'major' && <KfMajor setKi={setKi}/>}
        {only === 'minor' && <KfMinor i={ki} setI={setKi}/>}
        {only === 'piece' && <KfPiece i={ki} setI={setKi}/>}
      </KfCtx.Provider>
      </KfOnlyCtx.Provider>
    </div>);""")
# --- tools
rep("TOOL_CONCEPT['cb-p-scales'] = 'p-scales';\n",
"""TOOL_CONCEPT['cb-p-scales'] = 'p-scales';
// Phase 510: the five Learn lessons, each its own short tool (opened from the concept home)
[['kf-sharps', 'sharps', 'Sharp order', '샤프 순서', 'All seven, one by one, then your turn.', '일곱 개를 한꺼번에, 하나씩, 그다음 내가 해 보기.'],
 ['kf-flats', 'flats', 'Flat order', '플랫 순서', 'All seven, one by one, then your turn.', '일곱 개를 한꺼번에, 하나씩, 그다음 내가 해 보기.'],
 ['kf-major', 'major', 'Find the major key', '장조 찾기', 'The sharp way, then the flat way.', '샤프로 찾는 법, 그다음 플랫으로 찾는 법.'],
 ['kf-minor', 'minor', 'Find the minor key', '단조 찾기', 'From the major, three half steps down.', '장조에서 반음 세 칸 아래로.'],
 ['kf-piece', 'piece', 'Before a piece', '곡 치기 전에', 'Find the key, then play its scale.', '조를 찾고, 그 스케일을 쳐 봐요.']].forEach(([id, only, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '조 찾기' : 'Learn'); }, C: () => <KeyFinder only={only}/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-scales';
});
""")
# --- home
rep("    learnLine: ['Four steps: find the key from its signature', '네 단계: 조표로 조 찾기'],",
    "    learnLine: ['Five short lessons, one at a time', '짧은 레슨 다섯 개, 하나씩'],\n    lessons: ['kf-sharps', 'kf-flats', 'kf-major', 'kf-minor', 'kf-piece'],")
rep("  // level 3: the tools of one concept\n  if (cat && live && st.hs === 'try') return (",
"""  // level 3: the five Learn lessons
  if (cat && live && st.hs === 'learn') return (
    <div className="fade-up">
      <button className="ghost-btn" style={ghost} onClick={() => go({ hs: null })}>← {cat.name}</button>
      <StaffHead title={t('Learn', '배우기')}/>
      <div style={{display:'flex',flexDirection:'column',gap:10,marginTop:12}}>
        {live.lessons.map((id, i) => { const tl = TOOLS.find(x => x.id === id); return tl ? step(i + 1, tl.title, tl.blurb, false, () => go({ view: 'tools', tool: id, ret: 'home' })) : null; })}
      </div>
    </div>
  );
  // level 3: the tools of one concept
  if (cat && live && st.hs === 'try') return (""")
rep("() => go({ view: 'tools', tool: live.learn, ret: 'home' }))}","() => go(live.lessons ? { hs: 'learn' } : { view: 'tools', tool: live.learn, ret: 'home' }))}")
rep("const homeBack = '← ' + (st.hs === 'try' ? t('Try', '해 보기') :","const homeBack = '← ' + (st.hs === 'try' ? t('Try', '해 보기') : st.hs === 'learn' ? t('Learn', '배우기') :")
rep('      <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={back || (() => kc && kc.setStep(1))}>{t(\'← Back\', \'← 이전\')}</button>\n      <button className="ghost-btn" style={{...KF_BTN,minWidth:140,background:\'#26296b\',color:\'#fffefa\',borderColor:\'#26296b\'}} onClick={go}>{t(\'Try it →\', \'해 보기 →\')}</button>', '      {(back || (kc && kc.step > 1)) && <button className="ghost-btn" style={{...KF_BTN,minWidth:110}} onClick={back || (() => kc && kc.setStep(1))}>{t(\'← Back\', \'← 이전\')}</button>}\n      <button className="ghost-btn" style={{...KF_BTN,minWidth:140,background:\'#26296b\',color:\'#fffefa\',borderColor:\'#26296b\'}} onClick={go}>{t(\'Try it →\', \'해 보기 →\')}</button>')
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
