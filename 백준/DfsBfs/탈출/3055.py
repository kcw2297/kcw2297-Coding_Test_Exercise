import sys
from collections import deque

r, c = map(int, sys.stdin.readline().split())

graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]

distance = [[0]*c for _ in range(r)]

queue = deque()



for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            queue.append((i,j))
            distance[i][j] = 1
        if graph[i][j] == 'D':
            queue.append((i,j))

for i in range(r):
    for j in range(c):
        if graph[i][j] == '*':
            queue.append((i,j))


dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(queue):
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr, nc = r + dx[i], c + dy[i]

            if 0 <= nr < r and 0 <= nc < c:
                if graph[nr][nc] == 'D' and graph[r][c] == 'S':
                    return distance[nr][nc]

                if graph[nr][nc] == '.' and graph[r][c] == 'S':
                    graph[nr][nc] = 'S'
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr,nc))

                if (graph[nr][nc] == '.' or graph[nr][nc] == 'S') and graph[r][c] == '*':
                    graph[nr][nc] = '*'
                    queue.append((nr,nc))

    return 'KAKTUS'


print(bfs(queue))