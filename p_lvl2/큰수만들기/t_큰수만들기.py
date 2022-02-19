"""https://programmers.co.kr/learn/courses/30/lessons/42883"""


"""
보기에서 주어진 흐름대로 조합을 만들어 리스트 중에서 가장 큰수를 반환하게 하였다
자릿수가 적은 문제는 통과하였지만 대부분 테스트에서는 시간오류가 나왔다
"""


from itertools import combinations

def solution(number, k):
    length = len(number) - k
    num = combinations(number,length)

    nums = []
    for n in num:
        test = "".join(n)
        nums.append(int(test))

    answer = max(nums)
    return str(answer)
