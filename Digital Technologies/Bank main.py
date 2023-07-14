from Account import *

a = Account(123, 'Bailey', 'pass', 1000) 
a.withdraw(1200)

l = []

try:
    l.pop()
except AccountBalanceError:
    print("Can't help you!!")

print("We still going!")