

"""
join()함수를 이용해서 리스트를 문자열로 이어준다
-추가로 join앞에 특정 기호로 넣으면 문자열 사이에
기호를 넣는다
"""


def solution(s):
    return ''.join(sorted(s, reverse=True))
