# expression and statements
# Logical operators (booleans)
# if, else amd elif
# Statement blocks via indentation
from pprint import pprint

name = input('Please tell me your name: ')
rawAge = input('Please tell me your age: ')
age = int(rawAge)

if age >= 21:
    print(name, 'you are at least 20 years old. You are allowed in!')
    clientDrink = print(input('What would you like to drink? '))
elif age >= 18:
    print(name, 'you are allowed in!')
    print('But you are not allowd to drink, please feel free to dance. Thanks!')
else:
    print('Unfortunately,', name, 'you are not allowed in!')
