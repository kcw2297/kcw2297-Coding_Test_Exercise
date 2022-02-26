"""https://programmers.co.kr/learn/courses/30/lessons/60057"""



"""
문제에서 3개단위로 자른다는 의미를 잘못 이해했다
대표적인 자료구조/알고리즘으로 풀리지 않는다면 for, str 등등 customize하자
in range(::x)에서 특정 단위로 반복하는 것을 이용해 풀어낸 문제이다
"""


# # Stack을 활용해 하나씩 비교하려하였지만, 단위 계산에서 막혔다
# def solution(s):
#     if len(s) == 1:
#         return 1
    
#     min_num = 0
#     count = 0
#     stack = []
#     temp = 0

#     for num in range(2,len(s)):
#         temp = 0
#         for str in s:
#             if stack[] == str and temp>=num:
#                 count += 1
#                 stack.pop()
#             stack.append(str)
