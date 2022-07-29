import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for tc in range(1, T+1):
    # 3개의 숫자를 list에 담아준다
    numbers = list(map(int,input().split()))
    # 리스트를 오름차순으로 정렬해준다
    numbers.sort()
 
    # 0번째 인덱스와 그 다음 인덱스가 불일치하면 서로 다른 값이기 때문에
    if numbers[0] != numbers[1]: 
        print(f'#{tc} {numbers[0]}') #0번째 인덱스의 값을 넣어주고 
    else:
        print(f'#{tc} {numbers[2]}') # 같다면 2번째 인덱스의 값이 다른 값이기에 출력해준다.