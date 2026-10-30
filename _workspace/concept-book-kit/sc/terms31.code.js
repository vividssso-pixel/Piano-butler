
// ─── Build DO (call 31, her 21:23, 21:25 and 21:41): the dictionary ───────────────────────────────────────────
// A term an earlier room taught, met again in a later room's text, is underlined (dotted navy) on screen; a tap opens a
// small card: the term, one neutral line (no metaphors: those stay inside the rooms), the room's own small picture,
// 'Go to the room', and a one-question quick check from that room's own check. The opener also shows 'Bring with you':
// up to four such terms, the ones the chapter's text uses most (DICT_BRING, baked from the Lesson Books by scan31.js).
// Only terms from rooms before this one, and the first time each appears on a screen page. The books print the
// 'Bring with you' line on the opener (no underlines in print). The definitions are mine (terms31.json), for her to check.
const DICT_TERMS = [
__TERMS__
];
const DICT_BY_ID = Object.fromEntries(DICT_TERMS.map(x => [x.id, x]));
const DICT_BRING = __BRING__;
const dictName = (x) => (LANG === 'ko' ? x.ko[0] : x.en[0]);
const DICT_RX = (() => {
  const esc = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), en = [], ko = [];
  DICT_TERMS.forEach(x => { x.en.forEach(a => en.push([a, x.id])); x.ko.forEach(a => ko.push([a, x.id])); });
  en.sort((a, b) => b[0].length - a[0].length); ko.sort((a, b) => b[0].length - a[0].length);
  return { en: { rx: new RegExp('\\b(' + en.map(x => esc(x[0])).join('|') + ')\\b', 'gi'), map: Object.fromEntries(en.map(([a, i]) => [a.toLowerCase(), i])) },
    ko: { rx: new RegExp('(' + ko.map(x => esc(x[0])).join('|') + ')', 'g'), map: Object.fromEntries(ko) } };
})();
const DictCtx = React.createContext(null);     // { open(id), room(id) }: the App
const GlossSeen = React.createContext(null);   // one Set per screen page: each term underlined once a page
function dictEarlier(id, ch) { const x = DICT_BY_ID[id]; if (!x || x.room === ch) return false; const a = bkChapterNo(x.room), b = bkChapterNo(ch); return a > 0 && b > 0 && a < b; }
function glossText(s, ch, seen) {
  const L = LANG === 'ko' ? DICT_RX.ko : DICT_RX.en, out = []; let last = 0, m; L.rx.lastIndex = 0;
  while ((m = L.rx.exec(s))) { const id = L.map[LANG === 'ko' ? m[1] : m[1].toLowerCase()]; if (!id || !dictEarlier(id, ch) || (seen && seen.has(id))) continue; if (seen) seen.add(id); out.push(s.slice(last, m.index), <DictLink key={m.index} id={id}>{m[1]}</DictLink>); last = m.index + m[1].length; }
  if (!out.length) return s; out.push(s.slice(last)); return out;
}
function glossNode(node, ch, seen) {
  if (typeof node === 'string') return glossText(node, ch, seen);
  if (Array.isArray(node)) return node.map((n, i) => <React.Fragment key={i}>{glossNode(n, ch, seen)}</React.Fragment>);
  if (React.isValidElement(node) && (typeof node.type === 'string' || node.type === React.Fragment) && node.props.children != null && !node.props.dangerouslySetInnerHTML) return React.cloneElement(node, {}, glossNode(node.props.children, ch, seen));
  return node;
}
function DictLink({ id, children }) {
  const Tc = React.useContext(DictCtx);
  return <button type="button" className="term-link" data-term={id} onClick={() => Tc && Tc.open(id)} style={{all:'unset',cursor:'pointer',borderBottom:'1.6px dotted var(--navy)',paddingBottom:1}}>{children}</button>;
}
function Gloss({ children }) {   // on screen, inside a chapter: the earlier rooms' words become links
  const scr = React.useContext(LbScreenCtx), ch = React.useContext(BkChapterCtx), seen = React.useContext(GlossSeen);
  if (!scr || !ch) return children;
  return glossNode(children, ch, seen);
}
function DictIcon({ room, size = 46 }) { return <svg viewBox="0 0 48 44" width={size} height={size * 44 / 48} fill="none" stroke={BK.ink} strokeWidth="1.6" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" dangerouslySetInnerHTML={{ __html: HOUSE_ICONS[room] || '' }}/>; }
function DictChips({ ch, label }) {   // 'Bring with you': the opener's chips (screen)
  const Tc = React.useContext(DictCtx), ids = (DICT_BRING[ch] || []).filter(id => dictEarlier(id, ch));
  if (!ids.length) return null;
  return <div data-term-chips={ch} style={{display:'flex',alignItems:'center',flexWrap:'wrap',gap:6,margin:'2px 0 8px'}}>
    <span style={{fontSize:11.5,fontWeight:900,color:'var(--muted)',letterSpacing:'0.06em'}}>{label || t('BRING WITH YOU', '가져올 것')}</span>
    {ids.map(id => <button key={id} type="button" className="chip" data-term={id} style={{padding:'3px 10px',fontSize:13,fontWeight:800}} onClick={() => Tc && Tc.open(id)}>{dictName(DICT_BY_ID[id])}</button>)}
  </div>;
}
function DictCard({ id, onClose }) {
  const x = DICT_BY_ID[id], Tc = React.useContext(DictCtx);
  const [chk, setChk] = useState(false), [res, setRes] = useState(null);
  if (!x) return null;
  const room = x.room, lv = (chkLevels(room) || [])[0];
  return <div role="dialog" aria-label={dictName(x)} data-term-card={id} onClick={onClose} style={{position:'fixed',inset:0,zIndex:60,background:'rgba(38,41,107,0.28)',display:'flex',alignItems:'flex-end',justifyContent:'center'}}>
    <div onClick={(e) => e.stopPropagation()} style={{background:'#fffefa',borderRadius:'14px 14px 0 0',width:'100%',maxWidth:560,maxHeight:'88vh',overflow:'auto',padding:'14px 16px 20px',boxShadow:'0 -6px 24px rgba(38,41,107,0.18)'}}>
      <div style={{display:'flex',alignItems:'center',gap:12}}>
        <DictIcon room={room}/>
        <div style={{flex:1,minWidth:0}}>
          <div style={{fontFamily:LB_SERIF,fontSize:23,fontWeight:900,color:'var(--navy)',lineHeight:1.1}}>{dictName(x)}</div>
          <div style={{fontSize:12,color:'var(--muted)',fontWeight:700,marginTop:2}}>{(LANG === 'ko' ? bkChapterNo(room) + '장' : 'Chapter ' + bkChapterNo(room)) + ' · ' + bkChapterName(room)}</div>
        </div>
        <button type="button" className="chip" aria-label={t('Close', '닫기')} style={{padding:'3px 10px'}} onClick={onClose}>✕</button>
      </div>
      <div style={{fontSize:16.5,lineHeight:1.5,color:BK.ink,margin:'10px 0 12px'}}>{t(x.defEn, x.defKo)}</div>
      <div style={{display:'flex',gap:8,flexWrap:'wrap',alignItems:'center'}}>
        <button type="button" className="primary-btn" data-term-room={room} style={{width:'auto',padding:'8px 14px',fontSize:14}} onClick={() => Tc && Tc.room(room)}>{t('Go to the room →', '그 방으로 →')}</button>
        {!chk && lv && <button type="button" className="chip" data-term-check="1" style={{padding:'6px 12px',fontSize:13.5,fontWeight:800}} onClick={() => { setRes(null); setChk(true); }}>{t('Quick check', '바로 확인')}</button>}
        {res != null && <span style={{fontSize:14,fontWeight:800,color:res ? '#2e8a6e' : 'var(--navy)'}}>{res ? t('Got it!', '맞았어요!') : t('Not yet: the room is one tap away.', '아직이에요: 그 방이 한 번에 열려요.')}</span>}
      </div>
      {chk && lv && <CheckRun items={[{ id: room, lv }]} onDone={(r) => { setRes(!!(r[0] && r[0].ok)); setChk(false); }} onQuit={() => setChk(false)}/>}
    </div>
  </div>;
}
