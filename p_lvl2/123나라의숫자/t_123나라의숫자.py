"""https://programmers.co.kr/learn/courses/30/lessons/12899"""



"""
1,2,4를 각 자리수마다 넣어주면서 자릿수를 키워야하는 문제였다
총 3개의 값 중 1개를 넣어야하기에 3을 나누어 idx로 활용해야한다
"""


def solution(n):
    rule = [1,2,4]
    각 자리수가 3으로 나누어진다
    각 10의 자리수마다 3으로 나누어 index로 값을 넣는다
