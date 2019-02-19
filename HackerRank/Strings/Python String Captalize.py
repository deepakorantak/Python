import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if len(s) > 0 and len(s) < 1000:
        name_list = s.split(' ')
        output = ' '.join([a.capitalize() for a in name_list])

    return output    

s = input()
result = solve(s)
print(result)