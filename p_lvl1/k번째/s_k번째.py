"""
lambda map 조합으로 space-effiency를 챙긴 모습이다
"""


"""교휸 : 정해진 범위에서 loop를 해야하는 경우에 lambda, map을 이용하자"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
