class Month(object):
    
    # __slots__ = ('period', 'balances', 'num_trans', 'checks', 'other_debits', 'other_credits')
    period = None
    balances = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            print("KEY: ", key, "VALUE: ", value)
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                raise ValueError("Unknown key argument: {!r}".format(key))

    def __str__(self):
        return "MONTHLY STATEMENT: {}".format(self.period)

    def set_balances(self, balances):
        try:
            if self.check_balances(balances):
                self.balances = balances
        except ValueError:
            pass


    def check_balances(self, balances):
        if all(isinstance(x, float) for x in balances) and len(balances) == 4:
            return balances[1] + balances[2] == balances[0] + balances[3]
        else:
            raise ValueError("Error on balances: {!r}".format(balances))
    

    


        