"""https://programmers.co.kr/learn/courses/30/lessons/12932"""





def solution(n):

    model = []
    answer = str(n)[::-1]

    for i in range(len(answer)):
        model.append(int(answer[i]))

    return model
