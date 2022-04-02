"""
똑같은 결과를 다향한 방법으로 짠 부분에서, 각 함수의 사용처를 넓혀가자
"""


def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])


def solution(a, b):
    return sum(map(lambda i: a[i]*b[i], range(len(a))))
