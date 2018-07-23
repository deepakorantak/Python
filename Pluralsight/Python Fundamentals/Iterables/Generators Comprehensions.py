# generator expression which returns a generator object and assigned to variable g
g = (x for x in range(1,1001) if x % 2 == 0 )
print(type(g))

# get_top is a generator since it has yield in it when called not in a loop it just returns a generator object
# in this example that generatot object is assigned to res
def get_top(cnt,x):
    counter = 0
    for i in x:
        if counter == cnt:
            return
        counter = counter+1
        print(i)
        yield i

res = get_top(3,g)        
print(res)

# actutal evaluation of the generator objects results in an iterable 
#[x for x in res]
print(sum(res))