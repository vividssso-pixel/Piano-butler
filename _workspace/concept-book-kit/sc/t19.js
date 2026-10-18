const { start } = require('/home/claude/pbtest/kit/contentharness');
const OUT='/home/claude/pbtest/sc/shots/';
const L=['C','D','E','F','G','A','B'], NAT=[0,2,4,5,7,9,11], MAJ=[0,2,4,5,7,9,11];
const spell=(tonic)=>{const base=L.indexOf(tonic[0]);const acc=tonic.slice(1);const tpc=(NAT[base]+(acc==='#'?1:acc==='b'?-1:0)+12)%12;
 return MAJ.map((iv,i)=>{const li=(base+i)%7;let d=((tpc+iv-NAT[li])%12+12)%12;if(d>6)d-=12;return L[li]+(d===1?'♯':d===-1?'♭':d===0?'':'?'+d);});};
const TON=[['C','C'],['D♭','Db'],['D','D'],['E♭','Eb'],['E','E'],['F','F'],['F♯','F#'],['G','G'],['A♭','Ab'],['A','A'],['B♭','Bb'],['B','B']];
(async()=>{const H=await start('drills.t494.html');
 const p=await H.open({path:'?teacher=1&tool=scale-finder',w:390,h:900,lang:'en'});await p.waitForTimeout(1500);
 const box=p.locator('[data-sf-steps]').first();await box.scrollIntoViewIfNeeded();
 await box.locator('[role=tab]').nth(2).click();await p.waitForTimeout(300);
 let bad=0;
 for(const [label,key] of TON){
  await box.locator('button.chip',{hasText:new RegExp('^'+label+'$')}).first().click();await p.waitForTimeout(150);
  for(const hand of ['Right','Left']){
   await box.locator('button.chip',{hasText:hand+' hand'}).click();await p.waitForTimeout(120);
   const got=await box.locator('svg').first().evaluate(s=>[...s.querySelectorAll('text')].map(t=>t.textContent.trim()).filter(x=>x&&!/^\d$/.test(x)));
   const exp=spell(key).concat([spell(key)[0]]);
   const ok=JSON.stringify([...got].sort())===JSON.stringify([...exp].sort());
   if(!ok){bad++;console.log('MISMATCH',label,hand,got.join(' '),'| exp',exp.join(' '));}
  }}
 console.log('12 keys x 2 hands compared, mismatches:',bad,'errs',p._errs.length);
 await box.locator('button.chip',{hasText:/^D♭$/}).first().click();await p.waitForTimeout(200);
 await box.locator('button.chip',{hasText:'Both hands'}).click();await p.waitForTimeout(300);
 await box.screenshot({path:OUT+'nn-en-Db-both.png'});
 await box.locator('button.chip',{hasText:/^G$/}).first().click();await p.waitForTimeout(200);
 await box.locator('button.chip',{hasText:'Right hand'}).click();await p.waitForTimeout(300);
 await box.screenshot({path:OUT+'nn-en-G-rh.png'});
 await p.context().close();
 const q=await H.open({path:'?teacher=1&tool=scale-finder&key=Gb',w:390,h:900,lang:'ko'});await q.waitForTimeout(1500);
 await q.screenshot({path:OUT+'nn-ko-free-Gb.png',fullPage:false});console.log('free errs',q._errs.length);
 const r=await H.open({path:'?teacher=1&tool=scale-finder',w:320,h:900,lang:'ko'});await r.waitForTimeout(1500);
 const b2=r.locator('[data-sf-steps]').first();await b2.scrollIntoViewIfNeeded();await b2.locator('[role=tab]').nth(1).click();await r.waitForTimeout(300);
 await b2.screenshot({path:OUT+'nn-ko320-2.png'});console.log('hs',await r.evaluate(()=>document.documentElement.scrollWidth-document.documentElement.clientWidth),r._errs.length);
 await H.close();})();
