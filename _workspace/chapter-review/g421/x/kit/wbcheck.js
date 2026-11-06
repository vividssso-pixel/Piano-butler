// Workbook / Teacher / spread overflow check for one chapter, plus per-page screenshots of the Workbook
//   BUILD=drills.t412.html CH=first-steps TAG=n412 node wbcheck.js
const { start } = require('./contentharness');
const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
(async () => {
  const H = await start(process.env.BUILD), CH = process.env.CH, TAG = process.env.TAG || 'wb';
  for (const [kind, lang] of [['work', 'en'], ['work', 'ko'], ['teacher', 'en'], ['spread', 'en'], ['lesson', 'en']]) {
    const p = await H.open({ path: '?book=' + kind + '&ch=' + CH + '&lang=' + lang, w: 900, h: 1200 });
    await p.waitForTimeout(2600);
    const r = await p.evaluate(() => ({
      pages: document.querySelectorAll('.bk-page').length,
      over: [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : 0; }),
      hor: [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); if (!b) return 0; const R = b.getBoundingClientRect().right; return Math.max(0, ...[...b.querySelectorAll('*')].map(x => Math.round(x.getBoundingClientRect().right - R))); }),
      slack: [...document.querySelectorAll('.bk-page')].map(pg => Math.max(0, ...[...pg.querySelectorAll('div')].filter(d => d.style.border && d.style.border.includes('dashed')).map(d => { const inner = d.lastElementChild; if (!inner || inner.style.justifyContent !== 'center') return 0; const kids = [...inner.children]; if (!kids.length) return 0; const used = kids[kids.length - 1].getBoundingClientRect().bottom - kids[0].getBoundingClientRect().top; return Math.round(inner.getBoundingClientRect().height - used); }))),
      free: [...document.querySelectorAll('.bk-page')].map(e => { const b = e.querySelector('.bk-body'); if (!b) return 0; const kids = [...b.children]; if (!kids.length) return 0; const last = kids[kids.length - 1].getBoundingClientRect(); return Math.round(b.getBoundingClientRect().bottom - last.bottom); }),
    }));
    ok(r.over.every(x => x <= 0) && r.hor.every(x => x <= 0), kind + ' ' + lang + ' pages ' + r.pages + ' over ' + JSON.stringify(r.over) + ' hor ' + JSON.stringify(r.hor) + ' free ' + JSON.stringify(r.free) + ' playSlack ' + JSON.stringify(r.slack));
    ok(p._errs.length === 0, kind + ' ' + lang + ' no errors ' + p._errs.join('|').slice(0, 200));
    if (kind === 'work' && lang === 'en') {
      const pages = await p.$$('.bk-page');
      for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: TAG + '-' + (i + 1) + '.png' });
    }
    await p.context().close();
  }
  await H.close();
})();
