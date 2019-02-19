no_test_cases = int(input())

if no_test_cases > 0 and no_test_cases < 21 :
       
    for _ in range(no_test_cases):
        _ = int(input())
        A = set(map(int,input().split()))
        _ = int(input())
        B = set(map(int,input().split()))
       
        if len(A) > 0 and len(A) < 1001 and  len(B) > 0 and len(B) < 1001 :            
            print(A.issubset(B))
                    
