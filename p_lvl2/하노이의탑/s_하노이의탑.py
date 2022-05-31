

"""
사용한 논리:
재귀함수를 이용해 풀어나갔다
3개의 단계가 존재하는데, 
-start에서 진행되는 과정
-start에서 end
-bypass에서 end
위 3단계에서 개별적으로 재귀함수를 진행이 된다
"""

def solution(n):
    answer = hanoi(n,1,3,2)  
    return answer

def hanoi(n, start, end, bypass):
    if n == 1:
        return [[start, end]]
    else:
        path = []
        path += hanoi(n-1, start, bypass, end)
        path += [[start, end]]
        path += hanoi(n-1, bypass, end, start)
        
        return path