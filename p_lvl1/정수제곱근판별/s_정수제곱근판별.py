




"""
정수 소수를 파악하기 위해 %1 ==0을 이용한게 인상적이다

"""


def solution(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1
