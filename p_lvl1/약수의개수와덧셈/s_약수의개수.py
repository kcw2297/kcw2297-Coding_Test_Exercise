

"""
약수를 구하는 문제에서 루트를 사용하여 구한다
약수가 홀수이면 int(루트)!=루트 인것을 활용한 예시이다
"""




def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
