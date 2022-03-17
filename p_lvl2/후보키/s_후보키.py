

"""
사용한 논리:
1~리스트 길이만큼의 범위를 조합으로 구한다
*extend를 사용하면 object대신에 데이터 타입으로 전환하여 저장이 가능하다

조합 인덱스를 이용해서 relation 리스트 반복 및 개별 리스트 반복으로
전체 조합 값을 반환한다

set()를 활용하여 해당값의 유일성을 확인
issubset()을 사용하여서 해당값이 서브셋인지 확인하고 맞으면 최소성 법칙으로
제외시킨다. 마지막으로 남은 값을 저장 후 전체길이를 반환한다
"""

from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    #가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
    
    
    #유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:    # 유일성
            put = True
            
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break
                    
            if put: unique.append(i)
   
    return len(unique)
