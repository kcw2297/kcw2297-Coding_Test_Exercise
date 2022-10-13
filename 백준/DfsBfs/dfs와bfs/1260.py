import sys
from collections import deque

nodes, edges, start = map(int, sys.stdin.readline().split())

graph = [ [0]*(nodes+1) for _ in range(nodes+1)]

for i in range(edges):
    s, e = map(int, sys.stdin.readline().split())
    graph[s][e] = 1
    graph[e][s] = 1


visited_bfs = [ 0 for _ in range(nodes+1)]
visited_dfs = [ 0 for _ in range(nodes+1)]



def dfs(graph, start):
    visited_dfs[start] = 1
    print(start, end=' ')
    for i in range(1,nodes+1):
        if graph[i][start] == 1 and visited_dfs[i] == 0:
            dfs(graph, i) 





def bfs(graph, start):
    queue = deque()
    queue.append(start)
    visited_bfs[start]

    while queue:
        start = queue.popleft()
        if not visited_bfs[start]:
            print(start, end=' ')
            visited_bfs[start] = 1
            for edge in range(1,nodes+1):
                if graph[start][edge] == 1:
                    queue.append(edge)


dfs(graph, start)
print()
bfs(graph, start)


