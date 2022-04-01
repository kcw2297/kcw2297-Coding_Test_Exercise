"""https://programmers.co.kr/learn/courses/30/lessons/12980"""



"""
사용한 논리:
주어진 n을 2로 나누면서 홀수면 cost 1을 더한 후 1을 뺀다
이를 1이 될 때까지 반복한다


점프는 자유, 단 비용으로 처리
순간이동은 현재 이동거리*2, 무료
이동거리 변수, 비용 변수

2의 배수로 만들어 나아간다
N이 홀수면 마지막에 1을 더하고, 짝수면 그대로
"""



def solution(n):
    cost = 0

    while n >= 1:
        if n % 2 == 0:
            n = n / 2
        else:
            cost += 1
            n = n - 1
            n = n / 2
    
    return cost
