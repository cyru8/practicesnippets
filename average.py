count = 0
sum = 0
print("Before", count, sum)

my_list =  [9,41,12,3,74,15,75]

for value in my_list:
    count += 1     # an also be written as count = count + 1
    sum = sum + value
    average = sum / count
    f_average = float(average)
    print(count, sum, value)
print("After", count, sum, f_average)


