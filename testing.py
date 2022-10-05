import sys

count = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()


min_v = sys.maxsize
result = []

for i in range(count-1):
    s = i + 1
    e = count - 1

    while s <= e:
        mid = (s+e)//2  
        if abs(num_list[mid] + num_list[i]) <= min_v:
            min_v = abs(num_list[mid] + num_list[i])
            result = [num_list[i], num_list[mid]]
            s = mid + 1
        else:
            e = mid - 1

    

print(result[0],result[1])