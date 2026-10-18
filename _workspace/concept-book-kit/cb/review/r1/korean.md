# Phase 485 review, round 1: Korean (the concept book "스케일과 조")

Reviewer side: every Korean word, print and screen; natural for a child of 8+ and a parent; the app's own terms; dictionary
style (rule 14); line breaks (rule 8: `ㄹ 수 있어요` on one line; rule 8 ch. 19: a sign never parts from the syllable after
it).

What I read: every second argument of `t()` / `X()` in `cbscales.jsx` (lines 1-376), the eight Korean print pages and the
screen lesson. I rendered them again with the harness (`review/r1/korean/shot.js`, `pages.js`) because two of the shots in
`cb/shots/` are older than the build. `cb-ko-3.png` and `step-ko-3.png` still show "그다음 워크북의 건반 시계에서 그 조를
색칠해요", and the source now has "만든 조에 표시해요". The new renders are `review/r1/korean/pko-1..8.png`, `screen-ko-390.png`
and `screen-ko-360.png`. A script listed every place a line breaks (`print-lines.txt`, `screen-lines-390/360.txt`). For each
Korean term I compared the app's own wording in `t485.src.html`: chapter 16 (`sscLbPages`), chapter 19 (`skgLbPages`,
`skgKo`), chapter 21 (`ivx…`), chapter 27, `TOOL_KO` and `CAT_KO`.

Line numbers are `cbscales.jsx` unless marked `src:` (= `t485.src.html`).

---

## Blockers

### B1. p4 "조표" definition says 줄마다. Rule 8 forbids it, and it teaches something wrong
- **Where.** Print p4 and screen step 3, the first definition (line 295).
- **What is wrong.** "음계의 샤프나 플랫을, **줄마다** 맨 앞의 음자리표 뒤에 한 번 써요. 곡 전체에서, 모든 옥타브에 **유효해요**."
  Rule 8 (chapter 19) says 조표 is written "오선마다 맨 앞, never 줄마다, since 줄 is a staff line here". A child who has
  learnt 줄 = a staff line (chapters 6 and 7) reads this as "on every line of the staff". 유효해요 is also not the app's verb.
  Chapters 17 and 19 say 효과가 있어요, and chapter 19 says "곡 끝까지, 모든 옥타브에서 효과가 있어요".
- **Fix.** Use chapter 19's own words:
  `'음계의 샤프나 플랫을 오선마다 맨 앞, 음자리표 바로 뒤에 한 번 적어요. 곡 끝까지, 모든 옥타브에서 효과가 있어요.'`

### B2. A sharp or flat splits from its syllable: "C♭ / 장조", "F♯ / 장조", "D♭ / 장조"
- **Where.**
  - Print p3, definition "두 이름" (line 283). The printed line ends "B장조와 C♭" and the next line starts "장조도 그래요."
  - Screen step 2 ("어느 음에서나"): "C♯장조와 D♭ / 장조".
  - Screen step 4 ("5도권"), the third key note: "F♯ / 장조와 G♭장조는".
  - CbKeyPad on G♭: "· F♯ / 장조(샤프 여섯)와 건반이 같아요" (line 58).
- **What is wrong.** A word is broken in two. Rule 8 (chapter 19) says "a sign never parts from the syllable after it (a
  word joiner)". Chapter 19 already does this in `skgKo` (src: 45416).
  `sscNbKo`, which this book uses through `X5 = sscT` and in `checksRows`, has no such rule.
- **Fix.** Give the book its own Korean helper that adds `skgKo`'s rules to `sscNbKo`. Use it for `X5`, for `checksRows`
  (line 236) and for the pad's line (line 58). I tested it on the book's strings (`review/r1/korean/nbtest.js`). The same
  helper also fixes M3, part of M4 and m2.
  ```js
  const cbNbKo = (x) => sscNbKo(x)
    .replace(/([♯♭])(?=[가-힣(])/g, '$1⁠')                    // F♯장조, C♭장조, G♯를 (as skgKo, ch. 19)
    .replace(/(\S) 수(도)? 있어요/g, '$1 수$2 있어요')      // 말할 수 있어요, 골라 줄 수도 있어요 (rule 8)
    .replace(/조 이름/g, '조 이름')
    .replace(/한 (걸음|칸|번|손|옥타브)/g, '한 $1')
    .replace(/([온반]), ([온반])(?=$|\.| 걸음)/g, '$1, $2')   // never a lone '반.' at a line start
    .replace(/(?<![A-Za-z])([A-G][♯♭]?) (?=[A-G][♯♭]?(?![A-Za-z]))/g, '$1 ');   // a list of note names stays whole
  const X5 = (en, ko) => sscSx(LANG === 'ko' ? cbNbKo(ko) : sscNbEn(en));
  ```
  In `checksRows` (line 236), change `sscNbKo(x)` to `cbNbKo(x)`. For line 58, wrap the Korean string in `cbNbKo(...)` before
  `sscSx`.

---

## Must fix

### M1. "반대 방향" sits next to the app's "반시계 방향" on the same screen
- **Where.**
  - p5 legend (line 188).
  - p5 At the piano 2 (line 314).
  - p5 REMEMBER (line 316).
  - The aria-labels at lines 154 and 185.
- **What is wrong.** Chapter 19 and the circle-of-fifths tool (shown inside this book's screen step 4) say **반시계 방향**. On
  screen step 4 a child reads "반대 방향" in the legend and "반시계 방향" in the tool just below. 반대 방향 is also the app's
  word for contrary motion (MotionTypes).
- **Fix.**
  - Line 188: `'반시계 방향: 한 칸마다 5도 아래의 조, 플랫이 하나 더.'`
  - Line 316: `'시계 방향: 샤프 하나 더. 반시계 방향: 플랫 하나 더.'`
  - Line 314: see M6.
  - Lines 154 and 185: change `반대 방향으로` to `반시계 방향으로`.

### M2. The opener: the drop capital splits "모든", and the line starts with a lone "반."
- **Where.** Print p1, the opener LbSay (lines 244-246). The screen opener has the orphan too.
- **What is wrong.**
  - The drop capital boxes "모" and the line goes on "든 장음계는…". The finished Korean openers start on a word of one
    syllable, so the drop capital is a whole word: 한 음에서 (ch. 16), 두 음 (ch. 21), 세 음 (ch. 22).
  - The step list breaks before its last item, so line 2 starts with "반." (print and the 390 px screen).
  - "5도권은 열두 조를 차례로 놓아요" makes the circle the subject of 놓다. That reads oddly.
- **Fix** (Korean branch of line 245):
  ```jsx
  <><b>한 가지 규칙</b>으로 모든 장음계를 만들어요. 어느 음에서 시작하든 온, 온, 반, 온, 온, 온,{' '}반 걸음이에요. 음계의 샤프나 플랫은 그 조의 <b>조표</b>가 되고, <b>5도권</b>에는 열두 조가 차례로 놓여 있어요.</>
  ```
  The drop capital is now "한", a whole word.

### M3. `ㄹ 수 있어요` and `조 이름` break across lines
- **Where.**
  - The "By the end" list on p1 and the five checks on p8 (print and screen): "만들 수 / 있어요", "말할 수 / 있어요",
    "조 / 이름을".
  - The p7 intro on screen: "골라 줄 / 수도 있어요".
  - p4 "조 이름" definition: "…두 번째 플랫이 조 / 이름.".
- **What is wrong.** Rule 8 keeps `ㄹ 수 있어요` on one line. `sscNbKo` only covers 칠 수 있어요.
- **Fix.** The `cbNbKo` helper in B2. It is verified on all five check rows.

### M4. 온+반 breaks inside itself, and step patterns leave one word alone on a line
- **Where.**
  - p6 small clocks on screen (two columns at 360 and 390 px): "온 반 온 온 반 온 / +반 반" and "온 온 온+반 온 온 / +반".
  - Lone last tokens: "온 온 반 온 온 온 / 반" and "온 반 온 온 반 온 / 온".
  - `cbSteps`, line 31.
- **Fix.** Line 31. Tie 온+반 together and keep the last token with the one before it. For the chromatic scale use one short
  phrase instead of twelve 반s that wrap; the line above already says 열두 건반 모두.
  ```js
  const cbSteps = (pat) => { if (pat.length === 12) return t('S S S S S S S S S S S S', '반 걸음만 열두 번');
    const s = pat.map((o, i) => { const g = ((i + 1 < pat.length ? pat[i + 1] : 12) - o); return g === 1 ? t('S', '반') : g === 2 ? t('T', '온') : t('T+S', '온⁠+⁠반'); });
    return s.slice(0, -1).join(' ') + ' ' + s[s.length - 1]; };
  ```
  The English branch of the chromatic case is only a placeholder that keeps today's English. The English reviewer decides
  it.

### M5. Shapes pad: 조 where the English means a piano key
- **Where.** CbShapesPad note (line 78).
- **What is wrong.** "모양을 고르고, 시계에서 **조를** 눌러 그 음에서 시작해요." Here "a key on the clock" is a piano key
  (건반), and the sentence then says "그 음". With 조 the sentence mixes a tonality and a note, and it is unclear for minor
  and chromatic shapes. CbKeyPad (line 49) may keep 조: there you do pick a key.
- **Fix.** `'모양을 고르고, 시계에서 건반을 눌러 그 음에서 시작해요.'`

### M6. p5 At the piano: "5도권의 조를 쳐요". You cannot play a 조
- **Where.** p5 At the piano steps 1 and 2 (lines 313-314).
- **What is wrong.** "Play the keys of the circle" means play each key's note. In Korean "조를 쳐요" is the wrong
  collocation. Step 2 also has no verb for playing ("반대 방향으로: F B♭ …, 플랫이 몇 개인지 말해요").
- **Fix.**
  - Line 313: `'5도권을 따라 시계 방향으로 각 조의 으뜸음을 쳐요: C G D A E B, 한 칸마다 5도 위예요. 조마다 샤프가 몇 개인지 말해요.'`
  - Line 314: `'이번에는 C에서 반시계 방향으로 쳐요: F B♭ E♭ A♭ D♭ G♭. 조마다 플랫이 몇 개인지 말해요.'`

### M7. "음의 번호" is defined with itself, and its other name is missing
- **Where.** p2, third definition (line 269).
- **What is wrong.**
  - "음의 번호: 음계에서 **음의 번호**, 1부터 8까지." is circular. Chapter 13's review fixed the same fault ('빠르기 defined
    with itself').
  - Chapter 16 gives the other name, 음도 (rule 8 ch. 16: "음의 번호 (its other name 음도)"); this book drops it.
  - "8은 다시 으뜸음." is a fragment.
- **Fix.** `'음계의 음마다 아래에서부터 붙이는 번호, 1에서 8까지. 1번 음과 8번 음은 음계의 집 같은 으뜸음이에요. 다른 이름은 음도예요.'`

### M8. 한 걸음 is used against the app's own meaning
- **Where.**
  - p6, "다른 음계" definition (line 325): "반음계: 열두 건반 모두, **한 걸음마다** 반 걸음." On print and screen it also
    breaks "한 / 걸음마다".
  - The shapes-pad label for the chromatic shape (line 82): "모든 건반, 한 걸음마다 반 걸음".
- **What is wrong.** In the app, 한 걸음 is a step to the next letter, a 2nd (rule 8, chapter 9). The p2 definition of 음계
  uses it that way too. A chromatic scale does not go to the next letter each time (C to C♯), so "한 걸음마다 반 걸음" mixes
  two terms in one phrase.
- **Fix.**
  - Line 325: `'5음음계는 장음계에서 4번과 7번 음을 뺀 음계예요. 반음계는 열두 건반을 모두 반 걸음씩 가는 음계예요.'`
  - Line 82: `'열두 건반 모두, 반 걸음씩'`

### M9. The tool names on p7 say 스케일 next to the book's 장음계 and 화성단음계
- **Where.** p7 ladder, "Tools" rows (`TOOL_KO`, src: 18838-18839). They show "장조 스케일 만들기" in the second row and "화성
  단조 스케일 만들기" in the third. The same tool sits on screen step 2 under the book's own "장음계" definitions.
- **What is wrong.**
  - The book (and chapter 16) says 장음계 and 화성단음계 every time. The tool beside it says 장조 스케일 and 화성 단조 스케일.
  - The third row's text says "가락단음계" while its tool builds the harmonic minor. That pairing is for the theory reviewer.
- **Fix** (src: 18838-18839):
  - `'build-major': ['장음계 만들기', '온 온 반 온 온 온 반, 한 걸음씩.']`
  - `'build-minor': ['화성단음계 만들기', '온+반 걸음이 있는 단음계.']`
  - Keep 스케일 찾기 (the scale finder); 스케일 is the other name and the concept's name.

### M10. The ladder labels are not parallel, and one is not finished
- **Where.** p7 (lines 201-204): 처음 / 그다음 / **더 나아가** / 나중에.
- **What is wrong.** 더 나아가 is a verb form waiting for its next word ("더 나아가 …"). The four labels also mix a noun (처음),
  an adverb (그다음) and an adverb with its particle (나중에). This ladder is the model for the twelve books to come, so settle
  it now.
- **Fix.** Four adverbs that read the same way:
  - Line 201: `t('First', '처음에')`
  - Line 202: `t('Then', '그다음에')`
  - Line 203: `t('Further', '더 나아가서')`
  - Line 204: `t('Later', '나중에')`

### M11. The books say "선생님이…", and they no longer assume who is teaching
- **Where.** p3 At the piano 1 (line 286); p4 At the piano 2 (line 301). Line 335 (선생님이 나의 단계를…) may stay: the
  teacher sets the student's keys in the dashboard ("선생님이 정한 나의 조").
- **What is wrong.** Since Phase 392 the books never assume a teacher. No finished Lesson Book has "선생님이 …" in an At the
  piano step. Chapter 19 does the same task alone: "그림의 이름을 가려요. 조표를 하나씩 가리키며 개수를 세고 조 이름을
  말해요."
- **Fix.**
  - Line 286: `'조를 하나 골라요. 걸음대로 음계를 올라가며 음이름을 하나씩 말해요.'`
  - Line 301: `'그림의 조 이름을 가려요. 샤프나 플랫을 하나씩 가리키며 개수를 세고 조 이름을 말해요. 그다음 그 음계를 쳐요.'`
  - The English for both is the English reviewer's to word.

### M12. The five checks on screen say "2~6쪽"
- **Where.** Screen step 7 (line 341). On screen the five pages are steps 1-5 of 7. There are no pages.
- **Fix.** Give the screen its own Korean, for example `lbScreen() ? '1~5단계를 하나씩 펴고 피아노 앞에서 보여 줘요.' : '2~6쪽을…'`.
  Chapter 16's screen lesson has the same line, so this is a series-wide fix.

---

## Minor

### m1. 음 이름 should be 음이름
- **Where.** Lines 282 and 286.
- **What is wrong.** The app writes 음이름 as one word (59 times); 음 이름 appears only in a few older tools.
- **Fix.** Write 음이름 (already done in the replacements in M11 and m6).

### m2. The opener and REMEMBER still leave a lone "반." on screen
- **Where.** Lines 268 and 275, and check 1 on screen ("…온, 온, 온, / 반").
- **Fix.** The `cbNbKo` last-pair rule (B2) keeps "온, 반" together. M2 fixes the opener.

### m3. 코랄색 should be 산호색
- **Where.** Aria-labels at lines 102, 154, 166 and 173.
- **What is wrong.** The app's alt text says **산호색** (94 times). 코랄색 appears once, for the Queen. Line 173 also has
  translationese: "걸음이 그 음을 요구해요".
- **Fix.**
  - Lines 102, 154, 166 and 173: `코랄색` → `산호색`.
  - Line 173, end: `'…3번과 7번 음 F♯와 C♯는 산호색: 걸음을 맞추려면 이 두 음이 필요해요.'`

### m4. The p2 "장음계" definition repeats its list
- **Where.** Line 268.
- **What is wrong.** "…온, 온, 반 … 반 걸음으로 올라가요. 온음과 반음으로는 온 온 반 온 온 온 반." In Korean both 온 걸음 and
  온음 shorten to 온, so the second sentence repeats the first. It also breaks "…온 / 온 반…". Chapter 16 has the same
  sentence; fix it there too.
- **Fix.** Use rule 8's "다른 이름" form:
  `'여덟 음이 온, 온, 반, 온, 온, 온, 반 걸음으로 올라가요. 온 걸음의 다른 이름은 온음, 반 걸음의 다른 이름은 반음이에요.'`

### m5. The p2 At the piano step needs quotation marks
- **Where.** Line 272.
- **What is wrong.** Chapter 16 quotes the words to say: "온" 또는 "반"이라고.
- **Fix.** `'C에서 C장조 음계를 올라가며, 두 건반 사이마다 "온" 또는 "반"이라고 말해요.'`

### m6. p3's title and term "어느 음에서나" is a fragment, and its definition switches to 조
- **Where.** Line 278 (title), line 251 (TOC), line 281 (definition).
- **What is wrong.** As a page and step title, "어느 음에서나" reads unfinished. As a dictionary term, its definition
  switches to "그 조의 음", which mixes 음 and 조.
- **Fix.**
  - Title (line 278) and TOC (line 251): `'어느 음에서나 장음계'`.
  - Definition (line 281): `'고른 음을 으뜸음으로 삼아 같은 걸음으로 올라가요: 온, 온, 반, 온, 온, 온, 반.'`
  - Line 282 (글자는 한 번씩):
    `'일곱 글자를 차례로 한 번씩 써서 음이름을 붙여요. 걸음을 맞추려고 검은건반을 쳐야 하면, 그 글자에 샤프나 플랫을 붙여요. 그래서 D장조에는 G♭이 아니라 F♯가 있어요.'`
  - The particles are right: G♭이, F♯가.

### m7. "두 이름": use the app's "같은 건반, 두 이름" (rule 8)
- **Where.** Line 283.
- **What is wrong.** The app says "건반 하나, 이름 둘" (ch. 11), "같은 자리, 두 이름" and "한 건반의 두 이름" (CAT_KO). "두
  이름" alone is a fragment as a term.
- **Fix.**
  - Term: `t('two names', '같은 건반, 두 이름')`
  - Definition: `'F♯장조와 G♭장조는 같은 건반에서 치고, 이름만 달라요. C♯장조와 D♭장조, B장조와 C♭장조도 그래요.'`

### m8. p3 At the piano 2 is vague
- **Where.** Line 287.
- **What is wrong.** "만든 조에 표시해요": mark what, where?
- **Fix.** `'표에서 음을 하나씩 확인하고, 만든 조의 줄에 ✓ 표시를 해요.'`

### m9. The p4 "순서" and "조 이름" definitions are telegraphic and translated word for word
- **Where.** Line 296 (순서) and line 297 (조 이름).
- **What is wrong.** Line 296 has "샤프의 거꾸로예요" and "…처음 세 개를 가져요" (가지다 for 'has'). Line 297 has two colons in
  each half ("샤프: … 조 이름. 플랫: …"); the house rule is one colon a sentence.
- **Fix.**
  - Line 296: `'샤프는 언제나 F C G D A E B 순서예요. 플랫은 B E A D G C F, 샤프 순서를 거꾸로 한 거예요. 샤프가 셋인 조에는 앞의 셋, F♯ C♯ G♯가 붙어요.'`
  - Line 297: `'샤프가 있으면 마지막 샤프보다 반 걸음 위가 조 이름이에요. 플랫이 있으면 끝에서 두 번째 플랫이 조 이름이에요. 플랫이 하나뿐이면 F장조예요.'`

### m10. The p5 definitions are fragments with two colons, and "5도" does not count the way chapter 21 does
- **Where.** Line 309 (5도권) and line 310 (5도).
- **What is wrong.** Chapter 21 counts "두 음을 모두 세어". 양 끝 is chapter 18's word for the two ends of the keyboard.
- **Fix.**
  - Line 309: `'열두 장조를 둥글게 놓은 거예요. 맨 위는 C예요. 시계 방향으로 한 칸마다 5도 위의 조가 오고, 샤프가 하나 늘거나 플랫이 하나 줄어요.'`
  - Line 310: `'두 음을 모두 세어 음이름 다섯 개 거리예요(C D E F G). G는 C장조의 5번 음이에요.'`

### m11. The p6 definitions put two colons in one line
- **Where.** Lines 322-324.
- **What is wrong.** The colons are in the Korean, after the term's own colon. The natural minor is also used before it is
  named.
- **Fix.**
  - Line 322: `'장음계의 6번 음에서 시작하고 그 장조와 조표가 같은 단조예요. A단조는 C장조의 나란한조예요. 조표 그대로 치는 자연단음계의 걸음은 온 반 온 온 반 온 온이에요.'`
  - Line 323: `'자연단음계에서 7번 음을 반 걸음 올린 음계예요. A단조에서는 G♯예요.'`
  - Line 324: `'올라갈 때는 6번과 7번 음을 반 걸음 올리고, 내려올 때는 자연단음계로 내려와요.'`

### m12. p6 At the piano 1: "새로운 집" needs its word
- **Where.** Line 328.
- **Fix.** `'C장조 음계를 치고, 그다음 A단조 자연단음계를 쳐요: 흰건반은 같고, 집(으뜸음)만 A로 바뀌어요.'`

### m13. The shape names
- **Where.**
  - CB_SHAPES line 28: the chromatic name "C에서 시작하는 반음계" wraps to three lines in the phone's two columns.
  - Line 27: "C 5음음계". With line 28 changed, the two read the same way (C 5음음계, C 반음계).
  - The aria-labels at lines 81 and 139 build "C 장음계", "A 자연단음계" from `sh.ko`, while the visible label says "C장조
    음계", "A단조 자연단음계".
- **Fix.**
  - Line 28: `full: (n) => t('Chromatic, from ' + n, n + ' 반음계')`
  - Line 81, Korean: `'건반 시계: ' + sh.full(prettyNote(tn)) + '가 모양으로 그려져 있어요.'`
  - Line 139, Korean: `'건반 시계의 ' + sh.full(prettyNote(tn)) + '.'`
- **Checked and right as they are:** A단조 (not 가단조, not A 단조) and 화성단음계 (rule 8). These match chapter 19's
  G장조 and the chapter 16 drill's "A단조 화성단음계".

### m14. The older tools inside this book's screen pages write the keys with a space
- **Where.**
  - On screen steps 3 and 4, the sharps-order and circle-of-fifths tools show "샤프 없음 = **C 장조 / A 단조**" and "**C 장조
    / A 단조**" just under the book's C장조 and A단조. Sources: src: 4766-4767 `majName` and `minName`, and src: 4946.
  - The minor-forms tool's blurb says 가단조 (src: 18789).
- **Fix.**
  - src: 4766: `t(' major', '장조')`
  - src: 4767: `t(' minor', '단조')`
  - src: 4946, Korean: `'… 없음 = C장조 / A단조'`
  - src: 18789 blurb: `'자연, 화성, 가락: A단조로 나란히 비교해요.'`
  - Follow-up for her call (app-wide): the older minor tools still say 자연 단음계, 화성 단음계, 가락 단음계 with a space (src:
    6555-6557 and about 20 places). This book follows rule 8's 화성단음계.

### m15. Pads: the titles and the key line
- **Where.**
  - CbKeyPad title (line 48): "조 하나, 한 번에 전부" is word for word and unnatural.
  - CbKeyPad note (line 49).
  - Line 58: "플랫 여섯 (B♭ …)" puts a space before the bracket. That is English style; chapter 19 writes "B♭(A♯가 아니에요)".
- **Fix.**
  - Line 48: `'조 하나를 한눈에'`
  - Line 49: `'두 원 어디에서든 조를 눌러요. 건반 시계는 장음계 모양을 그 조에서 시작하도록 돌리고, 5도권은 그 조의 자리와 샤프나 플랫의 개수를 보여 줘요.'`
  - Line 58: write `(LANG === 'ko' ? '(' : ' (')` and wrap the Korean string in `cbNbKo` (B2).

### m16. p1 caption under the clock has no object
- **Where.** Line 157.
- **What is wrong.** "…그 조에서 시작하게 돌리면 돼요": turn what?
- **Fix.** `'모든 장음계는 같은 모양이에요. 모양을 돌려 그 조에서 시작하면 돼요.'`

### m17. p1 check 2 ends on a fragment
- **Where.** Line 232; on print it also leaves "한 번씩" alone on a line.
- **What is wrong.** "어느 음에서나 장음계를 만들 수 있어요. 글자는 한 번씩"
- **Fix.** `'글자를 한 번씩 써서, 어느 음에서나 장음계를 만들 수 있어요'`

### m18. p7 rows and panel
- **Where.**
  - Line 203: "…까지의 조와 그 / 단조" leaves 단조 alone on screen. Its text says 조표 그리기 while the tool is named 조표 자리
    찾기.
  - Line 335 (the p7 intro).
  - Line 337 (the panel at the foot of p7).
- **Fix.**
  - Line 203, keys: `'샤프 넷, 플랫 넷까지의 장조와 그 나란한조'`
  - Line 203, text: `'5도권, 조표 자리 찾기, 가락단음계.'`
  - Line 335: `'규칙은 모든 조에서 같아요. 단계마다 조의 수만 달라요. 선생님이 나의 단계를 정하고, 다른 조를 골라 줄 수도 있어요.'`
  - Line 337: `'음계를 손가락 번호대로 한 손씩, 그리고 양손으로 치는 연습은 테크닉 영역의 ‘스케일과 화음 치기’에 있어요.'`

### m19. Minor keys are shown as Am, Em… with no key to the coins
- **Where.** The coins on p7 (Am, Em, F♯m …) and the C → Am check icon on p8.
- **What is wrong.** The text says A단조, but the coins use the chord-symbol m, which a Korean child of 8 does not read as
  단조. No legend says which coins are major and which are minor.
- **Fix.** One small line under the ladder on p7: `t('Navy: major. White, with m: minor.', '남색 동전은 장조, m이 붙은 흰 동전은 단조예요.')`.
  The p8 icon can stay.

### m20. The book's name and blurb
- **Where.** Line 8; the kicker (line 241); the card (line 371); the blurbs (lines 353, 360, 372).
- **What is wrong.** The shelf writes its books as one word: 레슨북, 워크북. "개념 책" has a space. In the blurb, "모든 조를 한
  번에" means "in one go"; "at a glance" is 한눈에.
- **Fix.**
  - `'개념 책'` → `'개념책'` in all three places.
  - Blurbs: `'규칙 하나, 모든 조를 한눈에, 그리고 단계별 연습.'`
  - Lesson intro (line 353): `'음높이 · 개념책: 규칙 하나로 모든 조를 한눈에 보고, 단계별로 연습해요.'`
- **For her call:** 개념서 is the usual publishing word, and parents know it.

### m21. The build-major tool on screen step 2
- **Where.** src: 7395 and the Restart button at src: 7386.
- **What is wrong.** The tool sits under the book's p3 definitions.
  - "**1번째** 걸음" is unnatural Korean.
  - The 처음부터 button breaks inside its word ("처음부 / 터") at 390 and 360 px.
- **Fix.**
  - src: 7395, Korean: `['첫', '두', '세', '네', '다섯', '여섯', '일곱'][n] + ' 번째 걸음: ' + prettyAny(names[n]) + '에서 다음은 어떤 걸음일까요?'`
  - The Restart button: add `style={{whiteSpace:'nowrap'}}`.
  - The T/S buttons and the TRY IT badge stay English in Korean mode. These are the open series-wide questions from Phase 476.

---

## Checked and right
- **Terms match the app:**
  - 음계 (its other name 스케일) and 장음계.
  - 온 걸음 / 반 걸음, with 온 / 반 in lists, as chapter 16 does.
  - 온+반, as chapter 16's harmonic minor builder writes it.
  - 으뜸음 (음계의 집 같은 음); N번 음.
  - 조표; 조 이름; 5도권; 건반 시계.
  - 나란한조; 화성단음계; 5음음계 (as chapter 27 normalised it); 반음계; 온음음계; 선법.
  - 샤프 / 플랫; 음자리표.
  - 테크닉 영역 and 스케일과 화음 치기 (TOOL_AREAS, CAT_KO).
  - 피아노 앞에서, 기억해요, 점검, 나의 다섯 가지 확인; 2~6쪽 in print.
- **Particles:** all right. Examples: G♭이 아니라 F♯가, F♯와 C♯는, G♯를, B♭장조와, A단조에서는 G♯예요, B C를, E F와. A sign
  is read 샤프 / 플랫, as rule 8 (chapter 16) says.
- **No English left in Korean mode:** none, except the minor m on the coins (m19) and the series-wide TRY IT and T/S (m21).
- **Chrome:** the left running head (PIANO BUTLER · 개념 책), the right one (음높이 · 스케일과 조) and the QR label (화면으로 보기)
  read well.
