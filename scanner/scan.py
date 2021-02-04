import os
import sys
sys.path.append('/home/will/will_workspace/python_workspace/scanner/venv/lib/python3.8/site-packages')
import pdfreader
from pdfreader import SimplePDFViewer
import re


def scan():
    file = '/home/will/Desktop/output.pdf'
    fd = open(file, "rb")
    viewer = SimplePDFViewer(fd)
    for canvas in viewer:
        page_strings = canvas.strings
        if page_strings[0] == 'Prise ':
            page_join = ''.join(page_strings)
            page_t = page_join.split('DAILY BALANCE INFORMATION')[0]
            #print(page_t)
            print("\n")
            st_per_rx = "STATEMENT PERIOD [\d]{1,2}/[\d]{1,2}/[\d]{4} To [\d]{1,2}/[\d]{1,2}/[\d]{4}"
            st_period = re.findall(st_per_rx, page_t)
            print(st_period)
            tr_date_rx = "[\d]{1,2}/[\d]{1,2}/[\d]{4} "








if __name__ == '__main__':
    scan()
