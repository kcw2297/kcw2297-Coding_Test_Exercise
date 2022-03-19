"""https://programmers.co.kr/learn/courses/30/lessons/76502"""



"""
사용한 논리 및 오류:
회전 => 반복 => for, while
올바른 괄호 확인 => stack

마지막 }}}인 edge case에서 오류가 나온다
"""


def solution(s):

    result = 0
    left = ['[','{','(']
    right = [']','}',")"]


    for _ in range(len(s)):
        s = s[1:] + s[0]
        stack = []

        for ele in s:
            
            if ele in left:
                stack.append(ele)
            elif len(stack)>0 and ele in right:
                if stack[-1] in left and left.index(stack[-1]) == right.index(ele):
                    stack.pop()
            else:
                stack.append(ele)
            
                    

        if len(stack) == 0:
            result += 1
    
    return result
