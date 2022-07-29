

"""
	1. 3개의 모듈로 나눈다
    2. SDT를 치환할 함수를 만든다
    3. 위 함수를 이용해 계산한다
"""


def SplitDart(dartResult):
    result = {}
    key = 0
    start = 0

    for i in range(len(dartResult)):
        if dartResult[i] in ["*", "#"]:
            result[key] += dartResult[i]
            start += 1

        if dartResult[i] in ["S", "D", "T"]:
            key += 1
            result[key] = dartResult[start:i+1]
            start += (i-start+1)
    return result


def Bonus(num, str):
    if str == "S":
        return num
    if str == "D":
        return num * num
    if str == "T":
        return num * num * num


def Calculator(container):
    one, two, three = 0, 0, 0
    for key in [1, 2, 3]:
        if key == 1 and "*" in container[key]:
            num = int(container[key][:-2])
            one = Bonus(num, container[key][-2]) * 2
            continue
        if key == 1 and "#" in container[key]:
            num = int(container[key][:-2])
            one = Bonus(num, container[key][-2]) * -1
            continue
        if key == 1:
            num = int(container[key][:-1])
            one = Bonus(num, container[key][-1])
            continue

        if key == 2 and "*" in container[key]:
            num = int(container[key][:-2])
            two = Bonus(num, container[key][-2]) * 2
            one *= 2
            continue
        if key == 2 and "#" in container[key]:
            num = int(container[key][:-2])
            two = Bonus(num, container[key][-2]) * -1
            continue
        if key == 2:
            num = int(container[key][:-1])
            two = Bonus(num, container[key][-1])
            continue

        if key == 3 and "*" in container[key]:
            num = int(container[key][:-2])
            three = Bonus(num, container[key][-2]) * 2
            two *= 2
            continue
        if key == 3 and "#" in container[key]:
            num = int(container[key][:-2])
            three = Bonus(num, container[key][-2]) * -1
            continue
        if key == 3:
            num = int(container[key][:-1])
            three = Bonus(num, container[key][-1])
            continue
    
    return one + two + three


def solution(dartResult):
    container = SplitDart(dartResult)
    return Calculator(container)

