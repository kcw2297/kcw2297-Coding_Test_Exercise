
"""
sys를 활용하자
"""

import sys
input = sys.stdin.readline

N, M = map(int,input().split()) # 나무 수, 필요한 나무 길이
trees = list(map(int, input().split()))

start, end = 0, max(trees) # 시작 점, 끝점

# 이분 탐색
while start <= end:
    mid = (start+end)//2
    tree = 0 # 잘린 나무 합
    for i in trees:
        if i > mid: # mid보다 큰 나무 높이는 잘림
            tree += i - mid

    if tree >= M: # 원하는 나무 높이보다 더 많이 잘렸으면
        start = mid + 1
    else: # 원하는 나무 높이보다 덜 잘렸으면
        end = mid - 1
print(end)



"""
논라는 맞았지만 input을 사용해 시간초과가 되었다
"""

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    
    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    
    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
