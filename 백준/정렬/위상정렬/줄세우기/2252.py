import queue
from re import L
import sys
from collections import deque


students, cmp = map(int, sys.stdin.readline().split())
line_list = [ list(map(int, sys.stdin.readline().split())) for _ in range(cmp)]
graph = [[] for _ in range(32001)]
inDegree = [0 for _ in range(32001)]

queue = deque()


for line in line_list:
    s, e = line
    graph[s].append(e)
    inDegree[e] += 1


for student in range(1,students+1):
    if inDegree[student] == 0:
        queue.append(student)


while queue:
    student = queue.popleft()

    for i in graph[student]:
        inDegree[i] -= 1

        if inDegree[i] == 0:
            queue.append(i)

    print(student, end=' ')














