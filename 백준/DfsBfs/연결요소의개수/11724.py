import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:  # 만약 그래프가 비어있다면
            count += 1  # 개수 1개 추가
            visited[i] = True  # 방문 처리
        else:  # 만약 그래프가 비어있지 않다면(어느 점과 연결된 점이 있다면)
            bfs(i)  # 해당 i를 시작노드로 bfs를 돈다.
            count += 1  # 연결요소 를 +1개 해준다.

print(count)


#######################################################################################################


import sys
sys.setrecursionlimit(10 ** 6)

nodes, edges = map(int, sys.stdin.readline().split())


graph = [[] for _ in range(nodes+1)]
for _ in range(edges):
    s,e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (nodes+1)

cnt = 0
def dfs(s):

    visited[s] = 1
    
    for i in graph[s]:
        if not visited[i]:
            dfs(i)
    return 1

for i in range(1,nodes+1):
    if not visited[i]:
        cnt += dfs(i)
          

print(cnt)




