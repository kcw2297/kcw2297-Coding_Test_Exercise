"""https://programmers.co.kr/learn/courses/30/lessons/42587"""




"""
pop()을 사용하여 조건에 부합되지 않는 값은 뒤로 보내였지만, 이후
index를 어떤식으로 해결할지 몰랐다
"""


def solution(priorities, location):

    while True:
        for i in range(len(priorities)):
            if priorities[i] == max(priorities):
                continue
            else:
                loop = priorities.pop(i)
                priorities.append(loop)
