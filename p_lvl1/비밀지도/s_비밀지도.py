



"""
zip(), bin(), rjust(), replace()를 이용하여 간결하고 효율적인
코드를 작성한
"""

"""
replace를 이용하여 원하는 값을 변경하도록하자(각 함수들의 용도를
최대한 활용해서 코드의 가독성을 높이자)
rjust는 비트연산자 함수로 빈 공간을 0으로 채운다
"""



def solution(n,arr1,arr2):
    answer = []

    for i,j in zip(arr1,arr2):
        state = str(bin(i|j)[2:])
        state=state.rjust(n,"0")
        state=state.replace("1","#")
        state=state.replace("0"," ")
        answer.append(state)
    return answer
