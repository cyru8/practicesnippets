import os
import myfun


# def exp(x, y):
#    z = x ** y
#    print(z)


#raw_base = input('Please enter the base value: ')
base = int(input('Please enter the base value: '))
#base = int(raw_base)

#raw_exponent = input('Please enter the exponent value: ')
exponent = int(input('Please enter the exponent value: '))
#exponent = int(raw_exponent)
myfun.exp(base, exponent)

myfun.printFib(50)

fibseries = myfun.calcFib(50)
print(fibseries)
