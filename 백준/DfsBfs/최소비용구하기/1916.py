import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

g = [[] for _ in range(n+1)]
for i in range(m):
    a,b,w = map(int, input().split())
    g[a].append((b,w))

st, ed = map(int, input().split())
dist = [10000000000000] * (n+1)

def dijkstra(start):
    dist[start] = 0
    q = [(0,st)]

    while q:
        w, cur = heapq.heappop(q)
        if dist[cur] < w:
            continue

        for dest, wei in g[cur]:
            cost = w + wei
            if dist[dest] > cost:
                dist[dest] = cost
                heapq.heappush(q, (cost,dest))

dijkstra(st)
print(dist[ed])







