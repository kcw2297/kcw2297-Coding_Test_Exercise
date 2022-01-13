"""https://programmers.co.kr/learn/courses/30/lessons/87389"""



"""
수학적 접근으로 prime number인지 확인 후 약수를 이용하여
풀어보려 했지만 식이 더 복잡해져서 전체 for loop을 하였다.
"""


def solution(n):
    for x in range(1,n):
        if n%x ==1:
            return x



"""pythonic하게 list comprehension으로 바꾼 것이"""
def solution(n):
    return [x for x in range(1,n) if n%x==1][0]
