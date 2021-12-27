"""https://programmers.co.kr/learn/courses/30/lessons/42862"""

"""
코딩 팁
 if (a or b) in c => 틀린 접근

이것은 틀린 표현이다
a와b 중에 먼저 a가 true이면 a만 반환한다


if any(x in c for x in (a,b)):

any함수를 사용하여 논리식을 펼친다 (전체는 all() 함수)
"""

def check_reserve(num, reserve):
    if num in reserve:
        return num
    elif num-1 in reserve:
        return num-1
    elif num+1 in reserve:
        return num+1
    else:
        return 0

def solution(n, lost, reserve):
    for num in lost:
        spare = check_reserve(num, reserve)
        if spare:
            reserve.remove(spare)
        else:
            n -= 1
    return n
