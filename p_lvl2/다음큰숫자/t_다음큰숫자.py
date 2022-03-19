"""https://programmers.co.kr/learn/courses/30/lessons/12911"""


"""
사용한 논리:
주어진 n의 이진수 1의 개수를 파악
n에서 1씩 더하면서 이진수를 바꾸고, 이진수의 1의 개수를 비교
"""


def solution(n):
    num = bin(n)
    n_count = 0
    for ele in num:
        if ele == '1':
            n_count += 1
    
    while True:
        result = 0
        n+= 1
        temp = bin(n)
        for ele in temp:
            if ele == '1':
                result += 1
        
        if result == n_count:
            return n