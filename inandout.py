#print('Hello', 'World' '!', end=' ')
#print('Hello', 'World' '!', sep=' ')
userName = input('Please enter your name:')
age = float(input('Please enter your age: '))

factor = 2
finalAge = age + factor
multAge = age * factor
divAge = age / factor

print('In', factor, 'years you will be', finalAge, 'years old', userName)
print('Your age multiplied by', factor, 'is', multAge)
print('Your age divided by', factor, 'is', divAge)

#print('Hello', userName + '!')
