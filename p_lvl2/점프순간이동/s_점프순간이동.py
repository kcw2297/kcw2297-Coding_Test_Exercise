

"""
내가 푼 논리와 같지만 훨씬 효율적이다
"""


def solution(n):
    cnt = 0
    while n > 0:
        q, r = divmod(n, 2)
        n = q
        if r != 0:
            cnt += 1
    return cnt




"""
홀수인 경우에만 1을 더하는 식으로 재귀함수를 만들어
홀수 값의 return이 많을 수록 값이 올라간다
"""

def solution(n):
    if n == 1:
        return 1
    if n%2 == 0:
        return solution(n/2)
    else:
        return solution(n-1)+1
    

"""
이진수로 푼 모습이다
"""

def solution(n):
    return bin(n).count('1')