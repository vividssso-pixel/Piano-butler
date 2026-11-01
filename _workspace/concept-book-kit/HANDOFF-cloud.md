# Heavy jobs in the cloud (her 31 Oct 2026, 18:20 and 18:23)

Sohyun runs the heavy jobs in Claude Code cloud sessions, on her credits, not in the chat window and not on her Mac.
One window, one job, one at a time (two windows would both add the same CLAUDE-history row). Each window pushes its own
branch; she merges it herself. Paste the common header, then one job.

## Common header

```
RUN THIS ENTIRELY IN THE CLOUD (Claude Code cloud session, on my credits). Do not use my computer or any tool that reaches my Mac.
Director mode for Piano Butler (Sohyun / Clara). Talk to me in Korean; files, code and documents in English.
Repo: vividssso-pixel/Piano-butler (main). Read CLAUDE.md first (Top Priority, the rules) and the last rows of CLAUDE-history.md.
Constraints: never push to main and never merge; commit on a new branch and push only that branch, then tell me its name (I merge it myself). Never touch money, credentials or passwords. Ask before sending anything outside, strategic changes, an AdSense re-review or deleting files.
Style: navy #26296b and coral #e4572e on cream, green #2e8a6e only for correct. Only what is needed, useful and fun, concisely: one activity per idea, no layer added everywhere. No music facts from memory unless checked against the rooms' data, the syllabus or a source. No new metaphors unless I ask. Floors are named by grade only.
Setup in this session (it starts fresh every time): npm install at the repo root; in _workspace/concept-book-kit/kit install what contentharness.js requires (playwright, react 18, react-dom 18, @babel/standalone 7, the @fontsource fonts it names); use the Chromium this environment has (or Playwright's own) instead of /opt/pw-browsers/chromium if that path is missing. Build drills.src.html into _workspace/concept-book-kit/a3/drills.t807.html and check sc/ed807.js and sc/chsweep.js pass before changing anything.
Builds: never edit drills.html by hand. Change drills.src.html through a patch script (pattern: _workspace/concept-book-kit/sc/patch806.py, run as python3 patchNNN.py in.src.html out.src.html), then node _workspace/concept-book-kit/precompile.js out.src.html out.html.
Regression after every build: chsweep, booksweep, ov761, pic769 (ALL=1), heads786 all (6 known FIX: dots of r 3 or less, not noteheads, the same since before EF), stems795 all (4 known FIX false positives), dict790, dr794, dq793, dp791, dd779, dg782, dn789, cu768, reg807 (reg674 with each context closed), dt796, du797, dw799, dx804, dz802, ed807, ee808, ef809, eg810, eh811, ei812. At most two lanes at a time (reg807 alone takes most of an hour: give a background run two hours).
Ship: copy the build to drills.html / drills.app.js / drills.src.html, commit with the trailer lines and a new row in CLAUDE-history.md, push the branch. Show me screenshots of what changed.
```

## Jobs, in order

(The rest of call 39 was done in the chat on 31 Oct, Build EE: the staff under the 7th chords only. The Beginner Workbooks: Build EF; the Prelim Workbooks: Build EG; the Grade 1 Workbooks: Build EH; the Grade 2 Workbooks: Build EI.)


1. The Workbooks, fun first, one floor a window (open the next only after she merges the last):
```
Today's task: the Workbooks, fun first, one floor in this window: <Grade 3>. (Beginner to Grade 2 were done in the chat on 31 Oct and 1 Nov, Builds EF to EI: only the parts better changed, each swapped for one that practises the same thing, never a part added; first the parts that need someone else at home, the free ones, and the same task again and again; sc/wbf44.code.js to sc/wbf47.code.js show the way. Rooms shared by two grades (Intervals and Chords, Rhythm, Scales: H3Workbook, R2Workbook, ScfWorkbook with g) print each grade's own steps: change only the steps of the floor in hand.) For each room's Workbook (?book=work&ch=<room>), make its activities fun the How to Blitz way (its approach, never its content), one activity per idea, nothing added everywhere. Build the floor the way you think best (her 1 Nov 19:44: no plan first; she checks the result), then check print overflow is 0 on every page, run the regression and push the branch.
```
2. A Pieces shelf waits for her: which grade first, and what the pieces are for.

The decision board (a Claude Docs project) is updated from the chat window once she merges a branch.
