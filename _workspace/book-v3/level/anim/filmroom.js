const {chromium}=require('playwright'); const {spawn}=require('child_process');
(async()=>{const rid=process.argv[2];const b=await chromium.launch();const p=await b.newPage({viewport:{width:1280,height:720}});
await p.goto(`file:///tmp/claude-0/anim/rooms/${rid}.html`);await p.waitForTimeout(1500);
const dur=await p.evaluate(()=>TL.dur), fps=30, n=Math.ceil(dur*fps);
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate','30','-c:v','mjpeg','-i','-','-c:v','libx264','-crf','20','-preset','veryfast','-pix_fmt','yuv420p',`/tmp/claude-0/anim/rooms/${rid}_v.mp4`]);
for(let i=0;i<n;i++){ await p.evaluate(x=>setT(x), i/fps); const buf=await p.screenshot({type:'jpeg',quality:92}); if(!ff.stdin.write(buf)) await new Promise(r=>ff.stdin.once('drain',r)); }
ff.stdin.end(); await new Promise(r=>ff.on('close',r)); await b.close(); console.log('done',rid);})();
