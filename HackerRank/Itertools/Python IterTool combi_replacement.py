from itertools import combinations_with_replacement
S,k = input().split()
k = int(k)

if str.isupper(S) and k > 0 and k <= len(S) :
    print('\n'.join([ ''.join(i) for i in combinations_with_replacement(sorted(S),k)]))