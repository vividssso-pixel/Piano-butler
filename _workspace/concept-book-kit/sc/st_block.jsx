
// ─── Keys and staff on Home (her call 2026-10-21: "1, 2, 3, in order"). The old concept is split like the chapters into six concepts:
// p-keys, p-names, p-stf, p-lines, p-ledger, p-range. Each lesson re-hangs one of her existing tools (the book's own moving parts) under a title and one line,
// and the Queen's and King's five get a new lesson (the chapter had only a picture). Lines are her wording (tool blurbs and Learn text); the Korean is mine.
function KsBox({ en, ko, lEn, lKo, children }) {
  return scBox('st', <>
    <div style={scS.title}>{t(en, ko)}</div>
    {(lEn || lKo) && <div style={{ ...scS.line, minHeight: 0 }}>{t(lEn, lKo)}</div>}
    {children}
  </>);
}
const ksL = (en, ko, lEn, lKo, node) => () => <KsBox en={en} ko={ko} lEn={lEn} lKo={lKo}>{node}</KsBox>;
// the Queen's five (treble) and the King's five (bass): one note at a time on the staff and on the keys
function KsFive({ clef }) {
  const bass = clef === 'bass', [i, setI] = useState(0), P = useScPlay([clef]);
  const d0 = bass ? 24 : 28, N = bass ? ['F', 'G', 'A', 'B', 'C'] : ['C', 'D', 'E', 'F', 'G'], sh = bass ? 12 : 0, K = bass ? [5, 7, 9, 11, 12] : [0, 2, 4, 5, 7];
  const where = bass ? [t('on the King’s line', '왕의 줄'), t('in the space above', '그 위 칸'), t('on the top line', '맨 윗줄'), t('above the top line', '맨 윗줄 위'), t('on Clara’s little ladder', '클라라의 작은 사다리 발판')]
    : [t('on Clara’s little ladder', '클라라의 작은 사다리 발판'), t('under line 1', '1번 줄 아래'), t('on line 1', '1번 줄'), t('in space 1', '1번 칸'), t('on the Queen’s line', '여왕의 줄')];
  const items = N.map((_, j) => ['q', 1, d0 + j]).concat([['||']]), marks = {}, names = {};
  K.forEach((k, j) => { marks[k] = j === i ? 'pick' : 'pass'; names[k] = N[j]; });
  const say = (j) => { setI(j); playKey(K[j] - sh, 0.6); };
  return scBox('st', <>
    <div style={scS.title}>{bass ? t('The King’s five', '왕의 다섯 음') : t('The Queen’s five', '여왕의 다섯 음')}</div>
    <div style={scS.line}>{bass ? t('The bass clef is the King’s: his house is the 4th line, F. From the King’s F to Clara: F G A B C.', '낮은음자리표는 왕의 것이에요: 왕의 집은 4번째 줄, F예요. 왕의 F에서 클라라까지: F G A B C.')
      : t('The treble clef is the Queen’s: her house is the 2nd line, G. From Clara (middle C) to the Queen’s G: C D E F G.', '높은음자리표는 여왕의 것이에요: 여왕의 집은 2번째 줄, G예요. 클라라(가운데 도)에서 여왕의 G까지: C D E F G.')}</div>
    <div style={{ textAlign: 'center', fontSize: 15, fontWeight: 900, color: '#c0431f', margin: '2px 0 4px' }}>{N[i]} {where[i]}</div>
    <div style={{ maxWidth: 330, margin: '0 auto' }}><SkgStaff items={items} k="C" clef={clef} width={330} o={{ boxS: 26, D: 30, ring: [i], ...skgUnder(items, 'C', null, []) }}/></div>
    <ScKeys ks={K} marks={marks} names={names} arcs={[]} nonce={clef + i} onTap={(k) => { const j = K.indexOf(k); if (j >= 0) say(j); }}/>
    {scRow(<>
      <button className="ghost-btn" style={scS.back} disabled={i === 0} onClick={() => say(Math.max(0, i - 1))}>{t('← Back', '← 이전')}</button>
      <button className="ghost-btn" style={scS.back} onClick={() => P.play(K.map(k => k - sh))}>{t('▶ Hear the five', '▶ 다섯 음 듣기')}</button>
      <button className="ghost-btn" style={scS.prim} disabled={i === 4} onClick={() => say(Math.min(4, i + 1))}>{t('Next →', '다음 →')}</button>
    </>)}
  </>);
}
