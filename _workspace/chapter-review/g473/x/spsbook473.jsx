// ─── Phase 473: chapter 18, The Piano's Story: the last room of Level 3 (the level plan of Phase 435), built in full under
// Book rules 14 and 15 (her 2026-10-14 09:17 '계속 가줘 최종검토는 한꺼번에하게'). What the room teaches at Level 3: the two
// keyboards before the piano (the harpsichord's quills pluck; the clavichord's tangents push up against the strings and stay
// there); the first piano (Bartolomeo Cristofori, Florence, about 1700; pianoforte, 'soft-loud'); inside the piano (key,
// hammer, string, damper); the three pedals; grand and upright, 88 keys from the lowest A to the highest C. The eras and how
// the piano grew stay in the toolbox (the timeline and the eras) and the drill's extra level. Facts: the Met's Cristofori
// essay (an inventory of 1700; Florence; the name in Maffei's 1711 article); the clavichord's tangent strikes the string and
// stays on it while the key is held; the soft pedal shifts a grand's hammers to fewer strings (on an upright it moves them
// closer); 88 keys became the standard in the late 1880s (52 white, 36 black).
// It builds on chapter 10 (p and f) and chapter 12 (long, thick strings sound low; the 88 keys).

const SPS_SW = { stroke: PEN_N, strokeWidth: 1.8, strokeLinecap: 'round', strokeLinejoin: 'round', fill: 'none' };
const SPS_SWF = { ...SPS_SW, fill: '#fff' };
const spsTx = (x, y, s, o = {}) => <text x={x} y={y} textAnchor={o.a || 'middle'} fontSize={o.size || 12} fontWeight={o.w || 900} fill={o.c || PEN_N} paintOrder="stroke" stroke="#fff" strokeWidth={o.halo === false ? 0 : 4} strokeLinejoin="round">{s}</text>;
const spsNbKo = (x) => x.replace(/(\S) 수 있/g, '$1 수 있').replace(/양 끝/g, '양 끝');

// ── the instruments, side or front views in navy lines; cut: the strings shown inside, in coral ──
// a grand piano from the side: the keys on the left, the lid open (or closed), three legs (two seen), the pedals
function SpsGrand({ x = 0, y = 0, s = 1, cut, lidUp = true }) {
  return <g transform={'translate(' + x + ' ' + y + ') scale(' + s + ')'}>
    {lidUp ? <><path d="M26 50 L182 14 L186 20 L34 54 Z" {...SPS_SWF}/><line x1="150" y1="54" x2="160" y2="24" {...SPS_SW} strokeWidth="1.5"/></> : <path d="M20 48 L176 48 Q196 48 196 52 L20 52 Z" {...SPS_SWF} strokeWidth="1.5"/>}
    <path d="M18 52 L176 52 Q198 52 198 64 L198 72 L18 72 Z" {...SPS_SWF}/>
    <rect x="2" y="56" width="18" height="7" rx="1" {...SPS_SWF} strokeWidth="1.4"/>{[5, 10, 15].map(k => <rect key={k} x={k} y="53.5" width="2.6" height="3" fill={PEN_N}/>)}
    {cut && [57, 61, 65, 69].map((yy, i) => <line key={yy} x1={26 + i * 3} x2={194 - i * 4} y1={yy} y2={yy} stroke={PEN_C} strokeWidth="1.3"/>)}
    <path d="M26 72 L28 112 L34 112 L36 72" {...SPS_SWF} strokeWidth="1.5"/><path d="M180 72 L182 112 L188 112 L190 72" {...SPS_SWF} strokeWidth="1.5"/>
    <path d="M66 72 L70 104 M80 72 L76 104" {...SPS_SW} strokeWidth="1.4"/><rect x="64" y="104" width="18" height="4" rx="2" fill={PEN_N}/>
  </g>;
}
// an upright piano from the front: wider than tall; the strings standing up inside (cut) or a music desk; a key bed wider
// than the case; three small pedals
function SpsUpright({ x = 0, y = 0, s = 1, cut }) {
  const keys = [];
  for (let i = 0; i <= 22; i++) keys.push(<line key={'w' + i} x1={10 + i * 6.4} x2={10 + i * 6.4} y1="64" y2="76" stroke={PEN_N} strokeWidth="0.9"/>);
  [0, 1, 3, 4, 5, 7, 8, 10, 11, 12, 14, 15, 17, 18, 19, 21].forEach(i => keys.push(<rect key={'b' + i} x={13.6 + i * 6.4} y="64" width="3.6" height="7" fill={PEN_N}/>));
  return <g transform={'translate(' + x + ' ' + y + ') scale(' + s + ')'}>
    <rect x="4" y="2" width="152" height="6" rx="2" {...SPS_SWF} strokeWidth="1.5"/>
    <rect x="8" y="8" width="144" height="56" {...SPS_SWF}/>
    {cut ? Array.from({ length: 14 }, (_, i) => <line key={i} x1={20 + i * 9.4} x2={22 + i * 9} y1={14 + (i < 5 ? 0 : 4)} y2="58" stroke={PEN_C} strokeWidth={i < 5 ? 2 : 1.3}/>) : <rect x="44" y="26" width="72" height="18" rx="2" {...SPS_SW} strokeWidth="1.4"/>}
    <rect x="0" y="64" width="160" height="12" rx="1.5" {...SPS_SWF} strokeWidth="1.6"/>{keys}
    <rect x="8" y="76" width="144" height="38" {...SPS_SWF}/>
    <rect x="2" y="112" width="14" height="6" rx="1" fill={PEN_N}/><rect x="144" y="112" width="14" height="6" rx="1" fill={PEN_N}/>
    {[66, 80, 94].map(px => <rect key={px} x={px - 4} y="108" width="8" height="4" rx="2" fill={PEN_N}/>)}
  </g>;
}
// a harpsichord from the side: a thin case tapering to a straight tail, two stepped keyboards with navy naturals, a thin
// stand without pedals. one: one keyboard (Cristofori's piano looked like this)
function SpsHarpsichord({ x = 0, y = 0, s = 1, one }) {
  const manual = (mx, my) => <g><rect x={mx} y={my} width="22" height="7" rx="1" fill={PEN_N}/>{[4, 9, 14, 19].map(k => <rect key={k} x={mx + k - 1} y={my + 1} width="2" height="3" fill="#fff"/>)}</g>;
  return <g transform={'translate(' + x + ' ' + y + ') scale(' + s + ')'}>
    <path d="M28 54 L178 30 L181 35 L34 57 Z" {...SPS_SWF}/><line x1="140" y1="57" x2="146" y2="36" {...SPS_SW} strokeWidth="1.5"/>
    <path d="M22 56 L130 56 L198 64 L198 70 L22 70 Z" {...SPS_SWF}/>
    {one ? manual(2, 58) : <>{manual(6, 52)}{manual(1, 60)}</>}
    <path d="M32 70 L32 112 M190 70 L190 112 M32 94 L190 94" {...SPS_SW} strokeWidth="1.5"/>
  </g>;
}
// a clavichord from the front: a plain box, its lid up behind, the keys standing out at its front, on a table stand
function SpsClavichord({ x = 0, y = 0, s = 1 }) {
  const keys = [];
  for (let i = 0; i <= 14; i++) keys.push(<line key={'w' + i} x1={36 + i * 6} x2={36 + i * 6} y1="62" y2="76" stroke={PEN_N} strokeWidth="0.9"/>);
  [0, 1, 3, 4, 5, 7, 8, 10, 11, 12].forEach(i => keys.push(<rect key={'b' + i} x={38.8 + i * 6} y="62" width="3.4" height="8" fill={PEN_N}/>));
  return <g transform={'translate(' + x + ' ' + y + ') scale(' + s + ')'}>
    <path d="M22 48 L34 16 L184 16 L172 48" {...SPS_SWF} strokeWidth="1.5"/>
    <rect x="14" y="48" width="172" height="22" rx="2" {...SPS_SWF}/>
    <rect x="36" y="62" width="90" height="14" {...SPS_SWF} strokeWidth="1.3"/>{keys}
    <path d="M26 70 L26 112 M174 70 L174 112 M26 94 L174 94" {...SPS_SW} strokeWidth="1.5"/>
  </g>;
}

// ── how each sounds its string, close up: the string, the key (a lever on its rest, pressed at its front) and what the key
// moves. kind: 'pluck' (the harpsichord's jack and quill), 'press' (the clavichord's tangent: it pushes up against the string
// and stays), 'strike' (the piano's hammer). The moving part in coral when hl; w = 130, h = 100; label under it (or none) ──
function SpsMech({ kind, x = 0, y = 0, s = 1, label, hl = true }) {
  const C = hl ? PEN_C : PEN_N, up = (ax) => <path d={'M' + ax + ' 58 L' + ax + ' 40 M' + (ax - 5) + ' 45 L' + ax + ' 40 L' + (ax + 5) + ' 45'} {...SPS_SW} stroke={C} strokeWidth="1.8"/>;
  return <g transform={'translate(' + x + ' ' + y + ') scale(' + s + ')'}>
    <circle cx="10" cy="22" r="3.5" fill={PEN_N}/><circle cx="120" cy="22" r="3.5" fill={PEN_N}/>
    <path d={kind === 'pluck' ? 'M10 22 L56 17 L120 22' : 'M10 22 L120 22'} {...SPS_SW} strokeWidth="1.6"/>
    <rect x="8" y="78" width="114" height="8" rx="2" {...SPS_SWF} strokeWidth="1.5"/><path d="M52 86 L46 94 L58 94 Z" fill={PEN_N}/>
    <path d="M20 58 L20 72 M15 67 L20 72 L25 67" {...SPS_SW} stroke={PEN_N} strokeWidth="1.6"/>
    {kind === 'pluck' && <g><rect x="74" y="28" width="9" height="50" rx="1" {...SPS_SWF} strokeWidth="1.5"/><path d="M74 29 L55 18 L74 35 Z" fill={C}/>{up(96)}</g>}
    {kind === 'press' && <g><rect x="72" y="22" width="17" height="4" fill={C}/><rect x="78" y="26" width="5" height="52" fill={C}/>{up(98)}</g>}
    {kind === 'strike' && <g><line x1="108" y1="70" x2="82" y2="36" {...SPS_SW} strokeWidth="2.2"/><circle cx="108" cy="70" r="2.6" fill={PEN_N}/><rect x="66" y="24" width="20" height="14" rx="5" fill={C} stroke={PEN_N} strokeWidth="1.3"/></g>}
    {label && spsTx(65, 112, label, { size: 13, c: C })}
  </g>;
}

// ── inside the piano: one key's action, side view (a grand's). down: the key pressed (the damper off the string); ham:
// 'rest', 'strike' (at the string) or 'held' (fallen back while the key is held); show: 'words' (each part named), 'boxes' (a
// lettered box with a short line to each part), or nothing; hl: a part in coral (the hammer then white unless it is the one) ──
const SPS_PARTS = ['key', 'hammer', 'string', 'damper'];
const SPS_PART_W = { key: () => t('key', '건반'), hammer: () => t('hammer', '해머'), string: () => t('string', '현'), damper: () => t('damper', '댐퍼') };
function SpsAction({ down = false, ham, show = 'words', hl, letters = 'ABCD', size = 13, pedal = false, ring = false, arrow = true }) {
  const lift = down || pedal, hm = ham || (down ? 'held' : 'rest'), col = (p) => hl === p ? PEN_C : PEN_N, fillOf = (p) => hl === p ? '#fbd9cc' : '#fff';
  const boxes = show === 'boxes', H = boxes ? 210 : 196, dy = lift ? -16 : 0;
  const box = (p, bx, by, lx1, ly1, lx2, ly2) => <g><line x1={lx1} y1={ly1} x2={lx2} y2={ly2} stroke={PEN_N} strokeWidth="1.2"/><rect x={bx} y={by} width="34" height="28" rx="4" fill="#fff" stroke={PEN_N} strokeWidth="1.3"/>{spsTx(bx + 17, by + 19, letters[SPS_PARTS.indexOf(p)], { size: 14, c: BK.muted, halo: false })}</g>;
  return <svg viewBox={'0 0 340 ' + H} style={{width:'100%',display:'block'}}>
    {/* the string: a tuning pin on the left, the bridge on the right */}
    <circle cx="30" cy="62" r="5" fill={PEN_N}/><path d="M300 62 l10 10 h-20 Z" fill={PEN_N}/>
    <line x1="30" x2="300" y1="62" y2="62" stroke={hl === 'string' ? PEN_C : PEN_N} strokeWidth={hl === 'string' ? 3 : 2}/>
    {ring && <path d="M40 62 Q120 55 165 62 T290 62" fill="none" stroke={PEN_C} strokeWidth="1.4" opacity="0.8"/>}
    {/* the damper on its wire, resting on the string (off it when the key is down or the pedal is down) */}
    <g transform={lift ? 'translate(0 -16)' : undefined}>
      <line x1="126" x2="126" y1="18" y2="50" stroke={col('damper')} strokeWidth="2"/>
      <rect x="112" y="48" width="28" height="13" rx="2" fill={fillOf('damper')} stroke={col('damper')} strokeWidth="1.6"/>
    </g>
    {/* the hammer on its shank, pivoting at (246, 118) */}
    <g transform={hm === 'strike' ? 'rotate(20 246 118)' : hm === 'held' ? 'rotate(11 246 118)' : undefined}>
      <line x1="246" x2="176" y1="118" y2="100" stroke={col('hammer')} strokeWidth="2.8" strokeLinecap="round"/>
      <path d="M160 86 h24 a6 6 0 0 1 6 6 v12 h-36 v-12 a6 6 0 0 1 6 -6 Z" fill={hl === 'hammer' ? PEN_C : hl ? '#fff' : '#fbd9cc'} stroke={col('hammer')} strokeWidth="1.6"/>
      <circle cx="246" cy="118" r="3.6" fill={PEN_N}/>
    </g>
    {/* the rod from the back of the key up to the hammer's shank, and the key: a lever on its rest, pressed at its front */}
    <rect x="222" y={down ? 107 : 113} width="6" height="43" rx="2" fill={PEN_N}/>
    <g transform={down ? 'rotate(-4 160 168)' : undefined}>
      <rect x="18" y="156" width="270" height="12" rx="2" fill={fillOf('key')} stroke={col('key')} strokeWidth="1.8"/>
    </g>
    <path d="M160 168 l-7 10 h14 Z" fill={PEN_N}/>
    {arrow && !hl && <path d="M34 126 L34 146 M28 140 L34 146 L40 140" {...SPS_SW} stroke={PEN_C} strokeWidth="2"/>}
    {show === 'words' && <>{spsTx(36, 46, SPS_PART_W.string(), { a: 'start', size, c: col('string') })}{spsTx(148, 30, SPS_PART_W.damper(), { a: 'start', size, c: col('damper') })}{spsTx(146, 102, SPS_PART_W.hammer(), { a: 'end', size, c: col('hammer') })}{spsTx(54, 192, SPS_PART_W.key(), { a: 'start', size, c: col('key') })}</>}
    {boxes && <>{box('string', 40, 18, 57, 46, 57, 60)}{box('damper', 150, 4, 150, 18, 140, 48 + dy)}{box('hammer', 104, 110, 138, 116, hm === 'rest' ? 156 : 160, hm === 'rest' ? 104 : 88)}{box('key', 60, 178, 77, 178, 77, 170)}</>}
  </svg>;
}

// ── the three pedals, from the front: left (soft), middle, right (sustain); hl: one in coral; words: their names under them;
// side: left / right under the names; down: pedals pressed; onTap(p): each pedal a button ──
const SPS_PEDALS = ['soft', 'middle', 'sustain'];
const SPS_PEDAL_W = { soft: () => t('soft pedal', '소프트 페달'), middle: () => t('middle pedal', '가운데 페달'), sustain: () => t('sustain pedal', '댐퍼 페달') };
const SPS_PEDAL_S = { soft: () => t('soft', '소프트'), middle: () => t('middle', '가운데'), sustain: () => t('sustain', '댐퍼') };
function SpsPedals({ hl, words = true, down = [], size = 13, side = true, onTap, short }) {
  const xs = [66, 170, 274], H = words ? (side ? 162 + size * 1.25 : 158) : 136;
  return <svg viewBox={'0 0 340 ' + H} style={{width:'100%',display:'block',touchAction:'manipulation'}}>
    <rect x="30" y="2" width="280" height="12" rx="2" {...SPS_SWF} strokeWidth="1.6"/>
    <path d="M120 14 L124 74 Q126 86 140 88 L200 88 Q214 86 216 74 L220 14" {...SPS_SWF} strokeWidth="2"/>
    <path d="M148 14 L148 80 M170 14 L170 80 M192 14 L192 80" {...SPS_SW} strokeWidth="1.3"/>
    <rect x="40" y="88" width="260" height="14" rx="4" {...SPS_SWF}/>
    {SPS_PEDALS.map((p, i) => { const on = down.includes(p), c = hl === p || on ? PEN_C : PEN_N, x = xs[i];
      return <g key={p} onClick={onTap ? () => onTap(p) : undefined} style={{cursor:onTap ? 'pointer' : 'default'}}>
        {onTap && <rect x={x - 46} y="76" width="92" height="66" fill="transparent"/>}
        <g transform={on ? 'translate(0 5)' : undefined}><path d={'M' + (x - 7) + ' 98 L' + (x - 12) + ' 126 Q' + x + ' 134 ' + (x + 12) + ' 126 L' + (x + 7) + ' 98 Z'} fill={hl === p || on ? PEN_C : '#fff'} stroke={c} strokeWidth="1.8" strokeLinejoin="round"/></g>
        {words && spsTx(x, 156, (short ? SPS_PEDAL_S : SPS_PEDAL_W)[p](), { size, c })}
        {words && side && i !== 1 && spsTx(x, 156 + size * 1.25, i === 0 ? t('left', '왼쪽') : t('right', '오른쪽'), { size: size - 1.5, w: 700, c: BK.muted })}
      </g>; })}
  </svg>;
}

// ── the timeline, running down: the harpsichord and clavichord (about 1400), Cristofori's piano in Florence (about 1700:
// harpsichord-shaped, soft and loud), 88 keys (late 1800s) ──
function SpsTimeline({ scr }) {
  const ys = [62, 196, 330], lx = scr ? 214 : 270, s = scr ? 0.95 : 1.15, dS = scr ? 25 : 20, wS = scr ? 19 : 15.5, fs = scr ? 1.2 : 1;
  return <svg viewBox="0 0 560 400" style={{width:'100%',display:'block'}} role="img" aria-label={t('A timeline running down. About 1400: the harpsichord and the clavichord. About 1700, in Florence: Cristofori builds the first piano, shaped like a harpsichord; beside it a hairpin from p to f: soft and loud. The late 1800s: the grand piano with 88 keys.', '위에서 아래로 가는 연표. 1400년쯤: 하프시코드와 클라비코드. 1700년쯤 피렌체: 크리스토포리가 하프시코드 모양의 최초의 피아노를 만들었어요. 그 옆에 p에서 f로 점점 세게. 1800년대 후반: 88건반 그랜드 피아노.')}>
    <line x1={lx} x2={lx} y1="30" y2="370" stroke={PEN_N} strokeWidth="2"/>
    <SpsHarpsichord x={4} y={ys[0] - 62 * s / 1.15} s={s}/>
    <SpsHarpsichord x={4} y={ys[1] - 62 * s / 1.15} s={s} one/>
    <SpsGrand x={4} y={ys[2] - 62 * s / 1.15} s={s} cut/>
    {[[t('about 1400', '1400년쯤'), t('the harpsichord, the clavichord', '하프시코드, 클라비코드')], [t('about 1700', '1700년쯤'), t('Cristofori, Florence', '크리스토포리, 피렌체')], [t('late 1800s', '1800년대 후반'), t('88 keys', '88건반')]].map(([y, w], i) =>
      <g key={i}><circle cx={lx} cy={ys[i]} r={i === 1 ? 9 : 7} fill={i === 1 ? PEN_C : '#fff'} stroke={i === 1 ? PEN_C : PEN_N} strokeWidth="2"/>
        {spsTx(lx + 20, ys[i] - 2, y, { a: 'start', size: dS, c: i === 1 ? PEN_C : PEN_N })}{spsTx(lx + 20, ys[i] + 26, w, { a: 'start', size: wS, w: 700 })}</g>)}
    <text x={lx + 20} y={ys[1] + 62} fontFamily={MUSIC_FONT} fontStyle="italic" fontWeight="700" fontSize={24 * fs} fill={PEN_N}>p</text>
    <path d={'M' + (lx + 44) + ' ' + (ys[1] + 54) + ' L' + (lx + 138) + ' ' + (ys[1] + 44) + ' M' + (lx + 44) + ' ' + (ys[1] + 54) + ' L' + (lx + 138) + ' ' + (ys[1] + 64)} {...SPS_SW} stroke={PEN_C} strokeWidth="2"/>
    <text x={lx + 148} y={ys[1] + 62} fontFamily={MUSIC_FONT} fontStyle="italic" fontWeight="700" fontSize={24 * fs} fill={PEN_N}>f</text>
  </svg>;
}
// the 88 keys with the lowest A and the highest C filled coral
const spsKeysEnds = (x0, y0, kw = 10, h = 46) => <g><SprKeys88 x0={x0} y0={y0} kw={kw} h={h} middleC={false} sw={0.8}/><rect x={x0} y={y0} width={kw} height={h} fill={PEN_C} stroke={PEN_N} strokeWidth="0.8"/><rect x={x0 + 51 * kw} y={y0} width={kw} height={h} fill={PEN_C} stroke={PEN_N} strokeWidth="0.8"/></g>;

function spsLbPages(scr = false) {
  const ch = 'piano-story', X = (en, ko) => sscT(en, spsNbKo(ko)), fs = scr ? 1.3 : 1;
  const live = (still, comp) => <LbLive still={still} live={comp}/>;
  const pic = (node, h = 230, mw = 600) => <LbPic h={h}><div style={{width:'100%',maxWidth:mw,margin:'0 auto'}}>{node}</div></LbPic>;
  const svg = (vb, kids, label) => <svg viewBox={vb} style={{width:'100%',display:'block'}} role="img" aria-label={label}>{kids}</svg>;

  // 1. a grand piano, its strings shown inside
  const p1 = svg('0 0 220 124', <SpsGrand x={10} y={2} cut/>, t('A grand piano from the side, its lid open, the strings inside it drawn in coral.', '옆에서 본 그랜드 피아노, 뚜껑이 열려 있고 안의 현은 산호색.'));
  // 2. the harpsichord and the clavichord, each over its string and key: a quill plucks, a tangent pushes and stays
  const p2 = svg('0 0 520 332', <>
    <SpsHarpsichord x={0} y={0} s={1.25}/><SpsClavichord x={262} y={4} s={1.25}/>
    {spsTx(128, 162, t('harpsichord', '하프시코드'), { size: 15 * fs })}{spsTx(384, 162, t('clavichord', '클라비코드'), { size: 15 * fs })}
    <SpsMech kind="pluck" x={37} y={172} s={1.4} label={t('a quill plucks', '깃촉이 뜯어요')}/><SpsMech kind="press" x={293} y={172} s={1.4} label={t('a tangent pushes and stays', '탄젠트가 밀고 머물러요')}/>
  </>, t('A harpsichord and a clavichord. Under each, its string and key drawn large: in the harpsichord a quill on a jack plucks the string; in the clavichord a brass tangent pushes up against the string and stays there while the key is held.', '하프시코드와 클라비코드. 각 악기 아래에 현과 건반을 크게 그렸어요. 하프시코드는 잭에 달린 깃촉이 현을 뜯고, 클라비코드는 놋쇠 조각인 탄젠트가 현을 밀어 올린 채 건반을 누르는 동안 머물러요.'));
  // 3. the timeline
  const p3 = <SpsTimeline scr={scr}/>;
  // 4. the action, each part named
  const p4 = <div role="img" aria-label={t('Inside a grand piano, one key from the side: the key is a lever, pressed at its front; at its back a rod sends the felt hammer up to the string; above the string a felt damper rests on it.', '그랜드 피아노 속, 건반 하나를 옆에서: 건반은 앞을 누르는 지렛대예요. 건반 뒤쪽의 막대가 펠트 해머를 현으로 보내요. 현 위에는 펠트 댐퍼가 얹혀 있어요.')}><SpsAction show="words" size={13 * fs}/></div>;
  // 5. the pedals
  const p5 = <div role="img" aria-label={t('The three pedals from the front: on the left the soft pedal, in the middle the middle pedal, on the right the sustain pedal.', '앞에서 본 페달 세 개: 왼쪽은 소프트 페달, 가운데는 가운데 페달, 오른쪽은 댐퍼 페달.')}><SpsPedals size={14 * fs}/></div>;
  // 6. grand and upright, strings inside; the 88 keys with their two ends
  const p6 = svg('0 0 560 330', <>
    <SpsGrand x={4} y={4} s={1.3} cut/><SpsUpright x={312} y={2} s={1.45} cut/>
    {spsTx(134, 197, t('grand: strings lie flat', '그랜드: 현이 누워 있어요'), { size: 13.5 * fs })}{spsTx(428, 197, t('upright: strings stand up', '업라이트: 현이 서 있어요'), { size: 13.5 * fs })}
    {spsKeysEnds(20, 214)}
    {spsTx(22, 280, t('lowest A', '가장 낮은 A'), { a: 'start', size: 13 * fs, c: PEN_C })}{spsTx(538, 280, t('highest C', '가장 높은 C'), { a: 'end', size: 13 * fs, c: PEN_C })}
    {spsTx(280, 312, t('88 keys: 52 white, 36 black', '88건반: 흰건반 52, 검은건반 36'), { size: 13.5 * fs })}
  </>, t('A grand piano from the side, its strings lying flat inside; an upright from the front, its strings standing up inside. Under them, the 88 keys with the lowest A and the highest C in coral.', '옆에서 본 그랜드 피아노, 안의 현이 누워 있어요. 앞에서 본 업라이트, 안의 현이 서 있어요. 그 아래 88건반, 가장 낮은 A와 가장 높은 C는 산호색.'));

  // the check icons
  const ic = {
    before: [{ k: 'raw', svg: '<path d="M6 12 L28 8 L86 12" stroke="' + PEN_N + '" stroke-width="1.6" fill="none"/><rect x="34" y="14" width="7" height="22" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.4"/><path d="M34 14 L26 8 L34 20 Z" fill="' + PEN_C + '"/><rect x="62" y="12" width="12" height="3" fill="' + PEN_C + '"/><rect x="66" y="15" width="4" height="21" fill="' + PEN_C + '"/>' }],
    first: [{ k: 'raw', svg: '<text x="12" y="31" font-family="' + MUSIC_FONT + '" font-style="italic" font-weight="700" font-size="22" fill="' + PEN_N + '">p</text><path d="M34 24 L60 16 M34 24 L60 32" stroke="' + PEN_C + '" stroke-width="1.8" fill="none"/><text x="68" y="31" font-family="' + MUSIC_FONT + '" font-style="italic" font-weight="700" font-size="22" fill="' + PEN_N + '">f</text>' }],
    inside: [{ k: 'raw', svg: '<line x1="6" x2="86" y1="10" y2="10" stroke="' + PEN_N + '" stroke-width="1.6"/><rect x="20" y="2" width="14" height="7" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.3"/><rect x="50" y="12" width="14" height="9" rx="3" fill="' + PEN_C + '"/><line x1="64" y1="18" x2="80" y2="26" stroke="' + PEN_N + '" stroke-width="2"/><rect x="6" y="30" width="80" height="6" rx="2" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.4"/>' }],
    pedals: [{ k: 'raw', svg: [24, 46, 68].map((x, i) => '<path d="M' + (x - 4) + ' 10 L' + (x - 8) + ' 30 Q' + x + ' 35 ' + (x + 8) + ' 30 L' + (x + 4) + ' 10 Z" fill="' + (i === 2 ? PEN_C : '#fff') + '" stroke="' + (i === 2 ? PEN_C : PEN_N) + '" stroke-width="1.5"/>').join('') }],
    kinds: [{ k: 'raw', svg: '<path d="M4 22 L50 22 Q58 22 58 27 L58 30 L4 30 Z" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.5"/><path d="M8 21 L52 9" stroke="' + PEN_N + '" stroke-width="1.5"/><rect x="64" y="8" width="24" height="12" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.4"/><rect x="62" y="20" width="28" height="4" fill="#fff" stroke="' + PEN_C + '" stroke-width="1.4"/><rect x="64" y="24" width="24" height="10" fill="#fff" stroke="' + PEN_N + '" stroke-width="1.4"/>' }],
  };
  const checksRows = [
    ['before', t('I can say how the harpsichord and the clavichord sound their strings', '하프시코드와 클라비코드가 현을 울리는 방법을 말할 수 있어요')],
    ['first', t('I can say who built the first piano, where and when, and what its name means', '최초의 피아노를 누가, 어디서, 언제 만들었는지, 그 이름이 무슨 뜻인지 말할 수 있어요')],
    ['inside', t('I can name the key, the hammer, the string and the damper, and say what each does', '건반, 해머, 현, 댐퍼의 이름과 하는 일을 말할 수 있어요')],
    ['pedals', t('I can say what each of the three pedals does', '페달 세 개가 각각 하는 일을 말할 수 있어요')],
    ['kinds', t('I can tell a grand from an upright and play both ends of the 88 keys', '그랜드와 업라이트를 구별하고 88건반의 양 끝을 칠 수 있어요')],
  ].map(([a, x]) => [a, LANG === 'ko' ? spsNbKo(sscNbKo(x)) : sscNbEn(x)]);

  return [
    <LbPage key="1" no={1} chId={ch}>
      <LbOnly print><div data-ch={ch}>
        <div style={{fontSize:13,fontWeight:900,color:BK.coral,letterSpacing:'0.12em'}}>CHAPTER {bkChapterNo(ch)}</div>
        <div style={{fontFamily:LB_SERIF,fontSize:44,fontWeight:900,color:BK.ink,lineHeight:1.02,margin:'4px 0 0'}}>{bkChapterName(ch)}</div>
      </div></LbOnly>
      {pic(p1, 210, 640)}
      <LbSay size={17.5}>{LANG === 'ko' ? <><b>피아노</b>는 해머가 현을 치는 건반 악기예요. 1700년쯤 처음 만들어졌어요.</> : <>The <b>piano</b> is a keyboard instrument whose hammers strike its strings. It was invented about 1700.</>}</LbSay>
      <div className="lb-toc" style={{display:'grid',gridTemplateColumns:scr ? '1fr' : '1fr 1fr',gap:20}}>
        <LbOnly print><div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('In this chapter', '이 챕터에서는')}</div>
          {[[t('Before the piano', '피아노 이전'), 2], [t('The first piano', '최초의 피아노'), 3], [t('Inside the piano', '피아노 속'), 4], [t('The pedals', '페달'), 5], [t('Grand and upright', '그랜드와 업라이트'), 6], [t('My five checks', '나의 다섯 가지 확인'), 7]].map(([n, p]) => <div key={p} className="lb-toc-row" style={{display:'flex',justifyContent:'space-between',alignItems:'center',fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}><span style={{display:'flex',alignItems:'center',gap:9}}>{bkGoal(15)}{n}</span><span style={{color:BK.muted,fontWeight:800}}>{p}</span></div>)}
        </div></LbOnly>
        <div>
          <div className="lb-toc-h" style={{fontFamily:LB_SERIF,fontSize:20,fontWeight:800,marginBottom:6}}>{t('By the end, you can', '이 챕터를 마치면')}</div>
          {checksRows.map(([, x], i) => <div key={i} style={{display:'flex',gap:9,fontSize:14.5,padding:'4px 0',borderBottom:'1px solid rgba(38,41,107,0.16)'}}>{bkGoal(15)}<span>{x.replace(/^I can /, '')}</span></div>)}
        </div>
      </div>
      <LbOnly print><LbDrillStrip id={ch}/></LbOnly>
    </LbPage>,

    <LbPage key="2" no={2} chId={ch} kicker={t('Step 1', '1단계')} title={t('Before the piano', '피아노 이전')}>
      {live(pic(p2, 300, 660), <SpsPad page={2}/>)}
      <LbDefs items={[
        [t('harpsichord', '하프시코드'), X('A keyboard instrument whose strings are plucked by quills. Pressing harder does not make it louder.', '깃촉이 현을 뜯는 건반 악기예요. 세게 눌러도 소리가 커지지 않아요.')],
        [t('clavichord', '클라비코드'), X('A small keyboard instrument whose brass tangents push up against its strings and stay there while you hold the key. It plays soft and loud, but always quietly.', '탄젠트라는 놋쇠 조각이 현을 밀어 올린 채, 건반을 누르는 동안 머무는 작은 건반 악기예요. 세게 누르면 소리가 커지지만, 늘 작은 소리예요.')],
      ]}/>
      <LbPiano steps={[
        X('Play C D E F G all at one loudness, like a harpsichord.', '하프시코드처럼 C D E F G를 모두 같은 세기로 쳐요.'),
        X('Play it again, soft, then loud: a harpsichord cannot do that by touch.', '다시 여리게, 그다음 세게 쳐요. 하프시코드는 누르는 힘으로는 못 하는 일이에요.'),
      ]}/>
      <LbRemember>{X('A quill plucks; a tangent pushes and stays.', '깃촉은 뜯고, 탄젠트는 밀어 올린 채 머물러요.')}</LbRemember>
    </LbPage>,

    <LbPage key="3" no={3} chId={ch} kicker={t('Step 2', '2단계')} title={t('The first piano', '최초의 피아노')}>
      {live(pic(p3, 300, 560), <SpsPad page={3}/>)}
      <LbDefs items={[
        [t('Cristofori', '크리스토포리'), X('Bartolomeo Cristofori: an Italian instrument maker. He built the first piano in Florence, about 1700.', '바르톨로메오 크리스토포리: 이탈리아의 악기 제작자. 1700년쯤 피렌체에서 최초의 피아노를 만들었어요.')],
        [t('pianoforte', '피아노포르테'), X('Italian for “soft-loud”: it plays soft or loud by how hard you press. Its short name is piano.', '이탈리아 말로 “여리게-세게”라는 뜻이에요. 누르는 힘에 따라 여리게도 세게도 소리가 나요. 줄여서 피아노라고 해요.')],
      ]}/>
      <LbPiano steps={[
        X('Play middle C as softly as you can, then as loudly as you can: piano, then forte.', '가운데 도를 가장 여리게, 그다음 가장 세게 쳐요: 피아노, 그다음 포르테.'),
        X('Play C D E F G getting louder, from p to f.', 'C D E F G를 p에서 f까지 점점 세게 쳐요.'),
      ]}/>
      <LbRemember>{X('Pianoforte: soft and loud.', '피아노포르테: 여리게도, 세게도.')}</LbRemember>
    </LbPage>,

    <LbPage key="4" no={4} chId={ch} kicker={t('Step 3', '3단계')} title={t('Inside the piano', '피아노 속')}>
      {live(pic(p4, 270, 680), <SpsPad page={4}/>)}
      <LbDefs items={[
        [t('key', '건반'), X('A lever: press its front, and its back sends the hammer to the string.', '지렛대. 앞을 누르면 뒤쪽이 해머를 현으로 보내요.')],
        [t('hammer', '해머'), X('A small wooden hammer covered in felt. It strikes the string and comes straight back.', '펠트를 씌운 작은 나무 망치. 현을 치고 곧바로 되돌아와요.')],
        [t('string', '현'), X('A steel wire pulled tight. Low notes have long, thick strings; high notes short, thin ones.', '팽팽하게 당긴 강철 줄. 낮은 음은 길고 굵은 현, 높은 음은 짧고 가는 현이에요.')],
        [t('damper', '댐퍼'), X('A felt pad resting on the string. It moves off when you press the key and stops the sound when you let go.', '현에 얹힌 펠트 조각. 건반을 누르면 현에서 떨어지고, 손을 떼면 다시 닿아 소리를 멈춰요.')],
      ]}/>
      <LbPiano steps={[
        X('On an acoustic piano, press a key so slowly that it makes no sound: the hammer never reaches the string.', '어쿠스틱 피아노에서 건반을 소리가 나지 않을 만큼 아주 천천히 눌러요: 해머가 현까지 가지 못해요.'),
        X('Play a key and hold it. Then let go: the damper stops the sound.', '건반을 하나 치고 그대로 누르고 있어요. 그다음 손을 떼요: 댐퍼가 소리를 멈춰요.'),
      ]}/>
      <LbRemember>{X('The hammer strikes the string; the damper stops the sound.', '해머는 현을 치고, 댐퍼는 소리를 멈춰요.')}</LbRemember>
    </LbPage>,

    <LbPage key="5" no={5} chId={ch} kicker={t('Step 4', '4단계')} title={t('The pedals', '페달')}>
      {live(pic(p5, 240, 600), <SpsPad page={5}/>)}
      <LbDefs items={[
        [t('sustain pedal', '댐퍼 페달'), X('The right pedal. It moves every damper off its string, so the notes keep sounding after you let go. Its other name is the damper pedal.', '오른쪽 페달. 댐퍼를 모두 현에서 떼어서, 손을 떼도 소리가 계속 나요. 다른 이름은 서스테인 페달이에요.')],
        [t('soft pedal', '소프트 페달'), X('The left pedal. It makes each note a little softer. Its other name is una corda.', '왼쪽 페달. 음을 조금 더 여리게 해요. 다른 이름은 우나 코르다예요.')],
        [t('middle pedal', '가운데 페달'), X('On most grands, it keeps sounding only the notes you are holding when you press it. On most uprights, it makes the piano very quiet for practice.', '그랜드에서는 대개, 밟을 때 누르고 있던 음만 계속 울리게 해요. 업라이트에서는 대개 연습용으로 소리를 아주 작게 해요.')],
      ]}/>
      <LbPiano steps={[
        X('Play C E G and press the right pedal. Let go of the keys: the notes keep sounding. Lift the pedal: silence.', 'C E G를 치고 오른쪽 페달을 밟아요. 건반에서 손을 떼요: 소리가 계속 나요. 페달을 떼요: 조용해져요.'),
        X('Play C D E F G softly, then again with the left pedal down.', 'C D E F G를 여리게 쳐요. 그다음 왼쪽 페달을 밟고 다시 쳐요.'),
      ]}/>
      <LbRemember>{X('The right pedal keeps the sound; the left pedal softens it.', '오른쪽 페달은 소리를 이어 주고, 왼쪽 페달은 여리게 해요.')}</LbRemember>
    </LbPage>,

    <LbPage key="6" no={6} chId={ch} kicker={t('Step 5', '5단계')} title={t('Grand and upright', '그랜드와 업라이트')}>
      {live(pic(p6, 300, 680), <SpsPad page={6}/>)}
      <LbDefs items={[
        [t('grand piano', '그랜드 피아노'), X('A piano whose strings lie flat. Its lid opens like a wing.', '현이 누워 있는 피아노. 뚜껑이 날개처럼 열려요.')],
        [t('upright piano', '업라이트 피아노'), X('A piano whose strings stand up in a tall case. It fits against a wall.', '현이 키 큰 상자 안에 서 있는 피아노. 벽에 붙여 놓을 수 있어요.')],
        [t('88 keys', '88건반'), X('52 white and 36 black, from the lowest A to the highest C. 88 keys became the standard in the late 1800s.', '흰건반 52개와 검은건반 36개, 가장 낮은 A부터 가장 높은 C까지. 피아노는 1800년대 후반부터 88건반이 표준이에요.')],
      ]}/>
      <LbPiano steps={[
        X('On an 88-key piano, play the lowest key, an A, and the highest key, a C.', '88건반 피아노에서 가장 낮은 건반 A와 가장 높은 건반 C를 쳐요.'),
        X('Play every C from the bottom to the top and count them: eight.', '맨 아래부터 맨 위까지 C를 모두 치며 세어요: 여덟 개.'),
      ]}/>
      <LbRemember>{X('88 keys, from A to C.', '88건반, A부터 C까지.')}</LbRemember>
    </LbPage>,

    <LbPage key="7" no={7} chId={ch} kicker={t('Check-up', '점검')} title={t('My five checks', '나의 다섯 가지 확인')}>
      <LbSay>{t('Show each one at the piano, on its page (2 to 6). The check-up on paper is in the Workbook.', '2~6쪽을 하나씩 펴고 피아노 앞에서 보여 줘요. 종이 점검은 워크북에 있어요.')}</LbSay>
      <LbLive still={<LbStageRows big rows={checksRows.map(([a, x]) => [<PenArt shapes={ic[a]} vb={[0, 0, 92, 40]} style={{width:96}}/>, x])}/>} live={<FiveChecks376 storeKey="pb_five_sps_v1" rows={checksRows.map(([a, x]) => [{ shapes: ic[a], vb: [0, 0, 92, 40] }, x])}/>}/>
    </LbPage>,
  ];
}
function PianoStoryLessonBook() { return <>{spsLbPages(false)}</>; }
