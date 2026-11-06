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
    return f'<section class="pg">{inner}<div class="foot"><span>Piano Butler · Chapter 4 review v2 · Reading the Staff</span><span>{foot}</span></div></section>'

def doc(pages):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'

tick = '<div class="tick"><span></span>Fix it &nbsp;&nbsp;<span></span>No / differently</div>'


cover = """
<div class="k">PIANO BUTLER · CHAPTER-BY-CHAPTER REVIEW · 2026-10-09 · DRAFT 2</div>
<h1>Chapter 4 · Reading the Staff (v2)</h1>
<p class="sub">소현님 답을 그대로 반영한 두 번째 초안이에요. <b>다섯 음 먼저</b>: 이 챕터는 클라라 공주(가운데 도) 둘레의 아홉 음만 읽어요 &mdash; 위로 여왕의 G까지 다섯(C D E F G), 아래로 왕의 F까지 다섯(F G A B C). 줄 외우는 문장과 오선 전체는 <b>새 5챕터</b>, 덧줄은 6챕터로. <span class="yel">노란 표시 N1&ndash;N7</span> = 새로 넣은 활동 제안이에요.</p>
<div class="box">
  <h2>소현님 답 &rarr; 이렇게 바꿨어요</h2>
  <table class="toc">
    <tr><td>a1 다섯 음 기준, 늘어나는 건 뒤로</td><td class="n">3&middot;4&middot;5단계 = C&ndash;G, F&ndash;C, 큰보표</td></tr>
    <tr><td>a2 / B5 알토음자리표 빼기</td><td class="n">없어졌어요</td></tr>
    <tr><td>a3 / B2 문장은 뒤에</td><td class="n">5챕터로 (아이디어는 3쪽)</td></tr>
    <tr><td>a4 / B1 가운데 도 = 클라라 공주로 하나만</td><td class="n">하버 브리지&middot;도시 그림 빠짐</td></tr>
    <tr><td>a5 이름 통일</td><td class="n">Reading the Staff / 오선보 읽기</td></tr>
    <tr><td>a6 / B7 플래시 카드&middot;쓰기는 드릴 안으로</td><td class="n">드릴 6단계 &ldquo;Write it&rdquo; (3쪽)</td></tr>
    <tr><td>B3 기준 음 다섯</td><td class="n">여기선 셋(G, 가운데 도, F), 칸의 C 둘은 5챕터</td></tr>
    <tr><td>B4 줄 위 / 두 줄 사이를 확실하게</td><td class="n">돋보기 그림 + 엄지 시험 + 바닥 오선 (2쪽)</td></tr>
    <tr><td>B6 하나씩 소화하기 쉽게</td><td class="n">드릴 7단계, 한 단계에 한 가지</td></tr>
    <tr><td>B8 사다리</td><td class="n">&ldquo;little ladder rung&rdquo; / &ldquo;작은 사다리 발판&rdquo;</td></tr>
    <tr><td>B9 거울, B10 다섯 가지 확인</td><td class="n">그대로 (6쪽, 8쪽)</td></tr>
  </table>
  <p style="font-size:9.5pt;margin:2mm 0 0;color:#4a4d86">한국어는 &ldquo;사다리 <b>칸</b>&rdquo; 대신 &ldquo;사다리 <b>발판</b>&rdquo;으로 썼어요 &mdash; 오선의 &ldquo;칸&rdquo;(space)과 헷갈리지 않게.</p>
</div>
<div class="box">
  <h2>In this pack</h2>
  <table class="toc">
    <tr><td>1. 활동 제안 (레슨북 N1&ndash;N7, 워크북 W1&ndash;W6)</td><td class="n">p. 2</td></tr>
    <tr><td>2. 드릴 7단계 &middot; 5챕터 문장 아이디어 &middot; 결정 4개</td><td class="n">p. 3</td></tr>
    <tr><td><b>The Lesson Book &mdash; draft 2</b> (8 pages)</td><td class="n">p. 4&ndash;11</td></tr>
  </table>
</div>
"""

n_items = [
    ("N1", "2쪽", "<b>엄지 시험</b> &mdash; 음표를 엄지로 가렸을 때 줄이 엄지 양옆 한가운데로 삐져나오면 줄 음표, 위아래로 보이면 칸 음표. 그림의 돋보기와 같은 생각을 손으로."),
    ("N2", "2쪽", "<b>바닥 오선</b> &mdash; 바닥에 테이프 다섯 줄. &ldquo;3번 줄!&rdquo; &ldquo;2번 칸!&rdquo; 하면 줄 <i>위로</i>, 칸 <i>안으로</i> 뛰어요. 몸으로 위/사이를 느끼게."),
    ("N3", "3쪽", "<b>오선 사방치기</b> &mdash; 같은 바닥 오선에서 한 걸음(줄&rarr;칸)과 건너뛰기(줄&rarr;줄)를 뛰고, 피아노에서 똑같이 쳐요."),
    ("N4", "4쪽", "<b>여왕의 소용돌이 그리기</b> &mdash; 높은음자리표는 G 줄에서 시작해 밖으로 감아요: &ldquo;여왕의 집에서 출발!&rdquo; (워크북에 따라 그리기)"),
    ("N5", "5쪽", "<b>왕의 경비병 그리기</b> &mdash; 낮은음자리표는 F 줄 위의 점에서 시작, 그리고 F 줄 위아래에 경비병 두 점."),
    ("N6", "6쪽", "<b>어느 궁전?</b> &mdash; 클라라를 위 오선 아래에 쓰든 아래 오선 위에 쓰든 같은 건반. 그다음 F, C, G = 왕, 공주, 여왕."),
    ("N7", "7쪽", "<b>깃발 게임</b> &mdash; 건반의 G, 가운데 도, F에 포스트잇 깃발. 오선의 음을 짚으면 가장 가까운 깃발에서 출발해 그 건반으로 &mdash; 빨리!"),
]
w_items = [
    ("W1", "<b>클라라 말</b> &mdash; 오려 쓰는 작은 클라라 공주 카드. 큰보표 위 어디에 세워도 사다리 발판 위, 같은 건반이에요. (6쪽 맞은편)"),
    ("W2", "<b>왕을 집에 데려다 줘요</b> (옛 워크북의 F 미로, 살려요) &mdash; F 줄 음표만 밟고 가는 길, 다섯 음 안에서."),
    ("W3", "<b>비밀 편지</b> (옛 워크북, 살려요) &mdash; 아홉 음만으로 쓰는 낱말: BAG, CAGE, FACE, BADGE, 그리고 긴 것 하나 <b>CABBAGE</b>."),
    ("W4", "<b>오선 접기</b> (옛 워크북, 살려요) &mdash; 종이를 가운데 도에서 접으면 G가 F에 겹쳐요."),
    ("W5", "<b>꼬치와 샌드위치 분류</b> &mdash; 음표 카드를 줄 음표(꼬치)/칸 음표(샌드위치) 두 접시에 나눠 담기."),
    ("W6", "<b>음표 빙고</b> (옛 워크북, 살려요) &mdash; 칸은 아홉 음만, 선생님이 건반을 치면 학생이 오선에서 찾아 표시."),
]
ktick = '<div class="tick"><span></span>Keep &nbsp;&nbsp;<span></span>No / differently</div>'
act_page = '<div class="k">CHAPTER 4 REVIEW v2</div><h2>1. 활동 제안 &mdash; 개념마다 몸&middot;손으로 하는 것 하나씩</h2><p class="sub" style="font-size:10pt">레슨북 초안에서 <span class="yel">노란색</span>인 것들이에요. 워크북(W)은 레슨북이 정해지면 같은 쪽 맞은편에 들어가요.</p>' + \
  '<h2 style="font-size:13pt;margin-top:4mm">Lesson Book</h2>' + ''.join(
    f'<div class="item"><div class="id">{i}</div><div class="t"><span style="color:#6d6f9c;font-weight:700">{pg}</span> &middot; {txt}</div>{ktick}</div>' for i, pg, txt in n_items) + \
  '<h2 style="font-size:13pt;margin-top:5mm">Workbook</h2>' + ''.join(
    f'<div class="item"><div class="id">{i}</div><div class="t">{txt}</div>{ktick}</div>' for i, txt in w_items)

dec_page = """
<div class="k">CHAPTER 4 REVIEW v2</div><h2>2. 드릴 7단계 (한 단계에 한 가지)</h2>
<table class="toc" style="font-size:10.3pt">
  <tr><td><b>1</b> Line or space? &mdash; 음표 하나: 줄일까 칸일까</td><td class="n">새</td></tr>
  <tr><td><b>2</b> Step or skip, up or down? &mdash; 음표 둘: 한 걸음/건너뛰기, 위/아래</td><td class="n">새</td></tr>
  <tr><td><b>3</b> The Queen's five: C D E F G &mdash; 높은음자리표, 가운데 도~G</td><td class="n">좁힘</td></tr>
  <tr><td><b>4</b> The King's five: F G A B C &mdash; 낮은음자리표, F~가운데 도</td><td class="n">좁힘</td></tr>
  <tr><td><b>5</b> Around Clara: both staves &mdash; 큰보표, 아홉 음 섞어서</td><td class="n">새</td></tr>
  <tr><td><b>6</b> Write it: tap where it goes &mdash; 음이름을 보고 오선에 직접 놓기 (쓰기 = a6)</td><td class="n">새</td></tr>
  <tr><td><b>7</b> Find it on the keys &mdash; 오선의 음을 건반에서 (아홉 음)</td><td class="n">좁힘</td></tr>
</table>
<p class="sub" style="font-size:9.5pt">지금의 &ldquo;높은음자리표 전체 / 낮은음자리표 전체 / 덧줄까지&rdquo; 단계는 5&middot;6챕터 드릴로 옮겨요. 플래시 카드는 따로 만들지 않고 드릴이 그 역할(랜덤, 날마다) &mdash; Q2 답 그대로.</p>

<h2 style="margin-top:5mm">5챕터 문장 아이디어 (b2: 다른 방법?)</h2>
<p style="font-size:10.3pt;margin:1mm 0">Q1에서 말씀하신 진짜 문제는 문장이 아니라 <b>음자리표를 먼저 안 보는 것</b>이라서, 문장마다 <b>주인</b>을 붙이는 걸 제안해요. 문장은 소현님 것 그대로.</p>
<ul style="font-size:10.3pt;margin:1mm 0 0;padding-left:5mm">
  <li><b>왕관 먼저(Crown check)</b>: 읽기 전에 음자리표를 손가락으로 짚고 &ldquo;여왕!&rdquo; / &ldquo;왕!&rdquo; 하고 말해요. 드릴 첫 단계도 &ldquo;Whose palace?&rdquo;(누구의 궁전?)부터.</li>
  <li><b>여왕의 문장</b>: 줄 &ldquo;Every Good Boy Deserves Fun&rdquo; &mdash; 여왕이 착한 아이들에게 상을 줘요. 칸 &ldquo;FACE&rdquo; &mdash; 여왕이 거울 속 자기 <b>얼굴</b>을 봐요.</li>
  <li><b>왕의 문장</b>: 줄 &ldquo;Great Big Dragon Flies Away&rdquo; &mdash; 왕의 성에서 용이 날아가요. 칸 &ldquo;All Cows Eat Grass&rdquo; &mdash; 왕의 들판에서 소가 풀을 먹어요.</li>
  <li>문장 카드도 여왕 카드(진주 왕관) / 왕 카드(십자 왕관)로 나눠서, 섞이면 그림이 안 맞게.</li>
  <li>문장은 <b>확인용</b>, 읽기는 기준 음(G, 가운데 도, F + 칸의 C 둘)에서 &mdash; 문장을 처음부터 외워 세는 습관이 안 들게.</li>
</ul>

<h2 style="margin-top:5mm">결정 필요</h2>
<div class="q"><b>D1. 활동 N1&ndash;N7, W1&ndash;W6 &mdash; 2쪽에 체크해 주세요.</b></div>
<div class="q"><b>D2. 5챕터 문장: 위처럼 여왕/왕에게 붙이기 + 왕관 먼저 (추천) / 문장만 그대로 / 다른 생각?</b><div class="lines s"></div></div>
<div class="q"><b>D3. 드릴 7단계 &mdash; 이대로? (6단계 &ldquo;Write it&rdquo;은 화면에서 오선을 탭해서 음표를 놓는 새 방식)</b><div class="lines s"></div></div>
<div class="q"><b>D4. 새 5챕터 이름: &ldquo;The Whole Staff / 오선 전체 읽기&rdquo; 괜찮을까요?</b><div class="lines s"></div></div>
"""

pages = [page(cover, 'p. 1'), page(act_page, 'p. 2'), page(dec_page, 'p. 3')]
open('front.html', 'w').write(doc(pages))
print('front.html written')
