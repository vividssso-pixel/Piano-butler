// ── Phase 376: the online lesson opens like the Lesson Book (lb376.jsx), and its pictures move (pen376.js, sit376.jsx) ──
// 1. the pen engine and the new "Set up the stool" replace the old SitCheck (same name, so the Toolbox gets it too)
{
  const a = s.indexOf('function SitCheck() {'), b = s.indexOf('// ── 2. Hand shape: one finger on a key');
  if (a < 0 || b < a) throw new Error('376 SitCheck block');
  const pen = read('pen376.js').replace('__PEN_FIELD__', read('penfield.json').trim());
  s = s.slice(0, a) + pen + '\n' + read('sit376.jsx') + '\n' + read('warm376.jsx') + '\n' + read('hand376.jsx') + '\n\n' + s.slice(b);
}
// 2. the chapter's pages written once (postureLbPages), printed as the book and shown as the lesson
{
  const a = s.indexOf('function PostureLessonBook() {'), b = s.indexOf('const LESSON_BOOKS = {');
  if (a < 0 || b < a) throw new Error('376 PostureLessonBook block');
  s = s.slice(0, a) + read('lb376.jsx') + '\n' + s.slice(b);
}
// 3. the old 8-step lesson goes (the new PostureHandsLearn lives in lb376.jsx)
{
  const a = s.indexOf('function PostureHandsLearn({ onStart }) {'), b = s.indexOf('const POSTURE_LEVELS = [');
  if (a < 0 || b < a || s.indexOf('function PostureHandsLearn({ onStart }) {', a + 10) < 0) throw new Error('376 old PostureHandsLearn');
  s = s.slice(0, a) + s.slice(b);
}
// 4. the book's parts on screen: tick boxes that tick, pictures that fit the screen, words in both languages
repIn('LbPiano', `function LbPiano({ steps, title = 'At the piano' }) {`, `function LbPiano({ steps, title }) {`, '376 piano title');
repIn('LbPiano', `<span style={{fontFamily:LB_SERIF,fontSize:21,fontWeight:800,color:BK.ink}}>{title}</span>`, `<span style={{fontFamily:LB_SERIF,fontSize:21,fontWeight:800,color:BK.ink}}>{title || t('At the piano', '피아노 앞에서')}</span>`, '376 piano title 2');
repIn('LbPiano', `<span style={{flex:'0 0 auto',width:18,height:18,border:'1.6px solid ' + BK.ink,borderRadius:4,marginTop:3}}/>`, `<LbTick label={t('Done', '했어요') + ' ' + (i + 1)}/>`, '376 piano tick');
repIn('LbRemember', `>REMEMBER</span>`, `>{t('REMEMBER', '기억해요')}</span>`, '376 remember');
repIn('LbNot', `>Not like this</div>`, `>{t('Not like this', '이렇게는 안 돼요')}</div>`, '376 not');
repIn('LbPic', `minHeight:h,`, `minHeight:lbScreen() ? 0 : h,`, '376 pic');
repIn('LbFig', `style={{display:'grid',justifyItems:'center',gap:5,width:'min-content'}}`, `style={lbScreen() ? {display:'flex',flexDirection:'column',alignItems:'center',gap:5,maxWidth:'100%',minWidth:0} : {display:'grid',justifyItems:'center',gap:5,width:'min-content'}}`, '376 fig');
repIn('LbNot', `gridTemplateColumns:'repeat(' + items.length + ',1fr)'`, `gridTemplateColumns:'repeat(' + items.length + (lbScreen() ? ',minmax(0,1fr))' : ',1fr)')`, '376 not grid');
repIn('PbArt', `style={{display:'inline-block',lineHeight:0,width:w,height:h,flex:'0 0 auto',...style}}`,
  `style={lbScreen() ? {display:'inline-block',lineHeight:0,width:w,maxWidth:'100%',height:'auto',aspectRatio:w + ' / ' + h,flex:'0 1 auto',...style} : {display:'inline-block',lineHeight:0,width:w,height:h,flex:'0 0 auto',...style}}`, '376 art');
// 5. a lesson that opens with its book page has no staff-line drawing on top
repIn('Lesson', `function Lesson({ id, title, intro, children, onStart, startLabel, head }) {`, `function Lesson({ id, title, intro, children, onStart, startLabel, head, noArt }) {`, '376 lesson prop');
repIn('Lesson', `      <ChapterArt id={STAFF_ART[id] ? id : String(id).split('-')[0]}/>
      {head}`, `      {!noArt && <ChapterArt id={STAFF_ART[id] ? id : String(id).split('-')[0]}/>}
      {head}`, '376 lesson art');
// 6. finger walks inside the book page: the page already says what the box would say
repIn('FingerWalks', `function FingerWalks() {`, `function FingerWalks({ bare }) {`, '376 fw prop');
repIn('FingerWalks', `      <div style={actTitle}>{t('Play: finger walks', '연주: 손가락 걷기')}</div>
      <div style={actNote}>`, `      {!bare && <div style={actTitle}>{t('Play: finger walks', '연주: 손가락 걷기')}</div>}
      {!bare && <div style={actNote}>`, '376 fw bare');
repIn('FingerWalks', `<b>One circle is one steady beat.</b></>}</div>`, `<b>One circle is one steady beat.</b></>}</div>}`, '376 fw bare 2');
// 7. the Workbook follows: six lesson steps, one per Lesson Book page
repIn('PostureWorkbook', `concepts={C} steps={8} checkPage`, `concepts={C} steps={6} checkPage`, '376 wb steps');
repIn('PostureWorkbook', `<WbTop step="2-3"/>`, `<WbTop step={2}/>`, '376 wb top 2');
repIn('PostureWorkbook', `<WbTop step={4}/>`, `<WbTop step={3}/>`, '376 wb top 3');
repIn('PostureWorkbook', `<WbTop step="5-6" mins={10}/>`, `<WbTop step={4} mins={10}/>`, '376 wb top 4');
repIn('PostureWorkbook', `<WbTop step={7}/>`, `<WbTop step={5}/>`, '376 wb top 5');
repIn('phConcepts', `    { id: 'ar', name: 'The arm leads', step: '2-3', page: '3' },
    { id: 'hs', name: 'A round hand', step: '4', page: '4' },
    { id: 'lr', name: 'Left hand, right hand', step: '5-6', page: '5' },
    { id: 'fn', name: 'Finger numbers', step: '5-6', page: '5' },
    { id: 'fw', name: 'Finger walks', step: '7', page: '6' },`, `    { id: 'ar', name: 'The arm leads', step: '2', page: '3' },
    { id: 'hs', name: 'A round hand', step: '3', page: '4' },
    { id: 'lr', name: 'Left hand, right hand', step: '4', page: '5' },
    { id: 'fn', name: 'Finger numbers', step: '4', page: '5' },
    { id: 'fw', name: 'Finger walks', step: '5', page: '6' },
    { id: 'ck', name: 'My five checks', step: '6', page: '7', chk: false },`, '376 concepts');
// 8. the Toolbox's warm-ups are the book's moving cards too
rep(`C: () => <><ExplPostureHands2/><ArmExercises/></> },`, `C: () => <><ExplPostureHands2/><div className="try-box" style={actBox}><WarmUps376 cards={postureWarmCards()}/></div></> },`, '376 tool warm-ups');
// 9. the hand faults point to the warm-ups by their new numbers (Phase 371 reordered them; the book's order)
rep(`get fix() { return t('Knuckle bridge (exercise 2): tap each finger while the knuckles stay up.', '마디 다리(운동 2): 마디를 세운 채로 손가락을 하나씩 눌러요.'); }`,
  `get fix() { return t('Knuckle bridge (warm-up 5): press one key slowly and hold for 3 -- the knuckles stay up like a bridge.', '마디 다리(워밍업 5): 건반 하나를 천천히 누르고 셋을 세는 동안, 마디는 다리처럼 위로 그대로.'); }`, '376 bridge fix');
rep(`get fix() { return t('Wrist balloon (exercise 5): the wrist floats up to level with the forearm.', '손목 풍선(운동 5): 손목이 아래팔 높이까지 둥실 떠올라요.'); }`,
  `get fix() { return t('Wrist balloon (warm-up 6): after each key, the wrist comes straight back up to level.', '손목 풍선(워밍업 6): 건반을 칠 때마다 손목이 바로 같은 높이로 다시 올라와요.'); }`, '376 balloon fix');
// 10. "tip joint", as the Lesson Book says it (review A7)
rep(`get title() { return t('Nail joint caving in', '손끝 관절이 꺾여요'); }`, `get title() { return t('Tip joint caving in', '손끝 관절이 꺾여요'); }`, '376 nail title');
rep(`{ id: 'nail',   en: 'Nail joint caving in',  ko: '손톱 마디가 꺾여요',   px: 'NAIL JOINT',   why: ['The last joint bends backwards. Play slowly on the tip and keep it firm like a little pillar.', '끝마디가 뒤로 꺾여요. 천천히 끝으로 누르고, 끝마디를 작은 기둥처럼 단단하게 유지해요.'] },`,
  `{ id: 'nail',   en: 'Tip joint caving in',  ko: '손끝 관절이 꺾여요',   px: 'TIP JOINT',   why: ['The last joint bends backwards. Notice it: play slowly on the tip and feel it stay firm, like a little pillar.', '끝마디가 뒤로 꺾여요. 알아차려 봐요: 손끝으로 천천히 누르며 작은 기둥처럼 단단한지 느껴 봐요.'] },`, '376 drill nail');
// 11. the Toolbox shows the same moving drawings as the lesson
rep(`C: () => <><ExplPostureHands3/><HandShape/></> },`, `C: () => <><ExplPostureHands3/><RoundHand376/></> },`, '376 tool hand');
rep(`C: () => <><ExplPostureHands4/><FingerNumbers/></> },`, `C: () => <><ExplPostureHands4/><FingerNumbers376/></> },`, '376 tool fingers');
