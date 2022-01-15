"""https://programmers.co.kr/learn/courses/30/lessons/12910?language=python3"""



"""
정답이 빈 리스트인 경우 if not answer 혹은 answer==[]으로 표현했다
"""


def solution(arr, divisor):
    answer = []
    for num in arr:
        if num%divisor ==0:
            answer.append(num)

    if answer == []:
        return [-1]
    return sorted(answer)
