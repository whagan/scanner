import os
import sys
#sys.path.append('/home/will/will_workspace/python_workspace/scanner/venv/lib/python3.8/site-packages')
sys.path.extend(['C:\\Users\\nsecurity\\project\\scanner\\scanner', 'C:\\Users\\nsecurity\\project\\scanner', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages', 'C:\\Users\\nsecurity\\project\\venv\\Lib\\site-packages']
)
sys.path.append('C:\\Users\\nsecurity\\project\\venv\\Lib\\site-packages')
import pdfreader
from pdfreader import SimplePDFViewer
import re


def scan():
    #file = '/home/will/Desktop/output.pdf'
    file = 'X:\\output.PDF'
    fd = open(file, "rb")
    viewer = SimplePDFViewer(fd)
    r = 0
    for canvas in viewer:
        r = r + 1
        print(r)
        page_string = ''.join(canvas.strings)
        print("\n\n")
        if 'CALL OUR 24 HOUR TELEPHONE BANKING' in page_string:
            continue
        if 'STATEMENT PERIOD' not in page_string:
            continue
        print(page_string)
        page_top = page_string.split("Minimum Average Average Enclosed")[0]
        page_botton = page_string.split("CHECKS CHECK NO DATE AMOUNT CHECK NO DATE AMOUNT")[1]
        st_per_rx = "STATEMENT PERIOD [\d]{1,2}/[\d]{1,2}/[\d]{4} To [\d]{1,2}/[\d]{1,2}/[\d]{4}"
        st_period = re.findall(st_per_rx, page_top)
        print(st_period)
        bal_rx = "((?:\d{1,3}(?:,?\d{3})*?)\.\d{2}| \.\d{2})"
        balances = [float(x) for x in [x.strip(' ').replace(',', '') for x in re.findall(bal_rx, page_top)[:4]]]
        print(balances)
        print("LENGTH: ", len(balances) == 4)
        print("MATH: ", (balances[3] == round((balances[0] + balances[1] - balances[2]), 2))) 
        

        


if __name__ == '__main__':
    scan()
