#!/usr/bin/env python3
# Phase 438 on the site: the guides' front-page house without frames or lamps, and its sharing picture.
#   python3 site438.py <repo root> <this x dir>
import sys, os, shutil
root, x = sys.argv[1], sys.argv[2]
def cp(a, b): shutil.copyfile(os.path.join(x, a), os.path.join(root, b)); print('copy', b)
cp('svg/index/house-wide.svg', 'tools/lessons/svg/index/house-wide.svg')
cp('svg/index/house-tall.svg', 'tools/lessons/svg/index/house-tall.svg')
cp('img/house.jpg', 'lessons/img/house.jpg')
