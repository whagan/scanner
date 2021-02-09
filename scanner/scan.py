#import logging
import os
import re
import sys
#sys.path.append('/home/will/will_workspace/python_workspace/scanner/venv/lib/python3.8/site-packages')
#sys.path.extend(['C:\\Users\\nsecurity\\project\\scanner\\scanner', 'C:\\Users\\nsecurity\\project\\scanner', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32\\Lib\\idlelib', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32\\python38.zip', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32\\DLLs', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32\\lib', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32', 'C:\\Users\\nsecurity\\AppData\\Local\\Programs\\Python\\Python38-32\\lib\\site-packages', 'C:\\Users\\nsecurity\\project\\venv\\Lib\\site-packages']
#)
sys.path.append('C:\\Users\\nsecurity\\project\\venv\\Lib\\site-packages')
import pdfreader
from pdfreader import SimplePDFViewer
import re

#logger = logging.getLogger(__name__)

        

def scan():
    file = '/home/will/Desktop/output.pdf'
    file = 'X:\\output.PDF'
    try:
        fd = open(file, "rb")
    except OSError:
        print('file not found')
        return
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
        get_period(page_string, r)
        page_bottom = page_string.split('CHECKS CHECK NO DATE AMOUNT CHECK NO DATE AMOUNT')[1]
        balances(page_string, r)
        checks(page_string,  r)
        

def get_period(page_string, r):
    period_string = page_string.split('PAGE 1')[0]
    st_per_rx = "STATEMENT PERIOD [\d]{1,2}/[\d]{1,2}/[\d]{4} To [\d]{1,2}/[\d]{1,2}/[\d]{4}"
    st_period = re.findall(st_per_rx, period_string)
    if (len(st_period) != 1):
        print("ERROR: STATEMENT PERIOD")
    print(st_period)

def balances(page_string, r):
    bal_string = page_string.split('CHECKS CHECK NO DATE AMOUNT CHECK NO DATE AMOUNT')[0]
    bal_rx = "((?:\d{1,3}(?:,?\d{3})*?)\.\d{2}| \.\d{2})"
    balances = [float(x) for x in [x.strip(' ').replace(',', '') for x in re.findall(bal_rx, bal_string)[:4]]]
    if (len(balances) != 4):
        print("MISSING BALANCE! Page ", r)
    if (balances[3] != round((balances[0] + balances[1] - balances[2]), 2)):
        print("BALANCE TOTALS OFF! Page ", r)


def checks(page_string, r):
    ck_string = re.split('CHECKS CHECK NO DATE AMOUNT CHECK NO DATE AMOUNT | OTHER DEBITS DATE AMOUNT DESCRIPTION', page_string)[1]
    ck_rx = "\d{3,4}\*? [\d]{1,2}/[\d]{1,2}/[\d]{4} (?:\d{1,3}(?:,?\d{3})*?)\.\d{2}"
    checks = re.findall(ck_rex, ck_string)

def other_credits(page_string, r):
    oc_string = re.split('OTHER CREDITS DATE AMOUNT DESCRIPTION | DAILY BALANCE INFORMATION DATE BALANCE DATE', page_string)[1]
    oc_rex = "[\d]{1,2}/[\d]{1,2}/[\d]{4} ((?:\d{1,3}(?:,?\d{3})*?)\.\d{2}| \.\d{2}) 
    
        


if __name__ == '__main__':
    scan()
