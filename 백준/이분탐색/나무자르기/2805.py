N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

def binary(s,e):
    global tree, M
    
    if s >e:
        return (s+e)//2
    
    mid = (s+e)//2
    log = 0
    for i in tree:
        if i >=mid:
            log += i-mid
            
    if log >= M:
        s = mid+1
        return binary(s,e)
    else:
        e = mid -1
        return binary(s,e)
    
print(binary(start,end))
        


#다른 예제, 시간 속도 약간 느림
# def binary_search(arr, start, end):
#     res = 0
#     while start <= end:
#         mid = (start+end) // 2
#         total = 0
        
#         for x in arr:
#             if x > mid:
#                 total+= x- mid
            
#         if total < m:
#             end = mid-1
#         else:
#             res = mid
#             start = mid +1
#     return res
        
# n , m = map(int,input().split())
# li = list(map(int,input().split()))

# r = binary_search(li, 0, max(li))
# print(r)