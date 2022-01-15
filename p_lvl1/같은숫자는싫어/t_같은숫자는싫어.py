"""https://programmers.co.kr/learn/courses/30/lessons/12906"""

"""
지속적으로 검사하는 리스트와 정답 리스트 2개를 만들어서 계산하였다
하지만 공간 효율성면에서 2배로 차지하기에 최적의 알고리즘은 아니었다
"""

def solution(arr):

    answer = []
    memory = []

    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[i])
            memory.append(arr[i])
        elif arr[i]==memory[i-1]:
            memory.append(arr[i])
        else:
            memory.append(arr[i])
            answer.append(arr[i])

    return answer
