# The drills' student picker shows the teacher's test student apart: "Try it yourself · Me (test)" (2026-11-01).
import sys
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
def rep(o, n, c=1):
    global h
    k = h.count(o)
    if k != c: raise SystemExit("count %d != %d for %r" % (k, c, o[:100]))
    h = h.replace(o, n)
rep("return { ...s, paused: !!ex.paused,", "return { ...s, paused: !!ex.paused, test: !!ex.test,")
rep("  const todays = rows.filter(s => s.when != null).sort((a, b) => String(a.when).localeCompare(String(b.when))), rest = rows.filter(s => s.when == null);",
    "  const tests = rows.filter(s => s.test), real = rows.filter(s => !s.test);\n  const todays = real.filter(s => s.when != null).sort((a, b) => String(a.when).localeCompare(String(b.when))), rest = real.filter(s => s.when == null);")
rep("          {rest.length > 0 && <>{lab(todays.length ? t('Everyone else', '나머지 학생') : t('Students', '학생'))}<div style={{display:'flex',flexWrap:'wrap',gap:6}}>{rest.map(chip)}</div></>}",
    "          {rest.length > 0 && <>{lab(todays.length ? t('Everyone else', '나머지 학생') : t('Students', '학생'))}<div style={{display:'flex',flexWrap:'wrap',gap:6}}>{rest.map(chip)}</div></>}\n          {tests.length > 0 && <>{lab(t('Try it yourself', '직접 해 보기'))}<div style={{display:'flex',flexWrap:'wrap',gap:6}}>{tests.map(s => <button key={s.id} type=\"button\" className=\"chip\" data-testid=\"tpick-test\" onClick={() => { setOpen(false); onStart({ ...s, name: 'Me (test)' }); }} style={{minHeight:40,padding:'6px 13px',fontSize:14,fontWeight:800,borderStyle:'dashed'}}>{t('Me (test)', '나 (테스트)')}</button>)}</div></>}")
rep("    when: s.lesson_day === today ? (s.lesson_time || '') : s.lesson_day2 === today ? (s.lesson_time2 || '') : null }; }).filter(s => !s.paused) : [];",
    "    when: s.lesson_day === today ? (s.lesson_time || '') : s.lesson_day2 === today ? (s.lesson_time2 || '') : null }; }).filter(s => !s.paused).map(s => s.test ? { ...s, when: null } : s) : [];")
open(p, 'w', encoding='utf-8').write(h); print('m10 ok')
