"""https://programmers.co.kr/learn/courses/30/lessons/70128?language=python3"""


"""
교훈 : pythonic하게 짜는 방법을 고려해야겠다. list comprehension 혹은
lambda와 같은 방식으로 코드의 수를 줄여보자
"""

def solution(a, b):
    answer = 0

    for idx in range(len(a)):
        a_num = a[idx]
        b_num = b[idx]
        num = a_num*b_num
        answer += num
    return answer
