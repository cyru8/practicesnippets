ages = {"Ben": 20, "Len": 40, "wayne": 27}
print(ages)

print(ages.keys())
x = ages.keys()
# print(x[Ben])

for age in ages:
    # print(age)
    print('The age of ', age, 'is', ages[age], sep=(' '))
