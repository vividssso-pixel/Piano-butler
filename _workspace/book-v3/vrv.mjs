import createVerovioModule from 'verovio/wasm';
import { VerovioToolkit } from 'verovio/esm';
import fs from 'fs';
const M = await createVerovioModule(); const tk = new VerovioToolkit(M);
// mini language per bar: tokens like q q | c. q | m  ; beams with [ ] ; triplet {q q q}; tie ~ after note; r prefix = rest; count text after '/' e.g. c/1
const D = {b:'breve',s:'1',m:'2',c:'4',q:'8',x:'16'};
let id=0; let LOC=0; let TIES=[]; let pend=null;
function note(tok){
  if(tok==='R'){id++;return `<mRest xml:id="n${id}"/>`;}
  let [t,cnt]=tok.split('/'); let tie=''; if(t.endsWith('~')){tie='i';t=t.slice(0,-1);} let rest=false; if(t[0]==='r'){rest=true;t=t.slice(1);} let dots=0; while(t.endsWith('.')){dots++;t=t.slice(0,-1);}
  const syl=cnt?`<verse n="1"><syl>${cnt.replace(/_/g,' ')}</syl></verse>`:'';
  const d=D[t]; const dd=dots?` dots="${dots}"`:''; id++;
  if(!rest){ if(pend){TIES.push([pend,'n'+id]);pend=null;} if(tie) pend='n'+id; }
  if(rest) return `<rest xml:id="n${id}" dur="${d}"${dd}/>` + (cnt?'':'');
  return `<note xml:id="n${id}" dur="${d}"${dd} loc="${LOC}" stem.dir="up"${tie?` tie="${tie}"`:''}>${syl}</note>`;
}
function layer(bar){
  let out=''; const toks=bar.trim().split(/\s+/).filter(Boolean);
  for(let t of toks){
    if(t==='['){out+='<beam>';continue;} if(t===']'){out+='</beam>';continue;}
    if(t==='{'){out+='<tuplet num="3" numbase="2" num.visible="true" bracket.visible="false"><beam>';continue;} if(t==='}'){out+='</beam></tuplet>';continue;}
    if(t==='('){out+='<tuplet num="2" numbase="3" num.visible="true" bracket.visible="false"><beam>';continue;} if(t===')'){out+='</beam></tuplet>';continue;}
    if(t==='<'){out+='<tuplet num="3" numbase="2" num.visible="true" bracket.visible="true">';continue;} if(t==='>'){out+='</tuplet>';continue;}
    out+=note(t);
  }
  return out;
}
function mei(src, meter, lines=1){
  const bars=src.split('|'); let ms=''; let tiesOpen=[];
  bars.forEach((b,i)=>{ const before=TIES.length; const L=layer(b); ms+=`<measure n="${i+1}"${i===bars.length-1?' right="end"':''}><staff n="1"><layer n="1">${L}</layer></staff>__TIES${i}__</measure>`; });
  ms=ms.replace(/__TIES(\d+)__/g,'');
  const tieXml=TIES.map(([a,b])=>`<tie startid="#${a}" endid="#${b}"/>`).join('');
  if(tieXml){ ms=ms.replace(/<\/staff>/, '</staff>'+tieXml); }
  TIES=[]; pend=null;
  const m = meter? (meter==='C'?' meter.sym="common"':meter==='C|'?' meter.sym="cut"':` meter.count="${meter.split('/')[0]}" meter.unit="${meter.split('/')[1]}"`):'';
  return `<?xml version="1.0" encoding="UTF-8"?><mei xmlns="http://www.music-encoding.org/ns/mei" meiversion="5.0"><meiHead><fileDesc><titleStmt><title/></titleStmt><pubStmt/></fileDesc></meiHead><music><body><mdiv><score><scoreDef><staffGrp><staffDef n="1" lines="${lines}" clef.shape="perc" clef.line="1" clef.visible="false"${m}/></staffGrp></scoreDef><section>${ms}</section></score></mdiv></body></music></mei>`;
}
// ties: verovio needs <tie startid endid>; handle simple: note tie="i" next note tie="t" -> use attribute pairs
function fixTies(x){ return x.replace(/tie="i">([\s\S]*?)<\/note>([\s\S]*?)<note xml:id="(n\d+)"([^>]*)>/g,(a,inner,mid,nid,attrs)=>`tie="i">${inner}</note>${mid}<note xml:id="${nid}"${attrs} tie="t">`); }
const S = JSON.parse(fs.readFileSync(process.argv[2],'utf8')); const out={};
for (const [k,v] of Object.entries(S)) {
  tk.setOptions({ pageWidth: v.w||1400, adjustPageHeight: true, adjustPageWidth: true, scale: 50, header:'none', footer:'none', svgViewBox:true, pageMarginTop:10,pageMarginBottom:10,pageMarginLeft:10,pageMarginRight:30, breaks:'none', lyricSize:3.2, spacingLinear: v.sp||0.25, spacingNonLinear:0.6, font:'Leipzig' });
  LOC=(v.lines??1)===5?4:0; let x=(mei(v.src, v.meter||'', v.lines??1));
  tk.loadData(x); out[k]=tk.renderToSVG(1);
}
fs.writeFileSync(process.argv[3], JSON.stringify(out)); console.log(Object.keys(out).length);
