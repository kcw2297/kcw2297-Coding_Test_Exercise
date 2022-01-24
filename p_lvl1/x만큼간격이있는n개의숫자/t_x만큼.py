"""https://programmers.co.kr/learn/courses/30/lessons/12954"""



"""
pythonic하게 한줄로 작성해보록하자
"""



def solution(x, n):
    answer=[]

    for i in range(1,n+1):
        answer.append(x*i)
    return answer
