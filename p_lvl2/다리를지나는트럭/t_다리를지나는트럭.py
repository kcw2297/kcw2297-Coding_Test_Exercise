"""https://programmers.co.kr/learn/courses/30/lessons/42583"""



"""
각 트럭마다 다리를 지나는 기간을 어떤식으로 고민하다가 멈췄다
index를 이용해야하나 생각을 해봤는데, 그러면 처음 리스트에 저장시에
tuple로 저장하고 이후 다시 분리해야하는데, 코드가 너무 복잡해졌다
"""


from collections import deque

def solution(bridge_length, weight, truck_weights):

    wait = deque(truck_weights)
    bridge = []
    count = 0
    answer = 0

    while wait:
        answer+=1
        if sum(bridge)+wait[0] < weight:
            bridge.append(wait.popleft())


    return answer
