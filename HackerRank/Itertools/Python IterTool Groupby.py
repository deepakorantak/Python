from itertools import groupby
S = input()

int_validation = ( (int(i) >= 0 and int(i) <= 9) for i in S)


if all(int_validation) :
    print(*[(len(list(g)), int(k)) for k,g in groupby(S)])
   
          