



"""
스택을 사용하여 처음 저장한 문자가 다음 문자와 같을시 pop한다
"""


def solution(s):
    stack = []
    for i in s:
        if len(stack) == 0: stack.append(i)
        elif stack[-1] == i: stack.pop()
        else: stack.append(i)
    if len(stack) == 0: return 1
    else: return 0
