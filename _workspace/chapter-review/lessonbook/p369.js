// ── Phase 370 (draft, with chapter 1): the app's chapter 1 drill draws the Lesson Book's cast (art369.jsx) ──
// Level 1 (stool set-up) and level 2 (hand-shape faults): the same pen-and-ink pictures as the book, no hints.
repIn('PostureQuestion', `      {q.kind === 'sit' ? <SeatedFigure S={preset.S} F={preset.F}/> : <HandSide pose={q.key} labels={false} tall/>}`,
  `      <div style={{display:'flex',justifyContent:'center'}}><PbArt name={'q-' + q.kind + '-' + q.key} h={q.kind === 'sit' ? 230 : 150} style={{maxWidth:'100%'}}/></div>`, '369 drill pictures');
// Level 3 (which finger?): the book's hand from above, one finger lit in coral
repIn('FsQuestion', `<HandPic hand={q.hand} lit={q.f} size={170}/>`, `<PbArt name={'q-fingers-' + q.hand} lit={q.f} h={200}/>`, '369 finger picture');
