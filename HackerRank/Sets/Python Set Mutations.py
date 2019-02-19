no_set_A = int(input())
A = set(map(int,input().split()))
no_set = int(input())


if len(A) > 0 and len(A) < 1000  and no_set > 0 and no_set < 100 :
       
    for i in range(no_set):
        operation,no_elements = input().split()
        no_elements = int(no_elements)
        input_set = set(map(int,input().split()))
        if len(input_set) > 0 and len(input_set) < 100 :            
            getattr(A,operation)(input_set)
                    
    print(sum(A))