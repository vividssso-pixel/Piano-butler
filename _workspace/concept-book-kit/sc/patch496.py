#!/usr/bin/env python3
# Phase 496: the Key finder's sharps and flats steps open on all seven (her 2026-10-19 09:09), so 'Say the order' plays the whole order.
import sys
s = open(sys.argv[1], encoding='utf-8').read()
a = "  const [n, setN] = useState(3);\n  const [lit, setLit] = useState(3);"
assert s.count(a) == 1
s = s.replace(a, "  const [n, setN] = useState(7);\n  const [lit, setLit] = useState(7);")
open(sys.argv[2], 'w', encoding='utf-8').write(s); print('ok')
