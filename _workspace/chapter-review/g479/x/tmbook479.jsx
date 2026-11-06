// ─── Phase 479: chapter 23, Musical Terms, built in full (Book rules 14 and 15; her 2026-10-17 macro-first plan, and
// her 09:42 order: terms, then form, then melody). The fifth room of Level 4. Page 1 is the expression ladder: every word
// for how to play on one map (speed slow to fast, volume soft to loud, the changes, touch and character, the little
// words); the steps zoom in; the screen lesson ends with the map again, the words the student can say and play ticked.
// Placement (AMEB Music Craft 2022: Preliminary Adagio Andante Moderato Allegro, pp p mf f, legato staccato; Grade 1
// Lento Allegretto Vivace Presto, accel. rall. rit. riten. a tempo, mp ff cresc. decresc., sf rf; Grade 2 Largo Vivo
// Prestissimo Largamente Larghetto Con moto Maestoso, Allargando Più mosso Meno mosso, sostenuto sempre poco molto senza
// cantabile leggiero espressivo mezzo staccato). Chapters 10 (dynamics) and 13 (tempo) met the Preliminary words.
// The old chapter's TERMS (AMEB meanings), playTerm and speakTerm are reused; its tools stay in the toolbox.

// fam: speed | change | vol | touch | little. w: as printed; name: TERMS' name (its sound); met: the chapter that met it
const TMX = [
  // speed, slow to fast (bpm: its place on the ladder)
  { w: 'Largo', fam: 'speed', bpm: 46, en: 'broadly, very slow', ko: '아주 느리고 폭넓게', rd: '라르고', g: 2 },
  { w: 'Lento', fam: 'speed', bpm: 56, en: 'slowly', ko: '아주 느리게', rd: '렌토', g: 1 },
  { w: 'Adagio', fam: 'speed', bpm: 70, en: 'slow', ko: '느리게', rd: '아다지오', met: 'tempo', g: 0 },
  { w: 'Andante', fam: 'speed', bpm: 90, en: 'at a walking pace', ko: '걷는 빠르기로', rd: '안단테', met: 'tempo', g: 0 },
  { w: 'Moderato', fam: 'speed', bpm: 110, en: 'at a medium speed', ko: '보통 빠르기로', rd: '모데라토', met: 'tempo', g: 0 },
  { w: 'Allegretto', fam: 'speed', bpm: 120, en: 'moderately fast', ko: '조금 빠르게', rd: '알레그레토', g: 1 },
  { w: 'Allegro', fam: 'speed', bpm: 140, en: 'fast and lively', ko: '빠르고 경쾌하게', rd: '알레그로', met: 'tempo', g: 0 },
  { w: 'Vivace', fam: 'speed', bpm: 160, en: 'lively, spirited', ko: '생기 있고 활발하게', rd: '비바체', g: 1 },
  { w: 'Presto', fam: 'speed', bpm: 184, en: 'very fast', ko: '매우 빠르게', rd: '프레스토', g: 1 },
  { w: 'Prestissimo', fam: 'speed', bpm: 208, en: 'as fast as possible', ko: '할 수 있는 한 빠르게', rd: '프레스티시모', g: 2 },
  // changing speed
  { w: 'accel.', name: 'Accelerando', fam: 'change', en: 'gradually faster', ko: '점점 빠르게', rd: '아첼레란도', g: 1 },
  { w: 'rall.', name: 'Rallentando', fam: 'change', en: 'gradually slower', ko: '점점 느리게', rd: '랄렌탄도', g: 1 },
  { w: 'rit.', name: 'Ritardando', fam: 'change', en: 'gradually slower', ko: '점점 느리게', rd: '리타르단도', g: 1 },
  { w: 'riten.', name: 'Ritenuto', fam: 'change', en: 'slower at once, held back', ko: '곧바로 느리게', rd: '리테누토', g: 1 },
  { w: 'a tempo', name: 'A tempo', fam: 'change', en: 'back to the speed before', ko: '원래 빠르기로', rd: '아 템포', g: 1, hear: { from: 120, to: 72, back: true }, cat: 'Changing speed' },   // the first speed, held back, the first speed again
  // loud and soft
  { w: 'pp', name: 'Pianissimo', fam: 'vol', en: 'very soft', ko: '매우 여리게', rd: '피아니시모', met: 'dynamics', g: 0 },
  { w: 'p', name: 'Piano', fam: 'vol', en: 'soft', ko: '여리게', rd: '피아노', met: 'dynamics', g: 0 },
  { w: 'mp', name: 'Mezzo piano', fam: 'vol', en: 'medium soft', ko: '조금 여리게', rd: '메조 피아노', g: 1 },
  { w: 'mf', name: 'Mezzo forte', fam: 'vol', en: 'medium loud', ko: '조금 세게', rd: '메조 포르테', met: 'dynamics', g: 0 },
  { w: 'f', name: 'Forte', fam: 'vol', en: 'loud', ko: '세게', rd: '포르테', met: 'dynamics', g: 0 },
  { w: 'ff', name: 'Fortissimo', fam: 'vol', en: 'very loud', ko: '매우 세게', rd: '포르티시모', g: 1 },
  { w: 'cresc.', name: 'Crescendo', fam: 'vol', en: 'getting louder', ko: '점점 세게', rd: '크레셴도', met: 'dynamics', g: 1 },
  { w: 'decresc.', name: 'Decrescendo', fam: 'vol', en: 'getting softer', ko: '점점 여리게', rd: '데크레셴도', met: 'dynamics', g: 1 },
  { w: 'sf', name: 'Sforzando', fam: 'vol', en: 'a strong accent on one note', ko: '그 음만 특히 세게', rd: '스포르찬도', g: 1 },
  // touch and character
  { w: 'legato', name: 'Legato', fam: 'touch', en: 'smoothly, connected', ko: '부드럽게 이어서', rd: '레가토', met: 'dynamics', g: 0 },
  { w: 'staccato', name: 'Staccato', fam: 'touch', en: 'short, detached', ko: '짧게 끊어서', rd: '스타카토', met: 'dynamics', g: 0 },
  { w: 'mezzo staccato', name: 'Mezzo staccato', fam: 'touch', en: 'moderately short', ko: '조금 짧게 끊어서', rd: '메조 스타카토', g: 2 },
  { w: 'sostenuto', name: 'Sostenuto', fam: 'touch', en: 'sustained', ko: '음을 충분히 끌어서', rd: '소스테누토', g: 2 },
  { w: 'cantabile', name: 'Cantabile', fam: 'touch', en: 'in a singing style', ko: '노래하듯이', rd: '칸타빌레', g: 2 },
  { w: 'leggiero', name: 'Leggiero', fam: 'touch', en: 'lightly', ko: '가볍게', rd: '레지에로', g: 2 },
  { w: 'maestoso', name: 'Maestoso', fam: 'touch', en: 'majestically', ko: '장엄하게', rd: '마에스토소', g: 2 },
  { w: 'espressivo', fam: 'touch', en: 'with expression', ko: '표정 있게', rd: '에스프레시보', g: 2, hear: { bpm: 80, len: 1.02, vol: 0.2 }, cat: 'Other' },
  // the little words
  { w: 'molto', fam: 'little', en: 'very, much', ko: '매우, 많이', rd: '몰토', g: 2 },
  { w: 'poco', fam: 'little', en: 'a little', ko: '조금', rd: '포코', g: 2 },
  { w: 'sempre', fam: 'little', en: 'always', ko: '항상, 계속', rd: '셈프레', g: 2 },
  { w: 'senza', fam: 'little', en: 'without', ko: '~ 없이', rd: '센차', g: 2 },
  { w: 'più', fam: 'little', en: 'more', ko: '더', rd: '피우', g: 2 },
  { w: 'meno', fam: 'little', en: 'less', ko: '덜', rd: '메노', g: 2 },
  { w: 'con', fam: 'little', en: 'with', ko: '~와 함께', rd: '콘', g: 2 },
];
// a little word with a big one (page 6)
const TMX_COMBO = [
  { w: 'poco rit.', a: 'poco', b: 'rit.', en: 'slowing down a little', ko: '조금 점점 느리게', rd: '포코 리타르단도', hear: { from: 120, to: 88 }, cat: 'Changing speed' },
  { w: 'molto cresc.', a: 'molto', b: 'cresc.', en: 'getting much louder', ko: '매우 점점 세게', rd: '몰토 크레셴도', hear: { vFrom: 0.04, vTo: 0.6 }, cat: 'Volume' },
  { w: 'sempre staccato', a: 'sempre', b: 'staccato', en: 'short all the way', ko: '계속 짧게 끊어서', rd: '셈프레 스타카토', hear: { len: 0.2 }, cat: 'Other' },
  { w: 'più mosso', a: 'più', b: 'mosso', name: 'Più mosso', en: 'quicker (more movement)', ko: '더 빠르게', rd: '피우 모소' },
  { w: 'meno mosso', a: 'meno', b: 'mosso', name: 'Meno mosso', en: 'slower (less movement)', ko: '더 느리게', rd: '메노 모소' },
  { w: 'con moto', a: 'con', b: 'moto', name: 'Con moto', en: 'with movement', ko: '움직임 있게', rd: '콘 모토' },
  { w: 'senza rit.', a: 'senza', b: 'rit.', en: 'without slowing down', ko: '느려지지 않게', rd: '센차 리타르단도', hear: { bpm: 120 }, cat: 'Speed' },
  { w: 'poco a poco cresc.', a: 'poco a poco', b: 'cresc.', en: 'getting louder little by little', ko: '조금씩 점점 세게', rd: '포코 아 포코 크레셴도', hear: { vFrom: 0.05, vTo: 0.42, bpm: 90 }, cat: 'Volume' },
];
const TMX_FAM = { speed: ['Speed', '빠르기'], change: ['Changing speed', '빠르기 변화'], vol: ['Loud and soft', '셈여림'], touch: ['Touch and character', '터치와 느낌'], little: ['Little words', '꾸며 주는 말'] };
const tmxFam = (f) => t(TMX_FAM[f][0], TMX_FAM[f][1]);
const tmxOf = (w) => TMX.find(x => x.w === w) || TMX_COMBO.find(x => x.w === w);
const tmxMean = (e) => t(e.en, e.ko);
// its sound: the old chapter's TERMS entry (AMEB), else its own
// (a speed word: clicks at its own number on the ladder, chapter 13's for the four met there)
const tmxSound = (e) => { if (!e) return null; if (e.fam === 'speed') return { term: e.w, hear: { bpm: e.bpm }, cat: 'Speed' }; if (e.hear) return { term: e.w, hear: e.hear, cat: e.cat || 'Other' };
  const x = TERMS.find(tm => tm.term === (e.name || e.w)); return x && x.hear ? x : null; };
const tmxPlay = (e) => { const s = tmxSound(e); if (s) { chxStop(); playTerm(s); } };
// the word as music prints it: speed words upright bold; signs bold italic; the rest italic
const TMX_SERIF = "'Playfair Display', Georgia, serif";
const tmxStyle = (e, size) => e && e.fam === 'speed' ? { fontFamily: TMX_SERIF, fontWeight: 900, fontStyle: 'normal', fontSize: size }
  : e && e.fam === 'vol' && /^[pmfs]+$/.test(e.w) ? { fontFamily: SDY_FONT, fontWeight: 900, fontStyle: 'italic', fontSize: size * 1.2 }
  : { fontFamily: SDY_FONT, fontWeight: 700, fontStyle: 'italic', fontSize: size };
const tmxWord = (w, size = 17, col) => { const e = tmxOf(w); return <span style={{...tmxStyle(e || { fam: 'touch' }, size), color:col || PEN_N, lineHeight:1.1, whiteSpace:'nowrap'}}>{w}</span>; };
const tmxSvgStyle = (e, size) => { const s = tmxStyle(e, size); return { fontFamily: s.fontFamily, fontStyle: s.fontStyle, fontWeight: s.fontWeight, fontSize: s.fontSize }; };
// Korean: words that belong together never part at a line end
const tmxNbKo = (x) => typeof x !== 'string' ? x : chxNbKo(x).replace(/~ 없이/g, '~ 없이')
  .replace(/(아|메조|피우|메노|콘|포코|셈프레|몰토|센차) (템포|스타카토|피아노|포르테|모소|모토|아 포코|리타르단도|크레셴도)/g, '$1 $2').replace(/포코 아 포코/g, '포코 아 포코')
  .replace(/맨 (위|아래)/g, '맨 $1').replace(/할 수 있는 한/g, '할 수 있는 한').replace(/꾸며 주는 말/g, '꾸며 주는 말');
const tmxKoT = (x) => LANG === 'ko' ? tmxNbKo(x) : x;
[['Espressivo', 'es-pres-SEE-voh'], ['Più', 'PYOO'], ['Meno', 'MEH-noh'], ['Con', 'kohn']].forEach(([k, v]) => { if (!PRON[k]) PRON[k] = v; });
// running text with the signs set as signs: chapter 10's sdyRich, and sf as well
const tmxRich = (str) => { if (typeof str !== 'string') return str; const out = []; let last = 0, m; const re = /(^|[^A-Za-z.])(sf)(?![A-Za-z])/g;
  while ((m = re.exec(str))) { const at = m.index + m[1].length; out.push(...sdyRich(str.slice(last, at)), <React.Fragment key={'sf' + at}>{sdyDm('sf', '1.1em')}</React.Fragment>); last = at + 2; }
  out.push(...sdyRich(str.slice(last))); return out; };

// the speed ladder: the speed words from slow to fast, one rung each (the numbers are only about); nums: '♩ = n' by each
const TMX_SPEED = TMX.filter(e => e.fam === 'speed');
function TmxSpeedSvg({ sel, onTap, nums, words = TMX_SPEED, label }) {
  const W = 640, H = nums ? 132 : 100, ax = nums ? 64 : 54, X = (i) => 70 + i * 56;
  return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>
    <line x1={20} x2={W - 14} y1={ax} y2={ax} stroke={PEN_N} strokeWidth="2"/>
    <polygon points={`${W - 6},${ax} ${W - 16},${ax - 5} ${W - 16},${ax + 5}`} fill={PEN_N}/>
    <text x={20} y={ax + 18} fontSize="11.5" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{t('slow', '느리게')}</text>
    <text x={W - 18} y={ax - 8} textAnchor="end" fontSize="11.5" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{t('fast', '빠르게')}</text>
    {words.map((e, i) => { const x = X(i), up = i % 2 === 0, last = i === words.length - 1, y = up ? ax - 18 : ax + 30, on = sel === e.w, col = on ? PEN_C : PEN_N;
      return <g key={e.w} onClick={onTap ? () => onTap(e) : undefined} style={{cursor:onTap ? 'pointer' : 'default'}} data-tmx={e.w}>
        {onTap && <rect x={x - 46} y={up ? 0 : ax + 2} width={92} height={up ? ax - 2 : H - ax - 2} fill="transparent"/>}
        <line x1={x} x2={x} y1={ax - 5} y2={ax + 5} stroke={col} strokeWidth="2"/>
        <text x={last ? x + 36 : x} y={y} textAnchor={last ? 'end' : 'middle'} fill={col} style={tmxSvgStyle(e, 15.5)}>{e.w}</text>
        {nums && <StmMark x={last ? x + 6 : x} y={up ? ax - 38 : ax + 50} n={e.bpm} size={10.5} c={BK.muted} anchor="middle"/>}
      </g>; })}
  </svg>;
}
// the volume ladder: a wedge from soft to loud, the six signs under it
const TMX_VOL6 = ['pp', 'p', 'mp', 'mf', 'f', 'ff'];
function TmxVolSvg({ sel, onTap, label, hair }) {
  const W = 640, H = hair ? 150 : 84, xs = TMX_VOL6.map((_, i) => 70 + i * 100);
  return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={label} style={{width:'100%',display:'block',touchAction:'manipulation',userSelect:'none'}}>
    <polygon points={`40,26 600,10 600,42`} fill="rgba(38,41,107,0.10)" stroke={PEN_N} strokeWidth="1.6" strokeLinejoin="round"/>
    {TMX_VOL6.map((w, i) => { const e = tmxOf(w), on = sel === w;
      return <g key={w} onClick={onTap ? () => onTap(e) : undefined} style={{cursor:onTap ? 'pointer' : 'default'}} data-tmx={w}>
        {onTap && <rect x={xs[i] - 40} y={0} width={80} height={84} fill="transparent"/>}
        <line x1={xs[i]} x2={xs[i]} y1={26 + (i - 2.5) * 0} y2={50} stroke={on ? PEN_C : BK.muted} strokeWidth="1.2" strokeDasharray="2 3"/>
        <text x={xs[i]} y={76} textAnchor="middle" fill={on ? PEN_C : PEN_N} style={tmxSvgStyle(e, 22)}>{w}</text>
      </g>; })}
    {hair && <g>
      {[['cresc.', 70, 260, 1], ['decresc.', 380, 570, -1]].map(([w, x0, x1, dir]) => { const on = sel === w, c = on ? PEN_C : PEN_N, a = dir > 0 ? x0 : x1, b = dir > 0 ? x1 : x0;
        return <g key={w} onClick={onTap ? () => onTap(tmxOf(w)) : undefined} style={{cursor:onTap ? 'pointer' : 'default'}} data-tmx={w}>
          {onTap && <rect x={x0 - 10} y={96} width={x1 - x0 + 20} height={54} fill="transparent"/>}
          <path d={`M${b} 104 L${a} 114 L${b} 124`} fill="none" stroke={c} strokeWidth="2" strokeLinejoin="round"/>
          <text x={(x0 + x1) / 2} y={144} textAnchor="middle" fill={c} style={tmxSvgStyle(tmxOf(w), 15)}>{w}</text></g>; })}
      <g onClick={onTap ? () => onTap(tmxOf('sf')) : undefined} style={{cursor:onTap ? 'pointer' : 'default'}} data-tmx="sf">
        {onTap && <rect x={286} y={96} width={68} height={54} fill="transparent"/>}
        <text x={320} y={124} textAnchor="middle" fill={sel === 'sf' ? PEN_C : PEN_N} style={tmxSvgStyle(tmxOf('sf'), 17)}>sf</text></g>
    </g>}
  </svg>;
}
function TmxVolBig({ label }) {
  const xs = TMX_VOL6.map((_, i) => 70 + i * 100), hw = (w, x0, x1, dir) => { const a = dir > 0 ? x0 : x1, b = dir > 0 ? x1 : x0;
    return <g key={w}><path d={`M${b} 196 L${a} 212 L${b} 228`} fill="none" stroke={PEN_N} strokeWidth="2.2" strokeLinejoin="round"/><text x={(x0 + x1) / 2} y={258} textAnchor="middle" fill={PEN_N} style={tmxSvgStyle(tmxOf(w), 19)}>{w}</text></g>; };
  const head = (x, big, col) => <ellipse key={x} cx={x} cy={318} rx={big ? 12 : 8.5} ry={big ? 8.6 : 6.2} transform={`rotate(-22 ${x} 318)`} fill={col}/>;
  return <svg viewBox="0 0 640 380" role="img" aria-label={label} style={{width:'100%',display:'block'}}>
    <polygon points="40,62 600,18 600,106" fill="rgba(38,41,107,0.10)" stroke={PEN_N} strokeWidth="1.8" strokeLinejoin="round"/>
    <text x={40} y={40} fontSize="13" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{t('soft', '여리게')}</text>
    <text x={608} y={68} textAnchor="start" fontSize="13" fontWeight="800" fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}}>{t('loud', '세게')}</text>
    {TMX_VOL6.map((w, i) => <g key={w}><line x1={xs[i]} x2={xs[i]} y1={62} y2={128} stroke={BK.muted} strokeWidth="1.2" strokeDasharray="2 3"/>
      <text x={xs[i]} y={166} textAnchor="middle" fill={PEN_N} style={tmxSvgStyle(tmxOf(w), 27)}>{w}</text></g>)}
    {hw('cresc.', 60, 280, 1)}{hw('decresc.', 360, 580, -1)}
    {[200, 260, 320, 380].map(x => head(x, false, PEN_N))}{head(450, true, PEN_C)}{[520, 580].map(x => head(x, false, PEN_N))}
    <text x={450} y={362} textAnchor="middle" fill={PEN_C} style={tmxSvgStyle(tmxOf('sf'), 22)}>sf</text>
  </svg>;
}
// the speed ladder standing up (page 2): Largo on the bottom rung, Prestissimo on the top; ♩ = about
function TmxLadderSvg({ label }) {
  const n = TMX_SPEED.length, y = (i) => 350 - i * 36;
  return <svg viewBox="0 0 520 372" role="img" aria-label={label} style={{width:'100%',display:'block'}}>
    {[214, 300].map(x => <line key={x} x1={x} x2={x} y1={8} y2={366} stroke={PEN_N} strokeWidth="2.4" strokeLinecap="round"/>)}
    {TMX_SPEED.map((e, i) => <g key={e.w}><line x1={214} x2={300} y1={y(i)} y2={y(i)} stroke={PEN_N} strokeWidth="2"/>
      <text x={200} y={y(i) + 6} textAnchor="end" fill={PEN_N} style={tmxSvgStyle(e, 19)}>{e.w}</text>
      <StmMark x={314} y={y(i) + 6} n={e.bpm} size={13} c={BK.muted}/></g>)}
    <g fill={BK.muted} style={{fontFamily:'Inter, sans-serif'}} fontSize="12.5" fontWeight="800">
      <text x={440} y={y(n - 1) + 6}>{t('fast', '빠르게')}</text><text x={440} y={y(0) + 6}>{t('slow', '느리게')}</text></g>
    <line x1={452} x2={452} y1={y(1)} y2={y(n - 2) + 4} stroke={BK.muted} strokeWidth="1.6"/><polygon points={`452,${y(n - 2) - 6} 447,${y(n - 2) + 4} 457,${y(n - 2) + 4}`} fill={BK.muted}/>
  </svg>;
}
// a row of beats: gaps (the space between each) say the speed: accel. closer, rit. further apart
function TmxBeatsSvg({ gaps, w, sel, onTap, word = true, label, x0, w0 = 0, text }) {
  const span = gaps.reduce((a, g) => a + g, 0), W = Math.max(150, span + 24, w0), s0 = x0 != null ? x0 : (W - span) / 2, r = Math.min(5.5, Math.min(...gaps) * 0.36);
  const xs = [s0]; gaps.forEach(g => xs.push(xs[xs.length - 1] + g)); const e = tmxOf(w), on = sel === w, c = on ? PEN_C : PEN_N;
  return <svg viewBox={`0 0 ${W} ${word ? 56 : 30}`} role="img" aria-label={label} onClick={onTap ? () => onTap(e) : undefined} style={{width:'100%',display:'block',cursor:onTap ? 'pointer' : 'default'}} data-tmx={w}>
    {xs.map((x, i) => <circle key={i} cx={x} cy={15} r={r} fill={c}/>)}
    {word && <text x={W / 2} y={48} textAnchor="middle" fill={c} style={tmxSvgStyle(e, 15)}>{text || w}</text>}
  </svg>;
}
// a tempo: the first speed, held back, then the first speed again (after riten., the speed before comes back)
const TMX_GAPS = { 'accel.': [36, 29, 24, 20, 17, 15], 'rit.': [15, 17, 20, 24, 29, 36], 'riten.': [16, 16, 16, 34, 34, 34], 'a tempo': [16, 16, 34, 34, 16, 16] };
TMX_GAPS['rall.'] = TMX_GAPS['rit.'];
const tmxChip = (w, on, onTap, key, tick, size = 16, fill) => { const e = tmxOf(w), st = {border:'1.5px solid ' + (on ? PEN_C : 'rgba(38,41,107,0.28)'),background:'#fff',borderRadius:999,padding:fill ? '2px 0' : onTap ? '2px 10px' : '1px 10px',minHeight:onTap ? 44 : 26,minWidth:onTap && !fill ? 44 : 0,width:fill ? '100%' : undefined,position:'relative',justifyContent:'center',cursor:onTap ? 'pointer' : 'default',color:on ? PEN_C : PEN_N,display:'inline-flex',alignItems:'center',gap:5,boxSizing:'border-box'};
  if (!onTap) return <span key={key || w} data-tmx={w} style={st}>{tmxWord(w, size)}</span>;   // print: a word, not a button
  return <button key={key || w} type="button" onClick={() => onTap(e)} data-tmx={w} aria-pressed={!!on} style={st}>{tick && <span aria-label={t('known', '알아요')} style={fill ? {position:'absolute',top:1,right:3,color:PEN_G,fontWeight:900,fontSize:11} : {color:PEN_G,fontWeight:900,fontSize:14}}>✓</span>}{tmxWord(w, 15, on ? PEN_C : PEN_N)}</button>; };

// the expression ladder: page 1 (print). On screen (the pad) every family is a row of words in its order.
function TmxMap({ sel, onTap, label }) {
  const lab = (f) => <div style={{fontSize:11.5,fontWeight:900,letterSpacing:'0.08em',textTransform:'uppercase',color:BK.muted,paddingTop:4,lineHeight:1.2}}>{tmxFam(f)}</div>;
  const row = (f, node) => <div key={f} style={{display:'grid',gridTemplateColumns:'96px minmax(0,1fr)',gap:10,alignItems:'center'}}>{lab(f)}<div style={{minWidth:0}}>{node}</div></div>;
  const chips = (fam) => <div style={{display:'flex',flexWrap:'wrap',gap:5}}>{TMX.filter(e => e.fam === fam).map(e => tmxChip(e.w, sel === e.w, onTap, null, false, 14.5))}</div>;
  return <div role="img" aria-label={label} style={{display:'flex',flexDirection:'column',gap:6,width:'100%'}}>
    {row('speed', <TmxSpeedSvg sel={sel} onTap={onTap}/>)}
    {row('change', <div style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:14}}>{['accel.', 'rit.', 'riten.', 'a tempo'].map((w, i) => <div key={w} style={{maxWidth:150,borderLeft:i ? '1px solid rgba(38,41,107,0.15)' : 0,paddingLeft:i ? 6 : 0}}><TmxBeatsSvg gaps={TMX_GAPS[w]} w0={174} w={w} sel={sel} onTap={onTap} text={w === 'rit.' ? 'rit. · rall.' : null}/></div>)}</div>)}
    {row('vol', <TmxVolSvg sel={sel} onTap={onTap} hair/>)}
    {row('touch', chips('touch'))}
    {row('little', chips('little'))}
  </div>;
}
// page 5's bars (and the Workbook's): four crotchets with their marks: legato a slur, staccato dots, mezzo staccato both
const TMX_T3B = { legato: [{ slurs: [[0, 3]] }, [28, 29, 30, 31]], staccato: [{ stacc: [0, 1, 2, 3] }, [28, 29, 30, 31]], 'mezzo staccato': [{ slurs: [[0, 3]], stacc: [0, 1, 2, 3] }, [28, 29, 30, 31]] };
const tmxBar = (notes) => [['ts', 4], ...notes.map(d => ['q', 1, d]), ['||']];

function tmxLbPages(scr = false) {
  const ch = 'terms';
  const live = (still, comp) => <LbLive still={still} live={comp}/>;
  const stack = (nodes, h, gap = 12, mw = 680) => <LbPic h={h}><div style={{display:'flex',flexDirection:'column',gap,width:'100%',maxWidth:mw,margin:'0 auto',alignItems:'stretch'}}>{nodes}</div></LbPic>;
  const X = (en, ko) => tmxRich(LANG === 'ko' ? sscNbKo(skgKo(tmxNbKo(ko))) : sscNbEn(en));
  const cap = (x, key = 'cap') => <div key={key} style={{textAlign:'center',fontSize:scr ? 14 : 13.5,fontWeight:800,color:BK.ink,margin:'2px auto 0',maxWidth:560,lineHeight:1.35,textWrap:'balance'}}>{typeof x === 'string' ? tmxRich(tmxKoT(x)) : x}</div>;
  // a term as a dictionary headword: the word as printed (and in Korean its reading)
  const hw1 = (w) => { const e = tmxOf(w); return <span style={{whiteSpace:'nowrap'}}>{tmxWord(w, 19)}{LANG === 'ko' && e && e.rd ? <span style={{fontSize:13,fontWeight:700,color:BK.muted,marginLeft:5}}>{tmxNbKo(e.rd)}</span> : null}</span>; };
  const hw = (w) => <span>{hw1(w)}{'\u200b'}</span>;
  const hw2 = (a, b) => <span>{hw1(a)}<span style={{color:BK.muted}}>{' · '}</span>{hw1(b)}{'\u200b'}</span>;

  // p1 (macro first): the expression ladder
  const p1 = <LbLive still={stack([<TmxMap key="m" label={t('The expression ladder. Speed: Largo, Lento, Adagio, Andante, Moderato, Allegretto, Allegro, Vivace, Presto, Prestissimo, from slow to fast. Changing speed: accel., rit. (or rall.), riten., a tempo, each a row of beats. Loud and soft: pp, p, mp, mf, f, ff under a widening wedge, then cresc., sf and decresc. Touch and character: legato, staccato, mezzo staccato, sostenuto, cantabile, leggiero, maestoso, espressivo. Little words: molto, poco, sempre, senza, più, meno, con.', '표현의 사다리. 빠르기: 라르고, 렌토, 아다지오, 안단테, 모데라토, 알레그레토, 알레그로, 비바체, 프레스토, 프레스티시모, 느린 것부터 빠른 것까지. 빠르기 변화: 아첼레란도, 리타르단도(랄렌탄도), 리테누토, 아 템포, 박의 간격으로. 셈여림: 점점 넓어지는 쐐기 아래 pp, p, mp, mf, f, ff, 그리고 크레셴도, sf, 데크레셴도. 터치와 느낌: 레가토, 스타카토, 메조 스타카토, 소스테누토, 칸타빌레, 레지에로, 마에스토소, 에스프레시보. 꾸며 주는 말: 몰토, 포코, 셈프레, 센차, 피우, 메노, 콘.')}/>,
    ], 380, 6)} live={<TmxMapPad/>}/>;
  // p2: the speed ladder standing up, a metronome number by each rung
  const p2 = stack([<div key="s" style={{width:'100%',maxWidth:470,margin:'0 auto'}}><TmxLadderSvg label={t('A ladder of ten rungs, slow at the bottom, fast at the top: Largo (about 46 crotchets a minute), Lento 56, Adagio 70, Andante 90, Moderato 110, Allegretto 120, Allegro 140, Vivace 160, Presto 184, Prestissimo 208.', '열 칸짜리 사다리, 아래는 느리고 위는 빨라요: 라르고(1분에 4분음표 약 46), 렌토 56, 아다지오 70, 안단테 90, 모데라토 110, 알레그레토 120, 알레그로 140, 비바체 160, 프레스토 184, 프레스티시모 208.')}/></div>,
    cap(<><svg viewBox="0 0 16 22" width="12" height="16" aria-hidden="true" style={{verticalAlign:'-3px',marginRight:3}}><StmMark x={1} y={20} size={13} c={BK.ink}/></svg>{tmxKoT(t('= about how many crotchet beats a minute (chapter ' + bkChapterNo('tempo') + '). Pieces differ a little.', '= 뒤의 숫자는 1분에 4분음표를 약 몇 박 치는지 나타내요(' + bkChapterNo('tempo') + '챕터). 곡마다 조금씩 달라요.'))}</>)], 380, 8, 560);
  // p3: changing speed: a row of beats for each word
  const p3 = stack(['accel.', 'rall.', 'rit.', 'riten.', 'a tempo'].map(w => <div key={w} style={{display:'grid',gridTemplateColumns:'120px minmax(0,1fr)',alignItems:'center',gap:14}}>
      <div style={{textAlign:'right'}}>{tmxWord(w, 22)}</div><div style={{maxWidth:440}}><TmxBeatsSvg gaps={TMX_GAPS[w].map(g => g * 2.2)} x0={12} w0={174 * 2.2} w={w} word={false} label={t(w + ': ' + tmxOf(w).en + '.', tmxOf(w).rd + ': ' + tmxOf(w).ko + '.')}/></div></div>)
    .concat([cap(t('The dots are beats: the closer they are, the faster.', '점은 박이에요. 가까울수록 빨라요.'), 'c3')]), 360, 40, 600);
  // p4: the volume ladder and the hairpins
  const p4 = stack([<TmxVolBig key="v" label={t('A wedge widening from soft to loud, with pp, p, mp, mf, f and ff under it; a hairpin that opens, cresc., and one that closes, decresc.; then a row of notes with one bigger coral note marked sf.', '여린 것부터 센 것까지 넓어지는 쐐기, 그 아래 pp, p, mp, mf, f, ff. 벌어지는 헤어핀 크레셴도, 좁아지는 헤어핀 데크레셴도. 그리고 음표들 가운데 크고 붉은 음표 하나에 sf.')}/>,
    cap(t('One rung louder each time: pp p mp mf f ff.', '한 칸씩 더 세게: pp p mp mf f ff.'), 'c4')], 360, 10, 640);
  // p5: one bar for each touch, its word beside it; then the character words
  const p5 = stack(Object.keys(TMX_T3B).map(w => <div key={w} style={{display:'grid',gridTemplateColumns:'150px minmax(0,1fr)',alignItems:'center',gap:12}}>
      <div style={{textAlign:'right'}}>{tmxWord(w, 19)}</div><div style={{maxWidth:330}}><SdyStaff full items={tmxBar(TMX_T3B[w][1])} k={TMX_T3B[w][0]} o={{ D: 40 }} label={t(w + ': C D E F, ' + (w === 'legato' ? 'in one slur.' : w === 'staccato' ? 'each with a dot.' : 'each with a dot, all in one slur.'), tmxOf(w).rd + ': C D E F, ' + (w === 'legato' ? '이음줄 하나로.' : w === 'staccato' ? '음마다 점.' : '음마다 점, 모두 이음줄 하나로.'))}/></div></div>)
    .concat([<div key="c" style={{display:'flex',flexWrap:'wrap',gap:8,justifyContent:'center',marginTop:10}}>{['sostenuto', 'cantabile', 'leggiero', 'maestoso', 'espressivo'].map(w => tmxChip(w, false, null, null, false, 17))}</div>]), 380, 10, 560);
  // p6: a little word and a big one: every term the drill asks
  const tile = (x, on) => <span style={{display:'inline-flex',alignItems:'center',border:'1.5px solid rgba(38,41,107,0.3)',borderRadius:8,padding:'3px 10px',background:'#fff'}}>{tmxWord(x, 21, on ? PEN_C : PEN_N)}</span>;
  const p6 = stack(TMX_COMBO.map(c => <div key={c.w} style={{display:'grid',gridTemplateColumns:'158px 18px 124px 22px minmax(0,1fr)',alignItems:'center',gap:8}}>
      <span style={{textAlign:'right'}}>{tile(c.a, true)}</span><span style={{fontWeight:900,color:BK.muted,textAlign:'center'}}>+</span><span>{tile(c.b)}</span>
      <span style={{fontWeight:900,color:BK.muted,textAlign:'center'}}>=</span><span style={{fontSize:17,fontWeight:800,color:BK.ink,wordBreak:'keep-all',lineHeight:1.3}}>{tmxKoT(tmxMean(c))}</span></div>), 400, 20, 640);

  // the check icons
  const tx = (x, c, col, s = 18, y = 28, it) => '<text x="' + x + '" y="' + y + '" text-anchor="middle" style="font-family:' + (it ? 'Georgia, serif' : 'Inter, sans-serif') + ';font-style:' + (it ? 'italic' : 'normal') + '" font-size="' + s + '" font-weight="900" fill="' + col + '">' + c + '</text>';
  const ic = {
    speed: [{ k: 'raw', svg: '<line x1="6" x2="80" y1="20" y2="20" stroke="' + PEN_N + '" stroke-width="2"/><polygon points="90,20 80,15 80,25" fill="' + PEN_N + '"/>' + [16, 40, 64].map((x, i) => '<line x1="' + x + '" x2="' + x + '" y1="14" y2="26" stroke="' + (i === 2 ? PEN_C : PEN_N) + '" stroke-width="2.2"/>').join('') }],
    change: [{ k: 'raw', svg: [8, 32, 51, 66, 78, 88].map((x, i) => '<circle cx="' + x + '" cy="20" r="3.4" fill="' + (i > 3 ? PEN_C : PEN_N) + '"/>').join('') }],
    vol: [{ k: 'raw', svg: tx(16, 'pp', PEN_N, 15, 28, 1) + tx(46, 'mp', PEN_N, 15, 28, 1) + tx(76, 'ff', PEN_C, 15, 28, 1) }],
    touch: [{ k: 'raw', svg: '<path d="M8 14 Q30 2 52 14" fill="none" stroke="' + PEN_N + '" stroke-width="1.8"/>' + [14, 30, 46].map(x => '<ellipse cx="' + x + '" cy="26" rx="4.4" ry="3.1" fill="' + PEN_N + '"/>').join('') + [64, 78].map(x => '<ellipse cx="' + x + '" cy="26" rx="4.4" ry="3.1" fill="' + PEN_C + '"/><circle cx="' + x + '" cy="17" r="1.8" fill="' + PEN_C + '"/>').join('') }],
    little: [{ k: 'raw', svg: tx(26, 'poco', PEN_C, 14, 26, 1) + tx(54, '+', PEN_N, 13, 26) + tx(74, 'rit.', PEN_N, 14, 26, 1) }],
  };
  const checksRows = [
    ['speed', t('I can put the speed words in order, Largo to Prestissimo, and say what each means', '빠르기말을 라르고부터 프레스티시모까지 차례로 놓고 뜻을 말할 수 있어요')],
    ['change', t('I can play accel., rit., riten. and a tempo', '아첼레란도, 리타르단도, 리테누토, 아 템포를 칠 수 있어요')],
    ['vol', t('I can play pp, p, mp, mf, f and ff, a crescendo and an sf', 'pp, p, mp, mf, f, ff와 크레셴도, sf를 칠 수 있어요')],
    ['touch', t('I can play legato, staccato and mezzo staccato, and say five character words', '레가토, 스타카토, 메조 스타카토를 치고 느낌을 나타내는 말 다섯 개를 말할 수 있어요')],
    ['little', t('I can read a term with a little word: poco rit., molto cresc., sempre staccato', '꾸며 주는 말이 붙은 용어를 읽을 수 있어요: 포코 리타르단도, 몰토 크레셴도, 셈프레 스타카토')],
  ].map(([a, x]) => [a, LANG === 'ko' ? skgKo(sscNbKo(tmxNbKo(x))) : sscNbEn(x)]);
  const ch10 = bkChapterNo('dynamics'), ch13 = bkChapterNo('tempo');

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <>어떻게 칠지 알려 주는 말이 <b>음악{'\u00a0'}용어</b>예요. 대부분 이탈리아어이고, 빠르기, 셈여림, 터치와 느낌을 나타내요.</> : <>A <b>musical term</b> is a word, mostly Italian, that says how to play: how fast, how loud, and with what touch and character.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('The speed ladder', '빠르기 사다리'), 2], [t('Changing speed', '빠르기 변화'), 3], [t('Loud and soft', '셈여림'), 4], [t('Touch and character', '터치와 느낌'), 5], [t('Little words', '꾸며 주는 말'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}<span>{n}</span></span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)',textWrap:'pretty'}}>{bkGoal(15)}<span>{tmxRich(x.replace(/^I can /, ''))}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('The speed ladder', '빠르기 사다리')}>
      {live(p2, <TmxSpeedPad/>)}
      <LbDefs items={[
        [t('speed words', '빠르기말'), X('Written above the staff at the start of a piece (chapter ' + ch13 + '). From slow to fast: Largo, Lento, Adagio, Andante, Moderato, Allegretto, Allegro, Vivace, Presto, Prestissimo.', '곡의 맨 앞, 오선 위에 써요(' + ch13 + '챕터). 느린 것부터: 라르고, 렌토, 아다지오, 안단테, 모데라토, 알레그레토, 알레그로, 비바체, 프레스토, 프레스티시모.')],
        [hw2('Largo', 'Lento'), X('Very slow and broad; slowly. Both slower than Adagio.', '라르고는 아주 느리고 폭넓게, 렌토는 아주 느리게. 둘 다 아다지오보다 느려요.')],
        [hw('Allegretto'), X('Moderately fast: a little slower than Allegro.', '조금 빠르게. 알레그로보다 조금 느려요.')],
        [hw2('Vivace', 'Presto'), X('Lively, spirited; very fast. Both faster than Allegro.', '비바체는 생기 있고 활발하게, 프레스토는 매우 빠르게. 둘 다 알레그로보다 빨라요.')],
        [hw('Prestissimo'), X('As fast as possible. ‑issimo means “very”, as in pianissimo.', '할 수 있는 한 빠르게. ‑issimo는 ‘매우’라는 뜻으로, 피아니시모에도 있어요.')],
      ]}/>
      <LbPiano steps={[
        X('Play C D E F G at Lento, Andante, Allegretto and Presto: four rungs of the ladder.', 'C D E F G를 렌토, 안단테, 알레그레토, 프레스토로 쳐요: 사다리 네 칸.'),
        X('Your teacher plays a scale at one speed. Say its word.', '선생님이 음계를 쳐요. 어떤 빠르기인지 빠르기말로 말해요.'),
      ]}/>
      <LbRemember>{X('Largo at the bottom, Prestissimo at the top.', '맨 아래는 라르고, 맨 위는 프레스티시모.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('Changing speed', '빠르기 변화')}>
      {live(p3, <TmxChangePad/>)}
      <LbDefs items={[
        [hw('accel.'), X('Accelerando: gradually faster.', '점점 빠르게.')],
        [hw2('rall.', 'rit.'), X('Rallentando, ritardando: gradually slower. Two names, one meaning.', '점점 느리게. 이름은 둘, 뜻은 하나예요.')],
        [hw('riten.'), X('Ritenuto: slower at once, held back.', '곧바로 느리게.')],
        [hw('a tempo'), X('Back to the speed before.', '원래 빠르기로 돌아가요.')],
      ]}/>
      <LbPiano steps={[
        X('Play C D E F G A B C getting faster (accel.), then down again getting slower (rit.).', 'C D E F G A B C를 점점 빠르게(아첼레란도), 내려올 때는 점점 느리게(리타르단도) 쳐요.'),
        X('Play twelve Cs: four at a steady speed, four held back (riten.), then four at the first speed again (a tempo).', 'C를 열두 번 쳐요: 네 번은 일정한 빠르기로, 네 번은 곧바로 느리게(리테누토), 네 번은 처음 빠르기로(아 템포).'),
      ]}/>
      <LbRemember>{X('accel. faster, rit. slower, a tempo back.', '아첼레란도는 점점 빠르게, 리타르단도는 점점 느리게, 아 템포는 원래 빠르기로.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Loud and soft', '셈여림')}>
      {live(p4, <TmxVolPad/>)}
      <LbDefs items={[
        [t('the volume ladder', '셈여림 사다리'), X('pp p mp mf f ff: very soft to very loud (chapter ' + ch10 + ').', 'pp p mp mf f ff: 매우 여리게부터 매우 세게까지(' + ch10 + '챕터).')],
        [hw('mp'), X('Mezzo piano: medium soft, between p and mf.', '조금 여리게. p와 mf 사이예요.')],
        [hw('ff'), X('Fortissimo: very loud. The same letter twice means very.', '매우 세게. 같은 글자 두 개는 ‘매우’.')],
        [hw2('cresc.', 'decresc.'), X('Getting louder; getting softer. Other name for decresc.: dim.', '점점 세게, 점점 여리게. 데크레셴도의 다른 이름은 디미누엔도(dim.).')],
        [hw('sf'), X('Sforzando: a strong accent on one note.', '그 음만 특히 세게.')],
      ]}/>
      <LbPiano steps={[
        X('Play C six times: pp, p, mp, mf, f, ff, one rung louder each time.', 'C를 여섯 번 쳐요: pp, p, mp, mf, f, ff, 한 칸씩 더 세게.'),
        X('Play C D E F G with a crescendo, then with an sf on the G.', 'C D E F G를 점점 세게 친 다음, G에만 sf를 넣어 쳐요.'),
      ]}/>
      <LbRemember>{X('pp p mp mf f ff.', 'pp p mp mf f ff.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('Touch and character', '터치와 느낌')}>
      {live(p5, <TmxTouchPad/>)}
      <LbDefs items={[
        [hw('mezzo staccato'), X('Moderately short: dots and a slur together.', '조금 짧게 끊어서. 점과 이음줄이 함께 있어요.')],
        [hw('sostenuto'), X('Sustained: each note held its full length.', '음을 충분히 끌어서. 음마다 제 길이를 다 채워요.')],
        [hw2('cantabile', 'leggiero'), X('In a singing style; lightly.', '칸타빌레는 노래하듯이, 레지에로는 가볍게.')],
        [hw2('maestoso', 'espressivo'), X('Majestically; with expression.', '마에스토소는 장엄하게, 에스프레시보는 표정 있게.')],
      ]}/>
      <LbPiano steps={[
        X('Play the picture’s three bars: legato, staccato, then mezzo staccato.', '그림의 세 마디를 레가토, 스타카토, 메조 스타카토로 차례로 쳐요.'),
        X('Play C D E F G three times: cantabile, leggiero, maestoso.', 'C D E F G를 세 번 쳐요: 칸타빌레, 레지에로, 마에스토소.'),
      ]}/>
      <LbRemember>{X('Dots: short. A slur: smooth. Both: in between.', '점은 짧게, 이음줄은 부드럽게, 둘 다 있으면 그 사이.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Little words', '꾸며 주는 말')}>
      {live(p6, <TmxBuildPad/>)}
      <LbDefs items={[
        [hw2('molto', 'poco'), X('Very, much; a little. poco a poco: little by little.', '몰토는 매우, 많이. 포코는 조금. 포코 아 포코는 조금씩.')],
        [hw2('sempre', 'senza'), X('Always; without.', '셈프레는 항상(계속), 센차는 ~ 없이.')],
        [hw2('più', 'meno'), X('More; less. più mosso: quicker. meno mosso: slower.', '피우는 더, 메노는 덜. 피우 모소는 더 빠르게, 메노 모소는 더 느리게.')],
        [hw('con'), X('With. con moto: with movement.', '~와 함께. 콘 모토는 움직임 있게.')],
      ]}/>
      <LbPiano steps={[
        X('Play C D E F G A B C poco rit., then molto rit. Hear the difference.', 'C D E F G A B C를 포코 리타르단도로, 그다음 몰토 리타르단도로 쳐요. 차이를 들어요.'),
        X('Play a piece you know sempre staccato, then più mosso.', '아는 곡을 셈프레 스타카토로, 그다음 피우 모소로 쳐요.'),
      ]}/>
      <LbRemember>{X('A little word changes the term beside it: poco rit., slowing down a little.', '꾸며 주는 말이 용어의 뜻을 바꿔요: 포코 리타르단도는 조금 점점 느리게.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, tmxRich(x)])}/>} live={<FiveChecks376 storeKey="pb_five_tmx_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, tmxRich(x)])}/>}/>
    </LbPage>,
  ];
}
function TermsLessonBook() { return <>{tmxLbPages(false)}</>; }
