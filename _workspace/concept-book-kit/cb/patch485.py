#!/usr/bin/env python3
# Phase 485 (her 2026-10-17 22:09 '스케일과 조 첫개념 책으로 만든거 보자'): the first concept book, Scales and keys
# (rule 16): eight A4 pages (?book=concept&ch=p-scales) and the same pages on screen (the Toolbox's cb-p-scales, opened
# from a card under the concept's name). The keyboard clock learns other shapes (o.pat: the minors, the pentatonic and
# the chromatic scale on the same clock); a book page can name its own place on the cornice (LbPage head).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)

# 1. the keyboard clock: any shape (o.pat, offsets from the key; o.names, its spelling), its half steps coral
rep("const sp = pbSpell(sel), deg = (i) => (i - idx + 12) % 12, inScale = (i) => PB_MAJOR.includes(deg(i));",
    "const PAT = o.pat || PB_MAJOR, sp = o.pat ? (o.names || []) : pbSpell(sel), deg = (i) => (i - idx + 12) % 12, inScale = (i) => PAT.includes(deg(i));")
rep("const spAt = (i) => inScale(i) ? sp[PB_MAJOR.indexOf(deg(i))] : null, spelled = o.shape && !o.plain;",
    "const spAt = (i) => inScale(i) ? sp[PAT.indexOf(deg(i))] || null : null, spelled = o.shape && !o.plain;")
rep("const shapePts = PB_MAJOR.map(s => pt(-90 + s * 30, RP)), LR = st ? 126 : 133;",
    "const shapePts = PAT.map(s => pt(-90 + s * 30, RP)), LR = st ? 126 : 133;")
rep("const q = shapePts[(j + 1) % 7], half = j === 2 || j === 6;",
    "const q = shapePts[(j + 1) % PAT.length], half = (PAT[(j + 1) % PAT.length] - PAT[j] + 12) % 12 === 1;")
rep("{o.nums && PB_MAJOR.map((s, j) => {", "{o.nums && PAT.map((s, j) => {")

# 2. a book page may name its own place on the cornice (a concept book: its area and concept)
rep("function LbPage({ no, chId, kicker, title, teacher, qr, book, children }) {", "function LbPage({ no, chId, kicker, title, teacher, qr, book, head, children }) {")
rep("<VicHead left={book || 'Lesson Book'} right={'Chapter ' + bkChapterNo(chId) + ' · ' + bkChapterName(chId)} mb={14}/>",
    "<VicHead left={book || 'Lesson Book'} right={head || ('Chapter ' + bkChapterNo(chId) + ' · ' + bkChapterName(chId))} mb={14}/>")

# 3. the print route: ?book=concept&ch=<concept>
rep("const fixed = kind === 'spread' || kind === 'work'", "const fixed = kind === 'concept' || kind === 'spread' || kind === 'work'")
rep("const reg = kind === 'teacher' ? TEACHER_COPIES", "const reg = kind === 'concept' ? CONCEPT_BOOKS : kind === 'teacher' ? TEACHER_COPIES")
rep("printParams.get('book') === 'spread')) {", "printParams.get('book') === 'spread' || printParams.get('book') === 'concept')) {")

# 4. the Toolbox: the concept book's card under the concept's name
rep("<div style={{padding:'3px 14px 0',fontSize:12.5,color:'var(--navy-soft)',lineHeight:1.35}}>{c.when}</div>",
    "<div style={{padding:'3px 14px 0',fontSize:12.5,color:'var(--navy-soft)',lineHeight:1.35}}>{c.when}</div>\n            <CbCard cid={c.id} onOpen={onOpen}/>")

# 6. the circle of fifths can show the keys with two names (B and C♭, D♭ and C♯) as it shows F♯ and G♭ (o.twins)
rep("""{k === 'Gb' ? <text x={x} y={y} textAnchor="middle" fontSize={P ? 14 : 13.5} fontWeight="900" fill={ink} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}><tspan x={x} dy="-2.5">F♯</tspan><tspan x={x} dy="15">G♭</tspan></text>""",
    """{(k === 'Gb' || (o.twins && FIFTHS_TWIN[k])) ? <text x={x} y={y} textAnchor="middle" fontSize={P ? 14 : 13.5} fontWeight="900" fill={ink} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}><tspan x={x} dy="-2.5">{(FIFTHS_TWIN[k] || ['F♯', 'G♭'])[0]}</tspan><tspan x={x} dy="15">{(FIFTHS_TWIN[k] || ['F♯', 'G♭'])[1]}</tspan></text>""")
rep("""fill={BK.muted} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{FIFTHS_SIG[i]}</text>""",
    """fill={BK.muted} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{(o.twins && FIFTHS_TWIN_SIG[k]) || FIFTHS_SIG[i]}</text>""")
rep("const FIFTHS_SIG = ['0', '1♯', '2♯', '3♯', '4♯', '5♯', '6♯ 6♭', '5♭', '4♭', '3♭', '2♭', '1♭'];",
    "const FIFTHS_SIG = ['0', '1♯', '2♯', '3♯', '4♯', '5♯', '6♯ 6♭', '5♭', '4♭', '3♭', '2♭', '1♭'];\nconst FIFTHS_TWIN = { B: ['B', 'C♭'], Db: ['D♭', 'C♯'] }, FIFTHS_TWIN_SIG = { B: '5♯ 7♭', Db: '5♭ 7♯' };")

# 7. the older scale tools shown inside the book: their Korean follows the book (장조/단조 with no space; 장음계, 화성단음계)
rep("function majName(k) { return prettyNote(k.major) + t(' major', ' 장조'); }", "function majName(k) { return prettyNote(k.major) + t(' major', '장조'); }")
rep("function minName(k) { return prettyNote(k.minor) + t(' minor', ' 단조'); }", "function minName(k) { return prettyNote(k.minor) + t(' minor', '단조'); }")
rep("' 없음 = C 장조 / A 단조')", "' 없음 = C장조 / A단조')")
rep("'자연, 화성, 가락: 가단조로 나란히 비교해요.'", "'자연, 화성, 가락: A단조로 나란히 비교해요.'")
rep("'build-major': ['장조 스케일 만들기', '온 온 반 온 온 온 반, 한 단계씩.'],", "'build-major': ['장음계 만들기', '온 온 반 온 온 온 반, 한 걸음씩.'],")
rep("'build-minor': ['화성 단조 스케일 만들기', '온음 반 간격과 함께.'],", "'build-minor': ['화성단음계 만들기', '온+반 걸음이 있는 단음계.'],")
rep("'modes': ['일곱 가지 선법', '리디안부터 로크리안까지: 같은 음, 새로운 집, 밝음에서 어두움으로.'],", "'modes': ['일곱 가지 선법', '이오니안부터 로크리안까지: 같은 음, 새로운 집.'],")
rep("blurb: 'Lydian to Locrian: same notes, new home, brighter to darker.'", "blurb: 'Ionian to Locrian: same notes, a new home note.'")
rep("""<button className="ghost-btn" disabled={!n} onClick={() => { setN(0); setWrong(0); }}>{t('Restart', '처음부터')}</button>""",
    """<button className="ghost-btn" disabled={!n} style={{whiteSpace:'nowrap'}} onClick={() => { setN(0); setWrong(0); }}>{t('Restart', '처음부터')}</button>""")
rep("(n + 1) + '번째 걸음: ' + prettyAny(names[n]) + '에서 다음은 어떤 걸음일까요?'", "['첫', '두', '세', '네', '다섯', '여섯', '일곱'][n] + ' 번째 걸음: ' + prettyAny(names[n]) + '에서 다음은 어떤 걸음일까요?'")
rep("prettyNote(key) + ' 장조에는 ' + accs.map(prettyAny).join(' ') + '이 필요해요. 그게 바로 조표예요.'", "prettyNote(key) + '장조에는 ' + accs.map(prettyAny).join(' ') + ' 음이 필요해요. 그게 바로 조표예요.'")
rep("'C 장조: 샤프도 플랫도 전혀 없어요.'", "'C장조: 샤프도 플랫도 전혀 없어요.'")

# 8. design review (r1): what the concept book needs from shared parts
# the keyboard clock: only the scale's own notes named, in its spelling, big enough to read (o.only, o.labFs; o.ghost the
# other white keys faint, for tapping); its numbers bigger and navy (o.numFs)
rep("""  const tick = (x, y, bg, fg) =>""",
    """  const onlyLab = (x, y, n, fill) => { const fs = o.labFs || 26, acc = n.slice(1), dbl = acc.length > 1, g = acc === '##' ? '𝄪' : acc === 'bb' ? '𝄫' : acc === '#' ? '♯' : acc === 'b' ? '♭' : '';
    return <text x={x} y={y + fs * 0.36} textAnchor="middle" fontSize={fs} fontWeight="900" fill={fill} style={{fontFamily:"'Playfair Display', Georgia, serif",pointerEvents:'none'}}>{n[0]}{g ? <tspan fontSize={dbl ? fs * 0.95 : fs * 0.78} fontWeight={dbl ? 400 : 800} style={{fontFamily:dbl ? MUSIC_FONT : 'Inter, sans-serif'}}>{g}</tspan> : null}</text>; };
  const tick = (x, y, bg, fg) =>""")
rep("""        const lab = spelled && nm ? one(lx, ly, prettyNote(nm), ink, b ? 16 : 18)""",
    """        const lab = o.only ? (nm ? onlyLab(lx, ly, nm, ink) : o.ghost && !b ? one(lx, ly, k, 'rgba(38,41,107,0.38)', 15) : null)
          : spelled && nm ? one(lx, ly, prettyNote(nm), ink, b ? 16 : 18)""")
rep("""<text key={'n' + j} x={x} y={y + 4} textAnchor="middle" fontSize="12" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{j + 1}</text>""",
    """<text key={'n' + j} x={x} y={y + (o.numFs ? o.numFs * 0.36 : 4)} textAnchor="middle" fontSize={o.numFs || 12} fontWeight={o.numFs ? 900 : 800} fill={o.numFs ? PEN_N : BK.muted} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{j + 1}</text>""")
# the scale on the keys: the tonic's circle may be navy (o.tonicInk: coral is for what needs attention); bigger step words (o.stepFs)
rep("""  const ko = LANG === 'ko', sw = (w) => ko ? 16 : w === 'half' ? 23 : 36;""",
    """  const SF = o.stepFs || 12, SX = SF - 12, ko = LANG === 'ko', sw = (w) => (ko ? 16 : w === 'half' ? 23 : 36) * SF / 12;""")
rep("""  const B = o.steps ? (rows2 ? 58 : 40) : o.arrow && !o.arrow.over ? 36 : 8;""",
    """  const B = o.steps ? (rows2 ? 58 + SX * 2 : 40 + SX) : o.arrow && !o.arrow.over ? 36 : 8;""")
rep("""<circle cx={cx(k)} cy={T + H - 22} r="13" fill={s.d === 0 || s.d === 7 ? PEN_C : '#fff'} stroke={s.d === 0 || s.d === 7 ? PEN_C : PEN_N} strokeWidth="1.6"/>""",
    """<circle cx={cx(k)} cy={T + H - 22} r="13" fill={s.d === 0 || s.d === 7 ? (o.tonicInk || PEN_C) : '#fff'} stroke={s.d === 0 || s.d === 7 ? (o.tonicInk || PEN_C) : PEN_N} strokeWidth="1.6"/>""")
rep("""          {stepRow[d] === 1 && <line x1={(a + b) / 2} x2={(a + b) / 2} y1={y + 2} y2={y + 22} stroke={c} strokeWidth="1" strokeDasharray="2 2"/>}
          <text x={(a + b) / 2} y={y + (stepRow[d] === 1 ? 40 : 21)} textAnchor="middle" fontSize={ko ? 14 : 12} fontWeight="900" fill={c}>""",
    """          {stepRow[d] === 1 && <line x1={(a + b) / 2} x2={(a + b) / 2} y1={y + 2} y2={y + 22 + SX} stroke={c} strokeWidth="1" strokeDasharray="2 2"/>}
          <text x={(a + b) / 2} y={y + (stepRow[d] === 1 ? 40 + SX * 2 : 21 + SX)} textAnchor="middle" fontSize={SF + (ko ? 2 : 0)} fontWeight="900" fill={c}>""")
# the scale on the staff: the word 'tonic' may be navy too
rep("""textAnchor="middle" fontSize="13" fontWeight="900" fill={PEN_C} style={txt}>{o.tonicLabel}</text>""",
    """textAnchor="middle" fontSize="13" fontWeight="900" fill={o.tonicInk || PEN_C} style={txt}>{o.tonicLabel}</text>""")
# chapter 16's pad passes the tonic's colour on; its buttons a finger's size
rep("function SscPad({ page }) {", "function SscPad({ page, tonicInk }) {")
rep("  const o = { nums: P.nums, steps: P.steps, coral: P.coral, fingers: fing,", "  const o = { tonicInk, nums: P.nums, steps: P.steps, coral: P.coral, fingers: fing,")
rep("""      <div style={{maxWidth:460,margin:'0 auto'}}><SscKeys start={P.start} o={o} onTap={onTap}/></div>
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:miss ? BK.coral : BK.ink,minHeight:22,margin:'6px 0'}}>{msg}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center'}}>
        <button className="ghost-btn" onClick={listen}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" onClick={tapMode}>{t('▶ Tap it', '▶ 쳐 보기')}</button>""",
    """      <div style={{maxWidth:460,margin:'0 auto'}}><SscKeys start={P.start} o={o} onTap={onTap}/></div>
      <div style={{textAlign:'center',fontSize:15,fontWeight:900,color:miss ? BK.coral : BK.ink,minHeight:22,margin:'6px 0'}}>{msg}</div>
      <div style={{display:'flex',gap:6,justifyContent:'center'}}>
        <button className="ghost-btn" style={{minHeight:44}} onClick={listen}>{t('▶ Listen', '▶ 듣기')}</button>
        <button className="ghost-btn" style={{minHeight:44}} onClick={tapMode}>{t('▶ Tap it', '▶ 쳐 보기')}</button>""")
rep("""{['RH', 'LH'].map(h => <button key={h} className={'chip' + (h === hand ? ' active' : '')} onClick={() => { clear(); setHand(h);""",
    """{['RH', 'LH'].map(h => <button key={h} className={'chip' + (h === hand ? ' active' : '')} style={{minHeight:44}} onClick={() => { clear(); setHand(h);""")
# the key signature's numbers: on the palette, a little bigger (they were #a3a5c2 at 8.5)
rep("""textAnchor="middle" fontSize="8.5" fontWeight="800" fill={upto === i ? '#c8361b' : '#a3a5c2'}>{i + 1}</text>""",
    """textAnchor="middle" fontSize="9.5" fontWeight="800" fill={upto === i ? '#c8361b' : '#6d6f9c'}>{i + 1}</text>""")
# REMEMBER: on a narrow phone the words go under the portrait and the label (they ran out of the band at 320)
rep("""      <div style={{display:'flex',alignItems:'center',gap:12,borderTop:'0.7px solid ' + BK.ink,borderBottom:'0.7px solid ' + BK.ink,padding:'3px 2px'}}>
        <img src={VIC_CAMEO} alt="" style={{height:42,width:'auto',flex:'0 0 auto'}}/>""",
    """      <div className="lb-rem-row" style={{display:'flex',alignItems:'center',gap:12,borderTop:'0.7px solid ' + BK.ink,borderBottom:'0.7px solid ' + BK.ink,padding:'3px 2px'}}>
        <img src={VIC_CAMEO} alt="" style={{height:42,width:'auto',flex:'0 0 auto'}}/>""")
rep("""        <span style={{fontSize:16.5,fontWeight:800,color:BK.ink}}>{children}</span>""",
    """        <span className="lb-rem-txt" style={{fontSize:16.5,fontWeight:800,color:BK.ink,minWidth:0}}>{children}</span>""")
rep("""    @media (min-width: 900px) { .pb-main { zoom: 1.12; } }""",
    """    @media (min-width: 900px) { .pb-main { zoom: 1.12; } }
    @media (max-width: 400px) { .lb-rem-row { flex-wrap: wrap; row-gap: 2px; } .lb-rem-txt { flex: 1 1 100%; overflow-wrap: anywhere; padding: 0 2px 2px; } }""")
# the tick box on screen: a 44 px target round the 24 px box (the layout does not move)
rep("""  return <button onClick={() => setOn(v => !v)} aria-pressed={on} aria-label={label} style={{flex:'0 0 auto',width:24,height:24,border:'1.8px solid ' + BK.green,borderRadius:3,marginTop:0,background:on ? BK.green : '#fff',color:'#fff',fontWeight:900,fontSize:14,lineHeight:1,padding:0,cursor:'pointer'}}>{on ? '✓' : ''}</button>;""",
    """  return <button onClick={() => setOn(v => !v)} aria-pressed={on} aria-label={label} style={{flex:'0 0 auto',width:44,height:44,margin:-10,padding:10,border:0,background:'none',cursor:'pointer'}}>
    <span style={{display:'block',width:24,height:24,border:'1.8px solid ' + BK.green,borderRadius:3,background:on ? BK.green : '#fff',color:'#fff',fontWeight:900,fontSize:14,lineHeight:'21px',textAlign:'center'}}>{on ? '✓' : ''}</span></button>;""")
# the five checks: buttons a finger's size, the rows on the palette
rep("""        <div key={r} style={{border:'1px solid #ece6d8',borderRadius:12,padding:'6px 8px 8px',display:'flex',flexWrap:'wrap',alignItems:'center',gap:'6px 10px'}}>""",
    """        <div key={r} style={{border:'1px solid ' + BK.line,borderRadius:12,padding:'6px 8px 8px',display:'flex',flexWrap:'wrap',alignItems:'center',gap:'6px 10px'}}>""")
rep("""              style={{height:34,border:'1.5px solid ' + (on ? BK.green : BK.line),borderRadius:17,""",
    """              style={{minHeight:44,minWidth:64,justifyContent:'center',border:'1.5px solid ' + (on ? BK.green : BK.line),borderRadius:22,""")
# a step's 'Got it' button
rep("""<button className="ghost-btn" style={{fontSize:13,padding:'5px 12px',borderColor:color,color:color}} onClick={onDone}>""",
    """<button className="ghost-btn" style={{fontSize:13,minHeight:44,padding:'8px 16px',borderColor:color,color:color}} onClick={onDone}>""")
# the scale builder: no beige; key chips a finger's size; the buttons wrap on a narrow phone; the Korean words
rep("""        {KEYS.map(k => <button key={k} className={'chip' + (k === key ? ' active' : '')} style={{padding:'3px 10px',fontSize:13}} onClick={() => setKey(k)}>{prettyNote(k)}{mode === 'major' ? '' : 'm'}</button>)}""",
    """        {KEYS.map(k => <button key={k} className={'chip' + (k === key ? ' active' : '')} style={{padding:'8px 12px',fontSize:14,minHeight:44,minWidth:44}} onClick={() => setKey(k)}>{prettyNote(k)}{mode === 'major' ? '' : 'm'}</button>)}""")
rep("""            background:i < n ? (s === 'T' ? '#e4eeea' : '#fbe3da') : i === n ? '#26296b' : '#f5f0e4',
            color:i < n ? '#26296b' : i === n ? '#fff' : '#c9c0aa',transition:'background 0.25s'}}>""",
    """            background:i < n ? (s === 'T' ? '#e4eeea' : '#fbe3da') : i === n ? '#26296b' : '#fff', border:i > n ? '1px solid var(--navy-line)' : '1px solid transparent',
            color:i < n ? '#26296b' : i === n ? '#fff' : 'rgba(38,41,107,0.45)',transition:'background 0.25s'}}>""")
rep("""      <div style={{display:'flex',gap:6,justifyContent:'center',margin:'8px 0 4px'}}>
        {buttons.map(b => <button key={b} className="ghost-btn" disabled={done} onClick={() => choose(b)} style={{minWidth:70,fontWeight:900}}>{b}</button>)}""",
    """      <div style={{display:'flex',flexWrap:'wrap',gap:6,justifyContent:'center',margin:'8px 0 4px'}}>
        {buttons.map(b => <button key={b} className="ghost-btn" disabled={done} onClick={() => choose(b)} style={{minWidth:64,minHeight:44,fontWeight:900}}>{b}</button>)}""")
rep("""<button className="ghost-btn" disabled={!n} style={{whiteSpace:'nowrap'}} onClick={() => { setN(0); setWrong(0); }}>""",
    """<button className="ghost-btn" disabled={!n} style={{whiteSpace:'nowrap',minHeight:44}} onClick={() => { setN(0); setWrong(0); }}>""")
rep("""(mode === 'major' ? '장조 스케일을' : '화성 단음계를')""", """(mode === 'major' ? '장음계를' : '화성단음계를')""")
# the order of sharps and flats: its clef chips a finger's size; the row wraps
rep("""      <div style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',marginBottom:4}}>
        <div style={{fontSize:12,fontWeight:800,color:'var(--muted)',textTransform:'uppercase',letterSpacing:'0.05em'}}>""",
    """      <div style={{display:'flex',flexWrap:'wrap',gap:6,justifyContent:'space-between',alignItems:'center',marginBottom:4}}>
        <div style={{fontSize:12,fontWeight:800,color:'var(--muted)',textTransform:'uppercase',letterSpacing:'0.05em'}}>""")
rep("""{['treble', 'bass'].map(c => <button key={c} className={'chip' + (clef === c ? ' active' : '')} style={{padding:'3px 9px',fontSize:12}} onClick={() => setClef(c)}>""",
    """{['treble', 'bass'].map(c => <button key={c} className={'chip' + (clef === c ? ' active' : '')} style={{padding:'8px 12px',fontSize:13,minHeight:44}} onClick={() => setClef(c)}>""")
# a tool page's kicker: a tool may name its own (the concept book: its area · Concept book)
rep("""letterSpacing:'0.06em',marginBottom:12}}>{(TOOL_CATS.find(c => c.id === toolMeta(t.id).cat) || {}).name || 'Tool'}</div>""",
    """letterSpacing:'0.06em',marginBottom:12}}>{t.kicker || (TOOL_CATS.find(c => c.id === toolMeta(t.id).cat) || {}).name || 'Tool'}</div>""")
# the header's right side wraps on a narrow phone (the teacher row ran 27 px off the screen at 320)
rep("""          <div style={{display:'flex',alignItems:'center',gap:8,flex:'0 0 auto',marginLeft:'auto'}}>""",
    """          <div style={{display:'flex',flexWrap:'wrap',justifyContent:'flex-end',alignItems:'center',gap:8,flex:'0 1 auto',minWidth:0,marginLeft:'auto'}}>""")
# room at the foot of every page, so the round find button never covers the last line
rep("""      <div className="pb-main" key={mk} style={{maxWidth:600,margin:'0 auto',padding:'20px 16px 60px'}}>""",
    """      <div className="pb-main" key={mk} style={{maxWidth:600,margin:'0 auto',padding:'20px 16px 92px'}}>""")

# an unknown concept book says so (it printed a blank page)
rep("""        : ids.map(id => { const Wb = reg[id]; return Wb ? <Wb key={id}/> : null; })""",
    """        : ids.map(id => { const Wb = reg[id]; return Wb ? <Wb key={id}/> : kind === 'concept' ? <p key={id} style={{textAlign:'center',fontSize:16,margin:'40px 16px'}}>{t('No concept book called “' + id + '”.', '“' + id + '”라는 개념책이 없어요.')}</p> : null; })""")

# the circle of fifths: each key's relative minor inside it (o.minors: every minor at once); o.bare: no words (an icon)
rep("""const FIFTHS_TWIN = { B: ['B', 'C♭'], Db: ['D♭', 'C♯'] }, FIFTHS_TWIN_SIG = { B: '5♯ 7♭', Db: '5♭ 7♯' };""",
    """const FIFTHS_TWIN = { B: ['B', 'C♭'], Db: ['D♭', 'C♯'] }, FIFTHS_TWIN_SIG = { B: '5♯ 7♭', Db: '5♭ 7♯' };
const FIFTHS_MINOR = { C: 'Am', G: 'Em', D: 'Bm', A: 'F♯m', E: 'C♯m', B: ['G♯m', 'A♭m'], Gb: ['D♯m', 'E♭m'], Db: ['B♭m', 'A♯m'], Ab: 'Fm', Eb: 'Cm', Bb: 'Gm', F: 'Dm' };""")
rep("""      <text x={C + 44} y={C - 56} textAnchor="middle" fontSize={P ? 13 : 12} fontWeight="900" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{hint('more ♯ →', '♯ 많아짐 →')}</text>
      <text x={C - 44} y={C - 56} textAnchor="middle" fontSize={P ? 13 : 12} fontWeight="900" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{hint('← more ♭', '← ♭ 많아짐')}</text>""",
    """      {!o.minors && !o.bare && <text x={C + 44} y={C - 56} textAnchor="middle" fontSize={P ? 13 : 12} fontWeight="900" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{hint('more ♯ →', '♯ 많아짐 →')}</text>}
      {!o.minors && !o.bare && <text x={C - 44} y={C - 56} textAnchor="middle" fontSize={P ? 13 : 12} fontWeight="900" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{hint('← more ♭', '← ♭ 많아짐')}</text>}""")
rep("""          <text x={lx} y={ly + 4} textAnchor="middle" fontSize={P ? 14 : 12} fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{(o.twins && FIFTHS_TWIN_SIG[k]) || FIFTHS_SIG[i]}</text>""",
    """          {!o.bare && <text x={lx} y={ly + 4} textAnchor="middle" fontSize={P ? 14 : 12} fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{(o.twins && FIFTHS_TWIN_SIG[k]) || FIFTHS_SIG[i]}</text>}
          {o.minors && (() => { const [mx, my] = pt(-90 + i * 30 + (i === 5 ? -5 : i === 7 ? 5 : 0), R - 50), mn = FIFTHS_MINOR[k], two = Array.isArray(mn) ? (k === 'Gb' ? mn : [mn[0]]) : [mn];
            return <text x={mx} y={my + (two.length > 1 ? -3 : 5)} textAnchor="middle" fontSize={P ? 14 : 13} fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{two.map((x, j) => <tspan key={j} x={mx} dy={j ? 15 : 0}>{x}</tspan>)}</text>; })()}""")

# 9. verification (r2): shared parts
# the five checks on a narrow phone: the three buttons share the row's width (Got it! ran 34 px past its card at 320)
rep("""<div style={{flex:'0 0 auto',display:'flex',gap:4,marginLeft:'auto'}}>{[0, 1, 2].map(k =>""",
    """<div className="fc-btns" style={{flex:'0 0 auto',display:'flex',gap:4,marginLeft:'auto'}}>{[0, 1, 2].map(k =>""")
# the order of sharps and flats: its three buttons keep their words whole; the row wraps instead
rep("""      <div style={{display:'flex',gap:6,justifyContent:'center',marginTop:8}}>
        <button className="ghost-btn" disabled={n === 0} onClick={() => { setAuto(false); setN(x => Math.max(0, x - 1)); }}>""",
    """      <div className="ob-row" style={{display:'flex',flexWrap:'wrap',gap:6,justifyContent:'center',marginTop:8}}>
        <button className="ghost-btn" disabled={n === 0} onClick={() => { setAuto(false); setN(x => Math.max(0, x - 1)); }}>""")
rep("""    @media (max-width: 400px) { .lb-rem-row { flex-wrap: wrap; row-gap: 2px; } .lb-rem-txt { flex: 1 1 100%; overflow-wrap: anywhere; padding: 0 2px 2px; } }""",
    """    @media (max-width: 400px) { .lb-rem-row { flex-wrap: wrap; row-gap: 2px; } .lb-rem-txt { flex: 1 1 100%; overflow-wrap: anywhere; padding: 0 2px 2px; } }
    @media (max-width: 370px) { .fc-btns { flex: 1 1 100% !important; display: grid !important; grid-template-columns: repeat(3, minmax(0, 1fr)); margin-left: 0 !important; } .fc-btns > button { min-width: 0 !important; padding: 2px 4px !important; flex-direction: column; gap: 1px !important; line-height: 1.1; } }
    .ob-row > button { white-space: nowrap; word-break: keep-all; min-height: 44px; }
    [data-cb-tool] .chip { border-color: var(--navy-line); }
    [data-cb-tool] svg rect[fill="#1d1c22"] { fill: #26296b; }""")
# the scale builder joins 'one sound at a time': a step stops a pad that is still playing
rep("""    if (s === pat[n]) { playKey(r + offs[n + 1], 0.3);""",
    """    if (SSC_STOP.fn) { SSC_STOP.fn(); SSC_STOP.fn = null; }
    if (s === pat[n]) { playKey(r + offs[n + 1], 0.3);""")
# the address keeps the language, so Back and a refresh stay in Korean
rep("""      if (st.lock) p.set('lock', '1');
      history.replaceState(null, '', location.pathname + '?' + p.toString() + location.hash);""",
    """      if (st.lock) p.set('lock', '1');
      if (lang === 'ko') p.set('lang', 'ko');
      history.replaceState(null, '', location.pathname + '?' + p.toString() + location.hash);""")
rep("""}, [active.id, st.drill, st.tab, level, st.mode, st.lock, st.view, st.tool, st.kit, st.kn]);""",
    """}, [active.id, st.drill, st.tab, level, st.mode, st.lock, st.view, st.tool, st.kit, st.kn, lang]);""")
# signs in the rings drawn in the music font (the Korean fallback font's flat is wide, with a gap)
rep("""<tspan key={i} style={{fontFamily:'Inter, sans-serif'}}>{p}</tspan>""",
    """<tspan key={i} fontWeight="400" style={{fontFamily:MUSIC_FONT,fontSize:'1.2em'}}>{p}</tspan>""")
rep("""<tspan x={x} dy="-2.5">{a}</tspan><tspan x={x} dy="15">{b}</tspan></text>;""",
    """<tspan x={x} dy="-2.5">{pbAccT(a)}</tspan><tspan x={x} dy="15">{pbAccT(b)}</tspan></text>;""")
rep("""<tspan fontSize={dbl ? fs * 0.95 : fs * 0.78} fontWeight={dbl ? 400 : 800} style={{fontFamily:dbl ? MUSIC_FONT : 'Inter, sans-serif'}}>{g}</tspan>""",
    """<tspan fontSize={fs * 0.95} fontWeight="400" style={{fontFamily:MUSIC_FONT}}>{g}</tspan>""")

# the circle: o.bare is an icon (no letters, hidden from screen readers); signs in the music font; the twins' minors both named
rep("""    <svg viewBox="0 0 360 360" role="img" aria-label={label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>
      <circle cx={C} cy={C} r={R} fill="none" stroke="rgba(38,41,107,0.18)\"""",
    """    <svg viewBox="0 0 360 360" role={o.bare ? undefined : 'img'} aria-hidden={o.bare ? 'true' : undefined} aria-label={o.bare ? undefined : label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>
      <circle cx={C} cy={C} r={R} fill="none" stroke="rgba(38,41,107,0.18)\"""")
rep("""          {(k === 'Gb' || (o.twins && FIFTHS_TWIN[k])) ? <text x={x} y={y} textAnchor="middle" fontSize={P ? 14 : 13.5} fontWeight="900" fill={ink} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}><tspan x={x} dy="-2.5">{(FIFTHS_TWIN[k] || ['F♯', 'G♭'])[0]}</tspan><tspan x={x} dy="15">{(FIFTHS_TWIN[k] || ['F♯', 'G♭'])[1]}</tspan></text>""",
    """          {o.bare ? null : (k === 'Gb' || (o.twins && FIFTHS_TWIN[k])) ? <text x={x} y={y} textAnchor="middle" fontSize={P ? 14 : 13.5} fontWeight="900" fill={ink} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}><tspan x={x} dy="-2.5">{pbAccT((FIFTHS_TWIN[k] || ['F♯', 'G♭'])[0])}</tspan><tspan x={x} dy="15">{pbAccT((FIFTHS_TWIN[k] || ['F♯', 'G♭'])[1])}</tspan></text>""")
rep("""fontSize={P ? 14 : 12} fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{(o.twins && FIFTHS_TWIN_SIG[k]) || FIFTHS_SIG[i]}</text>}""",
    """fontSize={14} fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif',pointerEvents:'none'}}>{pbAccT((o.twins && FIFTHS_TWIN_SIG[k]) || FIFTHS_SIG[i])}</text>}""")
rep("""mn = FIFTHS_MINOR[k], two = Array.isArray(mn) ? (k === 'Gb' ? mn : [mn[0]]) : [mn];""",
    """mn = FIFTHS_MINOR[k], two = Array.isArray(mn) ? mn : [mn];""")
rep("""{two.map((x, j) => <tspan key={j} x={mx} dy={j ? 15 : 0}>{x}</tspan>)}""",
    """{two.map((x, j) => <tspan key={j} x={mx} dy={j ? 15 : 0}>{pbAccT(x)}</tspan>)}""")
rep(""">{hint('more ♯ →', '♯ 많아짐 →')}</text>}""", """>{pbAccT(hint('more ♯ →', '♯ 많아짐 →'))}</text>}""")
rep(""">{hint('← more ♭', '← ♭ 많아짐')}</text>}""", """>{pbAccT(hint('← more ♭', '← ♭ 많아짐'))}</text>}""")

# 5. the book itself
i = s.index("const LESSON_BOOKS = {")
s = s[:i] + open(here + '/cbscales.jsx', encoding='utf-8').read() + "\n" + s[i:]

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
