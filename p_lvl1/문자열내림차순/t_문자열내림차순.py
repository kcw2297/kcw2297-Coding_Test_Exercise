"""https://programmers.co.kr/learn/courses/30/lessons/12917"""



"""
sorted(reverse=True)를 하면 대문자가 뒤로가기 때문에 굳이 2개로
분리 할 필요가 없었다
"""


def solution(s):
    answer = ''
    b_list = []
    s_list = []
    for ele in s:
        if ele.isupper():
            b_list.append(ele)
        else:
            s_list.append(ele)

    b_list = sorted(b_list,reverse=True)
    s_list = sorted(s_list,reverse=True)
    for ele in s_list:
        answer+=ele

    for ele in b_list:
        answer+=ele

    return answer
