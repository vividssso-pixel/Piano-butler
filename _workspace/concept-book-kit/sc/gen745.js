// Generic room check for the Grade 7 and 8 floors: learn steps (en/ko), drill levels, Home lessons, the three books.
// node gen745.js drills.tNNN.html chapterId tool1,tool2,... [nLevels]
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/g/';
const [, , FILE, CH, TOOLS, NLV] = process.argv;
(async () => { const H = await start(FILE); const sleep = (ms) => new Promise(r => setTimeout(r, ms)); const errs = [];
  const w = (p, tag) => { p.on('pageerror', e => errs.push(tag + ': ' + String(e).slice(0, 300))); p.on('console', m => { if (m.type() === 'error' && !/Failed to load resource|agent-proxy/.test(m.text())) errs.push(tag + ' console: ' + m.text().slice(0, 200)); }); return p; };
  for (const lang of ['en', 'ko']) {
    const p = w(await H.open({ path: '?drill=' + CH + '&tab=learn', w: 390, h: 1500, lang, dsf: 1.5 }), 'learn-' + lang); await sleep(2500);
    await p.screenshot({ path: SH + CH + '-open-' + lang + '.png' });
    const heads = p.locator('section > button', { hasText: lang === 'en' ? /Step \d+ of/ : /\d+ \/ \d+ 단계/ });
    const N = await heads.count(); console.log(lang, 'steps', N);
    for (let i = 0; i < N; i++) {
      const hd = heads.nth(i); const sec = hd.locator('xpath=..');
      const isOpen = await sec.locator('div[style*="border-left"]').count();
      if (!isOpen) { await hd.scrollIntoViewIfNeeded(); await hd.click(); await sleep(900); }
      await sec.screenshot({ path: SH + CH + '-s' + (i + 1) + '-' + lang + '-a.png' });
      const box = sec.locator('.try-box').first();
      if (await box.count()) {
        const go = box.locator('button', { hasText: /Your turn|내가 해보기|Which one|어느 것|Where did|어디로|Major or minor|장조\? 단조|Which hand|어느 손|Test me|문제/ }).first();
        if (await go.count()) { await go.click(); await sleep(1200); }
        const ch = box.locator('.choice-btn').first(); if (await ch.count()) { await ch.click(); await sleep(400); }
        await sec.screenshot({ path: SH + CH + '-s' + (i + 1) + '-' + lang + '-b.png' });
        console.log(lang, 'step', i + 1, '|', (await box.innerText()).split('\n').slice(-3).join(' | ').slice(0, 220));
      }
    }
    await p.close();
  }
  const nl = +(NLV || 5);
  for (let lv = 1; lv <= nl; lv++) { const lang = lv % 2 ? 'ko' : 'en'; const d = w(await H.open({ path: '?drill=' + CH + '&tab=drill&level=' + lv + '&mode=lesson', w: 390, h: 1100, lang, dsf: 1.5 }), 'drill' + lv); await sleep(2000);
    await d.screenshot({ path: SH + CH + '-drill' + lv + '.png' });
    const b = d.locator('.choice-btn').first(); if (await b.count()) { await b.click(); await sleep(600); await d.screenshot({ path: SH + CH + '-drill' + lv + 'b.png' }); }
    console.log('drill', lv, (await d.locator('body').innerText()).split('\n').filter(x => x.trim()).slice(0, 14).join(' | ').slice(0, 300));
    await d.close(); }
  let li = 0;
  for (const tool of (TOOLS || '').split(',').filter(Boolean)) { const lang = li++ % 2 ? 'ko' : 'en'; const e = w(await H.open({ path: '?teacher=1&view=tools&tool=' + tool + '&ret=home', w: 390, h: 1300, lang, dsf: 1.5 }), 'home-' + tool); await sleep(1400);
    for (let g = 0; g < 9; g++) { const nx = e.locator('button', { hasText: /하나씩|다음 →|내가 해보기|One at a time|One by one|Next →|My turn|Your turn/ }).first(); if (!(await nx.count())) break; await nx.click(); await sleep(350); }
    await sleep(400); await e.screenshot({ path: SH + CH + '-home-' + tool + '.png', fullPage: true }); await e.close(); }
  for (const kind of ['lesson', 'work', 'teacher']) {
    const b2 = w(await H.open({ path: '?book=' + kind + '&ch=' + CH + '&lang=en', w: 900, h: 1300, lang: 'en', dsf: 1 }), 'book-' + kind); if (kind !== 'teacher') await b2.emulateMedia({ media: 'print' }); await sleep(3000);
    const nP = await b2.locator('section.bk-page').count();
    for (let n = 0; n < nP; n++) { const pg = b2.locator('section.bk-page').nth(n); await pg.scrollIntoViewIfNeeded(); await pg.screenshot({ path: SH + CH + '-' + kind + '-' + (n + 1) + '.png' }); }
    const ov = await b2.evaluate(() => [...document.querySelectorAll('.bk-page')].map((pg) => { const b = pg.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : 0; })); console.log(kind, 'pages', nP, 'overflow', ov.join(' '));
    await b2.close(); }
  console.log('errors', JSON.stringify(errs)); process.exit(0);
})();
