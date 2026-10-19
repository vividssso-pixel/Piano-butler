import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a,s.count(a)); s=s.replace(a,b)
rep("function KSStaff({ count, type, width = 170, ink = '#26296b', accent = '#e4572e', upto, clef = 'treble', numbers }) {",
    "function KSStaff({ count, type, width = 170, ink = '#26296b', accent = '#e4572e', upto, clef = 'treble', numbers, onPick, ghostPos }) {   // Phase 509: onPick(step) = tap the staff; ghostPos = a faint wrong guess")
rep("    <svg viewBox={`0 ${base - (numbers ? 72 : 60)} ${width} ${numbers ? 90 : 78}`} style={{width:'100%',maxWidth:width * 1.6,display:'block',margin:'0 auto'}}>\n      {numbers && accs.map(",
    """    <svg viewBox={`0 ${base - (numbers ? 72 : 60)} ${width} ${numbers ? 90 : 78}`} style={{width:'100%',maxWidth:width * 1.6,display:'block',margin:'0 auto',cursor:onPick ? 'pointer' : undefined,touchAction:onPick ? 'manipulation' : undefined}} data-staff-pick={onPick ? '1' : undefined}
      onClick={onPick ? (e) => { const r = e.currentTarget.getBoundingClientRect(); const vy = (base - (numbers ? 72 : 60)) + (e.clientY - r.top) / r.height * (numbers ? 90 : 78); const st = Math.round((base - vy) / 5); if (st >= 0 && st <= 10) onPick(st); } : undefined}>
      {onPick && <rect x="0" y={base - (numbers ? 72 : 60)} width={width} height={numbers ? 90 : 78} fill="transparent"/>}
      {ghostPos != null && (type === 'sharp' ? <g opacity="0.55"><SharpShape x={56 + accs.length * 15} y={yPos(ghostPos)} color="#c8361b"/></g> : <g opacity="0.55"><FlatShape x={56 + accs.length * 15} y={yPos(ghostPos)} color="#c8361b"/></g>)}
      {numbers && accs.map(""")
rep("  const [got, setGot] = useState(0);\n  const [bad, setBad] = useState(null);","  const [got, setGot] = useState(0);\n  const [bad, setBad] = useState(null);\n  const [badPos, setBadPos] = useState(null);")
rep("    else { setBad(i); clear(); timers.current.push(setTimeout(() => setBad(null), 650)); }\n  };",
    """    else { setBad(i); clear(); timers.current.push(setTimeout(() => setBad(null), 650)); }
  };
  const tapStaff = (st) => {
    if (got >= 7) return;
    if (st === (sharp ? SHARP_POS : FLAT_POS)[order[got]]) { clear(); setBadPos(null); playKey(kidx(order[got]), 0.45); setGot(got + 1); setLit(got + 1); }
    else { setBadPos(st); clear(); timers.current.push(setTimeout(() => setBadPos(null), 650)); }
  };""")
rep("""    <div style={titleStyle}>{got >= 7 ? t('All seven!', '일곱 개 모두!') : t('Tap ' + nameWord + ' ' + (got + 1), nameWord + ' ' + (got + 1) + '번을 눌러요')}</div>
    {staff}""","""    <div style={titleStyle}>{got >= 7 ? t('All seven!', '일곱 개 모두!') : t('Tap ' + nameWord + ' ' + (got + 1), nameWord + ' ' + (got + 1) + '번을 눌러요')}</div>
    <div style={{textAlign:'center',fontSize:12,color:'#5a5d8f',margin:'-4px 0 4px',minHeight:16}}>{got >= 7 ? '' : t('on the staff or on the keys', '오선이나 건반에서')}</div>
    <div style={{maxWidth:260,margin:'0 auto'}}><KSStaff count={lit} type={type} width={200} numbers upto={lit > 0 ? lit - 1 : undefined} onPick={got >= 7 ? undefined : tapStaff} ghostPos={badPos}/></div>""")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
