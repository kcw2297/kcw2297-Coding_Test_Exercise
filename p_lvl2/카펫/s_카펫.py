


"""
둘레를 이용해 풀어낸 문제로 가로 a가 세로 b보다 커야한다
갈색 타일의 개수는 전체 가로 세로의 길이*2 -4이다
노란 타일의 개수는 (가로-2)*(세로-2)이다
"""


def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for b in range(1, total+1):
        if (total / b) % 1 == 0:
            a = total / b
            if a>= b:
                if 2*a + 2*b == brown +4:
                    return [a,b]
    return answer
