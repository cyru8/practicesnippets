largest_so_far = -1
print("Before" , largest_so_far)
number_arrays = [9,41,12,3,74,15]

for the_num in number_arrays:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print("After", largest_so_far)
