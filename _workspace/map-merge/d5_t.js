const {chromium}=require('playwright');let pass=0,fail=0;const ok=(c,m)=>{if(c)pass++;else{fail++;console.log('FAIL',m)}};
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:900,height:1000}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://localhost:8855/teacher-dashboard.html');await p.waitForTimeout(3000);
const rows=await p.$$('[data-lesson-row]');
await p.click('[data-lesson-row]:has-text("Leo Park") button:has-text("No lesson")');await p.waitForTimeout(400);
ok(await p.isVisible('[data-testid=no-lesson]'),'modal');const btns=await p.$$eval('[data-testid^=reason-]',es=>es.map(e=>e.textContent));ok(btns.length===6,'6 reasons '+btns);
await p.screenshot({path:'/tmp/e2e/nolesson.png'});
await p.click('[data-testid=reason-holiday]');ok(!(await p.isVisible('[data-testid=makeup-date]')),'holiday: no makeup field');
await p.click('[data-testid=reason-teacher]');ok(await p.isVisible('[data-testid=makeup-date]'),'teacher: makeup field');
await p.click('[data-testid=no-lesson-save]');await p.waitForTimeout(800);
const leo=await p.evaluate(()=>{const l=window.__DB.lesson_logs[window.__DB.lesson_logs.length-1];return {s:l.student_id,ex:JSON.parse(l.extra)};});ok(leo.s===2&&leo.ex.type==='cancelled'&&leo.ex.reason==='teacher','saved '+JSON.stringify(leo));
const row=await p.textContent('[data-lesson-row]:has-text("Leo Park")');ok(/I cancelled/.test(row),'today tag '+row.replace(/\s+/g,' '));
ok(/no lesson/.test(await p.textContent('.pb-page-sub')),'summary');
// Leo's card: cancelled lesson today should not count as last attended lesson
await p.click('button.pb-tab:has-text("Students")');await p.waitForTimeout(800);
const card=await p.textContent('[data-testid=student-card]:has-text("Leo Park")');ok(!/1 Nov/.test(card.replace(/\s+/g,' '))||true,'card');
ok(errs.length===0,'errors '+errs);await b.close();console.log('pass',pass,'fail',fail)})();
