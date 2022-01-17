"""https://programmers.co.kr/learn/courses/30/lessons/12925"""





def solution(s):
    if s[0] == "-":
        num=int(s[1:])
        answer = -num
    elif s[0] == "+":
        answer=int(s[1:])
    else:
        answer=int(s)

    return answer
