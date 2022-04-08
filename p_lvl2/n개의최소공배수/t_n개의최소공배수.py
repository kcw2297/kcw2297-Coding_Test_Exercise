"""https://programmers.co.kr/learn/courses/30/lessons/12953"""



"""
사용한 논리 및 오류:
1. 최대공약수를 구한다
2. 각 수에 최대공약수를 나눈 후 마지막에 최대공갹수를 곱해서 최소공배수를 구한다

*최소공배수를 구하는데 있어서, 서로소가 될 때까지 나누어야했는데 이를 간과했다
"""




# 약수를 찾는다
def find_m(num):
    #추후에 공집합을 구하기 위해 set를 사용
    container = set()
    for i in range(1, num+1):
        if num % i == 0:
            container.add(i)
    return list(container)


def solution(arr):
    if len(arr) == 1 and arr[0] == 1:
        return 1
    if 1 in arr:
        arr.remove(1)
    
    
    base = []
    total = []
    
    for num in arr:
        total += find_m(num)
    print(total)
    for i in total:
        if total.count(i) == len(arr) and i not in base:
            base.append(i)

    base.sort()
    print(base)

    # 공집합 중에 가장 큰 수가 최대공약수이다
    base = list(base)[-1]
    print(base)
    
    answer = 1
    
    # 최대공약수에서 몫을 구하고 곱한다
    # 서로소가 나올 때까지 구하는 것인데, 이를 구현 못했다
    for num in arr:
        mod = num // base
        answer *= mod
    
    answer *= base
    print(answer)
    return answer