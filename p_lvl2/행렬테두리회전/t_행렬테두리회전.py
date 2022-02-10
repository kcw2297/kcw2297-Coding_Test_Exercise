"""https://programmers.co.kr/learn/courses/30/lessons/77485"""

"""
전체를 기준으로 rotate을 하는 방법을 고민하다가 너무 복잡해져서 아이디어가 나오지 못했다
항상 무언가 큰 덩어리를 해결하려고할 때 작은 단위로 분리하여 계산하면 해답이 나온다
이 문제는 테두리를 4개로 분리하여 접근했어야하는 문제였다
"""


def rotate(rows,x1,y1,x2,y2):
    return rows*(y1-1)+x1




def solution(rows, columns, queries):

    entire = [x for x in range(1,rows*columns+1)]

    while queries:
        query = queries.pop(0)
        x1 = query[0]
        y1 = query[1]
        x2 = query[2]
        y2 = query[3]

        if (x2-x1+1) == 2:
            a =
