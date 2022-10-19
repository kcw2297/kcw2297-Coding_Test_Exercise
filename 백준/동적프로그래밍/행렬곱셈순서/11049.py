import sys
input = sys.stdin.readline


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
DP = [[0]*N for _ in range(N)]

for size in range(1,N):
    for start in range(N-size):
        end = start + size
        result = float('inf')
        for cut in range(start, end):
            result = min(result, DP[start][cut]+DP[cut+1][end] +
                    matrix[start][0]*matrix[cut][1]*matrix[end][1])
        DP[start][end] = result

print(DP[0][-1])



#################################################################

import sys

N = int(sys.stdin.readline())

matrix_r = []
matrix_c = []

for _ in range(N):
    r,c = map(int,sys.stdin.readline().split())
    matrix_r.append(r)
    matrix_c.append(c)

dp = [[0]*N for _ in range(N)]

def func(x,y):
    if dp[x][y] >0:
        return dp[x][y]
    
    if y-x <= 0:
        return 0
    
    mm = float('inf')

    for i in range(x,y):
        mm = min(mm, func(x,i) + func(i+1,y) +
                matrix_r[x]*matrix_c[i]*matrix_c[y])
    dp[x][y] = mm
    return dp[x][y] 


print(func(0,N-1))


