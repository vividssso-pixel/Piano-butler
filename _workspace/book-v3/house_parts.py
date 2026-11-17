# Her 17 Nov ("층별로 파트로 나눠지고 그 안에서 순서대로 가는게 더 깔끔할 것 같아. a"): the house's floors become the Handbook's
# parts, the rooms in book order, read from the top left. The grade each room first belongs to stays (the old grade floors
# are kept as HB_GRADE_FLOORS) and shows on the room; "My exam" dims the rooms a chosen grade does not need yet and the
# next room follows it. The ten Ear training rooms become one room (Ear games) with a grade picker; the review rooms
# leave the map (kept in the code). Pieces grow by part.
import sys, re
P = sys.argv[1]; h = open(P).read()
def rep(a, b, n=1):
    global h
    assert h.count(a) == n, (a[:90], h.count(a)); h = h.replace(a, b)

# 1. the grade floors keep their data under a new name; the part floors are built from the rooms
rep('const HB_FLOORS = [{"ids": ["hbr-B1"', 'const HB_GRADE_FLOORS = [{"ids": ["hbr-B1"')
i = h.index('const HB_GRADE_FLOORS = '); j = h.index('\n', i)
NEW = r'''
// her 17 Nov: the floors are the Handbook's parts, the rooms in book order; the grade floors above give each room its grade
const ROOM_GRADE = {}; HB_GRADE_FLOORS.forEach(f => f.ids.forEach(id => { if (!ROOM_GRADE[id]) ROOM_GRADE[id] = f.en[0]; }));
const HB_GRADES = HB_GRADE_FLOORS.map(f => f.en[0]);
const HB_EAR_HUB = 'hbr-ear-beginner';
const HB_PARTS = [['BP', 'Before you play', '연주 전에'], ['P', 'Pitch', '음높이'], ['T', 'Time', '박과 리듬'], ['B', 'Bars and repeats', '마디와 반복'], ['E', 'Expression', '표현'], ['S', 'Scales and keys', '음계와 조'], ['H', 'Chords', '화음'], ['M', 'Harmony in music', '음악 속 화성'], ['F', 'Shape and style', '형식과 양식'], ['L', 'Playing and listening', '연주와 듣기'], ['G', 'Going further', '더 나아가기']];
const hbChNo = (ch) => parseInt(String(ch).replace(/^[A-Z]+/, ''), 10) || 0;
const HB_FLOORS = HB_PARTS.map(([pre, en, ko]) => {
  const rs = HB_ROOMS.filter(r => !r.review && !r.ear && r.ch && (pre === 'BP' ? r.ch === 'BP' : r.ch !== 'BP' && r.ch.replace(/\d+$/, '') === pre)).sort((a, b) => hbChNo(a.ch) - hbChNo(b.ch));
  const ids = rs.map(r => r.id); if (pre === 'L') ids.push(HB_EAR_HUB);
  const part = rs[0] && rs[0].part ? rs[0].part : [en, ko];
  return { ids, en: [en, part[0]], ko: [ko, part[1]], part: pre };
});
const HB_ROOM_NO = {}; HB_FLOORS.forEach(f => f.ids.forEach((id, j) => { const r = HB_ROOMS.find(x => x.id === id); HB_ROOM_NO[id] = id === HB_EAR_HUB ? '♪' : f.part === 'BP' ? '★' : (r && r.num) || j + 1; }));
const EXAM_KEY = 'pb_exam_v1';
const loadExam = () => { try { const v = localStorage.getItem(EXAM_KEY) || ''; return HB_GRADES.includes(v) ? v : ''; } catch (e) { return ''; } };
const examOK = (id, ex) => !ex || !ROOM_GRADE[id] || HB_GRADES.indexOf(ROOM_GRADE[id]) <= HB_GRADES.indexOf(ex);'''
h = h[:j] + NEW + h[j:]

# 2. the Ear training and Review rooms read their grade from the room, not the floor; the room links keep the grade floors
rep("const fl = (HB_FLOORS.find(f => f.ids.includes(r.id)) || { en: [''] }).en[0]", "const fl = ROOM_GRADE[r.id] || ''", 2)
rep("order = HB_FLOORS.flatMap((f, k) => f.ids.map(id => [id, k]));", "order = HB_GRADE_FLOORS.flatMap((f, k) => f.ids.map(id => [id, k]));")
rep("return hit ? { id: hit[0], floor: HB_FLOORS[hit[1]].en[0] } : null; };", "return hit ? { id: hit[0], floor: HB_GRADE_FLOORS[hit[1]].en[0] } : null; };")

# 3. one Ear games room: the grade's listening games, picked inside
rep("function HbRoom({ r }) { return r.ear ? <HbEar r={r}/>",
    "function HbEarHub() {   // her 17 Nov: the ten Ear training rooms in one room on the Playing and listening floor\n"
    "  const ears = HB_ROOMS.filter(x => x.ear); const [g, setG] = useState(() => { const ex = loadExam(); const r = ex && ears.find(x => ROOM_GRADE[x.id] === ex); return r ? r.id : HB_EAR_HUB; });\n"
    "  const r = ears.find(x => x.id === g) || ears[0];\n"
    "  return <div><div style={{display:'flex',flexWrap:'wrap',gap:6,margin:'0 0 12px'}}>{ears.map(x => <button key={x.id} type=\"button\" className={'chip' + (x.id === g ? ' active' : '')} data-ear-grade={ROOM_GRADE[x.id]} onClick={() => setG(x.id)} style={{fontSize:12.5,padding:'4px 10px'}}>{lvlName(ROOM_GRADE[x.id])}</button>)}</div><HbEar key={r.id} r={r}/></div>;\n"
    "}\n"
    "function HbRoom({ r }) { return r.id === HB_EAR_HUB ? <HbEarHub/> : r.ear ? <HbEar r={r}/>")

# 4. the room's second line: its Handbook page and its grade (was the part's name; Bar lines said "Start here" by mistake)
rep(": r.ch === 'B1' ? ['Start here', '여기서 시작'] : r.again ? ['Again: ' + r.again[0], '다시: ' + r.again[1]] : [r.part[0].split(' · ').pop(), r.part[1].split(' · ').pop()]; });",
    ": r.again ? ['Again: ' + r.again[0], '다시: ' + r.again[1]] : ['p. ' + r.pages + ' · ' + (ROOM_GRADE[r.id] || ''), r.pages + '쪽 · ' + (ROOM_GRADE[r.id] || '')]; if (r.id === HB_EAR_HUB) { CH_SHORT[r.id] = ['Ear games', '청음 게임']; CH_SUB[r.id] = ['Beginner to Grade 8', 'Beginner부터 Grade 8까지']; } });")

# 5. the house drawing: rooms read from the top left; two to a row on phones; the room's own number; dimmed rooms; counts
rep("const m = o.wide ? 6 : cmp ? 4 : 3, nr = Math.ceil(n / m)", "const m = o.wide ? 6 : cmp ? 2 : 3, nr = Math.ceil(n / m)")
rep("body += thRoom(view, state, id, L0 + cc * rw, yy + LH + (nr - 1 - r) * rh, rw, rh, fs, out, o.dimNew, lay, cmp);",
    "body += thRoom(view, state, id, L0 + cc * rw, yy + LH + (HB_HOUSE ? r : nr - 1 - r) * rh, rw, rh, fs, out, o.dimNew, lay, cmp);   // her 17 Nov: book order, top left first")
rep("s += stSquare(x + pad, y + pad, sq, num, done ? ST.G : null, cmp ? 9 : 11);",
    "s += stSquare(x + pad, y + pad, sq, view.disp && view.disp[id] != null ? view.disp[id] : num, done ? ST.G : null, cmp ? 9 : 11);")
rep("  if (view.lock && view.lock(id)) { const lx",
    "  if (view.dim && view.dim(id)) s += '<rect x=\"' + pFix(x + 1) + '\" y=\"' + pFix(y + 1) + '\" width=\"' + pFix(w - 2) + '\" height=\"' + pFix(h - 2) + '\" fill=\"#fff\" opacity=\"0.72\" stroke=\"none\"/>';   // her 17 Nov: not needed for My exam yet\n  if (view.lock && view.lock(id)) { const lx")
rep("      const dn = st.st.filter(v => v === 'done').length;\n      body += stT(L1 - 8, yy + (cmp ? 15.2 : 18.4), dn + '/' + n + '  ▸', { size: cmp ? 10 : 11.5, weight: 800, font: TH_SANS, fill: dn === n ? ST.G : '#6d6f9c', anchor: 'end' });",
    "      const sel = view.dim ? st.st.filter((v, j) => !view.dim(st.ids[j])) : st.st, dn = sel.filter(v => v === 'done').length, nn = sel.length;   // her 17 Nov: with My exam, the rooms that exam needs\n      body += stT(L1 - 8, yy + (cmp ? 15.2 : 18.4), (nn ? dn + '/' + nn : '–') + '  ▸', { size: cmp ? 10 : 11.5, weight: 800, font: TH_SANS, fill: nn && dn === nn ? ST.G : '#6d6f9c', anchor: 'end' });")
rep("  { wp: 'damask', fl: 'planks', lamp: 'globe' }         // 10 (Build CC: Prelim and Grade 1 are a floor each)\n];",
    "  { wp: 'damask', fl: 'planks', lamp: 'globe' },        // 10 (Build CC: Prelim and Grade 1 are a floor each)\n  { wp: 'regency', fl: 'herring', lamp: 'chandelier' }  // 11 (her 17 Nov: eleven part floors)\n];")

# 6. the map: My exam, the next room within it, the room numbers and dimming handed to the drawing
rep("  const here = last && all.includes(last) && chapterState(last).status !== 'done' ? last : placeNext(all, id => chapterState(id).status !== 'done');\n  const link = loadStoredLink()",
    "  const [exam, setExam] = useState(loadExam);   // her 17 Nov: My exam\n  const setEx = (g) => { try { localStorage.setItem(EXAM_KEY, g); } catch (e) {} setExam(g); setOpenK(null); };\n"
    "  const here = last && all.includes(last) && chapterState(last).status !== 'done' && examOK(last, exam) ? last : placeNext(all, id => chapterState(id).status !== 'done' && examOK(id, exam)) || placeNext(all, id => chapterState(id).status !== 'done');\n  const link = loadStoredLink()")
rep("+ Object.keys(star).join(',') + placeReview().join(',');", "+ Object.keys(star).join(',') + placeReview().join(',') + exam;")
rep("focus: null, star, review: placeReview(), lock:", "focus: null, disp: HB_HOUSE ? HB_ROOM_NO : null, dim: HB_HOUSE && exam ? (id) => !examOK(id, exam) : null, star, review: placeReview(), lock:")
rep("        {false && inside && !compact && <HouseTopics value={topic} onChange={setTopic}/>}",
    "        {HB_HOUSE && inside && !compact && <div data-testid=\"my-exam\" style={{display:'flex',flexWrap:'wrap',gap:5,alignItems:'center',margin:'0 0 12px'}}><span style={{fontSize:12.5,fontWeight:800,color:'#6d6f9c',marginRight:2}}>{t('My exam:', '내 시험:')}</span>{['', ...HB_GRADES].map(g => <button key={g || 'all'} type=\"button\" className={'chip' + (g === exam ? ' active' : '')} aria-pressed={g === exam} data-exam={g || 'all'} onClick={() => setEx(g)} style={{fontSize:12.5,padding:'3px 10px'}}>{g ? lvlName(g) : t('All', '전체')}</button>)}</div>}\n"
    "        {false && inside && !compact && <HouseTopics value={topic} onChange={setTopic}/>}")

# 7. pieces grow by part: Pawn on the first two floors, then a Knight on Time, a Bishop on Expression, a Rook on Chords, a Queen on Shape and style
rep("function pieceOfRoom(id) {\n", "function pieceOfRoom(id) {\n  if (HB_HOUSE) { const k = Math.max(0, PATH_STAGES.findIndex(st => st.ids.includes(id))); return k <= 1 ? 'pawn' : k <= 3 ? 'knight' : k <= 5 ? 'bishop' : k <= 7 ? 'rook' : 'queen'; }\n")
rep("const PIECE_FROM = { pawn: 'Beginner', knight: 'Grade 2', bishop: 'Grade 4', rook: 'Grade 6', queen: 'Grade 8' };",
    "const PIECE_FROM = HB_HOUSE ? { pawn: 'Before you play', knight: 'Time', bishop: 'Expression', rook: 'Chords', queen: 'Shape and style' } : { pawn: 'Beginner', knight: 'Grade 2', bishop: 'Grade 4', rook: 'Grade 6', queen: 'Grade 8' };")
rep("'You start as a pawn and grow as you climb: a Knight on Grade 2, a Bishop on 4, a Rook on 6, and on Grade 8 you are crowned Queen.', '폰으로 시작해서 올라갈수록 자라요: Grade 2에서 나이트, 4에서 비숍, 6에서 룩, Grade 8에서 퀸이 돼요.'",
    "HB_HOUSE ? 'You start as a pawn and grow as you climb: a Knight on the Time floor, a Bishop on Expression, a Rook on Chords, and on Shape and style you are crowned Queen.' : 'You start as a pawn and grow as you climb: a Knight on Grade 2, a Bishop on 4, a Rook on 6, and on Grade 8 you are crowned Queen.', HB_HOUSE ? '폰으로 시작해서 올라갈수록 자라요: 박과 리듬 층에서 나이트, 표현 층에서 비숍, 화음 층에서 룩, 형식과 양식 층에서 퀸이 돼요.' : '폰으로 시작해서 올라갈수록 자라요: Grade 2에서 나이트, 4에서 비숍, 6에서 룩, Grade 8에서 퀸이 돼요.'")
rep("' · next: ' + PIECE_NAME[nx][0] + ' on ' + PIECE_FROM[nx], ' · 다음: ' + PIECE_FROM[nx].replace('Level', '레벨') + '에서 ' + PIECE_NAME[nx][1])",
    "' · next: ' + PIECE_NAME[nx][0] + ' on ' + (HB_HOUSE ? 'the ' + PIECE_FROM[nx] + ' floor' : PIECE_FROM[nx]), ' · 다음: ' + (HB_HOUSE ? (HB_PARTS.find(x => x[1] === PIECE_FROM[nx]) || [0, 0, PIECE_FROM[nx]])[2] + ' 층' : PIECE_FROM[nx].replace('Level', '레벨')) + '에서 ' + PIECE_NAME[nx][1])")

# 8. a teacher's old plan named a grade floor: the part floors start from the bottom; the Library tags rooms by grade
rep("const placeFloor = () => { const pl = loadPlan();", "const placeFloor = () => { if (HB_HOUSE) return 0; const pl = loadPlan();")
rep("tag={stageOfChapter(id) >= 0 ? lvlName(PATH_STAGES[stageOfChapter(id)].en[0]) : GRADE_TAGS[id]}",
    "tag={HB_HOUSE && ROOM_GRADE[id] ? lvlName(ROOM_GRADE[id]) : stageOfChapter(id) >= 0 ? lvlName(PATH_STAGES[stageOfChapter(id)].en[0]) : GRADE_TAGS[id]}")
open(P, 'w').write(h); print('house by parts applied')
