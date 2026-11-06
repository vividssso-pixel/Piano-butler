#!/usr/bin/env node
// Phase 424: the Victorian music room, for real (chapters 1-5 and every book that shares the parts).
// Sohyun 2026-10-10: wainscoting and chess; navy, coral and green only, pink only for Clara, no beige; the royal family
// as chess pieces; the fox butler, in his portrait only, with a coral bow tie.
//   node patch424.js <drills.src.html> <dir with vic424.gen.jsx and vic424.jsx>
const fs = require('fs'), path = require('path');
const parser = require(path.resolve(__dirname, '../node_modules/@babel/parser'));
const [srcFile, dir] = [process.argv[2], process.argv[3] || __dirname];
let h = fs.readFileSync(srcFile, 'utf8');
const OPEN = '<script id="app-jsx" type="text/jsx-raw">';
const bi = h.indexOf(OPEN) + OPEN.length, bj = h.indexOf('</script>', bi);
let src = h.slice(bi, bj);
const rep = (a, b, what, n = 1) => { const c = src.split(a).length - 1; if (c !== n) throw new Error(what + ': expected ' + n + ', got ' + c); src = src.split(a).join(b); };
const repH = (a, b, what, n = 1) => { const c = h.split(a).length - 1; if (c !== n) throw new Error(what + ': expected ' + n + ', got ' + c); h = h.split(a).join(b); };

// 1. the old parts go (their new versions come in one block below)
const OLD = ['LbPage', 'WbPage', 'LbPic', 'LbRemember', 'LbTick', 'LbPiano', 'LbStageIcon', 'LbStageRows', 'BkTag', 'Faces', 'BkCell', 'ExCell', 'WbTop', 'TcBlock', 'sfQueen', 'sfKing', 'sfClara'];
{
  const ast = parser.parse(src, { sourceType: 'script', plugins: ['jsx'] });
  const found = {};
  for (const n of ast.program.body) if (n.type === 'FunctionDeclaration' && OLD.includes(n.id.name)) (found[n.id.name] = found[n.id.name] || []).push([n.start, n.end]);
  for (const k of OLD) if (!found[k] || found[k].length !== 1) throw new Error('declaration ' + k + ': ' + (found[k] || []).length);
  const ranges = OLD.map(k => found[k][0]).sort((a, b) => b[0] - a[0]);
  for (const [a, b] of ranges) { let e = b; if (src[e] === '\n') e++; src = src.slice(0, a) + src.slice(e); }
}
for (const c of ['// the printed five checks: three boxes in each row\n', '// One fixed A4 page. Header: book + chapter; footer: page number.\n', '// Three faces to circle: how did this page feel?\n',
  '// One fixed A4 page of the Lesson Book.\n', '// the picture box takes whatever height the page has left, so every page ends level (it shrinks back to h when printed inside page margins)\n',
  '// an "At the piano" tick box: printed, an empty box; on screen, a box the student can tick\n',
  '// The strip at the top of every lesson page: which step, the code straight to that step online, the drill line.\n',
  '// Sohyun 2026-10-09 (Phase 393): no Set / Due / minutes / drill line -- just which step this is, and its code\n'])
  rep(c, '', 'comment ' + c.slice(0, 40));
{ const i = src.indexOf('// Phase 420: the royals are signs, like chess pieces'); const j = src.indexOf('\n', src.indexOf('\n', i) + 1) + 1; if (i < 0) throw new Error('420 comment'); src = src.slice(0, i) + src.slice(j); }

// 2. the new parts
const add = fs.readFileSync(path.join(dir, 'vic424.gen.jsx'), 'utf8') + fs.readFileSync(path.join(dir, 'vic424.jsx'), 'utf8');
rep('const LESSON_BOOKS = {', add + '\nconst LESSON_BOOKS = {', 'insert');
rep('const LB_CSS = PB_KID_CSS + `', 'const LB_CSS = PB_KID_CSS + VIC_CSS + `', 'LB_CSS');

// 3. the palette: white paper, green for the check, hairlines
rep("const BK = { ink: '#26296b', coral: '#e4572e', muted: '#6d6f9c', line: '#d9d3c4', soft: '#faf6ec',",
    "const BK = { ink: '#26296b', coral: '#e4572e', muted: '#6d6f9c', line: '#d9d3c4', soft: '#ffffff', green: '#2b6e56', greenSoft: '#e2efe9', hair: 'rgba(38,41,107,0.28)', ink2: 'rgba(38,41,107,0.55)',", 'BK');

// 4. small parts
rep(`? <div style={{border:'1.6px dashed ' + BK.coral,borderRadius:12,padding:'9px 14px 10px',margin:'10px 0 0',`, `? <div style={{...VIC_PANEL,padding:'10px 16px 10px',margin:'10px 0 0',`, 'PLAY panel');
rep(`      <span style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:18.5,fontWeight:800,color:BK.ink,lineHeight:1.15}}>{title}</span>`,
    `      <span style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:19,fontWeight:800,color:BK.ink,lineHeight:1.15}}>{title}</span>`, 'part title');
rep(`const bkTick = (s = 18) => <span style={{display:'inline-block',width:s,height:s,border:'1.5px solid ' + BK.ink,borderRadius:4,`,
    `const bkTick = (s = 18) => <span style={{display:'inline-block',width:s,height:s,border:'1.5px solid ' + BK.green,borderRadius:2,`, 'bkTick');
rep(`const bkSec = (letter, title) => <div style={{display:'flex',alignItems:'baseline',gap:8,margin:'9px 0 4px'}}><span style={{fontSize:13,fontWeight:900,color:BK.coral}}>{letter}</span>`,
    `const bkSec = (letter, title) => <div style={{display:'flex',alignItems:'center',gap:9,margin:'7px 0 3px'}}><span style={{flex:'0 0 18px',height:18,display:'flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:12.5,fontWeight:800,lineHeight:1,...vicSquare(letter.charCodeAt(0) - 65)}}>{letter}</span>`, 'bkSec');
rep(`<span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',fontSize:11,fontWeight:900,color:BK.coral,whiteSpace:'nowrap'}}>{it.ex ? 'e.g.' : it.n}</span>`,
    `<span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',fontFamily:LB_SERIF,fontStyle:'italic',fontSize:13,fontWeight:700,fontVariantNumeric:'lining-nums',color:it.ex ? BK.coral : BK.ink,whiteSpace:'nowrap'}}>{it.ex ? 'e.g.' : it.n}</span>`, 'SfRow numbers');
rep(`border:'1.5px solid ' + (it.ex ? BK.coral : BK.ink),borderRadius:7,`, `border:'1.5px solid ' + (it.ex ? BK.coral : BK.ink),borderRadius:3,`, 'SfRow box');
rep(`<span style={{color:BK.muted}}>{i + 1}.</span> <b>{a}</b></span>`, `<span style={{color:BK.muted}}>{i + 1}.</span> <b style={{color:BK.green}}>{a}</b></span>`, 'tcAns green');
rep(`style={{height:34,border:'1.5px solid ' + (on ? BK.coral : BK.line),borderRadius:17,background:on ? '#fdeee8' : '#fff',display:'flex',alignItems:'center',gap:4,padding:'0 9px',fontSize:11.5,fontWeight:800,color:on ? BK.coral : BK.muted,cursor:'pointer'}}>`,
    `style={{height:34,border:'1.5px solid ' + (on ? BK.green : BK.line),borderRadius:17,background:on ? BK.greenSoft : '#fff',display:'flex',alignItems:'center',gap:4,padding:'0 9px',fontSize:11.5,fontWeight:800,color:on ? BK.green : BK.muted,cursor:'pointer'}}>`, 'five checks app');
rep(`const bkBox = (w = 44, h = 26) => <span style={{display:'inline-block',width:w,height:h,border:'1.5px solid ' + BK.line,borderRadius:6,`,
    `const bkBox = (w = 44, h = 26) => <span style={{display:'inline-block',width:w,height:h,border:'1.5px solid ' + BK.line,borderRadius:3,`, 'bkBox');
rep(`width:w,height:h,border:'1.5px solid ' + BK.coral,borderRadius:6,background:'#fff',color:BK.coral`, `width:w,height:h,border:'1.5px solid ' + BK.coral,borderRadius:3,background:'#fff',color:BK.coral`, 'bkHand');
rep(`<div style={{padding:4,border:'1.5px solid ' + BK.line,borderRadius:8,background:'#fff',lineHeight:0}}><QR url={bkLink('drill=' + id`,
    `<div style={{padding:4,border:'0.8px solid ' + BK.hair,borderRadius:2,background:'#fff',lineHeight:0}}><QR url={bkLink('drill=' + id`, 'QR strip');
rep(`  return <div style={{display:'flex',alignItems:'baseline',justifyContent:'space-between',gap:10,borderTop:'1.6px solid ' + BK.ink,paddingTop:6,flexWrap:'wrap'}}>
    <span style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,color:BK.ink}}>On paper</span>`,
    `  return <div style={{display:'flex',alignItems:'baseline',justifyContent:'space-between',gap:10,paddingTop:2,flexWrap:'wrap'}}>
    <span style={{fontFamily:LB_SERIF,fontSize:22,fontWeight:800,color:BK.ink}}>On paper</span>`, 'paper head');
rep(`    <div style={{border:'1.6px dashed ' + BK.coral,borderRadius:14,padding:'8px 14px 10px',display:'flex',alignItems:'center',gap:14}}>`,
    `    <div style={{...VIC_PANEL,padding:'8px 15px 9px',display:'flex',alignItems:'center',gap:14}}>`, 'LbTune panel');

// 5. the chapter openers: one contents style in every chapter (a number with dotted leaders; green tick boxes)
rep(`      <div style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>`, `      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>`, 'toc grid', 5);
rep(`<div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>In this chapter</div>`, `<div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>In this chapter</div>`, 'toc h1', 5);
rep(`<div style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>`, `<div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>`, 'toc h2', 5);
rep(`.map(([n, p]) => <div key={p} style={{display:'flex',justifyContent:'space-between',alignItems:'center',`, `.map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',`, 'toc rows', 5);
rep(`<span style={{color:BK.muted,fontWeight:700}}>page {p}</span></div>)}`, `<span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}`, 'toc ch1 page');
rep(`<b>{'page ' + p}</b></div>)}`, `<span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}`, 'toc page', 3);
rep(`map((x, i) => <div key={i} style={{display:'flex',gap:8,fontSize:14.5,padding:'4px 0'}}><span style={{color:BK.coral,fontWeight:900}}>✓</span><span>{x}</span></div>)}`,
    `map((x, i) => <div key={i} style={{display:'flex',gap:9,alignItems:'flex-start',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid #ece6d8'}}><span style={{flex:'0 0 auto',marginTop:2}}>{bkTick(15)}</span><span>{x}</span></div>)}`, 'goals ticks', 3);
rep(`<span style={{flex:'0 0 16px',height:16,border:'1.6px solid ' + BK.ink,borderRadius:4,marginTop:3}}/><span>{x}</span></div>)}`,
    `<span style={{flex:'0 0 auto',marginTop:3}}>{bkTick(15)}</span><span>{x}</span></div>)}`, 'goals ch1');

// 6. the butler in his portrait only: at the chapter map's front door and on the print cover
rep(`  const rab = (PB_ART.rabbit || '').replace(/^<svg[^>]*>|<\\/svg>$/g, '');
  if (wide) s.push({ k: 'raw', svg: '<g transform="translate(4 ' + pFix(gy - 210 * 0.6) + ') scale(0.6)">' + rab + '</g>' },
    penText(58, gy + 18, t('Your butler', '버틀러가'), { size: 11.5, weight: 700, fill: PEN_N, anchor: 'middle', serif: true, italic: true }),
    penText(58, gy + 32, t('opens the door', '문을 열어 줘요'), { size: 11.5, weight: 700, fill: PEN_N, anchor: 'middle', serif: true, italic: true }));
  else s.push({ k: 'raw', svg: '<g transform="translate(8 ' + pFix(gy + 4) + ') scale(0.34)">' + rab + '</g>' },
    penText(70, gy + 34, t('Your butler opens the door.', '버틀러가 문을 열어 줘요.'), { size: 12, weight: 700, fill: PEN_N, serif: true, italic: true }),`,
    `  // Phase 424: the fox butler's portrait hangs by the front door (he appears only in his portrait)
  const cam = (x, y, hh) => ({ k: 'raw', svg: '<image href="' + VIC_CAMEO + '" x="' + pFix(x) + '" y="' + pFix(y) + '" height="' + pFix(hh) + '" width="' + pFix(hh * 184 / 232) + '"/>' });
  if (wide) s.push(cam(14, gy - 116, 108),
    penText(58, gy + 18, t('Your butler', '버틀러가'), { size: 11.5, weight: 700, fill: PEN_N, anchor: 'middle', serif: true, italic: true }),
    penText(58, gy + 32, t('welcomes you', '반겨 줘요'), { size: 11.5, weight: 700, fill: PEN_N, anchor: 'middle', serif: true, italic: true }));
  else s.push(cam(12, gy + 6, 64),
    penText(70, gy + 34, t('Your butler welcomes you.', '버틀러가 반겨 줘요.'), { size: 12, weight: 700, fill: PEN_N, serif: true, italic: true }),`, 'house map butler');
rep(`{SPREAD_SCENES[id] ? SPREAD_SCENES[id]() : <PbArt name="rabbit" h={300}/>}`, `{SPREAD_SCENES[id] ? SPREAD_SCENES[id]() : <img src={VIC_CAMEO} alt="" style={{height:300,width:'auto'}}/>}`, 'spread cover');

h = h.slice(0, bi) + src + h.slice(bj);
// 7. Playfair italic and the lighter weights
repH('family=Playfair+Display:wght@800;900', 'family=Playfair+Display:ital,wght@0,700;0,800;0,900;1,600;1,700;1,800', 'font link');
fs.writeFileSync(srcFile, h); console.log('patch424 ok');
