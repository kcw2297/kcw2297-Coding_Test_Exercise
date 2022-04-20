"""https://programmers.co.kr/learn/courses/30/lessons/70129"""


"""
사용한 논리:
재귀함수를 이용해서 반복되는 0을 제거하고 이진수로 변환한다
"""    


from math import remainder


def zero_check(s, total,repeat):
    if len(s) < 1:
        return total, repeat

    repeat += 1
    zero = s.count('0')
    one = s.count('1')

    total += zero
    binary = str(format(one,'b'))
    if binary.count('1') == 1 and binary.count('0') == 0:
        return total, repeat
    else:
        return zero_check(binary, total,repeat)


def solution(s):
    count_z = 0
    repeat=0
    count_z, repeat = zero_check(s, count_z,repeat)
    return [repeat, count_z]





