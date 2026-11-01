p='drills.src.html'; s=open(p).read()
if 'function RefSearch' in s: print('already'); raise SystemExit
def rep(old, new, cnt=1):
    global s
    assert s.count(old)==cnt, (s.count(old), old[:90])
    s=s.replace(old,new)

# 1. the House: no topic chips above it; the house comes first (her 'line them up, or keep it clean, the house first')
rep("        {inside && !compact && <HouseTopics value={topic} onChange={setTopic}/>}", "        {false && inside && !compact && <HouseTopics value={topic} onChange={setTopic}/>}   {/* m29: the Library does topics now */}")
rep("  const view = { stages, here, nums, openK: effK, focus: topic,", "  const view = { stages, here, nums, openK: effK, focus: null,")

# 2. the Library's search (her 'a search box here: find minim fast, and see which book it is in')
comp = r'''// m29: search the Library. Every book is rendered once, hidden, and its rows are searched; a result opens its book at the row.
const REF_FIND_SEL = '[data-ref-table] > div, [data-ref-sign], [data-ref-word], [data-ref-scale], [data-ref-clef], [data-ref-movement], [data-ref-period], [data-ref-term]';
const refFold = (x) => String(x || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
function refFind(root, q) {
  const f = refFold(q).trim(); if (!root || f.length < 2) return [];
  const out = [], seen = {};
  REF_SECS.forEach(sec => { const name = t(sec.en, sec.ko); if (refFold(name).includes(f) || refFold(sec.en).includes(f)) { out.push({ sec: sec.id, text: name, book: true, rank: 0 }); seen[sec.id + '|'] = 1; } });
  root.querySelectorAll('[data-ref-find]').forEach(box => {
    const sec = box.getAttribute('data-ref-find');
    box.querySelectorAll(REF_FIND_SEL).forEach(el => {
      if (el.querySelector && el.querySelector(REF_FIND_SEL)) return;   // the innermost only
      const raw = (el.textContent || '').replace(/\s+/g, ' ').trim(); if (!raw || raw.length > 260) return;
      const low = refFold(raw), i = low.indexOf(f); if (i < 0) return;
      const key = sec + '|' + low; if (seen[key]) return; seen[key] = 1;
      out.push({ sec, text: raw.length > 110 ? (i > 40 ? '… ' + raw.slice(i - 30, i + 80) : raw.slice(0, 110)) + ' …' : raw, rank: i === 0 || /[\s(·]/.test(low[i - 1] || ' ') ? 1 : 2 });
    });
  });
  return out.sort((a, b) => a.rank - b.rank).slice(0, 14);
}
function RefSearch({ onOpen }) {
  const [q, setQ] = useState(''), [on, setOn] = useState(false), [res, setRes] = useState([]), box = useRef(null);
  useEffect(() => { if (!on) return; const id = setTimeout(() => setRes(refFind(box.current, q)), 120); return () => clearTimeout(id); }, [q, on]);
  const name = (id) => { const x = REF_SECS.find(z => z.id === id); return x ? t(x.en, x.ko) : id; };
  return <div data-ref-search style={{margin:'12px 0 0',position:'relative'}}>
    <input type="search" value={q} onFocus={() => setOn(true)} onChange={e => { setOn(true); setQ(e.target.value); }} placeholder={t('Find in the Library: minim, Dorian, staccato…', '서재에서 찾기: 2분음표, 도리안, 스타카토…')} aria-label={t('Find in the Library', '서재에서 찾기')}
      style={{width:'100%',boxSizing:'border-box',font:'inherit',fontSize:15,padding:'10px 14px',border:'1.5px solid rgba(38,41,107,0.22)',borderRadius:12,background:'#fff',color:'var(--navy)'}}/>
    {q.trim().length >= 2 && <div data-ref-results style={{marginTop:6,border:'1.5px solid rgba(38,41,107,0.18)',borderRadius:12,background:'#fff',overflow:'hidden'}}>
      {res.length ? res.map((r, i) => <button key={i} type="button" data-ref-result={r.sec} onClick={() => { onOpen(r.sec, r.book ? null : q); setQ(''); }}
        style={{display:'flex',width:'100%',textAlign:'left',gap:10,alignItems:'baseline',justifyContent:'space-between',border:'none',borderTop:i ? '1px solid rgba(38,41,107,0.1)' : 'none',background:'none',font:'inherit',padding:'8px 12px',cursor:'pointer',color:'var(--navy)'}}>
        <span style={{fontSize:13.5,lineHeight:1.35,minWidth:0}}>{r.book ? <b>{r.text}</b> : r.text}</span>
        <span style={{flex:'none',fontSize:11,fontWeight:900,color:'#e4572e',whiteSpace:'nowrap'}}>{r.book ? t('the book ›', '책 ›') : name(r.sec) + ' ›'}</span></button>)
        : <div style={{padding:'9px 12px',fontSize:13.5,color:'#6d6f9c'}}>{t('Nothing found. Try another word.', '찾지 못했어요. 다른 낱말로 해 봐요.')}</div>}
    </div>}
    {on && <div ref={box} aria-hidden="true" style={{display:'none'}}><RefGo.Provider value={null}>{REF_SECS.map(sec => { const B = REF_BODY[sec.id]; return B ? <div key={sec.id} data-ref-find={sec.id}><B/></div> : null; })}</RefGo.Provider></div>}
  </div>;
}
'''
rep("const SHELF_TOOLS = {", comp + "const SHELF_TOOLS = {")
# put it under the greeting, and let a result open its book at the row
rep("    {onTool && <div data-ref-favs", "    <RefSearch onOpen={(id, q) => { pick(id); if (q) setTimeout(() => { try { const pn = document.querySelector('[data-ref-panel=\"' + id + '\"]'); if (!pn) return; const f = refFold(q).trim(); const el = [...pn.querySelectorAll(REF_FIND_SEL)].find(e => !e.querySelector(REF_FIND_SEL) && refFold(e.textContent).includes(f)); if (el) { el.scrollIntoView({ behavior: 'smooth', block: 'center' }); const o = el.style.background; el.style.background = '#ffe9df'; el.style.transition = 'background .6s'; setTimeout(() => { el.style.background = o; }, 1800); } } catch (e) {} }, 380); }}/>\n    {onTool && <div data-ref-favs")
open(p,'w').write(s); print('ok')
