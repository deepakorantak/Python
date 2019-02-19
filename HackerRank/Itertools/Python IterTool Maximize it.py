from itertools import product
input_list = list(map(int,input().split()))
K,M = input_list[0],input_list[1]
lol = []


if K >= 1 and K <= 7 and M >=1 and M <= 1000:
    for i in range(K) :
        l = list(map(int,input().split()))        
        N , l = l[0],l[1:] 
        element_val = ( e < 1 or e > 10 ** 9 or len (l) > 7 or len (l) < 1 for e in l)
        if N >= 1 and N <= 7 and not any(element_val) :
            lol.append(l)
            
       
    res = map( lambda x : sum(i ** 2 for i in x) % M , product(*lol))     
    print(max(res))

