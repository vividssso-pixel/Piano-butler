# Cache-busting for Read & listen (her 16 Nov): every page image, pop image, clip and script URL gets ?v=<build time>,
# so a rebuilt book shows at once instead of the browser's stored copy. Safe to run again (it replaces an old ?v=).
import re, sys, time
def bust(html, v=None):
    v = v or str(int(time.time()))
    return re.sub(r'(\.webp|\.mp3|pen\.js|warm\.js)(\?v=\d+)?(?=["\'`])', lambda m: m.group(1) + '?v=' + v, html)
if __name__ == '__main__':
    p = sys.argv[1]; h = open(p).read(); n = bust(h)
    open(p, 'w').write(n); print('busted', len(re.findall(r'\?v=\d+', n)), 'urls')
