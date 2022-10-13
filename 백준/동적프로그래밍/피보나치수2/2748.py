
import sys

count = int(sys.stdin.readline())

fibo_list = [0,1]

def fibonacci(count):
    if count < len(fibo_list):
        return fibo_list[count]
    else:
        fib = fibonacci(count-1) + fibonacci(count-2)
        fibo_list.append(fib)
        return fib

print(fibonacci(count))


############################################################

def fib_dp(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    fib_array = [0,1]

    for i in range(2,n+1):
        num = fib_array[i-1] + fib_array[i-2]
        fib_array.append(num)
    return fib_array[n]

print(fib_dp(count))








