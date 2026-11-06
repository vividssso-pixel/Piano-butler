#!/usr/bin/env python3
# Phase 463 (her 2026-10-14 00:07 '이것도 다른 단어로 바꿔줘 walk running 아님 ta titi ta titi'): chapter 3's
# beat-or-rhythm words. bird / tur-tle / light-house become walk (one sound) and run-ning (two sounds), the words of
# chapter 5. Korean says 타 / 티-티: a spoken word must have as many syllables as sounds, and 걷기 / 달리기 have two and
# three, so chapter 5's Korean labels change to 타 / 티-티 too (the pictures still walk and run).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)

# the book, page 5: footprints instead of the bird and the turtle; the words; the tasks
rep("""  // p5: beat or rhythm: four beats (hearts) under four words; one dot for each sound on top: bird (one), tur-tle (two)""",
    """  // p5: beat or rhythm: four beats (hearts) under four words; one dot for each sound on top: walk (one), run-ning (two)""")
rep("""      if (n === 1) s.push(...plBird(cx - 4, 40, 2.1)); else s.push(...fsTurtle(cx - 3, 46, 1.55));
      s.push({ ...penText(cx, 92, n === 1 ? t('bird', '새') : t('tur-tle', '거-북'), { size: 15, weight: 900, fill: PEN_N, anchor: 'middle' }) });""",
    """      if (n === 1) s.push(...plFoot(cx, 46, 2.6, PEN_N)); else s.push(...plFoot(cx - 13, 40, 2.1, PEN_C, true), ...plFoot(cx + 13, 52, 2.1, PEN_C));   // Phase 463: a step, two quick steps
      s.push({ ...penText(cx, 92, n === 1 ? t('walk', '타') : t('run-ning', '티-티'), { size: 15, weight: 900, fill: PEN_N, anchor: 'middle' }) });""")
rep("""t('Four beats, four coral hearts in a row. Over them four words: bird, tur-tle, bird, tur-tle, with the bird and the turtle drawn above them. One coral dot for each sound: one over bird, two over tur-tle', '박 넷, 산호색 심장 네 개가 한 줄로. 그 위에 낱말 넷: 새, 거-북, 새, 거-북, 그 위에 새와 거북 그림. 소리마다 산호색 점 하나: 새 위에 하나, 거-북 위에 둘')""",
    """t('Four beats, four coral hearts in a row. Over them four words: walk, run-ning, walk, run-ning, with one footprint over walk and two quick coral footprints over run-ning. One coral dot for each sound: one over walk, two over run-ning', '박 넷, 산호색 심장 네 개가 한 줄로. 그 위에 낱말 넷: 타, 티-티, 타, 티-티, 타 위에 발자국 하나, 티-티 위에 빠른 산호색 발자국 둘. 소리마다 산호색 점 하나: 타 위에 하나, 티-티 위에 둘')""")
rep("""박 하나에 <b>새</b>라고 하면 소리 하나, <b>거-북</b>이면 소리 둘. 박은 그대로, 리듬은 바뀌어요.""",
    """박 하나에 <b>타</b>라고 하면 소리 하나, <b>티-티</b>면 소리 둘. 박은 그대로, 리듬은 바뀌어요.""")
rep("""Say <b>bird</b> on one beat: one sound. Say <b>tur-tle</b>: two sounds. The beat stays the same; the rhythm changes.""",
    """Say <b>walk</b> on one beat: one sound. Say <b>run-ning</b>: two sounds. The beat stays the same; the rhythm changes.""")
rep("""        <>발로 박을 치며 말해요: 새, 거-북, 새, 거-북. 박마다 낱말 하나. 그다음 발로 박을 지키며 낱말 소리마다 손뼉을 쳐요.</>,
        <>이번엔: 거-북, 거-북, 새, 새. 그리고: 등-대, 새, 등-대, 새.</>,""",
    """        <>발로 박을 치며 말해요: 타, 티-티, 타, 티-티. 박마다 하나. 그다음 발로 박을 지키며 소리마다 손뼉을 쳐요.</>,
        <>이번엔: 티-티, 티-티, 타, 타. 그리고: 타, 타, 티-티, 타.</>,""")
rep("""        <>Tap the beat with your foot and say: bird, tur-tle, bird, tur-tle, one word on each beat. Then clap the words while your foot keeps the beat.</>,
        <>Now: tur-tle, tur-tle, bird, bird. And: light-house, bird, light-house, bird.</>,""",
    """        <>Tap the beat with your foot and say: walk, run-ning, walk, run-ning, one word on each beat. Then clap the words while your foot keeps the beat.</>,
        <>Now: run-ning, run-ning, walk, walk. And: walk, walk, run-ning, walk.</>,""")

# the beat-or-rhythm tool and the drill: the same two words (the keys stay: bird = one sound, turtle = two)
rep("""const PL_WORDS = { bird: [t => t('bird', '새'), 1], turtle: [t => t('tur-tle', '거-북'), 2], lighthouse: [t => t('light-house', '등-대'), 2] };
const PL_WORD_SETS = [['bird', 'turtle', 'bird', 'turtle'], ['turtle', 'turtle', 'bird', 'bird'], ['lighthouse', 'bird', 'lighthouse', 'bird']];""",
    """const PL_WORDS = { bird: [t => t('walk', '타'), 1], turtle: [t => t('run-ning', '티-티'), 2] };   // Phase 463: walk and run-ning (Korean 타, 티-티); the keys stay
const PL_WORD_SETS = [['bird', 'turtle', 'bird', 'turtle'], ['turtle', 'turtle', 'bird', 'bird'], ['bird', 'bird', 'turtle', 'bird']];""")
rep("""    do { row = Array.from({ length: 4 }, () => pick(['bird', 'turtle', 'lighthouse'])); } while ((row.every(w => w === 'bird') || row.filter(w => w === 'lighthouse').length > 1 || (prev && prev.key === row.join())) && g++ < 20);""",
    """    do { row = Array.from({ length: 4 }, () => pick(['bird', 'turtle'])); } while ((row.every(w => w === 'bird') || (prev && prev.key === row.join())) && g++ < 20);""")

# the Workbook and the Teacher copy (English)
rep("""const PL_WN = { bird: ['bird', 1], turtle: ['tur-tle', 2], lighthouse: ['light-house', 2], sea: ['sea', 1], sky: ['sky', 1] };""",
    """const PL_WN = { bird: ['walk', 1], turtle: ['run-ning', 2], sea: ['sea', 1], sky: ['sky', 1] };   // Phase 463: walk and run-ning""")
rep("""  dots: [['turtle', 'bird', 'bird', 'turtle'], ['bird', 'lighthouse', 'bird', 'bird'], ['turtle', 'turtle', 'lighthouse', 'bird'], ['lighthouse', 'turtle', 'bird', 'turtle']],
  count: [['bird', 'bird', 'bird', 'turtle'], ['turtle', 'turtle', 'turtle', 'turtle'], ['lighthouse', 'bird', 'turtle', 'bird'], ['bird', 'bird', 'bird', 'bird']],""",
    """  dots: [['turtle', 'bird', 'bird', 'turtle'], ['bird', 'turtle', 'bird', 'bird'], ['turtle', 'turtle', 'turtle', 'bird'], ['bird', 'turtle', 'turtle', 'turtle']],
  count: [['bird', 'bird', 'bird', 'turtle'], ['turtle', 'turtle', 'turtle', 'turtle'], ['turtle', 'bird', 'bird', 'turtle'], ['bird', 'bird', 'bird', 'bird']],""")
rep("""  wordsFromDots: [[1, 2, 2, 1], [2, 1, 2, 2], [1, 1, 1, 2]],   // one dot: bird; two dots: tur-tle""",
    """  wordsFromDots: [[1, 2, 2, 1], [2, 1, 2, 2], [1, 1, 1, 2]],   // one dot: walk; two dots: run-ning""")
rep("""  sounds: [['turtle', 'bird', 'bird', 'bird'], ['lighthouse', 'bird', 'bird', 'turtle'], ['bird', 'turtle', 'bird', 'bird'], ['turtle', 'bird', 'turtle', 'turtle']],""",
    """  sounds: [['turtle', 'bird', 'bird', 'bird'], ['bird', 'bird', 'turtle', 'turtle'], ['bird', 'turtle', 'bird', 'bird'], ['turtle', 'bird', 'turtle', 'turtle']],""")
rep("""how="One dot: write bird. Two dots: write tur-tle. Then say each row, tapping the beat with your foot.\"""",
    """how="One dot: write walk. Two dots: write run-ning. Then say each row, tapping the beat with your foot.\"""")
rep("""W.wordsFromDots.map(r => r.map(d => d === 1 ? 'bird' : 'tur-tle').join(' '))""", """W.wordsFromDots.map(r => r.map(d => d === 1 ? 'walk' : 'run-ning').join(' '))""")
rep("""Number 8: bird bird bird bird has 4 beats and 4 sounds""", """Number 8: walk walk walk walk has 4 beats and 4 sounds""")
rep("""row.includes('lighthouse') ? 14 : 15.5""", """15.5""")

# chapter 5's Korean word labels: 타 and 티-티 (one syllable a sound)
rep("""      s.push(txt(H(i), 124, t('walk', '걷기'), { size: 13, weight: 900, fill: PEN_N, anchor: 'middle' }));""",
    """      s.push(txt(H(i), 124, t('walk', '타'), { size: 13, weight: 900, fill: PEN_N, anchor: 'middle' }));""")
rep("""      s.push(txt(H(i), 122, pr ? t('run-ning', '달리기') : t('walk', '걷기'), { size: 13, weight: 900, fill: PEN_N, anchor: 'middle' }));""",
    """      s.push(txt(H(i), 122, pr ? t('run-ning', '티-티') : t('walk', '타'), { size: 13, weight: 900, fill: PEN_N, anchor: 'middle' }));""")
rep("""const nvWord = (k) => k === 'p' ? t('run-ning', '달리기') : t('walk', '걷기');""", """const nvWord = (k) => k === 'p' ? t('run-ning', '티-티') : t('walk', '타');""")
rep("""t('walk, run-ning, walk, run-ning', '걷기, 달리기, 걷기, 달리기')""", """t('walk, run-ning, walk, run-ning', '타, 티-티, 타, 티-티')""")
rep("""t('run-ning, run-ning, walk, walk', '달리기, 달리기, 걷기, 걷기')""", """t('run-ning, run-ning, walk, walk', '티-티, 티-티, 타, 타')""")
rep("silent beats as dashed circles, bird and tur-tle, finger numbers", "silent beats as dashed circles, walk and run-ning (Phase 463), finger numbers")

# Her 00:12 '탭할 때 소리가 길게 끌리지 않아 들을 때는 끌리는데': a tapped note now sounds for as long as the pad is held
# (pointer down to up, or the space bar down to up), up to a semibreve, like a key; blip and pianoNote return a release.
rep("""function blip(ctx, t, freq, len, vol, type) {
  if (type === 'triangle' && SOUND.piano) { pianoNote(ctx, t, freq, len, vol); return; }""", """function blip(ctx, t, freq, len, vol, type) {   // returns release(): stop the note early (Phase 463, a held tap)
  if (type === 'triangle' && SOUND.piano) return pianoNote(ctx, t, freq, len, vol);""")
rep("""  o.connect(g); g.connect(ctx.destination);
  o.start(t); o.stop(t + len + 0.03);
  _clickNodes.push(o);
}
""", """  o.connect(g); g.connect(ctx.destination);
  o.start(t); o.stop(t + len + 0.03);
  _clickNodes.push(o);
  return () => { const now = ctx.currentTime; try { g.gain.cancelScheduledValues(now); g.gain.setValueAtTime(Math.max(0.0002, g.gain.value), now); g.gain.exponentialRampToValueAtTime(0.0001, now + 0.08); o.stop(now + 0.1); } catch (e) {} };
}
""")
rep("""  const end = t + Math.max(len, 0.08);
  out.gain.setValueAtTime(0.9 * vel, t);""", """  const end = t + Math.max(len, 0.08), stops = [];
  const release = () => { const now = ctx.currentTime; if (now >= end) return; try { out.gain.cancelScheduledValues(now); out.gain.setValueAtTime(0.9 * vel, now); out.gain.exponentialRampToValueAtTime(0.0008, now + 0.16); stops.forEach(n => n.stop(now + 0.2)); } catch (e) {} };
  out.gain.setValueAtTime(0.9 * vel, t);""")
rep("""    src.connect(filt); src.start(t, _piano.on[near] || 0); src.stop(end + 0.3);
    _clickNodes.push(src);
    return;
  }""", """    src.connect(filt); src.start(t, _piano.on[near] || 0); src.stop(end + 0.3);
    _clickNodes.push(src); stops.push(src);
    return release;
  }""")
rep("""    o.connect(g); g.connect(filt); o.start(t); o.stop(end + 0.3); _clickNodes.push(o);
  });
}""", """    o.connect(g); g.connect(filt); o.start(t); o.stop(end + 0.3); _clickNodes.push(o); stops.push(o);
  });
  return release;
}""")
rep("""function PlPad({ on, onTap, label, h = 74 }) {
  useEffect(() => {
    if (!on) return;
    const k = (e) => { if (e.code === 'Space' || e.key === ' ') { e.preventDefault(); onTap(); } };
    window.addEventListener('keydown', k); return () => window.removeEventListener('keydown', k);
  }, [on, onTap]);
  return <button data-pl-pad onPointerDown={(e) => { e.preventDefault(); if (on) onTap(); }} disabled={!on}""", """function PlPad({ on, onTap, onRelease, label, h = 74 }) {   // onRelease (Phase 463): the pad let go, so a note can sound as long as it is held
  useEffect(() => {
    if (!on) return;
    const k = (e) => { if ((e.code === 'Space' || e.key === ' ') && !e.repeat) { e.preventDefault(); onTap(); } };
    const u = (e) => { if ((e.code === 'Space' || e.key === ' ') && onRelease) onRelease(); };
    window.addEventListener('keydown', k); window.addEventListener('keyup', u); return () => { window.removeEventListener('keydown', k); window.removeEventListener('keyup', u); };
  }, [on, onTap, onRelease]);
  const up = () => { if (onRelease) onRelease(); };
  return <button data-pl-pad onPointerDown={(e) => { e.preventDefault(); if (on) onTap(); }} onPointerUp={up} onPointerLeave={up} onPointerCancel={up} disabled={!on}""")
# chapter 5's two tap places: the note sounds while the pad is held, up to four beats
rep("""    taps.current.push(r.now());
    const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime, 261.63, 0.16, 0.16, 'triangle');
  }, [phase, mode]);""", """    taps.current.push(r.now());
    const ctx = getAudio(); if (ctx) { if (held.current) held.current(); held.current = blip(ctx, ctx.currentTime, 261.63, 4.3 * r.spb, 0.18, 'triangle'); }
  }, [phase, mode]);
  const release = React.useCallback(() => { if (held.current) { held.current(); held.current = null; } }, []);""")
rep("""  const run = useRef(null), taps = useRef([]);
  const row = rows[ri][1], snd = nvSounds(row), n = nvBeats(row);""", """  const run = useRef(null), taps = useRef([]), held = useRef(null);
  const row = rows[ri][1], snd = nvSounds(row), n = nvBeats(row);""")
rep("""      {mode === 'tap' && <PlPad on={live} onTap={tap} label={t('TAP EACH NOTE', '음마다 쳐요')}/>}""",
    """      {mode === 'tap' && <PlPad on={live} onTap={tap} onRelease={release} label={t('HOLD EACH NOTE', '음마다 누르고 있어요')}/>}""")
rep("""    const onTap = () => { const r = run.current; if (r && (phase === 'count' || phase === 'go')) { taps.current.push(r.now()); const ctx = getAudio(); if (ctx) blip(ctx, ctx.currentTime, 261.63, 0.16, 0.16, 'triangle'); } };""",
    """    const onTap = () => { const r = run.current; if (r && (phase === 'count' || phase === 'go')) { taps.current.push(r.now()); const ctx = getAudio(); if (ctx) { if (held.current) held.current(); held.current = blip(ctx, ctx.currentTime, 261.63, 4.3 * r.spb, 0.18, 'triangle'); } } };
    const onRelease = () => { if (held.current) { held.current(); held.current = null; } };""")
rep("""      {!done && <PlPad on={phase === 'count' || phase === 'go'} onTap={onTap} h={64}/>}""", """      {!done && <PlPad on={phase === 'count' || phase === 'go'} onTap={onTap} onRelease={onRelease} h={64}/>}""")
rep("""  const [grow, setGrow] = useState({});
  const run = useRef(null), taps = useRef([]);
  const done = !!given;""", """  const [grow, setGrow] = useState({});
  const run = useRef(null), taps = useRef([]), held = useRef(null);
  const done = !!given;""")
rep("""Then <b>tap it</b>: 4 clicks to get ready, then tap once for each note""", """Then <b>tap it</b>: 4 clicks to get ready, then press once for each note and hold it as long as the note""")
rep("""그다음 <b>쳐 봐요</b>: 클릭 4번을 듣고, 음마다 한 번씩 쳐요""", """그다음 <b>쳐 봐요</b>: 클릭 4번을 듣고, 음마다 한 번 눌러 음의 길이만큼 누르고 있어요""")

# Her 00:14 '킹 모양이 짤렸어 십자가 모양처럼 있지 않아?': the clef intros cut the top of the King's cross; the pieces move
# down so the whole cross shows, and the cross gets a thinner bar and a clear top (a cross, not a T).
rep("""<PenArt shapes={clef === 'treble' ? sfQueen(26, 28, 1.2) : sfKing(26, 28, 1.2)}""", """<PenArt shapes={clef === 'treble' ? sfQueen(26, 31, 1.2) : sfKing(26, 31, 1.2)}""")
rep("L1.4 -84.4 L1.4 -88.6 L5.4 -88 L5.4 -92.6 L1.4 -92 L1.8 -97 L-1.8 -97 L-1.4 -92 L-5.4 -92.6 L-5.4 -88 L-1.4 -88.6 L-1.4 -84.4",
    "L1.4 -84.4 L1.4 -89.6 L5.8 -89.6 L5.8 -92.4 L1.4 -92.4 L1.4 -97 L-1.4 -97 L-1.4 -92.4 L-5.8 -92.4 L-5.8 -89.6 L-1.4 -89.6 L-1.4 -84.4")

# Her 00:15 'space도 보여줘야지, 그리고 내려오는것도' (chapter 6, page 3): skips on the spaces too, and skips coming down;
# the bird's cloud no longer cut off at the top. The tasks name their keys (Book rule 3).
rep('  const p3 = <SfStaff clef="none" width={340} pad={[46, 44]} label={t(\'Notes on the staff: steps climb line, space, line, space to the top and walk back down; skips go line, line, line; the bird is up at the high end, the turtle down at the low end, and an arrow under the staff points both ways\', \'오선 위의 음표: 한 걸음은 줄, 칸, 줄, 칸 꼭대기까지 올라갔다가 다시 내려와요; 건너뛰기는 줄, 줄, 줄; 높은 쪽엔 새, 낮은 쪽엔 거북이, 오선 아래 화살표는 양쪽을 가리켜요\')}\n    notes={[30, 31, 32, 33, 34, 33, 32].map((d, i) => ({ d, x: 56 + i * 21 })).concat([30, 32, 34, 36].map((d, i) => ({ d, x: 216 + i * 27, color: PEN_C })))}\n    icons={[SF_ICON(bird, 300, 6, 0.85), SF_ICON(turtle, 0, 116, 0.75)]}\n    extra={(yOf, layer, txt) => layer === \'over\' && <g style={txt}>\n      <text x="119" y={yOf(38) - 14} fontSize="10" fontWeight="900" fill={BK.ink} textAnchor="middle">{t(\'steps: up... and down\', \'한 걸음: 위로... 그리고 아래로\')}</text>\n      <text x="257" y={yOf(38) - 14} fontSize="10" fontWeight="900" fill={BK.coral} textAnchor="middle">{t(\'skips: line, line, line\', \'건너뛰기: 줄, 줄, 줄\')}</text>\n      {[0, 1, 2].map(i => <g key={i}>{sfHop(216 + i * 27 + 3, 216 + (i + 1) * 27 - 3, yOf(32 + 2 * i) - 9, 11)}</g>)}\n      <path d={`M64 ${yOf(30) + 24} L292 ${yOf(30) + 24}`} stroke={BK.coral} strokeWidth="1.8"/>{sfArrowHead(296, yOf(30) + 24, 1, BK.coral)}{sfArrowHead(60, yOf(30) + 24, -1, BK.coral)}\n      <text x="178" y={yOf(30) + 37} fontSize="9" fontWeight="800" fill={BK.ink} textAnchor="middle">{t(\'up = higher, to the right · down = lower, to the left\', \'위로 = 높게, 오른쪽으로 · 아래로 = 낮게, 왼쪽으로\')}</text>\n    </g>}/>;\n', '  const p3 = <div style={{display:\'flex\',flexDirection:\'column\',gap:6,width:\'100%\'}}>\n    <SfStaff clef="none" width={300} pad={[56, 52]} label={t(\'Steps on the staff: line, space, line, space up to the top and back down; the bird is up at the high end, the turtle down at the low end, and an arrow under the staff points both ways\', \'오선 위의 한 걸음: 줄, 칸, 줄, 칸 꼭대기까지 올라갔다가 다시 내려와요; 높은 쪽엔 새, 낮은 쪽엔 거북이, 오선 아래 화살표는 양쪽을 가리켜요\')}\n      notes={[30, 31, 32, 33, 34, 33, 32, 31, 30].map((d, i) => ({ d, x: 48 + i * 24 }))}\n      icons={[SF_ICON(bird, 256, 6, 0.85), SF_ICON(turtle, 0, 124, 0.75)]}\n      extra={(yOf, layer, txt) => layer === \'over\' && <g style={txt}>\n        <text x="144" y={yOf(38) - 16} fontSize="10.5" fontWeight="900" fill={BK.ink} textAnchor="middle">{t(\'steps: up and down\', \'한 걸음: 위로, 아래로\')}</text>\n        <path d={`M48 ${yOf(30) + 24} L242 ${yOf(30) + 24}`} stroke={BK.coral} strokeWidth="1.8"/>{sfArrowHead(246, yOf(30) + 24, 1, BK.coral)}{sfArrowHead(44, yOf(30) + 24, -1, BK.coral)}\n        <text x="146" y={yOf(30) + 38} fontSize="9.5" fontWeight="800" fill={BK.ink} textAnchor="middle">{t(\'up = higher, to the right · down = lower, to the left\', \'위로 = 높게, 오른쪽으로 · 아래로 = 낮게, 왼쪽으로\')}</text>\n      </g>}/>\n    <SfStaff clef="none" width={300} pad={[36, 14]} label={t(\'Skips on the staff: line to line up and back down, then space to space up and back down, a coral arrow over each skip\', \'오선 위의 건너뛰기: 줄에서 줄로 올라갔다 내려오고, 칸에서 칸으로 올라갔다 내려와요, 건너뛸 때마다 산호색 화살표\')}\n      notes={[30, 32, 34, 32, 30].map((d, i) => ({ d, x: 34 + i * 24, color: PEN_C })).concat([31, 33, 35, 33, 31].map((d, i) => ({ d, x: 170 + i * 24, color: PEN_C })))}\n      extra={(yOf, layer, txt) => { if (layer !== \'over\') return null;\n        const hop = (x1, d1, x2, d2, k) => { const y1 = yOf(d1) - 9, y2 = yOf(d2) - 9, top = Math.min(y1, y2) - 10;\n          return <g key={k}><path d={`M${x1 + 3} ${y1} Q${(x1 + x2) / 2} ${top} ${x2 - 3} ${y2}`} fill="none" stroke={BK.coral} strokeWidth="1.6"/><path d={`M${x2 - 8.5} ${y2 - 4.5} L${x2 - 3} ${y2} L${x2 - 9.5} ${y2 + 1.5}`} fill="none" stroke={BK.coral} strokeWidth="1.6" strokeLinecap="round"/></g>; };\n        const L = [30, 32, 34, 32, 30], S = [31, 33, 35, 33, 31];\n        return <g style={txt}>\n          <text x="82" y={yOf(38) - 16} fontSize="10.5" fontWeight="900" fill={BK.coral} textAnchor="middle">{t(\'skips: line to line\', \'건너뛰기: 줄에서 줄\')}</text>\n          <text x="218" y={yOf(38) - 16} fontSize="10.5" fontWeight="900" fill={BK.coral} textAnchor="middle">{t(\'skips: space to space\', \'건너뛰기: 칸에서 칸\')}</text>\n          {L.slice(1).map((d, i) => hop(34 + i * 24, L[i], 34 + (i + 1) * 24, d, \'l\' + i))}\n          {S.slice(1).map((d, i) => hop(170 + i * 24, S[i], 170 + (i + 1) * 24, d, \'s\' + i))}\n        </g>; }}/>\n  </div>;\n')
rep("        <>아무 흰건반에서 시작해 그림처럼 <b>한 걸음</b>으로 꼭대기까지 올라갔다가 <b>다시 내려와요</b>, 매번 이웃 건반으로.</>,\n        <>이번엔 <b>건너뛰기</b>: 줄, 줄, 줄 위로, 건반 하나씩 넘어가요. 그리고 건너뛰기로 다시 내려와요.</>,\n      ] : [\n        <>Start on any white key and play the picture's <b>steps</b>: up to the top and <b>back down</b>, the next key each time.</>,\n        <>Now the <b>skips</b>: line, line, line going up, a key jumped over each time. Then skip your way back down.</>,\n      ]}/>", '        <>오른손 엄지를 가운데 도에: 그림처럼 <b>한 걸음</b>씩 C D E F G 올라갔다가 F E D C로 <b>다시 내려와요</b>.</>,\n        <>이번엔 <b>건너뛰기</b>, 매번 건반 하나를 넘어가요: C E G E C, 그다음 D F A F D. 올라갔다 내려와요.</>,\n      ] : [\n        <>Right hand, thumb on middle C: play the <b>steps</b> as in the picture, up C D E F G and <b>back down</b> F E D C.</>,\n        <>Now the <b>skips</b>, a key jumped over each time: C E G E C, then D F A F D. Up and back down.</>,\n      ]}/>')
rep("{t('Line to space: a step. Line to line: a skip. Up or down.', '줄에서 칸: 한 걸음. 줄에서 줄: 건너뛰기. 위로도, 아래로도.')}", "{t('Line to space: a step. Line to line, space to space: a skip.', '줄에서 칸: 한 걸음. 줄에서 줄, 칸에서 칸: 건너뛰기.')}")
open(dst, 'w', encoding='utf-8').write(s); print('ok')
