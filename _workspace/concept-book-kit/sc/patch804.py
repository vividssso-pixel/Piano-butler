"""Build EB (her 13:42: 'the doll's house: 3', 'the grand's legs: c', 'making things is good, but not too many useless
ones: only what is needed and useful and fun, concisely'):
1. The doll's house: the corner stones in a pastel per floor, the floor's own wallpaper colour (look 3); nothing else
   coloured; paper stays plain. The setting behind ?house= goes.
2. The grand piano (PB_INST): the legs 16 longer (the lyre and its pedals down to the floor with them), the lid on a
   shorter stick (0.72 of its opening); the whole drawing scaled to stay in its old box.
3. One toy per idea, the step's own activity first: the toys that repeated their step's activity leave the step (they
   stay in the toolbox): Loud and soft, your way (From pp to f does it), Drive the tempo (Four tempo words), Make a
   rhythm card (the step has its own card), Climb the ladders (The five Cs), My word tune (Spell it on the keys),
   My tune, my chords (Chords for a melody).
4. The Piano's Story: its new play merges into the pads it repeated: the three keyboards are played on a keyboard inside
   'Pluck, push or strike' (near the front strong, near the back gentle, the bass that goes round), the pedal playground
   is 'The pedals' (its quiz stays), the 88-key slide is 'Grand, upright, 88 keys'. Strum the strings stays (new idea)."""
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def R(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, n, old[:120]); s = s.replace(old, new)
def CUT(a, b, new):   # replace from the first a to just before b (b found after a)
    global s
    i = s.index(a); j = s.index(b, i); assert s.count(a) == 1, a[:80]; s = s[:i] + new + s[j:]

# 1. the house: look 3 always on screen
CUT("// Build DV: the corner stones floor by floor (mock-up). read once at load", "const TH_Q_TINT = ",
    "// Build DV / EB (her 13:42 'the doll's house: 3'): the corner stones in a pastel per floor, the floor's wallpaper colour\n")
R("""  const qm = o.print ? null : TH_Q;
  if (!qm) body += stQuoins(X0, qTop, gb, false) + stQuoins(X1, qTop, gb, true);
  else { const segs = spans.filter(sp => sp.y1 > qTop).map(sp => ({ ...sp, y0: Math.max(sp.y0, qTop) })).concat([{ y0: hallTop, y1: gb, wp: 'panel', here: false, k: -1, hall: true }]);
    segs.forEach((sp, i) => { const f = qm === 'alt' ? (i % 2 === 0 ? ST.N : '#fff') : qm === 'tint' ? (sp.hall ? '#fff' : TH_Q_TINT[sp.wp] || '#fff') : (sp.here ? ST.C : '#fff');
      body += stQuoins(X0, sp.y0, sp.y1, false, f) + stQuoins(X1, sp.y0, sp.y1, true, f); }); }""",
  """  if (o.print) body += stQuoins(X0, qTop, gb, false) + stQuoins(X1, qTop, gb, true);   // paper stays plain
  else spans.filter(sp => sp.y1 > qTop).map(sp => ({ ...sp, y0: Math.max(sp.y0, qTop) })).concat([{ y0: hallTop, y1: gb, wp: '', hall: true }]).forEach(sp => {
    const f = sp.hall ? '#fff' : TH_Q_TINT[sp.wp] || '#fff'; body += stQuoins(X0, sp.y0, sp.y1, false, f) + stQuoins(X1, sp.y0, sp.y1, true, f); });""")

# 2. the grand on longer legs, its lid lower, scaled into its old box
R("""  if (lidUp) s += F('M16 70 L128 38 C150 30 186 14 196 8 C204 4 200 -2 190 0 C160 6 130 20 104 30 Z', 'url(#' + id + ')', 1.6) + F('M30 64 L120 38 C140 30 170 16 182 9 C162 14 132 26 108 34 Z', '#fff', 0.8);""",
  """  // Build EB (her 13:42, c): the lid opens 0.72 as far, turning on the spine (16,70)-(128,38)
  if (lidUp) s += '<g transform="matrix(1 -0.08 0 0.72 0 20.88)">' + F('M16 70 L128 38 C150 30 186 14 196 8 C204 4 200 -2 190 0 C160 6 130 20 104 30 Z', 'url(#' + id + ')', 1.6) + F('M30 64 L120 38 C140 30 170 16 182 9 C162 14 132 26 108 34 Z', '#fff', 0.8) + '</g>';""")
R("""  if (lidUp) s += L('M160 58 L150 22', 1.6);""", """  if (lidUp) s += L('M160 58 L150 24.72', 1.6);""")
R("""  s += leg(20, 83, 114, 6) + leg(108, 83, 114, 6) + leg(190, 58, 104, 5);
  s += F('M58 83 H72 V86 H58 Z', '#fff', 1.1) + L('M60 86 C56 92 60 98 61 104 M70 86 C74 92 70 98 69 104 M63 86 V104 M67 86 V104', 1.1) + F('M56 104 H74 V107 H56 Z', N, 1) + L('M60 107 V111 M65 107 V111 M70 107 V111', 1.8);
  return s;""",
  """  s += leg(20, 83, 130, 6.64) + leg(108, 83, 130, 6.64) + leg(190, 58, 118.08, 5.48);   // Build EB: 16 longer (the far leg 14, it stands further back)
  s += F('M58 83 H72 V86 H58 Z', '#fff', 1.1) + L('M60 86 C56 97.3 60 108.7 61 120 M70 86 C74 97.3 70 108.7 69 120 M63 86 V120 M67 86 V120', 1.1) + F('M56 120 H74 V123 H56 Z', N, 1) + L('M60 123 V127 M65 123 V127 M70 123 V127', 1.8);
  return '<g transform="translate(9.1 -5.12) scale(0.9163)">' + s + '</g>';   // the taller piano fits its old 210 x 120 box""")

# 3. one toy per idea: the ones that repeated their step leave it
for x in ["'note-names': { 5: ['mk-word'] }, ", "dynamics: { 1: ['mk-dyn'] }, ", "tempo: { 1: ['mk-tempo'] }, rhythm: { 4: ['make-card'] }, 'ledger-lines': { 4: ['mk-ladders'] },", "'harmony-4': { 3: ['mk-tunechords'] }, "]:
    R(x, '')
R("""// Build DW (call 40): each toy in the step that teaches what it needs.""", """// Build DW (call 40): each toy in the step that teaches what it needs. Build EB (her 13:42 'only what is needed, useful and fun'):
// not where the step's own activity already does the same (mk-word, mk-dyn, mk-tempo, make-card, mk-ladders, mk-tunechords).""")

# 4. the Piano's Story: the play inside the pads it repeated
CUT("function SpsTimeKeys() {", "// ── step 3, inside the piano:", """function Sps9Play({ inst, onLevel }) {   // Build EB: the keyboard and the bass inside 'Pluck, push or strike'
  const [lit, setLit] = useState([]), [bass, setBass] = useState(false);
  const sched = useRef(null), next = useRef(0), k = useRef(0), instRef = useRef(inst); instRef.current = inst;
  const stopBass = () => { clearInterval(sched.current); sched.current = null; setBass(false); };
  const me = useRef(() => stopBass()).current;
  useEffect(() => () => { clearInterval(sched.current); spsRelease(me); }, []);
  function startBass() { const ctx = getAudio(); if (!ctx) return; spsTake(me); clearInterval(sched.current); next.current = ctx.currentTime + 0.12; k.current = 0;
    const SPB = 60 / 72;
    const tick = () => { while (next.current < ctx.currentTime + 0.35) { const m = SPS9_BASS[k.current % 8];
      instNote(instRef.current, ctx, next.current, m, SPB * 0.92, 0.42); k.current++; next.current += SPB; } };
    tick(); sched.current = setInterval(tick, 80); setBass(true); }
  function down(m, v) { const ctx = getAudio(); if (!ctx) return; const i = instRef.current;
    instNote(i, ctx, ctx.currentTime + 0.005, m, i === 'piano' ? 1.4 : 0.9, i === 'piano' ? v * 0.75 : v);
    if (onLevel) onLevel(v); setLit(l => l.concat(m)); }
  const up = (m) => setLit(l => l.filter(x => x !== m));
  return <div data-sps9="keys">
    <div style={{margin:'10px auto 0',maxWidth:460}}><Sps9Keys lo={60} hi={83} lit={lit} onDown={down} onUp={up}/></div>
    {spsRow(<button className={bass ? 'primary-btn' : 'ghost-btn'} style={{...SPS_TAP,width:'auto',padding:'8px 18px'}} data-sps9-bass onClick={() => (bass ? (stopBass(), spsRelease(me)) : startBass())}>{bass ? t('■ Stop the bass', '■ 베이스 멈추기') : t('▶ Start the bass', '▶ 베이스 켜기')}</button>)}
  </div>;
}

""")
R("""t('Pick a keyboard. Press gently, then hard: does it get louder?', '건반 악기를 골라요. 살살, 그다음 세게 눌러 봐요: 소리가 커지나요?')""",
  """t('Pick a keyboard and play. Near the front of a key is a strong touch, near the back a gentle one: does it get louder? Start the bass, and every white key fits over it.', '건반 악기를 골라 쳐 봐요. 건반 앞쪽은 세게, 안쪽은 살살: 소리가 커지나요? 베이스를 켜면 흰건반은 무엇이든 어울려요.')""")
R("""        {spsRow(<><button className="ghost-btn" style={SPS_TAP} onClick={() => press(0.15)}>{t('▶ Gently', '▶ 살살')}</button><button className="ghost-btn" style={SPS_TAP} onClick={() => press(0.95)}>{t('▶ Hard', '▶ 세게')}</button></>)}""",
  """        <Sps9Play inst={inst} onLevel={setLv}/>""")
# the pedals: the playground is the pad's free part
R("""t('Tap a pedal to press it; tap it again to let it up. Then play C E G.', '페달을 한 번 누르면 밟고, 다시 누르면 떼요. 밟은 채로 C E G를 쳐요.')""",
  """t('Tap a pedal to press it down, tap it again to let it up. Play a few notes with the right pedal down, then let it up.', '페달을 한 번 누르면 밟고, 다시 누르면 떼요. 오른쪽 페달을 밟은 채 몇 음 쳐 보고, 페달을 떼 봐요.')""")
CUT("""      {!quiz && <>
        <div style={{maxWidth:420,margin:'0 auto'}}><SpsPedals down={[sus && 'sustain', soft && 'soft'].filter(Boolean)}""", """      {quiz && <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(130px,1fr))',gap:6,maxWidth:420,margin:'6px auto 0'}}>""",
    """      {!quiz && <SpsPedalPlay/>}
""")
R("""  return <div className="try-box" style={sps9Box} data-sps9="pedals">
    <div style={actTitle}>{t('Pedal playground', '페달 놀이터')}</div>
    <div style={actNote}>{t('Tap a pedal to press it down, tap it again to let it up. Play a few notes with the right pedal down, then let it up.', '페달을 한 번 누르면 밟고, 다시 누르면 떼요. 오른쪽 페달을 밟은 채 몇 음 쳐 보고, 페달을 떼 봐요.')}</div>""",
  """  return <div data-sps9="pedals">""")
# 88 keys: the slide is the pad's strip
CUT("""      <div style={actNote}>{t('Hear the two ends and the middle. Then count the Cs from the bottom to the top.'""", """
    </div>
  );
}
function SpsPad""", """      <div style={actNote}>{t('Put a finger on the lowest key and slide all the way to the top: from the lowest A to the highest C. Every C you pass lights up: how many are there?', '가장 낮은 건반에 손가락을 대고 맨 위까지 쭉 미끄러져 봐요: 가장 낮은 A부터 가장 높은 C까지. 지나가는 C마다 불이 켜져요: 모두 몇 개일까요?')}</div>
      <SpsSlide88/>""")
R("""  return <div className="try-box" style={sps9Box} data-sps9="slide">
    <div style={actTitle}>{t('Slide along all 88', '88건반 미끄럼틀')}</div>
    <div style={actNote}>{t('Put a finger on the lowest key and slide all the way to the top. Every C you pass lights up: how many are there?', '가장 낮은 건반에 손가락을 대고 맨 위까지 쭉 미끄러져 봐요. 지나가는 C마다 불이 켜져요: 모두 몇 개일까요?')}</div>""",
  """  return <div data-sps9="slide">""")
R("""const SPS9_AT = { 0: SpsTimeKeys, 2: SpsStringHarp, 3: SpsPedalPlay, 4: SpsSlide88 };""", """const SPS9_AT = { 2: SpsStringHarp };   // Build EB: the other three live inside their steps' pads""")
open(dst, 'w', encoding='utf-8').write(s)
print('ok concise', len(s))
