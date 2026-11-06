#!/usr/bin/env python3
# Phase 420: the royals become chess-like signs, no faces (Sohyun 2026-10-10 08:12: '전체 다 바꾸자 -- 체스처럼 저렇게
#하는게 좀 더 깔끔한 듯. 상상력도 주고'): the Queen = her crown (coral, five points with pearls), the King = his crown
# (navy, a cross on top, three jewels), Princess Clara = her tiara. Everywhere the faces were (chapters 3-5, the books,
# the Workbooks, the app, the check rows). The words keep the story. The King's dragon and cows are words only now;
# the rabbit butler leaves chapter 2's opener (he stays in the REMEMBER band).
#   python3 patch420.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# 1. the three royal signs replace the three faces (same names, same call sites: every drawing follows)
for name in ['sfQueen', 'sfKing', 'sfClara']:
    rep('function %s(cx, cy, k = 1) {' % name, 'function %sFace(cx, cy, k = 1) {   // Phase 420: no longer drawn (kept for the record)' % name, name)
rep("function SfStaff({ clef = 'treble',", """// Phase 420: the royals are signs, like chess pieces -- a crown for the Queen, a crown for the King, a tiara for Clara.
// Each fills the box a face used to fill (centred on cx, cy), so every picture keeps its layout.
function sfQueen(cx, cy, k = 1) {   // the Queen's crown: coral, five points with pearls, a jewelled band
  const K = k * 2.1, P = (a, b) => [cx + a * K, cy + (b + 13) * K], s = [];
  s.push({ k: 'pa', seg: [['M', P(-6.6, -7.6)], ['L', P(-8, -16.6)], ['L', P(-4.6, -12.2)], ['L', P(-2.6, -18.4)], ['L', P(0, -13)], ['L', P(2.6, -18.4)], ['L', P(4.6, -12.2)], ['L', P(8, -16.6)], ['L', P(6.6, -7.6)], ['Z']], f: PEN_C, s: PEN_N, w: 1.6, nw: true });
  [[-8, -16.6], [-2.6, -18.4], [2.6, -18.4], [8, -16.6]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 1.2 * K, ry: 1.2 * K, f: PEN_P, s: PEN_N, w: 1, nw: true }));
  s.push({ ...penLine(P(-6.8, -9.6), P(6.8, -9.6), 1.4), nw: true });
  s.push({ k: 'el', c: P(0, -8.5), rx: 1.3 * K, ry: 1 * K, f: PEN_N, nw: true });
  return s;
}
function sfKing(cx, cy, k = 1) {   // the King's crown: navy, a cross on top, three coral jewels on a pearl band
  const K = k * 2.1, P = (a, b) => [cx + a * K, cy + (b + 12.4) * K], s = [];
  s.push({ k: 'pa', seg: [['M', P(-7.2, -6.2)], ['L', P(-7.4, -14)], ['L', P(-3.6, -10.6)], ['L', P(0, -15.2)], ['L', P(3.6, -10.6)], ['L', P(7.4, -14)], ['L', P(7.2, -6.2)], ['Z']], f: PEN_N, s: PEN_N, w: 1.6, nw: true });
  s.push({ ...penLine(P(-7.2, -8.2), P(7.2, -8.2), 1.4, PEN_P), nw: true });
  [[-4.4, -7.2], [0, -7.2], [4.4, -7.2]].forEach(([a, b]) => s.push({ k: 'el', c: P(a, b), rx: 0.9 * K, ry: 0.9 * K, f: PEN_C, s: PEN_P, w: 0.6, nw: true }));
  s.push({ ...penLine(P(0, -15.2), P(0, -19.2), 2), nw: true }, { ...penLine(P(-1.8, -17.3), P(1.8, -17.3), 2), nw: true });
  return s;
}
function sfClara(cx, cy, k = 1) {   // Princess Clara's tiara: small, coral, one jewel
  const K = k * 3.4, P = (a, b) => [cx + a * K, cy + (b + 9.4) * K], s = [];
  s.push({ k: 'pa', seg: [['M', P(-4.6, -7.4)], ['L', P(-3.6, -10.2)], ['L', P(-1.7, -8.8)], ['L', P(0, -12)], ['L', P(1.7, -8.8)], ['L', P(3.6, -10.2)], ['L', P(4.6, -7.4)], ['Q', P(0, -6.2), P(-4.6, -7.4)], ['Z']], f: '#f6c9bb', s: PEN_C, w: 1.4, nw: true });
  s.push({ k: 'el', c: P(0, -9.2), rx: 0.9 * K, ry: 0.9 * K, f: PEN_C, nw: true });
  return s;
}
function SfStaff({ clef = 'treble',""", 'royal signs')
rep("function nnClara(cx, cy, k = 1) { return sfClara(cx, cy, k); }   // Phase 405: Clara A (Royals-new-looks), drawn with the chapter-4 cast",
    "function nnClara(cx, cy, k = 1) { return sfClara(cx, cy, k); }   // Phase 420: Clara's tiara (the royals are signs, not faces)", 'nnClara')

# 2. chapter 5: the dragon and the cow leave the pictures (the sayings keep them in words); the King's crown sits by his
#    spaces, as the Queen's crown sits by hers
i0 = s.index('// the King\'s dragon (flies along his lines) and one of his cows'); i1 = s.index('function wsLbPages(scr = false) {')
s = s[:i0] + s[i1:]
rep("""  const dragon = wsDragon(24, 26, 1), cow = wsCow(22, 22, 1.25);
  const p4a = <SfStaff clef="bass" width={340} pad={[78, 34]} span={[4, 318]}""", """  const p4a = <SfStaff clef="bass" width={340} pad={[22, 34]} span={[4, 318]}""", 'p4a')
rep("""label={t('Kingsland\\'s five lines from the bottom: G B D F A -- Great Big Dragon Flies Away, with the King\\'s dragon flying above', '킹스랜드의 다섯 줄, 아래에서부터: G B D F A -- Great Big Dragon Flies Away, 위로 왕의 용이 날아가요')}""",
    """label={t('Kingsland\\'s five lines from the bottom: G B D F A -- Great Big Dragon Flies Away', '킹스랜드의 다섯 줄, 아래에서부터: G B D F A -- Great Big Dragon Flies Away')}""", 'p4a label')
rep("""icons={[SF_ICON(dragon, 270, 42, 1.2)]}""", """icons={[]}""", 'p4a icon')
rep("""label={t('Kingsland\\'s four spaces from the bottom: A C E G -- All Cows Eat Grass, with one of the King\\'s cows beside them', '킹스랜드의 네 칸, 아래에서부터: A C E G -- All Cows Eat Grass, 옆에 왕의 소')}""",
    """label={t('Kingsland\\'s four spaces from the bottom: A C E G -- All Cows Eat Grass, with the King\\'s crown beside them', '킹스랜드의 네 칸, 아래에서부터: A C E G -- All Cows Eat Grass, 옆에 왕의 왕관')}""", 'p4b label')
rep("""icons={[SF_ICON(cow, 290, 106, 1.05)]}""", """icons={[SF_ICON(king, 290, 104, 1.05)]}""", 'p4b icon')
rep("""    kings: [...wsCow(18, 22, 0.9), { ...penText(58, 28, 'ACEG', { size: 11, weight: 900, fill: PEN_C, anchor: 'middle' }) }],""",
    """    kings: [...sfKing(18, 22, 0.75), { ...penText(58, 28, 'ACEG', { size: 11, weight: 900, fill: PEN_C, anchor: 'middle' }) }],""", 'check row art')
rep("""label={t('The grand staff as a map of two lands: QUEENSLAND is the top staff, with the Queen beside it; KINGSLAND is the bottom staff, with the King beside it; Princess Clara stands between them', '큰보표는 두 나라의 지도: 위 오선은 퀸즈랜드, 옆에 여왕; 아래 오선은 킹스랜드, 옆에 왕; 그 사이에 클라라 공주')}""",
    """label={t('The grand staff as a map of two lands: QUEENSLAND is the top staff, with the Queen\\'s crown beside it; KINGSLAND is the bottom staff, with the King\\'s crown beside it; Princess Clara\\'s tiara between them', '큰보표는 두 나라의 지도: 위 오선은 퀸즈랜드, 옆에 여왕의 왕관; 아래 오선은 킹스랜드, 옆에 왕의 왕관; 그 사이에 클라라 공주의 티아라')}""", 'p1 label')

# 3. chapter 4: the picture labels say crowns, not people
rep("""label={t('The piano: the King stands at the low end, the Queen at the high end, and Princess Clara in the middle, on middle C', '피아노: 낮은 쪽 끝에 왕, 높은 쪽 끝에 여왕, 그리고 한가운데, 가운데 도 위에 클라라 공주')}""",
    """label={t('The piano: the King\\'s crown at the low end, the Queen\\'s crown at the high end, and Princess Clara\\'s tiara in the middle, on middle C', '피아노: 낮은 쪽 끝에 왕의 왕관, 높은 쪽 끝에 여왕의 왕관, 그리고 한가운데, 가운데 도 위에 클라라 공주의 티아라')}""", 'ch4 p1 label')

# 4. chapter 2's opener: the houses, the sea and the sky -- the butler stays in the REMEMBER band only
rep("""    return [...fsCoverShapes({ letters: false }), { k: 'raw', svg: rabbit }];""", """    return [...fsCoverShapes({ letters: false })];   // Phase 420: no rabbit in the lesson pictures (he stays in the REMEMBER band)""", 'ch2 opener rabbit')

open(src, 'w', encoding='utf-8').write(s); print('patch420 ok')
