a = int(input())
b = int(input())
m = int(input())

if a >= 1 and a <= 10 and b >= 1 and b <= 10 and  m >= 2 and m <= 1000 :
    pow_res = (a ** b)
    print(pow_res)
    print( pow_res % m )