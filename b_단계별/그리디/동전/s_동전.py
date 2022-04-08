


"""
n의수 만큼 input을 배열에 저장한다
일정한 배수별로 동전의 가치가 있기에 나누기로 총 필요한 
동전의 개수를 구한다
"""



n, k = map(int, (input().split()))
coin = []
cnt = 0
for i in range(n):
    coin.append(input())
for j in range(n-1, -1, -1):
    if int(coin[j]) <= k :
        cnt += k // int(coin[j])
        k -= (int(coin[j]) * (k // int(coin[j])))
    else :
        cnt = cnt
print(cnt)

