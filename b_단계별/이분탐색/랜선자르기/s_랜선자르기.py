


"""
end는 그 전의 이분탐색에서 주어진 숫자보다 나눈 값이 적을 때,
즉 mid값이 큰 경우 -1을 한 후에 end에 할당 받는다
이후 값들 중에 n보다 같거나 클시 end가 가장 길이가 큰 경우이다
"""


import sys
K, N = map(int, input().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(lan) #이분탐색 처음과 끝위치

while start <= end: #적절한 랜선의 길이를 찾는 알고리즘
    mid = (start + end) // 2 #중간 위치
    lines = 0 #랜선 수
    for i in lan:
        lines += i // mid #분할 된 랜선 수
        
    if lines >= N: #랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)

