# Unpack a ship-<ts> folder from the cloud session into its places (files are rewritten in place; nothing is deleted).
import tarfile, os, sys, hashlib
S = sys.argv[1]
REN = {'center.js': 'vrvcenter.js', 'split.py': 'books-split.py', 'gen.py': 'printables-gen.py', 'items.py': 'printables-items.py'}
def ext(tgz, dest, flat=False):
    t = tarfile.open(os.path.join(S, tgz)); n = 0
    for m in t.getmembers():
        if not m.isfile(): continue
        name = os.path.normpath(m.name)
        if flat: name = REN.get(os.path.basename(name), os.path.basename(name))
        p = os.path.join(dest, name); os.makedirs(os.path.dirname(p) or '.', exist_ok=True)
        open(p, 'wb').write(t.extractfile(m).read()); n += 1
    return n
print(ext('books-latest.tgz', 'Claude outputs/Books - latest'), ext('printables.tgz', '_drafts/printables-preview'), ext('books-dir.tgz', '.'), ext('src.tgz', '_workspace/book-v3', True))
