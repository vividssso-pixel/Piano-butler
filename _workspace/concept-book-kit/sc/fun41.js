const { start } = require('/home/claude/pbtest/kit/contentharness');
const fs = require('fs');
const sleep = (ms) => new Promise(r => setTimeout(r, ms));
const SP = '/tmp/claude-0/-home-claude/c245f740-5546-5c71-9064-9bfc4952b3ac/scratchpad/';
(async () => { const H = await start(process.argv[2]);
  const p0 = await H.open({ path: '?view=path', w: 420, h: 900, dsf: 1 }); await sleep(1200);
  const rooms = await p0.evaluate(() => STAGES.flatMap(s => s.ids)); await p0.close();
  const out = [];
  for (const [ri, room] of rooms.entries()) {
    const p = await H.open({ path: '?drill=' + room, w: 420, h: 1000, dsf: 1 }); await sleep(900);
    const n = await p.locator('section > button').count();
    const steps = [];
    for (let k = 0; k < n; k++) {
      if (k > 0) { await p.locator('section > button').nth(k).click(); await sleep(450); }
      const r = await p.evaluate((k) => { const sec = document.querySelectorAll('section')[k]; if (!sec) return null;
        const spans = sec.querySelectorAll(':scope > button > span > span'); const title = spans.length > 1 ? spans[1].innerText : '';
        const body = sec.querySelector(':scope > div'); if (!body) return { title, boxes: [] };
        const boxes = [...body.querySelectorAll('.try-box')].filter(b => !b.parentElement.closest('.try-box')).map(b => { const bt = [...b.querySelectorAll('button')].map(x => (x.innerText || '').trim()); return { t: (b.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 160), bt: bt.join(' · ').slice(0, 300), nb: bt.length, choice: b.querySelectorAll('.choice-btn, .pixel-choice').length, ptr: b.querySelectorAll('[style*="cursor: pointer"], [style*="cursor:pointer"], [role="button"], svg [onclick]').length, inp: b.querySelectorAll('input, select, [contenteditable]').length }; });
        const other = (body.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 200), allBt = [...body.querySelectorAll('button')].map(x => (x.innerText || '').trim()).filter(x => !/Got it|이해했어요/.test(x)).join(' · ').slice(0, 300), ptrAll = body.querySelectorAll('[style*="cursor: pointer"], [style*="cursor:pointer"], [role="button"]').length;
        return { title, boxes, other, allBt, ptrAll }; }, k);
      steps.push(r);
    }
    out.push({ no: ri + 1, room, steps });
    await p.close(); process.stdout.write(ri + 1 + ' ');
  }
  fs.writeFileSync(SP + 'fun41c.json', JSON.stringify(out));
  console.log('\nrooms', out.length); await H.close(); })();
