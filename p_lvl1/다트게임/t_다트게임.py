"""https://programmers.co.kr/learn/courses/30/lessons/17682"""

"""
숫자를 기준으로 string을 3개의 단위로 나누려고 했다. re module을
가져와서 각 숫자의 idx위치를 알아내었지만 이후 계산에서 어려움이 있었다
"""



import re

def solution(dartResult):
    접근 방법
    *와 샵과 찬스의 위치를 조사한다
    이를 이용해서 총 3개의 단위로 나눈다
    이후 정해진 값을 계산한다

    numbers = re.findall(r'\d+',dartResult) # ['1','2','10']

    for num in numbers:


    return
