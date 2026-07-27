#!/bin/bash
# Double-click this file to open Piano Butler in your browser.
# It serves this folder over http on port 8899, which the app needs in order to
# load the syllabus data. Close this Terminal window when you are finished.

cd "$(dirname "$0")" || exit 1
PORT=8899
URL="http://localhost:$PORT/butler.html"

if lsof -ti:"$PORT" >/dev/null 2>&1; then
  echo "Already running on port $PORT."
else
  echo "Starting Piano Butler on port $PORT ..."
  # serve-butler.py sends no-store headers, so a plain reload always shows the
  # current files instead of a cached copy.
  python3 serve-butler.py "$PORT" >/dev/null 2>&1 &
  SERVER_PID=$!
  trap 'kill $SERVER_PID 2>/dev/null' EXIT
  sleep 1
fi

open "$URL"
echo ""
echo "  Piano Butler is open at $URL"
echo "  Close this window when you are finished."
echo ""

# Keep the server alive while this window stays open.
while lsof -ti:"$PORT" >/dev/null 2>&1; do sleep 5; done
