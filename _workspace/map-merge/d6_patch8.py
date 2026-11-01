# Dashboard D6 (2026-11-01, her 'and a separate one for me to try, not applied to a student'): a test student that is hers.
# It never appears in Today, the Schedule or today's names; it has its own card ("Test · only you") and everything else
# works for real (lesson mode, homework, its own student link to try the student view in a private window).
import sys
p=sys.argv[1]; h=open(p,encoding='utf-8').read()
def rep(o,n,c=1):
    global h
    k=h.count(o)
    if k!=c: raise SystemExit("count %d != %d for %r"%(k,c,o[:90]))
    h=h.replace(o,n)
rep("students.filter(s => !s.paused)", "students.filter(s => !s.paused && !s.test)", 3)
rep("""  // Today's lessons -- paused students are listed too (faded)
  const slots = [];
  students.forEach(s => {""","""  // Today's lessons -- paused students are listed too (faded)
  const slots = [];
  students.forEach(s => {
    if (s.test) return;   // Dashboard D6: the test student has no lesson day""")
rep("""  const skippedSlots = []; // slots hidden this week (skip override)
  students.forEach(s => {""","""  const skippedSlots = []; // slots hidden this week (skip override)
  students.forEach(s => {
    if (s.test) return;   // Dashboard D6""")
rep("""function studentStatus(student, studentLogs, act) {
  if (student.paused) return null;""","""function studentStatus(student, studentLogs, act) {
  if (student.test) return { tone: "n", text: "Test · only you" };   // Dashboard D6
  if (student.paused) return null;""")
# the card: no next-lesson pill for the test student
rep("""              {!student.paused && nextLessonDays !== null && <span""","""              {!student.paused && !student.test && nextLessonDays !== null && <span""")
# the add button, as a card in the grid
rep("""                {filtered.map(s=>(
                  <StudentCard key={s.id} student={s} logs={logs} act={roster[s.id]}
                    onLog={setLogging} onSelect={selectStudent}/>
                ))}""","""                {filtered.map(s=>(
                  <StudentCard key={s.id} student={s} logs={logs} act={roster[s.id]}
                    onLog={setLogging} onSelect={selectStudent}/>
                ))}
                {!students.some(s => s.test) && (
                  <button onClick={addTestStudent} data-testid="add-test-student" className="card no-print"
                    style={{border:"1.5px dashed #cfc9b6",background:"transparent",padding:20,textAlign:"left",cursor:"pointer",color:"#62649a"}}>
                    <p className="font-bold text-sm" style={{color:"#26296b"}}>+ A test student for you</p>
                    <p className="text-xs mt-1" style={{lineHeight:1.5}}>Try lesson mode, homework and the student’s own page without touching a real student. It stays off Today and the Schedule.</p>
                  </button>
                )}""")
rep("""  const updateStudent = async (f) => {""","""  const addTestStudent = async () => {   // Dashboard D6
    if (students.some(s => s.test)) return;
    const row = studentToRow({ name: "Test (me)", grade: "", lessonDay: "Monday", lessonTime: "00:00", lessonDuration: 30, startDate: todayStr(), test: true }, userId);
    const { data, error } = await _supabase.from("students").insert(row).select().single();
    if (error) { alert("Could not add the test student: " + error.message); return; }
    setStudents(p => [...p, rowToStudent(data)]);
  };

  const updateStudent = async (f) => {""")
rep('{rest.map(s => chip(s, null, s.id))}','{rest.map(s => chip(s, s.test ? "test" : null, s.id))}')
open(p,'w',encoding='utf-8').write(h); print('d6 ok')
