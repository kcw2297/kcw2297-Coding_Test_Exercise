"""
항상 pythonic!!! 코드 방식을 고려하자
"""

def solution(ls):
    return min(len(ls)/2, len(set(ls)))
