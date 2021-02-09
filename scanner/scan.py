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

class Month:
    
    def __init__(self, period):
        period = None
        balances = None
        checks = None
        other_debits = None
        other_credits = None
        for (key, value) in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    def __str__(self):
        return f"{self.period}"



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
        while '  ' in page_string:
            page_string = page_string.replace('  ', ' ')
        print("\n\n")
        if 'CALL OUR 24 HOUR TELEPHONE BANKING' in page_string:
            continue
        if 'STATEMENT PERIOD' not in page_string:
            continue
        #print(page_string)
        print("PERIOD: ", get_period(page_string, r))
        print(balances(page_string, r))
        print("CHECKS: ", checks(page_string,  r))
        print("OTHER DEBITS: ", other_debits(page_string, r))
        print("OTHER CREDITS: ", other_credits(page_string, r))
        

def get_period(page_string, r):
    period_string = page_string.split('PAGE 1')[0]
    st_per_rx = "STATEMENT PERIOD [\d]{1,2}/[\d]{1,2}/[\d]{4} To [\d]{1,2}/[\d]{1,2}/[\d]{4}"
    st_period = re.findall(st_per_rx, period_string)
    if (len(st_period) != 1):
        return("ERROR: STATEMENT PERIOD PAGE ", r)
    return(st_period)

def balances(page_string, r):
    bal_string = page_string.split('CHECKS CHECK NO DATE AMOUNT CHECK NO DATE AMOUNT')[0]
    bal_rx = "((?:\d{1,3}(?:,?\d{3})*?)\.\d{2}| \.\d{2})"
    balances = [float(x) for x in [x.strip(' ').replace(',', '') for x in re.findall(bal_rx, bal_string)[:4]]]
    if (len(balances) != 4):
        print("MISSING BALANCE! Page ", r)
    if (balances[3] != round((balances[0] + balances[1] - balances[2]), 2)):
        print("BALANCE TOTALS OFF! Page ", r)
    return balances


def checks(page_string, r):
    ck_string = re.split('CHECKS CHECK NO DATE AMOUNT CHECK NO DATE AMOUNT | OTHER DEBITS DATE AMOUNT DESCRIPTION', page_string)[1]
    ck_rx = "\d{3,4}\*? [\d]{1,2}/[\d]{1,2}/[\d]{4} (?:\d{1,3}(?:,?\d{3})*?)\.\d{2}"
    checks = re.findall(ck_rx, ck_string)
    return(checks)

def other_debits(page_string, r):
    od_string = re.split('OTHER DEBITS DATE AMOUNT DESCRIPTION | OTHER CREDITS DATE AMOUNT DESCRIPTION', page_string)[1]
    od_rx = "([\d]{1,2}/[\d]{1,2}/[\d]{4} (?:\d{1,3}(?:,?\d{3})*?)\.\d{2} (?:(?![\d]{1,2}/[\d]{1,2}/[\d]{4}).)*)"
    other_debits = [x for x in re.split(od_rx, od_string) if x]
    return(other_debits)

def other_credits(page_string, r):
    oc_string = re.split('OTHER CREDITS DATE AMOUNT DESCRIPTION | DAILY BALANCE INFORMATION DATE BALANCE DATE', page_string)[1]
    oc_rx = "([\d]{1,2}/[\d]{1,2}/[\d]{4} (?:\d{1,3}(?:,?\d{3})*?)\.\d{2} (?:(?![\d]{1,2}/[\d]{1,2}/[\d]{4}).)*)"
    other_credits = [x for x in re.split(oc_rx, oc_string) if x]
    return(other_credits)
    


if __name__ == '__main__':
    scan()
