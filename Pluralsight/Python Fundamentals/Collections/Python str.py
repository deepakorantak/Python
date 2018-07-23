# join
op = ':'.join(["a","b","c"])
print(op)
op = ''.join(["Hello","Deepa","Korantak"])
print(op)

# partition
par = "abc_xyz".partition("_") 
first,_,second = "abc_xyz".partition("_")
print(par)


# split
sp = "aaa:bbb:ccc".split(":")


# format
import math
format_output = "Mathamatical constants: pi={m.pi:.4f}, e={m.e:.3f}".format(m=math)
print(format_output)

format_output = "My full name is {last} , {first} ".format(first="Deepa",last="Korantak")
print(format_output)

format_output = "Post partion the output is : {} , {} ".format(first,second)
print(format_output)

format_output = "Post split the output is : {a[0]} , {a[1]} , {a[2]}".format(a=sp)
print(format_output)

# join operator
rgb= ''.join(['Red','Green','Blue'])
print(rgb)

# split operator
result = 'one,two,three'.split(',')
print(result)

# partition operator
name = 'deepa_korantak'.partition('_')
print(name)
firstname,_,surname = name
print(firstname)
print(surname)

#format opertor
pos=[2334,5565,8999]
print("X,Y,Z coordinates of a point are X={p[0]} Y={p[1]} Z={p[2]}".format(p=pos))

import math
print("Constant values of pi={m.pi:.4f} e={m.e:.6f}".format(m=math))