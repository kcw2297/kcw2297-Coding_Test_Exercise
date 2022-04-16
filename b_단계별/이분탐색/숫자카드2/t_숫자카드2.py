"""https://www.acmicpc.net/problem/10816"""


"""
사용한 논리:
count 내장 함수를 이용해 단순하게 구하려 하였지만 역시 문제의 취지와
맞지 않는 관계로 실패하였다
"""

from sys import stdin

_ = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
M = map(int,stdin.readline().split())


def binary(n,N,start,end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n,N,start,m-1)
    else:
        return binary(n,N,m+1,end)


n_dic = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in n_dic:
        n_dic[n] = binary(n,N,start,end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in M  ))


# tot_N = int(input())
# tot_L = list(map(str,input.split()))
# tot_n = int(input())
# tot_l = list(map(str,input.split()))


# for ele in tot_l:
#     print(tot_L.count(ele))