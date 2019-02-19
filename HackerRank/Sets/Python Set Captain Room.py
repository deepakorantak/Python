K = int(input())
list_rooms = list(map(int,input().split()))

if K > 1 and K < 1000:
   
    room_num = set(list_rooms)
    captain_room =  ((sum(room_num) * K) - sum(list_rooms)) // (K-1)

    print(captain_room)

