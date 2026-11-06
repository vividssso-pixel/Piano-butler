# Chapter review kit (working scripts, not part of the site)

Used to make the chapter 1 review pack (2026-10-08). Chapter-specific bits live in pack.py (the A/B lists and
the drill answer lines) and in rv1svg.js / rv1drill2.js (which drawings and drill levels to capture).

Steps (needs Node + Playwright with Chromium, Python 3 with pypdf + reportlab):
1. Build the drills page (`node tools/precompile.js`) and serve it; contentharness.js does this for tests.
2. `CH=<chapter-id> node rv1books.js`  -> lesson.pdf, work.pdf, teacher.pdf (+ .txt for checking)
3. `node rv1drill2.js`                 -> dq1-3.png (drill screenshots)
4. `node rv1svg.js`                    -> drawings for the public page (tools/lessons/svg/<id>/)
5. `python3 ../../tools/lessons/build.py <id>` then `node shotlesson.js` -> page.pdf (+ screenshots)
6. `python3 pack.py` (front.html) -> print it to front.pdf with Chromium (preferCSSPageSize)
7. `python3 merge.py "Chapter N" Chapter-NN-review-<name>.pdf`
