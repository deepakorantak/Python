# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng_set = set(map(int,input().split()))

b = int(input())
french_set = set(map(int,input().split()))

total_student = [i for i in eng_set.union(french_set) if ((i in eng_set) or (i in french_set)) and i not in eng_set.intersection(french_set) ]
if len(total_student) > 0 and len(total_student) < 1000:
    print(len(total_student))
