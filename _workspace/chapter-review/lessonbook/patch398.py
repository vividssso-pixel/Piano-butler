#!/usr/bin/env python3
# Phase 398: Sohyun picks the small house's C and E (2026-10-09): Princess Clara lives at C ("the Queen and the King come
# later" -- the clefs), and E is the Exit. The Dog in his doghouse (D) stays; the big house is unchanged.
#   python3 patch398.py <drills.src.html>
import sys
src = sys.argv[1]
s = open(src, encoding='utf-8').read()

def rep(a, b, what, n=1):
    global s
    c = s.count(a)
    if c != n: raise SystemExit(what + ': expected %d, got %d' % (n, c))
    s = s.replace(a, b)

def cut(start, end, new, what):
    global s
    i = s.find(start); j = s.find(end, i)
    if i < 0 or j < 0 or s.count(start) != 1: raise SystemExit(what + ': markers not found once')
    s = s[:i] + new + s[j:]

rep("// D is the Dog in his doghouse between the two black keys, with the Cat (C) and the Elephant (E) either side (her C/E\n// words were left to Claude: alphabet-book words, see the Phase 397 row); the word",
    "// D is the Dog in his doghouse between the two black keys; Princess Clara lives at the left door (C) and the right door is\n// the Exit (E) -- her picks, Phase 398 (the Queen and the King arrive later, with the staff); the word", 'header')

# the drawings: Princess Clara (a crown, long hair) and the Exit (a door under its sign)
cut('function nnCat(cx, cy, k = 1) {', 'function nnDog(cx, cy, k = 1) {', '''function nnClara(cx, cy, k = 1) {
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'pa', seg: [['M', P(-7.6, -2)], ['Q', P(-9.6, 8), P(-6.4, 11.6)], ['L', P(6.4, 11.6)], ['Q', P(9.6, 8), P(7.6, -2)], ['Z']], f: PEN_N, s: PEN_N, w: 1.2 });   // long hair
  s.push({ k: 'pa', seg: [['M', P(-10, 13.4)], ['Q', P(-9, 7.2), P(0, 7.6)], ['Q', P(9, 7.2), P(10, 13.4)], ['Z']], f: '#fbe9e2', s: PEN_N, w: 1.5 });   // her dress
  s.push({ k: 'el', c: P(0, -0.6), rx: 6.4 * k, ry: 7.2 * k, f: PEN_P, s: PEN_N, w: 1.8 });
  s.push({ k: 'pa', seg: [['M', P(-6.4, -1.8)], ['Q', P(-6.6, -8), P(0, -8)], ['Q', P(6.6, -8), P(6.4, -1.8)], ['Q', P(3, -4.8), P(0, -4.4)], ['Q', P(-3, -4.8), P(-6.4, -1.8)], ['Z']], f: PEN_N, s: PEN_N, w: 1.1 });   // fringe
  s.push({ k: 'pa', seg: [['M', P(-4.8, -7.2)], ['L', P(-5.6, -13)], ['L', P(-2.6, -10)], ['L', P(0, -14.2)], ['L', P(2.6, -10)], ['L', P(5.6, -13)], ['L', P(4.8, -7.2)], ['Z']], f: PEN_C, s: PEN_N, w: 1.1 });   // the crown
  s.push({ k: 'el', c: P(-2.4, 0.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N }, { k: 'el', c: P(2.4, 0.4), rx: 0.85 * k, ry: 0.95 * k, f: PEN_N });
  s.push({ k: 'el', c: P(-3.9, 2.6), rx: 1.1 * k, ry: 0.7 * k, f: '#f6c9bb' }, { k: 'el', c: P(3.9, 2.6), rx: 1.1 * k, ry: 0.7 * k, f: '#f6c9bb' });
  s.push(penCurve([['M', P(-1.8, 3.4)], ['Q', P(0, 4.8), P(1.8, 3.4)]], 1.1, PEN_N));
  return nnCh(s);
}
''', 'clara')
cut('function nnElephant(cx, cy, k = 1) {', 'function nnGrandma(cx, cy, k = 1) {', '''function nnExit(cx, cy, k = 1) {   // a prop: straight lines
  const P = (a, b) => [cx + a * k, cy + b * k], s = [];
  s.push({ k: 'rc', x: cx - 8.6 * k, y: cy - 14.6 * k, w: 17.2 * k, h: 6.8 * k, rx: 1.2 * k, f: PEN_C, nw: true });
  s.push({ ...penText(cx, cy - 9.4 * k, 'EXIT', { size: 5 * k, weight: 900, fill: '#fffdf7', anchor: 'middle' }) });
  s.push({ k: 'rc', x: cx - 6.4 * k, y: cy - 5.6 * k, w: 12.8 * k, h: 18.6 * k, rx: 0.8 * k, f: PEN_P, s: PEN_N, sw: 1.6, nw: true });
  s.push({ k: 'el', c: P(3.8, 4.4), rx: 1.1 * k, ry: 1.1 * k, f: PEN_N });
  s.push({ ...penLine(P(-3.8, 0.6), P(0.6, 0.6), 1.5, PEN_C), nw: true }, { k: 'pa', seg: [['M', P(-0.2, -1.8)], ['L', P(2.8, 0.6)], ['L', P(-0.2, 3)], ['Z']], f: PEN_C, nw: true });   // the way out
  return s;
}
''', 'exit')
rep("""const NN_RES = { C: ['Cat', '고양이'], D: ['Dog', '강아지'], E: ['Elephant', '코끼리'],""",
    """const NN_RES = { C: ['Princess Clara', '클라라 공주'], D: ['Dog', '강아지'], E: ['Exit', '출구'],""", 'words')
rep("  if (L === 'C') return nnCat(cx, cy + 1 * k, k);", "  if (L === 'C') return nnClara(cx, cy, k);", 'res C')
rep("  if (L === 'E') return nnElephant(cx, cy - 1 * k, k);", "  if (L === 'E') return nnExit(cx, cy, k);", 'res E')
rep("  // p5: who lives there -- Cat, Dog (in his doghouse), Elephant; Front door, Grandma, Apple garden, Back door",
    "  // p5: who lives there -- Princess Clara, her Dog (in his doghouse), the Exit; Front door, Grandma, Apple garden, Back door", 'art comment')

# the Lesson Book page (and so the app lesson)
rep("""-- and each word starts with its key\\'s letter. Watch for counting up from C on every key: ask "Who lives there?" instead.', '""",
    """-- and each word starts with its key\\'s letter. Watch for counting up from C on every key: ask "Who lives there?" instead. Princess Clara belongs to the royal family: the Queen and the King arrive with the staff.', '""", 'teacher en')
rep("""그리고 단어마다 그 건반의 글자로 시작해요. 건반마다 C부터 세는지 봐 주세요: 대신 "거기 누가 살지?" 하고 물어요.')}""",
    """그리고 단어마다 그 건반의 글자로 시작해요. 건반마다 C부터 세는지 봐 주세요: 대신 "거기 누가 살지?" 하고 물어요. 클라라 공주는 왕실 가족이에요: 여왕과 왕은 오선보와 함께 등장해요.')}""", 'teacher ko')
rep("the Cat on C, the Dog in his doghouse on D, the Elephant on E;", "Princess Clara on C, her Dog in his doghouse on D, the Exit on E;", 'label en')
rep("C에 고양이, D에 개집 속 강아지, E에 코끼리;", "C에 클라라 공주, D에 개집 속 강아지, E에 출구;", 'label ko')
rep("""작은 집 한가운데, 검은건반 두 개 사이 개집에는 <b>강아지(Dog)</b>가 살아요: <b>D</b>. 왼쪽 문에는 <b>고양이(Cat)</b>, <b>C</b>. 오른쪽 문에는 <b>코끼리(Elephant)</b>, <b>E</b>.""",
    """작은 집에는 왼쪽 문에 <b>클라라 공주(Princess Clara)</b>, <b>C</b>가 살고, 검은건반 두 개 사이 개집에는 공주의 <b>강아지(Dog)</b>, <b>D</b>가 살아요. 오른쪽 문은 <b>출구(Exit)</b>, <b>E</b>예요.""", 'say ko')
rep("""In the small house, the <b>Dog</b> lives in the middle, in his doghouse between the two black keys: that is <b>D</b>. The <b>Cat</b> sits at the left door (<b>C</b>) and the <b>Elephant</b> at the right door (<b>E</b>).""",
    """In the small house lives <b>Princess Clara</b>, at the left door (<b>C</b>), with her <b>Dog</b> in his doghouse between the two black keys (<b>D</b>); the right door is the <b>Exit</b> (<b>E</b>).""", 'say en')
rep('''누가 사는지와 글자를 말해요 -- "코끼리: E!" 그다음 바꿔서!''', '''누가 사는지와 글자를 말해요 -- "할머니: G!" 그다음 바꿔서!''', 'game ko')
rep('''say who lives there and its letter -- "Elephant: E!" Then swap.''', '''say who lives there and its letter -- "Grandma: G!" Then swap.''', 'game en')

# the app's "Who lives here?"
rep("""{ C: 'C -- 고양이(Cat): 작은 집의 왼쪽 문.', D: 'D -- 강아지(Dog): 검은건반 두 개 사이, 개집에 살아요.', E: 'E -- 코끼리(Elephant): 작은 집의 오른쪽 문.',""",
    """{ C: 'C -- 클라라 공주(Princess Clara): 작은 집의 왼쪽 문.', D: 'D -- 공주의 강아지(Dog): 검은건반 두 개 사이, 개집에 살아요.', E: 'E -- 출구(Exit): 작은 집의 오른쪽 문.',""", 'who ko')
rep("""{ C: 'C -- the Cat, at the small house\\'s left door.', D: 'D -- the Dog, in his doghouse between the two black keys.', E: 'E -- the Elephant, at the small house\\'s right door.',""",
    """{ C: 'C -- Princess Clara, at the small house\\'s left door.', D: 'D -- her Dog, in his doghouse between the two black keys.', E: 'E -- the Exit, the small house\\'s right door.',""", 'who en')
rep("""{t('Cat · Dog · Elephant -- Front door · Grandma · Apple garden · Back door', '고양이 · 강아지 · 코끼리 -- 앞문 · 할머니 · 사과 정원 · 뒷문')}""",
    """{t('Princess Clara · Dog · Exit -- Front door · Grandma · Apple garden · Back door', '클라라 공주 · 강아지 · 출구 -- 앞문 · 할머니 · 사과 정원 · 뒷문')}""", 'who idle')

# the Workbook and the Teacher copy
rep('how="Draw them on their keys: the Cat, the Dog in his doghouse and the Elephant in the small house;',
    'how="Draw them on their keys: Princess Clara, her Dog in his doghouse and the Exit in the small house;', 'wb play')
rep("PLAY</b>  C the Cat, D the Dog in his doghouse, E the Elephant;", "PLAY</b>  C Princess Clara, D her Dog in his doghouse, E the Exit;", 'tc play')
rep('say="“Cat, Dog, Elephant -- Front door, Grandma, Apple garden, Back door.”"', 'say="“Princess Clara, Dog, Exit -- Front door, Grandma, Apple garden, Back door.”"', 'tc say')

for w in ['Elephant', '코끼리', "'Cat'", '고양이']:
    if w in s[s.find('// ─── Chapter 3: The Musical Alphabet'):]: raise SystemExit('left over: ' + w)
open(src, 'w', encoding='utf-8').write(s)
print('patch398 ok')
