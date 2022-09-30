import sys


count = int(sys.stdin.readline())

num_list = [ int(sys.stdin.readline()) for _ in range(count)]

record_num = 0
def countNum(num):
    """
        1. num을 1까지 분해 => 종료
        2. num -1 => 진행
        3. 
    """
    if num == 1:
        record_num += 1
        return 1

    remain = num%2
    quo = num//2
    
    
    
    countNum(num-1)
    