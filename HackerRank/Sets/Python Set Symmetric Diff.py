m = int(input())
M = set(map(int,input().split()))
n = int(input())
N = set(map(int,input().split()))
# print(M.union(N))
# print(M.intersection(N))
res = [i for i in M.union(N) if ((i in M) or (i in N)) and i not in M.intersection(N) ]
res.sort()
for i in res : 
    print(i)