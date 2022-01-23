


"""
reversed함수를 사용하여서 배열을 뒤집었고 이후 map을 이용해 str을 iterable한
container로 잡고 int로 바꾸고 list로 마무리했다
"""


def solution(n):
    return list(map(int, reversed(str(n))))
