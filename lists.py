from pprint import pprint

names = ["Ben", "Jack", "Len", "Santos", "Banjo"]
print(names)

raw_newIndex = input('Please enter the index to replace: ')
integNewIndex = int(raw_newIndex)
# print(integNewIndex)

newName = input('Please enter the name to put into index: ')

names[integNewIndex] = newName
print(names)

newName = input('Please enter the name to add to the list: ')
names.append(newName)
print(names)

remName = input('Please enter the name to remove from the list: ')
names.remove(remName)
print(names)
