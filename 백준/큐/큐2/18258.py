import queue
import sys
from collections import deque

count = int(sys.stdin.readline())

queue = deque()

for _ in range(count):
    command = sys.stdin.readline().rsplit()

    if command[0] == 'push':
        queue.append(command[1])
        continue

    if command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
        continue

    if command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
        continue

    if command[0] == 'size':
        print(len(queue))
        continue

    if command[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
        continue

    if command[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
        continue



