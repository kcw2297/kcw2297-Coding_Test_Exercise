"""https://www.acmicpc.net/problem/1541"""



"""
사용한 논리 및 오류:
1. 분리하기
2. 0으로 시작하는거 삭제
*문제에서는 괄호를 활용해서 최소값을 구하는 것인데, 단순히 최솟값을 구하는 것으로
이해했다
"""

# 주어진 값을 받는다
num = input().split()

# +와 -의 개수를 센다
m_count = num.count('-')
p_count = num.count('+')

count = []

# +와 - 개수만큼 split한다
for _ in range(m_count):
    a, b = num.split('-')
    count.append(a,b)

for _ in range(p_count):
    a, b = num.split('+')
    count.append(a,b)

# 앞자리가 0으로 시작하는 것은 0을 제거한다
for num in count:
    while num[0] == "0":
        num.remove('0')

# 문자열에서 정수로 바꾼다
total = [int(x) for x in count]

total.sort()

answer = total[0]
for num in range(1, p_count+1):
    answer += total[num]

for num in range(-1,m_count,-1):
    answer -= total[num]

print(answer)




