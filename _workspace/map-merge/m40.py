p='drills.src.html'; s=open(p).read()
if "id: 'scales-1'" in s: print('already'); raise SystemExit
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:100])
    s=s.replace(old,new)

# --- the drill object and its place in the house
rep("const SCALE_PLAY_DRILL = { id: 'scale-play', label: 'Playing Scales' };",
    "const SCALE_PLAY_DRILL = { id: 'scale-play', label: 'Playing Scales' };\nconst SCALES_1_DRILL = { id: 'scales-1', label: 'Scales, Grade 1' };   // m40: Level 1's scales (two octaves, contrary motion G and E minor, chromatic from G)")
rep("  { id: 'scale-play', label: 'Playing Scales', concept: SCALE_PLAY_DRILL, track: 'start' },   // Build AB",
    "  { id: 'scale-play', label: 'Playing Scales', concept: SCALE_PLAY_DRILL, track: 'start' },   // Build AB\n  { id: 'scales-1', label: 'Scales, Grade 1', concept: SCALES_1_DRILL, track: 'start' },   // m40")
rep("{ ids: ['listen-write', 'accidentals', 'key-signatures', 'terms', 'six-eight', 'intervals', 'chords', 'form'],",
    "{ ids: ['listen-write', 'scales-1', 'accidentals', 'key-signatures', 'terms', 'six-eight', 'intervals', 'chords', 'form'],")
rep("'scales-23': ['Scales 2', '스케일 2'],", "'scales-1': ['Scales 1', '스케일 1'], 'scales-23': ['Scales 2', '스케일 2'],")
rep('  "scales-23": ["Black-key starts, chromatic", "검은건반 시작, 반음계"],',
    '  "scales-1": ["Two octaves, mirror twins, chromatic", "두 옥타브, 거울 쌍둥이, 반음계"],\n  "scales-23": ["Black-key starts, chromatic", "검은건반 시작, 반음계"],')
rep("  'scales-23': 'scales grade 2 black key start",
    "  'scales-1': 'scales grade 1 level 1 two octaves hands together g major f major e minor d minor natural harmonic contrary motion mirror twins chromatic scale from g',\n  'scales-23': 'scales grade 2 black key start")
rep("const LESSON_SF_ROOMS = ['scales', 'scale-play', 'minor-scales', 'scales-23',", "const LESSON_SF_ROOMS = ['scales', 'scale-play', 'minor-scales', 'scales-1', 'scales-23',")
rep("  const SF_ROOMS = ['scales', 'scale-play', 'minor-scales', 'scales-23',", "  const SF_ROOMS = ['scales', 'scale-play', 'minor-scales', 'scales-1', 'scales-23',")
rep("'scale-play': 'k-play', 'scales-23': 'k-play',", "'scale-play': 'k-play', 'scales-1': 'k-play', 'scales-23': 'k-play',")

# --- contrary motion in G and E minor; chromatic from G
rep("const SP_CM = { C: { s: 0, steps: SP_MAJ, nm: SP_SC.C.nm, en: 'C major, from middle C', ko: '가운데 도에서 C장조' },",
    "const SP_CM = { G: { s: -5, steps: SP_MAJ, nm: SP_SC.G.nm, en: 'G major, from the G below middle C', ko: '가운데 도 아래 G에서 G장조' }, Emh: { s: -8, steps: SP_HAR, nm: SP_SC.Emh.nm, en: 'E harmonic minor, from the E below middle C', ko: '가운데 도 아래 E에서 E 화성 단음계' },   // m40\n  C: { s: 0, steps: SP_MAJ, nm: SP_SC.C.nm, en: 'C major, from middle C', ko: '가운데 도에서 C장조' },")
rep("const SCF_CHROM = [['D', 2, 2], ['A', -3, 3], ['E♭', 3, 3]];", "const SCF_CHROM = [['D', 2, 2], ['A', -3, 3], ['E♭', 3, 3], ['G', -5, 1]];   // m40: G for Level 1 (the drills of scales-23 pick from the first three)")
rep("function SpMirrorPad({ onResult }) {\n  const T = useSpTimers();\n  const [k, setK] = useState('C'),",
    "function SpMirrorPad({ onResult, keys }) {   // m40: keys, the scales on offer\n  const T = useSpTimers(), KS = keys || [['C', t('C major', 'C장조')], ['Amh', t('A harmonic minor', 'A 화성 단음계')]];\n  const [k, setK] = useState(KS[0][0]),")
rep("      {spChips([['C', t('C major', 'C장조')], ['Amh', t('A harmonic minor', 'A 화성 단음계')]], k, (x) => reset(() => setK(x)))}",
    "      {spChips(KS, k, (x) => reset(() => setK(x)))}")

# --- the levels: two new ones, and scale-play keeps the one-octave ones
rep("  { n: 6, label: 'Listen: natural or harmonic?', kind: 'earNH', time: 16, noPrint: true },\n];",
    "  { n: 6, label: 'Listen: natural or harmonic?', kind: 'earNH', time: 16, noPrint: true },\n  { n: 7, label: 'Mirror twins: G major and E minor', kind: 'mirror2', time: 12 },   // m40: Level 1\n  { n: 8, label: 'Chromatic from G: which finger?', kind: 'chromG', time: 12 },\n];")
rep("Object.assign(LEVEL_KO, { 'Which finger? One octave': '몇 번 손가락? 한 옥타브',",
    "Object.assign(LEVEL_KO, { 'Mirror twins: G major and E minor': '거울 쌍둥이: G장조와 E단조', 'Chromatic from G: which finger?': 'G에서 반음계: 몇 번 손가락?', 'Which finger? One octave': '몇 번 손가락? 한 옥타브',")
rep("  if (kind === 'mirror') { let k, j, g = 0; do { k = Math.random() < 0.6 ? 'C' : 'Amh';",
    "  if (kind === 'chromG') { let h, j, g = 0; do { h = Math.random() < 0.5 ? 'R' : 'L'; j = 1 + Math.floor(Math.random() * 11); } while (prev && prev.key === 'g' + h + j && g++ < 10);   // m40\n    const i = SCF_CHROM[3][1] + j; return { kind: 'chrom', st: 3, h, j, i, answer: scfChF(i, h, false), choices: [1, 2, 3], key: 'g' + h + j, uid }; }\n"
    "  if (kind === 'mirror' || kind === 'mirror2') { let k, j, g = 0; do { k = kind === 'mirror2' ? (Math.random() < 0.5 ? 'G' : 'Emh') : Math.random() < 0.6 ? 'C' : 'Amh';")
rep("    return { kind, k, j, answer: ans, choices: shuffle([ans].concat(shuffle(pool).slice(0, 3))), key: k + j, uid }; }\n  if (kind === 'f2')",
    "    return { kind: 'mirror', k, j, answer: ans, choices: shuffle([ans].concat(shuffle(pool).slice(0, 3))), key: k + j, uid }; }\n  if (kind === 'f2')")
rep("function spAnswerLabel(q) {\n  if (q.kind === 'f1' || q.kind === 'f2')", "function spAnswerLabel(q) {\n  if (q.kind === 'f1' || q.kind === 'f2' || q.kind === 'chrom')")
rep("function SpQuestion({ q, given, locked, onAnswer, pixel }) {\n  const T = useSpTimers(),",
    "function SpQuestion(props) { return props.q.kind === 'chrom' ? <ScfQuestion {...props}/> : <SpQuestion0 {...props}/>; }   // m40: the chromatic question is the Scales rooms' own\nfunction SpQuestion0({ q, given, locked, onAnswer, pixel }) {\n  const T = useSpTimers(),")
rep("Object.assign(SCALE_PLAY_DRILL, { levels: SP_LEVELS, generate: genSpQuestion,",
    "Object.assign(SCALE_PLAY_DRILL, { allLevels: SP_LEVELS, levels: SP_LEVELS.filter(l => [1, 2, 3, 5, 6].includes(l.n)), generate: genSpQuestion,")
rep("Question: SpQuestion, Learn: SpLearn });\n", "Question: SpQuestion, Learn: SpLearn });\nsplitDrill(SCALES_1_DRILL, SCALE_PLAY_DRILL, [4, 7, 8], (p) => <SpLearn part=\"1\" {...p}/>);   // m40\n", 1)

# --- the Lesson Book: scale-play keeps steps 1-4; scales-1 gets two octaves, the G/E-minor mirror, chromatic from G
rep("function spLbPages(scr = false) {\n  const ch = 'scale-play', sc = bkChapterNo('scales');",
    "function spLbPages(scr = false, part) {   // m40: part '1', the Level 1 room's pages\n  const ch = part === '1' ? 'scales-1' : 'scale-play', sc = bkChapterNo('scales');")
# keep the old array, then pick
i = s.index("function spLbPages(scr = false, part) {")
j = s.index("  return [\n    // 1. opener", i)
s = s[:j] + "  const ALL = [\n    // 1. opener" + s[j + len("  return [\n    // 1. opener"):]
k = s.index("    </LbPage>,\n  ];\n}\nfunction ScalePlayLessonBook()", j)
end = k + len("    </LbPage>,\n  ];\n")
tail = r'''  if (part !== '1') return [ALL[0], ALL[1], ALL[2], ALL[3], ALL[4], React.cloneElement(ALL[6], { no: 6, kicker: t('Check-up', '점검') }, ...[].concat(ALL[6].props.children).map(c => c && c.props && c.props.live ? React.cloneElement(c, { still: <LbStageRows big rows={checks5.slice(0, 4).map(([a, txt]) => [pen(a), txt])}/>, live: <FiveChecks376 rows={checks5.slice(0, 4)} storeKey="pb_sp_five"/> }) : c))];
  // Level 1 (m40): the opener, two octaves (the old step 5), the mirror in G and E minor, chromatic from G, the checks
  const cG = spCm('G'), s1checks = [checks5[4], [spPicMirror(), t('I play contrary motion from G and from E: mirror twins, two octaves', 'G와 E에서 반대 방향으로: 거울 쌍둥이, 두 옥타브')], [scfPicChrom(), t('I play the chromatic scale from G: 3 on black, 1 on white, 2 where two white keys sit together', 'G에서 반음계: 검은건반 3, 흰건반 1, 흰건반 둘이 붙은 곳은 2')]];
  const s1toc = [[t('Two octaves, hands together', '두 옥타브, 양손 함께'), 2], [t('Mirror twins in G and E minor', 'G장조와 E단조의 거울 쌍둥이'), 3], [t('Chromatic from G', 'G에서 반음계'), 4], [t('My checks', '나의 확인'), 5]];
  return [
    <LbPage key="1" no={1} chId={ch} teacher={<>{spTx(t('Level 1 scales, as on the Grade 1 technical list: G and F major, E and D minor (natural and harmonic), two octaves, hands separately and together, two notes a beat at ♩ = 76; contrary motion over two octaves in C major, A harmonic minor, G major and E harmonic minor at ♩ = 66; the chromatic scale from G, one octave, hands separately. Chapter ' + bkChapterNo('scale-play') + ' (Level ½) has the one-octave scales and C and A minor contrary motion. From memory, mf, legato.', 'Level 1 스케일, Grade 1 테크닉 목록과 같아요: G장조와 F장조, E단조와 D단조(자연·화성), 두 옥타브, 한 손씩 그리고 양손 함께, ♩ = 76에 한 박에 두 음; 두 옥타브 반진행 C장조, A 화성 단음계, G장조, E 화성 단음계 ♩ = 66; G에서 반음계 한 옥타브, 한 손씩. 챕터 ' + bkChapterNo('scale-play') + '(Level ½)에 한 옥타브 스케일과 C·A단조 반진행이 있어요. 외워서, mf, 레가토.'))}</>}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:50,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{t('Scales, Level 1', '스케일, Level 1')}</div>
      </div></LbOnly>
      <LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}><SpStrip k="G" found={spThumbs('G')} mw={640}/></div></LbPic>
      <LbSay size={18}>{t('Two octaves with both hands, mirror twins in new keys, and every key in a row: the chromatic scale.', '양손으로 두 옥타브, 새 조의 거울 쌍둥이, 그리고 모든 건반을 차례로: 반음계.')}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {s1toc.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h lb-can-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('After this chapter, I can', '이 챕터를 마치면')}</div>
          {[t('play G and F major, E and D minor, two octaves, hands together', 'G장조, F장조, E단조, D단조를 두 옥타브 양손 함께 칠 수 있어요'), t('play contrary motion from G and from E', 'G와 E에서 반대 방향으로 칠 수 있어요'), t('play the chromatic scale from G', 'G에서 반음계를 칠 수 있어요')].map(x => <div key={x} style={{display:'flex',gap:9,alignItems:'flex-start',fontSize:14.5,padding:'5px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,
    React.cloneElement(ALL[5], { key: '2', no: 2, kicker: t('Step 1', '1단계') }),
    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Mirror twins in G and E minor', 'G장조와 E단조의 거울 쌍둥이')}
      teacher={<>{spTx(t('Contrary motion, two octaves, ♩ = 66: G major from the G below middle C, E harmonic minor from the E below middle C. The fingers match all the way, as in C major: 1 2 3, 1 2 3 4 5. In E harmonic minor the right hand\'s 4 plays D♯ above and the left hand\'s 4 plays F♯ below; check the raised 7th (D♯) in both hands.', '두 옥타브 반진행 ♩ = 66: 가운데 도 아래 G에서 G장조, 가운데 도 아래 E에서 E 화성 단음계. C장조처럼 손가락이 끝까지 같아요: 1 2 3, 1 2 3 4 5. E 화성 단음계에서 올린 7음(D♯)을 두 손 모두 확인해요.'))}</>}>
      <LbLive still={<LbPic h={190}><div style={{width:'100%',maxWidth:600,margin:'0 auto'}}><SpKb lo={cG.L[7]} hi={cG.R[7]} W={30} H={74} lit={Object.fromEntries(cG.R.concat(cG.L).map(x => [x, 'pale']))} names={Object.assign(spNameMap(cG.R, cG.nmR), spNameMap(cG.L, cG.nmL))} up={spFingMap(cG.R, SP_CM_F)} dn={spFingMap(cG.L, SP_CM_F)}/>
        <div style={{display:'flex',justifyContent:'space-between',fontSize:12.5,fontWeight:900,color:BK.muted,margin:'2px 4px 0'}}><span>{t('← left hand: down', '← 왼손: 아래로')}</span><span>{t('right hand: up →', '오른손: 위로 →')}</span></div></div></LbPic>} live={<SpMirrorPad keys={[['G', t('G major', 'G장조')], ['Emh', t('E harmonic minor', 'E 화성 단음계')]]}/>}/>
      <LbSay>{t('The same mirror as in C, from a new note. Both thumbs on the G below middle C: one hand up, one hand down, the same number every time. Then from E, with D♯ in both hands.', 'C에서 하던 거울을 새 음에서. 두 엄지를 가운데 도 아래 G에: 한 손은 위로, 한 손은 아래로, 언제나 같은 번호. 그다음 E에서, 두 손 모두 D♯.')}</LbSay>
      <LbPiano steps={[t('G major, one octave, slowly, saying the numbers: 1 2 3, thumb, 1 2 3 4 5.', 'G장조 한 옥타브, 천천히, 번호를 말하며: 1 2 3, 엄지, 1 2 3 4 5.'), t('Then two octaves: the thumbs turn together twice on the way out.', '그다음 두 옥타브: 나갈 때 엄지가 두 번 함께 넘어가요.'), t('E harmonic minor the same way: find both D♯s before you start.', 'E 화성 단음계도 같은 방법으로: 시작 전에 두 D♯을 찾아요.')]}/>
      <LbRemember>{t('A new note, the same mirror.', '새 음, 같은 거울.')}</LbRemember>
    </LbPage>,
    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Chromatic from G', 'G에서 반음계')}
      teacher={<>{spTx(t('Grade 1: the chromatic scale from G, one octave, hands separately. Every key in order, black and white. Fingering: 3 on every black key, 1 on the white keys, 2 where two white keys sit together (B C and E F) in the right hand going up and the left hand coming down.', 'Grade 1: G에서 반음계 한 옥타브, 한 손씩. 검은건반과 흰건반을 차례로. 손가락: 검은건반은 언제나 3, 흰건반은 1, 흰건반 둘이 붙은 곳(B C, E F)은 2.'))}</>}>
      <LbLive still={<LbPic h={150}><div style={{width:'100%',maxWidth:560,margin:'0 auto'}}><SpKb lo={-5} hi={7} W={36} H={92} lit={Object.fromEntries(Array.from({ length: 13 }, (_, j) => [j - 5, spIsW(j - 5) ? 'pale' : 'cor']))} up={Object.fromEntries(Array.from({ length: 13 }, (_, j) => [j - 5, scfChF(j - 5, 'R', j === 0 || j === 12)]))} names={{ [-5]: 'G', 7: 'G' }}/></div></LbPic>} live={<ScfChromPad fixed={{ st: 3, h: 'R' }}/>}/>
      <LbSay>{t('Every key, one after another: twelve half steps to the next G. Black keys always 3. White keys 1, but 2 where two white keys sit together.', '모든 건반을 하나씩: 다음 G까지 반음 열두 개. 검은건반은 언제나 3. 흰건반은 1, 흰건반 둘이 붙은 곳은 2.')}</LbSay>
      <LbRemember>{t('Black 3, white 1, two whites together: 2.', '검은건반 3, 흰건반 1, 흰건반 둘이 붙으면 2.')}</LbRemember>
    </LbPage>,
    <LbPage key="5" no={5} chId={ch} kicker={t('Check-up', '점검')} title={t('My checks', '나의 확인')} teacher={<>{t('Each one played to you, from memory.', '하나씩 외워서 선생님에게 들려줘요.')}</>}>
      <LbSay>{t('At the piano, tick each one: not yet, nearly, or got it!', '피아노 앞에서 하나씩 표시해요: 아직, 거의, 됐어요!')}</LbSay>
      <LbLive still={<LbStageRows big rows={s1checks.map(([a, txt]) => [pen(a), txt])}/>} live={<FiveChecks376 rows={s1checks} storeKey="pb_s1_checks"/>}/>
    </LbPage>,
  ];
'''
s = s[:end] + tail + s[end:]
rep("function SpLearn({ onStart }) {\n  const pages = spLbPages(true), opener = pages[0];\n  return (\n    <Lesson id=\"scale-play\" title={t('Playing scales', '스케일 치기')} onStart={onStart} noArt\n      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value=\"scale-play\">",
    "function SpLearn({ onStart, part }) {\n  const pages = spLbPages(true, part), opener = pages[0], cid = part === '1' ? 'scales-1' : 'scale-play';\n  return (\n    <Lesson id={cid} title={part === '1' ? t('Scales, Level 1', '스케일, Level 1') : t('Playing scales', '스케일 치기')} onStart={onStart} noArt\n      head={<LbScreenCtx.Provider value={true}><BkChapterCtx.Provider value={cid}>")
rep("function ScalePlayLessonBook() { return <>{spLbPages(false)}</>; }",
    "function ScalePlayLessonBook() { return <>{spLbPages(false)}</>; }\nfunction Scales1LessonBook() { return <>{spLbPages(false, '1')}</>; }   // m40")

# --- the Reference: Level 1 plays F major, D minor; the Scales map has a Level 1 row
rep("const REF_SCALE_PLAY = { D: 'scales-23', 'B♭': 'scales-23' };",
    "const REF_SCALE_PLAY = { F: 'scales-1', D: 'scales-23', 'B♭': 'scales-23', B: 'scales-5', 'D♭': 'scales-5', 'F♯': 'scales-6', 'G♭': 'scales-6' };   // m40: where each scale is played; G♭ = F♯")
rep("    { id: 'scales-23', floor: lvlName('Grade 2'), rows:",
    "    { id: 'scales-1', floor: lvlName('Grade 1'), rows: [[F.sim, ['G major', 'F major', 'E minor', 'D minor'].map(nm), t('two octaves, hands together, two notes a beat', '두 옥타브, 양손 함께, 한 박에 두 음')], [F.cm, ['C major', 'A harmonic minor', 'G major', 'E harmonic minor'].map(nm), '♩ = 66'], [F.chr, ['G'], t('one octave', '한 옥타브')]] },   // m40\n    { id: 'scales-23', floor: lvlName('Grade 2'), rows:")
open(p,'w').write(s); print('ok')
