const {chromium}=require('playwright');const fs=require('fs');
let pass=0,fail=0;const ok=(c,m)=>{if(c)pass++;else{fail++;console.log('FAIL',m)}};
async function pg(b,w,ls){const c=await b.newContext({viewport:{width:w,height:900}});const p=await c.newPage();p.errs=[];p.on('pageerror',e=>p.errs.push(e.message.slice(0,200)));
await p.route(/cdnjs\.cloudflare\.com.*react-dom/,r=>r.fulfill({body:fs.readFileSync('/tmp/da/node_modules/react-dom/umd/react-dom.production.min.js'),contentType:'application/javascript'}));
await p.route(/cdnjs\.cloudflare\.com.*\/react\//,r=>r.fulfill({body:fs.readFileSync('/tmp/da/node_modules/react/umd/react.production.min.js'),contentType:'application/javascript'}));
await p.route(/googletagmanager|fonts\.g/,r=>r.abort());return p;}
const tabs=p=>p.evaluate(()=>[...document.querySelectorAll('.pb-main button')].map(b=>b.textContent.trim()).filter(x=>['Home','Chapters','Map','Books','Printables','Practice','Learn','Today'].includes(x)));
(async()=>{const b=await chromium.launch();
 // teacher
 let p=await pg(b,430);await p.goto('http://localhost:8833/m1.html?teacher=1');await p.waitForTimeout(3500);
 const tb=await tabs(p);ok(tb.join()==='Map,Books,Printables,Practice'||tb.join()==='Map,Practice','teacher tabs '+tb);
 ok(await p.$('[data-map-switch=house]'),'house switch on landing');
 await p.screenshot({path:'m1-house.png'});
 await p.click('[data-map-view=topics]');await p.waitForTimeout(800);
 ok(await p.$('[data-map-switch=topics]'),'topics view');ok(/Where do you want to go/.test(await p.textContent('body')),'concept home shown');
 await p.screenshot({path:'m1-topics.png'});
 await p.click('button:has-text("Practice")');await p.waitForTimeout(500);await p.click('.pb-main button:has-text("Map")');await p.waitForTimeout(700);
 ok(await p.$('[data-map-switch=topics]'),'map tab returns to last view (topics)');
 await p.click('text=Pitch');await p.waitForTimeout(700);ok(!(await p.$('[data-map-switch]')),'no switch inside an area');
 ok(/← Topics/.test(await p.textContent('body')),'back says Topics');
 await p.click('text=← Topics');await p.waitForTimeout(500);ok(await p.$('[data-map-switch=topics]'),'back to topics');
 await p.click('[data-map-view=house]');await p.waitForTimeout(700);ok(await p.$('[data-map-switch=house]'),'house again');
 await p.click('text=Posture & Hand Shape');await p.waitForTimeout(900);ok(!(await p.$('[data-map-switch]')),'no switch inside a chapter');
 ok(p.errs.length===0,'teacher errors '+p.errs);
 // korean
 p=await pg(b,430);await p.goto('http://localhost:8833/m1.html?teacher=1&lang=ko');await p.waitForTimeout(3500);ok(/지도/.test(await p.textContent('body')),'ko Map');ok(/집/.test(await p.textContent('[data-map-switch]')),'ko house');ok(p.errs.length===0,'ko errors');
 // visitor
 p=await pg(b,430);await p.goto('http://localhost:8833/m1.html?teacher=0');await p.waitForTimeout(3500);
 const vt=await tabs(p);ok(vt.join()==='Map,Practice','visitor tabs '+vt);ok(!(await p.$('[data-map-switch]')),'visitor has no switch');
 await p.click('button:has-text("Practice")');await p.waitForTimeout(500);await p.click('.pb-main button:has-text("Map")');await p.waitForTimeout(700);
 ok(/Music map/.test(await p.textContent('body')),'visitor map = house');
 ok(p.errs.length===0,'visitor errors '+p.errs);
 // old URL still works
 p=await pg(b,430);await p.goto('http://localhost:8833/m1.html?teacher=1&view=home');await p.waitForTimeout(3500);ok(await p.$('[data-map-switch=topics]'),'old ?view=home opens Topics');
 await b.close();console.log('pass',pass,'fail',fail)})();
