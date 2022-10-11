

"""
사용한 논리:
BFS 알고리즘 활용 =>
재귀적으로 동작x, 노드 방문여부 확인, queue사용 및 FIFO

-1로 된 동일한 크기의 테이블을 생성
전체 가로 세로의 길이를 변수에 저장
queue에 [0,0]을 넣은 후, queue가 사라질 때까지 반복
현재 위치에서 4가지 방향으로 벽을 확인하고, 조건 충족시 임시 테이블에 1을 더한다
*만약 최종 도착지가 벽으로 막혀있으면 처음 설정한 -1이 반환된다
*popleft()에서 리스트안에 원소가 2개이며 변수가 2개면 분리가 된다
"""


from collections import deque

def solution(maps):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    r = len(maps)
    c = len(maps[0])

    graph = [[-1 for _ in range(c)] for _ in range(r)]

    queue = deque()
    queue.append([0, 0])

    graph[0][0] = 1

    while queue:
        y, x = queue.popleft()

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
                if graph[ny][nx] == -1:
                    graph[ny][nx] = graph[y][x] + 1
                    queue.append([ny, nx])

    answer = graph[-1][-1]
    return answer

