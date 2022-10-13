import sys

n = int(sys.stdin.readline())



fibo_list = [0,1]


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fibo_list = [0,1]

    for i in range(2,n+1):
        num = fibonacci(n-1) + fibonacci(n-2)
        fibo_list.append(num)
    return fibo_list[n]



print(fibonacci(n))







