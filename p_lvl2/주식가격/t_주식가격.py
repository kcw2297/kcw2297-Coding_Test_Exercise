"""https://programmers.co.kr/learn/courses/30/lessons/42584"""


"""
어차피 1을 더하는것은 공통점이기에 나누지 말고, break조건문에만
if를 주어야했다
queue가 0이면 for loop도 안되니 if len()조건이 필요 없었다
"""


def solution(prices):
    answer = []

    while prices:
        count = 0

        if len(prices) == 1:
            answer.append(0)
            prices.pop()

        num = prices[0]
        for i in prices:
            if num <= i:
                count += 1
            elif num > i:
                count += 1
                answer.append(count)
                prices.pop(0)
                break

    return answer
