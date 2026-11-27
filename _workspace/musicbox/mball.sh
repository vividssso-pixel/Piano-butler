#!/bin/bash
# Regenerate every Music Box data file in the right order, then the story touches (mbstory.py is not safe to run twice on its own).
set -e; cd "$(dirname "$0")"
python3 mbox.py >/dev/null; python3 mbox2.py >/dev/null; python3 mbfront2.py >/dev/null; python3 mbox3.py >/dev/null; python3 mbfront3.py >/dev/null; python3 mbstory.py
