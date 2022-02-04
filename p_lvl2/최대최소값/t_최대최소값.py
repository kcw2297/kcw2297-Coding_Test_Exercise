"""https://programmers.co.kr/learn/courses/30/lessons/12939"""




"""
list comprehension을 사용하거나 map()을 사용하여 int를 바꾼후 list에
저장한 모습이다
"""



def solution(s):
    temp = s.split()
    temp2 = [int(i) for i in temp]
    temp2.sort()
    min = str(temp2[0])
    max = str(temp2[-1])
    answer = f'{min} {max}'
    return answer
