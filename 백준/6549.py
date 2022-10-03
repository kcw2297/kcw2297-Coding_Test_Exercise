# 분할 정복 방식
import sys
input = sys.stdin.readline
arr = []


def solve(lt, rt):
    global arr
    if lt == rt:
        return arr[lt]

    mid = (lt+rt)//2
    res = max(solve(lt,mid), solve(mid+1,rt))
    lo = mid
    hi = mid + 1
    height = min(arr[lo], arr[hi])
    res = max(res,2*height)

    while lt < lo or hi < rt:
        if hi < rt and (lt == lo or arr[lo-1] < arr[hi+1]):
            hi += 1
            height = min(height, arr[hi])

        else:
            lo -= 1
            height = min(height, arr[lo])

        res = max(res, height*(hi-lo+1))

    return res



while True:
    input_arr = list(map(int, input().rstrip().split()))
    if input_arr[0] == 0:
        break
    N = input_arr[0]
    arr = input_arr[1:]
    print(solve(0,N-1))



# 스택 방식 2
# import sys
# input = sys.stdin.readline


# arr = []

# while 1:
#     f_arr = list(map(int, input().rstrip().split()))
#     if f_arr[0] == 0:
#         break
#     ans = 0
#     st = []
#     arr = f_arr[1:]

#     for val in arr:
#         tmp = 0
#         while len(st) != 0 and st[-1][0] > val:
#             tmp += st[-1][1]  # 스택이 갖고 있던 밑변 값을 넘겨준다
#             ans = max(ans, tmp * st[-1][0]) # 높이
#             st.pop()

#         tmp += 1
#         st.append([val, tmp])  # 높이와 밑변

#     tmp = 0
#     while len(st) != 0:  # 남은 값들 처리
#         tmp += st[-1][1]
#         ans = max(ans, tmp*st[-1][0])
#         st.pop()

#     print(ans)


# 스택 방식 1
# from collections import deque
# import sys

# while True:
#     rec = list(map(int, sys.stdin.readline().split()))
#     n = rec.pop(0)
#     if n == 0:
#         break

#     stack = deque()
#     ans = 0

#     for i in range(n):
#         while stack and rec[stack[-1]] > rec[i]:
#             tmp = stack.pop()


#             if not stack:
#                 width = i
#             else:
#                 width = i - stack[-1] -1 
            
#             ans = max(ans, width*rec[tmp])

#         stack.append(i)

#     while stack:
#         tmp = stack.pop()

#         if not stack:
#             width = n
#         else:
#             width = n - stack[-1] -1 
        
#         ans = max(ans, width*rec[tmp])

#     print(ans)







