// Phase 405 checks: chapter 4 applied -- the book, the app lesson, the 7-level drill, the Workbook and Teacher copy
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
(async () => {
  const H = await start(process.env.BUILD || 'drills.t405.html');
  // 1. the Lesson Book
  let p = await H.open({ path: '?book=lesson&ch=staff&lang=en', w: 900, h: 1200 });
  await p.waitForTimeout(3000);
  let r = await p.evaluate(() => ({
    pages: document.querySelectorAll('.bk-page').length,
    over: [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : 0; }),
    title: document.body.textContent.includes('Reading the Staff'),
    ask: document.querySelectorAll('[data-lb-ask]').length,
  }));
  ok(r.pages === 7, 'B1 lesson book 7 pages: ' + r.pages);
  ok(r.over.every(x => x <= 0), 'B2 no overflow ' + JSON.stringify(r.over));
  ok(r.ask === 0, 'B3 no draft marks left: ' + r.ask);
  ok(p._errs.length === 0, 'B4 no errors ' + p._errs.join('|').slice(0, 200));
  await p.context().close();
  // 2. the Workbook and the Teacher copy
  for (const [kind, want] of [['work', 7], ['teacher', 2]]) {
    p = await H.open({ path: '?book=' + kind + '&ch=staff&lang=en', w: 900, h: 1200 });
    await p.waitForTimeout(2600);
    r = await p.evaluate(() => ({
      pages: document.querySelectorAll('.bk-page').length,
      over: [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : 0; }),
    }));
    ok(r.pages === want, 'B5 ' + kind + ' pages ' + r.pages + ' (want ' + want + ')');
    ok(r.over.every(x => x <= 0), 'B6 ' + kind + ' no overflow ' + JSON.stringify(r.over));
    ok(p._errs.length === 0, 'B7 ' + kind + ' no errors ' + p._errs.join('|').slice(0, 200));
    await p.context().close();
  }
  // 3. the app lesson (the book on screen) -- no teacher strips, steps present
  p = await H.open({ path: '?drill=staff', w: 390, h: 1200 });
  await p.waitForTimeout(1600);
  r = await p.evaluate(() => ({
    steps: [...document.querySelectorAll('section button')].length,
    strips: [...document.querySelectorAll('*')].filter(e => e.childElementCount === 0 && e.tagName !== 'SCRIPT' && e.tagName !== 'STYLE' && /TEACHER/.test(e.textContent || '')).length,
    title: /Reading the Staff|오선보 읽기/.test(document.body.textContent),
    scroll: document.documentElement.scrollWidth - document.documentElement.clientWidth,
  }));
  ok(r.title, 'A1 lesson title');
  ok(r.strips === 0, 'A2 0 teacher strips: ' + r.strips);
  ok(r.scroll <= 1, 'A3 no sideways scroll: ' + r.scroll);
  ok(p._errs.length === 0, 'A4 no errors ' + p._errs.join('|').slice(0, 200));
  const stepTitles = await p.evaluate(() => [...document.querySelectorAll('section')].map(e => (e.querySelector('button span:nth-child(2)') || {}).textContent).filter(Boolean));
  ok(stepTitles.length === 6, 'A5 six steps: ' + stepTitles.join(' | '));
  // 4. the drill: 7 levels, each kind answers
  const tab = await p.$('button:has-text("Drill")'); await tab.click(); await p.waitForTimeout(700);
  const lv = await p.$$eval('button', bs => bs.filter(b => /^Level \d/.test(b.textContent)).map(b => b.textContent));
  ok(lv.length === 7, 'D1 7 levels: ' + lv.length);
  async function playLevel(n, answer) {
    await (await p.$('button:has-text("Level ' + n + '")')).click(); await p.waitForTimeout(900);
    const before = p._errs.length;
    const okAns = await answer();
    await p.waitForTimeout(900);
    const fb = await p.evaluate(() => document.body.textContent.includes('Question 2') || !!document.querySelector('.choice-btn.good, .choice-btn.bad, button.good, button.bad'));
    ok(okAns && p._errs.length === before, 'D2 level ' + n + ' answers without errors' + (p._errs.length > before ? ' ' + p._errs.slice(before).join('|').slice(0, 160) : ''));
    return fb;
  }
  await playLevel(1, async () => { const b = await p.$('button:has-text("On a line")'); if (!b) return false; await b.click(); return true; });
  await playLevel(2, async () => { const b = await p.$('button:has-text("Step up")'); if (!b) return false; await b.click(); return true; });
  await playLevel(3, async () => { const b = await p.$$('.choice-btn'); if (!b.length) return false; await b[0].click(); return true; });
  await playLevel(6, async () => {
    // tap a row on the write staff: click the svg at the guide column, middle C height
    const svg = await p.$('svg[viewBox*=" -"]') || (await p.$$('svg'))[2];
    const g = await p.$$eval('svg', () => 0);
    const el = await p.evaluateHandle(() => { const svgs = [...document.querySelectorAll('svg')]; return svgs.find(s => s.querySelector('[data-row]')) || svgs.find(s => s.getBoundingClientRect().height > 150); });
    const box = await el.asElement().boundingBox(); if (!box) return false;
    await p.mouse.click(box.x + box.width * 0.53, box.y + box.height * 0.5);
    return true;
  });
  ok(p._errs.length === 0, 'D3 no errors after drill taps ' + p._errs.join('|').slice(0, 200));
  await p.context().close();
  // 5. Clara's new design everywhere: chapter 3 app page renders without errors
  p = await H.open({ path: '?drill=note-names', w: 390, h: 1100 });
  await p.waitForTimeout(1400);
  ok(p._errs.length === 0, 'C1 chapter 3 renders with the new Clara ' + p._errs.join('|').slice(0, 160));
  await p.context().close();
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
