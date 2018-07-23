import time
s = ["a","b"]

def append_list(a=[],b=time.ctime()):
    a.append('z')
    return (a,b)
    
print(append_list())    
print(append_list(s))
print(append_list())
print(append_list())


