"""
itertools은 효과적으로 반복문을 사용하기 위한 함수로
for loop의 남발로 인한 시간 복작도 증가를 줄이고 코드
가독성을 올린다
"""

from itertools import combinations
def check(a, b, c):
    total = a + b + c
    for i in range(2, total):
        if total % i == 0 : return False
    return True

def solution(nums):
    answer = 0
    A = list(combinations(nums, 3))
    for i in A:
        if check(i[0], i[1], i[2]): answer += 1
    return answer
