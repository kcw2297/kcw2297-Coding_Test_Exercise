"""https://programmers.co.kr/learn/courses/30/lessons/12913"""


"""
사용한 논리 및 오류:
그리디 문제로 간주하면 편할것 같다, 매순간 최대값을 고르는식으로한다
인덱스와 값을 비교하면서 더해간다
첫 행의 최대값을 구한 후 다음 행의 같은 인덱스를 0으로 바꾼후 max값을 찾는다


find함수를 이용해 list를 str으로 변환후 값을 찾으려하다보니 시간이 지체되었다
이를 index함수를 대체하였더니 처음 생각한 논리는 구현하였다

하지만 전체 값을 전부 고려해 O(n^2)의 시간복잡도를 나타내서 실패하였다


| 1 | 2 | 3 | 5 |
| 5 | 6 | 7 | 8 |
| 4 | 3 | 2 | 1 |
"""

def solution(lands):
    big = 0
    mid = 0
    idx = lands[0].index(max(lands[0]))

    for land in lands:
        for ele in land:
            ele += big

        land[idx] -= big
        land[idx] += mid


        big = max(land)
        land.sort()
        mid = land[-2]
        idx = land.index(max(land))
    
    return max(lands[-1])



def solution(lands):
    total = []
    

    for idx in range(len(lands[0])):
        temp = 0
        for land in lands:
            land[idx] = 0
            temp += max(land)
            idx = land.index(max(land))
        total.append(temp)
    
    return max(total)
