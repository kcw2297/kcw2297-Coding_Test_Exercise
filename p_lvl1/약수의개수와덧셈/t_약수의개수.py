"""https://programmers.co.kr/learn/courses/30/lessons/77884?language=python3"""



"""
약수 문제가 나올 경우 루트를 활용해서 문제의 핵심을 풀어가자
"""

def solution(left, right):

    if right==0:
        return None
    right += 1

    answer = 0

    rep = []
    while left!=right:
        if left==0:
            continue
        rep.append(left)
        left+=1


    for num in rep:
        str = set()
        for x in range(num+1):
            if x ==0:
                continue
            if num%x==0:
                str.add(x)
        if len(str)%2==0:
            answer+=num
        else:
            answer-=num
    return answer
