"""https://programmers.co.kr/learn/courses/30/lessons/17687"""



"""
사용한 논리:
진법 변환를 위한 divmod
최대 고려 수의 범위 : t * m
특정 반복하는 숫자출력 => test와 answer의 2개의 변수에 값을 저장 및 반복

* 처음 시작을 0을 주어야만 포함시킨다
"""


def solution(n, t, m, p):
    data = "0123456789ABCDEF"
    total = '0'
    for number in range(1,t*m):
        temp = ''
        while number > 0:
            temp = data[number%n] + temp
            number //= n 
        total += temp
    return total[p-1:t*m:m]


