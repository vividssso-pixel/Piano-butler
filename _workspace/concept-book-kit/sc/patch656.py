import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:80])
    s = s.replace(old, new)
# PlaceIt: the letter named in the miss message was one step too high (pos 0 is the bottom line E, pos -1 is D below it)
rep("const pos2name = (p) => ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'][p + 1];",
    "const pos2name = (p) => ['D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G'][p + 1];")
# Minor lesson blurb: the lesson is on D minor, not A
rep("'Natural, harmonic and melodic, shown on A.', 'A에서 보는 자연, 화성, 가락.'", "'Natural, harmonic and melodic, shown on D.', 'D에서 보는 자연, 화성, 가락.'")

# ---- staff taps (sharp/flat order and finding the key): guide dots, bigger staff, and a message that names the wrong letter
rep("function KSStaff({ count, type, width = 170, ink = '#26296b', accent = '#e4572e', upto, clef = 'treble', numbers, onPick, ghostPos, ring, tonicPos, tonicFrom, tallBox }) {",
    "const KF_POS_NAME = ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A'];   // treble staff, bottom line = 0\nfunction KSStaff({ count, type, width = 170, ink = '#26296b', accent = '#e4572e', upto, clef = 'treble', numbers, onPick, ghostPos, ring, tonicPos, tonicFrom, tallBox, zoom = 1.6, dots }) {")
rep("style={{width:'100%',maxWidth:width * 1.6,display:'block',margin:'0 auto',cursor:onPick ? 'pointer' : undefined,touchAction:onPick ? 'manipulation' : undefined}} data-staff-pick",
    "style={{width:'100%',maxWidth:width * zoom,display:'block',margin:'0 auto',cursor:onPick ? 'pointer' : undefined,touchAction:onPick ? 'manipulation' : undefined}} data-staff-pick")
rep("      <ClefGlyph clef={clef} st={clef} yOf={yOf} ink={ink}/>\n      {accs.map((acc, i) => {",
    "      <ClefGlyph clef={clef} st={clef} yOf={yOf} ink={ink}/>\n      {dots && Array.from({ length: 11 }, (_, p) => <circle key={'dt' + p} cx={56 + accs.length * 15} cy={base - p * 5} r=\"1.4\" fill=\"#e4572e\" opacity=\"0.7\" pointerEvents=\"none\"/>)}\n      {accs.map((acc, i) => {")
rep("else { setBadPos(st); clear(); timers.current.push(setTimeout(() => setBadPos(null), 650)); }",
    "else { setBadPos(st); clear(); timers.current.push(setTimeout(() => setBadPos(null), 1400)); }")
rep("timers.current.push(setTimeout(() => { setBad(null); setBadPos(null); }, 650)); };",
    "timers.current.push(setTimeout(() => { setBad(null); setBadPos(null); }, keyIdx != null ? 650 : 1400)); };")
MSG = "{<div role=\"status\" style={{textAlign:'center',fontSize:13,fontWeight:700,color:'#c8361b',minHeight:18}}>{badPos != null ? t('That is ' + KF_POS_NAME[badPos] + '. Try again.', '그건 ' + KF_POS_NAME[badPos] + '예요. 다시 해 봐요.') : ''}</div>}"
rep("<div style={{maxWidth:260,margin:'0 auto'}}><KSStaff count={lit} type={type} width={200} numbers upto={lit > 0 ? lit - 1 : undefined} onPick={got >= 7 ? undefined : tapStaff} ghostPos={badPos}/></div>",
    "<div style={{maxWidth:340,margin:'0 auto'}}><KSStaff count={lit} type={type} width={200} zoom={2} dots={got < 7} numbers upto={lit > 0 ? lit - 1 : undefined} onPick={got >= 7 ? undefined : tapStaff} ghostPos={badPos}/>" + MSG + "</div>")
rep("<div style={{maxWidth:260,margin:'0 auto'}}><KSStaff count={lit} type={type} width={200} numbers upto={(stage === 1 || done) && !auto ? want : undefined} tallBox={sharp} onPick={done || auto ? undefined : (st) => hit(null, st)} ring={(stage === 1 || (done && !auto)) ? want : undefined} tonicPos={done && !auto ? tonicStep : undefined} tonicFrom={done && !auto && sharp ? lastPos : undefined} ghostPos={badPos}/></div>",
    "<div style={{maxWidth:340,margin:'0 auto'}}><KSStaff count={lit} type={type} width={200} zoom={2} dots={!(done || auto)} numbers upto={(stage === 1 || done) && !auto ? want : undefined} tallBox={sharp} onPick={done || auto ? undefined : (st) => hit(null, st)} ring={(stage === 1 || (done && !auto)) ? want : undefined} tonicPos={done && !auto ? tonicStep : undefined} tonicFrom={done && !auto && sharp ? lastPos : undefined} ghostPos={badPos}/>" + MSG + "</div>")

# ---- the circle of fifths: F sharp, C sharp and C flat share a slot with G flat, D flat and B; clicking the slot again flips between the twins
rep("const FIFTHS_TWIN = { B: ['B', 'C♭'], Db: ['D♭', 'C♯'] }, FIFTHS_TWIN_SIG",
    "const FIFTHS_SLOT = { 'F#': 'Gb', 'C#': 'Db', Cb: 'B' }, FIFTHS_PAIR = { B: ['B', 'Cb'], Gb: ['Gb', 'F#'], Db: ['Db', 'C#'] };\nconst fifthsSlot = (m) => FIFTHS_SLOT[m] || m;\nconst fifthsPick = (slot, cur) => { const tw = FIFTHS_PAIR[slot]; return !tw ? slot : fifthsSlot(cur) === slot ? tw[(tw.indexOf(cur) + 1) % tw.length] : tw[0]; };\nconst FIFTHS_TWIN = { B: ['B', 'C♭'], Db: ['D♭', 'C♯'] }, FIFTHS_TWIN_SIG")
# KfCircle
rep("  const [sel, setSel] = useState(FIFTHS.includes(ks.major) ? ks.major : 'C');\n  const sg = KEY_SIGS.find(x => x.major === sel) || KEY_SIGS[0];\n  const pick = (k) => { setSel(k); playKey(pcOfName(k), 0.5); const j = KEY_SIGS.findIndex(q => q.major === k); if (j >= 0) setI(j); };",
    "  const [selM, setSelM] = useState(FIFTHS.includes(fifthsSlot(ks.major)) ? ks.major : 'C');\n  const sel = fifthsSlot(selM), sg = KEY_SIGS.find(x => x.major === selM) || KEY_SIGS[0];\n  const pick = (slot) => { const k = fifthsPick(slot, selM); setSelM(k); playKey(pcOfName(k), 0.5); const j = KEY_SIGS.findIndex(q => q.major === k); if (j >= 0) setI(j); };")
rep("{cbKeyLines(sel)[0]}</div>\n    <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'6px 0 0'}}", "{cbKeyLines(selM)[0]}</div>\n    <div style={{textAlign:'center',fontSize:15,fontWeight:800,color:'#26296b',margin:'6px 0 0'}}")
# KfPiece
rep("    {view === 'circle' && (() => { const sel = FIFTHS.includes(ks.major) ? ks.major : 'C', sg = KEY_SIGS.find(x => x.major === sel) || KEY_SIGS[0];\n      const pick = (k) => { playKey(pcOfName(k), 0.5); const j = KEY_SIGS.findIndex(q => q.major === k); if (j >= 0) setI(j); };",
    "    {view === 'circle' && (() => { const sel = FIFTHS.includes(fifthsSlot(ks.major)) ? fifthsSlot(ks.major) : 'C', sg = FIFTHS.includes(fifthsSlot(ks.major)) ? ks : KEY_SIGS[0];\n      const pick = (slot) => { const k = fifthsPick(slot, ks.major); playKey(pcOfName(k), 0.5); const j = KEY_SIGS.findIndex(q => q.major === k); if (j >= 0) setI(j); };")

# ---- kf-what: one box, not two
rep("    <div className=\"try-box\" data-kf-lesson=\"what\" style={{background:'#fff',border:'1px solid var(--border)',borderRadius:10,padding:'10px 10px 12px',margin:'4px 0 16px'}}>\n      <div style={titleStyle}>{view === 'all' ? t('What a key signature does'",
    "    <div data-kf-inner=\"what\">\n      <div style={titleStyle}>{view === 'all' ? t('What a key signature does'")

# ---- drill, ko: key names are made when the question is made; show them in the language on screen
rep("function genKnQuestion(lv, prev) {", "const knLang = (s) => typeof s !== 'string' ? s : LANG === 'ko' ? s.replace(/ major$/, '장조').replace(/ minor$/, '단조') : s.replace(/장조$/, ' major').replace(/단조$/, ' minor');\nfunction genKnQuestion(lv, prev) {")
rep("  if (q.kind === 'kn-min') return majName(q.k) + ' → ' + q.answer;\n  if (q.kind === 'kn-last') return q.answer + t(", "  if (q.kind === 'kn-min') return majName(q.k) + ' → ' + knLang(q.answer);\n  if (q.kind === 'kn-last') return knLang(q.answer) + t(")
rep("  if (q.kind && q.kind.indexOf('kn-') === 0) return q.answer + ' (' + sigLabel(q.k) + ')';", "  if (q.kind && q.kind.indexOf('kn-') === 0) return knLang(q.answer) + ' (' + sigLabel(q.k) + ')';")
rep("{q.kind === 'kn-order' ? prettyNote(c) : c}</button>)}</div></div>;\n}\nconst SkgQuestionAll", "{q.kind === 'kn-order' ? prettyNote(c) : knLang(c)}</button>)}</div></div>;\n}\nconst SkgQuestionAll")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
