import sys

count = int(sys.stdin.readline())
num_list = [ int(sys.stdin.readline()) for _ in range(count) ]

first = num_list[-1]
result = 1
for i in range(count-2, -1, -1):
    if num_list[i] > first:
        result += 1
        first = num_list[i]


print(result)



