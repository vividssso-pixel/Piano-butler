// Render a book HTML (self-paginating) to an A4 PDF, waiting for its fit pass.
const {chromium}=require('playwright');(async()=>{const [src,out]=process.argv.slice(2);const b=await chromium.launch();const p=await b.newPage({viewport:{width:900,height:1200}});
await p.goto('file://'+src);try{await p.waitForFunction(()=>document.body.dataset.fit,null,{timeout:120000});}catch(e){await p.waitForTimeout(3000);}
await p.evaluate(()=>document.fonts.ready);await p.pdf({path:out,format:'A4',printBackground:true,preferCSSPageSize:true});await b.close();})();
