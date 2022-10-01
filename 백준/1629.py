



def solve(a,b,c):
    if b == 1:
        return a%c
    else:
        k = solve(a, b//2,c)
        if b%2 == 0:
            return (k*k)%c
        else:
            return (k*k*a)%c  

a,b,c = map(int, input().split())
print(solve(a,b,c))







# import sys

# base, factor, divide = map(int, sys.stdin.readline().split())

# """
# 시간 초과
# """


# pattern = []

# if factor == 1:
#     print(base%divide)

# for i in range(1, factor):

#     remain = base**(i)%divide
#     if remain in pattern:
#         break

#     pattern.append(remain)


# num = factor%len(pattern)
# print(pattern[num])

