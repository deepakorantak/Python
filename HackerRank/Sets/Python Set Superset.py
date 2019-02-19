A = set(input().split(' '))
no_set = int(input())

if len(A) > 0 and len(A) < 501  and no_set > 0 and no_set < 21 :

    set_list = []
    
    for i in range(no_set):
        input_set = set(input().split(' '))
        if len(input_set) > 0 and len(input_set) < 101 :
            set_list.append(input_set)
        
                
    if len(set_list) == no_set:
        """ print("super set : ",A)
        print("no of sub sets : ",no_set)
        print("subset list : ",set_list)  """   

        print(sum([1 for i in range(no_set) if A.issuperset(set_list[i]) and len(A) > len(set_list[i])]) == no_set)