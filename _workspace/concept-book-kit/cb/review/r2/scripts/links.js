// Links inside the screen book: count, ids, lang and lock kept; follow a few as a student and as a Korean student
const { start } = require('/home/claude/pbtest/kit/contentharness');
(async () => {
  const H = await start('drills.t485.html');
  for (const [r, lang] of [['?tool=cb-p-scales&lock=1', 'en'], ['?tool=cb-p-scales&lock=1', 'ko'], ['?teacher=1&tool=cb-p-scales', 'en'], ['?teacher=1&tool=cb-p-scales', 'ko']]) {
    const p = await H.open({ path: r, w: 390, h: 860, lang, dsf: 1 }); await p.waitForTimeout(1200);
    const hrefs = await p.$$eval('.pb-main a[href]', a => a.map(x => x.getAttribute('href')));
    const tools = hrefs.filter(h => /tool=/.test(h));
    const bad = tools.filter(h => (lang === 'ko' && !/lang=ko/.test(h)) || (/lock=1/.test(r) && !/lock=1/.test(h)));
    const qrs = await p.$$eval('canvas, svg[data-qr], [data-qr]', a => a.length);
    console.log(lang, r, 'links', hrefs.length, 'tool links', tools.length, 'bad', JSON.stringify(bad), '\n   ', tools.join(' '));
    // the tab bar and header in this view
    const tabs = await p.$$eval('button, a', a => a.map(x => x.innerText.trim()).filter(x => /^(Chapters|Toolbox|Practice|챕터|도구함|연습|Student view|학생 화면|TEACHER VIEW|교사 화면)$/.test(x)));
    console.log('    chrome visible:', JSON.stringify([...new Set(tabs)]));
    await p.context().close();
  }
  // follow: a student taps 'Fingering' after picking G♭, and a ladder chip
  for (const lang of ['en', 'ko']) {
    const p = await H.open({ path: '?tool=cb-p-scales&lock=1', w: 390, h: 860, lang, dsf: 1 }); await p.waitForTimeout(1200);
    const pad = await p.$('[data-cb="key-pad"]');
    const circleBtn = await pad.$('button[role=tab]:nth-child(2)'); if (circleBtn) { await circleBtn.click(); await p.waitForTimeout(200); }
    const g = await pad.$('g[data-key="Gb"]'); if (g) { await g.click(); await p.waitForTimeout(200); }
    const fing = await pad.$('a'); const href = await fing.getAttribute('href');
    await fing.click(); await p.waitForTimeout(1600);
    const st = await p.evaluate(() => ({ url: location.search, title: (document.querySelector('.pb-main h2, .pb-main [class*=title]') || {}).innerText, tabs: [...document.querySelectorAll('button, a')].map(x => x.innerText.trim()).filter(x => /^(Chapters|Toolbox|Practice|챕터|도구함|연습|Learn|배우기|← Toolbox|← 도구 모음|TEACHER VIEW|교사 화면|Copy student link|학생 링크 복사)$/.test(x)), lang: document.documentElement.lang, txt: document.querySelector('.pb-main').innerText.slice(0, 300).replace(/\s+/g, ' ') }));
    console.log('FOLLOW fingering', lang, href, JSON.stringify(st));
    await p.goBack(); await p.waitForTimeout(1500);
    const back = await p.evaluate(() => location.search + ' ' + !!document.querySelector('[data-cb="key-pad"]'));
    console.log('   back ->', back);
    // a ladder chip
    const chip = await p.$('.cb-ladder a[href*="tool=relative-minor"]'); if (chip) { const h = await chip.getAttribute('href'); await chip.click(); await p.waitForTimeout(1500);
      const st2 = await p.evaluate(() => ({ url: location.search, tabs: [...document.querySelectorAll('button, a')].map(x => x.innerText.trim()).filter(x => /^(Chapters|Toolbox|Practice|챕터|도구함|연습|← Toolbox|← 도구 모음|TEACHER VIEW|교사 화면)$/.test(x)), ko: /[가-힣]/.test(document.querySelector('.pb-main').innerText) }));
      console.log('FOLLOW chip', lang, h, JSON.stringify(st2)); }
    console.log('   errs', p._errs.join('|'));
    await p.context().close();
  }
  // a fresh visit to a link with lang=ko and lock=1 (as copied), on a device that never chose a mode
  for (const path of ['?tool=scale-finder&key=Gb&lang=ko&lock=1', '?tool=relative-minor&lang=ko&lock=1']) {
    const p = await H.open({ path, w: 390, h: 860, dsf: 1 }); await p.waitForTimeout(1200);
    const st = await p.evaluate(() => ({ lang: document.documentElement.lang, ko: /[가-힣]{3}/.test(document.querySelector('.pb-main').innerText), tabs: [...document.querySelectorAll('button, a')].map(x => x.innerText.trim()).filter(x => /^(Chapters|Toolbox|Practice|챕터|도구함|연습|TEACHER VIEW|교사 화면)$/.test(x)) }));
    console.log('FRESH', path, JSON.stringify(st));
    await p.context().close();
  }
  await H.close();
})();
