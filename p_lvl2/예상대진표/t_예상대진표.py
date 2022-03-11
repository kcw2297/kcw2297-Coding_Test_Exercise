"""https://programmers.co.kr/learn/courses/30/lessons/12985"""


"""
사용한 논리:
    다음 번호는 현재 번호의 /2인데, 짝수와 홀수인 경우를 고려해서 구함
    한번씩 나눌 수록 숫자가 올라간다
"""

def check(num):
    if num%2 == 0:
        return num//2
    else:
        return num//2 +1

def solution(n,a,b):
    count = 0
    if a == b:
        return count

    while a!=b:
        a = check(a)
        b = check(b)
        count += 1
    return count


