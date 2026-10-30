#!/usr/bin/env python3
"""Build DP (on t790 -> t791; her 22:26, 22:30, 22:53 and 23:05: calls 34 to 37).
34  The doll's house lights only the room you are in: a warm window glow behind that room, the others as before.
35  'I don't know' in the placement: a button under each question, counted as a miss, the count shown in the result.
36  The placement judges by skill inside a floor (A): a floor's questions come round-robin from four skills (ear, rhythm,
    reading, keys and scales: PLACE_SKILL); a miss in one skill only (4 of 6) still climbs, and that skill's rooms are
    'rooms to review': in the result, saved with the placement (pb_place_v1.review) and marked in the house until the
    room's check is passed.
37  The Scale finder: a Quick line at the top of the Home (Scale finder, Metronome), a card at the top of every scales
    room's 'More to play with'; one keyboard, two octaves wide, right-hand numbers above the keys and left-hand numbers
    below, thumbs in coral, thin navy brackets for the finger groups instead of coloured fills; black keys named only
    when the scale uses them, spelt for the key; hands-together: one tap is one note, both hands' keys light and sound.
"""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)

# ── 34: the lit room ──
R("""    + p('thwp-damask', 12, 14, '<path d="M6 2 L9 7 L6 12 L3 7 Z" fill="none" stroke="' + N + '" stroke-width="0.8"/>')""",
  """    + '<radialGradient id="thglow" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="#ffd98a" stop-opacity="0.75"/><stop offset="0.55" stop-color="#ffe9b8" stop-opacity="0.45"/><stop offset="1" stop-color="#fff6dc" stop-opacity="0"/></radialGradient>'   // Build DP (34): the lit room
    + p('thwp-damask', 12, 14, '<path d="M6 2 L9 7 L6 12 L3 7 Z" fill="none" stroke="' + N + '" stroke-width="0.8"/>')""")
R("""  let s = '<rect x="' + pFix(x) + '" y="' + pFix(y) + '" width="' + pFix(w) + '" height="' + pFix(h) + '" stroke-width="1"/>';
  if (fs.wp === 'drape') {""", """  let s = '<rect x="' + pFix(x) + '" y="' + pFix(y) + '" width="' + pFix(w) + '" height="' + pFix(h) + '" stroke-width="1"/>';
  if (on) s += '<rect x="' + pFix(x + 1) + '" y="' + pFix(y + 1) + '" width="' + pFix(w - 2) + '" height="' + pFix(h - 2) + '" fill="#fff4d6" stroke="none"/><rect x="' + pFix(x + 1) + '" y="' + pFix(y + 1) + '" width="' + pFix(w - 2) + '" height="' + pFix(h - 2) + '" fill="url(#thglow)" stroke="none"/>';   // Build DP (34): the light is on in your room
  if (fs.wp === 'drape') {""")

# ── 35 and 36: the placement ──
R("""function CheckRun({ items, floor, onDone, onQuit }) {""", """function CheckRun({ items, floor, onDone, onQuit, dunno }) {   // Build DP (35): dunno: an 'I don't know' button (the placement)""")
R("""  const answer = (ans, force) => {
    if (given || !it) return;
    let ok = false; if (force != null) ok = !!force; else { try { ok = ans !== null && ans !== undefined && !!drill.check(it.q, ans); } catch (e) { ok = false; } }
    const r = res.concat([{ id: it.id, n: it.lv.n, ok }]);""", """  const answer = (ans, force, dk) => {
    if (given || !it) return;
    let ok = false; if (force != null) ok = !!force; else { try { ok = ans !== null && ans !== undefined && !!drill.check(it.q, ans); } catch (e) { ok = false; } }
    const r = res.concat([{ id: it.id, n: it.lv.n, ok, dunno: !!dk }]);""")
R("""      {given && <button className="primary-btn" style={{marginTop:10}} onClick={() => next(res)}>{i + 1 >= list.length ? t('See how I did →', '결과 보기 →') : t('Next →', '다음 →')}</button>}
    </div>
    <button className="ghost-btn" style={{marginTop:8,fontSize:13}} onClick={() => { clearTimeout(timer.current); try { stopClicks(); } catch (e) {} onQuit(); }}>{t('Stop the check', '그만하기')}</button>""",
  """      {given && <button className="primary-btn" style={{marginTop:10}} onClick={() => next(res)}>{i + 1 >= list.length ? t('See how I did →', '결과 보기 →') : t('Next →', '다음 →')}</button>}
    </div>
    <div style={{display:'flex',gap:8,flexWrap:'wrap',alignItems:'center'}}>
      <button className="ghost-btn" style={{marginTop:8,fontSize:13}} onClick={() => { clearTimeout(timer.current); try { stopClicks(); } catch (e) {} onQuit(); }}>{t('Stop the check', '그만하기')}</button>
      {dunno && !given && <button className="ghost-btn" data-testid="check-dunno" style={{marginTop:8,fontSize:13}} onClick={() => answer(null, false, true)}>{t("I don't know", '모르겠어요')}</button>}
    </div>""")
# the skills, the round-robin, the one-skill pass, the review rooms
R("""const placeFloor = () => {""", """// Build DP (36, her A): a room's skill, for the placement: a floor's questions come round-robin from the four skills, and a
// miss in one skill only still climbs, with that skill's rooms marked to review
const PLACE_SKILL = (id) => /^(listen|ear-)/.test(id) ? 'ear' : /^(pulse|note-values|time-signatures|rhythm|six-eight|tempo)/.test(id) ? 'rhythm' : /^(note-names|staff|reading-steps|whole-staff|ledger-lines|signs|dynamics|terms|accidentals|key-signatures|keys-)/.test(id) ? 'reading' : 'keys';
const PLACE_SKILL_NAME = { ear: ['ear', '귀'], rhythm: ['rhythm', '리듬'], reading: ['reading', '악보 읽기'], keys: ['keys and scales', '건반과 스케일'] };
const placeReview = () => { const p = loadPlace(); return p && Array.isArray(p.review) ? p.review : []; };
const placeFloor = () => {""")
R("""function placeItems(ids, n, noSound) {   // n questions from as many rooms as possible; the theory ladder asks without sound or tapping
  const lv = (id) => chkLevels(id).filter(l => !(noSound && l.noPrint));
  const rooms = chkShuffle(ids.filter(id => lv(id).length)), out = [];
  let r = 0; while (out.length < n && rooms.length) { const id = rooms[r % rooms.length], L = lv(id); out.push({ id, lv: L[Math.floor(Math.random() * L.length)] }); r++; }
  return chkShuffle(out);
}""", """function placeItems(ids, n, noSound) {   // n questions from as many rooms as possible, round-robin over the four skills (Build DP); the theory ladder asks without sound or tapping
  const lv = (id) => chkLevels(id).filter(l => !(noSound && l.noPrint));
  const bySkill = {}; chkShuffle(ids.filter(id => lv(id).length)).forEach(id => { const k = PLACE_SKILL(id); (bySkill[k] = bySkill[k] || []).push(id); });
  const skills = chkShuffle(Object.keys(bySkill)), out = []; if (!skills.length) return out;
  let r = 0; while (out.length < n) { const k = skills[r % skills.length], list = bySkill[k], id = list[Math.floor(r / skills.length) % list.length], L = lv(id); out.push({ id, lv: L[Math.floor(Math.random() * L.length)] }); r++; }
  return chkShuffle(out);
}""")
R("""  const [down, setDown] = useState(false), [last, setLast] = useState(null), [res, setRes] = useState({}), [miss, setMiss] = useState([]);""",
  """  const [down, setDown] = useState(false), [last, setLast] = useState(null), [res, setRes] = useState({}), [miss, setMiss] = useState([]);
  const [review, setReview] = useState([]), [dk, setDk] = useState(0);   // Build DP: the rooms of a one-skill miss; the 'I don't know' count""")
R("""  const begin = () => { setRes({}); setMiss([]); setDown(false); ask('piano', placeStartRung(lads.piano, pg)); };""",
  """  const begin = () => { setRes({}); setMiss([]); setReview([]); setDk(0); setDown(false); ask('piano', placeStartRung(lads.piano, pg)); };""")
R("""    try { localStorage.setItem(PLACE_KEY, JSON.stringify({ piano: piano.k, theory: th ? th.n : 7, at: Date.now() })); } catch (e) {}""",
  """    try { localStorage.setItem(PLACE_KEY, JSON.stringify({ piano: piano.k, theory: th ? th.n : 7, at: Date.now(), review: [...new Set(review)] })); } catch (e) {}""")
R("""  const done = (r) => {
    const right = r.filter(x => x.ok).length, pass = right >= PLACE_PASS, missed = r.filter(x => !x.ok).map(x => x.id);
    setLast({ right, total: r.length, pass, name: rungName(track, rung) });
    if (pass) { setMiss(m => m.concat(missed)); if (rung + 1 < lad.length && !down) { setPhase('climb'); return; } finish(track, down ? rung + 1 : lad.length); return; }""",
  """  const done = (r) => {
    const right = r.filter(x => x.ok).length, missed = r.filter(x => !x.ok).map(x => x.id), skills = [...new Set(missed.map(PLACE_SKILL))];
    const oneSkill = right === PLACE_PASS - 1 && skills.length === 1, pass = right >= PLACE_PASS || oneSkill;   // Build DP (36): a miss in one skill only still climbs
    setDk(x => x + r.filter(x => x.dunno).length);
    setLast({ right, total: r.length, pass, name: rungName(track, rung), skill: oneSkill ? skills[0] : null });
    if (pass) { setMiss(m => m.concat(missed)); if (oneSkill) setReview(v => v.concat([...new Set(missed)])); if (rung + 1 < lad.length && !down) { setPhase('climb'); return; } finish(track, down ? rung + 1 : lad.length); return; }""")
R("""    <CheckRun key={'p' + runKey} items={items} floor onDone={done} onQuit={onClose}/>""", """    <CheckRun key={'p' + runKey} items={items} floor dunno onDone={done} onQuit={onClose}/>""")
R("""    <div style={{fontSize:16,fontWeight:900,color:phase === 'climb' ? '#2e8a6e' : '#26296b',margin:'4px 0 10px'}}>{phase === 'climb' ? t(last.name + ': easy for you! Up a floor.', last.name + ': 쉽네요! 한 층 위로.') :""",
  """    <div style={{fontSize:16,fontWeight:900,color:phase === 'climb' ? '#2e8a6e' : '#26296b',margin:'4px 0 10px'}}>{phase === 'climb' ? (last.skill ? t(last.name + ': up a floor, and ' + PLACE_SKILL_NAME[last.skill][0] + ' rooms to review.', last.name + ': 한 층 위로, ' + PLACE_SKILL_NAME[last.skill][1] + ' 방은 다시 볼 방.') : t(last.name + ': easy for you! Up a floor.', last.name + ': 쉽네요! 한 층 위로.')) :""")
R("""    const visit = [...new Set(miss)].filter(id => pathIds().indexOf(id) >= 0);""",
  """    const rev = [...new Set(review)].filter(id => pathIds().indexOf(id) >= 0), visit = [...new Set(miss)].filter(id => pathIds().indexOf(id) >= 0 && !rev.includes(id));   // Build DP""")
R("""        {visit.length > 0 && <div style={{borderTop:'1px solid rgba(38,41,107,0.12)',paddingTop:8}}>
          <div style={{fontSize:13,fontWeight:800,color:'#4a4d86',margin:'0 0 4px'}}>{t('Missed on the way up: worth a quick look', '올라오다 틀린 방: 잠깐 들러 봐요')}</div>
          <div style={{display:'flex',flexWrap:'wrap',gap:6}}>{visit.slice(0, 6).map(room)}</div></div>}""",
  """        {rev.length > 0 && <div data-testid="place-review" style={{borderTop:'1px solid rgba(38,41,107,0.12)',paddingTop:8}}>
          <div style={{fontSize:13,fontWeight:900,color:'#e4572e',margin:'0 0 4px'}}>{t('Rooms to review: the house marks them until their check is passed', '다시 볼 방: 체크를 통과할 때까지 집에 표시돼요')}</div>
          <div style={{display:'flex',flexWrap:'wrap',gap:6}}>{rev.slice(0, 8).map(room)}</div></div>}
        {visit.length > 0 && <div style={{borderTop:'1px solid rgba(38,41,107,0.12)',paddingTop:8}}>
          <div style={{fontSize:13,fontWeight:800,color:'#4a4d86',margin:'0 0 4px'}}>{t('Missed on the way up: worth a quick look', '올라오다 틀린 방: 잠깐 들러 봐요')}</div>
          <div style={{display:'flex',flexWrap:'wrap',gap:6}}>{visit.slice(0, 6).map(room)}</div></div>}
        {dk > 0 && <div style={{fontSize:12.5,color:'#6d6f9c'}}>{t("'I don't know': " + dk + (dk === 1 ? ' time' : ' times') + ', counted as misses.', "'모르겠어요' " + dk + '번, 틀린 것으로 셌어요.')}</div>}""")
# the house marks the rooms to review
R("""  const star = view.star && view.star[id];   // Build CN: the chapter check passed""",
  """  const star = view.star && view.star[id];   // Build CN: the chapter check passed
  if (!done && !star && view.review && view.review.includes(id)) { const rw = cmp ? 34 : 44, rh = cmp ? 10 : 12, rx0 = x + w - rw - (cmp ? 5 : 8), ry0 = y + h - 6 - (cmp ? 14 : 17);   // Build DP (36): a room to review, from the placement
    s += '<rect x="' + pFix(rx0) + '" y="' + pFix(ry0) + '" width="' + rw + '" height="' + rh + '" rx="' + (rh / 2) + '" fill="#fff" stroke="' + ST.C + '" stroke-width="0.9"/>' + stT(rx0 + rw / 2, ry0 + rh - (cmp ? 2.4 : 2.8), t('review', '다시'), { size: cmp ? 7 : 8.4, weight: 800, fill: ST.C, anchor: 'middle' }); }""")
R("""  const view = { stages, here, nums, focus: topic, star, pawn: name ? (x, y, k) => stPiece(VIC_PAWN_NAVY, x, y, k) : null };""",
  """  const view = { stages, here, nums, focus: topic, star, review: placeReview(), pawn: name ? (x, y, k) => stPiece(VIC_PAWN_NAVY, x, y, k) : null };   // Build DP: the rooms to review""")
R("""  const sig = stages.map(x => x.st.join(',')).join('|') + here + LANG + compact + name + today + fontTick + wide + (topic || '') + Object.keys(star).join(',');""",
  """  const sig = stages.map(x => x.st.join(',')).join('|') + here + LANG + compact + name + today + fontTick + wide + (topic || '') + Object.keys(star).join(',') + placeReview().join(',');""")

# ── 37: the Scale finder ──
R("""        <div style={{fontSize:12,fontWeight:900,color:'var(--muted)',letterSpacing:'0.05em',marginBottom:4}}>{t('RIGHT HAND', '오른손')}</div>
        <ScaleKeyboard rootPc={info.rootPc} offsets={offs} fingers={fing('RH')} hand="RH" plain={clash} names={names.concat([names[0]])}/>
        <div style={{fontSize:12,fontWeight:900,color:'var(--muted)',letterSpacing:'0.05em',margin:'10px 0 4px'}}>{t('LEFT HAND', '왼손')}</div>
        <ScaleKeyboard rootPc={info.rootPc} offsets={offs} fingers={fing('LH')} hand="LH" plain={clash} names={names.concat([names[0]])}/>
        <div style={{display:clash ? 'none' : 'flex',gap:10,flexWrap:'wrap',alignItems:'center',justifyContent:'center',marginTop:8,fontSize:12,fontWeight:700,color:'#4a4d86'}}>
          <span style={{display:'inline-flex',alignItems:'center',gap:5}}><span style={{width:14,height:14,borderRadius:3,background:SEGMENT_COLORS.three.fill,border:'1.5px solid ' + SEGMENT_COLORS.three.stroke}}/>{t('1-2-3 group', '1-2-3 묶음')}</span>
          <span style={{display:'inline-flex',alignItems:'center',gap:5}}><span style={{width:14,height:14,borderRadius:3,background:SEGMENT_COLORS.four.fill,border:'1.5px solid ' + SEGMENT_COLORS.four.stroke}}/>{t('1-2-3-4 group', '1-2-3-4 묶음')}</span>
          <span style={{display:'inline-flex',alignItems:'center',gap:5}}><span style={{width:14,height:14,borderRadius:3,background:'#fff',border:'1.5px solid #7f81a8'}}/>{t('start / end note', '시작 / 끝 음')}</span>
        </div>""",
  """        <SfHandsKeyboard rootPc={info.rootPc} offsets={offs} fR={clash ? null : fing('RH')} fL={clash ? null : fing('LH')} names={names.concat([names[0]])} downOffsets={mode === 'minor' && form === 'melodic' ? minorOffsets('natural', oct) : null}/>""")
R("""        <div style={{textAlign:'center',marginTop:8}}><button className="ghost-btn" onClick={() => playScaleNotes(info.rootPc, offs, mode === 'minor' && form === 'melodic' ? minorOffsets('natural', oct) : null)}>{t('♪ Hear it up and down', '♪ 올라갔다 """,
  """        <div style={{textAlign:'center',marginTop:8,display:'none'}}><button className="ghost-btn" onClick={() => playScaleNotes(info.rootPc, offs, mode === 'minor' && form === 'melodic' ? minorOffsets('natural', oct) : null)}>{t('♪ Hear it up and down', '♪ 올라갔다 """)
R("""function ScaleFinderFree({ ext, onKey } = {}) {""", """// Build DP (37, her 22:53 and 23:05): one keyboard for both hands. Right-hand numbers above the keys, left-hand numbers
// below, the thumbs in coral; thin navy brackets join each finger group (from one thumb to the next) instead of coloured
// fills; a black key is named only when the scale uses it, spelt for the key. Hands together, one tap is one note: the
// key lights and both hands sound (the left an octave lower); 'Up and down' plays the whole scale both hands.
function SfHandsKeyboard({ rootPc, offsets, fR, fL, names, downOffsets }) {
  const total = offsets[offsets.length - 1], { keys, whiteCount } = buildKeyboard(rootPc, total);
  const W = 30, H = 78, BW = 18, BH = 48, TOP = 44, BOT = 40;
  const [at, setAt] = useState(-1), timer = useRef(null);
  const seq = useMemo(() => [...offsets, ...(downOffsets || offsets).slice(0, -1).reverse()], [offsets, downOffsets]);
  useEffect(() => { setAt(-1); return () => clearTimeout(timer.current); }, [rootPc, offsets]);
  const base = 60 + rootPc - (rootPc > 6 ? 12 : 0);
  const sound = (off) => { const ctx = getAudio(); if (!ctx) return; blip(ctx, ctx.currentTime + 0.01, 440 * Math.pow(2, (base + off - 69) / 12), 0.36, 0.2, 'triangle'); blip(ctx, ctx.currentTime + 0.01, 440 * Math.pow(2, (base + off - 12 - 69) / 12), 0.36, 0.16, 'triangle'); };
  const step = () => { clearTimeout(timer.current); const n = (at + 1) % seq.length; setAt(n); sound(seq[n]); };
  const playAll = () => { clearTimeout(timer.current); let i = 0; const tick = () => { setAt(i); sound(seq[i]); i++; if (i < seq.length) timer.current = setTimeout(tick, 320); else timer.current = setTimeout(() => setAt(-1), 500); }; tick(); };
  const xOf = (k) => k.isWhite ? k.whiteIndex * W + W / 2 : (k.precedingWhiteIndex + 1) * W;
  const idxOf = {}; offsets.forEach((o, i) => { idxOf[o] = i; });
  const litOff = at >= 0 ? seq[at] : null;
  const groups = (f, up) => { if (!f) return []; const g = []; let st = up ? f.indexOf(1) : 0; if (st < 0) st = 0; for (let i = st + 1; i <= f.length; i++) { if (i === f.length || (up ? f[i] === 1 : f[i - 1] === 1)) { if (i - st >= 2) g.push([st, i - 1]); st = i; } } return g; };
  const gR = groups(fR, true), gL = groups(fL, false);
  const num = (x, y, f, lit) => <g>{f === 1 && <circle cx={x} cy={y - 4.5} r="8.5" fill={lit ? '#e4572e' : '#fff'} stroke="#e4572e" strokeWidth="1.6"/>}<text x={x} y={y} textAnchor="middle" fontSize="13" fontWeight="900" fill={f === 1 ? (lit ? '#fff' : '#e4572e') : lit ? '#e4572e' : '#26296b'}>{f}</text></g>;
  const bracket = (g, y, dir) => g.map(([a, b], j) => { const x1 = xOf(keys[offsets[a]]) - 9, x2 = xOf(keys[offsets[b]]) + 9; return <path key={j} d={'M' + x1 + ' ' + (y - 4 * dir) + ' V' + y + ' H' + x2 + ' V' + (y - 4 * dir)} fill="none" stroke="#26296b" strokeWidth="1.1" opacity="0.7"/>; });
  return <div data-sf-hands>
    <svg viewBox={(-BW / 2) + ' 0 ' + (whiteCount * W + BW) + ' ' + (TOP + H + BOT)} style={{width:'100%',display:'block',margin:'0 auto'}}>
      {fR && <text x={-BW / 2 + 2} y="11" fontSize="9" fontWeight="900" fill="#6d6f9c" letterSpacing="0.06em">{t('RIGHT HAND', '오른손')}</text>}
      {fL && <text x={-BW / 2 + 2} y={TOP + H + BOT - 3} fontSize="9" fontWeight="900" fill="#6d6f9c" letterSpacing="0.06em">{t('LEFT HAND', '왼손')}</text>}
      {keys.filter(k => k.isWhite).map(k => { const i = idxOf[k.i], lit = litOff === k.i, inS = i != null; return <g key={'w' + k.i}>
        <rect x={k.whiteIndex * W} y={TOP} width={W} height={H} fill={lit ? '#fbe3da' : inS ? '#fff' : '#f6f3ea'} stroke={lit ? '#e4572e' : 'rgba(38,41,107,0.45)'} strokeWidth={lit ? 2 : 1.2}/>
        {inS && names[i] && <text x={xOf(k)} y={TOP + H - 8} textAnchor="middle" fontSize="11" fontWeight="900" fill="#26296b">{prettyAny(names[i])}</text>}
      </g>; })}
      {keys.filter(k => !k.isWhite).map(k => { const i = idxOf[k.i], lit = litOff === k.i, inS = i != null; return <g key={'b' + k.i}>
        <rect x={xOf(k) - BW / 2} y={TOP} width={BW} height={BH} fill={lit ? '#e4572e' : '#26296b'} stroke={inS ? '#fff' : 'none'} strokeWidth={inS ? 1.2 : 0}/>
        {inS && names[i] && <text x={xOf(k)} y={TOP + BH - 7} textAnchor="middle" fontSize="9.5" fontWeight="900" fill="#fff">{prettyAny(names[i])}</text>}
      </g>; })}
      {fR && offsets.map((o, i) => <React.Fragment key={'r' + i}>{num(xOf(keys[o]), TOP - 12, fR[i], litOff === o)}</React.Fragment>)}
      {fR && bracket(gR, TOP - 4, 1)}
      {fL && offsets.map((o, i) => <React.Fragment key={'l' + i}>{num(xOf(keys[o]), TOP + H + 22, fL[i], litOff === o)}</React.Fragment>)}
      {fL && bracket(gL, TOP + H + 6, -1)}
    </svg>
    <div style={{display:'flex',gap:8,flexWrap:'wrap',justifyContent:'center',alignItems:'center',marginTop:6}}>
      <button type="button" className="primary-btn" data-sf-step style={{width:'auto',padding:'9px 16px',fontSize:14}} onClick={step}>{at < 0 ? t('▶ Hands together: tap for each note', '▶ 양손: 한 음씩 탭') : t('Next note ▶', '다음 음 ▶')}</button>
      <button type="button" className="ghost-btn" data-sf-all style={{fontSize:13}} onClick={playAll}>{t('♪ Up and down', '♪ 올라갔다 내려오기')}</button>
      {at >= 0 && <button type="button" className="chip" style={{fontSize:12}} onClick={() => { clearTimeout(timer.current); setAt(-1); }}>{t('Reset', '처음으로')}</button>}
    </div>
    {!fR && !fL && <p style={{fontSize:13,color:'var(--muted)',margin:'8px 0 0',textAlign:'center',lineHeight:1.5}}>{t('No finger numbers for this form: look the fingering up in the book.', '이 형태엔 손가락 번호가 없어요: 책에서 찾아 보세요.')}</p>}
  </div>;
}
function ScaleFinderFree({ ext, onKey } = {}) {""")
# the finder in every scales room, and the chapter list's title without the Toolbox
R("""  const list = (CHAPTER_TOOL_ORDER[id] || []).filter(x => !/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|ivx|chx|tmx|fmx|mlx|cpx|csx|sac|ts|nv|mk)-/.test(x) && !own.includes(x) && !(MAKE_EXTRA[id] || []).includes(x)).map(x => TOOLS.find(tl => tl.id === x)).filter(Boolean);""",
  """  const SF_ROOMS = ['scales', 'scale-play', 'minor-scales', 'scales-23', 'scales-3', 'scales-4', 'scales-5', 'scales-6', 'scales-7', 'scales-8', 'arps-6', 'arps-7', 'arps-8'];   // Build DP (37): the Scale finder in every scales room, first
  const base = (CHAPTER_TOOL_ORDER[id] || []).filter(x => x !== 'scale-finder');
  const list = (SF_ROOMS.includes(id) ? ['scale-finder'].concat(base) : base).filter(x => !/^(sdy|ssk|srh|ssc|stm|sps|spr|skg|sgn|ivx|chx|tmx|fmx|mlx|cpx|csx|sac|ts|nv|mk)-/.test(x) && !own.includes(x) && !(MAKE_EXTRA[id] || []).includes(x)).map(x => TOOLS.find(tl => tl.id === x)).filter(Boolean);""")
R("""    <div style={{fontSize:14,fontWeight:900,color:'var(--text)',margin:'0 0 6px'}}>{t('More in the toolbox', '툴박스에 더 있어요')}</div>""",
  """    <div style={{fontSize:14,fontWeight:900,color:'var(--text)',margin:'0 0 6px'}}>{t('More to play with', '더 놀아 보기')}</div>""")
# the Home's Quick line
R("""      <h2 style={{fontFamily:"'Playfair Display', Georgia, serif",fontWeight:900,fontSize:32,lineHeight:1.1,margin:'4px 0 16px',color:'var(--navy)',textWrap:'balance'}}>{t('Where do you want to go?', '어디로 갈까요?')}</h2>
      <div style={{display:'flex',flexDirection:'column',gap:10}}>
        {TOOL_AREAS.filter(a => a.id !== 'beside').map(a => (""",
  """      <h2 style={{fontFamily:"'Playfair Display', Georgia, serif",fontWeight:900,fontSize:32,lineHeight:1.1,margin:'4px 0 12px',color:'var(--navy)',textWrap:'balance'}}>{t('Where do you want to go?', '어디로 갈까요?')}</h2>
      <div data-testid="home-quick" style={{display:'flex',alignItems:'center',gap:6,flexWrap:'wrap',margin:'0 0 14px'}}>
        <span style={{fontSize:11.5,fontWeight:900,color:'var(--muted)',letterSpacing:'0.06em'}}>{t('QUICK', '바로')}</span>
        {[['scale-finder', t('Scale finder', '스케일 찾기')], ['metronome', t('Metronome', '메트로놈')]].map(([id, l]) => <button key={id} type="button" className="chip" data-quick={id} style={{padding:'5px 12px',fontSize:13.5,fontWeight:800}} onClick={() => go({ view: 'tools', tool: id, ret: 'home' })}>{l}</button>)}
      </div>
      <div style={{display:'flex',flexDirection:'column',gap:10}}>
        {TOOL_AREAS.filter(a => a.id !== 'beside').map(a => (""")

# the dial (the tool itself, ScaleFinderDial): one keyboard for both hands, in place of the two rows and the thumb-stop play
R("      {clash ? <>\n        <ScKeys clean ks={K} marks={marks} names={names} arcs={[]} nonce={mode + key + form} mw={520}/>\n        <p style={{ fontSize: 13, color: 'var(--muted)', margin: '8px 0 0', textAlign: 'center', lineHeight: 1.5 }}>{t('No finger numbers for this form: the harmonic fingering would put a thumb on a black key. Look the fingering up in your book.', '이 형태는 손가락 번호를 보여 주지 않아요: 화성 단음계의 손가락 번호로는 엄지가 검은건반에 놓여요. 책에서 찾아보세요.')}</p></>\n        : (() => { const e = mode === 'major' ? info.octaves[oct] : fing, KK = offs.map(o => info.rootPc + o), kn = mode === 'major' ? key : 'm' + key;\n          const paint = (hand) => { const F = e[hand], mk = {}, nm = {}, nc = {}, curK = an >= 0 ? seq[an].k : null; scRuns(kn, hand, F).forEach(g => { for (let q = g.from; q < g.from + g.len; q++) { mk[KK[q]] = g.kind === 3 ? 'seg3' : g.kind === 4 ? 'seg4' : 'pass'; nc[KK[q]] = g.kind === 3 ? '#c0431f' : g.kind === 4 ? '#3b4fa8' : '#26296b'; } }); F.forEach((f, q) => { nm[KK[q]] = String(f); }); if (curK != null) { mk[curK] = 'pick'; nc[curK] = '#fff'; } return { mk, nm, nc }; };\n          const row = (hand, label) => { const P = paint(hand); return <div style={{ marginTop: hand === 'RH' ? 4 : 10 }}>\n            <div style={{ fontSize: 12, fontWeight: 900, color: 'var(--muted)', letterSpacing: '0.05em', marginBottom: 2 }}>{label}</div>\n            <div><div><ScKeys inKey clean ks={KK} marks={P.mk} names={P.nm} ncol={P.nc} arcs={[]} nonce={hand + key + mode + form + oct} mw={oct === 2 ? 640 : 520} oct={oct === 2 ? 3 : 2}/></div></div></div>; };\n          return <div data-sfd-fing>\n            {row('RH', t('RIGHT HAND', '오른손'))}{row('LH', t('LEFT HAND', '왼손'))}\n            <div style={{ display: 'flex', gap: 14, flexWrap: 'wrap', alignItems: 'center', justifyContent: 'center', marginTop: 8, fontSize: 12.5, fontWeight: 800, color: '#26296b' }}>\n              <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5 }}><span style={{ width: 14, height: 14, borderRadius: 3, background: MARK_STYLE.seg3.white, border: '1.5px solid ' + MARK_STYLE.seg3.stroke }}/>{t('1-2-3', '1-2-3')}</span>\n              <span style={{ display: 'inline-flex', alignItems: 'center', gap: 5 }}><span style={{ width: 14, height: 14, borderRadius: 3, background: MARK_STYLE.seg4.white, border: '1.5px solid ' + MARK_STYLE.seg4.stroke }}/>{t('1-2-3-4', '1-2-3-4')}</span>\n            </div>\n            <div data-sfd-thumb style={{ minHeight: 24, textAlign: 'center', fontWeight: 900, fontSize: 14, color: '#c0431f', marginTop: 6 }}>{thumbMsg}</div>\n            {wt && <div style={{ textAlign: 'center', marginTop: 4 }}><button className=\"ghost-btn\" style={scS.prim} data-sfd-next onClick={() => runFrom(an + 1)}>{t('Next →', '다음 →')}</button></div>}\n          </div>; })()}\n", """      <SfHandsKeyboard rootPc={info.rootPc} offsets={offs} fR={clash ? null : eF.RH} fL={clash ? null : eF.LH} names={offs.map(o => names[info.rootPc + (o % 12)] || '')} downOffsets={mode === 'minor' && form === 'melodic' ? minorOffsets('natural', oct) : null}/>
      {clash && <p style={{ fontSize: 13, color: 'var(--muted)', margin: '8px 0 0', textAlign: 'center', lineHeight: 1.5 }}>{t('No finger numbers for this form: the harmonic fingering would put a thumb on a black key. Look the fingering up in your book.', '이 형태는 손가락 번호를 보여 주지 않아요: 화성 단음계의 번호로는 엄지가 검은건반에 와요. 책에서 찾아 보세요.')}</p>}
""")
R("      {scRow(<>\n        <button className=\"ghost-btn\" style={scS.back} data-sfd-play onClick={playA}>{an >= 0 ? t('■ Stop', '■ 멈추기') : t('▶ Up and down: you press Next at each thumb', '▶ 올라갔다 내려오기: 엄지마다 \\'다음\\'을 눌러요')}</button>\n      </>)}\n", "")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
