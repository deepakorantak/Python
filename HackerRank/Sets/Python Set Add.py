# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

res = set()
if N > 0 and N < 1000:
    for i in range(N):
        res.add(input())

print(len(res))