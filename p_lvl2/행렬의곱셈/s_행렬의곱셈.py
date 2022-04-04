










"""
사용한 논리:
총 3개의 반복문을 사용하여 전체 값을 반복하였다
1. 행의 배열 반복
2. 열의 원소 반복
3. 열의 배열 반복

"""



def solution(arr1, arr2):
    answer = []
    
    for row in range(len(arr1)): #행의 배열 개수
        temp_lst = []
        for col_ele in range(len(arr2[0])): #열의 원소 개수
            temp = 0
            for col in range(len(arr2)): #열의 배열 개수
                temp += arr1[row][col] * arr2[col][col_ele]
            temp_lst.append(temp)
        answer.append(temp_lst) 
        
    return answer


"""
사용한 논리:
zip(*arr2)를 활용하여 배열의 idx끼리 묶어서 사용한다
"""

def productMatrix(arr1, arr2):
    return [[sum(a*b for a, b in zip(arr1_row,arr2_col)) for arr2_col in zip(*arr2)] for arr1_row in arr1]