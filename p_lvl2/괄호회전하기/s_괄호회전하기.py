

"""
for loop 인덱스와 slicing으로 괄호 회전
dictionary를 사용하여 괄호의 조합을 맞춘다
해당하는 조건시에 pop을 하고 마지막에 값이 비어있으면 1을 추가한다
"""



def solution(s):
    answer = 0
    dic = {'{':'}', '[':']', '(':')'}
           
    for i in range(len(s)):
        right = list(s[i:] + s[:i])
        left = []
        while right:
            temp = right.pop(0)
            if not left:
                left.append(temp)
            else:
                if left[-1] in ['}', ')', ']']:
                    break
                    
                if dic[left[-1]] == temp:
                    left.pop()
                else:
                    left.append(temp)
        
        if not left:
            answer += 1
            
    return answer



# 나와 유사한 접근 방식으로 푼 예시이다

def solution(s):
    answer = 0    
    starts = ['(', '[', '{']
    ends = [')', ']', '}']

    for i in range(len(s)):
        s = s[1:] + s[0]

        stack = []
        for x in s:            
            if x in starts:
                stack.append(x)

            elif x in ends and len(stack) > 0:

                for i in range(3):
                    if stack[-1] == starts[i] and x == ends[i]:
                        stack.pop()     
                        break

            else:
                stack.append(x)            

        if len(stack) == 0:
            answer += 1            

    return answer