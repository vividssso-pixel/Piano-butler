#!/usr/bin/env python3
"""Build CY (on t773 -> t774). Sohyun 2026-10-30 00:35:
1. 'Make your own' plays right there in the chapter: a tap opens the thing to make under its name (one at a time).
2. A tool opened from a chapter goes back to that chapter, not to the Toolbox ('← <chapter>'). A tool opened from the
   Toolbox still goes back to the Toolbox; any other tool that belongs to a chapter goes back to its chapter.
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

# 1. Make your own, in place
R("""function LessonMake({ id }) {   // Build CA: the room's own thing to make, at the end of the room
  const toys = TOOLS.filter(tl => tl.ch === id && /^mk-/.test(tl.id) && !tl.hidden).concat((MAKE_EXTRA[id] || []).map(x => TOOLS.find(tl => tl.id === x)).filter(Boolean));
  if (!toys.length) return null;""", """function LessonMake({ id }) {   // Build CA: the room's own thing to make, at the end of the room; Build CY: it opens right here
  const toys = TOOLS.filter(tl => tl.ch === id && /^mk-/.test(tl.id) && !tl.hidden).concat((MAKE_EXTRA[id] || []).map(x => TOOLS.find(tl => tl.id === x)).filter(Boolean));
  const [open, setOpen] = useState(null), box = useRef(null);
  useEffect(() => { if (open && box.current) { try { box.current.scrollIntoView({ behavior: 'smooth', block: 'start' }); } catch (e) {} } }, [open]);
  if (!toys.length) return null;""")
R("""    {toys.map(tl => <a key={tl.id} href={'?tool=' + tl.id + (LANG === 'ko' ? '&lang=ko' : '')} style={{display:'flex',alignItems:'center',gap:10,textDecoration:'none',color:'var(--text)',minHeight:44,padding:'4px 0'}}>
      <span style={{flex:1,minWidth:0}}><span style={{display:'block',fontSize:16,fontWeight:900,color:'#26296b'}}>{sscSx(LANG === 'ko' && TOOL_KO[tl.id] ? TOOL_KO[tl.id][0] : tl.title)}</span>
        <span style={{display:'block',fontSize:13,color:'#4a4d86',lineHeight:1.4}}>{LANG === 'ko' && TOOL_KO[tl.id] ? TOOL_KO[tl.id][1] : tl.blurb}</span></span>
      <span aria-hidden="true" style={{flex:'0 0 auto',color:'#e4572e',fontSize:22,fontWeight:900}}>›</span></a>)}""",
  """    {toys.map(tl => <div key={tl.id} ref={open === tl.id ? box : undefined}>
      <button data-make-tool={tl.id} aria-expanded={open === tl.id} onClick={() => setOpen(o => (o === tl.id ? null : tl.id))} style={{display:'flex',alignItems:'center',gap:10,width:'100%',textAlign:'left',background:'none',border:'none',cursor:'pointer',color:'var(--text)',minHeight:44,padding:'4px 0'}}>
        <span style={{flex:1,minWidth:0}}><span style={{display:'block',fontSize:16,fontWeight:900,color:'#26296b'}}>{sscSx(LANG === 'ko' && TOOL_KO[tl.id] ? TOOL_KO[tl.id][0] : tl.title)}</span>
          <span style={{display:'block',fontSize:13,color:'#4a4d86',lineHeight:1.4}}>{LANG === 'ko' && TOOL_KO[tl.id] ? TOOL_KO[tl.id][1] : tl.blurb}</span></span>
        <span aria-hidden="true" style={{flex:'0 0 auto',color:'#e4572e',fontSize:22,fontWeight:900,transform:open === tl.id ? 'rotate(90deg)' : 'none',transition:'transform 0.2s'}}>›</span></button>
      {open === tl.id && <div data-make-open={tl.id} style={{borderTop:'1px solid rgba(38,41,107,0.14)',padding:'10px 0 8px',animation:'fadeUp 0.25s both',minWidth:0}}><tl.C/></div>}
    </div>)}""")
# the toolbox chips of a room remember the room
R("""{list.map(tl => <a key={tl.id} className="chip" href={'?tool=' + tl.id + (LANG === 'ko' ? '&lang=ko' : '')}""",
  """{list.map(tl => <a key={tl.id} className="chip" href={'?tool=' + tl.id + '&from=' + id + (LANG === 'ko' ? '&lang=ko' : '')}""")

# 2. back to the chapter
R("""ret: p.get('ret') === 'home' ? 'home' : null,""", """ret: p.get('ret') === 'home' ? 'home' : null, rc: DRILLS.find(d => d.id === p.get('from')) ? p.get('from') : null,""")
R("""function ToolView({ id, locked, onBack, onChapter, backLabel = '← Toolbox' }) {""", """function ToolView({ id, locked, onBack, onChapter, backLabel = '← Toolbox', backAlways }) {""")
R("""      {(!locked || backLabel !== '← Toolbox') && <button className="ghost-btn" style={{fontSize:13,padding:'5px 12px',marginBottom:10}} onClick={onBack}>""",
  """      {(!locked || backAlways || backLabel !== '← Toolbox') && <button className="ghost-btn" data-testid="tool-back" style={{fontSize:13,padding:'5px 12px',marginBottom:10}} onClick={onBack}>""")
R("""            ? <ToolView id={st.tool} locked={st.lock} backLabel={st.from && st.from.tool === st.tool ? '← Today' : st.view === 'practice' ? '← Practice' : st.ret === 'home' ? homeBack : '← Toolbox'} onBack={() => st.from && st.from.tool === st.tool ? update({ tool: null, view: 'today', from: null }) : update({ tool: null, view: (st.view === 'practice' ? null : st.ret) || (T && st.view === 'tools' ? 'toolbox' : st.view), ret: null })} onChapter""",
  """            ? <ToolView id={st.tool} locked={st.lock} backAlways={!!toolBackCh} backLabel={st.from && st.from.tool === st.tool ? '← Today' : st.view === 'practice' ? '← Practice' : st.ret === 'home' ? homeBack : toolBackCh ? '← ' + bkChapterName(toolBackCh) : '← Toolbox'} onBack={() => st.from && st.from.tool === st.tool ? update({ tool: null, view: 'today', from: null }) : st.view !== 'practice' && st.ret !== 'home' && toolBackCh ? update({ view: 'path', tool: null, drill: toolBackCh, tab: 'learn', level: 1, ret: null, rc: null }) : update({ tool: null, view: (st.view === 'practice' ? null : st.ret) || (T && st.view === 'tools' ? 'toolbox' : st.view), ret: null })} onChapter""")
# which chapter a tool goes back to: the room it was opened from; else, unless it came from the Toolbox, its own chapter
R("""  const homeBack = '← ' +""", """  const toolBackCh = (() => { if (!st.tool || st.ret === 'toolbox' || st.ret === 'home' || st.view === 'practice' || (st.from && st.from.tool === st.tool)) return null;   // Build CY
    if (st.rc) return st.rc; if (st.lock) return null; const tl = TOOLS.find(x => x.id === st.tool); return tl && DRILLS.find(d => d.id === tl.ch) ? tl.ch : null; })();
  const homeBack = '← ' +""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
