import sys
a, b = sys.argv[1], sys.argv[2]
s = open(a, encoding='utf-8').read()
def rep(x, y, n=1):
    global s
    assert s.count(x) == n, (s.count(x), x[:80])
    s = s.replace(x, y)
# Scales: lessons 1-11, then the Scale finder as the last step (the Try step)
rep("""'sc-chrom', 'sc-min', 'sc-modes'], check: 'scales', tools: [], more: [],
    tryLine: ['Twelve short lessons: the shape, fingering, all twelve keys, the minor scales, the modes', '열두 개의 짧은 레슨: 모양, 손가락, 열두 조, 단음계, 선법'],""",
"""'sc-chrom', 'sc-min'], check: 'scales', tools: ['scale-finder'], more: [],
    tryLine: ['Scale finder: turn the circle of fifths to any key', '스케일 찾기: 5도권을 돌려 어느 조든 찾아요'],""")
# Modes: its own concept after Scales
rep("""    checkLine: ['Questions, level by level', '문제를 단계별로'],
  },
};
const HOME_AREA_LINE""", """    checkLine: ['Questions, level by level', '문제를 단계별로'],
  },
  'p-modes': {
    lessons: ['sc-modes'], tools: [], more: [],
  },
};
const HOME_AREA_LINE""")
rep("{ id: 'p-scale', area: 'pitch', en: 'Scales', ko: '스케일' }]", "{ id: 'p-scale', area: 'pitch', en: 'Scales', ko: '스케일' }, { id: 'p-modes', area: 'pitch', en: 'Modes', ko: '선법' }]")
rep("  'p-scale': ['The same pattern from every note', '어느 음에서나 같은 패턴'],", "  'p-scale': ['The same pattern from every note', '어느 음에서나 같은 패턴'],\n  'p-modes': ['The same notes, a new home', '같은 음, 새로운 집'],")
rep("      <button onClick={() => go({ view: 'home', drill: live.check, tab: 'drill', level: 1, mode: 'lesson' })} style={{display:'block'", "      {live.check && <button onClick={() => go({ view: 'home', drill: live.check, tab: 'drill', level: 1, mode: 'lesson' })} style={{display:'block'")
rep("{t('Start the drill →', '드릴 시작 →')}</button>\n    </div>\n  );\n  // level 1", "{t('Start the drill →', '드릴 시작 →')}</button>}\n    </div>\n  );\n  // level 1")
rep("  TOOL_CONCEPT[id] = 'p-scale';\n});", "  TOOL_CONCEPT[id] = id === 'sc-modes' ? 'p-modes' : 'p-scale';\n  if (id === 'sc-modes') Object.defineProperty(tl, 'kicker', { get: () => TOOL_AREAS.find(a => a.id === 'pitch').name + ' · ' + (LANG === 'ko' ? '선법' : 'Modes'), enumerable: true, configurable: true });\n});")
open(b, 'w', encoding='utf-8').write(s)
