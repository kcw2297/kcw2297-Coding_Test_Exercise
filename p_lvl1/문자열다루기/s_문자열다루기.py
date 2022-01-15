


"""
전체 값이 int가 되야하니 isdigit을 활용해서 푼 모습이다
"""

def solution(s):
    return s.isdigit() and len(s) in (4, 6)
