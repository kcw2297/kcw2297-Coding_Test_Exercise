"""https://programmers.co.kr/learn/courses/30/lessons/12982/solution_groups?language=python3"""


"""
결과를 저장하는 변수를 만들고 조건에 부합하는 경우 1씩 더해갔다
하지만 이 방법에서 space complexity가 O(n)이 되기에 약간 비효율적이다
"""

def solution(d, budget):

    d = sorted(d)
    answer = 0

    for ele in d:
        if ele<=budget:
            budget-=ele
            answer+=1
        else:
            break

    return answer
