import sys
from collections import deque

cities, roads, dis, start = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(cities+1)]
for _ in range(roads):
    s,e = map(int, sys.stdin.readline().split())
    graph[s].append(e)

visited = [0] * (cities+1)

stack = []

def bfs(s,k):

    queue = deque([(s,k)])
    visited[s] = 1

    while queue:
        city, k = queue.popleft()
        
        if k == 0:
            stack.append(city)
            continue

        
        for i in graph[city]:
            if not visited[i]:
                visited[i] = 1
                queue.append((i,k-1))

bfs(start,dis)

if stack:
    stack.sort()
    for i in stack:
        print(i)
else:
    print(-1)












