// Phase 387 checks: the chapter 2 app lesson is the book on screen; drill has the naming level;
// the printed books: ch1 lesson without teacher strips still fits; ch2 lesson book prints 7 pages.
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
(async () => {
  const H = await start(process.env.BUILD || 'drills.new.html');
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?drill=first-steps', w: 390, h: 900, lang });
    await p.waitForTimeout(900);
    const titles = await p.$$eval('section[id^="first-steps-step-"]', els => els.map(e => e.querySelector('button span span:last-child').textContent));
    const EN = ['Small house, big house', 'The white keys of each house', 'The whole piano & middle C', 'Play on the patterns', 'My five checks'];
    const KO = ['작은 집, 큰 집', '집마다 딸린 흰건반', '피아노 전체와 가운데 도', '패턴 위에서 연주', '나의 다섯 가지 확인'];
    ok(JSON.stringify(titles) === JSON.stringify(lang === 'en' ? EN : KO), 'T1 ' + lang + ' steps = book pages: ' + titles.join(' / '));
    const parts = await p.evaluate(() => {
      const q = (i, sel) => !!document.querySelector('#first-steps-step-' + i + ' ' + sel);
      return [q(0, '.try-box svg'), q(1, '[data-whose-house]'), q(2, '.try-box svg'), q(3, 'button'), q(4, '[data-five-checks]')];
    });
    ok(parts.every(Boolean), 'T2 ' + lang + ' moving parts on steps 1-6: ' + JSON.stringify(parts));
    const scroll = await p.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    ok(scroll <= 1, 'T3 ' + lang + ' no sideways scroll (' + scroll + ')');
    ok(p._errs.length === 0, 'T4 ' + lang + ' no errors ' + p._errs.join('|').slice(0, 150));
    await p.context().close();
  }
  // whose-house + which-letter respond
  let p = await H.open({ path: '?drill=first-steps', w: 390, h: 900 });
  await p.waitForTimeout(700);
  await p.evaluate(() => document.querySelector('#first-steps-step-1 [data-whose-house]').scrollIntoView({ block: 'center' }));
  await p.click('#first-steps-step-1 [data-whose-house] [data-key="0"]');
  await p.waitForTimeout(300);
  const msg = await p.$eval('#first-steps-step-1 [data-whose-house]', e => e.innerText);
  ok(/SMALL|3/.test(msg), 'T5 whose-house answers a tap');
  // drill: level 3 shows the naming question
  const tab = await p.$('button:has-text("Drill")'); await tab.click(); await p.waitForTimeout(700);
  const chip = await p.$('button:has-text("Level 3")'); await chip.click(); await p.waitForTimeout(900);
  const txt = await p.evaluate(() => document.body.innerText);
  ok(/Whose house is this white key\?/.test(txt), 'T6 level 3 asks whose house');
  ok(!/Loud or soft/.test(txt), 'T6b loud/soft level gone');
  const letters = await p.$$eval('.choice-btn', els => els.map(e => e.textContent.trim()));
  ok(letters.join(',') === 'Small house,Big house', 'T7 two house choices: ' + letters.join(','));
  // the five checks: three stages, tap one
  await p.goto(p.url().split('?')[0] + '?drill=first-steps'); await p.waitForTimeout(800);
  await p.evaluate(() => document.querySelector('#first-steps-step-4 [data-five-checks]').scrollIntoView({ block: 'center' }));
  const b3 = await p.$$('#first-steps-step-4 [data-five-checks] button[aria-pressed]');
  ok(b3.length === 15, 'T7b five checks x three stages (' + b3.length + ')');
  await b3[2].click(); await p.waitForTimeout(200);
  const sum = await p.$eval('#first-steps-step-4 [data-five-checks]', e => e.innerText);
  ok(/1 of 5: got it!/.test(sum), 'T7c a got-it counts');
  const fsTxt = await p.evaluate(() => document.querySelector('.fade-up') ? document.body.innerText : '');
  ok(p._errs.length === 0, 'T8 drill no errors');
  await p.context().close();
  // books
  p = await H.open({ path: '?book=lesson&ch=first-steps&lang=en', w: 900, h: 1200 });
  await p.waitForTimeout(1600);
  let info = await p.$$eval('.bk-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : null; }));
  ok(info.length === 6 && info.every(v => v <= 1), 'T9 ch2 lesson book: 6 pages, no overflow ' + JSON.stringify(info));
  const strips = await p.$$eval('[data-lb-teacher]', els => els.length);
  ok(strips === 0, 'T10 no teacher strips in the printed ch2 book (' + strips + ')');
  await p.context().close();
  p = await H.open({ path: '?book=lesson&ch=posture-hands&lang=en', w: 900, h: 1200 });
  await p.waitForTimeout(1600);
  info = await p.$$eval('.bk-page', els => els.map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : null; }));
  const strips1 = await p.$$eval('[data-lb-teacher]', els => els.length);
  ok(info.length === 7 && info.every(v => v <= 1), 'T11 ch1 lesson book still fits without strips ' + JSON.stringify(info));
  ok(strips1 === 0, 'T12 no teacher strips in the printed ch1 book');
  await p.context().close();
  // teacher view keeps the strips on screen
  p = await H.open({ path: '?drill=first-steps&teacher=1', w: 390, h: 900, store: { pb_mode_v1: 'teacher' } });
  await p.waitForTimeout(900);
  const appStrips = await p.$$eval('[data-lb-teacher]', els => els.length);
  ok(appStrips === 0, 'T13 no teacher strips in the app teacher view (Phase 399) (' + appStrips + ')');
  ok(p._errs.length === 0, 'T14 teacher view no errors');
  await p.context().close();
  await H.close(); process.exit(process.exitCode || 0);
})().catch(e => { console.error('CRASH', e); process.exit(1); });
