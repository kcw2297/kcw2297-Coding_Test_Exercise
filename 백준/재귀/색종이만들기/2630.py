import sys
N = int(sys.stdin.readline())
paper = [ list(map(int, sys.stdin.readline().split())) for _ in range(N)]


result = []


def solution(x,y,N):
    color = paper[x-N][y-N]
    for i in range(x-N,x):
        for j in range(y-N,y):
            if color != paper[i][j]:
                solution(x,y,N//2)
                solution(x,y-N//2,N//2)
                solution(x-N//2,y,N//2)
                solution(x-N//2,y-N//2,N//2)
                return 
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(N,N,N)
print(result.count(0))
print(result.count(1))













# import sys

# length = int(sys.stdin.readline())

# """
# 4사분면으로 나누어 계산을 하려하였지만
# 각 행과 열을 나누는 부분을 고려하지 못하였다
# """

# paper_list = []
# for _ in range(length):
#     paper_list.append(list(map(int, sys.stdin.readline().split())))

# white=0
# blue=0

# def paperCut(arr,n):
#     global white, blue

#     def check(arr,n):
#         global white, blue
#         if n == arr.count(0):
#             white += 1
#             return 1
#         if n == arr.count(1):
#             blue += 1
#             return 1
#         return 0

#     if n == 1:
#         return


#     #1사분면
#     temp = []
#     for i in range(n//4,n//4):
#         for j in range(n//4,n//4):
#             temp.append(paper_list[i][j])
#     if not check(temp,n//2):
#         return paperCut(arr,n//2,n//2)

#     #2사분면
#     temp = []
#     for i in range(n//2,n//4):
#         for j in range(n//2,n//4):
#             temp.append(paper_list[i][j])
#     check(temp,n//2)

#     #3사분면
#     temp = []
#     for i in range(n//4,n//2):
#         for j in range(n//4,n//2):
#             temp.append(paper_list[i][j])
#     check(temp,n//2)

#     #4사분면
#     temp = []
#     for i in range(n//2,n//2):
#         for j in range(n//2,n//2):
#             temp.append(paper_list[i][j])
#     check(temp,n//2)

#     return paperCut(arr,n//2)




