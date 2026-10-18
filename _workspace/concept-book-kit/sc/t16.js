const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT='/home/claude/pbtest/sc/shots/';
(async()=>{const H=await start('drills.t492.html');
for (const [lang,w] of [['en',390],['ko',390],['ko',320]]) {
 const p=await H.open({path:'?teacher=1&tool=key-finder',w,h:900,lang});await p.waitForTimeout(1500);
 const box=p.locator('[data-kf-steps]').first(); const log=[];
 await box.scrollIntoViewIfNeeded();
 await box.screenshot({path:OUT+`kt-${lang}${w}-1a.png`});
 const chips=()=>box.locator('button.chip[aria-label]:not([role=tab])');
 let c=await chips().count(); await chips().nth(0).click();await p.waitForTimeout(200); await chips().nth(c-1).click();await p.waitForTimeout(500);
 await box.screenshot({path:OUT+`kt-${lang}${w}-1b.png`});
 await box.locator('[role=tab]').nth(1).click();await p.waitForTimeout(300);
 c=await chips().count(); await chips().nth(c-2).click();await p.waitForTimeout(500);
 await box.screenshot({path:OUT+`kt-${lang}${w}-2.png`});
 await box.locator('[role=tab]').nth(2).click();await p.waitForTimeout(400);
 await box.screenshot({path:OUT+`kt-${lang}${w}-3.png`});
 await box.locator('[role=tab]').nth(3).click();await p.waitForTimeout(400);
 await box.screenshot({path:OUT+`kt-${lang}${w}-4.png`});
 log.push('hs '+await p.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth));
 log.push('heights '+[...new Set(await box.evaluate(e=>[...e.querySelectorAll('button,a.ghost-btn')].map(b=>Math.round(b.getBoundingClientRect().height))))].join(','));
 console.log(lang,w,log.join(' | '),'errs='+JSON.stringify(p._errs));await p.context().close();}
await H.close();})();
