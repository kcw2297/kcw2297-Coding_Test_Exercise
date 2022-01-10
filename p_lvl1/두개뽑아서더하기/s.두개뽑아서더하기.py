


"""
https://docs.python.org/ko/3/library/itertools.html
"""

"""
시간 효율성에서 O(r)로 훨씬 빠르며 보다 수학적인 접근이 가능해서
논리적인 코드로 나아보인다
"""


from itertools import combinations
def solution(numbers):
    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))
