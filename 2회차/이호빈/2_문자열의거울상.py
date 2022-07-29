import sys

sys.stdin = open("_문자열의거울상.txt")

dictionary = {'b': 'd', 'd':'b', 'p': 'q', 'q': 'p'} #거울에 반사되는 문자열을 담은 딕셔너리
for tc in range(1, int(input())+1):
    alphabet = list(map(str, input())) #입력값을 리스트에 받아온다
    result = "" #결과값 받을 변수

    for alpha in alphabet: #입력값들을 for문을 돌아주면서
        if alpha in dictionary: # 딕셔너리에 해당 key값이 있다면
            result += dictionary[alpha] # result에 딕셔너리에 해당 value를 더해준다

    print(f"#{tc} {result[::-1]}") # 문자열 슬라이싱 이용해서 print한다
