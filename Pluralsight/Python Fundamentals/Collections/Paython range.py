# only one argument = stop argument
print("Result of one argument to Range")
for i in range(5):
   print(i)

# two arguments = start and stop argument
print('')
print("Result of two arguments to Range")
for i in range(5,10):
   print(i)

# three arguments = start , stop and step argument
print('')
print("Result of three arguments to Range")
for i in range(0,10,2):
   print(i)   

l = [112,5565,9977,757575]
it = enumerate(l)
d = {i[0]:i[1] for i in it}
print(d)



