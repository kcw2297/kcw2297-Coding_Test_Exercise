"""https://www.acmicpc.net/problem/1920"""

"""
사용한 논리:
이분탐색문제에서 브루트포스 탐색을 하면 실패
deep copy를 한후에 했어야했다
"""



def binarycheck(start:int, end:int, list_:list, val:int):
    if start > end:
        return 0

    
    else:
        mid = (start+end)//2
        mid_val = list_[mid]

        if val == mid_val:
            return 1
        elif mid_val > val:
            return binarycheck(start,mid-1,list_,val)
        elif mid_val < val:
            return binarycheck(mid+1,end,list_,val)

N = int(input())
A_l = list(map(int,input().split()))

N_n = int(input())
N_l = list(map(int,input().split()))

A_l.sort()
N_l.sort()


for i in N_l:
    print(binarycheck(0,N-1,A_l,i))













# import copy

# A_n = int(input())
# A_l = map(int,input().split())

# N_n = int(input())
# N_l = map(int,input().split())

# A_l.sort()
# N_l.sort()

# def check(ele, lit):
#     if len(lit) == 1:
#         if ele == lit[0]:
#             return True
#         else:
#             return False

#     half = len(lit)//2
#     if ele == lit[half]:
#         return True
#     elif ele > lit[half]:
#         new_list = copy.deepcopy(lit[half:])
#         check(ele,new_list)
#     else:
#         new_list = copy.deepcopy(lit[:half])
#         check(ele,new_list)

# for i in N_l:
#     if check(i,A_l):
#         print(1)
#     else:
#         print(0)
