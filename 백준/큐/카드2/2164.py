from collections import deque

count = int(input())

queue = deque()


if count == 1:
    print(1)

for i in range(1,count+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()

    if len(queue) == 1:
        print(queue[0])
        break

    first = queue.popleft()
    queue.append(first)















