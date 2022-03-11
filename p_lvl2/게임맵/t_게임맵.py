"""https://programmers.co.kr/learn/courses/30/lessons/1844"""




"""
사용한 논리 및 오류:
동일한 크기의 테이블을 만들어 이동시마다 1을 더한다
옆 아래가 막힌 경우 -1을 반환하는 조건을 추가한다
오류=>문제는 벽을 막힌 경우를 고려하지 않고 전체를 더했다
"""

"""
전반적인 논리는 전에 최단거리 문제와 유사했지만, 어떤식으로 조건을
설정하는지 여부에서 막혔다
deque를 활용하여 조건에 해당되는 값을 queue에 더하고 queue에 값이 없을 때까지
반복한다
"""

def solution(maps):
    
    temp = [ [0 for _ in i] for i in maps ]

    for i in range(len(maps)):
        for j in range(len(i)-1):
            if maps[i][j+1] == 0 and maps[i+1][j] == 0:
                return -1
            if maps[i][j+1] == 1:

                temp[i][j+1] += 1
            if maps[i+1][j] == 1:
                temp[i+1][j] += 1


