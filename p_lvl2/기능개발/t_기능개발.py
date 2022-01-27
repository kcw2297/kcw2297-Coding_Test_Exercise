"""https://programmers.co.kr/learn/courses/30/lessons/42586"""



"""
index를 활용해서 리스트 안에 값을 더하고, 일정 조건에 해당되는 것은 del로 삭제하였다.
하지만 index range error가 나오면서 실패한 코드이
"""

"""
for loop인 경우에 문제가 삭제나 추가시에 index관리가 어려워진다
이번 문제처럼 특정 조건에 해당되면 리스트에서 요소를 삭제해야할 경우에는
for loop보다는 pop()와 while를 반복한다
"""


def solution(progresses, speeds):
    del_index = []
    answer = []
    count = 0

    while len(progresses)>0:
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
            if progresses[i] >100:
                count +=1
                del_index.append(i)

        if len(del_index)>0:
            for i in del_index:
                del progresses[i]
                del speeds[i]

        del_index=[]
        answer.append(count)
        count=0
    return answer
