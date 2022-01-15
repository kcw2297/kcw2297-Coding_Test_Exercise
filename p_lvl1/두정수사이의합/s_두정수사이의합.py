


"""
range를 이용해서 전체를 더한 방법이다
"""


def adder(a, b):
    if a > b: a, b = b, a

    return sum(range(a,b+1))
