"""https://programmers.co.kr/learn/courses/30/lessons/12973"""


"""
더이상 즉흥적으로 하기에는 효율성이나 코드짜는데 어려움이 있다
레벨2부터는 적극적으로 알고리즘/자료구조를 활용할 생각부터해야할거같다
"""


def solution(s):

    s = list(s)
    temp = s
    first = ""
    second = s[0]

    while s:

        for index in range(1,len(s)):
            first = second
            second = s[index]
            if first == second:
                del s[index-1:index]
                break

        if temp == s:
            return 0

    return 1
