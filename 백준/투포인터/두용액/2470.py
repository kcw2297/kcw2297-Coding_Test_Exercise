import sys

count = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()


min_v = sys.maxsize
solutions = []

def twosolution(num_list,s,e):
    global min_v, solutions

    if s >= e:
        return

    left = num_list[s]
    right = num_list[e]
    sum_v = left + right

    if abs(sum_v) < min_v:
        min_v = abs(sum_v)
        solutions = [left, right]

    if sum_v < 0:
        s += 1
    else:
        e -= 1
    return twosolution(num_list,s,e)


twosolution(num_list,0,len(num_list)-1)

print(solutions[0], solutions[1])



