"""https://programmers.co.kr/learn/courses/30/lessons/42748"""

def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]-1
        end = command[1]
        nth = command[2]-1
        s_array = array[start:end]
        answer.append(sorted(s_array)[nth])
    return answer
