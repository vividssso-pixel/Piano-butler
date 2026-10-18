# Concept book "Scales and keys" (Phase 485): theory and teaching review (r1)

Reviewer: strict AMEB / ABRSM theory examiner. My side: the theory is right and complete, and the concept-first teaching is sound.
Build checked: `a3/drills.t485.html` (source `cb/cbscales.jsx`, `cb/patch485.py`, `cb/t485.src.html`). I read every print page (EN and KO), the screen steps and both pads, and re-rendered the print book myself at 2x (`r1/p4-en.png`, `r1/p6-en.png`, `r1/book-en.txt`, `r1/book-ko.txt`).
Note: `shots/cb-*-3.png` and `step-*-3.png` are stale. They show "Then colour that key on the clock in your Workbook"; the build says "Check each note in the table, and tick the key you built". There is no Workbook for this book yet, so the build is right.

## Scripts (in `cb/review/r1/`)

- `theory_check.js` evaluates the page's own `cbSpell7`, `cbNames`, `cbTonic`, `cbSteps` and `cbMidi` for all 12 clock keys × 6 shapes, against an independent speller. It also checks `spellScale` for the 13 table rows, all 15 `KEY_SIGS` (relative minors, natural minor = key signature) and the page 4 naming rules. Result: **0 errors.**
  - Minor tonics on black keys are C♯, E♭, F♯, G♯, B♭: the usual spellings.
  - Every scale uses each letter once.
  - G♯ harmonic minor is G♯ A♯ B C♯ D♯ E F𝄪. G♯ melodic minor up is G♯ A♯ B C♯ D♯ E♯ F𝄪, and coming down is the natural minor.
  - E♭ harmonic minor has D♮; B♭ harmonic minor has A♮.
  - The pentatonic is degrees 1 2 3 5 6 of the major scale. G♭ pentatonic is the five black keys.
  - `cbMidi` is right: up, the octave, then down. The melodic minor comes down natural, and the tonic pitch matches the spelled tonic every time.
- `print_check.js` dumps the EN/KO print text, takes 2x shots of pages 4 and 6, and lists the 17 tools named on page 7. All exist; no page errors.

## Checked and right

- **The rule.** T T S T T T S; "whole, whole, half…". The two half steps are E F (3–4) and B C (7–8). Degree 1 is the tonic, and 8 is the tonic again (AMEB also numbers 1̂ to 8̂).
- **Page 2 picture.** C major on the keys, the staff and the clock. The half steps are coral, on 3–4 and 7–1.
- **Page 3.** D major from the rule: F♯ and C♯ are coral, and the reasoning is right. **All 13 table rows are right, every note** (C, G, D, A, E, B, F♯, G♭, D♭, A♭, E♭, B♭, F), and so are their counts.
- **Page 4.**
  - Order of sharps F C G D A E B, order of flats B E A D G C F.
  - "Half step above the last sharp" and "last flat but one" (one flat is F) work for all 14 signatures; I checked by script.
  - **All 28 sign positions are right** (2x crop, `r1/p4-crop.png`):
    - Treble sharps: F5 line, C5 space, G5 above the staff, D5 line, A4 space, E5 space, B4 line.
    - Bass sharps: F3, C3, G3, D3, A2, E3, B2.
    - Treble flats: B4, E5, A4, D5, G4, C5, F4.
    - Bass flats: B2, E3, A2, D3, G2, C3, and F2 under the staff.
  - The keys under the signs are right: G D A E B F♯ C♯, and F B♭ E♭ A♭ D♭ G♭ C♭.
- **Circles.**
  - FifthsRing order and counts are right (0, 1♯ … 6♯/6♭ … 1♭), with "more ♯ →" and "← more ♭".
  - On the clock (KeyRing), `o.pat` colours exactly the half steps:
    - natural minor: B–C and E–F;
    - harmonic minor: B–C, E–F and G♯–A;
    - melodic minor up: B–C and G♯–A;
    - pentatonic: none;
    - chromatic: all 12.
- **Page 6 notes and step words** are all right: A natural T S T T S T T; A harmonic …G♯, T S T T S T+S S; A melodic up …F♯ G♯, T S T T T T S; C pentatonic C D E G A, T T T+S T T+S; chromatic 12 × S.
- **Opener pad.** Every clock or circle key finds its `KEY_SIGS` row, the signs and the count words, including the G♭ twin line.
- **Five checks.** Each check matches its page: 1 → p2, 2 → p3, 3 → p4, 4 → p5, 5 → p6.

## Findings

### Blockers

**B1. "A scale's sharps or flats are its key signature": wrong for the minor scales the same book teaches. The book never says the raised notes are accidentals.**
- Where:
  - opener LbSay (cbscales.jsx:244–246);
  - p4 entry `key signature` (:295);
  - p6 `harmonic minor` (:323), whose picture then shows G♯ in A minor.
- What: a child puts the rules together and writes G♯ in A minor's key signature. That is the classic theory-paper error, marked wrong by both AMEB (harmonic minor from Grade 1) and ABRSM (Grade 2).
- Fix:
  - Opener EN: `Every major scale comes from <b>one rule</b>: whole, whole, half, whole, whole, whole, half, from any note. A major scale’s sharps or flats are its <b>key signature</b>, and the <b>circle of fifths</b> puts the twelve major keys in order.`
  - Opener KO: `모든 장음계는 <b>규칙 하나</b>로 만들어요: 어느 음에서나 온, 온, 반, 온, 온, 온, 반. 장음계의 샤프나 플랫은 그 조의 <b>조표</b>가 되고, <b>5도권</b>은 열두 장조를 차례로 놓아요.`
  - p4 `key signature`: the full replacement text is under M11.
  - p6 `harmonic minor` EN: `The natural minor with degree 7 raised a half step: G♯ in A minor, B♮ in C minor. The raised note is written as an accidental each time, never in the key signature.`
  - p6 `harmonic minor` KO: `자연단음계에서 7번 음을 반 걸음 올린 음계: A단조에서는 G♯, C단조에서는 B♮. 올린 음은 그때마다 임시표로 쓰고, 조표에는 넣지 않아요.`

**B2. Page 3 'each letter once': "Where a step needs a black key, the letter takes a sharp or a flat" teaches sharp/flat = black key. The table on the same page disproves it.**
- Where: cbscales.jsx:282 (EN and KO).
- What:
  - F♯ major's E♯ and G♭ major's C♭ are coral in the table, yet both are white keys. C♯ and C♭ majors (named on p3 and p4) add B♯ and F♭.
  - This is the exact misconception Sohyun asked to avoid in Phase 441 ("a sharp or a flat is not always a black key").
- Fix EN: `Name the notes with the seven letters in order, each once. When the steps need a note the plain letter does not give, the letter takes a sharp or a flat: so D major has F♯, never G♭. That note can be a white key: F♯ major has E♯, played on F.`
- Fix KO: `일곱 글자를 차례로 한 번씩 써서 음 이름을 붙여요. 걸음이 원래 글자의 음과 다른 음을 요구하면 그 글자에 샤프나 플랫이 붙어요. 그래서 D장조에는 G♭이 아니라 F♯가 있어요. 그 음이 흰건반일 수도 있어요: F♯장조의 E♯는 F 건반에서 쳐요.`

### Must fix

**M1. 'Key' is never defined, and in English it means two things on the same pages.**
- Where (the two senses: a piano key and a musical key):
  - the opener puts the "keyboard clock" (12 piano keys) beside "the circle of fifths puts the twelve keys in order" (musical keys), and also says "from any key";
  - p5 legend: "F♯ major and G♭ major are the same keys";
  - p6: "Chromatic: all twelve keys";
  - the pad: "Tap a key on either ring".
- Korean is fine (조 vs 건반). The book is titled "Scales and keys" but never says what a key is.
- Fix:
  - Add the first entry on p2.
    - EN: `key` `The scale a piece uses, named after its tonic: a piece in D major uses the notes of the D major scale.`
    - KO: `조` `곡이 쓰는 음계를 그 으뜸음 이름으로 부른 것. D장조 곡은 D장조 음계의 음을 써요.`
  - Opener: "from any note" and "twelve major keys" (B1 text).
  - p5 legend: see M5.
  - p6: `Chromatic: every note, white and black, a half step each.`
  - Pad intro: `Tap a piano key on the clock, or a key on the circle.`

**M2. 'a 5th: Five letters up, counting both ends' gives the wrong next key at B and F.**
- Where: p5 entry (:310) and pad/legend wording.
- What: five letters up from B gives F, but the circle needs F♯. Five letters down from F gives B, but it needs B♭. Those two letter pairs are exactly where the circle moves from the white keys into sharps and flats. Every 5th on the circle is perfect (7 half steps).
- Fix EN: `Five letters up, counting both ends: C D E F G. On the circle every 5th is 7 half steps (a perfect 5th): a 5th above B is F♯, not F. G is degree 5 of C major; its other name is the dominant.`
- Fix KO: `양 끝을 세어 다섯 글자 위: C D E F G. 5도권의 5도는 언제나 반 걸음 7개(완전5도)예요: B에서 5도 위는 F가 아니라 F♯. G는 C장조의 5번 음, 다른 이름은 딸림음이에요.`
- "Dominant" is AMEB Music Craft Grade 1 vocabulary.

**M3. 'T+S' is used but never defined, and it labels two different things.**
- Where: p6 figures and both pads (`cbSteps`).
- What:
  - In the harmonic minor, F–G♯ is a step to the next letter (an augmented 2nd).
  - In the pentatonic, E–G and A–C skip a letter (minor 3rds).
  - So "T+S" makes the pentatonic look step-by-step, which also contradicts p2's 'scale … step by step'.
- Fix:
  - Add to p6 `other scales` (or as its own entry):
    - EN: `T+S: a tone and a semitone together, 3 half steps. In the harmonic minor it is a step to the next letter (F to G♯); in the pentatonic it is a skip (E to G, A to C).`
    - KO: `온+반: 온음과 반음을 합한 거리, 반 걸음 3개. 화성단음계에서는 다음 글자로 가는 걸음(F에서 G♯), 5음음계에서는 글자 하나를 건너뛰는 거리(E에서 G, A에서 C)예요.`
  - p2 `scale` EN: `Notes in order from one note to the same note an octave higher or lower. A major or minor scale goes step by step, each letter once.`
  - p2 `scale` KO: `한 음에서 한 옥타브 위나 아래의 같은 음까지 차례로 가는 음들. 장음계와 단음계는 한 걸음씩, 글자를 한 번씩 써요. 다른 이름은 스케일이에요.`

**M4. "Every major scale" lists 13; C♯ and C♭ major are missing. The book never squares "twelve keys" with "fifteen key signatures".**
- Where:
  - `CB_TABLE` (:97) and its aria-label "Every major scale";
  - p3 `two names` names C♯ and C♭;
  - p4 names C♯ and C♭ under the 7th sign;
  - p7 'Later' says "All fifteen key signatures";
  - the pad has no C♯ or C♭.
- What: a teacher who names C♯ or C♭ major on p3 ("Check each note in the table") finds no row.
- Fix:
  - `const CB_TABLE = ['C','G','D','A','E','B','Cb','F#','Gb','C#','Db','Ab','Eb','Bb','F'];` puts each twin pair together (B/C♭, F♯/G♭, C♯/D♭). `spellScale` and `KEY_SIGS` already support C♯ and C♭.
  - Join the twins with the no-border row as now, and make the aria-label list all 15.
  - p5 `circle of fifths` add EN: `Three places have two names (B and C♭, F♯ and G♭, C♯ and D♭), so there are fifteen key signatures.`
  - p5 `circle of fifths` add KO: `세 자리는 이름이 둘이에요(B와 C♭, F♯와 G♭, C♯와 D♭). 그래서 조표는 모두 15개예요.`

**M5. Page 5's direction words and "the same keys"; enharmonic is never named (AMEB Music Craft Grade 1).**
- Where: p5 legends and REMEMBER (:187–189, :316); opener ringCap "one more sharp or flat each step" (:159); p3 `two names` (:283).
- What:
  - "Clockwise … one more sharp" is false from F♯/G♭ on: D♭ has fewer flats.
  - "the same keys" is ambiguous.
  - AMEB Grade 1 asks for the concept "enharmonic", but the word appears only as a tool title on p7.
- Fix:
  - Legends EN:
    - `Clockwise from C: each key a 5th higher, one more sharp.`
    - `Anticlockwise from C: each key a 5th lower, one more flat.`
    - `At the bottom they meet: F♯ major (6 sharps) and G♭ major (6 flats) sound the same and are played on the same piano keys.`
  - Legends KO:
    - `C에서 시계 방향: 한 칸마다 5도 위, 샤프 하나 더.`
    - `C에서 시계 반대 방향: 한 칸마다 5도 아래, 플랫 하나 더.`
    - `맨 아래에서 만나요: F♯장조(샤프 6개)와 G♭장조(플랫 6개)는 소리가 같고 같은 건반에서 쳐요.`
  - REMEMBER EN: `From C: clockwise one more sharp, anticlockwise one more flat.`
  - REMEMBER KO: `C에서: 시계 방향은 샤프 하나 더, 시계 반대 방향은 플랫 하나 더.`
  - ringCap EN: `Every key in order: from C, one more sharp or flat each step.`
  - ringCap KO: `모든 조를 순서대로: C에서 한 칸마다 샤프나 플랫이 하나씩 더.`
  - p3 `two names` EN: `F♯ major and G♭ major are played on the same piano keys. So are C♯ and D♭ major, and B and C♭ major. Its other name is enharmonic: two names for one sound.`
  - p3 `two names` KO: `F♯장조와 G♭장조는 같은 건반에서 쳐요. C♯장조와 D♭장조, B장조와 C♭장조도 그래요. 다른 이름은 딴이름한소리: 소리 하나, 이름 둘.` (The app's chromatic tool already uses 딴이름한소리.)

**M6. One key signature belongs to two keys, and the book never says how to tell which.**
- Where: p4 `naming the key` (:297), check 3 (:233), p6.
- What: p4's rule gives only the major. AMEB Grade 1 and ABRSM Grade 2 papers ask for "the key of this melody" in minor keys too.
- Fix:
  - p4 EN: `Sharps: the major key is a half step above the last sharp. Flats: the major key is the last flat but one. One flat is F major.`
  - p4 KO: `샤프: 마지막 샤프보다 반 걸음 위가 장조 이름. 플랫: 끝에서 두 번째 플랫이 장조 이름. 플랫 하나는 F장조.`
  - Add a p6 entry. EN: `which key?` `A key signature belongs to two keys: a major and its relative minor. The music tells you: a minor piece shows its raised degree 7 as an accidental (G♯ in A minor) and usually ends on its tonic.`
  - Add a p6 entry. KO: `어느 조?` `조표 하나는 두 조의 것이에요: 장조와 그 나란한조. 곡을 보면 알아요: 단조 곡에는 올린 7번 음이 임시표로 나오고(A단조의 G♯), 보통 그 으뜸음으로 끝나요.`
  - Check 3 EN: `… and name the major key from its key signature`.
  - Check 3 KO: `… 조표를 보고 장조 이름을 말할 수 있어요`.

**M7. "Raised" is shown only with sharps; in flat minors the raised note is a natural.**
- Where: p6 `melodic minor` (:324) and the harmonic minor entry (fixed in B1).
- What: AMEB Grade 2 sets C minor and Grade 3 F minor. A child who takes "raise" to mean "add a sharp" writes B♯ in C minor.
- Fix EN: `Up: degrees 6 and 7 raised a half step (A minor: F♯ G♯; C minor: A♮ B♮). Down: the natural minor.`
- Fix KO: `올라갈 때 6번과 7번 음을 반 걸음 올려요(A단조: F♯ G♯, C단조: A♮ B♮). 내려올 때는 자연단음계.`

**M8. The double sharp appears with no word.**
- Where: the pad "Other shapes, the same clock" (G♯/A♭ tapped: harmonic and melodic minor show F𝄪, drawn small, like "F×"). Not in the ladder either.
- What: AMEB places double sharps and the G♯/D♯ minors at Grade 4. Show it if you like, but say what it is.
- Fix:
  - In `CbShapesPad`, under the names, when `names.some(n => n.endsWith('##'))`:
    - EN: `F𝄪 is F double sharp: two half steps up from F, played on G. Each letter once, so it is not written G.`
    - KO: `F𝄪는 F 겹샤프: F에서 반 걸음 두 번 올린 음이라 G 건반에서 쳐요. 글자는 한 번씩이라 G로 쓰지 않아요.`
    - Build the letter from the data, not hard-coded F.
  - p7 'Later' add `double sharps (G♯ minor’s F𝄪)` / `겹샤프(G♯단조의 F𝄪)`.

**M9. Page 7: the tools named do not match the words beside them.**
- Where: STEPS (:202–203).
- What:
  - 'Further' says "the melodic minor", but its tool `build-minor` is "Build a harmonic minor".
  - 'Then' says "natural and harmonic", but its tool `minor-forms` ("Three kinds of minor") is where the melodic minor is.
- Fix: swap them.
  - Then: `['build-major','sharps-order','flats-order','relative-minor','build-minor']`
  - Further: `['circle-fifths','place-it','minor-forms','scale-finder']`

**M10. The ladder clashes with AMEB Music Craft in two places.**
- Source: the 2022 syllabus PDF. I could not check the 2026 manual.
- (a) G minor.
  - AMEB Grade 1 is D and B♭ major plus **harmonic minor A, E, D and G**. G minor (B♭'s relative) sits in 'Further'.
  - Fix: Then keys EN `D and B♭ major; A, E, D and G minor`, KO `D장조와 B♭장조, A단조·E단조·D단조·G단조`.
  - Coins `['D','Bb','Am','Em','Dm','Gm']`; remove `Gm` from Further.
- (b) The pentatonic.
  - AMEB Grade 2 has the **major pentatonic on C and G** (and Mixolydian on G), a grade before the melodic minor (Grade 3). The ladder puts the pentatonic at 'Later'.
  - Fix: Further text EN `The circle of fifths; placing a key signature; the melodic minor; the major pentatonic on C and G.`, KO `5도권, 조표 그리기, 가락단음계, C와 G의 장조 5음음계.`
  - Move `csx-penta` into Further's tools.
- What fits:
  - First = AMEB Prelim (C, G, F) exactly.
  - Further ≈ AMEB Grades 2–3 / ABRSM Grades 2–3 (melodic minor at Grade 3 in both).
  - Later ≈ AMEB Grade 4 (B, F♯/G♭, C♯/D♭ major; B♭, E♭/D♯, A♭/G♯ minor; double sharps).

**M11. Page 4 `key signature`: "every line" means a staff line in this book, Korean "줄마다" breaks rule 8, and the time signature's place is missing.**
- Where: :295.
- Fix EN: `The sharps or flats of a key, written after the clef at the start of every line of music, before the time signature. They last the whole piece, in every octave.`
- Fix KO: `그 조의 샤프나 플랫을, 오선마다 맨 앞 음자리표 뒤에, 박자표보다 먼저 써요. 곡 전체에서, 모든 옥타브에 유효해요.`
- This also carries B1 ("a key's", not "a scale's").

**M12. The book uses whole/half and T/S but never says what they are.**
- Where: p2.
- What: a concept book "taught whole, once" has to stand on its own. AMEB and ABRSM papers use tone and semitone.
- Fix: add one p2 entry.
  - EN: `half step, whole step` `A half step goes to the very next key, black or white; its other name is a semitone (S). A whole step is two half steps; its other name is a tone (T).`
  - KO: `반 걸음, 온 걸음` `반 걸음은 바로 옆 건반까지, 검은건반이든 흰건반이든. 다른 이름은 반음(반). 온 걸음은 반 걸음 두 개. 다른 이름은 온음(온).`
  - Then the `major scale` entry can keep "In tones and semitones: T T S T T T S".

### Minor

- **m1. "Pentatonic" is the major pentatonic.**
  - AMEB's term is "major pentatonic scale", and the A minor pentatonic (A C D E G) will come later.
  - Label `Major pentatonic` / `장조 5음음계`; full name `C major pentatonic`.
  - Entry EN: `Major pentatonic: a major scale without degrees 4 and 7.`
- **m2. On paper, the melodic minor shows only the way up.** The At the piano step asks for up and down.
  - Under the figure add `down: A G F E D C B A` / `내려올 때: A G F E D C B A`, from `cbSpell7(tn, sh.down)` reversed.
  - In the pad, prefix the steps line with `up: ` / `올라갈 때: ` for the melodic minor. It now sits under "Coming down" and reads as the way down.
- **m3. Relative minor.** Add the quick rule, as the app's own Relative minor tool has it:
  - EN: `… Three half steps below the major key's note: C → A.`
  - KO: `장조 으뜸음에서 반 걸음 세 개 아래: C → A.`
- **m4. The two circles disagree.**
  - The book's FifthsRing shows only F♯/G♭ twinned.
  - The embedded Circle of fifths tool (screen p5) and p3 show B/C♭ and D♭/C♯ too.
  - Give FifthsRing small second names at B (C♭) and D♭ (C♯), with counts `5♯ 7♭` and `5♭ 7♯`.
- **m5. The opener pad's twin line is only for G♭.**
  - Add for B: `· the same keys as C♭ major (7 flats)` / `· C♭장조(플랫 일곱)와 건반이 같아요`.
  - Add for D♭: `· the same keys as C♯ major (7 sharps)` / `· C♯장조(샤프 일곱)와 건반이 같아요`.
- **m6. Page 4's visible "key" row has no gloss.** A child may read "G" under F♯ as F♯ = G.
  - Caption EN: `key: the major key whose signature ends at this sign`.
  - Caption KO: `조: 조표가 이 기호에서 끝나는 장조`.
- **m7. Page 4 never says why the naming rule works.**
  - EN: `Each new sharp is the new key's degree 7, a half step below its tonic.`
  - KO: `새로 붙는 샤프는 새 조의 7번 음, 으뜸음보다 반 걸음 아래예요.`
- **m8. Page 7 'Later' names the whole-tone and blues scales, which have no tool.**
  - `csx-blues` is the 12-bar blues, not the blues scale. Neither scale is in AMEB Music Craft Grades 1–4 or ABRSM Grades 1–5, as far as I could check.
  - EN: `All fifteen key signatures; double sharps; the chromatic scale; the modes.`
  - KO: `조표 15개 전부, 겹샤프, 반음계, 선법.`
- **m9. Korean "반대 방향" alone means "the opposite direction".**
  - Write `시계 반대 방향` on p5 (entry, legend, At the piano 2, REMEMBER).
- **m10. Harmonic minor figure: the T+S segment (F–G♯) is the scale's mark but is drawn plain.** Optionally draw it dashed or double.
- **m11. Harmonic minor's raised 7th.** Optionally name it `Its other name is the leading note` / `다른 이름은 이끎음` (the app uses both 이끎음 and 이끔음; 이끎음 is right).
- **m12. No task to write a key signature on the staff.** Page 4 draws positions on both staves and both boards examine writing them, but nothing asks the child to write one (it only appears as "placing" in Further).
  - Add an At-the-piano step 3, EN: `Draw G major's and F major's key signatures on the treble and the bass staff.`
  - KO: `G장조와 F장조의 조표를 높은음자리표와 낮은음자리표 오선에 그려요.`
- **m13. "The seven modes" blurb is stale.** It still says "Lydian to Locrian … brighter to darker" (Toolbox). Phase 175 put the modes in Ionian-first order.
- **m14. "They last the whole piece" is the usual Grade 1 simplification.** Strictly, a key signature lasts until a new key signature. FOR HER, as in chapter 19: keep it, and note the key change for the Teacher copy.
- **m15. Page 5 At the piano 1: "each a 5th above the last" runs off the keyboard after a few steps.**
  - EN: `… each a 5th higher (or a 4th lower, to stay in the middle) …`
  - KO: `… 한 칸마다 5도 위(가운데에 머물려면 4도 아래) …`

## Ladder and syllabus: what I am sure of, and what I am not

- **AMEB Music Craft 2022 (read from the PDF):**
  - Preliminary: C, G, F major.
  - Grade 1: D, B♭ major; harmonic minor A, E, D, G; the concepts enharmonic and chromatic; tonic and dominant.
  - Grade 2: E♭, A major; harmonic minor C, B, F♯; major pentatonic on C and G; Mixolydian on G.
  - Grade 3: E, A♭ major; C♯ and F minor, harmonic and melodic.
  - Grade 4: B, F♯/G♭, C♯/D♭ major; B♭, E♭/D♯, A♭/G♯ minor; double sharps and flats; major pentatonic.
  - Grade 5: the chromatic scale.
  - The natural minor is not named at any grade.
  - **Unsure:** the 2026 wording.
- **ABRSM Theory (mymusictheory, not the ABRSM PDF):**
  - Grade 1: C, G, D, F major, no minors. So D major is 'Then' here but Grade 1 for ABRSM.
  - Grade 2: B♭ and E♭ major (A major too, per an earlier reviewer: unconfirmed); A, E, D minor, **harmonic only**.
  - Grade 3: up to 4 sharps and flats, harmonic and melodic.
  - **Unsure:** Grades 4–5 (up to 5 and then 6 or 7 signs?) and the chromatic scale grade.
- **Natural minor.** Teaching it first, as the bridge from the relative major, is sound. Neither board's theory papers ask for it at these grades, though: check 5's "natural and harmonic" should be read with "the exam form is harmonic". FOR HER: a Teacher-copy line.
- **Technical Work (practical).** The app's own fingering sources (Sohyun's AMEB Technical Work books) put A minor at Preliminary (P.3), F major at Grade 1 (1.4), B♭ at Grade 2, E♭ at Grade 3 and A♭ at Grade 4. The ladder follows Music Craft, not Technical Work: a Preliminary piano student plays A minor in 'First'. FOR HER: say "keys follow AMEB Music Craft" in the Teacher copy, or add Am to First.
- **Unsure:** which minor forms ABRSM piano practical accepts at Grades 1–2.

## Concept-first teaching

- The arc is sound, and the pictures carry it well: one rule → D major worked → every key in a table → the signatures as the same notes → the circle as their order → the minors as other shapes on the same clock. The p3 table → p4 order link is the strongest page.
- It depends on three prerequisites the book never states: half and whole steps, letter names, and accidentals. Add M12, or a one-line "You need: Semitones and accidentals".
- The real risks are wording, not order: B1, B2, M1 and M2 are each a rule a child would apply literally and get wrong on an exam paper.
- The five checks match pages 2–6 (with the M6 wording for check 3).

## Counts

Blockers 2 · Must fix 12 · Minor 15.
