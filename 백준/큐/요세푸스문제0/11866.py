from collections import deque 
import sys

queue = deque()
answer = []

n, k = map(int, sys.stdin.readline().split())

for i in range(1, n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print('<', end='')
for i in range(len(answer)-1):
    print(f'{answer[i]}', end=', ')
print(f'{answer[-1]}', end='')
print('>')

