"""https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3"""



def solution(s):

    p_check = 0
    y_check = 0

    s = s.lower()
    if "p" not in s and "y" not in s:
        return True

    for ele in s:
        if ele == "y":
            y_check+=1
        elif ele == "p":
            p_check+=1

    if p_check==y_check:
        return True
    else:
        return False
