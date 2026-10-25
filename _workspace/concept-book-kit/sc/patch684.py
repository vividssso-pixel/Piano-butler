import sys, os
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
V = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'v684.jsx'), encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build V (her 2026-10-25 23:10-23:15, four notes):
# 1. 'the King and Queen home animation -- put it here' (the staff chapter's clef = piece pictures): SfClefHome, on screen.
rep("""function sfLbPages(scr = false) {""", V + """
function sfLbPages(scr = false) {""")
rep("""{pic2(clefIntro('treble'), p4, 290)}""", """{pic2(<LbLive still={clefIntro('treble')} live={<SfClefHome clef="treble"/>}/>, p4, 290)}""")
rep("""{pic2(clefIntro('bass'), p5, 290)}""", """{pic2(<LbLive still={clefIntro('bass')} live={<SfClefHome clef="bass"/>}/>, p5, 290)}""")

# 2. 'show high C and low C too: then the mirror image hits home' (Line and space names, the fold): the ledger Cs join the fold,
#    on screen, in the tool and on the page.
rep("""const FOLD_PAIRS = [   // Phase 419: the two space Cs meet; High C / Low C (two ledger lines) wait for chapter 6""",
    """const FOLD_PAIRS = [   // Phase 419: the two space Cs meet; Build V: High C / Low C (two ledger lines) fold in Line and space names too (FoldStaff ledger)""")
rep("""t('Like a paint print, now with the ledger Cs: ink on the treble side, fold along Clara\\'s ladder, and open it.', '데칼코마니처럼, 이번엔 덧줄의 C까지:""",
    """t('Like a paint print, now with high C and low C too, two ladders out: ink on the treble side, fold along Clara\\'s ladder, and open it.', '데칼코마니처럼, 이번엔 발판 둘 바깥의 높은 도와 낮은 도까지:""")
rep("""      <LbLive still={pic(p5, 250, 640)} live={<FoldStaff/>}/>""", """      <LbLive still={pic(p5, 250, 640)} live={<FoldStaff ledger/>}/>""")
rep("""C: () => <><ExplStaff3/><FoldStaff/></> },""", """C: () => <><ExplStaff3/><FoldStaff ledger/></> },""")
rep("""  const p5 = <SfStaff clef="grand" width={360} span={[4, 300]} pad={[24, 24]} label={t('The grand staff with a dashed fold line between the staves, at Clara\\'s ladder: folded, the Queen\\'s G lands on the King\\'s F, the C in the treble staff\\'s third space lands on the C in the bass staff\\'s second space, and middle C lands on middle C',""",
    """  const p5 = <SfStaff clef="grand" width={400} span={[4, 344]} pad={[24, 24]} label={t('The grand staff with a dashed fold line between the staves, at Clara\\'s ladder: folded, the Queen\\'s G lands on the King\\'s F, the C in the treble staff\\'s third space lands on the C in the bass staff\\'s second space, high C two ladders above lands on low C two ladders below, and middle C lands on middle C',""")
rep("""{ d: 35, x: 244, color: PEN_C }, { d: 21, x: 244, staff: 'bass', color: PEN_C }]}
    icons={[SF_ICON(clara, 304, 110, 0.7)]}""", """{ d: 35, x: 244, color: PEN_C }, { d: 21, x: 244, staff: 'bass', color: PEN_C }, { d: 42, x: 312, color: PEN_C }, { d: 14, x: 312, staff: 'bass', color: PEN_C }]}
    icons={[SF_ICON(clara, 352, 110, 0.7)]}""")
rep("""{[[92, 28, 28, ''], [168, 32, 24, ''], [244, 35, 21, '']].map(""", """{[[92, 28, 28, ''], [168, 32, 24, ''], [244, 35, 21, ''], [312, 42, 14, '']].map(""")
rep("""[244, 35, 'treble', 'C'], [244, 21, 'bass', 'C']].map(""", """[244, 35, 'treble', 'C'], [244, 21, 'bass', 'C'], [312, 42, 'treble', 'C'], [312, 14, 'bass', 'C']].map(""")
rep("""      return layer === 'under' ? <line x1="4" x2="300" y1={mid} y2={mid} stroke={BK.coral} strokeWidth="1.6" strokeDasharray="6 5"/>""",
    """      return layer === 'under' ? <line x1="4" x2="344" y1={mid} y2={mid} stroke={BK.coral} strokeWidth="1.6" strokeDasharray="6 5"/>""")
rep("""Clara lands on Clara. That makes <b>three Cs</b>: one up, Clara in the middle, one down.</>""",
    """Clara lands on Clara. That makes <b>three Cs</b>: one up, Clara in the middle, one down. And two ladders further out, <b>high C</b> lands on <b>low C</b>.</>""")
rep("""클라라는 클라라에 닿아요. 그래서 <b>C가 세 개</b>: 위에 하나, 가운데 클라라, 아래에 하나.</>""",
    """클라라는 클라라에 닿아요. 그래서 <b>C가 세 개</b>: 위에 하나, 가운데 클라라, 아래에 하나. 발판 둘 더 바깥에서는 <b>높은 도</b>가 <b>낮은 도</b>에 닿아요.</>""")

# 3. 'Loud & soft comes too late: before the staff' and 'Pitch is something to know on the side: put it in an attic'.
#    The Beginner floor: Loud & soft right after Notes & rests (before The staff); Pitch, Hz & range goes up to the attic, a room
#    above the floors, to explore any time (it keeps its pages; it is not part of a floor's order).
rep("""['posture-hands', 'first-steps', 'pulse', 'note-names', 'hand-positions', 'listen-sing', 'note-values', 'staff', 'reading-steps', 'whole-staff', 'time-signatures', 'dynamics', 'pitch-range', 'tones'], en: ['Beginner', 'Sitting and hands, the keys and their letters, beat and note values, listening and singing, the staff and the first tunes, loud and soft, high and low, half and whole steps.'], ko: ['Beginner', '자세와 손, 건반과 글자, 박과 음표 길이, 듣고 노래하기, 오선과 첫 선율, 셈여림, 높고 낮은 소리, 반음과 온음.'] },""",
    """['posture-hands', 'first-steps', 'pulse', 'note-names', 'hand-positions', 'listen-sing', 'note-values', 'dynamics', 'staff', 'reading-steps', 'whole-staff', 'time-signatures', 'tones'], en: ['Beginner', 'Sitting and hands, the keys and their letters, beat and note values, listening and singing, loud and soft, the staff and the first tunes, half and whole steps.'], ko: ['Beginner', '자세와 손, 건반과 글자, 박과 음표 길이, 듣고 노래하기, 셈여림, 오선과 첫 선율, 반음과 온음.'] },   // Build V: Loud & soft before the staff""")
rep("""  { ids: ['melody', 'composers', 'styles', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped, music through time, and more scales.'], ko: ['Grade 2–3', '선율의 모양, 시대별 음악, 그리고 더 많은 음계.'] },""",
    """  { ids: ['melody', 'composers', 'styles', 'more-scales'], en: ['Grades 2–3', 'How a tune is shaped, music through time, and more scales.'], ko: ['Grade 2–3', '선율의 모양, 시대별 음악, 그리고 더 많은 음계.'] },
  { ids: ['pitch-range'], attic: true, en: ['Attic', 'Rooms to explore any time: high and low, why a big instrument sounds low, and the instrument families.'], ko: ['다락방', '언제든 둘러볼 방: 높고 낮은 소리, 큰 악기가 낮은 소리를 내는 이유, 악기 가족.'] },   // Build V: the attic, above the floors""")
rep("""const houseFloors = (ko) => (ko ? ['', '한 층', '두 층', '세 층', '네 층', '다섯 층', '여섯 층', '일곱 층', '여덟 층', '아홉 층', '열 층'] : ['', 'one floor', 'two floors', 'three floors', 'four floors', 'five floors', 'six floors', 'seven floors', 'eight floors', 'nine floors', 'ten floors'])[PATH_STAGES.length] || PATH_STAGES.length + (ko ? '층' : ' floors');   // Build Q""",
    """const houseFloorsN = () => PATH_STAGES.filter(x => !x.attic).length;
const houseFloors = (ko) => { const n = houseFloorsN(), w = (ko ? ['', '한 층', '두 층', '세 층', '네 층', '다섯 층', '여섯 층', '일곱 층', '여덟 층', '아홉 층', '열 층'] : ['', 'one floor', 'two floors', 'three floors', 'four floors', 'five floors', 'six floors', 'seven floors', 'eight floors', 'nine floors', 'ten floors'])[n] || n + (ko ? '층' : ' floors');
  return PATH_STAGES.some(x => x.attic) ? w + (ko ? '과 다락방' : ' and an attic') : w; };   // Build Q; Build V: and the attic""")
rep("""const floorName = (k, caps) => { const s = PATH_STAGES[k], nm""", """const floorName = (k, caps) => { if (PATH_STAGES[k].attic) return caps ? 'ATTIC' : t('The attic', '다락방'); const s = PATH_STAGES[k], nm""")
rep("""t('Floor ' + (k + 1) + ' of ' + PATH_STAGES.length + ': ' + s.en[0], PATH_STAGES.length + '층 중 ' + (k + 1) + '층: ' + s.ko[0])""",
    """s.attic ? t('The attic: a room to explore any time', '다락방: 언제든 둘러볼 방') : t('Floor ' + (k + 1) + ' of ' + houseFloorsN() + ': ' + s.en[0], houseFloorsN() + '층 중 ' + (k + 1) + '층: ' + s.ko[0])""")
rep("""    const name = st.s ? (o.print || LANG !== 'ko' ? 'FLOOR ' : '')""", """    const name = st.s && st.s.attic ? (o.print || LANG !== 'ko' ? 'ATTIC' : '다락방') : st.s ? (o.print || LANG !== 'ko' ? 'FLOOR ' : '')""")
rep("""dynamics: ['reading-steps', 'time-signatures'], 'hand-positions': ['note-names'],""", """dynamics: ['note-values', 'hand-positions'], 'hand-positions': ['note-names'],""")
rep("""'piano-story': ['dynamics', 'pitch-range'],""", """'piano-story': ['dynamics'],""")   # the Pitch room is in the attic now
#    Loud & soft before the staff: its tunes (right hand, C position) carry the finger numbers over the notes, and the tie is met
#    here first (Time signatures then takes it over the bar line).
rep("""function SdyStaff({ items, clef = 'treble', width = 400, o = {}, k = {}, label, extra, full, pad, room = 0 }) {   // room: more space above, for a word""",
    """function SdyStaff({ items, clef = 'treble', width = 400, o = {}, k = {}, label, extra, full, pad, room = 0, fing }) {   // room: more space above, for a word; fing (Build V): C position finger numbers over the notes""")
rep("""  const p = pad || [Math.max(12, hi - mk.top + 6) + room, Math.max(12, mk.bottom - lo + 6)];""", """  const p = pad || [Math.max(12, hi - mk.top + 6) + room + (fing ? 26 : 0), Math.max(12, mk.bottom - lo + 6)];""")
rep("""      return <g><g dangerouslySetInnerHTML={{ __html: mm.raw + mk2.raw }}/>{extra && extra(yOf, txt, mm, mk2)}</g>; }}/></div>;""",
    """      let fg = null; if (fing) { const ns = mm.notes.filter(n => n.d >= 28 && n.d <= 32), fy = Math.min(yOf(38, clef), ...ns.map(n => (n.up ? n.end : n.y - 8))) - 12; mm.fingY = fy;
        fg = ns.map((n, i) => <g key={'f' + i}><circle cx={n.x} cy={fy} r="7.2" fill="#fff" stroke={BK.coral} strokeWidth="1.3"/><text x={n.x} y={fy + 3.7} textAnchor="middle" fontSize="10.5" fontWeight="900" fill={BK.coral} style={{fontFamily:'Inter, sans-serif'}}>{n.d - 27}</text></g>); }
      return <g><g dangerouslySetInnerHTML={{ __html: mm.raw + mk2.raw }}/>{fg}{extra && extra(yOf, txt, mm, mk2)}</g>; }}/></div>;""")
rep("""function SdySystems({ rows, clef = 'treble', os = [], ks = [], labels = [], extras = [], gap = 8 }) {""", """function SdySystems({ rows, clef = 'treble', os = [], ks = [], labels = [], extras = [], gap = 8, fing }) {""")
rep("""label={labels[i]} extra={extras[i]} room={extras[i] ? 16 : 0}/>)}</div>;""", """label={labels[i]} extra={extras[i]} room={extras[i] ? 16 : 0} fing={fing}/>)}</div>;""")
a = s.index('function sdyLbPages(scr = false) {'); b = s.index('\nfunction ', a + 10)
body = s[a:b]
assert body.count('<SdySystems rows=') == 5 and body.count('<SdyStaff full room={4}') == 1
body = body.replace('<SdySystems rows=', '<SdySystems fing rows=').replace('<SdyStaff full room={4}', '<SdyStaff fing full room={4}')
body = body.replace("""<text x={mm.notes[0].x - 16} y={yOf(38) - 12} textAnchor="start\"""", """<text x={mm.notes[0].x - 16} y={mm.fingY != null ? mm.fingY - 14 : yOf(38) - 12} textAnchor="start\"""")
for o_, n_ in [("""<>{RHC}: play the top tune {dm('p')}, fingertips close to the keys and the arm light.</>""", """<>{RHC}, the finger numbers over the notes: play the top tune {dm('p')}, fingertips close to the keys and the arm light.</>"""),
               ("""<>{RHC}: 위 악보를 {dm('p')}로 쳐요. 손끝은 건반 가까이 두고, 팔은 가볍게 해요.</>""", """<>{RHC}, 음표 위의 손가락 번호대로: 위 악보를 {dm('p')}로 쳐요. 손끝은 건반 가까이 두고, 팔은 가볍게 해요.</>"""),
               ("""['붙임줄', '같은 음 두 개를 잇는 곡선(' + bkChapterNo('time-signatures') + '챕터). 첫 음만 치고, 두 음의 길이만큼 누르고 있어요.'],""", """['붙임줄', '같은 음 두 개를 잇는 곡선. 첫 음만 치고, 두 음의 길이만큼 누르고 있어요.'],"""),
               ("""['tie', 'A curve joining two of the same note (chapter ' + bkChapterNo('time-signatures') + '). Play the first, then hold it for both.'],""", """['tie', 'A curve joining two of the same note. Play the first, then hold it for both.'],""")]:
    assert body.count(o_) == 1, o_[:60]; body = body.replace(o_, n_)
s = s[:a] + body + s[b:]

# 4. 'which room is rhythm, which is pitch? a selector to see just the rhythm rooms': the house's topic chips (HouseTopics, v684.jsx)
rep("""  const label = num + '. ' + t(nm[0], nm[1] || nm[0]) + (done ? t(', done'""", """  if (view.focus && thArea(id) !== view.focus) s += '<rect x="' + pFix(x + 1) + '" y="' + pFix(y + 1) + '" width="' + pFix(w - 2) + '" height="' + pFix(h - 2) + '" fill="#fff" opacity="0.78" stroke="none"/>';   // Build V: another topic's room, paled
  const label = num + '. ' + t(nm[0], nm[1] || nm[0]) + (done ? t(', done'""")
rep("""  const [inside, setInside] = useState(() => houseCameIn);""", """  const [inside, setInside] = useState(() => houseCameIn);
  const [topic, setTopic0] = useState(() => { try { return localStorage.getItem(HOUSE_TOPIC_KEY) || null; } catch (e) { return null; } });   // Build V
  const setTopic = (v) => { setTopic0(v); try { if (v) localStorage.setItem(HOUSE_TOPIC_KEY, v); else localStorage.removeItem(HOUSE_TOPIC_KEY); } catch (e) {} };""")
rep("""  const sig = stages.map(x => x.st.join(',')).join('|') + here + LANG + compact + name + today + fontTick + wide;
  const view = { stages, here, nums, pawn: name ? (x, y, k) => stPiece(VIC_PAWN_NAVY, x, y, k) : null };""",
    """  const sig = stages.map(x => x.st.join(',')).join('|') + here + LANG + compact + name + today + fontTick + wide + (topic || '');
  const view = { stages, here, nums, focus: topic, pawn: name ? (x, y, k) => stPiece(VIC_PAWN_NAVY, x, y, k) : null };""")
rep("""        <div ref={houseRef} data-house-view role="group\"""", """        {inside && !compact && <HouseTopics value={topic} onChange={setTopic}/>}
        <div ref={houseRef} data-house-view role="group\"""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
