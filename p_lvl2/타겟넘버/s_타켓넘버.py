
"""
1 -> 2
       -> 3
       -> 1
        ~~~~~~~~~

1 -> 0
       -> 1
       -> -1
        ~~~~~~~~~

인덱스를 이용하여 전체 리스트의 길이를 초과하지 않는 동안 queue에 append를 하여서
전체 리스트 안에 있는 값을 더하거나 뺄 수가 있다
"""

from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


"""
재귀함수를 이용하여 푼 문제이다
*이 문제가 재귀함수로 사용된 이유는 전체 리스트 요소를 더하거나 뺄때 target한 값이 나와야하기
때문에 재귀의 끝 부분만 고려하면 된다

리스트 안에 마지막 값까지 돌린 후,
재귀 과정에서 not numbers(numbers가 false,즉 전체 리스트를 확인했다)와 target==0인 경우에만
1을 반환하여서 +와-인 경우의 수를 모두 고려한 값이 최종적으로 반환된다
"""

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
