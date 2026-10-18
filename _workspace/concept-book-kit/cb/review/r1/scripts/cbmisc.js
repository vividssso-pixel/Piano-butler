// The Toolbox card, search (Toolbox box and the Find overlay), the student link, and the links inside the screen book.
const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT = '/home/claude/pbtest/cb/review/r1/shots';
(async () => {
  const H = await start('drills.t485.html');
  const log = (...a) => console.log(...a);
  // ── Toolbox: the card ──
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?teacher=1&view=toolbox', w: 390, h: 860, lang });
    await p.waitForTimeout(800);
    const cards = await p.$$('xpath=//div[contains(., "The concept book") or contains(., "개념 책")][count(.//button)=1 and .//a]');
    const cardInfo = await p.evaluate(() => { const out = []; document.querySelectorAll('a[href*="book=concept"]').forEach(a => { const box = a.closest('div').parentElement; out.push({ href: a.getAttribute('href'), target: a.getAttribute('target'), text: box.innerText.replace(/\s+/g, ' ').slice(0, 140), under: (box.parentElement.querySelector('.stf-title') || {}).textContent }); }); return out; });
    log(lang + ' toolbox cards: ' + JSON.stringify(cardInfo));
    const a = await p.$('a[href*="book=concept"]');
    if (a) { const box = await a.evaluateHandle(e => e.closest('div').parentElement); await box.asElement().screenshot({ path: OUT + '/toolbox-card-' + lang + '.png' }); }
    // Open
    const open = await p.$('a[href*="book=concept"] >> xpath=../button');
    if (open) { await open.click(); await p.waitForTimeout(700); log(lang + ' Open -> ' + await p.evaluate(() => location.search) + ' title=' + (await p.evaluate(() => (document.querySelector('h2') || {}).textContent))); }
    // Back
    const back = await p.$('button:has-text("←")'); if (back) { const bt = await back.innerText(); await back.click(); await p.waitForTimeout(500); log(lang + ' back "' + bt + '" -> ' + await p.evaluate(() => location.search)); }
    log(lang + ' errs=' + JSON.stringify(p._errs));
    await p.context().close();
  }
  // ── search ──
  {
    const p = await H.open({ path: '?teacher=1&view=toolbox', w: 390, h: 860 });
    for (const q of ['concept', 'concept book', 'scales and keys', 'cb-p', 'the rule']) {
      await p.fill('input.search-input', q); await p.waitForTimeout(250);
      const hit = await p.evaluate(() => [...document.querySelectorAll('#root *')].filter(e => e.children.length === 0 && /Concept book: Scales and keys/.test(e.textContent)).length);
      const count = await p.evaluate(() => (document.body.innerText.match(/(\d+) tools?/) || [])[1]);
      log('toolbox search "' + q + '": rows naming the concept book=' + hit + ' (count line ' + count + ')');
    }
    await p.fill('input.search-input', '');
    // the Find overlay
    const fb = await p.$('button[aria-label*="ind"], button[title*="ind"]');
    const fbs = await p.$$eval('button', a => a.filter(b => /🔎|search|Find/i.test((b.getAttribute('aria-label') || '') + b.textContent)).map(b => (b.getAttribute('aria-label') || '') + '|' + b.textContent.slice(0, 20)));
    log('find buttons: ' + JSON.stringify(fbs));
    const btn = await p.$('button[aria-label="Find a tool"], button[aria-label="Find"], button[aria-label*="tool"]');
    if (btn) { await btn.click(); await p.waitForTimeout(300);
      for (const q of ['concept', 'scales and keys', 'rule']) { await p.fill('input[autofocus], input[placeholder*="Type a word"]', q); await p.waitForTimeout(250);
        const hit = await p.evaluate(() => [...document.querySelectorAll('div,button,span')].filter(e => e.children.length === 0 && /Concept book: Scales and keys/.test(e.textContent)).length);
        log('find overlay "' + q + '": concept-book rows=' + hit); } }
    log('search errs=' + JSON.stringify(p._errs));
    await p.context().close();
  }
  // ── the student link, on a device that never chose a mode ──
  for (const store of [{}, { pb_mode_v1: 'student' }]) {
    const p = await H.open({ path: '?tool=cb-p-scales&lock=1', w: 390, h: 860, store });
    await p.evaluate(() => localStorage.removeItem('pb_mode_v1')); if (store.pb_mode_v1) await p.evaluate(() => localStorage.setItem('pb_mode_v1', 'student'));
    await p.reload(); await p.waitForSelector('#root *'); await p.waitForTimeout(900);
    const head = await p.evaluate(() => document.body.innerText.slice(0, 200).replace(/\s+/g, ' '));
    const tabs = await p.evaluate(() => ['Chapters', 'Toolbox', 'Practice', 'TEACHER VIEW'].filter(w => document.body.innerText.includes(w)));
    log('student link (mode ' + (store.pb_mode_v1 || 'unset') + '): head="' + head.slice(0, 120) + '" tabs/teacher words=' + JSON.stringify(tabs) + ' errs=' + JSON.stringify(p._errs));
    const link = await p.$('a.chip[href*="tool="]');
    const hrefs = await p.$$eval('a[href*="tool="]', a => a.map(x => x.getAttribute('href')));
    log('  links in the book: ' + hrefs.length + ' e.g. ' + JSON.stringify(hrefs.slice(0, 3)) + ' ... ' + JSON.stringify(hrefs.slice(-2)));
    if (link) { await link.click(); await p.waitForTimeout(1500);
      const after = await p.evaluate(() => ({ url: location.search, words: ['Chapters', 'Toolbox', 'Practice', 'TEACHER VIEW', 'Copy student link'].filter(w => document.body.innerText.includes(w)) }));
      log('  after tapping a tool link: ' + JSON.stringify(after)); }
    await p.context().close();
  }
  // ── links keep the language ──
  {
    const p = await H.open({ path: '?teacher=1&tool=cb-p-scales', w: 390, h: 860, lang: 'ko' });
    const hrefs = await p.$$eval('a[href*="tool="]', a => a.map(x => x.getAttribute('href')));
    log('ko links: ' + JSON.stringify(hrefs));
    const first = await p.$('a.chip[href*="tool="]'); await first.click(); await p.waitForTimeout(1500);
    log('  after ko link: ' + await p.evaluate(() => location.search) + ' lang button shows ' + JSON.stringify(await p.$$eval('button.chip', a => a.map(b => b.textContent).filter(x => /한국어|EN/.test(x)))));
    await p.context().close();
  }
  await H.close();
})();
