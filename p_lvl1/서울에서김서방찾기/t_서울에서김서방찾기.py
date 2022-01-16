"""https://programmers.co.kr/learn/courses/30/lessons/12919?language=python3"""



def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i]=="Kim":
            return f'김서방은 {i}에 있다'
