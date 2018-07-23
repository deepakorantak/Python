def count_substring(string, sub_string):
    found = True
    start = 0
    count = 0
    end = len(string)
    while found:
        start = string.find(sub_string,start,end)
        if start != -1:
            count += 1
            start += 1
            found = True
        else:
             found = False

    return count 

def count_substring_eff(string, sub_string):
    count = sum([1 for i in range(len(string) - len(sub_string) + 1)  if string[i:i+len(sub_string)] == sub_string ]) 
    return count   
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()    
    count = count_substring(string, sub_string)
    print(count)
