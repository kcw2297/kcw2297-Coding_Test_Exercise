
    


import sys
import heapq

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())

    heap_l = []
    heap_r = []

    if len(heap_l) == len(heap_r):
        heapq.heappush(heap_l, (-num, num))
    else:
        heapq.heappush(heap_r, (num, num))

    if heap_l[0][1] > heap_r[0][1]:
        min = heapq.heappop()
        min = heap_r[0][1]
        max = heap_l[0][1]
        heap_l[0][1] = min
        heap_r[0][1] = max

    






