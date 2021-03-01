from month import * 
from scan import *
ls = [5.50, 4.56, 5.01, 4.07]

a = Month(period="jan 2020", balances=ls)
#print(pq)
#print(pq)
print(a.period)
print(a)

d = Scan(fp='X:\\output.PDF')
d.run()