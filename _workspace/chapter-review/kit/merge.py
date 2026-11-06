# Merge the review pack: front pages + Lesson Book + Workbook + Teacher copy + draft public page, stamping pack page numbers
import pypdf, io, sys
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
CH = sys.argv[1] if len(sys.argv) > 1 else 'Chapter 1'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'review-pack.pdf'
parts = [('front.pdf', None), ('lesson.pdf', 'Lesson Book'), ('work.pdf', 'Workbook'), ('teacher.pdf', 'Teacher copy'), ('page.pdf', 'Draft public page')]
w = pypdf.PdfWriter(); n = 0
for f, label in parts:
    r = pypdf.PdfReader(f)
    for i, pg in enumerate(r.pages):
        n += 1
        W = float(pg.mediabox.width); H = float(pg.mediabox.height)
        if label:
            buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=(W, H))
            c.setFillColor(HexColor('#e4572e')); c.setFont('Helvetica-Bold', 7.5)
            c.drawRightString(W - 18, H - 12, f'{CH} review  ·  pack page {n}  ·  {label} {i + 1}/{len(r.pages)}')
            c.save(); buf.seek(0); pg.merge_page(pypdf.PdfReader(buf).pages[0])
        w.add_page(pg)
w.write(OUT); print(OUT, n, 'pages')
