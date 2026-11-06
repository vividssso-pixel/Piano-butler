#!/usr/bin/env python3
# Phase 484 (her 2026-10-17 21:13 and 21:32: '이게 pitch 영역이면 그것만, 리듬 영역이면 그것만, 터치 아티큘레이션, 테크닉에
# 스케일 코드 이런식으로 나눠져서 거기 안에서 레벨별로 어디로 가야할지'; '그렇게 하자. 이렇게 가는게 맞아 내 레슨 성격에 더 맞아'):
# the foundation, step 1: the Toolbox in five areas (pitch, rhythm, touch and expression, technique, pieces) and 13
# concepts, with the stories of music and the practice helpers beside them. Every tool keeps its page; only its topic
# changes (TOOL_CONCEPT, from the inventory of 17 October: every lesson step, Workbook page, drill level and tool sorted
# under its concept; the verifier's moves of 17 October in inv/map.py). Tools that do the same job stay, side by side in
# one concept, until she decides which to keep. A chapter's header names its concept; its ‹ › arrows follow the book's
# chapter numbers. The search overlay's buttons are grouped by area. Nothing else moves yet.
import sys, json
src, dst = sys.argv[1], sys.argv[2]
here = sys.argv[3] if len(sys.argv) > 3 else '.'
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    if s.count(a) != n: raise SystemExit('found %d: %s' % (s.count(a), a[:90]))
    s = s.replace(a, b)
def at(a, start=0):
    if s.count(a) != 1: raise SystemExit('anchor found %d: %s' % (s.count(a), a[:90]))
    return s.index(a, start)

# 1. the topics: 13 concepts in five areas, then the stories of music and the practice helpers
i = at("// Phase 221: order = teaching order"); j = at("// cat, level range [from, to]")
s = s[:i] + open(here + '/cats484.jsx', encoding='utf-8').read() + s[j:]   # old TOOL_CATS, CAT_KO and their getters out

# 2. each chapter's own concept (the All chapters page, the chapter header's group)
i = at("const CHAPTER_CAT = {\n"); j = s.index("\n};\n", i) + 4
s = s[:i] + """const CHAPTER_CAT = {   // Phase 484: a chapter goes under the concept most of its steps belong to
  'posture-hands': 'k-posture', 'first-steps': 'p-staff', 'note-names': 'p-staff', 'staff': 'p-staff', 'whole-staff': 'p-staff', 'ledger-lines': 'p-staff',
  'tones': 'p-clock', 'accidentals': 'p-clock', 'intervals': 'p-intervals', 'scales': 'p-scales', 'key-signatures': 'p-scales', 'chords': 'p-chords',
  'pulse': 'r-beat', 'note-values': 'r-beat', 'time-signatures': 'r-beat', 'rhythm': 'r-beat',
  'dynamics': 't-touch', 'tempo': 't-tempo', 'terms': 't-tempo', 'pitch-range': 'p-staff',
  'reading-steps': 'c-reading', 'signs': 'c-map', 'melody': 'c-map', 'form': 'c-map',
  'piano-story': 'about', 'composers': 'about', 'styles': 'about',
};
""" + s[j:]
i = at("const CAT_CHAPTER_ORDER = {"); j = s.index("\n", i) + 1
rep("function orderedChapterIds() { return TOOL_CATS.flatMap(c => catChapterIds(c.id)); }",
    "function orderedChapterIds() { return pathIds(); }   // Phase 484: a chapter's ‹ › follow the book's chapter numbers, 1 to 27 (the groups run side by side)")
s = s[:i] + "const CAT_CHAPTER_ORDER = { 'p-staff': ['first-steps', 'note-names', 'staff', 'whole-staff', 'ledger-lines', 'pitch-range'], 'p-clock': ['tones', 'accidentals'], 'p-scales': ['scales', 'key-signatures'], 'r-beat': ['pulse', 'note-values', 'time-signatures', 'rhythm'], 't-tempo': ['tempo', 'terms'], 'c-map': ['signs', 'melody', 'form'], about: ['piano-story', 'composers', 'styles'] };\n" + s[j:]

# 3. every tool's concept: the inventory's table over the old topic
i = at("function toolMeta(id) {")
tc = json.load(open(here + '/tool_concept.json'))
s = s[:i] + "// Phase 484: each tool's concept (the inventory of 17 October); the old topic stays in TOOL_META for its level and kinds\nconst TOOL_CONCEPT = " + json.dumps(tc, ensure_ascii=False, sort_keys=True).replace('", "', "', '").replace('": "', "': '").replace('{"', "{ '").replace('"}', "' }") + ";\n" \
    "Object.keys(TOOL_META).forEach(id => { if (TOOL_CONCEPT[id]) TOOL_META[id][0] = TOOL_CONCEPT[id]; });\n" + s[i:]
rep("function toolMeta(id) { const m = TOOL_META[id]; if (m) return { cat: m[0], lo: m[1], hi: m[2], kinds: m[3].split(' ') }; const t = TOOLS.find(x => x.id === id); return { cat: 'practice', lo: 0, hi: 3, kinds: ['show'], ch: t && t.ch }; }",
    "function toolMeta(id) { const m = TOOL_META[id]; if (m) return { cat: m[0], lo: m[1], hi: m[2], kinds: m[3].split(' ') }; const t = TOOLS.find(x => x.id === id); return { cat: TOOL_CONCEPT[id] || 'practice', lo: 0, hi: 3, kinds: ['show'], ch: t && t.ch }; }")

# 4. the Toolbox: an area's heading over its concepts
rep("      {TOOL_CATS.map(c => {\n        const list = TOOLS.filter(t => (toolMeta(t.id).cat === c.id",
    "      {TOOL_AREAS.map(a => { const blocks = TOOL_CATS.filter(c => c.area === a.id).map(c => {\n        const list = TOOLS.filter(t => (toolMeta(t.id).cat === c.id")
rep("""            </div>}
          </div>
        );
      })}
      {!shown && !parseScaleQuery(q) && <div className="card" style={{textAlign:"center",color:"var(--muted)"}}>Nothing matches. Try fewer filters.</div>}""",
"""            </div>}
          </div>
        );
      }).filter(Boolean); return blocks.length ? <div key={a.id}>{toolAreaHead(a)}{blocks}</div> : null; })}
      {!shown && !parseScaleQuery(q) && <div className="card" style={{textAlign:"center",color:"var(--muted)"}}>Nothing matches. Try fewer filters.</div>}""")

# 5. the All chapters list (LessonPath: kept, but no longer shown since the house became the map): the same areas
rep("""      {TOOL_CATS.filter(c => catChapterIds(c.id).length).map(c => {
        const ids = catChapterIds(c.id).filter(id => DRILLS.find(x => x.id === id));""",
"""      {TOOL_AREAS.map(a => { const cats = TOOL_CATS.filter(c => c.area === a.id && catChapterIds(c.id).length); return cats.length ? <div key={a.id}>{toolAreaHead(a)}{cats.map(c => {
        const ids = catChapterIds(c.id).filter(id => DRILLS.find(x => x.id === id));""")
i = at("      {!UI_TEACHER && <StartGuide onOpen={onOpen}/>}")
j = s.index("        );\n      })}\n", i)
s = s[:j] + "        );\n      })}</div> : null; })}\n" + s[j + len("        );\n      })}\n"):]
# 6. the search overlay: the concept buttons under their areas; the scale finder also listed under Playing scales and chords
rep("const TOOL_ALSO_IN = { 'metronome': ['practice'] };", "const TOOL_ALSO_IN = { 'metronome': ['practice'], 'scale-finder': ['k-play'] };")
rep("""              <div style={{fontSize:14,color:'var(--muted)',fontWeight:700,margin:'10px 4px 10px'}}>{t('Or jump to a topic:', '아니면 주제를 골라보세요:')}</div>
              <div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
                {TOOL_CATS.map(c => <button key={c.id} className="cat-pill" style={{fontSize:14.5,padding:'8px 15px 8px 12px'}} onClick={() => setQ(c.name)}><span className="cat-dot" style={{width:10,height:10,background:c.color}}/>{c.name}</button>)}
              </div>""",
"""              <div style={{fontSize:14,color:'var(--muted)',fontWeight:700,margin:'10px 4px 10px'}}>{t('Or jump to a concept:', '아니면 개념을 골라보세요:')}</div>
              {TOOL_AREAS.map(a => <div key={a.id} style={{marginBottom:12}}>
                <div style={{fontSize:13,fontWeight:900,color:'var(--navy)',margin:'0 4px 6px'}}>{a.name}</div>
                <div style={{display:'flex',gap:8,flexWrap:'wrap'}}>
                {TOOL_CATS.filter(c => c.area === a.id).map(c => <button key={c.id} className="cat-pill" style={{fontSize:14.5,padding:'8px 15px 8px 12px'}} onClick={() => setQ(c.name)}><span className="cat-dot" style={{width:10,height:10,background:c.color}}/>{c.name}</button>)}
                </div></div>)}""")
rep("t('Every chapter as a full lesson with a drill, grouped by topic (same groups as the Toolbox).", "t('Every chapter as a full lesson with a drill, grouped by area and concept (the same groups as the Toolbox).")
rep("'모든 챕터를 드릴이 있는 레슨으로, 주제별로 묶었어요 (도구함과 같은 묶음).", "'모든 챕터를 드릴이 있는 레슨으로, 영역과 개념별로 묶었어요 (도구함과 같은 묶음).")
rep("or browse by topic.", "or browse by area and concept.")
rep("검색하거나 주제별로 찾아보세요.", "검색하거나 영역과 개념별로 찾아보세요.")

open(dst, 'w', encoding='utf-8').write(s)
print('ok')
