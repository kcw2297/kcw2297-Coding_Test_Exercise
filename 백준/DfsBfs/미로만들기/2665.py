import queue
import sys 
from collections import deque

N = int(sys.stdin.readline())
map = [ list(map(int, sys.stdin.readline().rstrip())) for _ in range(N) ]


dr = [1,-1,0,0]
dc = [0,0,1,-1]

def bfs():

    queue = deque()
    queue.append([0,0])
    visited = [[-1] * N for _ in range(N)]
    visited[0][0] = 0

    while queue:
        r, c = queue.popleft()

        if r == (N-1) and c == (N-1):
            return visited[r][c]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if  0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                if map[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr,nc))
                else:
                    visited[nr][nc] = visited[r][c]
                    queue.appendleft((nr,nc))

print(bfs())