


"""
stack과 brute force 방법을 사용하여 전체를 loop하여 푼 예시이다
"""


def solution(number, k):
    answer = [] # Stack

    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)

    return ''.join(answer[:len(answer) - k])
