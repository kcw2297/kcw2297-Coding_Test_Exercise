import sys
from collections import deque


def bfs(s, group):
    queue = deque([s])
    visited[s] = group
    while queue:
        i = queue.popleft()
        for j in graph[i]:
            if not visited[j]:
                queue.append(j)
                visited[j] = -1 * visited[i]
            elif visited[j] == visited[i]:
                return False
    return True

count = int(sys.stdin.readline())

for _ in range(count):
    nodes, edges = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(nodes+1)]
    visited = [0] * (nodes+1)

    for _ in range(edges):
        s, e = map(int, sys.stdin.readline().split())
        graph[s].append(e)
        graph[e].append(s)

    for i in range(1,nodes+1):
        if not visited[i]:
            result = bfs(i,1)
            if not result:
                break
    if result:
        print('Yes')
    else:
        print('NO')


#############################################################################

import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline


def dfs(start, group):
    global error

    # 만약 사이클이 true라면 재귀탈출
    if error:
        return

    visited[start] = group  # 해당 그룹으로 등록

    for i in graph[start]:
        if not visited[i]:
            dfs(i, -group)  # 다른 그룹으로 설정
        elif visited[start] == visited[i]:  # 인접한데 같은 그룹이라면
            error = True  # 에러값 True
            return  # 그후 재귀 리턴


T = int(input())

for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)  # 방문한 정점 체크
    error = False

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if not visited[i]:  # 만약 아직 방문하지 않았다면
            dfs(i, 1)  # dfs를 돈다.
            if error:  # 만약 에러가 참이라면
                break  # 탈출

    if error:
        print('NO')
    else:
        print('YES')



