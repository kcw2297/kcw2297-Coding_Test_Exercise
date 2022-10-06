# import sys

# N, K = map(int, sys.stdin.readline().split())

# # num_v = str(sys.stdin.readline().split())
# num_v = input()
# stack = []

# for i in range(N):

#     while stack and K > 0 and stack[-1] < num_v[i]:
#         K -= 1
#         stack.pop()

#     stack.append(num_v[i])

# print(''.join(stack))


N, K = map(int, input().split())
num = list(input())
k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]:
        stack.pop()
        k -= 1
    stack.append(num[i])

print(''.join(stack[:N-K]))





