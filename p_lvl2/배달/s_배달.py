
"""
사용한 논리:
다익스트라 알로리즘을 활용한 문제로 최단거리를 구할 때 사용된다. 

근접 노드를 나타내는 변수에 각 노드와 거리를 배열안에 저장을 한다.
최단거리를 나타내는 배열을 변수에 저장한다

dijkstra 알고리즘으로 최단거리인경우 push를 한후 그 거리를 기준으로
다음 노드까지의 거리를 조사한다
"""


from collections import deque

def dijkstra(dist,adj):
    deq = deque()
    deq.append([0,1])
    while deq:
        cost, node = deq.pop()
        for c,n in adj[node]:
            if cost+c < dist[n]:
                dist[n] = cost+c
                deq.append([cost+c,n])



def solution(N, road, K):
    dist = [float('inf')]*(N+1)  # dist 배열에 최단거리를 저장
    dist[1] = 0  # 1번을 기준으로 최단거리를 찾기 때문에 0
    adj = [[] for _ in range(N+1)]  # 인접노드&거리 기록할 배열
    for r in road:
        adj[r[0]].append([r[2],r[1]]) # 각 노드를 인덱스로 표현하며, 근접한 노드와 거리를 저장
        adj[r[1]].append([r[2],r[0]])
    dijkstra(dist,adj)
    return len([i for i in dist if i <=K])


"""
N   Road                                                        K   Result
6	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	4	4

    adj
	[[], [[1, 2], [2, 3]], [[1, 1], [2, 3]], 
    [[2, 1], [2, 2], [3, 4], [2, 5], [3, 5]], 
    [[3, 3]], [[2, 3], [3, 3], [1, 6]], [[1, 5]]] 

    dist
    [inf, 0, inf, inf, inf, inf, inf]
"""



 