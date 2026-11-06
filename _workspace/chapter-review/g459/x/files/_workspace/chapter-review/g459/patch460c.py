# Phase 460c: real names in the ledger-lines and tones chapters, the tools and the drills; then a sweep.
import re
B = '/home/claude/pbtest/g460/out/'
s = open(B + 't460b0.src.html').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:120])
    s = s.replace(old, new)

# ── labels and maps ──
rep("'One ladder: Queensland': '발판 하나: 퀸즈랜드', 'One ladder: Kingsland': '발판 하나: 킹스랜드', 'Two ladders, both lands': '발판 둘: 두 나라'",
    "'One ladder: treble clef': '발판 하나: 높은음자리표', 'One ladder: bass clef': '발판 하나: 낮은음자리표', 'Two ladders, both clefs': '발판 둘: 두 음자리표'")
rep("'Between the lands: the same key, two ways': '두 나라 사이: 같은 건반, 두 가지로'", "'Between the staves: the same key, two ways': '두 오선 사이: 같은 건반, 두 가지로'")
rep("'Both lands, fast': '두 나라, 빠르게'", "'Both clefs, fast': '두 음자리표, 빠르게'")
rep("label: 'Both lands, fast',                    ", "label: 'Both clefs, fast',                    ")
rep("label: 'One ladder: Queensland',                        ", "label: 'One ladder: treble clef',                       ")
rep("label: 'One ladder: Kingsland',                         ", "label: 'One ladder: bass clef',                         ")
rep("label: 'Two ladders, both lands',                       ", "label: 'Two ladders, both clefs',                       ")
rep("label: 'Between the lands: the same key, two ways',   ", "label: 'Between the staves: the same key, two ways',  ")
rep("t('Clara\\'s middle C, on her own little ladder between the two lands: the middle of the piano.', '클라라의 가운데 도, 두 나라 사이 자기만의 작은 사다리 발판 위: 피아노의 한가운데.')",
    "t('Clara\\'s middle C, on her own little ladder between the two staves: the middle of the piano.', '클라라의 가운데 도, 두 오선 사이 자기만의 작은 사다리 발판 위: 피아노의 한가운데.')")
rep("blurb: 'The two lands are mirror images: G meets F, C meets C.'", "blurb: 'The two staves are mirror images: G meets F, C meets C.'")
rep("'두 나라는 거울처럼 마주 봐요: G는 F와, C는 C와.'", "'두 오선은 거울처럼 마주 봐요: G는 F와, C는 C와.'")
rep("title: 'Climb out of the lands', blurb:", "title: 'Climb out of the staff', blurb:")
rep("title: 'Between the lands', blurb: 'Borrowed ladders", "title: 'Between the staves', blurb: 'Borrowed ladders")
rep("'ledger-walk': ['두 나라 밖으로 오르내리기',", "'ledger-walk': ['오선 밖으로 오르내리기',")
rep("'ledger-twins': ['두 나라 사이',", "'ledger-twins': ['두 오선 사이',")
rep('watch="Using the Queen\'s sayings in the King\'s land.', 'watch="Using the treble clef\'s sayings in the bass clef.')

# ── ledger lines: the place words ──
rep("const llLand = (clef) => clef === 'treble' ? t('Queensland', '퀸즈랜드') : t('Kingsland', '킹스랜드');",
    "const llLand = (clef) => clef === 'treble' ? t('the treble staff', '높은음자리표 오선') : t('the bass staff', '낮은음자리표 오선');")
rep("(ko ? L + ' ' + (k / 2 + 1) + '번 줄' : L + ' line ' + (k / 2 + 1)) : (ko ? L + ' ' + ((k + 1) / 2) + '번 칸' : L + ' space ' + ((k + 1) / 2))",
    "(ko ? L + ' ' + (k / 2 + 1) + '번 줄' : 'line ' + (k / 2 + 1) + ' of ' + L) : (ko ? L + ' ' + ((k + 1) / 2) + '번 칸' : 'space ' + ((k + 1) / 2) + ' of ' + L)")

# ── ledger lines: the book's words ──
rep("덧줄은 나라 밖으로 나가는 {A('B2', '사다리의 발판')}이에요. 퀸즈랜드 위로는 새의 하늘로, 킹스랜드 아래로는 거북의 바다로 가요.",
    "덧줄은 오선 밖으로 나가는 {A('B2', '사다리의 발판')}이에요. 높은음자리표 오선 위로는 새의 하늘로, 낮은음자리표 오선 아래로는 거북의 바다로 가요.")
rep("Ledger lines are {A('B2', 'little ladders')} out of the lands: up from Queensland into the bird's sky, down from Kingsland into the turtle's sea.",
    "Ledger lines are {A('B2', 'little ladders')} out of the staff: up from the treble staff into the bird's sky, down from the bass staff into the turtle's sea.")
rep("[t('Between the lands', '두 나라 사이'), 5]", "[t('Between the staves', '두 오선 사이'), 5]")
rep("title={t('Between the lands', '두 나라 사이')}>", "title={t('Between the staves', '두 오선 사이')}>")
rep("t('read up to three ladders above Queensland', '퀸즈랜드 위로 발판 세 개까지 읽을 수 있어요')", "t('read up to three ladders above the treble staff', '높은음자리표 오선 위로 발판 세 개까지 읽을 수 있어요')")
rep("t('read up to three ladders below Kingsland', '킹스랜드 아래로 발판 세 개까지 읽을 수 있어요')", "t('read up to three ladders below the bass staff', '낮은음자리표 오선 아래로 발판 세 개까지 읽을 수 있어요')")
rep("t('read the ladders between the lands both ways', '두 나라 사이의 발판을 두 가지로 읽을 수 있어요')", "t('read the ladders between the staves both ways', '두 오선 사이의 발판을 두 가지로 읽을 수 있어요')")
rep("t('I can read the ladders between the lands, both ways', '두 나라 사이의 발판을 두 가지로 읽을 수 있어요')", "t('I can read the ladders between the staves, both ways', '두 오선 사이의 발판을 두 가지로 읽을 수 있어요')")
rep("t('I can climb out of Queensland: G, A, B, C, D, E', '퀸즈랜드 밖으로 올라갈 수 있어요: G, A, B, C, D, E')", "t('I can climb up out of the treble staff: G, A, B, C, D, E', '높은음자리표 오선 밖으로 올라갈 수 있어요: G, A, B, C, D, E')")
rep("t('I can climb out of Kingsland: F, E, D, C, B, A', '킹스랜드 밖으로 내려갈 수 있어요: F, E, D, C, B, A')", "t('I can climb down out of the bass staff: F, E, D, C, B, A', '낮은음자리표 오선 밖으로 내려갈 수 있어요: F, E, D, C, B, A')")
rep("<>퀸즈랜드 위 발판의 <b>A</b>를 쳐요.", "<>높은음자리표 오선 위 발판의 <b>A</b>를 쳐요.")
rep("<>Play the <b>A</b> on the ladder above Queensland.", "<>Play the <b>A</b> on the ladder above the treble staff.")
rep("<>퀸즈랜드 맨 윗줄 <b>F</b>에서 출발해요.", "<>높은음자리표 맨 윗줄 <b>F</b>에서 출발해요.")
rep("<>Start on Queensland's top line, <b>F</b>.", "<>Start on the treble staff's top line, <b>F</b>.")
rep("t('Out of Queensland: G in the space, then A, C, E on the ladders.', '퀸즈랜드 밖으로: 칸에 G, 그다음 발판에 A, C, E.')", "t('Up out of the treble staff: G in the space, then A, C, E on the ladders.', '높은음자리표 오선 위로: 칸에 G, 그다음 발판에 A, C, E.')")
rep("<>킹스랜드 맨 아랫줄 <b>G</b>에서 내려가요.", "<>낮은음자리표 맨 아랫줄 <b>G</b>에서 내려가요.")
rep("<>Climb down from Kingsland's bottom line, <b>G</b>.", "<>Climb down from the bass staff's bottom line, <b>G</b>.")
rep("t('Out of Kingsland: F in the space, then E, C, A on the ladders.', '킹스랜드 밖으로: 칸에 F, 그다음 발판에 E, C, A.')", "t('Down out of the bass staff: F in the space, then E, C, A on the ladders.', '낮은음자리표 오선 아래로: 칸에 F, 그다음 발판에 E, C, A.')")
rep("t('Between the lands, the ladders are borrowed: the same key, two ways.', '두 나라 사이의 발판은 빌려 온 줄: 같은 건반, 두 가지로.')", "t('Between the staves, the ladders are borrowed: the same key, two ways.', '두 오선 사이의 발판은 빌려 온 줄: 같은 건반, 두 가지로.')")
rep("t('Tap a note between the lands: see it in Queensland and in Kingsland, one key on the piano.', '두 나라 사이의 음을 눌러 봐요: 퀸즈랜드에서도, 킹스랜드에서도, 피아노에서는 건반 하나예요.')",
    "t('Tap a note between the staves: see it in the treble clef and in the bass clef, one key on the piano.', '두 오선 사이의 음을 눌러 봐요: 높은음자리표에서도, 낮은음자리표에서도, 피아노에서는 건반 하나예요.')")
rep("t('Start on Queensland\\'s top line, F.", "t('Start on the treble staff\\'s top line, F.")
rep("'퀸즈랜드 맨 윗줄 F에서 출발해요.", "'높은음자리표 맨 윗줄 F에서 출발해요.")
rep("t('Start on Kingsland\\'s bottom line, G.", "t('Start on the bass staff\\'s bottom line, G.")
rep("'킹스랜드 맨 아랫줄 G에서 출발해요.", "'낮은음자리표 맨 아랫줄 G에서 출발해요.")
rep("t('Up out of Queensland', '퀸즈랜드 위로')], ['bass', t('Down out of Kingsland', '킹스랜드 아래로')]", "t('Up out of the treble staff', '높은음자리표 오선 위로')], ['bass', t('Down out of the bass staff', '낮은음자리표 오선 아래로')]")

# the ledger book's page 5 and its step (both languages)
i = s.index("{A('B6', <>두 나라 사이의 발판은")
j = s.index("</LbSay>", i)
blk = s[i:j]
blk2 = (blk.replace('두 나라 사이의', '두 오선 사이의').replace('퀸즈랜드 아래', '높은음자리표 오선 아래').replace('킹스랜드 <b>맨 윗줄', '낮은음자리표 <b>맨 윗줄')
        .replace('킹스랜드 위', '낮은음자리표 오선 위').replace('퀸즈랜드 <b>맨 아랫줄', '높은음자리표 <b>맨 아랫줄').replace('어느 나라에서 봐도', '어느 오선에서 봐도')
        .replace('자기 나라에', '자기 오선에')
        .replace('The ladders between the lands', 'The ladders between the staves').replace('ladder 2 under Queensland', 'ladder 2 under the treble staff')
        .replace("Kingsland's <b>top line", "the bass staff's <b>top line").replace('ladder 2 over Kingsland', 'ladder 2 over the bass staff')
        .replace("Queensland's <b>bottom line", "the treble staff's <b>bottom line").replace('seen from either land', 'seen from either staff')
        .replace('stay in its own land', 'stay on its own staff'))
assert 'Queensland' not in blk2 and 'Kingsland' not in blk2 and '퀸즈' not in blk2 and '킹스' not in blk2 and '나라' not in blk2 and ' land' not in blk2, blk2
s = s[:i] + blk2 + s[j:]
rep("<>오른손으로 퀸즈랜드 아래로 내려가요: <b>E D C B A</b>, \"줄, 칸, 발판 1, 칸, 발판 2\", 그리고 킹스랜드 맨 윗줄 A를 짚어요.</>",
    "<>오른손으로 높은음자리표 오선 아래로 내려가요: <b>E D C B A</b>, \"줄, 칸, 발판 1, 칸, 발판 2\", 그리고 낮은음자리표 맨 윗줄 A를 짚어요.</>")
rep("<>With your right hand, climb down out of Queensland: <b>E D C B A</b>, \"line, space, ladder 1, space, ladder 2\", then point to Kingsland's top line, A.</>",
    "<>With your right hand, climb down out of the treble staff: <b>E D C B A</b>, \"line, space, ladder 1, space, ladder 2\", then point to the bass staff's top line, A.</>")

# ledger Workbook and Teacher copy
rep('title="Name the sky notes" how="Count up from Queensland\'s top line, F,', 'title="Name the sky notes" how="Count up from the treble staff\'s top line, F,')
rep('title="Name the sea notes" how="Count down from Kingsland\'s bottom line, G,', 'title="Name the sea notes" how="Count down from the bass staff\'s bottom line, G,')
rep('title="The same key in the other land" how="1-3: draw the same key in Kingsland. 4-6: draw it in Queensland. Write the letter."',
    'title="The same key on the other staff" how="1-3: draw the same key on the bass staff. 4-6: draw it on the treble staff. Write the letter."')
rep('how="Whose land is the note in? Count out from that land, then write the letter."', 'how="Which staff is the note on? Count out from that staff, then write the letter."')
rep('how="Each picture has a note in each land.', 'how="Each picture has a note on each staff.')
rep("bkSec('D', 'Between the lands: count out from the note\\'s land, then name it.')", "bkSec('D', 'Between the staves: count out from the note\\'s staff, then name it.')")
rep('<TcBlock page={5} title="Between the lands"', '<TcBlock page={5} title="Between the staves"')
rep("(st === 'treble' ? 'Kingsland ' : 'Queensland ')", "(st === 'treble' ? 'bass staff ' : 'treble staff ')")
rep('watch="Reading a note under Queensland as a Kingsland note: it belongs to the land it hangs from, so count out from Queensland. The same key in the other land is written another way."',
    'watch="Reading a note under the treble staff as a bass staff note: it belongs to the staff it hangs from, so count out from the treble staff. The same key on the other staff is written another way."')
rep('say="“Whose land is it in? Count out from that land.”"', 'say="“Which staff is it on? Count out from that staff.”"')
rep('say="“Count out from the land, or hop from the nearest C.”"', 'say="“Count out from the staff, or hop from the nearest C.”"')

# ── tones ──
rep("<>오른손으로 퀸즈랜드의 네 음을 읽고 쳐요:", "<>오른손으로 높은음자리표의 네 음을 읽고 쳐요:")
rep("<>왼손으로 킹스랜드의 네 음을 읽고 쳐요:", "<>왼손으로 낮은음자리표의 네 음을 읽고 쳐요:")
rep("<>Read and play Queensland's four notes with the right hand:", "<>Read and play the treble clef's four notes with the right hand:")
rep("<>Read and play Kingsland's four with the left hand:", "<>Read and play the bass clef's four with the left hand:")
rep("t('Queensland, ', '퀸즈랜드, ') : t('Kingsland, ', '킹스랜드, ')", "t('treble clef, ', '높은음자리표, ') : t('bass clef, ', '낮은음자리표, ')")

# ── the sweep: every remaining picture label and plain name ──
rep("t('Queensland', '퀸즈랜드')", "t('Treble clef', '높은음자리표')", s.count("t('Queensland', '퀸즈랜드')"))
rep("t('Kingsland', '킹스랜드')", "t('Bass clef', '낮은음자리표')", s.count("t('Kingsland', '킹스랜드')"))

def sweep_line(L):
    if L.lstrip().startswith('//'):
        return L
    for land, staff in (('Queensland', 'treble'), ('Kingsland', 'bass')):
        L = re.sub(r'\b(above|over|under|below|out of|from|into) ' + land + r'\b', r'\1 the ' + staff + ' staff', L)
        L = re.sub(r"\b" + land + r"'s\b", 'the ' + staff + " staff's", L)
        L = re.sub(r"\b" + land + r"\\'s\b", 'the ' + staff + " staff\\'s", L)
        L = re.sub(r'\bin ' + land + r'\b', 'in the ' + staff + ' clef', L)
        L = re.sub(r"(?<=t\(')" + land + r' with', 'The ' + staff + ' staff with', L)
    L = L.replace('between the lands', 'between the staves').replace('the two lands', 'the two staves')
    ko = (('퀸즈랜드 위로', '높은음자리표 오선 위로'), ('퀸즈랜드 아래', '높은음자리표 오선 아래'), ('퀸즈랜드 위 ', '높은음자리표 오선 위 '), ('퀸즈랜드 맨', '높은음자리표 맨'),
          ('킹스랜드 아래', '낮은음자리표 오선 아래'), ('킹스랜드 위', '낮은음자리표 오선 위'), ('킹스랜드 맨', '낮은음자리표 맨'),
          ('퀸즈랜드', '높은음자리표'), ('킹스랜드', '낮은음자리표'), ('두 나라 사이', '두 오선 사이'), ('두 나라', '두 오선'))
    for a, b in ko:
        L = L.replace(a, b)
    return L

lines = s.split('\n')
# the chapter 7 opener keeps the story names, said once
keep = [k for k, L in enumerate(lines) if "It is the Queen\\'s land, Queensland." in L]
assert len(keep) == 1
for k, L in enumerate(lines):
    if k in keep:
        continue
    lines[k] = sweep_line(L)
s = '\n'.join(lines)
# sentence starts after the sweep
s = re.sub(r"(t\('|<>|\. |how=\")the (treble|bass) staff", lambda m: m.group(1) + 'The ' + m.group(2) + ' staff', s)

s = s.replace("const llLand = (clef) => clef === 'treble' ? t('The treble staff', '높은음자리표 오선') : t('The bass staff', '낮은음자리표 오선');", "const llLand = (clef) => clef === 'treble' ? t('the treble staff', '높은음자리표 오선') : t('the bass staff', '낮은음자리표 오선');")
rep("'네 음이 있는 높은음자리표, 기호는", "'네 음이 있는 높은음자리표 오선, 기호는")
rep("'네 음과 기호가 있는 낮은음자리표: 왕의", "'네 음과 기호가 있는 낮은음자리표 오선: 왕의")
rep("this book counts out of each land and reads from the five Cs instead.", "this book counts out of each staff and reads from the five Cs instead.")
rep("Grade 1 one ladder above and below both lands; Grade 2 up to three.", "Grade 1 one ladder above and below both staves; Grade 2 up to three.")
open(B + 't460b.src.html', 'w').write(s)
print('ok')

# the clef chooser on paper: two words that never wrap, a little tighter beside an answer box
s = open(B + 't460b.src.html').read()
rep("const wsChoose = (words, on) => <span style={{display:'inline-flex',gap:6}}>{words.map(w => <span key={w} style={{fontSize:12.5,fontWeight:800,color:on === w ? BK.coral : BK.ink,border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:12,padding:'0 7px',lineHeight:'19px'}}>{w}</span>)}</span>;",
    "const wsChoose = (words, on, tight) => <span style={{display:'inline-flex',gap:tight ? 2 : 6,flexShrink:0}}>{words.map(w => <span key={w} style={{fontSize:12.5,fontWeight:800,color:on === w ? BK.coral : BK.ink,border:'1.5px solid ' + (on === w ? BK.coral : 'transparent'),borderRadius:12,padding:tight ? '0 4px' : '0 7px',lineHeight:'19px',whiteSpace:'nowrap'}}>{w}</span>)}</span>;")
rep("{wsChoose(['treble', 'bass'])}{bkBox(34, 30)}", "{wsChoose(['treble', 'bass'], null, true)}{bkBox(34, 30)}")
rep("{choose && wsChoose(['treble', 'bass'])}{bkBox(34, 30)}", "{choose && wsChoose(['treble', 'bass'], null, true)}{bkBox(34, 30)}")
open(B + 't460b.src.html', 'w').write(s)
print('ok2')
