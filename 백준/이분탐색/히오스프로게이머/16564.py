import sys
input = sys.stdin.readline

n, k = map(int,input().split())
levels = [ int(input()) for _ in range(n)]

start = min(levels)
end = start + k

res = 0
while start <= end:
    mid = (start + end) // 2
    
    hap = 0
    for level in levels:
        if mid > level:
           hap+= (mid - level)
           
    if hap <= k:
        start = mid+1
        res = max(mid,res)
    else:
        end = mid -1


print(res)




