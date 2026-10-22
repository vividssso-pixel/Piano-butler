import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:70])
    s = s.replace(old, new)

# 1. One Keyboard patterns drill that carries the note-name levels too (Home shows one Questions button per concept)
rep("""const FIRST_STEPS_DRILL = {
  id: 'first-steps', label: 'Keyboard Patterns', levels: FS_LEVELS, generate: genFsQuestion,
  check: (q, ans) => ans !== null && ans !== undefined && ans === q.answer,
  answerLabel: (q) => LANG === 'ko' ? fsLabel(q.answer) : q.answer.toLowerCase(),
  Question: FsQuestion, Learn: FirstStepsLearn,
};""", """const FS_ALL_LEVELS = [...FS_LEVELS, ...NOTE_NAME_LEVELS.map(l => ({ ...l, n: l.n + FS_LEVELS.length, src: 'nn' }))];
const FIRST_STEPS_DRILL = {
  id: 'first-steps', label: 'Keyboard Patterns', levels: FS_ALL_LEVELS,
  generate: (lv, prev) => lv.src === 'nn' ? { ...genNoteQuestion(lv, prev), src: 'nn' } : genFsQuestion(lv, prev),
  check: (q, ans) => q.src === 'nn' ? NOTE_NAMES_DRILL.check(q, ans) : ans !== null && ans !== undefined && ans === q.answer,
  answerLabel: (q) => q.src === 'nn' ? NOTE_NAMES_DRILL.answerLabel(q) : LANG === 'ko' ? fsLabel(q.answer) : q.answer.toLowerCase(),
  Question: (props) => props.q.src === 'nn' ? <NoteNamesQuestion {...props}/> : <FsQuestion {...props}/>, Learn: FirstStepsLearn,
};""")

# 2. Keys and staff: one check per group
rep("lessons: ['kq-black', 'kq-houses', 'kq-names'], checks: [['first-steps', 'Questions: keyboard patterns', '문제: 건반 패턴'], ['note-names', 'Questions: note names', '문제: 음 이름']] }",
    "lessons: ['kq-black', 'kq-houses', 'kq-names'], check: 'first-steps' }")

# 3. Same Questions button everywhere, directly under the lessons
QSTYLE = "{{display:'block',width:'100%',minHeight:52,marginTop:4,borderRadius:26,border:'none',background:'var(--navy)',color:'#fffefa',fontWeight:800,fontSize:17,cursor:'pointer'}}"
i = s.index("                {(g.checks || (g.check ?")
j = s.index("\n", i)
s = s[:i] + "                {g.check && <button data-questions={g.check} onClick={() => go({ view: 'home', drill: g.check, tab: 'drill', level: 1, mode: 'lesson' })} style=" + QSTYLE + ">{t('Questions', '문제')} →</button>}" + s[j:]
rep("""        </>; })()}
      </div>
      {live.check && <button onClick={() => go({ view: 'home', drill: live.check, tab: 'drill', level: 1, mode: 'lesson' })} style={{display:'block',width:'100%',minHeight:60,marginTop:18,borderRadius:30,border:'none',background:'var(--navy)',color:'#fffefa',fontWeight:800,fontSize:20,cursor:'pointer'}}>{t('Start the drill →', '드릴 시작 →')}</button>}
""", """          {live.check && <button data-questions={live.check} onClick={() => go({ view: 'home', drill: live.check, tab: 'drill', level: 1, mode: 'lesson' })} style=""" + QSTYLE + """>{t('Questions', '문제')} →</button>}
        </>; })()}
      </div>
""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok')
