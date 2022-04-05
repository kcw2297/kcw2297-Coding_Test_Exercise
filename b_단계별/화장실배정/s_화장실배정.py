


"""
사용한 논리:
time 안에 값을 저장 후 시작시간으로 정렬 한후 끝나는 시간으로 정렬한다
time안의 배열을 반복하면서 끝과 시작 시간을 비교한다


"""


n = int(input())
time_list = [[0]*2 for i in range(n)]
for j in range(n):
    start, end = map(int, input().split())
    time_list[j][0] = start
    time_list[j][1] = end
time_list.sort(key=lambda x:(x[1],x[0]))
cnt = 1
end_time = time_list[0][1]
for k in range(1,n):
    if time_list[k][0] >= end_time:
        cnt += 1
        end_time = time_list[k][1]
print(cnt)

"""
같은 논리지만 오류가 생겼다
"""

N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])

time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순
time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)