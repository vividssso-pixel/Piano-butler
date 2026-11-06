#!/usr/bin/env python3
# Phase 472 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'; Book rules 14 and 15; the level plan of Phase 435):
# chapter 17, Accidentals, a new room on Level 3 after Scales, built in full: the Lesson Book (dictionary entries), its
# screen lesson (the book with a listen-and-tap pad on pages 2 to 6), a 9-level drill, the Workbook and the Teacher copy.
# The room joins the map (PATH_STAGES already lists it; it waited for its chapter): every chapter after it moves up one.
#   sacbook472.jsx: the tune staff with its signs (SacStaff), the keyboard (SacKeys), the Lesson Book
#   sacapp472.jsx:  the pads of pages 2 to 6, SacLearn, the drill (Object.assign on SAC_DRILL)
#   sacwb472.jsx:   the Workbook (pages 2 to 7) and the Teacher copy
# Base: Phase 471 (chapter 9's sskRaw draws the tunes; chapter 11's tnAcc the signs; chapter 16's sscT the words).
import sys
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
add = ''.join(open(here + '/' + f, encoding='utf-8').read() + '\n' for f in ['sacbook472.jsx', 'sacapp472.jsx', 'sacwb472.jsx'])

# 1. the new code before the Lesson Book registry; accidentals joins the books
a = "const LESSON_BOOKS = { 'posture-hands': PostureLessonBook,"
i = s.index(a); j = s.index('};', i) + 2
line = s[i:j]
if not line.endswith("scales: ScalesLessonBook };"): raise SystemExit('LESSON_BOOKS line changed')
s = s[:i] + add + line.replace(" };", ", accidentals: AccidentalsLessonBook };") + s[j:]
rep("rhythm: srhLbPages, scales: sscLbPages };", "rhythm: srhLbPages, scales: sscLbPages, accidentals: sacLbPages };")

# 2. the chapter: its drill concept (filled in by sacapp472.jsx), its place after Scales, its names, grade, category, words
rep("const DRILLS = [ // Phase 361: in the music map's order", "const SAC_DRILL = { id: 'accidentals', label: 'Accidentals' };   // Phase 472: filled in with the chapter's code\nconst DRILLS = [ // Phase 361: in the music map's order")
rep("  { id: 'scales', label: 'Scales', concept: SCALES_DRILL, track: 'pitch' },", "  { id: 'scales', label: 'Scales', concept: SCALES_DRILL, track: 'pitch' },\n  { id: 'accidentals', label: 'Accidentals', concept: SAC_DRILL, track: 'pitch' },")
rep("'tones': '온음과 반음', 'scales': '스케일',", "'tones': '온음과 반음', 'scales': '스케일', 'accidentals': '임시표',")
rep("tones: 'Prelim–G1', scales: 'Prelim–G3',", "tones: 'Prelim–G1', accidentals: 'Prelim–G1', scales: 'Prelim–G3',")
rep("  'tones': 'tones', 'intervals': 'intervals',", "  'tones': 'tones', 'accidentals': 'tones', 'intervals': 'intervals',")
rep("scales: ['scales', 'key-signatures'] };", "scales: ['scales', 'key-signatures'], tones: ['tones', 'accidentals'] };")
rep("  'tones': 'tone semitone half step whole step tone sharp flat natural accidental enharmonic chromatic',", "  'tones': 'tone semitone half step whole step tone sharp flat enharmonic chromatic',\n  'accidentals': 'accidental sharp flat natural bar line cancel sign same line space octave reading',")
rep("  { name: 'Grade 1–2', ids: ['intervals', 'scales',", "  { name: 'Grade 1–2', ids: ['accidentals', 'intervals', 'scales',")
rep("  { name: 'Preliminary', ids: ['staff', 'whole-staff', 'ledger-lines', 'tones',", "  { name: 'Preliminary', ids: ['staff', 'whole-staff', 'ledger-lines', 'tones', 'accidentals',")
rep("'ledger-lines': ['Ledger lines', '덧줄'],", "'ledger-lines': ['Ledger lines', '덧줄'], 'accidentals': ['Accidentals', '임시표'],")
rep('const HOUSE_ICONS = {"posture-hands":', 'const HOUSE_ICONS = {"accidentals": "<path d=\\"M19 3 V25 M29 11 V33\\"/><path d=\\"M19 15 L29 11 M19 25 L29 21\\" stroke-width=\\"3.2\\"/>", "posture-hands":')
rep("const STAFF_ART = {", """const STAFF_ART = {
  // an accidental lasts until the bar line: F sharp, F sharp again, then a plain F in the next bar
  'accidentals': () => <g>
    <AClef/>
    <ASharp x={92} y={62} c={ART_C}/><ANote x={110} y={62} c={ART_C}/>
    <ANote x={150} y={58}/><ANote x={190} y={62} c={ART_C}/>
    <ABar x={226}/><ANote x={262} y={62}/>
    <AText x={190} y={94} size={11} c={ART_C} serif={false} weight={700}>F♯</AText><AText x={262} y={94} size={11} serif={false} weight={700}>F</AText>
  </g>,""")

# 3. the toolbox: this room's five pads. Chapter 11's two older accidental tools stay there (they also show key signatures);
# their bar-line line no longer says the bar line 'wipes it clean' (a tied note keeps its sign)
rep("A natural cancels it; the next bar line wipes it clean.', '그 마디 안에서 같은 줄이나 칸에 나오는 이후 음표도 모두 바뀌어요. 내추럴이 취소시키고, 다음 세로줄이 되면 깨끗이 지워져요.'", "A natural cancels it; after the bar line the note is plain again (a note tied over the bar line keeps it).', '그 마디 안에서 같은 줄이나 칸에 나오는 이후 음표도 모두 바뀌어요. 내추럴이 취소시키고, 세로줄 다음에는 다시 원래 음이에요(붙임줄로 이어진 음표는 그대로예요).'", 2)
rep("return t('New bar: the bar line wipes it clean. Plain F.', '새 마디: 세로줄이 깨끗이 지워요. 그냥 F.');", "return t('New bar: plain F again.', '새 마디: 다시 그냥 F.');")
rep("  { id: 'tone-semitone', ch: 'tones',", """  { id: 'sac-signs', ch: 'accidentals', title: 'Play sharps and flats', blurb: 'F♯, B♭, C♯ on the staff and the keys: listen, then play them.', C: () => <SacPad page={2}/> },
  { id: 'sac-natural', ch: 'accidentals', title: 'The natural', blurb: 'B♭, then B♮: the natural brings back the plain note.', C: () => <SacPad page={3}/> },
  { id: 'sac-bar', ch: 'accidentals', title: 'Until the bar line', blurb: 'A sign lasts to the end of its bar; after the bar line the note is plain again.', C: () => <SacPad page={4}/> },
  { id: 'sac-line', ch: 'accidentals', title: 'Its own line or space', blurb: 'The high F keeps its sharp; the low F stays plain.', C: () => <SacPad page={5}/> },
  { id: 'sac-tune', ch: 'accidentals', title: 'Read the tune', blurb: 'Four bars with F♯ and E♭: listen, then play.', C: () => <SacPad page={6}/> },
  { id: 'tone-semitone', ch: 'tones',""")
rep("  'accidental-cards': ['임시표: 샤프, 플랫, 내추럴',", """  'sac-signs': ['샤프와 플랫 치기', '오선과 건반의 F♯, B♭, C♯: 듣고 쳐 봐요.'],
  'sac-natural': ['내추럴', 'B♭ 다음 B♮: 내추럴은 원래 음으로 돌려놓아요.'],
  'sac-bar': ['세로줄까지', '임시표는 그 마디 끝까지 효과가 있고, 다음 마디는 임시표 없이 시작해요.'],
  'sac-line': ['같은 줄이나 칸만', '높은 F는 아직 F♯, 낮은 F는 그대로 F예요.'],
  'sac-tune': ['선율 읽기', 'F♯와 E♭이 있는 네 마디: 듣고 쳐 봐요.'],
  'accidental-cards': ['임시표: 샤프, 플랫, 내추럴',""")
rep("  'tone-semitone': ['tones', 1, 1, 'show game'],", "  'sac-signs': ['tones', 1, 2, 'game ear'], 'sac-natural': ['tones', 1, 2, 'game ear'], 'sac-bar': ['tones', 1, 2, 'game ear'], 'sac-line': ['tones', 1, 2, 'game ear'], 'sac-tune': ['tones', 1, 2, 'game ear'],\n  'tone-semitone': ['tones', 1, 1, 'show game'],")
rep("['srh-read', 'rhythm-cards-all'],", "['srh-read', 'rhythm-cards-all'], ['sac-signs', 'accidental-cards'], ['sac-natural', 'sharp-flat'], ['sac-bar', 'accidental-bar'], ['sac-line', 'accidental-bar'], ['sac-tune', 'ssk-read'],")
rep("  'tones': ['tone-semitone', 'accidental-cards', 'sharp-flat', 'accidental-bar', 'chromatic'],", "  'tones': ['tone-semitone', 'accidental-cards', 'sharp-flat', 'accidental-bar', 'chromatic'],\n  'accidentals': ['sac-signs', 'sac-natural', 'sac-bar', 'sac-line', 'sac-tune'],")
# 4. chapter 16's pads: one stable stop function each, released when not sounding (a stale one could stop another pad)
rep("  const stopMe = () => { clear(); setLit(null); setMsg(''); setMode(null); };\n  useEffect(() => () => { clear(); if (SSC_STOP.fn === stopMe) SSC_STOP.fn = null; }, []);",
    "  const meRef = useRef(null);\n  meRef.current = () => { clear(); setLit(null); setMiss(null); setMsg(''); setMode(null); };\n  const me = useRef(() => meRef.current()).current;\n  const release = () => { if (SSC_STOP.fn === me) SSC_STOP.fn = null; };\n  useEffect(() => () => { clear(); release(); }, []);")
rep("    if (SSC_STOP.fn && SSC_STOP.fn !== stopMe) SSC_STOP.fn(); SSC_STOP.fn = stopMe;", "    if (SSC_STOP.fn && SSC_STOP.fn !== me) SSC_STOP.fn(); SSC_STOP.fn = me;")
rep("    timers.current.push(setTimeout(() => { setLit(null); setMsg(''); setMode(null); }, order.length * SSC_GAP + 200));", "    timers.current.push(setTimeout(() => { release(); setLit(null); setMsg(''); setMode(null); }, order.length * SSC_GAP + 200));")
rep("  function tapMode() { clear(); setMode('tap');", "  function tapMode() { clear(); release(); setMode('tap');")
# 5. chapter 11's keyboard: an opt-in ring on every white key too, so a dot can go on any key (this chapter's Workbook)
rep("rings = [], gaps = [], slots = false }) {\n  const s0 = TN_WL.indexOf(start)", "rings = [], gaps = [], slots = false, wslots = false }) {\n  const s0 = TN_WL.indexOf(start)")
rep("      {Object.entries(labels).filter(([k]) => k[0] === 'b').map(([k, v]) => <text key={k} x={cx(k)} y={T - 4}",
    "      {wslots && Array.from({ length: whites }, (_, i) => !youW.includes('w' + i) && !dots.includes('w' + i) && <circle key={'ws' + i} cx={2 + (i + 0.5) * w} cy={T + h - 18} r={w * 0.17} fill=\"none\" stroke={BK.ink} strokeWidth=\"0.9\" strokeOpacity=\"0.45\"/>)}\n      {Object.entries(labels).filter(([k]) => k[0] === 'b').map(([k, v]) => <text key={k} x={cx(k)} y={T - 4}")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
