"""
Greedy 알고리즘 문제
특정 조건에 의해서 현재 상황에서 가장 알맞은 조건으로 진행한다

1. set를 사용하여 - 연산자를 이용해 차집합을 구한다
*list는 연산자 지원을 하지 않는

2. 왼쪽을 기준으로 여분의 옷을 빌려주어야만 가장 효율적인 배분이 된다
"""

"""
배운점 :
1. 전처리 과정을 통해 전체 수행을 줄일자
2. set를 이용해서 차집합을 한다
3. 무작정 반복문으로 접근하려는 습관을 버리고 문제의 상황에 맞게
   논리적으로 풀어가자
"""

"""
나의 코드와 다른점 :
나는 전체 reserve에 있는 값을 전부 비교 대입하려는 접근인 반면에,
해당 풀이는 Greedy 알고리즘의 특성을 활용해서 정확히 문제가 요구하는
답안에 접근하였다.
"""


def solution(n,lost,reserve):
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)
