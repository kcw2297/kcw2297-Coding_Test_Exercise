"""https://www.acmicpc.net/problem/1654"""


"""
사용한 논리:
기준이 되는 선을 이분탐색을 이용해 구한 예시이다
반복문과 몫을 이용해 풀이한 모습이다
"""

import sys

K, N = map(int, sys.stdin.readline().split())
num_list = [int(sys.stdin.readline()) for _ in range(K)] 

start, end = 1, max(num_list)

while start <= end:
    mid = (start+end)//2
    lines = 0
    for i in num_list:
        lines += i//mid

    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)
    
