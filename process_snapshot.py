from decimal import *

filepath = 'balances.txt'  
max = Decimal(100000)
with open(filepath) as fp:  
    line = fp.readline()
    print(line)
    cnt = 1
    maxed = 0
    balance = Decimal(0)
    while line:
        line = fp.readline()
        if line == '':
            continue
        line = Decimal(line)
        if line > max:
            #print("maxed out with {} and max value of {}".format(line, max))
            line = max 	
            maxed += 1
        balance = balance + Decimal(line)
        cnt += 1
    print("Total Balance {}: Total Maxed: {}".format(balance, maxed))
