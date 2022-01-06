"""https://programmers.co.kr/learn/courses/30/lessons/68935?language=python3"""


"""
divmod와 int()의 새로운 사용 방법에 대해 배웠다
divmod를 이용해서 몫과 나머지를 돌려준다
int("num_string",진법)으로 문자로 된 base를 10진법으로 바꾼다
"""


def solution(n):
    answer = ''

    while n >= 1:
        n, rest = divmod(n, 3)
        answer += str(rest)

    answer = int(answer, 3)

    return answer
