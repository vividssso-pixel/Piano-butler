s = open('drills.src.html').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c); s = s.replace(a, b)

# 1. the pieces
rep("""const stPiece = (svg, x, y, k) => '<g transform="translate(' + pFix(x) + ' ' + pFix(y) + ') scale(' + k + ')">' + svg + '</g>';""",
"""const stPiece = (svg, x, y, k) => '<g transform="translate(' + pFix(x) + ' ' + pFix(y) + ') scale(' + k + ')">' + svg + '</g>';
/* m63 (her 2 Nov): your chess piece grows as you climb: Pawn on Level 0, ½ and 1, Knight on 2-3, Bishop 4-5, Rook 6-7, Queen 8.
   The 11 floor check-ups match a set: 4 pawns, 2 knights, 2 bishops, 2 rooks, 1 queen. Base at (0,0), about 100 units tall. */
const PC_BASE = 'M-20 0 L20 0 Q21.5 -4 18 -6.5 L15 -8 Q16 -11 13 -12.5 L-13 -12.5 Q-16 -11 -15 -8 L-18 -6.5 Q-21.5 -4 -20 0Z';
const PC_HL = (d) => '<path d="' + d + '" fill="none" stroke="#fffdf7" stroke-width="1.2" stroke-linecap="round" opacity="0.85"/>';
const PC_BODY = {
  knight: ['M-13 -12 L13 -12 Q12 -26 7 -36 Q9 -42 16 -48 Q20 -52 17 -57 Q15 -60 11 -60 Q8 -62 5 -64 L4 -73 L0 -66 L-3 -72 Q-8 -66 -12 -58 Q-16 -48 -15.5 -34 Q-15 -22 -13 -12Z', '', ['M-10 -56 Q-13 -44 -12 -30', 'M-5 -18 L-6 -30'], '<circle cx="5" cy="-56" r="1.6" fill="#fffdf7"/>'],
  bishop: ['M-11 -12 Q-8 -30 -6 -46 L-11 -48 L-11 -52 L-6 -54 Q-14 -64 -6 -75 Q0 -80 6 -75 Q14 -64 6 -54 L11 -52 L11 -48 L6 -46 Q8 -30 11 -12Z', '<circle cx="0" cy="-82" r="3.4"/>', ['M-9 -50 L9 -50', 'M2 -73 L-5 -60', 'M-4 -18 L-2.5 -44'], ''],
  rook: ['M-12 -12 L-10 -48 L-15 -52 L-15 -68 L-9 -68 L-9 -63 L-3 -63 L-3 -68 L3 -68 L3 -63 L9 -63 L9 -68 L15 -68 L15 -52 L10 -48 L12 -12Z', '', ['M-13 -52 L13 -52', 'M-4 -18 L-3 -44'], ''],
};
const PIECE_ORDER = ['pawn', 'knight', 'bishop', 'rook', 'queen'];
const PIECE_NAME = { pawn: ['Pawn', '폰'], knight: ['Knight', '나이트'], bishop: ['Bishop', '비숍'], rook: ['Rook', '룩'], queen: ['Queen', '퀸'] };
const PIECE_SYM = { pawn: '♟', knight: '♞', bishop: '♝', rook: '♜', queen: '♛' };
const PIECE_FROM = { pawn: 'Level 0', knight: 'Level 2', bishop: 'Level 4', rook: 'Level 6', queen: 'Level 8' };
const PIECE_COLS = [['#26296b', 'Navy', '네이비'], ['#e4572e', 'Coral', '코랄'], ['#e98ba0', 'Pink', '핑크'], ['#2e8a6e', 'Green', '초록']];
const PIECE_COL_KEY = 'pb_piece_col_v1', PIECE_LAST_KEY = 'pb_piece_last_v1';
const pieceCol = () => { try { return localStorage.getItem(PIECE_COL_KEY) || ''; } catch (e) { return ''; } };
const pieceOfFloor = (i) => i <= 3 ? 'pawn' : i <= 5 ? 'knight' : i <= 7 ? 'bishop' : i <= 9 ? 'rook' : 'queen';
function pieceOfRoom(id) {
  const fl = checkFloors(); let i = fl.findIndex(f => f.ids.includes(id));
  if (i < 0) { const k = PATH_STAGES.findIndex(st => pathStageIds(st).includes(id)); i = fl.findIndex(f => f.k >= k); if (i < 0) i = fl.length - 1; }
  return pieceOfFloor(Math.max(0, i));
}
function pieceSvg(kind, col) {
  if (kind === 'pawn') return VIC_PAWN_NAVY.split('#26296b').join(col);
  if (kind === 'queen') return VIC_QUEEN.split('#e4572e').join(col);
  const b = PC_BODY[kind];
  return '<g fill="' + col + '" stroke="' + col + '" stroke-width="0.8" stroke-linejoin="round"><path d="' + PC_BASE + '"/><path d="' + b[0] + '"/>' + b[1] + '</g>' + b[2].map(PC_HL).join('') + PC_HL('M-15 -4 L15 -4') + b[3];
}
const PieceIcon = ({ kind, col, h }) => <svg viewBox="-26 -100 52 104" aria-hidden="true" style={{ height: h, width: h * 0.5, display: 'block', flex: 'none' }} dangerouslySetInnerHTML={{ __html: pieceSvg(kind, col || '#26296b') }}/>;""")

# 2. the room: your piece beside the rabbit butler
a = s[s.index("  if (on && PB_ART.rabbit) {   /* m61/m62"):]
a = a[:a.index("'</g>'; }\n") + len("'</g>'; }\n")]
b = """  if (on && PB_ART.rabbit) {   /* m61/m62: the rabbit butler stands in the corner of your room; m63: your chess piece beside him. As big as the corner allows without touching a word */
    const boxes = [], ny0 = y + pad + sq + 5 + tz * 0.9;
    (lay.lines[id] || []).forEach((ln, i) => boxes.push([x + pad + rdWidth(ln, 800, tz, TH_SANS), ny0 + i * tz * 1.12 + tz * 0.3]));
    (lay.subs[id] || []).forEach((ln, i) => boxes.push([x + pad + rdWidth(ln, 500, sz, TH_SANS), ty + i * sz * 1.3 + sz * 0.3]));
    const pk = pieceOfRoom(id), pw = (RH) => RH * 0.92 * 0.46;
    const fits = (RH) => { const L = x + w - RH * 160 / 210 * 0.72 - 3 - pw(RH), T = y + h - RH - 2 + RH * 0.06; return boxes.every(([r, b]) => r < L - 2 || b < T); };
    let RH = Math.min(h * 0.62, cmp ? 48 : 74); while (RH > (cmp ? 26 : 34) && !fits(RH)) RH -= 2;
    const RW = RH * 160 / 210, r = PB_ART.rabbit, inner = r.slice(r.indexOf('>') + 1, r.lastIndexOf('</svg>')), rx = x + w - RW - 1;
    s += stPiece(pieceSvg(pk, view.pcol || '#26296b'), rx + RW * 0.31 - pw(RH) / 2 - 1, y + h - 3, (RH * 0.92 / 100).toFixed(4));
    s += '<g transform="translate(' + pFix(rx) + ' ' + pFix(y + h - RH - 2) + ') scale(' + (RH / 210).toFixed(4) + ')">' + inner + '</g>'; }
"""
rep(a, b)

# 3. the house knows your colour; the piece bar above it
rep("""  const [chkPick, setChkPick] = useState(null);
  const view = { stages, here, nums,""", """  const [chkPick, setChkPick] = useState(null);
  const [pcol, setPcol] = useState(pieceCol);   /* m63 */
  const view = { pcol, stages, here, nums,""")
rep("""  const sig = stages.map(x => x.st.join(',')).join('|') + here + LANG""", """  const sig = stages.map(x => x.st.join(',')).join('|') + here + pieceCol() + LANG""")
rep("""        {!compact && <ReviewCard/>}
        {false && inside""", """        {!compact && <ReviewCard/>}
        {!compact && inside && <PieceBar here={here} col={pcol} onCol={(c) => { try { localStorage.setItem(PIECE_COL_KEY, c); } catch (e) {} setPcol(c); }}/>}
        {false && inside""")

rep("""// ─── the house in the books ───""", """// m63: your piece above the house: the colour to pick (once), what you are now, the moment it changes
const PIECE_PROMO = {
  knight: ['Knights leap over the other pieces. You can leap further now.', '나이트는 다른 말을 뛰어넘어요. 이제 더 멀리 뛸 수 있어요.'],
  bishop: ['Bishops glide far along the diagonals. Longer phrases are yours now.', '비숍은 대각선으로 멀리 미끄러져요. 이제 긴 프레이즈도 거뜬해요.'],
  rook: ['Rooks are the strong towers of the board, and your playing is that strong now.', '룩은 체스판의 든든한 탑이에요. 이제 연주도 그만큼 든든해요.'],
  queen: ['The pawn reached the far side and is crowned. Every move is yours.', '폰이 끝까지 가서 왕관을 썼어요. 이제 모든 길이 열려요.'],
};
function PieceBar({ here, col, onCol }) {
  const kind = pieceOfRoom(here), c = col || '#26296b', i = PIECE_ORDER.indexOf(kind), nx = PIECE_ORDER[i + 1];
  const [promo, setPromo] = useState(() => { if (UI_TEACHER) return null; let last = null; try { last = localStorage.getItem(PIECE_LAST_KEY); localStorage.setItem(PIECE_LAST_KEY, kind); } catch (e) {}
    return last && PIECE_ORDER.indexOf(last) >= 0 && i > PIECE_ORDER.indexOf(last) ? last : null; });
  const [pick, setPick] = useState(() => !col && !UI_TEACHER);
  const card = { background: '#fff', border: '1.5px solid rgba(38,41,107,0.18)', borderRadius: 14, padding: '12px 14px', margin: '0 0 12px' };
  if (pick) return <div data-testid="piece-pick" style={card}>
    <b style={{ color: '#26296b', fontSize: 16 }}>{t('Pick the colour of your chess piece', '내 체스 말의 색을 골라요')}</b>
    <div style={{ fontSize: 13, color: '#6d6f9c', lineHeight: 1.45, margin: '3px 0 10px' }}>{t('You start as a pawn and grow as you climb: a Knight on Level 2, a Bishop on 4, a Rook on 6, and on Level 8 you are crowned Queen.', '폰으로 시작해서 올라갈수록 자라요: 레벨 2에서 나이트, 4에서 비숍, 6에서 룩, 레벨 8에서 퀸이 돼요.')}</div>
    <div style={{ display: 'flex', gap: 8 }}>{PIECE_COLS.map(([h, en, ko]) => <button key={h} type="button" data-piece-col={h} onClick={() => { onCol(h); setPick(false); }} style={{ flex: 1, minWidth: 0, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4, padding: '8px 0 6px', borderRadius: 12, border: '1.5px solid ' + (h === c && col ? '#26296b' : 'rgba(38,41,107,0.2)'), background: '#fff', cursor: 'pointer', font: 'inherit', color: '#26296b', fontSize: 12.5, fontWeight: 700 }}><PieceIcon kind="pawn" col={h} h={40}/>{t(en, ko)}</button>)}</div>
  </div>;
  return <div data-testid="piece-bar">
    {promo && <div data-testid="piece-promo" style={{ ...card, display: 'flex', alignItems: 'center', gap: 10, background: '#fbdfe3', borderColor: 'transparent' }}>
      <PieceIcon kind={promo} col={c} h={40}/><span style={{ color: '#e4572e', fontSize: 22, fontWeight: 700 }}>›</span><PieceIcon kind={kind} col={c} h={56}/>
      <div style={{ flex: 1, minWidth: 0 }}><b style={{ color: '#26296b', fontSize: 16 }}>{t('Your ' + PIECE_NAME[promo][0].toLowerCase() + ' is now a ' + PIECE_NAME[kind][0] + '!', '내 ' + PIECE_NAME[promo][1] + '이(가) ' + PIECE_NAME[kind][1] + '이(가) 됐어요!')}</b>
        <div style={{ fontSize: 13, color: '#5a5d92', lineHeight: 1.4, marginTop: 2 }}>{t(PIECE_PROMO[kind][0], PIECE_PROMO[kind][1])}</div></div>
      <button type="button" aria-label={t('Close', '닫기')} onClick={() => setPromo(null)} style={{ border: 'none', background: 'transparent', color: '#6d6f9c', fontSize: 18, cursor: 'pointer', alignSelf: 'flex-start' }}>×</button></div>}
    <div style={{ display: 'flex', alignItems: 'center', gap: 8, margin: '0 0 10px', fontSize: 13.5, color: '#5a5d92' }}>
      <PieceIcon kind={kind} col={c} h={30}/>
      <span><b style={{ color: '#26296b' }}>{UI_TEACHER ? t('A ' + PIECE_NAME[kind][0] + ' on this floor', '이 층에서는 ' + PIECE_NAME[kind][1]) : t('You are a ' + PIECE_NAME[kind][0], '나는 ' + PIECE_NAME[kind][1])}</b>{nx ? t(' · next: ' + PIECE_NAME[nx][0] + ' on ' + PIECE_FROM[nx], ' · 다음: ' + PIECE_FROM[nx].replace('Level', '레벨') + '에서 ' + PIECE_NAME[nx][1]) : t(' · the whole board is yours', ' · 체스판 전체가 내 거예요')}</span>
      {!UI_TEACHER && <button type="button" data-testid="piece-recolour" onClick={() => setPick(true)} style={{ marginLeft: 'auto', border: '1px solid rgba(38,41,107,0.25)', background: '#fff', borderRadius: 20, padding: '3px 10px', fontSize: 12, color: '#6d6f9c', cursor: 'pointer', font: 'inherit' }}>{t('Colour', '색')}</button>}
    </div>
  </div>;
}
// ─── the house in the books ───""")

# 4. the cards: still playing cards, a chess piece on the face
rep("""rank: CARD_RANKS[i % 13], suit: CARD_SUITS[i % 4],""", """rank: f.key === '0a' ? '0A' : f.key === '0b' ? '0B' : f.k === 1 ? '½' : String(f.k - 1), suit: PIECE_SYM[pieceOfFloor(i)], piece: pieceOfFloor(i), pname: t(PIECE_NAME[pieceOfFloor(i)][0], PIECE_NAME[pieceOfFloor(i)][1]),""")
a = s[s.index("function PlayingCard({ c, small }) {"):]
a = a[:a.index("\nfunction MyCards() {")]
assert "const col = c.suit === '♥'" in a
b = a.replace("const col = c.suit === '♥' || c.suit === '♦' ? '#e4572e' : '#26296b';", "const col = '#26296b', pcol = pieceCol() || '#26296b';   /* m63: still a playing card; your chess piece on its face, the floor in its corners */")
b = b.replace("<span style={{ position: 'absolute', left: 0, right: 0, top: '26%', textAlign: 'center', fontSize: small ? 26 : 38, color: col }}>{c.suit}</span>",
              "<span style={{ position: 'absolute', left: 0, right: 0, top: small ? '24%' : '20%', display: 'flex', justifyContent: 'center' }}><PieceIcon kind={c.piece} col={pcol} h={small ? 40 : 58}/></span>")
assert b != a and 'PieceIcon' in b
rep(a, b)
rep("""The butler deals you the ' + fresh.rank + ' ' + fresh.suit + '.', fresh.name + ' 중간점검을 통과했어요. 버틀러가 ' + fresh.suit + fresh.rank + ' 카드를 줘요.')""",
    """The butler deals you the ' + fresh.pname + ' card.', fresh.name + ' 중간점검을 통과했어요. 버틀러가 ' + fresh.pname + ' 카드를 줘요.')""")
rep("""t(' Pass it for the ' + nextCard.rank + ' ' + nextCard.suit + ' card.', ' 통과하면 ' + nextCard.suit + nextCard.rank + ' 카드.')""",
    """t(' Pass it for the ' + nextCard.pname + ' card.', ' 통과하면 ' + nextCard.pname + ' 카드.')""")
open('drills.src.html', 'w').write(s)
print('ok')
