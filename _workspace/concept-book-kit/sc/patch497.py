#!/usr/bin/env python3
# Phase 497: 'Say the order' lights the keys one by one on the keyboard (her 2026-10-19 09:10: the zigzag pattern she teaches in lessons).
import sys
s = open(sys.argv[1], encoding='utf-8').read()
def rep(a, b):
    global s
    assert s.count(a) == 1, a[:80]
    s = s.replace(a, b)
rep("  const [found, setFound] = useState(false);\n  const [wrong, setWrong] = useState(null);\n  const timers = useRef([]);\n  const tiny = useCbNarrow(380);\n  const clear = () =>",
    "  const [found, setFound] = useState(false);\n  const [wrong, setWrong] = useState(null);\n  const [ran, setRan] = useState(false);   // Phase 497: the order has been said: its keys are lit\n  const timers = useRef([]);\n  const tiny = useCbNarrow(380);\n  const clear = () =>")
rep("  if (done) { if (sharp) marks[pcOfName(order[want])] = 'mate'; marks[tonic] = 'pick'; }\n  const pickN = (i) => { clear(); setN(i); setLit(i); setFound(false); setWrong(null); };\n  const say = () => { clear(); setLit(0);",
    "  if (done) { if (sharp) marks[pcOfName(order[want])] = 'mate'; marks[tonic] = 'pick'; }\n  else if (ran) order.slice(0, lit).forEach((nm, i) => { marks[pcOfName(nm)] = i === lit - 1 ? 'pick' : 'mate'; });\n  const pickN = (i) => { clear(); setN(i); setLit(i); setFound(false); setWrong(null); setRan(false); };\n  const say = () => { clear(); setLit(0); setRan(true);")
open(sys.argv[2], 'w', encoding='utf-8').write(s); print('ok')
