"""https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3"""


"""
1. 처음 접근방법으로 신고자와 신고받은자 dict을 만들어서 신고받은자의 숫자가
k를 넘으면 신고자한자 dict에서 숫자로 바꾸려고 했지만, 바꾸는 과정에서
어려움이 있어서 중단하였다.
"""

"""
pythonic 하기 위해서 for loop를 dict comprehension을 사용하여 가독성을 높이자
dictionary에서 for in을 할 경우 key만 돌려보낸다
"""

def solution(id_list, report, k):


    report = {}
    take = {}

    for id in id_list:
        report[id] = []

    for id in id_list:
        take[id] = 0

    for id in report:
        a, b = id.split()
        report[a] += b
        take[b] += 1

    for check in take.keys():
        if take[check] >=2:
            report[]

    answer = []
    return answer
