"""https://programmers.co.kr/learn/courses/30/lessons/86491"""


"""
2차원 배열 문제였지만, 결론은 min과 max를 요구한 문제였다
"""


"""
1번째 시도로 넓이와 높이를 따로 list에 저장한 후에 최대 값으로 비교를
하려고 하였지만, 이후 idx를 어떤식으로 처리해야하는지에서 막혔다
"""


def solution(sizes):
    width = []
    height = []

    for ele in sizes:
        width.append(ele[0])
        height.append(ele[1])

    max_height = max(width)

    if max()

    return answer

"""
2번째 시도로는 width와 height에 직접 값을 일력하여서 진행해보았지만
logic에서 오류가 있었는데, 리스트 안의 순서에 따라 결과가 다르게 나오는
오류가 있었다
"""


def solution(sizes):
    width = 0
    height = 0

    for ele in sizes:
        if width<ele[0]:
            width=ele[0]
        if height<ele[1] and ele[0]<ele[1]:
            height=ele[0]
        elif height<ele[1]:
            height=ele[1]

    answer = width*height
    return answer
