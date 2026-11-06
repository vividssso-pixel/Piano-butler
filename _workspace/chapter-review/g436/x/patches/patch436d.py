#!/usr/bin/env python3
# Phase 436d: the path in five levels (Sohyun 2026-10-11 11:19 "좋아. 그렇게 해보자", 2026-10-12 12:08 "너 의견에 맞춰가자"):
# the floors of the house are levels 1-5, the rooms the chapters in the plan's order (plan435/levels.json), free order
# inside a floor; "LEVEL n" / "n층" everywhere a stage name stood; the finished books count their chapters from the
# path (no fixed numbers in the text); one gentle "easier after" line on a chapter opened early (plan C5).
import sys, json
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit('count %d != %d for: %s' % (c, n, a[:100]))
    s = s.replace(a, b)

# 1. the levels
old_start = "const PATH_STAGES = [\n  { cats: ['body', 'keys'],"
i = s.find(old_start); j = s.find("];\n", i)
if i < 0 or s.count(old_start) != 1: raise SystemExit('PATH_STAGES')
LV = [
 (['posture-hands', 'first-steps', 'pulse', 'note-names', 'note-values', 'staff'],
  'Sitting well, the keys and their letters, a steady beat, the first note values and the staff.', '바른 자세, 건반과 글자, 일정한 박, 처음 음표 길이, 그리고 오선.'),
 (['whole-staff', 'time-signatures', 'reading-steps', 'dynamics', 'tones', 'pitch-range'],
  'Both staves, bar lines and time signatures, the first tunes, loud and soft, half and whole steps, high and low.', '두 오선, 마디줄과 박자표, 첫 선율, 셈여림, 반 걸음과 온 걸음, 높고 낮은 소리.'),
 (['tempo', 'rhythm', 'ledger-lines', 'scales', 'accidentals', 'piano-story'],
  'Speed, quavers and dots, ledger lines, scales, accidentals, and the piano’s own story.', '빠르기, 8분음표와 점, 덧줄, 스케일, 임시표, 그리고 피아노 이야기.'),
 (['key-signatures', 'signs', 'intervals', 'chords', 'composers', 'melody'],
  'Key signatures, signs, intervals and chords, the composers, and how a tune is shaped.', '조표, 기호, 음정과 화음, 작곡가, 그리고 선율의 모양.'),
 (['form', 'terms', 'styles'],
  'How pieces are built, the Italian terms, and the styles of music.', '곡의 짜임, 이탈리아어 용어, 그리고 음악의 스타일.'),
]
body = "const PATH_STAGES = [   // Phase 436: five levels, the floors of the house, in the plan's order; inside a floor any room first\n"
for k, (ids, en, ko) in enumerate(LV):
    body += "  { ids: " + json.dumps(ids).replace('"', "'").replace("', '", "', '") + ", en: ['Level " + str(k + 1) + "', '" + en + "'], ko: ['" + str(k + 1) + "층', '" + ko + "'] },\n"
s = s[:i] + body + s[j:]
rep("const pathStageIds = (s) => s.cats.flatMap(catChapterIds).filter(id => DRILLS.find(d => d.id === id));",
    "const pathStageIds = (s) => s.ids.filter(id => DRILLS.find(d => d.id === id));   // a room waits off the map until its chapter exists (accidentals)")

# 2. the end of a chapter, the Start guide
rep("""{nk !== k ? t('You’ve reached the end of “' + s.en[0] + '”. Next stage: ' + PATH_STAGES[nk].en[0] + '.', '“' + s.ko[0] + '” 단계를 마쳤어요. 다음 단계: ' + PATH_STAGES[nk].ko[0] + '.') : t('Stage ' + (k + 1) + ' of ' + PATH_STAGES.length + ': ' + s.en[0], PATH_STAGES.length + '단계 중 ' + (k + 1) + '단계: ' + s.ko[0])}""",
    """{nk !== k ? t('That was the last room on ' + s.en[0] + '. Next floor: ' + PATH_STAGES[nk].en[0] + '.', s.ko[0] + '의 마지막 방이에요. 다음 층: ' + PATH_STAGES[nk].ko[0] + '.') : t(s.en[0] + ' of ' + PATH_STAGES.length, PATH_STAGES.length + '층 중 ' + s.ko[0])}""")
rep("""{t('Everything here follows one path: from the first lesson at the piano, through reading, rhythm and theory, to the music and composers behind it. Three things to know:', '여기 있는 모든 것은 하나의 길을 따라가요: 피아노 앞 첫 레슨부터 읽기, 리듬, 이론을 지나 음악과 작곡가 이야기까지. 알아 둘 세 가지:')}""",
    """{t('Everything here is one house: five floors, a room for each chapter. Start on Level 1 and go up floor by floor -- on each floor, any room first. Three things to know:', '여기 있는 모든 것은 집 한 채예요: 다섯 층, 챕터마다 방 하나. 1층에서 시작해 한 층씩 올라가요 -- 같은 층에서는 어느 방부터 해도 돼요. 알아 둘 세 가지:')}""")

# 3. the rooms' short names (plan C8)
rep("'tones': ['Sharps & flats', '올림·내림표']", "'tones': ['Tones & semitones', '온음과 반음']")
rep("'reading-steps': ['Steps & skips', '이웃음·건너뛰기']", "'reading-steps': ['Steps & skips', '걸음·건너뛰기']")

# 4. the house's words
rep("""T_('Start · climb up, one room at a time', '출발 · 한 방씩 위로 올라가요')""", """T_('Start · floor by floor, any room first', '출발 · 한 층씩, 방은 마음대로')""")
rep("""const TH_FLOOR = [   // per stage: wallpaper, floor, the stair's lamp""", """const TH_FLOOR = [   // per floor (Phase 436: levels 1-5 use the first five): wallpaper, floor, the stair's lamp""")
rep("""t('The Piano Butler’s house: every floor is a stage, every room is a chapter. Your butler meets you in the hall -- open the door and go up, floor by floor. New to the piano? Start on the first floor. Already playing? Go straight to any room, or carry on with the button.', '피아노 버틀러의 집: 층마다 단계 하나, 방마다 챕터 하나. 버틀러가 현관에서 맞아 줘요 -- 문을 열고 한 층씩 올라가요. 처음이라면 1층부터, 이미 배우고 있다면 어느 방으로든 바로 가거나 버튼을 눌러 이어서 해요.')""",
    """t('The Piano Butler’s house: five floors, a room for each chapter. Your butler meets you in the hall -- open the door and go up, floor by floor; on each floor, any room first. New to the piano? Start on Level 1. Already playing? Go straight to any room, or carry on with the button.', '피아노 버틀러의 집: 다섯 층, 챕터마다 방 하나. 버틀러가 현관에서 맞아 줘요 -- 문을 열고 한 층씩 올라가요. 같은 층에서는 어느 방부터 해도 돼요. 처음이라면 1층부터, 이미 배우고 있다면 어느 방으로든 바로 가거나 버튼을 눌러 이어서 해요.')""")
rep("""const intro = t('The Piano Butler’s house: every floor is a stage, every room is a chapter. Your butler meets you in the hall -- open the door and go up, floor by floor. New to the piano? Start on the first floor. Already playing? Go straight to any room.', '피아노 버틀러의 집: 층마다 단계 하나, 방마다 챕터 하나. 버틀러가 현관에서 맞아 줘요 -- 문을 열고 한 층씩 올라가요. 처음이라면 1층부터, 이미 배우고 있다면 어느 방으로든 바로 가요.');""",
    """const intro = t('The Piano Butler’s house: five floors, a room for each chapter. Your butler meets you in the hall -- open the door and go up, floor by floor; on each floor, any room first. New to the piano? Start on Level 1. Already playing? Go straight to any room.', '피아노 버틀러의 집: 다섯 층, 챕터마다 방 하나. 버틀러가 현관에서 맞아 줘요 -- 문을 열고 한 층씩 올라가요. 같은 층에서는 어느 방부터 해도 돼요. 처음이라면 1층부터, 이미 배우고 있다면 어느 방으로든 바로 가요.');""")
rep("""aria-label={t('The Piano Butler’s house: one floor for each stage, one room for each chapter', '피아노 버틀러의 집: 단계마다 층 하나, 챕터마다 방 하나')}""",
    """aria-label={t('The Piano Butler’s house: five floors, one room for each chapter', '피아노 버틀러의 집: 다섯 층, 챕터마다 방 하나')}""")

# 5. the small house in the books: "LEVEL n", up to six rooms a floor, each room's number and name centred in its cell
rep("""// The small map at the foot of a chapter's map page: one row per stage, a chess square with each chapter's number,
// your chapter in coral -- the same order as the app's house, stage 1 at the top.
function houseMiniShapes(current, W = 600) {
  const s = [], X0 = 4, HW = W - 8, SC = 118, FH = 19, TOP = 4;""",
"""// The small map at the foot of a chapter's map page: one row per level, a chess square with each chapter's number,
// your chapter in coral -- the same order as the app's house, level 1 at the top. Each room centred in its cell (Phase 436).
function houseMiniShapes(current, W = 600) {
  const s = [], X0 = 4, HW = W - 8, SC = 66, FH = 19, TOP = 4;""")
rep("""    const has = x.ids.includes(current), rw = (HW - SC) / 5;
    svg += stL(X0, y + FH, X0 + HW, y + FH, 0.6);
    svg += stT(X0 + 2, y + 13, (x.i + 1) + ' · ' + x.st.en[0].toUpperCase(), { size: 8.6, weight: 700, fill: has ? ST.C : ST.N, font: TH_CAPS, ls: '0.06em' });
    x.ids.forEach((id, j) => {
      const rx = X0 + SC + j * rw, on = id === current, nm = (CH_SHORT[id] || [bkChapterName(id)])[0];
      if (on) svg += '<rect x="' + pFix(rx) + '" y="' + pFix(y + 1.5) + '" width="' + pFix(rw - 3) + '" height="' + (FH - 3) + '" fill="#fff" stroke="' + ST.C + '" stroke-width="1.3"/>';
      svg += stSquare(rx + 2.5, y + 3.5, 12, nums[id], null, 8.5) + stT(rx + 18.5, y + 13.4, nm, { size: 11, weight: 700, fill: on ? ST.C : ST.N, font: TH_SERIF });
    });""",
"""    const has = x.ids.includes(current), rw = (HW - SC) / 6, nm = (id) => (CH_SHORT[id] || [bkChapterName(id)])[0];
    // one size on the row: the largest at which every name fits beside its number; else 10, a long name on two lines
    const one = (id, z) => 16 + rdWidth(nm(id), 700, z, TH_SERIF) <= rw - 8;
    let z = [11, 10.5, 10, 9.5].find(z => x.ids.every(id => one(id, z))), lines = {};
    if (z == null) z = 10;
    x.ids.forEach(id => { lines[id] = one(id, z) ? [nm(id)] : thWrap(nm(id), rw - 24, z, TH_SERIF).slice(0, 2); });
    const fh = FH + (x.ids.some(id => lines[id].length > 1) ? 11 : 0);
    svg += stL(X0, y + fh, X0 + HW, y + fh, 0.6);
    svg += stT(X0 + 2, y + 13, 'LEVEL ' + (x.i + 1), { size: 8.6, weight: 700, fill: has ? ST.C : ST.N, font: TH_CAPS, ls: '0.06em' });
    x.ids.forEach((id, j) => {
      const rx = X0 + SC + j * rw, on = id === current, ls = lines[id], cx = rx + (rw - 3) / 2, fill = on ? ST.C : ST.N;
      const gx = cx - (16 + rdWidth(ls[0], 700, z, TH_SERIF)) / 2;   // the number and the first line together, centred in the cell
      if (on) svg += '<rect x="' + pFix(rx) + '" y="' + pFix(y + 1.5) + '" width="' + pFix(rw - 3) + '" height="' + (fh - 3) + '" fill="#fff" stroke="' + ST.C + '" stroke-width="1.3"/>';
      svg += stSquare(gx, y + 3.5, 12, nums[id], null, 8.5) + stT(gx + 16, y + 13.4, ls[0], { size: z, weight: 700, fill, font: TH_SERIF });
      if (ls[1]) svg += stT(cx, y + 24.4, ls[1], { size: z, weight: 700, fill, font: TH_SERIF, anchor: 'middle' });
    });""")
rep("""    y += FH;
  });
  s.push({ k: 'raw', svg: stG(stL(X0, TOP, X0 + HW, TOP, 1.2) + svg""", """    y += fh;
  });
  s.push({ k: 'raw', svg: stG(stL(X0, TOP, X0 + HW, TOP, 1.2) + svg""")
rep("""<span style={{fontSize:10.5,color:BK.muted}}>every floor a stage, every room a chapter -- the same order as the app</span>""",
    """<span style={{fontSize:10.5,color:BK.muted}}>five floors, a room for each chapter -- the same order as the app</span>""")
rep("""Every floor is a stage and every room is a chapter, numbered 1 to 26. Your butler meets you in the hall: go up, floor by floor. When you""",
    """Every floor is a level and every room is a chapter, numbered 1 to {pathIds().length}. Your butler meets you in the hall: go up, floor by floor -- on each floor, any room first. When you""")

# 6. the finished books: chapter numbers from the path, not typed in
rep("""the letter names come in chapter 3.'""", """the letter names come in chapter ' + bkChapterNo('note-names') + '.'""")
rep("""음이름은 챕터 3에서 배워요.')""", """음이름은 챕터 ' + bkChapterNo('note-names') + '에서 배워요.')""")
rep("""<b>건너뛰기</b> -- 3챕터의 그 건너뛰기""", """<b>건너뛰기</b> -- {bkChapterNo('note-names')}챕터의 그 건너뛰기""")
rep("""the same skip as in Chapter 3, one letter""", """the same skip as in Chapter {bkChapterNo('note-names')}, one letter""")
rep("""{t('Chapter 5 · The Whole Staff -- """, """{t('Chapter ' + bkChapterNo('whole-staff') + ' · The Whole Staff -- """)
rep("""'5챕터 · 오선 전체 읽기 -- """, """bkChapterNo('whole-staff') + '챕터 · 오선 전체 읽기 -- """)
rep("""In Chapter 4 you read the nine notes""", """In Chapter ' + bkChapterNo('staff') + ' you read the nine notes""")
rep("""4챕터에서는 클라라 공주""", """' + bkChapterNo('staff') + '챕터에서는 클라라 공주""")
rep("""맨 아래 줄 바로 아래는 4챕터의 <b>D</b>""", """맨 아래 줄 바로 아래는 {bkChapterNo('staff')}챕터의 <b>D</b>""")
rep("""just under the bottom line is Chapter 4's <b>D</b>""", """just under the bottom line is Chapter {bkChapterNo('staff')}'s <b>D</b>""")
rep("""꼭대기 줄 바로 위는 4챕터의 <b>B</b>""", """꼭대기 줄 바로 위는 {bkChapterNo('staff')}챕터의 <b>B</b>""")
rep("""Just over the top line is Chapter 4's <b>B</b>""", """Just over the top line is Chapter {bkChapterNo('staff')}'s <b>B</b>""")
rep("""바로 위 칸은 5챕터의 <b>G</b>""", """바로 위 칸은 {bkChapterNo('whole-staff')}챕터의 <b>G</b>""")
rep("""바로 아래 칸은 5챕터의 <b>F</b>""", """바로 아래 칸은 {bkChapterNo('whole-staff')}챕터의 <b>F</b>""")
rep("""in the space, is Chapter 5's <b>G</b>""", """in the space, is Chapter {bkChapterNo('whole-staff')}'s <b>G</b>""")
rep("""in the space, is Chapter 5's <b>F</b>""", """in the space, is Chapter {bkChapterNo('whole-staff')}'s <b>F</b>""")
rep("""5챕터처럼 <b>클라라의 발판에서 접어</b>""", """{bkChapterNo('whole-staff')}챕터처럼 <b>클라라의 발판에서 접어</b>""")
rep("""like in Chapter 5, and they meet in pairs""", """like in Chapter {bkChapterNo('whole-staff')}, and they meet in pairs""")

# 7. "easier after" (plan C5): never a lock; a student sees it while those rooms are unfinished, a teacher always
rep("""// The end of every chapter: what comes next on the path.
function PathNext(""",
"""// Phase 436 (plan C5): the rooms a chapter is easier after. Never a lock: one gentle line at the top of the chapter,
// for a student only while one of those rooms is unfinished; a teacher always sees what the chapter builds on.
const ROOM_AFTER = { 'first-steps': ['posture-hands'], 'note-names': ['first-steps'], 'note-values': ['pulse'], staff: ['note-names'],
  'whole-staff': ['staff'], 'time-signatures': ['note-values', 'staff'], 'reading-steps': ['staff', 'time-signatures'], dynamics: ['first-steps', 'staff'], tones: ['whole-staff'], 'pitch-range': ['first-steps'],
  tempo: ['pulse'], rhythm: ['time-signatures'], 'ledger-lines': ['whole-staff'], scales: ['tones'], accidentals: ['tones', 'reading-steps'],
  'key-signatures': ['scales', 'accidentals'], signs: ['reading-steps', 'dynamics'], intervals: ['reading-steps', 'scales'], chords: ['intervals', 'key-signatures'], composers: ['piano-story'], melody: ['reading-steps', 'signs'],
  form: ['melody', 'signs'], terms: ['dynamics', 'tempo'], styles: ['composers'] };
function AfterNote({ id, onOpen }) {
  const ids = pathIds(), before = (ROOM_AFTER[id] || []).filter(x => ids.includes(x));
  const show = UI_TEACHER ? before : before.filter(x => chapterState(x).status !== 'done');
  if (!show.length) return null;
  const name = (x) => bkChapterNo(x) + ' · ' + (DRILLS.find(d => d.id === x) || {}).label;
  return (
    <div data-testid="after-note" style={{fontSize:13,color:'var(--navy-soft)',margin:'-4px 0 14px',lineHeight:1.45}}>
      {UI_TEACHER ? t('Builds on ', '바탕이 되는 방: ') : t('Easier after ', '먼저 하면 더 쉬워요: ')}
      {show.map((x, i) => <React.Fragment key={x}>{i > 0 && (LANG === 'ko' ? ' · ' : i === show.length - 1 ? ' and ' : ', ')}<button onClick={() => onOpen(x)} style={{border:'none',background:'none',padding:0,font:'inherit',fontWeight:800,color:'var(--navy)',textDecoration:'underline',textUnderlineOffset:2,cursor:'pointer'}}>{name(x)}</button></React.Fragment>)}
      {UI_TEACHER ? (LANG === 'ko' ? '' : '.') : t(' -- or carry on here.', ' -- 여기서 계속해도 돼요.')}
    </div>
  );
}
// The end of every chapter: what comes next on the path.
function PathNext(""")
rep("""        {concept ? (
          <>
            <ConceptView concept={concept}""",
"""        {!st.lock && <AfterNote id={active.id} onOpen={(id) => { update({ drill: id, tab: 'learn', level: 1 }); try { window.scrollTo(0, 0); } catch (e) {} }}/>}
        {concept ? (
          <>
            <ConceptView concept={concept}""")
open(out, 'w', encoding='utf-8').write(s); print('436d ok')
