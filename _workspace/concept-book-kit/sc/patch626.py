import sys
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
blk2 = open('/home/claude/pbtest/sc/md_block2.jsx', encoding='utf-8').read()
par2 = open('/home/claude/pbtest/sc/md_parent2.jsx', encoding='utf-8').read()
# 6: new parent lesson replaces the first version
i0 = s.index("// 4: find the parent major: the home note is the nth note of its parent, so count back"); i1 = s.index("// 5: any key. Choose the mode")
s = s[:i0] + par2 + s[i1:]
rep("\nconst scDirTag = (dn) =>", blk2 + "\nconst scDirTag = (dn) =>")
# the home note is held under the scale when she listens
rep("<button className=\"ghost-btn\" style={scS.back} onClick={() => P.play(K)}>{t('▶ Hear it', '▶ 듣기')}</button>\n        <button className=\"ghost-btn\" style={scS.prim} onClick={() => { setView('try'); setQ(1); }}>", "<button className=\"ghost-btn\" style={scS.back} onClick={() => P.play(K)}>{t('▶ Hear it', '▶ 듣기')}</button>\n        <button className=\"ghost-btn\" style={scS.back} onClick={() => mdHold(P, K)}>{t('▶ Home held', '▶ 집을 길게')}</button>\n        <button className=\"ghost-btn\" style={scS.prim} onClick={() => { setView('try'); setQ(1); }}>")
rep("<button className=\"ghost-btn\" style={scS.back} onClick={() => P.play(K)}>{t('▶ Hear it', '▶ 듣기')}</button>\n        <button className=\"ghost-btn\" style={scS.prim} onClick={() => { if (i === 6) {", "<button className=\"ghost-btn\" style={scS.back} onClick={() => mdHold(P, K)}>{t('▶ Hear it, home held', '▶ 듣기(집을 길게)')}</button>\n        <button className=\"ghost-btn\" style={scS.prim} onClick={() => { if (i === 6) {")
# 7: the shape of each mode travels: show its step pattern
rep("      <ScKeys ks={K} marks={X.marks} names={X.names} arcs={[]} nonce={'k' + st + ':' + pc}/>\n", "      <ScKeys ks={K} marks={X.marks} names={X.names} arcs={[]} nonce={'k' + st + ':' + pc}/>\n      <ScPillRow st={K.slice(1).map((k, j) => k - K[j])} upTo={7} cur={P.an > 0 ? P.an - 1 : -1}/>\n      <div style={{ textAlign: 'center', fontSize: 12.5, fontWeight: 700, color: '#6d6f9c', marginTop: 4 }}>{t('T = a tone, S = a half step. Every mode has its own shape, and the shape works from any home note, like the major scale shape you know.', 'T = 온음, S = 반음. 선법마다 자기 모양이 있고, 아는 장음계 모양처럼 어느 집에서든 그대로 써요.')}</div>\n")
# registrations: md-colour out, three new lessons in
reg0 = s.index("['md-colour', 'The same home, a new colour'"); reg1 = s.index("\n", reg0)
s = s[:reg0] + "['md-home', 'Which note feels like home?', '어느 음이 \u201c\uc9d1\u201d\ucc98\ub7fc \ub290\uaed8\uc838\uc694?', 'Stop the scale on different notes.', '\uc74c\uacc4\ub97c \uc5ec\ub7ec \uc74c\uc5d0\uc11c \uba48\ucdb0 \ubcf4\uc544\uc694.', MdHome],\n ['md-family', 'The 3rd decides the family', '3\ubc88\uc9f8 \uc74c\uc774 \uacc4\uc5f4\uc744 \uc815\ud574\uc694', 'Major-sounding or minor-sounding.', '\uc7a5\uc870 \uc18c\ub9ac\uc778\uc9c0 \ub2e8\uc870 \uc18c\ub9ac\uc778\uc9c0.', MdFamily],\n ['md-ladder', 'From bright to dark', '\ubc1d\uc740 \uac83\uc5d0\uc11c \uc5b4\ub450\uc6b4 \uac83\uae4c\uc9c0', 'One note moves down at a time.', '\ud55c \uc74c\uc529 \ub0b4\ub824\uac00\uc694.', MdLadder]," + s[reg1:]
rep("lessons: ['md-start', 'sc-modes', 'md-colour', 'md-parent', 'md-keys']", "lessons: ['md-home', 'md-start', 'sc-modes', 'md-family', 'md-ladder', 'md-parent', 'md-keys']")
open(bb, 'w', encoding='utf-8').write(s)
