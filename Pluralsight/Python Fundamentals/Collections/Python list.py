
s = [21,2,12,4]

##python shallow copy
# sc = s[:]

# print("s is sc = {}".format(s is sc))
# print("s is equal sc = {}".format(s == sc))

# sc.append(5) 

# print("post operation s is sc = {}".format(s == sc))
# print("s is {}".format(s))
# print("sc is {}".format(sc))

##python deep copy

# dc = s

# print("s is dc = {}".format(s is dc))
# print("s is equal dc = {}".format(s == dc))

# dc.append(5) 

# print("post updating dc list....")
# print("s is dc = {}".format(s is dc))
# print("s is equal dc = {}".format(s == dc))

# print("s is {}".format(s))
# print("dc is {}".format(dc))

##repitition
# r = [0,1]
# ns =[r]*3

# print("list r is {}".format(r))
# print("list ns is {}".format(ns))
# ns.append([1,1])

# print("Post appending to the inner list...")
# print("list r is {}".format(r))
# print("list ns is {}".format(ns))

## sorting and reversing
u = sorted(s)
print(s == u)


