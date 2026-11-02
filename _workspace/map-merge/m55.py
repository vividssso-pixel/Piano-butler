p='teacher-dashboard.html'; s=open(p).read()
def rep(o,n,c=1):
    global s
    assert s.count(o)==c,(s.count(o),o[:80]); s=s.replace(o,n)
rep('''  const [notes, setNotes] = useState("");
  const [busy, setBusy] = useState(false);
  const toggle = (k) =>''', '''  const [notes, setNotes] = useState("");
  const [busy, setBusy] = useState(false);
  // m55: the pieces and scales carry on from the last lesson (unfinished ones), with their stages, right here at the end of the lesson
  const prev = [...studentLogs].filter(l => !noLesson(l)).sort((a, b) => String(b.date).localeCompare(String(a.date)))[0];
  const carry = (txt) => parseItems(String(txt || "").split("\\n").filter(x => x.trim() && !parsePiece(x).f).join("\\n"), true).filter(it => it.t);
  const [rep, setRep] = useState(() => carry(prev && prev.repertoire));
  const [sc, setSc] = useState(() => carry(prev && prev.technical));
  const [newPiece, setNewPiece] = useState("");
  const addPiece = () => { const t = newPiece.trim(); if (!t) return; setRep(r => [...r, { t, r: "", b: "" }]); setNewPiece(""); };
  const toggle = (k) =>''')
rep('''  const save = async () => { setBusy(true); await onSave({ homework: items.filter(x => on.has(x.key)).map(x => x.line).join("\\n"), notes: notes.trim(), shown: shown.map(it => it.label) }); setBusy(false); };''',
    '''  const save = async () => { setBusy(true); const hw = items.filter(x => on.has(x.key)).map(x => x.line).join("\\n"), ks = sc.length ? scKeys(sc) : [];
    await onSave({ homework: [ks.length ? "[keys:" + ks.join(",") + "]" : "", hw].filter(Boolean).join("\\n"), notes: notes.trim(), shown: shown.map(it => it.label), repertoire: joinItems(rep, true), technical: joinItems(sc, true) }); setBusy(false); };''')
rep('''        <textarea className="input" rows={2} placeholder="Notes (optional)" value={notes}''',
'''        <div data-testid="end-pieces" style={{marginTop:12}}>
          <p style={{fontSize:11,fontWeight:800,letterSpacing:"0.07em",textTransform:"uppercase",color:"#26296b",margin:"0 0 4px"}}>Pieces</p>
          {rep.map((it, i) => <div key={it.t + i} style={{display:"flex",alignItems:"flex-start",gap:8,marginBottom:8}}>
            <div style={{flex:1,minWidth:0}}><div style={{fontSize:14,fontWeight:700,color:"#26296b",background:"#ecebf5",borderRadius:10,padding:"7px 12px"}}>{it.t}</div>
              <StageBar it={it} onPatch={pt => setRep(r => r.map((x, j) => j === i ? { ...x, ...pt } : x))}/></div>
            <button type="button" aria-label={"Remove " + it.t} onClick={() => setRep(r => r.filter((_, j) => j !== i))} style={{border:"none",background:"none",color:"#9b9cbd",fontSize:18,marginTop:6,cursor:"pointer"}}>×</button></div>)}
          <div style={{display:"flex",gap:6}}><input className="input" value={newPiece} onChange={e => setNewPiece(e.target.value)} onKeyDown={e => { if (e.key === "Enter") { e.preventDefault(); addPiece(); } }} placeholder="Start a new piece" style={{flex:1,fontSize:14}}/>
            <button type="button" className="btn-ghost text-xs py-1.5 px-3" onClick={addPiece}>Add</button></div>
        </div>
        <div style={{marginTop:12}}><ScalesField items={sc} onChange={(x) => setSc(x.filter(it => it.t))}/></div>
        <textarea className="input" rows={2} placeholder="Everything else (optional)" value={notes}''')
rep('''    const row = logToRow({ date: todayStr(), notes: f.notes, homework: f.homework, shown: f.shown, type: "regular" }, s.id, userId);''',
    '''    const row = logToRow({ date: todayStr(), notes: f.notes, homework: f.homework, shown: f.shown, repertoire: f.repertoire || "", technical: f.technical || "", type: "regular" }, s.id, userId);   // m55''')
open(p,'w').write(s); print('ok')
