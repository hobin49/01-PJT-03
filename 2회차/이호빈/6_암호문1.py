import sys

sys.stdin = open("_암호문1.txt")

for tc in range(1, 11):
    n = int(input())
    original = list(input().split())

    order_number = int(input())
    order = list(input().split())

    idx = 0 
    i_count = 0
    for i in range(len(order)): # 0부터 59까지
        
        if order[i] == "I":
            #[1,10, 2,3,3,3] #인덱스를 삽입하면 계속 늘어난다
            idx = int(order[i + 1]) #1 더하면 더한다
            i_count = int(order[i + 2]) # i + 2 (삽입, x, y)
            
            for j in range(i_count-1, -1, -1):
                original.insert(idx, order[i + j + 3]) #삽입(x, y, s)
    #I(삽입) x, y, s 핵심

    print(f"#{tc}", end=" ")
    print(*original[:10]) 