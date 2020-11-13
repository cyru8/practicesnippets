import os
han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    wds = line.split()
    # guardian in a compound statement
    #print("Word: ",wds)
    if len(wds) < 3 or wds[0] != "From":
        continue
    #print(wds)
    print(wds[2])