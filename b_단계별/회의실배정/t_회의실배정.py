"""https://www.acmicpc.net/problem/1931"""




"""
사용한 논리 오류:
시작과 끝의 시간이 가장 작은 수를 기준으로 정렬한다
끝의 시간과 시작 시간을 비교해서 일치하는 경우 count한다

*문제 접근시에 확실한 논리가 잡히지 않는다면 결국에 에러 케이스를 낳게된다
*설령 구현을 못하더라도 논리만 맞아도 아직은 괜찮다

*시작 시간과 끝 시간의 정렬하는 순서에 따라 결과값이 달라진다
*[a,b]로 되어 있는 경우, for i, j in 배열 => 안에 있는 원소가 하나씩 분리된다
"""

count = 0
manage = []

total_meeting = input()
total = []

for _ in range(total_meeting):
    a,b = input().split()
    c = b-a
    meeting = [c,a,b]
    total.append(meeting)


total.sort()

for meeting in total:
    if manage == []:
        manage.append(me)


"""/////////////////////////////////////////////////"""


n = int(input())
times = []
for _ in range(n):
    a, b = map(int,input().split())
    times.append([a,b])

times = sorted(times, key= lambda x: x[0])
times = sorted(times, key= lambda x: x[1])



start = 0
count = 0

for i, j in times:
    if i >= start:
        count += 1
        start = j
    
print(count)

