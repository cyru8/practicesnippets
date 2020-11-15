import re
x = "This is my study cave time with my other half from 20:00 to 23:59 and 04:00"
y = re.findall("[0-9]+",x)
print(y)