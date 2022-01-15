




"""
파이썬에서 빈 리스트는 false로 인식하기에 or를 이용해서 조건에 따른
결과 반환을 하였다
"""


def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
