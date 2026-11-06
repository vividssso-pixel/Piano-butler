#!/usr/bin/env python3
# Phase 400: chapter 2's lonely black key is the LIGHTHOUSE, not the kennel (Sohyun 2026-10-09) -- the Dog's doghouse is D
# now (chapter 3), and the low end of the piano is the sea, so the one black key standing alone at the bottom is a lighthouse.
#   python3 patch400.py <drills.src.html>
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

# the Lesson Book drawing (chapter 2, The whole piano & middle C)
rep("""  // p5: the whole piano -- 7+7 houses, the kennel, middle C where the two voices meet""",
    """  // p5: the whole piano -- 7+7 houses, the lighthouse (Phase 400), middle C where the two voices meet""", 'art comment')
rep("""        s.push(...fsRoof({ ...h, kind: 'small' }, 54, 10));
        s.push({ ...penText((h.x1 + h.x2) / 2 - 2, 27, t('the kennel', '개집'), { size: 8.5, weight: 900, fill: PEN_C, anchor: 'start' }), halo: true });
        s.push({ ...penCurve([['M', [(h.x1 + h.x2) / 2, 30]], ['L', [(h.x1 + h.x2) / 2, 42]]], 1.2, PEN_C), nw: true });""",
    """        s.push(...fsLighthouse((h.x1 + h.x2) / 2, 54, 1));
        s.push({ ...penText((h.x1 + h.x2) / 2 + 8, 30, t('the lighthouse', '등대'), { size: 8.5, weight: 900, fill: PEN_C, anchor: 'start' }), halo: true });""", 'art lighthouse')
rep("""// a bracket under a group of white keys, with a count""",
    """// the lighthouse on the lonely black key at the bottom (Phase 400): a striped tower, its lamp and two rays; a prop, straight
function fsLighthouse(cx, baseY, k = 1) {
  const P = (a, b) => [cx + a * k, baseY + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-4, 0)], ['L', P(-2.4, -18)], ['L', P(2.4, -18)], ['L', P(4, 0)], ['Z']], f: PEN_P, s: PEN_N, w: 1.4, nw: true });
  s.push({ k: 'pa', seg: [['M', P(-3.45, -6)], ['L', P(-3.1, -9.6)], ['L', P(3.1, -9.6)], ['L', P(3.45, -6)], ['Z']], f: PEN_C, nw: true });
  s.push({ k: 'pa', seg: [['M', P(-2.85, -13)], ['L', P(-2.6, -15.8)], ['L', P(2.6, -15.8)], ['L', P(2.85, -13)], ['Z']], f: PEN_C, nw: true });
  s.push({ k: 'rc', x: cx - 2.6 * k, y: baseY - 22.6 * k, w: 5.2 * k, h: 4.6 * k, rx: 0.4, f: '#fbe9e2', s: PEN_N, sw: 1.2, nw: true });
  s.push({ k: 'pa', seg: [['M', P(-3.4, -22.6)], ['L', P(0, -25.6)], ['L', P(3.4, -22.6)], ['Z']], f: PEN_N, nw: true });
  s.push({ ...penLine(P(3.6, -21.2), P(8, -23.4), 1, PEN_C), nw: true }, { ...penLine(P(3.6, -19.8), P(8, -18.6), 1, PEN_C), nw: true });
  s.push({ ...penLine(P(-3.6, -21.2), P(-8, -23.4), 1, PEN_C), nw: true }, { ...penLine(P(-3.6, -19.8), P(-8, -18.6), 1, PEN_C), nw: true });
  return s;
}
// a bracket under a group of white keys, with a count""", 'fsLighthouse')
rep("""{t('"Kennel" for the lonely key -- your call.', '외로운 건반의 "개집" -- 선생님이 정해 주세요.')}""",
    """{t('The lonely key is the lighthouse, standing by the sea at the low end.', '외로운 건반은 등대예요: 낮은 쪽 바닷가에 홀로 서 있어요.')}""", 'teacher')
rep("""label={t('All 88 keys: 7 small and 7 big houses, the kennel, and middle C, the ground between the sea and the sky', '88개 건반 전체: 작은 집 7채와 큰 집 7채, 개집, 그리고 바다와 하늘 사이의 땅인 가운데 도')}""",
    """label={t('All 88 keys: 7 small and 7 big houses, the lighthouse on the lonely black key by the sea, and middle C, the ground between the sea and the sky', '88개 건반 전체: 작은 집 7채와 큰 집 7채, 바닷가 외로운 검은건반 위의 등대, 그리고 바다와 하늘 사이의 땅인 가운데 도')}""", 'label')
rep("""        <>Find the <b>lonely black key</b> at the very bottom -- right beside it is the lowest key of all.</>,""",
    """        <>Find the <b>lonely black key</b> at the very bottom: the <b>lighthouse</b>, standing by the sea -- right beside it is the lowest key of all.</>,""", 'piano en')
rep("""        <>맨 아래의 <b>외로운 검은건반</b>을 찾아요 -- 바로 옆이 가장 낮은 건반이에요.</>,""",
    """        <>맨 아래의 <b>외로운 검은건반</b>을 찾아요: 바닷가에 홀로 선 <b>등대</b>예요 -- 바로 옆이 가장 낮은 건반이에요.</>,""", 'piano ko')
# the app's Whole piano tool
rep("""t('7 big houses too -- plus one lonely black key at the bottom: the end of a big house that doesn’t fit on the piano.', '큰 집도 7개 -- 그리고 맨 아래에 외톨이 검은건반 하나: 피아노에 다 들어가지 못한 큰 집의 끝이에요.')""",
    """t('7 big houses too -- plus one lonely black key at the bottom, the lighthouse by the sea: the end of a big house that doesn’t fit on the piano.', '큰 집도 7개 -- 그리고 맨 아래에 외톨이 검은건반 하나, 바닷가의 등대: 피아노에 다 들어가지 못한 큰 집의 끝이에요.')""", 'whole piano')
# the paper keyboard's lone-key picture (no caller today) and the Workbook / Teacher copy
rep("""// black key (a 1-group) gets a dog kennel.""", """// black key (a 1-group) gets a lighthouse (Phase 400).""", 'keyscene comment')
rep("""the letters at the windows. kennel: the lone""", """the letters at the windows. lighthouse: the lone""", 'keyscene comment 2')
s = s.replace("houses = true, doors = false, families = false, kennel = false,", "houses = true, doors = false, families = false, lighthouse = false,", 1)
rep("""(kennel ? 44 : 0), top = roofH""", """(lighthouse ? 44 : 0), top = roofH""", 'keyscene h')
rep("""      {(houses || kennel) && groups.map(([a, b], k) => {""", """      {(houses || lighthouse) && groups.map(([a, b], k) => {""", 'keyscene map')
old_k = s[s.index("        if (n === 1) return kennel ? <g key={k}>"):]
old_k = old_k[:old_k.index("\n") + 1]
rep(old_k, """        if (n === 1) return lighthouse ? <g key={k}><path d={`M${xm - 6} ${top - 2} L${xm - 3.6} ${top - 28} L${xm + 3.6} ${top - 28} L${xm + 6} ${top - 2} Z`} {...ART_SWF} strokeWidth="1.6"/><path d={`M${xm - 5.2} ${top - 10} L${xm - 4.6} ${top - 16} L${xm + 4.6} ${top - 16} L${xm + 5.2} ${top - 10} Z`} fill={BK.coral}/><rect x={xm - 4} y={top - 35} width="8" height="7" fill="#fbe9e2" stroke={BK.ink} strokeWidth="1.4"/><path d={`M${xm - 5} ${top - 35} L${xm} ${top - 40} L${xm + 5} ${top - 35} Z`} fill={BK.ink}/>{w >= 28 && <text x={xm + 10} y={top - 30} fontSize="10" fontWeight="800" fill={BK.muted}>lighthouse</text>}</g> : null;
""", 'keyscene draw')
rep("""        <div>2 · Draw a little kennel over the lonely black key at the very bottom.</div>""",
    """        <div>2 · Draw a little lighthouse on the lonely black key at the very bottom, by the sea.</div>""", 'wb')
rep("""'the kennel over the 2nd key from the bottom (A♯0/B♭0)'""", """'the lighthouse on the 2nd key from the bottom (A♯0/B♭0)'""", 'tc')
assert 'kennel' not in s.lower(), 'kennel left'
open(src, 'w', encoding='utf-8').write(s); print('patch400 ok')
