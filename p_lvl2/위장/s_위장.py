




def solution(clothes):
    hash_map = {}
    # 옷을 종류별로 구분
    for cloth, type in clothes:
        hash_map[type] = hash_map.get(type,0) + 1

    # 모든 조합을 계산
    answer = 1
    for type in hash_map:
        answer *= (hash_map[type]) + 1

    # 아무 종류의 옷도 입지 않는 경우
    return answer - 1



"""
Counter를 활용해서 풀어낸 방안으로 훨씬 깔끔하다
"""

from collections import Counter
from functools import reduce
Counter({'headgear': 2, 'eyewear': 1})

def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
