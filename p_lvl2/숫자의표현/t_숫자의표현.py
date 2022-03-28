"""https://programmers.co.kr/learn/courses/30/lessons/12924"""


"""
사용한 논리:
모든 수는 1부터 시작
주어진 값에서 순서대로 차감을해서 정확히 값이 빼지면 count+=1

"""

def solution(n):
    count = 0

    for i in range(1,n+1):
        check = n
        for j in range(i,n+1):
            check -= j
            if check == 0:
                count += 1
                break
            elif check < 0:
                break
    return count