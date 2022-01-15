


"""
list[-1:]은 가장 뒤에 있는 값을 리스트로 반환하기에 빈 리스트도 가능하다
이를 이용해서 1개의 리스트로 가장 최근 값과 비교 할 수 있다
"""



def solution(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
