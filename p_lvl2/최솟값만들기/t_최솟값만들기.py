"""https://programmers.co.kr/learn/courses/30/lessons/12941"""


"""
항상 모든 요소를 전부 고려해야지 하면서 loop를 떠오리는데,
문제의 핵심과 해결책을 찾는 습관을 들이자
예를들어, 보기에 주어진 해답지에서 통찰을 할 수 있거나 보기 조건에
정답이 들어있는 경우가 있다
"""

"""
전체를 loop으로 돌려 저장하려했지만, 이는 동일한 값을 2번 사용하는
경우가 있어서 실패하였다
"""

def solution(a,b):

    temp = []
    for n in range(len(a)):
        temp.append(0)


    for i in range(len(a)):
        fir = a[i]
        for j in range(len(b)):
            sec = b[j]
            temp[j] = temp[j]+fir*sec

    return min(temp)
