import sys
sys.path.append('/home/will/will_workspace/python_workspace/scanner/venv/lib/python3.8/site-packages')

from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_doc = "/home/will/Desktop/test.pdf"
pdf = PdfFileReader(pdf_doc)

for page in range(pdf.getNumPages()):
    pdf_writer = PdfFileWriter()
    current_page = pdf.getPage(page)
    if ('Will' in current_page.extractText()):
        pdf_writer.addPage(current_page)
output = "/home/will/Desktop/out2.pdf"
with open(output, "wb") as out:
    pdf_writer.write(out)

