"""https://programmers.co.kr/learn/courses/30/lessons/12918?language=python3"""


"""
try except를 활용해서 int()로 전환이 안되면 오류가 나오게 하여서 계산했다
"""



def solution(s):
    if len(s) not in [4,6]:
        return False

    try:
        for ele in s:
            int(ele)
        return True
    except:
        return False
