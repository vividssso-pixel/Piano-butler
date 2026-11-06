#!/usr/bin/env python3
# Phase 399: no teacher strips in the app either (Sohyun 2026-10-09: "didn't we decide to delete all the teacher parts?").
# Phase 387 took them out of the printed Lesson Book; the app's teacher view still showed them under each step.
# Teacher content lives in the Teacher copy (?book=teacher) only. The pages keep their `teacher` text in the source, unused.
import sys
src = sys.argv[1]; s = open(src, encoding='utf-8').read()
a = """          {teacher && <TeacherOnly><div data-lb-teacher style={{display:'flex',gap:10,alignItems:'flex-start',borderTop:'1.3px dashed ' + BK.line,paddingTop:9}}>
            <span style={{flex:'0 0 auto',fontSize:9.5,fontWeight:900,letterSpacing:'0.06em',color:'#fff',background:BK.ink,borderRadius:4,padding:'3px 7px',marginTop:2}}>{t('TEACHER', '선생님')}</span>
            <div style={{flex:1,fontSize:13,color:BK.ink,lineHeight:1.5}}>{teacher}</div>
          </div></TeacherOnly>}
"""
assert s.count(a) == 1, s.count(a)
s = s.replace(a, "          {/* Phase 399: no teacher strip on screen either -- teacher content lives in the Teacher copy */}\n")
s = s.replace("function LbScreenPage({ page }) {\n  const { teacher, children } = page.props;", "function LbScreenPage({ page }) {\n  const { children } = page.props;", 1)
open(src, 'w', encoding='utf-8').write(s); print('patch399a ok')
