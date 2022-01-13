"""https://programmers.co.kr/learn/courses/30/lessons/12903"""



"""
정답만 맞았다고 넘어가지 말고 어떤식으로 코드 가독성을 높일지도
고민하자. 정답을 보기전에 최대한 코드리뷰를 하는 습관을 들이자
"""



def solution(s):
    if len(s)==1:
        return s

    idx = len(s)%2
    idx1 = len(s)//2
    if idx == 1:
        return s[idx1]
    else:
        return s[idx1-1] + s[idx1]
