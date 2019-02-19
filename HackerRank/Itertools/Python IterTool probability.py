from itertools import combinations

N = int(input())
S = list(input().split())
K = int(input())

if N >= 1 and N <= 10 and K >= 1 and K <= N and str.islower(''.join(S)) and str.isalpha(''.join(S)) :
    indices = [i+1 for i,k in enumerate(S) if k == 'a']
    combi = [i for i in combinations(range(1,N+1),K)]
    possible_val = len(set([i for i in combi for j in indices if  j in i]))
    print(possible_val/len(combi))
