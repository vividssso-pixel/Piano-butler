# Build BG (2026-10-27): before the whole passage by ear (her 15:04: "four bars heard at once is hard to catch;
# how do we fill the gap before it?"). Every clap-back pad in a Lesson Book (Grades 1, 2-3, 4 and 5) now starts with
# one bar at a time, then two, then all four (the test: heard twice, then the metre). One bar or two is heard once and
# echoed at once; the notes are shown at first (Grade 1 with her walk and run-ning under them: walk = a crotchet,
# run-ning = two quavers; a minim 'hold', the app's word since Listen, Clap, Write), and can be hidden. After a try
# at all four, only the bar that went wrong is offered again. The drills and Home lessons stay as the test is.
# The longer tune of Hear and Sing Further gets the same: the first half, the second half, then the whole tune.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:90])
    s = s.replace(old, new)

def rep_in(fn, pairs):
    global s
    a = s.index(fn); b = s.index('\n}\n', a) + 3
    body = s[a:b]
    for old, new in pairs:
        c = body.count(old)
        assert c == 1, (fn, c, old[:90])
        body = body.replace(old, new)
    s = s[:a] + body + s[b:]

HELPERS = r'''
// ══ Build BG: one bar, two bars, then all four (her 15:04) ══
// The bars of a passage, a run of them as a passage of its own, walk / run-ning under a Grade 1 line, and the
// bars a try missed. useEcho keeps which run of bars a pad is on; off (the drills, the Home) it is the whole passage.
const ecBars = (items) => { const out = [[]]; items.forEach(it => { if (it[0] === 'ts' || it[0] === '||') return; if (it[0] === '|') out.push([]); else out[out.length - 1].push(it); }); return out.filter(b => b.length); };
const ecSlice = (items, a, b) => { const ts = items.find(it => it[0] === 'ts'), out = ts ? [ts] : []; ecBars(items).slice(a, b).forEach((bar, k) => { if (k) out.push(['|']); out.push(...bar); }); out.push(['||']); return out; };
const EC_SAY = ['q', 'p', 'h', 'hd'];
const ecSay = (items) => (items.every(it => ['ts', '|', '||'].includes(it[0]) || EC_SAY.includes(it[0]))
  ? srhSounds(items).map(x => (x.rest ? null : x.d >= 2 ? t('hold', '길게') : x.d === 1 ? t('walk', '타') : Math.abs(x.b % 1) < 1e-6 ? t('run-', '티') : t('ning', '티'))) : null);
const ecWords = (E) => { const w = ecSay(E.sub); return w ? { words: w, counts: false } : {}; };
function useEcho(items, on) {
  const nb = ecBars(items).length;
  const [rung, setRung] = useState(on ? 1 : nb), [part, setPart] = useState(0), [see, setSee] = useState(true);
  const span = Math.min(rung, nb), parts = Math.ceil(nb / span), p = Math.min(part, parts - 1), a = p * span, full = span >= nb;
  const set = (r, q = 0, sh) => { setRung(r); setPart(q); setSee(sh != null ? sh : true); };
  return { on, nb, rung: span, part: p, parts, a, full, see, setSee, set, sub: full ? items : ecSlice(items, a, a + span) };
}
const ecMiss = (E, res) => { if (!res || !res.marks) return []; const top = srhTop(E.sub), out = new Set(); srhSounds(E.sub).forEach((x, j) => { if (res.marks[j] === '?') out.add(Math.floor(x.b / top + 1e-6)); }); return [...out].sort((a, b) => a - b); };
const ecRow = (E, change) => !E.on ? null : <div data-ec="rungs" style={{margin:'0 0 4px'}}>
  <div style={{textAlign:'center',fontSize:12.5,fontWeight:800,color:BK.muted,margin:'2px 0 0'}}>{t('One bar, then two, then all ' + E.nb + '.', '한 마디, 두 마디, 그다음 ' + E.nb + '마디 전부.')}</div>
  {spChips([[1, t('1 bar', '한 마디')], [2, t('2 bars', '두 마디')], [E.nb, t('All ' + E.nb + ', like the test', E.nb + '마디 전부, 시험처럼')]], E.rung, (r) => change(() => E.set(r)))}
  {!E.full && <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',alignItems:'center'}}>
    {spChips(Array.from({ length: E.parts }, (_, q) => [q, E.rung === 1 ? t('Bar ' + (q + 1), (q + 1) + '마디') : t('Bars ' + (q * E.rung + 1) + '–' + (q * E.rung + E.rung), (q * E.rung + 1) + '–' + (q * E.rung + E.rung) + '마디')]), E.part, (q) => change(() => E.set(E.rung, q, E.see)))}
    <button className="ghost-btn" style={{...spBtn,padding:'6px 12px',fontSize:13}} onClick={() => E.setSee(!E.see)}>{E.see ? t('Hide the notes', '음표 가리기') : t('Show the notes', '음표 보기')}</button></div>}
</div>;
const ecNext = (E, res, change) => { if (!E.on || !res) return null;
  if (!E.full) { const last = E.part >= E.parts - 1;
    return <button className="ghost-btn" style={spBtn} onClick={() => change(() => (last ? E.set(E.rung === 1 && E.nb > 2 ? 2 : E.nb, 0, E.rung === 1 && E.nb > 2 ? E.see : false) : E.set(E.rung, E.part + 1, E.see)))}>{last ? (E.rung === 1 && E.nb > 2 ? t('▶ Now two bars', '▶ 이제 두 마디') : t('▶ Now all ' + E.nb, '▶ 이제 ' + E.nb + '마디 전부')) : (E.rung === 1 ? t('▶ Next bar', '▶ 다음 마디') : t('▶ The next two', '▶ 다음 두 마디'))}</button>; }
  return <>{ecMiss(E, res).map(b => <button key={b} className="ghost-btn" style={spBtn} onClick={() => change(() => E.set(1, b, true))}>{t('▶ Bar ' + (b + 1) + ' again', '▶ ' + (b + 1) + '마디 다시')}</button>)}</>; };
'''
rep("// ── step 3: clap it back: a passage in two or three, heard twice, then tapped; the notes show only afterwards ──",
    HELPERS + "\n// ── step 3: clap it back: a passage in two or three, heard twice, then tapped; the notes show only afterwards ──")

# ── Grade 1: Listen, Clap, Write ──
rep_in('function LwClapPad(', [
  ("const items = LW_CLAP[i], snd", "const E = useEcho(LW_CLAP[i], fixed == null), items = E.sub, snd"),
  ("setPhase('listen');\n    T.at(r, r.at[r.lead] + n * r.spb, () => {", "setPhase('listen');\n    if (!E.full) { T.at(r, r.at[r.lead] + n * r.spb + 0.2, () => { setPhase('ready'); setHeard(2); }); setHeard(1); return; }\n    T.at(r, r.at[r.lead] + n * r.spb, () => {"),
  ("ok: mt.hits >= notes.length - 1 && mt.extra <= 1 }; setRes(out); setPhase('done'); if (onResult) onResult(out);",
   "ok: E.full ? mt.hits >= notes.length - 1 && mt.extra <= 1 : mt.hits === notes.length && mt.extra === 0 }; setRes(out); setPhase('done'); if (onResult && E.full) onResult(out);"),
  ("{!fixed && spChips(LW_CLAP.map((_, j) => [j, t('Passage ' + (j + 1), (j + 1) + '번')]), i, (j) => { reset(); setI(j); })}",
   "{!fixed && spChips(LW_CLAP.map((_, j) => [j, t('Passage ' + (j + 1), (j + 1) + '번')]), i, (j) => { reset(); setI(j); E.set(E.rung === E.nb ? E.nb : 1, 0, E.rung !== E.nb); })}\n      {ecRow(E, (f) => { reset(); f(); })}"),
  ("{res ? rqStaffEl(items, { marks: res.marks, hearts: false }) : <div",
   "{res ? rqStaffEl(items, { marks: res.marks, hearts: false, ...ecWords(E) }) : E.see && !E.full ? rqStaffEl(items, { hearts: false, ...ecWords(E) }) : <div"),
  ("<button className=\"ghost-btn\" style={lwBtn} onClick={listen}>{t('▶ Listen (twice)', '▶ 듣기 (두 번)')}</button>",
   "<button className=\"ghost-btn\" style={lwBtn} onClick={listen}>{E.full ? t('▶ Listen (twice)', '▶ 듣기 (두 번)') : t('▶ Listen', '▶ 듣기')}</button>"),
  ("{res ? t('▶ Again', '▶ 다시') : t('▶ Tap it back', '▶ 따라 치기')}</button>\n      </>)}",
   "{res ? t('▶ Again', '▶ 다시') : t('▶ Tap it back', '▶ 따라 치기')}</button>\n        {ecNext(E, res, (f) => { reset(); f(); })}\n      </>)}"),
])

# ── Grades 2-3, and Grades 4 and 5 (one pad) ──
for fn, bpmv, row, btn, src_items in [('function L2ClapPad(', 'L2_CLAP_BPM', 'l2Row', 'l2Btn', 'L2_CLAP[i]'), ('function L4ClapPad(', 'bpm', 'lwRow', 'lwBtn', 'P.items')]:
    pairs = []
    if fn.startswith('function L2'):
        pairs.append(("const items = L2_CLAP[i], snd", "const E = useEcho(L2_CLAP[i], fixed == null), items = E.sub, snd"))
        pairs.append(("{!fixed && spChips(L2_CLAP.map((_, j) => [j, t('Passage ' + (j + 1), (j + 1) + '번')]), i, (j) => { reset(); setI(j); })}",
                      "{!fixed && spChips(L2_CLAP.map((_, j) => [j, t('Passage ' + (j + 1), (j + 1) + '번')]), i, (j) => { reset(); setI(j); E.set(E.rung === E.nb ? E.nb : 1, 0, E.rung !== E.nb); })}\n      {ecRow(E, (f) => { reset(); f(); })}"))
    else:
        pairs.append(("const P = set[i], items = P.items, snd", "const P = set[i], E = useEcho(P.items, fixed == null), items = E.sub, snd"))
        pairs.append(("{!fixed && spChips(set.map((_, j) => [j, t('Passage ' + (j + 1), (j + 1) + '번')]), i, (j) => { reset(); setI(j); })}",
                      "{!fixed && spChips(set.map((_, j) => [j, t('Passage ' + (j + 1), (j + 1) + '번')]), i, (j) => { reset(); setI(j); E.set(E.rung === E.nb ? E.nb : 1, 0, E.rung !== E.nb); })}\n      {ecRow(E, (f) => { reset(); f(); })}"))
    pairs += [
        ("setPhase('listen');\n    T.at(r, r.at[r.lead] + n * r.spb, () => {", "setPhase('listen');\n    if (!E.full) { T.at(r, r.at[r.lead] + n * r.spb + 0.2, () => { setPhase('ready'); setHeard(2); }); setHeard(1); return; }\n    T.at(r, r.at[r.lead] + n * r.spb, () => {"),
        ("setRes({ hits: mt.hits, total: notes.length, extra: mt.extra, marks, ok: mt.hits >= notes.length - 1 && mt.extra <= 1 }); setPhase('done'); }); };",
         "setRes({ hits: mt.hits, total: notes.length, extra: mt.extra, marks, ok: E.full ? mt.hits >= notes.length - 1 && mt.extra <= 1 : mt.hits === notes.length && mt.extra === 0 }); setPhase('done'); }); };"),
        ("{met ? rqStaffEl(items, { marks: res.marks, hearts: false }) : <div",
         "{met || (res && !E.full) ? rqStaffEl(items, { marks: res.marks, hearts: false, ...ecWords(E) }) : E.see && !E.full ? rqStaffEl(items, { hearts: false, ...ecWords(E) }) : <div"),
        ("res && !met ? t('On time: ' + res.hits + ' of ' + res.total + '. Two or three?', '제때: ' + res.total + '개 중 ' + res.hits + '개. 두 박? 세 박?')",
         "res && !met ? t('On time: ' + res.hits + ' of ' + res.total + (E.full ? '. Two or three?' : res.ok ? ' ✓' : ''), '제때: ' + res.total + '개 중 ' + res.hits + '개' + (E.full ? '. 두 박? 세 박?' : res.ok ? ' ✓' : ''))"),
        ("{res && !met && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>",
         "{res && !met && E.full && <div style={{display:'grid',gridTemplateColumns:'repeat(2,minmax(0,1fr))',gap:8,marginTop:8}}>"),
        ("<button className=\"ghost-btn\" style={" + btn + "} onClick={listen}>{t('▶ Listen (twice)', '▶ 듣기 (두 번)')}</button>",
         "<button className=\"ghost-btn\" style={" + btn + "} onClick={listen}>{E.full ? t('▶ Listen (twice)', '▶ 듣기 (두 번)') : t('▶ Listen', '▶ 듣기')}</button>"),
        ("{res ? t('▶ Again', '▶ 다시') : t('▶ Tap it back', '▶ 따라 치기')}</button>\n      </>)}",
         "{res ? t('▶ Again', '▶ 다시') : t('▶ Tap it back', '▶ 따라 치기')}</button>\n        {(E.full ? met : res) && ecNext(E, res, (f) => { reset(); f(); })}\n      </>)}"),
    ]
    rep_in(fn, pairs)

# ── Hear and Sing Further: the longer tune, half by half ──
rep_in('function L2SingPad(', [
  ("[wrong, setWrong] = useState(null);\n  const ph = L2_PH[i],",
   "[wrong, setWrong] = useState(null), [half, setHalf] = useState(fixed != null ? 2 : 0);\n  const PH = L2_PH[i], cut = l2Half(PH), ph = half === 0 ? PH.slice(0, cut) : half === 1 ? PH.slice(cut) : PH,"),
  ("const listen = () => { T.clear(); setHeard(true); const len = lwPlay(ph, 80, T, setLit); const spb = 60 / 80; T.at((0.15 + (len + 1) * spb) * 1000, () => lwPlay(ph, 80, T, setLit)); };",
   "const listen = () => { T.clear(); setHeard(true); const len = lwPlay(ph, 80, T, setLit); const spb = 60 / 80; if (half === 2) T.at((0.15 + (len + 1) * spb) * 1000, () => lwPlay(ph, 80, T, setLit)); };"),
  ("const reset = (j) => { T.clear(); setI(j); setGot(0); setMiss(0); setHeard(false); setWrong(null); setLit(-1); };",
   "const reset = (j, h) => { T.clear(); setI(j); setGot(0); setMiss(0); setHeard(false); setWrong(null); setLit(-1); if (h != null) setHalf(h); };"),
  ("if (g >= ks.length && onResult) onResult({ ok: miss === 0, miss }); }",
   "if (g >= ks.length && onResult && half === 2) onResult({ ok: miss === 0, miss }); }"),
  ("{l2Msg(!heard ? t('Tap ▶ Listen: it plays twice.', '▶ 듣기를 눌러요: 두 번 나와요.')", "{l2Msg(!heard ? (half < 2 ? t('Tap ▶ Listen.', '▶ 듣기를 눌러요.') : t('Tap ▶ Listen: it plays twice.', '▶ 듣기를 눌러요: 두 번 나와요.'))"),
  ("{!fixed && spChips(L2_PH.map((_, j) => [j, String(j + 1)]), i, reset)}",
   "{!fixed && spChips(L2_PH.map((_, j) => [j, String(j + 1)]), i, (j) => reset(j, 0))}\n      {fixed == null && spChips([[0, t('First half', '앞 절반')], [1, t('Second half', '뒤 절반')], [2, t('The whole tune', '선율 전체')]], half, (h) => reset(i, h))}"),
  ("{l2Row(<button className=\"ghost-btn\" style={l2Btn} onClick={listen}>{t('▶ Listen (twice)', '▶ 듣기 (두 번)')}</button>)}",
   "{l2Row(<><button className=\"ghost-btn\" style={l2Btn} onClick={listen}>{half === 2 ? t('▶ Listen (twice)', '▶ 듣기 (두 번)') : t('▶ Listen', '▶ 듣기')}</button>\n        {done && half < 2 && <button className=\"ghost-btn\" style={l2Btn} onClick={() => reset(i, half + 1)}>{half === 0 ? t('▶ Now the second half', '▶ 이제 뒤 절반') : t('▶ Now the whole tune', '▶ 이제 선율 전체')}</button>}</>)}"),
])
rep("function L2SingPad({ onResult, fixed }) {",
    "// Build BG: where a tune splits in two: the first note that starts at or after half its beats\n"
    "const l2Half = (ph) => { const tot = ph.reduce((a, [, b]) => a + b, 0); let acc = 0; for (let j = 0; j < ph.length; j++) { if (acc >= tot / 2 - 1e-6) return j; acc += ph[j][1]; } return Math.ceil(ph.length / 2); };\n"
    "function L2SingPad({ onResult, fixed }) {")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
