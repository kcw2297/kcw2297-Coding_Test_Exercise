


"""
에라토테네의 체를 활용한 소수 구하는 공식을 이용한 것이다
주어진 숫자만큼의 elements들을 리스트 안에 true로 만든다
이후 2,3~~~의 배수로 각각 False로 만든 후 마지막에 남은
True의 개수를 반환한다
"""

"""
아래에는 더 간단한 방법으로 번위를 set안에 넣고 특정 배수로 나누어
지는 숫자는 set에서 삭제하는 식으로 하였다
"""

import math

def solution(number):
    numbers = [True] * (number + 1)
    answer = 0

    for num in range(2,int(math.sqrt(number))+1):
        if numbers[num] == False:
            continue;

        for i in range(num+num,number+1,num):
            numbers[i] = False

    for i in range(2,number+1):
        if numbers[i] == True:
            answer+=1

    return answer


def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
