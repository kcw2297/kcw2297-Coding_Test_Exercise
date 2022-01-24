"""https://programmers.co.kr/learn/courses/30/lessons/12933"""



"""
sort()는 변수로 저장하지 않고 하나의 메모리 안에서 정렬
"""


def solution(n):

    n=str(n)
    n=list(n)
    n.sort(reverse=True)
    n="".join(n)
    n = int(n)
    return n
