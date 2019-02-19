def merge_the_tools(string, k):
    # your code goes here
    def get_unique_string(s):
        i = 1
        n = len(s)
        while i < n:
            if s[i] == s[i-1]:
                s = s[:i-1] + s[i :]
                i = 1
                n = len(s)
            else:
                i += 1    
        
        print(s)

    n = len(string)
    if n >= 1 and n <= 10**4 and k >= 1 and k <= n and n%k == 0 :
    
        l_seg = n/k

        # for i in range(k):
        #     start = int(i*l_seg)
        #     end = int(start + l_seg)
        #     seg = string[start:end]
            #get_unique_string(seg)  
      

        for seg in zip(*[iter(string)] * k):   
            
            #res = [ ele for i in range[k] for index,ele in enumerate(string[i*l_seg:(i*l_seg)+ l_seg]) if ele not in string[i*l_seg:(i*l_seg)+ l_seg][:index] ]
            res =   ''.join([ ele for index,ele in enumerate(seg) if ele not in seg[:index]])
            print(seg)
            print(res)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

    