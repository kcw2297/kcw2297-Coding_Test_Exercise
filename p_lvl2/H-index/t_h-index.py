"""https://programmers.co.kr/learn/courses/30/lessons/42747"""




"""
문제에서 요구하는 것이 인용이 된 논문의 개수와 인용된 수가 같은 값을 반환하는
것이었는데, 잘못 이해하고 중간 값에 해당되는 값을 반환하였다
"""


def solution(citations):

    lessStack = []
    moreStack = []
    citations.sort()

    for idx in range(len(citations)):
        middle = citations[idx]

        for cite in citations:
            if cite >= middle:
                moreStack.append(cite)

        if len(lessStack) == len(moreStack):
            return middle
        else:
            lessStack = []
            moreStack = []
    return False
