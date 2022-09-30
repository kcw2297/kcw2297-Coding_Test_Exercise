import sys
from itertools import (
    permutations, 
    combinations
)

n = int(sys.stdin.readline())

soccer_field = []
for _ in range(n):
    soccer_field.append(list(map(int, sys.stdin.readline().split())))

min_v = 100000000000000000

def compute(comb):
    result = 0
    permute_output = permutations(comb, 2)
    for r, c in permute_output:
        result += soccer_field[r][c]
    return result


def findMin(n):
    global min_v
    num_list = [i for i in range(n)]
    people_comb = list(combinations(num_list, n//2))[n//2:]

    for comb in people_comb:
        result1 = compute(list(comb))
        temp = []
        for i in range(n):
            if i not in comb:
                temp.append(i)

        result2 = compute(temp)

        if min_v > (abs(result1-result2)):
            min_v = (abs(result1-result2))

    return 

findMin(n)
print(min_v)


"""
def findMin(people):

    사람_조합 = list(조합(숫자리스트, n//2))[:n//2+1] # 사람_조합의 절반만 계산해도 결과값이 나온다
    
    for i in 사람_조합:
        계산_결과1 = 계산(특정조합)
        계산_결과2 = 계산(그외조합)
        if min > (계산_결과1 - 계산_결과2):
            min = (계산_결과1 - 계산_결과2)


def 계산(특정조합):
    순열_결과 = permutations(특정조합, 2)
    result = 0
    for r, c in 순열결과:
        result += occer_field[r][c]

    return result

"""















