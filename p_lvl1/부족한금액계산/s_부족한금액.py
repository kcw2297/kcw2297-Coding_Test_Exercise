"""
등차수열의 합 : Sn = n(a1+an)/2 = n(a+l)/2
수학적 접근이 가능한 부분은 for loop 대신해서 수학적으로 접근하여
시간 효율성을 챙기자
"""


def solution(price, money, count):
    return max(0,count*((price*count)+price)//2-money)


def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
