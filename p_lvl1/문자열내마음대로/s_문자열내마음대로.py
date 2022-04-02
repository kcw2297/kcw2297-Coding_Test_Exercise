


"""
리스트 안에 어떤 기준으로 정렬을 하고자 한다면 sorted()안에 key를 활용해서
정렬한다. 여기서 lambda를 활용해 가상 함수로 쉽게 key를 정의했다
"""


def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])
