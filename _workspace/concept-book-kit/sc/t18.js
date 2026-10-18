const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT='/home/claude/pbtest/sc/shots/';
(async()=>{const H=await start('drills.t493.html');
for (const [lang,w] of [['en',390],['ko',320]]) {
 const p=await H.open({path:'?teacher=1&tool=scale-finder',w,h:900,lang});await p.waitForTimeout(1500);
 const box=p.locator('[data-sf-steps]').first();const log=[];
 log.push('steps box '+await box.count());
 await box.scrollIntoViewIfNeeded();
 await box.screenshot({path:OUT+`sf-${lang}${w}-1.png`});
 await box.locator('button.chip:has-text("Left"), button.chip:has-text("왼손")').first().click();await p.waitForTimeout(300);
 await box.locator('button.chip:has-text("Both"), button.chip:has-text("양손")').first().click();await p.waitForTimeout(300);
 await box.screenshot({path:OUT+`sf-${lang}${w}-1both.png`});
 await box.locator('[role=tab]').nth(1).click();await p.waitForTimeout(400);
 await box.locator('button.chip:has-text("F♯"), button.chip:has-text("F#")').first().click().catch(()=>{});await p.waitForTimeout(300);
 await box.screenshot({path:OUT+`sf-${lang}${w}-2.png`});
 await box.locator('[role=tab]').nth(2).click();await p.waitForTimeout(400);
 await box.screenshot({path:OUT+`sf-${lang}${w}-3.png`});
 log.push('hs '+await p.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth));
 log.push('heights '+[...new Set(await box.evaluate(e=>[...e.querySelectorAll('button')].map(b=>Math.round(b.getBoundingClientRect().height))))].join(','));
 await p.context().close();
 const q=await H.open({path:'?teacher=1&tool=scale-finder&key=Gb',w,h:900,lang});await q.waitForTimeout(1500);
 log.push('link opens free: '+(await q.locator('[data-sf-steps]').count()===0)+' | '+(await q.evaluate(()=>document.body.innerText)).includes('G')+' errs '+q._errs.length);
 await q.context().close();
 console.log(lang,w,log.join(' | '));}
await H.close();})();
