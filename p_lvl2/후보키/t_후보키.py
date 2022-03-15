"""https://programmers.co.kr/learn/courses/30/lessons/42890"""

"""
사용한 논리:
combinations을 이용해 전체 원소들의 조합을 짠 후에 유일성을 구한다
이후 최소성을 구하는 함수로 중복되는 것을 제거 한 후 최종 길이를
반환한다


유일성 함수
1 ~ 전체 길이만큼의 조합을 반복
전체 값에 값 확인 후 없으면 저장, 있으면 break

최소성 함수

"""

from itertools import combinations

def combi(relation, col):
    result = []
    for i in range(1,col+1):
        result.extend(combinations(range(col),i))

    return result

def unique(relation, uni_list, row):
    result = []
    for i in uni_list:
        tmp = [ tuple([item[key] for key in i]) for item in relation]
    
    if len(set(tmp)) == row:
        put = True

        for x in result:
            if set(x).issubset(set(i)):
                put = False
                break
        if put: result.append(i)

    return result
    


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    uni_list = combi(relation, col)
    result = unique(relation, uni_list, row)
    return len(result)

