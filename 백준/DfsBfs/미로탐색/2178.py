from collections import deque


N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

# 너비 우선 탐색
def bfs(x, y):
  # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
  dx = [-1, 1, 0, 0] 
  dy = [0, 0, -1, 1]

  # deque 생성
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()
    
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 위치가 벗어나면 안되기 때문에 조건 추가
      # if nx < 0 or nx >= N or ny < 0 or ny >= M:
      #   continue
      
      # # 벽이므로 진행 불가
      # if graph[nx][ny] == 0:
      #   continue
      
      # 벽이 아니므로 이동
      if 0<= nx < N and 0<= ny < M:
        if graph[nx][ny] == 1:
          graph[nx][ny] = graph[x][y] + 1
          queue.append((nx, ny))
  
  # 마지막 값에서 카운트 값을 뽑는다.
  return graph[N-1][M-1]

print(bfs(0, 0))


# import sys
# from collections import deque

# e_r, e_c = map(int, sys.stdin.readline().split())

# map = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(e_r)]

"""
#시간 초과 풀이
bfs 문제풀이 => queue사용예정
고정 => map
유동 => 이동 순서
중간 종료조건으로 0을 주거나 벽을 넘어갈시
0,0에서 시작

dx와 dy를 준비하여서 이동 수단을 정한다
종료조건으로 끝에 다다르면 전역변수 min_v와 비교후 대입
이동 거리는 인자준 후 방문한 부분에서 수정한다
"""

# min_v = 100000000000000000000

# def bfs(new_r, new_c, cur):
#     global min_v
#     queue = deque([(new_r,new_c,cur)])
    
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]

#     while queue:
#         r,c,new_cur = queue.popleft()

#         if r == (e_r-1) and c == (e_c-1):
#             min_v = min(min_v, new_cur)
#             return

#         for i in range(4):
#             if e_r <= r+dr[i] or r+dr[i] < 0 or e_c <= c+dc[i] or c+dc[i] < 0:
#                 continue

#             if map[r+dr[i]][c+dc[i]] == 0:
#                 continue

#             if map[r+dr[i]][c+dc[i]] == 1:
#                 queue.append([r+dr[i], c+dc[i],new_cur+1]) 


# bfs(0,0,1)
# print(min_v)