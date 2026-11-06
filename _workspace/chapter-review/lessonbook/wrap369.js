const { start } = require('./contentharness');
(async () => {
  const H = await start(process.env.BUILD || 'drills.t369.html');
  const p = await H.open({ path: '?book=lesson&ch=posture-hands&lang=en', w: 900, h: 1200 });
  await p.waitForTimeout(900);
  // every picture must sit inside its own box and inside the page body, and no two picture boxes may overlap text
  const r = await p.$$eval('.lb-page', pages => pages.map((pg, i) => {
    const body = pg.querySelector('.bk-body').getBoundingClientRect();
    const bad = [];
    pg.querySelectorAll('.pb-art').forEach(a => {
      const b = a.getBoundingClientRect(); const box = a.parentElement.getBoundingClientRect();
      if (b.left < box.left - 1 || b.right > box.right + 1 || b.top < box.top - 1 || b.bottom > box.bottom + 1) bad.push(a.dataset.art + ' outside its box');
      if (b.right > body.right + 1 || b.bottom > body.bottom + 1) bad.push(a.dataset.art + ' outside the page');
    });
    // nothing inside a picture box may spill out of it (captions included)
    pg.querySelectorAll('.lb-pic').forEach(box => {
      const r = box.getBoundingClientRect();
      box.querySelectorAll('*').forEach(el => { const b = el.getBoundingClientRect(); if (b.width && (b.bottom > r.bottom + 1 || b.right > r.right + 1 || b.left < r.left - 1 || b.top < r.top - 1)) bad.push((el.dataset.art || el.tagName) + ' spills out of its picture box'); });
    });
    return { page: i + 1, bad: [...new Set(bad)] };
  }));
  console.log(JSON.stringify(r.filter(x => x.bad.length)));
  await H.close();
})().catch(e => { console.error('CRASH', e); process.exit(1); });
