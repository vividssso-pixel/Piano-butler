#!/usr/bin/env python3
# Phase 476 (her 2026-10-17 02:05 '1.2.3. 다동의해': the macro-first plan): the twelve keys first, then the parts, then
# the twelve keys again, in chapters 16 (Scales) and 19 (Key Signatures); the student's keys, set by the teacher.
#   keymap476.jsx: the keys store and the [keys:...] line; the keyboard clock (KeyRing) and the circle of fifths
#   (FifthsRing); the two map pads; the drills' 'My keys' levels; the Workbooks' any-key pages
# Chapter 16: the opener's picture is the keyboard clock with C major's shape (on screen the map pad); the screen lesson
#   ends with the map again (with the scale stamps); level 10 'My keys'; the Workbook's any-key page before the check-up.
# Chapter 19: the opener's picture is the circle of fifths (the chapter's five keys filled; on screen the map pad); the
#   screen lesson ends with it again (with the keys I know); level 10 'My keys'; the any-key page; the Teacher copy gets a
#   third page (any key, the check-up, the drill, the five checks).
# The Today page keeps the teacher's [keys:...] line out of the homework list and stores its keys; "Not me" forgets them.
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
def between(a, b, new):   # replace from a (inclusive) up to b (exclusive)
    global s
    i = s.index(a); j = s.index(b, i)
    if s.count(a) != 1: raise SystemExit('not unique: ' + a[:60])
    s = s[:i] + new + s[j:]
add = open(here + '/keymap476.jsx', encoding='utf-8').read() + '\n'

# 1. the new code before the Lesson Book registry
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); s = s[:i] + add + s[i:]

# 2. chapter 16's opener: the keyboard clock with C major's shape and a key to it; on screen the map pad
LINE = lambda col, w: "<svg width=\"22\" height=\"8\" viewBox=\"0 0 22 8\" style={{verticalAlign:'middle',marginRight:5}}><line x1=\"2\" y1=\"4\" x2=\"20\" y2=\"4\" stroke={" + col + "} strokeWidth=\"" + w + "\" strokeLinecap=\"round\"/></svg>"
between("  // p1: C major on the staff and on the keys, numbered 1 to 8, each note over its key\n", "  // p2: the steps of C major\n",
"""  // p1 (Phase 476, macro first): the twelve keys as a keyboard clock, C major drawn as one shape; on screen the map pad
  const p1 = <LbLive still={<LbPic h={410}><div role="img" aria-label={t('The keyboard clock: the piano’s twelve keys in a ring, white and black, C at the top, clockwise up. C major is drawn as one shape across seven of them; its two half steps, E to F and B to C, in coral. Turned, the same shape starts on any key.', '건반 시계: 열두 건반이 피아노처럼 흰건반과 검은건반으로 원을 이루고, 맨 위에 C가 있어요. C장조는 일곱 건반을 잇는 모양 하나로 그려져 있고, 반 걸음 둘(E에서 F, B에서 C)은 산호색이에요. 모양을 돌리면 어느 건반에서나 시작해요.')} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:6,width:'100%'}}>
    <div aria-hidden="true" style={{width:'100%',maxWidth:330}}><KeyRing sel="C" o={{ shape: true, center: (C) => <><text x={C} y={C - 4} textAnchor="middle" fontSize="22" fontWeight="900" fill={PEN_N} style={{fontFamily:"'Playfair Display', Georgia, serif"}}>C</text><text x={C} y={C + 18} textAnchor="middle" fontSize="13" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{t('major', '장조')}</text></> }}/></div>
    <div aria-hidden="true" style={{display:'flex',gap:18,justifyContent:'center',flexWrap:'wrap',fontSize:12.5,fontWeight:800,color:BK.muted}}><span>""" + LINE('PEN_N', '2') + """{t('whole step', '온 걸음')}</span><span>""" + LINE('PEN_C', '3.4') + """{t('half step', '반 걸음')}</span><span><svg width="14" height="14" viewBox="0 0 14 14" style={{verticalAlign:'-2px',marginRight:5}}><circle cx="7" cy="7" r="5.5" fill={PEN_N}/></svg>{t('the first note', '첫 음')}</span></div>
    <div style={{fontSize:14,fontWeight:800,color:BK.ink,textAlign:'center',maxWidth:480,lineHeight:1.4,textWrap:'balance'}}>{t('The piano’s twelve keys in a ring, clockwise up: after B comes C again. Turned, C major’s shape starts on any key.', '피아노의 열두 건반을 둥글게 이었어요. 시계 방향으로 가면 올라가고, B 다음은 다시 C예요. C장조의 모양을 돌리면 어느 건반에서나 시작해요.')}</div></div></LbPic>} live={<SscMapPad/>}/>;
""")
# 3. chapter 16's screen lesson ends with the map again (a seventh step, screen only; the step ticks keep their places)
i = s.index('function SscLearn'); a = """        </Step>
      ))}
    </Lesson>"""; j = s.index(a, i)
s = s[:j] + """        </Step>
      ))}
      <Step key="map" extra title={t('My twelve keys', '나의 열두 조')}><SscMapPad end/></Step>
    </Lesson>""" + s[j + len(a):]
# 4. chapter 16's level 10: the student's keys
rep("  { n: 9, label: 'Extra: harmonic minor, the raised 7th', kind: 'minor7', time: 9 },\n];",
    "  { n: 9, label: 'Extra: harmonic minor, the raised 7th', kind: 'minor7', time: 9 },\n  { n: 10, label: 'My keys: the scale notes', kind: 'mykeys', time: 10 },\n];")
rep("'Extra: harmonic minor, the raised 7th': '더 해 보기: 화성단음계의 올린 7번 음',", "'Extra: harmonic minor, the raised 7th': '더 해 보기: 화성단음계의 올린 7번 음', 'My keys: the scale notes': '나의 조: 음계의 음 맞히기',")
rep("function genSscQuestion(lv, prev) {\n", "function genSscQuestion(lv, prev) {\n  if (lv.kind === 'mykeys') return genMyScaleQ(prev);\n")
rep("function sscAnswerLabel(q) {\n", "function sscAnswerLabel(q) {\n  if (q.kind === 'mykeys') return myScaleLabel(q);\n")
rep("Object.assign(SCALES_DRILL, { levels: SSC_LEVELS, generate: genSscQuestion, check: sscCheck, answerLabel: sscAnswerLabel, Question: SscQuestion, Learn: SscLearn });",
    "const SscQuestionAll = (p) => p.q && p.q.kind === 'mykeys' ? <MyScaleQuestion {...p}/> : <SscQuestion {...p}/>;\nObject.assign(SCALES_DRILL, { levels: SSC_LEVELS, generate: genSscQuestion, check: sscCheck, answerLabel: sscAnswerLabel, Question: SscQuestionAll, Learn: SscLearn });")
# 5. chapter 16's any-key page, before the check-up; the Teacher copy's page numbers follow
rep("  // 7. the check-up on paper\n  P(<SscPaperCheck/>);", "  // 7. any key (Phase 476): the teacher writes the key; 8. the check-up on paper\n  P(<SscAnyKeyPage/>);\n  P(<SscPaperCheck/>);")
i = s.index('function SscTeacher'); j = s.index("<TcBlock page={7} title=\"The check-up on paper (the Workbook's last page)\"", i)
s = s[:j] + """<TcBlock page={7} title="Any key (photocopy it for each new key)" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.5}}>For whichever key you write at the top (set in Log lesson › For the student › Keys). Its notes and fingering: the Scale finder (toolbox). Keep the student's first copy as the record: colour a key on its clock when that scale is solid with each hand. Fingering groups: C, G, D, A and E share both hands (right hand 1 2 3 1 2 3 4 5, left hand 5 4 3 2 1 3 2 1); B the same right hand (left hand 4 3 2 1 4 3 2 1); F the same left hand (right hand 1 2 3 4 1 2 3 4); B♭, E♭, A♭ and D♭ share the left hand 3 2 1 4 3 2 1 3, and every black-key right hand starts on 2.</div>}/>
    <TcBlock page={8} title="The check-up on paper (the Workbook's last page)\"""" + s[j + len("<TcBlock page={7} title=\"The check-up on paper (the Workbook's last page)\""):]
rep("The drill comes after page 6; levels 8 and 9 (D and B♭ major, the harmonic minors) are extra.</div>",
    "The drill comes after page 6; levels 8 and 9 (D and B♭ major, the harmonic minors) are extra; level 10: the student’s own keys. The keyboard clock: Lesson Book page 1, the end of the screen lesson, Workbook page 7.</div>")

# 6. chapter 19's opener: the circle of fifths, the chapter's five keys filled; on screen the map pad
between("  // p1: a tune in G major on two lines of music, the key signature at the start of each; every F (in coral) is F♯.\n", "  // p2: one sharp on the F line: both Fs sharp\n",
"""  // p1 (Phase 476, macro first): the twelve major keys round the circle of fifths, this chapter's five filled; on screen the map pad
  const p1 = <LbLive still={<LbPic h={360}><div role="img" aria-label={t('The circle of fifths: the twelve major keys in a ring, C at the top with no sharps or flats; from there, clockwise one more sharp each step, anticlockwise one more flat. This chapter’s five keys, C, G, D, F and B flat, are filled.', '5도권: 열두 장조가 원을 이루고, 맨 위의 C는 샤프도 플랫도 없어요. 시계 방향으로 한 칸마다 샤프가 하나씩, 반시계 방향으로 한 칸마다 플랫이 하나씩 늘어요. 이 챕터의 다섯 조 C, G, D, F, B♭은 칠해져 있어요.')} style={{display:'flex',flexDirection:'column',alignItems:'center',gap:4,width:'100%'}}>
    <div aria-hidden="true" style={{width:'100%',maxWidth:330}}><FifthsRing o={{ filled: SKG_FIVE }}/></div>
    <div style={{fontSize:14,fontWeight:800,color:BK.ink,textAlign:'center',maxWidth:480,lineHeight:1.4,textWrap:'balance'}}>{sscSx(t('Twelve major keys, each with its key signature. This chapter teaches the five filled.', '장조는 열두 개, 조마다 조표가 있어요. 이 챕터에서는 칠해진 다섯 조를 배워요.'))}</div></div></LbPic>} live={<SkgMapPad/>}/>;
""")
# 7. chapter 19's screen lesson ends with the map again
rep("""        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order: which key (1), what it changes (2)""", """        <Step key={i} title={<span>{pg.props.title}</span>} storeAs={'k' + (i + 1)}>
          <LbScreenPage page={pg}/>
        </Step>
      ))}
      <Step key="map" extra title={t('My twelve keys', '나의 열두 조')} storeAs="k7"><SkgMapPad end/></Step>
    </Lesson>
  );
}

// ── the drill, after page 6, in the book's order: which key (1), what it changes (2)""")
# 8. chapter 19's level 10
rep("  { n: 9, label: 'Extra: three sharps or flats', kind: 'three', time: 10 },\n];",
    "  { n: 9, label: 'Extra: three sharps or flats', kind: 'three', time: 10 },\n  { n: 10, label: 'My keys: name the key', kind: 'mykeys', time: 10 },\n];")
rep("  'Extra: three sharps or flats': '더 해 보기: 샤프나 플랫 셋',", "  'Extra: three sharps or flats': '더 해 보기: 샤프나 플랫 셋', 'My keys: name the key': '나의 조: 조 이름 맞히기',")
rep("function genSkgQuestion(lv, prev) {\n", "function genSkgQuestion(lv, prev) {\n  if (lv.kind === 'mykeys') return genMyKeySigQ(prev);\n")
rep("function skgAnswerLabel(q) {\n", "function skgAnswerLabel(q) {\n  if (q.kind === 'mykeys') return myKeySigLabel(q);\n")
rep("Object.assign(KEYSIG_DRILL, { levels: SKG_LEVELS, generate: genSkgQuestion, check: skgCheck, answerLabel: skgAnswerLabel, Question: SkgQuestion, Learn: SkgLearn });",
    "const SkgQuestionAll = (p) => p.q && p.q.kind === 'mykeys' ? <MyKeySigQuestion {...p}/> : <SkgQuestion {...p}/>;\nObject.assign(KEYSIG_DRILL, { levels: SKG_LEVELS, generate: genSkgQuestion, check: skgCheck, answerLabel: skgAnswerLabel, Question: SkgQuestionAll, Learn: SkgLearn });")
# 9. chapter 19's any-key page; the Teacher copy's third page: any key, the check-up, the drill, the five checks
rep("  // 7. the check-up on paper\n  P(<SkgPaperCheck/>);", "  // 7. any key (Phase 476): the teacher writes the key; 8. the check-up on paper\n  P(<SkgAnyKeyPage/>);\n  P(<SkgPaperCheck/>);")
i = s.index('function SkgTeacher'); a = "    <TcBlock page={7} title=\"The check-up on paper (the Workbook's last page)\""; j = s.index(a, i)
s = s[:j] + """  </>);
  P(<>
    <TcBlock page={7} title="Any key (photocopy it for each new key)" answers={<div style={{fontSize:12,color:BK.ink,lineHeight:1.55}}>{sscSx('For whichever key you write at the top (the student’s keys: Log lesson › For the student › Keys). How many signs: the number by the key on the circle at the foot of the page; then that many, in order (E major, four sharps: F♯ C♯ G♯ D♯; A♭ major, four flats: B♭ E♭ A♭ D♭). Treble sharps: F top line, C third space, G the space above the staff, D fourth line, A second space, E top space. Treble flats: B middle line, E top space, A second space, D fourth line, G second line, C third space. Bass staff: every sign two places lower (a line to the line below, a space to the space below). The scale’s notes: the Scale finder (toolbox). F♯ and G♭ share the bottom of the circle: write which one you mean. Keep the student’s first copy as the record: colour a key on its circle once they can draw its key signature and name it.')}</div>}/>
    <TcBlock page={8} title="The check-up on paper (the Workbook's last page)\"""" + s[j + len(a):]
rep("Not here: minor keys and the relative minor, all seven sharps and flats, the circle of fifths (all in the toolbox); A and E♭ major are drill level 9 (extra).')}</div>",
    "Not here: minor keys. A and E♭ major: drill level 9 (extra); level 10: the student’s own keys. The circle of fifths: Lesson Book page 1, the end of the screen lesson, Workbook page 7; C♯ and C♭ major (seven signs) are not on it.')}</div>")
rep("7 listening (screen only) · 8 the bass staff · 9 extra: A and E♭ major.')}</div>", "7 listening (screen only) · 8 the bass staff · 9 extra: A and E♭ major · 10 the student’s keys.')}</div>")

# 10. the Today page: the teacher's [keys:...] line is not homework to tick; its keys are stored ([keys:-]: cleared)
rep("  return String(text || '').split(/\\r?\\n/).map(x => x.replace(/^\\s*(?:[-*•·]|\\d+[.)])\\s+/, '').trim()).filter(Boolean).slice(0, 12).map(line => {",
    "  return String(text || '').split(/\\r?\\n/).map(x => x.replace(/^\\s*(?:[-*•·]|\\d+[.)])\\s+/, '').trim()).filter(x => x && !HW_KEYS_RE.test(x)).slice(0, 12).map(line => {")
rep("        setData(r.data); setStatus('ok'); keep(r.data);\n",
    "        setData(r.data); setStatus('ok'); keep(r.data);\n        try { const mk = pbKeysFromHomework(r.data.lesson && r.data.lesson.homework); if (mk) { if (mk.length) pbSetMyKeys(mk); else pbClearMyKeys(); } } catch (e) {}\n")
# 11. "Not me" / another student's link on this device: the keys go with the rest of the student's things
rep("  [SYNC_OWNER_KEY, SYNC_REVS_KEY, SYNC_DIRTY_KEY, SYNC_LOGQ_KEY, TODAY_CACHE_KEY, TODAY_TICKS_KEY].forEach(syDel);",
    "  [SYNC_OWNER_KEY, SYNC_REVS_KEY, SYNC_DIRTY_KEY, SYNC_LOGQ_KEY, TODAY_CACHE_KEY, TODAY_TICKS_KEY, 'pb_my_keys_v1'].forEach(syDel);")
# 12. a step marked extra (the closing maps) is not counted: a chapter finished before Phase 476 stays finished
rep("  const count = steps.filter((s, i) => done[sk(i)]).length;\n  useEffect(() => { try { const m = loadStepTotals(); if (m[id] !== steps.length) { m[id] = steps.length; localStorage.setItem(STEPS_TOTAL_KEY, JSON.stringify(m)); } } catch (e) {} }, [id, steps.length]);",
    "  const counted = steps.map((x, i) => i).filter(i => !(steps[i].props && steps[i].props.extra)), nTot = counted.length;   // Phase 476: an extra step is not counted\n  const count = counted.filter(i => done[sk(i)]).length;\n  useEffect(() => { try { const m = loadStepTotals(); if (m[id] !== nTot) { m[id] = nTot; localStorage.setItem(STEPS_TOTAL_KEY, JSON.stringify(m)); } } catch (e) {} }, [id, nTot]);")
rep("{t(count + ' of ' + steps.length + ' steps done', steps.length + '개 중 ' + count + '개 완료')}", "{t(count + ' of ' + nTot + ' steps done', nTot + '개 중 ' + count + '개 완료')}")
# 13. the Today page's circle of fifths is a circle (the keyboard clock is chapter 16's)
rep("t('Tap a key on the clock, then stamp it when it’s solid.', '시계에서 조를 누르고, 확실해지면 도장을", "t('Tap a key on the circle, then stamp it when it’s solid.', '원에서 조를 누르고, 확실해지면 도장을")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
