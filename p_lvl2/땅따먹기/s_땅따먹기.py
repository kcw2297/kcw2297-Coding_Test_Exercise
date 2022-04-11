


"""
사용한 논리:
반복문의 값을 인덱스로 활용하여 해당 값을 제외한 최대값을 찾은 모습이다
"""

def solution(land): 
    for i in range(1, len(land)): 
        for j in range(len(land[0])): 
            #앞의 행에서 해당 열 제외 최대값 더하기 갱신 
            land[i][j] += max(land[i-1][0:j] + land[i-1][j+1:]) 
    return max(land[-1])
