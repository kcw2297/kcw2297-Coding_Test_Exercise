"""https://programmers.co.kr/learn/courses/30/lessons/12945"""




"""
2개의 변수를 적을 때 한줄에 적을 수 있으면 쉼표로 구분하여 적자
"""


def solution(n):

    first = 0
    second = 1

    for _ in range(n-2):
        temp = first
        first = second
        second = temp+second

    return (first+second) % 1234567


"""
def solution(n):
    first, second = 0, 1
    for _ in range(n-2):
        first, second = second, second+first
    return (first+second) % 1234567
"""
