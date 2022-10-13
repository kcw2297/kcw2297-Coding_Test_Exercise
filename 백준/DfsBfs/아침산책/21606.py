import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

numVertices = int(input())
col = list(map(int, list("0"+input().strip())))

graph = [[] for _ in range(numVertices + 1)]

for _ in range(1, numVertices):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
    
count = 0
visited = set()

def dfs(exterior: int) -> int:
    cnt = 0
    for neighbor in graph[exterior]:
        if col[neighbor] == 1:
            cnt += 1
        else:
            if neighbor not in visited:
                visited.add(neighbor)
                cnt += dfs(neighbor)
    return cnt

for i in range(1, numVertices + 1):
    # 각 실내별 인접한 실내 구하기
    if col[i] == 1:
        for j in graph[i]:
            if col[j] == 1:
                count += 1
    # 인접한 실외를 한 덩어리로 보고 그 덩어리에 인접한 실내의 수를 구한 뒤 
    # 각 덩어리별로 n*(n-1)의 경우의 수를 계산
    else:
        if i not in visited:
            visited.add(i)
            tmp = dfs(i)
            count += tmp * (tmp - 1)
print(count)



    



