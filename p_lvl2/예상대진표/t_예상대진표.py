"""https://programmers.co.kr/learn/courses/30/lessons/12985"""




"""
    참가자의 번호는 순서대로 나열
    최종 1명이 남을 때까지 반복
    2명의 선수가 겨루는때까지 횟수
    
    주어진 숫자 변환 => n//2+1
    총 반복 횟수 => n//2 => 남는수 1이 될때 까지
"""

def check(num):
    if num%2 == 0:
        return num//2
    else:
        return num//2 +1

def solution(n,a,b):
    count = 0
    if a == b:
        return count

    while a!=b:
        a = check(a)
        b = check(b)
        count += 1
    return count


