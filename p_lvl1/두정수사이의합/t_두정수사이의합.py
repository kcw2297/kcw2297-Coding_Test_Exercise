"""https://programmers.co.kr/learn/courses/30/lessons/12912?language=python3"""


"""
a부터 b까지 1씩 증가하니깐 등차수열의 합 공식으로 풀었다
"""


def solution(a, b):
    if a==b:
        return a
    if b>a:
        answer = (b-a+1)*(a+b)/2
    elif a>b:
        answer = (a-b+1)*(a+b)/2
    return answer
