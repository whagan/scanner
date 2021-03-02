import sys
from month import *
import pdfreader
from pdfreader import SimplePDFViewer
import re
from regs import *

class Scan:
    
    def __init__(self, fp):
        self.fp = fp
        self.page_num = 0
        self.curr_page = None
        self.curr_period = None
        self.curr_month = None

    def run(self):
        with open(self.fp, "rb") as file_:
            viewer = SimplePDFViewer(file_)
            for canvas in viewer:
                self.page_increment()
                #print("PAGE: ", self.page_num)
                curr_page = ''.join(canvas.strings)
                while '  ' in curr_page:
                    curr_page = curr_page.replace('  ', ' ')
                if 'STATEMENT PERIOD' not in curr_page:
                    continue
                self.curr_page = curr_page
                self.parse_page()
    
    def get_page_num(self):
        return self.page_num
    
    def page_increment(self):
        self.page_num += 1

    def page_decrement(self):
        self.page_num -= 1

    def parse_page(self):
        period = self.get_period()
        if self.check_period(period):
            self.curr_month = Month(_period=period)
            print(self.curr_month)
            print(self.curr_month._period)
        self.curr_month._balances = self.get_balances()
        print(self.curr_month._balances)
        self.curr_month._checks = self.get_checks()
        print(self.curr_month._checks)
        # print(self.curr_page)
        self.curr_month._num_checks = self.get_num_checks()
        print(self.curr_month.num_checks)
        self.curr_month.check_checks

    def check_period(self, period):
        if period == self.curr_period: return False
        else: return True
    
    def get_period(self):   
        period = re.findall(PERIOD_RX, self.curr_page.split('PAGE')[0])
        if (len(period) != 1): raise ValueError("Error on statement period: {!r}".format(period))
        else: return period[0]
    
    def get_balances(self):
        bal_string = self.curr_page.split('CHECKS CHECK NO DATE AMOUNT CHECK NO DATE AMOUNT')[0]
        balances = [float(x) for x in [x.strip(' ').replace(',', '') for x in re.findall(BAL_RX, bal_string)[:4]]]
        if (len(balances) != 4): raise ValueError("Error on number of balances: {!r}".format(balances))
        else: return balances
    
    def get_checks(self):
        ck_string = re.split('CHECKS CHECK NO DATE AMOUNT CHECK NO DATE AMOUNT | OTHER DEBITS DATE AMOUNT DESCRIPTION', self.curr_page)[1]
        checks = re.findall(CK_RX, ck_string)
        return checks

    def get_num_checks(self):
        num_string = re.split('Available Balance', self.curr_page)[1]
        num_checks = int(re.search(NUM_RX, num_string).group())
        return num_checks



