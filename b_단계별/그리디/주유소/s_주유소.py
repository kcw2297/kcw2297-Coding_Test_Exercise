







"""
사용한 논리:
코드의 길이가 더 짧은 방법으로 최소값의 주유소를 변수에 
저장한 후 반복문이 진행되면서 최솟값을 따로 계산한다
"""



N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

minVal = cities[0]
sum = 0
for i in range(N-1):
    if minVal > cities[i]:
        minVal = cities[i]
    sum += (minVal * roads[i])
    
print(sum)