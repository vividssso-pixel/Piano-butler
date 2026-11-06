// ── Phase 372: the chapter 1 Workbook and Teacher copy follow the Lesson Book, page by page (wb372data.jsx, wb372.jsx) ──
{
  const a = s.indexOf("// ─── Posture and hand shape (chapter 'posture-hands') ───"), b = s.indexOf('const tfPill = ', a);
  if (a < 0 || b < 0) throw new Error('372 data span');
  s = s.slice(0, a) + read('wb372data.jsx') + s.slice(b);
  const c = s.indexOf('function PostureWorkbook({ startNo = 1 }) {'), d = s.indexOf('function PostureTeacher() {', c);
  const e = s.indexOf('\n// ─── Drawn metaphors for Rhythm Patterns', d);
  if (c < 0 || d < 0 || e < 0) throw new Error('372 workbook span');
  s = s.slice(0, c) + read('wb372.jsx') + '\n' + s.slice(e);
}
