import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# state + reset
rep("  const [badPos, setBadPos] = useState(null);   // Phase 507: the order screen shows all seven first, then one by one\n","  const [badPos, setBadPos] = useState(null);\n  const [stage, setStage] = useState(0);   // Phase 517: find the key by tapping: 0 = the last sign, 1 = the key\n  useEffect(() => { setStage(0); setBad(null); setBadPos(null); }, [n, phase]);\n")
# marks: stage 1 lights the last sharp
rep("  else if (ran || phase === 'order') order.slice(0, lit).forEach(","  else if (stage === 1 && sharp && phase === 'find') marks[kidx(order[want])] = 'mate';\n  else if (ran || phase === 'order') order.slice(0, lit).forEach(")
# handlers
rep("  const tap = (i) => { if (done) return; if (i === want) {",
"""  const m12 = (x) => ((x % 12) + 12) % 12;
  const lastPos = want >= 0 ? (sharp ? SHARP_POS : FLAT_POS)[order[want]] : undefined, tonicStep = sharp ? lastPos + 1 : lastPos;
  const finish = () => { setFound(true); playKey(tonic, 0.6); const j = KEY_SIGS.findIndex(q => q.major === k.major); if (j >= 0) setKi(j); };
  const hit = (keyIdx, step) => {
    if (done || auto) return;
    const flash = () => { if (keyIdx != null) setBad(keyIdx); else setBadPos(step); timers.current.push(setTimeout(() => { setBad(null); setBadPos(null); }, 650)); };
    if (stage === 0) {
      const ok = keyIdx != null ? m12(keyIdx) === pcOfName(order[want]) : step === lastPos;
      if (!ok) return flash();
      if (sharp) { setStage(1); playKey(kidx(order[want]), 0.5); } else finish();
    } else {
      const ok = keyIdx != null ? m12(keyIdx) === tonic : step === tonicStep;
      if (ok) finish(); else flash();
    }
  };
  const tap = (i) => { if (done) return; if (i === want) {""")
# find view: staff, prompt, no chips, board with taps
rep("    {staff}\n    {wordsRow}\n    <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px'}}>{auto ? t('Only one: it is F.', '하나뿐이면 F예요.') : sharp ? t('Now tap the last ♯.', '이제 마지막 샤프를 눌러요.') : t('Now tap the second-to-last ♭.', '이제 뒤에서 두 번째 플랫을 눌러요.')}</div>",
"""    <div style={{maxWidth:260,margin:'0 auto'}}><KSStaff count={lit} type={type} width={200} tallBox={sharp} onPick={done || auto ? undefined : (st) => hit(null, st)} ring={(stage === 1 || (done && !auto)) ? want : undefined} tonicPos={done && !auto ? tonicStep : undefined} tonicFrom={done && !auto && sharp ? lastPos : undefined} ghostPos={badPos}/></div>
    {wordsRow}
    <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'8px 0 6px',minHeight:40,textWrap:'balance'}}>{done ? '' : auto ? t('Only one: it is F.', '하나뿐이면 F예요.') : !sharp ? t('Tap the second-to-last ♭ on the staff or the keys. That is the key.', '뒤에서 두 번째 플랫을 오선이나 건반에서 눌러요. 그게 바로 그 조예요.') : stage === 0 ? t('Tap the last ♯ on the staff or the keys.', '마지막 샤프를 오선이나 건반에서 눌러요.') : t('Now go up a half step: tap the key.', '이제 반음 위, 그 조를 눌러요.')}</div>""")
# remove chips block
i=s.index("    {!auto && <div style={{display:'flex',gap:4,justifyContent:'center',marginBottom:8}}>\n      {order.slice(0, n).map(")
j=s.index("    {board}\n    <div style={{textAlign:'center',fontSize:13,fontWeight:700", i)
s=s[:i]+s[j:]
rep("    {board}\n    <div style={{textAlign:'center',fontSize:13,fontWeight:700","    <div style={{maxWidth:300,margin:'0 auto'}}><TapKeyboard octaves={1} marks={bad != null ? { ...marks, [bad]: 'miss' } : marks} labels=\"all\" bigLabels extraC={sharp} onTap={done || auto ? undefined : (i) => hit(i, null)}/></div>\n    <div style={{textAlign:'center',fontSize:13,fontWeight:700")
# drill: its own button under the lessons
rep("          {step(++n, t('Drill', '드릴'), LANG === 'ko' ? live.checkLine[1] : live.checkLine[0], false, () => go({ view: 'home', drill: live.check, tab: 'drill', level: 1, mode: 'lesson' }))}\n        </>; })()}\n      </div>",
"        </>; })()}\n      </div>\n      <button onClick={() => go({ view: 'home', drill: live.check, tab: 'drill', level: 1, mode: 'lesson' })} style={{display:'block',width:'100%',minHeight:60,marginTop:18,borderRadius:30,border:'none',background:'var(--navy)',color:'#fffefa',fontWeight:800,fontSize:20,cursor:'pointer'}}>{t('Start the drill →', '드릴 시작 →')}</button>")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
