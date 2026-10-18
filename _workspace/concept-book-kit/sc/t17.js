const { start } = require('/home/claude/pbtest/kit/contentharness');
(async()=>{const H=await start('drills.t492.html');const p=await H.open({path:'?teacher=1&tool=key-finder',w:390,h:900,lang:'en'});await p.waitForTimeout(1500);
const box=p.locator('[data-kf-steps]').first();await box.scrollIntoViewIfNeeded();
await box.locator('button.chip:has-text("5♯")').click();await p.waitForTimeout(200);
const ch=box.locator('button.chip[aria-label]:not([role=tab])');const c=await ch.count();await ch.nth(c-1).click();await p.waitForTimeout(400);
await box.locator('[role=tab]').nth(2).click();await p.waitForTimeout(400);
console.log((await box.innerText()).replace(/\s+/g,' ').slice(0,200),p._errs.length);await H.close();})();
