# Chapter 2 review pack: front pages (cover, A, B) + the drill page, as HTML for Chromium to print
import os
NM = os.path.abspath('../node_modules/@fontsource')
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
    return f'<section class="pg">{inner}<div class="foot"><span>Piano Butler · Chapter 4 review · Reading the Staff</span><span>{foot}</span></div></section>'

def doc(pages):
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'

tick = '<div class="tick"><span></span>Fix it &nbsp;&nbsp;<span></span>No / differently</div>'

cover = """
<div class="k">PIANO BUTLER · CHAPTER-BY-CHAPTER REVIEW · 2026-10-09</div>
<h1>Chapter 4 · Reading the Staff</h1>
<p class="sub">소현님의 <b>여왕과 왕 이야기</b>(높은음자리표 = G의 여왕, 소용돌이가 G 줄을 감싸요 / 낮은음자리표 = F의 왕, 두 점이 경비병)를 중심에 두고 새로 짰어요: 줄과 칸 → 오선 위로 = 피아노 위로(한 걸음·건너뛰기, 3챕터와 연결) → G의 여왕 → F의 왕 → 가운데 도(<span class="yel">클라라 공주, B1</span>), 거울처럼 접기 → 기준 음으로 빨리 읽기 → 다섯 가지 확인. 노래는 없어요(개념만). 덧줄은 가운데 도의 짧은 줄만, 나머지는 5챕터로. <span class="yel">노란 표시</span> = 답을 기다리는 부분.</p>
<div class="box">
  <h2>공개 가이드 페이지를 위한 질문 3개</h2>
  <div class="q"><b>Q1. 오선보 읽기에서 학생들이 가장 많이 막히는 곳은 어디인가요?</b> ("From the teacher" 칸)<div class="lines s"></div></div>
  <div class="q"><b>Q2. 음표를 빨리 읽게 만드는 소현님만의 방법이 있나요?</b> (여왕과 왕 이야기 말고도 있다면 — "Teacher's tip")<div class="lines s"></div></div>
  <div class="q"><b>Q3. 집에서는 음표 읽기를 어떻게 연습시키세요?</b> (플래시 카드? 하루 몇 분?)<div class="lines s"></div></div>
</div>
<div class="box">
  <h2>In this pack</h2>
  <table class="toc">
    <tr><td>A. What I found (8 items)</td><td class="n">p. 2</td></tr>
    <tr><td>B. Teaching questions (10)</td><td class="n">p. 3</td></tr>
    <tr><td><b>The new Lesson Book &mdash; draft</b> (yellow = waiting for B answers)</td><td class="n">p. 4&ndash;11</td></tr>
    <tr><td>The Workbook as it is today</td><td class="n">p. 12&ndash;21</td></tr>
    <tr><td>The Teacher copy as it is today</td><td class="n">p. 22&ndash;23</td></tr>
    <tr><td>The online lesson and the drill as they are today</td><td class="n">p. 24</td></tr>
  </table>
</div>
<div class="box how">
  <h2>How to mark</h2>
  <ul>
    <li>A 항목: <b>Fix it</b>에 체크하면 그대로 고칠게요. 다르게 고치고 싶으면 옆에 적어 주세요.</li>
    <li>B 질문: 한 줄이면 충분해요. "응"도 답이에요.</li>
    <li>레슨북 초안: 아무 쪽이나 빨간펜 환영 — 사진으로 보내시거나 채팅에 번호로 답해 주세요.</li>
  </ul>
</div>
"""

a_items = [
    ("A1", "<b>Ledger lines arrive early.</b> Drill level 3 is “Both clefs + ledger lines” and level 4 reaches notes above and below the staves; the grand-staff tool explains notes with two ledger lines. Chapter 5 is Ledger Lines.",
     "&rarr; Here only middle C's own short line; every other ledger-line note moves to chapter 5 (the levels in B6)."),
    ("A2", "<b>The alto clef.</b> Step 8 “A third clef” and the clef tool's alto tab teach the viola's C clef &mdash; not needed at the piano, not in the beginner syllabus.",
     "&rarr; Out of this chapter (B5)."),
    ("A3", "<b>The rhymes come before the clefs.</b> Step 2 teaches E G B D F / F A C E / G B D F A / A C E G before step 3 has said which clef they belong to.",
     "&rarr; Clefs first, then landmarks; the rhymes only if you want them (B2)."),
    ("A4", "<b>Middle C has three pictures.</b> Chapter 2 says “the ground”; the hands-and-clefs tool says “the city in the middle”; the Workbook's opener is a Sydney Harbour map with middle C as the Harbour Bridge to the CBD.",
     "&rarr; One storyline: the ground + Princess Clara (B1)."),
    ("A5", "<b>One chapter, four names.</b> The map: “Reading the Staff / 오선보 읽기”; the app lesson: “From the keyboard to the staff / 건반에서 오선보로”; the app's top bar: “Reading the staff”; the house room: “The staff / 오선”.",
     "&rarr; “Reading the Staff / 오선보 읽기” everywhere."),
    ("A6", "<b>Drill work inside the lesson.</b> Steps 6 “Fast flash cards” and 7 “Write them” are really the drill and the Workbook.",
     "&rarr; In the book-on-screen format: flash cards = the drill levels, writing notes = the Workbook pages (B7)."),
    ("A7", "<b>Two different rhymes for the same lines.</b> The app says “Every Good Boy Deserves <b>Fun</b>” and “<b>Great Big Dragon Flies Away</b>”; the draft's page 7 uses “&hellip;Deserves <b>Fruit</b>”.",
     "&rarr; One set of words, yours (B2)."),
    ("A8", "<b>Old Workbook.</b> 10 pages + check-up following the old 8 steps, old flat drawings; good activities inside: kebab/sandwich, Help the King get home (the F maze), the secret message, Fold the staff, note bingo, Compose your first tune.",
     "&rarr; When applied: one Workbook page facing each book page, pen drawings in the two inks, the good activities kept."),
]

a_page = '<div class="k">CHAPTER 4 REVIEW</div><h2>A. What I found</h2><p class="sub" style="font-size:10pt">각 항목: 그대로 고칠까요? 체크해 주세요.</p>' + ''.join(
    f'<div class="item"><div class="id">{i}</div><div class="t">{txt}<div class="fx">{fx}</div></div>{tick}</div>' for i, txt, fx in a_items)

b_items = [
    ("B1", "가운데 도 = <b>클라라 공주</b>(여왕과 왕 사이, 2챕터의 땅)로 갈까요? 그러면 워크북의 시드니 하버 지도(가운데 도 = 하버 브리지/CBD)와 “가운데 도시”는 빼요. (추천: 예)"),
    ("B2", "<b>줄 외우는 문장</b>(Every Good Boy&hellip;, FACE, Good Boys Deserve Fruit Always, All Cows Eat Grass): 7쪽에 작은 참고로만 / 아예 빼기 / 정식으로? 쓰신다면 어떤 문장인가요? (추천: 참고로만)"),
    ("B3", "기준 음: 여왕의 G, 왕의 F, 가운데 도 <b>세 개</b>만, 아니면 칸의 C 두 개(한 옥타브 위·아래)까지 <b>다섯 개</b>? (추천: 다섯, C 둘은 7쪽에서만)"),
    ("B4", "줄 음표 = <b>꼬치</b>, 칸 음표 = <b>샌드위치 속</b>, 그리고 <b>손 오선</b>(손가락 5개 = 줄 5개) &mdash; 쓰시나요? 다른 비유가 있으세요?"),
    ("B5", "<b>알토음자리표</b>: 이 챕터에서 빼기 (추천) &mdash; 나중에 “음악 알기” 단계에 한 줄로 둘까요?"),
    ("B6", "드릴 단계 제안: 1 줄일까 칸일까 · 2 한 걸음/건너뛰기, 위/아래 · 3 높은음자리표 음 · 4 낮은음자리표 음 · 5 두 음자리표와 가운데 도 · 6 건반에서 찾기. <b>덧줄 음은 5챕터로.</b>"),
    ("B7", "음표 <b>쓰기</b>는 워크북에서만 (레슨북은 줄 음표·칸 음표가 어떻게 생겼는지만)?"),
    ("B8", "“<b>큰보표</b>(grand staff)”라는 말은 여기서 쓰고, “<b>덧줄</b>(ledger line)”은 5챕터에서 처음 (여기서는 “가운데 도의 짧은 줄”)?"),
    ("B9", "6쪽의 <b>거울</b>(가운데 도에서 접으면 여왕의 G가 왕의 F에 겹쳐요, 양쪽으로 다섯 건반) &mdash; 이 챕터에 둘까요?"),
    ("B10", "8쪽 <b>다섯 가지 확인</b>(줄/칸 · 한 걸음/건너뛰기 · 여왕의 G · 왕의 F · 가운데 도와 기준 음) &mdash; 실제로 확인하실 다섯 가지와 맞나요?"),
]
b_page = '<div class="k">CHAPTER 4 REVIEW</div><h2>B. Teaching questions</h2><p class="sub" style="font-size:10pt">한 줄씩이면 충분해요.</p>' + ''.join(
    f'<div class="q"><b>{i}. {txt}</b><div class="lines s"></div></div>' for i, txt in b_items)

drill_page = """
<div class="k">CHAPTER 4 · AS IT IS TODAY</div><h2>The online lesson (8 steps) and the drill (4 levels)</h2>
<p class="sub" style="font-size:10pt">레슨 제목은 “From the keyboard to the staff”(A5), 2단계 문장이 음자리표보다 먼저(A3), 6&middot;7단계는 드릴과 워크북(A6), 8단계는 알토음자리표(A2). 드릴 3&middot;4단계는 덧줄 음까지(A1).</p>
<div class="grid3" style="grid-template-columns:1.1fr 1fr 1fr 1fr 1fr;gap:2.5mm">
  <div><img src="app-head.png"><div class="cap">The lesson today</div></div>
  <div><img src="drill-l1.png"><div class="cap">1 · Treble clef notes</div></div>
  <div><img src="drill-l2.png"><div class="cap">2 · Bass clef notes</div></div>
  <div><img src="drill-l3.png"><div class="cap">3 · Both + ledger lines (A1)</div></div>
  <div><img src="drill-l4.png"><div class="cap">4 · Find it on the keys</div></div>
</div>
"""

pages = [page(cover, 'p. 1'), page(a_page, 'p. 2'), page(b_page, 'p. 3'), page(drill_page, 'p. 24')]
open('front.html', 'w').write(doc(pages[:3]))
open('drillpg.html', 'w').write(doc([pages[3]]))
print('front.html + drillpg.html written')
