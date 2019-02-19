n = int(input())
s = set(map(int,input().split()))
no_operation = int(input())

valid_element = ( i > 9 or i < 0 for i in s )

if len(s) > 0 and len(s) < 20  and no_operation > 0 and no_operation < 20 and (not any(valid_element)) :
       
    for _ in range(no_operation):
        
        command = input()
        if (' ' in command) == True:
            del_operation,element = command.split()
            element = int(element)
            getattr(s,del_operation)(element)
        else:
            getattr(s,command)() 
                          
    print(sum(s))