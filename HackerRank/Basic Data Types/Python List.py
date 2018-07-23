if __name__ == '__main__':
    N = int(input())
    list_input = list()
    list_output = list()

    def isint(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    while(N>0):
        list_input.append(input())
        N -= 1

    for item in  list_input:
        if "insert" in item:
            opt,index,value = item.split(" ")
            if isint(value) and isint(index):
                value_int = int(value)
                index_int = int(index)
                list_output.insert(index_int,value_int)
        elif "remove" in item:
            opt,value = item.split(" ")
            if isint(value):
                value_int = int(value)
                if  value_int in list_output:
                    list_output.remove(value_int)
        elif "append" in item:
            opt,value = item.split(" ")
            if isint(value):
                value_int = int(value)
                list_output.append(value_int)
        elif "pop" in item:
            if len(list_output) > 0 :
                list_output.pop()            
        elif "sort" in item:
            list_output.sort()            
        elif "reverse" in item:
            list_output.reverse()
        elif "print" in item:
            print(list_output)              
                       