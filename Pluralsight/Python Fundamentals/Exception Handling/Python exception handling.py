import sys
import math as m

def convert_to_int(val):
    try:
        res = int(val)
    except (ValueError,TypeError) as e:
        res = -1
        print("Error in converting input {0} to integer with error:  {1}".format(str(val),type(e).__name__+","+str(e)),file=sys.stderr)
    finally:
        print("end of function - conver_to_int")

    return res    

result = convert_to_int("10")
result = convert_to_int("abcd")
result = convert_to_int([1,3,6])

def combination_cal(n,k):
    try:
        res = m.factorial(n)/(m.factorial(k)*m.factorial(n-k))
    except Exception as e:
        res = -1
        print("Error in calculatin the combination of N : {0}  and K : {1}  with error:  {2}".format(str(n),str(k),type(e).__name__+","+str(e)))
        raise 
    finally:
        print("end of function - combination_cal")

    return res    

result = combination_cal(2,3)
result = combination_cal(5,3)




