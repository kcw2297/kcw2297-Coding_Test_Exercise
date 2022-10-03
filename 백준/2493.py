
n = int(input())
top = list(map(int,input().split()))
stack = []
answer = [0 for _ in range(n)]

for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i,top[i]])

print(*answer)



# import sys

# count = int(sys.stdin.readline())

# tower_list = list(map(int,sys.stdin.readline().split()))

# result = []

# for i in range(count-1,0,-1):
#     for j in range(i-1,-1,-1):
#         if tower_list[i] <= tower_list[j]:
#             result.append(j+1)
#             tower_list.pop()
#             break

#     if len(result) != count-i:
#         result.append(0)

# result.append(0)

# for i in range(len(result)-1,-1,-1):
#     print(result[i], end=' ')






