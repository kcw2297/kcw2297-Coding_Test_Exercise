



"""
수학적 논리로 1의 나머지를 구하기 위해 1을 뺀 후에 그 값의
약수 중 가장 작은 값을 돌려냈다
"""


def solution(n):
    answer = 0
    n -= 1
    div = []
    for i in range(2, n+1):
        if n % i == 0:
            div.append(i)

    answer = div[0]
    return answer
