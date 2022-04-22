



"""
인덱스의 시작점과 끝점을 분리시켜서 계산하였다
마지막 c의 값이 전체 msg와 같으면 최종 조건을 실행후 종료시킨다
"""

def solution(msg):
    answer = []
    dic = {}

    for i in range(26):
        dic[chr(65+i)] = i+1

    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(dic[msg[w:c]])
            break
        if msg[w:c+1] not in dic:
            dic[msg[w:c+1]] = len(dic) + 1
            answer.append(dic[msg[w:c]])
            w = c

    return answer


"""
사용한 논리:
초기 지정된 값을 넣는 것은 동일하다
추가한 글자를 하나씩 제외하면서 풀어낸 풀이이다
"""

def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer
