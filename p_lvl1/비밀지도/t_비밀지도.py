"""https://programmers.co.kr/learn/courses/30/lessons/17681"""



"""
bin()함수를 사용하여 2인수로 바꾼 후에 OR를 이용하여 구하는 방식을
사용하였지만, 처음 빈칸을 확인하지 못하는 에러가 나왔다
"""

"""
교훈 : zip()을 이용하여 2개의 동일한 수의 list의 ele를 묶어서
쉽게 값을 구하자
"""


def solution(n, arr1, arr2):
    answer = []

    for idx in range(n):
        state = bin(arr1[idx] | arr2[idx])[2:]
        state = state.rjust(n,"0")
        add = ""
        for ele in state:
            if ele=="1":
                add += "#"
            else:
                add += " "
        answer.append(add)
    return answer
