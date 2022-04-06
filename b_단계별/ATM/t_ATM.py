"""https://www.acmicpc.net/problem/11399"""





"""
사용한 논리:
5
3 1 4 3 2

"""


n = int(input())

line = sorted(map(int,input().split()))

count = 0
while line:
    count += (len(line) * line.pop(0))
print(count)
