// ─── Phase 425-426: the chapter map ───
// Phase 425 made it a street of seven classical buildings; on 2026-10-10 (13:00-17:30) Sohyun took it through a
// village, a château garden and a street of two rows, and settled on the TOWNHOUSE ('좋다 이렇게 정하자', 17:30): one
// tall house cut open like a doll's house -- the hall with the butler's portrait and the front door at the foot, a floor
// for each stage, a room for each chapter, each floor dressed in its own wallpaper, floor and lamp; quoins, dentil
// cornices, panelled wainscot, a pedimented door and dormer, a mansard in chequered slates and two turrets, the King on
// the left and the Queen on the right. Classical letters: Cinzel for the floors, Cormorant Garamond for the rooms. The
// map opens on the hall; the door opens the house, which rises above the hall. Above it, the week board (the pawn's
// week). Lines only, navy on white; coral marks where you are and the lamps' flames, green what is done.
const ST = { N: '#26296b', C: '#e4572e', G: '#2b6e56', NEW: '#8a8cb0', M: '#6d6f9c', LW: 1.6, MW: 0.9, FW: 0.55, CW: 360, BX0: 28, BX1: 332 };
const ST_SANS = "Inter,'Pretendard',sans-serif", ST_SERIF = "'Playfair Display',Georgia,serif";
// the drawing's parts sit inside ST_G (white fill, navy line), so each part names only what differs
const ST_G = '<g fill="#fff" stroke="#26296b" stroke-linejoin="round">', stG = (svg) => ST_G + svg + '</g>';
const stL = (x1, y1, x2, y2, w = ST.MW) => '<line x1="' + pFix(x1) + '" y1="' + pFix(y1) + '" x2="' + pFix(x2) + '" y2="' + pFix(y2) + '" stroke-width="' + w + '"/>';
const stR = (x, y, w, h, sw = ST.MW, fill = '#fff') => '<rect x="' + pFix(x) + '" y="' + pFix(y) + '" width="' + pFix(w) + '" height="' + pFix(h) + '"' + (fill === '#fff' ? '' : ' fill="' + fill + '"') + ' stroke-width="' + sw + '"/>';
const stP = (d, sw = ST.MW, fill = '#fff') => '<path d="' + d + '"' + (fill === '#fff' ? '' : ' fill="' + fill + '"') + ' stroke-width="' + sw + '"/>';
const stD = (...a) => a.map(v => typeof v === 'number' ? pFix(v) : v).join(' ');   // a path's d: numbers rounded, letters kept
const stC = (cx, cy, r, sw = ST.MW, fill = '#fff') => '<circle cx="' + pFix(cx) + '" cy="' + pFix(cy) + '" r="' + pFix(r) + '"' + (fill === '#fff' ? '' : ' fill="' + fill + '"') + (fill === 'none' || fill === '#fff' ? '' : ' stroke="' + fill + '"') + ' stroke-width="' + sw + '"/>';
function stT(x, y, s, o = {}) {
  const st = (o.font ? 'font-family:' + o.font + ';' : o.serif ? 'font-family:' + ST_SERIF + ';font-variant-numeric:lining-nums;' : '') + (o.italic ? 'font-style:italic;' : '') + (o.ls ? 'letter-spacing:' + o.ls + ';' : '');
  return '<text x="' + pFix(x) + '" y="' + pFix(y) + '" font-size="' + (o.size || 11) + '" font-weight="' + (o.weight || 600) + '" fill="' + (o.fill || ST.N) + '" stroke="none" text-anchor="' + (o.anchor || 'start') + '" font-family="' + (o.font || ST_SANS) + '"' + (st ? ' style="' + st + '"' : '') + (o.op ? ' opacity="' + o.op + '"' : '') + '>' + penEsc(s) + '</text>';
}
function stQuoins(x, y0, y1, left) {   // the stepped corner stones, long and short in turn
  let s = '', y = y0, k = 0;
  while (y < y1 - 2) { const h = Math.min(9, y1 - y), w = k % 2 === 0 ? 12 : 8; s += stR(left ? x : x - w, y, w, h, ST.FW); y += h; k++; }
  return s;
}
const stPilaster = (x, y0, y1, w = 8) => stR(x - w / 2, y0 + 4, w, y1 - y0 - 8, ST.FW) + stR(x - w / 2 - 1.5, y0, w + 3, 4, ST.FW) + stR(x - w / 2 - 1.5, y1 - 4, w + 3, 4, ST.FW);
const stUrn = (x, y) => stP(stD('M', x - 3, y, 'L', x - 2, y - 2, 'C', x - 6, y - 4, x - 5, y - 10, x, y - 11, 'C', x + 5, y - 10, x + 6, y - 4, x + 2, y - 2, 'L', x + 3, y, 'Z'), ST.FW) + stC(x, y - 12.5, 1.4, 0, ST.N);
const stFinial = (x, y, h = 10) => stL(x, y, x, y - h) + stC(x, y - h - 1.5, 1.8, 0, ST.N) + stP(stD('M', x - 3, y - 3, 'l', 3, -4, 'l', 3, 4, 'Z'), ST.FW, ST.N);
const stPawn = (x, y, k) => '<g transform="translate(' + pFix(x) + ' ' + pFix(y) + ') scale(' + k + ')">' + VIC_PAWN + '</g>';
const stPiece = (svg, x, y, k) => '<g transform="translate(' + pFix(x) + ' ' + pFix(y) + ') scale(' + k + ')">' + svg + '</g>';
// a chess square with a number (dark when the number is odd); green when done
function stSquare(x, y, s, num, fill, size) {
  const dark = fill || (num % 2 === 1 ? ST.N : '#fff');
  return '<rect x="' + pFix(x) + '" y="' + pFix(y) + '" width="' + s + '" height="' + s + '" fill="' + dark + '" stroke="' + (fill || ST.N) + '" stroke-width="1.1"/>'
    + stT(x + s / 2, y + s * 0.72, String(num), { size: size || s * 0.62, weight: 800, fill: dark === '#fff' ? ST.N : '#fff', anchor: 'middle', serif: true });
}
// The week board (Sohyun 2026-10-10 14:22-14:30: the chessboard shows practice, not the map; "클라라는 디폴트 세팅이고 ...
// 학생이름으로 이야기를"; the goal is ours to propose): every day you practise, your pawn moves one square up the board --
// two on the week's first practice day, as a real pawn's first move may -- so five practice days take it from its
// starting square to the far side, where it becomes a queen. Last weeks stand beside it: a queen for a full week, a pawn
// otherwise. The pawn is Clara (pink) unless the device belongs to a student (their link's name; a navy pawn).
// A practice day: the "I practised today" tick (linked students), a drill played, or a lesson step ticked on this device.
const PRACTICE_DAYS_KEY = 'pb_practice_days_v1', WEEK_GOAL = 5;
const stWrap = (text, maxW, size, weight = 600) => { const out = []; let cur = ''; String(text).split(' ').forEach(w => { const nx = cur ? cur + ' ' + w : w; if (cur && rdWidth(nx, weight, size) > maxW) { out.push(cur); cur = w; } else cur = nx; }); if (cur) out.push(cur); return out; };
const VIC_PAWN_NAVY = "<g fill=\"#26296b\" stroke=\"#26296b\" stroke-width=\"0.8\" stroke-linejoin=\"round\"><path d=\"M-18 0 L18 0 C18.08 -0.23 18.37 -0.87 18.5 -1.4 C18.63 -1.93 18.88 -2.53 18.8 -3.2 C18.72 -3.87 18.47 -4.8 18 -5.4 C17.53 -6 16.57 -6.43 16 -6.8 C15.43 -7.17 14.73 -7.23 14.6 -7.6 C14.47 -7.97 15.2 -8.5 15.2 -9 C15.2 -9.5 15.03 -10.17 14.6 -10.6 C14.17 -11.03 13.27 -11.27 12.6 -11.6 C11.93 -11.93 11.2 -12.03 10.6 -12.6 C10 -13.17 9.45 -13.93 9 -15 C8.55 -16.07 8.2 -17.67 7.9 -19 C7.6 -20.33 7.32 -21.83 7.2 -23 C7.08 -24.17 6.8 -25.33 7.2 -26 C7.6 -26.67 8.8 -26.7 9.6 -27 C10.4 -27.3 11.52 -27.43 12 -27.8 C12.48 -28.17 12.52 -28.73 12.5 -29.2 C12.48 -29.67 12.52 -30.23 11.9 -30.6 C11.28 -30.97 9.65 -31.07 8.8 -31.4 C7.95 -31.73 7.17 -32.1 6.8 -32.6 C6.43 -33.1 6.63 -34.1 6.6 -34.4 L-6.6 -34.4 C-6.63 -34.1 -6.43 -33.1 -6.8 -32.6 C-7.17 -32.1 -7.95 -31.73 -8.8 -31.4 C-9.65 -31.07 -11.28 -30.97 -11.9 -30.6 C-12.52 -30.23 -12.48 -29.67 -12.5 -29.2 C-12.52 -28.73 -12.48 -28.17 -12 -27.8 C-11.52 -27.43 -10.4 -27.3 -9.6 -27 C-8.8 -26.7 -7.6 -26.67 -7.2 -26 C-6.8 -25.33 -7.08 -24.17 -7.2 -23 C-7.32 -21.83 -7.6 -20.33 -7.9 -19 C-8.2 -17.67 -8.55 -16.07 -9 -15 C-9.45 -13.93 -10 -13.17 -10.6 -12.6 C-11.2 -12.03 -11.93 -11.93 -12.6 -11.6 C-13.27 -11.27 -14.17 -11.03 -14.6 -10.6 C-15.03 -10.17 -15.2 -9.5 -15.2 -9 C-15.2 -8.5 -14.47 -7.97 -14.6 -7.6 C-14.73 -7.23 -15.43 -7.17 -16 -6.8 C-16.57 -6.43 -17.53 -6 -18 -5.4 C-18.47 -4.8 -18.72 -3.87 -18.8 -3.2 C-18.88 -2.53 -18.63 -1.93 -18.5 -1.4 C-18.37 -0.87 -18.08 -0.23 -18 0 Z\"/><circle cx=\"0\" cy=\"-41.6\" r=\"9.4\"/></g><g fill=\"none\" stroke=\"#fff\" stroke-opacity=\"0.55\" stroke-width=\"0.9\" stroke-linecap=\"round\"><path d=\"M-15.42 -2.8 Q0 -1.4 15.42 -2.8\"/><path d=\"M-11.97 -10.2 Q0 -8.8 11.97 -10.2\"/><path d=\"M-10.25 -28.8 Q0 -27.4 10.25 -28.8\"/><path d=\"M-3.6 -15 L-2.8 -24\"/></g>";
function pbMarkDay() { try { const a = JSON.parse(localStorage.getItem(PRACTICE_DAYS_KEY)) || [], d = localDay(); if (!a.includes(d)) { a.push(d); localStorage.setItem(PRACTICE_DAYS_KEY, JSON.stringify(a.slice(-400))); } } catch (e) {} }
function practiceDays() {
  const set = new Set();
  try { const c = JSON.parse(localStorage.getItem(TODAY_CACHE_KEY)); ((c && c.data && c.data.checkins) || []).forEach(x => set.add(String(x.day).slice(0, 10))); } catch (e) {}
  try { Object.values(loadRecords()).forEach(r => ((r && r.history) || []).forEach(h => { if (h && h.at) set.add(localDay(new Date(h.at))); })); } catch (e) {}
  try { (JSON.parse(localStorage.getItem(PRACTICE_DAYS_KEY)) || []).forEach(d => set.add(String(d).slice(0, 10))); } catch (e) {}
  return set;
}
const VIC_PAWN_WHITE = () => VIC_PAWN_NAVY.replace('fill="#26296b"', 'fill="#fff"').replace('stroke-width="0.8"', 'stroke-width="2.2"');   // a student's pawn on the board: white with a navy line, seen on every square
const weekRank = (n) => n <= 0 ? 1 : Math.min(7, 2 + n);   // rank index 1..7 (0-based ranks 0..7): start on the 2nd rank; the first day two squares
function weekSvg({ days, today, name }) {
  const SQ = 17, N = 8, bx = 16, by = 22, bw = N * SQ, file = 4, named = !!name;
  const dow = (dayDate(today).getDay() + 6) % 7, monday = dayPlus(today, -dow);
  const count = (mon) => [0, 1, 2, 3, 4, 5, 6].filter(i => days.has(dayPlus(mon, i)) && dayPlus(mon, i) <= today).length;
  const n = count(monday), rank = weekRank(n), queen = n >= WEEK_GOAL;
  let s = stR(bx - 6, by - 6, bw + 12, bw + 12, 1.6) + stR(bx - 3, by - 3, bw + 6, bw + 6, 0.55, 'none');
  for (let r = 0; r < N; r++) for (let c = 0; c < N; c++) {
    const dark = (r + c) % 2 === 0, x = bx + c * SQ, yy = by + (N - 1 - r) * SQ;   // a1 dark, as on a real board
    s += '<rect x="' + x + '" y="' + yy + '" width="' + SQ + '" height="' + SQ + '" fill="' + (dark ? ST.N : '#fff') + '" stroke="none"/>';
  }
  // the pawn's file: the squares it has passed this week, then the far side
  const fx = bx + file * SQ;
  for (let r = 1; r < rank; r++) { const yy = by + (N - 1 - r) * SQ; s += '<circle cx="' + (fx + SQ / 2) + '" cy="' + (yy + SQ / 2) + '" r="2.6" fill="' + ST.G + '" stroke="#fff" stroke-width="0.8"/>'; }
  s += '<rect x="' + (fx + 1) + '" y="' + (by + 1) + '" width="' + (SQ - 2) + '" height="' + (SQ - 2) + '" fill="none" stroke="' + ST.C + '" stroke-width="1.6" stroke-dasharray="2.5 2"/>';
  const py = by + (N - rank) * SQ - 2;
  s += queen ? stPiece(VIC_QUEEN, fx + SQ / 2, py, 0.25) : stPiece(named ? VIC_PAWN_WHITE() : VIC_PAWN, fx + SQ / 2, py, 0.3);
  // the words beside the board
  const tx = bx + bw + 22, who = name || 'Clara';
  s += stT(tx, 24, t(who + '’s week', who + '의 일주일'), { size: 18, weight: 800, serif: true, italic: LANG !== 'ko' });
  s += stT(tx, 50, t(n + (n === 1 ? ' practice day' : ' practice days') + ' this week', '이번 주 연습 ' + n + '일'), { size: 13.5, weight: 800, fill: queen ? ST.G : ST.N });
  s += stT(tx, 68, queen ? t('A queen this week!', '이번 주는 퀸!') : t((WEEK_GOAL - n) + ' more to become a queen', '퀸까지 ' + (WEEK_GOAL - n) + '일 더'), { size: 12, weight: 700, fill: queen ? ST.G : ST.C });
  stWrap(t('Each day you practise, the pawn moves up one square -- two on the first day, like a real pawn. At the far side it becomes a queen.', '연습한 날마다 폰이 한 칸 앞으로 -- 첫날은 진짜 폰처럼 두 칸. 끝줄에 닿으면 퀸이 돼요.'), 360 - tx - 8, 10.5).forEach((ln, i) => { s += stT(tx, 87 + i * 12.5, ln, { size: 10, weight: 600, fill: ST.M }); });
  // last weeks: a queen for a full week, a pawn for the rest (only weeks that had practice)
  const past = [];
  for (let w = 6; w >= 1; w--) { const mon = dayPlus(monday, -7 * w), c = count(mon); if (c > 0 || past.length) past.push(c); }
  if (past.length) {
    s += stT(tx, by + bw - 14, t('Last weeks', '지난 주들'), { size: 10, weight: 800, fill: ST.M, ls: '0.12em' });
    past.forEach((c, i) => { const x = tx + 8 + i * 22, yy = by + bw + 6; s += c >= WEEK_GOAL ? stPiece(VIC_QUEEN, x, yy, 0.2) : stPiece(VIC_PAWN_WHITE(), x, yy, 0.24); });
  }
  return { svg: stG(s), W: 360, H: by + bw + 16, n, rank, queen };
}

function stLantern(x, y, k = 1) {   // a garden lantern: a slim post with a scrolled bracket, a glazed lantern lit coral, a pointed cap
  const S = (v) => v * k;
  return stR(x - S(3), y - S(2.5), S(6), S(2.5), 0.8) + stR(x - S(1), y - S(25), S(2), S(22.5), 0.8)
    + stP(stD('M', x - S(1), y - S(18), 'q', S(-5), S(-2), S(-3.5), S(-6), 'M', x + S(1), y - S(18), 'q', S(5), S(-2), S(3.5), S(-6)), 0.6, 'none')
    + stP(stD('M', x - S(3.2), y - S(26), 'L', x - S(4.6), y - S(35), 'L', x + S(4.6), y - S(35), 'L', x + S(3.2), y - S(26), 'Z'), 0.9)
    + '<path d="' + stD('M', x, y - S(27.5), 'q', S(2), S(-2.6), 0, S(-5.6), 'q', S(-2), S(3), 0, S(5.6), 'z') + '" fill="' + ST.C + '" stroke="none"/>'
    + stP(stD('M', x - S(6), y - S(35), 'L', x, y - S(41), 'L', x + S(6), y - S(35), 'Z'), 0.9) + stC(x, y - S(42.5), S(1.2), 0, ST.N);
}
const stGlow = (x, y, k = 1) => '<ellipse cx="' + pFix(x) + '" cy="' + pFix(y - 1) + '" rx="' + pFix(17 * k) + '" ry="' + pFix(6 * k) + '" fill="url(#vmglow)" stroke="none"/>' + '<circle cx="' + pFix(x) + '" cy="' + pFix(y - 31 * k) + '" r="' + pFix(19 * k) + '" fill="url(#vmglow)" stroke="none"/>';   // the lantern's halo and its pool of light on the ground

// ── The townhouse (Sohyun 17:08-17:10: '그래 지금은 타운하우스로 가자 ... 각 층마다 살짝씩 다르게 인테리어 ... 돌하우스처럼';
// 'A · The townhouse, close up' -- '이 디자인은 이게 더 나은듯. 여기서 좀더 클래식함 가미해줘') ──
// One tall house cut open like a doll's house: the ground floor is the hall (the fox's portrait, the front door), then
// a floor for each stage, a room for each chapter, climbed by the stair on the left; at the top a mansard roof in
// chequered slates with a pedimented dormer and two turrets, the Queen on one and the King on the other. Classical
// dress: quoins up both corners, a dentil cornice between floors, panelled wainscot in every room, a pedimented door.
// Every floor has its own interior -- its wallpaper, its floor and the lamp on its stair -- like the rooms of a doll's
// house. A room is a chapter button; a finished room's number is green; yours has a coral frame and Clara in it.
const TH = { W: 360, X0: 22, X1: 338, SC: 0, RH: 86, LH: 28, SLAB: 13, GH: 112 };
const TH_SERIF = "'Cormorant Garamond',Georgia,serif", TH_CAPS = "Cinzel,Georgia,serif";   // her 17:22: classical letters (Inter and the plain icons had no classicism)
const thFontsIn = () => { try { return document.fonts.check('700 12px Cinzel') && document.fonts.check("700 15px 'Cormorant Garamond'"); } catch (e) { return false; } };
function thWrap(text, maxW, size, font) { const out = []; let cur = ''; String(text).split(' ').forEach(w => { const nx = cur ? cur + ' ' + w : w; if (cur && rdWidth(nx, 700, size, font) > maxW) { out.push(cur); cur = w; } else cur = nx; }); if (cur) out.push(cur); return out; }
function thPic(cx, top, ic, faded) {   // the chapter's picture in a frame with cut-in corners, hung from a nail on two cords
  const k = 0.6, iw = 48 * k, ih = 34 * k, w = iw + 14, h = ih + 12, x = cx - w / 2, y = top, r = 4;
  const fr = (a, rr) => stD('M', x + a + rr, y + a, 'L', x + w - a - rr, y + a, 'A', rr, rr, 0, 0, 0, x + w - a, y + a + rr, 'L', x + w - a, y + h - a - rr, 'A', rr, rr, 0, 0, 0, x + w - a - rr, y + h - a, 'L', x + a + rr, y + h - a, 'A', rr, rr, 0, 0, 0, x + a, y + h - a - rr, 'L', x + a, y + a + rr, 'A', rr, rr, 0, 0, 0, x + a + rr, y + a, 'Z');
  return stL(cx, y - 7, x + 7, y, 0.5) + stL(cx, y - 7, x + w - 7, y, 0.5) + stC(cx, y - 7.5, 1.2, 0, ST.N)
    + stP(fr(0, r), 1.1) + stP(fr(3, r - 1.5), 0.45, 'none')
    + '<g transform="translate(' + pFix(cx - iw / 2) + ' ' + pFix(y + 6) + ') scale(' + k + ')" fill="none" stroke="' + ST.N + '" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" opacity="' + (faded ? 0.5 : 1) + '">' + ic + '</g>';
}
const TH_FLOOR = [   // per stage: wallpaper, floor, the stair's lamp
  { wp: 'panel', fl: 'chequer', lamp: 'sconce' },       // 1 Getting started
  { wp: 'sprig', fl: 'planks', lamp: 'globe' },         // 2 Reading notes
  { wp: 'scale', fl: 'herring', lamp: 'bell' },         // 3 Rhythm
  { wp: 'trellis', fl: 'tiles', lamp: 'lantern' },      // 4 Reading tunes
  { wp: 'damask', fl: 'planks', lamp: 'pendant' },      // 5 Theory
  { wp: 'drape', fl: 'boards', lamp: 'candelabrum' },   // 6 Making music
  { wp: 'regency', fl: 'chequer', lamp: 'chandelier' }  // 7 Know the music
];
function thDefs() {
  const N = ST.N, p = (id, w, h, body) => '<pattern id="' + id + '" width="' + w + '" height="' + h + '" patternUnits="userSpaceOnUse">' + body + '</pattern>';
  return '<defs>'
    + p('thslate', 12, 12, '<rect width="12" height="12" fill="#fff"/><path d="M0 6 L6 0 L12 6 L6 12 Z" fill="' + N + '"/>')
    + p('thwp-sprig', 12, 12, '<g fill="' + N + '"><circle cx="3" cy="3" r="0.9"/><circle cx="9" cy="9" r="0.9"/></g>')
    + p('thwp-scale', 12, 8, '<path d="M0 8 A6 6 0 0 1 12 8 M-6 4 A6 6 0 0 1 6 4 M6 4 A6 6 0 0 1 18 4" fill="none" stroke="' + N + '" stroke-width="0.7"/>')
    + p('thwp-trellis', 11, 11, '<path d="M0 0 L11 11 M11 0 L0 11" stroke="' + N + '" stroke-width="0.7"/>')
    + p('thwp-damask', 12, 14, '<path d="M6 2 L9 7 L6 12 L3 7 Z" fill="none" stroke="' + N + '" stroke-width="0.8"/>')
    + p('thwp-regency', 14, 8, '<line x1="3" y1="0" x2="3" y2="8" stroke="' + N + '" stroke-width="2.4"/><line x1="7" y1="0" x2="7" y2="8" stroke="' + N + '" stroke-width="0.6"/>')
    + p('thfl-chequer', 12, 6, '<rect width="6" height="6" fill="' + N + '"/>')
    + p('thfl-planks', 24, 6, '<path d="M0 3 H24 M6 0 V3 M18 3 V6" stroke="' + N + '" stroke-width="0.6"/>')
    + p('thfl-herring', 8, 6, '<path d="M0 6 L4 0 L8 6" fill="none" stroke="' + N + '" stroke-width="0.7"/>')
    + p('thfl-tiles', 6, 6, '<rect x="0.5" y="0.5" width="5" height="5" fill="none" stroke="' + N + '" stroke-width="0.6"/>')
    + p('thfl-boards', 40, 6, '<path d="M0 3 H40 M14 0 V3 M30 3 V6" stroke="' + N + '" stroke-width="0.7"/>')
    + '<radialGradient id="vmglow"><stop offset="0" stop-color="' + ST.C + '" stop-opacity="0.42"/><stop offset="0.5" stop-color="' + ST.C + '" stop-opacity="0.16"/><stop offset="1" stop-color="' + ST.C + '" stop-opacity="0"/></radialGradient>'
    + '</defs>';
}
function thCornice(y, X0, X1) {   // the slab between floors: a thick line, a thin one, dentils, a fine line under (on white)
  return stR(X0, y, X1 - X0, 12, 0, '#fff') + stR(X0 - 5, y, X1 - X0 + 10, 3, 0, ST.N) + stR(X0 - 3, y + 4.6, X1 - X0 + 6, 0.9, 0, ST.N)
    + '<defs><pattern id="thdn" width="6" height="3.5" patternUnits="userSpaceOnUse"><rect width="3" height="3.5" fill="' + ST.N + '"/></pattern></defs><rect x="' + (X0 + 2) + '" y="' + pFix(y + 7) + '" width="' + (X1 - X0 - 4) + '" height="3.5" fill="url(#thdn)" stroke="none"/>'
    + stR(X0, y + 11.6, X1 - X0, 0.6, 0, ST.N);
}
function thLamp(kind, x, y) {   // the stair's lamp, hanging from the ceiling at y; returns [svg, glow]
  const flame = (fx, fy, k = 1) => '<path d="' + stD('M', fx, fy, 'q', 1.8 * k, -2.4 * k, 0, -5 * k, 'q', -1.8 * k, 2.6 * k, 0, 5 * k, 'z') + '" fill="' + ST.C + '" stroke="none"/>';
  const glow = (gx, gy, r) => '<circle cx="' + pFix(gx) + '" cy="' + pFix(gy) + '" r="' + r + '" fill="url(#vmglow)" stroke="none"/>';
  if (kind === 'chandelier') {
    let s = stL(x, y, x, y + 10, 0.8) + stC(x, y + 12, 2.2, 0.8);
    [-10, 0, 10].forEach(d => { s += stP(stD('M', x, y + 13, 'Q', x + d * 0.6, y + 21, x + d, y + 18), 0.8, 'none') + stR(x + d - 1.2, y + 13, 2.4, 5, 0.6) + flame(x + d, y + 12.5, 0.8); });
    return [s, glow(x, y + 14, 15)];
  }
  if (kind === 'candelabrum') {   // a wall bracket with three candles
    let s = stR(x - 2, y + 18, 4, 6, 0.8) + stP(stD('M', x - 9, y + 16, 'Q', x - 9, y + 21, x, y + 21, 'Q', x + 9, y + 21, x + 9, y + 16), 0.8, 'none');
    [-9, 0, 9].forEach(d => { s += stR(x + d - 1.3, y + 10 - (d ? 0 : 2), 2.6, 6 + (d ? 0 : 2), 0.6) + flame(x + d, y + 9.5 - (d ? 0 : 2), 0.8); });
    return [s, glow(x, y + 12, 15)];
  }
  if (kind === 'globe') return [stL(x, y, x, y + 9, 0.8) + stR(x - 2, y + 9, 4, 2.5, 0.7) + stC(x, y + 17, 6.5, 0.9) + stP(stD('M', x - 3.5, y + 14, 'q', 2, -2.5, 5, -1.5), 0.5, 'none') + stC(x, y + 17, 1.6, 0, ST.C), glow(x, y + 17, 14)];
  if (kind === 'bell') return [stL(x, y, x, y + 7, 0.8) + stP(stD('M', x - 6, y + 21, 'L', x - 6, y + 13, 'Q', x - 6, y + 7, x, y + 7, 'Q', x + 6, y + 7, x + 6, y + 13, 'L', x + 6, y + 21, 'Z'), 0.9) + stR(x - 7, y + 21, 14, 2, 0.7) + flame(x, y + 19, 0.9), glow(x, y + 15, 14)];
  if (kind === 'pendant') return [stL(x, y, x, y + 12, 0.8) + stP(stD('M', x - 7, y + 20, 'Q', x - 7, y + 12, x, y + 12, 'Q', x + 7, y + 12, x + 7, y + 20, 'Z'), 0.9) + stC(x, y + 21.5, 1.8, 0, ST.C), glow(x, y + 21, 14)];
  if (kind === 'lantern') return [stL(x, y, x, y + 8, 0.8) + stP(stD('M', x - 4, y + 11, 'L', x, y + 7, 'L', x + 4, y + 11, 'Z'), 0.8) + stR(x - 3.4, y + 11, 6.8, 9, 0.8) + flame(x, y + 18.5, 0.9) + stR(x - 4, y + 20, 8, 1.8, 0.7), glow(x, y + 15, 14)];
  return [stR(x - 1.5, y + 14, 3, 7, 0.8) + stP(stD('M', x, y + 21, 'q', 4, 0, 5, -5), 0.8, 'none') + stR(x + 3.8, y + 11, 2.4, 5, 0.6) + flame(x + 5, y + 10.5, 0.8), glow(x + 5, y + 10, 12)];   // a wall sconce
}
function thRoom(view, state, id, x, y, w, h, fs, out, dimNew) {   // dimNew: the guides' front page greys the rooms without a page
  const st = state[id], on = id === view.here, done = st === 'done', num = view.nums[id], cy = y + h - 22;
  let s = '<rect x="' + pFix(x) + '" y="' + pFix(y) + '" width="' + pFix(w) + '" height="' + pFix(h) + '" stroke-width="1"/>';
  if (fs.wp === 'drape') {   // a theatre: a scalloped valance and two curtains tied back
    let v = stD('M', x + 2, y + 2, 'L', x + w - 2, y + 2, 'L', x + w - 2, y + 6);
    const nsc = Math.max(3, Math.round((w - 4) / 10)), sw2 = (w - 4) / nsc;
    for (let k = nsc - 1; k >= 0; k--) v += ' ' + stD('Q', x + 2 + (k + 0.5) * sw2, y + 11, x + 2 + k * sw2, y + 6);
    s += stP(v + ' Z', 0.7);
  } else if (fs.wp !== 'panel') s += '<rect x="' + pFix(x + 1) + '" y="' + pFix(y + 1) + '" width="' + pFix(w - 2) + '" height="' + pFix(cy - y - 1) + '" fill="url(#thwp-' + fs.wp + ')" stroke="none" opacity="0.13"/>';
  // the wainscot: a chair rail and panels
  s += '<g opacity="0.4">' + stL(x + 2, cy, x + w - 2, cy, 0.9) + stL(x + 2, cy + 2.4, x + w - 2, cy + 2.4, 0.5) + '</g>';
  const fh = 6, np = w > 120 ? 3 : 2, pw = (w - 6 - np * 6) / np;
  for (let k = 0; k < np; k++) s += '<rect x="' + pFix(x + 6 + k * (pw + 6)) + '" y="' + pFix(cy + 6) + '" width="' + pFix(pw) + '" height="' + pFix(y + h - fh - cy - 9) + '" fill="none" stroke-width="0.6" opacity="0.3"/>';
  s += '<rect x="' + pFix(x + 1) + '" y="' + pFix(y + h - fh) + '" width="' + pFix(w - 2) + '" height="' + fh + '" fill="url(#thfl-' + fs.fl + ')" stroke="none" opacity="0.32"/>' + stL(x + 1, y + h - fh, x + w - 1, y + h - fh, 0.5);
  if (on) s += '<rect x="' + pFix(x + 1.2) + '" y="' + pFix(y + 1.2) + '" width="' + pFix(w - 2.4) + '" height="' + pFix(h - 2.4) + '" fill="none" stroke="' + ST.C + '" stroke-width="2.4"/>';
  // number on a chess square (green when done), the name, the picture
  const sq = 17, sx = x + 6, sy = y + (fs.wp === 'drape' ? 13 : 6);
  s += stSquare(sx, sy, sq, num, done ? ST.G : null, 11);
  const nm = CH_SHORT[id] || [id, ''], bare = st === 'print' ? nm[0] : t(nm[0], nm[1] || nm[0]), avail = w - sq - 12;
  const fits = (txt, z) => thWrap(txt, avail, z, TH_SERIF).length <= 1 && rdWidth(txt, 700, z, TH_SERIF) <= avail;
  let name = (done ? '✓\u00a0' : '') + bare, nz = [16.5, 15, 13.5].find(z => fits(name, z));
  if (!nz && done) { name = bare; nz = [16.5, 15, 13.5].find(z => fits(name, z)); }   // the green square already says done
  if (!nz) nz = 13.5;
  const lines = thWrap(name, avail, nz, TH_SERIF).slice(0, 2);
  lines.forEach((ln, k) => { s += stT(sx + sq + 5, sy + 13 + k * 14, ln, { size: nz, weight: 700, font: TH_SERIF, fill: on ? ST.C : dimNew && st === 'new' ? ST.NEW : ST.N }); });
  const ic = HOUSE_ICONS[id];
  if (ic) s += thPic(x + w / 2, Math.max(sy + lines.length * 14 + 14, cy - 40), ic, st === 'new' && !on);
  if (on) out.fig = (view.pawn || stPawn)(x + w - 20, y + h - fh - 0.5, 0.4);
  const label = num + '. ' + t(nm[0], nm[1] || nm[0]) + (done ? t(', done', ', 완료') : on ? t(', you are here', ', 지금 여기') : '');
  out.btns.push({ num, html: '<g data-chapter="' + id + '" data-status="' + st + '" data-here="' + (on ? '1' : '0') + '" role="button" tabindex="0" aria-label="' + penEsc(label).replace(/"/g, '&quot;') + '" style="cursor:pointer"><rect x="' + pFix(x + 1) + '" y="' + pFix(y + 1) + '" width="' + pFix(w - 2) + '" height="' + pFix(h - 2) + '" fill="transparent"/></g>' });
  return s;
}
// o.hall: the hall alone, cropped, with the front door as the button. o.wide: big screens and paper -- twice as wide,
// every floor's rooms in one row. o.print: the Workbook's page to colour in (no glow, every room the same).
function townhouseSvg(view, o = {}) {
  const state = {}; view.stages.forEach(x => x.ids.forEach((id, j) => { state[id] = x.st[j]; }));
  const { RH, LH, SLAB, GH } = TH, W = o.wide ? 720 : TH.W, X0 = TH.X0, X1 = W - TH.X0, RX0 = X0, out = { btns: [], fig: null };
  const cols = (n) => o.wide ? n : n <= 3 ? n : n === 4 ? 2 : 3;
  let head = '', body = '', glow = '';
  const top = 176; let y = top;
  for (let k = 6; k >= 0; k--) {   // the floors, the top stage first
    const st = view.stages[k], fs = TH_FLOOR[k], n = st.ids.length, c = cols(n), fh = LH + RH * Math.ceil(n / c), here = st.ids.includes(view.here);
    body += thCornice(y, X0, X1); const yy = y + SLAB;
    body += '<rect x="' + RX0 + '" y="' + pFix(yy) + '" width="' + (X1 - RX0) + '" height="' + LH + '" stroke="none"/>';
    // the floor's plaque: its number on a chess square and its name, in a moulded frame
    const name = (o.print ? st.s.en[0] : t(st.s.en[0], st.s.ko[0])).toUpperCase(), mw = rdWidth(name, 700, 11.5, TH_CAPS), pw = (thFontsIn() ? mw : Math.max(mw, name.length * 9.4)) + name.length * 1.04 + 36;   // Cinzel's capitals are wide: trust a measure only once the letters are in
    body += stR(RX0 + 6, yy + 4, pw, 20, 0.9) + stR(RX0 + 8, yy + 6, pw - 4, 16, 0.4, 'none') + stSquare(RX0 + 11, yy + 7.5, 13, k + 1, st.st.every(v => v === 'done') ? ST.G : null, 9)
      + stT(RX0 + 30, yy + 18.4, name, { size: 11.5, weight: 700, font: TH_CAPS, ls: '0.09em', fill: here ? ST.C : ST.N });
    const [lp, lg] = thLamp(fs.lamp, X1 - 24, yy); body += lp; glow += lg;
    st.ids.forEach((id, j) => {
      const r = Math.floor(j / c), cc = j - r * c, inrow = Math.min(c, n - r * c), rw = (X1 - RX0) / inrow;
      body += thRoom(view, state, id, RX0 + cc * rw, yy + LH + r * RH, rw, RH, fs, out, o.dimNew);
    });
    y = yy + fh;
  }
  // the ground floor: the hall -- the fox's portrait, a pedimented front door with a fanlight
  body += thCornice(y, X0, X1); const gy = y + SLAB, dx = W / 2 + 2;
  body += '<rect x="' + X0 + '" y="' + pFix(gy) + '" width="' + (X1 - X0) + '" height="' + GH + '" stroke-width="1"/>';
  body += '<rect x="' + (X0 + 1) + '" y="' + pFix(gy + GH - 7) + '" width="' + (X1 - X0 - 2) + '" height="7" fill="url(#thfl-chequer)" stroke="none" opacity="0.32"/>' + stL(X0 + 1, gy + GH - 7, X1 - 1, gy + GH - 7, 0.5);
  body += stP(stD('M', dx - 40, gy + 30, 'L', dx, gy + 12, 'L', dx + 40, gy + 30, 'Z'), 1.2) + stR(dx - 42, gy + 30, 84, 3, 0.9);
  [-1, 1].forEach(sd => { body += stPilaster(dx + sd * 36, gy + 33, gy + GH - 7, 7); });
  body += stP(stD('M', dx - 26, gy + GH - 7, 'L', dx - 26, gy + 60, 'A', 26, 26, 0, 0, 1, dx + 26, gy + 60, 'L', dx + 26, gy + GH - 7), 1.6);
  body += '<path d="' + stD('M', dx - 19, gy + 60, 'A', 19, 19, 0, 0, 1, dx + 19, gy + 60, 'Z') + '" fill="' + ST.N + '" stroke="none"/>' + [0.5, 1.05, 1.57, 2.1, 2.65].map(a => '<line x1="' + pFix(dx) + '" y1="' + pFix(gy + 60) + '" x2="' + pFix(dx + 18 * Math.cos(a)) + '" y2="' + pFix(gy + 60 - 18 * Math.sin(a)) + '" stroke="#fff" stroke-width="1"/>').join('');
  body += '<rect x="' + pFix(dx - 24) + '" y="' + pFix(gy + 63) + '" width="48" height="' + (GH - 70) + '" fill="#fbe3da" stroke="none"/>'
    + '<g data-leaf="l"><rect x="' + pFix(dx - 24) + '" y="' + pFix(gy + 63) + '" width="23.5" height="' + (GH - 70) + '" fill="' + ST.N + '" stroke="none"/>' + stC(dx - 4, gy + 90, 1.6, 0, '#fff') + '</g>'
    + '<g data-leaf="r"><rect x="' + pFix(dx + 0.5) + '" y="' + pFix(gy + 63) + '" width="23.5" height="' + (GH - 70) + '" fill="' + ST.N + '" stroke="none"/>' + stC(dx + 4, gy + 90, 1.6, 0, '#fff') + '</g>';
  const hallTop = y, door = [dx - 27, gy + 34, 54, GH - 41];
  const camH = 66, camX = o.wide ? dx - 200 : X0 + 22;
  body += '<ellipse cx="' + pFix(camX + camH * 0.4) + '" cy="' + pFix(gy + 18 + camH / 2) + '" rx="' + pFix(camH * 0.44) + '" ry="' + pFix(camH * 0.55) + '" fill="none" stroke-width="0.8"/>' + '<image href="' + VIC_CAMEO + '" x="' + pFix(camX) + '" y="' + pFix(gy + 18) + '" height="' + camH + '" width="' + pFix(camH * 0.794) + '"/>';
  [camX - 6, camX + camH * 0.8 + 6].forEach(sx => { const [lp, lg] = thLamp('sconce', sx - 2, gy + 26); body += lp; glow += lg; });
  const tx = o.wide ? dx + 200 : X1 - 10, T_ = (en, ko) => o.print ? en : t(en, ko);
  const ita = o.print || LANG !== 'ko';   // Hangul is never slanted
  body += stT(tx, gy + 58, T_('Your butler', '버틀러가'), { size: 17, weight: 700, anchor: 'end', font: TH_SERIF, italic: ita }) + stT(tx, gy + 76, T_('welcomes you.', '맞아 줘요.'), { size: 17, weight: 700, anchor: 'end', font: TH_SERIF, italic: ita });
  const gb = gy + GH;
  // the corners: quoins from the roof to the ground; the steps; the chequered pavement; lanterns by the steps
  body += stQuoins(X0, top, gb, false) + stQuoins(X1, top, gb, true) + stL(X0, top, X0, gb, 2.2) + stL(X1, top, X1, gb, 2.2);
  body += stR(dx - 38, gb, 76, 5, 0, ST.N) + stR(dx - 44, gb + 7, 88, 5, 0, ST.N);
  [dx - 58, dx + 58].forEach(lx => { body += stLantern(lx, gb + 12, 0.62); glow += stGlow(lx, gb + 12, 0.62); });
  const pv = gb + 14;
  body += '<rect x="6" y="' + pFix(pv) + '" width="' + (W - 12) + '" height="16" fill="url(#thpv)" stroke-width="0.8"/>';
  if (!o.print) body += stT(W / 2, pv + 34, T_('Start · climb up, one room at a time', '출발 · 한 방씩 위로 올라가요'), { size: 11, weight: 700, fill: ST.C, anchor: 'middle', font: TH_CAPS, ls: '0.1em' });
  // the roof: a mansard in chequered slates, iron cresting, a pedimented dormer with the name, chimneys, two turrets
  const rb = top, rt = top - 66, roof = stD('M', X0 + 6, rb, 'L', X0 + 30, rt, 'L', X1 - 30, rt, 'L', X1 - 6, rb, 'Z');
  head += '<path d="' + roof + '" fill="url(#thslate)" stroke-width="1.6"/>';
  for (let x = X0 + 30; x < X1 - 26; x += 8) head += '<path d="' + stD('M', x, rt, 'l', 0, -7, 'm', -3, 3, 'l', 3, -3, 'l', 3, 3) + '" fill="none" stroke-width="1"/>';
  head += stR(X0 + 26, rt - 1, X1 - X0 - 52, 2, 0, ST.N);
  (o.wide ? [X0 + 150, X1 - 166] : [X0 + 70, X1 - 86]).forEach(x => { head += stR(x, rt - 26, 16, 30, 1.4) + stR(x - 2, rt - 30, 20, 5, 0, ST.N); });
  const dw = 132, dx0 = W / 2 - dw / 2;
  head += stP(stD('M', dx0, rb - 4, 'L', dx0, rt + 22, 'L', dx0 + dw, rt + 22, 'L', dx0 + dw, rb - 4, 'Z'), 1.6) + stP(stD('M', dx0 - 8, rt + 22, 'L', W / 2, rt - 2, 'L', dx0 + dw + 8, rt + 22, 'Z'), 1.6) + stP(stD('M', dx0 + 4, rt + 19, 'L', W / 2, rt + 3, 'L', dx0 + dw - 4, rt + 19), 0.5, 'none') + stUrn(dx0 - 8, rt + 22) + stUrn(dx0 + dw + 8, rt + 22) + stFinial(W / 2, rt - 2, 6);
  head += stT(W / 2, rb - 18, 'Piano Butler', { size: 19, weight: 800, anchor: 'middle', serif: true, italic: true });
  head += '<g transform="translate(' + (W / 2) + ' ' + (rt + 14) + ') scale(0.8)"><path d="M-12 0 L-2 -5 L-2 5 Z M12 0 L2 -5 L2 5 Z" fill="none" stroke-width="1.4" stroke-linejoin="round"/><circle r="1.8" fill="' + ST.C + '" stroke="none"/></g>';
  [[X0 + 4, VIC_KING], [X1 - 40, VIC_QUEEN]].forEach(([tx, pc]) => {   // the turrets: the King on the left, the Queen on the right (her 17:17)
    const tw = 36;
    head += stR(tx, rt - 30, tw, rb - rt + 30, 1.4) + '<path d="' + stD('M', tx + 11, rt, 'A', 7, 7, 0, 0, 1, tx + 25, rt, 'L', tx + 25, rt + 22, 'L', tx + 11, rt + 22, 'Z') + '" fill="' + ST.N + '" stroke="none"/>'
      + stR(tx - 3, rt - 33, tw + 6, 3, 0, ST.N) + '<path d="' + stD('M', tx - 3, rt - 33, 'L', tx + tw / 2, rt - 82, 'L', tx + tw + 3, rt - 33, 'Z') + '" fill="url(#thslate)" stroke-width="1.4"/>' + stPiece(pc, tx + tw / 2, rt - 81, 0.3);
  });
  const pvDef = '<defs><pattern id="thpv" width="16" height="16" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="' + ST.N + '"/><rect x="8" y="8" width="8" height="8" fill="' + ST.N + '"/></pattern></defs>';
  const y0 = rt - 112, H = pv + (o.print ? 20 : 42) - y0;
  const btns = o.hall ? '<g data-door role="button" tabindex="0" aria-label="' + penEsc(t('Open the door and come in', '문을 열고 들어가요')) + '" style="cursor:pointer"><rect x="' + pFix(door[0]) + '" y="' + pFix(door[1]) + '" width="' + door[2] + '" height="' + door[3] + '" rx="3" fill="transparent"/></g>'
    : o.print ? '' : out.btns.sort((a, b) => a.num - b.num).map(b => b.html).join('');   // on paper nothing is a button
  const svg = '<g transform="translate(0 ' + (-y0) + ')">' + thDefs() + pvDef + stG(head + body) + (o.print ? '' : glow) + (out.fig && !o.hall ? '<g data-testid="map-figure">' + out.fig + '</g>' : '') + btns + '</g>';
  return { svg, W, H, vb: o.hall ? [0, pFix(hallTop - y0), W, pFix(H - (hallTop - y0))] : [0, 0, W, H] };
}
const HOUSE_IN_KEY = 'pb_house_in_v1';   // this session has come in through the door
// The chapter map (Sohyun 17:17: '맨 아래에 집사 얼굴 있는 층을 홈으로 바로 보이게 한다음 문을 열고 들어가면 아래서부터
// 앵커링'): it opens on the hall -- the butler's portrait and the front door. Tap the door: it swings open and the whole
// house rises above the hall, which stays where it was, so you climb from the bottom; your room comes into view. Once
// in, the map shows the house straight away for the rest of the session. The week board stands above.
function HouseMap({ onOpen, compact, noIntro }) {
  const box = useRef(null), houseRef = useRef(null), artRef = useRef(null), anchor = useRef(null), cameIn = useRef(false);
  const [fontTick, setFontTick] = useState(0);
  const [inside, setInside] = useState(() => { try { return sessionStorage.getItem(HOUSE_IN_KEY) === '1'; } catch (e) { return false; } });
  const [opening, setOpening] = useState(false);
  const [wide, setWide] = useState(() => { try { return window.innerWidth >= 760; } catch (e) { return false; } });   // big screens: the wide house, a floor's rooms in one row
  useEffect(() => { const el = box.current; if (!el) return; const f = () => setWide(el.clientWidth >= 700); f(); let ro = null; try { ro = new ResizeObserver(f); ro.observe(el); } catch (e) { window.addEventListener('resize', f); } return () => { try { ro && ro.disconnect(); } catch (e) {} window.removeEventListener('resize', f); }; }, []);
  useEffect(() => { try { Promise.all([document.fonts.ready, document.fonts.load('700 12px Cinzel'), document.fonts.load("700 15px 'Cormorant Garamond'"), document.fonts.load("italic 700 17px 'Cormorant Garamond'")]).then(() => { rdCtx = null; setFontTick(n => n + 1); }); } catch (e) {} }, []);   // measure the names in their own letters
  const stages = PATH_STAGES.map((s, i) => { const ids = pathStageIds(s); return { s, i, ids, st: ids.map(id => chapterState(id).status) }; });
  const all = stages.flatMap(x => x.ids), nums = {}; all.forEach((id, k) => { nums[id] = k + 1; });
  const finished = stages.reduce((a, x) => a + x.st.filter(v => v === 'done').length, 0);
  let last = null; try { last = localStorage.getItem(LAST_CHAPTER_KEY); } catch (e) {}
  const here = last && all.includes(last) && chapterState(last).status !== 'done' ? last : all.find(id => chapterState(id).status !== 'done');
  const link = loadStoredLink(), name = link && link.name ? link.name.trim() : '', today = localDay();
  const sig = stages.map(x => x.st.join(',')).join('|') + here + LANG + compact + name + today + fontTick + wide;
  const view = { stages, here, nums, pawn: name ? (x, y, k) => stPiece(VIC_PAWN_NAVY, x, y, k) : null };
  const house = useMemo(() => townhouseSvg(view, { wide }), [sig]);
  const hall = useMemo(() => townhouseSvg(view, { hall: true, wide }), [sig]);
  const week = useMemo(() => compact ? null : weekSvg({ days: practiceDays(), today, name }), [sig]);
  const reduced = (() => { try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } })();
  const enter = () => {
    if (inside || opening) return;
    try { anchor.current = artRef.current.getBoundingClientRect().bottom; } catch (e) { anchor.current = null; }
    cameIn.current = true; setOpening(true);
    setTimeout(() => { setOpening(false); setInside(true); try { sessionStorage.setItem(HOUSE_IN_KEY, '1'); } catch (e) {} }, reduced ? 0 : 520);
  };
  React.useLayoutEffect(() => {   // through the door: keep the hall where it was, the floors rise above it
    if (!inside || anchor.current == null) return;
    const el = houseRef.current, art = artRef.current; if (!el || !art) return;
    try { window.scrollBy(0, art.getBoundingClientRect().bottom - anchor.current); } catch (e) {}
    anchor.current = null;
    const t0 = setTimeout(() => { try { const r = el.querySelector('[data-here="1"]'); if (!r) return; const b = r.getBoundingClientRect(); if (b.top < 60) window.scrollBy({ top: b.top - window.innerHeight * 0.35, behavior: reduced ? 'auto' : 'smooth' }); } catch (e) {} }, reduced ? 0 : 820);
    return () => clearTimeout(t0);
  }, [inside]);
  const open = (e) => {
    if (e.target.closest && e.target.closest('[data-door]')) { enter(); return; }
    const c = e.target.closest && e.target.closest('[data-chapter]'); if (c) onOpen(c.getAttribute('data-chapter'));
  };
  const key = (e) => {
    const g = e.target; if (!g || !g.getAttribute || (e.key !== 'Enter' && e.key !== ' ')) return;
    if (g.getAttribute('data-door') != null) { e.preventDefault(); enter(); }
    else if (g.getAttribute('data-chapter')) { e.preventDefault(); onOpen(g.getAttribute('data-chapter')); }
  };
  const weekEl = week && <div data-testid="map-week" role="img" aria-label={t((name || 'Clara') + '’s week: ' + week.n + ' practice days this week' + (week.queen ? ', a queen' : ', ' + (WEEK_GOAL - week.n) + ' more to become a queen'), (name || '클라라') + '의 일주일: 이번 주 연습 ' + week.n + '일' + (week.queen ? ', 퀸' : ', 퀸까지 ' + (WEEK_GOAL - week.n) + '일'))} style={{lineHeight:0}} dangerouslySetInnerHTML={{__html: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + week.W + ' ' + week.H + '" width="100%">' + week.svg + '</svg>'}}/>;
  const intro = t('The Piano Butler’s house: every floor is a stage, every room is a chapter. Your butler meets you in the hall -- open the door and go up, floor by floor. New to the piano? Start on the first floor. Already playing? Go straight to any room.', '피아노 버틀러의 집: 층마다 단계 하나, 방마다 챕터 하나. 버틀러가 현관에서 맞아 줘요 -- 문을 열고 한 층씩 올라가요. 처음이라면 1층부터, 이미 배우고 있다면 어느 방으로든 바로 가요.');
  const hint = { textAlign:'center', fontFamily:"'Cormorant Garamond', Georgia, serif", fontStyle:LANG === 'ko' ? 'normal' : 'italic', fontSize:19, fontWeight:700, color:'#e4572e', marginTop:4, lineHeight:'26px' };   // the same line under the hall and under the house, so the hall keeps its place
  const css = '[data-house] [data-chapter]:focus-visible,[data-house] [data-door]:focus-visible{outline:none}[data-house] [data-chapter]:focus-visible rect,[data-house] [data-door]:focus-visible rect{stroke:#e4572e;stroke-width:3}'
    + '[data-hall] [data-leaf]{transition:transform .45s cubic-bezier(.3,.7,.3,1);transform-box:fill-box}[data-hall] [data-leaf="l"]{transform-origin:left center}[data-hall] [data-leaf="r"]{transform-origin:right center}[data-opening] [data-leaf]{transform:scaleX(.16)}'
    + '@keyframes pbRise{from{clip-path:inset(100% 0 0 0)}to{clip-path:inset(0 0 0 0)}}@media (prefers-reduced-motion: reduce){[data-house] [data-leaf]{transition:none}[data-house] [data-grow]{animation:none!important}}';
  return (
    <div data-testid="music-map" data-layout={inside ? 'house' : 'hall'} data-wide={wide ? '1' : '0'} data-house ref={box} className={compact ? '' : 'fade-up'} onClick={open} onKeyDown={key}>
      <style>{css}</style>
      {!compact && !noIntro && <PageIntro title={UI_TEACHER ? t('Music map', '음악 지도') : t('My music map', '나의 음악 지도')} text={intro}/>}
      <div data-testid="map-count" style={{fontSize:12.5,fontWeight:600,color:'#6d6f9c',maxWidth:wide ? 820 : 440,margin:'0 auto 4px'}}>{t(finished + ' of ' + all.length + ' chapters done', all.length + '개 챕터 중 ' + finished + '개 완료')}</div>
      <div style={{maxWidth:wide ? 820 : 440,margin:'0 auto'}}>
        {weekEl && <div style={{marginBottom:14,maxWidth:440}}>{weekEl}</div>}
        <div ref={houseRef} data-house-view role="group" aria-label={t('The Piano Butler’s house: one floor for each stage, one room for each chapter', '피아노 버틀러의 집: 단계마다 층 하나, 챕터마다 방 하나')}>
          {inside
            ? <><div ref={artRef} data-grow style={{animation: cameIn.current ? 'pbRise .8s cubic-bezier(.25,.7,.3,1) both' : 'none'}}><PenArt shapes={[{ k: 'raw', svg: house.svg }]} vb={house.vb} inter/></div>
                <div style={hint}>{t('Tap a room to go in', '방을 누르면 들어가요')}</div></>
            : <div data-hall data-opening={opening ? '1' : undefined}>
                <div ref={artRef}><PenArt shapes={[{ k: 'raw', svg: hall.svg }]} vb={hall.vb} inter/></div>
                <div style={hint}>{t('Tap the door to come in', '문을 눌러 들어와요')}</div>
              </div>}
        </div>
      </div>
    </div>
  );
}
// ─── the house in the books ───
// The small map at the foot of a chapter's map page: one row per stage, a chess square with each chapter's number,
// your chapter in coral -- the same order as the app's house, stage 1 at the top.
function houseMiniShapes(current, W = 600) {
  const s = [], X0 = 4, HW = W - 8, SC = 118, FH = 19, TOP = 4;
  const stages = PATH_STAGES.map((st, i) => ({ st, i, ids: pathStageIds(st) }));
  let n = 0; const nums = {}; stages.forEach(x => x.ids.forEach(id => { nums[id] = ++n; }));
  let y = TOP, svg = '';
  stages.forEach(x => {
    const has = x.ids.includes(current), rw = (HW - SC) / 5;
    svg += stL(X0, y + FH, X0 + HW, y + FH, 0.6);
    svg += stT(X0 + 2, y + 13, (x.i + 1) + ' · ' + x.st.en[0].toUpperCase(), { size: 8.6, weight: 700, fill: has ? ST.C : ST.N, font: TH_CAPS, ls: '0.06em' });
    x.ids.forEach((id, j) => {
      const rx = X0 + SC + j * rw, on = id === current, nm = (CH_SHORT[id] || [bkChapterName(id)])[0];
      if (on) svg += '<rect x="' + pFix(rx) + '" y="' + pFix(y + 1.5) + '" width="' + pFix(rw - 3) + '" height="' + (FH - 3) + '" fill="#fff" stroke="' + ST.C + '" stroke-width="1.3"/>';
      svg += stSquare(rx + 2.5, y + 3.5, 12, nums[id], null, 8.5) + stT(rx + 18.5, y + 13.4, nm, { size: 11, weight: 700, fill: on ? ST.C : ST.N, font: TH_SERIF });
    });
    y += FH;
  });
  s.push({ k: 'raw', svg: stG(stL(X0, TOP, X0 + HW, TOP, 1.2) + svg + stL(X0, y + 1.5, X0 + HW, y + 1.5, 1.2)) });
  return { shapes: s, W, H: y + 4 };
}
function BkHouse({ current, compact }) {
  const h = useMemo(() => houseMiniShapes(current), [current]);
  return (
    <div data-bk-house style={{border:'1.5px solid ' + BK.line,borderRadius:3,padding:compact ? '8px 12px 6px' : '10px 14px 8px'}}>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',marginBottom:4}}><div style={bkH(compact ? 15 : 17, 4)}>The Piano Butler’s house</div><span style={{fontSize:10.5,color:BK.muted}}>every floor a stage, every room a chapter -- the same order as the app</span></div>
      <PenArt shapes={h.shapes} vb={[0, 0, h.W, h.H]} label="The Piano Butler’s house: the chapter map"/>
    </div>
  );
}
// the whole house to colour in, on one page (the Workbook's opening page): the wide house, every room numbered
function BkHousePage() {
  const stages = PATH_STAGES.map((s, i) => { const ids = pathStageIds(s); return { s, i, ids, st: ids.map(() => 'print') }; });
  const nums = {}; stages.flatMap(x => x.ids).forEach((id, k) => { nums[id] = k + 1; });
  const [ft, setFt] = useState(0);
  useEffect(() => { try { Promise.all([document.fonts.load('700 12px Cinzel'), document.fonts.load("700 15px 'Cormorant Garamond'")]).then(() => { rdCtx = null; setFt(1); }); } catch (e) {} }, []);
  const v = useMemo(() => townhouseSvg({ stages, here: null, nums }, { wide: true, print: true }), [ft]);
  return <>
    <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em',marginTop:4}}>YOUR MAP</div>
    <h1 style={{fontFamily:"'Playfair Display', Georgia, serif",fontSize:32,fontWeight:900,color:BK.ink,margin:'2px 0 4px',lineHeight:1.05}}>The Piano Butler’s house</h1>
    <p style={{fontSize:13.5,color:BK.muted,margin:'0 0 8px',lineHeight:1.5}}>Every floor is a stage and every room is a chapter, numbered 1 to 26. Your butler meets you in the hall: go up, floor by floor. When you finish a chapter, <b style={{color:BK.ink}}>colour in its room</b>. Draw a little pawn -- that’s you -- in the room you are in.</p>
    <div style={{flex:1,minHeight:0,display:'flex',alignItems:'center',justifyContent:'center'}}><PenArt shapes={[{ k: 'raw', svg: v.svg }]} vb={v.vb} label="The Piano Butler’s house" style={{maxHeight:'100%'}}/></div>
  </>;
}
