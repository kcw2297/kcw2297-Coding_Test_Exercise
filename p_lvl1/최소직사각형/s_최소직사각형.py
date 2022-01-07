

"""
문제의 핵심은 최소 넓이의 지갑을 구하는 것이기에, max와 min을 활용한
방식이다
"""


def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

"""
문제의 logic flow대로 푼 것으로 2개의 idx로 풀어 낸 모습이다
이로인해 내가 고민한 idx를 해결했다
"""

def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    return max(w) * max(h)
