#fhand = input("testinfile.txt")
#open(fhand)
fhand = open("testinfile.txt")
for line in fhand:
    line = line.rstrip()
    if line.startswith("oadetiba"):
        print(line)
    #else:
    #    print(line)
