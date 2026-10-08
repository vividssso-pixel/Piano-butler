# Lesson guide pages (one per chapter)

Public, indexable guide pages at `lessons/<slug>.html`, one per drills chapter, made **one chapter at a time
and only after Sohyun has checked that chapter** (decided 2026-10-08: "each one passes through my hands").
The guide page is the Lesson Book's short summary (Phase 368): if the two disagree, the Lesson Book wins.

## The review cycle for one chapter

1. **Claude prepares a review pack (PDF)** for the chapter: cover with three questions for the public page,
   "A. mistakes I found" (Fix / Leave it ticks), "B. please decide" (teaching questions), the online drill
   (screenshots + every answer line), then the chapter's Lesson Book, Workbook and Teacher copy
   (`drills.html?book=lesson|work|teacher&ch=<id>&lang=en`, printed by Chromium), then the draft public page.
2. **Sohyun checks it** with a red pen (photos) or in chat, ticks A, answers B and the three questions.
3. **Claude fixes** the app, books and teacher copy, fills her words into `src/<chapter-id>.html`,
   removes every DRAFT mark and builds with `--final`.
4. **She pushes**, opens the page live, and requests indexing in Search Console.

Progress is kept on the "Chapter Review Board" artifact (claude.ai/artifact/WPcDbn32yCFzyYTYcFCzTF;
collection `chapters`, one doc per chapter id: `status` todo|ready|checked|fixed|live, `updated`, `note`).

## Building a page

```
python3 tools/lessons/build.py <chapter-id>          # draft: noindex, yellow DRAFT marks shown
python3 tools/lessons/build.py <chapter-id> --final  # refuses while any DRAFT mark is left; index, follow
```

- `src/<chapter-id>.html` starts with a `<!--meta {...} -->` JSON block (slug, title, h1, description,
  teaches, image, updated), then the hand-written body. Her own words go where `class="draft"` marks are.
- Drawings are the Lesson Book's own pen-and-ink drawings as SVG (`svg/<chapter-id>/*.svg`), made by the art
  generator kept untracked in `_workspace/chapter-review/art/` (chapter 1: `guide374.py`), placed with
  `{{svg:name}}`. build.py prefixes every id inside a drawing with its name, so drawings never clash on a page.
- `{{beats:1 2 3 - | 3 2 1 -}}` draws a row of beat circles like the Lesson Book's tunes (a number is a
  finger, `-` holds for one more beat, `|` is a bar line).
- Only facts already in the Lesson Book go on the page; anything new is a question for Sohyun first.
- The worksheet picture is the chapter's Workbook page, printed by Chromium and saved as
  `lessons/img/<chapter-id>-worksheet.jpg` (880 px wide).
- Do not commit a draft build of `lessons/<slug>.html`: it would go live on push. Commit the page only
  after the `--final` build.
- After a page goes final: add it to `sitemap.xml`. (The Free printables page was taken down on 2026-10-08,
  so the guide pages do not link to it.)
