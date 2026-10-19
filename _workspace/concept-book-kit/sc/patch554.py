import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# arrows may carry a colour and a delay: the whole step is drawn as two half steps
rep("const arrows = arcs.map(([a, b, anim], j) => {", "const arrows = arcs.map(([a, b, anim, col, dly], j) => {")
rep("const dash = anim ? { strokeDasharray: '120', strokeDashoffset: '120', animation: 'drawArc 0.45s ease-out forwards' } : {};\n    const headAnim = anim ? { animation: 'fadeUp 0.3s both 0.3s' } : {};",
    "const dash = anim ? { strokeDasharray: '120', strokeDashoffset: '120', animation: 'drawArc 0.45s ease-out ' + (dly || 0) + 's forwards' } : {};\n    const headAnim = anim ? { animation: 'fadeUp 0.3s both ' + (0.3 + (dly || 0)) + 's' } : {};")
rep("<path d={line} stroke=\"#26296b\" strokeWidth={w} style={dash}/><path d={head} stroke=\"#26296b\" strokeWidth={w} style={headAnim}/>",
    "<path d={line} stroke={col || '#26296b'} strokeWidth={w} style={dash}/><path d={head} stroke={col || '#26296b'} strokeWidth={w} style={headAnim}/>")
# AcStep: legs of a move
rep("  const title = t(D.title[0], D.title[1]);\n  let body;",
"""  const title = t(D.title[0], D.title[1]);
  // a move as arrows: one for a half step; for a whole step two half steps (navy, then coral a moment later) through the key between
  const mid = (a, b) => a + (b > a ? 1 : -1);
  const legs = (a, b, anim) => SZ === 1 ? [[a, b, anim]] : [[a, mid(a, b), anim, '#26296b', 0], [mid(a, b), b, anim, '#c0431f', 0.55]];
  let body;""")
rep("const arcs = []; if (SZ === 1) { for (let k = 0; k <= 11; k++) arcs.push([k, k + 1, false]); } else { for (let k = 0; k <= 10; k += 2) arcs.push([k, k + 2, false]); }",
    "const arcs = []; if (SZ === 1) { for (let k = 0; k <= 11; k++) arcs.push([k, k + 1, false]); } else { for (let k = 0; k <= 10; k += 2) arcs.push(...legs(k, k + 2, false)); }")
rep("    const e = EX[i], marks = { [e.a]: 'pass' }; if (shown) marks[e.b] = 'pick';", "    const e = EX[i], marks = { [e.a]: 'pass' }; if (shown) { marks[e.b] = 'pick'; if (SZ === 2) marks[mid(e.a, e.b)] = 'pass'; }")
rep("<AcKeys marks={marks} arcs={shown ? [[e.a, e.b, true]] : []} nonce={nonce}/>", "<AcKeys marks={marks} arcs={shown ? legs(e.a, e.b, true) : []} nonce={nonce}/>")
rep("""    timers.current.push(setTimeout(() => { setShown(true); snd(e.b, 0.6); }, 750)); };""",
    """    timers.current.push(setTimeout(() => { setShown(true); if (SZ === 2) { snd(mid(e.a, e.b), 0.4); timers.current.push(setTimeout(() => snd(e.b, 0.6), 550)); } else snd(e.b, 0.6); }, 750)); };""")
rep("    if (from != null && to != null) { marks[to] = 'pick'; arcs.push([from, to, true]); }", "    if (from != null && to != null) { marks[to] = 'pick'; if (SZ === 2) marks[mid(from, to)] = 'pass'; arcs.push(...legs(from, to, true)); }")
rep("snd(from, 0.4); timers.current.push(setTimeout(() => snd(k, 0.6), 450)); };", "snd(from, 0.4); if (SZ === 2) { timers.current.push(setTimeout(() => snd(mid(from, k), 0.4), 450)); timers.current.push(setTimeout(() => snd(k, 0.6), 1000)); } else timers.current.push(setTimeout(() => snd(k, 0.6), 450)); };")
# the words
rep("all: ['Whole step (tone) = two half steps: skip one key.', '온음(tone)은 반음 두 개예요: 건반 하나를 건너뛰어요.'],", "all: ['Whole step (tone) = two half steps.', '온음(tone)은 반음 두 걸음이에요.'],")
rep("en: 'From C, skip the black key to D: a whole step.', ko: 'C에서 검은건반을 건너뛰면 D. 온음이에요.'", "en: 'From C, one half step to the black key, one more to D: a whole step.', ko: 'C에서 반음 하나로 검은건반, 하나 더 가면 D: 온음이에요.'")
rep("en: 'From E, skip F: a black key. A whole step.', ko: 'E에서 F를 건너뛰면 검은건반. 온음이에요.'", "en: 'From E, one half step to F, one more to the black key: a whole step.', ko: 'E에서 반음 하나로 F, 하나 더 가면 검은건반: 온음이에요.'")
rep("en: 'Black to black can be a whole step too.', ko: '검은건반에서 검은건반도 온음일 수 있어요.'", "en: 'Black to black: one half step to the white key, one more to the next black key.', ko: '검은건반에서 검은건반: 반음 하나로 흰건반, 하나 더 가면 검은건반.'")
rep("en: 'Down is a whole step too.', ko: '아래로 내려가도 온음이에요.'", "en: 'Down is the same: two half steps down make a whole step.', ko: '아래로도 같아요: 반음 두 걸음이 온음이에요.'")
rep("en: 'A to B: skip the black key between.', ko: 'A에서 B: 사이의 검은건반을 건너뛰어요.'", "en: 'From A, one half step to the black key, one more to B: a whole step.', ko: 'A에서 반음 하나로 검은건반, 하나 더 가면 B: 온음이에요.'")
rep("word: ['a whole step', '온음']", "word: ['a whole step (two half steps)', '온음 (반음 두 걸음)']")
rep("blurb: 'Two half steps: skip one key.'", "blurb: 'Two half steps.'", 0) if False else None
rep("'Two half steps: skip one key.', '반음 두 개: 건반 하나를 건너뛰어요.'", "'Two half steps in a row.', '반음 두 걸음을 이어서.'")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
