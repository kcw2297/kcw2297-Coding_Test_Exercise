





"""
map()을 이용해서 int화하였다.
전반적으로 동일한 개념을 사용하였지만 훨씬 pythonic하다
"""



def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
