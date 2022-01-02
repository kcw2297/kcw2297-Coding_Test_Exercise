"""https://programmers.co.kr/learn/courses/30/lessons/42889"""


"""
dictionary를 이용하여 각 스테이지에 숫자를 집계한 후에
구하려고 접근하였지만 전체 값의 오류를 고려하지 않아 실패하였다
"""

"""
교훈 : 특정 데이터 타입으로 접근하려다 실패시 다른 데이터 타입도 고려하자
"""

def solution(N, stages):
    N = sorted(stages)
    n = dict()
    tot = len(stages)
    answer = []

    for i in stages:
        n[i] = n.get(i,0)+1


    for x in range(N+1):
        start = x+1
        head = n[start]
        n[start] = head/tot
        tot = tot-head

    sorted_dict = sorted(n.items(), key = lambda item: item[1])

    for x in sorted_dict:
        answer.append(x[0])
    return answer
