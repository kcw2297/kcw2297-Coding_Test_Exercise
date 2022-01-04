"""https://programmers.co.kr/learn/courses/30/lessons/12901"""

def solution(a, b):
    date = date_check(a)
    start_date = {1:5,2:1,3:2,4:5,5:0,6:3,7:5,8:1,9:4,10:6,11:2,12:4}
    start = start_date[a]
    b = b%7
    week = (start+b)%7-1
    dates = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    answer = dates[week]
    return answer


def date_check(a):
    t = [2]
    z = [4,6,9,11]
    o = [1,3,5,7,8,10,12]

    date = 0

    if a in t:
        date = 29
    elif a in z:
        date = 30
    elif a in o:
        date = 31

    return date
