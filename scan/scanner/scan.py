import sys
sys.path.append('C:\\Users\\nsecurity\\project\\venv\\Lib\\site-packages')
import pdfreader
from pdfreader import SimplePDFViewer

class Scan:
    
    def __init__(self, fp):
        self.fp = fp
    

    def run(self):
        with open(self.fp, "rb") as file_:
            viewer = SimplePDFViewer(file_)
            for canvas in viewer:
                print(canvas.strings)
  