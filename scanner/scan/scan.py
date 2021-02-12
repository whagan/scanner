import sys
sys.path.append('C:\\Users\\nsecurity\\project\\venv\\Lib\\site-packages')
import pdfreader
from pdfreader import SimplePDFViewer

class Scan:
    
    def __init__(self, fp):
        self.fp = fp
        self.page_num = 0
    

    def run(self):
        with open(self.fp, "rb") as file_:
            viewer = SimplePDFViewer(file_)
            for canvas in viewer:
                self.page_increment()
                print(self.page_num)

    
    def get_page_num(self):
        return self.page_num
    
    def page_increment(self):
        self.page_num += 1

    def page_decrement(self):
        self.page_num -= 1
