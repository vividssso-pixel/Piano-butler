# Phase 393 (Sohyun 2026-10-09, second round on the chapter 2 print): (1) no print note on the spread cover;
# (2)+(5) the Lesson Book's words are bigger and easier to read, and "At the piano" is its own boxed section -- in every
# chapter's Lesson Book; (3) only the characters are hand-drawn: frames, houses, props, clouds and waves are drawn clean
# and straight (the pen engine wobbles a shape only when it belongs to a character); (4) the Workbook's page strip keeps
# only the step and its code (no Set / Due / minutes / drill line); (6) the honey pots lose their numbers: a dotted
# path from start to finish, traced in one smooth line.
# Run from the repo root: python3 _workspace/chapter-review/lessonbook/patch393.py
import json, os, re
p = 'drills.src.html'
s = open(p, encoding='utf-8').read()
here = os.path.dirname(os.path.abspath(__file__))
done = []
def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    assert c == n, f"{what}: expected {n}, got {c}"
    s = s.replace(a, b); done.append(what)

# (1) the spread cover: no print note
rep("""        <div style={{maxWidth:420,fontSize:13,color:BK.ink,lineHeight:1.55,border:'1.5px dashed ' + BK.line,borderRadius:12,padding:'10px 16px'}}>
          <b>Print double-sided</b> (flip on the long edge). Each Lesson Book page is on the left and its Workbook page faces it on the right, with the same page number. Read the left page, then do the right one.
        </div>
""", "", 'cover: no print note')

# (3) only the characters wobble
rep("""function penBakeList(list, hatch, shift, step = 4.6, small = 17) {
  let out = '';
  const fld = (x, y) => penField(x - shift[0], y - shift[1]);
  list.forEach(e => {
    if (e.k === 'g') { const sh = e.shift ? [shift[0] + e.shift[0], shift[1] + e.shift[1]] : shift;
      out += '<g' + (e.who ? ' data-who="' + e.who + '"' : '') + (e.hide ? ' display="none"' : '') + (e.testid ? ' data-testid="' + e.testid + '"' : '') + (e.floor != null ? ' data-map-stage="' + e.floor + '"' : '') + '>' + penBakeList(e.kids, hatch, sh, step, small) + '</g>'; return; }
    if (e.k === 'raw') { out += e.svg; return; }   // already drawn (a baked book picture, a small icon): passed through as it is
    if (e.nw) { out += penPlain(e, hatch); return; }   // keyboards: straight, no wobble (Sohyun 2026-10-09)""",
    """// Sohyun 2026-10-09 (Phase 393): only the characters look hand-drawn -- a shape wobbles only when it (or its group)
// carries ch: true (the siblings, their limbs and hands, the turtle, the bird); frames, houses, props, clouds and
// waves are drawn clean and straight, so a big frame never looks like a mistake.
function penBakeList(list, hatch, shift, step = 4.6, small = 17, chr = false) {
  let out = '';
  const fld = (x, y) => penField(x - shift[0], y - shift[1]);
  list.forEach(e => {
    if (e.k === 'g') { const sh = e.shift ? [shift[0] + e.shift[0], shift[1] + e.shift[1]] : shift;
      out += '<g' + (e.who ? ' data-who="' + e.who + '"' : '') + (e.hide ? ' display="none"' : '') + (e.testid ? ' data-testid="' + e.testid + '"' : '') + (e.floor != null ? ' data-map-stage="' + e.floor + '"' : '') + '>' + penBakeList(e.kids, hatch, sh, step, small, chr || !!e.ch) + '</g>'; return; }
    if (e.k === 'raw') { out += e.svg; return; }   // already drawn (a baked book picture, a small icon): passed through as it is
    if (e.nw) { out += penPlain(e, hatch); return; }   // keyboards: straight, no wobble (Sohyun 2026-10-09)
    if (e.k !== 'tx' && !(chr || e.ch)) { out += penPlain(e, hatch); return; }   // not a character: clean and straight""", 'engine: characters only')
rep("""  return [{ k: 'g', who: 'girl', hide: who !== 'girl', kids: penGirl(j, face) }, { k: 'g', who: 'boy', hide: who !== 'boy', kids: penBoy(j, face) }];""",
    """  return [{ k: 'g', ch: true, who: 'girl', hide: who !== 'girl', kids: penGirl(j, face) }, { k: 'g', ch: true, who: 'boy', hide: who !== 'boy', kids: penBoy(j, face) }];""", 'penKid is a character')
rep("""function penLimb(chain, w, fill, out = PEN_N, ow = 2.2) {
  const a = [{ k: 'pl', p: chain, s: out, w: w + 2 * ow }];
  if (fill !== out) a.push({ k: 'pl', p: chain, s: fill, w });""",
    """function penLimb(chain, w, fill, out = PEN_N, ow = 2.2) {
  const a = [{ k: 'pl', p: chain, s: out, w: w + 2 * ow, ch: true }];
  if (fill !== out) a.push({ k: 'pl', p: chain, s: fill, w, ch: true });""", 'limbs are characters')
rep("""function fsTurtle(x, y, k = 1) {
  const s = [], P = (a, b) => [x + a * k, y + b * k];""", """function fsTurtle(x, y, k = 1) { return fsTurtle0(x, y, k).map(e => ({ ...e, ch: true })); }
function fsTurtle0(x, y, k = 1) {
  const s = [], P = (a, b) => [x + a * k, y + b * k];""", 'turtle is a character')
rep("""function fsBird(x, y, k = 1) {
  const s = [];""", """function fsBird(x, y, k = 1) { return fsBird0(x, y, k).map(e => ({ ...e, ch: true })); }
function fsBird0(x, y, k = 1) {
  const s = [];""", 'bird is a character')
a = s.index("function wuGlideTop(")
b = s.index("\nfunction wuGlide(", a)
seg = s[a:b]
i = seg.rindex("  return s;\n}")
seg = seg[:i] + "  return s.map(e => e.nw ? e : { ...e, ch: true });   // everything but the keyboard is the child, seen from above\n}" + seg[i + len("  return s;\n}"):]
s = s[:a] + seg + s[b:]; done.append('glide: the child is a character')

# (2)+(5) the words are bigger; "At the piano" is its own section
rep("""function LbSay({ children, size = 16.5 }) {
  return <p style={{fontSize:size,lineHeight:1.5,color:BK.ink,margin:0}}>{children}</p>;
}""", """// Sohyun 2026-10-09 (Phase 393): the lesson's words must be easy to read -- bigger, a little heavier, more air
function LbSay({ children, size = 16.5 }) {
  return <p className="lb-say" style={{fontSize:Math.max(size + 1.5, 18),lineHeight:1.55,fontWeight:500,color:BK.ink,margin:'2px 0'}}>{children}</p>;
}""", 'LbSay bigger')
rep("""function LbPiano({ steps, title }) {
  return (
    <div>
      <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:7}}><LbKeysIcon/><span style={{fontFamily:LB_SERIF,fontSize:21,fontWeight:800,color:BK.ink}}>{title || t('At the piano', '피아노 앞에서')}</span></div>""",
    """function LbPiano({ steps, title }) {
  return (
    <div className="lb-piano" style={{border:'1.5px solid #e6dfcf',borderRadius:14,padding:'10px 14px 12px',background:'#fffdf7'}}>
      <div style={{display:'flex',alignItems:'center',gap:8,marginBottom:7}}><LbKeysIcon/><span style={{fontFamily:LB_SERIF,fontSize:21,fontWeight:800,color:BK.ink}}>{title || t('At the piano', '피아노 앞에서')}</span></div>""", 'LbPiano boxed')
rep("""      <div className="bk-body" style={{flex:1,minHeight:0,overflow:'hidden',display:'flex',flexDirection:'column',gap:14}}><BkChapterCtx.Provider value={chId}>{children}</BkChapterCtx.Provider></div>""",
    """      <div className="bk-body" style={{flex:1,minHeight:0,overflow:'hidden',display:'flex',flexDirection:'column',gap:16}}><BkChapterCtx.Provider value={chId}>{children}</BkChapterCtx.Provider></div>""", 'page gap')

# (4) the Workbook's page strip: the step and its code only
rep("""function WbTop({ step, mins = 10 }) {
  const chId = React.useContext(BkChapterCtx);
  const blank = (w) => <span style={{display:'inline-block',width:w,borderBottom:'1px solid ' + BK.ink}}>&nbsp;</span>;
  const n = bkStepNo(step);
  return (
    <div style={{display:'flex',alignItems:'center',gap:8,fontSize:11.5,color:BK.ink,margin:'0 0 4px',border:'1.4px solid ' + BK.line,borderRadius:9,padding:'3px 8px 3px 10px',background:BK.soft}}>
      <div style={{flex:1,display:'flex',flexWrap:'wrap',alignItems:'center',gap:'1px 10px',lineHeight:1.35}}>
        <b style={{color:BK.coral,fontSize:12.5}}>{bkStepLabel(step)}</b>
        <span>Set {blank(36)}</span>
        <span>Due {blank(36)}</span>
        <span style={{color:BK.muted}}>{mins} min</span>
        <span style={{color:BK.muted}}>· scan → {isNaN(n) ? 'the lesson' : 'step ' + n} online first · drill level {blank(20)} best {blank(20)}/10</span>
      </div>
      <QR url={bkStepLink(chId, step)} size={40}/>
    </div>
  );
}""", """// Sohyun 2026-10-09 (Phase 393): no Set / Due / minutes / drill line -- just which step this is, and its code
function WbTop({ step }) {
  const chId = React.useContext(BkChapterCtx);
  return (
    <div className="wb-top" style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8,margin:'0 0 2px'}}>
      <b style={{color:BK.coral,fontSize:12.5}}>{bkStepLabel(step)}</b>
      <span style={{display:'inline-flex',alignItems:'center',gap:6,fontSize:10.5,color:BK.muted}}>online<QR url={bkStepLink(chId, step)} size={34}/></span>
    </div>
  );
}""", 'page strip')
rep("""    <div style={{...bkH(18, 4), marginTop:10}}>The strip at the top of each page</div>""", """    <div style={{...bkH(18, 4), marginTop:10}}>The top of each page</div>""", 'front: strip title')
a = s.index("""    <div style={{...bkH(18, 4), marginTop:10}}>The top of each page</div>""")
b = s.index("""    <div style={{...bkH(18, 4), marginTop:10}}>In the app</div>""", a)
s = s[:a] + """    <div style={{...bkH(18, 4), marginTop:10}}>The top of each page</div>
    <div style={{fontSize:12.5,color:BK.ink,lineHeight:1.5}}>It names the lesson step the page belongs to. The small code opens that very step in the app: scan it <b>before</b> the page to see and hear the idea, and <b>after</b> the page to play the drill.</div>
""" + s[b:]
done.append('front: strip text')

# (6) the honey pots: a dotted path, start to finish, no numbers
rep("""Draw a smooth snake joining the honey pots without lifting your pencil!">""",
    """Trace the dotted path from pot to pot in one smooth line -- don't lift your pencil, no gaps: that's legato!">""", 'honey pots: words')
rep('<svg viewBox="0 0 640 112" style={{width:\'100%\',display:\'block\'}}>\n        {[[40, 80]', '<svg viewBox="0 0 640 140" style={{width:\'100%\',display:\'block\'}}>\n        {[[40, 80]', 'honey pots: taller box')
a = s.index("""        {[[40, 80], [150, 40], [260, 76], [370, 30], [480, 72], [590, 38]].map(([x, y], i) =>""")
b = s.index("""      </svg>""", a)
s = s[:a] + """        {(() => { const R = [[40, 98], [150, 58], [260, 94], [370, 48], [480, 90], [590, 56]].map(([x, y]) => [x, y - 22]);
          let d = 'M' + R[0][0] + ' ' + R[0][1];
          for (let i = 1; i < R.length; i++) { const [x0, y0] = R[i - 1], [x1, y1] = R[i], mx = (x0 + x1) / 2, cy = Math.min(y0, y1) - 12; d += ' C' + mx + ' ' + cy + ' ' + mx + ' ' + cy + ' ' + x1 + ' ' + y1; }
          return <path d={d} fill="none" stroke={BK.coral} strokeWidth="2" strokeDasharray="2 6" strokeLinecap="round"/>; })()}
        {[[40, 98], [150, 58], [260, 94], [370, 48], [480, 90], [590, 56]].map(([x, y], i) => <g key={i}><path d={`M${x - 18} ${y - 14} Q${x - 22} ${y + 22} ${x} ${y + 22} Q${x + 22} ${y + 22} ${x + 18} ${y - 14} Z`} fill="#fff" stroke={BK.ink} strokeWidth="1.6"/><rect x={x - 20} y={y - 19} width="40" height="6" rx="2" fill={BK.ink}/></g>)}
        <text x="40" y="134" textAnchor="middle" fontSize="11" fontWeight="800" fill={BK.coral}>start</text>
        <text x="590" y="92" textAnchor="middle" fontSize="11" fontWeight="800" fill={BK.coral}>finish</text>
""" + s[b:]
done.append('honey pots: dotted path')

rep("Goes with: the Workbook page beside each lesson page, and the online lesson (scan the code below).", "Goes with: the Workbook page beside each lesson page, and the online lesson.", 'opener: no code below', 2)

# (3) the baked book drawings: props straight too (chars8.py + handside.py mark them data-rigid; art393.json = the rebaked ones)
art = json.load(open(os.path.join(here, '..', 'art', 'art393.json'), encoding='utf-8'))
for k, v in art.items():
    m = re.search(r'("%s": )(".*?")(,\n|\n)' % re.escape(k), s)
    assert m, k
    s = s[:m.start(2)] + json.dumps(v, ensure_ascii=False) + s[m.end(2):]
done.append('%d baked drawings with straight props' % len(art))

open(p, 'w', encoding='utf-8').write(s)
print('\n'.join('ok: ' + d for d in done))
print('PATCH 393 DONE')
