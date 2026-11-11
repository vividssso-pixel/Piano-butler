# New cast (her 11 Nov): the Doorkeeper (rook), the Guest (knight), the Stationmaster (bishop) -- Staunton pieces like the King and Queen.
NV, CO, W = '#26296b', '#e4572e', '#fff'
def cr(pts, closed=True):
    # Catmull-Rom through pts -> cubic bezier path
    n = len(pts); P = pts + pts[:2] if closed else pts
    d = f'M{pts[0][0]:.2f} {pts[0][1]:.2f}'
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p0 = pts[(i - 1) % n] if closed else pts[max(i - 1, 0)]
        p1, p2 = pts[i % n], pts[(i + 1) % n]
        p3 = pts[(i + 2) % n] if closed else pts[min(i + 2, n - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6); c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += f' C{c1[0]:.2f} {c1[1]:.2f} {c2[0]:.2f} {c2[1]:.2f} {p2[0]:.2f} {p2[1]:.2f}'
    return d + (' Z' if closed else '')
def sym(half):   # half profile from the bottom right going up -> full closed outline
    return [(x, y) for x, y in half] + [(-x, y) for x, y in reversed(half)]
BASE = [(22, 0), (22.8, -3.4), (21, -6.6), (18.6, -8.2), (19.2, -10.4), (16.4, -12.8), (13.2, -14.6)]
HL = lambda ds: '<g fill="none" stroke="#fff" stroke-opacity="0.55" stroke-width="0.9" stroke-linecap="round">' + ''.join(f'<path d="{d}"/>' for d in ds) + '</g>'
def foot(): return [f'M-18.9 -3.1 Q0 -1.7 18.9 -3.1', f'M-15.3 -11.6 Q0 -10.2 15.3 -11.6']

def rook():
    half = BASE + [(12, -19), (11.2, -34), (11.6, -46), (14.4, -51), (16.6, -54.5)]
    pts = sym(half)
    body = f'<path d="{cr(pts)}"/>'
    # the crown: a block with three merlons
    crown = '<path d="M-17 -53 L17 -53 L17.6 -66 L17.6 -74 L11 -74 L11 -68.5 L3.4 -68.5 L3.4 -74 L-3.4 -74 L-3.4 -68.5 L-11 -68.5 L-11 -74 L-17.6 -74 L-17.6 -66 Z"/>'
    g = f'<g fill="{NV}" stroke="{NV}" stroke-width="0.8" stroke-linejoin="round">{body}{crown}</g>'
    # the door: an arched door cut in the body, in white line, a coral knob
    door = f'<path d="M-5.6 -15.5 L-5.6 -31 A5.6 5.6 0 0 1 5.6 -31 L5.6 -15.5" fill="none" stroke="#fff" stroke-width="1.3" stroke-opacity="0.9"/><path d="M0 -36.6 L0 -15.5" stroke="#fff" stroke-width="0.8" stroke-opacity="0.6"/><circle cx="3" cy="-23.5" r="1.2" fill="{CO}"/>'
    # the key ring on the right side: a coral ring and two keys
    keys = f'<g fill="none" stroke="{CO}" stroke-width="1.6" stroke-linecap="round"><circle cx="17.6" cy="-40" r="4"/><path d="M17.2 -36 L15.6 -28 M15.6 -28 L13.4 -28.6 M15.9 -30.4 L13.8 -31"/><path d="M19.6 -36.6 L23.4 -29.4 M23.4 -29.4 L25.4 -30.4 M22.4 -31.4 L24.4 -32.4"/></g>'
    hl = HL(foot() + ['M-14.6 -56 Q0 -54.6 14.6 -56', 'M-8.6 -44 L-8.2 -38'])
    return g + hl + door + keys

def knight():
    half_base = BASE + [(12.6, -18.4)]
    head = [(13.6, -24), (15.4, -33), (15.6, -42), (13.2, -52), (9.4, -60), (5.4, -65), (3.6, -71), (0.6, -66.2), (-3.4, -64.6),
            (-9.6, -60.8), (-15.6, -54.6), (-20.6, -48.4), (-22.4, -44.2), (-20.8, -40.6), (-16.4, -39.8), (-11.2, -42.2), (-8.4, -40.4),
            (-8.2, -35), (-10.6, -27.6), (-12.6, -18.4)]
    left = [(-x, y) for x, y in reversed(BASE)]
    pts = half_base + head + left
    g = f'<g fill="{NV}" stroke="{NV}" stroke-width="0.8" stroke-linejoin="round"><path d="{cr(pts)}"/></g>'
    eye = '<ellipse cx="-6.4" cy="-55" rx="1.6" ry="1.2" fill="#fff"/><path d="M-18.6 -45 Q-17.6 -43.6 -16.2 -44.2" fill="none" stroke="#fff" stroke-width="0.8" stroke-opacity="0.7" stroke-linecap="round"/>'
    mane = HL(foot() + ['M12.6 -26 Q14.6 -40 10.6 -54', 'M9 -27 Q10.4 -38 7.2 -50', 'M-12.2 -16.4 Q0 -15.2 12.2 -16.4'])
    # the Guest's hat: a coral top hat at a jaunty angle, a white band with a sharp sign
    hat = (f'<g transform="rotate(-14 -3 -70)"><ellipse cx="-3" cy="-69.4" rx="11.4" ry="2.6" fill="{CO}"/><path d="M-10 -70 L-9 -86 L3 -86 L4 -70 Z" fill="{CO}"/>'
           f'<path d="M-9.7 -72.6 L3.7 -72.6 L3.55 -74.6 L-9.55 -74.6 Z" fill="{NV}"/>'
           f'<g stroke="#fff" stroke-width="1.15" stroke-linecap="round"><path d="M-4.6 -76.8 L-4.9 -84.2 M-1.4 -77.4 L-1.7 -84.8 M-6.6 -79.4 L0.6 -80.6 M-6.6 -82 L0.6 -83.2"/></g></g>')
    return g + mane + eye + hat

def bishop():
    half = BASE + [(11.8, -19), (9.4, -32), (7.4, -46), (8.2, -50.6), (12.6, -52.2), (12.8, -55.4), (8.4, -57.4)]
    pts = sym(half)
    g = f'<g fill="{NV}" stroke="{NV}" stroke-width="0.8" stroke-linejoin="round"><path d="{cr(pts)}"/><ellipse cx="0" cy="-66" rx="9.4" ry="10"/></g>'
    # the Stationmaster's cap: a coral peaked cap with a navy peak and a white badge
    cap = (f'<path d="M-10.6 -72 L-12.4 -80.6 Q0 -84.4 12.4 -80.6 L10.6 -72 Z" fill="{CO}"/>'
           f'<path d="M-10.8 -72.4 L10.8 -72.4 L10.8 -70.2 L-10.8 -70.2 Z" fill="{NV}" stroke="#fff" stroke-width="0.6"/>'
           f'<path d="M-11.2 -70.6 Q-4 -66.8 6 -69.4 L-2 -70.6 Z" fill="{NV}" stroke="{NV}" stroke-width="1.2" stroke-linejoin="round"/>'
           f'<circle cx="0" cy="-77" r="1.8" fill="#fff"/>')
    # a pocket watch on a chain: a coral rim, a white face, two hands
    watch = (f'<path d="M-6.8 -45 Q-2 -38 3.2 -33.8" fill="none" stroke="{CO}" stroke-width="1" stroke-dasharray="1.4 1"/>'
             f'<circle cx="5" cy="-30" r="5" fill="#fff" stroke="{CO}" stroke-width="1.8"/><path d="M5 -30 L5 -33.2 M5 -30 L7.4 -29" stroke="{NV}" stroke-width="0.9" stroke-linecap="round"/>')
    hl = HL(foot() + ['M-10.6 -54 Q0 -52.6 10.6 -54', 'M-4.6 -20 L-3.4 -42'])
    return g + hl + cap + watch

PIECES = {'doorkeeper': rook(), 'guest': knight(), 'stationmaster': bishop()}
if __name__ == '__main__':
    import json, re
    s = open('/tmp/claude-0/dr/drills.src.html').read()
    get = lambda n: json.loads(s[s.index('const ' + n + ' = ') + len(n) + 9: s.index('\n', s.index('const ' + n + ' = '))].rstrip(';'))
    K, Q, P = get('VIC_KING'), get('VIC_QUEEN'), get('VIC_PAWN')
    cast = [('The King', 'bass clef', K), ('The Queen', 'treble clef', Q), ('The Doorkeeper', 'key signature', PIECES['doorkeeper']),
            ('The Guest', 'accidentals', PIECES['guest']), ('The Stationmaster', 'time signature', PIECES['stationmaster']), ('Clara', 'the student', P)]
    o = ''
    for i, (n, r, svg) in enumerate(cast):
        x = 70 + i * 120
        o += f'<g transform="translate({x},150)">{svg}</g><text x="{x}" y="178" font-family="Cormorant Garamond, Georgia, serif" font-size="15" font-weight="700" fill="{NV}" text-anchor="middle">{n}</text><text x="{x}" y="196" font-family="Inter, Arial, sans-serif" font-size="9.5" letter-spacing="1.4" fill="{CO}" text-anchor="middle">{r.upper()}</text>'
    floor = ''.join(f'<rect x="{x}" y="{214 + (k%2)*8}" width="8" height="8" fill="{NV}"/>' for k, x in enumerate(range(10, 720, 8)) if True)
    open('/tmp/claude-0/cast/cast-lineup.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 730 232" width="1460" height="464"><rect width="730" height="232" fill="#fff"/><path d="M10 206 L720 206" stroke="{NV}" stroke-opacity="0.3"/>{o}</svg>')
    json.dump(PIECES, open('/tmp/claude-0/cast/newcast.json', 'w'))
    print('ok')
