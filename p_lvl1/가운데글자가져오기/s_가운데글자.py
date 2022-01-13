




"""
특정 범위의 값을 구하려고 할 때 idx를 이용하는 것에서는 동일하였지만
space efficiency에서 아래가 더 효율적이
"""

"""
idx 첫번째는 len에서 1을 빼줌으로 처음 시작점을 올바르게 갖고
idx 두번째는 1을 더함으로써 짝수와 홀수인 경우를 구분한다
"""



def solution(str):
    return str[(len(str)-1)//2:len(str)//2+1]


abcde c
qwer  we

2:3
1:3
