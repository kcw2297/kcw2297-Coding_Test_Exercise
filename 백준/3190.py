import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [ [0]*N for _ in range(N)]
apples = int(sys.stdin.readline())
for _ in range(apples):
    apple_r, apples_c = map(int, sys.stdin.readline().split())
    arr[apple_r-1][apples_c-1] = 1
directions = int(sys.stdin.readline())
time_dir = {}
for _ in range(directions):
    key, value = sys.stdin.readline().rstrip().split()
    time_dir[int(key)] = value


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def change(d, c):
    if c == 'L':
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d


def start():
    direction = 1
    time = 1
    y, x = 0, 0
    visited = deque([[y, x]])
    arr[y][x] = 2
    while True:
        y, x = y + dy[direction], x + dx[direction]
        if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
            if not arr[y][x] == 1:
                temp_y, temp_x = visited.popleft()
                arr[temp_y][temp_x] = 0       
            arr[y][x] = 2
            visited.append([y,x])
            if time in time_dir:
                direction = change(direction, time_dir[time])
            time += 1
        else:
            return time


print(start())





