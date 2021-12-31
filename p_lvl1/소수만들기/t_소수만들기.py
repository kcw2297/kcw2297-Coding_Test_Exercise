"""https://programmers.co.kr/learn/courses/30/lessons/12977"""


"""
pseudo code를 파이썬 문법에 맞게 변경만 한 것이다
for loop을 3중 중첩으로 비효율적이고 가독성이 떨어지기에
itertools 모듈을 사용하여 combinations 조합 함수를 사용한다
"""

def check(a, b, c):
    total = a + b + c
    for i in range(2, total):
        if total % i == 0 : return False
    return True

def solution(nums):
    answer = 0
    for i in range(0, len(nums) - 2):
        for j in range(i+1, len(nums) - 1):
            for k in range(j+1, len(nums)):
                if check(nums[i], nums[j], nums[k]): answer += 1
    return answer
