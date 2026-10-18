set -e
cd /home/claude/pbtest
node /tmp/claude-0/jsxchk470.js cb/cbscales.jsx | grep -v '^ok' || true
python3 cb/patch485.py cb/base.src.html cb/t485.src.html cb
node precompile.js cb/t485.src.html a3/drills.t485.html | tail -1
