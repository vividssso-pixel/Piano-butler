const {chromium}=require('playwright');const fs=require('fs');let pass=0,fail=0;const ok=(c,m)=>{if(c)pass++;else{fail++;console.log('FAIL',m)}};
const today=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'][new Date().getDay()];
const STUD=[{id:1,name:'Mia Kim',lesson_day:today,lesson_time:'15:30',extra:null},{id:2,name:'Leo Park',lesson_day:today,lesson_time:'16:30',extra:null},{id:3,name:'Ava Chen',lesson_day:'Tuesday',lesson_time:'17:00',extra:null},{id:4,name:'Noah Lee',lesson_day:'Wednesday',extra:'{"paused":true}'}];
async function run(b,expired){let STORE=null,refreshed=0,auth=[];const c=await b.newContext({viewport:{width:430,height:900}});
 await c.addInitScript((exp)=>{try{localStorage.setItem('sb-icefqxaccclwasnfzgnp-auth-token',JSON.stringify({access_token:'old',refresh_token:'r1',expires_at:Math.floor(Date.now()/1000)+(exp?-100:3600),user:{id:'u1'}}));}catch(e){}},expired);
 await c.route(/supabase\.co\/auth\/v1\/token/,r=>{refreshed++;return r.fulfill({json:{access_token:'new',refresh_token:'r2',expires_in:3600,user:{id:'u1'}}});});
 await c.route(/supabase\.co\/rest\/v1\/students/,r=>{auth.push(r.request().headers()['authorization']);return r.fulfill({json:STUD});});
 await c.route(/supabase\.co\/rest\/v1\/lesson_sessions/,async r=>{const m=r.request().method();if(m==='GET')return r.fulfill({json:STORE?[STORE]:[]});STORE={...(STORE||{}),...JSON.parse(r.request().postData())};return r.fulfill({status:201,body:''});});
 await c.route(/cdnjs\.cloudflare\.com.*react-dom/,r=>r.fulfill({body:fs.readFileSync('/tmp/da/node_modules/react-dom/umd/react-dom.production.min.js'),contentType:'application/javascript'}));
 await c.route(/cdnjs\.cloudflare\.com.*\/react\//,r=>r.fulfill({body:fs.readFileSync('/tmp/da/node_modules/react/umd/react.production.min.js'),contentType:'application/javascript'}));
 await c.route(/googletagmanager|fonts\.g/,r=>r.abort());
 const p=await c.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://localhost:8855/drills.html?teacher=1');await p.waitForTimeout(3500);
 ok(await p.isVisible('[data-testid=tpick]'),'picker shown');await p.click('[data-testid=tpick-open]');await p.waitForTimeout(800);
 const names=await p.$$eval('[data-testid=tpick-name]',es=>es.map(e=>e.textContent));ok(names.join()==='Mia15:30,Leo16:30,Ava','names '+names);
 if(expired){ok(refreshed>=1,'refreshed');ok(auth[0]==='Bearer new','used new token '+auth[0]);}
 await p.screenshot({path:'pick'+(expired?'-exp':'')+'.png'});
 await p.click('[data-testid=tpick-name]:has-text("Leo")');await p.waitForTimeout(1200);
 ok(await p.isVisible('[data-testid=lesson-bar]'),'bar after pick');ok(/Leo/.test(await p.textContent('[data-testid=lesson-bar]')),'bar names Leo');ok(!(await p.isVisible('[data-testid=tpick]')),'picker hidden in lesson');
 ok(STORE&&STORE.student_id==='2'&&STORE.name==='Leo','server row '+JSON.stringify(STORE));
 ok(errs.length===0,'errors '+errs);await c.close();}
(async()=>{const b=await chromium.launch();await run(b,false);await run(b,true);await b.close();console.log('pass',pass,'fail',fail)})();
