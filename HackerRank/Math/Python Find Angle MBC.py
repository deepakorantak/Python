from  math import acos,degrees,hypot

c = int(input())
a = int(input())

if c > 0 and c <= 100 and a > 0 and a <= 100 :
    b = hypot(c,a)
    #print("a = {},b = {},c = {}".format(a,b,c))

    cos_C = (a**2 + b**2 - c**2)/(2*a*b)
    #print("cos C = {}".format(cos_C))
 
    print(str(round(degrees(acos(cos_C)))) + '\u00b0')

    # original implementation
    # a1 = a
    # b1 = b/2    

    # c1_square = a1**2 + b1**2 - (2*a1*b1*cos_C)
    # #print("c1 square = {}".format(c1_square))
    
    # c1 = sqrt(c1_square)
    # #print("a1 = {},b1 = {},c1 = {}".format(a1,b1,c1))

    # B1 = acos((a1**2 + c1**2 - b1**2)/(2*a1*c1))
    # #print("acos B1 = {}".format(B1))

    # B1 = round(degrees(B1))
    # print(str(B1)+'\u00b0')