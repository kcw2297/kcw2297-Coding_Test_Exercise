n,c = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort()

def binary(arr, s, e):
    global answer
    
    if s > e:
        return

    mid = (s+e) // 2
    cur = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] >= cur + mid:
            count += 1
            cur = arr[i]

    if count >= c:
        s = mid + 1
        answer = mid
    else:
        e = mid -1
    return binary(arr, s, e)


start = 1
end = arr[-1] - arr[0]
answer = 0



binary(arr, 1, end)
# print("결과는 다음과 같습니다")
print(answer)


