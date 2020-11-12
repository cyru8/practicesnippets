smallest = None
print("Before")
my_list = [2,4,5,6,7,8,9,5,3,93]
for value in my_list:
    if smallest is None:
        smallest = value
        #break
    elif value < smallest:
        smallest = value
    print("smallest", value)
print("After", smallest)

