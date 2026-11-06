// ── Phase 368: the Lesson Book written as a book; chapter 1 first (code in lb368.jsx) ──
rep('function BookRoot({ kind, ch }) {', read('art369.jsx') + '\n' + read('lb368.jsx') + '\nfunction BookRoot({ kind, ch }) {', '368 lesson book code');
// a chapter with its own Lesson Book pages prints in the fixed A4 frame, like the Workbook
repIn('BookRoot', `  const fixed = kind === 'work' || kind === 'teacher' || kind === 'cutouts';`,
  `  const fixed = kind === 'work' || kind === 'teacher' || kind === 'cutouts' || (kind === 'lesson' && ids.every(id => LESSON_BOOKS[id]));`, '368 fixed');
repIn('BookRoot', `       @media print { html, body { background: #fff } .bk-page { margin: 0 } .no-print { display: none !important } }\``,
  `       @media print { html, body { background: #fff } .bk-page { margin: 0 } .no-print { display: none !important } }\` + LB_CSS`, '368 fixed css');
repIn('BookRoot', `       @media print { .no-print { display: none !important } }\`;`, `       @media print { .no-print { display: none !important } }\` + LB_FLOW_CSS;`, '368 flow css');
repIn('BookRoot', `  const reg = kind === 'teacher' ? TEACHER_COPIES : kind === 'cutouts' ? CUTOUTS : WORKBOOKS;`,
  `  const reg = kind === 'teacher' ? TEACHER_COPIES : kind === 'cutouts' ? CUTOUTS : kind === 'lesson' ? LESSON_BOOKS : WORKBOOKS;`, '368 reg');
repIn('BookRoot', `: <LessonFix>{ids.map(id => <LessonBookChapter key={id} id={id}/>)}</LessonFix>}`,
  `: ids.map(id => LESSON_BOOKS[id] ? React.createElement(LESSON_BOOKS[id], { key: id }) : <LessonFix key={id}><LessonBookChapter id={id}/></LessonFix>)}`, '368 lesson book pages');
