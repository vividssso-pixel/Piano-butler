#!/usr/bin/env node
// Phase 425: the map is a street (Sohyun 2026-10-10: B, the street of Victorian buildings, with C, "Clara's journey"
// on a chessboard, to see where you are; lines only, classical shapes). Run after patch424.
//   node patch425.js <drills.src.html> <dir with street425.jsx>
const fs = require('fs'), path = require('path');
const parser = require(path.resolve(__dirname, '../node_modules/@babel/parser'));
const [srcFile, dir] = [process.argv[2], process.argv[3] || __dirname];
let h = fs.readFileSync(srcFile, 'utf8');
const OPEN = '<script id="app-jsx" type="text/jsx-raw">';
const bi = h.indexOf(OPEN) + OPEN.length, bj = h.indexOf('</script>', bi);
let src = h.slice(bi, bj);
const rep = (a, b, what, n = 1) => { const c = src.split(a).length - 1; if (c !== n) throw new Error(what + ': expected ' + n + ', got ' + c); src = src.split(a).join(b); };

// 1. the house goes: its drawing, its map, its book versions, the stairs and the siblings' pose
const OLD = ['houseShapes', 'HouseMap', 'houseMiniShapes', 'BkHouse', 'BkHousePage', 'houseStairs', 'HOUSE_STAND'];
{
  const ast = parser.parse(src, { sourceType: 'script', plugins: ['jsx'] });
  const found = {};
  for (const n of ast.program.body) {
    const name = n.type === 'FunctionDeclaration' ? n.id.name : n.type === 'VariableDeclaration' && n.declarations.length === 1 ? n.declarations[0].id.name : null;
    if (OLD.includes(name)) (found[name] = found[name] || []).push([n.start, n.end]);
  }
  for (const k of OLD) if (!found[k] || found[k].length !== 1) throw new Error('declaration ' + k + ': ' + (found[k] || []).length);
  const ranges = OLD.map(k => found[k][0]).sort((a, b) => b[0] - a[0]);
  for (const [a, b] of ranges) { let e = b; if (src[e] === '\n') e++; src = src.slice(0, a) + src.slice(e); }
}
rep(`// ─── Phase 377: the Piano Butler's House, the chapter map (Sohyun 2026-10-08: "the whole dollhouse") ───
// Every floor is a stage, every room is a chapter, in the map's order from the front door to the attic. The siblings
// stand on the stairs of the floor you are on; your room is tinted coral; a finished room has its number filled in.
// Drawn in the Lesson Book's pen and ink (pen376.js). Two drawings of the same house: phones get a tall house with
// the rooms of a floor in rows of up to three; wider screens get one row of rooms per floor and the butler outside.
`, `// Phase 377's house (the chapter map) became a street in Phase 425 (below, before MusicMap); the room pictures stay.
`, 'house comment');
rep(`// ─── Phase 378: the house in the books ───
// A small house (one line per floor, every room with its number and short name, your chapter's room in coral) takes
// the place of "The whole path" list; the Workbook's opening pages get the whole house to colour in, a room per chapter.
`, '', 'books house comment');
rep(`// the whole house to colour in (the Workbook's opening pages)
`, '', 'colour-in comment');

// 2. the street
rep('function MusicMap({', fs.readFileSync(path.join(dir, 'street425.jsx'), 'utf8') + '\nfunction MusicMap({', 'insert');

// 3. the words; a ticked lesson step marks today as a practice day (the week board)
rep("function saveDone(v) { try { localStorage.setItem(LESSON_KEY, JSON.stringify(v)); } catch (e) {} }", "function saveDone(v) { try { localStorage.setItem(LESSON_KEY, JSON.stringify(v)); } catch (e) {} pbMarkDay(); }", 'practice day');
rep(`text={t('The Piano Butler’s house: every floor is a stage, every room is a chapter, from the front door up to the attic. Tap a room to open it, or carry on with the button.', '피아노 버틀러의 집: 층마다 단계 하나, 방마다 챕터 하나, 현관에서 다락까지. 방을 누르거나, 버튼을 눌러 이어서 해요.')}`,
    `text={t('The Piano Butler’s house: every floor is a stage, every room is a chapter. Your butler meets you in the hall -- open the door and go up, floor by floor. New to the piano? Start on the first floor. Already playing? Go straight to any room, or carry on with the button.', '피아노 버틀러의 집: 층마다 단계 하나, 방마다 챕터 하나. 버틀러가 현관에서 맞아 줘요 -- 문을 열고 한 층씩 올라가요. 처음이라면 1층부터, 이미 배우고 있다면 어느 방으로든 바로 가거나 버튼을 눌러 이어서 해요.')}`, 'MapHome words');

// 3b. the house's classical letters (her 17:22): Cinzel for the floors, Cormorant Garamond for the rooms; rdWidth can measure them
rep(`rdCtx.font = weight + ' ' + size + 'px ' + (serif ? "'Playfair Display', Georgia, serif" : "Inter, 'Pretendard', sans-serif");`, `rdCtx.font = weight + ' ' + size + 'px ' + (typeof serif === 'string' ? serif : serif ? "'Playfair Display', Georgia, serif" : "Inter, 'Pretendard', sans-serif");`, 'rdWidth fonts');

// 4. the fresh-eyes review (2026-10-10)
// the rabbit leaves chapter 1's pictures: the butler is a fox now, and only in his portrait
{
  const { fixPuppet, fixMirror } = require(path.resolve(dir, 'art', 'fixart.js'));
  for (const [key, fn] of [['puppet', fixPuppet], ['mirror', fixMirror]]) {
    const m = new RegExp('^"' + key + '": (".*?"),?$', 'm').exec(src); if (!m) throw new Error('art ' + key);
    src = src.slice(0, m.index) + '"' + key + '": ' + JSON.stringify(fn(JSON.parse(m[1]))) + src.slice(m.index + 3 + key.length + 1 + m[1].length);
  }
}
// a section with two letters gets two chess squares
rep(`const bkSec = (letter, title) => <div style={{display:'flex',alignItems:'center',gap:9,margin:'7px 0 3px'}}><span style={{flex:'0 0 18px',height:18,display:'flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:12.5,fontWeight:800,lineHeight:1,...vicSquare(letter.charCodeAt(0) - 65)}}>{letter}</span>`,
    `const bkSec = (letter, title) => <div style={{display:'flex',alignItems:'center',gap:9,margin:'7px 0 3px'}}><span style={{display:'flex',gap:3,flex:'0 0 auto'}}>{letter.split(' · ').map(L => <span key={L} style={{width:18,height:18,display:'flex',alignItems:'center',justifyContent:'center',fontFamily:LB_SERIF,fontSize:12.5,fontWeight:800,lineHeight:1,...vicSquare(L.charCodeAt(0) - 65)}}>{L}</span>)}</span>`, 'bkSec two letters');
// pictures that crossed their frame's inner line (chapter 2 page 2, chapter 1 page 6)
rep(`<LbPic h={190}><div style={{width:'100%',maxWidth:420,margin:'0 auto'}}><PenArt shapes={art2}`, `<LbPic h={190}><div style={{width:'100%',maxWidth:330,margin:'0 auto'}}><PenArt shapes={art2}`, 'ch2 p2 picture 1');
rep(`<LbPic h={150} pad="10px 12px"><div style={{width:'100%'}}><PenArt shapes={art2b}`, `<LbPic h={150} pad="10px 12px"><div style={{width:'100%',maxWidth:500,margin:'0 auto'}}><PenArt shapes={art2b}`, 'ch2 p2 picture 2');
rep(`<LbPic h={164} gap={48} pad="6px 18px">
          <LbFig art="keys-hand-L" h={152}/>
          <LbFig art="keys-hand-R" h={152}/>`, `<LbPic h={164} gap={48} pad="8px 18px">
          <LbFig art="keys-hand-L" h={146}/>
          <LbFig art="keys-hand-R" h={146}/>`, 'ch1 p6 picture');
// the wrist's word clears the piano
rep(`s.push(...lab(p.wr[0] + 5, wy, [p.wr[0] + 4.5, wy - 1.5], [p.wr[0] + 2, p.wr[1] - 6], t('wrist', '손목'), undefined, wrOk ? PEN_G : PEN_C));`,
    `s.push(...lab(p.wr[0] + 1, wy, [p.wr[0] + 1.5, wy - 1.5], [p.wr[0] + 1, p.wr[1] - 6], t('wrist', '손목'), undefined, wrOk ? PEN_G : PEN_C));`, 'wrist label');
// chapter 4 page 6: the two words sit off the staff lines and clear of the dotted paths (the text says "just under / just over")
rep(`      <text x="104" y={yOf(28, 'treble') - 12} fontSize="9" fontWeight="900" fill={BK.ink} textAnchor="middle">{t('visiting the Queen', '여왕네 갈 때')}</text>
      <text x="104" y={yOf(28, 'treble') + 20} fontSize="8" fontWeight="800" fill={BK.muted} textAnchor="middle">{t('just under her staff', '여왕의 오선 바로 아래')}</text>
      <text x="266" y={yOf(28, 'bass') - 16} fontSize="8" fontWeight="800" fill={BK.muted} textAnchor="middle">{t('just over his staff', '왕의 오선 바로 위')}</text>
      <text x="266" y={yOf(28, 'bass') + 21} fontSize="9" fontWeight="900" fill={BK.ink} textAnchor="middle">{t('visiting the King', '왕네 갈 때')}</text>`,
`      <text x="110" y={yOf(28, 'treble') + 19} fontSize="9" fontWeight="900" fill={BK.ink} textAnchor="end">{t('visiting the Queen', '여왕네 갈 때')}</text>
      <text x="262" y={yOf(28, 'bass') - 14} fontSize="9" fontWeight="900" fill={BK.ink} textAnchor="start">{t('visiting the King', '왕네 갈 때')}</text>`, 'ch4 p6 labels');
// a run of note letters never breaks
rep(`Clara to the Queen: C D E F G.', '소용돌이는 G를 감싸요: 여왕의 줄. 공주에서 여왕까지: C D E F G.')`, `Clara to the Queen: C D E F G.', '소용돌이는 G를 감싸요: 여왕의 줄. 공주에서 여왕까지: C D E F G.')`, 'nbsp CDEFG');
rep(`The King to Clara: F G A B C.', '두 점은 F를 지켜요: 왕의 줄. 왕에서 공주까지: F G A B C.')`, `The King to Clara: F G A B C.', '두 점은 F를 지켜요: 왕의 줄. 왕에서 공주까지: F G A B C.')`, 'nbsp FGABC');
// the pictures' words for screen readers follow the pictures: chess pieces, no rabbit
rep(`label={t('The piano: the King\\'s crown at the low end, the Queen\\'s crown at the high end, and Princess Clara\\'s tiara in the middle, on middle C', '피아노: 낮은 쪽 끝에 왕의 왕관, 높은 쪽 끝에 여왕의 왕관, 그리고 한가운데, 가운데 도 위에 클라라 공주의 티아라')`,
    `label={t('The piano: the King, a navy chess king, at the low end, the Queen, a coral chess queen, at the high end, and Princess Clara, a pink pawn with a tiara, in the middle, on middle C', '피아노: 낮은 쪽 끝에 남색 체스 킹(왕), 높은 쪽 끝에 코랄색 체스 퀸(여왕), 그리고 한가운데, 가운데 도 위에 티아라를 쓴 분홍 폰 클라라 공주')`, 'label staff hero');
rep(`with the Queen\\'s crown beside it; KINGSLAND is the bottom staff, with the King\\'s crown beside it; Princess Clara\\'s tiara between them', '큰보표는 두 나라의 지도: 위 오선은 퀸즈랜드, 옆에 여왕의 왕관; 아래 오선은 킹스랜드, 옆에 왕의 왕관; 그 사이에 클라라 공주의 티아라')`,
    `with the Queen\\'s chess piece beside it; KINGSLAND is the bottom staff, with the King\\'s chess piece beside it; Princess Clara, a pink pawn, between them', '큰보표는 두 나라의 지도: 위 오선은 퀸즈랜드, 옆에 여왕의 체스 말; 아래 오선은 킹스랜드, 옆에 왕의 체스 말; 그 사이에 분홍 폰 클라라 공주')`, 'label ch5 lands');
rep(`All Cows Eat Grass, with the King\\'s crown beside them', '킹스랜드의 네 칸, 아래에서부터: A C E G -- All Cows Eat Grass, 옆에 왕의 왕관')`,
    `All Cows Eat Grass, with the King\\'s chess piece beside them', '킹스랜드의 네 칸, 아래에서부터: A C E G -- All Cows Eat Grass, 옆에 왕의 체스 말')`, 'label ch5 ACEG');
rep(`label="The rabbit butler stands on the ground between a small house of keys and a big house; the sea and a turtle at the low end, clouds and a bird at the high end"`,
    `label="A small house of keys and a big house on the ground; the sea and a turtle at the low end, clouds and a bird at the high end"`, 'label ch2 cover');
// no beige in the books: hairlines and ground lines in navy (Sohyun 2026-10-10: "베이지 빼고 그냥 웨인스코팅 선만")
{
  src = src.split('#bdb7a6').join('rgba(38,41,107,0.4)');   // the ground under every drawing
  const a = src.indexOf("const BK = { ink: '#26296b'"), b = src.indexOf('// ─── Phase 373: the Lesson Book and the Workbook side by side');
  if (a < 0 || b < a) throw new Error('book range');
  let book = src.slice(a, b);
  for (const [cols, to] of [[['#ece6d8', '#f1ece0', '#e6dfcf'], 'rgba(38,41,107,0.16)'], [['#e9e2d2', '#e9e3d4', '#e2dccb'], 'rgba(38,41,107,0.22)'], [['#d9d3c4'], 'rgba(38,41,107,0.3)'], [['#c9c0aa', '#c9c3b2', '#ddd7c6'], 'rgba(38,41,107,0.35)']])
    for (const c of cols) book = book.split(c).join(to);
  src = src.slice(0, a) + book + src.slice(b);
}

h = h.slice(0, bi) + src + h.slice(bj);
if (h.split('&family=Press+Start+2P').length !== 2) throw new Error('fonts link');   // the house's classical letters (3b)
h = h.replace('&family=Press+Start+2P', '&family=Cinzel:wght@600;700&family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600;1,700&family=Press+Start+2P');
fs.writeFileSync(srcFile, h);
console.log('patch425 ok');
