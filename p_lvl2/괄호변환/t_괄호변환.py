"""https://programmers.co.kr/learn/courses/30/lessons/60058"""



"""
1 :
균형잡힌 문자열을 나누기 위해 이것에 해당하는 조건을
for in range()를 활용해서 인덱스로 문자열의 위치를 파악한다
2 :
나눈 값을 이용해서 u와 v를 확인해야한다
stack을 활용해서 "("와 ")"가 올바른 순서로 들어있는지 확인한다
2 :
이후 올바른지 여부에 따라 다음 재귀를 하던가 문자열을 뒤집던가 한다
"""



def solution(p):

    return bracket(p)


def bracket(str):
    u, v = check(str)

    변환과정을 실행

    이를 특정 값에 저장

def check(str):
    괄호 매칭 여부를 확인한다
    괄호에 따라서 u와 v로 나눈다
    return u, v
