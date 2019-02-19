N,M = input().split(" ")
N = int(N)
M = int(M)
pattern = '.|.'
padding = '-'
if (N > 5 and N < 101 ) and (M > 15 and M < 303) and N % 2 > 0 and  N * 3 == M :
    """ mid_line = int(N/2)
    for n in range(N):
        if n < mid_line:
            factor = 0
        else: 
            factor = N - 1 

        pattern_repeat = abs(factor - n )  * 2 + 1  
        
        if n == mid_line :
            print('WELCOME'.center(M,padding))
        else:
            print((pattern * pattern_repeat).center(M,padding)) """

    output = [(pattern * (i*2 + 1)).center(M,padding) for i in range(N//2) ]
    output = ('\n').join(output + ['WELCOME'.center(M,padding)] + output[::-1])
    print(output)
                   




        




