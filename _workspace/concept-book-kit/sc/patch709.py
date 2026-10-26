import sys, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:90])
    s = s.replace(old, new)

# Build AP (Sohyun 26 Oct 20:24: "음악 이야기에 중복된 게 너무 많아서 다듬어야 할 것 같네"; and on the couplets: "나도 이해가 잘 안 가
# ... 너가 잘 잡아서 해줘").
# 1. Stories of music: each room keeps its chapter's own steps; Toolbox pieces that repeat a step are hidden (not deleted:
#    their links still open), as board call 11 recommended for the twins. The piano: Clavichord, harpsichord, piano (= Pluck,
#    push or strike); Inside the piano (= Key, hammer, damper); The piano's story (= the first piano on its timeline, and
#    the timeline of music); The style eras (= the composers' and the styles' periods). Composers: Step into each era (= the
#    timeline and each period's step); Who lived when? (= Who was alive?). Styles: Textures: how many voices? and Which
#    texture is this? (= One tune, three textures); What makes each style different? (= the styles' steps and Which style?);
#    Straight or swing? (= Blues and swing; the Rhythm room keeps its own swing lesson); The 12-bar blues (= Blues and swing).
#    Composers keeps four extras with something new: the 46 composer cards, Movements, Who am I?, Name that tune.
# 2. The couplets: every strong syllable is now an important word or the strong part of a long word, every weak one a small
#    word or a weak part (three lines changed). The pad says how to find them, can fade the small words (a hint), says why
#    a mark is right or wrong after the check, and can say the couplet aloud (the browser's voice, Australian English
#    first, as the counting voice does). The drill's two word levels can say the line too.

for id in ['keyboard-ancestors', 'piano-timeline', 'piano-action', 'eras', 'era-worlds', 'composer-time-machine', 'texture-types', 'texture-spotter', 'genre-traits', 'swing-feel', 'twelve-bar-blues']:
    m = re.findall(r"\{ id: '" + re.escape(id) + r"', ch: '[a-z-]+', title:", s)
    assert len(m) == 1, (id, m)
    s = s.replace(m[0], m[0].replace(", title:", ", hidden: true, title:"))   # Build AP: a twin of a chapter step
rep("""  'piano-story': ['sps-sound', 'sps-softloud', 'sps-action', 'sps-pedals', 'sps-keys', 'keyboard-ancestors', 'piano-timeline', 'piano-action', 'eras'],""",
    """  'piano-story': ['sps-sound', 'sps-softloud', 'sps-action', 'sps-pedals', 'sps-keys'],   // Build AP: keyboard-ancestors, piano-action, piano-timeline, eras were twins""")
rep("""  'styles': ['csx-map', 'csx-texture', 'csx-era', 'csx-penta', 'csx-blues', 'csx-pop', 'csx-ear', 'texture-types', 'texture-spotter', 'genre-traits', 'swing-feel', 'twelve-bar-blues'],""",
    """  'styles': ['csx-map', 'csx-texture', 'csx-era', 'csx-penta', 'csx-blues', 'csx-pop', 'csx-ear'],   // Build AP: texture-types, texture-spotter, genre-traits, swing-feel, twelve-bar-blues were twins""")
rep("""  'composers': ['cpx-map', 'cpx-baroque', 'cpx-classical', 'cpx-romantic', 'cpx-modern', 'cpx-alive', 'cpx-order', 'era-worlds', 'movement-map', 'composer-time-machine', 'composer-cards', 'who-am-i', 'name-that-tune'],""",
    """  'composers': ['cpx-map', 'cpx-baroque', 'cpx-classical', 'cpx-romantic', 'cpx-modern', 'cpx-alive', 'cpx-order', 'composer-cards', 'movement-map', 'who-am-i', 'name-that-tune'],   // Build AP: era-worlds, composer-time-machine were twins""")

# ── 2. the couplets ──
rep("""  { id: 'snow', m: 2, l: ['^Snow-flakes ^drift-ing ^soft-ly ^down', '^Cov-er ^all the ^qui-et ^town.'] },
  { id: 'boat', m: 2, l: ['A ^lit-tle ^boat sails ^out to ^sea,', 'Its ^sail is ^white as ^white can ^be.'] },""",
    """  { id: 'snow', m: 2, l: ['^Snow-flakes ^drift-ing ^soft-ly ^down', '^Paint-ing ^white the ^qui-et ^town.'] },   // Build AP: line 2 (was 'Cover all the quiet town': 'all' could go either way)
  { id: 'boat', m: 2, l: ['The ^lit-tle ^boat is ^far at ^sea,', 'Its ^sail is ^white as ^white can ^be.'] },   // Build AP: line 1 (was 'A little boat sails out to sea': 'sails' is said strongly too)""")
rep("""'All the ^fish in the ^wa-ter are ^dan-cing with ^me.'] },""",
    """'And the ^fish in the ^wa-ter are ^dan-cing with ^glee.'] },   // Build AP: line 2 (was 'All the fish ... with me': 'All' strong, 'me' a small word)""")
rep("""const mwStarts = (syls) => syls.map((x, i) => x.s ? i : -1).filter(i => i >= 0);""",
    """const mwStarts = (syls) => syls.map((x, i) => x.s ? i : -1).filter(i => i >= 0);
// Build AP: how to hear them. Important words are strong, small words weak, a long word strong in one part. Every couplet
// here keeps to it.
const mwOne = (syls, i) => (i === 0 || syls[i - 1].end) && syls[i].end;   // a word of one syllable
const mwSmall = (syls, i) => !syls[i].s && mwOne(syls, i);
const mwWordOf = (syls, i) => { let a = i, b = i; while (a > 0 && !syls[a - 1].end) a--; while (!syls[b].end) b++; return syls.slice(a, b + 1).map(x => x.s ? x.t.toUpperCase() : x.t.toLowerCase()).join('-').replace(/[,.]/g, ''); };
function mwWhy(syls, i) {
  const w = syls[i].t.replace(/[,.]/g, '').toLowerCase(), word = mwWordOf(syls, i);
  if (!mwOne(syls, i)) return [w + ': a long word is strong in one part: ' + word + '.', w + ': 긴 낱말은 한 부분만 세요: ' + word + '.'];
  return syls[i].s ? [w + ': an important word, so strong.', w + ': 중요한 낱말이라 세요.'] : [w + ': a small word, so weak.', w + ': 작은 낱말이라 여려요.'];
}
// the couplet said aloud by the browser's voice (as the counting voice: Australian English first)
const mwCanSay = () => { try { return !!window.speechSynthesis && typeof SpeechSynthesisUtterance !== 'undefined'; } catch (e) { return false; } };
const mwSay = (text) => { try { if (!mwCanSay()) return; window.speechSynthesis.cancel(); const u = new SpeechSynthesisUtterance(text), v = pickVoice(); if (v) u.voice = v; u.lang = v ? v.lang : 'en-AU'; u.rate = 0.82; window.speechSynthesis.speak(u); } catch (e) {} };
const mwPlain = (line) => line.replace(/\\^/g, '').replace(/-/g, '');""")

# the pad: the three ways to hear them, a hint, the voice, a reason after the check
rep("""  const [pid, setPid] = useState('kites'), [marks, setMarks] = useState({}), [chk, setChk] = useState(false), [show, setShow] = useState(false), [lit, setLit] = useState(-1);""",
    """  const [pid, setPid] = useState('kites'), [marks, setMarks] = useState({}), [chk, setChk] = useState(false), [show, setShow] = useState(false), [lit, setLit] = useState(-1), [hint, setHint] = useState(false);""")
rep("""  const choose = (id) => { T.clear(); stopClicks(); setPid(id); setMarks({}); setChk(false); setShow(false); setLit(-1); };""",
    """  const choose = (id) => { T.clear(); stopClicks(); setPid(id); setMarks({}); setChk(false); setShow(false); setLit(-1); setHint(false); };
  const wrong = chk ? flat.findIndex((x, i) => !!x.s !== !!marks[i]) : -1;""")
rep("""    return <button key={i} data-mw-syl={i} aria-pressed={on} onClick={() => tap(i)} style={{display:'inline-flex',alignItems:'center',gap:2,minHeight:42,padding:'4px 7px',marginLeft:gap ? 7 : 0,""",
    """    return <button key={i} data-mw-syl={i} aria-pressed={on} onClick={() => tap(i)} style={{display:'inline-flex',alignItems:'center',gap:2,minHeight:42,padding:'4px 7px',marginLeft:gap ? 7 : 0,opacity:hint && !chk && mwSmall(flat, i) ? 0.3 : 1,""")
rep("""      <div style={actNote}>{LANG === 'ko' ? <>두 줄 시를 소리 내어 말해요. <b>힘주어 말하는 음절</b>을 눌러 그 앞에 세로줄(|)을 그어요. 그다음 확인.</> : <>Say the couplet out loud. Tap each syllable you say <b>with more weight</b>: an upright line (|) goes before it. Then check.</>}</div>""",
    """      <div style={actNote}>{LANG === 'ko' ? <>두 줄 시를 소리 내어 읽고, <b>힘주어 말하는 음절</b>을 눌러 그 앞에 세로줄(|)을 그어요.</> : <>Say the couplet out loud. Tap each syllable said <b>with more weight</b>: an upright line (|) goes before it.</>}</div>
      <div data-mw-how style={{display:'grid',gap:3,maxWidth:440,margin:'0 auto 10px',fontSize:13.5,fontWeight:700,color:BK.ink,lineHeight:1.35}}>
        {[[t('Important words are strong', '중요한 낱말은 세게'), 'KITES · HIGH · FREE'], [t('Small words are weak', '작은 낱말은 여리게'), 'a · the · and · is · of · to'], [t('A long word is strong in one part', '긴 낱말은 한 부분만 세게'), 'FLY-ing · DAN-cing']].map(([a, b], j) => <div key={j} style={{display:'flex',gap:8,alignItems:'baseline'}}><b style={{color:PEN_C,flex:'0 0 auto'}}>{j + 1}</b><span>{a}: <span style={{fontWeight:900,letterSpacing:'0.02em'}}>{b.split(' · ').map((e, k) => <span key={k} style={{whiteSpace:'nowrap'}}>{k ? ' · ' : ''}{e.replace(/-/g, '\u2011')}</span>)}</span></span></div>)}
      </div>""")
rep("""      {chk && spMsg(got === nS && !extra ? t('All ' + nS + ' strong syllables.', '센 음절 ' + nS + '개를 모두 찾았어요.')""",
    """      {!chk && <div style={{display:'flex',gap:6,justifyContent:'center',flexWrap:'wrap',margin:'0 0 6px'}}>
        {mwCanSay() && <button className="ghost-btn" style={spBtn} data-mw-say onClick={() => mwSay(P.l.map(mwPlain).join(' '))}>{t('▶ Hear it said', '▶ 읽어 주기')}</button>}
        <button className="ghost-btn" style={spBtn} aria-pressed={hint} data-mw-hint onClick={() => setHint(!hint)}>{hint ? t('Hint: on', '힌트: 켬') : t('Hint: fade the small words', '힌트: 작은 낱말 흐리게')}</button>
      </div>}
      {chk && spMsg(got === nS && !extra ? t('All ' + nS + ' strong syllables.', '센 음절 ' + nS + '개를 모두 찾았어요.')""")
rep("""        : t('Found ' + got + ' of ' + nS + (extra ? '; ' + extra + ' on a weak syllable' : '') + '. Green: found; dashed: missed.', nS + '개 중 ' + got + '개' + (extra ? ', 여린 음절에 ' + extra + '개' : '') + '. 초록: 찾음, 점선: 놓침.'), got === nS && !extra ? BK.green : BK.coral)}""",
    """        : t('Found ' + got + ' of ' + nS + (extra ? '; ' + extra + ' on a weak syllable' : '') + '. Green: found; dashed: missed.', nS + '개 중 ' + got + '개' + (extra ? ', 여린 음절에 ' + extra + '개' : '') + '. 초록: 찾음, 점선: 놓침.'), got === nS && !extra ? BK.green : BK.coral)}
      {wrong >= 0 && <div data-mw-why style={{textAlign:'center',fontSize:14,fontWeight:800,color:BK.ink,margin:'2px 0 0'}}>{t(mwWhy(flat, wrong)[0], mwWhy(flat, wrong)[1])}</div>}""")
# the drill: the line said aloud
rep("""  const pic = q.kind === 'mwend' ? <div""", """  const say = (q.kind === 'stress' || q.kind === 'wrhythm') && !paper && mwCanSay() ? <div style={{textAlign:'center',margin:'-2px 0 8px'}}><button className={pixel ? 'pixel-btn' : 'ghost-btn'} style={{minHeight:40}} onClick={() => mwSay(mwPlain(mwPoem(q.pid).l[q.li]))}>{t('▶ Hear it said', '▶ 읽어 주기')}</button></div> : null;   // Build AP
  const pic = q.kind === 'mwend' ? <div""")
rep("""    {pic}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,maxWidth:q.kind === 'mwend' ? 360 : 520,margin:'0 auto'}}>""",
    """    {say}{pic}
    <div style={{display:'grid',gridTemplateColumns:'repeat(' + cols + ',minmax(0,1fr))',gap:8,maxWidth:q.kind === 'mwend' ? 360 : 520,margin:'0 auto'}}>""")
# the Lesson Book page: how to find them
rep("""        [t('strong syllable', '센 음절'), X('A syllable, or a short word, said with more weight: KITES are FLY-ing.', '더 힘주어 말하는 음절이나 짧은 낱말: KITES are FLY-ing.')],
      ]}/>""", """        [t('strong syllable', '센 음절'), X('A syllable, or a short word, said with more weight: KITES are FLY-ing.', '더 힘주어 말하는 음절이나 짧은 낱말: KITES are FLY-ing.')],
        [t('how to hear them', '찾는 법'), X('Say it as you talk. Important words are strong; small words (a, the, and, is, of, to) are weak; a long word is strong in one part: FLY-ing.', '말하듯이 읽어요. 중요한 낱말은 세고, 작은 낱말(a, the, and, is, of, to)은 여리고, 긴 낱말은 한 부분만 세요: FLY-ing.')],
      ]}/>""")
# the teacher's note
rep("""The couplets are new, written for this book. Grade 2 asks only for the marks; Grade 3 for the rhythm too.</div></>}""",
    """The couplets are new, written for this book, and keep to three plain rules a student can use: important words (nouns, verbs, describing words) are strong; small words (a, the, and, is, of, to, in, can) are weak; a word of two or more syllables is strong in one part, as a dictionary marks it (FLY-ing). The screen can say each couplet aloud. Grade 2 asks only for the marks; Grade 3 for the rhythm too.</div></>}""")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
