if __name__ == '__main__':
    students = []
    def key(item):
        return item[1]

    key_l = lambda x: x[1]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])

    students.sort(key=key_l) 
    mark_list = [ i[1] for i in students ]
    mark_list.sort()   
    name_list = [i[0] for i in students if i[1] ==  mark_list[mark_list.count(mark_list[0])]]
    name_list.sort()
    for i in name_list :
        print(i)

        

