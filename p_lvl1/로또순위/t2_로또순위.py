
"""
    1. 동일한 값을 count에 저장하여서 매칭되는 수를 저장
    2. lottos 안의 0을 세어서 최대값 구하기
"""



def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    
    count = 0
    for ele in lottos:
        if ele in win_nums:
            count += 1
    most = count + lottos.count(0)

    return [rank[most],rank[count]]