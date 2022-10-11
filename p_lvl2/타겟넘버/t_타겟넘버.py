"""https://programmers.co.kr/learn/courses/30/lessons/43165"""

"""
list안에 요소를 +와-인 경우를 고려해서 더했을 경우 target이 나오는 경우를 찾는 문제이다

deque를 사용한 이유는 리스트 안에 부여하는 조건이 같기 때문이다
tree형식으로 하나씩 특정 node에 값을 더하거나 빼기에 알맞은 방법이다
"""

"""
시간 복잡도 : O(V), 정확히는 마지막 노드 E를 더하는 것이지만, 전체에 비해 작기에 제외한다
        while문으로 전체 깊이를 돌리기에 n이나닌 깊이를 나타내는 V를 사용한다
공간 복잡도 : O(n), worst case, 전체 node가 더하거나 빼는 상황이 
"""

"""
프로그래머스 레벨 2부터는 단순 조건식보다는 자료구조 알고리즘 공부를 요구하는
문제들이 출제되는 것을 확인하였다
"""
    
def solution(num, target):
    def dfs(num, cur, idx, target):
        count = 0

        if idx == len(num) and target == cur:
            count += 1
            return 1
        
        if idx == len(num):
            return 0

        count += dfs(num, cur+num[idx], idx+1, target)
        count += dfs(num, cur-num[idx], idx+1, target)
        
        return count

    return dfs(num, 0, 0, target)
    
    











