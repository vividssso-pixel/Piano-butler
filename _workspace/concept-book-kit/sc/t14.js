const { start } = require('/home/claude/pbtest/kit/contentharness');
(async()=>{const H=await start('drills.t491.html');
for (const [lang,w] of [['en',390],['ko',320]]) {
 const p=await H.open({path:'?drill=note-values&tab=drill&level=1&mode=lesson',w,h:900,lang});await p.waitForTimeout(1500);
 const trk=p.locator('[role=img][aria-label*="/"], [role=img][aria-label*="of 10"]').first();
 console.log(lang,'track found',await trk.count(), await trk.getAttribute('aria-label').catch(()=>null));
 await p.screenshot({path:`/home/claude/pbtest/sc/shots/bd-${lang}-q1.png`});
 // answer 3 questions: click first choice each time, then next
 for (let i=0;i<3;i++){ const c=p.locator('.choice-btn').first(); if(!(await c.count())) break; await c.click(); await p.waitForTimeout(500);
   const nx=p.locator('button:has-text("Next"), button:has-text("다음")').first(); if(await nx.count()) { await nx.click(); await p.waitForTimeout(500);} }
 console.log(lang,'after 3:',await trk.getAttribute('aria-label').catch(()=>null));
 await p.screenshot({path:`/home/claude/pbtest/sc/shots/bd-${lang}-q4.png`});
 console.log(lang,'hs',await p.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth),'errs',p._errs.length, 'dice text', /Square|주사위|D\.C\.: back/.test(await p.evaluate(()=>document.body.innerText)));
 await p.context().close();}
await H.close();})();
