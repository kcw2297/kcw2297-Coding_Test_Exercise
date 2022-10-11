# import sys
# from itertools import (
#     permutations, 
#     combinations
# )

# n = int(sys.stdin.readline())

# soccer_field = []
# for _ in range(n):
#     soccer_field.append(list(map(int, sys.stdin.readline().split())))

# min_v = 100000000000000000

# def compute(comb):
#     result = 0
#     permute_output = permutations(comb, 2)
#     for r, c in permute_output:
#         result += soccer_field[r][c]
#     return result


# def findMin(n):
#     global min_v
#     num_list = [i for i in range(n)]
#     people_comb = list(combinations(num_list, n//2))[n//2:]

#     for comb in people_comb:
#         result1 = compute(list(comb))
#         temp = []
#         for i in range(n):
#             if i not in comb:
#                 temp.append(i)

#         result2 = compute(temp)

#         if min_v > (abs(result1-result2)):
#             min_v = (abs(result1-result2))

#     return 

# findMin(n)
# print(min_v)


###############################################################################################

import sys

def dfs(idx, cur, add, minus, multiply, divide):
    global max_v, min_v, count

    if idx == count:
        max_v = max(max_v, cur)
        min_v = min(min_v, cur)
        return

    if add > 0:
        dfs(idx+1,cur+num_list[idx],add-1,minus,multiply,divide)

    if minus > 0:
        dfs(idx+1,cur-num_list[idx],add,minus-1,multiply,divide)

    if multiply > 0:
        dfs(idx+1,cur*num_list[idx],add,minus,multiply-1,divide)

    if divide > 0:
        if cur <0:
            dfs(idx+1,-((-cur)//(num_list[idx])),add,minus,multiply,divide-1)
        else:
            dfs(idx+1,cur//num_list[idx],add,minus,multiply,divide-1)

count = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))
add, minus, multiply, divide = map(int, sys.stdin.readline().split())

max_v = -1000000000001
min_v = 1000000000001
    
dfs(1, num_list[0], add, minus, multiply, divide)
print(max_v)
print(min_v)

