"""https://www.acmicpc.net/problem/13305"""




"""
사용한 논리:
마지막 주유소를 제외하고 가장 적은 비용을 기준으로 계산한다
가장 적은 비용 이전은 그 다음으로 적은 비용을 기준으로 계산한다
"""


num_town = int(input())
bridges = list(map(int, input().split())) # 2 3 1
stations = list(map(int, input().split())) # 5 2 4 1
total_cost = 0


for i in range(num_town-1):
    if stations[i] < stations[i+1]:
        total_cost += bridges[i] * stations[i]
        stations[i+1] = stations[i]
    else:
        total_cost += bridges[i] * stations[i]

print(total_cost)