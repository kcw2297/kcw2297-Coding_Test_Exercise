

import sys
from collections import deque

comp_count = int(sys.stdin.readline())
num = int(sys.stdin.readline())

graph = [ [] for i in range(comp_count+1)]

for _ in range(num):
    s,e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0 for _ in range(comp_count+1)]

count = -1


def bfs(s):
    global count
    queue = deque([s])
    
    while queue:
        start = queue.popleft()
        if not visited[start]:
            visited[start] = 1
            count += 1
            for i in graph[start]:
                queue.append(i)

bfs(1)
print(count)


############################################


import sys

comp_count = int(sys.stdin.readline())
num = int(sys.stdin.readline())

graph = [ [0] * (comp_count+1) for _ in range(comp_count+1)]

for _ in range(num):
    s,e = map(int, sys.stdin.readline().split())
    graph[s][e] = 1
    graph[e][s] = 1

visited = [0 for _ in range(comp_count+1)]
count = 0

def dfs(s):
    global count
    visited[s] = 1
    for i in range(1,comp_count+1):
        if graph[i][s] and not visited[i]:
            count += 1
            dfs(i)

dfs(1)
print(count)


