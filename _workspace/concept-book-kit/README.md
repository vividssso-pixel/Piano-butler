# Concept-book kit (saved at the end of Phase 485)

Everything a fresh session needs to build, test and review a concept book without the session that made the first one.
Nothing here is served by the site and none of it is committed to git (`_workspace/` is untracked on purpose).

## What is in it
- `cb/cbscales.jsx`: the source of the first concept book, Scales and keys (the model for the other twelve).
- `cb/patch485.py`: the patch that applies it to `drills.src.html` (also the shared-component changes: KeyRing `o.pat`,
  FifthsRing `o.bare`/`o.twins`, `pbAccT`, LbPage `head`, the print route, the Toolbox card).
- `build-concept-book.sh`: jsx syntax check, then the patch, then the precompile. Paths are absolute (`/home/claude/pbtest`);
  change them to wherever you unpack this.
- `precompile.js`: `node precompile.js in.src.html out.html` (needs `@babel/standalone` 7.x to reproduce the committed `drills.html` byte for byte).
- `kit/contentharness.js`: the Playwright harness. `H.open({path,w,h,lang,dsf})`; it serves a build from `../a3/` and the fonts
  from `./node_modules/@fontsource/...`; React and Babel come from `node_modules` (react, react-dom, playwright, @babel/standalone, @fontsource/inter, noto-music, cinzel, cormorant-garamond, playfair-display).
  Chromium is at `/opt/pw-browsers/chromium`.
- `tools/jsxchk.js`: syntax check for a .jsx file.
- `cb/review/BRIEF.md`: the brief given to the four reviewers. `r1/*.md`: their reports; `r1/DISPOSITION.md`: every point and what was done; `r2/verify.md`: the verifier's report.
- `cb/review/r1/scripts`, `r2/scripts`: the measuring scripts (overflow at 320/360/390, ring comparison `ringdiff3.js`, links keep `lang=ko` and `lock=1`, one sound at a time, print overflow per page).

## To rebuild
1. `cp <repo>/drills.src.html cb/base.src.html`
2. Fix the paths in `build-concept-book.sh`, then run it. Output: `a3/drills.t485.html`.
3. Routes: print `?book=concept&ch=p-scales&lang=en|ko`; screen `?teacher=1&tool=cb-p-scales`; student `?tool=cb-p-scales&lock=1`.

## Rules to keep
See `CLAUDE.md` rules 15 (build with recommendations; review sized to the change) and 16 (the foundation: five areas, concept first),
and `HANDOFF.md` for the prompt to paste into a new window.
