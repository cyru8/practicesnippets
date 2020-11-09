ages = {"Ben": 35, "Sally": 40, "Joe": 10}
print(ages)

newKey = input("Please enter the key to change: ")
raw_newValue = input("Please ente the value to chage:")
new_Value = int(raw_newValue)

ages[newKey] = new_Value
print(ages)

newKey = input("Please enter the key to add: ")
raw_newValue = input("Please ente the value to chage:")
new_Value = int(raw_newValue)

ages[newKey] = new_Value
print(ages)

remKey = input("Please enter the key to remove: ")

del ages[remKey]
print(ages)
