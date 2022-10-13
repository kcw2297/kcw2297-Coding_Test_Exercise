import sys


count = int(sys.stdin.readline())

commands = [ sys.stdin.readline().rstrip() for _ in range(count) ]

stack = []
for command in commands:
    if 'push' in command:
        _, num = command.split()
        stack.append(int(num))
        continue

    if 'top' == command:
        if len(stack)==0 or type(stack[-1]) != int:
            print(-1)
        else:
            print(stack[-1])
        continue

    if 'size' == command:
        count = 0
        for i in stack:
            if type(i) != int:
                continue
            if type(i) == int:
                count += 1
        print(count)
        continue

    if 'empty' == command:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
        continue

    if 'pop' == command:
        if len(stack) != 0 and type(stack[-1]) == int:
            print(stack[-1])
            stack.pop()
            continue
        flag = 1
        for i in stack:
            if type(i) == int:
                flag = 0
                continue
        if flag:
            print(-1)
        
        













