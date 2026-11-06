// ── Phase 378: the house in the books (bkhouse378.jsx) ──
rep('function BkPath({ current, compact }) {', read('bkhouse378.jsx') + '\nfunction BkPath({ current, compact }) {', '378 code');
rep(`    {total <= 7 && levels.length <= 6 && <BkPath current={id} compact/>}`, `    {total <= 7 && levels.length <= 6 && <BkHouse current={id} compact/>}`, '378 map page');
repIn('FrontMatter', `    <BkPath/>`, `    <BkHouse/>`, '378 front');
repIn('FrontMatter', `  P(<WbLog/>);`, `  P(<BkHousePage/>);
  P(<WbLog/>);`, '378 colour-in page');
