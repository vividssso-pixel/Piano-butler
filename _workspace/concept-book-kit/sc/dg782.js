// Build DG: the rooms split by grade. For each sub-room: the Lesson Book (pages, step kickers, no overflow), the Workbook
// (pages, step labels, the check-up's parts), the Teacher copy (blocks, page numbers), the drill (levels), the chapter online.
// Usage: IDS=harmony-2,harmony-3 node dg782.js drills.t782.html [shoot]
const { start } = require('/home/claude/pbtest/kit/contentharness');
const SH = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/shots/dg/';
require('fs').mkdirSync(SH, { recursive: true });
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const IDS = (process.env.IDS || 'harmony-2,harmony-3').split(',');
(async () => {
  const H = await start(process.argv[2] || 'drills.t782.html'); let bad = 0;
  const say = (ok, ...a) => { if (!ok) bad++; console.log(ok ? 'ok  ' : 'BAD ', ...a); };
  for (const id of IDS) {
    for (const lang of ['en', 'ko']) {
      const p = await H.open({ path: '?book=lesson&ch=' + id + '&lang=' + lang, w: 900, h: 1300, dsf: 1 }); await sleep(1500);
      const r = await p.evaluate(() => [...document.querySelectorAll('.bk-page')].map((pg) => ({ no: pg.getAttribute('data-lb-page'), over: pg.scrollHeight - pg.clientHeight, kick: (pg.querySelector('.lb-kicker, [data-kicker]') || {}).innerText || '', txt: pg.innerText.replace(/\s+/g, ' ').slice(0, 90) })));
      const nos = r.map(x => x.no).join(','), want = r.map((_, i) => String(i + 1)).join(',');
      say(!p._errs.length && nos === want && r.every(x => x.over <= 2), 'lesson', id, lang, 'pages', r.length, 'nos', nos, 'overflow', JSON.stringify(r.map(x => x.over)), p._errs.slice(0, 1));
      r.forEach(x => console.log('      ', x.txt));
      if (process.argv[3] && lang === 'en') { const pg = p.locator('.bk-page'); const n = await pg.count(); for (let i = 0; i < n; i++) await pg.nth(i).screenshot({ path: SH + id + '-L' + i + '.png' }); }
      await p.close();
    }
    const w = await H.open({ path: '?book=work&ch=' + id, w: 900, h: 1300, dsf: 1 }); await sleep(1500);
    const wr = await w.evaluate(() => [...document.querySelectorAll('.bk-page')].map(pg => ({ over: pg.scrollHeight - pg.clientHeight, top: (pg.querySelector('.wb-top b') || {}).innerText || '', secs: [...pg.querySelectorAll('.lb-paper > [data-sec]')].filter(x => x.offsetParent !== null).map(x => x.getAttribute('data-sec')), head: (pg.querySelector('.vic-head, header') || { innerText: '' }).innerText.replace(/\s+/g, ' ').slice(0, 60) })));
    say(!w._errs.length && wr.every(x => x.over <= 2), 'work', id, 'pages', wr.length, JSON.stringify(wr.map(x => x.top || x.secs.join(''))), w._errs.slice(0, 1));
    if (process.argv[3]) { const pg = w.locator('.bk-page'); const n = await pg.count(); for (let i = 0; i < n; i++) await pg.nth(i).screenshot({ path: SH + id + '-W' + i + '.png' }); }
    await w.close();
    const tp = await H.open({ path: '?book=teacher&ch=' + id, w: 900, h: 1300, dsf: 1 }); await sleep(1500);
    const tr = await tp.evaluate(() => ({ pages: [...document.querySelectorAll('.bk-page')].map(pg => pg.scrollHeight - pg.clientHeight), blocks: [...document.querySelectorAll('.bk-page')].flatMap(pg => [...pg.querySelectorAll('span')].filter(x => /^p\. \d+$/.test(x.innerText)).map(x => x.innerText)) }));
    say(!tp._errs.length && tr.pages.every(x => x <= 2), 'teacher', id, 'pages', tr.pages.length, 'blocks', JSON.stringify(tr.blocks), tp._errs.slice(0, 1));
    if (process.argv[3]) { const pg = tp.locator('.bk-page'); const n = await pg.count(); for (let i = 0; i < n; i++) await pg.nth(i).screenshot({ path: SH + id + '-T' + i + '.png' }); }
    await tp.close();
    const q = await H.open({ path: '?drill=' + id, w: 390, h: 2000 }); await sleep(800);
    const d = await q.evaluate((id) => { const d = DRILLS.find(x => x.id === id); return { label: d.label, levels: d.concept.levels.map(l => l.n), steps: document.querySelectorAll('[data-make], .lb-guess').length, chk: CHECK_LV[id], no: bkChapterNo(id) }; }, id);
    say(!q._errs.length && d.levels.length > 0, 'room', id, JSON.stringify(d), q._errs.slice(0, 1));
    await q.close();
  }
  console.log('bad', bad); await H.close();
})();
