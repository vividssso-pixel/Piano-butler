import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
# a sharp is not always a black key: E sharp is the white key F, B sharp the white key C (her 15:43 note)
rep("function AcKeys({ marks, onTap, arcs, nonce, names }) {", "function AcKeys({ marks, onTap, arcs, nonce, names, stagger, topRoom = 26 }) {")
rep("onTap={onTap} top={26} overlay=", "onTap={onTap} top={topRoom} overlay=")
rep("<text key={'n' + k + txt} x={kx(+k)} y={-9}", "<text key={'n' + k + txt} x={kx(+k)} y={stagger && white(+k) ? -27 : -9}")
rep("  const ok = (k) => k != null && k >= 0 && k <= 11 && isW(k) && target(k) >= 0 && target(k) <= 11 && !isW(target(k));   // a white key with a black key right beside it on that side",
    "  const ok = (k) => k != null && k >= 0 && k <= 11 && isW(k);   // any white key of the octave: its sharp (or flat) is a black key or a white one")
rep("order: [0, 5, 9, 2, 7],", "order: [0, 4, 2, 5, 7, 9, 11],")
rep("all: ['Sharp (♯) = one half step up: the very next key to the right.', '샵(♯) = 반음 위: 바로 오른쪽 건반이에요.'],",
    "all: ['Sharp (♯) = one half step up, to the very next key on the right: black or white.', '샵(♯) = 반음 위, 바로 오른쪽 건반으로: 검은건반일 수도 흰건반일 수도 있어요.'],")
rep("""  const en = (k) => nameOf(k) + ' (' + L(k) + ' ' + D.word[0] + '): one half step ' + D.above[0] + ' ' + L(k) + '.';
  const ko = (k) => nameOf(k) + '(' + L(k) + ' ' + D.word[1] + '): ' + L(k) + '보다 반음 ' + D.above[1] + '예요.';""",
"""  const en = (k) => isW(target(k)) ? nameOf(k) + ' (' + L(k) + ' ' + D.word[0] + ') = the white key ' + L(target(k)) + '. ' + D.word[0][0].toUpperCase() + D.word[0].slice(1) + 's are not always black keys.'
    : nameOf(k) + ' (' + L(k) + ' ' + D.word[0] + '): one half step ' + D.above[0] + ' ' + L(k) + '.';
  const ko = (k) => isW(target(k)) ? nameOf(k) + '(' + L(k) + ' ' + D.word[1] + ')은 흰건반 ' + L(target(k)) + '예요. ' + D.word[1] + '이 늘 검은건반인 건 아니에요.'
    : nameOf(k) + '(' + L(k) + ' ' + D.word[1] + '): ' + L(k) + '보다 반음 ' + D.above[1] + '예요.';""")
rep("<AcKeys marks={{}} arcs={pairs.map(([a, b]) => [a, b, false])} names={names} nonce=\"all\"/>", "<AcKeys marks={{}} arcs={pairs.map(([a, b]) => [a, b, false])} names={names} nonce=\"all\" stagger topRoom={46}/>")
rep("      : !ok(from) ? t('No black key right beside this one. Try another.', '바로 옆에 검은건반이 없어요. 다른 건반을 눌러 봐요.')", "      : !ok(from) ? t('Tap a white key in the middle.', '가운데 흰건반을 눌러요.')")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
