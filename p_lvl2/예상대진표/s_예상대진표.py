


"""
사용한 논리:
    처음에 1을 더해서 2를 나누었을 때 동일한 값을 나오게한다
"""

def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer


"""
내장함수 비트를 사용해서 구한 모습이다
"""
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
