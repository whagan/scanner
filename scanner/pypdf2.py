import sys
sys.path.append('C://Users//nsecurity/project/venv//Lib//site-packages')
#sys.path.append('/home/will/will_workspace/python_workspace/scanner/venv/lib/python3.8/site-packages')

from PyPDF2 import PdfFileReader, PdfFileWriter
pdf_doc = "X://Will\'s Folder//1099_A.pdf"
pdf = PdfFileReader(pdf_doc)

for page in range(pdf.getNumPages()):
    pdf_writer = PdfFileWriter()
    current_page = pdf.getPage(page)
    print(current_page.extractText())
    #if ('Trust' in current_page.extractText()):
        #pdf_writer.addPage(current_page)
        #print("ONE")
#output = "C://Users//nsecurity//Desktop//out.pdf"
#with open(output, "wb") as out:
    #pdf_writer.write(out)

