from itertools import permutations
S,k = input().split()
k = int(k)

if str.isupper(S) and k > 0 and k <= len(S) :
    print('\n'.join(sorted([ ''.join(i) for i in permutations(S,k)])))
    
   