




"""
굳이 if문을 사용하지 않고 같냐 틀리냐고 true,false가 나오니
0과 비교하면 되는 문제였다

list를 sum()하면 정수로 반환된다
"""


def solution(n):

    return n % sum([int(c) for c in str(n)]) == 0
