import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)
SC = '/home/claude/pbtest/sc/'

# ── re-splice the three lesson files (kq, iv, ch) at their markers
i = s.index("// ─── Keys and staff, built again from the start in the Scales style"); j = s.index("\nKS_ROWS.forEach(")
s = s[:i] + open(SC + 'kq.jsx', encoding='utf-8').read() + s[j:]
i = s.index("// ─── Intervals, built in the Keys and staff style"); j = s.index("\nconst scDirTag = ")
s = s[:i] + open(SC + 'iv.jsx', encoding='utf-8').read() + "\n" + open(SC + 'ch.jsx', encoding='utf-8').read() + s[j:]

# ── 1. the keyboard crop ends on a white-key edge, never in the middle of a key (ScKeys, used by every new lesson and Scales)
rep("  const x0 = Math.min(...ks.map(kx)) - 24, x1 = Math.max(...ks.map(kx)) + 24;\n  const pt = (i) => [kx(i), white(i) ? 99 : 58];",
    "  const lo0 = Math.min(...ks), hi0 = Math.max(...ks), lo = white(lo0) ? lo0 : lo0 - 1, hi = white(hi0) ? hi0 : hi0 + 1;\n  const x0 = kx(lo) - 19, x1 = kx(hi) + 19;\n  const pt = (i) => [kx(i), white(i) ? 99 : 58];")


# the keyboard: black keys outside the crop are not drawn (a half black key at the edge was the 'clipping')
rep("      {blacks.map(k => {", "      {blacks.filter(k => !vx || (k.x + blackW / 2 > vx[0] + 6 && k.x + blackW / 2 < vx[1] - 6)).map(k => {")
rep("  const x0 = kx(lo) - 19, x1 = kx(hi) + 19;", "  const x0 = kx(lo) - 18.5, x1 = kx(hi) + 18.5;")

# ── 2. Scales and Modes: the line turns red on a wrong answer and green when done (the same colours as the kq lessons)
rep("const scRow = (children) =>", "const scLineEl = (line, st) => { const x = typeof line === 'string' ? line : (line && line.props && typeof line.props.children === 'string') ? line.props.children : ''; const bad = /^(Not\\b|No[.:,]|그 건반이 아니|아니에요|엄지 건반이 아니|[가-힣A-G♯♭ ]{0,14}(이|가) 아니에요)/.test(x), good = /^(Yes|That is|All |Both |Up and down|Found|맞아요|이게|모두|둘 다|올라갔다|다 찾았|다른 건 하나뿐|완성)/.test(x);\n  return <div style={{...(st || scS.line), color: bad ? '#c8361b' : good ? '#2e8a6e' : (st || scS.line).color}}>{line}</div>; };\nconst scRow = (children) =>")
s = s.replace("<div style={scS.line}>{line}</div>", "{scLineEl(line)}").replace("<div style={lineStyle}>{line}</div>", "{scLineEl(line, lineStyle)}")
s = s.replace("t('Hide the staff', '스태프 숨기기') : t('Show on the staff', '스태프로 보여주기')", "t('Hide the staff', '오선 숨기기') : t('Show on the staff', '오선으로 보여주기')")

# ── 3. Key signatures: a wrong key tap says what it was and where to look; the word row is hidden while she taps
rep("  const [badPos, setBadPos] = useState(null);\n  const [stage, setStage] = useState(0);", "  const [badPos, setBadPos] = useState(null);\n  const [badMsg, setBadMsg] = useState(null);\n  const [stage, setStage] = useState(0);")
rep("  useEffect(() => { setStage(0); setBad(null); setBadPos(null); }, [n, phase]);", "  useEffect(() => { setStage(0); setBad(null); setBadPos(null); setBadMsg(null); }, [n, phase]);\n  const keyNm = (i) => { const w = KQ_L[((i % 12) + 12) % 12]; return w ? [w, w] : ['a black key', '검은건반']; };\n  const signNm = (nm) => prettyNote(nm);")
rep("    const flash = () => { if (keyIdx != null) setBad(keyIdx); else setBadPos(step); timers.current.push(setTimeout(() => { setBad(null); setBadPos(null); }, keyIdx != null ? 650 : 1400)); };",
    "    const flash = () => { if (keyIdx != null) { setBad(keyIdx); const kn = keyNm(keyIdx), tgt = stage === 0 ? signNm(order[want]) : prettyNote(k.major); setBadMsg([`That is ${kn[0]}. ` + (stage === 0 ? (sharp ? 'The last sharp is ' : 'The second last flat is ') + tgt + '.' : 'A half step up from ' + signNm(order[want]) + ' is ' + tgt + '.'), `그건 ${kn[1]}예요. ` + (stage === 0 ? (sharp ? '마지막 샵은 ' : '뒤에서 두 번째 플랫은 ') + tgt + '이에요.' : signNm(order[want]) + '에서 반음 위는 ' + tgt + '예요.')]); } else setBadPos(step); timers.current.push(setTimeout(() => { setBad(null); setBadPos(null); setBadMsg(null); }, keyIdx != null ? 1600 : 1400)); };")
rep("    else { setBad(i); clear(); timers.current.push(setTimeout(() => setBad(null), 650)); }\n  };\n  const tapStaff = (st) => {",
    "    else { setBad(i); clear(); const kn = keyNm(i); setBadMsg(['That is ' + kn[0] + '. ' + (sharp ? 'Sharp ' : 'Flat ') + (got + 1) + ' is ' + prettyNote(order[got]) + '.', '그건 ' + kn[1] + '예요. ' + (got + 1) + '번 ' + (sharp ? '샵은 ' : '플랫은 ') + prettyNote(order[got]) + '이에요.']); timers.current.push(setTimeout(() => { setBad(null); setBadMsg(null); }, 1600)); }\n  };\n  const tapStaff = (st) => {")
rep("{badPos != null ? t('That is ' + KF_POS_NAME[badPos] + '. Try again.', '그건 ' + KF_POS_NAME[badPos] + '예요. 다시 해 봐요.') : ''}</div>}", "{badPos != null ? t('That is ' + KF_POS_NAME[badPos] + '. Try again.', '그건 ' + KF_POS_NAME[badPos] + '예요. 다시 해 봐요.') : badMsg ? t(badMsg[0], badMsg[1]) : ''}</div>}", 2)
rep("    <div style={{display:'flex',flexWrap:'wrap',gap:'0 6px',justifyContent:'center',fontSize:14,fontWeight:700,lineHeight:1.5,margin:'2px 0 6px',textWrap:'balance'}}>\n      {words.map((w, i) => <span key={i} style={{opacity:i < got ? 0.45 : 1,color:i === got ? '#c8361b' : '#26296b',fontWeight:i === got ? 900 : 700}}>{w}</span>)}\n    </div>",
    "    {got >= 7 && <div style={{display:'flex',flexWrap:'wrap',gap:'0 6px',justifyContent:'center',fontSize:14,fontWeight:700,lineHeight:1.5,margin:'2px 0 6px',textWrap:'balance'}}>\n      {words.map((w, i) => <span key={i} style={{opacity:0.45,color:'#26296b',fontWeight:700}}>{w}</span>)}\n    </div>}")
# KfMinor: the same for its two taps
rep("    else { setBad(idx); clearTimeout(timer.current); timer.current = setTimeout(() => setBad(null), 650); }\n  };\n  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};\n  const stageLine = tryMode",
    "    else { const w = KQ_L[((idx % 12) + 12) % 12]; setBad(idx); setBadTxt(stage === 0 ? ['That is ' + (w || 'a black key') + '. Find the major key first: the key signature’s key.', '그건 ' + (w || '검은건반') + '예요. 먼저 장조, 이 조표의 조를 찾아요.'] : ['That is ' + (w || 'a black key') + '. Count 3 half steps down from ' + prettyNote(ks.major) + '.', '그건 ' + (w || '검은건반') + '예요. ' + prettyNote(ks.major) + '에서 반음 3개 아래로 세어 보세요.']); clearTimeout(timer.current); timer.current = setTimeout(() => { setBad(null); setBadTxt(null); }, 1600); }\n  };\n  const prim = {...KF_BTN,minWidth:140,background:'#26296b',color:'#fffefa',borderColor:'#26296b'};\n  const stageLine = tryMode && badTxt ? t(badTxt[0], badTxt[1]) : tryMode")
rep("  const [bad, setBad] = useState(null);\n  const [found, setFound] = useState(false);\n  const [intro, setIntro] = useState(true);", "  const [bad, setBad] = useState(null), [badTxt, setBadTxt] = useState(null);\n  const [found, setFound] = useState(false);\n  const [intro, setIntro] = useState(true);")
rep("    <div key={ph + r + e + stage + found + intro} style={{textAlign:'center',fontSize:16,fontWeight:800,color:'#26296b',", "    <div key={ph + r + e + stage + found + intro} style={{textAlign:'center',fontSize:16,fontWeight:800,color:badTxt ? '#c8361b' : '#26296b',")

# ── 4. Accidentals: the names and bands are hidden while she answers (names after the answer; bands after a miss, as the guide)
rep("        {on && ask !== j && <text x={n.x} y={84} textAnchor=\"middle\" fontSize=\"12\" fontWeight=\"900\" fill={n.g ? col : '#6d6f9c'}>{NAME(n)}</text>}", "        {on && ask < 0 && <text x={n.x} y={84} textAnchor=\"middle\" fontSize=\"12\" fontWeight=\"900\" fill={n.g ? col : '#6d6f9c'}>{NAME(n)}</text>}", 2)
rep("      {staff(AC_BAR.length - 1, -1, AC_BANDS.length, -1, done ? -1 : j)}", "      {staff(AC_BAR.length - 1, -1, done || miss ? AC_BANDS.length : 0, -1, done ? -1 : j)}", 2)
rep("t('Not that one. Is the note on a coloured band?', '그 건반이 아니에요. 음표가 색 띠 위에 있나요?')", "t('Not that one. Look for a sign on this note, or earlier in its bar on the same line or space: the band shows how far it reaches.', '그 건반이 아니에요. 이 음표나 같은 마디 앞쪽 같은 줄·칸의 임시표를 찾아요. 띠가 어디까지 미치는지 보여 줘요.')", 2)

# ── 5. terms, app-wide
s = s.replace('샤프', '샵').replace('반 걸음', '반음').replace('온 걸음', '온음').replace('코랄', '산호색')
s = s.replace("'(orange)'", "'(coral)'").replace('under the orange box', 'under the coral box').replace('the orange box', 'the coral box')
s = s.replace("'Tone, tone, semitone, tone, tone, tone, semitone", "'Whole, whole, half, whole, whole, whole, half")
s = s.replace("a tone and a semitone up (T+S)", "a whole step and a half step up (T+S)").replace("a tone and a semitone down (T+S)", "a whole step and a half step down (T+S)")
s = s.replace("7th note a semitone", "7th note a half step").replace("a semitone below the tonic", "a half step below the tonic").replace("must be a tone", "must be a whole step")
s = s.replace("'완전8도'", "'옥타브'").replace("perfect octave", "octave")
s = s.replace("어느 음이 “집”처럼 느께져요?", "어느 음이 “집”처럼 느껴져요?")
s = s.replace("rangeName(low) + '은(는) 더 낮은 곳에서 시작해요.'", "cpxJ(rangeName(low), '은', '는') + ' 더 낮은 곳에서 시작해요.'")
s = re.sub(r"mdNm\(m\) \+ '은\(는\) ", "cpxJ(mdNm(m), '은', '는') + ' ", s)
s = re.sub(r"m\.nameKo \+ '은\(는\) ", "cpxJ(m.nameKo, '은', '는') + ' ", s)
s = re.sub(r"M\.nameKo \+ '은\(는\) ", "cpxJ(M.nameKo, '은', '는') + ' ", s)
s = s.replace("' + L + '은(는) ' + (small ? '2' : '3') + '개 묶음", "' + L + '는 ' + (small ? '2' : '3') + '개 묶음")

rep("const rangeName = (n) => t(n, RANGE_KO[n] || n);", "const rangeName = (n) => t(n, RANGE_KO[n] || n);\nconst kqRangeName = (n) => rangeName(n).replace('today, ', '').replace('오늘날, ', '');")
# ── 6. the order of the Pitch concepts: Keys and staff, Accidentals, Intervals, Scales, Key signatures, Chords, Modes
rep("const homeCats = (areaId) => TOOL_CATS.filter(c => c.area === areaId).flatMap(c => c.id === 'p-scales' ? HOME_VIRTUAL : [c]);",
    "const HOME_PITCH_ORDER = ['p-staff', 'p-clock', 'p-intervals', 'p-scale', 'p-keysig', 'p-chords', 'p-modes'];\nconst homeCats = (areaId) => { const all = TOOL_CATS.filter(c => c.area === areaId).flatMap(c => c.id === 'p-scales' ? HOME_VIRTUAL : [c]); return areaId === 'pitch' ? HOME_PITCH_ORDER.map(id => all.find(c => c.id === id)).filter(Boolean).concat(all.filter(c => !HOME_PITCH_ORDER.includes(c.id))) : all; };")

# ── 7. lessons numbered straight through the groups on the Home (1 … 9), so a drill level can name its lesson
rep("          {live.groups && live.groups.map((g, gi) => { const on =", "          {live.groups && live.groups.map((g, gi) => { const off = live.groups.slice(0, gi).reduce((a, x) => a + x.lessons.length, 0); const on =")
rep("                {g.lessons.map((id, i) => { const tl = TOOLS.find(x => x.id === id); return tl ? step(i + 1, tl.title, tl.blurb, false,", "                {g.lessons.map((id, i) => { const tl = TOOLS.find(x => x.id === id); return tl ? step(off + i + 1, tl.title, tl.blurb, false,")

# ── 8. drill levels carry the lesson number and a short name (the Key signatures and Scales drills already do)
rep("const IV_LEVELS = [\n", "const IV_LEVELS = [   // num = the Home lesson the level follows (Intervals: 1 Count the letters … 9 The tritone)\n")
for old, num, en, ko in [
    ("{ n: 1, label: 'Number only · treble',", '1', 'Count the letters', '글자 세기'),
    ("{ n: 2, label: 'Number only · treble and bass',", '2', 'On the staff', '오선에서'),
    ("{ n: 3, label: 'Major or minor 3rd, perfect 4th, 5th, 8ve',", '3', 'Major or minor 3rd', '장3도? 단3도?'),
    ("{ n: 4, label: 'Above the tonic in major keys',", '4', 'Above the key note', '으뜸음 위'),
    ("{ n: 5, label: 'Any interval · number and quality',", '5', 'Name it', '이름 맞히기'),
    ("{ n: 6, label: 'Build it on the keyboard',", '3–5', 'Build it', '만들기'),
    ("{ n: 7, label: 'By ear: 3rds, 4th, 5th, octave',", '7', 'By ear', '듣기'),
    ("{ n: 8, label: 'Invert it (Grade 3)',", '8', 'Upside down', '뒤집기'),
    ("{ n: 9, label: 'Any interval incl. aug 4th / dim 5th (Grade 3)',", '9', 'The tritone', '트라이톤')]:
    if s.count(old) == 1: s = s.replace(old, old + " num: '" + num + "', short: ['" + en + "', '" + ko + "'],")
    else: print('skip', s.count(old), old[:50])
for old, num, en, ko in [
    ("{ n: 1, label: 'Stack a triad: its letters',", '1', 'Stack a triad', '3화음 쌓기'),
    ("{ n: 2, label: 'Name the root',", '1', 'The root', '근음'),
    ("{ n: 3, label: 'Major or minor?',", '4', 'Major or minor?', '장3화음? 단3화음?'),
    ("{ n: 4, label: 'Write it: the triad on a note',", '2', 'On the staff', '오선에서'),
    ("{ n: 5, label: 'Listen: major or minor?',", '5', 'By ear', '듣기'),
    ("{ n: 7, label: 'Tonic triads: which key?',", '6', 'The tonic triad', '으뜸화음'),
    ("{ n: 8, label: 'I, IV or V, in my keys',", '7', 'I, IV or V', 'I, IV, V'),
    ("{ n: 9, label: 'Extra: spell I, IV and V',", '7', 'Spell I, IV, V', 'I, IV, V 음이름')]:
    if s.count(old) == 1: s = s.replace(old, old + " num: '" + num + "', short: ['" + en + "', '" + ko + "'],")
    else: print('skip', s.count(old), old[:50])
for old, num, en, ko in [
    ("{ n: 1, label: 'High or low?',", '1', 'High or low?', '높을까 낮을까?'),
    ("{ n: 2, label: 'Small house or big house?',", '1', 'Group of 2 or 3?', '2개? 3개?'),
    ("{ n: 3, label: 'Whose house is this white key?',", '2', 'Which group?', '어느 묶음?')]:
    if s.count(old) == 1: s = s.replace(old, old + " num: '" + num + "', short: ['" + en + "', '" + ko + "'],")
    else: print('skip', s.count(old), old[:50])
for old, num, en, ko in [
    ("{ n: 1, label: 'White keys · name the key',", '2', 'Name the key', '건반 이름'),
    ("{ n: 2, label: 'White keys · find the key',", '2', 'Find the key', '건반 찾기'),
    ("{ n: 3, label: 'Two octaves · both ways',", '3', 'Two octaves', '두 옥타브'),
    ("{ n: 4, label: 'Next letter up or down',", '3', 'Next letter', '다음 글자'),
    ("{ n: 5, label: 'Skip a letter, up or down',", '3', 'Skip a letter', '한 글자 건너')]:
    if s.count(old) == 1: s = s.replace(old, old + " num: '" + num + "', short: ['" + en + "', '" + ko + "'],")
    else: print('skip', s.count(old), old[:50])
rep("  { n: 5, label: 'Listen: major or minor?', num: '5', short: ['By ear', '듣기'], kind: 'ear', time: 10, noPrint: true },\n  { n: 6, label: 'The bass staff', kind: 'bass', time: 8 },", "  { n: 5, label: 'Listen: major or minor?', num: '5', short: ['By ear', '듣기'], kind: 'ear', time: 10, noPrint: true },\n  { n: 6, label: 'The bass staff', num: '2', short: ['Bass staff', '낮은음자리표'], kind: 'bass', time: 8 },")

# the intervals drill in use is IVX_LEVELS: lesson numbers from the Home (1 Count the letters, 2 On the staff, 3 Half steps, 4 Above the key note, 5 One half step smaller, 6 Melodic/harmonic, 7 Hear, 8 Upside down, 9 Tritone)
for old, num, en, ko in [
    ("{ n: 1, label: 'Count it', kind: 'count', time: 8 },", '1', 'Count it', '세어 보기'),
    ("{ n: 2, label: 'Count it: together too', kind: 'count2', time: 8 },", '2', 'On the staff', '오선에서'),
    ("{ n: 3, label: 'In C or G position', kind: 'hand', time: 8 },", '1', 'In the hand', '손 안에서'),
    ("{ n: 4, label: 'Write it: the note above', kind: 'write', time: 14 },", '2', 'Write it', '써 보기'),
    ("{ n: 5, label: 'Melodic or harmonic?', kind: 'mh', time: 6 },", '6', 'Melodic or harmonic?', '선율? 화성?'),
    ("{ n: 6, label: 'The bass staff', kind: 'bass', time: 8 },", '2', 'Bass staff', '낮은음자리표'),
    ("{ n: 7, label: 'Listen: 2nd, 3rd, 5th or octave?', kind: 'ear', time: 12, noPrint: true },", '7', 'By ear', '듣기'),
    ("{ n: 8, label: 'Above the tonic, in my keys', kind: 'tonic', time: 9 },", '4', 'Above the key note', '으뜸음 위'),
    ("{ n: 9, label: 'Extra: major or perfect?', kind: 'mp', time: 8 },", '4–5', 'Major or perfect?', '장? 완전?')]:
    rep(old, old[:-3] + ", num: '" + num + "', short: ['" + en + "', '" + ko + "'] },")
# the Home groups open the level that follows them: number 1-2 -> 1, quality 3-5 -> 8, hearing 6-7 -> 5, upside down -> 9 (no level yet)
rep("lessons: ['iv-half', 'iv-tonic', 'iv-minor'], check: 'intervals', level: 3 }", "lessons: ['iv-half', 'iv-tonic', 'iv-minor'], check: 'intervals', level: 8 }")
rep("lessons: ['iv-mh', 'iv-ear'], check: 'intervals', level: 7 }", "lessons: ['iv-mh', 'iv-ear'], check: 'intervals', level: 5 }")
rep("lessons: ['iv-invert', 'iv-tritone'], check: 'intervals', level: 8 }", "lessons: ['iv-invert', 'iv-tritone'], check: 'intervals', level: 9 }")


# the level pills in lesson order
rep("Object.assign(INTERVALS_DRILL, { levels: IVX_LEVELS,", "IVX_LEVELS.sort((a, b) => parseFloat(a.num) - parseFloat(b.num));\nObject.assign(INTERVALS_DRILL, { levels: IVX_LEVELS,")
rep("Object.assign(CHORDS_DRILL, { levels: CHX_LEVELS,", "CHX_LEVELS.sort((a, b) => parseFloat(a.num) - parseFloat(b.num));\nObject.assign(CHORDS_DRILL, { levels: CHX_LEVELS,")
rep("const FIRST_STEPS_DRILL = {", "FS_ALL_LEVELS.sort((a, b) => parseFloat(a.num) - parseFloat(b.num));\nconst FIRST_STEPS_DRILL = {")

# the older staff / ledger / range drills: a short name each (their levels predate the new lessons)
for old, en, ko in [
    ("{ n: 1, label: 'Line or space?',", 'Line or space?', '줄? 칸?'), ("{ n: 2, label: 'Step or skip? Up or down?',", 'Step or skip?', '한 걸음? 건너?'),
    ("{ n: 5, label: 'Around Clara: both staves',", 'Both staves', '두 오선'), ("{ n: 6, label: 'Write it: tap where it goes',", 'Write it', '써 보기'),
    ("{ n: 1, label: 'Clef check: treble or bass?',", 'Treble or bass?', '높은? 낮은?'), ("{ n: 2, label: 'Treble clef: every line and space',", 'Treble names', '높은음자리 이름'),
    ("{ n: 3, label: 'Bass clef: every line and space',", 'Bass names', '낮은음자리 이름'), ("{ n: 4, label: 'The five landmarks',", 'Landmarks', '기준 음'),
    ("{ n: 5, label: 'Landmark hop: a step or a skip away',", 'From a landmark', '기준 음에서'), ("{ n: 6, label: 'Both clefs, fast',", 'Both clefs', '두 음자리표'),
    ("{ n: 1, label: 'One ladder: treble clef',", 'Treble ledger', '높은음자리 덧줄'), ("{ n: 2, label: 'One ladder: bass clef',", 'Bass ledger', '낮은음자리 덧줄'),
    ("{ n: 3, label: 'Two ladders, both clefs',", 'Two ledgers', '덧줄 둘'), ("{ n: 4, label: 'High C and low C: a step or a skip',", 'High C, low C', '높은 C, 낮은 C'),
    ("{ n: 5, label: 'Between the staves: the same key, two ways',", 'Middle C', '가운데 도'), ("{ n: 6, label: 'Up to three ladders, fast (Grade 2)',", 'Three ledgers', '덧줄 셋'),
    ("{ n: 1, label: 'Low, middle or high?',", 'Low or high?', '낮을까 높을까?'), ("{ n: 2, label: 'Which sounds higher?',", 'Which is higher?', '어느 쪽이 높아요?'),
    ("{ n: 3, label: 'Which family?',", 'Which family?', '어느 가족?'), ("{ n: 4, label: 'How does it make its sound?',", 'How it sounds', '소리 내는 법'),
    ("{ n: 5, label: 'Which can go lower?',", 'Which goes lower?', '어느 쪽이 더 낮아요?'), ("{ n: 6, label: 'Listen: higher or lower?',", 'Listen', '듣기'),
    ("{ n: 7, label: 'Listen: low, middle or high?',", 'Listen: where?', '듣기: 어디?')]:
    if s.count(old) == 1: s = s.replace(old, old + " short: ['" + en + "', '" + ko + "'],")
    else: print('skip', s.count(old), old[:50])
s = s.replace("{ n: 7, label: 'Find it on the keys (exact octave)',", "{ n: 7, label: 'Find it on the keys (exact octave)', short: ['On the keys', '건반에서'],")
s = s.replace("{ n: 7, label: 'Find it on the keys',", "{ n: 7, label: 'Find it on the keys', short: ['On the keys', '건반에서'],")

open(dst, 'w', encoding='utf-8').write(s); print('ok')
