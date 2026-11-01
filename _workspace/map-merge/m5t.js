const {chromium}=require('playwright');const fs=require('fs');let pass=0,fail=0;const ok=(c,m)=>{if(c)pass++;else{fail++;console.log('FAIL',m)}};
async function pg(b,init){const c=await b.newContext({viewport:{width:430,height:900}});if(init)await c.addInitScript(init);const p=await c.newPage();p.errs=[];p.rpc=[];p.on('pageerror',e=>p.errs.push(e.message.slice(0,150)));
 await p.route(/cdnjs\.cloudflare\.com.*react-dom/,r=>r.fulfill({body:fs.readFileSync('/tmp/da/node_modules/react-dom/umd/react-dom.production.min.js'),contentType:'application/javascript'}));
 await p.route(/cdnjs\.cloudflare\.com.*\/react\//,r=>r.fulfill({body:fs.readFileSync('/tmp/da/node_modules/react/umd/react.production.min.js'),contentType:'application/javascript'}));
 await p.route(/googletagmanager|fonts\.g/,r=>r.abort());
 await p.route(/supabase\.co\/rest\/v1\/rpc\//,r=>{p.rpc.push(r.request().url().split('/').pop());return r.fulfill({json:{name:'Juliana',ok:true}});});
 return p;}
const B='http://localhost:8855/';const TK='a'.repeat(40);
(async()=>{const b=await chromium.launch();
 // teacher device holding Juliana's link
 let p=await pg(b,`try{localStorage.setItem('pb_link_token_v1','${TK}');localStorage.setItem('pb_link_name_v1','Juliana');}catch(e){}`);
 await p.goto(B+'drills.html?teacher=1');await p.waitForTimeout(4000);
 ok(await p.isVisible('[data-testid=quiet-link]'),'quiet notice');ok(/Juliana/.test(await p.textContent('[data-testid=quiet-link]')),'names Juliana');
 await p.goto(B+'drills.html?drill=note-names&tab=learn');await p.waitForTimeout(3000);
 ok(p.rpc.length===0,'no rpc calls from teacher view: '+p.rpc);
 const q=await p.evaluate(()=>localStorage.getItem('pb_sync_log_v1'));ok(!q||q==='[]','no queued log '+q);
 // Topics = At a glance
 await p.goto(B+'drills.html?teacher=1&view=home');await p.waitForTimeout(3500);
 ok(await p.$('[data-ref-pick]'),'at a glance shown');const first=await p.getAttribute('[data-ref-pick]','data-ref-pick');
 await p.click('[data-ref-pick-chip=keys]');await p.waitForTimeout(400);ok(await p.getAttribute('[data-ref-pick]','data-ref-pick')==='keys','chip switches to keys (was '+first+')');
 ok(/Where do you want to go/.test(await p.textContent('body')),'lessons by topic still below');
 const quick=await p.evaluate(()=>[...document.querySelectorAll('button')].map(b=>b.textContent.trim()).filter(t=>t==='Reference').length);ok(quick===0,'no Reference quick chip');
 await p.screenshot({path:'m5-topics.png',fullPage:false});
 await p.click('[data-testid=quiet-remove]');await p.waitForTimeout(500);ok(!(await p.evaluate(()=>localStorage.getItem('pb_link_token_v1'))),'link removed');
 ok(p.errs.length===0,'errors '+p.errs);
 // student device: still syncs
 let s=await pg(b);await s.goto(B+'drills.html?teacher=0#k='+TK);await s.waitForTimeout(4000);ok(s.rpc.includes('pb_student_info'),'student link checked: '+s.rpc);ok(!(await s.$('[data-testid=quiet-link]')),'no quiet notice for student');
 ok(s.errs.length===0,'student errors '+s.errs);
 await b.close();console.log('pass',pass,'fail',fail)})();
