import sys
from collections import deque

N = int(sys.stdin.readline())
lines = int(sys.stdin.readline())

num_list = [[0]*(N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
degree = [0]*(N+1)
q = deque()

for _ in range(lines):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[y].append((x,z))
    degree[x] += 1

for i in range(1,N+1):
    if degree[i] == 0:
        q.append(i)

while q:
    s = q.popleft()
    for e, z in graph[s]:
        if num_list[s].count(0) == N+1:
            num_list[e][s] += z
        else:
            for i in range(1, N+1):
                num_list[e][i] += num_list[s][i] * z
        
        degree[e] -= 1
        if degree[e] == 0:
            q.append(e)

for x in enumerate(num_list[N]):
    if x[1] > 0:
        print(*x)

    


