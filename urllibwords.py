from pprint import pprint
import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

counts = dict()
for line in fhand:
    words = line.decode().strip()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#pprint(counts)
print(counts)