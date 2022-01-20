"""https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3"""



"""
파이썬에서 iterable한 것은 string이니깐 문자를 string을
바꾼 후에 for loop으로 하나씩 list에 저장 후 전체를 더했다
"""


def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))

    return sum(answer)
