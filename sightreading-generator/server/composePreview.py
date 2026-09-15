#!/usr/bin/env python3
# ---------------------------------------------------------------------------
# Stacks a title/subtitle image on top of a score image, each independently
# horizontally centered on a shared canvas, and writes the result as a flat
# white-background PNG.
#
# Why this exists (2026-08-27): LilyPond's own header centers "title"/
# "subtitle" over the PAPER's line-width, not over the actual width of a
# short excerpt's music system -- for a 2-4 bar Preliminary piece the
# system is often much narrower than the title text, so cropping the whole
# page tightly around all the ink (title + system together) left the title
# looking off-center relative to the staff underneath it. Rendering the
# header and the score as two SEPARATE cropped images and centering each
# one independently on a common canvas guarantees true left-right symmetry
# regardless of how wide either piece is.
# ---------------------------------------------------------------------------

import sys
from PIL import Image

def main():
    if len(sys.argv) != 4:
        print('usage: composePreview.py <header.png> <score.png> <out.png>', file=sys.stderr)
        sys.exit(1)

    header_path, score_path, out_path = sys.argv[1], sys.argv[2], sys.argv[3]

    header = Image.open(header_path).convert('RGBA')
    score = Image.open(score_path).convert('RGBA')

    PAD_X = 40
    PAD_TOP = 30
    PAD_BOTTOM = 30
    GAP = 24

    width = max(header.width, score.width) + PAD_X * 2
    height = PAD_TOP + header.height + GAP + score.height + PAD_BOTTOM

    canvas = Image.new('RGBA', (width, height), (255, 255, 255, 255))

    header_x = (width - header.width) // 2
    score_x = (width - score.width) // 2

    canvas.alpha_composite(header, (header_x, PAD_TOP))
    canvas.alpha_composite(score, (score_x, PAD_TOP + header.height + GAP))

    canvas.convert('RGB').save(out_path)

if __name__ == '__main__':
    main()
