// Snapshot each Handbook chapter's opening picture (her 6 Nov) for the workbook's Learn pages. Usage: node heroshot.js
const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:820,height:1160},deviceScaleFactor:3});const caps={};
for(const [f,part] of [['handbook-time2','T'],['handbook-pitch','P'],['handbook-scales','S'],['handbook-harmony','H'],['handbook-harmony2','M'],['handbook-expression','E'],['handbook-shape','F'],['handbook-play','L']]){
 await p.goto('file:///mnt/user-data/outputs/house-rooms/'+f+'.html');await p.waitForTimeout(1800);
 const secs=await p.$$('section.pg');
 for(const s of secs){const k=await s.evaluate(e=>{const m=/· (\d+)$/.exec((e.querySelector('.kick')||{}).textContent||'');return m&&e.querySelector('h1')?m[1]:null;});if(!k)continue;
  const key=part+k;
  const h=await s.$('.hero');let el,cap='';
  if(h){await h.evaluate(e=>{const c=e.querySelector('.hcap');if(c)c.style.display='none';});el=h;cap=await h.evaluate(e=>(e.querySelector('.hcap')||{}).textContent||'');}
  else{el=await s.$('.body > .two > div:first-child');}
  if(!el)continue;await el.screenshot({path:__dirname+'/heroes/'+key+'.png',omitBackground:false});caps[key]=cap;
  if(h)await h.evaluate(e=>{const c=e.querySelector('.hcap');if(c)c.style.display='';});}}
fs.writeFileSync(__dirname+'/heroes/caps.json',JSON.stringify(caps,null,1));console.log(Object.keys(caps).join(' '));await b.close();})()
