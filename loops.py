# for loop - for x in objects
# while loop - while <exp> is true until <exp> is false
# range - [range to loop over]

from pprint import pprint

#strnum = print(input('Please enter a number: '))
#num = int(strnum)
num = 17
#prime = True

for test in range(2, num):
    if num % test == 0 and num != test:
        print(num, 'equals', test, '*', num/test)
#        prime = False
        break
else:
    print(num, 'is a prime number!')
# if prime:
#    print(num, 'is a prime number!')
# else:
#    print(num, 'is not a prime number')
