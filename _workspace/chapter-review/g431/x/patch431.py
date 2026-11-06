#!/usr/bin/env python3
# Phase 431 (her 2026-10-12 06:38 notes on the chapter 6 PDF v2):
#  1. the cross on the 4th 'how to draw' picture (no lid) was cut off -- its picture was shorter at the top;
#  2. the opener shows Clara's C from both lands: under Queensland and over Kingsland;
#  3. question numbers no longer sit over the notes (they read like note labels): each number goes in the corner of
#     its answer box (SfRow, all Workbooks), and the 'e.g.' over the example is gone -- the coral box is the example;
#  4. the fold comes back (chapter 5's paint print waited for these ledger Cs): Five Cs is folded at Clara's ladder,
#     Sky C lands on Sea C; on screen FoldStaff takes the ledger pair too.
import sys, re
src, out = sys.argv[1], sys.argv[2]; s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('%r found %d' % (a[:90], s.count(a)))
    s = s.replace(a, b)

# ── 1. the lid picture: as tall at the top as the other three, so its cross fits
rep("<SfStaff clef=\"treble\" width={128} pad={[12, 18]} span={[4, 124]} label={cap} notes={[{ d: bad === 'lid' ? 41 : 42, x: 66 }]}",
    "<SfStaff clef=\"treble\" width={128} pad={[bad === 'lid' ? 17 : 12, 18]} span={[4, 124]} label={cap} notes={[{ d: bad === 'lid' ? 41 : 42, x: 66 }]}")

# ── 2. the opener: Clara's C under Queensland and over Kingsland, Clara between them
rep("{ d: 28, x: 112, color: PEN_C }, { d: 16, x: 214, staff: 'bass', color: PEN_C }",
    "{ d: 28, x: 112, color: PEN_C }, { d: 28, x: 112, staff: 'bass', color: PEN_C }, { d: 16, x: 214, staff: 'bass', color: PEN_C }")
rep("icons={[SF_ICON(bird, 286, 4, 1), SF_ICON(clara, 124, 84, 0.8),", "icons={[SF_ICON(bird, 286, 4, 1), SF_ICON(clara, 124, 112, 0.8),")
rep("between the lands Princess Clara stands by middle C on its short line;", "between the lands Princess Clara stands by middle C, written on its short line under Queensland and again over Kingsland;")
rep("두 나라 사이에는 클라라 공주가 가운데 도의 짧은 줄 옆에 서 있고,", "두 나라 사이에는 클라라 공주가 퀸즈랜드 아래와 킹스랜드 위, 두 번 쓴 가운데 도 옆에 서 있고,")

# ── 3. SfRow: the question number in the answer box's corner, not over the note
sfrow = s.index('function SfRow(')
rowline = re.compile(r"    \{items\.some\(it => it\.n != null\) && <div style=\{\{position:'relative',height:15\}\}>.*?</div>\}\n")
mm = rowline.search(s, sfrow); assert mm and mm.start() < sfrow + 600, 'number row'
s = s[:mm.start()] + s[mm.end():]
rep("    {items.some(it => it.box !== false) && <div style={{position:'relative',height:items.some(it => it.choose) ? 50 : boxH + 4,marginTop:3}}>{items.map((it, i) => it.box !== false && (it.choose",
    "    {items.some(it => it.box !== false || it.n != null) && <div style={{position:'relative',height:items.some(it => it.choose) ? 50 : boxH + 4,marginTop:3}}>{items.map((it, i) => it.box === false ? (it.n != null && <span key={i} style={{...SF_NUM,position:'absolute',left:pct(it.x),transform:'translateX(-50%)',top:4,fontSize:12}}>{it.n}</span>) : (it.choose")
rep("? <span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',top:0,display:'grid',gap:3,justifyItems:'center'}}>{[['step', 'skip']",
    "? <span key={i} style={{position:'absolute',left:pct(it.x),transform:'translateX(-50%)',top:0,display:'grid',gap:3,justifyItems:'center'}}>{it.n != null && !it.ex && <span style={{...SF_NUM,position:'absolute',left:-14,top:2}}>{it.n}</span>}{[['step', 'skip']")
rep("fontSize:it.w && it.w > 40 ? 13 : 16,fontWeight:900,color:BK.coral,whiteSpace:'nowrap'}}>{it.ex ? it.ans : ''}</span>))}</div>}",
    "fontSize:it.w && it.w > 40 ? 13 : 16,fontWeight:900,color:BK.coral,whiteSpace:'nowrap'}}>{it.ex ? it.ans : ''}{it.n != null && !it.ex && <span style={{...SF_NUM,position:'absolute',left:3,top:2}}>{it.n}</span>}</span>))}</div>}")
rep("function SfRow(", """// Phase 431 (Sohyun 2026-10-12: numbers over the notes read like note labels): a question's number sits in the
// corner of its answer box, crossword-style; the example (coral) box has none
const SF_NUM = { fontFamily: "'Playfair Display', Georgia, serif", fontStyle: 'italic', fontSize: 10, fontWeight: 700, lineHeight: 1, color: '#6d6f9c', fontVariantNumeric: 'lining-nums', pointerEvents: 'none' };
function SfRow(""")

# ── 4a. FoldStaff: the ledger pair (chapter 6) -- Sky C lands on Sea C
rep("""const FOLD_LINE_COLOR = '#4a63c9';""", """const FOLD_LINE_COLOR = '#4a63c9';
const FOLD_LEDGER = { d: 42, color: '#c0431f', get label() { return t('Sky C ↔ Sea C -- two ladders up, two ladders down', '하늘 C ↔ 바다 C -- 발판 둘 위, 발판 둘 아래'); } };   // Phase 431: chapter 6""")
rep("function FoldStaff() {", "function FoldStaff({ ledger = false }) {   // ledger: chapter 6 -- the Cs on two ladders meet too\n  const PAIRS = ledger ? [...FOLD_PAIRS, FOLD_LEDGER] : FOLD_PAIRS;")
rep("  const topY = dY(41), botY = dY(15);", "  const topY = dY(ledger ? 44 : 41), botY = dY(ledger ? 12 : 15);")
rep("          {FOLD_PAIRS.map((p, i) => ink(p.d, p.color, 150 + i * 60))}", "          {PAIRS.map((p, i) => ink(p.d, p.color, 150 + i * 60))}")
rep("          {printed && FOLD_PAIRS.map((p, i) => ink(56 - p.d, p.color, 150 + i * 60))}", "          {printed && PAIRS.map((p, i) => ink(56 - p.d, p.color, 150 + i * 60))}")
rep("        {FOLD_PAIRS.map(p => <div key={p.d}><span", "        {PAIRS.map(p => <div key={p.d}><span")

# ── 4b. the book's Five Cs page: folded at Clara's ladder
a = s.index("  // p6: the five Cs, from the sea to the sky -- rungs, space, rung, space, rungs; and a hop from each new C")
b = s.index("  // the check page's little pictures:")
s = s[:a] + r"""  // p6 (Phase 431): the five Cs, folded at Clara's ladder like chapter 5's paint print -- now the ledger Cs meet too:
  // Clara's C on Clara's C, Queensland C on Kingsland C, Sky C (two ladders up) on Sea C (two ladders down)
  const C5 = [[120, 28, 28, t('Clara\'s C', '클라라의 C'), t('Clara\'s C', '클라라의 C')], [210, 35, 21, t('Queensland C', '퀸즈랜드 C'), t('Kingsland C', '킹스랜드 C')], [300, 42, 14, t('Sky C', '하늘 C'), t('Sea C', '바다 C')]];
  const p6 = <SfStaff clef="grand" width={384} span={[4, 340]} pad={[24, 24]} label={t('The grand staff folded at Clara\'s ladder: a dashed fold line between the staves; the five Cs meet in pairs -- Clara\'s C under Queensland and over Kingsland, Queensland C in the third space and Kingsland C in the second space, Sky C on two ladders above Queensland and Sea C on two ladders below Kingsland', '클라라의 발판에서 접은 큰보표: 두 오선 사이의 접는 점선; 다섯 C가 짝을 지어 만나요 -- 퀸즈랜드 아래와 킹스랜드 위의 클라라의 C, 셋째 칸의 퀸즈랜드 C와 둘째 칸의 킹스랜드 C, 퀸즈랜드 위 두 발판의 하늘 C와 킹스랜드 아래 두 발판의 바다 C')}
    notes={C5.flatMap(([x, a, b2]) => [{ d: a, x, staff: 'treble', color: PEN_C }, { d: b2, x, staff: 'bass', color: PEN_C }])}
    icons={[SF_ICON(clara, 344, 104, 0.7)]}
    extra={(yOf, layer, txt) => { const mid = (yOf(30, 'treble') + yOf(26, 'bass')) / 2;
      return layer === 'under' ? <line x1="4" x2="340" y1={mid} y2={mid} stroke={BK.coral} strokeWidth="1.6" strokeDasharray="6 5"/>
      : <g style={txt}>
        {C5.map(([x, a, b2], i) => <path key={i} d={`M${x + 12} ${yOf(a, 'treble')} Q${x + 34 + i * 4} ${mid} ${x + 12} ${yOf(b2, 'bass')}`} fill="none" stroke={BK.ink} strokeWidth="1.2" strokeDasharray="3 3"/>)}
        {C5.flatMap(([x, a, b2, na, nb], i) => [[x, a, 'treble', na], [x, b2, 'bass', nb]]).map(([x, d, st, L], i) => <text key={'l' + i} x={x - 17} y={yOf(d, st) + 4} fontSize="10.5" fontWeight="900" fill={BK.coral} textAnchor="end">{L}</text>)}
        <text x="12" y={mid - 6} fontSize="9" fontWeight="900" fill={BK.coral}>{t('fold here', '여기서 접어요')}</text>
      </g>; }}/>;

""" + s[b:]

# the page: the words, the piano and the screen's moving parts
rep("""      <LbLive still={pic(p6, 300, 680)} live={<LlFiveCs/>}/>""", """      <LbLive still={pic(p6, 300, 640)} live={<><FoldStaff ledger/><LlFiveCs/></>}/>""")
rep("""바다에서 하늘까지 C가 다섯 개, 한 옥타브씩 떨어져 있어요: {A('B3', <b>바다 C</b>)}, <b>킹스랜드 C</b>, <b>클라라의 C</b>, <b>퀸즈랜드 C</b>, {A('B3', <b>하늘 C</b>)}. 자리는 발판, 칸, 발판, 칸, 발판 -- 번갈아 가요.""",
    """바다에서 하늘까지 C가 다섯 개, 한 옥타브씩 떨어져 있어요: {A('B3', <b>바다 C</b>)}, <b>킹스랜드 C</b>, <b>클라라의 C</b>, <b>퀸즈랜드 C</b>, {A('B3', <b>하늘 C</b>)}. 5챕터처럼 <b>클라라의 발판에서 접어</b> 보면 C끼리 짝을 지어 만나요: 퀸즈랜드 C는 킹스랜드 C에, 그리고 이제 <b>하늘 C는 바다 C</b>에 -- 발판 둘 위, 발판 둘 아래.""")
rep("""They take turns: ladders, space, ladder, space, ladders. Every ledger note""",
    """Fold at <b>Clara's ladder</b>, like in Chapter 5, and they meet in pairs: Queensland C on Kingsland C -- and now <b>Sky C on Sea C</b>, two ladders up, two ladders down. Every ledger note""")
rep("""        <>다섯 C를 낮은 데서 높은 데로 쳐요 -- 이름을 말하면서. 바다 C와 킹스랜드 C는 왼손, 나머지는 오른손.</>,""",
    """        <>다섯 C를 낮은 데서 높은 데로 쳐요 -- 이름을 말하면서. 바다 C와 킹스랜드 C는 왼손, 나머지는 오른손.</>,
        <><b>접기 짝:</b> 바다 C와 하늘 C를 두 손으로 같이, 그다음 킹스랜드 C와 퀸즈랜드 C, 마지막에 두 엄지로 클라라의 C -- 두 손이 접는 선으로 모여요.</>,""")
rep("""        <>Play the five Cs from low to high, naming each one -- Sea C and Kingsland C with the left hand, the others with the right.</>,""",
    """        <>Play the five Cs from low to high, naming each one -- Sea C and Kingsland C with the left hand, the others with the right.</>,
        <><b>Fold partners:</b> Sea C and Sky C together, then Kingsland C and Queensland C, then both thumbs on Clara's C -- the hands meet at the fold.</>,""")
open(out, 'w', encoding='utf-8').write(s); print('patched')
# ── 4c. in chapter 6's words: Clara's C, not middle C (the fold on screen)
s = open(out, encoding='utf-8').read()
rep("        {t('Like a paint print: put ink on the treble side, fold the paper along middle C, and open it.', '데칼코마니처럼: 높은음자리표 쪽에 물감을 묻히고, 가운데 도를 따라 종이를 접었다가 펼쳐요.')}",
    "        {ledger ? t('Like a paint print, now with the ledger Cs: ink on the treble side, fold along Clara\\'s ladder, and open it.', '데칼코마니처럼, 이번엔 덧줄의 C까지: 높은음자리표 쪽에 물감을 묻히고, 클라라의 발판을 따라 접었다가 펼쳐요.') : t('Like a paint print: put ink on the treble side, fold the paper along middle C, and open it.', '데칼코마니처럼: 높은음자리표 쪽에 물감을 묻히고, 가운데 도를 따라 종이를 접었다가 펼쳐요.')}")
rep("        <BoxLabel x={104} y={foldY} text={t('middle C', '가운데 도')} anchor=\"start\"/>",
    "        <BoxLabel x={104} y={foldY} text={ledger ? t('Clara\\'s C', '클라라의 C') : t('middle C', '가운데 도')} anchor=\"start\"/>")
open(out, 'w', encoding='utf-8').write(s); print('patched 4c')
