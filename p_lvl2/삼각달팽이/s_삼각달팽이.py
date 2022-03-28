

"""
사용한 논리:
삼각형의 구조를 배열을 이용해서 만든다
이후 인덱스를 이용해 x==행, y==해당 행의 인덱스로 사용한다
num은 1부터 시작하여서 1씩 더해간다
%를 이용해 나머지에 따라서 좌표 값을 바꾼다
"""


def solution(n):
    answer = [[0 for _ in range(1, i+1)] for i in range(1, n+1)] #삼각형구조 만들기

    x, y = -1, 0 # 좌표 초기화, 처음 시작은 아래로 내려가기에 x=-1
    num = 1

    for i in range(n): # 방향 0
        for _ in range(i, n): # 좌표 구하기 0 1 2 3
            if i % 3 == 0: # 하
                x += 1 # x = 0
            elif i % 3 ==1: # 우
                y += 1 # y = 1
            else: # 상
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    return sum(answer, [])

