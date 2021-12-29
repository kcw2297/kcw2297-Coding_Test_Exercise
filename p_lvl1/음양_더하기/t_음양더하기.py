"""https://programmers.co.kr/learn/courses/30/lessons/76501"""

"""
zip()을 이용하여 2개의 리스트를 묶은 후 신호에 따른 결과값을 도출
"""

def solution(absolutes, signs):
    answer = 0

    for pair in zip(signs,absolutes):
        if pair[0] == True:
            answer += pair[1]
        else:
            answer -= pair[1]
    return answer
