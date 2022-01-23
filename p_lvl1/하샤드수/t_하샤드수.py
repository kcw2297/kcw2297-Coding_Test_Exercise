"""https://programmers.co.kr/learn/courses/30/lessons/12947"""






def solution(x):


    div = sum(map(int,str(x)))

    if x%div==0:
        return True
    else:
        return False
