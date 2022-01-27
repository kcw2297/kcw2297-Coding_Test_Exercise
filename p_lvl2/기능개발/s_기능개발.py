



"""
인덱스를 활용하였지만 이번에는 pop()을 활용해서 하나씩 처리하는 모습이 인상적이다
time과 count를 활용해 특정 조건에 리스트에서 값을 pop시킬지 결정한다
"""



def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0

    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
