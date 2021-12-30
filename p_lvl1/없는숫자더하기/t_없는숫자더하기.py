"https://programmers.co.kr/learn/courses/30/lessons/86051"


def solution(numbers):
    tot = [0,1,2,3,4,5,6,7,8,9]
    store = 0

    for ele in tot:
        if ele in numbers:
            continue
        else:
            store += ele

    return store
