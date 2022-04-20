"""
https://www.acmicpc.net/problem/2805
"""

"""
생각한 논리:


총 7미터, 5미터와 2미터
"""

N, L = map(int, input().split())

trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    line = 0
    mid = (start + end) // 2

    for tree in trees:
        if tree >= mid:
            line += (tree-mid)

    if line >= L:
        start = mid + 1
    else:
        end = mid - 1

print(end)
    