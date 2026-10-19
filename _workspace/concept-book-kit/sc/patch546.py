import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)

# ── 1. the Push-a-key tool: one sign at a time (only = 'sharp' | 'flat' | 'natural') ──
rep("function SharpFlatMover() {", "function SharpFlatMover({ only }) {")
rep("Try E and B too.</>}</div>\n      <svg viewBox", "Try E and B too.</>}</div>}\n      <svg viewBox")

rep("  let msg = t('Tap a white key, then push it up or down.', '흰건반을 누르고, 위나 아래로 밀어 봐요.');",
    "  let msg = only === 'sharp' ? t('Tap a white key, then push it up.', '흰건반을 누르고, 위로 밀어 봐요.') : only === 'flat' ? t('Tap a white key, then push it down.', '흰건반을 누르고, 아래로 밀어 봐요.')\n    : t('Tap a white key, then push it up or down.', '흰건반을 누르고, 위나 아래로 밀어 봐요.');")
rep("      <div style={actTitle}>{t('Push a key: sharp or flat', '건반 밀기: 샤프 또는 플랫')}</div>\n      <div style={actNote}>{LANG === 'ko' ?",
    "      <div style={actTitle}>{only === 'sharp' ? t('Push a key up: the sharp ♯', '건반 올리기: 샤프 ♯') : only === 'flat' ? t('Push a key down: the flat ♭', '건반 내리기: 플랫 ♭') : only === 'natural' ? t('Push a key, then cancel it: the natural ♮', '밀었다가 취소하기: 내추럴 ♮') : t('Push a key: sharp or flat', '건반 밀기: 샤프 또는 플랫')}</div>\n"
    "      {only ? <div style={actNote}>{only === 'sharp' ? (LANG === 'ko' ? <>샤프(♯)는 음을 <b>반음</b> 올려요: 건반 하나 <b>오른쪽</b>. 흰건반을 누르고 밀어 봐요. E와 B도 해 봐요.</> : <>A sharp (♯) raises a note by <b>one semitone</b>: one key to the <b>right</b>. Tap a white key and push it. Try E and B too.</>)\n"
    "        : only === 'flat' ? (LANG === 'ko' ? <>플랫(♭)은 음을 <b>반음</b> 내려요: 건반 하나 <b>왼쪽</b>. 흰건반을 누르고 밀어 봐요. C와 F도 해 봐요.</> : <>A flat (♭) lowers a note by <b>one semitone</b>: one key to the <b>left</b>. Tap a white key and push it. Try C and F too.</>)\n"
    "        : (LANG === 'ko' ? <>내추럴(♮)은 샤프나 플랫을 <b>취소</b>해요: 원래 음으로 돌아와요. 흰건반을 누르고, 밀어 본 다음 ♮을 눌러요.</> : <>A natural (♮) <b>cancels</b> a sharp or a flat: back to the plain note. Tap a white key, push it, then press ♮.</>)}</div>\n"
    "      : <div style={actNote}>{LANG === 'ko' ?")
rep("        <button className=\"ghost-btn\" style={{padding:'8px 10px',fontSize:14}} disabled={!base.white} onClick={() => push(-1)}>{t('← ♭ flat', '← ♭ 플랫')}</button>\n"
    "        <button className=\"ghost-btn\" style={{padding:'8px 10px',fontSize:14}} disabled={!base.white} onClick={() => push(1)}>{t('♯ sharp →', '♯ 샤프 →')}</button>\n"
    "        <button className=\"ghost-btn\" style={{padding:'8px 10px',fontSize:14}} disabled={!dir || !valid || back} onClick={() => { setBack(true); setNonce(x => x + 1); setTimeout(() => playKey(from), 350); }}>{t('♮ natural', '♮ 내추럴')}</button>",
    "        {only !== 'sharp' && <button className=\"ghost-btn\" style={{padding:'8px 10px',fontSize:14}} disabled={!base.white} onClick={() => push(-1)}>{t('← ♭ flat', '← ♭ 플랫')}</button>}\n"
    "        {only !== 'flat' && <button className=\"ghost-btn\" style={{padding:'8px 10px',fontSize:14}} disabled={!base.white} onClick={() => push(1)}>{t('♯ sharp →', '♯ 샤프 →')}</button>}\n"
    "        {only !== 'sharp' && only !== 'flat' && <button className=\"ghost-btn\" style={{padding:'8px 10px',fontSize:14}} disabled={!dir || !valid || back} onClick={() => { setBack(true); setNonce(x => x + 1); setTimeout(() => playKey(from), 350); }}>{t('♮ natural', '♮ 내추럴')}</button>}")

# ── 2. the three lessons as short tools (hidden from the Toolbox), then the Home concept ──
rep("// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(",
"""// Phase 543: Semitones and accidentals on the Home. Sharp, flat and natural are each their own lesson; every older tool of the concept sits in the order of the lessons
[['cl-sharp', 'sharp', 'The sharp ♯', '샤프 ♯', 'One semitone up: one key to the right.', '반음 위로: 건반 하나 오른쪽.'],
 ['cl-flat', 'flat', 'The flat ♭', '플랫 ♭', 'One semitone down: one key to the left.', '반음 아래로: 건반 하나 왼쪽.'],
 ['cl-natural', 'natural', 'Cancel it: the natural ♮', '취소하기: 내추럴 ♮', 'Push a key, then press ♮ to cancel it.', '건반을 밀고, ♮로 취소해 봐요.']].forEach(([id, only, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '반음과 임시표' : 'Semitones and accidentals'); }, C: () => <SharpFlatMover only={only}/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-clock';
});
// the Toolbox: a concept's book, right under its name (open on screen, or print)
function CbCard(""")

rep("const HOME_LIVE = {\n  'p-keysig': {",
"""const HOME_LIVE = {
  'p-clock': {
    lessons: ['tone-semitone', 'cl-sharp', 'cl-flat', 'sac-signs', 'cl-natural', 'sac-natural', 'chromatic', 'accidental-bar', 'sac-bar', 'sac-line', 'sac-tune', 'accidental-cards', 'sharp-flat'], check: 'clock', tools: [], more: [],
    checkLine: ['Questions, level by level', '문제를 단계별로'],
  },
  'p-keysig': {""")

# ── 3. the questions: feedback right under the question for the two older question screens ──
rep("function TnQuestion({ q, level, given, locked, onAnswer, pixel }) {", "function TnQuestion({ q, level, given, locked, onAnswer, pixel, fbAbove }) {")
rep("  const choose = (opts, cols = 2) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',1fr)',gap:8,marginTop:14}}>",
    "  const root = fbAbove ? { display: 'contents' } : undefined, pic = (n) => <div style={{order:2}}>{n}</div>;\n  const choose = (opts, cols = 2) => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',1fr)',gap:8,marginTop:14,order:3}}>")
rep("  if (q.kind === 'hw' || q.kind === 'wn') return (<div>", "  if (q.kind === 'hw' || q.kind === 'wn') return (<div style={root}>")
rep("    <TapKeyboard octaves={2} labels=\"white\" marks={{ [q.a]: 'target', [q.b]: 'target' }} pixel={pixel}/>", "    {pic(<TapKeyboard octaves={2} labels=\"white\" marks={{ [q.a]: 'target', [q.b]: 'target' }} pixel={pixel}/>)}")
rep("  if (q.kind === 'bname') return (<div>", "  if (q.kind === 'bname') return (<div style={root}>")
rep("    <TapKeyboard octaves={1} labels=\"white\" marks={{ [q.a]: 'target' }} pixel={pixel}/>\n    {choose(q.choices.map(c => [c, prettyNote(c)]), 4)}", "    {pic(<TapKeyboard octaves={1} labels=\"white\" marks={{ [q.a]: 'target' }} pixel={pixel}/>)}\n    {choose(q.choices.map(c => [c, prettyNote(c)]), 4)}")
rep("  if (q.kind === 'enh') return (<div>\n    {prompt(t('One key, two names. What is its other name?', '건반 하나, 이름 둘. 다른 이름은?'))}\n    <div style={{textAlign:'center',fontSize:60,fontWeight:900,margin:'0 0 6px',color:BK.ink}}>",
    "  if (q.kind === 'enh') return (<div style={root}>\n    {prompt(t('One key, two names. What is its other name?', '건반 하나, 이름 둘. 다른 이름은?'))}\n    <div style={{textAlign:'center',fontSize:60,fontWeight:900,margin:'0 0 6px',color:BK.ink,order:2}}>")
rep("    return (<div>\n      {prompt(t('Read the note with its sign. Tap its key.', '기호가 붙은 음을 읽어요. 그 건반을 눌러요.'))}\n      <div style={{maxWidth:300,margin:'0 auto 8px'}}>",
    "    return (<div style={root}>\n      {prompt(t('Read the note with its sign. Tap its key.', '기호가 붙은 음을 읽어요. 그 건반을 눌러요.'))}\n      <div style={{maxWidth:300,margin:'0 auto 8px',order:2}}>")
rep("      <TapKeyboard octaves={2} labels=\"white\" marks={marks} pixel={pixel} onTap={locked ? null : (i) => onAnswer(i)}/>\n    </div>);\n  }",
    "      {pic(<TapKeyboard octaves={2} labels=\"white\" marks={marks} pixel={pixel} onTap={locked ? null : (i) => onAnswer(i)}/>)}\n    </div>);\n  }")
rep("  return (<div>\n    {prompt(t('Tap the key ' + what + ' from ' + tnName(q.a)", "  return (<div style={root}>\n    {prompt(t('Tap the key ' + what + ' from ' + tnName(q.a)")
rep("    <TapKeyboard octaves={2} labels=\"white\" marks={marks} pixel={pixel} onTap={locked ? null : (i) => onAnswer(i)}/>\n  </div>);\n}\nObject.assign(TONES_DRILL",
    "    {pic(<TapKeyboard octaves={2} labels=\"white\" marks={marks} pixel={pixel} onTap={locked ? null : (i) => onAnswer(i)}/>)}\n  </div>);\n}\nObject.assign(TONES_DRILL")

rep("function SacQuestion({ q, given, locked, onAnswer, pixel }) {", "function SacQuestion({ q, given, locked, onAnswer, pixel, fbAbove }) {")
rep("  const grid = (cols, render, pad = '12px 2px') => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8}}>",
    "  const grid = (cols, render, pad = '12px 2px') => <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,order:3}}>")
rep("  const paper = (node, mw = 400) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '4px 0',margin:'0 auto 10px',maxWidth:mw}}>{node}</div>;\n  const staff = (items, o = {}, clef = 'treble', mw = 400) => paper(<SacStaff",
    "  const paper = (node, mw = 400) => <div style={{background:'#fff',borderRadius:pixel ? 0 : 8,padding:pixel ? 4 : '4px 0',margin:'0 auto 10px',maxWidth:mw,order:2}}>{node}</div>;\n  const staff = (items, o = {}, clef = 'treble', mw = 400) => paper(<SacStaff")
rep("    <div style={{display:'flex',flexDirection:'column',gap:4,margin:'0 0 8px'}}>{['a', 'b'].map(", "    <div style={{display:'flex',flexDirection:'column',gap:4,margin:'0 0 8px',order:2}}>{['a', 'b'].map(")
rep("    <div style={{textAlign:'center',margin:'0 0 10px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={() => sacPlayItems(q.items)}", "    <div style={{textAlign:'center',margin:'0 0 10px',order:2}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} onClick={() => sacPlayItems(q.items)}")
rep("  return <div><BoardTrack b={board} pixel={pixel}/>{body}</div>;\n}\nfunction sacCheck", "  return <div style={fbAbove ? {display:'contents'} : undefined}><BoardTrack b={board} pixel={pixel}/>{body}</div>;\n}\nfunction sacCheck")

# ── 4. one drill for the whole concept, numbered like the lessons ──
rep("Object.assign(KEYSIG_DRILL, { feedbackAbove: true, levels: SKG_LEVELS, generate: genSkgQuestion, check: skgCheck, answerLabel: skgAnswerLabel, Question: SkgQuestionAll, Learn: SkgLearn });\n",
"""Object.assign(KEYSIG_DRILL, { feedbackAbove: true, levels: SKG_LEVELS, generate: genSkgQuestion, check: skgCheck, answerLabel: skgAnswerLabel, Question: SkgQuestionAll, Learn: SkgLearn });

// ─── Phase 543: Semitones and accidentals, one drill for the Home concept. Every level of the two older drills (Tones and semitones; Accidentals),
// numbered like the Home lessons, plus the coral-note and accidental questions that came out of the key signatures drill (More practice). ───
const CLK_TN = ['hw', 'find', 'wn', 'bname', 'enh', 'staff'], CLK_SKG = ['note', 'acc'];
const CLK_LEVELS = [
  { n: 21, label: 'Half step or whole step?', short: ['Half or whole?', '반음? 온음?'], num: '1', kind: 'hw', time: 7, noPrint: true },
  { n: 22, label: 'Play a half step, up or down', short: ['Play a half step', '반음 치기'], num: '1', kind: 'find', size: 1, time: 9, noPrint: true },
  { n: 23, label: 'Play a whole step, up or down', short: ['Play a whole step', '온음 치기'], num: '1', kind: 'find', size: 2, time: 9, noPrint: true },
  { n: 24, label: 'White neighbours: E F and B C', short: ['White neighbours', '흰건반 이웃'], num: '1', kind: 'wn', time: 7, noPrint: true },
  { n: 25, label: 'Name the sign', short: ['Name the sign', '임시표 이름'], num: '2', kind: 'sign', time: 7, noPrint: true },
  { n: 26, label: 'Name the black keys', short: ['Black key names', '검은건반 이름'], num: '3', kind: 'bname', time: 7, noPrint: true },
  { n: 27, label: 'Find the key', short: ['Find the key', '건반 찾기'], num: '4', kind: 'key', time: 9, noPrint: true },
  { n: 28, label: 'Sharps and flats on the staff', short: ['On the staff', '오선 위 음'], num: '4', kind: 'staff', time: 10, noPrint: true },
  { n: 29, label: 'The natural', short: ['The natural', '내추럴'], num: '5', kind: 'nat', time: 10, noPrint: true },
  { n: 30, label: 'Which sign?', short: ['Which sign?', '어떤 임시표?'], num: '6', kind: 'write', time: 12, noPrint: true },
  { n: 31, label: 'One key, two names', short: ['Two names', '이름 둘'], num: '7', kind: 'enh', time: 8, noPrint: true },
  { n: 32, label: 'Until the bar line', short: ['Until the bar line', '세로줄까지'], num: '9', kind: 'bar', time: 10, noPrint: true },
  { n: 33, label: 'Its own line or space', short: ['Its own line or space', '같은 줄이나 칸'], num: '10', kind: 'line', time: 10, noPrint: true },
  { n: 34, label: 'Read the bar', short: ['Read the bar', '마디 읽기'], num: '11', kind: 'read', time: 15, noPrint: true },
  { n: 35, label: 'Listen: which bar?', short: ['Listen', '듣기'], extra: true, extraStart: true, kind: 'ear', time: 14, noPrint: true },
  { n: 36, label: 'Extra: the bass clef', short: ['Bass clef', '낮은음자리표'], extra: true, kind: 'bass', time: 10, noPrint: true },
  { n: 37, label: 'Coral note in a key signature', short: ['Coral note', '산호색 음'], extra: true, kind: 'note', time: 12, noPrint: true },
  { n: 38, label: 'Accidental in a key signature', short: ['Accidentals in a key', '조표 안의 임시표'], extra: true, kind: 'acc', time: 14, noPrint: true },
];
Object.assign(LEVEL_KO, { 'Coral note in a key signature': '조표 안의 산호색 음', 'Accidental in a key signature': '조표 안의 임시표' });
const clkWho = (q) => CLK_TN.includes(q.kind) ? 'tn' : CLK_SKG.includes(q.kind) ? 'skg' : 'sac';
const CLOCK_DRILL = {
  id: 'clock', label: 'Semitones and accidentals', feedbackAbove: true, levels: CLK_LEVELS,
  generate: (lv, prev) => CLK_TN.includes(lv.kind) ? genTnQuestion(lv, prev) : CLK_SKG.includes(lv.kind) ? genSkgQuestion(lv, prev) : genSacQuestion(lv, prev),
  check: (q, ans) => { const w = clkWho(q); return w === 'tn' ? TONES_DRILL.check(q, ans) : w === 'skg' ? skgCheck(q, ans) : sacCheck(q, ans); },
  answerLabel: (q) => { const w = clkWho(q); return w === 'tn' ? TONES_DRILL.answerLabel(q) : w === 'skg' ? skgAnswerLabel(q) : sacAnswerLabel(q); },
  Question: (p) => { const w = p.q ? clkWho(p.q) : 'sac'; return w === 'tn' ? <TnQuestion {...p}/> : w === 'skg' ? <SkgQuestionAll {...p}/> : <SacQuestion {...p}/>; },
  Learn: SacLearn,
};
DRILLS.push({ id: 'clock', label: 'Semitones and accidentals', concept: CLOCK_DRILL, track: 'pitch' });
""")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
