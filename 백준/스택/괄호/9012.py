import sys

count = int(sys.stdin.readline())

str_list = [sys.stdin.readline().rstrip() for _ in range(count)]


for parens in str_list:
    stack = []
    for paren in parens:
        if paren == '(':
            stack.append(paren)
            continue
        else:
            if len(stack) == 0:
                stack.append(1)
                break

            else:
                stack.pop()
    

    if len(stack) != 0:
        print('NO')
    else:
        print('YES')



