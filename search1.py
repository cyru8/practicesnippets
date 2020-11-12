found = False
print("Before", found)

my_list =  [9,41,12,3,74,15,75]
for value in my_list:
    if value == 3:
        found = True
        break
    print(found, value)
print("After", found)


