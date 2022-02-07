"""https://programmers.co.kr/learn/courses/30/lessons/42839"""



"""
슬슬 helper function이 필요해진다
check 함수는 소수인지 판별한다
전체 문자열을 하나씩 나누어 permutations을 이용해 순열을 만든다
이후 각 요소들이 소수인지 확인하고 set()에 저장한다
이후 set()의 길이를 측정한다
"""



from itertools import permutations


def check(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True


def solution(numbers):
    temp = set()
    answer = 0
    numbers = [x for x in numbers]
    length = len(numbers)
    for i in range(1,length+1):

        num = list(permutations(numbers,i))
        for ele in num:
            ele = int(''.join(map(str,ele)))
            if ele <= 1:
                continue
            elif check(ele):
                temp.add(ele)
    answer = len(temp)

    return answer
