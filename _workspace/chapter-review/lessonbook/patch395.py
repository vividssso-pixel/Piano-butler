# Phase 395 (Sohyun 2026-10-09): (1) the five checks are not tied to lessons any more -- each one is ticked as it goes:
# not yet, nearly, got it! (books and app); (2) "The seven letter names" leaves chapter 2 for chapter 3, where the
# letters are introduced properly as A B C D E F G: chapter 2 shows the keyboard by its pattern only (houses, the white
# keys of each house, the whole piano and middle C, play). Chapter 2 is now 6 pages; its drill's 3rd level asks
# "Whose house is this white key?" instead of the key's name.
# Run from the repo root: python3 _workspace/chapter-review/lessonbook/patch395.py
p = 'drills.src.html'
s = open(p, encoding='utf-8').read()
done = []
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    assert c == n, f"{what}: expected {n}, got {c}"
    s = s.replace(a, b); done.append(what)

# ── (1) not yet / nearly / got it! ──
a = s.index("function FiveChecks376({ rows, storeKey }) {")
b = s.index("\n}\n", a) + 3
s = s[:a] + """// Phase 395 (Sohyun 2026-10-09): a check is not tied to lessons -- each one is ticked as it goes: not yet, nearly, got it!
const lbStages = () => [t('Not yet', '아직'), t('Nearly', '거의'), t('Got it!', '됐어요!')];
function LbStageIcon({ i, on }) {
  const c = on ? BK.coral : '#c9c3b2';
  if (i === 2) { const pts = Array.from({ length: 10 }, (_, k) => { const r = k % 2 ? 2.9 : 6.8, an = Math.PI / 5 * k - Math.PI / 2; return (8 + r * Math.cos(an)).toFixed(2) + ',' + (8.4 + r * Math.sin(an)).toFixed(2); }).join(' ');
    return <svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><polygon points={pts} fill={on ? BK.coral : 'none'} stroke={c} strokeWidth="1.6" strokeLinejoin="round"/></svg>; }
  return <svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" stroke={c} strokeWidth="1.8"/>{i === 1 && <path d="M8 2 A6 6 0 0 1 8 14 Z" fill={on ? BK.coral : '#ddd7c6'}/>}</svg>;
}
// the printed five checks: three boxes in each row
function LbStageRows({ rows }) {
  const S = lbStages(), cols = '96px 1fr repeat(3, 62px)';
  return <div style={{display:'flex',flexDirection:'column',gap:5}}>
    <div style={{display:'grid',gridTemplateColumns:cols,gap:7,alignItems:'end',fontSize:11,fontWeight:800,color:BK.muted,textAlign:'center'}}>
      <span style={{gridColumn:'1 / 3',textAlign:'left',fontFamily:LB_SERIF,fontSize:18,color:BK.ink,whiteSpace:'nowrap'}}>{t('At the piano', '피아노 앞에서')}</span>
      {S.map((l, i) => <span key={i} style={i === 2 ? {color:BK.coral} : null}>{l}</span>)}
    </div>
    {rows.map(([pic, txt], i) => <div key={i} style={{display:'grid',gridTemplateColumns:cols,gap:7,alignItems:'center',border:'1px solid #ece6d8',borderRadius:10,padding:'3px 8px'}}>
      <div style={{display:'flex',justifyContent:'center'}}>{pic}</div>
      <div style={{fontSize:14,fontWeight:800,color:BK.ink}}>{txt}</div>
      {[0, 1, 2].map(k => <span key={k} style={{width:30,height:30,border:'1.5px solid ' + BK.line,borderRadius:15,justifySelf:'center',display:'flex',alignItems:'center',justifyContent:'center'}}><LbStageIcon i={k}/></span>)}
    </div>)}
    <div style={{fontSize:11.5,color:BK.muted}}>{t('Tick a box each time it gets better: not yet, then nearly, then got it!', '좋아질 때마다 한 칸씩 표시해요: 아직, 거의, 그리고 됐어요!')}</div>
  </div>;
}
// the app's five checks: tap how each one is going
function FiveChecks376({ rows, storeKey }) {
  const SK = (storeKey || FIVE_KEY) + ':stage';
  const [st, setSt] = useState(() => { try { return JSON.parse(localStorage.getItem(SK)) || {}; } catch (e) { return {}; } });
  const set = (r, k) => { const nx = { ...st }; if (nx[r] === k) delete nx[r]; else nx[r] = k; setSt(nx); try { localStorage.setItem(SK, JSON.stringify(nx)); } catch (e) {} };
  const S = lbStages(), got = rows.filter((_, r) => st[r] === 2).length;
  return (
    <div data-five-checks style={{display:'flex',flexDirection:'column',gap:7}}>
      {rows.map(([a, txt], r) => (
        <div key={r} style={{border:'1px solid #ece6d8',borderRadius:12,padding:'6px 8px 8px',display:'flex',flexWrap:'wrap',alignItems:'center',gap:'6px 10px'}}>
          <div style={{flex:'1 1 200px',display:'flex',alignItems:'center',gap:10,minWidth:0}}>
            <div style={{flex:'0 0 64px',display:'flex',justifyContent:'center'}}>{typeof a === 'string' ? <PbArt name={a} h={a === 'chk-hand' ? 38 : 52}/> : <PenArt shapes={a.shapes} vb={a.vb} style={{width:64}}/>}</div>
            <div style={{fontSize:14,fontWeight:800,color:BK.ink,lineHeight:1.3}}>{txt}</div>
          </div>
          <div style={{flex:'0 0 auto',display:'flex',gap:4,marginLeft:'auto'}}>{[0, 1, 2].map(k => { const on = st[r] === k; return (
            <button key={k} onClick={() => set(r, k)} aria-pressed={on} aria-label={txt + ': ' + S[k]}
              style={{height:34,border:'1.5px solid ' + (on ? BK.coral : BK.line),borderRadius:17,background:on ? '#fdeee8' : '#fff',display:'flex',alignItems:'center',gap:4,padding:'0 9px',fontSize:11.5,fontWeight:800,color:on ? BK.coral : BK.muted,cursor:'pointer'}}>
              <LbStageIcon i={k} on={on}/>{S[k]}</button>); })}</div>
        </div>))}
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:12.5,color:BK.muted}}>
        <span>{t(got + ' of ' + rows.length + ': got it!', rows.length + '개 중 ' + got + '개: 됐어요!')}</span>
        {Object.keys(st).length > 0 && <button className="ghost-btn" style={{fontSize:12,padding:'3px 10px'}} onClick={() => { setSt({}); try { localStorage.removeItem(SK); } catch (e) {} }}>{t('Start again', '처음부터')}</button>}
      </div>
    </div>
  );
}
""" + s[b:]
done.append('FiveChecks376 + LbStageRows')
# chapter 2's printed checks
a = s.index("      <LbLive still={<div style={{display:'flex',flexDirection:'column',gap:5}}>\n        <div style={{display:'grid',gridTemplateColumns:'96px 1fr repeat(6, 28px)'")
b = s.index("live={<FiveChecks376 storeKey=\"pb_five_fs_v1\"", a)
s = s[:a] + "      <LbLive still={<LbStageRows rows={checksRows.map(([a, vb, txt]) => [<PenArt shapes={chkArts[a]} vb={vb} style={{width:80}}/>, txt])}/>} " + s[b:]
done.append('ch2 printed checks')
# chapter 1's printed checks
a = s.index("      <LbLive still={\n      <div style={{display:'flex',flexDirection:'column',gap:5}}>")
b = s.index("live={<FiveChecks376 rows={checks5}/>}/>", a)
s = s[:a] + "      <LbLive still={<LbStageRows rows={checks5.map(([a, txt]) => [<PbArt name={a} h={a === 'chk-hand' ? 40 : 52}/>, txt])}/>} " + s[b:]
done.append('ch1 printed checks')
rep("""{t('At the piano: before you play, every time -- give yourself a star for each check in each lesson. On paper: do the check-up below.', '피아노 앞에서: 칠 때마다, 치기 전에 먼저 -- 레슨마다 확인 하나에 별 하나씩. 종이에서: 아래 점검을 풀어요.')}""",
    """{t('At the piano: before you play, every time -- tick how each one is going: not yet, nearly, or got it! On paper: do the check-up below.', '피아노 앞에서: 칠 때마다, 치기 전에 먼저 -- 하나씩 어떤지 표시해요: 아직, 거의, 됐어요! 종이에서: 아래 점검을 풀어요.')}""", 'ch1 checks words')
rep("""{t('At the piano: show each one and give yourself a star. On paper: do the check-up below. All done? Colour in the badge!', '피아노 앞에서: 하나씩 보여 주고 별을 칠해요. 종이에서: 아래 점검을 풀어요. 다 끝나면? 배지를 색칠해요!')}""",
    """{t('At the piano: show each one, then tick how it is going -- not yet, nearly, or got it! On paper: do the check-up below.', '피아노 앞에서: 하나씩 보여 주고 어떤지 표시해요 -- 아직, 거의, 됐어요! 종이에서: 아래 점검을 풀어요.')}""", 'ch2 checks words')
rep("""you only correct. All five easy? Do the Chapter check-up in the Workbook.', '1챕터의 다섯 가지 확인은 여전히 피아노 앞에서 늘 먼저예요. 이 다섯 가지는 이 챕터만의 확인이에요: 학생이 건반 위에서 직접 보여 주고, 선생님은 고쳐 주기만 해요. 다 쉬워지면 워크북의 챕터 점검을 해요.')}""",
    """you only correct. All five "got it"? Then the paper part on the same page.', '1챕터의 다섯 가지 확인은 여전히 피아노 앞에서 늘 먼저예요. 이 다섯 가지는 이 챕터만의 확인이에요: 학생이 건반 위에서 직접 보여 주고, 선생님은 고쳐 주기만 해요. 다섯 가지 다 "됐어요!"가 되면 같은 쪽의 종이 점검을 해요.')}""", 'ch2 checks teacher line')

# ── (2) chapter 2 without the letter names ──
a = s.index("    // 4. the seven letter names\n    <LbPage key=\"4\" no={4} chId={ch}")
b = s.index("    // 5. the whole piano & middle C", a)
s = s[:a] + "    // (the seven letter names moved to chapter 3, The Musical Alphabet -- Phase 395)\n\n" + s[b:]
done.append('ch2 LB p4 out')
rep("""    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The whole piano & middle C', '피아노 전체와 가운데 도')}""",
    """    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('The whole piano & middle C', '피아노 전체와 가운데 도')}""", 'ch2 middle C = p4')
rep("""    <LbPage key="6" no={6} chId={ch} kicker={t('Play', '연주')} title={t('Play on the patterns', '패턴 위에서 연주')}""",
    """    <LbPage key="5" no={5} chId={ch} kicker={t('Play', '연주')} title={t('Play on the patterns', '패턴 위에서 연주')}""", 'ch2 play = p5')
rep("""    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Chapter 1\\'s five checks""", """    <LbPage key="6" no={6} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}
      teacher={<>{t('Chapter 1\\'s five checks""", 'ch2 checks = p6')
rep("""[[t('Small house, big house', '작은 집, 큰 집'), 2], [t('The white keys of each house', '집마다 딸린 흰건반'), 3], [t('The seven letter names', '일곱 글자 음이름'), 4], [t('The whole piano & middle C', '피아노 전체와 가운데 도'), 5], [t('Play on the patterns', '패턴 위에서 연주'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]]""",
    """[[t('Small house, big house', '작은 집, 큰 집'), 2], [t('The white keys of each house', '집마다 딸린 흰건반'), 3], [t('The whole piano & middle C', '피아노 전체와 가운데 도'), 4], [t('Play on the patterns', '패턴 위에서 연주'), 5], [t('My five checks', '나의 다섯 가지 확인'), 6]]""", 'ch2 opener list')
rep("""t('name every white key, C to B', '모든 흰건반의 이름을 댈 수 있어요'), """, """t('hear high and low, and show the turtle\\'s end and the bird\\'s', '높은 소리와 낮은 소리를 듣고, 거북이 쪽과 새 쪽을 가리킬 수 있어요'), """, 'ch2 by the end')
rep("""Learn the pattern, and every key on the piano tells you its own name.', '피아노는 건반 88개처럼 보이지만, 사실은 작은 패턴 하나가 반복되는 거예요: 흰건반 3개를 거느린 검은건반 2개짜리 작은 집, 그리고 흰건반 4개를 거느린 3개짜리 큰 집. 이 패턴을 알면 피아노의 모든 건반이 자기 이름을 알려 줘요.')}""",
    """Learn the pattern, and you always know where you are on the piano -- in the next chapter, every key gets its name.', '피아노는 건반 88개처럼 보이지만, 사실은 작은 패턴 하나가 반복되는 거예요: 흰건반 3개를 거느린 검은건반 2개짜리 작은 집, 그리고 흰건반 4개를 거느린 3개짜리 큰 집. 이 패턴을 알면 피아노 어디에서든 길을 잃지 않아요 -- 다음 챕터에서는 건반마다 이름이 생겨요.')}""", 'ch2 opener words')
rep("""t('Pattern first, names second -- the same order at every age. Older beginners take this chapter in one sitting; younger ones live in the patterns for a while before the names stick. ', '어느 나이든 순서는 같아요: 패턴 먼저, 이름은 그다음. 나이가 있는 학습자는 이 챕터를 한 번에 지나가고, 어린 친구들은 패턴 속에서 한동안 지내다가 이름이 붙어요. ')""",
    """t('Pattern first, names second -- the same order at every age: this chapter is the pattern, the next one (The Musical Alphabet) gives every key its name. Older beginners take this chapter in one sitting; younger ones live in the patterns for a while. ', '어느 나이든 순서는 같아요: 패턴 먼저, 이름은 그다음 -- 이 챕터는 패턴이고, 다음 챕터(음악 알파벳)에서 건반마다 이름이 생겨요. 나이가 있는 학습자는 이 챕터를 한 번에 지나가고, 어린 친구들은 패턴 속에서 한동안 지내요. ')""", 'ch2 opener teacher')
# the five checks: high and low instead of naming keys
rep("""    letters: 'CDEFGAB'.split('').map((n, i) => ({ ...penText(8 + i * 12.6, 26, n, { size: 11, weight: 900, fill: n === 'C' || n === 'F' ? PEN_C : PEN_N, anchor: 'middle' }) })),""",
    """    highlow: [...fsTurtle(16, 26, 0.42), ...fsBird(76, 22, 0.62), { k: 'pa', seg: [['M', [30, 30]], ['L', [60, 30]]], f: 'none', s: PEN_C, w: 1.8, nw: true }, { k: 'pa', seg: [['M', [57, 27]], ['L', [62, 30]], ['L', [57, 33]], ['Z']], f: PEN_C }],""", 'check icon high/low')
rep("""    ['brace', [0, 0, 92, 40], t('I can say each house\\'s white keys: 3 and 4', '집마다 딸린 흰건반을 말할 수 있어요: 3개와 4개')],
    ['letters', [0, 0, 92, 40], t('I can name any white key (C at the small house\\'s left door)', '어떤 흰건반이든 이름을 댈 수 있어요 (C는 작은 집 왼쪽 문)')],""",
    """    ['highlow', [0, 0, 92, 40], t('I can hear high and low, and show the turtle\\'s end and the bird\\'s', '높고 낮은 소리를 듣고, 거북이 쪽과 새 쪽을 가리킬 수 있어요')],
    ['brace', [0, 0, 92, 40], t('I can say each house\\'s white keys: 3 and 4', '집마다 딸린 흰건반을 말할 수 있어요: 3개와 4개')],""", 'ch2 check rows')
# the paper part: high and low instead of naming keys
rep("""    {bkSec('B', 'Whose house is the dotted white key? Write S (small) or B (big).')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.wh.map((w, i) => <BkCell key={i} n={5 + i}>""",
    """    {bkSec('B', 'Put a star on the higher dot -- the one nearer the bird.')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.hl.map((pp, i) => <BkCell key={i} n={5 + i}><div style={{padding:'11px 6px 4px'}}><PaperKeys start="C" whites={10} w={22} h={44} dots={pp}/></div></BkCell>)}</BkGrid>
    {bkSec('C', 'Whose house is the dotted white key? Write S (small) or B (big).')}
    <BkGrid cols={4} gap="5px 10px">{W.chk.wh.map((w, i) => <BkCell key={i} n={9 + i}>""", 'paper B high/low')
a = s.index("    {bkSec('C', 'Name the dotted key. Write its letter.')}")
b = s.index("    {bkSec('D', 'Middle C: count the small houses from the bottom.')}", a)
s = s[:a] + s[b:]; done.append('paper: naming out')
rep("""    <TcBlock page={7} title="My five checks · the check-up on paper" answers={<>{tcAns('A', ['S B S B'])}{tcAns('B', W.chk.wh.map(w => fsHouse(w) + ' (' + fsLetter(w) + ')'))}{tcAns('C', W.chk.ln.map(fsLetter))}""",
    """    <TcBlock page={6} title="My five checks · the check-up on paper" answers={<>{tcAns('A', ['S B S B'])}{tcAns('B', W.chk.hl.map(hi))}{tcAns('C', W.chk.wh.map(w => fsHouse(w) + ' (' + fsLetter(w) + ')'))}""", 'tc ch2 checks answers')
rep("""This chapter's five checks are shown on the keyboard (find the houses, say 3 and 4, name any white key, find middle C, Hot Cross Buns legato); you only correct. The paper part follows the same order: score each part on its own (A, B, C, E: 4 marks, pass 3+; D: 2 marks). Not passed? Go back to that step's page: A p.2 · B p.3 · C p.4 · D p.5 · E p.6.""",
    """This chapter's five checks are shown on the keyboard (find the houses, high and low, say 3 and 4, find middle C, Hot Cross Buns legato); you only correct. The paper part follows the same order: score each part on its own (A, B, C, E: 4 marks, pass 3+; D: 2 marks). Not passed? Go back to that step's page: A and B p.2 · C p.3 · D p.4 · E p.5.""", 'tc ch2 checks scoring')
a = s.index("""    <TcBlock page={4} title="The seven letter names" answers=""")
b = s.index("  </>);\n  P(<>\n    <TcBlock page={5} title=\"The whole piano & middle C\"", a)
s = s[:a] + s[b:]; done.append('tc ch2 p4 out')
rep("""    <TcBlock page={5} title="The whole piano & middle C" answers=""", """    <TcBlock page={4} title="The whole piano & middle C" answers=""", 'tc ch2 middle C = p4')
rep("""    <TcBlock page={6} title="Play on the patterns" answers=""", """    <TcBlock page={5} title="Play on the patterns" answers=""", 'tc ch2 play = p5')
# the Workbook: the page facing the letter names goes (its tasks return in chapter 3)
a = s.index("""  // 4 (faces "The seven letter names")""")
b = s.index("""  // 5 (faces "The whole piano & middle C")""", a)
s = s[:a] + s[b:]; done.append('wb ch2 letters page out')
rep("""  // 5 (faces "The whole piano & middle C")
  P(<>
    <WbTop step={4}/>""", """  // 4 (faces "The whole piano & middle C")
  P(<>
    <WbTop step={3}/>""", 'wb middle C = step 3')
rep("""  // 6 (faces "Play on the patterns")
  P(<>
    <WbTop step={5}/>""", """  // 5 (faces "Play on the patterns")
  P(<>
    <WbTop step={4}/>""", 'wb play = step 4')
rep("""    { id: 'ln', name: 'The seven letter names', step: '3', page: '4' },
    { id: 'mc', name: 'Middle C', step: '4', page: '5', chk: false },
    { id: 'sg', name: 'Hot Cross Buns', step: '5', page: '6' },
    { id: 'lg', name: 'Legato', step: '5', page: '6' },
    { id: 'ck', name: 'My five checks', step: '6', page: '7', chk: false },""",
    """    { id: 'mc', name: 'Middle C', step: '3', page: '4', chk: false },
    { id: 'sg', name: 'Hot Cross Buns', step: '4', page: '5' },
    { id: 'lg', name: 'Legato', step: '4', page: '5' },
    { id: 'ck', name: 'My five checks', step: '5', page: '6', chk: false },""", 'fsConcepts')
rep("const FS_STORE = [1, 5, 6, 2, 3, 7];", "const FS_STORE = [1, 5, 2, 3, 7];   // Phase 395: the letter-names step left for chapter 3", 'FS_STORE')
# the drill: level 3 asks whose house a white key belongs to
rep("""  { n: 3, label: "What's this key's name?", kind: 'name', time: 7 },""", """  { n: 3, label: 'Whose house is this white key?', kind: 'whose', time: 6 },""", 'FS level 3')
rep("""  if (lv.kind === 'name') {
    const L7 = ['C', 'D', 'E', 'F', 'G', 'A', 'B'], PCS = [0, 2, 4, 5, 7, 9, 11];""", """  if (lv.kind === 'whose') {   // Phase 395: which house does this white key belong to?
    const PCS = [0, 2, 4, 5, 7, 9, 11]; let wi, g = 0;
    do { wi = Math.floor(Math.random() * 7); } while (prev && prev.key === 'w' + wi && g++ < 10);
    const o = Math.floor(Math.random() * 3), small = wi < 3;
    return { kind: 'whose', key: 'w' + wi, k: o * 12 + PCS[wi], small, answer: small ? 'Small house' : 'Big house', choices: ['Small house', 'Big house'], uid };
  }
  if (lv.kind === 'name') {
    const L7 = ['C', 'D', 'E', 'F', 'G', 'A', 'B'], PCS = [0, 2, 4, 5, 7, 9, 11];""", 'whose generator')
rep("""{ finger: '몇 번 손가락에 불이 켜졌나요?', name: '이 건반의 이름은 무엇일까요?',""", """{ finger: '몇 번 손가락에 불이 켜졌나요?', whose: '이 흰건반은 누구네 집일까요?', name: '이 건반의 이름은 무엇일까요?',""", 'whose title ko')
rep("""{ finger: 'Which finger number is lit?', name:""", """{ finger: 'Which finger number is lit?', whose: 'Whose house is this white key?', name:""", 'whose title en')
rep("""    {q.kind === 'name' && <div style={{marginBottom:12}}><TapKeyboard octaves={3} marks={{ [q.k]: 'target' }} tint pixel={pixel}/></div>}""",
    """    {q.kind === 'name' && <div style={{marginBottom:12}}><TapKeyboard octaves={3} marks={{ [q.k]: 'target' }} tint pixel={pixel}/></div>}
    {q.kind === 'whose' && <div style={{marginBottom:12}}><TapKeyboard octaves={3} marks={{ [q.k]: 'target' }} pixel={pixel}/></div>}""", 'whose keyboard')
# the toolbox: chapter 2's house tool shows the houses only (names come in chapter 3)
rep("""{ id: 'key-houses', ch: 'first-steps', title: 'Small house, big house (black keys)', blurb: 'The black-key map; where C and F live.', C: () => <><ExplFirstSteps1/><KeyHouses/></> },""",
    """{ id: 'key-houses', ch: 'first-steps', title: 'Small house, big house (black keys)', blurb: 'The black-key map: small houses and big houses, all the way up.', C: () => <><ExplFirstSteps1/><KeyHouses modes={['houses']}/></> },""", 'toolbox key-houses')
# the cover scene without letters (chapter 2 is the pattern)
rep("""function fsCoverShapes() {""", """function fsCoverShapes(opts = {}) {""", 'cover opts')
rep("""    letters.forEach((l, i) => out.push({ ...penText(x + (i + 0.5) * W, Y + H - 12, l, { size: 22, weight: 900, fill: i === 0 ? PEN_C : PEN_N, anchor: 'middle' }) }));""",
    """    if (opts.letters !== false) letters.forEach((l, i) => out.push({ ...penText(x + (i + 0.5) * W, Y + H - 12, l, { size: 22, weight: 900, fill: i === 0 ? PEN_C : PEN_N, anchor: 'middle' }) }));""", 'cover letters optional')
rep("""    return [...fsCoverShapes(), { k: 'raw', svg: rabbit }];""", """    return [...fsCoverShapes({ letters: false }), { k: 'raw', svg: rabbit }];""", 'ch2 scene without letters')
rep("""label="The rabbit butler stands on the ground between a small house of keys, C D E, and a big house, F G A B; the sea and a turtle at the low end, clouds and a bird at the high end\"""",
    """label="The rabbit butler stands on the ground between a small house of keys and a big house; the sea and a turtle at the low end, clouds and a bird at the high end\"""", 'scene label')

rep("<PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} h={50}/>", "<PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} h={46}/>", 'ch1 paper A a little smaller')

open(p, 'w', encoding='utf-8').write(s)
print('\n'.join('ok: ' + d for d in done))
print('PATCH 395 DONE')
