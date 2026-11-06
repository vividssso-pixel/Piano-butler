// ─── Phase 483: chapter 27, Styles & Genres, on chapter 26's timeline of music: its data, its pictures (texture, the
// sound of each period, the pentatonic keys, the 12-bar blues, swing, a song's map) and the Lesson Book (page 1 the
// timeline with the sound and styles rows its own; pages 2 to 6 texture, the periods, folk, blues and jazz, pop) ───
// Facts: the textures and the period sounds are Phases 282 and 304's (TEXTURE_TYPES, CMP_PERIODS.sound); the 12-bar
// blues is Phase 282's (BLUES_12: I I I I · IV IV I I · V IV I I); blues from African American communities of the
// southern USA in the late 1800s and jazz from New Orleans in the late 1800s and early 1900s (Library of Congress;
// Wikipedia "Jazz"); Arirang, a Korean folk song (UNESCO list 2012); the I V vi IV loop of pop; minimalism and
// nationalism as in CMP_MOVES; the pentatonic scale as a major scale without its 4th and 7th (C D E G A); popular music
// older than pop, which began in the 1950s (Wikipedia "Pop music"). Checked 2026-10-17; r1 review applied.
const csxD = (d) => 12 * Math.floor(d / 7) + [0, 2, 4, 5, 7, 9, 11][d % 7] + 12;   // a staff step (28 = middle C) as a MIDI note
// the tunes of the texture pictures: [beat, step, beats]
const CSX_TUNES = {
  a: [[0, 28, 1], [1, 30, 1], [2, 32, 1], [3, 30, 1], [4, 29, 1], [5, 28, 1], [6, 28, 2]],
  b: [[0, 32, 1], [1, 31, 1], [2, 30, 1], [3, 31, 1], [4, 32, 1], [5, 32, 1], [6, 32, 2]],
  c: [[0, 30, 1], [1, 29, 1], [2, 28, 1], [3, 29, 1], [4, 30, 1], [5, 30, 1], [6, 30, 2]],
};
// homophony: chords under the tune (C, G, C); polyphony: a second tune entering on beat 3 (the app's Phase 282 voice)
const CSX_CHORDS = { a: [[0, [21, 23, 25], 4], [4, [18, 20, 22], 1], [5, [21, 23, 25], 3]], b: [[0, [21, 23, 25], 4], [4, [18, 20, 22], 4]], c: [[0, [21, 23, 25], 8]] };
// a: a second tune of its own (r1); b and c: the tune itself an octave lower, two beats later (a round)
const CSX_VOICE2 = { a: [[2, 23, 1], [3, 25, 1], [4, 27, 1], [5, 26, 1], [6, 24, 1], [7, 23, 1], [8, 21, 2]] };   // E3 G3 B3 A3 F3 E3 C3: 3rds, 6ths, a 5th with the tune
CSX_VOICE2.b = CSX_TUNES.b.map(([b, d, l]) => [b + 2, d - 7, l]); CSX_VOICE2.c = CSX_TUNES.c.map(([b, d, l]) => [b + 2, d - 7, l]);
const CSX_TEX = ['monophony', 'homophony', 'polyphony'];
const CSX_TEX_W = { monophony: ['monophony', '모노포니'], homophony: ['homophony', '호모포니'], polyphony: ['polyphony', '폴리포니'] };
const csxTexW = (id) => t(CSX_TEX_W[id][0], CSX_TEX_W[id][1]);
// what to listen for in each period (from CMP_PERIODS.sound), and its texture
const CSX_ERA = {
  baroque: { tex: 'polyphony', listen: [['busy lines woven together', '바쁘게 얽히는 여러 선율'], ['a steady, busy pulse', '촘촘하고 일정한 박'], ['many ornaments, such as trills', '트릴 같은 많은 꾸밈음']] },
  classical: { tex: 'homophony', listen: [['a clear tune over light chords', '가벼운 화음 위의 또렷한 선율'], ['balanced phrases, like question and answer', '질문과 대답처럼 균형 잡힌 프레이즈'], ['an Alberti bass in the left hand', '왼손의 알베르티 베이스']] },
  romantic: { tex: 'homophony', listen: [['long, singing tunes', '길게 노래하는 선율'], ['rich chords and pedal', '풍부한 화음과 페달'], ['rubato that stretches the time', '빠르기를 늘였다 줄였다 하는 루바토']] },
  modern: { tex: null, listen: [['new scales and chords', '새로운 음계와 화음'], ['strong, surprising rhythms', '강하고 놀라운 리듬'], ['jazz and folk mixed in', '재즈와 민요가 섞인 소리']] },
  contemporary: { tex: null, listen: [['short patterns repeated, in minimalism', '짧은 패턴을 되풀이하는 미니멀리즘'], ['any sound at all, even silence', '어떤 소리든, 침묵까지도'], ['music for films and games', '영화와 게임 음악']] },
};
const CSX_PENTA = [0, 2, 4, 7, 9];        // C D E G A
const CSX_BLACK = [1, 3, 6, 8, 10];       // the five black keys
const CSX_SONG = ['verse', 'chorus', 'verse', 'chorus', 'bridge', 'chorus'];
const CSX_SONG_W = { verse: ['verse', '벌스'], chorus: ['chorus', '후렴'], bridge: ['bridge', '브리지'] };
const CSX_POP = [['C', [48, 60, 64, 67]], ['G', [43, 59, 62, 67]], ['Am', [45, 60, 64, 69]], ['F', [41, 60, 65, 69]]];
const csxNbKo = (x) => typeof x !== 'string' ? x : cpxNbKo(x).replace(/12마디 블루스/g, '12마디 블루스').replace(/5음 ?음계/g, '5음음계').replace(/민속 음악/g, '민속 음악')
  .replace(/길게-짧게/g, '길게-⁠짧게').replace(/8분음표 (두|한)/g, '8분음표 $1').replace(/(두|세|네|다섯) (개|음|화음|줄|번째|박)/g, '$1 $2').replace(/즉흥 연주/g, '즉흥 연주').replace(/새 가사/g, '새 가사').replace(/통통 튀는/g, '통통 튀는').replace(/재즈와 블루스/g, '재즈와 블루스').replace(/지어 쳐요/g, '지어 쳐요').replace(/ (것|선율|음악|노래|소리)\./g, ' $1.').replace(/C[  ]G[  ]Am[  ]F/g, 'C G Am F').replace(/오늘날 같은 팝/g, '오늘날 같은 팝').replace(/(I|IV|V) 화음/g, '$1 화음');
const csxKoT = (x) => LANG === 'ko' ? csxNbKo(x) : x;
// note names spaced apart (no letter-spacing), so that F♯ G♯ reads as two notes
const csxNotes = (x) => typeof x === 'string' && / /.test(x) && /^[A-G][♯♭]? [A-G]/.test(x) ? <span style={{display:'inline-flex',gap:'0.42em',letterSpacing:0,whiteSpace:'nowrap'}}>{x.split(' ').map((n, i) => <span key={i}>{n}</span>)}</span> : x;

// ── pictures ──
// a piano roll: the tune (navy), the chords under it (light), a second tune (coral, the thing to see; navy when even, in
// a test). Every roll has the same pitch range (steps 17 to 33) and ten beats, so the picture tells only the texture.
function CsxRoll({ tex, tune = 'a', W = 300, label, mini, even, alberti }) {
  const notes = CSX_TUNES[tune], beats = 10, x0 = 6, bw = (W - x0 - 6) / beats, H = mini ? 74 : 92;
  const lo = 17, hi = 33, Y = (d) => 8 + (hi - d) * ((H - 16) / (hi - lo)), bh = Math.max(4, (H - 16) / (hi - lo) - 1);
  const bar = (b, d, dur, col, k, op = 1) => <rect key={k} x={x0 + b * bw + 1.2} y={Y(d) - bh / 2} width={dur * bw - 2.4} height={bh} rx={bh / 2} fill={col} opacity={op}/>;
  return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={label} style={{width:'100%',height:'auto',display:'block'}}>
    {Array.from({ length: beats + 1 }, (_, i) => <line key={'g' + i} x1={x0 + i * bw} x2={x0 + i * bw} y1={2} y2={H - 2} stroke="rgba(38,41,107,0.10)" strokeWidth="0.8"/>)}
    {tex === 'homophony' && (alberti ? CSX_CHORDS[tune].flatMap(([b, ds, dur], i) => Array.from({ length: dur * 2 }, (_, k) => bar(b + k / 2, ds[[0, 2, 1, 2][k % 4]], 0.5, PEN_N, 'h' + i + '-' + k, 0.35)))   // root, fifth, third, fifth in quavers
      : CSX_CHORDS[tune].flatMap(([b, ds, dur], i) => ds.map((d, j) => bar(b, d, dur, PEN_N, 'h' + i + j, 0.28))))}
    {notes.map(([b, d, dur], i) => bar(b, d, dur, PEN_N, 'n' + i))}
    {tex === 'polyphony' && CSX_VOICE2[tune].map(([b, d, dur], i) => bar(b, d, dur, even ? PEN_N : PEN_C, 'p' + i))}
  </svg>;
}
const CSX_PC_W = ['C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B'];
const csxKeyTap = (onKey, pc) => onKey ? { role: 'button', tabIndex: 0, 'aria-label': CSX_PC_W[pc], className: 'csx-key', style: { cursor: 'pointer' }, onClick: () => onKey(pc), onKeyDown: (e) => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); onKey(pc); } } } : {};
// one octave of keys, C to B: the keys in `on` filled (white pale coral, black coral), their letters below; onKey makes
// them keys (a black key's hit area wider than it looks); hollow: black keys drawn open, to colour in; kh: the white keys' height
function CsxKeys({ on = [], W = 230, label, letters = true, onKey, lit = -1, hollow, kh = 60, fs = 12 }) {
  const ww = W / 7, bh = kh * 0.62, H = letters ? kh + fs + 6 : kh + 2, wh = [0, 2, 4, 5, 7, 9, 11], bl = [[1, 1], [3, 2], [6, 4], [8, 5], [10, 6]];
  return <svg viewBox={`0 0 ${W} ${H}`} role={onKey ? 'group' : 'img'} aria-label={label} style={{width:'100%',height:'auto',display:'block'}}>
    {wh.map((pc, i) => <g key={pc} {...csxKeyTap(onKey, pc)}><rect x={i * ww + 0.5} y={0.5} width={ww - 1} height={kh} rx={2} fill={lit === pc ? PEN_C : on.includes(pc) ? 'rgba(228,87,46,0.22)' : '#fff'} stroke={PEN_N} strokeWidth="1"/>
      {letters && on.includes(pc) && <text x={i * ww + ww / 2} y={kh + fs + 2} textAnchor="middle" fontSize={fs} fontWeight="900" fill={PEN_N}>{'CDEFGAB'[i]}</text>}</g>)}
    {bl.map(([pc, at]) => <g key={pc} {...csxKeyTap(onKey, pc)}>{onKey && <rect x={at * ww - ww * 0.42} y={0} width={ww * 0.84} height={bh + 4} fill="transparent"/>}<rect x={at * ww - ww * 0.3} y={0.5} width={ww * 0.6} height={bh} rx={1.5} fill={lit === pc ? PEN_C : on.includes(pc) ? PEN_C : hollow ? '#fff' : PEN_N} stroke={lit === pc ? '#fff' : PEN_N} strokeWidth={lit === pc ? 2 : hollow ? 1.3 : 1}/></g>)}
  </svg>;
}
// the pentatonic scale from the major scale: C D E F G A B C with its 4th and 7th (F, B) left out (dashed, struck)
function CsxMinus47({ W = 640, label }) {
  const n = 8, bw = W / n, H = 92, out = [3, 6];
  return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={label} style={{width:'100%',height:'auto',display:'block'}}>
    {'CDEFGABC'.split('').map((l, i) => { const x = i * bw, o = out.includes(i);
      return <g key={i}><rect x={x + 4} y={4} width={bw - 8} height={56} rx={8} fill={o || i === 7 ? '#fff' : 'rgba(228,87,46,0.18)'} stroke={o ? 'rgba(38,41,107,0.45)' : PEN_N} strokeWidth={o ? 1.2 : 1.4} strokeDasharray={o ? '5 4' : undefined}/>
        <text x={x + bw / 2} y={41} textAnchor="middle" fontSize="24" fontWeight="900" fill={o ? 'rgba(38,41,107,0.4)' : PEN_N}>{l}</text>
        {o && <line x1={x + 16} y1={50} x2={x + bw - 16} y2={14} stroke={PEN_C} strokeWidth="2.4" strokeLinecap="round"/>}
        <text x={x + bw / 2} y={82} textAnchor="middle" fontSize="15" fontWeight="800" fill={o ? PEN_C : BK.muted}>{i + 1}</text></g>; })}
  </svg>;
}
// the 12-bar blues: three lines of four bars; gaps empty (dashed); hl the bar playing
function CsxBlues({ gaps = [], hl = -1, letters = true, label, W = 360, ch = 40, nums, fill }) {
  const cw = W / 4, H = 3 * ch + 4, NM = { I: 'C', IV: 'F', V: 'G' }, f = Math.min(17, ch * 0.38 + 2);
  return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={label} style={{width:'100%',height:'auto',display:'block'}}>
    {BLUES_12.map((c, i) => { const x = (i % 4) * cw, y = Math.floor(i / 4) * ch + 2, gap = gaps.includes(i), on = hl === i;
      return <g key={i}><rect x={x + 2} y={y + 2} width={cw - 4} height={ch - 4} rx={4} fill={on || fill === i ? 'rgba(228,87,46,0.12)' : '#fff'} stroke={on || fill === i ? PEN_C : PEN_N} strokeWidth={on || fill === i ? 2 : 1} strokeDasharray={gap ? '4 3' : undefined}/>
        <text x={x + 8} y={y + 14} fontSize="10.5" fontWeight="700" fill={BK.muted}>{i + 1}</text>
        {gap && nums && <text x={x + cw - 9} y={y + 15} textAnchor="end" fontSize="11" fontWeight="700" fontStyle="italic" fill={BK.ink} style={{fontFamily:LB_SERIF}}>{nums[gaps.indexOf(i)]}</text>}
        {!gap && <text x={x + cw / 2} y={y + ch / 2 + f * 0.36 + 1} textAnchor="middle" fontSize={f} fontWeight="900" fill={on || fill === i ? PEN_C : PEN_N}>{c}{letters ? ' ' : ''}<tspan fontSize={f * 0.72} fontWeight="700" fill={BK.muted}>{letters ? NM[c] : ''}</tspan></text>}</g>; })}
  </svg>;
}
// four beats of quavers: written (even), or played straight or swung (long-short)
function CsxSwing({ swing, W = 300, label, lit = -1, H = 30 }) {
  const bw = W / 4, long = swing ? 2 / 3 : 1 / 2, rh = H - 12;
  return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={label} style={{width:'100%',height:'auto',display:'block'}}>
    {[0, 1, 2, 3].map(k => [0, 1].map(j => { const x = k * bw + (j ? long * bw : 0) + 2, w = (j ? 1 - long : long) * bw - 4, on = lit === k * 2 + j;
      return <rect key={k + '-' + j} x={x} y={6} width={w} height={rh} rx={Math.min(8, rh / 3)} fill={on ? PEN_C : j ? 'rgba(38,41,107,0.45)' : PEN_N}/>; }))}
  </svg>;
}
// a song's map: verse, chorus, verse, chorus, bridge, chorus; hl: the kind lit
function CsxSong({ hl, W = 460, label, bh = 34, fs = 12 }) {
  const cols = W < 400 ? 3 : 6, bw = W / cols, rowH = bh + 8, H = Math.ceil(6 / cols) * rowH + 2;
  return <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={label} style={{width:'100%',height:'auto',display:'block'}}>
    {CSX_SONG.map((k, i) => { const on = hl === k, ch = k === 'chorus', x = (i % cols) * bw, y = Math.floor(i / cols) * rowH + 4;
      return <g key={i}><rect x={x + 2} y={y} width={bw - 4} height={bh} rx={6} fill={on ? 'rgba(228,87,46,0.12)' : ch ? 'rgba(38,41,107,0.12)' : '#fff'} stroke={on ? PEN_C : PEN_N} strokeWidth={on ? 2 : 1}/>
        <text x={x + bw / 2} y={y + bh / 2 + fs * 0.36} textAnchor="middle" fontSize={fs} fontWeight="900" fill={on ? PEN_C : PEN_N}>{t(CSX_SONG_W[k][0], CSX_SONG_W[k][1])}</text></g>; })}
  </svg>;
}
// the sound of each period: its name and years, its texture, what to listen for
function CsxEraChart({ sel, onTap, scr }) {
  return <div style={{display:'flex',flexDirection:'column',width:'100%'}}>
    {MTL_ERAS.map(id => { const E = CSX_ERA[id], on = sel === id;
      const body = <><span style={{display:'block',fontSize:scr ? 15 : 17,fontWeight:900,color:on ? BK.coral : BK.ink,wordBreak:'keep-all'}}>{cmpEraTag(id)} <span style={{fontWeight:700,fontSize:scr ? 12.5 : 14,color:on ? BK.coral : BK.muted,whiteSpace:'nowrap'}}>{cpxYrs(id)}</span>{E.tex && <span style={{fontWeight:800,fontSize:scr ? 12.5 : 14,color:BK.ink,whiteSpace:'nowrap'}}>{' · ' + csxTexW(E.tex)}</span>}</span>
        <span style={{display:'block',fontSize:scr ? 13.5 : 15,color:BK.ink,lineHeight:1.4,marginTop:scr ? 0 : 2,wordBreak:'keep-all'}}>{csxKoT(E.listen.map(w => t(w[0], w[1])).join(' · '))}</span></>;
      const line = { borderStyle:'solid', borderColor:'rgba(38,41,107,0.16)', borderWidth:'1px 0 0', borderRadius:0, textAlign:'left' };
      return onTap ? <button key={id} type="button" className="cpx-who" aria-pressed={on} onClick={() => onTap(id)} style={{...line,display:'flex',flexDirection:'column',background:on ? 'rgba(228,87,46,0.07)' : 'transparent',font:'inherit',color:'inherit',cursor:'pointer',minHeight:44,padding:'6px 4px 4px',margin:0}}>{body}</button>
        : <div key={id} style={{...line,padding:'8px 0 7px',display:'grid',gridTemplateColumns:'120px minmax(0,1fr)',gap:16,alignItems:'center'}}><div>{E.tex && <CsxRoll tex={E.tex} tune="a" mini W={150} alberti={id === 'classical'} label={cmpEraTag(id) + ': ' + csxTexW(E.tex)}/>}</div><div>{body}</div></div>; })}
  </div>;
}

function csxLbPages(scr = false) {
  const ch = 'styles';
  const live = (still, comp) => <LbLive still={still} live={comp}/>;
  const stack = (nodes, h, gap = 12, mw = 680, pad) => <LbPic h={h} pad={pad}><div style={{display:'flex',flexDirection:'column',gap,width:'100%',maxWidth:mw,margin:'0 auto',alignItems:'stretch'}}>{nodes}</div></LbPic>;
  const X = (en, ko) => sscT(en, skgKo(csxNbKo(ko)));
  const cap = (x, key = 'cap') => <div key={key} style={{textAlign:'center',fontSize:scr ? 14 : 13.5,fontWeight:800,color:BK.ink,margin:'2px auto 0',maxWidth:600,lineHeight:1.35,textWrap:'balance',wordBreak:'keep-all'}}>{csxKoT(x)}</div>;
  const lab = (x, key) => <div key={key} style={{fontSize:12,fontWeight:900,letterSpacing:'0.08em',color:BK.muted,textAlign:'center',textTransform:'uppercase'}}>{csxKoT(x)}</div>;
  const ch26 = bkChapterNo('composers'), ch24 = bkChapterNo('form'), ch22 = bkChapterNo('chords');

  // p1 (macro first): chapter 26's timeline, the sound and styles rows its own
  const p1 = <LbLive still={stack([<MusTimeline key="m" focus={['sound', 'style']} cmpNames={false} fs={12} laneH={7} barH={4} firstPiano label={t('The timeline of music, 1600 to today. Sound: Baroque, counterpoint; Classical, a clear tune; Romantic, big feelings; Modern, new sounds; Contemporary, anything goes. Styles: folk songs always and everywhere; blues from 1890; ragtime 1895 to 1920; jazz from 1900; rock and pop from 1950. The composers of chapter ' + ch26 + ', lightly.', '음악의 타임라인, 1600년부터 오늘날까지. 소리: 바로크는 대위법, 고전주의는 또렷한 선율, 낭만주의는 풍부한 감정, 근대는 새로운 소리, 현대는 무엇이든 가능. 스타일: 민요는 언제나 어디서나, 블루스는 1890년부터, 래그타임은 1895~1920, 재즈는 1900년부터, 록과 팝은 1950년부터. ' + ch26 + '챕터의 작곡가는 흐리게.')}/>,
    cap(t('The sound row: how each period sounds. The styles row: the genres beside the concert hall. The faint lines are chapter ' + ch26 + '’s composers.', '소리 줄: 시대마다 다른 소리. 스타일 줄: 연주회장 밖의 장르. 흐린 선은 ' + ch26 + '챕터의 작곡가예요.'))], 300, 8)} live={<CsxMapPad/>}/>;
  // p2: texture: one tune, three ways
  const rollBox = (tex, key) => <div key={key} style={{display:'grid',gridTemplateColumns:'118px minmax(0,1fr)',alignItems:'center',gap:12}}>
    <div style={{fontSize:14,fontWeight:900,color:BK.ink,textAlign:'right'}}>{csxTexW(tex)}<div style={{fontSize:11.5,fontWeight:700,color:BK.muted}}>{csxKoT({ monophony: t('one line', '한 줄'), homophony: t('a tune and chords', '선율과 화음'), polyphony: t('two tunes at once', '두 선율이 함께') }[tex])}</div></div>
    <div style={{maxWidth:440}}><CsxRoll tex={tex} label={csxTexW(tex) + ': ' + t({ monophony: 'the tune alone.', homophony: 'the tune, with chords under it.', polyphony: 'the tune, and a second tune (coral) starting two beats later.' }[tex], { monophony: '선율만 있어요.', homophony: '선율 아래에 화음이 있어요.', polyphony: '선율이 있고, 두 박 뒤에 두 번째 선율(산호색)이 시작해요.' }[tex])}/></div></div>;
  const p2 = stack([...CSX_TEX.map((x, i) => rollBox(x, 'r' + i)), cap(t('The same tune three ways. Each block is a note: higher is higher, longer is longer.', '같은 선율을 세 가지 텍스처로 그렸어요. 막대 하나가 음 하나예요. 위에 있을수록 높은 음, 길수록 긴 음이에요.'), 'c2')], 330, 16, 620);
  // p3: the sound of each period
  const p3 = stack([<CsxEraChart key="e"/>, cap(t('Listen for these in a piece. Each period is chapter ' + ch26 + '’s, by its years.', '곡에서 이런 소리를 찾아 들어 봐요. 시대의 연도는 ' + ch26 + '챕터와 같아요.'), 'c3')], 330, 10, 660);
  // p4: folk music: the pentatonic scale on the white keys and on the black keys (folk's lane is on page 1)
  const p4 = stack([<div key="m" style={{maxWidth:600,margin:'0 auto',width:'100%'}}>{lab(t('the major scale without 4 and 7', '장음계에서 4와 7을 빼면'), 'l0')}<CsxMinus47 label={t('C D E F G A B C numbered 1 to 8; F (4) and B (7) crossed out: C D E G A are left.', 'C D E F G A B C에 1부터 8까지 번호를 붙였어요. F(4)와 B(7)를 지워서 C D E G A가 남아요.')}/></div>,
    <div key="k" style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:30,maxWidth:640,margin:'0 auto',width:'100%'}}>
      <div>{lab(t('five white keys', '흰건반 다섯 개'), 'l1')}<CsxKeys on={CSX_PENTA} kh={112} fs={16} label={t('One octave: C, D, E, G and A filled: a pentatonic scale.', '한 옥타브: C, D, E, G, A를 칠했어요. 5음음계예요.')}/></div>
      <div>{lab(t('the five black keys', '검은건반 다섯 개'), 'l2')}<CsxKeys on={CSX_BLACK} letters={false} kh={112} label={t('One octave: the five black keys coral: a pentatonic scale too.', '한 옥타브: 검은건반 다섯 개를 산호색으로 칠했어요. 이것도 5음음계예요.')}/></div></div>,
    cap(t('A major scale without its 4th and 7th notes: five notes, no half steps between them. Many folk songs use them, such as Korea’s “Arirang”.', '장음계에서 4번째와 7번째 음을 뺀 다섯 음: 사이에 반음이 없어요. “아리랑”처럼 많은 민요가 이 다섯 음을 써요.'), 'c4')], 300, 22, 640);
  // p5: blues and jazz: the 12-bar blues, and swing
  const p5 = stack([<div key="b" style={{maxWidth:600,margin:'0 auto',width:'100%'}}>{lab(t('the 12-bar blues in C', 'C장조 12마디 블루스'), 'l3')}<CsxBlues W={480} ch={62} label={t('The 12-bar blues in C: bars 1 to 4 I (C); bars 5 and 6 IV (F), 7 and 8 I; bar 9 V (G), 10 IV, 11 and 12 I.', 'C장조 12마디 블루스: 1~4마디 I(C), 5~6마디 IV(F), 7~8마디 I, 9마디 V(G), 10마디 IV, 11~12마디 I.')}/></div>,
    <div key="s" style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:30,maxWidth:620,margin:'0 auto',width:'100%'}}>
      <div>{lab(t('straight', '스트레이트'), 'l4')}<CsxSwing H={52} label={t('Four beats of quavers played straight: each pair even.', '8분음표를 스트레이트로 친 네 박: 두 음이 고르게.')}/></div>
      <div>{lab(t('swing', '스윙'), 'l5')}<CsxSwing swing H={52} lit={0} label={t('Four beats of quavers swung: each pair long-short; the first long one coral.', '8분음표를 스윙으로 친 네 박: 두 음이 길게-짧게. 첫 긴 음은 산호색.')}/></div></div>,
    cap(t('Three chords over twelve bars; quavers played long-short.', '열두 마디에 세 화음, 길게-짧게 치는 8분음표.'), 'c5')], 300, 16, 600);
  // p6: pop: a song's map and the four chords
  const p6 = stack([<div key="m" style={{maxWidth:640,margin:'0 auto',width:'100%'}}>{lab(t('a song’s map', '노래의 지도'), 'l6')}<CsxSong hl="chorus" W={640} bh={62} fs={18} label={t('A song’s map: verse, chorus, verse, chorus, bridge, chorus. The chorus (coral) is heard three times.', '노래의 지도: 벌스, 후렴, 벌스, 후렴, 브리지, 후렴. 후렴(산호색)이 세 번 나와요.')}/></div>,
    <div key="c" style={{display:'grid',gridTemplateColumns:'repeat(4,minmax(0,1fr))',gap:14,maxWidth:600,margin:'0 auto',width:'100%'}}>{CSX_POP.map(([n, ms], i) => <div key={n} style={{border:'1.2px solid ' + BK.ink,borderRadius:6,padding:'16px 10px 12px',textAlign:'center',background:'#fff'}}><div style={{fontSize:36,fontWeight:900,color:BK.ink,lineHeight:1.1}}>{n}</div><div style={{fontSize:13,fontWeight:800,color:BK.muted,margin:'2px 0 8px'}}>{['I', 'V', 'vi', 'IV'][i]}</div>
      <CsxKeys on={[...new Set(ms.slice(1).map(m => m % 12))]} W={120} kh={62} fs={12} label={t('The notes of ' + n + ': ', n + ' 화음의 음: ') + [...new Set(ms.slice(1).map(m => CSX_PC_W[m % 12]))].join(' ')}/></div>)}</div>,
    cap(t('The chorus comes back with the same words. Many songs loop four chords: C G Am F.', '후렴은 같은 가사로 다시 나와요. 많은 노래가 네 화음 C G Am F를 되풀이해요.'), 'c6')], 260, 24, 640);

  // the check icons
  const R = (x, y, w, h, extra = '') => '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" ' + extra + '/>';
  const ic = {
    tex: [{ k: 'raw', svg: [[8, 12, 22], [32, 8, 22], [56, 12, 22]].map(([x, y, w]) => R(x, y, w, 5, 'rx="2.5" fill="' + PEN_N + '"')).join('') + [[22, 26, 26], [46, 22, 26]].map(([x, y, w]) => R(x, y, w, 5, 'rx="2.5" fill="' + PEN_C + '"')).join('') }],
    sound: [{ k: 'raw', svg: [6, 24, 40, 56, 70].map((x, i, a) => R(x, 6, (a[i + 1] || 86) - x - 2, 10, 'fill="none" stroke="' + PEN_N + '" stroke-width="1.3"')).join('') + '<path d="M8 30 Q16 20 24 30 T40 30 T56 30 T72 30 T88 30" fill="none" stroke="' + PEN_C + '" stroke-width="1.6"/>' }],
    penta: [{ k: 'raw', svg: [0, 1, 2, 3, 4, 5, 6].map(i => R(18 + i * 8, 6, 8, 28, 'fill="#fff" stroke="' + PEN_N + '" stroke-width="1.1"')).join('') + [0, 1, 3, 4, 5].map(i => R(23.5 + i * 8, 6, 5, 16, 'fill="' + PEN_C + '"')).join('') }],
    blues: [{ k: 'raw', svg: [0, 1, 2, 3].map(i => R(10 + i * 19, 4, 17, 9, 'fill="none" stroke="' + PEN_N + '" stroke-width="1.1"')).join('') + [0, 1, 2, 3].map(i => R(10 + i * 19, 16, 17, 9, 'fill="none" stroke="' + PEN_N + '" stroke-width="1.1"')).join('') + [0, 1, 2, 3].map(i => R(10 + i * 19, 28, 17, 9, 'fill="' + (i === 0 ? PEN_C : 'none') + '" stroke="' + (i === 0 ? PEN_C : PEN_N) + '" stroke-width="1.1"')).join('') }],
    pop: [{ k: 'raw', svg: [0, 1, 2, 3, 4, 5].map(i => R(4 + i * 14.5, 12, 12.5, 16, 'rx="2" fill="' + ([1, 3, 5].includes(i) ? PEN_C : 'none') + '" stroke="' + ([1, 3, 5].includes(i) ? PEN_C : PEN_N) + '" stroke-width="1.2"')).join('') }],
  };
  const checksRows = [
    ['tex', t('I can hear and name monophony, homophony and polyphony', '모노포니, 호모포니, 폴리포니를 듣고 이름을 말할 수 있어요')],
    ['sound', t('I can name one sound of each period', '시대마다 소리의 특징을 하나씩 말할 수 있어요')],
    ['penta', t('I can play a pentatonic scale and make up a tune on it', '5음음계를 치고, 그 다섯 음으로 선율을 지어 칠 수 있어요')],
    ['blues', t('I can play the 12-bar blues chords and swing my quavers', '12마디 블루스의 화음을 치고, 8분음표를 스윙으로 칠 수 있어요')],
    ['pop', t('I can point to the verse and the chorus of a song', '노래에서 벌스와 후렴을 가리킬 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? skgKo(sscNbKo(csxNbKo(x))) : sscNbEn(x)]);

  const P = (k, kicker, title, pic, defs, steps, rem, pad) => <LbPage key={k} no={k} chId={ch} kicker={kicker} title={title}>
    {live(pic, pad)}
    <LbDefs items={defs}/>
    <LbPiano steps={steps}/>
    <LbRemember>{rem}</LbRemember>
  </LbPage>;

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {p1}
      <LbSay size={17.5}>{LANG === 'ko' ? <>음악 소리의 특징이 <b>스타일</b>이에요. 스타일이 같은 음악끼리 묶은 갈래가 <b>장르</b>예요. 민속 음악, 클래식, 재즈, 대중음악처럼요.</> : <><b>Style</b> is the way music sounds. A <b>genre</b> is a family of music that shares a style: folk, classical, jazz, pop.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Texture', '텍스처'), 2], [t('The sound of each period', '시대마다 다른 소리'), 3], [t('Folk music', '민속 음악'), 4], [t('Blues and jazz', '블루스와 재즈'), 5], [t('Pop', '대중음악'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'baseline',gap:8,fontSize:15,padding:'3px 0',borderBottom:'1px dotted rgba(38,41,107,0.3)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)',textWrap:'pretty'}}>{bkGoal(15)}<span>{x.replace(/^I can /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    P(2, t('Step 1', '1단계'), t('Texture', '텍스처'), p2, [
      [t('texture', '텍스처'), X('How the lines of music are layered.', '음악에서 선율과 화음이 짜인 모양. 다른 이름은 짜임새예요.')],
      [t('monophony', '모노포니'), X('One line alone.', '선율 한 줄만 있는 것.')],
      [t('homophony', '호모포니'), X('A tune with chords underneath.', '아래에서 화음이 받쳐 주는 선율.')],
      [t('polyphony', '폴리포니'), X('Two or more tunes at once, each as important as the other (counterpoint, chapter ' + ch26 + ').', '두 개 이상의 선율이 똑같이 중요하게 동시에 흐르는 것(대위법, ' + ch26 + '챕터).')],
    ], [
      X('Play a tune with your right hand alone. Then add left-hand chords under it.', '오른손으로 선율만 쳐요. 그다음 왼손으로 아래에 화음을 더해요.'),
      X('With your teacher, play a tune as a round: start when they reach bar 3.', '선생님과 돌림노래로 쳐요: 선생님이 3마디에 오면 시작해요.'),
    ], X('One line: monophony. A tune and chords: homophony. Tunes together: polyphony.', '한 줄은 모노포니, 선율과 화음은 호모포니, 여러 선율이 함께 흐르면 폴리포니.'), <CsxTexturePad/>),

    P(3, t('Step 2', '2단계'), t('The sound of each period', '시대마다 다른 소리'), p3, [
      [t('style', '스타일'), X('The way music sounds: its texture, rhythm, harmony and instruments.', '음악 소리의 특징: 텍스처, 리듬, 화음, 악기. 다른 이름은 양식이에요.')],
      [t('classical music', '클래식'), X('Written-down concert music of any period, such as Bach’s, Mozart’s or Chopin’s. The Classical period, with a capital C, is only 1750 to 1820.', '바흐, 모차르트, 쇼팽의 곡처럼, 어느 시대든 악보에 적어 연주회에서 연주하는 음악. 고전주의 시대는 1750~1820년이에요.')],
      [t('ornament', '꾸밈음'), X('A quick decoration of a note, such as a trill.', '음을 빠르게 꾸미는 것. 트릴도 꾸밈음이에요.')],
      [t('minimalism', '미니멀리즘'), X('Music of short patterns repeated many times, changing slowly.', '짧은 패턴을 여러 번 되풀이하며 조금씩 바꾸는 음악.')],
    ], [
      X('Play a piece you know. Say its period and one sound that shows it.', '아는 곡을 쳐요. 그 곡의 시대와, 그 시대를 보여 주는 소리 하나를 말해요.'),
      X('Play a short pattern of four notes again and again, changing one note every few times.', '네 음으로 된 짧은 패턴을 되풀이해서 치고, 몇 번 칠 때마다 음 하나를 바꿔요.'),
    ], X('Baroque: tunes woven together. Classical: a clear tune. Romantic: big feelings.', '바로크는 얽히는 선율, 고전주의는 또렷한 선율, 낭만주의는 풍부한 감정.'), <CsxEraPad/>),

    P(4, t('Step 3', '3단계'), t('Folk music', '민속 음악'), p4, [
      [t('folk music', '민속 음악'), X('The songs and dances of a people, passed on by ear. Their composers are often unknown.', '한 민족이 귀로 전해 온 노래와 춤곡. 작곡가를 모르는 경우가 많아요.')],
      [t('pentatonic scale', '5음음계'), X('A scale of five notes: a major scale without its 4th and 7th notes, such as C D E G A, or the five black keys.', 'C D E G A나 검은건반 다섯 개처럼, 장음계에서 4번째와 7번째 음을 뺀 다섯 음의 음계.')],
      [t('nationalism', '국민악파'), X('Using your own country’s folk music in concert music, as Bartók and Dvořák did.', '바르토크와 드보르자크처럼, 자기 나라의 민속 음악을 곡에 담은 작곡가들.')],
    ], [
      X('Play C D E G A up and down. Then make up a tune with only these notes.', 'C D E G A를 올라갔다 내려와요. 그다음 이 음들로만 선율을 지어 쳐요.'),
      X('Play a folk song you know, such as “Arirang” or “Auld Lang Syne”.', '“아리랑”이나 “올드 랭 사인”처럼 아는 민요를 쳐요.'),
    ], X('Folk songs are passed on by ear. Many use five notes.', '민요는 귀로 전해져요. 다섯 음을 쓰는 민요가 많아요.'), <CsxPentaPad/>),

    P(5, t('Step 4', '4단계'), t('Blues and jazz', '블루스와 재즈'), p5, [
      [t('blues', '블루스'), X('Music from African American communities of the southern USA, from the late 1800s.', '1800년대 후반 미국 남부의 아프리카계 미국인 공동체에서 생긴 음악.')],
      [t('12-bar blues', '12마디 블루스'), X('Three chords, I, IV and V, over twelve bars: I I I I · IV IV I I · V IV I I.', '세 화음 I, IV, V로 된 열두 마디: I I I I · IV IV I I · V IV I I.')],
      [t('swing', '스윙'), X('Pairs of quavers played long-short.', '8분음표 두 개를 길게-짧게 치는 것.')],
      [t('jazz', '재즈'), X('Music from New Orleans, from about 1900, grown from blues and ragtime. Its players improvise: they make music up as they play.', '1900년쯤 뉴올리언스에서 블루스와 래그타임을 바탕으로 생긴 음악. 연주자는 즉흥 연주를 해요: 연주하면서 음악을 지어내요.')],
    ], [
      X('Play the 12-bar blues in C with your left hand: C, F and G, one chord a bar.', '왼손으로 C장조 12마디 블루스를 쳐요: C, F, G를 한 마디에 한 화음씩.'),
      X('Play quavers on one note, straight, then swung: long-short.', '한 음으로 8분음표를 스트레이트로, 그다음 스윙으로 쳐요: 길게-짧게.'),
    ], X('Blues: three chords, twelve bars. Jazz swings and improvises.', '블루스는 세 화음, 열두 마디. 재즈는 스윙하고 즉흥 연주해요.'), <CsxBluesPad/>),

    P(6, t('Step 5', '5단계'), t('Pop', '대중음악'), p6, [
      [t('popular music', '대중음악'), X('Music made for many listeners: songs on records, radio and online. Today’s pop began in the 1950s.', '많은 사람이 듣도록 만든 음악: 음반, 라디오, 인터넷으로 듣는 노래. 오늘날 같은 팝은 1950년대에 시작됐어요.')],
      [t('verse', '벌스'), X('The part of a song with the same tune and new words each time.', '노래에서 같은 선율에 매번 새 가사가 붙는 부분.')],
      [t('chorus', '후렴'), X('The part of a song that comes back with the same tune and the same words.', '노래에서 같은 선율과 같은 가사로 다시 나오는 부분.')],
      [t('bridge', '브리지'), X('A new part, heard once near the end, before the last chorus.', '끝 무렵 마지막 후렴 전에 한 번 나오는 새로운 부분.')],
    ], [
      X('Play C G Am F as chords, four beats each, again and again.', 'C G Am F 화음을 하나에 네 박씩, 되풀이해서 쳐요.'),
      X('Sing or play a song you know. Point to each verse and each chorus.', '아는 노래를 부르거나 쳐요. 벌스와 후렴이 나올 때마다 가리켜요.'),
    ], X('The verse changes its words; the chorus comes back the same.', '벌스는 가사가 바뀌고, 후렴은 그대로 다시 나와요.'), <CsxPopPad/>),

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 펴고 하나씩 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:80}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_csx_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, x])}/>}/>
    </LbPage>,
  ];
}
function StylesLessonBook() { return <>{csxLbPages(false)}</>; }
