"""https://programmers.co.kr/learn/courses/30/lessons/12915"""


"""
시도한 접근 방식 :
1. 리스트와 idx를 이용해 각 문자를 뽑아서 크기를 비교후 정렬
--문제점 : 각 문자를 개별적으로 비교후 정렬하는데 어려움
2. dict를 이용해 key에 element, value에 문자를 넣어 비교
--문제점 : 마찬가지로 이를 활용해 비교하는데 어려움
"""


def solution(strings, n):

    key = lambda x: x[n]
