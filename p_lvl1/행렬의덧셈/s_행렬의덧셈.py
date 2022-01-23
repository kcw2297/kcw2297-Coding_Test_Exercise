



"""
zip()을 활용하여서 리스트 안에 있는 값을 하나씩 비교하였다
"""


def solution(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
