from itertools import combinations
S,k = input().split()
k = int(k)
S = ''.join(sorted(S))
res = []

if str.isupper(S) and k > 0 and k <= len(S) :
    for c_k in range(1,k+1):
            print('\n'.join([ ''.join(i) for i in combinations(S,c_k)]))
   