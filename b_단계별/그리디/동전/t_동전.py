"""https://www.acmicpc.net/problem/11047"""


"""
사용한 논리:
십의 단위별로 값을 분리한다
이후에 5이상일 때와 미만일 때로 나누어 값을 더한다

백준의 경우에는 input 값을 받아서 이를 다시 변수에 저장해야한다
보기에서 주어진 1,5의 증가는 n에 따라 다르다
"""


n, k = map(str, (input().split()))
coin = []
count = 0


n = int(n)
for i in range(n):
    coin.append(input())

for i in k:
    i = int(i)
    if i>= 5:
        i -= 5
        count += 1
        count += i
    if i < 5:
        count += i

print(count)
