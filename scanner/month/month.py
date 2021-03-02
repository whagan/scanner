class Month(object):
    
    # period = None
    # _balances = None
    # checks = None
    # num_checks = None

    #atts = ['_period', '_balances', 'checks', 'num_checks']

    def __init__(self, **kwargs):
        atts = ['_period', '_balances', '_checks', '_num_checks', '_other_debits', '_other_credit']
        for key, value in kwargs.items():
            if key in atts:
                setattr(self, key, value)
            else:
                if key in atts:
                    setattr(self, key, None)
                else:
                    raise ValueError("Unknown key argument: {!r}".format(key))

    def __str__(self):
        return  "MONTHLY STATEMENT: {}".format(self._period) 

    def _print_month(self):
        return  "MONTHLY STATEMENT: {}".format(self._period) + \
                "\nBALANCES: {}".format(self._balances) + \
                "\nNUMBER OF CHECKS: {}".format(self._num_checks) + \
                "\nCHECKS: {}".format(self._checks) + \
                "\nOTHER DEBITS: {}".format(self._other_debits) + \
                "\nOTHER CREDITS: {}".format(self._other_credits) + \
                "\n"
    
    @property
    def period(self):
        return self._period
    
    @period.setter
    def period(self, period):
        self._period = period

    @property
    def balances(self):
        return self._balances

    @balances.setter
    def balances(self, balances):
        try:
            if self.check_balances(balances):
                self._balances = balances
        except ValueError:
            pass

    @property
    def checks(self):
        return self._checks

    @checks.setter
    def checks(self, checks):
        self._checks = checks

    @property
    def num_checks(self):
        return self._num_checks

    @num_checks.setter
    def num_checks(self, num_checks):
        self._num_checks = num_checks

    @property
    def other_debits(self):
        return self._other_debits

    @other_debits.setter
    def other_debits(self, other_debits):
        self._other_debits = other_debits
    
    @property
    def other_credits(self):
        return self._other_credits

    @other_credits.setter
    def other_credits(self, other_credits):
        self._other_credits = other_credits

    def check_balances(self, balances):
        if all(isinstance(x, float) for x in balances) and len(balances) == 4:
            return round((balances[0] + balances[1]), 2) == round((balances[2] + balances[3]), 2)
        else:
            raise ValueError("Error on balances: {!r}".format(balances))
    
    def check_checks(self):
        if len(self._checks) != self._num_checks:
            raise ValueError("Error: Number of checks not equal to checks counted: {!r} - {!r}".format(self._num_checks, self._checks))


        



    


        