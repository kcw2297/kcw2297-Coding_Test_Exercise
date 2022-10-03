import sys

count = int(sys.stdin.readline())

num_list = [ int(sys.stdin.readline()) for _ in range(count) ]

stack = []
for i in num_list:
    if i == 0:
        stack.pop()
        continue
    else:
        stack.append(i)

print(sum(stack))



