from sympy import *

a = 0
summ = 0
while True:
    a += 1
    if isprime(a) is True:
        summ += a
    if a >= 2000000:
        print(summ)
        break
