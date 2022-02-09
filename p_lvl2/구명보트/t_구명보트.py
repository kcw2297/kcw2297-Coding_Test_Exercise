"""https://programmers.co.kr/learn/courses/30/lessons/42885"""
#https://stackoverflow.com/questions/19819907/python-using-del-in-for-loops



"""
del을 for loop 중간에 두면 생기는 오류가 index가 꼬이게 된다
추가로 문제에서 boat에는 2명이 max로 명시되어 있는 것을
고려하지 않았다
"""


def solution(people, limit):

    boat = 0
    answer = 0
    people.sort()

    while people:
        for index, person in enumerate(people):
            if boat + person <= limit:
                boat += person
                del people[index]
        boat = 0
        answer +=1
    return answer
