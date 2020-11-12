data = "From steph.curry@bcchr.ca Sat Jan 3  09:23:12 2021"
atpos = data.find("@")
print(atpos)

sppos = data.find(" ",atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)