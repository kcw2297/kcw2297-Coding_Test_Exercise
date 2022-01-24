



"""
문제에서 500번만 반복을 해도 된다고 명시가 되어 있기에 range를 500으로
잡은 모습이다
"""


def solution(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1
