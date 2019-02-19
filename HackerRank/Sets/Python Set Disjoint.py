m,n = (map(int,input().split()))
input_set = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))

# print(input_set)
# print(A)
# print(B)
# print(m)
# print(n)

def chk_valid_integer(l):
    proper_integer = (not ( i >=1 and i<= 10**9 ) for i in l)
    return  any(proper_integer)
    

if n >= 1 and n <= 10**5  and m >= 1 and m <= 10**5 and not ( chk_valid_integer(input_set) or chk_valid_integer(A) or chk_valid_integer(B)) :
     happy_score = sum([1 for input in input_set if input in A ])
     unhappy_score = sum([-1 for input in input_set if input in B ])

     print(happy_score + unhappy_score)
    