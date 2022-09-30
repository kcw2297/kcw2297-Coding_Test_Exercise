import sys
import math


tot = int(sys.stdin.readline())

# log3_n = int(math.log(n,3))


prototype = [ ['*'] * tot for _ in range(tot)]

start_remove = []
tot_remove = []

def starPick(n):
    global start_remove

    if n == 1:
        start_remove.append([n//3,n//3])
        tot_remove.append([n//3,n//3])
        return 

    starPick(n//3)

    space = int(math.log(n,3)) * 2

    r, c = start_remove[-1]
    temp = 0
    for _ in range((tot//3)-1):
        
        for _ in range((tot//3)-1):
            tot_remove.append([r, c])



    remove = []


