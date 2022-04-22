


"""
사용한 논리:
처음 분리하는 조건을 숫자인지 확인하는 isdigit()을 사용하였다.
이후 분리된 값을 저장한 후 정렬한후 다시 문자열으로 반환하였다
"""


def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''

        number_check = False
        for i in range(len(f)): # 문자열 자르기
            if f[i].isdigit():  # 처음 나오는 숫자부터는 NUMBER로
                number += f[i]
                number_check = True
            elif not number_check:  # NUMBER가 나오기 전까지는 HEAD
                head += f[i]
            else:               # NUMBER가 이미 나왔고, 숫자가 아닌 문자가 나오면 TAIL
                tail = f[i:]
                break
        answer.append((head, number, tail))  # HEAD, NUMBER, TAIL 하나의 튜플로 저장

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))  # HEAD 우선, NUMBER 차선으로 정렬

    return [''.join(t) for t in answer]   # 원래 형태로 문자열 만들어서 반환


"""
사용한 논리:
정규식을 활용한 풀이로 한것이다.
이후 
"""


import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b




"""
사용한 논리:
enumerate을 활용한 풀이 과정 및 sort의 속정을 이용해
새로운 helper function을 만들었다
"""

def head_compare(data):    
    route = 0
    answer = ['', '']
    for i, v in enumerate(data):
        if (route == 0):
            if (v.isnumeric() == True):
                answer[0] = data[:i].lower()
                route = 1
                answer[1] += v
        elif (route == 1):
            if (v.isnumeric() == True):
                answer[1] += v
            else:
                break
    answer[1] = int(answer[1])
    return answer


def solution(files):
    answer = []

    files.sort(key = lambda x:head_compare(x))
    return files