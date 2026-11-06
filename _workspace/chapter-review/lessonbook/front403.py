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
    return f'<section class="pg">{inner}<div class="foot"><span>Piano Butler · Chapter 4 review v3 · Reading the Staff</span><span>{foot}</span></div></section>'

def doc(pages):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'

tick = '<div class="tick"><span></span>Fix it &nbsp;&nbsp;<span></span>No / differently</div>'



cover = """
<div class="k">PIANO BUTLER · CHAPTER-BY-CHAPTER REVIEW · 2026-10-09 · DRAFT 3</div>
<h1>Chapter 4 · Reading the Staff (v3)</h1>
<p class="sub">밤에 주신 답(n1&ndash;n7, w1&ndash;w6, d2&ndash;d4, &ldquo;1쪽 미니멀하게&rdquo;)을 반영한 세 번째 초안이에요. 인물 디자인은 <b>Royals-new-looks</b>에서 골라 주시면 바로 갈아 끼워요 &mdash; 이 초안은 아직 예전 그림이에요.</p>
<div class="box">
  <h2>바뀐 것</h2>
  <table class="toc">
    <tr><td>1쪽 미니멀 + n2: 왕실 가족을 <b>건반 위에서 먼저</b> 소개 (음자리표 기호 없이), 글 세 문장</td><td class="n">1쪽</td></tr>
    <tr><td>n1: 엄지 시험 &rarr; <b>연필 꼬치 시험</b> (연필을 줄 위에 포개면 줄 음표는 한가운데가 꿰여요)</td><td class="n">2쪽 N1</td></tr>
    <tr><td>n3: 바닥 오선&middot;사방치기&middot;깃발 게임 빠짐 &mdash; 쪽마다 활동 2~3개로 컴팩트하게</td><td class="n">2&middot;3&middot;7쪽</td></tr>
    <tr><td>n4&middot;n5: 소용돌이 그리기&middot;경비병 그리기 확정 (노란 표시 없어짐)</td><td class="n">4&middot;5쪽</td></tr>
    <tr><td>n6: <b>가운데 도가 쓰인 곳마다 작은 클라라</b>가 서 있어요 &mdash; 위 오선에 붙어도, 아래 오선에 붙어도 같은 건반</td><td class="n">6&middot;7쪽</td></tr>
    <tr><td>w2: 앱에서 왕이 천천히 걸어와 경비병 두 점 사이에서 확인받고 F 줄로 들어가는 애니메이션 (적용 때)</td><td class="n">앱</td></tr>
    <tr><td>w4: 오선 접기는 5챕터의 높은음자리표 C&middot;낮은음자리표 C에서 다시</td><td class="n">5챕터</td></tr>
    <tr><td>d2: 5챕터 = <b>Queensland(여왕의 오선)과 Kingsland(왕의 오선)</b>, 문장 카드도 나라별로</td><td class="n">5챕터</td></tr>
    <tr><td>d3&middot;d4: 드릴 7단계, 새 챕터 이름 The Whole Staff 확정</td><td class="n">&mdash;</td></tr>
  </table>
</div>
<div class="box">
  <h2>남은 결정</h2>
  <div class="q"><b>E1. 인물 디자인 (Royals-new-looks): 왕 A/B &middot; 여왕 A/B &middot; 클라라 A/B/C/D &mdash; 조합으로 골라 주세요. 섞기&middot;수정 요청 환영.</b><div class="lines s"></div></div>
  <div class="q"><b>E2. 2쪽 연필 꼬치 시험 (노란 표시) &mdash; 이 정도면 쓸 만할까요?</b><div class="lines s"></div></div>
  <div class="q"><b>E3. 이대로 좋으면 적용 들어갈게요: 앱 레슨(책 그대로 화면에) + 드릴 7단계 + 워크북 + 선생님용 + 가이드 페이지(소현님 Q1~Q3 답 포함).</b><div class="lines s"></div></div>
</div>
"""
pages = [page(cover, 'p. 1')]
open('front.html', 'w').write(doc(pages))
print('front.html written')
