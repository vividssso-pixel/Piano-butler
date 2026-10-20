import sys
s=open(sys.argv[1],encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:90],s.count(a)); s=s.replace(a,b)
a=s.index("function AcBar() {"); b=s.index("\n[['ac-bar',",a)
fn=s[a:b]
def frep(a_,b_,n=1):
    global fn
    assert fn.count(a_)==n,(a_[:80],fn.count(a_)); fn=fn.replace(a_,b_)
frep("function AcBar() {","function AcCmp() {")
fn=fn.replace("AC_BARS","AC_CMP")
frep('data-ac-lesson="bar"','data-ac-lesson="cmp"')
frep("let x = 66;","let x = BAR.ks ? 86 : 66;")
frep("const x0 = placed[B.from].x - 17, x1 = B.to === 'bar' ? barAt - 5 : placed[B.to].x - 19, col = AC_BAR_COL[B.g];","const x0 = B.from === 'ks' ? 46 : placed[B.from].x - 17, x1 = B.to === 'bar' ? barAt - 5 : B.to === 'end' ? W - 10 : placed[B.to].x - 19, col = AC_BAR_COL[B.g];")
frep("""<ClefGlyph clef="treble" st="treble" yOf={(d) => y(d)} ink="#26296b"/>""","""<ClefGlyph clef="treble" st="treble" yOf={(d) => y(d)} ink="#26296b"/>
    {BAR.ks && <SharpShape x={54} y={y(38)} color={AC_BAR_COL.s[0]}/>}""")
frep("const title = t('Rules for sharps, flats and naturals', '샵, 플랫, 내추럴의 규칙');","const title = t('Accidental or key signature?', '임시표와 조표');")
frep("{t('A sign covers its own line or space until the bar line. The band shows how far.', '임시표는 자기 줄이나 칸을 세로줄까지 덮어요. 띠가 어디까지인지 보여줘요.')}","{t(BAR.all[0], BAR.all[1])}")
DATA = r"""
// the contrast card: an accidental reaches one note's line or space until the bar line; a key signature reaches every octave, the whole piece (her ACC_EXAMPLES wording)
const AC_CMP = [
  { all: ['An accidental is written on the note. It reaches one line or space, until the bar line.', '임시표는 음표에 직접 써요. 한 줄이나 한 칸에, 세로줄까지 적용돼요.'],
    notes: [{ d: 31, sign: 1, snd: 1, g: 's' }, { d: 32, sign: 0, snd: 0 }, { d: 31, sign: 0, snd: 1, g: 's' }, { d: 31, sign: 0, snd: 0, bar: true }],
    bands: [{ g: 's', d: 31, from: 0, to: 'bar' }],
    steps: [
      { upto: 0, cur: 0, bands: 0, en: 'An accidental is written right on the note: F♯.', ko: '임시표는 음표 바로 앞에 써요: F♯.' },
      { upto: 0, cur: -1, bands: 1, band: 0, en: 'It reaches only this space, and only until the bar line.', ko: '이 칸에만, 세로줄까지만 적용돼요.' },
      { upto: 1, cur: 1, bands: 1, en: 'G is on another line or space: not touched.', ko: 'G는 다른 칸이에요: 닿지 않아요.' },
      { upto: 2, cur: 2, bands: 1, en: 'Another F in the same bar: F♯ too, with no sign.', ko: '같은 마디의 또 다른 F: 표시가 없어도 F♯.' },
      { upto: 3, cur: 3, bands: 1, en: 'New bar: the accidental has stopped. Plain F.', ko: '새 마디: 임시표가 멈췄어요. 그냥 F.' },
    ],
    asks: [[2, 'Same space as the sharp, in the same bar.', '샵과 같은 칸, 같은 마디예요.'], [3, 'New bar: the accidental has stopped.', '새 마디: 임시표가 멈췄어요.'], [1, 'Another space, so plain.', '다른 칸이라 그냥 음이에요.']] },
  { all: ['A key signature is written once, at the start. It reaches every F, in every octave, the whole piece.', '조표는 처음에 한 번만 써요. 모든 F에, 모든 옥타브에, 곡 전체에 적용돼요.'], ks: true,
    notes: [{ d: 31, sign: 0, snd: 1, g: 's' }, { d: 32, sign: 0, snd: 0 }, { d: 38, sign: 0, snd: 1, g: 's' }, { d: 31, sign: 0, snd: 1, g: 's', bar: true }, { d: 38, sign: 0, snd: 1, g: 's' }],
    bands: [{ g: 's', d: 31, from: 'ks', to: 'end' }, { g: 's', d: 38, from: 'ks', to: 'end' }],
    steps: [
      { upto: -1, cur: -1, bands: 0, en: 'A key signature is written once, at the start of the line: F♯.', ko: '조표는 줄의 맨 앞에 한 번만 써요: F♯.' },
      { upto: 0, cur: 0, bands: 1, band: 0, en: 'Every F on this space is F♯. No sign is needed on the notes.', ko: '이 칸의 F는 모두 F♯이에요. 음표에는 표시가 필요 없어요.' },
      { upto: 1, cur: 1, bands: 1, en: 'G is not touched.', ko: 'G는 영향 받지 않아요.' },
      { upto: 2, cur: 2, bands: 2, band: 1, en: 'Every octave too: the high F is F♯.', ko: '모든 옥타브에서요: 높은 F도 F♯이에요.' },
      { upto: 3, cur: 3, bands: 2, en: 'The bar line does not stop it: F♯ in the next bar too.', ko: '세로줄이 멈추지 않아요: 다음 마디에서도 F♯.' },
      { upto: 4, cur: 4, bands: 2, en: 'The whole piece: the high F is F♯ again.', ko: '곡 전체에서: 높은 F도 또 F♯이에요.' },
    ],
    asks: [[0, 'The key signature raises every F.', '조표가 모든 F를 올려요.'], [2, 'The key signature covers every octave.', '조표는 모든 옥타브에 적용돼요.'], [3, 'The key signature does not stop at the bar line.', '조표는 세로줄에서 멈추지 않아요.'], [1, 'G is not touched.', 'G는 영향 받지 않아요.']] },
];
"""
REG = r"""
[['ac-cmp', 'Accidental or key signature?', '임시표와 조표', 'One note until the bar line, or every octave, the whole piece.', '한 음에 세로줄까지, 아니면 모든 옥타브에 곡 전체로.']].forEach(([id, en, ko, benEn, bko]) => {
  TOOLS.push({ id, ch: 'concept', title: en, blurb: benEn, hidden: true, get kicker() { return TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '임시표' : 'Accidentals'); }, C: () => <AcCmp/> });
  TOOL_KO[id] = [ko, bko];
  const tl = TOOLS[TOOLS.length - 1], k = TOOL_KO[id], ti = tl.title, bl = tl.blurb; tl.titleEn = ti; tl.blurbEn = bl;
  Object.defineProperty(tl, 'title', { get: () => (LANG === 'ko' ? k[0] : ti), enumerable: true, configurable: true });
  Object.defineProperty(tl, 'blurb', { get: () => (LANG === 'ko' ? k[1] : bl), enumerable: true, configurable: true });
  TOOL_CONCEPT[id] = 'p-clock';
});
"""
rep("// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(", DATA + fn + "\n" + REG + "// the Toolbox: a concept's book, right under its name (open on screen, or print)\nfunction CbCard(")
rep("'ac-two', 'ac-double', 'chromatic',", "'ac-two', 'ac-double', 'ac-cmp', 'chromatic',")
open(sys.argv[2],'w',encoding='utf-8').write(s);print('ok')
