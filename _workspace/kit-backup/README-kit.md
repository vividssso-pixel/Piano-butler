# Piano Butler build kit (backup of the cloud workspace, Phase 461)

Restore in a new cloud session:
1. mkdir -p /home/claude/pbtest && tar xzf pbkit-backup.tgz -C /home/claude/pbtest  (the /tmp/claude-0 screenshot scripts land in the root; move *.js that are not precompile.js into /tmp/claude-0)
2. cd /home/claude/pbtest && npm i @babel/core @babel/preset-react react@18 react-dom@18 playwright @fontsource/noto-sans-kr (check precompile.js and kit/contentharness.js for the exact requires)
3. cp "<repo>/drills.src.html" drills.src.html && node precompile.js drills.src.html a3/drills.html
4. Kit tests: BUILD=drills.html node kit/<test>.js  (contentharness resolves BUILD in a3/)
Chromium: /opt/pw-browsers/chromium.
