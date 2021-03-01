class Month(object):
    
    __slots__ = ('period', 'balances', 'num_trans', 'checks', 'other_debits', 'other_credits')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__slots__:
                setattr(self, key, value)
            else:
                raise ValueError("Unknown key argument: {!r}".format(key))

    def __str__(self):
        return "MONTHLY STATEMENT: {}".format(self.period)

    @balances.setter
    def balances(self, value):
        if self.check_balances(value):
            self._balances = value


    def check_balances(self):
        if all(isinstance(x, float) for x in self.balances) and len(self.balances) == 4:
            return self.balances[1] + self.balances[2] == self.balances[0] + self.balances[3]
        else:
            raise ValueError("Error on balances: {!r}".format(self.balances))
    

    


        