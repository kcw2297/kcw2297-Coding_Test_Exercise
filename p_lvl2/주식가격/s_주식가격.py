


"""
queue를 활용한 방식으로 먼저 들어온(왼쪽) element부터 pop을 하여서
저장한다
"""
from collections import deque

def solution(prices):
    queue = deque(prices)
    answer = []

    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    return answer


"""
stack을 활용한 방안으로 먼저 max값을 둔 후에 조건에 부합하는 값을
떨어트리는 식이다
"""
def solution(prices):
    length = len(prices)
    answer = [ i for i in range (length - 1, -1, -1)]

    stack = [0]
    for i in range (1, length, 1):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer
