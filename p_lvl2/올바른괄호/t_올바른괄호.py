"""https://programmers.co.kr/learn/courses/30/lessons/12909"""



"""
사용한 논리:
stack을 이용해 '('와')'를 저장한다
반복문을 이용해서 ()가 되는지 확인하고 되면 pop한다
"""



def solution(s):
    stack = []

    for i in range(len(s)):
        ele = s[i]

        stack.append(ele)
        if len(stack)>=2:
            if ele == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
    
            
    if len(stack) == 0:
        return True
    else:
        return False


