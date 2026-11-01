const {chromium}=require('playwright');const fs=require('fs');let pass=0,fail=0;const ok=(c,m)=>{if(c)pass++;else{fail++;console.log('FAIL',m)}};
const today=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][new Date().getDay()];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:900,height:1000}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8855/teacher-dashboard.html');await p.waitForTimeout(3000);
await p.click('button.pb-tab:has-text("Students")');await p.waitForTimeout(600);
ok(await p.isVisible('[data-testid=add-test-student]'),'add button');await p.click('[data-testid=add-test-student]');await p.waitForTimeout(800);
ok(!(await p.$('[data-testid=add-test-student]')),'button gone after add');
const card=await p.textContent('[data-testid=student-card]:has-text("Test (me)")');ok(/Test · only you/.test(card),'card pill');
// force the test student onto today's weekday, then Today must still not list it
await p.evaluate((d)=>{const s=window.__DB.students.find(x=>x.name==='Test (me)');s.lesson_day=d;},today);
await p.reload();await p.waitForTimeout(3000);
const rows=await p.$$eval('[data-lesson-row]',es=>es.map(e=>e.textContent));ok(!rows.some(r=>/Test/.test(r)),'not on Today');
const chips=await p.$$eval('[data-testid=name-chip]',es=>es.map(e=>e.textContent));ok(chips.some(c=>/Testtest/.test(c)),'chip in everyone '+chips);
await p.click('button.pb-tab:has-text("Schedule")');await p.waitForTimeout(600);ok(!/Test \(me\)/.test(await p.textContent('main')),'not on Schedule');
ok(errs.length===0,'errors '+errs);
// drills picker
const c=await b.newContext({viewport:{width:430,height:900}});await c.addInitScript(()=>{localStorage.setItem('sb-icefqxaccclwasnfzgnp-auth-token',JSON.stringify({access_token:'t',expires_at:Math.floor(Date.now()/1000)+3600,user:{id:'u1'}}));});
await c.route(/supabase\.co\/rest\/v1\/students/,r=>r.fulfill({json:[{id:1,name:'Mia Kim',lesson_day:today,lesson_time:'15:30'},{id:9,name:'Test (me)',lesson_day:today,lesson_time:'00:00',extra:'{"test":true}'}]}));
await c.route(/supabase\.co\/rest\/v1\/lesson_sessions/,r=>r.request().method()==='GET'?r.fulfill({json:[]}):r.fulfill({status:201,body:''}));
await c.route(/cdnjs\.cloudflare\.com.*react-dom/,r=>r.fulfill({body:fs.readFileSync('/tmp/da/node_modules/react-dom/umd/react-dom.production.min.js'),contentType:'application/javascript'}));
await c.route(/cdnjs\.cloudflare\.com.*\/react\//,r=>r.fulfill({body:fs.readFileSync('/tmp/da/node_modules/react/umd/react.production.min.js'),contentType:'application/javascript'}));
await c.route(/googletagmanager|fonts\.g/,r=>r.abort());
const q=await c.newPage();q.on('pageerror',e=>errs.push(e.message));await q.goto('http://localhost:8855/drills.html?teacher=1');await q.waitForTimeout(3500);
await q.click('[data-testid=tpick-open]');await q.waitForTimeout(700);
const names=await q.$$eval('[data-testid=tpick-name]',es=>es.map(e=>e.textContent));ok(names.join()==='Mia15:30','real names only '+names);
ok(await q.isVisible('[data-testid=tpick-test]'),'test chip');await q.screenshot({path:'pick-test.png'});
await q.click('[data-testid=tpick-test]');await q.waitForTimeout(800);ok(/Lesson with Me/.test(await q.textContent('[data-testid=lesson-bar]')),'bar Me');
ok(errs.length===0,'errors '+errs);await b.close();console.log('pass',pass,'fail',fail)})();
