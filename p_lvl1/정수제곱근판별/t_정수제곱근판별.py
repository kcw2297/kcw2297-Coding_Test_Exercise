"""https://programmers.co.kr/learn/courses/30/lessons/12934"""






import math

def solution(n):
    x = math.sqrt(n)
    if int(x)==float(x):
        answer = (x+1)**2
        return answer
    else:
        return -1
