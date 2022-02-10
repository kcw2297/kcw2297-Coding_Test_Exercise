

"""
특정 테이블안에 값을 순환시에는 전체 값을 하나의 리스트로 담지 말고 각 열에 맞게 리스트로
분리하여 저장한다

테두리 순환을 하기위해서 왼/아래/오른/위 순으로 값을 이동시켜야하기에 전체에서
분리하여 계산한다
"""



def solution(rows, columns, queries):
    answer = []
    table = []
    for r in range(rows):
        table.append([a for a in range(r*columns+1, (r+1)*columns+1)])

    for query in queries:
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = table[query[0]][query[1]] # 왼쪽 위 값 저장
        small = tmp

        # left
        for i in range(query[0]+1, query[2]+1):
            table[i-1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            table[query[2]][i-1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            table[i+1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1] = table[query[0]][i]
            small = min(small, table[query[0]][i])
        table[query[0]][query[1]+1] = tmp

        answer.append(small)

    return answer
