#!/usr/bin/env python3
# Phase 490: the concept book's key pad, one focus at a time (her 2026-10-19 00:52: 'everything is shown together, I do not know where to look;
# the circle of fifths and the key signature together; the keyboard clock together with the keyboard; a black key has two names: show both').
# Two tabs: the keyboard clock with a piano under it (both names on every black key), and the circle of fifths with the key signature under it.
# Runs on the output of patch489.  python3 patch490.py in.src.html out.src.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d (want %d): %s' % (s.count(a), n, a[:110]))
    s = s.replace(a, b)

# 1. the clock: o.both = both names on every black key, even when the scale spells it one way
rep("          : spelled && nm ? one(lx, ly, prettyNote(nm), ink, b ? 16 : 18)\n          : b ? two(",
    "          : spelled && nm && !(o.both && b) ? one(lx, ly, prettyNote(nm), ink, b ? 16 : 18)\n          : b ? two(")

rep("function TapKeyboard({ octaves, marks = {}, onTap, labels = null, tint = false, pixel = false, names = null, outline = null }) {",
    "function TapKeyboard({ octaves, marks = {}, onTap, labels = null, tint = false, pixel = false, names = null, outline = null, bigLabels = false }) {")
rep('<text key={n} x={k.x + blackW / 2} y={blackH - 22 + j * 12} textAnchor="middle" fontSize="8.5"',
    '<text key={n} x={k.x + blackW / 2} y={bigLabels ? blackH - 28 + j * 14 : blackH - 22 + j * 12} textAnchor="middle" fontSize={bigLabels ? 11 : 8.5}')

# 2. the pad
a = s.index("function CbKeyPad() {")
b = s.index("// pages 6 and 7: other shapes on the same clock, from any key")
NEW = r'''function cbKeyLines(sel) {
  const sg = KEY_SIGS.find(x => x.major === sel) || KEY_SIGS[0], signs = sg.type ? (sg.type === 'sharp' ? SHARP_ORDER : FLAT_ORDER).slice(0, sg.count) : [];
  const main = skgKeyName(sel) + ': ' + (sg.count ? pbCountWords(sel) + (LANG === 'ko' ? '(' : ' (') + signs.map(prettyNote).join('\u00a0') + ')' : t('no sharps or flats', '샤프도 플랫도 없음'));
  const out = [main]; if (CB_TWIN[sel]) out.push(t(CB_TWIN[sel][0], CB_TWIN[sel][1]));
  return out.map(x => cbSx(LANG === 'ko' ? cbNbKo(x) : x));
}
function CbKeyPad() {
  const [sel, setSel] = useState('C');
  const [view, setView] = useState('clock');
  const timers = useRef([]);
  const stop = cbUseOneSound(timers);
  const pickK = (k) => { stop(); setSel(k); };
  const tiny = useCbNarrow(360);
  const sg = KEY_SIGS.find(x => x.major === sel) || KEY_SIGS[0], names = pbSpell(sel), pc = pbKeyPc(sel);
  const marks = {}; PB_MAJOR.forEach(o => { marks[(pc + o) % 12] = 'mate'; }); marks[pc] = 'pick';
  const tabs = [['clock', t('Keyboard clock', '건반 시계')], ['circle', t('Circle of fifths', '5도권')]];
  const wrap = { maxWidth: tiny ? '100%' : 300, margin: '0 auto' };
  return (
    <div className="try-box" style={tiny ? { ...actBox, paddingLeft:4, paddingRight:4 } : actBox} data-cb="key-pad">
      <div style={actTitle}>{t('One key, two ways to look', '조 하나, 두 가지로 보기')}</div>
      <div role="tablist" aria-label={t('Two ways to look at one key', '조 하나를 보는 두 가지 방법')} style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'4px 0 10px'}} onKeyDown={(e) => { if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); const nv = view === 'clock' ? 'circle' : 'clock'; setView(nv); const el = document.getElementById('cbkp-tab-' + nv); if (el) el.focus(); } }}>{tabs.map(([v, l]) => <button key={v} id={'cbkp-tab-' + v} role="tab" aria-selected={view === v} aria-controls="cbkp-panel" tabIndex={view === v ? 0 : -1} className={'chip' + (view === v ? ' active' : '')} style={{minHeight:44,padding:'8px 16px',fontSize:14,outlineOffset:2}} onFocus={(e) => { e.currentTarget.style.outline = '3px solid #e4572e'; }} onBlur={(e) => { e.currentTarget.style.outline = 'none'; }} onClick={() => setView(v)}>{l}</button>)}</div>
      <div role="tabpanel" id="cbkp-panel" aria-labelledby={'cbkp-tab-' + view}>
      {view === 'clock' ? <>
        <div style={{...actNote,textWrap:'pretty'}}>{t('Tap a key on the clock: the major scale’s shape turns to start there. The piano under it lights the same keys.', '시계에서 건반을 눌러 보세요. 장음계 모양이 돌아서 그 음에서 시작하고, 아래 피아노에도 같은 건반이 켜져요.')}</div>
        <div style={wrap}><KeyRing sel={sel} onPick={pickK} o={{ shape: true, both: true, center: (C) => <text x={C} y={C + 7} textAnchor="middle" fontSize="22" fontWeight="900" fill={PEN_N} style={{fontFamily:"'Playfair Display', Georgia, serif"}}>{pbAccT(prettyNote(sel))}</text> }} label={t('The keyboard clock with the ' + prettyNote(sel) + ' major scale drawn as a shape.', '건반 시계: ' + prettyNote(sel) + '장조 음계가 모양으로 그려져 있어요.')}/></div>
        <div style={{maxWidth:tiny ? '100%' : 340,margin:'8px auto 0'}}><TapKeyboard octaves={1} marks={marks} labels="all" bigLabels onTap={(i) => pickK(KEY12[i])}/></div>
        <div style={{textAlign:'center',fontSize:12,fontWeight:800,color:BK.muted,marginTop:10}}>{t('The ' + prettyNote(sel) + ' major scale, note by note', prettyNote(sel) + '장음계의 음 이름')}</div>
        <div style={{display:'flex',flexWrap:'wrap',justifyContent:'center',gap:3,margin:'4px auto 4px',maxWidth:360}}>{[...names, names[0]].map((n, i) => <span key={i} style={{flex:'1 1 0',minWidth:0,maxWidth:tiny ? 38 : 42,textAlign:'center',padding:'4px 0',borderRadius:6,border:'1.5px solid ' + (cbAcc(n) ? PEN_C : BK.line),fontSize:tiny ? 13 : 15,fontWeight:900,color:cbAcc(n) ? PEN_C : BK.ink}}>{cbNoteEl(n)}</span>)}</div>
      </> : <>
        <div style={{...actNote,textWrap:'pretty'}}>{t('Tap a key on the circle: its key signature, the sharps or flats, is written right under it.', '5도권에서 조를 눌러 보세요. 그 조의 조표(샤프나 플랫)가 바로 아래에 나와요.')}</div>
        <div style={wrap}><FifthsRing sel={sel} onPick={pickK} o={{ filled: [], twins: true }} label={t('The circle of fifths, ' + skgKeyName(sel) + ' ringed.', '5도권: ' + skgKeyName(sel) + '에 동그라미.')}/></div>
        <div style={{maxWidth:300,margin:'4px auto 0'}}><KSStaff count={sg.count} type={sg.type}/></div>
        <div style={{textAlign:'center',fontSize:14,fontWeight:800,color:BK.ink,margin:'2px 0 8px',textWrap:'balance'}}>{cbKeyLines(sel).map((ln, i) => <div key={i} style={i ? {fontSize:13,fontWeight:700,marginTop:2} : null}>{ln}</div>)}</div>
      </>}
      </div>
      <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',marginTop:6}}>
        <button className="ghost-btn" style={{minHeight:44}} onClick={() => { stop(); stop.claim(); timers.current = pbPlayMidi(pbScaleMidi(sel), 110); }}>{t('▶ Listen', '▶ 듣기')}</button>
        <a className="ghost-btn" style={{minHeight:44,display:'inline-flex',alignItems:'center',textDecoration:'none'}} href={cbHref('tool=scale-finder&key=' + encodeURIComponent(sel))}>{t('Fingering →', '손가락 번호 →')}</a>
      </div>
    </div>
  );
}
'''
s = s[:a] + NEW + s[b:]

open(dst, 'w', encoding='utf-8').write(s)
print('patched 490', len(s))
