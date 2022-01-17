"""https://programmers.co.kr/learn/courses/30/lessons/12922"""



"""
n번 반복을 하기에 for loop으로 반복되는 숫자만큼 문자를 더했다
"""


def solution(n):
    answer = ''
    for i in range(n):
        if i%2==0:
            answer+= "수"
        else:
            answer+="박"
    return answer
