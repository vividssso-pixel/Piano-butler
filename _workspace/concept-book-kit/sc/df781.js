// Build DA: the Prelim checkpoint on paper (and, with FLOORS=0a,0b,1, all three). Pages, overflow, two parts a room, the key's answers.
// Usage: node ckp773.js drills.t776.html [shoot]
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/df/';
require('fs').mkdirSync(SH, { recursive: true });
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
(async () => {
  const H = await start(process.argv[2] || 'drills.t776.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const fk of (process.env.FLOORS || '1').split(',')) {
    const p = await H.open({ path: '?book=check&floor=' + fk + '&lang=en', w: 900, h: 1300 }); await sleep(1500);
    const r = await p.evaluate(() => {
      const pages = [...document.querySelectorAll('section.bk-page')].filter(x => x.offsetParent !== null);
      return { pages: pages.length, over: pages.map(pg => { const b = pg.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : -1; }),
        rooms: [...document.querySelectorAll('.ckp-room')].map(r => ({ id: r.dataset.ckpRoom, secs: [...r.querySelectorAll('[data-sec]')].filter(x => x.offsetParent !== null).map(x => x.getAttribute('data-sec')), h: Math.round(r.getBoundingClientRect().height) })) };
    });
    say(!p._errs.length && r.over.every(x => x <= 1), fk, 'pages', r.pages, 'overflow', JSON.stringify(r.over), p._errs.slice(0, 1));
    r.rooms.forEach(x => say(x.secs.length >= 1 && x.secs.length <= 2, '   ', x.id, x.secs.join(','), x.h + 'px'));
    if (process.argv[3]) { const pg = p.locator('section.bk-page'); const n = await pg.count(); for (let i = 0; i < n; i++) await pg.nth(i).screenshot({ path: SH + 'check-' + fk + '-' + i + '.png' }); }
    await p.close();
    const q = await H.open({ path: '?book=checkkey&floor=' + fk + '&lang=en', w: 900, h: 1300 }); await sleep(2500);
    const k = await q.evaluate(() => {
      const pages = [...document.querySelectorAll('section.bk-page')].filter(x => x.offsetParent !== null);
      return { pages: pages.length, over: pages.map(pg => { const b = pg.querySelector('.bk-body'); return b ? b.scrollHeight - b.clientHeight : -1; }),
        rooms: [...document.querySelectorAll('.ckp-room-key')].map(r => ({ id: r.dataset.ckpRoom, secs: [...r.querySelectorAll('.ckp-key-ans [data-sec]')].map(x => x.getAttribute('data-sec')), txt: (r.querySelector('.ckp-key-ans') || { innerText: '' }).innerText.replace(/\s+/g, ' ').slice(0, 160) })) };
    });
    say(!q._errs.length && k.over.every(x => x <= 1), fk, 'key pages', k.pages, 'overflow', JSON.stringify(k.over), q._errs.slice(0, 1));
    k.rooms.forEach(x => say(x.secs.length >= 1 && x.secs.length <= 2, '   key', x.id, x.secs.join(','), '|', x.txt));
    if (process.argv[3]) { const pg = q.locator('section.bk-page'); const n = await pg.count(); for (let i = 0; i < n; i++) if (await pg.nth(i).isVisible()) await pg.nth(i).screenshot({ path: SH + 'key-' + fk + '-' + i + '.png' }); }
    await q.close();
  }
  console.log('bad', bad); await H.close();
})();
