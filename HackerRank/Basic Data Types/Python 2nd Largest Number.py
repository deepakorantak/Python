if __name__ == '__main__':
    def check(x):
        x = int(x)
        if x <= 100 and x >= -100:
            return x
        else:
            return None
    
    n = int(input())
    arr = map(check, input().split())
    l = [i for i  in arr]
    
    if n >=2 and n <= 10 :             
        if None not in l:               
            l.sort(reverse=True) 
            count = l.count(l[0])
            print(l[count])
            