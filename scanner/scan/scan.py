import sys
from month import *
import os
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
        self.curr_month._balances = self.get_balances()
        self.curr_month._checks = self.get_checks()
        #print(self.curr_page + "\n")
        self.curr_month._num_checks = self.get_num_checks()
        self.curr_month._other_debits = self.get_other_debits()
        self.curr_month._other_credits = self.get_other_credits()
        #print(str(self.get_num_debits()) + "\n")
        if isinstance(self.get_num_debits(), int):
            self.curr_month._num_debits = self.get_num_debits()
        print(self.curr_month._print_month())
        try:
            self.curr_month.check_num_debits()
        except ValueError as v:
            print("Whoa!")
        


    def check_period(self, period):
        if period == self.curr_period: return False
        else: return True
    
    def get_period(self):   
        period = re.findall(PER_RX, self.curr_page.split(PER_SPL)[0])
        if (len(period) != 1): raise ValueError("Error on statement period: {!r}".format(period))
        else: return period[0]
    
    def get_balances(self):
        bal_string = self.curr_page.split(BAL_SPL)[0]
        balances = [float(x) for x in [x.strip(' ').replace(',', '') for x in re.findall(BAL_RX, bal_string)[:4]]]
        if (len(balances) != 4): raise ValueError("Error on number of balances: {!r}".format(balances))
        else: return balances
    
    def get_checks(self):
        ck_string = re.split(CK_SPL, self.curr_page)[1]
        checks = re.findall(CK_RX, ck_string)
        return checks

    def get_num_checks(self):
        num_string = re.split(NUM_SPL, self.curr_page)[1]
        num_checks = int(re.search(NUM_RX, num_string).group())
        return num_checks

    def get_other_debits(self):
        db_string = re.split(DB_SPL, self.curr_page)[1]
        other_debits = [x for x in re.split(DB_RX, db_string) if x]
        return other_debits

    def get_other_credits(self):
        cr_string = re.split(CR_SPL, self.curr_page)[1]
        other_credits = [x for x in re.split(CR_RX, cr_string) if x]
        return other_credits

    def get_num_debits(self):
        if self.curr_month.check_balances:
            bal_string = self.curr_page.split(BAL_SPL)[0]
            dels = ['$', ',', ' ']
            for ch in dels:
                bal_string = bal_string.replace(ch, '')
            num_debits = int(bal_string.split(str(self.curr_month._balances[1]))[1].split(str(self.curr_month._balances[2]))[0])
            return num_debits
        return -1