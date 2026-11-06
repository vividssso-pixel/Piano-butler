// ── Phase 373: print the Lesson Book and the Workbook side by side (sp373.jsx) ──
rep('function BookRoot({ kind, ch }) {', read('sp373.jsx') + '\nfunction BookRoot({ kind, ch }) {', '373 spread code');
repIn('BookRoot', `  const fixed = kind === 'work' || kind === 'teacher' || kind === 'cutouts' || (kind === 'lesson' && ids.every(id => LESSON_BOOKS[id]));`,
  `  const fixed = kind === 'spread' || kind === 'work' || kind === 'teacher' || kind === 'cutouts' || (kind === 'lesson' && ids.every(id => LESSON_BOOKS[id]));`, '373 fixed');
repIn('BookRoot', `        ? ids.map(id => { const Wb = reg[id]; return Wb ? <Wb key={id}/> : null; })`,
  `        ? kind === 'spread' ? ids.filter(id => LESSON_BOOKS[id] && WORKBOOKS[id]).map(id => <SpreadBook key={id} id={id}/>)
        : ids.map(id => { const Wb = reg[id]; return Wb ? <Wb key={id}/> : null; })`, '373 render');
rep(`printParams.get('book') === 'teacher' || printParams.get('book') === 'cutouts')) {`, `printParams.get('book') === 'teacher' || printParams.get('book') === 'cutouts' || printParams.get('book') === 'spread')) {`, '373 route');
// the Books shelf: a "Side by side" link for every chapter that has its own Lesson Book pages
repIn('BooksShelf', `    cutouts: { en: 'Cut-outs', ko: '오려 쓰는 교구', col: '#8a6a2c' },
  };`, `    cutouts: { en: 'Cut-outs', ko: '오려 쓰는 교구', col: '#8a6a2c' },
    spread: { en: 'Side by side', ko: '나란히', col: '#26296b' },
  };`, '373 shelf kind');
repIn('BooksShelf', `                {pill('teacher', id, null, !!TEACHER_COPIES[id])}`, `                {pill('teacher', id, null, !!TEACHER_COPIES[id])}
                {LESSON_BOOKS[id] && WORKBOOKS[id] && pill('spread', id, t('Lesson + Workbook, side by side', '레슨북 + 워크북 나란히'), true)}`, '373 shelf pill');
