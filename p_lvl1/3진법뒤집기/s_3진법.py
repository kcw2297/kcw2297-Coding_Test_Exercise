

"""
divmode를 사용하였지만 조금더 전체 로직을 따른 해결방안이다
list안에 몫을 저장한 후에 reversed()로 앞뒤를 뒤집었다
"""


def solution(n):
    answer = []
    while True:
        n, rest = divmod(n, 3)
        answer.append(rest)

        if n == 0:
            break

    return sum([i * 3**idx for idx, i in enumerate(reversed(answer))])
