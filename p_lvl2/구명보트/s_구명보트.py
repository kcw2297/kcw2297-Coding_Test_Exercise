


"""
문제의 2가지 조건으로 보트에 2명만 타고, 보트의 최대 가용무게를 고려한 코드이다
sort를 한 후에 처음과 끝을 이용해 풀어낸 모습이다
"""



def solution(people,limit):
    answer = 0
    people.sort()

    start, end = 0, len(people)-1

    while start<=end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    return answer
