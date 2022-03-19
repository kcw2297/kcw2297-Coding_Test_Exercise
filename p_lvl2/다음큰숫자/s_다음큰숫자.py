





"""
사용한 논리:
내가 접근한 방식과 동일하지만 count 내장함수를 이용해 훨씬 
간결하고 효율적으로 진행하였다
"""





def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n