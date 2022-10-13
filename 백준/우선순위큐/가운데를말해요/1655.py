

import sys
import heapq



N = int(sys.stdin.readline())

leftheap = []
rightheap = []
answer = []
for i in range(N):
    inputNum = int(sys.stdin.readline())

    if len(leftheap)  == len(rightheap):
        heapq.heappush(leftheap, (-inputNum, inputNum))
    else:
        heapq.heappush(rightheap, (-inputNum, inputNum))

    if rightheap and leftheap[0][1] > rightheap[0][0]:
        min = heapq.heappop(rightheap)[0]
        max = heapq.heappop(leftheap)[1]
        heapq.heappush(leftheap, (-min, min))
        heapq.heappush(rightheap, (max, max))

    answer.append(leftheap[0][1])

for j in answer:
    print(j)
