p='teacher-dashboard.html'; s=open(p).read()
assert 'gradeLabel' not in s
def rep(o,n,c=1):
    global s
    assert s.count(o)==c,(s.count(o),o[:80]); s=s.replace(o,n)
rep("// Map app student object → Supabase row (for insert/update)",
    "// m53 (her 2 Nov): a grade the student has for sure (exam taken, or clearly at it), in progress or finished\nconst gradeLabel = (s) => s && s.grade ? s.grade + (s.gradeDone ? \" · finished\" : \" · in progress\") : (s && s.level) || \"General\";\n// Map app student object → Supabase row (for insert/update)")
rep('''          {/* Exam or not */}''', '''          {/* m53: Grade, if known, in progress or finished (shown on Today and the student page) */}
          <div>
            <label className="field-label text-slate-500" htmlFor="student-grade">Grade <span className="font-normal text-slate-400 normal-case">(if you know it for sure)</span></label>
            <div className="flex gap-2 items-center">
              <select id="student-grade" className="input" style={{flex:"1 1 auto"}} value={f.grade || ""} onChange={e=>set("grade",e.target.value)}>
                <option value="">Not set</option>
                {gradeOptions.map(g=><option key={g} value={g}>{g}</option>)}
              </select>
              {f.grade && [[false,"In progress"],[true,"Finished"]].map(([v,lab])=>(
                <button key={lab} type="button" aria-pressed={!!f.gradeDone===v} data-grade-done={String(v)} onClick={()=>set("gradeDone",v)}
                  className="py-2 px-3 rounded-xl text-sm font-semibold border" style={!!f.gradeDone===v?{background:"#26296b",color:"white",borderColor:"#26296b",whiteSpace:"nowrap"}:{background:"white",color:"#62649a",borderColor:"#e9e2d2",whiteSpace:"nowrap"}}>{lab}</button>))}
            </div>
          </div>

          {/* Exam or not */}''')
i=s.index('''                <div>
                  <label className="field-label text-slate-500" htmlFor="student-grade">Grade</label>''')
j=s.index("</div>", s.index("</select>", i))+len("</div>")
s=s[:i]+"                {/* m53: the Grade moved above, for every student */}"+s[j:]
rep('{student.age ? "Age " + student.age + " · " : ""}{student.grade || student.level || "General"}', '{student.age ? "Age " + student.age + " · " : ""}{gradeLabel(student)}')
rep('{student.grade || student.level || "General"} · {student.lessonDuration}min lessons', '{gradeLabel(student)} · {student.lessonDuration}min lessons')
rep('{[student.grade || student.level || "General", student.lessonDay', '{[gradeLabel(student), student.lessonDay')
rep('const meta = [s.grade || "General"];', 'const meta = [gradeLabel(s)];')
open(p,'w').write(s); print('ok')
