class Scan:
    __slots__ = ('file')
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__slots__:
                setattr(self, key, value)
            else:
                raise ValueError("Uknown key: {!r}".format(key))


class Month(object):
    
    __slots__ = ('period', 'balances', 'num_trans', 'checks', 'other_debits', 'other_credits')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__slots__:
                setattr(self, key, value)
            else:
                raise ValueError("Unknown keyword argument: {!r}".format(key))

    def __str__(self):
        return "STATEMENT: {}".format(self.period)

    @property
    def svar(self):
        return "YO"

    def check_balances(self):
        

pq = Month(period="jan 2020", balances="2400", other_credits = "ll")
#print(pq)
#print(pq)
print(pq.period)
print(pq)
print(pq.other_credits)
print(pq.svar)
print(pq.__dict__)
