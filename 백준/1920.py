import sys

count1 = int(sys.stdin.readline())

base_list = list(map(int, sys.stdin.readline().split()))
base_list.sort()

count2 = int(sys.stdin.readline())


check_list = list(map(int, sys.stdin.readline().split()))



def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for i in check_list:
    print(binary(i,base_list,0,len(base_list)-1))





# 시간 초과
def bisect(num, base_list):
    if len(base_list) <= 0:
        return 0

    if len(base_list) == 1:
        if base_list[0] == num:
            return 1
        else:
            return 0

    mid = len(base_list)//2

    if base_list[mid] == num:
        return 1

    if base_list[mid] > num:
        return bisect(num, base_list[:mid])
    elif base_list[mid] < num:
        return bisect(num, base_list[mid+1:])

    return 0


import time 
start =time.time()

# for i in check_list:
#     print(bisect(i, base_list))


for i in check_list:
    print(binary(i, base_list,0,len(base_list)-1))

print('time: ', time.time()-start)








