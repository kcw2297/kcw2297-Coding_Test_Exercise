"""https://programmers.co.kr/learn/courses/30/lessons/82612/solution_groups?language=python3"""

"""
for loop이 아닌 수학적 방식으로 접근을 하려고 했지만 수학의 무지가 여기서 발목을 잡는다.
이번 알고리즘은 순열의 등차방식을 사용하여 접근하는 방법이었다
"""

def solution(price, money, count):
    tot = 0
    for x in range(1,count+1):
        tot += price*x

    if tot<=money:
        return 0
    else:
        return tot-money
