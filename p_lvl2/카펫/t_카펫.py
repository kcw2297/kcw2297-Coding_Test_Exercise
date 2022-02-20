"""https://programmers.co.kr/learn/courses/30/lessons/42842"""



"""
전체 타일에서 약수를 찾은 후에 가로와 세로의 길이가 가장 근접한 약수를
반환하였지만 3개의 테스트에서 에러가 나왔다. 문제에서 노란색의 격자의
수가 더 많은 이유가 있었는데 문제가 이해가 안갔다
"""




def solution(brown, yellow):

    total = brown + yellow
    return carpet(total)

def carpet(n):
    answer = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            answer.append(i)
            if ( (i**2) != n) :
                answer.append(n // i)
            elif ( (i**2) == n) :
                return [i, i]

    answer.sort()
    idx = len(answer)//2


    return [answer[idx],answer[idx-1]]
