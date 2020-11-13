fname = input("Enter file: ")
if len(fname) < 1 : fname = "dict,txt"

handle = open(fname)
#print(handle)

di = dict()
for line in handle:
    line = line.rstrip()
    #print(line)
    wds = line.split()
    #print(wds)
    
    for w in wds:
        di[w] = di.get(w,0) + 1
        
        # #print(w)
        # if w in di:
        #     di[w] = di[w] + 1
        #     print("***Existing***")
        # else:
        #     di[w] = 1
        #     print("**NEW**")
        # print(w,di[w])
        
print(di)

largest = -1
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k 
        
print("Done: ", theword, largest)    
        
        
        
    




# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word,0) + 1
# print(counts)
# bigcount = None
# bigword = None

# for word,count in count.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count
# print(bigword, bigcount)
    
    
    
    
    
    