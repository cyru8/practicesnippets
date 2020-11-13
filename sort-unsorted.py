#List comprehension LAMBDA
c = {"a":10, "b":20, "c":50}
print(sorted([(v,k) for (v,k) in c.items()]))