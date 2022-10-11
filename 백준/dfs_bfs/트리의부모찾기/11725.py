
import sys
sys.setrecursionlimit(10**6)

count = int(sys.stdin.readline())

graph = [[] for _ in range(count+1)]

for _ in range(count-1):
    p, c = map(int, sys.stdin.readline().split())
    graph[p].append(c)
    graph[c].append(p)

result = [0] * (count+1)

def dfs(s):
    for i in graph[s]:
        if result[i] == 0:
            result[i] = s
            dfs(i)



dfs(1)

for i in range(2,count+1):
    print(result[i])