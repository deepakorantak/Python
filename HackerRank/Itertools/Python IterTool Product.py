from itertools import product

A = list(map(int,input().split()))
B = list(map(int,input().split()))

if len(A) > 0 and len(A) < 30 and len(B) > 0 and len(B) < 30 :
    for i in product(A,B) :
        print(i,end = ' ')