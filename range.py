from pprint import pprint

numbers = range(1, 50, 10)
print(list(numbers))

for number in numbers:
    print(number)

# Applies same way to string literals
names = ['Ben', 'Alice', 'james', 'Banjo']
print(names)

for name in names:
    print(name, 'is a great person!')
