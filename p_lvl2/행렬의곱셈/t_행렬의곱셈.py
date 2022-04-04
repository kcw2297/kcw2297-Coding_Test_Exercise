"""https://programmers.co.kr/learn/courses/30/lessons/12949"""



"""
사용한 논리 오류:
행과 열의 배열의 수가 다름에도 같다고 가정해서 풀었다


[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	

[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	

[[22, 22, 11], [36, 28, 18], [29, 20, 14]]
"""


def solution(arr1, arr2):
    total = []

    for row in arr1: # 행의 배열 개수
        for idx1 in range(len(row)): # 행의 배열 안 원소의 개수
            temp1 = 0
            temp2 = []
            for idx2 in range(len(row)): # 행의 배열 안 원소의 개수
                temp1 += row[idx2] * arr2[idx2][idx1]
            temp2.append(temp1)
        total.append(temp2)
    return total


# def solution(arr1, arr2):

#     total = []

#     for row in arr1:
#         temp = []
#         for idx in range(len(row)):
#             for col in arr2:
#                 for ele in row:
#                     temp.append(ele * col[idx])

#             sum_list = sum(temp)
#         total.append(sum_list)
#     return total






