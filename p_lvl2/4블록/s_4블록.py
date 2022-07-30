
"""
사용한 논리:
기존의 테이블에서 행과열을 뒤집어 하나의 리스트로 관리 가능하게 바꾼다
*이때 zip(*board)는 iterable 객체를 나눌때 사용된다
set와 |= 연산자를 이용해 조건에 맞는 범위를 저장한다
조건에 해당하는 사각형을 0으로 전환 후에 해당 자리만큼 리스트 뒤로 간다
마지막으로 pop_set의 길이를 전환하는데 0이 아닌경우 count에 값을 더한 후
다시 반복하고, 0이면 count를 반환한다
"""


# 뒤집어서 n 높이, m 폭
def pop_num(b, m, n):
    pop_set = set()
    # search
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i-1][j-1] == b[i-1][j] == b[i][j-1] != '_':
                pop_set |= set([(i, j), (i-1, j-1), (i-1, j), (i, j-1)])
    # set_board
    for i, j in pop_set: # i 높이, j 폭
        b[i][j] = 0        
    for i, row in enumerate(b):
        empty = ['_'] * row.count(0) # 각 열의 0인 개수 == "_"
        b[i] = empty + [block for block in row if block != 0] # [_,_,F,T]
    return len(pop_set)
 
def solution(m, n, board):
    count = 0
    b = list(map(list,zip(*board)))
    while True:
        pop = pop_num(b, m, n)
        if pop == 0: 
            return count
        count += pop


"""
다른 이의 풀이
"""


def solution(m, n, board):
    x = board
    x2 =[]

    for i in x: 
        x1 = []
        for i2 in i:
            x1.append(i2)
        x2.append(x1)

    point = 1
    while point != 0:
        list = []
        point = 0
        for i in range(m - 1):
            for j in range(n - 1):
                if x2[i][j] == x2[i][j + 1] == x2[i + 1][j] == x2[i + 1][j + 1] != '팡!':
                    list.append([i, j])
                    point += 1

        for i2 in list:
            i, j = i2[0], i2[1]
            x2[i][j], x2[i][j + 1], x2[i + 1][j], x2[i + 1][j + 1] = '팡!', '팡!', '팡!', '팡!'

        for i3 in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if x2[i + 1][j] == '팡!':
                        x2[i + 1][j], x2[i][j] = x2[i][j], '팡!'

    cnt = 0
    for i in x2:
        cnt += i.count('팡!')
    return cnt


