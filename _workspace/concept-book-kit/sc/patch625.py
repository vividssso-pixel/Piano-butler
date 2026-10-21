import sys
a, bb = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
blk = open('/home/claude/pbtest/sc/md_block.jsx', encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:90])
    s = s.replace(x, y)
rep("\nconst scDirTag = (dn) =>", blk + "\nconst scDirTag = (dn) =>")
rep("'The major scale started on another of its notes.', '장음계를 다른 음에서 시작해요.', ScModes]].forEach(", "'The seven homes, each with its name.', '일곱 개의 집과 그 이름.', MdNames]].forEach(")
rep("'The major scale started on another of its notes.', '장음계를 다른 음에서 시작해요.', MdNames]", "'The seven homes and their names.', '일곱 개의 집과 이름.', MdNames]") if False else None
rep("    lessons: ['sc-modes'], tools: [], more: [],", "    lessons: ['md-start', 'sc-modes', 'md-colour', 'md-parent', 'md-keys'], tools: [], more: [],")
reg = """
[['md-start', 'The same white keys, a new home', '같은 흰건반, 새로운 집', 'Start on another white key.', '다른 흰건반에서 시작해요.', MdStart],
 ['md-colour', 'The same home, a new colour', '같은 집, 다른 색깔', 'Each mode on C, against C major.', 'C 위의 선법을 C장조와 견줘 봐요.', MdColour],
 ['md-parent', 'Find the parent major', '부모 장조 찾기', 'Count back to the first note.', '거꾸로 세서 첫 음을 찾아요.', MdParent],
 ['md-keys', 'Modes in any key', '어느 조에서든 선법', 'Pick a mode and a home note.', '선법과 집이 되는 음을 골라요.', MdKeys]].forEach(([id, en, ko, benEn, bko, Comp]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '선법' : 'Modes'); }, C: Comp });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-modes';
});
"""
anchor = "  if (id === 'sc-modes') Object.defineProperty(tl, 'kicker', { get: () => TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '선법' : 'Modes'), enumerable: true, configurable: true });\n});\n"
rep(anchor, anchor + reg)
open(bb, 'w', encoding='utf-8').write(s)
