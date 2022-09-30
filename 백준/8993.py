m, n, l = map(int, input().split())
shooters = list(map(int, input().split()))
animals = []
for _ in range(n):
    x, y = map(int, input().split())
    if y <= l:
        animals.append((x, y))
shooters.sort()
animals.sort(key=lambda axis: axis[0])
ans = 0
idx = 0
for i in range(len(animals)):
    left, right = idx, len(shooters)-1
    mid = 0
    # 사대의 중심점을 구하는데, mid는 사대
    while left <= right:
        mid = (left+right)//2
        if shooters[mid] <= animals[i][0]:
            if len(shooters) - 1 == mid or shooters[mid+1] > animals[i][0]:
                break
            left = mid + 1
        else:
            right = mid - 1
    idx = mid
    # 조건 발생문 
    if abs(animals[i][0] - shooters[mid]) + animals[i][1] <= l:
        ans += 1
    elif len(shooters) > mid+1 and abs(animals[i][0] - shooters[mid+1]) + animals[i][1] <= l:
        ans += 1
print(ans)



#내가 풀이한 8993문제

# import sys

# shootings_c, animals_c,max_range  = map(int, sys.stdin.readline().split())
# shootings = list(map(int, sys.stdin.readline().split()))

# animals = []
# for _ in range(animals_c):
#     animals.append(list(map(int, sys.stdin.readline().split())))


# left = 0
# right = shootings_c - 1

# result = 0
# for ani_coor in animals:
#     while left < right:
#         mid = (left + right)//2

#         shooter_coor = shootings[mid]

#         s_range =  abs(shooter_coor - ani_coor[0]) - ani_coor[1]

#         if s_range <= max_range:
#             result += 1

#         else:
#             right -= 1



