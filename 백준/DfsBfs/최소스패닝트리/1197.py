import sys
input = sys.stdin.readline
 
V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
Elist = []
for _ in range(E):
    Elist.append(list(map(int, input().split())))
 
Elist.sort(key=lambda x: x[2])
 
"""
-visited에 각 인덱스에 크기 값을 저장한다
-간선을 가중치 별로 정렬한다
-처음 1번 부터 시작한다
-s와e의 현재 값을 가져오는데, 동일할 경우 패쓰하고
동일하지 않을 경우 더 작은 값으로 변경한다
"""

def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]

answer = 0
for s, e, w in Elist:
    sRoot = find(s)
    eRoot = find(e)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        answer += w
 
print(answer)


###############################################################################################################



import sys
import heapq
input = sys.stdin.readline
 
V, E = map(int, input().split())
visited = [False]*(V+1)
Elist = [[] for _ in range(V+1)]
heap = [[0, 1]]
for _ in range(E):
    s, e, w = map(int, input().split())
    Elist[s].append([w, e])
    Elist[e].append([w, s])
 
answer = 0
cnt = 0
while heap:
    if cnt == V:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        answer += w
        cnt += 1
        for i in Elist[s]:
            heapq.heappush(heap, i)
 
print(answer)


