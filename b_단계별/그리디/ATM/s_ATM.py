







"""
주어진 n의 값을 반복하여서 값을 구한 모습이다
"""


input()
a=sorted(map(int,input().split()))
print(sum([a[i]*(len(a)-i)for i in range(len(a))]))