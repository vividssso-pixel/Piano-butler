# Chapter 2 review pack: front pages (cover, A, B) + the drill page, as HTML for Chromium to print
import os
NM = os.path.abspath('../../node_modules/@fontsource')
FONTS = ''.join(f"@font-face{{font-family:'Inter';font-weight:{w};src:url(file://{NM}/inter/files/inter-latin-{w}-normal.woff2) format('woff2');}}" for w in (400, 600, 700, 800)) + \
        ''.join(f"@font-face{{font-family:'Playfair Display';font-weight:{w};src:url(file://{NM}/playfair-display/files/playfair-display-latin-{w}-normal.woff2) format('woff2');}}" for w in (800, 900))
CSS = FONTS + """
@page { size:A4; margin:0; }
* { box-sizing:border-box; }
body { margin:0; font-family:Inter,'Noto Sans CJK KR',sans-serif; color:#26296b; font-size:11.5pt; line-height:1.45; }
.pg { width:210mm; height:297mm; padding:13mm 15mm 17mm; page-break-after:always; position:relative; overflow:hidden; }
.pg:last-child { page-break-after:auto; }
h1, h2 { font-family:'Playfair Display',Georgia,serif; margin:0; line-height:1.1; }
h1 { font-size:30pt; font-weight:900; }
h2 { font-size:17pt; font-weight:900; margin:0 0 2mm; }
.k { color:#e4572e; font-weight:800; font-size:10pt; margin-bottom:2mm; }
.sub { color:#4a4d86; margin:2mm 0 0; }
.box { border:1.2px solid #26296b; border-radius:3mm; padding:3.5mm 5mm; margin-top:4mm; }
.toc { width:100%; border-collapse:collapse; margin-top:2mm; font-size:11pt; }
.toc td { padding:1.4mm 0; border-bottom:0.6px solid #d9d4c4; }
.toc td.n { text-align:right; color:#6d6f9c; white-space:nowrap; }
.how li { margin:1mm 0; }
.q { margin-top:4mm; }
.q > b { display:block; }
.lines { height:12mm; background:repeating-linear-gradient(#fff 0 6.6mm, #b9b6d8 6.6mm 6.9mm); margin-top:1mm; }
.lines.s { height:8.5mm; }
.item { display:grid; grid-template-columns:9mm 1fr 30mm; gap:2mm; padding:2.2mm 0; border-bottom:0.6px solid #d9d4c4; font-size:10.3pt; break-inside:avoid; }
.item .id { font-weight:800; color:#e4572e; }
.item .t b { color:#26296b; }
.item .t { color:#3c3f78; }
.item .fx { color:#26296b; font-weight:600; margin-top:0.8mm; }
.tick { font-size:9.5pt; color:#26296b; white-space:nowrap; }
.tick span { display:inline-block; width:3.6mm; height:3.6mm; border:1.2px solid #26296b; border-radius:0.8mm; vertical-align:-0.6mm; margin-right:1mm; }
.yel { background:#fff1a8; }
.grid3 { display:grid; grid-template-columns:repeat(3,1fr); gap:4mm; margin-top:3mm; align-items:start; }
.grid3 img { width:100%; border:0.6px solid #d9d4c4; border-radius:2mm; }
.cap { font-size:9.5pt; font-weight:700; margin-top:1mm; }
.foot { position:absolute; bottom:8mm; left:15mm; right:15mm; font-size:8.5pt; color:#6d6f9c; display:flex; justify-content:space-between; }
"""


def page(inner, foot):
    return f'<section class="pg">{inner}<div class="foot"><span>Piano Butler · Chapter 4 review v4 · Reading the Staff</span><span>{foot}</span></div></section>'

def doc(pages):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'

tick = '<div class="tick"><span></span>Fix it &nbsp;&nbsp;<span></span>No / differently</div>'



cover = """
<div class="k">PIANO BUTLER · CHAPTER-BY-CHAPTER REVIEW · 2026-10-09 · DRAFT 4</div>
<h1>Chapter 4 · Reading the Staff (v4)</h1>
<p class="sub">v3 답을 반영했어요. <b>인물은 고르신 조합(왕 A &middot; 클라라 A &middot; 여왕 A)으로 전부 갈아 끼웠고</b>, 이제 7쪽이에요.</p>
<div class="box">
  <h2>바뀐 것</h2>
  <table class="toc">
    <tr><td>가족 캐릭터 확정: 왕 A(하얀 수염) &middot; 클라라 A(땋은 머리+티아라) &middot; 여왕 A(올림머리+진주) &mdash; 모든 그림에 반영</td><td class="n">전체</td></tr>
    <tr><td>2쪽 활동은 <b>손 오선 하나만</b> (실제 레슨에서 쓰시는 것) &mdash; 연필 꼬치 시험 뺌</td><td class="n">2쪽</td></tr>
    <tr><td>3쪽 <b>내려가기 추가</b>: 한 걸음은 언덕처럼 올라갔다 내려오고, 화살표는 양쪽을 가리켜요; 피아노 활동도 올라갔다 내려와요</td><td class="n">3쪽</td></tr>
    <tr><td>6쪽 접기 없음: 쓴 가운데 도가 <b>여왕의 오선 바로 아래</b>에 붙거나 <b>왕의 오선 바로 위</b>에 붙는 것, 같은 세로줄 + &ldquo;같은 건반!&rdquo; 점선으로. 접기 활동은 5챕터의 세 C(가운데 도&middot;높은자리 C&middot;낮은자리 C)에서</td><td class="n">6쪽</td></tr>
    <tr><td><b>기준 음(랜드마크) 쪽은 5챕터로 이동</b> &mdash; 이 챕터는 소개와 아홉 음까지, 빨리 읽기는 다음 챕터</td><td class="n">7쪽 &rarr; 5챕터</td></tr>
    <tr><td>다섯 가지 확인의 마지막 줄: &ldquo;두 오선에서 가운데 도를 찾을 수 있어요 &mdash; 위에 붙어도 아래에 붙어도 같은 건반&rdquo;</td><td class="n">7쪽</td></tr>
  </table>
</div>
<div class="box">
  <h2>남은 결정</h2>
  <div class="q"><b>F1. 이대로 적용 들어갈까요?</b> 앱 레슨(책 그대로 화면에) + 드릴 7단계 + 워크북 + 선생님용 + 가이드 페이지(Q1~Q3 답 포함) + 3챕터의 클라라도 새 디자인으로.<div class="lines s"></div></div>
  <div class="q"><b>F2. 드릴 7단계 중 &ldquo;기준 음&rdquo;이 들어가던 자리는 그대로 두고, 빨리 읽기 연습만 5챕터 드릴로 보낼게요 &mdash; OK?</b><div class="lines s"></div></div>
</div>
"""
pages = [page(cover, 'p. 1')]
open('front.html', 'w').write(doc(pages))
print('front.html written')
