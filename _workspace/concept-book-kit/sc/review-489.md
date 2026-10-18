# Review of Phase 489 (Home view): t489 vs t487
Method: Playwright walk-throughs in review2/ (nav.js, nav2.js, reg.js, reg2.js, lay.js), EN and KO, 320 and 390 px. Screenshots are lay-*.png. No page errors in any run.

Counts: must-fix 3, should-fix 8, minor 8.

## MUST-FIX

### 1. Back-button label says "Home" but lands one level lower (Learn, Try tools, More-practice chips)
Repro: `?teacher=1&view=home&area=pitch&concept=p-scales` -> "Learn". The button reads "← Home" (ko "← 홈"). Click it: you land on the concept screen (URL `...&concept=p-scales`), not on Home. Same for Try -> Scale finder / Key finder / any More-practice chip: the label is "← Home" but you land on the Try screen (`&sec=try`). Verified in EN and KO. This breaks "one level back at a time, right label". The cause is the fixed `backLabel` string `'← Home'` (line ~22721, and the ko map at ~20294).
Fix: compute the label from state. `st.ret==='home'`: if `st.hs==='try'` show `← Try` (ko `← 해 보기`), else `← {concept name}`. Pass a custom label to ToolView (or add dynamic entries to the ko map). For the Learn tool use the concept name.

### 2. Stale `ret:'home'` sends the Practice tab's tools back to Home
Repro: `?teacher=1&view=home&area=pitch&concept=p-scales&sec=try` -> Scale finder -> tap the "Practice" tab -> open "Practice timer". The button reads "← Practice", but it lands on the Home Try screen (URL `?view=home&area=pitch&concept=p-scales&sec=try`), not on Practice. The tab click does not clear `st.ret`, and `onBack` uses `st.ret || ...`. The same thing happens after Home -> Learn -> Practice tab. The wrong destination is shown under a correct-looking label.
Fix: clear `ret` in the tab-bar `update({...})` (`ret:null`), and also in the Practice `onOpen` and the kit/toolbox opens. Better: `onBack` should ignore `ret` when `st.view==='practice'`. (The same mechanism exists for `ret:'toolbox'`. I could not confirm it in 487 because the test could not open a Toolbox tool, but the code path is identical.)

### 3. Teacher Home leaks into the student view
Repro A: `?teacher=1&view=home` -> "Student view" button. The student now sees the teacher "Where do you want to go?" screen under the student tab bar (Learn / Practice, neither highlighted) and "Back to teacher view". Same with concept level. In 487 and elsewhere the Toolbox falls back to the Chapters map when T is false.
Repro B: `?view=home` with no teacher flag: a student/anonymous visitor gets the teacher Home with no Home tab.
The render condition is `st.view==='home' && !inChapter && !st.lock` with no `T` check. Also, `?view=home&lock=1` falls through to a chapter (Posture), so it is harmless but odd.
Fix: add `T &&` to the condition (else fall through to MapHome), and either map `view:'home'` to `path` in the initial state when not teacher, or reset `view` when entering preview.

## SHOULD-FIX

### 4. Check -> chapter: back button label is the generic "← Back" (ko "← 뒤로")
It lands on the concept screen. Compare "← Pitch" on the other screens: use "← Scales and keys" when the chapter was opened from Home (`ha/hc` set and view home). Today the chapter prev/next arrows `‹ ›` also keep the Home context and return to the Scales concept even after you moved to "Semitones and accidentals". Confusing but consistent. Consider hiding the arrows or labelling.

### 5. Tapping the Home tab while already in Home does nothing, and the other tabs return you to the deep level
Repro: Home -> Pitch -> Scales -> Try, tap "Home": stays on Try. Tap Toolbox then Home: you return to Try (state `ha/hc/hs` is never reset). There is no one-tap way to the five areas other than three back taps. Chapters and Toolbox tabs reset their own state.
Fix: Home tab onClick: `update({view:'home', ha:null, hc:null, hs:null, tool:null, kit:null, drill:null, ret:null})`.

### 6. Reload loses the Home context for tools and chapters
`?tool=scale-finder` (Home -> Try -> Scale finder) and `?drill=scales&tab=drill&level=1&mode=lesson` (Check) have no Home info. After reload, the tool's back button is "← Toolbox" and goes to the Toolbox, the chapter's back goes to the Chapters map, and the Home tab is not highlighted. The Home levels themselves (`area`, `concept`, `sec`) and `lang=ko` restore correctly at every level (tested 11 URLs, ko included). Fix: add `&from=home` (or keep area/concept in the URL while a tool or chapter is open) and restore `ret:'home'`.

### 7. Too many choices on two screens (goal: at most 5)
Level 0: 5 areas + "Search the Toolbox" button (+ the floating search button, + 4 tabs). Level 3 (Try): 2 tools + 5 "More practice" chips + back = 8. Suggested: cap "More practice" at 3 chips or put them under one "More practice" row that opens the existing Toolbox group; drop the extra "Search the Toolbox" button (the tab and the floating search already do it).

### 8. Tap targets under 44 px on the new screens
Measured: every new ghost back button ("← Home", "← Pitch", "← Scales and keys") is 28 px high (ko 30 px), "Search the Toolbox" 30 px (ko 32 px). Rows (76-92 px) and chips (44 px) are fine. The tab bar is 43 px (pre-existing). Fix: `minHeight:44` on the back buttons and the search button in ConceptHome.

### 9. Korean: area line reads as a broken sentence with a period
Level 1 appends "." to `whatKo`: "어떤 음인지." / "음이 얼마나 긴지." / "음을 어떻게 치는지." are clause fragments, not sentences (screenshot lay-ko-390-l1.png). On level 0 the same strings (without the period) are fine as subtitles. Suggest full sentences for level 1, e.g. "음이 무엇인지 배워요." / "음이 얼마나 오래 나는지 배워요." / "음을 어떻게 치는지 배워요." / "몸과 손 쓰는 법을 배워요." and drop the appended period.

### 10. Korean wording: "걸음" for steps; mixed terms
`HOME_LINE['p-clock']` "가장 작은 걸음" and HOME_TOOL_LINE scale-finder "음, 걸음, 손가락 번호" use "걸음" for step. The rest of the app uses 온음/반음. Suggest "가장 작은 간격(반음), 샤프와 플랫" and "음, 온음·반음, 손가락 번호". Concept line: "장음계는 모두 같은 패턴이에요" while the title says "스케일": pick one (e.g. "장음계(메이저 스케일)" once). The T/S boxes stay Latin letters but the legend is Korean (OK); consider 온/반 in ko.

### 11. English hard-coded in the Key-finder preview, also in ko
`HomeToolPreview` shows "Father Charles Goes Down And Ends Battle" in both languages (screenshot lay-ko-320-l3.png). The existing Key finder tool localises its sentence in ko. Use the same ko string.

## MINOR

12. "Same three buttons on every idea: Learn, Try, Check." is false today (only one concept is live) and is meta text a 12-year-old does not need. Remove or show only when all concepts are live.
13. Check line says "Quick questions" (ko "짧은 문제") but opens the full chapter with Learn/Drill tabs and Levels 1-6, plus "Builds on 11 · Tones & Semitones". Consider "Practice questions" or open the Drill tab only (it does: tab=drill) and say "Levels 1 to 6".
14. "More practice" chip "Every F" is not understandable alone (it is "Find every F" or similar). Check the `TOOLS` title; ko "모든 F" too.
15. Coral border and coral numeral on Pitch, on Try (step 2) and on every live row mean "available", but look "selected". On level 0 Pitch looks pre-selected. Use a small badge or no highlight for the live row.
16. The floating search button covers the last row's chevron at 320 px (Pieces row, last chips) and level 0 is 999 px tall at 320 (needs scrolling). Pre-existing control; add bottom padding on Home screens if needed.
17. Palette: preview and the rule card introduce extra tints (#c8361b, #c0431f, #efe8d6, #dbd2bd, #fbe3da). Close to navy+coral on cream, but not the tokens (`--coral`, `--navy`). The faded "Down And Ends Battle" words (opacity .25) have no text contrast.
18. `sec` URL key is also read by the Toolbox (`sec=books`, line ~20656). No clash today (`sec=try` only), but a future `sec=books` on Home would flip the Toolbox. Rename to `h=`/`step=` is NOT advised (`step` is used by chapter scrolling); use `hsec`. Also `area=rhythm&concept=p-scales` (inconsistent URL) shows back label "← Rhythm" over Scales; `area=bogus`/`beside` silently shows level 0 and keeps the bogus value in the URL. Sanitize `ha/hc/hs` at load.
19. Non-live concept rows open the Toolbox scrolled to the group correctly (`cat-p-intervals`, top offset 0), but there is no "back to Pitch" from there; only the Home tab (which returns to the area level, correct). The tag "Toolbox" (11 px, ko "도구함") is small; the ko app also uses "도구 모음" in the old back label, so the same thing has two names.
20. From a Learn tool, "Learn the whole chapter →" opens the chapter in the Chapters tab with `ret:'home'` still set (see #2); its back goes to the Chapters map, not Home. Acceptable, but note it.

## Regression result (t487 vs t489, EN and KO, 15 URLs each; text, URL, back label, destination, highlighted tab, errors)
Identical except the extra "Home" tab text: Chapters, Toolbox, Practice, `?tool=sharps-order`, `?tool=circle-fifths`, `?tool=cb-p-scales` (back "← Toolbox"/"← 도구 모음" -> Toolbox), `?tool=scale-finder&lock=1`, `?kit=scale-finder,key-finder&kn=Test`, `?teacher=1&drill=scales` (back -> Chapters map), student `?`, `?view=practice`, `?tool=cb-p-scales`, today, students. Student view of the normal tabs: unchanged. Only failure: item 3 (student/preview + Home). No horizontal scroll at 320 or 390 anywhere (EN/KO, 4 levels); no clipped text. Nothing deleted: all old routes behave as before.

## Navigation that works (no action)
Home -> Pitch -> Scales -> Learn / Try -> each tool / each chip / Check, and each tool's back lands correctly (apart from the label: #1). Chapter back from Check returns to the concept screen. Leaving Home via Chapters/Toolbox/Practice clears `st.drill` (no chapter leak). `lang=ko` survives every level and every reload. Home tab highlight: correct at all Home levels, in tools opened from Home, and in the Check chapter; becomes wrong only in #2/#3.

## Code smells
- `ret` is never cleared (see #2); consider clearing in `update` when `view` changes.
- Back-label logic is spread in three places (ko map, English strings, `onBack`); a single computed `{label, onBack}` would fix #1 and #4.
- Home state in `st.ha/hc/hs` is not validated at load (#18). `HOME_TOOL_LINE[id]` is indexed without a guard (fine for 2 tools, throws if a tool is added to `HOME_LIVE.tools` without a line).
- `setTimeout(..., 300)` scroll to `cat-...` after switching to the Toolbox works but is timing-based; it is not cleaned up if the user leaves quickly (harmless).
- Lists are keyed (`key={n}`, `key={id}`, `key={c.id}`); no unkeyed list found.
