import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
inDegree = [ 0 for i in range(32001)]
graph = [[] for i in range(32001)]
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    arr.append([a, b])

for a, b in arr:
    inDegree[b] += 1
    graph[a].append(b)

for i in range(1, n + 1):
    if inDegree[i] == 0:
        queue.append(i)

while queue:
    student = queue.popleft()
    #indegree가 0인 정점을 제거하고, 해당 정점이 참조하고있던 점들의 indegree를 감소시킨다.
    for j in graph[student]:
        inDegree[j] -= 1
        if inDegree[j] == 0:
            queue.append(j)
    print(student, end = ' ')









    