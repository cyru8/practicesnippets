# collections, lists and dictionaries
# Lists: x = [1,2,3,4,5] -- index and value,can contain different data types. can contain sub/child list e.g: x[0]
# Tuple: y = (1,2,3,4,5) -- They are imutable- unchangeable e.g: could be used to store months of the year as this does not change.
# Dictionaty: z = {'jack': 123, 'ben': 456} -- key-value pair z['ben']

x = [1, 2, 3, 4, 5]  # lists
print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

y = (1, 2, 3)  # Tuple
print(y)
print(y[0])
print(y[1])
print(y[2])

z = {'ben': 1, 'jack': 2, 'joe': 2, 99: 3}
print(z)
print(z['ben'])
print(z['jack'])
print(z['joe'])

names = ["Ben", "Sally", "Amy", "Randy", "Joe", "Ire"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])

print("")

for name in names:
    print(name)
print("")

l = len(names)
print(l)
print("")

for index in range(0, len(names)):
    print(names[index], 'is found at index', index)
print("")

# Using index function
q = names.index("Amy")
print(q)
print('')

for name in names:
    print(name, 'is found at index:', names.index(name))
print('')
