



"""
재귀함수를 이용해서 1의 자릿수까지 반복적으로 값을 더한다
"""

def solution(number):
    if number < 10:
        return number;
    return (number % 10) + solution(number // 10)
