"""https://programmers.co.kr/learn/courses/30/lessons/12914"""

"""
사용한 논리:
재귀함수와 memoization을 활용해 풀어가야한느 것으로 보인다



1. 1칸 이동한 경우 해결
2. 2칸 이동하는 경우


(1칸, 1칸, 1칸, 1칸)
(1칸, 2칸, 1칸)
(1칸, 1칸, 2칸)
(2칸, 1칸, 1칸)
(2칸, 2칸)
"""


def recursion(n, count):
    if n == 1:
        return 1
    count += 1
    recursion(n-1, count)

def soluction(n):
    count = 0
    answer = recursion(n, count)

    answer = answer%1234567
    return