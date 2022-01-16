"""https://programmers.co.kr/learn/courses/30/lessons/12921"""


"""
교훈 :
이번 문제의 핵심은 주어진 숫자를 2부터 container에 넣고
나누어지는 값들을 하나씩 빼주는 것이었다
리스트와 set 중 하나를 사용하여 계산을 하면 되는데
set가 조금더 간단히 풀 수 있는 접근법이었다

range안에서 (시작,끝,단계)를 활용해서 배수를 빼주었다
*set-set를 해야 안에 값을 뺀다
"""




def solution(numbers):
    answer = [0]

    for num in range(2,numbers+1):
        if num == 2:
            answer+=1
            continue

        for i in range(2,num):
            if num % i ==0:
                break
            if i == num-1:
                answer+=1
    return answer

def solution(numbers):
    num = set(range(2,numbers+1))

    for i in range(2,numbers+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
