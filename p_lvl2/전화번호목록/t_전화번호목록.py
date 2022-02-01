"""https://programmers.co.kr/learn/courses/30/lessons/42577"""



"""
문제를 잘못이해하고 처음 요소가 다른 번호의 접두사인 경우로 이해했다
"""

def solution(phone_book):
    pre = phone_book[0]
    leng = len(pre)
    for i in phone_book[1:]:
        text = i[0:leng]
        if str(text) == pre:
            return False
    return True
