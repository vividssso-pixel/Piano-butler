# Map merge M5 (2026-11-01, her 'do both now'):
# (1) Topics opens on the Reference ("At a glance"): one topic's table at a time, chosen with chips; the lessons by topic follow.
# (2) The teacher view never sends anything to a student link this browser happens to hold (no sync, no practice log),
#     and says so, with a way to remove the link from a teacher's device.
import sys
p = sys.argv[1]; h = open(p, encoding='utf-8').read()
def rep(o, n, c=1):
    global h
    k = h.count(o)
    if k != c: raise SystemExit("count %d != %d for %r" % (k, c, o[:100]))
    h = h.replace(o, n)
# (1) the Reference in pick mode
rep("function ReferenceView({ onChapter }) {\n  const jump = (id) =>",
    "function ReferenceView({ onChapter, pick }) {\n  if (pick) return <RefPick onChapter={onChapter}/>;   // M5: the Map's Topics view, one topic at a time\n  const jump = (id) =>")
rep("function ReferenceView({ onChapter, pick }) {", r'''const REF_PICK_KEY = 'pb_ref_pick_v1';
function RefPick({ onChapter }) {
  const [sel, setSel] = useState(() => { let x = null; try { x = localStorage.getItem(REF_PICK_KEY); } catch (e) {} return REF_SECS.some(s => s.id === x) ? x : REF_SECS[0].id; });
  const choose = (id) => { setSel(id); try { localStorage.setItem(REF_PICK_KEY, id); } catch (e) {} };
  const s = REF_SECS.find(z => z.id === sel) || REF_SECS[0], B = REF_BODY[s.id];
  return <RefGo.Provider value={onChapter || null}><div data-reference data-ref-pick={s.id} style={{display:'flex',flexDirection:'column',gap:12,marginBottom:26}}>
    <div>
      <div style={{fontSize:11.5,fontWeight:900,letterSpacing:'0.08em',textTransform:'uppercase',color:'#e4572e',margin:'0 0 4px'}}>{t('At a glance', '한눈에 보기')}</div>
      <div style={{fontSize:13.5,color:'#4a4d86',lineHeight:1.5,margin:'0 0 8px'}}>{t('The theory on a few tables, Beginner to Grade 8. Tap a row to go to the room where you learn it. ♪ plays it.', 'Beginner부터 Grade 8까지의 이론을 표 몇 장에. 줄을 누르면 그걸 배우는 방으로 가요. ♪는 소리를 들려줘요.')}</div>
      <div role="tablist" style={{display:'flex',flexWrap:'wrap',gap:5}}>{REF_SECS.map(z => <button key={z.id} type="button" role="tab" aria-selected={z.id === s.id} className={'chip' + (z.id === s.id ? ' active' : '')} data-ref-pick-chip={z.id} onClick={() => choose(z.id)} style={{minHeight:34,padding:'3px 11px',fontSize:12.5,fontWeight:800}}>{t(z.en, z.ko)}</button>)}</div>
    </div>
    <section style={{minWidth:0}}><RefHead id={s.id}/><B/></section>
  </div></RefGo.Provider>;
}
function ReferenceView({ onChapter, pick }) {''')
rep("{!st.ha && !st.hc && !st.hs && <MapSwitch value=\"topics\"",
    "{!st.ha && !st.hc && !st.hs && <MapSwitch value=\"topics\"", 1)
rep("<ConceptHome st={st} update={update}/></>",
    "{!st.ha && !st.hc && !st.hs && <ReferenceView pick onChapter={jumpToChapter}/>}<ConceptHome st={st} update={update}/></>")
rep("[['scale-finder', t('Scale finder', '스케일 찾기')], ['reference', t('Reference', '한눈에 보기')], ['metronome'",
    "[['scale-finder', t('Scale finder', '스케일 찾기')], ['metronome'")
# (2) teacher view: quiet student link
rep("function useStudentLink() {", "function useStudentLink(quiet) {   // M5: quiet = the teacher view (also its student preview): the link is only shown, never synced")
rep("    if (l) syWatch(); // from now on", "    if (l && !quiet) syWatch(); // from now on")
rep("  const [state, setState] = useState(link ? 'checking' : 'none');", "  const [state, setState] = useState(link ? (quiet ? 'quiet' : 'checking') : 'none');")
rep("  useEffect(() => {\n    if (!token) return;\n    let off = false;\n    (async () => {\n      const r = await fetchStudentInfo(token);",
    "  useEffect(() => {\n    if (!token || quiet) return;\n    let off = false;\n    (async () => {\n      const r = await fetchStudentInfo(token);")
rep("    if (!SY.watch && !loadStoredLink() && !linkTokenFromHash()) return;", "    if (SY.quiet) return;   // M5: nothing from the teacher view reaches a student's practice log\n    if (!SY.watch && !loadStoredLink() && !linkTokenFromHash()) return;")
rep("  const sl = useStudentLink();", "  SY.quiet = !!teacher;   // M5\n  const sl = useStudentLink(!!teacher);")
rep("  if (!link || state === 'none') return null;\n  const name = link.name;",
    "  if (!link || state === 'none') return null;\n  const name = link.name;\n  if (state === 'quiet') return (   // M5: the teacher view on a device that holds a student link\n    <div role=\"status\" data-testid=\"quiet-link\" style={{ ...box, flexWrap: 'wrap', fontSize: 13 }}>\n      <span>{t('This browser holds ' + (name || 'a student') + '’s student link. In the teacher view nothing is sent to their progress.', '이 브라우저에 ' + (name || '학생') + '의 학생 링크가 있어요. 교사 화면에서는 학생 진도로 아무것도 보내지 않아요.')}</span>\n      <button className=\"chip\" style={small} data-testid=\"quiet-remove\" onClick={leaveAnyway}>{t('Remove it from this browser', '이 브라우저에서 지우기')}</button>\n    </div>\n  );")
open(p, 'w', encoding='utf-8').write(h); print('m5 ok')
