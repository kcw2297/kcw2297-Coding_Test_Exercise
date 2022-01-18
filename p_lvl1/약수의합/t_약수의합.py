"""https://programmers.co.kr/learn/courses/30/lessons/12928"""



def solution(n):
    check = []

    for i in range(1,n+1):
        if n%i == 0:
            check.append(i)
    answer = sum(check)
    return answer
