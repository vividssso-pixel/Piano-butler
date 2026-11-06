#!/usr/bin/env python3
# Phase 397: chapter 3 (The Musical Alphabet) applied -- the Lesson Book with Sohyun's notes on draft v2, the app lesson as
# the book on screen, the drill's levels (1 name, 2 find, 3 two octaves, 4 next letter, 5 skip a letter; the black-key
# level moves to Tones & Semitones), the Workbook and Teacher copy page by page.
#   python3 patch397.py <drills.src.html> <dir with nn397.lb.jsx, nn397.wb.jsx, nn397.wb2.jsx>
import sys, os
src, d = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
LB = open(os.path.join(d, 'nn397.lb.jsx'), encoding='utf-8').read()
WB = open(os.path.join(d, 'nn397.wb.jsx'), encoding='utf-8').read()
WB2 = open(os.path.join(d, 'nn397.wb2.jsx'), encoding='utf-8').read()

def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

def cut(start, end, new, what):
    """replace s[start:end) (end marker kept) with new"""
    global s
    i = s.find(start); j = s.find(end, i)
    if i < 0 or j < 0 or s.count(start) != 1: raise SystemExit(what + ': markers not found once')
    s = s[:i] + new + s[j:]

# 1. the old Learn (four steps) gives way to the book on screen (NoteNamesLearn, defined with the chapter's pages)
cut('function NoteNamesLearn({ onStart }) {', '// ─── Letter steps inside Note Names (Phase 97)',
    '// Phase 397: NoteNamesLearn is the Lesson Book opened on screen -- defined with the chapter pages (nnLbPages).\n\n', 'old learn')

# 2. the drill's levels (B7, Phase 391-397)
rep("""  { n: 4, label: 'Black keys too (sharps & flats)', octaves: 2, black: true, dirs: ['key2name', 'name2key'], time: 7 },
  { n: 5, label: 'Letter steps · next letter up or down', octaves: 1, black: false, dirs: ['step'], time: 6 },
  { n: 6, label: 'Letter jumps · 3rds to octaves, up or down', octaves: 1, black: false, dirs: ['jump'], time: 8 },
];""",
    """  { n: 4, label: 'Next letter up or down', octaves: 1, black: false, dirs: ['step'], time: 6 },
  { n: 5, label: 'Skip a letter, up or down', octaves: 1, black: false, dirs: ['skip'], time: 7 },
];
// Phase 397: the black keys' names moved to Tones & Semitones (its level 4); interval numbers (3rd ... octave) to Intervals
const NN_BLACK_LEVEL = { n: 4, label: 'Name the black keys (sharps & flats)', kind: 'black', octaves: 2, black: true, dirs: ['key2name', 'name2key'], time: 7 };""", 'levels')
rep("  if (lv.dirs[0] === 'step' || lv.dirs[0] === 'jump') return genLetterQuestion(lv, prev);",
    "  if (lv.dirs[0] === 'step' || lv.dirs[0] === 'jump' || lv.dirs[0] === 'skip') return genLetterQuestion(lv, prev);", 'gen')
rep("  return props.q.dir === 'step' || props.q.dir === 'jump' ? <LetterStepQuestion {...props}/> : <NoteNameQuestion {...props}/>;",
    "  return props.q.dir === 'step' || props.q.dir === 'jump' || props.q.dir === 'skip' ? <LetterStepQuestion {...props}/> : <NoteNameQuestion {...props}/>;", 'question')
rep("  const size = lv.dirs[0] === 'step' ? 2 : pick([3, 4, 5, 6, 7, 8]);",
    "  const size = lv.dirs[0] === 'step' ? 2 : lv.dirs[0] === 'skip' ? 3 : pick([3, 4, 5, 6, 7, 8]);", 'size')
rep("""    q.size === 2 ? (q.up ? 'next letter up' : 'next letter down') : dirWord + ' ' + withArticle(intervalWord(q.size)),
    q.size === 2 ? (q.up ? '다음 글자 (위)' : '다음 글자 (아래)') : intervalWordKo(q.size) + ' ' + (q.up ? '위' : '아래')""",
    """    q.size === 2 ? (q.up ? 'next letter up' : 'next letter down') : q.dir === 'skip' ? (q.up ? 'skip a letter up' : 'skip a letter down') : dirWord + ' ' + withArticle(intervalWord(q.size)),
    q.size === 2 ? (q.up ? '다음 글자 (위)' : '다음 글자 (아래)') : q.dir === 'skip' ? (q.up ? '한 글자 건너 (위)' : '한 글자 건너 (아래)') : intervalWordKo(q.size) + ' ' + (q.up ? '위' : '아래')""", 'cue')
rep("""      ? (q.size === 2 ? q.letter + '에서 한 글자 ' + (q.up ? '위' : '아래') : q.letter + '에서 ' + (q.up ? '위로' : '아래로') + ' ' + intervalWordKo(q.size))
      : (q.size === 2 ? 'one letter ' + (q.up ? 'up' : 'down') + ' from ' + q.letter : q.letter + ' ' + (q.up ? 'up' : 'down') + ' ' + withArticle(intervalWord(q.size)))) + ')'""",
    """      ? (q.size === 2 ? q.letter + '에서 한 글자 ' + (q.up ? '위' : '아래') : q.dir === 'skip' ? q.letter + '에서 한 글자 건너 ' + (q.up ? '위' : '아래') : q.letter + '에서 ' + (q.up ? '위로' : '아래로') + ' ' + intervalWordKo(q.size))
      : (q.size === 2 ? 'one letter ' + (q.up ? 'up' : 'down') + ' from ' + q.letter : q.dir === 'skip' ? 'a skip ' + (q.up ? 'up' : 'down') + ' from ' + q.letter : q.letter + ' ' + (q.up ? 'up' : 'down') + ' ' + withArticle(intervalWord(q.size)))) + ')'""", 'answer label')
rep("  'Letter jumps · 3rds to octaves, up or down': '글자 건너뛰기 · 3도부터 옥타브까지, 위나 아래로',",
    "  'Letter jumps · 3rds to octaves, up or down': '글자 건너뛰기 · 3도부터 옥타브까지, 위나 아래로',\n  'Next letter up or down': '다음 글자 · 위나 아래로',\n  'Skip a letter, up or down': '한 글자 건너뛰기 · 위나 아래로',\n  'Name the black keys (sharps & flats)': '검은건반 이름 (샵과 플랫)',", 'level ko')

# 3. Tones & Semitones gets the black-key naming level (moved from the musical alphabet)
rep("  { n: 3, label: 'Two names, one key',             kind: 'enh',   time: 8 },",
    "  { n: 3, label: 'Two names, one key',             kind: 'enh',   time: 8 },\n  NN_BLACK_LEVEL,", 'tones level')
rep("function genTonesQuestion(lv, prev) {\n  const uid = Math.random();",
    "function genTonesQuestion(lv, prev) {\n  if (lv.kind === 'black') return { ...genNoteQuestion(lv, prev), kind: 'black' };\n  const uid = Math.random();", 'tones gen')
rep("  check: (q, ans) => ans !== null && ans !== undefined && (q.kind === 'find' ? ans === q.target : ans === q.answer),\n  answerLabel: (q) => q.kind === 'find' ?",
    "  check: (q, ans) => ans !== null && ans !== undefined && (q.kind === 'black' ? (q.dir === 'key2name' ? ans === q.pc : ans % 12 === q.pc) : q.kind === 'find' ? ans === q.target : ans === q.answer),\n  answerLabel: (q) => q.kind === 'black' ? (q.dir === 'key2name' ? withSolfa(pcLabel(q.pc)) : t('the key shown in green', '초록색으로 표시된 건반')) : q.kind === 'find' ?", 'tones check')
rep("  Question: TonesQuestion, Learn: TonesLearn,",
    "  Question: (props) => props.q.kind === 'black' ? <NoteNameQuestion {...props}/> : <TonesQuestion {...props}/>, Learn: TonesLearn,", 'tones q')

# 4. the letter chain can be limited to steps and skips (chapter 3's skip page), without the staff
rep("function LetterChainDrill() {", "function LetterChainDrill({ sizes, noStaff } = {}) {", 'chain sig')
rep("""        {INTERVALS.map(iv => (
          <button key={iv.size} className={'chip'+(interval===iv.size?' active':'')} onClick={()=>setIntervalSize(iv.size)}>
            {LANG === 'ko' ? intervalWordKo(iv.size) : iv.label}""",
    """        {(sizes ? INTERVALS.filter(iv => sizes.includes(iv.size)) : INTERVALS).map(iv => (
          <button key={iv.size} className={'chip'+(interval===iv.size?' active':'')} onClick={()=>setIntervalSize(iv.size)}>
            {sizes ? (iv.size === 2 ? t('Step', '한 걸음') : iv.size === 3 ? t('Skip', '건너뛰기') : iv.label) : LANG === 'ko' ? intervalWordKo(iv.size) : iv.label}""", 'chain chips')
rep("""        <button className={'chip'+(showStaff?' active':'')} onClick={()=>setShowStaff(v=>!v)}>{t('Staff', '오선')}</button>""",
    """        {!noStaff && <button className={'chip'+(showStaff?' active':'')} onClick={()=>setShowStaff(v=>!v)}>{t('Staff', '오선')}</button>}""", 'chain staff')

# 5. an "At the piano" box can carry another title and icon ("Away from the piano")
rep("function LbPiano({ steps, title }) {", "function LbPiano({ steps, title, icon }) {", 'lbpiano sig')
rep("<div style={{display:'flex',alignItems:'center',gap:8,marginBottom:7}}><LbKeysIcon/><span style={{fontFamily:LB_SERIF,fontSize:21",
    "<div style={{display:'flex',alignItems:'center',gap:8,marginBottom:7}}>{icon || <LbKeysIcon/>}<span style={{fontFamily:LB_SERIF,fontSize:21", 'lbpiano icon')

# 6. the Workbook data and the Workbook / Teacher copy, page by page
cut('function nnWorkbook() {', 'function UpDownCell({ it, n, ex }) {', WB, 'workbook data')
cut('function NoteNamesWorkbook({ startNo = 1 }) {', '// Lesson Book paper pictures for Note Names', WB2, 'workbook pages')

# 7. the Lesson Book pages, registered (one opener and one check-up for both books)
rep("const LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook };",
    LB + "\nconst LESSON_BOOKS = { 'posture-hands': PostureLessonBook, 'first-steps': FirstStepsLessonBook, 'note-names': NoteNamesLessonBook };", 'lesson books')
rep("const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'first-steps': fsLbPages };",
    "const LB_PAGE_FNS = { 'posture-hands': postureLbPages, 'first-steps': fsLbPages, 'note-names': nnLbPages };", 'page fns')

# 8. chapter 1's check page in Korean was 3px too tall (longer check lines): the set-up pictures a little smaller there
rep("<PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} h={46}/>", "<PhPic key={id} art={'q-sit-' + id} ok={ok} n={i + 1} h={LANG === 'ko' ? 42 : 46}/>", 'ch1 ko fit')

open(src, 'w', encoding='utf-8').write(s)
print('patch397 ok', len(s))
